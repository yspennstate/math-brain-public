Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — level-Palm excursion budget, a dimension-two boundary-law reduction, and the remaining selection bias

Date: 2026-09-20 UTC  
Worker: C04 / R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Status: **PROVED PARTIAL**. The full Drewitz--Ramírez implication remains open in this work.

## 1. Source and inherited bridge

Source: Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20. In an i.i.d. uniformly elliptic nearest-neighbor environment on `Z^d`, `d>=2`, does positive limiting velocity in direction `ell` imply the source polynomial ballisticity condition? The standard effective threshold retained in this project is `M>=15d+5`.

The preceding R7-05 report proved the following reduction. If, for every direction `u` in an open neighborhood of `ell`, the initial pre-regeneration backward radius `R_u` satisfies

`r^(d-1) P_0(R_u>=r) -> 0`,

then Guerra's polynomial transience criterion of degree `d-1` applies, giving `(T)|ell`; Guerra--Ramírez then gives the standard `(P)_M|ell` conclusion. In dimension two the target is only

`r P_0(R_u>=r) -> 0`.

The missing step is to obtain that tail from positive velocity using the spatial i.i.d. structure, not from another finite-periodic model.

## 2. New theorem: positive speed gives a finite mean budget for a typical far-ahead level excursion

Fix a unit vector `u` with

`v_u := v dot u > 0`,

where `v` is the deterministic limiting velocity. Put

`a_u := max_i |u_i|`.

Every nearest-neighbor step changes the `u`-projection by at most `a_u`.

For integer `k>=0` define the threshold hitting times

`T_k^u := inf{n>=0 : X_n dot u >= k}`.

Positive velocity implies

`T_k^u/k -> 1/v_u` almost surely.

Define the depth of the excursion between successive threshold crossings by

`D_k^u := ( k - inf_{T_k^u <= n <= T_{k+1}^u} X_n dot u )_+`.

### Proposition 2.1 — deterministic depth/time inequality

For every path and every `k`,

`2 D_k^u + 1 <= a_u (T_{k+1}^u-T_k^u)`.

#### Proof

At time `T_k^u` the projection is at least `k`. If the path reaches a minimum `k-D_k^u`, then the total downward variation from the starting projection to that minimum is at least `D_k^u`. To finish the interval it must then reach projection at least `k+1`, requiring upward variation at least `D_k^u+1`. Hence the total absolute variation in the `u`-projection on the interval is at least `2D_k^u+1`. Each individual step contributes at most `a_u` absolute variation, proving the claim.

Summing from `k=0` to `N-1` gives

`2 sum_{k<N} D_k^u + N <= a_u T_N^u`.

Therefore

`limsup_{N->infinity} (1/N) sum_{k<N} D_k^u
 <= (1/2)(a_u/v_u - 1)`                                             (2.1)

almost surely. The right side is nonnegative because a walk whose projection steps are bounded by `a_u` cannot have speed larger than `a_u`.

This is already a nontrivial restriction coming from positive speed alone: although individual level excursions can be arbitrarily deep, their pathwise Cesaro depth budget is finite.

## 3. Annealed level-Palm compactness

Let

`nu_N^u := (1/N) sum_{k=0}^{N-1} Law_0(D_k^u)`.

These are deterministic probability laws on `[0,infinity)`.

### Proposition 3.1 — finite-mean subsequential level-Palm law

The family `{nu_N^u}` is tight. Every subsequential weak limit `nu_u` obtained along a subsequence selected from a tight sequence can be chosen to satisfy

`int_0^infinity r nu_u(dr) <= (1/2)(a_u/v_u - 1)`.               (3.1)

In particular,

`r nu_u([r,infinity)) -> 0`.                                  (3.2)

#### Proof

Fix `A>0`. Pathwise,

`A (1/N) # {k<N : D_k^u >= A}
 <= (1/N) sum_{k<N} D_k^u`.

The frequency on the left is bounded by one. By (2.1) and the reverse Fatou inequality for bounded random variables,

`limsup_N nu_N^u([A,infinity))
 <= [ (a_u/v_u -1)/2 ] / A`.

Hence the annealed laws are tight.

For a fixed truncation level `R`, the random variables

