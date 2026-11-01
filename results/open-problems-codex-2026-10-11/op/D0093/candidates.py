import json,pathlib
x=json.loads(pathlib.Path('semantic.json').read_text())
for w in x['data']:
 if any(t in w['title'].lower() for t in ['cycle','cutoff','stationary','slow phase','exact sampling']): print(json.dumps(w,ensure_ascii=False,indent=2))
