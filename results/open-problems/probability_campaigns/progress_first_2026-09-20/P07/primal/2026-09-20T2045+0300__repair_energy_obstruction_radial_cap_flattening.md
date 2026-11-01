Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — the Euclidean repair route is impossible, and an exact radial-cap flattening criterion

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Captured pre-write master:** `f47929e435aa5f84820ead0cd37ca477bc07e505`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1945+0300__random_reflection_positive_repair_energy.md`.  
**Complementary checkpoint consulted:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T2014+0300__cubic_preconditioning_matched_decoupling.md`. P07-B owns Fourier-dual / exceptional-frequency / bounded-interpolation work. The present report stays on the primal orthogonal-core LP and a one-sided cap-flattening construction.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; with `m=(n-1)/2`, each nonzero conjugate difference pair is selected independently with probability `1/2`.  
**Endpoint:** `E theta(G_n)=(1+o(1)) sqrt(n)`.

A bounded primary-source check on 20 September 2026 again found arXiv:2502.16227 stating that the exact asymptotics remain open and retaining the upper scale `O(sqrt(n log log n))`; Randomstrasse101 still records the sharp-constant problem. No later source-matching proof was found in this bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric remains

`alpha_LL = 1/2 -> 1/2`.

Nothing below is represented as a proof of the full conjecture.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Inherited orthogonal-core normal form

Let `M={1,...,m}`, `m=(n-1)/2`, and let

`O^T=O`, `O^2=I`, `O 1=-1`

be the exact near-flat folded-cosine core from the preceding runs. Its entries satisfy

`max_{a,b}|O_ab| <= 2/sqrt(n)+2/n`.                         (1.1)

For a source mask `D subset M`, let `d=|D|`, `A=D^c`,

`Pi_D = O_D^T O_D`, `Pi_A=I-Pi_D`,

and

`p_D=Pi_D 1=(1-O epsilon)/2`,

where `epsilon_a=+1` on `D` and `-1` on `A`. The exact core mass is

`S_D = min { 1^T u : O_D u=-1_D, u>=0 }`.                 (1.2)

The inherited identities are

`S_D+S_A=m`,                                               (1.3)

and

`theta_D/sqrt(n)
 = (1-lambda S_D)/(1-lambda(m-S_D))`,                     (1.4)

where

`lambda=2/(sqrt(n)(sqrt(n)+1))`.                          (1.5)

Equivalently, with

`rho=lambda m=1-1/sqrt(n)`, `s_D=S_D/m`,

`X_D:=theta_D/sqrt(n)
 = (1-rho s_D)/(1-rho+rho s_D)`.                          (1.6)

The previous run introduced the least-Euclidean-energy positive repair

`E_D = min { ||h||_2^2 : h in range(Pi_A), p_D+h>=0 }`    (1.7)

and observed that the sufficient condition `E E_D=o(sqrt(n))` would imply the conjecture. The first result below shows that this sufficient condition is in fact impossible in the exact source model. This closes that route rather than allowing it to generate repeated no-progress runs.

---

# 2. New obstruction: the Euclidean repair energy is necessarily linear in n

Put

`g_D:=O epsilon`, so `p_D=(1-g_D)/2`.                     (2.1)

For every feasible repair `h` in (1.7), whenever `g_D(j)>1` one has `p_D(j)<0`, hence

`h_j >= -p_D(j) = (g_D(j)-1)/2`.

Therefore, deterministically,

`boxed(
 E_D >= (1/4) sum_{j in M} (g_D(j)-1)_+^2.
)`                                                        (2.2)

This lower bound already has linear expectation.

## Theorem P07-A.51 — source-exact linear repair-energy barrier

Under the exact fair source model,

`boxed(
 E E_D >= [gamma_1/8 + o(1)] n,
)`                                                        (2.3)

where, for `Z~N(0,1)`,

`gamma_1 := E (Z-1)_+^2
          = 2 Phi(-1)-phi(1)
          = 0.07533978334377078...`.                     (2.4)

Thus

`boxed(
 E E_D >= (0.00941747291797135...+o(1)) n.
)`                                                        (2.5)

In particular, the previous sufficient target

`E E_D=o(sqrt(n))`                                       (2.6)

cannot hold. The Euclidean-repair route is therefore discarded.

### Proof

Fix a coordinate `j`. Because `O` is orthogonal,

`g_D(j)=sum_a O_{ja} epsilon_a`,

with

`sum_a O_{ja}^2=1`.                                      (2.7)

By (1.1),

`max_a |O_{ja}| -> 0`