`(1/N) sum_{k<N} (D_k^u wedge R)`

are bounded by `R`, while their almost-sure limsup is bounded by the right side of (2.1). Reverse Fatou again gives

`limsup_N int (r wedge R) nu_N^u(dr)
 <= (1/2)(a_u/v_u -1)`.

Pass to a weakly convergent subsequence and then let `R->infinity`. Monotone convergence proves (3.1). Any finite-mean nonnegative law satisfies (3.2), because

`r nu_u([r,infinity))
 <= int_{[r,infinity)} x nu_u(dx) -> 0`.

QED.

### Interpretation

Positive speed automatically creates an asymptotic **typical far-ahead level-crossing law** whose backward-excursion depth has finite first moment. In `d=2`, this is exactly the tail exponent needed by Guerra's `d-1=1` criterion — but under the level-Palm law, not yet under the source's initial/failed-regeneration law.

That distinction is now the core issue.

## 4. Exact coordinate harmonic-measure density: where the selection bias sits

For this subsection take `u=e_1`, so threshold planes are

`H_k={x in Z^d : x_1=k}`

and `T_k` is the first hit of `H_k`. Let `Q_k` denote the annealed law of the shifted environment seen at the first hit of `H_k`:

`Q_k(A) = P_0( tau_{X_{T_k}} omega in A )`.

Then `Q_k` is absolutely continuous with respect to the original product environment law `P`, with an exact density

`f_k(omega)
 = sum_{x in H_k} P_{-x,omega}( X_{T_0}=0 )`.                  (4.1)

Here the probability on the right starts at `-x`, and `T_0` is the first hit of the plane `H_0`.

### Proof of (4.1)

For bounded measurable `g`,

`E_{Q_k} g
 = E_P [ sum_{x in H_k} P_{0,omega}(X_{T_k}=x) g(tau_x omega) ]`.

Use translation invariance of the i.i.d. law in each summand, replacing `omega` by `tau_{-x}omega`. The quenched path probability becomes the probability, in the unshifted environment, that a walk started at `-x` first reaches `H_0` at the origin. Thus

`E_{Q_k} g = E_P[g(omega) f_k(omega)]`.

Taking `g=1` also gives `E_P f_k=1`.

The formula is useful because it isolates the selection bias completely: the environment seen from a far-ahead first entrance is the original i.i.d. environment tilted by an incoming harmonic-measure density.

Now define the fresh one-level backward-excursion observable

`q_r(omega) := P_{0,omega}( T_{-r} < T_1 )`.

By the strong Markov property at `T_k` and translation,

`P_0(D_k^{e_1} >= r) = E_P[f_k q_r]`.                         (4.2)

Hence, writing

`bar f_N = (1/N) sum_{k=0}^{N-1} f_k`,

we have the exact identity

`nu_N^{e_1}([r,infinity)) = E_P[bar f_N q_r]`.                (4.3)

Combining Proposition 3.1 with (4.3), there is a subsequence `N_j` and a finite-mean law `nu_{e_1}` such that, for every fixed integer `r`,

`E_P[bar f_{N_j} q_r] -> nu_{e_1}([r,infinity))`,

and therefore

`r * lim_{j->infinity} E_P[bar f_{N_j} q_r] -> 0`              (4.4)

as `r->infinity`.

This is a genuine `1/r`-little-o tail produced by positive speed, but **after the incoming-harmonic-measure tilt**.

## 5. Dimension-two conditional closure criterion

The previous run reduced the source problem in `d=2` to a uniform `o(1/r)` bound for the depth of a failed regeneration attempt. The new level-Palm law gives a natural comparison target.

Let `B_j^u` be the downward depth of failed record attempt `j`, and `H_j` its attempt-start history. Let `K` be the first successful attempt, with the standard geometric tail

`P(K>=j) <= q^j`, `q<1`.

Suppose that for every `u` in a neighborhood of `ell` there exists one of the finite-mean level-Palm laws `nu_u` from Proposition 3.1 and a constant `C_u<infinity` such that

`P(B_j^u >= r, j<K | H_j)
 <= C_u nu_u([r,infinity)) 1_{K>=j}`                           (5.1)

