from pathlib import Path
import json
s=Path('minimal.txt').read_text(encoding='utf8');pos=s.find('Proposition 28 (Quasistability)');page=s.rfind('PDF PAGE ',0,pos);print(s[page:s.find('\n',page)])
p=Path('LITERATURE.md');t=p.read_text(encoding='utf8');actual=s[page:s.find('\n',page)].split()[-1];t=t.replace('Proposition 28, PDF p.33','Proposition 28, PDF p.'+actual);p.write_text(t,encoding='utf8')
for line in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():json.loads(line)
assert Path('STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
assert 'exit=0' in Path('lean_check.log').read_text()
lean=Path('FiniteChecks.lean').read_text();assert 'sorry' not in lean and 'native_decide' not in lean
print('Final records valid; claims:',len(Path('CLAIMS.jsonl').read_text().splitlines()))
print(Path('STATUS.md').read_text())
