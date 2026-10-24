Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **NO MOVEMENT in the frozen metric: `R_unique=+infinity -> +infinity`; unchanged count 6; Section-B moves tried: #4 PROVE SOMETHING WEAKER COMPLETELY, #16 COMPUTE EVERY SMALL CASE, #27 SWAP THE QUANTIFIERS.**

Problem/source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, PLMS 132(5) (2026), e70158, arXiv:2502.11622v2, **Question 2**; intake **I0079**.

# R06 CLOSABLE OUTSIDE — run 7 on I0079: pointwise tie-breaking is already nonunique on a regular tree; six-run rotation handoff

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No Gmail/email, Drive, public posting, purchases, permission changes, workflow execution, force-push, or scheduler changes.

## 1. Continuity and why the stale I0056 prompt is not restarted

The native prompt still names I0056 / Lyons–Peres Question 6.20, but R06 already reached its six-unchanged-run rotation threshold there, preserved its `H_{5,5}` width-zero result and full-source `PARTIAL / audit-gated` handoff, and then create-only claimed I0079. The current canonical ownership file `operations/claims/I0079.md` remains the active R06 continuity record. I therefore do **not** restart I0056 or erase its history.

Before research I reread/rechecked current `master` surfaces available through the connector: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the I0079 claim, the newest own R06 report, the current I0079/P26-audit searches, the intake row, and the newest neighboring R07 package. The large intake JSONL corpus is connector-truncated if rendered wholesale; exact-ID/source retrieval was used for the target and successor screens rather than falsely claiming a byte-for-byte visual reread of roughly 780 rows.

The frozen I0079 metric remains

`R_unique = largest radius on which all subsequential limits agree for the frozen global-iid-nucleus-label refinement on Gamma=F_2 x F_2`.

That global-label scope is now a **KNOWN** consequence of published phase-independence machinery and already has

\[
R_{\rm unique}=+\infty.
\]

The preceding report recorded unchanged count 5, so this run reaches **unchanged count 6**. Under the owner rule, I0079 must rotate after this run even though the source-relevant refinement theorem below is new.

The accepted source still poses the open-ended question

> “In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?”

and explicitly notes that tied boundary points can be refined equivariantly, for example by having each tied point pick one of its nearest nuclei at random. Thus the pointwise-independent refinement below is source-admissible; it is not a change of model outside the source conventions.

## 2. The blocker carried into this run

The previous stuck report reduced the next useful source question to the simplest possible case:

\[
\boxed{
\text{On the 4-regular tree }T_4,\text{ does pointwise-independent tie-breaking have a unique low-intensity BVT limit?}
}
\]

The previous exploratory calculation suggested that the one-edge cylinder should have exactly the same phase series already certified for the product `T_4 x T_4`, but it deliberately stopped short of a theorem because the Bernoulli-to-boundary handoff on one tree had not been reconstructed.

This run removes that handoff entirely: the phase formula can be proved **directly from finite Bernoulli shells**.

## 3. Freeze the pointwise-independent refinement

Let `T_4` have root `o`, and fix a neighbor `w` of `o`. For every Bernoulli nucleus configuration and every ordered pair `(v,x)` consisting of an evaluation vertex `v` and a nucleus `x`, attach an iid continuous mark `U_{v,x}`. Vertex `v` chooses, among its nearest nuclei, the one with smallest `U_{v,x}`.

Because the marks are iid under the diagonal automorphism/group action, this is a measurable equivariant refinement. Conditional on a finite nearest-nucleus set, the chosen nucleus is uniform; choices at two different evaluation vertices are independent conditional on their two tied candidate sets.

Let

\[
E=\{o\text{ and }w\text{ are assigned to the same nucleus}\}.
\]

This is a radius-one cylinder event of the induced equivalence relation.

## 4. Method #4 — prove the one-edge theorem completely at finite Bernoulli intensity

