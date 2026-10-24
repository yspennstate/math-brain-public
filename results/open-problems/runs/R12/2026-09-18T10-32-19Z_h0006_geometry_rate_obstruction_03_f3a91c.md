Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated applied-model/reasoning selector or completed-run effort telemetry, so I do not claim otherwise. **NO MOVEMENT: H0006 `FSS_layers = 2/3 -> 2/3`; methods actually used: #1 CHANGE THE CATEGORY, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS.**

# R12 HARD OUTSIDE — H0006 third run: the finite-graph layer needs a quantitative geometry rate, not merely graph size

Repository / branch: private `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Current exclusive claim: `operations/claims/H0006.md`.
Current source: Achyut Kumar (2026), arXiv:2608.15987v1, Section 12.3 open problem (4), **“Finite-size scaling on `G_n`.”**
Status after this run: **PARTIAL / OPEN**.

## 1. Continuity: do not reopen the stale Paley title

The native scheduler title still names Randomstrasse Conjecture 28 / I0102. That title is stale relative to R12's immutable research history. I0102 was terminally handed off earlier at the best R12 uniform certificate `(a,C,p0)=(1/2,1,5)`, with no further R12 recovery permitted. I0115 was subsequently terminally handed off as well. After the required successor-admission screen R12 lawfully claimed H0006.

The immediately preceding own report is

`runs/R12/2026-09-18T09-50-00Z_h0006_multitype_fss_02_e7c3a1.md`.

That report moved the frozen H0006 metric from `1/3` to `2/3` by proving the general finite-type Galton--Watson skeleton crossover. In the notation of that report, with

\[
\rho(M_\varepsilon)=1-\varepsilon,
\qquad
\xi=\varepsilon^{-1},
\]

and intrinsic Perron variance

\[
\beta=\pi Q(h,h)>0,
\]

it proved

\[
\log r_\varepsilon
=\frac{\varepsilon^2}{2\beta}+O(\varepsilon^3)
\]

and, when `sqrt(N) epsilon_N -> lambda`, the local total-progeny crossover

\[
N^{3/2}\Pr_i\{T_{\varepsilon_N}=\lfloor xN\rfloor\}
\to
\frac{h_i}{\sqrt{2\pi\beta}}
 x^{-3/2}e^{-\lambda^2x/(2\beta)}.
\]

Thus the branching-skeleton **total-progeny** cutoff is of order `xi^2`, and matching it to a hard size `N` gives `xi ~ sqrt(N)`.

This run does not re-prove either layer 1 or layer 2. It attacks only the remaining transfer to the actual cascade on finite `G_N`.

Before new work I reread the owner-required campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical H0006 claim, the two preceding H0006 reports, the H intake statement, and the newest same-source H0003 and H0005 reports recovered by exact path/search. H0003 is especially relevant because its newest report finds that the source's literal full-tree total-variation Conjecture 11.8 cannot hold in the supercritical finite-graph setting: a finite graph cluster has zero mass on infinite genealogies whereas the supercritical GW target has positive survival mass. H0005 concerns the different CRT-moment problem and does not duplicate H0006.

## 2. Source/current-literature check — 18 September 2026

The primary source was checked again at

`https://arxiv.org/html/2608.15987`

and its abstract record. It remains arXiv:2608.15987v1, submitted 17 August 2026. The exact H0006 source sentence is still:

> “Finite-size scaling on `G_n`. Quasi-stationary theory [6] for the cutoff `xi=(1-rho(M))^{-1}` against the finite size `n`; the window near criticality.”

The source assumptions at the start of the paper are finite connected graphs with uniformly bounded average degree, converging in the Benjamini--Schramm sense to a unimodular Galton--Watson tree. Hypothesis 2.4 introduces only a qualitative graph error `eta_n -> 0`; Proposition 11.2 identifies the short-cycle contribution through fixed-radius cycle density. Theorem 11.5 gives, in the bounded-degree dissipative subcritical regime,

\[
d_{\rm TV}(\mathcal L(\text{cluster}),\mathcal L(\mathrm{GW}(M)))
\le
C\frac{\varepsilon_{\rm sat}(\delta)}
{(1-\kappa\rho(M))^2(1-\rho(M))}
+\eta_n.
\tag{2.1}
\]

I write the saturation error as `epsilon_sat(delta)` below so that it is not confused with the near-critical spectral gap `epsilon=1-rho(M)`.

