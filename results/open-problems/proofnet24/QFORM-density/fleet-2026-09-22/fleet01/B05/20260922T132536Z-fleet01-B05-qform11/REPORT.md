# fleet01/B05 — universal rank-two half-Riesz bound by heavy-row coarea

**Run:** `20260922T132536Z-fleet01-B05-qform11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and conditional route

The full target remains open: for every dimension, every independent real input vector with coordinate densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, sign, diagonal-basis, or post-rotation-independence hypothesis is used below. Continuity is a separate requested regularity conclusion and is not proved here.

The previous B05 run proved a determinant-scale half-Riesz estimate for a *diffuse* rank-two quadratic residual and inserted it into the scalar-Schur inequality of the assigned partner fleet02/B05. Its first geometric debt was the localized rank-two Schur residual. This run closes that debt completely: every rank-two quadratic form has the required half-Riesz bound at the determinant scale, with no leverage or sign hypothesis.

The remaining rank-exactly-three obstruction is therefore no longer residual localization; it is the genuinely near-isotropic heavy-pivot regime. Arbitrary additional nonzero spectral directions remain a separate spectral-truncation/interaction debt.

## 2. Dependencies actually applied

### Assigned partner: fleet02/B05

Canonical report:

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`.

For a nonzero physical pivot `a`, after completing the square only in that original independent coordinate,

`Q=a(X+m(Z))^2+R(Z)`,                                      (2.1)

the partner proves the pointwise density inequality

`p_Q(t) <= |a|^(-1/2) E |t-R(Z)|^(-1/2)`.                 (2.2)

I apply (2.2) in Section 7 to the new general rank-two half-Riesz theorem.

### Prior diffuse rank-two theorem

The preceding fleet01/B05 report

`yspennstate/math-open-problems@0b0918d419af754cc2a180e8c444747963dd24ff`

proved, using the completed fleet03/B05 Fourier--Brascamp--Lieb theorem, that if a rank-two quadratic form `S` has active spectral projector `P` satisfying

`max_j ||P e_j||_2 <= 1/2`,

then

`sup_s E|s-X^T S X|^(-1/2) <= C_diff |mu_1 mu_2|^(-1/4)`, (2.3)

where `C_diff=2 sqrt(2) B/pi` and `B` is the absolute Brascamp--Lieb/Fourier constant from that source.

### One-dimensional marginal theorem

I also use the sharp product-marginal theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures* (arXiv:1507.07949; Israel J. Math. 216 (2016)): if the coordinates are independent with densities bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. In particular, for every unit vector `c`, the linear form `c.X` has density bounded by `sqrt(2)`. This result is applied only to an original-coordinate linear form; no independence after rotation is asserted.

## 3. Three elementary coarea kernels

The proofs below are included because they are the part that removes the localized residual.

### Lemma 3.1 — scalar square half-kernel

Let `F` be any probability density on `R` with `0<=F<=1`. For `a!=0`, `d!=0` and arbitrary `m`,

`int F(x) |d-a(x+m)^2|^(-1/2) dx`
` <= 4 |a|^(-1/4)|d|^(-1/4)`.                           (3.1)

**Proof.** Translation removes `m`; factor out `|a|`. Put `q=d/a`. For every `r>0`,

`Leb{x: |q-x^2|<r} <= 4 r / sqrt(|q|)`.                  (3.2)

For `q>0,r<q`, the left side equals

`2(sqrt(q+r)-sqrt(q-r))=4r/(sqrt(q+r)+sqrt(q-r))`,

which is at most `4r/sqrt(q)`. For `q>0,r>=q` it is `2sqrt(q+r)<=2sqrt(2r)<=4r/sqrt(q)`. For `q<0` it is zero when `r<=|q|`, and otherwise equals `2sqrt(r-|q|)<=2r/sqrt(|q|)`.

Thus, by layer cake and the facts `F<=1`, `int F=1`,

`int F(x)|q-x^2|^(-1/2)dx`
` <= int_0^infty min(1,4 t^(-2)/sqrt(|q|)) dt`
` =4 |q|^(-1/4)`.

Scaling by `a` gives (3.1). QED.

### Lemma 3.2 — square quarter-kernel under a marginal cap

If `W` is a real random variable with probability density bounded by `M`, then for every `q` and every `nu!=0`,

`E |q-nu W^2|^(-1/4) <= 4 sqrt(M) |nu|^(-1/4)`.          (3.3)

**Proof.** Uniformly in `s in R` and `r>0`,

`Leb{w: |s-w^2|<r} <= 4 sqrt(r)`.                        (3.4)

Indeed, when `s>=0,r<s` rationalize the two square-root intervals, while for `r>=s` their union lies in `[-sqrt(s+r),sqrt(s+r)]`; for `s<0` the claim is immediate. Hence

`P(|s-W^2|^(-1/4)>t) <= min(1,4M t^(-2))`.

Layer cake gives

`int_0^infty min(1,4M t^(-2))dt=4 sqrt(M)`.

Scale by `nu`. QED.

### Lemma 3.3 — linear half-kernel