uniformly in `j`. Moreover

`sum_a |O_{ja}|^3
 <= (max_a|O_{ja}|) sum_a O_{ja}^2
 = o(1)`                                                 (2.8)

uniformly. Berry--Esseen therefore gives a uniform central-limit approximation

`g_D(j) => N(0,1)`.                                      (2.9)

The fourth moments are uniformly bounded; in fact for a variance-one Rademacher sum,

`E g_D(j)^4
 = 3 - 2 sum_a O_{ja}^4
 <= 3`.                                                   (2.10)

Hence `(g_D(j)-1)_+^2` is uniformly integrable. Combining (2.9)--(2.10), uniformly in `j`,

`E (g_D(j)-1)_+^2 = gamma_1+o(1)`.                       (2.11)

Average (2.2) over the source mask and sum over `m=(n-1)/2` coordinates:

`E E_D
 >= (m/4)(gamma_1+o(1))
 = (gamma_1/8+o(1))n`.                                  (2.12)

Finally,

`E(Z-1)_+^2
 = int_1^infty (z-1)^2 phi(z) dz
 = 2 Phi(-1)-phi(1)`.                                   (2.13)

QED.

### Interpretation

The failure is structural, not a missing concentration estimate. About `Phi(-1)=0.158655...` of the coordinates of the signed least-norm point lie below zero in the Gaussian source limit, with constant mean squared deficit. Any coordinatewise-positive repair must therefore spend `Theta(n)` Euclidean energy. A sharp theta certificate may still exist because the theta objective sees **radial mass**, not Euclidean repair energy. The next sections replace the dead norm target by exactly that one-sided radial geometry.

---

# 3. New exact dual form: core mass is a capped radial vector in the selected subspace

Let

`V_D:=range(Pi_D)=span{ rows of O indexed by D }`.         (3.1)

Applying the inherited complement-duality identity to `A=D^c` gives

`boxed(
 S_D = max { 1^T v : v in V_D, v <= 1 coordinatewise }.
)`                                                        (3.2)

This is an exact all-odd-`n` dual of the positive core LP.

### Proof

The inherited identity for any mask `B` is

`m-S_B = max {1^T h : O_B h=0, h<=1}`.                  (3.3)

Take `B=A`. Then `m-S_A=S_D` by (1.3), while orthogonality of the rows of `O` gives

`ker O_A = V_D`.                                         (3.4)

Substitute (3.4) into (3.3). QED.

The important change of viewpoint is that positivity of the primal certificate is equivalent to finding, inside the **selected row span**, a vector with large radial sum but with only a one-sided coordinate cap. Large negative coordinates are completely free.

---

# 4. New exact scalarization by a one-sided flattening constant

For `d>0`, define

`boxed(
 tau_D := min { max_j v_j : v in V_D, 1^T v=d }.
)`                                                        (4.1)

For `d=0`, set `tau_D=1` by convention. Since every vector in (4.1) has positive average, `tau_D>0` when `d>0`.

Because `p_D=Pi_D1` has

`1^T p_D=||p_D||_2^2=d`,                                 (4.2)

every vector in (4.1) has the unique decomposition

`v=p_D+z`,

`z in V_D cap p_D^perp`.                                 (4.3)

Thus `tau_D` is exactly the smallest possible upper coordinate peak after **transverse flattening of the radial projection**.

## Theorem P07-A.52 — exact cap/core identity

For every odd `n` and every nonempty mask `D`,

`boxed(
 S_D = d/tau_D.
)`                                                        (4.4)

Consequently the complement conservation becomes

`boxed(
 d/tau_D + (m-d)/tau_A = m.
)`                                                        (4.5)

### Proof

By (3.2), for every `v in V_D` with `v<=1` and `1^Tv=t>0`, the rescaled vector

`w=(d/t)v`

lies in `V_D`, has sum `d`, and satisfies

`max_j w_j <= d/t`.

Hence `tau_D<=d/t`, or `t<=d/tau_D`. Taking the supremum over capped feasible `v` gives

`S_D<=d/tau_D`.                                          (4.6)

Conversely, for every `eta>0` choose `w in V_D`, `1^Tw=d`, with

`max_j w_j <= tau_D+eta`.

Then

`v=w/(tau_D+eta)`

satisfies `v<=1`, so (3.2) gives

`S_D>=d/(tau_D+eta)`.

Let `eta downarrow 0`. This proves (4.4); (4.5) follows from (1.3). QED.

