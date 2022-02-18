import torch
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
user_inputB = input("download or exec[download/exec]?:")
if user_inputB == "download":
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.save_pretrained("./cached-GPT2")
    tokenizer.save_pretrained("./cached_t-GPT2")
if user_inputB == "exec":
    model = GPT2LMHeadModel.from_pretrained('./cached-GPT2')
    tokenizer = GPT2Tokenizer.from_pretrained('./cached_t-GPT2')
while(True):
    user_input = input("USER:")
    inputs = tokenizer.encode(user_input, return_tensors='pt')
    outputs = model.generate(
    inputs, max_length=50, do_sample=True, temperature=5.0
    )
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))