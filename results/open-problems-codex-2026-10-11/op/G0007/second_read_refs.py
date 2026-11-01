from pathlib import Path
s=Path('second_broman.txt').read_text().splitlines();print('\n'.join(s[952:993]))
s=Path('second_liggett_steif.txt').read_text().splitlines();print('\n'.join(s[-140:]))
