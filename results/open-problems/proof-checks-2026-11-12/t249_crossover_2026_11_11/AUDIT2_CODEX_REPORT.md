# Independent referee report

Overall verdict: **WRONG**.

The main uniform estimate for D_L is supported by the proof: I found no substantive gap in Steps 0–4. The note as a whole is wrong because its spectral corollary is false at allowed depths, with a two-input counterexample. Remark 2 also claims more regularity than (H) supplies. These defects can be repaired without changing the main theorem or g(t).

I read both documents, derived the recursions independently, and wrote all numerical code in this folder. I used no browsing, external code, agents, or writes outside this folder. Detailed calculations and intermediate verdicts are in LOG.md. Line numbers below refer to the original PROOF_UNIFORM.md.

## Verdict table

| Statement or step | Verdict | Reason |
|---|---|---|
| Correlation map, lines 7–15 | CORRECT | The fixed-point variance normalizes the covariance map; Gaussian differentiation gives the three endpoint derivatives. |
| Hermite facts, lines 27–28 | CORRECT | Squared orthonormal Hermite coefficients are nonnegative; their mass is one by the fixed-point equation. |
| NTK recursion and diagonal, lines 17–18 | CORRECT | With the specified initialization, T_{l+1}=q*+chi T_l and T_1=q*. |
| Deficit recursion (1) | CORRECT | Direct subtraction gives f'(c_l)D_l+q*delta_{l+1}+(chi-f'(c_l))T_l. |
| Hypotheses (H) | CORRECT | A fixed-bias sine family satisfies them with explicit bounds below. |
| Continuity parenthesis in (H) | GAP | Compact parameters alone do not guarantee existence of a finite nondegenerate limiting critical fixed point; that condition is needed for the proposed continuity argument. |
| Choice of delta_* and transient indices | CORRECT | H supplies a uniform positive threshold; round indices to integers and interpret division by M=0 as infinity or enlarge M. |
| Step 0(a), negative initial correlation | CORRECT | f(c)>=a0+(1-a0)c while c<0, giving a uniformly bounded entry time. |
| Step 0(b), invariance | CORRECT | Convexity and the tangent at 1 give f(c)>c for c<1 on [0,1). |
| Step 0(c), Taylor formula (2) | CORRECT | The cubic remainder has the asserted positive sign and uniform bound. |
| Step 0(c), entry into the local regime | CORRECT | Monotonicity of f(c)-c extends the local lower bound to the remaining compact interval. |
| Step 0(d), exclusion of both endpoints | CORRECT | 1-|f(c)|>=(1-a0)(1-|c|), so the finite transient cannot erase the eta separation. |
| Step 1, inverse recurrence (3) | CORRECT | Its remainder is O(delta_l) with negative part at most 4M delta_l. |
| Step 1, solution for v_l-V_l | CORRECT | V_l solves the affine inverse recurrence exactly. |
| Lemma A | CORRECT | The weighted harmonic sum is O(1+log min(l,1/eps)); division by V_l gives the asserted relative error. |
| Choice of l_2 and eps_0 | CORRECT | Choose l_2 first, then decrease eps_0; both depend only on the permitted bounds and eta. |
| Tail bound (4) | CORRECT | Integrate (K+1+log i)/i^2 below 1/eps and use a geometric tail above it. |
| Step 2, source formula (5) | CORRECT | The main source is exactly 2q*chi^{l+1}/(1+theta_l); other sources are O(chi^l/N_l). |
| Step 3, log A_i expansion | CORRECT | Smallness of E_i gives a positive A_i and controls the quadratic logarithmic remainder. |
| Step 3, sum/integral comparison | CORRECT | The suppressed eps/h correction is O(1/N_j); its verification is given below. |
| Product formula (6) | CORRECT | Bound (4) controls accumulated logarithmic errors uniformly in final depth. |
| Step 4, initial product index | CORRECT | The printed range of (6) omits j=l_2-1, but its same proof applies since every product index is still >=l_2. |
| Step 4, weighted source sum | CORRECT | S_L is bounded below by c eps^2 N_L^2 L and the error numerator above by C eps^2(K+Lambda_L)N_L L. |
| Step 4, omitted and initial terms | CORRECT | Their relative size is at most C l_2^3/(N_L^2 L), absorbed with constants depending on eta. |
| Finite depths L<l_2 | CORRECT | PSD bounds D_L<=2q*L; F_L is uniformly bounded below on this finite range. |
| Main uniform-deficit theorem | CORRECT | The audited estimates close with the stated dependence on eta and H. |
| Closed form of S_L | CORRECT | It is the sum of three finite geometric series. |
| Three regimes of F_L | CORRECT | Direct expansion and a Riemann sum give the stated formulas. |
| g(t) and its small-t limit | CORRECT | g(t)=2t/3-t^2/2+O(t^3). |
| Matrix decomposition and entrywise error | CORRECT | E_ab=F_L-D_L off the diagonal. |
| Operator norm factor n | CORRECT | The sharper bound is (n-1) times the entrywise bound; order n is unavoidable from entrywise control alone. |
| Claimed ordered eigenvalue formulas, line 50 | WRONG | At L=1 the error vanishes and the predicted eigenvalues are false; the parallel model eigenvalue need not be largest. |
| Depth-uniform condition number, line 52 | WRONG | The same allowed example predicts a condition number below one; a positive denominator and small relative perturbation must be assumed. |
| Limiting condition number, line 54 | CORRECT | For fixed n>=2 and t>0, it is the eps->0 limit; its t->0 limit is (n+2)/2. |
| Remark 1, initial-angle dependence | CORRECT | It identifies the small-delta obstruction; the upper endpoint also matters for even activations. |
| Remark 2, remainder and cancellation | WRONG | H gives o(delta_l), not O(delta_l^2), after the linear rho term; exact finite-eps cancellation includes a factor chi. |
| Need for a logarithm in general | CORRECT | The quadratic activation gives relative error asymptotic to -(log L)/(2L) in the critical limit. |
| Remark 3, ordered-phase coefficient | CORRECT | Conditional on existence of the quoted fixed-eps asymptotic, it follows from the theorem; the heuristic derivation is not needed. |
| Remark 4, initialization conventions | GAP | Valid for bounded changes to the initial NTK with the same correlation dynamics; arbitrary “other conventions” are not specified. |
| Original numerical evidence | GAP | Its files are absent here and its excluded rounding-floor row was not validated there; independent replacement checks are supplied below. |

