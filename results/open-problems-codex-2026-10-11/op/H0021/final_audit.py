import pathlib,json
p=pathlib.Path('STATUS.md');s=p.read_text(encoding='utf8');p.write_text(s,encoding='utf8',newline='\n')
assert p.read_bytes().startswith(b'STATE: DONE\n')
a=[json.loads(x) for x in pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()];assert len(a)==7
log=pathlib.Path('lean_check.txt').read_text(encoding='utf8');assert 'exit_code=0' in log and 'sorryAx' not in log
for f in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:assert pathlib.Path(f).stat().st_size>0
print('Final artifact checks passed.');print(s);print(log)
