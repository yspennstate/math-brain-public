Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — orthogonal-core mass scalarization and a source-exact variance bridge

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Captured pre-write master:** `c0f4845da24011daa587e8108b600a328d8ba169`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1745+0300__bipositive_basis_plucker_volume_balance.md`.  
**Latest complementary checkpoint read:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1830+0300__adaptive_quadratic_tilt_mean_QBI.md`. P07-B owns the Fourier-dual / exceptional-frequency / quadratic-interpolation route. This report stays on the primal LP and its exact orthogonal geometry.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; each of the `m=(n-1)/2` nonzero conjugate difference pairs is selected independently with probability `1/2`.  
**Endpoint:**

`E theta(G_n) = (1+o(1)) sqrt(n)`.

A bounded current-source check on 20 September 2026 found the primary paper still describing the exact asymptotics as open and retaining the `O(sqrt(n log log n))` upper scale; the Randomstrasse collection still records the sharp-constant target. I also checked the standard random-DFT-submatrix comparison represented by Farrell, arXiv:1003.1021: its limiting empirical singular-value law does not by itself control the adaptive positive basis below. No later source-matching sharp-constant proof was found in this bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric remains

`alpha_LL = 1/2 -> 1/2`.

Nothing below is represented as a proof of the full conjecture.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Inherited folded cosine LP

Let

`M={1,...,m}`, `m=(n-1)/2`,

and let

`C_ab = cos(2 pi a b/n)`, `a,b in M`.

For `D subset M`, the inherited exact circulant theta reduction is

`theta_D := theta(G_D) = n/(1+s_D)`,

where

`boxed( s_D = min { 1^T x : C_D x = -1_D, x >= 0 }. )`          (1.1)

Here `C_D` denotes the rows indexed by `D`. This normalization has the correct extremes: `D=emptyset` gives `theta=n`, while `D=M` has the feasible point `x=2*1` and gives `theta=1`.

The folded cosine identities, valid for every odd `n`, are

`C 1 = -(1/2) 1`,

`C C^T = (n/4) I - (1/2) J`.                         (1.2)

The preceding prime-order work exploited square minors of `C`. The first new point here is that the **whole folded matrix is only a rank-one radial perturbation of an exact orthogonal involution**, and this works for every odd `n`, not merely primes.

---

# 2. New exact orthogonal core

Put

`Q = (2/sqrt(n)) C`,

`P = J/m`,

`rho = 1 - 1/sqrt(n)`,

and define

`boxed( O = Q - rho P. )`                              (2.1)

Because `Q 1 = -n^(-1/2) 1`, while (1.2) gives

`Q^2 = I - (2/n) J`,

`Q` acts isometrically on `1^perp` and by the scalar `-1/sqrt(n)` on the radial line. Therefore `O` has eigenvalue `-1` on the radial line and agrees with `Q` on `1^perp`.

## Theorem P07-A.39 — exact symmetric orthogonal core

For every odd `n`,

`boxed( O^T=O,   O^2=I,   O 1=-1. )`                  (2.2)

Moreover

`Q = O + lambda J`,

where the rank-one coefficient simplifies exactly to

`boxed( lambda = rho/m = 2/(sqrt(n)(sqrt(n)+1)). )`     (2.3)

Thus the entries obey

`O_ab = (2/sqrt(n)) cos(2 pi ab/n) - lambda`,           (2.4)

so the core is also near-flat entrywise:

`max_ab |O_ab| <= 2/sqrt(n) + 2/n`.                    (2.5)

### Proof

Symmetry is immediate. On `1^perp`, `P=0` and (1.2) gives `Q^2=I`. On `span{1}`, `Q=-n^(-1/2)I` and `rho P=rho I`, so `O=-I`. Hence `O^2=I` on both invariant subspaces. The formula for `lambda` follows from

`rho/m = ((sqrt(n)-1)/sqrt(n)) / ((n-1)/2)
       = 2/(sqrt(n)(sqrt(n)+1))`.

QED.

This is the folded-pair analogue of the earlier critical Householder normal form, but now it is inserted directly into the exact pair-cosine LP and therefore interacts cleanly with the bi-positive basis and complementary-minor work from the last two runs.

---

# 3. New theorem: theta is a monotone Möbius transform of an orthogonal-core LP mass

