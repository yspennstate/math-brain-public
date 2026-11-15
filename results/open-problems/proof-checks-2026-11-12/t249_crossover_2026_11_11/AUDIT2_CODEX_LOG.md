# Independent referee log

Task: referee PROOF_UNIFORM.md and the dependent parts of T249_CROSSOVER.md. Started 11 November 2026 (local Asia/Tbilisi time; exact shell time recorded with the environment check).

Only this directory will be modified. No live brain/checklist/mesh commands are run because the author's run-specific instructions prohibit their writes. No browsing, agents, or external code reuse.

## Step 1 — setting

CORRECT, with the NTK convention stated in the note. Expand phi(sqrt(q) z) in orthonormal Gaussian Hermites with coefficients b_k. Then a_0=(sw2 b_0^2+sb2)/q and a_k=sw2 b_k^2/q for k>=1. The fixed-point equation makes their sum one. Gaussian differentiation gives f'(1)=sw2 E phi'^2, f''(1)=sw2 q E phi''^2, f'''(1)=sw2 q^2 E phi'''^2. The stated regularity justifies these identities.

Independently subtract the off-diagonal recursion from T_{l+1}=q+chi T_l:
D_{l+1}=q(1-c_{l+1})+chi T_l-f'(c_l)(T_l-D_l)
=f'(c_l)D_l+q delta_{l+1}+(chi-f'(c_l))T_l.
Thus (1), D_1=q delta_1, and T_l=q(1-chi^l)/eps are correct. Positivity of the kernel follows from its network/positive-kernel recursion; f' may be negative at negative correlations, which matters only in the bounded transient.

Initial observation reserved for the later corollary audit: its log N (without 1+) vanishes at L=1, and its ordering of the rank-one model's eigenvalues needs checking. This does not invalidate (1).

## Step 2 — hypotheses

