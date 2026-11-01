# P0487 admission-side mathematics — periodic spectral tilt, bounded correctors, and a negative-local-drift ballistic example

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Candidate only: `P0487`  
Shard check: `sum(ord(c) for c in "P0487") % 7 = 4`  
Admission state: **HARD / NOT ADMITTED**

## 1. Source and literature boundary

Repository source recovery identifies `P0487` with Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment*, Springer Proc. Math. Stat. 69 (2014), Open Question 3.20. In the i.i.d. uniformly elliptic setting on `Z^d`, `d>=2`, the question asks whether positive velocity in a direction `ell` forces the polynomial ballisticity condition `(P)_M` for the standard large-`M` range.

Guerra--Ramírez, *A Proof of Sznitman's Conjecture about Ballistic RWRE*, Comm. Pure Appl. Math. 73 (2020), proves the equivalence of `(T)`, `(T')`, `(T)_gamma` for some `gamma`, and `(P)_M` for `M>=15d+5`. Thus the unresolved bridge relevant to P0487 is still conceptually

`positive velocity  ==>  exponential/stretched-exponential wrong-way slab control`.

A bounded fresh search on 2026-09-19/20 for the exact implication and source terminology did not surface a later theorem proving this implication. This is negative evidence only, not proof that no resolution exists.

The preceding R7-05 artifact proved an exponential slab bound under the much stronger hypothesis of a uniform pointwise drift margin and solved the homogeneous case exactly. This run does not repeat that route. It asks whether a **nonconstant multiplicative corrector** can recover exponential slab control when some sites have negative local drift.

## 2. Idea before code

The constant exponential test function `exp(-theta x.ell)` fails as soon as some local drifts point backward. The natural replacement is

`F(x)=exp(-theta x.ell) h(state(x))`,

where `h>0` compensates for local bad phases. In a finite periodic environment, `h` is supplied exactly by Perron--Frobenius theory for a tilted finite-state transition matrix.

This gives a complete periodic theorem, an exact two-phase example with genuinely negative local drift on half the sites, and a precise infinite-state object that the i.i.d. source problem would need to construct.

Methods this run: **B15 / B20 / B30**.

## 3. B30 — one scale and one direction: finite-state Markov-additive theorem

Consider a finite state space `E`. From state `i`, one step chooses a new state `j` and a bounded real additive increment `z`; write the joint transition law as `p_ij(dz)`. Let

`P_ij = integral p_ij(dz)`

and assume `P` is irreducible. Let `pi` be its stationary distribution. Define the additive coordinate

`S_n = z_1 + ... + z_n`

and the stationary mean increment

`mu = sum_i pi_i sum_j integral z p_ij(dz)`.

For real `theta` near zero, define the tilted matrix

`K_theta(i,j) = integral exp(-theta z) p_ij(dz)`.

### Theorem 3.1 — positive finite-state drift produces an exponential corrector

If `mu>0`, then there exist `theta>0`, `r<1`, and a strictly positive vector `h` such that

`K_theta h = r h`.

Consequently, for

`tau_- = inf{n>=0:S_n<=-L}` and `tau_+ = inf{n>=0:S_n>=L}`,

one has, from every initial internal state,

`P(tau_- < tau_+) <= (h_max/h_min) exp(-theta L)`.          (3.1)

#### Proof

Because increments are bounded, `K_theta` is analytic in `theta` near zero. At `theta=0`, `K_0=P`, whose Perron eigenvalue `1` is simple because `P` is finite and irreducible. Let `r(theta)` denote the analytic continuation of this Perron eigenvalue, normalized with left eigenvector `pi` and right eigenvector `1` at zero. Standard simple-eigenvalue differentiation gives

`r'(0) = pi^T K'_0 1`.

But

`K'_0(i,j) = - integral z p_ij(dz)`,

so

`r'(0) = -mu < 0`.

Hence `r(theta)<1` for all sufficiently small `theta>0`. Perron--Frobenius supplies a strictly positive right eigenvector `h` for `K_theta`.

Now set

`Y_n = exp(-theta S_n) h(J_n)`.

Conditioning on the present state,

`E[Y_{n+1}|F_n]
 = exp(-theta S_n) (K_theta h)(J_n)
 = r(theta)Y_n
 <= Y_n`.

Thus `Y_n` is a nonnegative supermartingale. Stop at

`tau=tau_- wedge tau_+`.