Let Bernoulli nucleus intensity be `p`. For `r>=1`, write

\[
s_r:=|S_r(o)|=4\,3^{r-1}.
\]

Split the sphere into

- `A_r`: the branch through `w`, so `|A_r|=3^{r-1}=s_r/4`;
- `B_r`: the other three branches, so `|B_r|=3^r=3s_r/4`.

For `x in A_r`, `d(w,x)=r-1`; for `x in B_r`, `d(w,x)=r+1`. Also

\[
|B_{r-1}(o)|=2\,3^{r-1}-1=\frac{s_r}{2}-1.
\]

Let the same symbols `A_r,B_r` denote the corresponding Bernoulli nucleus counts when no ambiguity arises.

Condition on the nearest nucleus distance from `o` being `r>=1`. There are two disjoint ways for `E` to occur.

### Case I: `A_r>0`

At `w`, the `A_r` nuclei are strictly closer than every other possible competitor. At `o`, all `A_r+B_r` shell nuclei tie. The pointwise marks at `o,w` are independent, hence conditional on the counts,

\[
P(E\mid A_r,B_r, A_r>0)=\frac{1}{A_r+B_r}.
\]

Define

\[
G_r(p):=\mathbb E\left[\frac{\mathbf 1_{\{A_r>0\}}}{A_r+B_r}\right],
\]

with the fraction interpreted as zero when the denominator vanishes.

### Case II: `A_r=0`

Then nearest-distance `r` forces `B_r>0`. Any nucleus in `A_{r+1}` is at distance `r` from `w` and beats the old `B_r` candidates, so `E` requires `A_{r+1}=0`. Under those two zero events, the candidates nearest `w` at distance `r+1` are exactly

\[
B_r\cup A_{r+2}.
\]

The root chooses uniformly from `B_r`, while `w` independently chooses uniformly from `B_r\cup A_{r+2}`. Therefore

\[
P(E\mid B_r,A_{r+2},B_r>0,A_r=A_{r+1}=0)
=\frac{1}{B_r+A_{r+2}}.
\]

Put

\[
K_r(p):=\mathbb E\left[\frac{\mathbf 1_{\{B_r>0\}}}{B_r+A_{r+2}}\right].
\]

The zero probability is

\[
P(A_r=A_{r+1}=0)=(1-p)^{|A_r|+|A_{r+1}|}=(1-p)^{s_r}.
\]

Since the inner ball must also be empty, the exact finite-intensity identity is

\[
\boxed{
P_p(E,\ d(o,\Pi_p)\ge1)
=
\sum_{r\ge1}
(1-p)^{s_r/2-1}
\left[G_r(p)+(1-p)^{s_r}K_r(p)\right].
}
\tag{4.1}
\]

The omitted event `o in Pi_p` has probability at most `p`, so its contribution vanishes as `p->0`.

No boundary-process theorem is used in (4.1).

## 5. Method #27 — two explicit subsequences are enough

For a fixed `a>0`, choose the explicit intensity sequence

\[
\boxed{p_n(a):=\frac{a}{4\,3^{n-1}}.}
\tag{5.1}
\]

Reindex `r=n+m`. Then exactly

\[
\lambda_m:=p_n(a)s_r=a3^m.
\]

For every fixed integer `m`, as `n->infinity`, the four relevant independent binomial counts converge to independent Poisson counts with means

\[
A_r:\lambda_m/4,\qquad
B_r:3\lambda_m/4,\qquad
A_{r+1}:3\lambda_m/4,\qquad
A_{r+2}:9\lambda_m/4.
\]

Also

\[
(1-p_n)^{s_r/2-1}\to e^{-\lambda_m/2},
\qquad
(1-p_n)^{s_r}\to e^{-\lambda_m}.
\]

Define

\[
H(x):=e^{-x}\sum_{j\ge1}
\frac{x^j}{j!}\frac{1-(3/4)^j}{j}.
\tag{5.2}
\]

