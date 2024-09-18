from model import DataGemma, Claude
from data_commons import DataCommonsClient
import json
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
import asyncio
import logging
import argparse

console = Console()

async def get_user_input(prompt="Your question: "):
    style = Style.from_dict({
        'prompt': 'cyan bold',
    })
    session = PromptSession(style=style)
    return await session.prompt_async(prompt, multiline=False)

async def main(llm : DataGemma | Claude, pretty_response: bool, execute_queries: bool):
    console.print(Panel("Welcome to the Retrieval Interleaved Generation (RIG) Demo!", title="Welcome", style="bold green"))

    while True:
        user_input = await get_user_input()
        if user_input.lower() == 'exit':
            console.print(Panel("Thank you for chatting. Goodbye!", title_align="left", title="Goodbye", style="bold green"))
            break
        else:
            #QUERY = "What progress has Pakistan made against health goals?"
            console.print(f"Calling {llm.name} with '{user_input.lower()}'", style="green")
            completion = llm.complete(user_input.lower())
            questions = llm.parse_completion(completion)

            if pretty_response:
                console.print(Panel(
                    Syntax(json.dumps(questions, indent=2), "json", theme="monokai"),
                    title="Data Gemma Response",
                    expand=False
                ))
            else:
                console.print(Panel(
                    Syntax(completion, "text"),
                title="Data Gemma Raw Response",
                expand=False
            ))                

            if execute_queries: 
                dc = DataCommonsClient()

                q2resp = dc.call_dc(questions)
                filtered_q2resp = {}
                for k, v in q2resp.items():
                    if v and v.val != '':
                        filtered_q2resp[k] = v
                    else:
                        console.print(f"Did not find any answer to question '{k}' in Data Commons. Skipping.", style="yellow")
                q2resp = filtered_q2resp

                if not pretty_response:
                    console.print(Panel(
                        Syntax(json.dumps(q2resp, default=lambda o: o.__dict__, indent=2), "json", theme="monokai"),
                    title="Data Commons Raw Response",
                    expand=False
                ))
                else:
                    markdown_output = dc.pretty_print(q2resp)
                    console.print(Panel(
                        Markdown(markdown_output),
                        title="Data Commons Response",
                        expand=False
                    ))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieval Interleaved Generation Demo")
    parser.add_argument("--pretty-response", action="store_true", help="Enable pretty response formatting")
    parser.add_argument("--execute-queries", action="store_true", help="Execute queries against Data Commons")
    parser.add_argument("--model", choices=['data-gemma', 'claude'], default='data-gemma', help="Choose the model to use")
    args = parser.parse_args()
    pretty_response = args.pretty_response
    execute_queries = args.execute_queries
    model = args.model

    if model == 'data-gemma':
        llm = DataGemma()
    elif model == 'claude':
        llm = Claude()

    try:
        asyncio.run(main(llm, pretty_response, execute_queries))
    except KeyboardInterrupt:
        console.print("\nProgram interrupted by user. Exiting...", style="bold red")
    except Exception as e:
        console.print(f"An unexpected error occurred: {str(e)}", style="bold red")
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
    finally:
        console.print("Goodbye!", style="bold green")