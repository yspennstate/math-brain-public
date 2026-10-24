# account03/B18 r23 — capped-basis high-shear barrier and exact partner splice

Run: `20260923T042706Z-account03-B18-QFORM-r23`

Status: `PROVED_SUPPORTING_TARGET_BRANCH_AND_METHOD_BARRIER / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and control scope

The owner target is unchanged: for arbitrary finite `n`, independent real original-coordinate random variables `X_i` with densities bounded by one, and an arbitrary real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, or post-rotation independence hypothesis is added. Continuity is tracked separately.

This run works only on the live exact-rank-three Schur-isotropic core

`Q=(Y+u X_0)^T D (Y+u X_0),   Y=V^T X_res,   V^T V=I_3,   u^T D u=0`,

which remains one of the structural model packets for the full target. Put `r=||u||`, `n=u/r` when `r>0`, and write the residual physical rows of `V` as `v_j^T`.

The live corrections are respected: no arbitrary-joint coarea theorem, no conditional-cap-as-independence step, no fixed-good-minor implication, no positive conditional projection-height moment, no near-zero-as-zero replacement, and no law-uniform pointwise Fresnel decay is used.

## 2. Primary literature actually transferred

The analytic source theorem used by the partner packets is account01/B18's completed `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, whose primary inputs are:

1. W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159–182, DOI 10.2307/1970980: the sharp Hausdorff–Young inequality.
2. E. Lieb's Gaussian-extremizer theorem for Brascamp–Lieb, in the Gaussian-exhaustion framework treated by J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp–Lieb inequalities: finiteness, structure, and extremals*, arXiv:math/0505065.
3. For product marginals elsewhere in the same splice, Livshyts–Paouris–Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016): if a product density has one-dimensional factors bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`.

The capped-basis theorem is used at its literal hypotheses. If `L` is `3 x N` of rank three, `D` is invertible symmetric, `A=L^T D L`, and `w` is a probability law on nonsingular three-column bases with coordinate marginals `alpha_i<=1/2`, define

`Z_w = exp(H(w)+ sum_S w_S log det(L_S)^2)`.

Then, for independent cap-one original-coordinate inputs,

`||p_(X^T A X)||_infinity <= 3 e (|det D| Z_w)^(-1/3)`,

and the density is continuous. Canonical proof: `yspennstate/math-open-problems@1f269a8ae64baa9401910aec1f14251128537afd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

The designated partner account04/B18 has two completed applications of that source theorem which are used below:

