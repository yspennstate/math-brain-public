from pathlib import Path
for name,words in [('source.txt',['Open problems','fraction','identity','weak','Pegden']),('ellipse.txt',['Theorem','Proposition','identity','maximal']),('apollonian.txt',['Theorem','conjecture'])]:
 t=Path(name).read_text(encoding='utf8');lines=t.splitlines();print('\nFILE',name,'length',len(t))
 for i,l in enumerate(lines):
  if any(w.lower() in l.lower() for w in words):print('\n',i+1,'\n','\n'.join(lines[max(0,i-3):i+10]))
import xml.etree.ElementTree as E
r=E.parse('arxiv_target.xml').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
print('\nTARGET PAPERS')
for e in r.findall('a:entry',ns):
 title=e.findtext('a:title',namespaces=ns).replace('\n',' ');summary=e.findtext('a:summary',namespaces=ns).replace('\n',' ')
 print(e.findtext('a:id',namespaces=ns),title)
 if any(w in title.lower() for w in ['pattern','identity','scaling','apollonian']):print(summary)