This replaces the impossible small-Euclidean-repair condition by a scale-free one-sided flattening quantity. At source-typical `d/m -> 1/2`, the conjectured sharp core mass `S_D/m -> 1/2` corresponds precisely to

`tau_D -> 1`.                                            (4.7)

---

# 5. Exact minimax cosine-polynomial form

Every `v in V_D` has a unique coefficient vector on the selected orthonormal rows. Write

`v=-O_D^T y`.

Since `O_D 1=-1_D`,

`1^T v=1_D^T y`.                                         (5.1)

Therefore (4.1) is exactly

`boxed(
 tau_D
 = min_{y in R^D, 1^T y=d}
   max_{j in M} [-(O_D^T y)_j].
)`                                                        (5.2)

Using

`O = (2/sqrt(n)) C - rho J/m`,

`rho=1-1/sqrt(n)`,                                       (5.3)

this becomes

`boxed(
 tau_D
 = rho d/m
 + min_{1^T y=d}
   max_{j in M}
   [ -(2/sqrt(n)) sum_{a in D} y_a cos(2 pi a j/n) ].
)`                                                        (5.4)

This is a concrete feasible-certificate construction problem:

- frequencies are restricted to the random selected set `D`;
- the coefficient sum is fixed exactly at `d`;
- coefficients `y_a` may have either sign;
- only the **upper** physical excursion is penalized;
- no lower bound and no all-directions Fourier RIP estimate is required.

For a source-typical balanced mask `d/m=1/2+o(1)`, proving `tau_D<=1+o_{L1}(1)` is equivalent to constructing selected-frequency weights of total mass `d` whose nonzero cosine polynomial has upper peak at most

`1-rho d/m+o_{L1}(1) = 1/2+o_{L1}(1)`.                 (5.5)

This is the new primal bottleneck. It is deliberately one-sided and therefore does not duplicate P07-B's Fourier-dual exceptional-frequency interpolation problem.

---

# 6. Exact positive-measure dual of the cap functional

Let

`W_D:=V_D cap p_D^perp`.                                 (6.1)

The form (4.3) gives

`tau_D=min_{z in W_D} max_j (p_D(j)+z_j)`.               (6.2)

Dualizing this finite-dimensional minimax problem yields:

## Theorem P07-A.53 — radial probability-multiplier dual

For every nonempty `D`,

`boxed(
 tau_D
 = max {
     p_D^T q :
     q>=0,
     1^T q=1,
     Pi_D q in span{p_D}
   }.
)`                                                        (6.3)

### Proof

Introduce an epigraph variable `t` and minimize `t` subject to

`p_D+z <= t 1`, `z in W_D`.                              (6.4)

With multiplier `q>=0`, the Lagrangian is

`t(1-1^Tq)+q^Tp_D+q^Tz`.                                (6.5)

The infimum over `t` is finite exactly when `1^Tq=1`; the infimum over `z in W_D` is finite exactly when `q perp W_D`. Since `W_D` is the codimension-one subspace of `V_D` perpendicular to `p_D`,

`q perp W_D`

is equivalent to

`Pi_Dq in span{p_D}`.                                   (6.6)

Strict epigraph feasibility holds for sufficiently large `t`, so strong LP duality gives (6.3). QED.

Thus a failure of sharp flattening requires a positive probability vector whose projection onto the random selected row span is **exactly radial** and whose radial pairing with `p_D` exceeds one. This is a much narrower obstruction than the positive-cone Euclidean quotient from the previous run.

---

# 7. New expectation-level criterion: only mean positive cap excess must vanish

Define

`eta_D := (tau_D-1)_+`,                                  (7.1)

with the convention `eta_D=0` when `d=0`.

Since `tau_D<=1+eta_D`, Theorem P07-A.52 gives

`S_D/m = (d/m)/tau_D
      >= alpha_D/(1+eta_D)`,

where `alpha_D=d/m`.                                     (7.2)

The exact theta scalarization (1.6) is decreasing in `s_D=S_D/m`. Therefore, on the event `alpha_D>=1/4`,

`(X_D-1)_+
 <= 4( eta_D + |1-2 alpha_D| ).`                         (7.3)

Indeed, substituting `s_D>=alpha_D/(1+eta_D)` into (1.6), the positive part of the numerator difference is

`rho [1-2 alpha_D/(1+eta_D)]_+`,

while the denominator is at least

`rho alpha_D/(1+eta_D)`.

Their ratio is at most

`[(1+eta_D)-2alpha_D]_+/alpha_D
 <=4(eta_D+|1-2alpha_D|)`.                               (7.4)

