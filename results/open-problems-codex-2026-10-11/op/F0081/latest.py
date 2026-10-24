import json
for a in json.load(open('semantic_citations.json'))['data']:
 p=a['citingPaper']
 if p.get('year',0)>=2024 or any(w in p['title'].lower() for w in ['factor matching','minimal matchings']):print(json.dumps(p,ensure_ascii=False,indent=2))
