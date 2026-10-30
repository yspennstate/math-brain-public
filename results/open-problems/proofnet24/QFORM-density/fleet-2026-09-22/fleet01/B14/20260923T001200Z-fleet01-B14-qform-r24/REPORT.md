SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T00:11:50Z.
attacking: Schur-complement localization—feed a completed partner top-two cross density cap into the completed partner logarithmic physical-pair envelope, with arbitrary shifts, distant fragments, unbounded supports, and no moment assumptions.

# fleet01/B14 r24 — Schur-created cross smoothing pays an indefinite physical pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN`.

## 1. Exact target and correction boundary

The full target remains OPEN: for every finite `n`, independent real original-coordinate variables with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `X^T A X`, or produce a genuine counterexample.

Nothing below assumes moments, centering, connected support, bounded support, bounded fragment count, identical laws, log-concavity, or independence after a rotation. I do not use the refuted law-uniform pointwise quadratic Fourier decay, arbitrary-joint three-dimensional coarea, positive conditional projection-density moments, bounded-diameter localization, a universal good physical minor, or coefficient perturbation continuity. In particular, the newest fleet02/B14 remote-fragment obstruction shows that small matrix coefficients cannot be discarded uniformly in the present law class; the theorem below is exact, not perturbative.

The new mechanism is different from the preceding B14 run. Instead of requiring a zero-self cross block in the original matrix itself, it allows that useful cross smoother to appear only **after Schur-complementing an indefinite original-coordinate pair**. The remaining logarithmic singularity of that pair is then averaged against the genuinely bounded density produced by the Schur remainder.

## 2. Completed partner results actually applied

### 2.1 fleet02/B14 top-two cross averaging

Partner run `20260922T220604Z-fleet02-B14-QFORM-r21`, canonical report

`yspennstate/math-open-problems@2ca523ac73b814a97e846de8d37a932c127eecfb`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T220604Z-fleet02-B14-QFORM-r21/REPORT.md`

proves the following. For independent original-coordinate blocks `U,V`,

`T(U,V)=2 U^T C V + R(V)+ell_U^T U+ell_V^T V+c`,

with no `U`-self quadratic term, arbitrary measurable `R(V)`, arbitrary affine terms, and singular values `s_1(C)>=s_2(C)>=...`,

`||p_T||_infinity <= H_d := c_d [prod_{j=1}^d s_j(C)]^(-1/d)`       (2.1)

for every `2<=d<=rank(C)`, where

`c_d=[e d/(2(d-1))] v_d^(1/d)`.

In particular

`||p_T||_infinity <= e sqrt(pi)/sqrt(s_1(C)s_2(C)).`               (2.2)

The proof is translation-uniform and uses only original-coordinate product structure.

### 2.2 fleet02/B14 logarithmic leakage compiler

Partner run `20260922T230003Z-fleet02-B14-QFORM-r22`, canonical report

`yspennstate/math-open-problems@84093fddd5e3d3c692449d49c8b01537b28eb8d8`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T230003Z-fleet02-B14-QFORM-r22/REPORT.md`

combines the completed physical-pair logarithmic envelope with a sharp one-dimensional bathtub estimate. If an invertible indefinite ORIGINAL-coordinate principal pair `B` has

`D=|det B|`, `kappa=sigma_min(B)`,

and after completing the pair its outside critical-value/remainder random variable `R` has density cap `H`, define

`eta=8 D H/kappa`.                                                   (2.3)

Then

`||p_Q||_infinity <= 6 [ H/(kappa sqrt(D)) ]^(1/3),       eta<=1,`    (2.4)

and

`||p_Q||_infinity <= D^(-1/2)[3+log eta],               eta>=1.`     (2.5)

The pair translation may depend arbitrarily on the outside coordinates. No support, shift, fragment, or moment parameter enters.

These are the assigned-partner results used below, not merely cited.

## 3. A no-tax conditional localization lemma

### Lemma 3.1 — mass-linear conditional density assembly

Let `R` be a real random variable and `W` an arbitrary auxiliary variable. Suppose that for almost every `w` there is `H(w)>=0` such that for every interval `J`,

`P(R in J | W=w) <= H(w)|J|`,                                      (3.1)

and `E H(W)<infinity`. Then `R` has a density satisfying

`||p_R||_infinity <= E H(W)`.                                      (3.2)

Consequently any subsequent theorem that uses only the scalar density cap `H` may use `H=E H(W)`, rather than `ess sup H(W)`.