Define the **core mass**

`boxed(
 S_D = min { 1^T u : O_D u = -1_D, u >= 0 }.
)`                                                        (3.1)

The all-ones vector is always feasible because `O 1=-1`, so

`0 <= S_D <= m`.                                         (3.2)

## Theorem P07-A.40 — exact feasible-set bijection

The original cosine LP (1.1) and the orthogonal-core LP (3.1) have the same optimal supports. More precisely, if `u>=0` is core-feasible with `S=1^T u`, then

`boxed(
 x = (2/sqrt(n)) * u/(1-lambda S)
)`                                                        (3.3)

is feasible for (1.1). Conversely, if `x>=0` is feasible for (1.1), with `s=1^T x`, then

`boxed(
 u = x/(2/sqrt(n)+lambda s)
)`                                                        (3.4)

is core-feasible.

The objective values satisfy

`boxed(
 s = 2 S / ( sqrt(n) (1-lambda S) ).
)`                                                        (3.5)

Since `lambda m = rho < 1`, the right side is strictly increasing for `0<=S<=m`. Hence minimizing the original theta LP is **exactly equivalent** to minimizing core mass.

### Proof

If `O_Du=-1`, then using `Q=O+lambda J`,

`Q_Du = -(1-lambda S) 1_D`.

Multiplying by `(2/sqrt(n))/(1-lambda S)` gives

`Q_Dx = -(2/sqrt(n))1_D`,

which is equivalent to `C_Dx=-1_D`. This proves (3.3). Conversely, `C_Dx=-1_D` means

`Q_Dx = -(2/sqrt(n))1_D`.

Therefore

`O_Dx = -(2/sqrt(n)+lambda s)1_D`,

and (3.4) follows. Summing (3.3) gives (3.5). QED.

## Corollary P07-A.41 — exact scalar theta formula

Writing `S=S_D`, one has

`boxed(
 theta_D/sqrt(n)
 = (1-lambda S)/(1-lambda(m-S)).
)`                                                        (3.6)

This is already a substantial simplification: the complete theta optimum is encoded by one scalar mass of a positive LP over a **symmetric orthogonal near-flat matrix**.

---

# 4. New theorem: exact complement mass conservation

The scalarization becomes useful because the core LP has an exact primal-dual complementarity not visible in the original cosine coordinates.

The dual of (3.1) is

`S_D = max { -1_D^T y : O_D^T y <= 1 }`.                (4.1)

Now write `u=1-h`. Since `O_D1=-1_D`, the primal constraints become

`O_D h = 0`, `h <= 1`,

and therefore

`m-S_D = max { 1^T h : O_D h=0, h<=1 }`.               (4.2)

Let `A=M\D`. Because the rows of `O` are an orthonormal basis, every vector in `ker O_D` has a unique representation

`h=O_A^T y`.

Also `O_A1=-1_A`, so

`1^T h = -1_A^T y`.

Thus (4.2) is exactly the dual program (4.1) for `A`.

## Theorem P07-A.42 — orthogonal-core complement conservation

For **every odd `n` and every mask `D`**,

`boxed( S_D + S_{D^c} = m. )`                           (4.3)

This is an LP-duality proof of the same reciprocal symmetry that vertex transitivity gives at the theta level, but in core coordinates it is additive rather than multiplicative.

Under the exact fair source model, `D` and `D^c` have the same law. Hence

`boxed( E S_D = m/2 )`                                  (4.4)

**exactly**, for every odd `n`.

This mean identity is not asymptotic and uses no probability estimate.

---

# 5. Main new reduction: Conjecture 18 is an exact centered-mass concentration problem

Let

`sqrt_n = sqrt(n)`,

`kappa_n = (sqrt_n-1)/(sqrt_n+1)`,

and define the centered normalized core mass

`Y_D = (2 S_D - m)/m in [-1,1]`.                        (5.1)

Substituting `S_D=m(1+Y_D)/2` into (3.6) gives the exact Möbius form

`boxed(
 X_D := theta_D/sqrt(n)
 = (1-kappa_n Y_D)/(1+kappa_n Y_D).
)`                                                        (5.2)

Equivalently, if

`boxed(
 Z_D = 4 (S_D-m/2)/(sqrt(n)+1)^2,
)`                                                        (5.3)

