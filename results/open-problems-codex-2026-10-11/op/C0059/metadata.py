import requests,pathlib,json
queries=[('cauchy_ref','Infinite random planar maps related to Cauchy processes'),('geometry_ref','Geometry of infinite planar maps with high degrees'),('subdiffusive_ref','Infinite stable Boltzmann planar maps are subdiffusive')]
for name,q in queries:
 try:
  r=requests.get('https://api.crossref.org/works',params={'query.bibliographic':q,'rows':3},timeout=25);pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8')
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 Crossref '+q+': '+r.url+' HTTP '+str(r.status_code)+'; raw search_'+name+'.txt\n')
  print(name,[(x.get('title'),x.get('DOI'),x.get('published'),x.get('volume'),x.get('page')) for x in r.json().get('message',{}).get('items',[])])
 except Exception as e:print(name,e)
