from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf-8');s+=r'''

## 20. Parameter-only formulation, verification and final verdict
To express the results using the source's parameters rather than a particular retained p, set c=1-epsilon and

    R=c B/lambda,  B=min(Delta-1,lambda^2/4).

At the largest allowed parameter p=c/lambda, rho_k=max(c,c(B/lambda)^{1-2/k}); smaller p only improves the upper bounds. Thus R<=1 yields the universal O_epsilon((log n)^3) bound for every p in the source range, and R<=1-eta yields O_{epsilon,eta}(log n). For R>1, the integer moment orders available from this method satisfy

    2<=k<2 log(B/lambda)/log(R),

with the explicit finite probability estimate (13). No endpoint or noninteger-moment improvement is asserted. This is an upper-bound architecture with matching results in some regimes, not the full optimal all-regime answer.

The script second_checks.py completed in approximately 8.14 seconds and saved second_checks.json. It exhaustively checked all 1094 nonempty simple labeled host graphs on 2 through 5 vertices, at three retention parameters each (3282 laws), by enumerating every retained edge subset. All 396312 ordered triple and 1968258 ordered quadruple connectivity inequalities passed, including all repeated-terminal patterns. Summed diagrams and eligible operator-moment bounds through order five also passed. The maximum triple ratio was 1 within floating error, while the maximum quadruple ratio was about 0.632091. In addition, 41744 nonbacktracking row bounds through length eight passed; their maximum ratio was 1 within floating error. These are checks, not proofs of the general inequalities.

Weighted-path validation covered 960 random positive weighted paths of lengths 1 through 12 and the exact equality families w_0=w_{h-1}=1/sqrt(2), interior weights 1/2 (single-edge case weight 1). All product bounds passed and equality errors were below 4.9e-15. No job approached the 1 GB memory limit; matrices had at most five host vertices or thirteen path vertices.

The final SpectralFlow.lean invocation from ~/lean_verify completed with exit code 0 and empty diagnostics. It was wrapped with a 3600-second timeout, ran one at a time through the shared Lean checker, and its output is SPECTRAL_LEAN_CHECK.txt. The checked declaration flow_prod_bound proves the arbitrary finite product bound used in the weighted-path optimization. It imports only Mathlib.Data.Fintype.Card, Mathlib.Data.Real.Basic, Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset and Mathlib.Tactic.Linarith. No sorry, native_decide or explicit axiom is used. Earlier diagnostic failures were due to a shell-encoding issue and a missing cardinality import; those invocations are not claimed checked. Formal scope remains algebraic, not the full percolation proof.

Final second-attempt VERDICT: PARTIAL. Sections 12–19 contain full new mathematical derivations and their applicability checks; the historical row bound was explicitly reverified and is not counted as new. The optimal full-source largest-component scale in the effective-supercritical regime R>1 remains uncharacterized. In particular, universal interpolation loses against the regular-tree lower exponent, and arbitrary collision/multiplicity/Perron-profile effects have not been optimized. This remaining gap is real and is not hidden by the matching exact-parameter special cases.
'''
# Update the opening with the new result without removing the prior proof history.
marker='## Result obtained: critical complete trees have cubic logarithmic extremes'
intro='''## Latest result from the reopened attempt
The two-point-operator/BK diagram argument proves a universal cubic logarithmic upper bound under p min(Delta-1,lambda^2/4)<=1, a logarithmic bound under a fixed gap below one, and explicit higher-moment upper bounds in part of the complementary regime. An infinite family of exact triples, including (Delta,lambda,epsilon)=(10,6,1/3), has matching worst-case Theta((log n)^3) bounds for all large n. Full proofs are in Sections 12-20. The full source question remains PARTIAL.

'''
s=s.replace(marker,intro+marker,1);p.write_text(s,encoding='utf-8')
p=Path('CLAIMS.jsonl');rows=[json.loads(line) for line in p.read_text(encoding='utf-8').splitlines()]
for r in rows:
 r['checks']=r['checks'].replace('weighted-flow Lean check pending.','weighted-flow finite-product Lean check passed with exit code 0 (algebraic scope only).')
rows.append(dict(problem_id='G0010',claim='For integer k with rho_k<1, Q_k=ceil((e (2k-5)!! n [4/(1-rho_k)]^(2k-3))^(1/k)) satisfies P(L_1>=alpha Q_k)<=exp(-alpha/9) for alpha>=1.',status='proved',proof_location='ATTEMPT.md Section 19',remaining_gap='This confidence refinement does not identify the tight parameter-dependent quantile.',checks='Moment Markov bound plus Hutchcroft arXiv:2008.11197v2 Theorem 2.2 p.14, applied to the finite unit-weight host with beta=-log(1-p).'))
rows.append(dict(problem_id='G0010',claim='The finite Perron-flow product bound in SpectralFlow.lean is kernel checked for an arbitrary finite index type.',status='proved',proof_location='SpectralFlow.lean',remaining_gap='Graph compression, interpolation and probability remain written proofs, not fully formalized.',checks='Final hour-timeout lake env lean run returned exit 0 with empty diagnostics; no sorry or native_decide.'))
p.write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
p=Path('STATUS.md');s=p.read_text(encoding='utf-8');lines=s.splitlines();lines[0]='STATE: DONE';lines[1]='NEXT: Close the interpolation/tightness gap for R=(1-epsilon) min(Delta-1,lambda^2/4)/lambda>1, including collision and multiplicity effects.';lines[2]='VERDICT: PARTIAL';s='\n'.join(lines)+'\n';s+='''2026-10-12: Second attempt completed. Proved the general kth component-moment inequality, the enlarged effective-branching cubic/logarithmic wedges, and matching Theta((log n)^3) worst-case bounds for exact triples (m^2+1,2m,1-2/m). The fourth-moment bound also reaches a fixed-gap branching-supercritical regime. Full all-regime answer remains unresolved.
2026-10-12: Exhaustive finite-product/diagram tests passed (1094 graphs, 3282 laws, over 1.9 million quadruples); SpectralFlow.lean passed with exit 0. Verified Hutchcroft's universal-quantile theorem and derived an exponential confidence refinement. Final mathematical and literature limitations are in ATTEMPT.md Sections 16, 19-20 and LITERATURE.md.
''';p.write_text(s,encoding='utf-8')
print('Final status:',Path('STATUS.md').read_text().splitlines()[:3])
print('Claims:',len(rows))
