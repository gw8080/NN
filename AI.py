import torch
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
while(True):
    user_input = input("USER:")
    cancel = 0
    while(True):
        Str = ""
        i = 0
        processB = word_tokenize(user_input)
        for wordB in processB:
            if wn.synsets(wordB):
                scan2 = wn.synsets(wordB)[0]
                data = list(set([w for s in scan2.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
                for line in data:
                    syn_arr2 = wn.synsets(line)
                    scan3 = syn_arr2[0].definition()
                    process = word_tokenize("".join(scan3))
                    for word in process:
                        inputs = tokenizer.encode(scan3, return_tensors='pt')
                        outputs = model.generate(
                        inputs, max_length=50, do_sample=True, temperature=5.0
                        )
                        words = tokenizer.decode(outputs[0], skip_special_tokens=True)
                        if words.find(word) != -1:
                            i+=1
                            if i > len(inputs)/1.5:
                               Str = tokenizer.decode(outputs[0], skip_special_tokens=True)
                               break
                    if i > len(inputs)/1.5:
                        cancel = 1
                        break
            if cancel == 1:
                break
        if cancel == 1:
            break
    print(Str)
    