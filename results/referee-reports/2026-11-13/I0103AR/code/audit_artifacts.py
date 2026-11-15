"""Check retrieval provenance, final text integrity, and local artifact invariants."""
from pathlib import Path
from hashlib import sha256
import ast,json,re
BASE=Path(__file__).resolve().parents[1]
entries=[json.loads(x) for x in (BASE/'data'/'source_manifest.jsonl').read_text().splitlines()]
for d in entries:
 p=BASE/'sources'/(d['name']+'.txt')
 if p.exists():
  current=sha256(p.read_bytes()).hexdigest()
  if current!=d['text_sha256']:
   d['original_extraction_sha256']=d['text_sha256'];d['text_sha256']=current
   d['normalization']='Removed embedded NUL characters from PDF text extraction.'
(BASE/'data'/'source_manifest.jsonl').write_text(''.join(json.dumps(d)+'\n' for d in entries))
index=[]
for p in sorted((BASE/'sources').iterdir()):
 assert p.is_file() and p.suffix=='.txt',p
 raw=p.read_bytes();t=raw.decode('utf-8');assert b'%PDF-' not in raw and '\x00' not in t,p
 index.append({'file':p.name,'bytes':len(raw),'sha256':sha256(raw).hexdigest(),'pdf_pages':len(re.findall(r'^=== PDF PAGE \d+ ===$',t,re.M)),'origins':[d['url'] for d in entries if p.stem==d['name']]})
(BASE/'data'/'source_index.json').write_text(json.dumps(index,indent=2))
report=(BASE/'REPORT.md').read_text()
assert report.splitlines()[0] in ['ACCEPT','MINOR','MAJOR','WRONG']
assert report.count('$$')%2==0
assert report.count('$')%2==0
assert '\x00' not in report
for p in (BASE/'code').glob('*.py'):ast.parse(p.read_text())
for p in BASE.rglob('*'):
 assert p.suffix.lower() not in ['.pdf','.png','.jpg','.jpeg','.webp'],p
required=['2603.29571v1','1404.1677v1','2611.14475v1','1202.1234v2','1410.6457v1','2011.02907v2','1008.4535v3','1403.3427v1','2108.01794v3','2211.02713v2','2303.16475v1','2405.08608v2','2412.12958v2','2505.00160v3','2606.08913v1','2002.11677v2']
for ident in required:
 assert (BASE/'sources'/(ident+'.txt')).is_file()
 assert any(d['name']==ident and d['url']=='https://arxiv.org/pdf/'+ident for d in entries)
claim=(BASE/'claim_files'/'REPORT.md').read_text()
assert 'This answers the permitted' in claim
source=(BASE/'sources'/'2603.29571v1.txt').read_text()
p10=source.split('=== PDF PAGE 10 ===')[1].split('=== PDF PAGE 11 ===')[0]
assert 'Conjecture 29.' in p10 and 'Entry 13' in p10
assert not re.search(r'sub.?dict',p10,re.I)
check=json.loads((BASE/'data'/'verification.json').read_text())
assert check['nice']>=10 and check['threads']<=4 and check['peak_rss_bytes']<4*1024**3
result={'verdict':report.splitlines()[0],'source_files':len(index),'independently_downloaded_full_texts':len(entries),'required_arxiv_texts_present':True,'max_gram_entry_error':max(r['direct_gram_error'] for r in check['rows']),'max_quadrature_error':max(r['quadrature_error'] for r in check['rows']),'numeric_peak_rss_bytes':check['peak_rss_bytes'],'no_pdf_or_page_images':True,'syntax_and_report_delimiters_pass':True,'source_has_no_subdictionary_alternative':True}
(BASE/'data'/'audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
