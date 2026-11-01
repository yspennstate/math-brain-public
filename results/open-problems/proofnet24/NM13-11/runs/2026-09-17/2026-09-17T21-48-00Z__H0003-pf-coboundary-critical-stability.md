Model: GPT-5.6 Sol. Reasoning: UNVERIFIED. **NO MOVEMENT in the frozen `A_echo` metric (`Lambda_* -> Lambda_*` on the previously proved uniform-spectral subclass); methods actually tried this run: #12 FIND WHAT IS CONSERVED, #13 FIND WHAT ONLY INCREASES/DECREASES, #21 ASK WHO ELSE HAS THIS SHAPE.** A new proved branching-process lemma identifies an exact Perron-coboundary cancellation that converts the naive critical `O(sqrt(epsilon))` truncation loss into `O(epsilon)` for a source-relevant class of finite-type offspring-law perturbations, but I do not yet derive that score structure from the interacting SDE, so the source conjecture remains OPEN/PARTIAL.

# NM13-11 second run — H0003 critical-front cancellation via Perron coboundaries

Date: 2026-09-17 UTC  
Track: NM13-11 / HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, `master`  
Canonical source/claim: H0003 / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, residue 10 mod 13.

## 1. Runtime honesty and control-plane status

The actual model identity available to this run is **GPT-5.6 Sol**. The reasoning-effort setting is not authenticated by a model/reasoning selector or runtime telemetry and is therefore **UNVERIFIED**. This is not GPT-6/maximum and I do not claim otherwise.

The current exposed automation controls still do **not** contain a model selector or a reasoning-effort selector. They expose task text/title, timing, enablement and scheduling controls, so the requested `GPT-6 / maximum` line can only be prompt text in this interface. To make that setting binding, the platform would have to expose an actual model/reasoning control for the task (or the task would have to be edited from an authorized interface that owns such controls); prompt text alone cannot certify it.

The repository's current policy preserves an older native modification failure (`You cannot modify this task`) for P26/P01/P03 in one scheduler context, while current `RESULTS.md` also records that a later P26 prompt update succeeded in a different authorized context. I therefore do **not** describe the historical P26 denial as a permanent global state. The lawful workaround for a task that refuses modification is to use the owning account/workspace/task context or platform support; do not bypass the permission boundary and do not create a duplicate schedule. This research run changes no schedule and sends no support request.

## 2. Continuity recovered before new mathematics

I reread/recovered the current controlling surfaces and H0003-specific continuity before continuing:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the NM13 deployment manifest `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the H-intake row in `probability_1000_intake_H_20260914/problems.jsonl`;
- the live exclusive claim `operations/claims/H0003.md`;
- my previous immutable report `proofnet24/NM13-11/runs/2026-09-17/2026-09-17T20-49-43Z__H0003-spectral-echo-first-attack.md`;
- the newest neighboring NM13-10 admission report and NM13-12 P0483 report;
- the newest visible P14/G0007 contact-process state, solely to preserve the explicit exclusion and neighboring interacting-particle continuity.

A fresh repository search for `H0003`, `arxiv_2608_15987`, the exact theorem name from the prior run, and the source title recovered the live NM13-11 claim, intake/source verification, screening history, and my prior report, but no new owner, release, handoff, retirement, or outside audit. The current claim remains exclusively NM13-11-owned. No `H0003-A*` campaign attempt record beyond the already recovered intake/screening history was found. GitHub code search is a bounded default-branch search, so this is not represented as an omniscient history census.

The large root ledgers are read through scoped connector responses; I do not claim a byte-for-byte reread of every historical blob. Relevant H0003 continuity is accessible and no missing source-specific predecessor report was discovered.

## 3. Source and fresh current-literature check

Exact source: Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, submitted 17 August 2026:

`https://arxiv.org/abs/2608.15987`

