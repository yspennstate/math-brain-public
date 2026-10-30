# fleet02/B20 — three-pivot physical packet closure and aggregate rank-three curvature budget

**Run:** `20260922T152608Z-fleet02-B20-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Proof closure and keeper / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source pins

The target remains the full arbitrary-dimensional statement: if the coordinates `X_i` are independent real random variables with densities bounded by one and `A` is real symmetric with at least three eigenvalues of modulus at least one, then the law of `Q=X^TAX` should have one universal finite essential-supremum density bound. No post-rotation independence, support regularity, moments, Gaussianity, or log-concavity is assumed. Continuity is separate.

The newest completed assigned-partner package visible at the source refresh used here is fleet03/B20 run `20260922T141139Z-fleet03-B20-QFORM-r11`, canonical source

`yspennstate/math-open-problems@7530e8c6ffd7284eb9c8acf1d79f36c335bf4fd6:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T141139Z-fleet03-B20-QFORM-r11/REPORT.md`.

Its exact scalar-pivot reserve is the starting expression below: if

`M=[[a,b^T],[b,C]]`, `a!=0`, `S=C-bb^T/a`, `K=||b||_2/|a|`,

and `s_3(M)>=1`, then `s_2(S)>=(1+K)^(-2)`. The proof is the exact congruence

`M=L diag(a,S)L^T`, `L=[[1,0],[b/a,I]]`,

with `||L||<=1+K`.

I also use the completed fleet03/B06 two-stage physical-pivot endpoint package

`yspennstate/math-open-problems@8624700dc9342807bbdf427e271fffcc518a0315:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T151714Z-fleet03-B06-qform-r12/REPORT.md`.

Its analytic proof gives, for an exact three-variable nonsingular quadratic matrix with two nonzero successive physical pivots, the endpoint constant `C_3<94.356`. The spectral threshold `|lambda_j|>=1` is used there only after the endpoint formula to replace `|det Lambda|` by one; the kernel proof itself is homogeneous and remains valid for arbitrary nonzero eigenvalues with the determinant factor retained. I rederive the needed conditional form in Section 3 rather than assuming independence after any rotation.

Corrections retained throughout: no law-uniform pointwise quadratic-phase decay; no unrestricted fiber-supremum step; no conditional density cap manufactured by sum/difference conditioning; no post-spectral-rotation independence; no universal fixed physical triple/minor lower bound; no absolute phase-Wiener criterion.

## 2. Strongest conditional end-to-end picture before the new step

The current assembly has several genuine target-level branches:

1. the high-stable-rank physical off-diagonal branch is already bounded by a completed current package;
2. fleet03/B20 closes a scalar-pivot branch whenever the exact Schur residual has the required full-range diffuseness, and its fresh conditioned-whitened addendum closes another localization branch continuously;
3. the preceding B20 run showed that, in a minimum-dimensional counterexample, a heavy diagonal-dominated first pivot cannot simply disappear below the partner reserve scale;
4. cross-dominated heavy rows feed the product-provenant aggregate/hyperbolic mechanisms, but their correlation with the residual is not yet universally paid.

The first unpaid universal issue was therefore a vague low-stable-rank three-way packet extraction. Sections 3--5 make one large part exact: a **three-step physical Schur chain of large-spectrum, diagonal-dominated rows already closes the full arbitrary-spectrum target**. Consequently a failed chain has a sharply described stopping certificate: large-spectrum diffuseness or a uniformly strong physical cross export.

## 3. Arbitrary-spectrum closure from one paid physical `3x3` packet

### Theorem 3.1 — `QFORM-PHYSICAL-3X3-CONDITIONAL-ENDPOINT-v1`

Let `A` be any real symmetric `n x n` matrix, with no rank restriction. Let `I=(i_1,i_2,i_3)` be three distinct original coordinates and let

`D=A[I,I]`.

Write, in this order,

`a=D_11`,

`d=det D[{1,2},{1,2}]`.

Assume `a!=0`, `d!=0`, and `det D!=0`. For arbitrary independent original coordinates with densities at most one, the law of `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity <= C_3 [ |a| |d|^2 |det D| ]^(-1/8)`,             (3.1)

where the source constant satisfies `C_3<94.356`.

No condition is imposed on the spectrum outside this physical triple.

#### Proof

Condition on every original coordinate outside `I`. For a fixed outside value `w`,

`Q = x^T D x + 2 ell(w)^T x + c(w)`,                               (3.2)

where `x=(X_i)_{i in I}` still has three independent one-dimensional densities bounded by one. Since `D` is invertible, translate

`y=x+D^(-1)ell(w)`.

This is a coordinatewise deterministic translation for fixed `w`; it preserves independence and the unit density caps. Equation (3.2) becomes

`Q = y^T D y + c'(w)`.                                               (3.3)