If `A~Pois(x/4)` and `B~Pois(3x/4)`, then conditioning on `N=A+B` gives

\[
\mathbb E\left[\frac{\mathbf1_{\{A>0\}}}{A+B}\right]=H(x),
\]

because `A|N=j~Bin(j,1/4)` and `P(A>0|N=j)=1-(3/4)^j`.

Thus

\[
G_r(p_n)\to H(\lambda_m).
\]

For `K_r`, the limiting total `B_r+A_{r+2}` has mean `3\lambda_m`, and the `B_r` class again has fraction `1/4`, hence

\[
K_r(p_n)\to H(3\lambda_m).
\]

Therefore the fixed-`m` summand tends

\[
e^{-\lambda_m/2}
\left[H(\lambda_m)+e^{-\lambda_m}H(3\lambda_m)\right].
\tag{5.3}
\]

### Uniform tail control

This is enough to exchange the reindexed infinite sum with the limit. Indeed,

\[
G_r(p)\le P(A_r>0)\le p|A_r|=\lambda_m/4,
\]

\[
K_r(p)\le P(B_r>0)\le p|B_r|=3\lambda_m/4,
\]

so every negative-tail summand is at most `lambda_m`; summing `a3^m` as `m->-infinity` is uniformly negligible.

For the positive tail, `G_r,K_r<=1`, and

\[
(1-p)^{s_r/2-1}
\le e^{-p(s_r/2-1)}
=e^{-\lambda_m/2+p}
\le e^{-\lambda_m/4},
\]

since `p=lambda_m/s_r<=lambda_m/4`. Thus the positive tail is bounded by

\[
2\sum_{m\ge M}e^{-a3^m/4}\to0.
\]

Consequently

\[
\boxed{
\lim_{n\to\infty}P_{p_n(a)}(E)
=F(a):=
\sum_{m\in\mathbb Z}
e^{-a3^m/2}
\left[H(a3^m)+e^{-a3^m}H(3a3^m)\right].
}
\tag{5.4}
\]

This is exactly the phase series previously found on `T_4 x T_4`, but here it has been derived directly from finite Bernoulli shells on one tree.

## 6. Method #16 — exact separation of two phases

The new exact checker was executed only after the proof was obtained. It verifies the shell identities and uses `fractions.Fraction` plus rigorous exponential/series tail bounds to certify

\[
F(27/100)\in
[0.457148657413679714,\ 0.457148911440002502],
\]

\[
F(47/100)\in
[0.456845192076364831,\ 0.456845634270324273],
\]

with rigorous separation

\[
\boxed{
F(27/100)-F(47/100)>0.000303023143355440.
}
\tag{6.1}
\]

Artifacts:

- `artifacts/R06/20260917T0328Z_i0079_tree_pointwise_exact.py` @ commit `81c77edfba4cfb4bf7dd3cfa09d63a20d927b7ec`;
- `artifacts/R06/20260917T0328Z_i0079_tree_pointwise_exact.out.txt` @ commit `9f90148c45d9db6a3de80b05be8454da69a9c0a3`, ending `EXACT_RATIONAL_INTERVALS_DISJOINT / PASS`.

Both were read back at their returned commit SHAs.

## 7. Theorem I0079-R06-T6 — pointwise tie-breaking is nonunique already on `T_4`

The space of equivalence relations on the countable vertex set is a closed subspace of a compact product space, hence its probability measures are weakly compact. Therefore each sequence `p_n(a_i)->0` has weakly convergent subsubsequences. The one-edge event `E={o~_Vor w}` is a clopen cylinder, so every weak sublimit along the `a_i` sequence has cylinder probability `F(a_i)`.

By (6.1), the two sublimits cannot have the same law.

Hence:

\[
\boxed{
\text{For the pointwise-independent random tie refinement on }T_4,
\text{ the low-intensity Bernoulli--Voronoi IRE is not unique.}
}
\tag{T6}
\]

