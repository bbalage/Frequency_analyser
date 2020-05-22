swap_dict = {"á":"a","é":"e","í":"i","ó":"o","ö":"o","ő":"o","ú":"u","ü":"u","ű":"u"}
accept_list = [" ","\n"]

def prep(sourcetext):
  text = sourcetext.lower()
  i = 0
  textlist = list(text)
  newtext_list = []
  for c in textlist:
    if c in swap_dict:
      textlist[i]=swap_dict[c]
    if c.isalpha() or c in accept_list:
      newtext_list.append(textlist[i])
    i+=1
  return newtext_list

def prep_from_file(sourcename):
  source = open(sourcename, "r")
  text = source.read()
  return prep(text)