then `Z_D=kappa_n Y_D` and

`boxed( X_D=(1-Z_D)/(1+Z_D). )`                         (5.4)

Complementation sends

`S_D-m/2 -> -(S_D-m/2)`,

hence

`Y_D -> -Y_D`, `Z_D -> -Z_D`, `X_D -> X_D^{-1}`.        (5.5)

In particular

`log X_D = -2 artanh(Z_D)`.                              (5.6)

This collapses the previous selected-Plücker imbalance to one bounded scalar.

## Theorem P07-A.43 — exact expectation-gap identity

Under the exact fair source model,

`boxed(
 E theta(G_n)/sqrt(n) - 1
 = 2 E [ kappa_n^2 Y_D^2 / (1-kappa_n^2 Y_D^2) ]
 = 2 E [ Z_D^2/(1-Z_D^2) ].
)`                                                        (5.7)

### Proof

By complement invariance, `X_D` and `X_D^{-1}` have the same distribution. Therefore

`E X_D -1
 = (1/2) E [X_D + X_D^{-1} -2]`.

With `X=(1-Z)/(1+Z)`, direct algebra gives

`(1/2)(X+X^{-1}-2)=2 Z^2/(1-Z^2)`.

QED.

This is an exact all-odd-`n` reformulation of the requested **expectation** endpoint, not merely a high-probability proxy.

---

# 6. New concentration bridge: a much weaker variance target suffices

Since `E S_D=m/2`,

`E Y_D^2 = 4 Var(S_D)/m^2`.                              (6.1)

Also

`1-kappa_n^2 Y_D^2 >= 1-kappa_n^2`

and

`1-kappa_n^2 = 4 sqrt(n)/(sqrt(n)+1)^2`.                 (6.2)

Applying these to (5.7) yields an exact clean coefficient.

## Theorem P07-A.44 — core-mass variance criterion

For every odd `n` in the fair source model,

`boxed(
0 <= E theta(G_n)/sqrt(n)-1
   <= [8/(sqrt(n)(sqrt(n)+1)^2)] Var(S_D).
)`                                                        (6.3)

Consequently,

`boxed(
 Var(S_D)=o(n^(3/2))
 => E theta(G_n)=(1+o(1))sqrt(n).
)`                                                        (6.4)

The earlier direct reciprocal-variance bridge required `Var(theta)=o(n)`. The new variable `S_D` is bounded between `0` and `m~n/2`, is exactly centered by complementation, and only needs variance `o(n^(3/2))`. This is a materially weaker concentration obligation.

There is also the lower comparison

`E theta/sqrt(n)-1 >= (8 kappa_n^2/m^2) Var(S_D)`,       (6.5)

obtained by discarding the denominator in (5.7). Thus the core variance is not an arbitrary auxiliary statistic: it directly measures the sharp-constant gap on its natural scale.

---

# 7. New source-valid influence criterion

The core mass is monotone:

`D subset D' => S_D <= S_D'`,                            (7.1)

because adding rows only adds equality constraints to (3.1).

Define its one-sided deletion energy

`boxed(
 J_S(D) = sum_{a in D} (S_D-S_{D\{a}})^2.
)`                                                        (7.2)

For a fair product measure, the Poincaré/Efron-Stein inequality on the Boolean cube gives

`Var(S_D) <= (1/2) E J_S(D)`.                            (7.3)

Indeed the usual flip-energy form is `(1/4) E sum_a (S_D-S_{D triangle {a}})^2`; every undirected cube edge is counted at both endpoints there and only at its upper endpoint in `J_S`.

Combining (6.3) and (7.3) gives the source-exact primal criterion

`boxed(
0 <= E theta(G_n)/sqrt(n)-1
   <= [4/(sqrt(n)(sqrt(n)+1)^2)] E J_S(D).
)`                                                        (7.4)

Therefore it is enough to prove

`boxed( E J_S(D) = o(n^(3/2)). )`                       (7.5)

In particular, the very natural target

`E J_S(D)=O(n)`                                          (7.6)

would give the quantitative rate

`E theta(G_n)/sqrt(n)-1 = O(n^(-1/2)).`                 (7.7)

This is a new, sharply localized primal bottleneck: control the **mean square change of the minimum positive mass of a near-flat orthogonal LP when one random row constraint is deleted**.

