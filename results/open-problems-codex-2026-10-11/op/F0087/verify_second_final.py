from pathlib import Path
import json
P=Path('.')
p=P/'finish_second_attempt.py';s=p.read_text(encoding='utf-8-sig').replace("assert (P/'STATUS.md').read_bytes().startswith(b'STATE: DONE\\n')", "assert (P/'STATUS.md').read_text(encoding='utf8').splitlines()[0] == 'STATE: DONE'");p.write_text(s,encoding='utf8')
status=(P/'STATUS.md').read_text(encoding='utf8').splitlines();assert status[0]=='STATE: DONE' and status[2]=='VERDICT: PARTIAL'
claims=[json.loads(l) for l in (P/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()];assert len(claims)==16
assert 'exit_code=0' in (P/'fusion_lean_check.log').read_text(encoding='utf8')
print('Final file check passed: STATE DONE / VERDICT PARTIAL; 16 claims. Windows CRLF correctly accepted.')
