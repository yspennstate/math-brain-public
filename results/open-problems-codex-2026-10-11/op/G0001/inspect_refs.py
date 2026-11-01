from pathlib import Path
s=Path('cerf_source.txt').read_text()
for key in ['[62]','[84]','[63]']:
 i=s.rfind(key);print(s[i:i+2200])
print('new file?',Path('new_html_plain.txt').exists())