It is substantially weaker than proving a uniform RIP statement for all sparse Fourier vectors.

### Central-band reduction

The fair mask has

`|D| = m/2 + O_P(sqrt(n))`.

Choose, for example,

`B_n={ ||D|-m/2| <= n^(2/3) }`.

Hoeffding gives `P(B_n^c)<=exp(-c n^(1/3))`. Since always `0<=S_D<=m`, a crude deterministic bound gives `J_S(D)<=m^3`, so the contribution of `B_n^c` to `E J_S` is negligible.

Thus (7.5) reduces further to a central-density statement. Because there are `Theta(n)` active coordinates there, it is enough that a uniformly chosen active-row deletion have

`boxed(
 E[ (S_D-S_{D\{a}})^2 | B_n, a in D ] = o(sqrt(n)).
)`                                                        (7.8)

An `O((log n)^C)` mean-square deletion estimate would be far more than enough.

This gives a concrete next target that respects the exact source parity and expectation endpoint.

---

# 8. Prime-order basis form: reduced costs become the complementary core primal with no scale factor

The all-odd-`n` scalarization above does not require prime order. On primes, the inherited full-spark/unique-basis results make it even more explicit.

Let `p` be prime, let `H` be the unique optimal column basis for row mask `D`, put `A=D^c`, `K=H^c`, and block the orthogonal core as

`O = [[B,E],[F,G]]`

with `B=O_{D,H}` and `G=O_{A,K}`.

Define

`u=-B^{-1}1 >0`,

`w=-G^{-1}1 >0`.                                        (8.1)

Then

`S_D=1^T u`, `S_A=1^T w`,                               (8.2)

and Theorem P07-A.42 gives `1^Tu+1^Tw=m`.

Let `y=B^{-T}1` be the basic dual vector for the core LP and let the nonbasic reduced costs be

`r_K=1-E^T y`.

Orthogonality gives the cross-block identity

`G E^T = -F B^T`.

Hence

`G r_K = G1-GE^Ty
       = G1+F B^Ty
       = G1+F1
       = -1`,

so, exactly,

`boxed( r_K = -G^{-1}1 = w. )`                         (8.3)

Thus in orthogonal-core coordinates the complementary optimizer is literally the reduced-cost vector **with scalar factor one**. The scale `p/(2 theta)` found in the original cosine coordinates was entirely produced by the radial rank-one perturbation.

This is the cleanest primal/complementary-basis statement obtained so far.

---

# 9. New collapse of the previous Plücker-volume bottleneck

The previous report reduced prime-order theta to a ratio of selected complementary cosine minors. The orthogonal core shows that the two high-dimensional volume terms cancel before any probability is used.

Write

`Q=(2/sqrt(p))C = O + lambda J`,

with `lambda=2/(sqrt(p)(sqrt(p)+1))`.

For the selected blocks,

`Q_{D,H}=B+lambda J`,

`Q_{A,K}=G+lambda J`.

By the matrix determinant lemma and (8.1),

`det Q_{D,H} = det B * (1-lambda S_D)`,                 (9.1)

`det Q_{A,K} = det G * (1-lambda S_A)`.                 (9.2)

Because `O` is orthogonal, Jacobi's complementary-minor identity gives

`|det B|=|det G|`.                                      (9.3)

Therefore the previous exact determinant formula becomes

`boxed(
 theta(G_D)/sqrt(p)
 = (1-lambda S_D)/(1-lambda S_A),
)`                                                        (9.4)

which is exactly (3.6).

So the **selected Plücker-volume imbalance is not an independent high-dimensional fluctuation**. After removing the deterministic radial rank-one defect of the folded cosine matrix, the complementary selected volumes agree exactly. The whole theta deviation is a one-dimensional imbalance in the two positive core masses.

This materially changes the next attack: it is unnecessary to prove concentration of two adaptive determinant ensembles. One should instead control the deletion quadratic variation of the scalar core LP value.

---

# 10. A useful obstruction: uniform worst-case Lipschitz control cannot prove the result

The new influence route should not be attacked by seeking an `O(1)` deterministic one-row Lipschitz bound. Such a bound is false even in the most symmetric prime examples.

