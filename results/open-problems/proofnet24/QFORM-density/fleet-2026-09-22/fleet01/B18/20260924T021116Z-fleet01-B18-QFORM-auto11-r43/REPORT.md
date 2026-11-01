# fleet01/B18 r43 — exact rank-one cross / two-dimensional complement-active-plane closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T021116Z-fleet01-B18-QFORM-auto11-r43`  
**Role:** literature-to-proof transfer  
**Status:** `PROVED SUPPORTING TARGET-LEVEL BRANCH / LATEST DESIGNATED PARTNER FUNNEL APPLIED / PRIOR PARTNER RECEIVER APPLIED / FULL QFORM OPEN`  
**Continuity:** separate; proved below only for the literal three-original-coordinate endpoint.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-24T02:11:16Z.  
attacking: the newest fleet02/B18 zero-self survivor at the exact rank-one-cross endpoint; retain original-coordinate provenance and pay the two-dimensional complement-active-plane chamber by a source-valid marginal theorem plus the completed scalar/dependent-pair receiver.

## 1. Scope and correction discipline

The owner target remains unrestricted and **OPEN / NOT PROVED / NOT DISPROVED**: independent real original coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, iid hypothesis, centering, symmetry, smoothness, or post-rotation independence is assumed.

Fresh controls and the live correction inbox were reread before publication. This report does not use arbitrary-joint coarea, conditional-density-cap-as-independence, independence after rotation, pointwise law-uniform stationary phase, a uniformly good fixed physical minor, or deletion of a small nonzero quadratic tail. In particular, the theorem below is a **global exact block theorem**. I do not claim an arbitrary ambient principal-block lift, because conditioning outside a principal block can create affine directions not measurable through the retained low-dimensional projections; the live conditional-cap correction forbids silently treating those as harmless.

## 2. Primary-source hypothesis audit

### 2.1 Livshyts--Paouris--Pivovarov matches the rough product inputs exactly

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1.

For a genuine product probability density `f=prod_i f_i` and a `k`-dimensional orthogonal marginal, the theorem gives the cap-one specialization

`||pi_E f||_infinity <= 2^(k/2)`.

There is no moment, iid, bounded-support, log-concavity, centering, symmetry, or smoothness hypothesis. I use this only as a marginal-density statement on an ORIGINAL-coordinate product bank. It does **not** assert independence of the projected coordinates. If the source bank dimension equals the projected dimension, the needed endpoint follows directly by an orthogonal determinant-one change of variables and is at least as strong.

Thus, for a unit vector `u` on a genuine source bank,

`||p_(u dot X)||_infinity <= sqrt(2)`,                              (2.1)

and for orthonormal `v,z` on another genuine source bank,

`||p_(v dot X, z dot X)||_infinity <= 2`.                           (2.2)

### 2.2 Rudelson--Vershynin matches the newest partner's stable-rank branch, but not the endpoint here

M. Rudelson and R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492 / IMRN 2015, treats linear images of vectors with independent coordinates under one-dimensional concentration/density hypotheses, with no moment or iid requirement. The newest fleet02/B18 report source-checks Theorem 1.2 and Corollary 8.5 and spends them, via fleet03/B18, when the crossing block has floored stable rank at least two.

The exact rank-one crossing treated below has floored stable rank one, so that primary route is genuinely unavailable there. The replacement is the source-valid one-plus-two dimensional marginal packet (2.1)--(2.2).

### 2.3 A primary quadratic-form regularity theorem with narrower hypotheses

Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, assumes iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field. Those hypotheses do not cover arbitrary non-iid fragmented cap-one densities. I therefore do not use that theorem to claim the owner target.

A targeted literature/repository audit did not locate an exact published theorem matching every owner quantifier. This is only a hypothesis comparison, not a novelty claim. The nonlinear scalar/dependent-pair receiver used below is explicitly a prior fleet theorem.

## 3. Source-pinned partner inputs

### 3.1 Newest designated partner: zero-self stable-rank / fifth-volume / rank-four funnel

Newest completed fleet02/B18 source at the time of this report:

- `yspennstate/math-open-problems@54408b41c02166dbb98ac96c14635fd1ba353f27`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260924T020253Z-r11/REPORT.md`.

For an ORIGINAL-coordinate split

`A=[[0,B],[B^T,C]]`,                                                (3.1)

put `s=s_3(A)`, `c=||C||op`, `beta=||B||op`. Among its proved implications:

1. if `c<=s/2`, then

`||p_Q||infinity <= 2 sqrt(2 pi)/s`;                               (3.2)

2. if `beta<s/2`, then the complement satisfies `s_3(C)>s/2` (an exact affine-recursive structural branch, not counted as paid there);
3. if `beta>=s/2`, the stable-rank and fifth-volume mechanisms either pay the form or force a rank-at-most-four crossing carrier plus an explicitly retained residual; in particular an exact rank-one `B` has stable rank one and zero fifth cross volume, so it lands in that retained low-rank survivor rather than being discarded.

### 3.2 Earlier completed fleet02/B18 analytic receiver

Canonical source:

- `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`;
- theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`.

