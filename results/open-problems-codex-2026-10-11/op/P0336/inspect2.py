import json, pathlib, xml.etree.ElementTree as E
n={'a':'http://www.w3.org/2005/Atom'}
x=E.fromstring(pathlib.Path('arxiv_selection.txt').read_text())
for v in x.findall('a:entry',n):print('ARXIV',v.findtext('a:published',namespaces=n),v.findtext('a:id',namespaces=n),v.findtext('a:title',namespaces=n).replace('\n',' '))
print('SEMANTIC',pathlib.Path('semantic_retry.txt').read_text())
x=json.loads(pathlib.Path('crossref_recent.txt').read_text())
for v in x['message']['items']:print('CROSSREF',v.get('title'),v.get('DOI'),v.get('published'))
x=json.loads(pathlib.Path('github_rectangles.txt').read_text())
for v in x.get('items',[]):print('GITHUB',v['full_name'],v.get('description'))
s=pathlib.Path('source_text.txt').read_text(encoding='utf8');p=s.find('128.');print('REF128',s[p:p+600])