Now rerun the two-stage physical-pivot proof of fleet03/B06 on the **three physical variables**. If `D=R Lambda R^T`, then `R` is a `3x3` orthogonal matrix. Hence for its first two rows

`Delta_12=||r_1 wedge r_2||^2=1`,

and `|det Lambda|=|det D|`. The source proof therefore gives the conditional endpoint

`||p_(Q|w)||_infinity <= C_3 [ |a| |d|^2 |det D| ]^(-1/8)`.          (3.4)

The right-hand side is independent of `w`. Averaging the conditional laws over the outside product measure preserves the same essential-supremum bound, proving (3.1). QED.

**Important scope gain.** The exact-rank-three restriction of the source endpoint is no longer an extra-spectrum debt for a paid physical packet: arbitrary additional eigenvalues and arbitrary cross-terms to outside coordinates are frozen as linear/constant terms before the three-variable estimate is used.

Continuity is not asserted by this argument.

## 4. Partner reserve iterated: a three-step diagonal-dominated chain closes the full target

The fleet03/B20 congruence has the following scaled form.

### Lemma 4.1 — scaled scalar-Schur reserve

Suppose a real symmetric `M` satisfies `s_r(M)>=mu>0` for some `r>=2`. For a physical scalar pivot

`M=[[a,b^T],[b,C]]`, `a!=0`, `S=C-bb^T/a`, `K=||b||/|a|`,

one has

`s_(r-1)(S) >= mu/(1+K)^2`.                                         (4.1)

#### Proof

The exact partner congruence gives

`s_r(diag(a,S)) >= mu/(1+K)^2`.

The scalar block `a` can account for at most one of the `r` singular values above that level, so the Schur block accounts for at least `r-1`. QED.

This is the exact fleet03/B20 expression applied at arbitrary scale and at the next two Schur depths.

### Lemma 4.2 — a large-spectrum diagonal-dominated row pays a pivot

Let `P_mu=1_{ {|M|>=mu} }`. If for a physical row `i`

`(P_mu)_ii >= 1/32`                                                   (4.2)

and

`K_i:=||M_(i,-i)||_2/|M_ii| <=1`,                                    (4.3)

then

`|M_ii| >= mu/8`.                                                     (4.4)

#### Proof

Functional calculus gives `M^2 >= mu^2 P_mu`, hence

`M_ii^2+||M_(i,-i)||_2^2=(M^2)_ii >= mu^2/32`.

Under (4.3), the left side is at most `2 M_ii^2`, giving (4.4). QED.

### Theorem 4.3 — `QFORM-THREE-PIVOT-LARGE-SPECTRUM-CHAIN-v1`

Assume the full target spectral hypothesis `s_3(A)>=1`. Put `M_0=A`, `mu_0=1`. Suppose one can choose distinct original coordinates successively so that:

- at stage 1, a row of `M_0` obeys (4.2)--(4.3) with `mu_0=1`;
- after taking its scalar Schur complement `M_1`, a row of `M_1` obeys (4.2)--(4.3) with `mu_1=1/4`;
- after the second scalar Schur complement `M_2`, a row of `M_2` obeys (4.2)--(4.3) with `mu_2=1/16`.

Then the law of `Q=X^TAX` has an essentially bounded density with the explicit universal bound

`||p_Q||_infinity < 1800`.                                           (4.5)

#### Proof

