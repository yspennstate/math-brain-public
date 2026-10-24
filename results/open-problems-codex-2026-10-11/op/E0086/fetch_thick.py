import urllib.request,urllib.parse,pathlib,json,xml.etree.ElementTree as E
q='ti:"Thick points for planar Brownian motion"'
u='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':5})
p=pathlib.Path('.')
try:
 b=urllib.request.urlopen(u,timeout=30).read();p.joinpath('search_thick_original.txt').write_bytes(b);r=['arxiv_thick_original',u,'OK',len(b)]
 root=E.fromstring(b);ns={'a':'http://www.w3.org/2005/Atom'}
 for e in root.findall('a:entry',ns):
  aid=e.find('a:id',ns).text;print(aid,e.find('a:title',ns).text)
  pu=aid.replace('http://arxiv.org/abs/','https://arxiv.org/pdf/'); pdf=urllib.request.urlopen(pu,timeout=30).read();p.joinpath('thick_original.pdf').write_bytes(pdf)
  import pymupdf
  d=pymupdf.open('thick_original.pdf');p.joinpath('thick_original.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(d)),encoding='utf-8')
except Exception as e:r=['arxiv_thick_original',u,'ERROR',str(e)]
p.joinpath('search_log5.json').write_text(json.dumps([r],indent=2));print(r)
