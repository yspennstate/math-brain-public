from pathlib import Path
s=Path('source.txt').read_text().splitlines()
for a,b in [(245,465),(690,860),(1520,1655),(3220,3375),(4900,5000)]:
 print('\nLINES',a,b);print('\n'.join(f'{i+1}: {s[i]}' for i in range(a-1,min(b,len(s)))))
