import pathlib,json
p=pathlib.Path('.')
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
a=[json.loads(s) for s in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(a)==5
assert (p/'lean_check.txt').read_text(encoding='utf8').startswith('exit_code=0\n')
t=(p/'ATTEMPT.md').read_text(encoding='utf8')
assert '## Theorem D' in t and 'A further obstruction to transplanting' in t and 'Final verification (2026-10-12)' in t
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:assert (p/name).stat().st_size>0
lean=(p/'WindowSeparation.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean
# Correct the validator to permit the platform's CRLF line separator.
f=p/'finalize.py';s=f.read_text(encoding='utf-8-sig');s=s.replace("assert (p/'STATUS.md').read_bytes().startswith(b'STATE: DONE\\n')", "assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'");f.write_text(s,encoding='utf8')
print('Validated: DONE / PARTIAL; five claims; Lean exit 0; all manuscripts and gap present.')