For a probability density `F<=1`, `H!=0`, and arbitrary `c`,

`int F(x)|c-2Hx|^(-1/2)dx <= 2|H|^(-1/2)`.               (3.5)

If a random variable `H` has density bounded by `M_H`, then

`E|H|^(-1/2) <= 2 sqrt(2M_H)`.                           (3.6)

Both statements follow directly from layer cake: the affine image in (3.5) has density cap `1/(2|H|)`, while `P(|H|<t^(-2))<=min(1,2M_H t^(-2))` in (3.6).

## 4. Exact rank-two Schur identities at a heavy physical row

Let `S` be any real symmetric rank-two matrix. Write its active spectral representation as

`S=U Lambda U^T`, `U^T U=I_2`,

where `Lambda` is invertible symmetric `2x2`. Put

`D=|det Lambda|=|mu_1 mu_2|`.

Write `u_i in R^2` for row `i` of `U`, `ell_i=||u_i||^2`, and

`a_i=u_i^T Lambda u_i=S_ii`.

Assume row `i` is heavy in the sense

`||u_i||>1/2`, equivalently `ell_i>1/4`.                  (4.1)

### Nonzero pivot

If `a=a_i!=0`, completing the physical coordinate `X_i` yields

`X^T S X = a(X_i+m(Z))^2 + Z^T S_i Z`,                  (4.2)

where

`S_i=U_- K_i U_-^T`,
`K_i=Lambda-(Lambda u_i)(Lambda u_i)^T/a`.               (4.3)

Here `K_i u_i=0`, so the residual has rank one. Let its nonzero eigenvalue be `nu`. Since `U_-^T U_-=I-u_i u_i^T`, `U_-` is an isometry on `u_i^perp`, hence `nu` is also the nonzero eigenvalue of `K_i`.

The exact identity is

`a nu = (det Lambda) ell_i`.                              (4.4)

To see this, use the determinant lemma on

`K_i(s)=Lambda-s(Lambda u_i)(Lambda u_i)^T/a`:

`det K_i(s)=det(Lambda)(1-s)`.

At `s=1`, a symmetric rank-one `2x2` matrix with kernel `span(u_i)` has

`adj(K_i)=(nu/ell_i) u_i u_i^T`.

Differentiating the determinant at `s=1` also gives

`adj(K_i)=(det Lambda/a) u_i u_i^T`,

which proves (4.4).

Thus there is a unit coefficient vector `c` on the remaining original coordinates such that

`Z^T S_i Z = nu (c.Z)^2`.                                (4.5)

### Zero pivot

If `a_i=0`, write instead

`X^T S X = 2 X_i H(Z)+R_0(Z)`,                           (4.6)

with `H(Z)=b.Z` and `b=S_{i,-i}`. Then

`||b||_2^2=(S^2)_ii=u_i^T Lambda^2 u_i`.                 (4.7)

Cayley--Hamilton for the `2x2` matrix `Lambda` gives

`Lambda^2-(tr Lambda)Lambda+(det Lambda)I=0`.

Using `a_i=0` in (4.7),

`||b||_2^2=-(det Lambda) ell_i = D ell_i`.                (4.8)

In particular this case is necessarily indefinite.

## 5. Heavy-row rank-two half-Riesz theorem

### Theorem 5.1 — `QFORM-RANK2-HEAVY-HALF-RIESZ-v1`

Under (4.1), for arbitrary independent input coordinates with densities bounded by one,

`sup_s E |s-X^T S X|^(-1/2)`
` <= 16*2^(1/4) (D ell_i)^(-1/4)`.                       (5.1)

Consequently, because `ell_i>1/4`,

`sup_s E |s-X^T S X|^(-1/2)`
` <= 16*2^(3/4) D^(-1/4) < 26.91 D^(-1/4)`.             (5.2)

No sign restriction is imposed.

**Proof when `a_i!=0`.** Set `L=c.Z` in (4.5). The product-marginal theorem gives a density cap

`||p_L||_infinity <= sqrt(2)`.                            (5.3)

Condition on `Z`. Lemma 3.1 applied to the original independent coordinate `X_i` yields, except on the null set where `s-nu L^2=0`,

`E_{X_i}|s-X^TSX|^(-1/2)`
` <=4 |a|^(-1/4)|s-nu L^2|^(-1/4)`.                     (5.4)

Average and apply Lemma 3.2 with `M=sqrt(2)`:

`E|s-X^TSX|^(-1/2)`
` <=16*2^(1/4)|a nu|^(-1/4)`
` =16*2^(1/4)(D ell_i)^(-1/4)`,                          (5.5)

using (4.4).

**Proof when `a_i=0`.** Condition on `Z` in (4.6) and use Lemma 3.3:

`E_{X_i}|s-X^TSX|^(-1/2) <= 2|H(Z)|^(-1/2)`.             (5.6)

Let `sigma=||b||_2=sqrt(D ell_i)`. The normalized form `H/sigma` is a unit linear projection of a product law, so

`||p_H||_infinity <= sqrt(2)/sigma`.                     (5.7)