Fresh bounded searches for the exact source title/arXiv id, author, “Finite-size scaling on G_n”, “quasi-stationary”, and later author papers recovered no later source-matching solution. The Kumar--Duddala companion arXiv:2608.21125v1 (21 August 2026) treats front propagation/Bramson corrections and the continuous-type limit, not H0006. This is bounded negative evidence, not a worldwide novelty certificate.

The relevant older branching-process literature is important here rather than something to claim as new. Fahady--Quine--Vere-Jones, *Heavy traffic approximations for the Galton-Watson process* (Adv. Appl. Prob. 3, 1971), and Quine, *The multitype Galton-Watson process with rho near 1* (Adv. Appl. Prob. 4, 1972), already prove near-critical/quasi-stationary heavy-traffic limits: conditioned on nonextinction, the population is asymptotically gamma/exponential, and in the multitype case the limit is degenerate on the Perron ray. Those papers are the correct prior art for the source's phrase “quasi-stationary theory.”

No novelty is claimed for that branching-process mechanism.

## 3. Frozen metric

The claim-file metric is unchanged:

`FSS_layers` = number of the following nested source-valid layers for which a near-critical finite-size crossover is rigorously identified with an explicit scaling law:

1. exact one-type Bethe/GW subclass;
2. general finite-type GW skeleton;
3. actual finite-graph cascade on `G_N`, uniformly in the corresponding near-critical window.

Before this run: **2/3**.
After this run: **2/3**.

The reason layer 3 does not move is now sharper: the source assumptions supply no quantitative relation between graph size `N=|V(G_N)|` and the Benjamini--Schramm / short-cycle error, while the crossover probabilities to be transferred vanish polynomially in `N`. A qualitative `eta_N -> 0` is therefore insufficient.

This is the first unchanged H0006 run since the preceding metric movement. Stuck protocol does not yet fire.

---

# 4. Method #1 — CHANGE THE CATEGORY: separate quasi-stationary time from total-progeny size

The source writes `xi=(1-rho(M))^{-1}` and explicitly invokes quasi-stationary theory. The first two R12 H0006 runs studied total progeny and found a cutoff of order `xi^2`. These are not contradictory scales; they refer to different observables.

Let

\[
\varepsilon=1-\rho(M)>0,
\qquad
\xi=\varepsilon^{-1}.
\]

Keep the same primitive finite-type near-critical family and the same critical Perron normalization from the previous report:

\[
Mh=h,
\qquad
\pi M=\pi,
\qquad
\pi\mathbf1=1,
\qquad
\pi h=1,
\qquad
\beta=\pi Q(h,h)>0.
\]

The classical Quine heavy-traffic theorem, specialized to this normalization, gives the following near-critical picture. If

\[
k_\varepsilon=\left\lfloor t/\varepsilon\right\rfloor
=\lfloor t\xi\rfloor,
\qquad t>0,
\]

then for a process started at type `i`,

\[
\Pr_i\{Z_{k_\varepsilon}\neq0\}
\sim
\frac{2\varepsilon h_i}{\beta(e^t-1)}.
\tag{4.1}
\]

Conditioned on nonextinction at `k_epsilon`, the type vector collapses onto the left Perron composition:

\[
\varepsilon Z_{k_\varepsilon}
\ \Longrightarrow\
Y_t\,\pi,
\tag{4.2}
\]

where `Y_t` is exponential with mean

\[
\mathbb E Y_t=\frac{\beta}{2}(1-e^{-t}).
\tag{4.3}
\]

The constants in (4.1)--(4.3) can be read from the standard near-critical Feller branching approximation. The scalar Perron mass has branching mechanism

\[
\psi(q)=q+\frac{\beta}{2}q^2.
\]

Its Laplace exponent satisfies

\[
\partial_tu_t=-u_t-\frac\beta2u_t^2,
\qquad
u_0=\lambda,
\]

hence

\[
u_t(\lambda)
=\frac{\lambda e^{-t}}
{1+\frac\beta2\lambda(1-e^{-t})}.
\tag{4.4}
\]

Letting `lambda -> infinity` gives the extinction exponent

\[
v_t=\frac{2}{\beta(e^t-1)},
\]

which produces (4.1). Moreover

