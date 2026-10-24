import urllib.request,urllib.parse,json
from pathlib import Path
u='https://api.openalex.org/works?filter=locations.source.id:s4306400194&search='+urllib.parse.quote('Three puzzles on mathematics computation games')+'&per_page=5'
# Perform a direct arXiv-id lookup to identify the source before a cited-by query.
u='https://api.openalex.org/works?filter=locations.landing_page_url:'+urllib.parse.quote('http://arxiv.org/abs/1801.02602',safe='')+'&per-page=5'
try:
 data=urllib.request.urlopen(u,timeout=30).read();Path('openalex_identify.response').write_bytes(data);j=json.loads(data);print([(x['id'],x['title']) for x in j.get('results',[])])
 for x in j.get('results',[]):
  url='https://api.openalex.org/works?filter=cites:'+x['id'].split('/')[-1]+'&per-page=100'
  try:Path('openalex_citing.response').write_bytes(urllib.request.urlopen(url,timeout=30).read());status='OK'
  except Exception as e:status=str(e)
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- OpenAlex citing-source query 2026-10-12: '+url+'; '+status+'\n')
 status='OK'
except Exception as e:status=str(e)
with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- OpenAlex source lookup 2026-10-12: '+u+'; '+status+'\n')
print(status)
# Keep only matching prior attempts, without printing entire ledger lines.
base=Path('~/<private-repo>/06_math_research')
rows=[]
for d in base.glob('probability_1000_intake_*'):
 p=d/'attempts.jsonl'
 if p.exists():
  for line in p.open(encoding='utf8'):
   if 'F0093' in line:
    try:
     o=json.loads(line)
     if o.get('problem_id')=='F0093':rows.append(o)
    except:pass
Path('prior_attempts.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Prior attempt count',len(rows))