#### Proof

Integrating (3.1),

`P(R in J)<=E H(W)|J|`                                             (3.3)

for every interval. By the monotone-class/outer-regularity argument, the law of `R` is dominated by `E H(W)` times Lebesgue measure, so it has an essentially bounded density with (3.2). QED.

For a localization into normalized pieces of masses `w_alpha` and density caps `H_alpha`, take `W=alpha`. Then the only cost is

`H <= sum_alpha w_alpha H_alpha`.                                  (3.4)

Thus arbitrary numbers of fragments and arbitrarily distant fragments incur no separate normalization or diameter penalty. This is the exact mass-linear form needed below.

## 4. Main theorem: Schur-created top-two cross smoothing

Partition the ORIGINAL coordinates into a physical pair `P` of size two and its complement `O`. Write the quadratic matrix, and allow arbitrary affine terms, as

`A = [[B,F],[F^T,E]]`,
`Q(X)=X^T A X+b^T X+c`,                                            (4.1)

where `B` is an invertible indefinite `2x2` matrix. Define

`D=|det B|`, `kappa=sigma_min(B)`,
`S=E-F^T B^(-1)F`.                                                 (4.2)

Now partition the outside ORIGINAL coordinates as `O=I disjoint-union J disjoint-union K`. Assume

`S_II=0`,
`C=S_IJ`,
`rank(C)>=2`.                                                       (4.3)

No condition is imposed on `S_JJ,S_IK,S_JK,S_KK`, or on the original coupling `F`.

For `2<=d<=rank(C)` set

`H_d=c_d [prod_{j=1}^d s_j(C)]^(-1/d)`,
`c_d=[e d/(2(d-1))] v_d^(1/d)`,
`H_* = min_d H_d`,
`eta_* = 8 D H_*/kappa`.                                          (4.4)

### Theorem 4.1 — `QFORM-SCHUR-CROSS-PAIRLOG-v1`

Under (4.1)-(4.4), for arbitrary independent cap-one input laws,

`boxed:
 ||p_Q||_infinity
 <= 6 [H_*/(kappa sqrt(D))]^(1/3),              eta_*<=1,`        (4.5)

and

`boxed:
 ||p_Q||_infinity
 <= D^(-1/2)[3+log eta_*],                      eta_*>=1.`         (4.6)

In particular, paying only the top two Schur-cross singular values gives

`H_2 = e sqrt(pi)/sqrt(s_1(C)s_2(C))`,                            (4.7)

and (4.5)-(4.6) with `H_*=H_2` are valid even if all further Schur singular values are arbitrarily small.

The bound is uniform in arbitrary deterministic translations, conditioning-generated translations, distant support fragments, unbounded supports, and all moments.

### Proof

Complete the physical pair exactly. With `Z=X_O`,

`m(Z)=B^(-1)(FZ+b_P/2)`,                                          (4.8)

and a direct expansion gives

`Q=(X_P+m(Z))^T B (X_P+m(Z)) + R(Z)`,                             (4.9)

where

`R(Z)=Z^T S Z + beta^T Z + gamma`                                 (4.10)

for explicit but irrelevant affine coefficients `beta,gamma`. The pair variables remain the original independent coordinates `X_P`; the random translation `m(Z)` may be arbitrarily large and arbitrarily correlated with `R(Z)`.

We first prove a density cap for `R`. Condition on the original-coordinate block `X_K=w`. The quadratic part in `U=X_I,V=X_J` is

`2 U^T C V + V^T S_JJ V`,                                        (4.11)

because `S_II=0`; every term involving `w` becomes only an affine term in `U,V` plus a scalar. Thus, for every fixed `w`, equation (4.11) is exactly the hypothesis of the fleet02/B14 top-d cross theorem. Hence

`P(R in J_0 | X_K=w) <= H_* |J_0|`                               (4.12)

for every interval `J_0`, uniformly in `w`. Lemma 3.1 therefore gives

`||p_R||_infinity <= H_*`.                                        (4.13)

Now apply the completed fleet02/B14 logarithmic leakage compiler to (4.9), using the original physical pair `B` and the density cap (4.13). Its parameter is exactly `eta_*=8DH_*/kappa`, and its two optimized branches are (4.5) and (4.6). QED.

### Why this is a localization theorem rather than a hidden rotation