Conjecture 11.8 asks for the Front-Markov / multitype-Galton-Watson reduction throughout the full saturated regime, including strong coupling `kappa >= 1`, uniformly through the critical window, with source-scale total-variation error `C(epsilon(delta)+eta_n)`.

Dated bounded search: 2026-09-17. Queries included the exact arXiv id/title, `Front-Markov`, `Conjecture 11.8`, `strong coupling`, the author name, and later author work. The source is still arXiv v1. The search again recovered the companion Kumar--Duddala preprint, arXiv:2608.21125 (21 August 2026), which treats front propagation/Bramson correction and the continuous-type regime, not a proof of Conjecture 11.8:

`https://arxiv.org/abs/2608.21125`

No source-matching later resolution was recovered. This remains bounded negative evidence, not proof of worldwide openness or novelty.

For the branching-process mechanism used below I also searched `multitype Galton-Watson exponential tilt Perron eigenvector`, `Doob h-transform`, and `critical exponential tilting conditioned multitype trees`. The closest directly relevant prior art found is Paul Thevenin's work on critical exponential tiltings of multitype BGW trees, arXiv:2310.12897, and the 2025 follow-up arXiv:2503.11501. Those papers use exponential tilting to preserve conditioned multitype-tree laws/local limits. The telescoping mechanism below is therefore treated as **branching-process exponential-tilt/Perron folklore or a close relative of known machinery**, not claimed as a new general branching-process discovery. I did not find the exact unconditioned `O(|theta|)` total-variation modulus below in this bounded search. Its value here is the source-specific route it exposes.

## 4. Frozen metric — no movement this run

The metric remains exactly the one frozen at admission:

`A_echo` = the graph-amplification coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is carried through to a source-relevant front-decoupling theorem.

Previous run's proved PARTIAL value on the uniform-spectral, bounded-degree, strictly subcritical subclass:

`A_echo = Lambda_* := sup_n ||A(G_n)||_{2->2}`.

This run does **not** prove a smaller coefficient or enlarge that spectral subclass while retaining the same metric. Therefore

`before = Lambda_*`, `after = Lambda_*`, **no movement**.

The new theorem below attacks a different remaining obligation -- critical-window accumulation -- without renaming the metric. The full H0003 source remains OPEN.

---

# 5. Method #12 — FIND WHAT IS CONSERVED

The source itself says that the critical obstruction is that a cellwise `O(epsilon)` error can be multiplied by cluster volume, while the desired bound remains only `O(epsilon)`. The first run attacked spatial echo amplification. This run instead asks what exact balance in a critical branching genealogy can annihilate the first-order bulk term.

The answer is the right Perron mass.

Let the finite type set be `D={1,...,m}`. For a parent of type `i`, let `K=(K_1,...,K_m)` be its offspring-count vector with law `Q_i`. Write

`M_ij = E_i[K_j]`.

Assume `M` is irreducible and critical, `rho(M)=1`, and choose a positive right Perron vector `h`:

`M h = h`.

For one reproduction event define the Perron-flow increment

`Z_i(K) := <h,K> - h_i`.

Then

`E_i Z_i(K) = (Mh)_i-h_i = 0`.

So the total active Perron mass in a breadth-first exploration is conserved **in conditional expectation**. More importantly, over a *completed finite tree* the same quantity telescopes exactly:

`sum_{v in T} [sum_{u child of v} h_{type(u)} - h_{type(v)}] = -h_{type(root)}`.

Every nonroot vertex appears once with `+h` as a child and once with `-h` as a parent; only the root remains. This is the exact critical conservation law missing from a raw per-cell union bound.

That identity leads to the following complete lemma.

## Theorem NM13-11-H0003-PF-COBOUNDARY-TV-02

Let `P_0^r` be a finite-type Galton--Watson tree started from root type `r`. Assume:

1. the mean matrix `M` is irreducible and critical, `rho(M)=1`;
2. offspring counts are uniformly bounded by some `B<infinity`;
3. extinction is almost sure under `P_0^r`;
4. for some `C_tail`, the critical total progeny `N=|T|` obeys

