import pymupdf,pathlib,json
P=pathlib.Path('.')
D=pymupdf.open('jsw_pdf.pdf');txt='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(D));(P/'jsw.txt').write_text(txt,encoding='utf8')
print(txt[:1700]);lines=txt.splitlines()
for i,l in enumerate(lines):
 if any(w in l.lower() for w in ['dimer','dubédat','dubedat','theorem 1.1','theorem 1.2','universality']):
  print('\n'.join(f'{j+1}: {lines[j]}' for j in range(max(0,i-3),min(len(lines),i+8))))
J=json.loads((P/'semantic_kenyon_citations.json').read_text());print('CITATIONS',J.keys())
for c in J['data']:
 w=c['citingPaper'];title=w['title']
 if any(s in title.lower() for s in ['chaos','electric','cauchy','torsion','boson','dimer','height','conformal']):print(json.dumps(w,ensure_ascii=False))
for fn in ['crossref_vertex.json','crossref_cr.json']:
 print('FILE',fn)
 for w in json.loads((P/fn).read_text())['message']['items']:print(w.get('title'),w.get('DOI'),w.get('published'),w.get('container-title'),w.get('page'))