Take prime `p` and the full mask `D=M`, for which `S_D=m` and `theta=1`. Delete one generator pair `a`. The complement of the resulting graph is the cycle `C_p` (because `a` generates `Z_p`). The classical odd-cycle formula gives

`theta(C_p)=p cos(pi/p)/(1+cos(pi/p))`,

so by vertex-transitive complementarity

`theta(G_{M\{a}})=1+sec(pi/p)=2+O(p^(-2))`.

Substituting this into the exact mass map (3.6) gives

`boxed(
 S_M-S_{M\{a}} = (1/2+o(1)) sqrt(p).
)`                                                       (10.1)

Thus the worst-case one-row core-mass increment is at least order `sqrt(n)`. The required estimate (7.5) must exploit that the fair source lives exponentially far from these extreme-density masks; a global bounded-difference argument loses the needed factor.

This is a genuine obstruction to the naive concentration proof and explains why the central-band reduction (7.8) is the right next level.

---

# 11. Remaining gap and next primal attack

### What is now proved

1. For every odd `n`, the exact folded cosine matrix is a radial rank-one perturbation of a symmetric orthogonal near-flat core `O`.
2. The theta LP is exactly equivalent to the positive core LP `S_D=min{1^Tu:O_Du=-1,u>=0}`.
3. Complementation is additive in core mass: `S_D+S_{D^c}=m` exactly.
4. The full expectation gap is exactly

   `E theta/sqrt(n)-1 = 2 E[Z_D^2/(1-Z_D^2)]`.

5. `Var(S_D)=o(n^(3/2))` is sufficient for Conjecture 18.
6. More concretely, `E J_S(D)=o(n^(3/2))` is sufficient, and an `O(n)` deletion-energy estimate would give an `O(n^(-1/2))` relative gap.
7. On prime orders, the orthogonal-core complementary primal is exactly the reduced-cost vector, and the previous selected Plücker-volume ratio collapses to the one-dimensional core-mass imbalance.
8. A uniform `O(1)` row-Lipschitz bound is impossible: extreme masks have `Theta(sqrt(n))` increments.

### Remaining full-source gap

No bound of the required strength for `E J_S(D)` has yet been proved. The headline iterated-log exponent therefore remains unchanged. In particular, (7.5) is a **new reduction**, not a hidden solution.

### Next attack

Work entirely inside the central source band. For `a in D`, compare the optimal core primal before and after deleting row `a`. Since the rows of `O` are exactly orthonormal, the deleted row itself is an explicit unit vector in the new nullspace. The aim is to derive a source-average pivot inequality of the form

`E[(S_D-S_{D\{a}})^2 | a in D, B_n] <= polylog(n)`       (11.1)

or, more weakly, `o(sqrt(n))`.

A promising route is to express the deletion step through the prime basic block `B=O_{D,H}` and complementary reduced cost `w=-G^{-1}1`, use the exact identity `r_K=w`, and control only the **radial pivot leverage** rather than the least singular value of the whole adaptive Fourier block. This is a one-vector quantity and should be compared with source-average leverage, not worst-case RIP.

The complementary P07-B Fourier-dual/QBI route remains distinct and should not be duplicated.

---

# 12. Obligation ledger

- Full-source metric: `alpha_LL = 1/2 -> 1/2` — unchanged.
- New all-odd-`n` theorem: exact orthogonal core `O` and core LP scalarization — **PROVED PARTIAL**.
- New all-odd-`n` theorem: `S_D+S_{D^c}=m` — **PROVED PARTIAL**.
- New source-exact theorem: expectation gap identity (5.7) — **PROVED PARTIAL**.
- New sufficient condition: `Var(S)=o(n^(3/2))` or `E J_S=o(n^(3/2))` — **PROVED PARTIAL reduction**.
- New prime theorem: core reduced costs equal the complementary primal exactly — **PROVED PARTIAL**.
- New interpretation: previous adaptive Plücker ratio is only the radial rank-one defect after orthogonalization — **PROVED PARTIAL**.
- Worst-case row-increment obstruction `Theta(sqrt(p))` at the complete-mask endpoint — **PROVED PARTIAL**.
- Missing lemma: central-band mean-square deletion influence `o(sqrt(n))` per active row — **OPEN**.
- Conjecture 18 — **OPEN**.
