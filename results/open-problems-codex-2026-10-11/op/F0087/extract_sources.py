import tarfile,pathlib,json
P=pathlib.Path('.')
with tarfile.open('dubedat_source.tar') as T:
 for m in T.getmembers():
  if m.isfile() and m.name.endswith(('.tex','.bib')):
   b=T.extractfile(m).read();(P/('dubedat_'+pathlib.PurePosixPath(m.name).name)).write_bytes(b);print(m.name,len(b))
for fn in ['crossref_chaos.json','crossref_kenyon.json']:
 print('FILE',fn)
 for w in json.loads((P/fn).read_text())['message']['items']:
  print(w.get('title'),w.get('DOI'),w.get('published'),w.get('author'),w.get('container-title'),w.get('page'))
