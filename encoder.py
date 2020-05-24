import prepper as pr

def encode_prepped_caesar(text, language_name, shift_factor):
  text_list = list(text)
  lang = pr.fetch_language_by_name(language_name)
  abc_list = lang.abc
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

def encode_caesar(text, language_name, shift_factor):
  text_list = pr.prep(text, language_name)
  return encode_prepped_caesar(text_list, language_name, shift_factor)

def encode_caesar_from_file(sourcename, language_name, shift_factor):
  text_list = pr.prep_from_file(sourcename, language_name)
  return encode_prepped_caesar(text_list, language_name, shift_factor)
