"""Record source-text integrity and the exact PDF pages of relevant statements."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
QUERIES={
 'bou_rabee_peres_2026':['1.4.2. Partially oriented','Problem 3 ('],
 'gpln_2008b':['2.2     Simple random walk','Theorem 1 Assume','Lemma 1','3. Rotations:'],
 'bremont_planar_2016':['Theorem 1.2','Corollary 1.3','Proposition 1.5','7.3    Proof of Proposition 1.5'],
 'bremont_2017':['Theorem 2.4.','Proposition 7.1.'],
 'bremont_2021_author':['Theorem 3.2.','Proposition 3.3.','3.2      Proof of Proposition 3.3'],
 'campanino_petritis_2003':['Theorem 1.6','Theorem 1.7','Theorem 1.8'],
 'gpln_fkg':['Theorem 2.2'],
 'gpln_2008a':['Theorem 2 :'],
 'pene_2009':['Theorem 1.','Theorem 2.'],
 'devulder_pene_2013':['Theorem 1.'],
 'castell_et_al_2011':['Theorem 20.'],
 'campanino_petritis_2014':['Theorem 1.5.'],
}
rows=[]
for path in sorted((ROOT/'sources').glob('*.txt')):
 b=path.read_bytes();s=b.decode();pages=s.split('\f')
 rows.append(dict(file=str(path.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
  pdf_page_count=s.count('\f') or None,
  statement_locations={q:[i+1 for i,p in enumerate(pages) if q in p] for q in QUERIES.get(path.stem,[])}))
report=(ROOT/'REPORT.md').read_text()
assert report.splitlines()[0]=='RESOLVED_IN_LITERATURE'
for row in rows:
 for q,loc in row['statement_locations'].items():
  assert loc,(row['file'],q)
for path in (ROOT/'sources').iterdir():assert path.suffix=='.txt',path
for path in ROOT.rglob('*'):
 if path.is_file(): assert path.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.tiff','.tif','.webp','.gif'},path
out={'audit_date':'2026-11-13','note':'PDF-page indices are 1-based in the saved extraction; journal pages are separately identified in REPORT.md. Repeated matches may be later citations. No probability simulation was run.','sources':rows}
(ROOT/'data'/'source_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(rows)} text sources; all statement locations found; no retained PDF/image files.')