`P_0^r(N=n) <= C_tail n^(-3/2)`

for every `n>=1` (zeros on forbidden lattice classes are allowed).

Let `h>0` satisfy `Mh=h`, and define

`Z_i(k)=<h,k>-h_i`.

For real `theta` near zero, let

`psi_i(theta) = log E_{Q_i}[ exp(theta Z_i(K)) ]`

and define a tilted offspring law

`Q_i^theta(k) = Q_i(k) exp(theta Z_i(k)-psi_i(theta)).`

Let `P_theta^r` be the resulting multitype Galton--Watson tree law on the space of finite **and infinite** rooted typed trees. Then there are constants `theta_0>0` and `C<infinity`, depending only on the base offspring laws and `h`, such that

`d_TV(P_theta^r, P_0^r) <= C |theta|`

for `|theta|<=theta_0`.

If `Z_r(K)` is not almost surely zero under the root offspring law, then there is also `c>0` such that

`d_TV(P_theta^r, P_0^r) >= c |theta|`

for all sufficiently small nonzero `theta`. Hence the linear modulus is sharp in that nondegenerate case.

### Proof

Because `Mh=h`, each `Z_i` is centered. Bounded offspring and finite type imply a uniform bound `|Z_i|<=R`. Therefore, for small `theta`,

`0 <= psi_i(theta) <= C_psi theta^2`.                                      (5.1)

The lower bound is Jensen's inequality applied to a centered random variable; the upper bound follows, for example, from Taylor's theorem for the finite exponential moment on `[-R,R]`.

Fix a finite typed tree `tau` with root type `r`. The Radon--Nikodym ratio is the product of the offspring-law ratios over its vertices:

`L_theta(tau)
 = product_{v in tau} exp(theta Z_{type(v)}(K_v)-psi_{type(v)}(theta)).`

Taking logs and using the exact tree telescoping identity,

`log L_theta(tau)
 = -theta h_r - sum_{v in tau} psi_{type(v)}(theta).`                    (5.2)

Thus, writing `N=|tau|` and `H=max_i h_i`,

`log L_theta(tau) <= |theta| H`,

and by (5.1),

`|log L_theta(tau)| <= |theta|H + C_psi theta^2 N`.                     (5.3)

For a real number `u<=a`,

`|e^u-1| <= e^a min(1,|u|)`.

Apply this with `u=log L_theta`, `a=theta_0 H`, and choose `theta_0` small enough that `|theta|H<=1/2`. From (5.3), after changing constants,

`|L_theta(tau)-1|
 <= C_1 [ |theta| + min(1,C_2 theta^2 N) ].`                            (5.4)

Take expectation under `P_0^r`. The critical tail assumption gives

`E_0[min(1,C_2 theta^2 N)]
 <= C_2 theta^2 sum_{n<=c theta^(-2)} n P_0(N=n)
    + sum_{n>c theta^(-2)} P_0(N=n)`.

Using `P_0(N=n)<=C_tail n^(-3/2)`, the first term is bounded by a constant times

`theta^2 sum_{n<=c theta^(-2)} n^(-1/2) = O(|theta|)`,

while the second is

`sum_{n>c theta^(-2)} O(n^(-3/2)) = O(|theta|)`.                        (5.5)

Hence

`E_0 |L_theta(T)-1| <= C_3 |theta|`.                                    (5.6)

The tilted process may be supercritical, so we must also account for an infinite-tree atom. Summing (5.2) over all finite trees shows

`E_0 L_theta(T) = P_theta(T is finite)`.

Therefore

`P_theta(T is infinite) = 1-E_0 L_theta(T)
 <= E_0 |1-L_theta(T)|`.                                                (5.7)

On the extended finite/infinite tree space,

`2 d_TV(P_theta,P_0)
 = E_0|L_theta-1| + P_theta(T is infinite)`

