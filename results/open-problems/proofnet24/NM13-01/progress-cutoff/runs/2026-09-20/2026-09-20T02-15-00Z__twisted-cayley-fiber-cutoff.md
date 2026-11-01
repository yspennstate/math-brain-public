Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — twisted Cayley finite extensions and orbital entropy disintegration

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem proved here, pending later independent review; **PARTIAL / OPEN** for Salez Problem 2.3. Publication novelty is **UNVERIFIED**.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.
Pre-support-write master observed during the run: `4f5f50ce4069e0283044b377b8f22fa56c28dfb2`; concurrent fleet commits continued afterward.

## 0. Continuity and the deliberate new route

The pre-LIVE20 NM13-01 admission history is preserved. Under LIVE20 this slot works on T08.

Two previous NM13-01 T08 runs established, respectively:

1. cutoff for line graphs of fixed-degree edge-transitive long-range expanders by an incidence intertwining and constant-rate decay of endpoint-invisible modes; and
2. cutoff for graph truncations of fixed-degree arc-transitive long-range expanders by a non-lumpable two-state port/radial process, with a quantitative `O(sqrt(log n))` window.

The second report ended with a proposed finite directed-edge-orbit attack. Meanwhile P26 developed an exact finite-fiber/lexicographic entropy-TV transfer. I therefore do **not** repackage P26's commuting finite-fiber mechanism here.

This run takes a materially different route:

> build a **twisted finite-group Cayley extension** in which macroscopic moves carry fiber permutations rather than resetting the fiber, so the cross and local dynamics can genuinely fail to commute. Prove cutoff by pathwise `L^2` contraction under interspersed unitary permutations. Then correct and remove the earlier "arc transitivity is needed to synchronize directional entropy" obstruction by a finite-mixture entropy lemma and an automorphism-orbit Markov-chain reduction.

The first part enlarges the source-valid theorem class; the second part removes a mechanism-level obstruction toward the general conjecture.

## 1. Exact source and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), uses rate-one continuous time

\[
P_t=e^{t(T-I)}=e^{-t}\sum_{k\ge 0}\frac{t^kT^k}{k!},
\]

that is, independent mean-one exponential holding times. Problem 2.3 states:

> **Prove that all vertex-transitive expanders exhibit cutoff.**

Here expanders have diverging size, uniformly bounded degree, and spectral gaps bounded away from zero.

The relevant newer primary results remain:

- Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026: every fixed-degree long-range-expander sequence has cutoff with an explicit Gaussian profile; every Ramanujan graph is long-range expanding; and
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with **neither converse**. Thus long-range expansion is not interchangeable with Salez's arbitrary spectral-expansion hypothesis.
- Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, 6 July 2026: the local-product/non-equilibrium spectral criterion gives a universal cutoff-window theorem in terms of their `gamma_*`, but no current theorem derives the needed lower bound solely from vertex transitivity plus a fixed ordinary spectral gap.

A current neighboring PROB10-08 run also proved that Altschuler's tree-rate growth need only persist to the pre-entropic scale `n exp(-rho_n)` with `rho_n=o(log n)`. Importantly, that run proved that even this weakened maximal-tree-rate condition does **not** follow from vertex transitivity plus spectral expansion: the two-copy/matching construction has the wrong ambient branching rate. I treat that as a genuine obstruction and do not retry the same route.

The posted Abelian-Cayley/product-condition material concerns Salez Problem 2.4 and is not reopened.

### Bounded prior-art check, 20 September 2026

I searched combinations of `finite extension Cayley cutoff`, `skew product random walk cutoff Cayley finite group`, `twisted product Cayley graph mixing`, `cocycle finite-fiber cutoff`, and repository searches for the same mechanism. I found general Cayley-expander, lift, and product literature but did not locate the exact pathwise twisted-fiber theorem below. This is bounded negative evidence only. The safe label is **NEW REPOSITORY THEOREM / PUBLICATION NOVELTY UNVERIFIED**.

## 2. Source-level before / after

### Before this run

Salez Problem 2.3 was OPEN. Positive scope available to this project included Altschuler's long-range expanders, repository vanishing/pre-entropic LRE extensions, NM13-01's line-graph and graph-truncation non-LRE classes, and P26's exact lexicographic finite-fiber blow-ups.

### After this run

Salez Problem 2.3 remains OPEN. The source-compatible proved scope is enlarged by a different class:

