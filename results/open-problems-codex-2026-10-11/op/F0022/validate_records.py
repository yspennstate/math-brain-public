import pathlib,json,ast
for n in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:
 p=pathlib.Path(n);print(n,'exists',p.exists(),'bytes',p.stat().st_size if p.exists() else 0)
for x in json.loads(pathlib.Path('crossref.response').read_text())['message']['items']:
 if x.get('DOI')=='10.1007/s00440-010-0313-8':
  print('Hongler metadata',x.get('author'),x.get('volume'),x.get('page'),x.get('published'));p=pathlib.Path('LITERATURE.md');s=p.read_text();s=s.replace('**151** (2011), 613–631','**'+x.get('volume','151')+'** (2011), '+x.get('page','').replace('-','–'));p.write_text(s,encoding='utf-8')
for line in pathlib.Path('CLAIMS.jsonl').read_text().splitlines():json.loads(line)
assert pathlib.Path('STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
assert len(json.loads(pathlib.Path('search_log.json').read_text()))==14
assert 'openalex_citing' in pathlib.Path('LITERATURE.md').read_text()
print('Record validation passed');print(pathlib.Path('STATUS.md').read_text());print(pathlib.Path('lean_check.txt').read_text())
