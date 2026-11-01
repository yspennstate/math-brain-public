import pathlib,json,pymupdf
for name in ['markov_pdf','simple_pdf','budd']:
 d=pymupdf.open(name+'.pdf');print(name, '\n',d[0].get_text()[:1600])
j=json.loads(pathlib.Path('crossref.txt').read_text())
for x in j['message']['items']:
 if x.get('DOI')=='10.1007/978-3-031-36854-7': print({k:x.get(k) for k in ['title','author','publisher','volume','ISBN','published','container-title']})
s=pathlib.Path('ATTEMPT.md').read_text();print('unicode question chars',s.count('?'));print(s[:1300]);print('universal precedes auxiliary:',s.index('## Universal')<s.index('## Auxiliary'))