\[
1-\frac{u_t(\lambda)}{v_t}
=\frac{1}
{1+\frac\beta2\lambda(1-e^{-t})},
\]

the Laplace transform of the exponential variable in (4.3). Quine's multitype result supplies the Perron-ray collapse needed to pass from this scalar calculation to (4.2).

Again: this is **prior art specialized to the H0006 normalization**, not an R12 novelty claim.

The useful output is the scale separation:

\[
\boxed{\text{generation / QSD scale} \asymp \xi,}
\tag{4.5}
\]

whereas the preceding R12 theorem gives

\[
\boxed{\text{total-progeny exponential cutoff} \asymp 2\beta\xi^2.}
\tag{4.6}
\]

So H0006 has at least two finite-size questions. The phrase “cutoff `xi`” is natural for quasi-stationary lifetime/generation theory, but it must not be inserted as the exponential cutoff of total progeny. This reconciles the source's quasi-stationary language with the `xi^2` result already proved by R12.

**Outcome of #1:** success as a conceptual reparameterization. It does not move layer 3, but it identifies which observable lives on `xi` and which lives on `xi^2`.

---

# 5. Method #20 — FIND WHY THE ALGORITHM FAILS: exact transfer-rate requirements

The obvious finite-graph algorithm is:

1. prove the branching skeleton crossover;
2. couple the finite-graph cascade to that skeleton in total variation;
3. transfer the crossover.

Step 1 is now done. Step 3 looks automatic, but it is not, because the probabilities in the crossover vanish with `N`.

The following elementary lemma makes the missing rate exact.

## Lemma 5.1 — total-variation precision needed for a vanishing-probability crossover

Let `C_N` be an actual finite-graph cascade cluster and `T_N` the comparison branching cluster, and suppose

\[
D_N:=d_{\rm TV}(\mathcal L(C_N),\mathcal L(T_N)).
\]

Then for every event `A_N`,

\[
|\Pr(C_N\in A_N)-\Pr(T_N\in A_N)|\le D_N.
\tag{5.1}
\]

Consequently:

### (a) Local total-size law

If `m_N=floor(xN)` and the branching law has

\[
N^{3/2}\Pr\{|T_N|=m_N\}\to f(x),
\]

then the same local limit transfers by total variation whenever

\[
\boxed{N^{3/2}D_N\to0.}
\tag{5.2}
\]

### (b) Macroscopic total-size tail/window

If the branching law has a nondegenerate window or tail of order `N^{-1/2}`, for example

\[
\sqrt N\Pr\{xN\le |T_N|\le yN\}\to F(x,y),
\]

then the same limit transfers whenever

\[
\boxed{\sqrt N D_N\to0.}
\tag{5.3}
\]

### (c) Quasi-stationary generation law

Let `k_N=floor(t xi_N)` and let `D_N^{(k_N)}` be the total-variation distance between the actual and GW genealogies truncated at generation `k_N`. Since (4.1) says GW survival to that generation is of order `xi_N^{-1}`, transferring the scaled survival probability and the conditioned quasi-stationary law by a direct TV comparison requires

\[
\boxed{\xi_N D_N^{(k_N)}\to0.}
\tag{5.4}
\]

Indeed, for a conditioning event `A` with `Q(A)=p>0`,

\[
d_{\rm TV}(P(\cdot\mid A),Q(\cdot\mid A))
\le \frac{2d_{\rm TV}(P,Q)}{p-d_{\rm TV}(P,Q)}
\tag{5.5}
\]

whenever the denominator is positive, so `D=o(p)` is enough and is the natural precision scale for this direct route.

### Proof

Equation (5.1) is the variational definition of total variation. Multiply (5.1) by `N^{3/2}` or `sqrt(N)` for (a)--(b). For (c), use `A={nonempty generation k_N}` and the elementary conditional-probability decomposition

\[
|P(B\mid A)-Q(B\mid A)|
\le
\frac{|P(B\cap A)-Q(B\cap A)|}{P(A)}
+
Q(B\cap A)\left|\frac1{P(A)}-\frac1{Q(A)}\right|,
\]

then bound each unconditional difference by `D` and use `P(A)>=Q(A)-D`. This gives (5.5) up to an inessential factor convention. QED.

## 5.2 Insert the source's actual dissipative bound

In the subcritical near-critical regime, Theorem 11.5 of the source gives (2.1). For fixed `kappa<1` bounded away from one and `rho=1-epsilon`, the factor `(1-kappa rho)^{-2}` stays bounded, so

