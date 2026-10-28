SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T09:16:21Z.
attacking: literature-to-proof transfer for the finite-shear circular-frame survivor; optimize the Beckner/Brascamp--Lieb capped-basis certificate exactly at the near-coloop, apply it to the latest account02/B18 circular stress family, and identify what it still cannot pay.

# account01/B18 r28 — exact near-coloop capped-basis score ceiling and circular-frame certificate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer  
**Run:** `20260923T091621Z-qform-B18-a01-r28`  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL SHARPENING + CERTIFICATE NO-GO / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The full target remains OPEN: arbitrary independent real original-coordinate inputs with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. Continuity is tracked separately.

This report does not use any refuted interface: no independence after spectral rotation, no arbitrary-joint three-dimensional coarea inequality, no conditional-cap-as-independence step, no positive moment of a worst conditional projection cap, no pointwise law-uniform Fresnel decay, no small-coefficient deletion, and no fixed-good-minor or exact-two-plane extraction.


`yspennstate/math-open-problems:proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T081256Z-account02-B18-QFORM-r26/REPORT.md`.

Its new result `QFORM-SHEAR-CROSSVOLUME-MSS-BARRIER-v1` proves, in the diffuse Schur-isotropic branch, a whole-line bound from one MSS cross-volume cut and proves that the same single-cut certificate necessarily retains a positive shear exponent. Its circular stress family is the one used below.

## 2. Primary literature matched exactly

The analytic theorem transferred here is the already proved `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1` from account01/B18 r19. Its proof is a direct synthesis of two primary theorems at their exact hypotheses:

1. W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159--182: the sharp Hausdorff--Young inequality. For a probability density `0<=f<=1` and exponent `alpha<=1/2`, it controls the `L^(1/alpha)` norm of the translated Fourier transform. No moment, support, BV, log-concavity or smoothness assumption enters.
2. J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp--Lieb inequalities: finiteness, structure, and extremals*, GAFA 17 (2008), arXiv:math/0505065: Lieb's Gaussian-exhaustion theorem for Brascamp--Lieb constants. It applies to the rank-one linear maps appearing after Fresnel linearisation.

For a rank-three factorization `A=L^T D L`, any probability law `w` on nonzero three-column bases of `L`, with coordinate marginals

`alpha_i=P_w(i in S)<=1/2`,

and determinant-entropy score

`Z_w=exp(H(w)+sum_S w_S log det(L_S)^2)`,

the theorem gives a **continuous** density and

`||p_Q||_infinity <= 3 B_alpha^(2/3)(|det D| Z_w)^(-1/3)`,          (2.1)

where

`B_alpha=prod_i (1-alpha_i)^(-(1-alpha_i)/2)`.                      (2.2)

The proof stays in the original independent coordinates. This is important because the live correction archive forbids treating spectral projections as independent.

A fresh literature check also found Ruixiang Zhang, *Mixed-norm Brascamp-Lieb inequalities*, arXiv:2608.17952 (2026). That paper establishes configuration-specific mixed-norm inequalities and emphasizes rational-direction sensitivity and failure of perturbative stability in the genuinely mixed-norm regime. It does **not** supply the required universal cap-one circular-frame `1+2` trace estimate below, so it is not imported as a missing full-QFORM theorem.

## 3. Canonical normalized near-coloop coefficient map

The latest partner's circular family can be written in the normalized active coordinates

`Q_r=2 S C + D_0^2`,                                                (3.1)

with

`S=k X_0+t A_0`,
`k=r/sqrt(1+r^2)`, `t=1/sqrt(1+r^2)`, `k^2+t^2=1`,                  (3.2)

and residual circular projections

`A_0=sum_j X_j/sqrt(m)`,
`C=sum_j sqrt(2/m) cos(theta_j) X_j`,
`D_0=sum_j sqrt(2/m) sin(theta_j) X_j`,
`theta_j=2 pi j/m`.                                                 (3.3)

Thus, with

`J=[[0,1,0],[1,0,0],[0,0,1]]`,

we have `Q_r=X^T L^T J L X`, where the physical columns of `L` are