because the critical base process is finite almost surely. Equations (5.6)-(5.7) prove the upper bound.

For sharpness, project the full tree law to the root offspring vector. Since `psi_r'(0)=0`,

`Q_r^theta(k)=Q_r(k)[1+theta Z_r(k)+O(theta^2)]`

uniformly over the finite support. Hence

`d_TV(Q_r^theta,Q_r)
 = (|theta|/2) E_r|Z_r(K)| + O(theta^2)`.

If `Z_r` is not almost surely zero, this is at least `c|theta|` for small `theta`. Data processing gives the same lower bound for the full tree law. ∎

### Single-type sanity check

For the rooted `b`-ary Bernoulli percolation/GW model, `Q_p=Bin(b,p)` and the critical point is `p_0=1/b`. Here `h=1`, so the Perron increment is exactly `K-1`. Changing `p` is an exponential tilt by this affine score. For any finite tree with `n` vertices there are exactly `n-1` open child edges and `(b-1)n+1` closed child slots, so

`P_p(tau)/P_{p_0}(tau)
 = (p/p_0)^(n-1) ((1-p)/(1-p_0))^((b-1)n+1),`

which depends on `n`, not on the tree shape. The theorem therefore yields

`d_TV(P_p,P_{p_0}) = O_b(|p-p_0|)`.

The event that the root has no children gives the matching linear lower bound. This exact edge-count identity is the single-type shadow of the Perron-flow telescoping above.

**Outcome of method #12:** a genuine conserved quantity was found and turned into a complete critical perturbation theorem. It does not yet establish that the H0003 SDE's echo error lies in this Perron-coboundary family.

---

# 6. Method #13 — FIND WHAT ONLY INCREASES / DECREASES

The same tilt has a useful exploration monovariant that makes the source's phrase "the error is generated on the active front, not the failed bulk" mathematically exact in this model class.

Explore the tree one discovered vertex at a time, always after its parent. After `k` vertices have been explored, let `F_k` be the discovered but unexplored frontier and define its Perron mass

`H_k = sum_{u in F_k} h_{type(u)}`.

Under the critical base law,

`E[H_{k+1}-H_k | history] = 0`,

because exploring a type-`i` vertex replaces mass `h_i` by offspring mass `<h,K>` and `E_i<h,K>=h_i`. Thus `(H_k)` is a nonnegative martingale until extinction.

Let `L_k` be the likelihood ratio of the first `k` revealed offspring configurations under `Q^theta` versus `Q`. The same telescoping, stopped before extinction, gives the exact identity

`L_k = exp( theta(H_k-h_r) - sum_{ell=1}^k psi_{type(v_ell)}(theta) ).`   (6.1)

Therefore the **front-compensated likelihood**

`C_k := exp(-theta H_k) L_k
     = exp(-theta h_r - sum_{ell=1}^k psi_{type(v_ell)}(theta))`         (6.2)

is pathwise nonincreasing in `k`, because every `psi_i(theta)>=0`.

This isolates the only first-order term in the partial likelihood to the current active-front mass `H_k`. Everything contributed by already explored bulk vertices enters through the nonnegative compensator `psi_i(theta)=O(theta^2)`.

At extinction `H_N=0`, so the first-order front term disappears completely except for the root boundary term `-theta h_r`, recovering (5.2).

This is stronger than a verbal "front not volume" heuristic: in the PF-coboundary perturbation class, the explored bulk is exactly second order after the frontier is compensated.

### Why this matters for the source's critical window

If one only knows a per-cell coupling error `O(epsilon)` and union-bounds over a critical tree of size `n`, one gets a conditional error of order `min(1,C epsilon n)`. Combining this with the critical `n^(-3/2)` progeny law gives at best, by cutoff at `n~epsilon^(-1)`,

`sum_n P(N=n) min(1,C epsilon n) = O(sqrt(epsilon)).`                   (6.3)

