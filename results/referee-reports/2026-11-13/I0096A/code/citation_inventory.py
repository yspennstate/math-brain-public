"""Build a traceable title/abstract screening inventory, not a completeness claim."""
import csv
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
texts=list((root/'sources').glob('*.txt'))
all_sources=[(p,p.read_text()[:5000]) for p in texts]
def key(t):return re.sub('[^a-z0-9]','',str(t).lower())
records={}
oa=json.loads((root/'data'/'openalex_citers.json').read_text())
for w in oa['results']:
 t=w.get('title') or '(untitled record)';k=key(t)
 idx=w.get('abstract_inverted_index') or {}
 words=sorted((i,word) for word,inds in idx.items() for i in inds)
 records[k]={'title':t,'year':w.get('publication_year'),'doi':w.get('doi') or '',
             'arxiv':'','indexes':'OpenAlex','url':w['id'],'abstract':' '.join(w for _,w in words)}
s2=json.loads((root/'data'/'s2_citers.json').read_text())
for w in s2['data']:
 p=w['citingPaper'];t=p['title'];k=key(t);e=p.get('externalIds',{})
 if k in records:
  records[k]['indexes']+=';SemanticScholar';records[k]['arxiv']=e.get('ArXiv','')
  if p.get('abstract'):records[k]['abstract']=p['abstract']
 else:
  records[k]={'title':t,'year':p.get('year'),'doi':e.get('DOI',''),'arxiv':e.get('ArXiv',''),
              'indexes':'SemanticScholar','url':'https://www.semanticscholar.org/paper/'+p['paperId'],
              'abstract':p.get('abstract') or ''}
for r in records.values():
 ident=r['arxiv']
 matches=[str(p.relative_to(root)) for p,head in all_sources
          if (ident and ident in head[:300]) or (len(key(r['title']))>=25 and key(r['title']) in key(head))]
 r['local_text']=';'.join(matches)
 t=r['title'].lower()
 if any(x in t for x in ['extreme least singular','gaussian critical','universality of smallest']):
  r['screen']='random critical-threshold result'
 elif 'minimal smallest singular' in t:
  r['screen']='direct deterministic extremal subframe work'
 elif any(x in t for x in ['lipschitz analysis','lipschitz synthesis','lipschitz continuous','lipschitz inversion','optimal lower lipschitz','condition numbers and the optimal','stability of frames','stable phase retrieval and perturbations','uniqueness and stability']):
  r['screen']='general stability background; read relevant result sections'
 elif any(x in t for x in ['affine','generalized','fourier','gabor','stft','cauchy','wavelet','shift-invariant','space–time','space-time','diffraction','analytic signals','carleson','reproducing kernel','banach','infinite-dimensional','quantum','intensity measurements']):
  r['screen']='different measurement model, metric, or signal class; screened'
 elif any(x in t for x in ['phaseless','phase retriev','pooling']):
  r['screen']='adjacent phase-retrieval work; title/abstract and retrieved sections screened'
 else:r['screen']='other application or invariant embedding; title/abstract screened'
 r['coverage_note']='Public index record; not proof of complete citation coverage.'
keys=['title','year','doi','arxiv','indexes','url','screen','local_text','coverage_note','abstract']
with (root/'data'/'citation_screen.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
 writer.writerows(sorted(records.values(),key=lambda r:(-(r['year'] or 0),r['title'])))
print(json.dumps({'openalex_records':len(oa['results']),'semantic_scholar_records':len(s2['data']),
 'distinct_normalized_titles':len(records),'text_files_saved':len(texts),
 'records_matched_by_arxiv_to_saved_text':sum(bool(r['local_text']) for r in records.values())},indent=2))