## Setting and a nonempty hypothesis family

If phi(sqrt(q*)Z)=sum b_k H_k(Z) in orthonormal Gaussian Hermites, then a_0=(sw2 b_0^2+sb2)/q* and a_k=sw2 b_k^2/q* for k>=1. Parseval and the variance fixed point give sum a_k=1. The assumed Gaussian square-integrability of the first three derivatives gives the stated chi, beta, and third derivative identities.

Subtracting the NTK recursion from T_{l+1}=q*+chi T_l gives, without approximation,

```
D_{l+1} = q*(1-c_{l+1}) + chi T_l - f'(c_l)(T_l-D_l)
        = f'(c_l)D_l + q*delta_{l+1} + (chi-f'(c_l))T_l.
```

For an explicit family take phi(u)=sin u, sb2=0.05 and 0<eps<=0.01. Let q solve

```
q = (1-eps)tanh q + 0.05,
sw2 = 2(1-eps)/(1+exp(-2q)) = q+0.95-eps.
```

The equation has one positive root because its left-minus-right derivative is positive. Here

```
f(c) = [sw2 exp(-q)sinh(qc)+0.05]/q,
beta = q(q-0.05),     f'''(1)=(1-eps)q^2,     a0=0.05/q.
```

Conservative bounds are 0.53<q<0.56, 1.47<sw2<1.51, 0.25<beta<0.29, M=0.06, a_-=0.089 and gamma=0.90. All inverse bounds in H follow. At eps=0.01 the quadrature solution is q=0.532160691401069, sw2=1.47216069140107. At eps=0.0001 it is q=0.551870927192586, sw2=1.50177092719259.

