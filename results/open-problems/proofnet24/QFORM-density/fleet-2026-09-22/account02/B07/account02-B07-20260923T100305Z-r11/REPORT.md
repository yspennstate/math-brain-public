SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T10:03:05Z.
attacking: rank-three/four physical E2-edge receiver — carry the incident determinant bank through a curvature-safe fractional estimate, and stress the tempting pair-Schur transfer by an exact N3 family.

# account02/B07 r11 — fractional volume survives arbitrary curvature; anchored E2 need not survive pair completion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / complementary constructions and source-valid counterexamples  
Run: `account02-B07-20260923T100305Z-r11`  
Start brain control: `b6e14315c387982135fb075d936a39ff56c3d533`  
Pre-publication brain refresh: `d496d87720267c27b9728e8d659dc02d2ebeafb2`  
OWNER CONTROL revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING FRACTIONAL-VOLUME COROLLARY + EXACT TARGET-CLASS OBSTRUCTION TO E2-THROUGH-SCHUR / FULL QFORM OPEN**.

## 1. Scope and first unpaid implication

The unrestricted target remains OPEN: arbitrary independent real ORIGINAL-coordinate inputs with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, and a universal essential density bound for `X^T A X`; continuity is separate.

The first live B07 debt at startup was the nonlinear receiver left by account03/B07 r30. Its immutable source is

`yspennstate/math-open-problems@466a8413b3d1ec6ce723633be0fe14eafaa7175d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T090613Z-account03-B07-qform-r30/REPORT.md`.

In its double-anchored branch an ORIGINAL-coordinate cross block

`N=[[b,r^T],[c,D]]`

has an anchored third-compound bank

`G=G3^(i,a)(N)>gamma F^6`,
`gamma=1/113246208^2`,

and r30 proves, before reciprocal localization, either

`|b| sqrt(E2(D)) >= sqrt(G)/2`

or a four-disjoint-bank star-star-core certificate. Its remaining debt is to consume those lower-order banks while retaining arbitrary within-bank curvature and the true ambient remainder.

The corrections used here are the live programme restrictions: no post-rotation independence, no arbitrary-joint coarea estimate, no law-uniform scalar pointwise phase decay, no deletion of a small nonzero quadratic remainder, and no assertion of one uniformly good physical minor.

## 2. New corollary — `QFORM-DK-FRACTIONAL-POTENTIAL-v1`