CORRECT and nonempty. An explicit family is phi(u)=sin(u), sb2=0.05, 0<eps<=0.01. Define q as the unique positive root q=(1-eps)tanh(q)+0.05, and sw2=2(1-eps)/(1+exp(-2q))=q+0.95-eps. Then f(c)=[sw2 exp(-q)sinh(qc)+0.05]/q, beta=q(q-0.05), f'''(1)=(1-eps)q^2, a0=0.05/q. Conservative uniform bounds: 0.53<q<0.56, 1.47<sw2<1.51, 0.25<beta<0.29, M=0.06, a_-=0.089, gamma=0.90. These imply all required upper and reciprocal bounds. The scalar defining equation is strictly increasing for q>0 since its derivative is 1-(1-eps)sech(q)^2>0.

Computed independently with Gaussian quadrature (256, 512, 768 nodes): at eps=0.01, q=0.532160691401069 and sw2=1.47216069140107; at eps=0.0001, q=0.551870927192586 and sw2=1.50177092719259. Full parameter outputs saved in parameters.out. numpy 2.2.3, scipy 1.15.2 and mpmath 1.3.0 are available in the specified interpreter.

The compact-family continuity parenthesis needs a finite nondegenerate limiting critical fixed point; compact sw2 and fixed positive sb2 alone do not establish that such a point exists for every activation. The explicit H bounds, rather than this parenthesis, suffice for the theorem. No fourth derivative bound is supplied by H; this will matter for Remark 2, not for Steps 0–4.

Read compute state: warn/cpu_saturated, owner_away_open. Numerical work uses one thread, tiny arrays and a per-process time limit. Attempted nice -n 15 reports that setpriority is prohibited by the execution environment; no load governor or other job is altered.

## Step 3 — line audit of the proof

Line numbers refer to the unmodified PROOF_UNIFORM.md.

- Lines 58–59, threshold: CORRECT with integer rounding of the transient indices and the convention beta/(16M)=infinity when M=0 (or choose a larger positive M). H gives a uniform positive lower bound on delta_* and hence a uniform upper bound on l_1.
- Step 0(a), lines 62–63: CORRECT. For c<0, c times the total odd mass is at least c(1-a0). Before entry into c>=0, delta contracts by at least 1-a_-. Round the displayed step bound upwards.
- Step 0(b), line 64: CORRECT. The supporting tangent at 1 is 1-chi(1-c)>c. Strict interior invariance follows also from the positive nonconstant Hermite mass.
- Step 0(c), (2), lines 65–71: CORRECT. Taylor's integral remainder has the stated sign. The omitted positive eps delta in f(c)-c only helps. Monotonicity of f(c)-c extends the local improvement to the rest of [0,1-delta_*].
- Step 0(d), lines 72–74: CORRECT. For r in [0,1], f(r)<=a0+(1-a0)r. This controls both endpoints, including negative initial correlations, and bounds v_{l_1} by a constant times 1/eta. Replace the family-dependent l_1 by a common integer upper bound if desired.
- Step 1, (3), lines 76–85: CORRECT. Explicitly rho=-r/(chi^2 delta^2)+(v/chi)x^2/(1-x). Its negative part is at most 4M delta; all the other terms are O(delta). The proposed V_l solves V_{l+1}=V_l/chi+beta/(2chi^2) exactly.
- Lines 87–92, Lemma A: CORRECT. After shifting j-l_1, the weighted harmonic sum is bounded both by 1+log l and by 1+log(1/eps). Divide by V_l and use (1-chi^l)/eps>=N_l/4. The initial term is O(chi^{-l}/eta); no hidden exp(1/eps) occurs.
- Lines 94–97, (4): CORRECT. Write K=1/eta and R=1/eps. Below R, integrate (K+1+log x)/x^2: its tail at j is (K+2+log j)/j. Above R, the sum is at most C eps(K+1+log R)chi^{max(j,R)}, which is O(E_j). Choose l_2 large first and eps_0 small second. Then N_l>=min(l_2,1/eps_0) makes every required E_l small. Constants after this choice may depend on eta through l_2.
- Step 2, (5), lines 99–104: CORRECT. s_l T_l <= C delta_l^2 N_l <= C chi^{2l}/N_l and q delta_{l+1}<=C chi^l/N_l. Division by the main source 2q chi^{l+1} is uniform because q and chi are bounded below.
- Step 3, logarithm, lines 106–109: CORRECT. A_i is positive and bounded below by a fixed fraction of chi after l_2. The square in the logarithmic Taylor error is controlled by chi^i E_i/N_i because E_i>=1/N_i.
- Step 3, sum/integral comparison, lines 111–114: CORRECT, but one suppressed term deserves an explicit calculation. The factor eps/h differs from one by O(eps). Its error is bounded by C eps log[1/(1-chi^{j+1})]. If j<=1/eps, this is O(eps log(C/(eps j)))=O(1/j), using x log(C/x)=O(1) on (0,1]. If j>=1/eps it is O(eps chi^j)=O(1/N_j). The monotone Riemann-sum error is at most h psi((j+1)h)=O(1/N_j). Thus the displayed uniform error is valid even across depth 1/eps.
- Product (6), lines 116–118: CORRECT. Summing logarithmic errors uses (4); exponentiating an O(E_j) error is uniform after the choice of l_2.
- Step 4, lines 120–122: CORRECT. Its initial P has j=l_2-1, just outside the printed range of (6), but the identical product proof applies because its first index is i=l_2. This is an indexing omission, not a new estimate.
- Lines 124–126, weighted sum: CORRECT. For S_L restrict to j>=L/2 and use N_j>=N_L/2. For the error sum use (1-chi^j)^2 E_j <= C eps^2 N_j(K+1+log N_j), then N_j<=N_L. Replacing j by j+1 in the weight costs at most a constant factor.
- Lines 126–128, omitted terms and initial term: CORRECT with constants allowed to depend on l_2 and hence eta. Each contribution divided by F_L is bounded by C l_2^3/(N_L^2 L). Taking eps_0<=1/l_2 and L>=l_2 makes this <=C l_2/N_L. For L<l_2, PSD gives D_L<=2qL and F_L>=2q chi^L, uniformly on this finite range. This completes the main theorem; no substantive gap found in Steps 0–4.
- Line 130: CORRECT; the limiting Riemann sum will be recomputed next.

Remarks are weaker than the main proof. Remark 1 correctly identifies nonuniformity as delta_1 approaches zero, but does not describe the other endpoint: even activations also lose universality when delta_1 approaches 2 (at delta_1=2 they can give D_l=0 from l=2 onward). H and Step 0(d) correctly exclude this problem.

Remark 2, line 137: WRONG as written under H. C^3 supplies rho=(beta^2/(4chi^3)-f'''(1)/(6chi^2))delta+o(delta), not the claimed O(delta^2) remainder. A finite uniformly bounded fourth Gaussian derivative moment would justify the stronger remainder. Also the coefficient cancels at beta^2/4=chi f'''(1)/6, not at the displayed equality except at chi=1. Necessity of a logarithm requires a limiting nonzero coefficient and a propagated NTK asymptotic, rather than this sentence alone.

The logarithm nevertheless cannot be removed in general. Take phi(u)=u^2, sb2=b>0, q=4b/(1+3eps), sw2=chi/(4q). Then f(c)=1-chi/2+(chi/2)c^2, beta=chi and f'''=0, so H holds. In the critical limit, delta_{l+1}=delta_l-delta_l^2/2, giving delta_l=2/l-2 log(l)/l^2+O(l^{-2}); substituting into (1) gives D_l=(2q/3)l-(q/3)log l+O(1), whereas the critical limit of F_l is (2q/3)l+q+q/(3l). Thus the relative error has leading term -(log l)/(2l). Continuity in eps at each finite l rules out a general uniform O(1/N_l) improvement.