No extra smoothness is needed by the main proof. A common integer transient bound, and constants depending on eta after the choice of l_2, should be stated explicitly. Compactness alone is not a replacement for the explicit nondegeneracy bounds in H.

## The delicate uniform estimates and the logarithm

The inverse-gap error accumulates as sum chi^i/i. Bounding it both by the finite harmonic sum and by -log eps gives 1+log N_l. The estimate never assumes l is on only one side of 1/eps.

For (4), put K=1/eta and R=1/eps. Below R the relevant integral is

```
integral_j^infinity (K+1+log x)/x^2 dx = (K+2+log j)/j.
```

Above R, E_i is constant and the geometric tail is bounded by C eps(K+1+log R)chi^{max(j,R)}. Both pieces are O(E_j).

In Step 3, h=-log chi satisfies eps/h=1+O(eps). The monotone sum/integral error is O(h psi((j+1)h))=O(1/N_j). The additional factor eps/h costs at most

```
C eps log[1/(1-chi^{j+1})].
```

For j<=R this is O(eps log(C/(eps j)))=O(1/j); for j>=R it is O(eps chi^j)=O(1/N_j). Thus the displayed product approximation survives the crossover uniformly, including arbitrarily large final L.

The logarithm is necessary for some activations. With phi(u)=u^2, sb2=b>0, q=4b/(1+3eps), sw2=chi/(4q), one has f(c)=1-chi/2+(chi/2)c^2. In the critical limit,

```
delta_{l+1}=delta_l-delta_l^2/2,
delta_l=2/l-2 log(l)/l^2+O(l^-2),
D_l=(2q/3)l-(q/3)log l+O(1),
F_l=(2q/3)l+q+q/(3l).
```

The first expansion follows by summing the inverse-gap recurrence; substitution into (1) fixes the logarithmic coefficient of D. Hence the relative error is -(log l)/(2l)+O(1/l). Continuity as eps decreases at each fixed l rules out a general uniform O(1/N_l) bound.

Remark 2 should instead state

```
rho_l = [beta^2/(4chi^3)-f'''(1)/(6chi^2)]delta_l + o(delta_l).
```

