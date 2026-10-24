from pathlib import Path
for name,limit in [('ellipse.txt',550),('apollonian.txt',240)]:
 lines=Path(name).read_text(encoding='utf8').splitlines();print('\nFILE',name)
 print('\n'.join(f'{i+1}: {l}' for i,l in enumerate(lines[:limit])))
import xml.etree.ElementTree as E
r=E.parse('arxiv_target.xml').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns)[:35]:print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns).replace('\n',' '))
