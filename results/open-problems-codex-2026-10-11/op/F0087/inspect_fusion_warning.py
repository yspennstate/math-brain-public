from pathlib import Path
l=Path('dubedat.txt').read_text(encoding='utf8').splitlines()
for i,t in enumerate(l):
 if 'pairing of insertions' in t:
  print('\n'.join(l[i:i+24]))