\[
D_N
=O\big(\varepsilon_{\rm sat}(\delta_N)\,\xi_N+\eta_N\big).
\tag{5.6}
\]

Therefore the direct quasi-stationary transfer (5.4) requires the quantitative conditions

\[
\boxed{
\varepsilon_{\rm sat}(\delta_N)\,\xi_N^2\to0,
\qquad
\xi_N\eta_N\to0.
}
\tag{5.7}
\]

At the **total-progeny finite-size scale** `xi_N ~ sqrt(N)`, the macroscopic tail criterion (5.3) is the same order:

\[
\boxed{
N\,\varepsilon_{\rm sat}(\delta_N)\to0,
\qquad
\sqrt N\,\eta_N\to0.
}
\tag{5.8}
\]

For the sharper point-mass local limit (5.2), (5.6) would require the much stronger

\[
\boxed{
N^2\varepsilon_{\rm sat}(\delta_N)\to0,
\qquad
N^{3/2}\eta_N\to0.
}
\tag{5.9}
\]

These conditions are not claimed necessary for every possible proof. They are the exact precision demanded by the **current total-variation transfer architecture**.

This explains why “`eta_N -> 0`” is not enough to finish H0006. Near criticality one is trying to resolve probabilities that themselves vanish like `N^{-1/2}` or `N^{-3/2}`; an absolute coupling error with no rate can swamp the signal.

There is a second topological issue from the newest H0003 neighboring report. On the supercritical side, a finite graph cluster is always finite while the infinite GW target has positive mass on infinite genealogies, so literal full-tree total variation cannot tend to zero. Thus a two-sided H0006 critical window must use a corrected object: finite-generation/projective laws, extinction-conditioned laws, or a genuinely finite-size branching approximation. The QSD formulation in (5.4) is naturally finite-generation and avoids that support mismatch.

**Outcome of #20:** decisive diagnosis. The remaining layer is not “prove another branching lemma”; it is obtain a quantitative mesoscopic graph/front error on the same scale as the vanishing crossover probabilities.

---

# 6. Method #15 — BREAK THE SYMMETRY: Benjamini--Schramm convergence has arbitrarily slow cycle rate

The source assumes only Benjamini--Schramm convergence of finite connected bounded-average-degree graphs to a tree. Proposition 11.2 uses the fact that for every **fixed** cycle length cutoff `L`, the rooted short-cycle density tends to zero. H0006, however, needs a rate strong enough to compete with `xi_N` or powers of `N`.

There is no such universal rate under Benjamini--Schramm convergence alone.

## Proposition 6.1 — arbitrary slow short-cycle decay at fixed local weak limit

Let `b(N)>0` be any deterministic function with `b(N)->0`. There exists a sequence of finite connected graphs `G_m` with uniformly bounded maximum degree (in fact `Delta(G_m)<=5`) such that

\[
G_m\xrightarrow{\rm BS}T_3,
\]

the infinite 3-regular tree, but if

\[
c_3(G):=\Pr\{\text{a uniform root of }G\text{ lies on a cycle of length }\le3\},
\]

then along the sequence

\[
\boxed{
\frac{c_3(G_m)}{b(|V(G_m)|)}\to\infty.
}
\tag{6.1}
\]

In particular no function of graph size alone can upper-bound the local short-cycle error at a prescribed vanishing rate uniformly over all source-admissible Benjamini--Schramm sequences.

### Proof

For each `m`, choose a connected 3-regular graph `H_m` with girth at least `2m+1`. Such cubic graphs exist with girth tending to infinity. Choose it sufficiently large that every integer `N >= |V(H_m)|` satisfies

\[
b(N)<m^{-2};
\tag{6.2}
\]

this is possible because `b(N)->0`.

Write `h_m=|V(H_m)|` and set

\[
B_m=\left\lfloor\frac{h_m}{4m}\right\rfloor.
\]

Take `B_m` disjoint copies of `K_4`, together with `H_m`, and make the union connected by adding a chain of bridge edges between the components. On each `K_4` use distinct attachment vertices for its two possible bridge edges. Adding these bridges raises selected degrees by at most two, so the resulting graph `G_m` has uniformly bounded degree; the crude bound `Delta<=5` is enough.

Its order is