> **Any fixed finite-group twisted Cayley thickening of a continuous-time cutoff Cayley base inherits cutoff after an explicit constant time rescaling, even when cross-fiber and local-fiber kernels do not commute. Applied to fixed-degree Ramanujan/LRE Cayley bases, this gives bounded-degree vertex-transitive spectral expanders which are polynomially far from uniform long-range expansion and have an `O(sqrt(log n))` continuous-time cutoff window.**

This is a theorem-scope gain, not a claim that the full conjecture is solved.

## 3. The twisted finite-group construction

Let

\[
G_n=\operatorname{Cay}(\Gamma_n,S_n)
\]

be a connected simple Cayley graph with a fixed symmetric generating set

\[
S_n=S_n^{-1},\qquad |S_n|=d\ge 3.
\]

Let `K` be a fixed finite group, and let

\[
F=\operatorname{Cay}(K,T),\qquad T=T^{-1},\qquad |T|=s\ge 1,
\]

be connected and simple. Write `W` for SRW on `F` and

\[
\gamma_F:=1-\lambda_2(W)>0.
\]

Choose any map

\[
\phi_n:S_n\to K
\]

satisfying only the inverse compatibility

\[
\phi_n(u^{-1})=\phi_n(u)^{-1}.
\tag{3.1}
\]

Define

\[
H_n=\operatorname{Cay}(\Gamma_n\times K,U_n)
\]

with generating set

\[
U_n=
\{(u,\phi_n(u)):u\in S_n\}
\cup
\{(e,t):t\in T\}.
\tag{3.2}
\]

Thus a **cross move** changes the base coordinate and carries a prescribed fiber permutation, while a **vertical move** changes only the fixed fiber. Put

\[
D=d+s,\qquad a=\frac dD,\qquad b=\frac sD.
\tag{3.3}
\]

The vertical generators alone generate `{e}xK`, and after multiplying a cross generator by a suitable vertical word one obtains `(u,e)`. Hence `U_n` generates the full direct product. The graph is therefore connected. It is `D`-regular and vertex-transitive because it is a Cayley graph.

The point is that this is not P26's lexicographic reset. A cross move sends

\[
(g,k)\mapsto(gu,k\phi_n(u));
\]

it does not choose a fresh uniform fiber point. For nonabelian `K` and non-normal `T`, the cross and vertical kernels can fail to commute. The executed finite checker below gives an example with commutator norm `0.125`.

## 4. Main theorem: pathwise twisted-fiber cutoff transfer

Let `P_n` denote SRW on `G_n`, and let

\[
\mathsf H^G_t=e^{t(P_n-I)},
\qquad
\mathsf H^H_t=e^{t(Q_n-I)}
\]

be the rate-one Salez-convention semigroups on `G_n` and `H_n`. Let

\[
d_G(t)=\max_g\|\delta_g\mathsf H^G_t-\pi_G\|_{\rm TV},
\qquad
d_H(t)=\max_{g,k}\|\delta_{(g,k)}\mathsf H^H_t-\pi_H\|_{\rm TV}.
\]

### Theorem T08-NM01-TWIST

For every `n` and every `t>=0`,

\[
\boxed{
 d_G(at)
 \le d_H(t)
 \le d_G(at)+C_K e^{-b\gamma_F t},
 \qquad C_K=\frac12\sqrt{|K|-1}.
}
\tag{4.1}
\]

Consequently, for every fixed `epsilon in (0,1)`,

\[
\boxed{
\frac1a t^G_{\rm mix}(\epsilon)
\le t^H_{\rm mix}(\epsilon)
\le
\max\left\{
\frac1a t^G_{\rm mix}(\epsilon/2),
\frac1{b\gamma_F}\log\frac{2C_K}{\epsilon}
\right\}.
}
\tag{4.2}
\]

If `G_n` has cutoff at centers `T_n->infinity` with a quantitative window `w_n=o(T_n)`, then

\[
H_n
\quad\text{has cutoff at}\quad
\frac{T_n}{a}=\frac{d+s}{d}T_n
\tag{4.3}
\]

with window `O(w_n+1)`. In particular, when `w_n->infinity` the order of the window is unchanged. If the base has a limiting profile

\[
d_G(T_n+zw_n)\to\Psi(z),
\]

then

\[
d_H\!\left(\frac{T_n+zw_n}{a}\right)\to\Psi(z).
\tag{4.4}
\]

### Proof

Split the rate-one jump clock according to the two generator types. By Poisson thinning, the cross events form a Poisson process of rate `a` and the vertical events an independent Poisson process of rate `b`.