If `S` has density cap `K`, is genuinely independent of a possibly dependent pair `(Y,Z)` having joint-density cap `M`, and

`T=2 beta S Y + alpha Y^2 + 2 delta Y Z + gamma Z^2`,               (3.3)

with `beta gamma !=0`, then

`||p_T||infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`         (3.4)

No independence between `Y` and `Z` is required.

## 4. Main theorem — exact rank-one cross with a two-dimensional complement-active plane

### `QFORM-ZEROSELF-RANK1-ACTIVEPLANE-CLOSURE-v1`

Let the **full ORIGINAL coordinate set** split as `I disjoint_union J`, and write

`A=[[0,B],[B^T,C]]`,                                                (4.1)

where `A` is real symmetric. Assume

`rank(B)=1`,                                                        (4.2)

and write

`B=sigma u v^T`, `sigma>0`, `||u||=||v||=1`,                       (4.3)

with `u` supported on the original `I` bank and `v` on the original `J` bank. Assume the entire complement curvature lives in at most one further physical direction beyond `v`:

`dim(span{v}+ran C) <=2`.                                          (4.4)

If

`s:=s_3(A)>0`,                                                      (4.5)

then, for arbitrary independent original-coordinate probability densities bounded by one,

`boxed: ||p_(X^T A X)||infinity
        <= 3*2^(5/3)/s
        = 9.524406311809198.../s.`                                 (4.6)

The same proof permits affine terms lying in the active range

`span{u} direct_sum (span{v}+ran C)`,                              (4.7)

because those are removed by deterministic translation of the retained scalar/pair. No claim is made for arbitrary affine directions outside (4.7).

### Proof

Because `s_3(A)>0`, the active complement space in (4.4) must actually be two-dimensional; otherwise (4.1)--(4.3) would have rank at most two. Choose a unit vector `z perpendicular v` such that

`V=span{v,z}=span{v}+ran C`.                                       (4.8)

Since `C` is symmetric and `ran C subset V`, it annihilates `V^perp`. In the orthonormal basis `(v,z)` write

`C|_V=[[alpha,delta],[delta,gamma]]`.                              (4.9)

The matrix `A` vanishes on `u^perp` inside the `I` bank and on `V^perp` inside the `J` bank. Its complete nonzero carrier is therefore

`H=[[0,sigma,0],
    [sigma,alpha,delta],
    [0,delta,gamma]]`                                               (4.10)

in the deterministic orthonormal frame `(u,v,z)`. This frame is used only for matrix algebra, not to declare transformed random coordinates independent.

Expanding the determinant along the first row gives the twist-free identity

`det H = -sigma^2 gamma`.                                          (4.11)

The global matrix has rank at most three and (4.5) forces rank exactly three. Hence its three nonzero eigenvalues are precisely the eigenvalues of `H`, and all have modulus at least `s`. Therefore

`|sigma^2 gamma|
 =|det H|
 =prod_{r=1}^3 |mu_r(A)|
 >=s^3`.                                                           (4.12)

Now define the actual random aggregates

`S=u^T X_I`, `Y=v^T X_J`, `Z=z^T X_J`.                             (4.13)

The two banks are disjoint sets of ORIGINAL independent coordinates, so `S` is genuinely independent of the entire pair `(Y,Z)`. I do **not** assert that `Y,Z` are independent. By the primary LPP theorem,

`K:=||p_S||infinity<=sqrt(2)`,                                     (4.14)

`M:=||p_(Y,Z)||infinity<=2`.                                       (4.15)

The quadratic form is exactly

`X^TAX
 =2 sigma S Y + alpha Y^2+2 delta YZ+gamma Z^2`.             (4.16)

Apply the completed fleet02/B18 receiver (3.4), using (4.12):

`||p_(X^TAX)||infinity
 <=3(2*2*sqrt(2))^(2/3)|sigma^2 gamma|^(-1/3)
 <=3*2^(5/3)/s`.                                                   (4.17)

This proves (4.6). QED.

## 5. Concrete application to the newest partner funnel

The theorem closes a precise chamber that the newest fleet02/B18 structural result isolates but does not itself pay.

For the class (4.1)--(4.5), put `c=||C||op` and `beta=sigma`.

- If `c<=s/2`, the **newest partner report** gives the actual whole-line inequality

  `boxed: ||p_Q||infinity <=2 sqrt(2pi)/s
          =5.013256549262001.../s.`                                (5.1)

- If `c>s/2` and `beta<s/2`, the newest partner funnel sends the matrix to its affine-recursive complement branch `s_3(C)>s/2`. The present active-plane theorem pays that same matrix directly by (4.6), so no recursion is needed inside this chamber.

