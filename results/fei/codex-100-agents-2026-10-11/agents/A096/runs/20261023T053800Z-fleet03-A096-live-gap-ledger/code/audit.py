"""Final readback and in-entry correction of a superseded rolling gap."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root.parents[1]/'LEARNED.md'
lines=p.read_bytes().decode('utf-8').splitlines(keepends=True)
for i,line in enumerate(lines):
    if '20261023T010221Z-fleet03-A096-live-gap-ledger' in line and 'Stage19 correction:' not in line:
        ending='\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else ''
        lines[i]=line.rstrip('\r\n')+' [Stage19 correction: the stated ORIGINAL-source vacuum-return gap was closed by A003/A082/A097 calibration absorption; it is no longer unpaid. The current frontier is genuine conditional-nonempty transport, with the phase-funded sector now paid and the zero-singleton sector still open.]'+ending
p.write_bytes(''.join(lines).encode('utf-8'))
report=(root/'REPORT.md').read_text(encoding='utf-8')
assert report.rstrip().endswith('untouched.')
assert '1541504' in (root/'out/VALIDATION.json').read_text(encoding='utf-8')
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
receipt=json.loads((root/'out/LOCAL_PERSISTENCE.json').read_text(encoding='utf-8'))
receipt['files']=[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(root.rglob('*')) if p.is_file() and p.name!='LOCAL_PERSISTENCE.json']
receipt['superseded_rolling_gap_annotated_in_entry']=True
(root/'out/LOCAL_PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('PASS: final report read back; progress/delta identical; prior rolling gap explicitly marked closed; local hashes refreshed.')
