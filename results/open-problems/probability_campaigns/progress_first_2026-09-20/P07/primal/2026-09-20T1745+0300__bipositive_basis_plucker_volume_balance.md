Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — bi-positive complementary bases and an exact Plücker-volume balance reduction

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Captured pre-write master:** `192814caf3e189d2eff6c348e931380b5a3d0146`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1647+0300__complement_reduced_cost_leakage.md`.  
**Complementary checkpoint read:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1714+0300__physical_variance_imbalance_duality.md`. P07-B owns the Fourier-dual / exceptional-frequency interpolation route. This report stays on primal LP bases, complementary minors, volume sampling and selected-basis geometry.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` nonzero conjugate difference pairs are selected independently with probability `1/2`.  
**Endpoint:** `E theta(G_n)=(1+o(1)) sqrt(n)`.

A bounded current-source check on 20 September 2026 again found the primary paper stating that the exact asymptotics remain open and proving only square-root scale up to the `sqrt(log log n)` loss. No later source-matching sharp-constant proof was found in that bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric therefore remains

`alpha_LL = 1/2 -> 1/2`.

Nothing below is represented as an arbitrary-`n` proof of Conjecture 18.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Pair-cosine normalization and an arbitrary complementary basis

Let `p` be an odd prime, put

`M={1,...,m}`, `m=(p-1)/2`,

and let

`C_ab = cos(2 pi a b / p)`, `a,b in M`.

The inherited exact folded-Fourier identities are

`C 1 = -(1/2) 1`,

`C C^T = (p/4) I - (1/2) J`,

and hence

`C^{-1} = (4/p)(C-J)`.

Fix an edge-pair row set `D subset M`, let `A=M\D`, and write `d=|D|`, `k=|A|=m-d`.

Now take **any** `d`-subset `J subset M`, not necessarily the optimizer support, and put `K=M\J`. At prime order the inherited Chebotarev/folded-minor theorem makes all square blocks below invertible. Write

`B=C_{D,J}`, `E=C_{D,K}`, `F=C_{A,J}`, `G=C_{A,K}`.

Define the two inverse-one vectors and their Schur factors

`x=-B^{-1}1`,    `alpha=1+1^T x = 1-1^T B^{-1}1`,

`v=-G^{-1}1`,    `beta =1+1^T v = 1-1^T G^{-1}1`.

The previous report obtained the reduced-cost/complement identity only after inserting the actual optimal basis. The first theorem here shows that the complementary algebra is in fact exact for **every** basis.

---

# 2. New theorem: reciprocal Schur factors for every complementary pair of cosine minors

## Theorem P07-A.36 — `alpha beta = p`

For every prime-order partition above,

`boxed(alpha * beta = p)`.

### Proof

Jacobi's complementary-minor identity applied to the invertible full matrix `C` gives

`det((C^{-1})_{K,A}) = eps * det(B)/det(C)`,

where `eps` is the standard complementary-minor sign. Because

`(C^{-1})_{K,A}=(4/p)(G^T-J)`,

the matrix determinant lemma gives

`det(G^T-J)=det(G) (1-1^T G^{-T}1)=beta det(G)`.

Hence

`(4/p)^k beta det(G) = eps det(B)/det(C)`.        (2.1)

Interchanging the two complementary blocks gives

`(4/p)^d alpha det(B) = eps' det(G)/det(C)`.      (2.2)

The two Jacobi signs have product `+1`: their exponents add to twice the sum of all indices in `M`. Multiplying (2.1)-(2.2) and cancelling `det(B)det(G)` yields

`(4/p)^m alpha beta = 1/det(C)^2`.

From `C C^T=(p/4)I-(1/2)J`, the radial eigenvalue of `C C^T` is `1/4` and the other `m-1` eigenvalues are `p/4`. Therefore

`det(C)^2 = p^(m-1)/4^m`.

Substitution gives `alpha beta=p`. QED.

### Consequence

If `x>0`, then the basis `J` is a genuine primal feasible basis and its theta value is

