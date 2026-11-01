import json, xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv.txt')
for x in r.findall('a:entry',ns): print(x.findtext('a:published',namespaces=ns),x.findtext('a:id',namespaces=ns), ' '.join(x.findtext('a:title',namespaces=ns).split()))
r=json.load(open('crossref.txt',encoding='utf8'))
for x in r['message']['items']: print('CR',x.get('title'),x.get('DOI'),x.get('published'))
r=json.load(open('github.txt',encoding='utf8')); print('GITHUB',r.get('total_count')); print([(x['full_name'],x.get('description')) for x in r.get('items',[])])
