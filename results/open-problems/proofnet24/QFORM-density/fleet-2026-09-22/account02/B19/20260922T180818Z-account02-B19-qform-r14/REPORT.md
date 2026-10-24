SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B19, 2026-09-22T18:08:18Z.
Sub-piece attacked: pay aligned rank-one internal-curvature star banks, then splice that endpoint into the latest completed cross-bank/low-offdiagonal synthesis.

# account02/B19 — curved one-statistic star bank via an arrow-matrix pivot theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control applied:** revision `2026-09-22.10`  
**Run:** `20260922T180818Z-account02-B19-qform-r14`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source-pinned inputs

The owner target remains: for arbitrary independent real coordinates with densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound for the essential supremum of the density of `X^T A X`, or produce a genuine counterexample. No support, moment, log-concavity, diagonal-basis, or post-rotation independence hypothesis is introduced.

The newest **completed** designated-partner result available before publication is account03/B19 run `20260922T172719Z-account03-B19-QFORM-r16`. It proves `QFORM-EXACT-CROSS-RANK-L2-v1`: for disjoint original-coordinate banks with exact cross rank `r>=3`,

`||p_Q||_infinity <= e r/(r-2) Pi_r(C)^(-1/r)`,

with improvements when one or both active banks have exactly `r` physical coordinates. In particular a genuine physical `3 x 3` cross minor `C` gives

`||p_Q||_infinity <= 3 |det C|^(-1/3)`,

and the O0 exact-rank-three cross-bank endpoint is paid. The same partner synthesis retains the preceding r15 theorem `QFORM-LOW-OFFDIAG-ONE-HALF-BARRIER-v1`, so every still-unpaid target matrix satisfies

`s_2(A-diag A)>499/1000`.                                                   (1.1)

The r16 heavy-core splice further reduces O0 heavy-core sizes three and four to a projected-residual determinant/scale branch; O1/O2/O3 and O0 heavy-core size at most two or large-residual-determinant states remain structural debts.

I also use account03/B11 `QFORM-INDEFINITE-BINARY-HALF-POTENTIAL-v1`: for an indefinite binary quadratic with matrix `S`, arbitrary affine terms and independent cap-one variables,

`sup_t E[(t-R)_+^(-1/2)] <= 8 |det S|^(-1/4)`

and likewise after reflection. Together with its dependence-safe Abel square smoothing, a nonzero physical scalar pivot `p` whose Schur complement is indefinite gives

`||p_Q||_infinity <= 8 (|p det M|)^(-1/4)`                                (1.2)

for a physical three-variable matrix `M`.

Finally I consume account02/B04 `QFORM-ONE-CURVED-LEAF-STAR-BANK-v1`, which pays the pure rank-one star bank when the aggregate bank has zero internal quadratic curvature. The theorem below removes that zero-curvature restriction when the internal bank curvature is aligned with the same aggregate statistic.

All live no-go corrections remain in force: no eigen-coordinate independence; no conditional projection-cap surrogate; no fixed good minor/cross minor/triple; no normalized one-pair TT* shortcut; no claim that high offdiagonal spectral mass alone forces a rank-two coordinate cut; no fixed transverse-angle extraction.

## 2. New analytic lemma — every well-conditioned physical arrow is paid

### Theorem 2.1 — `QFORM-ARROW-3VAR-UNIFORM-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one, with arbitrary affine terms allowed. Let the quadratic matrix in these **physical independent variables** be

`M = [[a,b,c],
      [b,lambda,0],
      [c,0,d]]`.

If every eigenvalue of `M` has modulus at least `s>0`, then

`boxed: ||p_Q||_infinity <= 8/s.`                                           (2.1)

The missing `YZ` edge is the only structural hypothesis.

### Proof

Since `M` is symmetric and all eigenvalues have modulus at least `s`,

`||Mv||_2 >= s ||v||_2` for every `v`.                                     (2.2)

