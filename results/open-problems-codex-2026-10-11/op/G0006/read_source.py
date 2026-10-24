from pathlib import Path
s=Path('source_text.txt').read_text(encoding='utf8')
print(s[:13500]); print(s[s.find('References'):])