`ell_0=(k,0,0)`,
`ell_j=(t/sqrt(m), sqrt(2/m)cos(theta_j), sqrt(2/m)sin(theta_j))`.    (3.4)

Root-of-unity identities give

`LL^T=I_3`.                                                          (3.5)

Hence the physical quadratic matrix has nonzero spectrum exactly `{-1,1,1}` for every `m>=5` and every `r>0`. This is exactly the partner's target-valid circular family, merely written in an orthonormal active normalization.

The next result is actually more general than the circular frame.

## 4. New theorem: exact capped-basis score ceiling at a near-coloop

Let `V` be any residual Parseval `3`-frame and choose active coordinates so the shear direction is `e_1`. Put

`L=[k e_1, diag(t,1,1)V^T]`,                                       (4.1)

with `k^2+t^2=1` and `r=k/t>=1`. Then `LL^T=I_3`.

Partition the nonzero three-column bases into

`B_1={S:0 in S}` and `B_0={S:0 notin S}`.

Let

`W_a=sum_(S in B_a) det(L_S)^2`, `a=0,1`.                           (4.2)

### Lemma 4.1 — exact group determinant masses

`W_1=k^2`, `W_0=t^2`.                                               (4.3)

**Proof.** The total Cauchy--Binet mass is `det(LL^T)=1`. The volume-sampling marginal of column zero is its leverage `ell_0^T(LL^T)^(-1)ell_0=k^2`, which is exactly `W_1`. Hence `W_0=1-k^2=t^2`. Equivalently, the residual Gram is `diag(t^2,1,1)`, whose determinant is `t^2`. QED.

### Lemma 4.2 — entropy partition bound

For an arbitrary basis law `w`, put `q=P_w(0 in S)`. Then

`Z_w <= q^(-q)(1-q)^(-(1-q)) W_1^q W_0^(1-q)`.                    (4.4)

**Proof.** Condition `w` on the two groups. On each group, Gibbs' inequality / nonnegativity of relative entropy shows that

`H(w(.|B_a))+E[log det(L_S)^2 | B_a] <= log W_a`,                   (4.5)

with equality precisely for determinant-volume sampling inside that group. Add the binary entropy of the group label and exponentiate. QED.

### Theorem 4.3 — `QFORM-NEARCOLOOP-CAPPED-SCORE-CEILING-v1`

If the Hausdorff--Young admissibility condition requires

`q=alpha_0<=1/2`,                                                   (4.6)

then for every `r>=1`,

`boxed: Z_w <= 2 k t = 2r/(1+r^2).`                                (4.7)

**Proof.** Using (4.3), the logarithm of the right side of (4.4) has derivative

`log((1-q)/q)+2 log(k/t)
 =log((1-q)/q)+2log r`.                                             (4.8)

For `0<=q<=1/2` and `r>=1` this is nonnegative. Hence the maximum occurs at `q=1/2`; (4.4) becomes

`Z_w<=2 sqrt(W_0W_1)=2kt`. QED.

This is a **certificate obstruction**, not a lower bound on the true output density. Since `B_alpha>=1`, every numerical upper bound produced by (2.1) from such a capped basis law is at least

`3(2kt)^(-1/3)
 =3((1+r^2)/(2r))^(1/3)`,                                         (4.9)

which diverges like `r^(1/3)`. Therefore no reweighting inside the existing capped-basis Fresnel theorem can by itself close the shear-uniform near-coloop endpoint. This independently corroborates the latest partner r26 conclusion that its single-cut cross-volume certificate also necessarily leaves a positive shear exponent.

## 5. Circular frame: the score ceiling is attained by an admissible law

For the circular rows (3.4), use determinant-volume sampling **inside each group** and assign the two groups equal mass `1/2`. By Lemma 4.2 this attains

`Z_w=2kt`.                                                           (5.1)

Rotational/cyclic symmetry makes every residual coordinate have the same basis-inclusion marginal. In the hub group each basis uses exactly two residual columns, hence

`P(j in S | 0 in S)=2/m`.

In the residual-only group each basis uses three residual columns, hence

