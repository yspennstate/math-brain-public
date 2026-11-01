import pathlib,xml.etree.ElementTree as E,json
p=pathlib.Path('LITERATURE.md');s=p.read_text(encoding='utf8');s+='\n## Exact arXiv metadata for screened relevant hits\n'
ns={'a':'http://www.w3.org/2005/Atom'}
ids=['1506.01590','1909.10217','2505.05447','1902.10624','1910.09623','2304.01167','1602.01328']
seen=set()
for file in ['arxiv.txt','arxiv_exhaust.txt']:
 for e in E.parse(file).getroot().findall('a:entry',ns):
  id=e.find('a:id',ns).text
  if any(x in id for x in ids) and id not in seen:
   seen.add(id);title=' '.join(e.find('a:title',ns).text.split());authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns));date=e.find('a:published',ns).text
   s+=f'- {authors}, *{title}*, {id}; first submitted {date}.\n'
p.write_text(s,encoding='utf8')
p=pathlib.Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s+='\nFinal Lean run: `lake env lean ~/brain_workers/TRIO_1011/op/C0057/PeelingAlgebra.lean`, from ~/lean_verify; exit code 0. There is one unused-hypothesis warning. All six finite algebra lemmas are checked without sorry or native_decide. The formalization covers the Taylor identity, D positivity, denominator comparisons, and recurrence factor identity.\n';p.write_text(s,encoding='utf8')
# Remove the obsolete lossy draft generator, only inside this problem directory.
p=pathlib.Path('write_attempt.py').resolve();root=pathlib.Path('.').resolve()
assert p.parent==root
p.unlink()
# Check essential record integrity.
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','lean_check.txt']:
 p=pathlib.Path(name);print(name,p.stat().st_size)
for x in pathlib.Path('CLAIMS.jsonl').read_text().splitlines():assert json.loads(x)['problem_id']=='C0057'
assert pathlib.Path('lean_check.txt').read_text().startswith('exit_code=0')
assert 'sorry' not in pathlib.Path('PeelingAlgebra.lean').read_text()
