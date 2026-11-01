import pathlib,json,xml.etree.ElementTree as ET
r=ET.fromstring(pathlib.Path('arxiv_unimodal.response').read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
lines=[]
for e in r.findall('a:entry',ns):
 t=' '.join(e.findtext('a:title','',ns).split());su=' '.join(e.findtext('a:summary','',ns).split());lines.append(e.findtext('a:id','',ns)+' '+t+'\n'+su)
print('\n'.join(lines))
c=json.loads(pathlib.Path('semantic_citations.response').read_bytes());print('CITATIONS',json.dumps(c,ensure_ascii=False,indent=2))
with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n## arXiv unimodality/Brownian results\n'+'\n\n'.join(lines)+'\n## Semantic Scholar citations\n```json\n'+json.dumps(c,ensure_ascii=False,indent=2)+'\n```\n')