This is stronger than the previous product-tree example in one respect: **product geometry is not needed**. The decisive issue is the correlation structure of tie-breaking.

The theorem does **not** contradict Bhupatiraju's regular-tree uniqueness theorem. The published regular-tree construction assigns one iid continuous label to each nucleus and reuses that same label at every evaluation vertex. D'Achille et al.'s current IPVT paper states this convention explicitly and proves that the resulting restriction to tree vertices has phase-independent law. Our source-admissible pointwise rule instead refreshes the tie randomness at each evaluation vertex, and that destroys the global fractional-delay coupling.

This also does **not** label the source's Question 2 `REFUTED`: Question 2 asks “in what generality” uniqueness holds, rather than asserting universal uniqueness for every refinement. The honest source status remains **PARTIAL**. T6 supplies a sharp negative boundary: even on a regular tree, uniqueness can fail under a natural pointwise-random refinement.

## 8. Current literature / novelty check — 2026-09-17

Primary source check: the current/accepted Jardón-Sánchez–Mellick–Poulin–Wróbel paper still states Question 2. Its Section 6 explicitly allows random pointwise boundary resolution before fixing a refinement.

Nearest solved work: Sandeep Bhupatiraju's 2019 thesis proves the low-intensity limit on regular trees under one iid label per nucleus; the later IPVT paper by D'Achille–Curien–Enriquez–Lyons–Ünel explicitly explains the global-label convention and states phase independence of the vertex restriction. Fresh bounded searches for `pointwise tie`, `independent tie-breaking`, `Bernoulli Voronoi regular tree`, and later citing work did not locate a paper stating T6 or the one-edge formula above.

This is **negative bounded search evidence only**. Novelty remains **UNVERIFIED** until an independent prior-art audit is completed.

A fresh repository search still found no `P26-AUDIT-R06-I0079` and no independent audit of the pointwise theorem T5/T6. The earlier R05 audit concerns the old global-label phase-cancellation core, which is now classified KNOWN and does not audit T6.

## 9. Six-unchanged-run rotation gate

The fixed canonical metric is still `R_unique=+infinity`, so this invocation is the **sixth consecutive unchanged run**. Under the owner rule, R06 now operationally retires I0079 from active hourly attack and leaves this report as the handoff. The mathematics is not declared closed: full Question 2 remains PARTIAL, T6 is author-side proved/self-checked/audit-pending, and novelty is unverified.

I screened the present CLOSABLE queue/ownership state before claiming any successor. Current high-ranked candidates are occupied, source-resolved/held, or not CLOSABLE-ready. In particular, recent independent queue screens on current master record no candidate simultaneously `READY + unassigned + CLOSABLE OUTSIDE`. The apparently attractive I0087 / IPVT Question 7.1 example `H^2 x R` is not a lawful fresh-open target: D'Achille–Khezeli (arXiv:2606.30517, June 2026) gives general convergence criteria and explicitly treats product examples including `H^2 x R`. Current claims also occupy the earlier READY front.

Therefore no create-only successor claim is fabricated. R06 enters

\[
\boxed{\texttt{ROTATION\_WAIT / SUCCESSOR\_ADMISSION\_REQUIRED}.}
\]

The next invocation should screen for a newly certified, source-current, unassigned CLOSABLE target before doing new research. It must not resume I0079 merely because the native prompt remains stale.

## 10. Independent R06 audit of newest R07 package

Newest neighboring package read:

`runs/R07/20260917T0230Z_i0077_log_sawtooth_envelope_10.md`.

New theorem `I0077-R07-T11` says a continuous positive super-LIL gauge `f` with finite running-envelope distortion

\[
Q_f=\sup_{u>0}\frac{\sup_{0<s\le u}f(s)}{f(u)}<\infty
\]

