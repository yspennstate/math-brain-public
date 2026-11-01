Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029 — dual root-energy lower bound and first-merge flux conservation

## 1. Source and cumulative starting point

Target: `P0029`, Krzysztof Burdzy, *My favorite open problems*, Problem 9, “Do peaks of random labelings repell each other?”  For a uniformly random labeling of the `n x n` discrete square conditioned on exactly two peaks, with `rho_n` their graph distance, the source asks whether `rho_n/n -> 0` in distribution.

The frozen source metric is

`D_* := limsup_{n -> infinity} E[rho_n/n | exactly two peaks]`.

This artifact continues the exact positive first-merge representation proved in the preceding R7-04 run. For a finite connected graph `G`, let `F_G(T)` count the birth-free completions after a nonempty revealed seed set `T`. For connected `C`, let

`h_C(r)=F_{G[C]}({r})`,

`R(C)=sum_{r in C} h_C(r)`,

`mu_C(r)=h_C(r)/R(C)`.

For a revealed first-merge prestate `S=A union B` with exactly two connected components, let

`g_G(S)=sum_{x in M_G(S)} F_G(S union {x})`,

where `M_G(S)` is the common boundary of the two components, and

`Omega_G(S)=binom(|S|,|A|) R(A)R(B)g_G(S)`.

The preceding run proved

`Z_2(G)=# {descending orders with exactly two births}=sum_S Omega_G(S)`

and, conditional on a first-merge prestate `S=A union B`, the two peaks are independent with laws `mu_A` and `mu_B`. Thus

`E[rho | two peaks]
 = [sum_S Omega_G(S) E_{mu_A x mu_B} d_G(R_A,R_B)] / Z_2(G)`.      (1.1)

For every connected `C` with at least two vertices, it also proved the conductance representation

`c_C({x,y}) := F_{G[C]}({x,y})`,

`mu_C(x) = [sum_{y~x} c_C({x,y})] / [2 sum_{e in E(C)} c_C(e)]`.    (1.2)

The purpose of this run is to apply the prescribed new methods **B11 / B12 / B27** to (1.1), not to extend the finite checker.

## 2. B11 — dualize: deterministic barycenter and dispersion lower bounds

Specialize to the `n x n` square `G_n`, with vertices embedded at their lattice coordinates `z=(z_1,z_2) in {0,...,n-1}^2`. Graph distance is the `l^1` metric.

For a connected component `C`, define its root barycenter and root second moment by

`b(C) := E_{mu_C} R_C in R^2`,

`V(C) := E_{mu_C} ||R_C-b(C)||_2^2`.                       (2.1)

For a singleton, these have the evident values `b(C)=the unique vertex` and `V(C)=0`.

### Proposition 2.1 — edge-midpoint formula for the root barycenter

If `|C|>=2` and `C_C:=sum_{e in E(C)}c_C(e)`, then

`b(C)
 = [1/(2 C_C)] sum_{ {x,y} in E(C)} c_C({x,y}) (x+y)`.     (2.2)

Moreover

`V(C)
 = [1/(2 C_C)] sum_{ {x,y} in E(C)} c_C({x,y})
     ( ||x-b(C)||_2^2 + ||y-b(C)||_2^2 )`.                 (2.3)

#### Proof

By (1.2), `mu_C(x)=deg_c(x)/(2C_C)`, where `deg_c(x)=sum_{y~x}c_C({x,y})`. Therefore

`sum_x mu_C(x)x
 = [1/(2C_C)] sum_x sum_{y~x} c_C({x,y}) x`.

Each undirected edge `{x,y}` contributes once as `c_C({x,y})x` and once as `c_C({x,y})y`, giving (2.2). Replacing `x` by `||x-b(C)||_2^2` in the same degree-sum identity gives (2.3). QED.

Thus the root law is not an opaque probability measure: its first two moments are exact positive weighted edge geometry.

### Proposition 2.2 — Lipschitz-dual barycenter bound

For any first-merge state `S=A union B`,

`E_{mu_A x mu_B} d_1(R_A,R_B) >= ||b(A)-b(B)||_1`.         (2.4)

#### Proof

For every `t in R^2` with `||t||_infty<=1`, the function `f_t(z)=t dot z` is 1-Lipschitz for `d_1`. Hence pointwise

`d_1(x,y) >= t dot (x-y)`.

Taking expectations gives

`E d_1(R_A,R_B) >= t dot (b(A)-b(B))`.

Taking the supremum over `||t||_infty<=1` yields the dual norm `||b(A)-b(B)||_1`. QED.

This is the Kantorovich-dual route in the minimal form needed here; no transport theorem is required.

### Proposition 2.3 — root-energy lower bound

Define

`q_n(S)
 := ||b(A)-b(B)||_2^2 + V(A)+V(B)`.                       (2.5)

Then for every first-merge state on `G_n`,

`E_{mu_A x mu_B} d_1(R_A,R_B)
 >= q_n(S) / [2(n-1)]`.                                   (2.6)

#### Proof

