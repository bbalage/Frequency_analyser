def prep_from_file(sourcename):
  source = open(sourcename, "r")
  text = source.read()
  text = text.lower()
  hundict = {"á":"a","é":"e","í":"i","ó":"o","ö":"o","ő":"o","ú":"u","ü":"u","ű":"u"}
  hunlist = {"á", "é","í","ó","ö","ő","ú","ü","ű"}
  i = 0
  textlist = list(text)
  newtext = ""
  print(text)
  for c in textlist:
    if c in hunlist:
      textlist[i]=hundict[c]
    if c.isalpha() or c == " " or c == '\n':
      newtext+=textlist[i]
    i+=1
  return newtext
