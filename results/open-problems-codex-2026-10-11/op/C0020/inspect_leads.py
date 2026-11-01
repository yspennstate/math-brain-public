from pathlib import Path
for name in ['2606.32024','2609.15388','2408.08457']:
 s=Path(name+'.txt').read_text(encoding='utf8'); print('\nFILE',name);print(s[:4500])
 for term in ['algorithmic complexity','computational complexity','decision tree','7/4','3/2','percolation crossings']:
  start=0;hits=0
  while (i:=s.lower().find(term,start))>=0 and hits<4:
   print('TERM',term,s[max(0,i-250):i+1000]);start=i+len(term);hits+=1
s=Path('2408.12995.txt').read_text(encoding='utf8');print(s[s.find('=== PAGE 24'):s.find('=== PAGE 28')])
