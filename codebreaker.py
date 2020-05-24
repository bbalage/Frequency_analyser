import prepper as pr

def analyze_encoded_frequency(text, lang):
  freq_dict = dict()
  for c in lang.abc:
    freq_dict[c] = 0
  for c in text:
    if c in lang.abc:
      freq_dict[c]+=1
  ordered_abc_list = []
  for i in range(0,len(lang.abc)):
    freq_let = " "
    freq_num = -1
    for c in lang.abc:
      if freq_dict[c] > freq_num:
        freq_let = c
        freq_num = freq_dict[c]
    freq_dict[freq_let]=-1
    ordered_abc_list.append(freq_let)
  print("".join(ordered_abc_list))
  return ordered_abc_list

def break_caesar(enctext, language_name):
  lang = pr.fetch_language_by_name(language_name)
  ord_abc_list = analyze_encoded_frequency(enctext, lang)
  solutions = []
  for i in range(0,3):
    shift = lang.abc.index(ord_abc_list[0]) - lang.abc.index(lang.ordered_abc[i])
    templist = list(enctext)
    for j in range(0,len(enctext)):
      if templist[j] in lang.abc:
        newind = lang.abc.index(templist[j])-shift
        while newind >= len(lang.abc):
          newind-=len(lang.abc)
        while newind < 0:
          newind+=len(lang.abc)
        templist[j] = lang.abc[newind]
    solutions.append(templist)
  return solutions

def break_caesar_from_file(sourcename, language_name):
  source = open(sourcename,"r")
  sourcetext = source.read()
  source.close()
  return break_caesar(sourcetext, language_name)