- diffuse Schur-frame addendum at scientific commit `e9eb90e2a7746482fb3ba75bf449b224cbf507ce`: if `0<r<=1` and every residual row obeys `||v_j||^2<=1/2`, then the exact Schur-isotropic core has a continuous density with `||p_Q||_infinity<=3e`;
- mixed-volume Schur theorem, canonical report `yspennstate/math-open-problems@87dbe53e75a736bc87f97e02e40ebf2c3c13b095`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T001857Z-account04-B18-QFORM-r3/REPORT.md`: with `p_j=||v_j||^2` and `q_j=||(I-nn^T)v_j||^2`, if `p_j+q_j<=1` for every residual coordinate, then

`||p_Q||_infinity <= 3e ((1+r^2)/(2r))^(1/3)`

under target normalization, with continuity.

The older account04/B18 zero-pivot `1+2` theorem used in Section 5 is source-pinned at `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`. It requires a genuinely independent scalar and two-dimensional vector; I do not weaken that requirement to a conditional density cap.

## 3. A clean partner splice: all diffuse exact cores up to shear two

### Proposition `QFORM-SCHUR-ISOTROPIC-RLE2-DIFFUSE-CLOSURE-v1`

Assume the exact Schur-isotropic packet above is target-normalized, `0<r<=2`, and

`max_j ||v_j||^2 <= 1/2`.

Then `Q` has a continuous density and

`||p_Q||_infinity <= 3e (5/4)^(1/3) < 8.785`.

### Proof

If `0<r<=1`, the current account04/B18 diffuse-frame theorem applies directly and gives

`||p_Q||_infinity <=3e`.

If `1<=r<=2`, set

`p_j=||v_j||^2`,  `q_j=||(I-nn^T)v_j||^2`.

Since orthogonal projection cannot increase norm,

`0<=q_j<=p_j<=1/2`,

hence `p_j+q_j<=1`. Therefore the completed account04/B18 mixed-volume theorem applies:

`||p_Q||_infinity <=3e ((1+r^2)/(2r))^(1/3)`.

On `[1,2]`, `(1+r^2)/(2r)=(r+r^(-1))/2` is increasing and is at most `5/4`. Thus

`||p_Q||_infinity <=3e(5/4)^(1/3)=8.784541002773...`.

Both source theorems provide continuity. QED.

This closes a concrete implication left implicit across the two partner packets: **within the exact-rank-three Schur-isotropic core, every unpaid case with shear `r<=2` must contain a residual physical row of squared norm strictly greater than `1/2`.** Thus the remaining low/moderate-shear state is genuinely localized, not diffuse.

## 4. Exact entropy-score barrier for the same literature mechanism at high shear

The capped-basis theorem is powerful but has a mathematically exact obstruction when the special shear coordinate becomes dominant. This is not a QFORM counterexample; it is a limitation of this particular Beckner/BL certificate.

Let

`L=[u,V^T]`, `u=rn`, `V^T V=I_3`, `r>=1`.

For every nonsingular physical three-column basis `S`, put

`a_S=det(L_S)^2`.

Partition the bases into:

- `R`: residual triples, not containing the special shear column;
- `H`: bases containing the shear column and two residual columns.

Cauchy–Binet gives exactly

`sum_(S in R) a_S = det(V^T V)=1`.                    (4.1)

For `S={0,j,k}`,

`a_S=r^2 det[n,v_j,v_k]^2`.

Projecting the residual Parseval frame onto `n^perp` gives a rank-two Parseval frame there, hence rank-two Cauchy–Binet gives

`sum_(S in H) a_S = r^2`.                               (4.2)

Now let `w` be **any** probability distribution on nonsingular bases satisfying the capped-basis marginal gate. Let

`theta=sum_(S in H)w_S=alpha_0<=1/2`.

Write the conditional laws of `w` on `R` and `H` as `w_R,w_H`. The Gibbs/log-sum identity gives, for any positive weights `(a_s)`,

`H(p)+sum_s p_s log a_s <= log(sum_s a_s)`.             (4.3)

Splitting entropy across the two banks and using (4.1)–(4.2),

`log Z_w
 = h(theta)
   +(1-theta)[H(w_R)+E_R log a_S]
   +theta[H(w_H)+E_H log a_S]
 <= h(theta)+2theta log r`,                              (4.4)

where `h(theta)=-theta log theta-(1-theta)log(1-theta)`.

For `r>=1`, the right side is increasing on `0<=theta<=1/2`, because

`d/dtheta [h(theta)+2theta log r]
 = log((1-theta)/theta)+2 log r >=0`.

Therefore every capped basis law satisfies the sharp universal score bound

`boxed: Z_w <= 2r`.                                      (4.5)

This proves `QFORM-CAPPED-BASIS-HIGHSHEAR-BARRIER-v1`.

The statement is deliberately narrow: it says the exact capped-basis theorem cannot obtain a determinant-entropy score larger than order `r` in this Schur-isotropic geometry. It does **not** say the quadratic density itself grows with `r`.

## 5. Sharp target-valid witness: the certificate degenerates while account04/B18 stays uniform

The barrier is attained on a completely explicit diffuse target family.

Take six residual rows consisting of two copies of each coordinate axis divided by `sqrt(2)`:

`v_1=v_2=e_1/sqrt(2)`,
`v_3=v_4=e_2/sqrt(2)`,
`v_5=v_6=e_3/sqrt(2)`.

Then `V^T V=I_3` and every residual leverage is exactly `1/2`. Let

`u=r e_1`, `s=sqrt(1+r^2)`,

and

`D_r = [[0,1/s,0],[1/s,0,0],[0,0,1]]`.

Then `u^T D_r u=0`,

`G=LL^T=diag(1+r^2,1,1)`,

and

`G^(1/2) D_r G^(1/2)
 = [[0,1,0],[1,0,0],[0,0,1]]`.

Hence the three nonzero eigenvalues of the physical matrix

`A_r=L^T D_r L`

are exactly

`{-1,1,1}`                                                     (5.1)

for every `r>0`. Thus this family satisfies the owner's exact spectral target at every shear scale. Also

`|det D_r|=1/(1+r^2)`.                                      (5.2)

### Exact capped-score optimum

The residual-triple volume law has eight nonzero triples, each determinant square `1/8`, and total score mass one. The shear-pair volume law has four nonzero pairs, each full determinant square `r^2/4`, and total score mass `r^2`.

Put half the basis probability on each normalized volume law. The special-coordinate marginal is `1/2`; each `e_1` residual copy has marginal `1/4`; each `e_2` or `e_3` residual copy has marginal `1/2`. Thus every marginal is at most `1/2`, so this is admissible. Its determinant-entropy score is exactly

`Z_w=2r`.                                                     (5.3)

Together with (4.5), this proves that `2r` is the **optimal capped score** for this family.

Consequently, for every admissible capped-basis law, the numerical certificate supplied by `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1` contains

`|det D_r|Z_w <= 2r/(1+r^2)`,                               (5.4)

so even discarding its factor `B_alpha>=1`, its right-hand side is at least

`3 ((1+r^2)/(2r))^(1/3)`,                                  (5.5)

which diverges like a constant times `r^(1/3)`. Therefore **no choice of capped basis weights inside that exact theorem can by itself produce a shear-uniform QFORM bound on this target family.** This is a proof-method barrier, not a density lower bound.

### Applying the designated account04/B18 theorem instead

The same family has the source separation needed by account03/B18 r22's literal application of the account04/B18 zero-pivot `1+2` theorem: the `e_1` residual bank and the transverse `e_2,e_3` banks use disjoint original coordinates.

Let

`Z_1=<e_1,Y>`, `Z_2=<e_2,Y>`, `Z_3=<e_3,Y>`,
`S=X_0+Z_1/r`.

Then `S` is genuinely independent of `(Z_2,Z_3)`. Since `X_0` has density cap one, convolution gives `||p_S||_infinity<=1`. The two-dimensional product-marginal theorem gives

`||p_(Z_2,Z_3)||_infinity<=2`.

In variables `(S,Z_2,Z_3)`, the active zero-pivot coefficient matrix is

`K_r=diag(r,1,1) D_r diag(r,1,1)`,

so

`|det K_r|=r^2/(1+r^2)`.                                    (5.6)

Applying the completed account04/B18 zero-pivot theorem at these literal independence hypotheses gives

`||p_Q||_infinity
 <=6*2^(2/3)*((1+r^2)/r^2)^(1/3)`.                         (5.7)

For every `r>=1`, `(1+r^2)/r^2<=2`, so

`boxed: ||p_Q||_infinity <=12`,                             (5.8)

with continuity on this branch.

Thus the same exact target family on which the Beckner/BL capped-basis certificate necessarily degenerates is uniformly controlled by a product-separation/zero-pivot mechanism. This is the concrete partner application required by the B18 assignment.

## 6. What is genuinely gained

Two implications are now rigorous.

1. **Diffuse low/moderate shear is closed:** if the exact Schur-isotropic core has `r<=2` and no residual row leverage exceeds `1/2`, its density is continuous and universally bounded by `<8.785`.
2. **Pure capped-basis Fresnel cannot finish high shear:** for every Schur-isotropic core and every capped basis law, `Z_w<=2r`; on an explicit diffuse target-normalized family the optimum is exactly `2r`, causing the capped-basis theorem's certificate to diverge as `r^(1/3)`, while the actual quadratic density is still uniformly bounded (`<=12`) by the account04/B18 zero-pivot splice.

So the next high-value implication is not to optimize the same capped-basis score again. For `r>2`, a successful full proof must exploit additional product provenance before/alongside the Fresnel absolute value: a source-separated/grouped zero-pivot transducer, heavy-row localization, ridge/hub mechanism, or another dependence-safe aggregate argument. In the low/moderate region, only a genuinely heavy residual row remains unpaid.

Arbitrary additional spectrum is still not absorbed by these exact-rank-three statements. Therefore the unrestricted QFORM conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open.

## 7. Quantitative checks

`3e = 8.154845485377...`

`3e(5/4)^(1/3) = 8.784541002773...`

For the witness family, direct multiplication verifies

`G^(1/2)D_rG^(1/2)` has characteristic polynomial `(lambda-1)(lambda^2-1)`, so the nonzero physical spectrum is exactly `{-1,1,1}`.

The score ledger is exact: residual determinant-square mass `1`, shear determinant-square mass `r^2`, capped score optimum `2r`, and partner determinant `|det K_r|=r^2/(1+r^2)`.

No numerical simulation is used as proof.