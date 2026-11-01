import pathlib,json
p=pathlib.Path('.')
lean=(p/'lean_check.txt').read_text(encoding='utf8')
assert lean.startswith('exit_code=0\n'),lean
claims=[json.loads(line) for line in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==5
claims[0]['checks'][-1]='Lean kernel checked the two supporting inequalities in WindowSeparation.lean; whole probability theorem is not Lean-formalized.'
claims[-1]['checks'].append('54 sharpened indicator-translation checks in checks.json passed.')
(p/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
for name in ['ATTEMPT.md','LITERATURE.md']:
 q=p/name;q.write_text(q.read_text(encoding='utf-8-sig'),encoding='utf8')
with (p/'ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('\nFinal verification (2026-10-12): Lean compiler exited 0 for WindowSeparation.lean after adding the explicit Mathlib.Data.Real.Basic import and removing the BOM. Both supporting inequalities were kernel checked; no sorry, axiom, or native_decide occurs. Earlier failed compiler outputs are retained as lean_check_first_failed.txt and lean_check_second_failed.txt. The full probability theorems are proved on paper, not formalized in Lean. The sharpened [0,1]-valued translation bound in Theorem D also passed 54 deterministic checks.\n')
(p/'STATUS.md').write_text('''STATE: DONE
NEXT: Investigate whether the exact BBM/decomposability or independent-cut hypotheses yield a tight family of stationarizing shifts; this remains open in this attempt.
VERDICT: PARTIAL

2026-10-12: Verified exact source Definitions 2.1–2.2 and Problems 7.1–7.3, PDF pp.2–3 and 25–26.
2026-10-12: Completed bounded arXiv, Crossref, OpenAlex, Semantic Scholar and GitHub requests. No exact solution found among inspected papers. OpenAlex coverage was blocked by HTTP 429. Semantic Scholar's citation request succeeded; inspected Pitman–Tang 2015, a related bridge-embedding theorem rather than a compatibility solution.
2026-10-12: Proved the stationary-increment special case, the FBM equivalence with finite-shift stationarization, and path-independent duration special case; full proofs in ATTEMPT.md.
2026-10-12: Proved the stronger general finite-window total-variation bound under independent uniform centering: distance <= E min(1,abs(S+M)/R), for one finite Brownian-future starting time S. The uniform centers are not tight, so this does not solve the source questions.
2026-10-12: Refereed hypotheses, random-time conditioning, clock identifiability and reversal bias. Finite checks: 400 interval-separation, 35 signed translation-bound and 54 sharpened indicator-bound cases passed; discrete stopped-word enumeration agrees with the exact obstruction.
2026-10-12: Lean supporting-inequality check exited 0 with narrow imports and no sorry/native_decide. Encoding/import failures were corrected and their logs retained. No full Brownian theorem is claimed Lean-formalized.
2026-10-12: Closed this attempt as PARTIAL. No proof or counterexample for any full Problem 7.1–7.3 is claimed. Five typed claims and the precise remaining gap are saved.
''',encoding='utf8')
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:assert (p/name).stat().st_size>0
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
assert 'sorry' not in (p/'WindowSeparation.lean').read_text(encoding='utf8')
assert 'native_decide' not in (p/'WindowSeparation.lean').read_text(encoding='utf8')
print('DONE / PARTIAL; five claims; required records validated; Lean exit 0')
