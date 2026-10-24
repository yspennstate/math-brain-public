from pathlib import Path
root=Path(__file__).parent
if (root/'DIRECT_UPPER.md').exists():
 raise SystemExit('First-pass finalizer retained for provenance; use close_second.py for current status and formal-check records.')
p=root/'STATUS.md'
s=p.read_text(encoding='utf-8-sig')
s=s.replace('STATE: WORKING','STATE: DONE').replace('NEXT: Finish auxiliary Lean check, audit saved records, and finalize PARTIAL result.','NEXT: Seek a matching weak-moment upper bound; collect pending auxiliary Lean output before claiming formal verification.')
if 'Finalized PARTIAL with matching upper bound unresolved.' not in s:
 s+='2026-10-11: Proved finite-second-moment boundary law defeating every polynomial rate and having no higher moments. Six claims saved and JSON-validated.\n'
 s+='2026-10-11: Finalized PARTIAL with matching upper bound unresolved. Auxiliary Lean remains queued (session 84590); no kernel check claimed.\n'
p.write_text(s,encoding='utf8')
(root/'FORMAL_CHECK.md').write_text('Auxiliary.lean was submitted with lake env lean ~/brain_workers/TRIO_1011/op/C0109/Auxiliary.lean from ~/lean_verify on 2026-10-11. The shared scheduler reported waiting for a slot. At turn completion it remained queued (tool session 84590). No completed kernel check is claimed. The scope is five algebraic margin and radius inequalities; the stochastic theorem is not formalized. The file contains no sorry or native_decide. Numerical and exact rational checks completed separately in checks.json.\n',encoding='utf8')
assert p.read_bytes().splitlines()[0]==b'STATE: DONE'
print('STATE: DONE; VERDICT: PARTIAL; no completed Lean verification claimed.')
