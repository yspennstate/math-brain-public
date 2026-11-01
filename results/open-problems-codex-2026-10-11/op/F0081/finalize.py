from pathlib import Path
import json,re
s=Path('LITERATURE.md').read_text(encoding='utf8')
# Restore mathematical Unicode lost by the shell's legacy text encoding.
s=s.replace('d ? 2','d >= 2').replace('d?3','d>=3').replace('0<s(d)<1','0<s(d)<1')
s=s.replace('E* X^? < ? if and only if ? < d/2.','E* X^alpha < infinity if and only if alpha < d/2.')
s=s.replace('E* X^d = ?','E* X^d = infinity').replace('P*(X>r) ? C r^{-s(d)}','P*(X>r) <= C r^{-s(d)}').replace('E* X^{d/2}=?','E* X^{d/2}=infinity')
Path('LITERATURE.md').write_text(s,encoding='utf8')
rows=[json.loads(a) for a in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for a in rows:
 if a['status']!='numerical_evidence':a['checks']+=' Lean: ResidualChecks.lean compiled with exit 0; only finite count/chain arithmetic was formalized, not the stochastic reduction.'
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(a,ensure_ascii=False)+'\n' for a in rows),encoding='utf8')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: Establish scale-uniform residual-charge fluctuation bounds (ATTEMPT.md equations (2),(3)), or direct integrability bounds in (4); no further unconditional inference is justified by this attempt.
VERDICT: PARTIAL
2026-10-11: Verified original Open Problems (i), PDF p.34, intensity-one independent Poisson inputs and stable matching. Screened arXiv, Crossref and 81 Semantic Scholar citations; GitHub search returned no repositories. OpenAlex rate-limited; no exact published solution found in inspected material.
2026-10-11: Proved exact residual-charge identity, equivalent moment-integrability formulation, conditional second/fourth-moment criterion, short-edge boundary-flux conservation, and robust finite long-edge obstruction. No improved unconditional exponent and no proof/counterexample of the conjecture.
2026-10-11: Finite chain and eight torus simulations passed exhaustive blocking-pair and residual-identity checks. Lean finite arithmetic file compiled successfully (exit 0), kernel-checked Omega proofs, no sorry/native_decide. Remaining gap stated in ATTEMPT.md. Research attempt complete with partial verdict.
''',encoding='utf8')
print('Final status and claim ledger saved')
print(Path('LITERATURE.md').read_text(encoding='utf8')[:2600])
print(Path('lean_check.log').read_text(encoding='utf8'))
print('Records:',[(p.name,p.stat().st_size) for p in Path('.').iterdir() if p.name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']])
