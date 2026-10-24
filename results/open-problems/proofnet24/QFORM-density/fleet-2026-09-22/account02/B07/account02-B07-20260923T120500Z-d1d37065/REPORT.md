# account02/B07 — fixed-anchor determinant packets by Plancherel, and one-sided coordinate-core extraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / complementary constructions  
Run: `account02-B07-20260923T120500Z-d1d37065`  
Status: **NEW SUPPORTING THEOREM + PARTNER APPLICATION + STRUCTURAL OBSTRUCTION; FULL QFORM OPEN**.

The unrestricted theorem remains open. No moment, bounded-support, log-concavity, identical-law, diagonal-basis, or post-rotation independence hypothesis is used. All coordinate conditioning below is on ORIGINAL physical coordinates. Continuity is asserted only where Fourier inversion is integrable.

The first unpaid implication at entry was the designated partner's

`QFORM-COMMON-BANK-R1-AND-NONZERO-ANCHOR-RECEIVER-v1`:

account03/B07 had compiled two physical stars into either aggregate second-minor mass or a common-bank rank-one tube. Its aggregate-E2 density theorem covered an exactly zero two-anchor block, while the genuinely nonzero anchor block and arbitrary same-bank curvature remained unpaid.

The central observation here is that one should not Schur-complete the anchors. Instead, integrate the anchor variables in `L^2` and retain the entire determinant packet in the density of the physical coefficient projection.

---

## 1. Fixed-anchor volume theorem

### Theorem 1 — `QFORM-FIXED-ANCHOR-VOLUME-PLANCHEREL-v1`

Let `H,J` be disjoint sets of ORIGINAL coordinates, with `|H|=k`, and condition on every coordinate outside `H union J`. Write the resulting quadratic polynomial as

`Q(x,z)=x^T B x + 2 x^T G z + a^T x + R(z)`,                    (1.1)

where

* `x=(X_h)_(h in H) in R^k` has independent coordinate densities at most one;
* `z=(X_j)_(j in J)` also has independent coordinate densities at most one and is independent of `x`;
* `B` is an arbitrary real symmetric `k x k` matrix;
* `G=A[H,J]` is the physical `k x |J|` coefficient matrix;
* `R` is an arbitrary quadratic polynomial in `z` (so every same-bank quadratic coefficient is retained).

Assume `G` has full row rank and put

`Z_k := det(G G^T) = sum_{T subset J, |T|=k} det(G[:,T])^2`.     (1.2)

Then for every real `t != 0`, uniformly in all conditioned coordinate values,

`boxed: |phi_Q(t)| <= 2^(k/4) pi^(k/2) Z_k^(-1/4) |t|^(-k/2).`   (1.3)

Consequently, for every `k>=3`, `Q` has a continuous density and

`boxed: ||p_Q||_infinity <= sqrt(2) * k/(k-2) * Z_k^(-1/(2k)).`  (1.4)

In particular, for three fixed physical anchors,

`boxed: ||p_Q||_infinity <= 3 sqrt(2) Z_3^(-1/6).`               (1.5)

For two anchors the decay is critical for density but gives the curvature-safe half-Riesz estimate

`boxed: H_(1/2)(Q):=sup_s E|Q-s|^(-1/2) <= 2^(11/4) Z_2^(-1/8).` (1.6)

The conclusions remain valid for the full ambient form because all outside-coordinate conditioning is uniform.

### Proof

Absorb the anchor linear term into

`U := G z + a/2 in R^k`.

Let `Sigma=(G G^T)^(1/2)` and `R_0=Sigma^(-1)G`, so `R_0 R_0^T=I_k`. The required pinned e5 Fourier report, Section 2.4, records and checks the Livshyts-Paouris-Pivovarov projection-density theorem: a `k`-dimensional orthogonal projection of a product density with one-dimensional caps one has density at most `2^(k/2)` (and if `|J|=k`, the direct change-of-variables bound is even smaller). Therefore

`||p_U||_infinity <= 2^(k/2) det(GG^T)^(-1/2)
                   = 2^(k/2) Z_k^(-1/2).`                      (1.7)