`T_J = p/(1+1^T x)=p/alpha=beta`.                 (2.3)

So the complementary Schur factor is not merely related to the candidate objective: it **is exactly the candidate theta value**.

---

# 3. New theorem: generalized reduced costs and the bi-positive optimality criterion

Let `y=B^{-T}1` and define the nonbasic reduced-cost vector of the basis `J` by

`u = 1_K - E^T y`.

Exactly as in the optimal-basis calculation from the previous run, extend `y` by zero to the rows `A` and `u` by zero to the columns `J`. Then

`C y_tilde = 1-u_tilde`.

Applying `C^{-1}=(4/p)(C-J)` and restricting to rows `A` gives

`G u = (1^T u - p/2) 1_A`.

Since `v=-G^{-1}1`,

`u = (p/2-1^T u) v`.

Taking sums and using `1+1^T v=beta` yields the exact scalar.

## Theorem P07-A.37 — reduced costs of an arbitrary basis

For every complementary basis,

`boxed(u = (p/(2 beta)) v)`.                     (3.1)

If `x>0`, then `beta=T_J>0`, so standard LP optimality implies

`boxed(J is optimal for D  iff  v >= 0)`.         (3.2)

For the actual prime theta optimizer the inherited exact-support theorem gives strict positivity on both sides. Thus the unique optimal support `H` is equivalently the unique basis for which

`boxed(-C_{D,H}^{-1}1 >0  and  -C_{A,H^c}^{-1}1 >0)`.  (3.3)

I will call this the **bi-positive complementary-basis criterion**.

This is a more symmetric structural characterization than “find a positive primal basis and then compare objectives.” The primal feasibility and global LP optimality are two matching positivity tests on complementary cosine blocks.

---

# 4. Exact normalized determinant ratio

Put

`Q=(2/sqrt(p)) C`,

and for a basis `J` write

`Btilde=Q_{D,J}`, `Gtilde=Q_{A,K}`.

The magnitude of the full determinant is

`|det Q|=1/sqrt(p)`.

Equation (2.1), together with `beta>0` for a positive feasible basis, simplifies exactly to

`boxed(T_J/sqrt(p) = |det Btilde|/|det Gtilde|)`.  (4.1)

In particular, if `H` is the unique bi-positive optimal support and `K=H^c`, then

`boxed(theta(G_D)/sqrt(p)=|det Q_{D,H}|/|det Q_{A,K}|)`.  (4.2)

This is a hard-edge determinant formula for the **selected** complementary minors, not a worst-case singular-value estimate over all Fourier submatrices.

---

# 5. New exact projection-DPP normalization

The normalized row Gram is exceptionally simple:

`Q_D Q_D^T = I_d - (2/p) J_d`.

Therefore Cauchy-Binet gives

`S_D := sum_{|J|=d} det(Q_{D,J})^2
     = det(Q_D Q_D^T)
     = (p-2d)/p`.                               (5.1)

Similarly

`S_A := sum_{|K|=k} det(Q_{A,K})^2
     = (2d+1)/p`.                               (5.2)

Define the two fixed-size projection-volume laws

`w_D(J)=det(Q_{D,J})^2/S_D`,

`w_A(K)=det(Q_{A,K})^2/S_A`.

These are honest probability distributions on `d`- and `k`-subsets respectively.

For the actual bi-positive pair `(H,K)`, (4.2) becomes the exact selected-volume decomposition

`boxed(
 theta(G_D)/sqrt(p)
 = sqrt( ((p-2d)/(2d+1)) * (w_D(H)/w_A(K)) ).
)`                                                       (5.3)

This cleanly separates two effects:

1. the **degree imbalance** `(p-2d)/(2d+1)`, which is asymptotically 1 under the fair source; and
2. the **selected Plücker-volume imbalance** `w_D(H)/w_A(K)`, which carries the genuinely hard optimizer dependence.

---

# 6. New exact first and second moments over all complementary bases

The determinant relation is strong enough to compute the first two moments of the complementary Schur factor under volume sampling exactly.

