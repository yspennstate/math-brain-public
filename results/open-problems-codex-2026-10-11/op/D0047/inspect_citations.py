import json,pathlib
p=pathlib.Path('.')
x=json.loads((p/'semantic_citations.json').read_text());
for e in x.get('data',[]):
 c=e.get('citingPaper',{});print(c.get('year'),c.get('title'),c.get('externalIds'))
