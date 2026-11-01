from pathlib import Path
import json,re
p=Path(__file__).parent
log=(p/'lean_check.txt').read_text(encoding='utf8')
if 'EXIT_CODE: 0' not in log:
 print('Compiler result not yet successful. Status unchanged.');raise SystemExit(0)
lean=(p/'Capacity.lean').read_text(encoding='utf8')
assert not re.search(r'\b(sorry|native_decide|axiom)\b',lean)
assert '\nimport Mathlib\n' not in '\n'+lean
rows=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==8
assert all(set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=r.keys() for r in rows)
for r in rows:
 if r['proof_location']=='ATTEMPT.md Proposition B':r['checks']+=' Compiler verified Capacity.lean, vacant_antitone (EXIT_CODE 0); remaining analysis is a written proof.'
 if r['proof_location']=='ATTEMPT.md Proposition E':r['checks']+=' Compiler verified Capacity.lean, packing_capacity_obstruction (EXIT_CODE 0); the Poisson and measure steps are written proofs.'
(p/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
a=(p/'ATTEMPT.md').read_text(encoding='utf8');a+='\n## Final referee record\n2026-10-11: Reread all six deductions and the source hypotheses. The proofs use canonical openness, a.e. uniqueness, saturation and appetite order only where stated. The Poisson packing contradiction and the one-dimensional ergodic argument are complete written deductions from the cited inputs. No proof of either unresolved near-one regime was obtained. Lean compiler returned EXIT_CODE 0 for the two named elementary lemmas in Capacity.lean; this certifies only those lemmas. The original retry had no surviving F0085 Lean process and no final result; the sequential replacement used a streamed log and a one-hour timeout. All eight claim rows parse, and all ten exact arithmetic sanity checks passed.\n';(p/'ATTEMPT.md').write_text(a,encoding='utf8')
(p/'STATUS.md').write_text('STATE: DONE\nNEXT: No further step in this attempt; a continuation would need a near-one vacant-crossing estimate with dependence control, or a matching literature theorem.\nVERDICT: PARTIAL\n2026-10-11: Source and follow-up theorems verified. FPV Theorem 1.1 settles both small-appetite regimes for d>=2; Theorem 1.2 settles closed-claimed percolation in sufficiently high dimensions.\n2026-10-11: Completed and refereed canonical complement identification, appetite monotonicity consequences, raw canonical claimed nonpercolation, d=1 and endpoint cases, unbounded-radius obstruction, and a stationary-slab counterexample to the density heuristic.\n2026-10-11: Lean checked two elementary lemmas (EXIT_CODE 0); eight claim records and ten exact arithmetic checks validated.\n2026-10-11: Near-one unclaimed nonpercolation for d>=2 and low-dimensional near-one closed-claimed percolation are unresolved in this attempt. Bounded literature search did not certify a full solution; OpenAlex was rate limited.\n',encoding='utf8')
print('STATE: DONE; VERDICT: PARTIAL; Lean exit code 0; eight claims validated.')
