from llama_cpp import Llama
from huggingface_hub import hf_hub_download
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import prompts


class DataGemma:
   def __init__(self, model_id: str = "bartowski/datagemma-rag-27b-it-GGUF", model_file: str =  "datagemma-rag-27b-it-Q2_K.gguf"):
      self.generation_kwargs = {
         "max_tokens": 4096, # Max number of new tokens to generate
      }
      self.model_path = hf_hub_download(model_id, model_file)
      self.llm = Llama(
            self.model_path
      )
      self.name = "DataGemma"
   
   def complete(self, question: str) -> str:
      llm_resp = self.llm(question, **self.generation_kwargs)

      return llm_resp["choices"][0]["text"]
   
   @staticmethod
   def parse_completion(completion: str) -> list[str]:
      return [line for line in completion.split('\n') if line.strip()]
   

class Claude:
   def __init__(self, model_id: str = "claude-3-5-sonnet-20240620"):
      self.llm = ChatAnthropic(model=model_id, max_tokens_to_sample=4000)
      self.standard_parser = StrOutputParser()
      self.name = "Claude Sonnet 3.5"
      
   def complete(self, question: str) -> str:
      prompt_template = PromptTemplate.from_template(prompts.RAG_IN_CONTEXT_PROMPT)
      chain =  prompt_template | self.llm | self.standard_parser
      return chain.invoke(question)
   @staticmethod
   def parse_completion(completion: str) -> list[str]:
      return [line for line in completion.split('\n') if line.strip()]