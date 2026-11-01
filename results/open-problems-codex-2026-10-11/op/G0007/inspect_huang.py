from pathlib import Path
s=Path('huang.txt').read_text(encoding='utf8').splitlines()
print('\n'.join(s[535:620]))
import xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_stationary_energy.txt').findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