Independence and centering give the exact variance decomposition

`E ||R_A-R_B||_2^2
 = ||b(A)-b(B)||_2^2 + V(A)+V(B)
 = q_n(S)`.                                                (2.7)

For any two vertices of `G_n`,

`||x-y||_2^2 <= ||x-y||_1^2 <= 2(n-1)||x-y||_1`,          (2.8)

because the maximum `l^1` distance in the square is `2(n-1)`. Taking expectations in (2.8) and using (2.7) proves (2.6). QED.

Combining (1.1) and (2.6) yields the global positive lower bound

`E[rho_n/n | two peaks]
 >= [sum_S Omega_n(S) q_n(S)]
    / [2 n(n-1) sum_S Omega_n(S)]`.                        (2.9)

Define the dimensionless absorption-energy quantity

`Xi_n := [sum_S Omega_n(S) q_n(S)]
        / [n^2 sum_S Omega_n(S)]`.                         (2.10)

This is an auxiliary coordinate only; it does **not** replace the frozen source metric `D_*`. Equation (2.9) gives

`D_* >= (1/2) limsup_{n->infinity} Xi_n`.                  (2.11)

Therefore any proof that `limsup Xi_n>0` refutes the source's proposed convergence.

### Why the second-moment term is genuinely needed

A barycenter-only strategy is false as a statewise mechanism. On an odd square, take `B` to be a centered inner square, leave a one-lattice-layer moat, and take `A` to be a centered thick outer annulus. Then `A` and `B` are connected, have no edge between them, and have common-boundary merge vertices in the moat. Both induced graphs are invariant under the coordinate reflections. Since `h_C` and hence `mu_C` are graph-automorphism invariant, both barycenters are the geometric center, so

`b(A)=b(B)`.

Thus the dual lower bound (2.4) is zero even though the state is macroscopically extended. But every vertex of a thick annulus is a macroscopic Euclidean distance from the center, so `V(A)=Theta(n^2)` for such a family. The energy bound (2.6) detects exactly this failure mode. This is an obstruction to an overstrong B11 route, not a claim that such annular states carry positive `Omega_n` mass.

## 3. B12 — find what is conserved: two-front occupation and absorption flux

The first-merge representation also has an exact conservation law that identifies `Omega` as an absorption flux rather than an ad hoc weight.

Let `T_2(omega)` be the rank at which the second birth occurs in an exactly-two-birth descending order `omega`, and let `T_m(omega)` be the rank of the unique vertex that first merges the two revealed components. Then

`I_s(omega):=1{T_2(omega) <= s < T_m(omega)}`              (3.1)

is the indicator that the reveal process is in its two-component phase after `s` vertices have been exposed. Trajectory-by-trajectory,

`I_s-I_{s-1}=1{T_2=s}-1{T_m=s}`.                          (3.2)

This is the conserved injection-minus-absorption balance.

For a two-component set `S=A union B` of size `s`, put

`P_G(S):=binom(s,|A|)R(A)R(B)`.                           (3.3)

### Proposition 3.1 — exact active-state count

`P_G(S)` is exactly the number of length-`s` prefixes whose revealed set is `S`, whose revealed graph has components `A,B`, and which have exactly two births. Consequently

`Q_G(S):=P_G(S)F_G(S)`                                    (3.4)

is exactly the number of full exactly-two-birth orders that are in state `S` at time `s`.

#### Proof

Choose a one-birth successive order on `A` (`R(A)` choices) and independently one on `B` (`R(B)` choices). Interleave the two internal orders while preserving each internal order (`binom(s,|A|)` choices). Because there is no `A-B` edge, whichever component root appears second globally is a birth; every later vertex has an earlier neighbor in its own component. Thus there are exactly two births. The construction reverses uniquely by restricting a prefix to its two components, proving (3.3). Appending any birth-free suffix counted by `F_G(S)` gives exactly the full orders active at `S`, proving (3.4). QED.

### Proposition 3.2 — `Omega` is exactly first-merge flux

For every two-component state,

`Omega_G(S)=P_G(S)g_G(S)`,                                (3.5)

and hence

`Omega_G(S)/Q_G(S)=g_G(S)/F_G(S)=lambda_G(S)`,             (3.6)

where `lambda_G(S)` is the exact conditional probability that the next revealed vertex performs the first merge under the uniform birth-free suffix law.

If

`A_s := sum_{S: |S|=s, kappa(G[S])=2} Q_G(S)`,             (3.7)

`J_s := # {omega: exactly two births and T_2(omega)=s}`,

`M_s := # {omega: exactly two births and T_m(omega)=s}`,

then summing (3.2) over all exactly-two-birth orders gives

`A_s-A_{s-1}=J_s-M_s`.                                    (3.8)

Moreover

`M_{s+1}=sum_{S: |S|=s, kappa(G[S])=2} Omega_G(S)`.        (3.9)

Finally, summing (3.1) over `s` and over orders yields the exact Little-law identity

`sum_s A_s
 = sum_{omega} (T_m(omega)-T_2(omega))`,                    (3.10)