All conditioning is on original coordinate blocks. The only algebraic operation on the physical pair is completion of the square, which translates those two coordinates coordinatewise. The cross singular vectors enter only in the partner's proven negative-moment estimate; no claim of independence is made after singular-vector rotation. Equation (4.12) is uniform in the conditioning-induced affine terms, and Lemma 3.1 averages before any worst-case fragment normalization. Therefore no support geometry enters the constant.

## 5. Explicit nonseparable target-class family

The theorem is nonvacuous even when the useful zero-self cross block exists only after Schur complementation.

Let

`B=[[0,2],[2,0]]`,
`F=(1/2)[[1,0,0,0],[0,1,0,0]]`,                                  (5.1)

and, on four outside coordinates split as `I={3,4}`, `J={5,6}`, let

`S_0=[[0,0,2,0],
     [0,0,0,2],
     [2,0,0,0],
     [0,2,0,0]].`                                                 (5.2)

Set

`E=S_0+F^T B^(-1)F
  =[[0,1/8,2,0],
    [1/8,0,0,2],
    [2,0,0,0],
    [0,2,0,0]]`,                                                  (5.3)

and

`A_*=[[B,F],[F^T,E]].`                                            (5.4)

Then the original outside `I`-self block is **not** zero (`E_34=1/8`), but after eliminating the physical pair,

`E-F^T B^(-1)F=S_0`;                                              (5.5)

thus the Schur cross block is exactly `C=2I_2` and the Schur `I`-self block vanishes.

This is a genuine target matrix. The comparison matrix `diag(B,S_0)` has three eigenvalues `+2` and three eigenvalues `-2`. Moreover

`||A_*-diag(B,S_0)||
 <= ||F|| + ||F^T B^(-1)F||
 <= 1/2+1/8=5/8`.                                                 (5.6)

Weyl's inequality therefore gives three eigenvalues at least `11/8` and three at most `-11/8`. In particular all six eigenvalues have modulus greater than one.

Here

`D=4`, `kappa=2`, `s_1(C)=s_2(C)=2`,
`H_2=e sqrt(pi)/2`,
`eta_*=8 e sqrt(pi)>1`.                                           (5.7)

The high branch (4.6) yields the completely law-uniform bound

`boxed:
 ||p_{X^T A_* X}||_infinity
 <= (1/2)[3+log(8 e sqrt(pi))]
 < 3.326.`                                                        (5.8)

This is not a block-diagonal convolution argument: the original pair-outside coupling `F` is nonzero and creates a nonzero original `I`-self entry which is canceled only at the exact Schur-complement level.

Moreover, any larger symmetric matrix having `A_*` as this six-coordinate principal block may have completely arbitrary extra coordinates, arbitrary extra self-quadratic terms, and arbitrary couplings to these six coordinates. Condition first on all added original coordinates. They generate only affine terms on the six active coordinates, and Theorem 4.1 retains the same bound (5.8). By Cauchy interlacing, the enlarged matrix still has at least three eigenvalues of modulus at least one.

## 6. Why remote fragments do not break the argument

Fleet02/B14 r22 proves a target-valid obstruction to any uniform statement of the form “small operator-norm coefficient perturbation implies small output-law perturbation”: supports at distance of order `1/epsilon` can turn a coefficient of size `epsilon` into an order-one output change. The present proof never approximates `A`, truncates the support, bounds a translation magnitude, or discards a small coefficient. The identities (4.8)-(4.10) are exact, and both partner bounds are uniform in translations. Hence the remote-fragment obstruction is respected rather than bypassed.

Likewise, a finite-fragment decomposition is optional. If one is used, Lemma 3.1 pays the mass-weighted sum of the normalized caps and therefore does not replace distant fragments by a bounded-diameter surrogate.

## 7. Remaining connection to full QFORM

The full conjecture is not solved by Theorem 4.1. Its unpaid structural implication is:

> Starting only from `s_3(A)>=1`, either expose an original-coordinate indefinite physical pair whose exact Schur complement has a quantitatively strong top-two zero-self cross smoother as in (4.3), or route the matrix into one of the already-paid diffuse/ridge/grouped-bank branches, without selecting and reciprocating a tiny physical minor or using coefficient perturbation continuity.

The singleton-plus-two-diffuse-banks family shows why a uniformly good fixed physical minor cannot be required. The new theorem enlarges the paid region because the cross smoother may be **created by exact Schur complementation**, with arbitrary pair-to-outside coupling `F`; it does not prove that every three-large-eigenvalue matrix enters this region.

Claim introduced: `QFORM-SCHUR-CROSS-PAIRLOG-v1`.  
Classification: `SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.
