SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T14:02:32.669933Z.
attacking: canonical slab-fiber cores plus spectral-range truncation: turn positive slab mass into an exact diffuse-range payment, a physical volume star, or a quantitatively large slab-scale residual.

# account03/B13 r27 — canonical fiber-score cores and range-or-star compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full continuity: **OPEN**.

## 1. Source-pinned inputs actually used

Fresh owner control at publication refresh: `yspennstate/math-research-brain@4b3c16d9d23e1ad11a01fe272754e57a5e1680c1`, OWNER CONTROL revision `2026-09-22.15`, QFORM only.

### 1.1 Designated partner account04/B13

Canonical mathematics:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

The result used here is the no-attainment purification theorem: for every bounded measurable product kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 = sup_{|E_i|=1} int_(prod E_i) K`,

and the right-hand supremum is unchanged if every `E_i` is required to be a bounded finite union of intervals. There is no attained-optimizer claim and no uniform bound on fragment count or diameter.

### 1.2 New account01/B13 invariant range theorem

Canonical proof:

`yspennstate/math-open-problems@9d9e2369ad137664a48b1b7c6d682ddaed62bcad`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T125929Z-account01-B13-qform-auto23/FRESNEL_RANGE_ADDENDUM.md`.

Let `U,V` be disjoint original-coordinate banks, `Z` all remaining independent coordinates, `R` a real symmetric leaf matrix of rank `d>=3`, and `B` the physical `U`-to-`V` cross matrix. If

`row(B) subset range(R)`

and the orthogonal range projection `P_R` satisfies

`max_j (P_R)_{jj} <= 1/2`,

then every full ambient form

`Q=F(U,Z)+sum_j[d_j V_j^2+c_j(Z)V_j]+2U^T B V+V^T R V`

has a continuous density and

`||p_Q||_inf <= M(R):=[4d/(d-2)] |pdet R|^(-1/d)`.                (1.1)

The proof is in original physical coordinates; the spectral/range factorization is used only inside deterministic Fourier algebra and does not assert independence after a rotation.

## 2. A stronger extremal-product reduction: near-bathtub swap stability

Fix a real symmetric target matrix `A` and an interval `J`. Put

`K(x)=1_{x^T A x in J}`

and let

`M_*=sup P_f(X^TAX in J)`                                         (2.1)

where the supremum is over all independent cap-one mass-one marginals.

By account04/B13, for every `delta>0` there are bounded finite-union unit sets `E_1,...,E_n` such that

`m:=int_(prod E_i) K(x) dx >= M_*-delta`.                         (2.2)

For coordinate `i`, define the actual fiber score against the other selected sets

`g_i(t)=int_(prod_{j!=i} E_j) K(t,x_{-i}) dx_{-i}`.               (2.3)

Because every other set has measure one,

`0<=g_i<=1`, and `m=int_{E_i} g_i`.                               (2.4)

### Theorem 2.1 — `QFORM-NEAR-BATHTUB-SWAP-STABILITY-v1`

For every coordinate `i`,

`sup_{|F|=1} int_F g_i - int_{E_i} g_i <= delta`.                 (2.5)

Consequently, whenever `A0 subset E_i`, `B0 subset E_i^c`, and
`|A0|=|B0|`,

`int_{B0} g_i - int_{A0} g_i <= delta`.                          (2.6)

Equivalently, for every `t in R` and `gamma>0`,

`min( |{x in E_i:g_i(x)<=t}|,
      |{x notin E_i:g_i(x)>=t+gamma}| ) <= delta/gamma`.          (2.7)

#### Proof

Replacing only `E_i` by any measurable unit set `F` produces another admissible product indicator law, so its slab mass is at most `M_*`. By (2.2),

`int_F g_i-m <= M_*-m <=delta`,

which proves (2.5). Taking `F=(E_i\A0) union B0` gives (2.6). If both sets in (2.7) had measure larger than `delta/gamma`, nonatomicity of Lebesgue measure would let us choose equal-measure subsets `A0,B0` with common measure `alpha>delta/gamma`; then (2.6) would give `alpha gamma<=delta`, a contradiction. QED.

This is the correct extremal statement available without an attained optimizer. It does **not** say `E_i` is an interval. It says only that a near-global product extremizer is, coordinate by coordinate, an approximate measure-one superlevel set of its own genuine slab fiber score.

## 3. Canonical cores that carry positive slab mass

The previous B13 run allowed an arbitrary coordinate core satisfying a slab-mass condition. There is in fact a canonical such core supplied directly by the fiber scores.

Let `I` be any nonempty finite coordinate bank, `k=|I|`. For the product witness above define

`K_i={t in E_i: g_i(t)>=m/(2k)}`, `i in I`,                       (3.1)

and

`C_I=cap_{i in I}{X_i in K_i}`.                                  (3.2)

### Theorem 3.1 — `QFORM-CANONICAL-FIBER-SCORE-CORE-v1`

The joint core carries at least half of the **actual slab mass**:

`P_E( X^TAX in J, C_I ) >= m/2`.                                 (3.3)