#### Step 1: exact base projection

A vertical event does not alter the base coordinate. A cross event chooses `u in S_n` uniformly and sends `g` to `gu`. Hence the projected base process is exactly rate-`a` SRW on `G_n`:

\[
\operatorname{Law}(G_t\mid G_0=g)=\delta_g\mathsf H^G_{at}.
\tag{4.5}
\]

Projection contracts total variation, so immediately

\[
d_H(t)\ge d_G(at).
\tag{4.6}
\]

#### Step 2: condition on the full cross trajectory

Fix the complete cross trajectory up to real time `t`: its event times and labels `u_1,u_2,...`. On the fiber, each cross event acts by right multiplication by `phi_n(u_i)`, hence by a permutation of `K`. Such a permutation preserves the uniform law `u_K`, preserves the mean-zero subspace of `L^2(u_K)`, and is unitary there.

Between two consecutive cross events, the fiber evolves by the vertical continuous-time semigroup

\[
e^{\tau b(W-I)}.
\]

Because `F` is a finite connected undirected Cayley graph, the restriction of this semigroup to mean-zero functions has `L^2(u_K)` norm at most

\[
e^{-b\gamma_F\tau}.
\tag{4.7}
\]

The cross permutations need not commute with this semigroup; that is irrelevant. Along the conditioned trajectory they are merely interspersed `L^2` isometries. Multiplying the contraction factors over all vertical time intervals, whose lengths sum to `t`, yields

\[
\left\|
\frac{\nu_t^{\Xi}}{u_K}-1
\right\|_{L^2(u_K)}
\le
 e^{-b\gamma_F t}
\left\|
\frac{\delta_k}{u_K}-1
\right\|_{L^2(u_K)}
=\sqrt{|K|-1}\,e^{-b\gamma_F t}.
\tag{4.8}
\]

Here `Xi` denotes the conditioned cross trajectory. By Cauchy--Schwarz,

\[
\|\nu_t^{\Xi}-u_K\|_{\rm TV}
\le C_K e^{-b\gamma_F t}.
\tag{4.9}
\]

#### Step 3: remove the conditioning

For each conditioned cross trajectory, replace the actual terminal fiber law by `u_K`, leaving the cross trajectory and therefore the terminal base coordinate unchanged. Averaging these modified laws gives exactly

\[
(\delta_g\mathsf H^G_{at})\otimes u_K,
\]

because every cross permutation preserves `u_K`. Convexity of total variation and (4.9) give

\[
\left\|
\delta_{(g,k)}\mathsf H^H_t
-(\delta_g\mathsf H^G_{at})\otimes u_K
\right\|_{\rm TV}
\le C_K e^{-b\gamma_F t}.
\tag{4.10}
\]

Uniform measure on `Gamma_n x K` is `pi_G x u_K`. Uniform lifting preserves total variation exactly, so the triangle inequality yields the upper bound in (4.1). Equations (4.2)--(4.4) follow directly. `square`

### Why this is genuinely different from the P26 fiber theorem

P26's lexicographic theorem obtains an exact semigroup decomposition because a macroscopic jump **uniformly resets** the finite fiber and the relevant kernels commute. Here a macroscopic jump carries a deterministic twist depending on the chosen base generator. Cross and vertical operators can be noncommuting. The proof survives because it only needs the vertical gap plus the fact that every twist is a uniform-measure-preserving `L^2` isometry.

Thus the reusable mechanism is:

> **fixed local noise + arbitrary interspersed measure-preserving fiber permutations preserve a pathwise exponential memory-loss rate.**

No entropy/Green-function transfer is used.

## 5. Spectral expansion transfers with an explicit gap

Assume the normalized one-sided base gap is

\[
1-\lambda_2(P_n)\ge\gamma_G>0.
\]

### Proposition 5.1

The output satisfies

\[
\boxed{
\operatorname{gap}(H_n)
\ge
\min\{a\gamma_G,b\gamma_F\}.
}
\tag{5.1}
\]

### Proof

For `f:Gamma_n x K -> R`, define the fiber average

\[
\bar f(g)=\frac1{|K|}\sum_{k\in K}f(g,k)
\]

and the within-fiber variance

\[
V_{\rm fib}
=\frac1{|\Gamma_n|}\sum_g
\operatorname{Var}_{u_K}(f(g,\cdot)).
\]

The law-of-total-variance identity is exact:

\[
\operatorname{Var}_{\pi_H}(f)
=
\operatorname{Var}_{\pi_G}(\bar f)+V_{\rm fib}.
\tag{5.2}
\]