For fixed `t`, define

`g_t(x) := [prod_(h in H) f_h(x_h)] exp(i t x^T B x)`.

Push the complex measure `exp(i t R(z)) prod_j f_j(z_j) dz` forward by `z -> U`. It has a density `eta_t(u)` with

`|eta_t(u)| <= p_U(u)` a.e.                                      (1.8)

because its Radon-Nikodym multiplier is a conditional expectation of a unit-modulus phase. Hence

`||eta_t||_2^2 <= ||p_U||_infinity int p_U = ||p_U||_infinity`,

so from (1.7)

`||eta_t||_2 <= 2^(k/4) Z_k^(-1/4).`                            (1.9)

With Fourier convention `hat g(xi)=int g(x)e^(i<xi,x>) dx`,

`phi_Q(t) = int_(R^k) hat(g_t)(2 t u) eta_t(u) du`.              (1.10)

Cauchy-Schwarz and Plancherel give

`||hat(g_t)(2t .)||_2
 = (2|t|)^(-k/2) ||hat(g_t)||_2
 = (2|t|)^(-k/2) (2pi)^(k/2) ||g_t||_2
 <= pi^(k/2) |t|^(-k/2)`,                                      (1.11)

because `f_h<=1` implies `int f_h^2 <= int f_h=1`, and therefore `||g_t||_2<=1`. Multiplying (1.9) and (1.11) proves (1.3).

For `b=k/2>1`, set

`K=2^(k/4) pi^(k/2) Z_k^(-1/4)`.

Using `|phi|<=min(1,K|t|^-b)`,

`int_R min(1,K|t|^-b) dt = 2b/(b-1) K^(1/b)`.

Fourier inversion and `K^(1/b)=sqrt(2) pi Z_k^(-1/(2k))` give exactly (1.4). This also gives continuity.

For `k=2`, (1.3) is

`|phi(t)| <= pi sqrt(2) Z_2^(-1/4) |t|^-1`.

Apply the required pinned e5 Lemma 4.1, which for `|phi|<=min(1,K|t|^-1)` gives

`H_(1/2) <= 8 K^(1/2)/sqrt(2pi)`.

Substituting `K=pi sqrt(2) Z_2^(-1/4)` yields (1.6). QED.

### Why this is a determinant-packet theorem rather than a single-minor theorem

Equation (1.2) is Cauchy-Binet. The receiver spends the entire packet

`sum_T det(G[:,T])^2`

before taking any reciprocal quantity. No particular `k x k` coordinate minor is inverted or even required to be macroscopic.

---

## 2. One-sided determinant-tail coordinate extraction

The theorem yields a stronger bounded-support receiver than the previous two-sided physical-core argument: only one side of the third-volume packet has to concentrate.

Let `M=A[I,J]` be any physical cross block and define

`Z_3(M)=sum_(|S|=|T|=3) det(M[S,T])^2`.

For each row triple `S subset I`, put

`Z_S := sum_(|T|=3) det(M[S,T])^2
     = det(M[S,:] M[S,:]^T)`.                                  (2.1)

Then `Z_3(M)=sum_S Z_S`. Normalize `w(S)=Z_S/Z_3` and let

`alpha_i=P_w(i in S)`.

### Corollary 2 — `QFORM-ONE-SIDED-ROW-TAIL-RECEIVER-v1`

Suppose a physical row support `R subset I`, `m=|R|>=3`, satisfies

`delta_R := sum_(i notin R) alpha_i < 1`.                       (2.2)

Then

`boxed: ||p_Q||_infinity
 <= 3 sqrt(2) [ C(m,3) / ((1-delta_R) Z_3(M)) ]^(1/6).`          (2.3)

No column-support condition, operator-norm bound, or principal spectral core is required.

### Proof

By the union bound under `w`,

`P_w(S not subset R) <= sum_(i notin R) P_w(i in S)=delta_R`.

Therefore

`sum_(S subset R) Z_S >= (1-delta_R) Z_3(M)`.                   (2.4)