Remark 3: CORRECT as an implication of the theorem when the cited fixed-eps coefficient exists; the independent proof does not need the heuristic note. Remark 4: CORRECT for bounded changes to the initial NTK with the same fixed-point correlation dynamics; it is not a precise claim about arbitrary network conventions.

## Step 4 — F_L and the limiting function

CORRECT for all three stated regimes. Directly sum 1-2chi^j+chi^{2j} to recover the displayed S_L. If eps L=o(1), (1-chi^j)=eps j[1+O(eps L)] uniformly for j<=L, and
F_L=q (L+1)(2L+1)/(3L) [1+O(eps L)]. This is the stated (2q/3)L[1+O(eps L)+O(1/L)].

For eps L->t>0, eps S_L -> I(t)=integral_0^t(1-exp(-s))^2 ds=t-2(1-exp(-t))+(1-exp(-2t))/2. Thus eps F_L/q ->2 exp(-t)I(t)/(1-exp(-t))^2, exactly the stated g(t). Integer rounding L=floor(t/eps) makes no difference. For eps L->infinity, S_L=L+O(1/eps) and (1-chi^L)^{-2}=1+O(chi^L), with chi^L<=exp(-eps L)=O(1/(eps L)). This gives 2q L chi^L[1+O(1/(eps L))]. One must retain chi^L here; replacing it uniformly by exp(-eps L) at arbitrarily large L would be wrong.

Expanding the integral gives I(t)=t^3/3-t^4/4+O(t^5), hence g(t)=2t/3-t^2/2+O(t^3). Consequently (1-exp(-t))/g(t)->3/2, and n(1-exp(-t))/g(t)-(n-1)->(n+2)/2. These limits concern fixed n>=2. For n=1 the actual condition number is 1, not 3/2, because there is no transverse eigenvalue.

## Step 5 — spectral corollary

The matrix decomposition and entrywise bound (line 49): CORRECT. E_ab=F_L-D_L for a!=b. Its symmetric operator norm is bounded by the maximum absolute row sum, so ||E||_2 <= (n-1) C F_L r_L, r_L=(1+log N_L)/N_L. Using n is valid, though n-1 is sharper. This dimension factor cannot in general be dropped from an entrywise-only argument (all equal off-diagonal errors attain it).

Lines 50–52: WRONG as a depth-uniform corollary. At L=1, log N_L=0, so the printed eigenvalue and condition-number errors vanish. Choose n=2, c_1=0 and any member of the explicit sine family, say eps=0.01. The true matrix is q I, both eigenvalues q, condition number 1. But F_1=2q chi=1.98q; the corollary predicts eigenvalues 1.98q and 0.02q, calls the latter the top eigenvalue, and predicts condition number 1/chi-1=0.010101..., below 1. The pair is realizable on the fixed-point input sphere: the raw input cosine is -sb2/(q-sb2), which lies in (-1,0).

