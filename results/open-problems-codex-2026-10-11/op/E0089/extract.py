from pathlib import Path
s=Path('source.txt').read_text(encoding='utf8')
a=s.index('--- PDF PAGE 7 ---');b=s.index('--- PDF PAGE 9 ---')
print(s[a:b])
