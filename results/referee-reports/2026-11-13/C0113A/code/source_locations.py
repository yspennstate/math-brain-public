from pathlib import Path
import re,sys
p=Path(sys.argv[1]); text=p.read_text()
for pat in sys.argv[2:]:
 print('\nPATTERN:',pat)
 for m in list(re.finditer(pat,text,re.I))[:5]:
  a=text.rfind('=== PDF PAGE',0,m.start()); b=text.find('\n\n',a)
  print(text[a:b],repr(text[max(b,m.start()-100):m.start()+450]))
