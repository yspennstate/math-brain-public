from pathlib import Path
import json
claims=[
 {'problem_id':'E0110','claim':'For U=-exp(-x), Gamma=(R+R^T)/2 and all mu_i<=-m<0, the GRBM satisfies the conjectured pointwise TV bound with exponent min(m/16,m^2/4)/d; if m>=1 the exponent m/(4d) is valid.','status':'proved_special_case','proof_location':'ATTEMPT.md, Proved special case, sections 1-4','remaining_gap':'General Gamma and general admissible U, including Gamma=I for d>1.','checks':['Direct stationary-current cancellation','Complete log-gamma operator factorization proof','Weighted chain inequality','Local parabolic L2-to-pointwise-TV step','SpecialCase.lean algebraic checks only; lean_check.txt exit 0','checks.json and morse_refinement.json']},
 {'problem_id':'E0110','claim':'For Gamma with diagonal 1 and adjacent off-diagonal -1/2, sum_i v_i^2/i <= 2d v^T Gamma v for every v in R^d.','status':'proved','proof_location':'ATTEMPT.md, section 3','remaining_gap':'None for this finite inequality.','checks':['Full Cauchy-Schwarz and telescoping proof','Lean checks prefix Cauchy-Schwarz for arbitrary n and chain quadratic identity at d=3; full weighted sum is a written proof','Weighted matrix eigenvalue checks through d=1024']},
 {'problem_id':'E0110','claim':'The one-dimensional density proportional to exp(-a x-beta exp(-x)) has Poincare gap at least a^2/4 for 0<a<=1, a/8 for 1<a<2, and a-1 for a>=2.','status':'proved','proof_location':'ATTEMPT.md, section 2','remaining_gap':'None for the stated lower bounds.','checks':['Closed-operator factorization and closed-range argument','Lean morse_shift, small_shape_partner, middle_shape_partner','Finite-difference check and grid refinement; numerical errors documented']},
 {'problem_id':'E0110','claim':'For the product-form special case the invariant coordinates have 2exp(-X_i) distributed as Gamma(2M_i,1), M_i=-sum_{j<=i}mu_j.','status':'proved_special_case','proof_location':'ATTEMPT.md, section 1','remaining_gap':'This density is not established for general covariance.','checks':['Normalization by change of variables','Direct divergence-free skew-current calculation','Random floating-point residual <1e-12']},
 {'problem_id':'E0110','claim':'Tang Conjecture 1.5 holds for the full Theorem 1.3 class with an appropriate dimension-uniform interpretation of the inputs.','status':'conjecture','proof_location':'ATTEMPT.md, section 5; source_pdf.pdf p.5','remaining_gap':'No full proof or counterexample found; bounded literature search is incomplete because OpenAlex citing endpoints rate-limited.','checks':['Source verified','arXiv, Crossref, Semantic Scholar, OpenAlex, GitHub queried','Prior recorded attempt inspected read-only']}
]
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('''

## Computations and formal checks

Scripts: checks.py and refine.py. Both are short foreground computations with
dense vectors/tridiagonal eigensolvers; the largest grid has 20,000 points.
No stochastic simulation or joint-TV estimate is used to justify the theorem.

Weighted covariance eigenvalues were computed for d=1,2,4,...,1024. The smallest
value of d*lambda_min(diag(sqrt(i)) Gamma diag(sqrt(i))) increased from 1 at d=1
to 1.83345638 at d=1024; the proved lower bound is 1/2.
Random chain-vector and stationary-current calculations had maximal stationary
cancellation residual 9.1e-13 and no inequality violation.

The Morse operator was discretized with centered second differences and
Dirichlet boundaries at -6 and 100. At a=0.4,1,1.5,2,6,20, the estimates were
consistent with the proved bounds up to ordinary discretization error.
In particular the grid underestimated the a>=2 gap slightly: at a=20, N=10,000
gave 18.997692 instead of 19. This is NOT a counterexample to the proof.
At N=20,000 it gave 18.999423, with Richardson extrapolation 19.000000021.
At a=6 the analogous extrapolation was 4.999999999.
For a>2 the comparison value a-1 is itself exact: the weighted diffusion
operator f''-V_a' f' sends f(x)=exp(x)-beta/(a-1) to -(a-1)f,
and this centered eigenfunction belongs to L2(rho_a) exactly when a>2.
Combined with section 2 this proves equality of the gap there.
Finite interval and grid calculations are checks, not proofs of infinite-volume
gaps. Detailed results are in checks.json and morse_refinement.json.

SpecialCase.lean imports only the required order/real/tactic modules.
Running lake env lean on its full path from ~/lean_verify exited 0.
It checks arbitrary-prefix Cauchy-Schwarz, the d=3 chain energy identity,
the Morse shift identity, and two partner-potential inequalities. It does not
formalize stochastic analysis, the full discrete inequality, or PDE regularity.
Reported axioms: propext, Classical.choice, Quot.sound; no sorry or native_decide.
Initial failure was a UTF-8 BOM emitted by PowerShell, fixed before the successful
run. A harmless unused-hypothesis warning remains.
''')
print('Saved claims and checks')
