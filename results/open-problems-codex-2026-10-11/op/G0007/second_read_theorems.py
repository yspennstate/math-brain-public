from pathlib import Path
s=Path('second_broman.txt').read_text().splitlines()
for a,b in [(295,355),(1250,1310)]:print('\n'.join(s[a:b]))
s=Path('second_liggett_steif.txt').read_text().splitlines()
for a,b in [(85,105),(245,268)]:print('\n'.join(s[a:b]))
