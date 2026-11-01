from pathlib import Path
import xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
extra='\n## Recent arXiv records inspected (exact API bibliography)\n\n'
for e in E.parse('arxiv_continuity.txt').findall('a:entry',ns):
 title=' '.join(e.findtext('a:title',namespaces=ns).split())
 authors=', '.join(a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns))
 extra+=f"- {authors}. *{title}*. {e.findtext('a:id',namespaces=ns)}; submitted {e.findtext('a:published',namespaces=ns)}. Abstract inspected; different models except the source itself.\n"
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(extra)
