from pathlib import Path
from bs4 import BeautifulSoup
base = Path(__file__).resolve().parent
soup = BeautifulSoup((base/'fresh_source.html').read_text(encoding='utf8'), 'html.parser')
out = []
for sid in ['S2.SS2', 'S2.SS3', 'S2.SS4', 'S9', 'S11.SS5']:
    s = soup.find(id=sid)
    if s:
        text = s.get_text(' ', strip=True)
        out.append(sid+'\n'+text)
        print(sid, text, flush=True)
(base/'fresh_source_excerpts.txt').write_text('\n\n'.join(out), encoding='utf8')