Its coefficient vanishes at beta^2/4=chi f'''(1)/6. An O(delta_l^2) remainder needs additional regularity, for example a bounded fourth Gaussian derivative moment. This distinction is real: phi(u)=|u|^(13/4) is C^3 with polynomially bounded derivatives but its fourth derivative is not Gaussian-square-integrable. For p=13/4, set r=(2p-1)/p^2, q=sb2/(1-chi r), and sw2=chi/[p^2 q^(p-1) E|Z|^(2p-2)]. This is an H family. Its fourth Hermite factorial moment is infinite, so positivity makes the fourth Taylor remainder divided by delta^4 unbounded; the stated O(delta_l^2) rho remainder fails.

Negative correlations introduce no missing case in the theorem: Step 0 controls both endpoints. The upper exclusion delta_1<=2-eta is essential. For an even activation and c_1=-1 the two representations merge, and D_l can be zero from l=2 onward. The heuristic's unqualified phrase “any n distinct inputs” must therefore not replace the main theorem's pair-separation hypothesis.

## Regimes and the spectral counterexample

For eps L=o(1), sum (1-chi^j)^2=eps^2 sum j^2[1+O(eps L)], giving

```
F_L = q*(L+1)(2L+1)/(3L) [1+O(eps L)].
```

For eps L->t>0,

```
eps S_L -> I(t)=t-2(1-exp(-t))+(1-exp(-2t))/2,
eps F_L/q* -> 2 exp(-t) I(t)/(1-exp(-t))^2 = g(t).
```

For eps L->infinity, S_L=L+O(1/eps) and (1-chi^L)^-2=1+O(chi^L), yielding the stated ordered-phase formula. Retain chi^L in this regime: exp(-eps L) is not a uniform replacement at arbitrarily large L.

The corollary's decomposition is correct. With r_L=(1+log N_L)/N_L,

```
||E||_2 <= (n-1) C F_L r_L.
```

The comparison matrix has eigenvalues F_L with multiplicity n-1 and lambda_parallel=nT_L-(n-1)F_L. Weyl applies to their sorted order; lambda_parallel is largest only if T_L>=F_L.

A counterexample to the corollary as printed is n=2, L=1, c_1=0, eps=0.01 in the sine family above. The actual matrix is q*I and its condition number is 1. Since N_1=1, every printed O(n log N_1/N_1) error is zero. The corollary instead gives eigenvalues 1.98q* and 0.02q*, calls the latter the top eigenvalue, and gives condition number 1/chi-1=0.010101.... This pair is realizable on the input sphere: its raw input cosine is -sb2/(q*-sb2), between -1 and zero. Independently, the predicted determinant is 4(q*)^2 chi(1-chi), whereas the actual determinant is (q*)^2.

A sufficient corrected corollary assumes n>=2, sufficiently large N_L, and n C r_L sufficiently small. Then T_L>F_L, the lower n-1 eigenvalues are F_L[1+O(n r_L)], the largest is lambda_parallel+O(n F_L r_L), and

```
cond(Theta_L) = [n T_L/F_L-(n-1)] [1+O(n r_L)].
```

At general finite depths one should give sorted Weyl intervals instead, and form a condition-number bound only when the smallest lower interval is positive. Replacing log N_L by 1+log N_L alone does not supply that positivity or fix eigenvalue ordering.

For fixed t>0 and fixed n>=2 the limiting condition-number formula is correct. Since g(t)=2t/3-t^2/2+O(t^3), (1-exp(-t))/g(t)->3/2, giving (n+2)/2. For n=1 the condition number is always 1; there is no transverse eigenvalue.

## Independent numerical check

The specified interpreter has numpy 2.2.3, scipy 1.15.2 and mpmath 1.3.0. I fixed sb2=0.05 and solved the variance/slope equations by Gauss–Hermite quadrature and a scalar root solve. Both c_l and Theta_l are iterated in the discrete recursion; the reported D uses the equivalent deficit recurrence to avoid subtraction of nearly equal diagonal/off-diagonal values. No continuum dynamics are used.

| activation | eps | q* | sw2 |
|---|---:|---:|---:|
| tanh | 0.1 | 0.346039478292 | 1.362885964365 |
| tanh | 0.01 | 0.541950381562 | 1.714751881819 |
| tanh | 0.001 | 0.567179259821 | 1.756270874339 |
| tanh | 0.0001 | 0.569760431159 | 1.760485631207 |
| sin | 0.1 | 0.363327269698 | 1.213327269698 |
| sin | 0.01 | 0.532160691401 | 1.472160691401 |
| sin | 0.001 | 0.550078356673 | 1.499078356673 |
| sin | 0.0001 | 0.551870927193 | 1.501770927193 |

The entries are max over 1<=L<=ceil(20/eps) of |D_L/F_L-1| N_L/(1+log N_L). The initial correlations are respectively -0.5, 0, 0.5, 0.9.

| activation | eps | delta_1=1.5 | delta_1=1 | delta_1=0.5 | delta_1=0.1 |
|---|---:|---:|---:|---:|---:|
| tanh | 0.1 | 1.303845 | 0.444444 | 1.351109 | 2.597171 |
| tanh | 0.01 | 1.648839 | 0.922904 | 0.839971 | 6.707536 |
| tanh | 0.001 | 2.171279 | 1.665197 | 0.802628 | 6.227301 |
| tanh | 0.0001 | 2.474945 | 2.086412 | 1.223958 | 4.437979 |
| sin | 0.1 | 1.410758 | 0.497902 | 1.507849 | 2.654628 |
| sin | 0.01 | 1.093188 | 0.494949 | 1.193424 | 7.286567 |
| sin | 0.001 | 1.207693 | 0.727898 | 0.793290 | 7.514627 |
| sin | 0.0001 | 1.294552 | 0.922523 | 0.790018 | 5.762137 |

These values look bounded on this range. Some columns increase moderately, while the largest-error column decreases at the smallest eps. The global maximum is 7.514627. This is consistency evidence, not a proof of boundedness as eps tends to zero.

Commands producing the table, run separately:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation tanh > check_tanh.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation sin > check_sin.jsonl
```

The numerical approximation and validation are explicit:

- parameters.py compares GH orders 256, 512 and 768; the solved q and sw2 agree within 4e-14.
- Tanh uses a Gaussian Hermite expansion through degree 192 at GH512. Its endpoint mass/slope identities are restored by corrections of at most 3e-14. Below deficit 0.001, a 12-term Taylor evaluation avoids cancellation; the finite-polynomial map remainder is bounded by 3.1e-38, and the derivative remainder by 4.1e-34. These last bounds do not certify the infinite Hermite tail.
- Increasing to GH768 and degree 256 changes the scaled maxima by at most 2.35e-8 at eps=1e-4 and 2.12e-10 at eps=0.01. Direct two-dimensional GH at orders 128, 256, 512 and five correlations agrees with the Hermite map to 2.4e-14 and its derivative to 9.4e-15. This checks the computational representation independently.
- Sine's Gaussian map is also available analytically and is evaluated using stable sinh difference identities after quadrature parameter fitting. A separate 50-digit run at eps=1e-4, delta_1=1, through 200000 layers gives scaled maximum 0.9225232807044821 and final relative error 0.000864799005260079. Double precision differs by 3.90e-11 and 3.10e-12 respectively. The final deficit is 1.4875008498633e-12, so this check reaches the rounding-sensitive regime.

Validation commands:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 parameters.py > parameters.out
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee_check.py --activation tanh --eps 0.01 0.0001 --order 768 --degree 256 > check_tanh_refined.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 validate_numerics.py > validation.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 validate_numerics.py --quadrature-only > quadrature_validation.jsonl
```

All computation was single-thread CPU work. Each recursion process has a 280-second alarm. The final 50-digit validation took 13 seconds and 86.8 MB peak memory; ordinary four-pair parameter cases took under two seconds with smaller arrays. The system rejected the attempted nice setting; no governor or other job was changed. An initial matrix-multiplication validation emitted floating-point status warnings; the direct quadrature was repeated with explicit weighted sums and finite-value assertions. The saved quadrature_validation.jsonl contains that repeat, and the final validation.jsonl also uses the corrected implementation.

## Limits of this review and novelty

I did not verify the external literature survey, the absent original numerical scripts/outputs, or the cited fixed-eps ordered-phase theorem. The uniform proof does not depend on the heuristic note's unverified numerical or literature claims. Quadrature accuracy is checked by numerical convergence and an independent representation, not a rigorous infinite-tail error certificate. The numerical tests stop at 20/eps; arbitrary larger depths are covered only by the proof audit. I did not rerun the note's exact excluded tanh row, but the independent stable recursion and high-precision sine run address its stated numerical failure mechanism.

From memory, I know the critical NTK depth asymptotics and the separate ordered/chaotic phase analyses associated with Hayou–Doucet–Rousseau and Xiao–Pennington–Schoenholz, and conditioning/finite-width work associated with Seleznova–Kutyniok. I do not confidently recall this exact g(t), discrete F_L, or uniform error term in those or later papers. I cannot establish novelty from that recollection and make no priority claim.

Task: “You are refereeing a mathematical note” — 11 November 2026, 07:23 +04 start recorded; the incoming request's exact timestamp was not supplied.
