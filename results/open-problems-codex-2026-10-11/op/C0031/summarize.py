import pathlib,json,xml.etree.ElementTree as E
R=pathlib.Path(__file__).parent
for name in ['survey','original']:
 t=(R/(name+'.txt')).read_text(encoding='utf8')
 if name=='survey':
  for phrase in ['6. Heavy', 'Theorem 6.2', 'Remark 6.', 'Lemma 4.11', 'Lemma 4.18', '(6.1)']:
   start=0
   while True:
    pos=t.find(phrase,start)
    if pos<0:break
    print(name,phrase,t[max(0,pos-200):pos+3500],flush=True);start=pos+len(phrase)
 else:print('ORIGINAL FIRST',t[:17000],flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_broad.xml','arxiv_invertibility.xml']:
 if not (R/name).exists():continue
 for e in E.parse(R/name).findall('a:entry',ns):
  print(name,e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text[:2000],flush=True)
for name in ['cr_invertibility.json','cr_almostsure.json']:
 if (R/name).exists():
  for e in json.loads((R/name).read_text())['message']['items']:print(name,e.get('title'),e.get('DOI'),e.get('published'),flush=True)
if (R/'semantic_retry.json').exists():
 d=json.loads((R/'semantic_retry.json').read_text())
 for e in d.get('data',[]):
  p=e['citingPaper'];title=p.get('title','')
  if any(w in title.lower() for w in ['heavy','singular','invertib','circular','stable','levy','lévy']):print('SEMANTIC CITING',p,flush=True)