- If `c>s/2` and `beta>=s/2`, exact `rank(B)=1` means the partner's floored stable-rank gate is one and `Z_5=e_5(B^TB)=0`. Its rank-four survivor is therefore exact here: one may take `B_4=B`, `E=0`. Again (4.6) pays the retained survivor without deleting any residual.

Thus the combination gives the exhaustive source-valid statement

`boxed:
 rank(B)=1,
 dim(span{v}+ran C)<=2,
 s_3(A)=s>0
 ==> ||p_Q||infinity <=9.524407/s.`                                (5.2)

This is an actual application of the newest designated-partner funnel, not merely a parallel theorem.

## 6. Rank-one complement corollary and the partner's literal boundary model

If additionally

`rank(C)=1`,                                                        (6.1)

then (4.4) is automatic. Hence every exact zero-self two-bank matrix with `rank(B)=rank(C)=1` and `s_3(A)>0` obeys (4.6), even at the boundary `||C||op=s` where the earlier complement-norm funnel no longer forces a second cross singular direction.

The literal endpoint highlighted in the preceding fleet02/B18 report is

`A_*=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (6.2)

with spectrum `{-1,1,1}` and

`Q_*=2X_1X_2+X_3^2`.                                               (6.3)

Here the retained scalar is the original coordinate `X_1`, so `K<=1`, and the retained pair `(X_2,X_3)` is itself a two-coordinate original product density, so `M<=1`. Formula (3.4) therefore sharpens (4.6) on this exact family to

`boxed:
 ||p_(Q_*)||infinity
 <=3*2^(2/3)
 =4.762203155904598... .}`                                         (6.4)

This is a whole-line estimate, not only the one-sheet half-line estimate available from the earlier ruled-level-set theorem.

### Continuity for this literal endpoint only

Continuity can be tracked separately here without any disputed conditional step. The variables

`U=2X_1X_2`, `V=X_3^2`                                             (6.5)

are independent and each has an `L^1` probability density (possibly unbounded at isolated values). Therefore

`p_(Q_*)=p_U*p_V in C_0(R)`.                                       (6.6)

So the exact endpoint (6.2) has a continuous density vanishing at infinity, and that representative satisfies (6.4). I do **not** promote continuity to the entire active-plane theorem from this argument.

## 7. Optional source-dimension refinements

The universal constant in (4.6) records only the worst LPP marginal caps. The same proof immediately gives:

- if the `I` bank is one original coordinate, `K<=1`, hence

  `||p_Q||infinity <=3*4^(2/3)/s=7.559526299369239.../s`;           (7.1)

- if the active `J` bank consists of exactly two original coordinates, then `M<=1`, hence

  `||p_Q||infinity <=6/s`;                                         (7.2)

- if both occur, the literal three-original-coordinate bound is

  `||p_Q||infinity <=3*2^(2/3)/s=4.762203155904598.../s`.           (7.3)

These are just source-cap refinements of the same proved receiver.

## 8. What remains unpaid

The latest partner's `QFORM-ZEROSELF-HS-D5-RANK4-FUNNEL-v1` leaves a retained rank-at-most-four crossing carrier plus a nonzero residual in its crossing-heavy survivor. The theorem here closes the exact `rank(B)=1` chamber **only when all complement curvature interacting with that cross direction lies in a two-dimensional active source plane**.

The genuinely unpaid continuation is therefore more precise:

1. `B` is only near rank one (or near rank four), with a small but nonzero tail that cannot be deleted for unbounded rough inputs; and/or
2. the complement curvature `C` sends the cross direction into a source-active space of dimension at least three, so no single dependent pair captures all same-bank curvature.

One cannot condition away those additional source directions and assume the retained projection cap survives; the live conditional-density corrections rule that out. A useful next step is a dependent `1+k` receiver or a product-preserving bank decomposition that pays the extra complement directions jointly with the rank-one cross, while retaining the small crossing tail exactly.

## 9. Source and status ledger

- Fresh control consumed through brain main at least `9bb93c358fe585abc0f6c296b25bf9ed05903921`, owner control revision `2026-09-22.15`, programme revision `2026-09-22.5`.
- Owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` acknowledged.
- Latest designated partner actually applied: fleet02/B18 scientific commit `54408b41c02166dbb98ac96c14635fd1ba353f27`.
- Completed fleet02/B18 analytic receiver actually applied: `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`.
- Primary external theorem actually applied: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.
- Primary theorem audited for newest partner scope: Rudelson--Vershynin, arXiv:1402.4492.
- Primary quadratic-form regularity theorem checked but not applicable to full owner quantifiers: Herry--Malicet--Poly, arXiv:2303.09488.
- No exact full-QFORM prior solution was found in this targeted audit; no novelty claim is made from that search.
- Full QFORM status: **OPEN**.