Write `E_cross` and `E_vert` for the Dirichlet forms of the kernels that choose only a cross generator or only a vertical generator. For a cross generator `u`, the map `k -> k phi_n(u)` is a permutation of `K`. Jensen therefore gives, edge by edge and then after averaging,

\[
\mathcal E_{\rm cross}(f,f)
\ge
\mathcal E_{P_n}(\bar f,\bar f)
\ge
\gamma_G\operatorname{Var}_{\pi_G}(\bar f).
\tag{5.3}
\]

Fiberwise Poincare gives

\[
\mathcal E_{\rm vert}(f,f)
\ge\gamma_F V_{\rm fib}.
\tag{5.4}
\]

Since the full SRW kernel is the convex combination

\[
Q_n=aQ_{\rm cross}+bQ_{\rm vert},
\]

its Dirichlet form is the same convex combination. Combining (5.2)--(5.4),

\[
\mathcal E_{Q_n}(f,f)
\ge
\min\{a\gamma_G,b\gamma_F\}
\operatorname{Var}_{\pi_H}(f).
\]

This proves (5.1). `square`

Thus a spectral-expander Cayley base yields a bounded-degree vertex-transitive spectral-expander output.

## 6. The output is polynomially outside uniform long-range expansion

This is the source-relevant class separation.

Let

\[
N_n=|V(H_n)|=|K|\,|\Gamma_n|,
\qquad D=d+s.
\]

A path of length `r` in `H_n` projects to a base path of length at most `r`: vertical moves project to stays and cross moves to base edges. Therefore for every `(g,k)`,

\[
|B_{H_n}((g,k),r)|
\le |K|\,|B_{G_n}(g,r)|.
\tag{6.1}
\]

Every `d`-regular graph obeys the universal tree upper bound

\[
|B_{G_n}(g,r)|\le C_d(d-1)^r.
\tag{6.2}
\]

Hence

\[
|B_{H_n}((g,k),r)|
\le C_{d,K}(d-1)^r.
\tag{6.3}
\]

Altschuler's long-range-expansion definition for the `D`-regular output uses the branching parameter `D-1`, not `d-1`. Set

\[
r_n=\left\lfloor\frac12\log_{D-1}N_n\right\rfloor.
\]

At this radius, for any fixed candidate LRE constant `c'>0`, the LRE singleton lower bound would still be in the unsaturated branch and would require order

\[
c'(D-1)^{r_n}\asymp c' N_n^{1/2}.
\]

But (6.3) is at most

\[
C N_n^{\frac12\log_{D-1}(d-1)+o(1)}.
\]

Since `d-1<D-1`, this is a smaller power of `N_n`. More quantitatively, any admissible LRE constant `c'_n` must satisfy

\[
\boxed{
 c'_n\le C_{d,K,T}\,N_n^{-\beta+o(1)},
 \qquad
 \beta=\frac12\left(1-\frac{\log(d-1)}{\log(D-1)}\right)>0.
}
\tag{6.4}
\]

Therefore these outputs are not merely unproved to be LRE: they **cannot** form a uniform long-range-expander sequence. This separates the new class from Altschuler's hypothesis.

## 7. Explicit quantitative source-valid family

Take a fixed-degree Cayley Ramanujan family, for example a standard LPS-type sequence with fixed degree `d>=3`. Altschuler's current theorem gives long-range expansion for Ramanujan graphs, and the already established Salez-continuous-time conversion in the T08 repository history gives the rate-one cutoff center

\[
T_n^G
=\frac d{d-2}\log_{d-1}|\Gamma_n|
\tag{7.1}
\]

with window

\[
O(\sqrt{\log|\Gamma_n|}).
\tag{7.2}
\]

Choose, for instance, the fixed fiber `K=S_3` with the symmetric generating set

\[
T=\{(12),(23)\},
\qquad s=2,
\]

and any inverse-compatible twists `phi_n`. They may be chosen so that the cross and vertical kernels genuinely do not commute.

Theorem T08-NM01-TWIST gives a degree-`d+2` vertex-transitive spectral-expander sequence with

\[
\boxed{
T_n^H
=\frac{d+2}{d-2}\log_{d-1}|\Gamma_n|
}
\tag{7.3}
\]

and window

\[
\boxed{O(\sqrt{\log|\Gamma_n|})=O(\sqrt{\log|V(H_n)|}).}
\tag{7.4}
\]

