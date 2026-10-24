"""Bounded reads: one named public preprint and exact target cards, no mutations of stores."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sqlite3
import urllib.request

root=Path(__file__).resolve().parent
sources=root/'sources'
sources.mkdir(exist_ok=True)
url='https://raw.githubusercontent.com/openai/math/main/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf'
result={'url':url}
try:
    with urllib.request.urlopen(url,timeout=30) as response:
        data=response.read(4*1024*1024+1)
    if len(data)>4*1024*1024 or not data.startswith(b'%PDF'):
        raise ValueError('Unexpected or oversized preprint response')
    dest=sources/'directional_zero_one_2026_claim.pdf'
    dest.write_bytes(data)
    result.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),local_path=str(dest))
    if importlib.util.find_spec('pypdf'):
        from pypdf import PdfReader
        reader=PdfReader(dest)
        pages=[page.extract_text() or '' for page in reader.pages]
    elif importlib.util.find_spec('fitz'):
        import fitz
        with fitz.open(dest) as document:
            pages=[page.get_text() for page in document]
    else:
        raise RuntimeError('No installed PDF text reader; no installation attempted')
    result['pages']=len(pages)
    # Only the introduction/statement and lines identifying the possible proof bridge.
    first='\n'.join(f'PDF PAGE {i+1}\n{pages[i]}' for i in range(min(3,len(pages))))
    (sources/'directional_zero_one_first_pages.txt').write_text(first,encoding='utf-8')
    print(first[:12500])
    hits=[]
    for i,text in enumerate(pages):
        for j,line in enumerate(text.splitlines()):
            if any(term in line.lower() for term in ('stationary','invariant','absolute continuity','absolutely continuous','main lemma','coexistence','key lemma','uniformly integrable')):
                hits.append({'page':i+1,'line':j+1,'text':line[:400]})
    result['targeted_bridge_hits']=hits[:45]
except Exception as exc:
    result['error']=f'{type(exc).__name__}: {exc}'
(sources/'PUBLIC_CLAIM_READ.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PUBLIC_CLAIM_READ',json.dumps(result))

store_path=Path('~/math-brain-build/local/population/brain.sqlite3')
conn=sqlite3.connect(store_path.as_uri()+'?mode=ro',uri=True,timeout=10)
conn.execute('PRAGMA query_only=ON')
conn.set_progress_handler(lambda: 0,10000)
rows=conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE instr(id,'C0044')>0 OR instr(body,'C0044')>0 OR (lower(title) LIKE '%directional%' AND lower(title) LIKE '%zero%one%') LIMIT 12").fetchall()
conn.close()
records=[dict(zip(('id','kind','title','body','metadata_json'),row)) for row in rows]
(root/'STORE_TARGET_ROWS.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')
print('STORE_TARGET_SUMMARY',json.dumps([{'id':r['id'],'kind':r['kind'],'title':r['title'],'body':r['body'][:500]} for r in records],ensure_ascii=False))