So a plain cellwise union bound cannot certify the conjectured `O(epsilon)` critical rate.

By contrast, the PF-coboundary identity changes the finite-tree likelihood error from first-order bulk `epsilon n` to

`O(epsilon) + O(epsilon^2 n)`.

With the same critical tail,

`sum_n P(N=n) min(1,C epsilon + C epsilon^2 n) = O(epsilon)`,            (6.4)

which is exactly the source scale.

Equation (6.4) is the quantitative mechanism sought in the source's remark that critical uniformity should depend on front width rather than failed volume: here it is sharper still, because the first-order bulk term telescopes into the current Perron frontier.

**Outcome of method #13:** a pathwise monovariant and an exact front/bulk decomposition were proved for the tilted GW model. The missing step is an SDE-to-offspring-score derivation; without it this is not a proof of H0003.

---

# 7. Method #21 — ASK WHO ELSE HAS THIS SHAPE

The nearest mathematical shapes are:

1. the source's own Perron/many-to-one machinery and critical `n^(-3/2)` total-progeny law;
2. its Remark 11.6 front-energy supermartingale, which already says the active frontier rather than failed volume is the correct object;
3. the Kumar--Duddala companion's branching-random-walk/derivative-martingale viewpoint for front propagation;
4. critical exponential tilting of multitype BGW trees in Thevenin's 2023/2025 work.

The useful synthesis is not to build another global state norm. It is to compare **cell laws by their score** and ask whether the first-order score is a Perron coboundary.

A source-matching next lemma would have the following form. Let `Q_i` be the ideal directed cell offspring law at criticality and `Q_i^true(. | history)` the true conditional cell law on a tree-like neighborhood. Prove a uniform likelihood expansion

`log( d Q_i^true / d Q_i )(k | history)
 = theta_delta [ <h,k>-h_i ] + R_i(k,history)`                           (7.1)

with

`|theta_delta| <= C epsilon(delta)`,

`|R_i| <= C epsilon(delta)^2`,                                          (7.2)

or a more general history-dependent decomposition whose first-order part still telescopes as a front potential.

If (7.1)-(7.2) can be derived, Theorem PF-COBOUNDARY-TV-02 plus the source's tree-likeness error `eta_n` would remove the critical `n epsilon` accumulation for the bounded-degree finite-type case and give the desired `O(epsilon+eta_n)` scale at the branching-law level.

This is **not** asserted to hold. The source's Proposition 11.2 supplies `O(epsilon)` cellwise correctness and sibling-covariance control, but a total-variation bound does not identify the Radon--Nikodym score. Equation (7.1) is a materially stronger structural statement. The theorem above says exactly why such structure is worth looking for.

There is also a diagnostic obstruction: if the first-order score has a component orthogonal to the finite-tree flow constraints, that component generally need not telescope. In a generic conditioned critical GW perturbation one expects order-`sqrt(n)` score fluctuations, which would produce a logarithmic or worse accumulation rather than the clean linear modulus. I have **not** promoted that expectation to a theorem here; it is a warning that the source's `O(epsilon)` rate needs special structure, not merely small local TV error.

**Outcome of method #21:** the source's front-energy idea, multitype Perron theory, and known exponential-tilting machinery combine into a precise new proof target: establish a Perron-coboundary first-order score for the SDE cell law. The bounded literature search found related tilt machinery but no paper solving this source-specific bridge.

---

# 8. What moved and what did not

Frozen metric:

`A_echo: Lambda_* -> Lambda_*` **NO MOVEMENT**.

So the unchanged-run counter increases from 0 to **1**. This is not yet a stuck episode; the owner's stuck protocol begins after three unchanged runs or three repetitions of the same remaining obligation. Recovery count remains **0**.

What did move mathematically, without changing the metric:

