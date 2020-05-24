#swap_dict = {"á":"a","é":"e","í":"i","ó":"o","ö":"o","ő":"o","ú":"u","ü":"u","ű":"u"}
accept_list = [" ","\n"]
class UnknownLanguageException(Exception):
  pass
class Language:
  def __init__(self, name, abc):
    self.name = name
    self.abc = list(abc)
    self.ordered_abc = None
    self.frequency = dict()
    for c in abc:
      self.frequency[c] = 0

  def __str__(self):
    abc_list = []
    if self.ordered_abc != None:
      abc_list = self.ordered_abc
    retstring = self.name + "\n" + "".join(self.abc) + "\n" + "".join(abc_list)
    del(abc_list)
    return retstring

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
    self.ordered_abc = abc
    del(self.frequency)
    
language_list = []

def fetch_language_by_name(language_name):
  for lan in language_list:
    if lan.name == language_name:
      return lan
  raise UnknownLanguageException()

def prep(sourcetext, language_name):
  lang = fetch_language_by_name(language_name)
  text = sourcetext.lower()
  i = 0
  text_list = list(text)
  newtext_list = []
  for c in text_list:
    if c in lang.abc or c in accept_list:
      newtext_list.append(text_list[i])
    i+=1
  return newtext_list

def prep_from_file(sourcename, language_name):
  source = open(sourcename, "r")
  text = source.read()
  return prep(text, language_name)

def init_from_default_languages():
  language_list.clear()
  language_list.append(Language("hun","aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"))
  language_list.append(Language("eng","abcdefghijklmnopqrstuvwxyz"))

def learn_from_source(sourcename, language_name):
  lang = fetch_language_by_name(language_name)
  source = open(sourcename, "r")
  source_text = source.read()
  for c in source_text:
    if c in lang.abc:
      lang.frequency[c] += 1
  lang.conclude_order()