Among the `C(m,3)` row triples inside `R` there is one `S_*` for which

`Z_(S_*) >= (1-delta_R) Z_3(M)/C(m,3)`.                         (2.5)

Condition on all ORIGINAL coordinates in `I\S_*` and every outside coordinate. Keep the three ORIGINAL anchors `S_*` and the full column bank `J`. Theorem 1 with `k=3` spends the whole column-minor packet `Z_(S_*)`, proving (2.3). QED.

This is a legitimate selection of a **row packet**, not a universally good individual minor. Column determinant weight remains fully aggregated through conditioning.

---

## 3. Designated partner account03/B07 applied

The latest compatible completed partner result read in this run is

`yspennstate/math-open-problems@7ad9327f11c39bd465780bd1539d52de9feaacdd`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T110409Z-account03-B07-qform-r29/REPORT.md`.

It proves a joint four-color compiler for two physical star rows. With

`H = 1.1533650070389015e-6`,

its aggregate branch supplies either

* common-bank `Z_2 >= H^4/4096`, or
* transverse-bank `Z_2 >= H^4/64`.

Its previous density receiver required the physical two-anchor quadratic block to be exactly zero. Theorem 1 removes that exact-zero restriction at the fractional-potential level, while keeping **arbitrary** anchor block and arbitrary within-bank curvature:

common packet:

`boxed: H_(1/2)(Q) <= 2^(17/4) H^(-1/2)
                       = 17717.15954892967...`;                 (3.1)

transverse packet:

`boxed: H_(1/2)(Q) <= 2^(7/2) H^(-1/2)
                       = 10534.686096612784...`.                (3.2)

Thus a genuinely nonzero two-anchor block no longer destroys the aggregate-E2 resource merely by being nonzero. What remains is exactly the missing half power needed for density, and that half power must come from genuine third-spectral currency rather than from the two-star packet alone.

The partner's common-bank rank-one tube, where its `E_2` lower bound is intentionally absent, remains separate.

---

## 4. Exact target-class stress: bounded physical cores are not necessary

The next family is inside the full target and the standard no-pivot geometry, but every fixed-cardinality physical principal core vanishes. It is paid directly by the new row-packet theorem.

For an integer `m>=1`, take three physical anchors and three disjoint leaf banks of size `m`. Let `p_1,p_2,p_3` be the three flat unit vectors, each equal to `m^(-1/2)` on one bank and zero on the other two. Put

`G_m = [p_1^T; p_2^T; p_3^T]`,

and

`A_m = [[0_(3x3), G_m], [G_m^T, 0_(3m x 3m)]].`                (4.1)

Because `G_m G_m^T=I_3`, the nonzero spectrum of `A_m` is exactly

`{-1,-1,-1,1,1,1}`.                                             (4.2)

Hence this is a genuine target matrix.

All diagonal entries vanish. Every nonzero physical principal-pair determinant is `-1/m`; therefore for `m>128` the family lies in the usual `tau=1/128` no-pivot class.

For any fixed `M` and any physical coordinate set `K` with `|K|<=M`, the principal block has the form `[0,G';G'^T,0]` with at most `M` selected leaf edges, so

`||A_m[K,K]||_op = ||G'||_op <= ||G'||_F <= sqrt(M/m) -> 0`.    (4.3)

Thus no bounded-cardinality physical spectral core carries a fixed third singular/eigenvalue scale.

Nevertheless the fixed three-anchor determinant packet is

`Z_3 = det(G_m G_m^T)=1`.                                       (4.4)

Every nonzero individual `3x3` cross minor has magnitude only `m^(-3/2)`, but there are exactly `m^3` of them and their squared masses sum to one. Theorem 1 therefore gives, for arbitrary independent input densities at most one,

`boxed: ||p_(X^T A_m X)||_infinity <= 3 sqrt(2).`               (4.5)

This is the intended coordinate-minor lesson: neither a bounded principal core nor one good minor is the right invariant; a fixed physical row packet can retain all determinant volume across an arbitrarily large column bank.

---

## 5. Exact obstruction: two-anchor `E_2` alone cannot imply density

The half-Riesz endpoint in (1.6) cannot in general be promoted to a density theorem without spending a third spectral direction.

Fix `epsilon>0`. Take two physical anchors `x_1,x_2` and two disjoint leaf banks `P,Q`, each of size `m`. Let `p,q` be the flat unit vectors on `P,Q`, respectively, and define orthogonal coefficient vectors

`ell_1 = epsilon e_(x1) + epsilon^(-1) p`,

`ell_2 = epsilon e_(x2) + epsilon^(-1) q`.

Set

`A = ell_1 ell_2^T + ell_2 ell_1^T`.                             (5.1)

Then

`X^T A X = 2 (ell_1^T X)(ell_2^T X)`.                           (5.2)

The two linear forms depend on disjoint coordinate families, hence are independent. For centered unit-interval input densities each has a continuous density strictly positive in a neighborhood of zero. Therefore the product density has the standard logarithmic divergence at zero: if both factor densities are at least `c>0` on `[-delta,delta]`, then for `0<s<2delta^2`,

`p_(2L1L2)(s)
 >= (c^2/2) int_(s/(2delta))^delta dx/x
 =  (c^2/2) log(2delta^2/s) -> infinity.`                       (5.3)

Yet the physical two-anchor block is genuinely nonzero,

`A[{x1,x2},{x1,x2}] = [[0,epsilon^2],[epsilon^2,0]]`,            (5.4)

and the anchor-to-leaf coefficient matrix has orthonormal rows, so

`Z_2=det(GG^T)=1`.                                               (5.5)

Moreover all diagonal entries are zero and the largest physical principal-pair determinant magnitude is

`max(epsilon^4, 1/m, epsilon^(-4)/m^2)`.                        (5.6)

Thus, by first taking `epsilon` small and then `m` large, this rank-two family can be placed arbitrarily deep inside the same physical no-pivot geometry while keeping `Z_2=1` and a nonzero anchor block.

Its nonzero spectrum is only

`{+(epsilon^2+epsilon^(-2)), -(epsilon^2+epsilon^(-2))}`,        (5.7)

so it is **not** a QFORM counterexample: it lacks the required third large eigenvalue. It refutes only the local intermediate claim

`two-anchor aggregate E2 + arbitrary same-bank curvature + nonzero anchor block => bounded density`.

Any valid completion of the partner branch must explicitly spend the third spectral currency. Theorem 1 identifies `H_(1/2)` as a curvature-safe currency available before doing so.

---

## 6. Required e5 source applied and later-directory check

The required source was read at the pinned commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

* `RESULTS.md`;
* `FOURIER_ROUTE_REPORT.md`;
* `COUNTEREXAMPLE_SEARCH.md`.

The actual completed results used at equations are `FOURIER_ROUTE_REPORT.md` Section 2.4 (LPP product-projection density) in (1.7), and Lemma 4.1 (fractional potentials) in (1.6). The current directory was checked before publication: the Fourier report blob is unchanged from the pinned e5 version; later `RESULTS.md` records additional continuations but does not retract those two inputs. The current counterexample report also keeps the product-projection use and no-counterexample status at its stated scope.

---

## 7. First unpaid implication after this run

`QFORM-TWOANCHOR-HALFRIESZ-PLUS-THIRDVOLUME-UPGRADE-v1`:

Starting from either the designated partner's curvature-safe two-anchor bound (3.1)/(3.2), or an anchored third-volume packet with two fixed physical rows and a diffuse third row, obtain the missing half Fourier power **without** Schur-completing away the incoming determinant bank and without selecting a reciprocal individual minor. A natural target is a hybrid Plancherel/decoupling estimate that combines the fixed two-anchor `|t|^-1` bound with the determinant-weighted third-row currency. The rank-two obstruction (5.1) proves that the third-spectral input is logically necessary.

Separately, Corollary 2 pays every third-volume state whose row determinant law has marginal tail `<1` outside a bounded physical support; no column-support localization remains necessary in that branch.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open.