For `d~Bin(m,1/2)`, Chernoff gives

`P(alpha_D<1/4) <= exp(-m/16)`,                          (7.5)

and always `X_D<=sqrt(n)`. Also

`E |1-2 alpha_D| <= 1/sqrt(m)`.                          (7.6)

Finally complement symmetry gives `E X_D>=1`. Hence:

## Theorem P07-A.54 — radial-cap criterion for Conjecture 18

For the exact fair source model,

`boxed(
0 <= E theta(G_n)/sqrt(n)-1
 <= 4 E eta_D + 4/sqrt(m) + sqrt(n) exp(-m/16).
)`                                                        (7.7)

In particular,

`boxed(
 E (tau_D-1)_+ = o(1)
 => E theta(G_n)=(1+o(1))sqrt(n).
)`                                                        (7.8)

### Significance

This is the corrected primal concentration target after Theorem P07-A.51 kills the Euclidean-energy route. It asks only for the **mean upper-cap excess** of a single radial vector after unrestricted transverse motion inside the selected row span. No small Euclidean correction, no lower coordinate control, and no global Fourier restricted-isometry theorem is required.

---

# 8. What failed, what changed, and the next attack

### Failed route now closed

The previous target `E E_D=o(sqrt(n))` cannot hold: Theorem P07-A.51 proves `E E_D=Omega(n)`. The obstruction is the source-Gaussian `15.9%` negative-coordinate fraction of the signed least-norm point. Continuing to seek a small Euclidean positive repair would therefore be mathematically stagnant.

### Fresh method

The new target is the one-sided minimax flattening problem (5.4), equivalently the positive radial-multiplier obstruction (6.3). It preserves the exact core mass and feeds directly into the requested **expectation** through (7.7).

A source-valid next lemma is now:

`CAP1:` construct measurable weights `y_D in R^D` with

`1^T y_D=d`

such that

`E [
  ( max_{j in M}
      { rho d/m
        -(2/sqrt(n)) sum_{a in D} y_D(a) cos(2 pi a j/n) }
    -1 )_+
 ] = o(1).`                                              (8.1)

By Theorem P07-A.54, `CAP1` alone proves Conjecture 18.

The first concrete attack on `CAP1` should be a **one-sided discrepancy / clipping iteration in coefficient space**: start from the radial coefficients `y=1_D`; whenever the upper physical polynomial exceeds `1`, move in a zero-sum selected-frequency direction that reduces only the active upper peaks. The exact dual (6.3) says such an iteration can fail only if its active positive multiplier has selected projection exactly parallel to `p_D`. Source randomness should then be used to rule out a persistent radial multiplier, rather than controlling every Fourier direction. This is substantially narrower than the discarded Euclidean repair program and remains distinct from P07-B's same-mask Fourier-dual recoupling problem.

---

## Self-checks

The identities (3.2), (4.4) and the coefficient minimax formula (5.2) were independently checked by linear programming on every mask for odd `n=5,7,9,11`; numerically `S_D tau_D=d` to solver tolerance in every nonempty case. These computations are only consistency checks; the proofs above are analytic and no finite numerical theta value is represented as an arbitrary-`n` theorem.

The Gaussian constant in (2.4) was independently evaluated from both the integral definition and `2 Phi(-1)-phi(1)`.

---

## Ledger delta

- full-source status: **OPEN / PROVED PARTIAL**;
- fixed headline metric: `alpha_LL: 1/2 -> 1/2`;
- source model and expectation/high-probability distinction preserved;
- **new obstruction:** the previous least-Euclidean positive repair has expected energy at least `(0.00941747...+o(1)) n`, so the `o(sqrt(n))` repair-energy route is impossible;
- **new exact all-odd-n dual:** `S_D=max{1^Tv:v in V_D, v<=1}`;
- **new exact flattening scalar:** `S_D=d/tau_D`;
- **new concrete certificate problem:** one-sided selected-frequency cosine-polynomial flattening with signed coefficients of fixed sum;
- **new exact positive-measure dual:** cap failure requires a probability vector whose selected-space projection is exactly radial;
- **new expectation criterion:** `E(tau_D-1)_+=o(1)` suffices for `E theta=(1+o(1))sqrt(n)`;
- next attack: prove `CAP1` by active-upper-peak coefficient clipping and rule out persistent radial multipliers;
- P07-B may freely use Theorems P07-A.51--P07-A.54 as shared exact lemmas without taking over this primal cap-flattening role;
- SRG69 remains preserved **OPEN / PARTIAL**, with no historical overwrite.