Replacing log N by 1+log N alone does not justify naming the model's eigenvalue top or dividing by the smallest actual eigenvalue. The model B=F I+(T-F)11^T has transverse eigenvalue F and parallel eigenvalue lambda_parallel=nT-(n-1)F. The parallel eigenvalue is largest only when T>=F. Weyl always compares the SORTED eigenvalues of B and Theta. At shallow depth T-F can be negative and lambda_parallel can even be negative for larger n.

A correct version: for n>=2, in the regime of sufficiently large N_L (depending on H and eta) and n C r_L sufficiently small, T>F, the n-1 lower eigenvalues are F[1+O(n r_L)], the largest is lambda_parallel+O(n F r_L), and
cond(Theta)=[nT/F-(n-1)] [1+O(n r_L)]. The condition n C r_L<1 is needed to keep the denominator bounded away from zero. T/F tends uniformly to a value at least 3/2 in the large-N asymptotic regimes; thus ordering is secure there. An unconditional finite-depth statement should instead give sorted Weyl intervals and require a positive lower interval before forming a condition-number bound.

Line 54: CORRECT as an eps->0 limit with fixed t>0, fixed n>=2 and fixed eta. It is not an equality at finite eps under the mere substitution L=t/eps. The t->0 condition-number limit from Step 4 is correct in that asymptotic interpretation.

## Step 6 — numerical check, first completed run

Wrote parameters.py and referee_check.py independently in this folder. The specified Python interpreter ran tanh at eps=0.1,0.01,0.001,0.0001, four initial deficits 1.5,1,0.5,0.1, through ceil(20/eps). The longest case (200000 layers for all four pairs) took 1.70 seconds. Results are saved incrementally as JSON lines in check_tanh.jsonl. The four scaled maxima at eps=0.0001 are 2.474945, 2.086412, 1.223958, 4.437979.

The implementation iterates both the direct off-diagonal Theta recursion and the algebraically equivalent deficit recursion (1). The latter supplies the reported numbers. Tanh's exact Gaussian Hermite series is evaluated as a degree-192 polynomial, with a 12-term deficit Taylor polynomial below delta=0.001. Its positive-coefficient Taylor remainder bound is <=3.1e-38 for the map and <=4.1e-34 for the derivative in these runs (apart from floating-point/quadrature error). The computed Hermite mass and slope differ from their exact identities by <=3e-14; endpoint/slope identities are explicitly restored to that tolerance, preventing an additive rounding floor in delta. Quadrature order and degree reruns, plus direct two-dimensional quadrature comparisons, remain to be done before accepting the numerical verdict.

## Step 6 — completed verdict and numerical table

CORRECT as a numerical consistency check: the scaled error looks bounded on the tested range. All runs iterate the discrete correlation and NTK recursions through L=ceil(20/eps). The maximum across both activations and all tested pairs/depths is 7.514627. This does not prove the theorem, nor test arbitrarily large depth.

Each entry below is max_{1<=L<=ceil(20/eps)} |D_L/F_L-1| N_L/(1+log N_L), with sb2=0.05.

| activation | eps | delta1=1.5 | delta1=1 | delta1=0.5 | delta1=0.1 |
|---|---:|---:|---:|---:|---:|
| tanh | 0.1 | 1.303845 | 0.444444 | 1.351109 | 2.597171 |
| tanh | 0.01 | 1.648839 | 0.922904 | 0.839971 | 6.707536 |
| tanh | 0.001 | 2.171279 | 1.665197 | 0.802628 | 6.227301 |
| tanh | 0.0001 | 2.474945 | 2.086412 | 1.223958 | 4.437979 |
| sin | 0.1 | 1.410758 | 0.497902 | 1.507849 | 2.654628 |
| sin | 0.01 | 1.093188 | 0.494949 | 1.193424 | 7.286567 |
| sin | 0.001 | 1.207693 | 0.727898 | 0.793290 | 7.514627 |
| sin | 0.0001 | 1.294552 | 0.922523 | 0.790018 | 5.762137 |