for all sufficiently large `r`, uniformly in `j` and the realized history.

Then

`P(R_u>=r)
 <= [C_u/(1-q)] nu_u([r,infinity))`,

by the geometric failed-attempt compression proved in the preceding run. Since `nu_u` has finite first moment,

`r P(R_u>=r) -> 0`.

Thus in `d=2`, if (5.1) holds on an open cone around `ell`, Guerra's degree-one criterion yields `(T)|ell`, and Guerra--Ramírez yields the source-standard `(P)_M|ell` for `M>=15d+5`.

So the two-dimensional source problem has been reduced to a precise **boundary-law comparison**:

> compare the conditional law of an early failed record excursion, whose lower half-space is history-biased, with the finite-mean law of a typical far-ahead level excursion selected by harmonic measure.

This is genuinely different from asking for a high regeneration moment.

## 6. Why the Cesaro depth budget does not by itself solve the source problem

A purely pathwise argument cannot upgrade (2.1) to the uniform tail estimate needed at the origin.

Consider a deterministic nearest-neighbor path on `Z` which, on first reaching each positive integer level `k`, immediately advances to `k+1`, except when `k=j^2` is a perfect square. At level `j^2` it first walks backward by `j` steps, returns to `j^2`, and then advances to `j^2+1`.

The excursion depths are

`D_k = j` if `k=j^2`, and `D_k=0` otherwise.

Up to level `N`, the extra excursion time is

`2 sum_{j<=sqrt(N)} j = N + O(sqrt(N))`.

Hence the full path has positive limiting speed `1/2`. Even at the deepest point of the `j`th excursion, the relative setback is only `j/j^2=1/j`, so the pointwise velocity limit is unchanged.

However

`(1/N) sum_{k<N} D_k 1_{D_k>R} -> 1/2`

for every fixed `R`, as `N->infinity` and then the squares beyond `R^2` dominate the tail contribution. Thus the depth empirical laws can converge weakly to `delta_0` while losing a positive amount of first-moment mass to moving scales.

This example is **not an RWRE counterexample**. Its role is to prove that positive speed plus bounded increments alone does not provide the needed uniform-integrability or boundary-law comparison. The i.i.d. spatial environment must rule out this moving-scale selection mechanism.

## 7. What is now the strongest next attack

The most concrete next target is no longer another finite-periodic corrector and not a blind attempt to prove `E R_u<infinity` directly.

For `d=2`, prove an **observable-specific anti-selection estimate** comparing early failed-attempt depth with the level-Palm law. In the coordinate model, the exact bias is `bar f_N`; a sufficient prototype would be

`E_P[q_r] <= C E_P[bar f_{N(r)} q_r] + o(1/r)`                (7.1)

for a suitable scale `N(r)->infinity`, together with the analogous bound after each failed-record history. A global lower bound on `bar f_N` would be much stronger than necessary; (7.1) only asks that the incoming harmonic-measure tilt not systematically suppress the particular deep-backtracking observable by a polynomial factor.

The i.i.d. geometry enters exactly here. One can try to prove (7.1) by revealing the explored upper region, resampling the untouched lower region, and comparing the entrance harmonic measure before and after resampling. If this succeeds with `O(1)` distortion (or any distortion preserving `o(1/r)`), the dimension-two source implication closes through the chain already established.

For `d>2`, Proposition 3.1 supplies only a first-moment level-Palm law. Additional spatial input is still required to create the `d-1` moment/tail scale.

## 8. Status

- Full source implication: **OPEN / unchanged**.
- New proved partial theorem: positive speed gives a finite pathwise Cesaro budget for threshold-excursion depth in every direction with positive velocity component.
- New proved partial theorem: annealed level-excursion laws admit finite-first-moment subsequential Palm limits.
- New exact identity in a coordinate direction: the far-level entrance-environment law has incoming-harmonic-measure density (4.1), and level-excursion tails are weighted fresh tails as in (4.2)--(4.3).
- New conditional dimension-two closure: a uniform failed-attempt-to-level-Palm tail domination closes P0487 in `d=2`.
- Decisive obstruction: positive speed and bounded increments alone permit moving-scale excursion mass, so an i.i.d.-specific anti-selection argument is indispensable.