or, after division by `Z_2(G)`,

`[sum_s A_s]/Z_2(G)
 = E[T_m-T_2 | exactly two births]`.                       (3.11)

Equations (3.8)--(3.11) provide a second positive representation: the law `Omega/Z_2` is the absorption-flux law of the active two-front process `Q`, and `lambda=g/F` is its statewise hazard. Any attempt to prove `Xi_n>0` can therefore work either directly under the absorption law or under the active occupation law plus a comparison of the merge hazard across geometric energy classes.

The same conservation identity can be weighted by any nonnegative symmetric function of the two peak roots: multiply (3.2) by that root-pair observable before summing. Thus spatial observables can be carried through the flux balance without reintroducing the alternating independent-set representation.

## 4. B27 — swap the quantifiers: what is actually sufficient for a source-valid NO

The source metric is a `limsup`. We do not need a uniform lower bound for every first-merge state, every `n`, or every peak pair.

Let

`widehatOmega_n(S):=Omega_n(S)/Z_2(G_n)`.

### Corollary 4.1 — one-family energy criterion

Suppose there exist constants `c>0`, `eta>0`, and infinitely many `n` such that

`widehatOmega_n{ S: q_n(S) >= c n^2 } >= eta`.             (4.1)

Then

`D_* >= c eta / 2 > 0`,                                   (4.2)

so Burdzy Problem 9 has the source-valid answer **NO**.

#### Proof

Under (4.1), `Xi_n>=c eta` along that subsequence. Apply (2.11). QED.

There is an even sharper barycenter-only sufficient condition on any family where it applies. If for fixed `eps,eta>0` and infinitely many `n`,

`widehatOmega_n{S: ||b(A)-b(B)||_1 >= eps n} >= eta`,       (4.3)

then (2.4) and (1.1) give immediately

`D_* >= eps eta`.                                         (4.4)

The important quantifier change is that **only one positive-mass geometric family along one infinite subsequence is needed**. The previous routes were often trying to control all states or all root pairs, which is substantially stronger than the source requires.

The energy criterion (4.1) is more robust than (4.3): it also accepts states with coincident component barycenters but macroscopically diffuse root laws, such as the centered-annulus obstruction described above.

## 5. What has and has not moved

The fixed source quantity remains

`D_*: UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

No asymptotic lower bound on `Xi_n` has yet been proved. Therefore this run is **PARTIAL / NO MOVEMENT**, not a source refutation.

What did move structurally is the exact obstruction. The remaining task can now be stated without signed cancellation and without pointwise pair weights:

> Prove that the first-merge absorption measure `widehatOmega_n` assigns a fixed positive mass, along an infinite subsequence, to two-component states whose conductance-root energy `q_n(S)` is of order `n^2`; equivalently, prove `limsup Xi_n>0`.

The conserved active/absorption relation gives two possible places to attack this: (i) prove high energy is typical under the active two-front occupation law `Q`, then show the hazard `lambda=g/F` does not suppress it too strongly; or (ii) work directly with the absorption partition function.

No exact checker was created in this run because the results above are theorem-sized algebraic identities with complete proofs, and the owner directive forbids checker churn when the source metric has not moved.

## 6. Dated source/literature check

Checked 2026-09-18 UTC. Burdzy's current official open-problems page still displays Problem 9 in the exact square-grid form above and cites Billey--Burdzy--Sagan (2013) and Burdzy--Pal (2020). Burdzy--Pal, *Twin peaks*, Random Structures & Algorithms 56 (2020), 432--460, studies the same conditioned-labeling framework; its published abstract records the square one-peak result, ladder behavior, and two-peak tree results, not this square two-peak asymptotic. Agrawal--Erturk--Louis, *Successive vertex orderings of connected graphs*, arXiv:2604.07408 (2026), gives exact general successive-order enumeration and independent-set generating machinery, but does not settle this source endpoint. A bounded current search found no later direct solution; this is negative evidence only, not a novelty or worldwide-openness certificate.

## 7. Next nonrepeating methods if the target remains active

The next ordinary attack should not repeat B11/B12/B27. A coherent new triple is:

- **B5 (add a parameter and differentiate):** introduce exponential spatial tilts `H_C(theta)=sum_r h_C(r)e^{theta dot r}`; `grad log H_C(0)=b(C)` and `Hess log H_C(0)=Cov(mu_C)`. Lift the tilt through the positive first-merge partition function so `Xi_n` becomes a second derivative at zero of a positive partition function.
- **B14 (find the group acting):** exploit the `D_4` symmetries of the square and of symmetric component families to quotient the tilted absorption partition and separate barycenter displacement from within-component dispersion.
- **B28 (replace all by typical):** prove a positive-mass `Omega_n` energy statement rather than any uniform statewise inequality; explicitly control the low-energy exceptional absorption states.

If the fixed source metric remains unchanged after the next ordinary run, the evidenced CLOSABLE streak reaches six and the owner protocol requires an immutable handoff/retirement and rotation rather than indefinite lemma accumulation.