Let `J` be distributed according to `w_A` through its complement `K=M\J`, and retain

`beta_J=1-1^T C_{A,K}^{-1}1`.

## Theorem P07-A.38 — exact volume moments

One has

`boxed(E_{w_A} beta_J = p/(2d+1))`,              (6.1)

`boxed(E_{w_A} beta_J^2 = p(p-2d)/(2d+1))`.      (6.2)

Dually, under `w_D`,

`boxed(E_{w_D} alpha_J = p/(p-2d))`,             (6.3)

`boxed(E_{w_D} alpha_J^2 = p(2d+1)/(p-2d))`.     (6.4)

### Proof of the `beta` identities

Let `eps_J` be the Laplace cofactor sign for splitting the rows into `D,A` and the columns into `J,K`. Tracking the Jacobi sign in (2.1) gives the signed identity

`eps_J det(Btilde) det(Gtilde)
 = sgn(det Q) * (beta_J/sqrt(p)) * det(Gtilde)^2`.   (6.5)

Sum over all `J`. The left side is the Laplace expansion of `det Q`, whose magnitude is `1/sqrt(p)`. Therefore

`sum_J beta_J det(Gtilde)^2 = 1`.                (6.6)

Divide by `S_A=(2d+1)/p` to get (6.1).

Squaring (4.1) in its unrestricted absolute form gives

`beta_J^2 det(Gtilde)^2 = p det(Btilde)^2`.

Sum over `J` and use `S_D=(p-2d)/p`; dividing again by `S_A` gives (6.2). The `alpha` identities follow by swapping complementary blocks. QED.

### Structural meaning in the source regime

When `d=(1+o(1))p/4`,

`E_{w_A} beta_J = 2+o(1)`,

while

`(E_{w_A} beta_J^2)^(1/2) = (1+o(1)) sqrt(p)`.

Thus the conjectural theta scale is the **RMS scale** of the all-basis Schur factor, whereas the ordinary volume-sampled mean stays order 1. The unconditioned volume law therefore has enormous signed cancellation/heavy spread. This proves a concrete obstruction to using the old volume-sampling moments without the bi-positivity selector: the selector is not a perturbative conditioning of a concentrated statistic.

---

# 7. New Plücker-overlap identity

The two normalized signed Plücker-amplitude vectors are

`psi_D(J)=det(Q_{D,J})/sqrt(S_D)`,

`phi_A(K)=det(Q_{A,K})/sqrt(S_A)`.

Their squared coordinates are the two volume laws. Laplace expansion of the full determinant gives the exact overlap

`boxed(
 | sum_{|J|=d} eps_J psi_D(J) phi_A(J^c) |
 = sqrt( p / ((p-2d)(2d+1)) ).
)`                                                       (7.1)

For a source-typical `d=p/4+O(sqrt(p))`, the right side is

`(2+o(1))/sqrt(p)`.                                     (7.2)

So the two complementary volume-amplitude vectors are almost orthogonal at precisely the inverse-square-root scale. This is the exterior-algebra version of the one exceptional radial principal angle between the two complementary cosine row spaces; all transverse row combinations are exactly orthogonal because the cross Gram is rank one.

There is also useful sign information in (6.5): the Laplace term indexed by `J` has the same orientation as the full determinant exactly when `beta_J>0`. Every positive primal basis has `alpha_J>1`, hence `beta_J=p/alpha_J>0`; in particular all primal-feasible basis terms lie on the same side of this signed Plücker decomposition. What is missing is a quantitative theorem controlling the one **bi-positive** term selected by LP optimality.

---

# 8. Source-random consequence: degree fluctuations are negligible; selected-volume imbalance is the prime bottleneck

Now let `D` come from the exact fair source model on prime order `p`, so

`d ~ Bin((p-1)/2,1/2)`.

Let `H=H(D)` be the unique bi-positive optimal basis, `K=H^c`, and define

`L_D = log(theta(G_D)/sqrt(p))`,