#### Proof

For each `i in I`, by Fubini and (3.1),

`P_E(X^TAX in J, X_i notin K_i)
 =int_{E_i\K_i}g_i(t)dt
 <=m/(2k)`,                                                       (3.4)

because `|E_i|=1`. A union bound over the `k` selected coordinates gives total lost slab mass at most `m/2`. QED.

Every `K_i` is bounded because it lies in the bounded finite-union witness `E_i`. Thus finite radii exist, but they are not assumed uniformly bounded. More importantly, a remote fragment irrelevant to the slab is automatically discarded by (3.1), while a remote fragment that survives (3.1) must have nonnegligible actual fiber score.

## 4. Spectral truncation on the canonical core

Now split selected original coordinates into disjoint banks `U` and `V`; write all remaining coordinates as `Z`. Every ambient quadratic form can be written

`Q=F(U,Z)+2U^T B V+V^T R V+c(Z)^T V`,                            (4.1)

for a physical cross matrix `B`, a real symmetric physical leaf block `R`, and arbitrary quadratic/affine terms absorbed into `F,c`.

Take the canonical joint core from Section 3 for `I=U union V`. Choose centers `u_0,v_0` and Euclidean core radii

`||U-u_0||_2<=R_U`, `||V-v_0||_2<=R_V`                           (4.2)

on this core.

For `tau>0`, let `P_tau` be the spectral projection of the **coefficient matrix** `R` onto eigenvalues with `|lambda|>=tau`; no random coordinates are rotated. Put

`d_tau=rank P_tau`,
`R_tau=P_tau R P_tau`,
`B_tau=B P_tau`,
`beta_tau=||B(I-P_tau)||_op`,
`Lambda_tau=|pdet R_tau|^(1/d_tau)` when `d_tau>0`.                (4.3)

Since `P_tau` commutes with `R`,

`||R-R_tau||_op <=tau`,                                         (4.4)

and `row(B_tau) subset range(R_tau)`.

Define a model polynomial `Q_tau` by replacing only the **centered** terms

`(V-v_0)^T R(V-v_0)+2(U-u_0)^TB(V-v_0)`

by the same expression with `R_tau,B_tau`, while retaining every affine and constant term generated by the original translations. Then `Q_tau` still has the form allowed by account01/B13, and on the canonical core

`|Q-Q_tau|
 <= tau R_V^2 +2 beta_tau R_U R_V
 =:Delta_tau`.                                                    (4.5)

The equality is not a perturbative deletion: (4.5) is used only as an event inclusion on a set already known to carry at least half of the actual slab mass.

### Theorem 4.1 — `QFORM-CANONICAL-CORE-SPECTRAL-RANGE-COMPILER-v1`

Assume `d_tau>=3` and

`max_j(P_tau)_{jj}<=1/2`.                                        (4.6)

Then

`boxed:
 rho_E:=m/|J|
 <=2 M_tau [1+2 Delta_tau/|J|],
 M_tau=[4d_tau/(d_tau-2)] Lambda_tau^(-1).
`                                                                    (4.7)

Equivalently,

`boxed:
 Delta_tau >=(|J|/2)
   (rho_E/(2M_tau)-1)_+.
`                                                                    (4.8)

Because `4d/(d-2)<=12` for every `d>=3`, if `Lambda_tau>=1`, then

`boxed:
 rho_E <=24 [1+2 Delta_tau/|J|].
`                                                                    (4.9)

In particular, a slab with `rho_E>48` forces

`Delta_tau>|J|/2`                                                  (4.10)

for every threshold satisfying `d_tau>=3`, (4.6), and `Lambda_tau>=1`.

#### Proof

By Theorem 3.1, at least `m/2` of the slab lies in the canonical core. On that core, (4.5) implies

`{Q in J} subset {Q_tau in J^{+Delta_tau}}`.

The range of `B_tau` lies in `range(R_tau)`, and (4.6) is exactly the account01/B13 leverage hypothesis. Therefore (1.1) gives a continuous density for the model with cap `M_tau`. Hence

`m/2 <= M_tau(|J|+2Delta_tau)`.

Divide by `|J|/2` to obtain (4.7); rearrange for (4.8). The bound `M_tau<=12` under `Lambda_tau>=1` gives (4.9), and (4.10) follows immediately. QED.

This is the first direct bridge in B13 from the previous “positive slab mass separation” obligation to the new exact range theorem: approximate global low rank is sufficient **at the slab scale** if its omitted curvature and cross-range leakage are small on the canonical high-fiber-score core.

## 5. The high-leverage complement is a weighted physical principal-minor star

The diffuse gate (4.6) has an exact algebraic alternative, and it can be strengthened from an orientation-only statement to one carrying the actual pseudodeterminant currency.

### Theorem 5.1 — `QFORM-WEIGHTED-SPECTRAL-VOLUME-STAR-v1`

Let `R_0` be any real symmetric rank-`d` matrix, `d>=1`, with range projection `P`. If `(P)_{jj}>1/2` for some original physical coordinate `j`, then