\[
N_m=h_m+4B_m
=h_m(1+O(m^{-1})).
\tag{6.3}
\]

Every vertex inside a `K_4` lies on a triangle. For all sufficiently large `m`, `B_m>=h_m/(8m)`, while `N_m<=2h_m`. Hence

\[
c_3(G_m)
\ge \frac{4B_m}{N_m}
\ge \frac{1}{4m}.
\tag{6.4}
\]

Since `N_m>=h_m`, (6.2) gives `b(N_m)<m^{-2}`, and therefore

\[
\frac{c_3(G_m)}{b(N_m)}
>\frac{m}{4}\to\infty,
\]

proving (6.1).

It remains to verify the Benjamini--Schramm limit. Fix a radius `R`. For `m>R`, any vertex of `H_m` whose `R`-ball avoids the bridge attachment points has an `R`-ball isomorphic to the radius-`R` ball of `T_3`, because the girth of `H_m` exceeds `2R+1`. The number of `H_m` vertices within graph distance `R` of all bridge attachment points is at most

\[
C_R B_m
\]

for a constant `C_R` depending only on `R` and the degree bound, hence its fraction is `O_R(1/m)`. The total fraction of vertices inside the `K_4` gadgets is also `O(1/m)`. Thus the probability that a uniform root fails to have the `T_3` radius-`R` neighbourhood tends to zero. Since `R` was arbitrary,

\[
G_m\xrightarrow{\rm BS}T_3.
\]

QED.

### What this proves and what it does not

This proposition is a graph-geometry statement. It does **not** assert that the actual cascade total-variation error `eta_N` is always bounded below by `c_3(G_N)` for every SDE parameter choice. What it proves is exactly what is needed to invalidate the simplest H0006 transfer strategy: the short-cycle quantity explicitly used in source Proposition 11.2 has no universal `N`-rate under the source's local-weak assumptions. Hence neither `eta_N=o(N^{-1/2})` nor any other prescribed polynomial rate follows from Benjamini--Schramm convergence alone.

The construction can make the defect density tend to zero as slowly as desired while preserving the same local weak tree limit.

**Outcome of #15:** success. Breaking homogeneity shows that graph size is not by itself a sufficient finite-size parameter over the full source class.

---

# 7. Synthesis: the source-level finite-size parameter must include mesoscopic geometry

The three routes fit together cleanly.

1. Classical quasi-stationary branching theory lives on the generation scale `xi`.
2. Total-progeny rare-event theory lives on the size scale `xi^2`.
3. Transfer from the branching skeleton to a finite graph requires coupling errors small **relative to the observable's own vanishing probability**.
4. Benjamini--Schramm convergence gives no universal rate for even the fixed-radius cycle term used by the source.

Therefore there cannot be a source-uniform finite-size law expressed only as a relation between `xi` and `N=|V(G_N)|` under the paper's current graph assumptions. An honest layer-3 theorem has to add or retain a quantitative geometry/front parameter.

One natural source-compatible profile is

\[
\chi_N(R)
:=\Pr\{B_R(U_N;G_N)\text{ contains a cycle}\},
\tag{7.1}
\]

where `U_N` is a uniform root. A stronger front-adapted quantity would measure the probability that the **explored cascade neighbourhood** develops a collision by the relevant generation/volume scale. The source's `eta_N` is already an abstract placeholder for such an error, but H0006 needs its dependence on the crossover scale.

A realistic theorem would therefore have a hypothesis of the form

\[
\xi_N\eta_N(\xi_N)\to0
\tag{7.2}
\]

for quasi-stationary generation limits, or

\[
\sqrt N\eta_N\to0
\tag{7.3}
\]

for the macroscopic `xi_N~sqrt(N)` total-progeny tail, together with the corresponding saturation-error condition from (5.7)--(5.9).

The hard remaining mathematical task is to replace the abstract `eta_N` by a graph quantity that can be estimated in interesting families. On arbitrary BS sequences that quantity cannot be a function of `N` alone; on random regular/configuration-model graphs it plausibly can be controlled by explicit exploration-collision estimates.

This is why layer 3 remains open rather than being declared solved by the branching theorem.

## 8. A concrete next route that can actually move layer 3

The next run should stop trying to prove a universal theorem for all Benjamini--Schramm sequences and instead prove a complete source-valid subclass theorem on a graph ensemble with quantitative local geometry, while keeping the source dynamics and crossover observable unchanged.