`Gamma_D = (1/2) log( w_D(H)/w_A(K) )`,

`R_D = (1/2) log( (p-2d)/(2d+1) )`.

Then (5.3) is exactly

`boxed(L_D = R_D + Gamma_D)`.                    (8.1)

Write `d=(p-1)/4 + Delta` and `a=(p+1)/2`. Then

`R_D = (1/2) log((a-2 Delta)/(a+2 Delta))
     = - artanh(2 Delta/a)`.

On `|2 Delta/a|<=1/2`, `|R_D|<=2|2 Delta/a|`; Hoeffding controls the complement exponentially. Since `E Delta^2=(p-1)/8`,

`boxed(E R_D^2 = O(1/p))`.                       (8.2)

Thus

`boxed(L_D-Gamma_D -> 0 in L^2)`.                (8.3)

Complementation sends `D` to `A`, `H` to `K`, and swaps the two selected volume weights, so

`Gamma_{D^c}=-Gamma_D`,

just as `L_{D^c}=-L_D`.

Finally, fair complement symmetry gives the exact expectation identity

`boxed(
 E theta(G_p)/sqrt(p)
 = E exp(L_D)
 = E cosh(L_D).
)`                                                       (8.4)

Therefore the prime sharp-constant problem is now localized to one precise primal quantity: the **selected complementary projection-DPP weight imbalance**. A sufficient route is to prove

`Gamma_D -> 0` in source probability together with enough exponential-tail control to make `cosh(Gamma_D)` uniformly integrable. The degree term is already negligible.

This is not yet the requested expectation theorem, but it removes the random edge-count fluctuation and all unselected determinant geometry from the leading constant.

---

# 9. What this changes, and what it does not

### Proved this run

- Reciprocal Schur factors `alpha beta=p` for every complementary prime cosine basis.
- General reduced-cost identity `u=(p/(2 beta))v` for every basis.
- A basis is globally optimal exactly when primal feasibility and complementary reduced-cost positivity hold; the actual optimizer is the unique **bi-positive** complementary basis.
- Exact candidate/optimizer determinant ratio `T_J/sqrt(p)=|det Btilde|/|det Gtilde|`.
- Exact projection-DPP normalizations `(p-2d)/p` and `(2d+1)/p`.
- Exact first and second volume moments of the Schur factors.
- Exact Plücker overlap of the complementary volume-amplitude vectors.
- Exact decomposition of `log(theta/sqrt(p))` into a negligible degree term plus the selected-volume imbalance.

### Not proved

- No arbitrary-`n` improvement of `O(sqrt(n log log n))` is claimed.
- No concentration theorem for the bi-positive selected Plücker weights is yet proved.
- The all-basis volume identities do **not** justify replacing the optimizer-selected basis by a typical volume-sampled basis; the exact moment calculation shows why that shortcut is unsafe.
- Prime-order structural statements do not by themselves settle composite odd `n` or the requested source expectation.

---

# 10. Next primal attack

The next target is no longer a generic Fourier RIP or an unconditioned determinant estimate. It is the following source-specific chamber statement.

> **Selected Plücker balance target.** For fair random prime-order `D`, let `(H,K)` be the unique complementary basis satisfying both inverse-one positivity systems. Prove
> 
> `log w_D(H)-log w_A(K)=o_P(1)`,
> 
> preferably with a source tail strong enough to control `E cosh(Gamma_D)`.

The first route will exploit that the two projection row spaces share all but one principal direction after taking orthogonal complements: their transverse parts are exactly orthogonal and only the radial two-plane remains. The bi-positivity inequalities should therefore be rewritten as a one-dimensional chamber condition inside the exterior-power/Plücker coordinates, rather than as a worst-case singular-value event. If this chamber condition forces the selected pair of squared Plücker coordinates to be asymptotically balanced, (8.1)-(8.4) would give the prime sharp constant. Expectation and general odd order would remain separate final steps.

This stays complementary to P07-B's physical-variance/exceptional-frequency route and does not take over its source claim.
