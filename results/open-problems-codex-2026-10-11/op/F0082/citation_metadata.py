import urllib.request,pathlib,xml.etree.ElementTree as E
u='https://export.arxiv.org/api/query?id_list=2311.17687,2109.13590,2506.16873,2402.13705,1910.01614,2303.05137,2304.11145,2509.08659,2601.08983'
try:
 b=urllib.request.urlopen(u,timeout=40).read();pathlib.Path('citation_metadata.xml').write_bytes(b);s=f'OK {len(b)} bytes'
except Exception as e:s=str(e)
with open('LITERATURE.md','a',encoding='utf8') as f:f.write(f'- 2026-10-11 arXiv citation metadata: {u} — {s}.\n')
if pathlib.Path('citation_metadata.xml').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 with open('LITERATURE.md','a',encoding='utf8') as f:
  f.write('\n## Citation-graph follow-up metadata (leads, not solutions)\n\n')
  for e in E.fromstring(b).findall('a:entry',ns):
   authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns));title=' '.join(e.find('a:title',ns).text.split());id=e.find('a:id',ns).text;summary=' '.join(e.find('a:summary',ns).text.split())
   f.write(f'- {authors}. **{title}**. {id}. Abstract: {summary}\n\n');print(title,summary[:600])