For every `N`, optional stopping at `tau wedge N` gives

`E Y_{tau wedge N} <= Y_0 <= h_max`.

On `{tau_-<tau_+, tau<=N}` we have `S_tau<=-L`, so

`Y_tau >= exp(theta L) h_min`.

Therefore

`P(tau_-<tau_+, tau<=N) <= (h_max/h_min) exp(-theta L)`.

Let `N->infinity`. This proves (3.1). QED.

### Interpretation

The theorem needs no pointwise positive drift. It needs only positive stationary drift of a finite internal-state Markov additive process. The price for allowing locally backward states is the nonconstant positive corrector `h`.

## 4. Periodic deterministic RWRE corollary

Let a nearest-neighbor environment on `Z^d` be periodic with respect to a finite-index lattice. Modulo the period lattice, the walk has a finite irreducible internal state `J_n`; the displacement in any fixed direction is an additive functional of the quotient transition.

If the limiting velocity satisfies

`v.ell > 0`,

then the stationary mean additive increment in direction `ell` equals `v.ell`, and Theorem 3.1 yields

`P_omega(H_{-L}^{ell}<H_{+L}^{ell}) <= C exp(-theta L)`

for constants `C<infinity`, `theta>0`.

Moreover, the finite tilted matrix depends continuously on the direction. Since `v.ell>0`, the same spectral inequality persists for all directions `ell'` in a sufficiently small neighborhood of `ell`. Thus positive velocity in a finite periodic uniformly elliptic environment implies a genuine exponential slab condition in a neighborhood of the velocity direction.

This is a complete theorem for the periodic subclass. It is **not** the i.i.d. source theorem.

## 5. B15 — break the local-drift symmetry on purpose

Here is an exact two-dimensional uniformly elliptic periodic example in which half the phases have **negative local drift**, yet the walk has positive speed and an explicit exponential corrector.

Let the transition probabilities depend only on the parity of `x_1`.

For even `x_1`:

- `+e_1`: `1/2`,
- `-e_1`: `1/10`,
- `+e_2`: `1/5`,
- `-e_2`: `1/5`.

For odd `x_1`:

- `+e_1`: `1/4`,
- `-e_1`: `7/20`,
- `+e_2`: `1/5`,
- `-e_2`: `1/5`.

The environment is uniformly elliptic with ellipticity constant `1/10`.

The local `e_1` drift is

`2/5` on even sites,

but

`-1/10` on odd sites.

Thus the pointwise-drift hypothesis from the preceding R7-05 run fails on every odd vertical line.

The parity chain changes state with probability `3/5` and stays put with probability `2/5` from either parity. Hence its stationary law is uniform. The exact limiting `e_1` velocity is therefore

`v_1 = (1/2)(2/5-1/10) = 3/20 > 0`.          (5.1)

### Exact tilted matrix

For `theta>0`, write

`a_0(theta)= (1/2)e^{-theta} + (1/10)e^{theta}`,

`a_1(theta)= (1/4)e^{-theta} + (7/20)e^{theta}`.

The tilted two-state matrix is

`K_theta = [[2/5, a_0(theta)], [a_1(theta), 2/5]]`.

Its Perron eigenvalue is

`r(theta)=2/5 + sqrt(a_0(theta)a_1(theta))`.

Put `y=e^{2theta}`. An exact multiplication gives

`a_0(theta)a_1(theta)
 = 1/(8y) + 1/5 + 7y/200`.

Therefore

`r(theta)<1`

is equivalent to

`1/(8y) + 1/5 + 7y/200 < 9/25`,

which after multiplying by `200y` becomes

`7y^2 - 32y + 25 < 0`

or

`(y-1)(7y-25)<0`.

Hence

`boxed[ 0 < theta < (1/2) log(25/7) ]`          (5.2)

is an exact nonempty interval of exponential tilts.

A positive right Perron vector is

`h(theta) = (sqrt(a_0(theta)), sqrt(a_1(theta)))`.

Thus for every `theta` in (5.2),

`P_omega(H_{-L}^{e_1}<H_{+L}^{e_1})
 <= sqrt(max(a_0,a_1)/min(a_0,a_1)) exp(-theta L)`.          (5.3)

This gives a fully explicit source-adjacent example where **positive speed plus a nonconstant corrector succeeds although uniform local drift is false**.

## 6. B20 — find why the obvious algorithm fails, and the exact replacement

