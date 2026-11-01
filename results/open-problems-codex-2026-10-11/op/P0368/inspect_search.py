import json, pathlib
x=json.loads(pathlib.Path('crossref.json').read_text())
for w in x['message']['items']:
 print(w.get('title'),w.get('DOI'),w.get('published',{}).get('date-parts'))
print('GITHUB')
for w in json.loads(pathlib.Path('github.json').read_text())['items']: print(w['full_name'],w['description'])