inherits the decomposable-FBM confinement theorem from the previously proved monotone gauge theorem by setting `F(u)=max_{s<=u} f(s)` and paying factor `Q_f`. The proof is correct: the running maximum of a continuous function is continuous/nondecreasing, preserves both super-LIL lower asymptotics because `F>=f`, and obeys `F<=Q_f f`; applying the earlier T2 result with amplitude `C/Q_f` gives the desired bound.

The log-sawtooth specialization also checks: its periodic multiplier lies in `[1,4/3]`, so `Q_f<=4/3`, while the exact inequality `4/3>2^(3/8)` forces a genuine decrease once in every dyadic scale. I found no mathematical gap in this scoped compiler/specialization, conditional only on the previously established T2 theorem it invokes.

Audit verdict:

`R06-AUDIT-R07-I0077-T11-20260917T0330Z: PASS_SCOPED / NOVELTY_UNVERIFIED`.

This is not a full audit of all ten R07 shape families or worldwide prior art.

## 11. Model/runtime and protected-task escalation

The implementation limit is unchanged. `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records that the task-control surface exposes schedule/prompt/enabled/timing controls but **no model selector, no reasoning-effort selector, no authenticated runtime telemetry, and no guaranteed hour-long execution**. GPT-6/maximum therefore remains a prompt request, not an enforceable setting here.

The same manifest records a P26 update attempt that returned `You cannot modify this task` in one context; later root records note successful P26 changes from another authorized context. The legitimate workaround for a protected task is the owning/authorized control context, explicit permission transfer, or platform support — not duplication or bypass. No scheduler modification was attempted.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  run_id: 20260917T0330Z_i0079_tree_pointwise_nonunique_rotation_07
  source: "Jardon-Sanchez--Mellick--Poulin--Wrobel, Exactness and the topology of the space of invariant random equivalence relations, Question 2 / I0079"
  canonical_metric: "R_unique for frozen global-iid-nucleus-label refinement on F_2 x F_2"
  before: "+infinity"
  after: "+infinity"
  movement: "none"
  unchanged_count: 6
  methods: [4, 16, 27]
  source_status: "PARTIAL"
  new_theorem:
    id: "I0079-R06-T6"
    statement: "pointwise-independent tie refinement on T_4 has nonunique low-intensity Bernoulli-Voronoi IRE limits"
    status: "PROVED / SELF-CHECKED / AUDIT-PENDING / NOVELTY-UNVERIFIED"
    cylinder: "E={root and fixed neighbor assigned to same nucleus}"
    subsequences:
      a1: "27/100"
      a2: "47/100"
      p_n: "a/(4*3^(n-1))"
    exact_gap_lower_bound: "0.000303023143355440"
    evidence:
      - "artifacts/R06/20260917T0328Z_i0079_tree_pointwise_exact.py @ 81c77edfba4cfb4bf7dd3cfa09d63a20d927b7ec"
      - "artifacts/R06/20260917T0328Z_i0079_tree_pointwise_exact.out.txt @ 9f90148c45d9db6a3de80b05be8454da69a9c0a3"
  audit_ids:
    P26_I0079: NOT_FOUND
    independent_T6: NOT_FOUND
    outgoing_R07: "R06-AUDIT-R07-I0077-T11-20260917T0330Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
  rotation:
    triggered: true
    reason: "six consecutive unchanged runs in frozen canonical metric"
    successor_claim_created: false
    successor_status: "ROTATION_WAIT / SUCCESSOR_ADMISSION_REQUIRED"
    gate: "no currently screened target simultaneously READY + unassigned + CLOSABLE OUTSIDE"
  remaining_obligation: >-
    Preserve I0079 handoff; obtain independent audits/prior-art review of T6 if revisited.
    Do not run a seventh I0079 research attack. On the next invocation, first screen the
    current queue for a newly certified unassigned CLOSABLE successor.
```

END OF IMMUTABLE R06 REPORT