This is a direct but previously unapplied combination of two completed results in the required Claude source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`:

1. the general `D_k` decoupling/volume argument; and
2. the Fourier-to-fractional-potential lemma.

Let `I,J` be disjoint ORIGINAL-coordinate sets and

`M=A[I,J]`,
`Z_k=e_k(M^T M)>0`.

All remaining coordinates may first be conditioned. The resulting polynomial on `I union J` may have arbitrary two self-blocks and arbitrary affine terms. The `D_k` proof states that, for Jensen exponent `q>=1`,

`E F^q <= e^(k/2) (2pi/|t|)^k q^(-k/2) Z_k^(-1/2)`

whenever every row k-volume inclusion marginal is at most `q/2`. Every inclusion marginal is at most one, so `q=2` is always admissible. The decoupling square root therefore gives

`|phi(t)| <= min(1, B_k |t|^(-k/4))`,                       (2.1)

with

`B_k=[e^(k/2)(2pi)^k 2^(-k/2) Z_k^(-1/2)]^(1/4)`.           (2.2)

Now use the proved identity

`H_alpha(Q):=sup_s E |Q-s|^(-alpha)
 <= c_alpha int |t|^(alpha-1)|phi(t)| dt`,

`c_alpha=2^(1-alpha) Gamma((1-alpha)/2)
        /(2 sqrt(pi) Gamma(alpha/2))`.

For `0<alpha<k/4`, integrate `min(1,B_k|t|^(-k/4))` at its crossover. This gives

`boxed:
H_alpha(Q)
 <= C_(k,alpha) Z_k^(-alpha/(2k)),`                           (2.3)

where

`C_(k,alpha)
 = c_alpha * k/[2 alpha (k/4-alpha)]
   * (pi sqrt(2e))^alpha.`                                    (2.4)

The exponent has the correct scaling: `Z_k` has coefficient degree `2k`, so (2.3) is homogeneous of degree `-alpha`.

Because the argument is conditional on all outside ORIGINAL coordinates and uniform in every affine term, averaging the conditional inequality preserves (2.3). Thus arbitrary same-bank curvature, outside couplings and extra spectrum are genuinely retained. No marginal gate remains; the price is that one obtains a fractional potential rather than a density when `k<=4`.

Two concrete cases are

`boxed: H_(1/4)(Q) <= 3.929131771 Z_2^(-1/16),`               (2.5)

and

`boxed: H_(1/2)(Q) <= 12.956788440 Z_3^(-1/12).`              (2.6)

The captured checker independently evaluates the constants.

## 3. Actual application to the completed account03/B07 r30 packet

The r30 anchored bank is a subset of the full third compound, hence

`E3(N)>=G>gamma F^6`.

Apply (2.6) to the ACTUAL physical cross block `N`. Without using any third-volume marginal condition,

`H_(1/2)(Q)
 < 12.956788440 gamma^(-1/12) F^(-1/2)
 < 284.994 F^(-1/2).`                                        (3.1)

This is a full-ambient half-Riesz estimate on the entire r30 double-anchored survivor. It is not yet a density estimate, but unlike a best-minor bound it survives every within-bank quadratic term and all outside affine terms.

There is also a sharper conditional statement on r30's E2-edge branch. Condition the two physical anchors and every coordinate outside the far row/column banks. The remaining quadratic polynomial has cross block `D`, arbitrary two self-blocks and arbitrary affine terms, so (2.5) gives

`H_(1/4)(Q_far | anchors)
 <=3.929131771 E2(D)^(-1/16).`                                (3.2)

From

`|b| sqrt(E2(D)) >=sqrt(G)/2`, `G>gamma F^6`, and `|b|<=F`,

one obtains

`boxed:
H_(1/4)(Q_far | anchors)
 <43.519 F^(-1/4)`                                             (3.3)

at the standard r30 collar. The bound is uniform in the conditioned anchor values. Again, (3.3) is input currency for a receiver, not by itself a density theorem for the unconditioned form.

## 4. Exact N3 construction — `QFORM-ANCHOR-H3-SCHUR-E2-COLLAPSE-v1`

The natural next shortcut would be: in the E2-edge branch, peel the physical anchor pair and reuse `E2(D)` in the pair Schur remainder. That implication is false even inside the exact no-pivot target class.

For every even integer `m>=12`, put

`N0=m^2`, `b=1/m`, `S=sqrt(m)`, `a=m^(-1/4)`.

On two disjoint `N0`-coordinate banks `U,V`, choose the flat orthonormal pairs

`p_j=N0^(-1/2)`, `u_j=(-1)^j N0^(-1/2)`,
`q_j=N0^(-1/2)`, `v_j=(-1)^j N0^(-1/2)`.

Add two physical anchors `x,y`, and define the symmetric matrix `A_m` only through

`A_xy=b`,
`A_xU=a p^T`,
`A_yV=a q^T`,
`A_UV=S(p q^T+u v^T)`,                                       (4.1)

with all other entries, including every diagonal, equal to zero.

### 4.1 Exact spectrum and target validity

In the modal span `(x,y,p,q)` the matrix is

`[[0,b,a,0],
  [b,0,0,a],
  [a,0,0,S],
  [0,a,S,0]]`.

Because `a^2=bS`, its eigenvalues are exactly

`+(S+b), -(S+b), 0, 0`.

The orthogonal `(u,v)` block contributes `+S,-S`, and every other direction is null. Hence

`spec_nonzero(A_m)={S+b,-(S+b),S,-S}`.                       (4.2)

For every `m>=12` there are four, not merely three, eigenvalues of modulus at least one.

### 4.2 It lies in the live no-pivot class

Every physical diagonal is zero. The physical entries satisfy

`|A_uv| <= max(1/m, m^(-5/4), 2m^(-3/2))=1/m`.

Therefore every physical 2x2 principal determinant has magnitude at most `1/m^2<1/128`. Thus, for the standard `tau=1/128`, every `A_m` is an exact N3 instance.

### 4.3 The incoming anchored determinant resource stays constant

Take the ORIGINAL-coordinate cross cut

`I={x} union U`, `J={y} union V`.

Its cross block is

`N_m=diag(b,D_m)`,
`D_m=S(p q^T+u v^T)`.

The two nonzero singular values of `D_m` are `S,S`. Consequently

`E2(D_m)=S^4=m^2`,
`|b| sqrt(E2(D_m))=1`.                                       (4.3)

Since `D_m` has rank exactly two, every nonzero 3x3 minor of `N_m` contains both anchors, and

`G3^(x,y)(N_m)=E3(N_m)=b^2 S^4=1`.                           (4.4)

Thus the partner's double-anchored third-volume and E2-edge resources remain order one as `m->infinity`, while the physical anchor edge `b` and its pair determinant `b^2` tend to zero.

### 4.4 Pair completion destroys the entire E2 bank

The zero-diagonal anchor pair is

`P=[[0,b],[b,0]]`.

The only same-bank anchor-to-far couplings are `a p` from `x` into `U` and `a q` from `y` into `V`. Since

`a^2/b=S`,

the `U x V` cross block in the Schur complement by `P` is

`D_m-(a^2/b)p q^T
 =S u v^T`,                                                   (4.5)

which has rank one. Hence

`boxed: E2((A_m/P)[U,V])=0`                                   (4.6)

although the incoming `E2(D_m)=m^2` diverges and the anchored third volume is identically one.

This is the exact obstruction: arbitrary within-bank anchor curvature can remove one entire singular component of the far cross block during pair completion. A receiver may not silently reuse the pre-completion E2 bank in the Schur remainder.

### 4.5 No bounded physical spectral core is forced either

Fix a cardinality bound `M`, and let `H` be any physical coordinate set with `|H|<=M`. Separate the possible anchor edge, a matrix of rank at most two. The remaining terms in `A_m[H,H]` have operator norm at most

`2 a sqrt(M/N0)+2 S M/N0
 =2 sqrt(M) m^(-5/4)+2M m^(-3/2).`                             (4.7)

By the rank-two approximation/min-max inequality,

`boxed:
s_3(A_m[H,H])
 <=2 sqrt(M) m^(-5/4)+2M m^(-3/2) ->0.`                       (4.8)

Thus constant double-anchored third volume and constant edge-times-E2 currency do not force a uniformly spectral bounded-cardinality physical core.

## 5. The required e5 result pays the obstruction for the correct reason

The family above is not a QFORM counterexample. Condition only on the two ORIGINAL anchor variables `x,y`. The far quadratic block on `U union V` is

`[[0,D_m],[D_m^T,0]]`,

whose nonzero eigenvalues are `+S,+S,-S,-S`. Conditioning the anchors adds only affine terms `2ax p^T U+2ay q^T V`, which are explicitly allowed in the completed e5 Theorem F.

The four-dimensional range projection has physical leverage

`p_j^2+u_j^2=2/N0`

on each `U` coordinate and likewise `2/N0` on each `V` coordinate. This is at most `1/2`. The e5 theorem with `r=4` therefore gives, uniformly in the anchor values,

`boxed:
||p_(Q | x,y)||_infinity
 <=8 (S^4)^(-1/4)=8/S=8/sqrt(m).`                              (5.1)

Averaging the conditional densities yields

`boxed: ||p_Q||_infinity <=8/sqrt(m) <=8.`                     (5.2)

So the obstruction is source-valid and target-valid: it kills the proposed bounded-core / E2-through-Schur mechanism but is itself uniformly paid by a genuine product-law theorem, with no rotation-independence assumption.

## 6. What changed and the new first unpaid implication

Two things are now fixed.

First, the entire account03/B07 r30 anchored-H3 survivor has an unconditional, curvature-safe half-Riesz estimate (3.1), and its E2-edge far form has the conditional quarter-Riesz estimate (3.3). These are aggregate determinant-weight outputs; no individual minor is selected.

Second, the exact N3 family (4.1) shows that neither a bounded physical core nor preservation of `E2(D)` under an anchor-pair Schur complement can be demanded from the same resource. Any proof that peels the anchors must explicitly pay the rank-one correction caused by same-bank anchor couplings.

The sharpened first unpaid implication is therefore

`QFORM-ANCHOR-H3-CURVATURE-COMPATIBLE-UPGRADE-v1`:

> Starting from r30's anchored-H3 / edge-E2 / four-bank resources, upgrade the curvature-safe `H_(1/2)` or conditional `H_(1/4)` bounds to an essential density bound without assuming the pre-completion E2 bank survives a pair Schur complement. Equivalently, build a mixed direct/decoupled receiver stable under the rank-one loss in (4.5), or force a different already-paid physical branch before completion.

The family (4.1) is a mandatory regression: a valid receiver must either pay it directly (as Theorem F does) or remain valid after the Schur E2 collapse.

The sibling r30 rank-one-tube, six-bank nested-E2 and four-star BICORE branches remain separate lower-order receiver debts. Full QFORM and full-target continuity remain OPEN.

## 7. Checks and review status

`CHECKS.py` verifies the fractional constants, modal spectrum, fixed anchored volume, edge-times-E2 product, N3 entry bound, exact Schur rank drop and the e5 Theorem-F density cap for `m=12,16,32,64`. Captured output ends

`QFORM_B07_ANCHORED_SCHUR_COLLAPSE_CHECK_PASS`.

These computations are regression checks, not proof evidence. The proof is the exact algebra above. Independent end-to-end review of this report has not yet occurred.
