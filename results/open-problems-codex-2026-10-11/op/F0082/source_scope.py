from pathlib import Path
s=Path('source.txt').read_text(encoding='utf8');print(s[:11000])
s=Path('minimal.txt').read_text(encoding='utf8');i=s.find('Theorem 7 (Higher');print(s[i-150:i+900])
