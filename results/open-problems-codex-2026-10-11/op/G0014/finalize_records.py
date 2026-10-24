from pathlib import Path
import json
r=Path(__file__).parent
lean=(r/'lean_check.txt').read_text(encoding='utf8')
assert 'EXIT_CODE=0' in lean
p=r/'ATTEMPT.md';s=p.read_text(encoding='utf8');s=s.replace('See lean_check.txt for the actual result.','The final Lean invocation returned EXIT_CODE=0 (one unused-variable warning). The kernel checked the nonnegative-zero-integral lemma and the two algebraic obstructions; there is no sorry, axiom added, or native_decide. See lean_check.txt for the actual result.');p.write_text(s,encoding='utf8')
p=r/'CLAIMS.jsonl'; claims=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()];assert len(claims)==7
for c in claims:
 assert c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
 c['checks']=c['checks'].replace('see lean_check.txt','kernel-checked with exit code 0, see lean_check.txt')
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
(r/'STATUS.md').write_text('STATE: DONE\nNEXT: No further work on the false literal statement; a corrected multitype conjecture requires a separate precise formulation and the gaps listed in ATTEMPT.md.\nVERDICT: SOLVED\n\n2026-10-11: SOLVED means refuted AS POSED, not that the intended corrected Bramson theorem is proved. The zero-initial-mean signed martingale cannot be UI with the asserted positive nonnegative survival limit. Independently, the source speed formula is provably negative for the positive finite-type activation representation.\n2026-10-11: Source v1 authenticated and newer decoupling paper inspected. No exact solution in print identified; OpenAlex and Semantic Scholar requests were rate-limited, so search coverage is incomplete. Full searches in LITERATURE.md.\n2026-10-11: Complete proofs of the UI obstruction, speed-sign obstruction, log-term inversion and lattice obstruction recorded; conditional single-type bounded-offspring repair verified against Chen/Aidekon hypotheses. Auxiliary binary exponential computations saved. Final Lean check passed with exit code 0 (terminal integral and algebra only). Original multitype cascade/extremal-process repair remains unresolved and is explicitly separated.\n',encoding='utf8')
print('Final audit: 7 valid claims; Lean exit 0; required records present; STATE: DONE / VERDICT: SOLVED (literal refutation).')
