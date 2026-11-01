from pathlib import Path
import xml.etree.ElementTree as ET,json
R=Path(__file__).resolve().parent;ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_leads','arxiv_sos','arxiv_wetting']:
 p=R/(name+'.json')
 if not p.exists():continue
 for e in ET.fromstring(p.read_bytes()).findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),[a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)])
s=(R/'degenerate_pdf.txt').read_text(encoding='utf8')
for term in ['[36]','[37]','[94]']:
 k=s.rfind(term);p=s.rfind('=== PDF PAGE',0,k);print(term,s[p:s.find('\n',p)],s[k:k+250])
for name in ['lean_check.json','prior_records.txt','math_recall.txt','memory_topic.txt','memory_mistakes.txt']:
 p=R/name
 if p.exists():print(name,p.read_text(encoding='utf8')[:10000])
 else: print(name,'pending or missing')