The most promising target is a bounded-degree random regular/configuration-model sequence, where a breadth-first exploration exposing `s` half-edges has collision probability of order `s^2/N`. The branching results already identify which `s` matters. The next task is to combine:

- the exact near-critical GW law from the first two H0006 reports;
- an exploration coupling up to a scale chosen from `xi_N`;
- source front-decoupling/saturation errors;
- collision probability of the configuration-model pairing process.

That could yield a first actual finite-`G_N` finite-size theorem and would be genuine movement toward layer 3, while the arbitrary-slow construction above explains why one should not expect the same statement for every BS sequence.

Reserved untried Section-B methods for the next H0006 run:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — close the random-regular/configuration-model finite-graph subclass;
- **#9 RANDOMIZE** — use the pairing process to obtain an explicit collision-rate coupling;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL** — prove the finite-size scaling for typical finite graphs before returning to deterministic geometry conditions.

These have not been used in the three H0006 runs so far.

## 9. Exact status / no closure inflation

`FSS_layers` remains

\[
\boxed{2/3\to2/3.}
\]

H0006 remains **OPEN / PARTIAL**.

This run did not solve the actual finite-graph layer. It did prove a source-relevant obstruction to an `N`-only theorem under bare Benjamini--Schramm convergence, and it derived the exact TV precision needed by the current transfer method.

No finite exhaustive claim was made, so no exact-arithmetic checker was manufactured. The new claims are symbolic graph/probability statements with proofs on the page.

## 10. Prior-art / novelty discipline

Queries and sources checked this run included:

- exact arXiv id/title `2608.15987`, exact H0006 phrase “Finite-size scaling on G_n”, `quasi-stationary`, `near critical`, and author `Achyut Kumar`;
- later author paper arXiv:2608.21125;
- M. P. Quine, *The multitype Galton-Watson process with rho near 1*, Adv. Appl. Prob. 4 (1972), 429--452;
- K. S. Fahady, M. P. Quine, D. Vere-Jones, *Heavy traffic approximations for the Galton-Watson process*, Adv. Appl. Prob. 3 (1971), 282--300;
- repository same-source H0003/H0005 work, especially the H0003 support obstruction to literal supercritical full-tree TV.

The near-critical QSD/exponential Perron-ray mechanism is classical and is labelled as such. The arbitrary-slow-BS construction is elementary graph folklore in spirit; no publication-novelty claim is made for the fact that local weak convergence has no universal rate. The source-specific use of that obstruction to delimit H0006 is the new research conclusion of this run. A bounded search finding no H0006 resolution is not a novelty certificate.

## 11. Runtime / task-control honesty

The scheduler/task-management surface exposed to this environment still has no binding model-family selector and no reasoning-effort selector, and no authenticated completed-run telemetry proving GPT-6 maximum. The prompt string requests GPT-6/maximum; that request is not runtime attestation.

The installed repository policy records historical task-modification denials such as `You cannot modify this task` for P26 in one context and a later successful update from an authorized context. A present denial must be handled through the owning account/workspace context, ownership transfer, or platform support. It is not permission to duplicate a task or bypass access controls. No scheduler state or permission was changed in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R12
  category: HARD_OUTSIDE
  target: H0006
  canonical_source: arxiv_2608_15987::section_12.3_open_problem_4_finite_size_scaling
  status_before: PARTIAL_OPEN
  status_after: PARTIAL_OPEN
  metric: FSS_layers
  value_before: "2/3"
  value_after: "2/3"
  movement: NO_MOVEMENT
  consecutive_unchanged_since_last_metric_move: 1
  methods_used: [1, 15, 20]
  new_results:
    - "Separated classical quasi-stationary generation scale xi from total-progeny cutoff scale xi^2."
    - "Proved exact TV precision requirements for transferring local, tail, and QSD crossovers to finite graphs."
    - "Proved BS convergence to T3 can have arbitrarily slow fixed-radius short-cycle decay, even for connected uniformly bounded-degree graphs."
  source_resolution_check: "No later source-matching H0006 resolution recovered in bounded 2026-09-18 search."
  closure: false
  checker_created: false
  remaining_obligation: "Quantitative finite-graph exploration/front coupling on a source-valid family; bare BS convergence has no N-only rate."
  next_methods: [4, 9, 28]
```