By (6.4), this sequence is polynomially outside uniform LRE. This is the promised new source-valid cutoff class.

The construction is broader than this application: the base need only be a Cayley sequence with a known continuous-time cutoff, not necessarily LRE or Ramanujan.

## 8. Removing the directional-entropy synchronization obstruction

The previous NM13-01 truncation report stated that full arc transitivity was used to equalize the entropy of fixed-first-edge NBRW sectors, and proposed finitely many directed-edge orbits as the next obstacle. That entropy synchronization issue can in fact be removed by a general finite-mixture inequality. This corrects an unnecessarily strong step in the previous mechanism without invalidating its theorem.

### Lemma 8.1 — finite-state entropy disintegration

Let `Y` take values in an `n`-point set and let `J` be any finite-valued random variable with probabilities `p_j`. If

\[
H(Y)\ge\log n-\Delta,
\]

then, writing

\[
\delta_j:=\log n-H(Y\mid J=j)\ge0,
\]

we have

\[
\boxed{
\sum_j p_j\delta_j
\le \Delta+H(J)
\le \Delta+\log |\operatorname{supp}J|.
}
\tag{8.1}
\]

Consequently every state with `p_j>=p_*` obeys

\[
\boxed{
H(Y\mid J=j)
\ge
\log n-\frac{\Delta+\log |\operatorname{supp}J|}{p_*}.
}
\tag{8.2}
\]

Also, for any `A>0`, the total probability of states with conditional entropy deficit exceeding `A` is at most

\[
\frac{\Delta+\log |\operatorname{supp}J|}{A}.
\tag{8.3}
\]

### Proof

The joint-entropy chain rule gives

\[
H(Y)\le H(Y,J)=H(J)+H(Y\mid J).
\]

Therefore

\[
\begin{aligned}
\sum_jp_j\delta_j
&=\log n-H(Y\mid J)\\
&\le \log n-H(Y)+H(J)\\
&\le\Delta+H(J).
\end{aligned}
\]

This is (8.1). Nonnegativity of every `delta_j` gives (8.2), while Markov's inequality gives (8.3). `square`

### Corollary 8.2 — fixed NBRW prefixes need no symmetry at all

For NBRW on a `d`-regular graph, there are

\[
M_\ell=d(d-1)^{\ell-1}
\]

admissible prefixes of a fixed length `ell>=1` from a fixed starting vertex, all with probability `1/M_ell`. If the endpoint at time `j` has entropy at least `log n-Delta`, then **every** fixed-prefix conditional endpoint law satisfies

\[
\boxed{
H(Y_j\mid \text{prefix }\omega)
\ge
\log n-M_\ell(\Delta+\log M_\ell).
}
\tag{8.4}
\]

For fixed `d,ell`, a marginal deficit `O(log log n)` therefore remains `O(log log n)` in every directional prefix sector. Arc transitivity is unnecessary for this conclusion.

### Proposition 8.3 — bounded-degree vertex transitivity gives a finite orbital chain

Now use transitivity in a more appropriate place. Let `G` be a vertex-transitive `d`-regular graph, let `Aut(G)` act on oriented edges, and let `J_t` be the orbit of the oriented edge traversed by NBRW at time `t`.

Then:

1. the number `m` of directed-edge orbits is at most `d`;
2. `(J_t)` is a Markov chain;
3. every transition probability has the form
   \[
   \frac{k}{d-1},\qquad k\in\{0,1,\dots,d-1\};
   \tag{8.5}
   \]
4. the initial orbital probabilities from a fixed vertex are integer multiples of `1/d`.

Indeed, vertex transitivity lets every oriented-edge orbit meet the `d` outgoing arcs from a fixed root, so `m<=d`. If two arcs lie in the same orbit, an automorphism maps one to the other and bijects their `d-1` nonbacktracking continuations while preserving orbit labels. Thus the continuation counts depend only on the current orbit, proving the Markov property and (8.5).

For fixed `d`, there are only finitely many possible pairs `(initial orbital law, orbital transition matrix)`. Standard finite-state decomposition, followed by taking extrema over this finite family, therefore supplies constants

\[
c_d>0,\qquad C_d<\infty,\qquad \rho_d<1,
\tag{8.6}
\]

such that, after a bounded burn-in depending only on `d`, the total mass of transient orbital types is at most `C_d\rho_d^t`, while every recurrent type that is allowed at the current periodic phase and is reachable from the initial law has probability at least `c_d`.