Let the three successive scalar pivots be `p_1,p_2,p_3`. Lemma 4.2 gives

`|p_1|>=1/8`.                                                         (4.6)

Lemma 4.1 with `r=3` and `K<=1` gives `s_2(M_1)>=1/4`. Applying Lemma 4.2 at the next stage gives

`|p_2|>=1/32`.                                                        (4.7)

Lemma 4.1 again, now with `r=2`, gives `s_1(M_2)>=1/16`; the third large-spectrum diagonal-dominated row therefore gives

`|p_3|>=1/128`.                                                       (4.8)

Let `D` be the physical `3x3` principal block of the three chosen coordinates in the chosen pivot order. Successive scalar Schur identities inside a principal block give exactly

`a=p_1`, `d=p_1p_2`, `det D=p_1p_2p_3`.                              (4.9)

Therefore the packet in Theorem 3.1 obeys

`|a| |d|^2 |det D|
 = |p_1|^4 |p_2|^3 |p_3|
 >= 2^(-34)`.                                                         (4.10)

Theorem 3.1 now yields

`||p_Q||_infinity <= C_3 2^(34/8)
 <94.356*2^(17/4)
 <1800`.                                                              (4.11)

QED.

This theorem is sign-free: the two-stage curved endpoint pays the alternating-sign case that a naive same-sign-pair argument would miss. It also allows arbitrary extra spectral directions because Section 3 conditions them away only after a physical packet has been produced.

### Corollary 4.4 — exact stopping certificate

At any stage with `s_r(M)>=mu` (`r=3,2,1`) where the next pivot required by Theorem 4.3 cannot be selected, at least one of the following holds:

1. **large-spectrum diffuse:**
   `max_i (1_{ {|M|>=mu} })_ii <1/32`; or
2. **large-spectrum cross-export:** there is a row with
   `(P_mu)_ii>=1/32` and `K_i>1`, and then necessarily
   `||M_(i,-i)||_2 >= mu/8`.                                         (4.12)

Indeed in the second case the same row-energy inequality gives `a^2+||b||^2>=mu^2/32`, while `||b||>|a|`, so `||b||^2>=mu^2/64`.

Thus the previous three-way packet debt is sharpened: **a persistent diagonal-dominated large-spectrum localization cannot survive three Schur levels.** If the chain fails, the proof must spend either genuine diffuseness of the large spectral subspace or a source-realizable physical cross row of strength at least `mu/8`. The remaining analytic difficulty is that present diffuse theorems are formulated for the entire range frame, while (4.12) gives a marginal linear aggregate whose correlation with the residual cannot be discarded.

## 5. Exact rank-three aggregate curvature before reciprocal inversion

The distributed regime defeats selection of one physical minor. The next theorem identifies a dimension-free **sum-before-inversion** currency in the exact-rank-three model.

Let

`A=U Lambda U^T`, `U^TU=I_3`,                                       (5.1)

with all three diagonal entries of `Lambda` nonzero. Write the physical rows of `U` as `u_i in R^3`, and for a fixed `i` put

`ell_i=||u_i||^2`, `a_i=A_ii`,

`Delta_ik=||u_i wedge u_k||^2`,

`d_ik=A_ii A_kk-A_ik^2`.                                             (5.2)

### Theorem 5.1 — `QFORM-RANK3-PLUECKER-CURVATURE-BUDGET-v1`

For every fixed row with `ell_i>0`,

`sum_(k!=i) Delta_ik = 2 ell_i`,                                     (5.3)

`sum_(k!=i) d_ik = a_i tr(Lambda)-u_i^T Lambda^2 u_i`,               (5.4)

and, omitting zero-`Delta` terms,

`boxed:
 sum_(k:Delta_ik>0) d_ik^2/Delta_ik
 >= [a_i tr(Lambda)-u_i^T Lambda^2 u_i]^2/(2 ell_i).
`                                                                         (5.5)

If additionally `|lambda_j|>=1` and `a_i=0`, then

`boxed:
 sum_(k:Delta_ik>0) d_ik^2/Delta_ik >= ell_i/2.
`                                                                         (5.6)

More generally, if for some `0<=theta<1`

