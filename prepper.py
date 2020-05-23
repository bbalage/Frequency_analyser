swap_dict = {"á":"a","é":"e","í":"i","ó":"o","ö":"o","ő":"o","ú":"u","ü":"u","ű":"u"}
accept_list = [" ","\n"]
class UnknownLanguageException(Exception):
  pass
class Language:
  def __init__(self, name, abc):
    self.name = name
    self.abc = list(abc)
    self.frequency = dict()
    for c in abc:
      self.frequency[c] = 0

  def conclude_order(self):
    abc = []
    for i in range(0,len(self.abc)):
      freq = -1
      freqlet = " "
      for c in self.abc:
        if self.frequency[c]>freq:
          freq = self.frequency[c]
          freqlet = c
      abc.append(freqlet)
      self.frequency[freqlet] = -1
    self.abc = abc
    del(self.frequency)
    
language_list = []

def prep(sourcetext):
  text = sourcetext.lower()
  i = 0
  text_list = list(text)
  newtext_list = []
  for c in text_list:
    if c in swap_dict:
      text_list[i]=swap_dict[c]
    if c.isalpha() or c in accept_list:
      newtext_list.append(text_list[i])
    i+=1
  return newtext_list

def prep_from_file(sourcename):
  source = open(sourcename, "r")
  text = source.read()
  return prep(text)

def init_from_default_languages():
  language_list.clear()
  language_list.append(Language("hun","aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"))
  language_list.append(Language("eng","abcdefghijklmnopqrstuvwxyz"))

def learn_from_source(sourcename, language):
  lang = None
  for lan in language_list:
    if lan.name == language:
      lang = lan
      break
  if lang == None:
    raise UnknownLanguageException()
  source = open(sourcename, "r")
  source_text = source.read()
  for c in source_text:
    if c in lang.abc:
      lang.frequency[c] += 1
  lang.conclude_order()