Combining this with Lemma 8.1 gives the following useful conclusion. If at an entropic time `j=Theta(log n)` the ordinary NBRW endpoint entropy obeys

\[
H(Y_j)\ge\log n-\Delta_n,
\tag{8.7}
\]

then:

- the total mass of transient directed-edge orbit types is `n^{-Omega_d(1)}`; and
- every persistent recurrent orbital sector satisfies
  \[
  H(Y_j\mid J_j=i)
  \ge
  \log n-C_d'(\Delta_n+1).
  \tag{8.8}
  \]

In particular, whenever a mechanism such as Altschuler's gives `Delta_n=O(log log n)`, all persistent orbital sectors automatically have the same near-maximal entropy scale.

### What obstruction was actually removed?

The earlier proposed need to **prove entropy synchronization among finitely many directed-edge orbit types** is not a real obstacle. Entropy disintegration plus bounded-degree transitivity already supplies it. Full arc transitivity was overused at that point.

This does **not** prove Salez Problem 2.3. The remaining hard step is earlier: under vertex transitivity plus spectral expansion alone, we still do not know how to prove the marginal near-maximal endpoint entropy (8.7), or an equivalent weighted collision/Green-function estimate. The two-copy/product obstruction shows that one cannot demand ambient-degree maximal tree growth even only to a near-entropic scale.

Thus the obstruction has been narrowed:

> **sector synchronization is solved; source-level endpoint entropy / collision control is the real remaining bottleneck.**

That is a genuine mechanism-level advance connected to the parent conjecture, separate from the new twisted-extension class theorem.

## 9. Essential executed sanity check

The executed checker is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T02-15-00Z__twisted-fiber-checker.py`

with archived output

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T02-15-00Z__twisted-fiber-checker.out`.

It uses the finite instance

- base `Cay(Z/7Z,{+-1,+-2})`, `d=4`;
- fiber `Cay(S_3,{(12),(23)})`, `s=2`;
- noncommuting twists including a 3-cycle.

The run verifies:

- exact projection identity, error `0`;
- cross/vertical noncommutation, max commutator entry `0.125`;
- base gap `0.799515566048790`;
- fiber gap `0.5`;
- output gap `0.501560893574976`, exceeding the theorem's lower bound `1/6`;
- the TV lower/upper sandwich at `t=0.5,1,2,4,8,16`;
- output/base branching ratio `(d-1)/(D-1)=3/5` and the predicted positive non-LRE exponent `beta=0.158696902757`.

The archived output terminates

`ALL_CHECKS_PASS`.

This finite computation is only a sanity check on exact identities and inequalities; it is **not** presented as evidence for the asymptotic theorem by itself.

## 10. Honest status, failed routes, and next attack

### Parent source status

**Before:** Salez Problem 2.3 OPEN/PARTIAL.

**After:** still **OPEN/PARTIAL**. The new theorem adds a twisted non-LRE vertex-transitive spectral-expander class with a quantitative continuous-time window. It does not cover arbitrary vertex-transitive spectral expanders.

### Mechanism-level progress

1. A noncommuting finite-group fiber transfer is proved by pathwise `L^2` contraction under arbitrary cross permutations.
2. The prior finite-orbit directional-entropy synchronization obstruction is removed by Lemma 8.1 and Proposition 8.3.

### Routes deliberately not repeated

- **P26 lexicographic exact-semigroup/fiber-reset transfer:** pruned as active partner duplication.
- **Derive maximal or pre-entropic tree-rate LRE from transitivity plus spectral gap:** pruned because the current two-copy expander construction is a direct obstruction.

### Remaining obligation

Prove a near-maximal NBRW endpoint entropy or equivalent collision/Green estimate directly from bounded-degree vertex transitivity plus spectral expansion, in a form that survives two-copy and local-product constructions.

### Next attack

Use the directed-edge orbital chain to formulate an **orbit-averaged collision kernel**. Because the number of orbital states is at most `d` and the transition matrices come from a finite `d`-dependent family, try to bound the cumulative collision excess after quotienting out the recurrent orbital state, rather than comparing ball growth to the ambient `(d-1)^r` tree rate. The target inequality should be stable under finite-group twisted extensions and the two-copy construction proved above to defeat raw LRE approaches.

## 11. Compact ledger delta

The structured ledger is saved beside this report as

`2026-09-20T02-15-00Z__ledger_delta.json`.

No historical or peer file, shared root ledger, POSTED item, workflow, permission, public surface, email/Drive object, paid-compute resource, or schedule was modified.