Put `r^2=b^2+c^2`. If `r>0`, use the leaf-plane vector

`v=(0,c,-b)/r`.

Then

`Mv=(0,lambda c/r,-d b/r)`,

hence

`lambda^2 c^2+d^2 b^2 >= s^2(b^2+c^2)`.                                   (2.3)

Therefore `max(|lambda|,|d|)>=s`. Choose a leaf coefficient `p` with `|p|>=s` and pivot in that original variable. Its binary Schur complement `S` satisfies

`det S=det M/p !=0`.                                                        (2.4)

If `S` is indefinite, (1.2) gives

`||p_Q||_infinity <=8(|p det M|)^(-1/4)`.                                  (2.5)

If `S` is definite, after affine completion the two-variable residual has density at most

`L=pi/sqrt(|det S|)`                                                        (2.6)

by the physical two-dimensional definite coarea bound. For any probability density bounded by `L`, one-sided inverse-half rearrangement gives

`sup_t int_{r<t}p_R(r)(t-r)^(-1/2)dr <=2sqrt(L)`,                           (2.7)

and similarly on the other side. Dependence-safe Abel smoothing of the pivot square gives

`||p_Q||_infinity <=2sqrt(pi)(|p det M|)^(-1/4)`.                           (2.8)

Since `|p|>=s` and `|det M|` is the product of the three absolute eigenvalues, `|det M|>=s^3`; thus `(|p det M|)^(1/4)>=s`, proving (2.1).

If `r=0`, the matrix is diagonal and every diagonal entry has modulus at least `s`. Two have the same sign. Conditioning on the third variable, the resulting two-dimensional same-sign physical quadratic has density at most `pi/s<8/s`. QED.

No probabilistic rotation is used anywhere in this proof.

## 3. New grouped target branch — aligned rank-one internal curvature

### Theorem 3.1 — `QFORM-ONE-STATISTIC-CURVED-STAR-v1`

Let `X,Y,Z_1,...,Z_m` be independent cap-one variables, let `||u||_2=1`, and put `L=sum_k u_k Z_k`. Consider

`Q=aX^2+2bXY+lambda Y^2+2BXL+theta L^2`                                   (3.1)

with effective three-dimensional matrix

`M_0=[[a,b,B],[b,lambda,0],[B,0,theta]]`.                                  (3.2)

If all three eigenvalues of `M_0` have modulus at least one, then

`boxed: ||p_Q||_infinity <=16.`                                             (3.3)

### Proof

The standard one-dimensional product-projection estimate gives

`||p_L||_infinity <=sqrt(2)`.                                               (3.4)

Set `W=sqrt(2)L`. Then `W` has density at most one and is genuinely independent of `X,Y`, because it is a function of a disjoint original-coordinate bank. In `(X,Y,W)` the quadratic matrix is

`M=S M_0 S`, `S=diag(1,1,1/sqrt(2))`.                                      (3.5)

Hence

`s_min(M)>=s_min(S)^2 s_min(M_0)>=1/2`.                                    (3.6)

The matrix has the arrow form of Theorem 2.1, so (2.1) with `s=1/2` gives (3.3). QED.

Equivalently, an original-coordinate block

`[[a,b,Bu^T],[b,lambda,0],[Bu,0,theta uu^T]]`                              (3.7)

is paid whenever its three nonzero eigenvalues have modulus at least one. A bank rotation may be used only to read its spectrum; the probability proof uses the original product variables through `L=u^T Z`.

This strictly extends account02/B04's pure star-bank endpoint (`theta=0`) to aligned rank-one internal bank curvature.

## 4. Source-valid refutation — no universal transverse angle

A stronger structural shortcut is false. Take a two-coordinate bank, curvature direction `u=e_1`, and center-coupling vector

`c_phi=2(cos(phi)e_1+sin(phi)e_2)`.

At `phi=0` the nonzero effective block

`[[0,2,2],[2,2,0],[2,0,2]]`