`|a_i tr(Lambda)| <= theta u_i^T Lambda^2 u_i`,                       (5.7)

then

`sum d_ik^2/Delta_ik >= (1-theta)^2 ell_i/2`.                         (5.8)

#### Proof

Since `sum_k u_k u_k^T=I_3`,

`sum_k ||u_i wedge u_k||^2
 = sum_k [ell_i||u_k||^2-(u_i.u_k)^2]
 =3ell_i-ell_i
 =2ell_i`,

proving (5.3).

Also

`sum_k A_kk=tr(Lambda)`,

and

`sum_k A_ik^2=(A^2)_ii=u_i^T Lambda^2 u_i`.

Therefore summing `d_ik=a_iA_kk-A_ik^2` gives (5.4). If `Delta_ik=0`, then `u_k` is parallel to `u_i`, and the corresponding `d_ik` is exactly zero, so no term is lost by restricting to positive `Delta`.

Weighted Cauchy--Schwarz gives

`(sum_k d_ik)^2
 <= (sum_(Delta>0) d_ik^2/Delta_ik)(sum_k Delta_ik)`.

Insert (5.3)--(5.4) to obtain (5.5).

If `a_i=0`, then the numerator in (5.5) is `(u_i^T Lambda^2u_i)^2`. Under `|lambda_j|>=1`,

`u_i^T Lambda^2u_i>=ell_i`,

which gives (5.6). Under (5.7), the absolute numerator in (5.5) is at least `(1-theta)u_i^T Lambda^2u_i`, proving (5.8). QED.

### Why this is the right distributed currency

For the heavy-isotropic branch of current rank-three work, `ell_i>1/32` and `a_i=0` imply the completely explicit aggregate payment

`sum d_ik^2/Delta_ik >1/64`.                                         (5.9)

For the trace-balanced near-isotropic collar with `theta=1/2`, one gets

`sum d_ik^2/Delta_ik >1/256`.                                        (5.10)

This does **not** force one local B06 certificate to be uniformly large; the flat-bank counterexamples correctly spread the payment over many tiny channels. Instead (5.5) proves that the geometry itself has not lost curvature. The missing step is analytic: consume this aggregate before taking reciprocal local pivot factors.

## 6. First unpaid universal implication after this run

The full conjecture is still open. The first unpaid implication is now the following source-valid closure, not a search for one fixed minor.

### `QFORM-HIGH-SPECTRAL-DIFFUSE-OR-CROSS-AGGREGATE-CLOSURE-v1`

Let a current physical Schur residual `M` arise after zero, one, or two legitimate original-coordinate scalar pivots, with

`s_r(M)>=mu`, `r in {3,2,1}`, and `mu in {1,1/4,1/16}`

at the corresponding stage. Prove a dimension-free endpoint whenever Theorem 4.3 stops because either

- `max_i (1_{ {|M|>=mu} })_ii<1/32`, **without upgrading this to an unsupported entire-range diffuseness assumption**, or
- some heavy large-spectrum row has the source-realizable physical cross export `||M_(i,-i)||>=mu/8`, **without replacing its marginal projection cap by a conditional independence statement**.

A quantitatively sufficient exact-rank-three subgoal is an averaged two-stage curved-fiber estimate whose right side depends on

`E_i=sum d_ik^2/Delta_ik`

before inversion. Theorem 5.1 guarantees `E_i>=ell_i/2` at an isotropic heavy row and `E_i>=(1-theta)^2ell_i/2` in the trace-balanced near-isotropic collar. Such an averaged estimate would close the distributed heavy-isotropic wall that defeats every one-triple selection rule.

This is a strictly sharper residual than the prior generic low-stable-rank packet-extraction statement: a three-deep diagonal-dominated high-spectrum chain is now fully paid with a universal `<1800` density constant, arbitrary extra spectrum included.

## 7. Status

`ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN`.

No full QFORM proof is claimed. No continuity claim is made for Sections 3--5. The new target-level branch is arbitrary-dimensional and arbitrary-spectrum; the aggregate curvature theorem is exact-rank-three and is explicitly labeled as such.
