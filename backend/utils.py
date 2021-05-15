import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def saveFileToServer(file):
  with open('text.txt', 'wb+') as destination:
    for chunk in file.chunks():  
      destination.write(chunk)

def cleanFileContent():
  f = open('text.txt', "r")
  text = f.read()
  text= text[45:]

  preprocess_text = text.strip().split("\n\n")
  print(preprocess_text)
  array = []
  for line in preprocess_text:
    split_text = line.split(":")
    array.extend(split_text)

  final_array = []
  for i in range(len(array)):
    if ((i+1) % 3 == 0):
      stripped_text = array[i].strip()
      final_array.append(stripped_text)
  
  preprocess_text = ''.join(final_array)
  t5_prepared_Text = "summarize: "+preprocess_text
  return t5_prepared_Text

def tokenizeAndSummarize(text):
  model = T5ForConditionalGeneration.from_pretrained('t5-small')
  tokenizer = T5Tokenizer.from_pretrained('t5-small')
  device = torch.device('cpu')

  tokenized_text = tokenizer.encode(text, return_tensors="pt").to(device)
  # summmarize
  summary_ids = model.generate(tokenized_text,
                                num_beams=4,
                                no_repeat_ngram_size=2,
                                min_length=30,
                                max_length=100,
                                early_stopping=True)

  output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
  return output