has eigenvalues `{4,2,-2}`. In four physical coordinates the perturbation from `phi=0` is a symmetric star edge with operator norm

`||c_phi-c_0||_2=4 sin(phi/2)`.                                             (4.1)

Therefore

`s_3(A_phi)>=2-4 sin(phi/2)`.                                               (4.2)

For every positive `phi` with `sin(phi/2)<=1/4`, the exact owner target still holds, while the angle between coupling and bank-curvature directions equals `phi` and tends to zero. Thus the spectral target cannot force a fixed positive transverse angle.

This is not a QFORM counterexample; it refutes only an angle-extraction shortcut. The correct near-parallel theorem must remain stable as the angle tends to zero, and Theorem 3.1 pays the exact aligned endpoint.

## 5. Conditional end-to-end assembly after applying current partner r16

A compact source-valid proof tree is now:

1. Completed ridge/spectral-window diffuse branches pay their stated regimes.
2. Partner r15/r16 pays the low-offdiagonal regime, so every survivor satisfies (1.1).
3. Third-compound structure reduces the high-offdiagonal region to O0/O1/O2/O3 packets.
4. Partner r16 pays every exact-rank cross bank of rank at least three, in particular O0 exact rank three and every honest physical `3 x 3` cross minor. Its heavy-core factorization/splice pays the O0 finite heavy-core analytic step for core size three or four up to the residual determinant/scale branch.
5. Existing opposite-diagonal, same-sign definite-pair, majority-pivot, rank-two Schur, high-Schur-offdiagonal and grouped hyperbolic/cross-bank theorems pay their quantitative packets.
6. Account02/B04 pays the pure rank-one star bank.
7. **New:** Theorem 3.1 pays the same bank when its internal curvature is rank one and exactly aligned with the center-coupling aggregate.

Thus exact aligned one-statistic curvature and exact-rank cross banks are no longer the synthesis bottleneck.

## 6. First unpaid implication with exact quantifiers

### `QFORM-NEARPARALLEL-BANK-STABILITY-v1`

Prove that there exist universal constants `epsilon_0,c_0>0` and a finite list of already-paid product-preserving packets with the following property. For every dimension `n`, every symmetric target matrix `A` with at least three eigenvalues of modulus at least one, and every surviving high-offdiagonal state satisfying (1.1) after the completed ridge/third-compound reductions, at least one of the following holds:

(a) there is an exact one-statistic aligned curved-star block whose effective three eigenvalues have modulus at least a universal positive scale, so Theorem 3.1 (after scaling) pays it;

(b) there is a genuinely transverse grouped bank with a quantitative two- or three-channel product-preserving resource at least `c_0`, covered by the existing mixed/hyperbolic or partner-r16 exact-cross-rank theorem;

(c) there is an already-paid physical pivot/Schur, same-sign, ridge, majority-pivot, or high-Schur-offdiagonal packet;

(d) in O0, the state descends to the remaining partner-r16 projected-residual determinant/scale branch with core size at most two, with a quantitative parameter suitable for one of (a)-(c).

The conclusion must hold **without** a fixed lower bound on the angle between the rank-one curvature direction and the center-coupling direction, without selecting a reciprocal tiny minor, and without replacing the original product law by a conditional projected-density cap.

A quantitatively equivalent replacement is a direct stability theorem that pays the near-parallel bank uniformly as its angle tends to zero. Theorem 3.1 supplies the exact endpoint to which such an argument must converge.

## 7. Status

**Proved:** `QFORM-ARROW-3VAR-UNIFORM-v1`.  
**Proved:** `QFORM-ONE-STATISTIC-CURVED-STAR-v1`.  
**Refuted candidate shortcut:** universal positive transverse-angle extraction.  
**Current designated partner applied:** account03/B19 r16 exact-cross-rank payment, together with its retained r15 low-offdiagonal reduction.  
**Full conjecture:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** not claimed in the two new branches.  
**Independent end-to-end reviews:** not applicable because this is not a full proof candidate.
