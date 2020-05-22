import prepper as pr
abc_list = list("abcdefghijklmnopqrstuvwxyz")

def encode_prepped_caesar(text, shift_factor):
  text_list = list(text)
  num = 0
  for i in range(0,len(text_list)):
    if text_list[i] in pr.accept_list:
      continue
    num = abc_list.index(text_list[i]) + shift_factor
    while num >= len(abc_list):
      num-=len(abc_list)
    while num < 0:
      num+=len(abc_list)
    text_list[i] = abc_list[num]
  return text_list
