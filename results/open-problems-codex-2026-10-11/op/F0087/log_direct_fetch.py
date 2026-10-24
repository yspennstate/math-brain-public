from pathlib import Path
import json
P=Path('.')
r={'date':'2026-10-11','service':'dubedat_pdf_direct_fetch','url':'https://arxiv.org/pdf/1110.2808','result':'HTTP 200; downloaded PDF, 95 pages; direct fetch made before search3; logged retrospectively'}
with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(r)+'\n')
with (P/'LITERATURE.md').open('a',encoding='utf8') as f:f.write(f"- {r['date']} — **{r['service']}**: `{r['url']}` — {r['result']}\n")
print('Direct PDF fetch also recorded.')