Commands (each is a separate process, one thread):

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation tanh > check_tanh.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation sin > check_sin.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation tanh --eps 0.01 0.0001 --order 768 --degree 256 > check_tanh_refined.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 validate_numerics.py > validation.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 validate_numerics.py --quadrature-only > quadrature_validation.jsonl
```

Quadrature checks: parameters.out compares GH orders 256,512,768; q and sw2 agree within 4e-14. Increasing tanh from GH512/degree192 to GH768/degree256 changes scaled maxima by <=2.35e-8 (eps=1e-4) and <=2.12e-10 (eps=0.01). Direct two-dimensional GH128/256/512 at c=-0.5,0,0.5,0.99,0.9999 agrees with the Hermite map within 2.4e-14 and its derivative within 9.4e-15. The first direct-quadrature run raised floating-point status warnings inside the system matrix multiplication despite finite bounded outputs; reran using explicit elementwise weighted sums and finite-value assertions, saved as quadrature_validation.jsonl. These are numerical convergence checks, not rigorous infinite-tail quadrature certificates.

Sine uses its analytic Gaussian map after GH parameter fitting, evaluated with sinh difference identities. A separate 50-digit mpmath run for eps=1e-4, delta1=1, through 200000 layers gives maximum 0.9225232807044821 at L=10000 and t=20 error 0.000864799005260079. Double precision differs by less than 4e-10 in the scaled maximum and 4e-12 in the final relative error. Final delta is 1.4875008498633e-12, so this specifically checks the regime where direct subtraction of correlations is unsafe. The 50-digit validation used 87.2 MB peak RSS and 9.92 seconds; ordinary runs used smaller arrays and <=2 seconds per four-pair parameter case. Recursion and validation processes have a 280-second alarm; the parameter-only check completed in under a second.

## Step 7 — novelty, memory only

UNCHECKED, not established. From memory I know the critical-depth NTK asymptotics and the ordered/chaotic phase distinction associated with Hayou–Doucet–Rousseau and Xiao–Pennington–Schoenholz, and work on finite-width/conditioning questions associated with Seleznova–Kutyniok. I do not confidently recall an exact statement of this g(t), this discrete F_L, or this depth-uniform relative error in that literature or later papers. That is not evidence of novelty. I did not search, browse, read the alleged literature files, or treat the heuristic note's literature survey as independently verified. The main proof does not rely on those novelty claims.

## Final audit before report

Rechecked the load-bearing counterexample a second way: at n=2,L=1,c1=0 the actual trace/determinant are 2q and q^2. The corollary's two predicted eigenvalues have the same trace but determinant 4q^2 chi(1-chi), which is unequal to q^2 for chi>1/2. Its proposed condition number is below one. This is a literal counterexample, not merely a missing big-O smallness assumption.

A concrete regularity counterexample to Remark 2 is phi(u)=|u|^(13/4). It is C^3 with polynomially bounded derivatives, but its fourth derivative has a non-square-integrable singularity at zero. For general p=13/4 put r=(2p-1)/p^2, q=sb2/(1-chi r), sw2=chi/[p^2 q^(p-1) E|Z|^(2p-2)]. This gives a nondegenerate H family with chi approaching one. Gaussian Hermite coefficients have finite third factorial moment but infinite fourth factorial moment. Positivity then makes the fourth Taylor remainder divided by delta^4 unbounded. Consequently the corresponding rho remainder after its linear term is not O(delta^2), as claimed in the note. The weaker o(delta) is valid and sufficient for the main theorem.

Numerical validation scripts include all computations used in the report. No source document was edited. Overall verdict will be WRONG for the note as written, while the main uniform-deficit theorem is supported by the audited proof. A corrected asymptotic corollary and a weakened/strengthened-regularity Remark 2 would remove the identified mathematical defects. Novelty remains unverified.

## Completion

REPORT.md is complete: verdict table, independent derivations, explicit H family, spectral counterexample, corrected scope, numerical tables and reproducible commands, limitations, and memory-only novelty assessment. Re-executed the final validation script after replacing the matrix multiplication with explicit sums; it completed without warnings and reproduced the 50-digit result. All artifacts are confined to this folder. Task: “You are refereeing a mathematical note” — 11 November 2026, 07:23 +04 recorded start; request timestamp unavailable.

Final validation resource measurement: 12.98 seconds, 86.8 MB peak RSS. REPORT.md now records that final run rather than the preliminary timing.
