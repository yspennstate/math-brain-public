"""Retrieve indexed phase-retrieval citation texts where an arXiv copy exists."""
import json
import re
from pathlib import Path
from fetch_sources import fetch

root=Path(__file__).resolve().parents[1]
existing='\n'.join(p.read_text()[:150] for p in (root/'sources').glob('*.txt'))
records=json.loads((root/'data'/'s2_citers.json').read_text())['data']
for record in records:
 p=record['citingPaper'];title=p['title'];ident=p.get('externalIds',{}).get('ArXiv')
 if not ident or not any(s in title.lower() for s in ['phase retriev','phaseless','pooling']):continue
 if ident in existing:continue
 name='citing_'+ident.replace('/','_')
 try:r=fetch(name,'https://arxiv.org/pdf/'+ident)
 except Exception as e:r={'name':name,'arxiv':ident,'title':title,'error':str(e)}
 with (root/'data'/'source_manifest.jsonl').open('a') as f:f.write(json.dumps(r)+'\n')
 print(json.dumps(r),flush=True)
