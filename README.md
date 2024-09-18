# Retrieval-Interleaved Generation (RIG) Demo

This project demonstrates the Retrieval-Interleaved Generation (RIG) technique using either the DataGemma or Claude language model. It combines the power of large language models with real-time data retrieval from Data Commons to provide accurate and up-to-date responses to statistical queries.

## Features

- Utilizes either DataGemma (downloaded from HuggingFace for local inference) or Claude 3.5 Sonnet (via Anthropic's API) for generating statistical sub-queries
- By default, uses a 2-bit quantized version of DataGemma 27b for local inference
- Integrates with Data Commons API for retrieving statistical data
- Implements RIG technique to enhance response accuracy with factual information
- Requires only one LLM (either DataGemma or Claude) at a time for generating statistical sub-queries

## Installation

### Prerequisites

- Python 3.12 or higher
- Git

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/ag-chirag/retrieval-interleaved-generation.git
   cd retrieval-interleaved-generation
   ```

2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   - For macOS with Metal support:
     ```
     CMAKE_ARGS="-DGGML_METAL=on" pip install -r requirements.txt
     ```
   - For other systems:
     ```
     pip install -r requirements.txt
     ```

4. Set up environment variables:
   Create a `.env` file in the project root and add your API keys. 
   ```
   DC_API_KEY=your_data_commons_api_key # Only needed if you want to execute queries on Data Commons.
   ANTHROPIC_API_KEY=your_anthropic_api_key # Only needed if you want to use Claude.
   ```

## Usage

To run the demo:

1. Ensure you have set up the environment variables as described in the Installation section.

2. Run the main script with optional arguments:
   ```
   python run.py [--pretty-response] [--execute-queries] [--model {data-gemma,claude}]
   ```
   - `--pretty-response`: Enable pretty response formatting
   - `--execute-queries`: Execute queries against Data Commons
   - `--model`: Choose the model to use (default is 'data-gemma')

3. The script will prompt you to enter a query. Type your statistical question and press Enter.

4. The program will then:
   - Generate statistical questions based on your query using the selected model (DataGemma or Claude).
   - If `--execute-queries` is enabled, it will retrieve relevant data from Data Commons API.
   - Provide a response that incorporates the retrieved data (if applicable).

5. After each response, you'll be prompted to enter another query or type 'exit' to end the program.

Example usage:

```
python run.py --execute-queries --pretty-response 

╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Welcome ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Welcome to the Retrieval Interleaved Generation (RIG) Demo!                                                                                                                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Your question: Has the use of renewables increased in the world?
Calling DataGemma with 'has the use of renewables increased in the world?'

llama_print_timings:        load time =    1894.64 ms
llama_print_timings:      sample time =       4.18 ms /    43 runs   (    0.10 ms per token, 10277.25 tokens per second)
llama_print_timings: prompt eval time =    1894.58 ms /    11 tokens (  172.23 ms per token,     5.81 tokens per second)
llama_print_timings:        eval time =   10258.07 ms /    42 runs   (  244.24 ms per token,     4.09 tokens per second)
llama_print_timings:       total time =   12196.58 ms /    53 tokens
╭──────────────────────── Data Gemma Response ─────────────────────────╮
│ [                                                                    │
│   "What is the carbon emission in world?",                           │
│   "How has carbon emission changed over time in world?",             │
│   "What is the renewable energy consumption in world?",              │
│   "How has renewable energy consumption changed over time in world?" │
│ ]                                                                    │
╰──────────────────────────────────────────────────────────────────────╯
... calling DC with "What is the carbon emission in world?"
... calling DC with "How has carbon emission changed over time in world?"
... calling DC with "What is the renewable energy consumption in world?"
... calling DC with "How has renewable energy consumption changed over time in world?"
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Data Commons Response ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │
│ ┃                                                                                                                                 Data Commons Response                                                                                                                                 ┃ │
│ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ │
│                                                                                                                                                                                                                                                                                           │
│ What is the carbon emission in world?                                                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                           │
│ According to datacatalog.worldbank.org, "CO2 Emissions Per Capita in the World" was 4.2923 t in 2020.                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                           │
│ How has carbon emission changed over time in world?                                                                                                                                                                                                                                       │
│                                                                                                                                                                                                                                                                                           │
│ According to datacatalog.worldbank.org, "CO2 Emissions Per Capita in the World" was 4.2923 t in 2020.                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                           │
│ What is the renewable energy consumption in world?                                                                                                                                                                                                                                        │
│                                                                                                                                                                                                                                                                                           │
│ According to Global SDG Database, "Renewable Energy Share in the Total Final Energy Consumption in the World" was 18.71 Percentage in 2021.                                                                                                                                               │
│                                                                                                                                                                                                                                                                                           │
│ How has renewable energy consumption changed over time in world?                                                                                                                                                                                                                          │
│                                                                                                                                                                                                                                                                                           │
│ According to Global SDG Database, "Renewable Energy Share in the Total Final Energy Consumption in the World" was 18.71 Percentage in 2021.                                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Project Structure

- `model.py`: Contains the `DataGemma` and `Claude` classes for interacting with the language models
- `prompts.py`: Defines the prompts used for generating statistical questions
- `data_commons.py`: Handles interactions with the Data Commons API
- `requirements.txt`: Lists all the Python dependencies required for the project

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgements

- [Data Commons](https://datacommons.org/) for providing the statistical data API
- [Hugging Face](https://huggingface.co/) for downloading the DataGemma model
- [Anthropic](https://www.anthropic.com/) for the Claude API