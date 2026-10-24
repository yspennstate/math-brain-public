from pathlib import Path
s=Path('source.txt').read_text().splitlines()
for a,b in [(1,45),(470,690),(960,1138),(1350,1550)]:
 print('\nLINES',a,b)
 print('\n'.join(f'{i+1}: {s[i]}' for i in range(a-1,min(b,len(s)))))