`P(j in S | 0 notin S)=3/m`.

Therefore

`alpha_0=1/2`,
`alpha_j=5/(2m) <=1/2  (m>=5)`.                                    (5.2)

So the score maximizer is genuinely admissible for the Beckner/Brascamp--Lieb theorem.

Its exact Hausdorff--Young factor is

`B_m
 =2^(1/4) (1-5/(2m))^(-(m-5/2)/2)`.                            (5.3)

The residual factor increases with `m`: putting `x=2m/5>1`, its logarithm is

`(5/4)(x-1) log(x/(x-1))`,                                         (5.4)

whose derivative is `(5/4)[log(x/(x-1))-1/x]>0`. Thus

`B_m < 2^(1/4)e^(5/4)`.                                             (5.5)

Substitute (5.1)--(5.5) and `|det J|=1` into (2.1): for every `m>=5`, every `r>=1`, and **every** admissible collection of independent cap-one input laws,

`boxed:
 ||p_(Q_r)||_infinity
 <= 3 B_m^(2/3) ((1+r^2)/(2r))^(1/3)
 < 3*2^(1/6)*e^(5/6) ((1+r^2)/(2r))^(1/3).`                       (5.6)

Numerically,

`3*2^(1/6)*e^(5/6)=7.748274334806134...`.                           (5.7)

The characteristic-function proof behind (2.1) is `L^1`, so (5.6) supplies a **continuous** density, not only an essential bound.

Examples:

- at `r=1`, the uniform-in-`m` certificate is `<7.748275`;
- at `r=2`, `<8.346576`;
- at `r=8`, `<12.363349`.

This applies directly to the latest account02/B18 circular stress family. In particular it improves its r26 MSS one-cut certificate

`54 sqrt(e) (1+r^2)^(1/6)`                                         (5.8)

throughout the circular large-shear regime and lowers the frame threshold from `m>=54` to `m>=5`. It does **not** remove the asymptotic `r^(1/3)` growth.

## 6. Actual use of the designated partner result

The partner r26 report proves all of the structural facts required above for the stress family: the Schur-isotropic representation, exact target spectrum `{-1,1,1}`, residual Parseval identity, and the fact that this full-spark circular frame has no dimension-free exact two-plane bank. Applying the source-valid capped-basis theorem to that exact partner coefficient map gives the concrete target inequality (5.6).

The partner also identifies the next unpaid implication as `QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1`: an asymmetric product-preserving `1+2` estimate that spends the full residual Pluecker mass at the scale `r^2|det D|`, rather than a squared single-cut determinant scale. Theorem 4.3 sharpens that diagnosis: **basis reweighting cannot manufacture the missing shear scale either**, even before one specializes to the circular frame. A genuinely new aggregate mechanism is necessary.

## 7. Fresh literature implication for the next mechanism

The obvious language for an asymmetric `1+2` estimate is a mixed-norm Brascamp--Lieb inequality. I checked the fresh primary arXiv source Ruixiang Zhang, arXiv:2608.17952 (18 Aug 2026). Its positive theorems concern specific lower-dimensional mixed-norm configurations, with rational-direction hypotheses entering the endpoint transference, and the paper explicitly highlights lack of perturbative stability. The circular QFORM projection directions vary through a full regular polygon and the desired estimate has a different three-dimensional quadratic-trace structure. Thus the current mixed-norm theorem does not match the hypotheses of the unpaid `1+2` step. This is a source-hypothesis audit, not a novelty claim from search absence.

## 8. Status

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.

**Proved this run:** `QFORM-NEARCOLOOP-CAPPED-SCORE-CEILING-v1`, plus the attained circular certificate (5.6) with continuity.

**First unpaid implication:** construct a product-preserving nonplanar `1+2` aggregate estimate whose effective determinant sees `r^2|det D|`, or route every such near-coloop survivor into a different already-paid branch. The capped-basis score ceiling (4.7), the partner's single-cut barrier, the full-spark no-exact-split theorem from account01/B18 r27, and the live conditional-cap correction jointly rule out the most direct existing interfaces.
