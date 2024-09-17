import torch
import os
import data_gemma as dg

from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from dotenv import load_dotenv

load_dotenv()

# Initialize Data Commons API client
DC_API_KEY = os.getenv('DC_API_KEY')
dc = dg.DataCommons(api_key=DC_API_KEY)


# Get finetuned Gemma2 model from HuggingFace
HF_TOKEN = os.getenv('HF_TOKEN')

nf4_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_compute_dtype=torch.bfloat16
)

model_name = 'google/datagemma-rig-27b-it'
tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
datagemma_model = AutoModelForCausalLM.from_pretrained(model_name,
                                             device_map="auto",
                                             quantization_config=nf4_config,
                                             torch_dtype=torch.bfloat16,
                                             token=HF_TOKEN)

# Build the LLM Model stub to use in RIG flow
datagemma_model_wrapper = dg.HFBasic(datagemma_model, tokenizer)