Using (3.6),

`E|s-X^TSX|^(-1/2)`
` <=4*2^(3/4)(D ell_i)^(-1/4)`,                          (5.8)

which is stronger than (5.1). QED.

The theorem is fully compatible with the logarithmically unbounded density of a rank-two opposite-sign form: it bounds only the half-order Riesz potential needed for a third smoothing direction.

## 6. Universal rank-two half-Riesz theorem

### Theorem 6.1 — `QFORM-RANK2-UNIVERSAL-HALF-RIESZ-v1`

Let `S` be any real symmetric rank-two matrix with nonzero eigenvalues `mu_1,mu_2`, and let `X` have independent coordinates with densities bounded by one. Then

`sup_s E |s-X^T S X|^(-1/2)`
` <= C_2 |mu_1 mu_2|^(-1/4)`,                            (6.1)

where one may take

`C_2=max(C_diff,16*2^(3/4))`,
`C_diff=2 sqrt(2) B/pi`.                                  (6.2)

**Proof.** If every active-projector row norm is at most `1/2`, apply the already proved diffuse estimate (2.3). Otherwise choose a row with norm greater than `1/2` and apply Theorem 5.1. QED.

This closes the mixed/localized rank-two half-Riesz regime that remained open in the preceding B05 report. The argument preserves original-coordinate product structure throughout: the only rotated object is a one-dimensional marginal, for which a theorem valid for arbitrary product densities is explicitly invoked.

## 7. Assigned-partner application: rank-exactly-three Schur closure without residual diffuseness

Let now

`A=U Lambda U^T`

have rank exactly three, with `Lambda` invertible `3x3`, and let `ell_i=||u_i||^2`, `a_i=A_ii=u_i^T Lambda u_i`. The previous B05 report proved the exact Schur identity

`|mu_1 mu_2| = |det Lambda| ell_i/|a_i|`                 (7.1)

for the two nonzero eigenvalues of the rank-two residual after a nonzero physical pivot `a_i`.

Apply the assigned partner's inequality (2.2) and Theorem 6.1:

`||p_{X^TAX}||_infinity`
` <= |a_i|^(-1/2) C_2 |mu_1mu_2|^(-1/4)`
` = C_2 (|a_i| |det Lambda| ell_i)^(-1/4)`.              (7.2)

This is the same determinant-scale Schur estimate as before, but **all Schur-residual localization hypotheses have disappeared**.

In particular, if `ell_i>1/4`, `|a_i|>=eta>0`, and `|det Lambda|>=1`, then

`||p_Q||_infinity <= sqrt(2) C_2 eta^(-1/4)`.            (7.3)

Equivalently, if the physical Rayleigh quotient `rho_i=a_i/ell_i` obeys `|rho_i|>=eta`, then

`||p_Q||_infinity <= 2 C_2 eta^(-1/4)`                  (7.4)

because `ell_i>1/4`.

Thus, for a rank-exactly-three target form, the structural dichotomy is now:

1. all active spectral rows have norm at most `1/2`: the completed diffuse rank-three theorem applies;
2. some heavy row has a quantitatively non-isotropic physical pivot: (7.2)--(7.4) apply with no residual geometry condition;
3. the only remaining uniform obstruction is the **heavy near-isotropic pivot regime**, where every heavy row has very small `|u_i^T Lambda u_i|` (or small Rayleigh quotient).

The hard saddle families already present in the team state show that this third regime is genuine and may require high-cardinality product-preserving aggregation; it cannot be replaced by a single strong fixed physical minor or by a generic conditional-density cap.

## 8. What this does and does not solve

What is proved here:

- a universal determinant-scale half-Riesz estimate for every rank-two quadratic form under arbitrary independent coordinate densities bounded by one;
- a rank-exactly-three heavy-pivot density bound that is independent of Schur-residual localization;
- an exact reduction of the remaining rank-exactly-three geometric debt to near-isotropic heavy pivots.

What is **not** proved:

- the full arbitrary-rank theorem with merely three eigenvalues of modulus at least one;
- a uniform treatment of the near-isotropic heavy-pivot branch;
- a valid way to discard or condition away arbitrary additional small spectral directions;
- continuity of the density in the new branch.

The first unpaid implication is therefore

`QFORM-HEAVY-ISOTROPIC-AGGREGATE-v2`:

> In the rank-exactly-three core, close the regime in which a physical spectral row has norm `>1/2` but every such heavy row has small quadratic Rayleigh value `|u_i^T Lambda u_i|`, using original-coordinate product provenance (for example a high-cardinality hyperbolic/aggregate mechanism) rather than only pair/conditional density caps. After that, handle the separate arbitrary-extra-spectrum truncation/interaction problem.

## 9. Corrections respected

This report does not use the refuted law-uniform pointwise one-dimensional Fresnel decay, post-rotation independence, unrestricted fiber suprema, a fixed-principal-minor dichotomy, single-Schur rank-two extraction, conditional-cap-as-independence, or bounded-diameter localization. No simulation is used as proof evidence. The full conjecture remains open.