- proved `NM13-11-H0003-PF-COBOUNDARY-TV-02`, a source-relevant critical GW stability lemma with sharp `O(|theta|)` TV modulus;
- proved the stopped exploration identity (6.1) and pathwise decreasing compensated likelihood (6.2);
- identified a precise SDE bridge, the score decomposition (7.1)-(7.2), that would replace the naive `O(n epsilon)` critical accumulation by `O(epsilon)`;
- proved that the naive critical union-bound architecture gives only `O(sqrt(epsilon))` from the source's `n^(-3/2)` tail, so it cannot by itself reach Conjecture 11.8's stated rate.

These are PARTIAL route results. They do not improve the strong-coupling graph-amplification threshold and do not prove the full Front-Markov conjecture.

## 9. Exact remaining obligations

1. **Cell-score derivation.** Starting from the saturated single-cell SDE and first-passage law, differentiate the conditional offspring law with respect to the echo perturbation and determine whether its first-order score is the Perron coboundary `<h,k>-h_i`, another exact tree coboundary, or has a non-telescoping component.
2. **History dependence.** If the score coefficient varies with the front history, identify a predictable potential whose summation-by-parts leaves only an active-front term; a common scalar `theta_delta` cannot simply be assumed.
3. **Strong coupling.** The original `A_echo` obligation remains: replace the global Lipschitz/spectral mode by a source-valid front-localized stability estimate that survives `kappa>=1`. The new likelihood route only addresses critical accumulation after local cell control is available.
4. **Cycle transfer.** Reinsert finite-graph tree-likeness `eta_n` only after the tree-level score estimate is proved; do not infer an infinite-volume theorem from a finite computation.
5. **Unbounded degrees.** Still untouched.
6. **Audits.** No P26 or NM13-12 audit is claimed. This theorem is an internal PARTIAL route result, not a closure package.

## 10. Next Section-B methods

Do not repeat `12,13,21` next run. If H0003 remains active, the next genuinely different triple is:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce an explicit saturation/echo interpolation parameter in the one-cell first-passage law and compute the first score at zero;
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite that score as a finite-type likelihood/coboundary problem rather than an SDE norm estimate;
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** first settle a single parent type, one generation, and one echo direction exactly before trying to glue the front.

No checker artifact is created this run. The new claims are theorem-sized analytic identities with complete proofs on this page; there is no finite enumeration or arithmetic certificate whose checking would warrant spending the run on code.

---

```yaml
ledger_delta:
  track: NM13-11
  source_id: H0003
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  claim_path: operations/claims/H0003.md
  category: HARD_OUTSIDE
  exact_source_status: OPEN
  mathematical_status: PARTIAL
  metric:
    name: A_echo
    before: Lambda_star_on_uniform_spectral_subclass
    after: Lambda_star_on_uniform_spectral_subclass
    movement: false
    meaning: sufficient graph-amplification coefficient in gamma_max*L_sigma*A_echo < alpha_min carried through to front decoupling
  new_internal_theorem:
    id: NM13-11-H0003-PF-COBOUNDARY-TV-02
    statement: critical finite-type GW Perron-coboundary exponential tilts have full-tree total-variation distance O(abs(theta)), sharp when the root score is nondegenerate
    source_level_scope: PARTIAL_ROUTE_LEMMA_NOT_H0003_CLOSURE
  methods_tried: [12, 13, 21]
  method_outcomes:
    12: exact Perron-flow conservation/telescoping found and proved
    13: front-compensated likelihood is pathwise nonincreasing; first-order term lives on active frontier
    21: linked source front energy to multitype exponential-tilting machinery; isolated cell-score bridge
  unchanged_runs: 1
  stuck_recoveries: 0
  audits:
    p26: MISSING
    nm13_12: MISSING
  closure: false
  next_obligation: derive the first-order Radon-Nikodym score of the true saturated one-cell law and test whether it is a Perron/tree coboundary uniformly in front history
  next_methods: [5, 18, 30]
  shared_root_edit_requested: false
  artifacts_created: []
```

**End of complete run report.**