The previous run used the constant test function `h=1`. That can only work when

`sum_e omega(x,e) exp(-theta e.ell) <= 1`

holds at every site; differentiating at `theta=0` forces nonnegative local drift at every site, so bad-drift phases destroy that route.

The periodic example shows that the failure is not fatal. The exact replacement is a bounded positive corrector.

### Corrector criterion

For a fixed deterministic environment, suppose there exist `theta>0` and a function `H:Z^d->(0,infinity)` with

`0 < c <= H(x) <= C < infinity`

such that for every `x`,

`sum_{|e|=1} omega(x,e) exp(-theta e.ell) H(x+e) <= H(x)`.          (6.1)

Then

`Y_n = exp(-theta X_n.ell) H(X_n)`

is a nonnegative quenched supermartingale, and exactly the same stopping argument gives

`boxed[ P_omega(H_{-L}^ell < H_{+L}^ell) <= (C/c) exp(-theta L) ]`.          (6.2)

The uniform-drift theorem from the preceding run is the special case `H=1`. The periodic theorem constructs `H` by lifting the finite Perron vector from the quotient.

### Infinite-state source bottleneck

For an i.i.d. RWRE, the analogous tilted operator on environments viewed from the particle is formally

`(K_theta h)(omega)
 = sum_e omega(0,e) exp(-theta e.ell) h(tau_e omega)`.

If one could construct a positive `h` bounded above and below with

`K_theta h <= h`

for some `theta>0`, then `(T)`-type slab control would follow immediately from (6.2). Positive velocity supplies only a long-time averaged drift statement; it does **not** by itself provide this pointwise tilted corrector.

This identifies a sharper version of the P0487 bridge:

`positive velocity`

must somehow be upgraded to

`a bounded positive exponential corrector (or a renormalized block analogue)`.

The finite periodic theorem proves that this upgrade is automatic in a finite internal-state model. The i.i.d. source difficulty is the infinite-dimensional environment state space and the absence of a finite Perron--Frobenius compactness argument.

## 7. What this changes and what it does not

New cumulative facts from this run:

1. A complete finite-state Markov-additive theorem: positive stationary drift implies exponential wrong-way slab exit via the derivative of the tilted Perron eigenvalue.
2. A complete periodic-RWRE corollary: positive velocity in a finite periodic uniformly elliptic environment implies an exponential slab condition.
3. A fully explicit `d=2` period-two environment with negative local drift on half the phases, positive speed `3/20`, and exact admissible tilt interval `0<theta<(1/2)log(25/7)`.
4. An exact bounded-corrector criterion (6.1)--(6.2) that strictly generalizes the preceding constant-corrector/local-drift route.
5. The source bottleneck is sharpened from "find a renormalized drift" to "construct a bounded positive tilted corrector, or a block-scale substitute, from positive velocity alone."

What is **not** proved:

- no implication from positive velocity to `(T)` in i.i.d. random environment;
- no source-level proof or refutation of P0487;
- no novelty claim for the finite-state spectral-tilt theorem (it is a standard Markov-additive/Perron--Frobenius mechanism in different language);
- no CLOSABLE classification.

P0487 remains **HARD / OPEN-LOOKING / NOT ADMITTED** by R7-05.

## 8. Admission state

The current canonical claim path `operations/claims/P0487.md` was absent at the pre-delivery master check, but absence of a claim is not enough for admission. The theorem-scale source target remains mismatched to this slot's required CLOSABLE OUTSIDE class.

Accordingly:

- R7-05 target remains `PENDING_ADMISSION`;
- successor metric remains `UNKNOWN/UNMEASURED`;
- successor stagnation count is not instantiated;
- no claim is created;
- no shared `RESULTS/QUEUE/POSTED` file is edited.

## 9. Next mathematical route if P0487 is revisited only as admission-side work

Do not repeat B15/B20/B30 next time. The most informative next triple would be:

- **B5**: add a disorder parameter to a finite-period environment and differentiate the tilted spectral radius/eigenvector;
- **B18**: reformulate the bounded-corrector condition as a multiplicative Poisson equation for the environment-seen-from-the-particle chain;
- **B23**: assume the opposite — construct positive-speed stationary ergodic examples where every bounded one-step corrector fails, to determine whether block correctors are genuinely necessary.

These are admission-side directions only unless a future repository delta supplies a genuinely free shard-4 CLOSABLE source.