`boxed:
 sum_{I: |I|=d, j in I} |det R_0[I,I]|
 > (1/2)|pdet R_0|.
`                                                                    (5.1)

Moreover

`sum_{|I|=d}|det R_0[I,I]|=|pdet R_0|`.                           (5.2)

#### Proof

Write the spectral decomposition

`R_0=U Lambda U^T`,                                                (5.3)

where `U` is `m x d` with orthonormal columns and `Lambda` is invertible diagonal. For every `d`-set `I`,

`det R_0[I,I]=det(Lambda) det(U_I)^2`,                            (5.4)

so

`|det R_0[I,I]|=|pdet R_0| det(U_I)^2`.                           (5.5)

Cauchy--Binet gives

`sum_{|I|=d}det(U_I)^2=1`,                                        (5.6)

which proves (5.2). The exact coordinate-star Cauchy--Binet identity

`sum_{|I|=d,j in I}det(U_I)^2=P_{jj}`                             (5.7)

is the account01/B13 high-leverage identity; multiplying by `|pdet R_0|` gives (5.1). QED.

Applied to `R_tau`, failure of (4.6) therefore means that one **original coordinate** carries more than half of the complete absolute `d_tau`-principal-minor volume of the retained curvature. No tiny reciprocal minor is selected.

## 6. Combined range-or-star-or-residual trichotomy

For the near-global extremal product witness of Section 2 and every spectral threshold `tau` with `d_tau>=3`, exactly one of the following useful states is available:

1. **Diffuse range, paid unless the slab core sees a large residual.** If `max_j(P_tau)_{jj}<=1/2`, then (4.7)--(4.8) hold. In particular if `Lambda_tau>=1` and `rho_E>48`, the canonical half-slab core must satisfy
   `tau R_V^2+2 beta_tau R_U R_V>|J|/2`.

2. **High physical leverage.** If `max_j(P_tau)_{jj}>1/2`, Theorem 5.1 gives a single physical coordinate carrying more than half of the full retained principal-volume currency.

Thus a high-density slab can no longer hide merely behind the phrase “cutwise approximately low rank.” At every threshold with at least three retained directions it must exhibit one of three quantitative objects: weak retained geometric mean `Lambda_tau`, a physical principal-volume star, or slab-scale-large omitted curvature/cross-range leakage on a core selected by the actual slab fibers.

This trichotomy is compatible with the live correction forbidding global perturbative deletion of a max-norm-small tail: the tail is never discarded globally, and its cost is charged only where positive slab mass is actually present.

## 7. Designated partner applied to the actual inequality

The account04/B13 purification theorem is used twice, not merely cited.

First, it identifies `M_*` in (2.1) with the supremum over bounded finite-union unit-product indicators, so the near-extremal witness needed for Theorem 2.1 exists without any attained maximizer.

Second, given any arbitrary cap-one product law whose slab ratio is `rho`, the same finite-mixture approximation produces, for every `epsilon>0`, a bounded finite-union product indicator witness with slab ratio at least `rho-epsilon`. The canonical cores and spectral-range compiler can therefore be run on that physical product witness and `epsilon` sent to zero. No single interval, centered uniform law, bounded support diameter, or fixed fragment count is introduced.

## 8. What this does and does not solve

This run proves:

* `QFORM-NEAR-BATHTUB-SWAP-STABILITY-v1`;
* `QFORM-CANONICAL-FIBER-SCORE-CORE-v1`;
* `QFORM-CANONICAL-CORE-SPECTRAL-RANGE-COMPILER-v1`;
* `QFORM-WEIGHTED-SPECTRAL-VOLUME-STAR-v1`.

The full conjecture is still **OPEN**. The missing implication is now sharper:

`QFORM-RANGE-STAR-RESIDUAL-CLOSURE-v1`:

> Under the bare three-large-eigenvalue hypothesis, show that for a candidate slab ratio tending to infinity, the threshold trichotomy above cannot persist at every useful physical bank: either a retained curvature range has `Lambda_tau` bounded below and small canonical-core residual (paid by (4.7)), or the physical volume star activates an already-paid hub/grouped-bank theorem, or the slab-scale residual itself forces enough disjoint curvature/cross-bank volume to activate a paid D5/ridge mechanism.

The present result does **not** turn a cutwise singular-value estimate into an exact global range statement by deleting a residual. It instead supplies the rigorous probability interface needed to charge that residual on positive slab mass.

Continuity: account01/B13 proves continuity for the exact model `Q_tau` in the diffuse paid branch. The event-transfer argument here proves a slab inequality for the actual form under the displayed gate; it does **not** prove continuity of the actual law. Full continuity remains open separately.

## 9. Correction compliance

No step uses law-uniform pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea, a conditional projection density cap, projection-density-only control of an indefinite pushforward, a bounded support diameter, a fixed fragment count, interval extremality, or global deletion of a small residual. The only spectral rotation is of the deterministic coefficient matrix in Theorem 5.1 and in defining `P_tau`; random coordinates remain the original independent coordinates throughout.
