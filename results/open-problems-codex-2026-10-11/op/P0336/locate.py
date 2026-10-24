from pathlib import Path
s=Path('source_text.txt').read_text(encoding='utf8')
for term in ['Problem 4','Problem','rectangles','squares','[2, 3]','[2,3]','7. Open']:
 start=0
 for k in range(12):
  p=s.find(term,start)
  if p<0: break
  print('TERM',term,'OFFSET',p,'\n',s[max(0,p-300):p+2300]); start=p+len(term)
