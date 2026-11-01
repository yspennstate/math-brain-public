import pathlib,xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
ids={'2609.27927','2609.30304','2609.26329','2610.08362','2609.29451','2610.09992','2608.06358'}
seen=set()
for f in ['arxiv_recent.txt','arxiv_recent2.txt','candidate_abstracts.txt','arxiv_universality_recent.txt']:
 for x in E.parse(f).findall('a:entry',ns):
  u=x.findtext('a:id',namespaces=ns);aid=u.split('/')[-1].split('v')[0]
  if aid in ids and u not in seen:
   seen.add(u);print(u,'; '.join(y.findtext('a:name',namespaces=ns) for y in x.findall('a:author',ns)),x.findtext('a:title',namespaces=ns).replace('\n',' '))
