from pathlib import Path
import json,urllib.request
p=Path('FiniteChecks.lean');s=p.read_text(encoding='utf8');p.write_text('import Mathlib.Data.Real.Basic\n'+s if not s.startswith('import Mathlib.Data.Real.Basic') else s,encoding='utf8')
claims=[
('Nonnegative boundary heights and domain enlargement stochastically increase the finite-volume uniformly convex wall field.','proved','ATTEMPT.md, Proposition 1','None for finite volumes; uses standard continuous FKG association.','Mixed log-density derivatives and boundary interpolation checked analytically; two-vertex quadrature supports direction.'),
('E_{mu_N^+} phi_i >= c(V) log ||i||_infty for sufficiently large ||i||_infty and N >= 2||i||_infty.','proved','ATTEMPT.md, Proposition 2','External dependency: ordinary full-box convex wall lower theorem, verified in Velenik PDF p.22; original D-G theorem text not retrieved. Does not construct the infinite-volume limit.','Pin-free translated square and boundary signs checked; weak limit uses stochastic comparison of bounded truncations.'),
('The finite-volume orthant Gibbs field satisfies E sum_e grad_e(phi) V\'(grad_e(phi)) = n and n/c_+ <= E sum_e grad_e(phi)^2 <= n/c_-.','proved','ATTEMPT.md, Proposition 3','None for finite graphs with all grounded heights zero.','Integration boundary term checked; numerical energy 2.0000271962 versus 2 in a nonlinear two-coordinate example.'),
('Finite-volume E phi_i <= sqrt(n R_N(i)/c_-) where R_N is the resistance to grounded pin and outer boundary.','proved','ATTEMPT.md, Proposition 3','This upper bound depends on n and cannot prove the target infinite-volume upper bound.','Grounded Laplacian Cauchy-Schwarz proof; finite path step submitted to Lean, not yet marked checked.'),
('For the positive nearest-neighbor field E[phi_v | others] >= (c_-/(4c_+)) sum_{w~v} phi_w.','proved','ATTEMPT.md, Proposition 4','None in finite volume with nonnegative neighbors.','Derivative inequality, increasing likelihood ratio comparison, and truncated-normal integral checked in full.'),
('The positive pinned box exhaustion has a proper infinite-volume limit iff sup_N E phi_(1,0) < infinity.','proved','ATTEMPT.md, Proposition 5','The uniform neighboring mean bound itself is not proved. Uses standard Brascamp-Lieb variance theorem.','Soft-wall approximation, path propagation, product tightness, monotone uniqueness, uniform integrability and Chebyshev escape checked analytically.'),
('Two-coordinate quadrature for V(t)=t^2/2+0.3(1-cos t) supports the energy identity and boundary monotonicity.','numerical_evidence','numerical_checks.json and ATTEMPT.md, Computation','No certified quadrature error or inference about large boxes.','401 and 801 grids; Gaussian exact mean benchmark and grid refinement.'),
('For all even C^2 uniformly strictly convex V in dimension 2 the pinned positive field exists and E phi_i is comparable to log |i|.','conjecture','ATTEMPT.md, Remaining gap and verdict','Missing volume-uniform neighboring mean estimate and logarithmic spatial upper bound.','No exact published resolution found in bounded search; no proof or counterexample produced.')]
with Path('CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for c,s,l,g,k in claims:f.write(json.dumps({'problem_id':'F0073','claim':c,'status':s,'proof_location':l,'remaining_gap':g,'checks':k},ensure_ascii=False)+'\n')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\nJournal metadata from Crossref: Belius–Wu, Annals of Probability 48(6) (2020), DOI 10.1214/19-AOP1416. Schweiger–Wu–Zeitouni, Annals of Probability (2026), DOI 10.1214/25-AOP1808; Crossref publication date 2026-09-01. Exact-title search identified Yvan Velenik, Wetting of gradient fields: pathwise estimates, arXiv:0706.1632v4, PTRF (2008), DOI 10.1007/s00440-007-0130-x.\n')
url='https://arxiv.org/pdf/0706.1632'
try:
 with urllib.request.urlopen(url,timeout=35) as r:b=r.read()
 Path('wetting_correct.pdf').write_bytes(b)
 import pymupdf
 d=pymupdf.open('wetting_correct.pdf');Path('wetting_correct.txt').write_text('\n'.join('\nPAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');result='OK '+str(len(b))
except Exception as e:result=repr(e)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(f'\n- 2026-10-12 | corrected wetting primary PDF | `{url}` | {result}\n')
print('Claims saved; wetting PDF',result)
