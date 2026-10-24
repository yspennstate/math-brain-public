Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `31 -> 32` genuinely distinct nonparabolic shape families; Section-B moves actually used: #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The following source sentence is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 32: moving Cantor laminations

Run date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T2325Z_i0077_accelerating_log_chirps_31.md`,

which moved the metric `30 -> 31` and used moves `#7,#13,#30`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. Thus the literal instruction to choose three moves never previously used on this problem is exhausted; I do not invent a false history. What matters here is a new structural mechanism and a triple different from the immediately preceding run.

Before new mathematics I recovered current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the full visible R07 directory and the searchable I0077 chain through run 31;
- current neighboring R15 state, including the preserved six-run handoff from distinct Burdzy–Scheutzow Problem 7.2 / I0076 and R15's later rotation to other sources;
- C29's I0077 duplicate-exclusion records;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 separately. The canonical claim names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of this exact target to R07. R15's distinct Problem 7.2 is not reopened. The old R07 KPZ/FPP route remains preserved by immutable handoff rather than deleted.

The large `probability_1000_intake_*/problems.jsonl` resources cannot be rendered byte-for-byte through the available connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: the exact I0077 statement, ownership, exclusions, and searchable prior attempts were recovered; I do not claim a literal reread of every unrelated intake row.

Entering metric: **31**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary paper was rechecked, including Definitions 2.1–2.2, Remarks 4.1–4.2, Theorem 4.3, its proof, Proposition 4.4, and the open-problem page.

An FBM is a continuous real-indexed process `X` (with the source normalization `X_0=0`) for which there are random witness times `S_j -> -infinity` such that for each fixed `j`

\[
B^{(j)}(t):=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is standard Brownian motion. A decomposable FBM is built by concatenating independent Brownian pieces stopped at finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, the paper writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact static parabolic strip for every `t<=0`.

Remark 4.1 gives continuity and strict domain monotonicity of `lambda_0`; Remark 4.2 records, among other critical pairs,

\[
\lambda_0(-1,1)=1.
\tag{2.2}
\]

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. The next sentence is separately Problem 7.9 on forward Lévy processes.

## 3. Fresh current-status / prior-art pass

Fresh bounded searches on 2026-09-18 UTC included:

- the exact paper title/arXiv ID and exact Problem-7.8 wording;
- later/citing material around Burdzy–Scheutzow;
- `Brownian motion moving Cantor set confinement`;
- `Brownian motion Cantor set time-dependent boundary`;
- `Ornstein-Uhlenbeck Cantor set moving domain`;
- disconnected-set diffusions and quasidiffusions.

The closest clearly relevant disconnected-state-space reference remains Shankar Bhamidi, Steven N. Evans, Ron Peled and Peter Ralph, *Brownian motion on disconnected sets, basic hypergeometric functions, and some continued fractions of Ramanujan* (IMS Collections, 2008; DOI 10.1214/193940307000000383). That work constructs a different Markov process whose state space itself is a closed disconnected subset of the line; it is not ordinary Euclidean Brownian motion or an FBM required to remain in a deterministic moving space-time lamination. A 2025 quasidiffusion/Fukushima-subspace literature also cites that disconnected-state-space program. These are related prior art, not source-level resolutions of Problem 7.8.

I found no explicit later resolution of exact Problem 7.8 and no theorem matching the moving-lamination result below in this bounded search. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The facts that continuous maps into totally disconnected sets are constant and that Brownian quadratic variation is nonzero are classical and are not claimed novel.

## 4. Attack the negation first: can a path switch Cantor leaves?

The candidate extension was designed to defeat the static-component argument from run 14. Instead of keeping a Cantor cross-section fixed, move and breathe the whole Cantor set continuously in logarithmic time. A natural counterexample attempt is then:

> perhaps a continuous path can keep changing its Cantor address as the fibers move, so the static “one connected component forever” obstruction disappears.

That attempt fails for an exact topological reason. After undoing the ambient motion, the Cantor address is a continuous map from a connected time interval into a totally disconnected set. It therefore cannot change at all.

This failure is the new mechanism of the run. It does **not** say the source's open-ended Problem 7.8 is false.

## 5. New shape family: affinely moving totally disconnected laminations

Let `K` be a nonempty compact totally disconnected subset of `R`. Let

\[
a,b\in C^1(\mathbb R),\qquad
0<a_-\le a(r)\le a_+<\infty,
\qquad |b(r)|\le b_+<\infty.
\tag{5.1}
\]

Define the moving normalized fiber

\[
D(r)=a(r)K+b(r)
=\{a(r)z+b(r):z\in K\}
\tag{5.2}
\]

and the backward space-time lamination

\[
\boxed{
\mathcal L(K,a,b)
=
\left\{(-u,\sqrt u\,[a(\log u)z+b(\log u)]):u>0,\ z\in K\right\}
\cup\{(0,0)\}.
}
\tag{5.3}
\]

The shape is closed. For `u>0` this follows from compactness of `K` and continuity of the parameterization. As `u downarrow0`, boundedness of `a`, `b`, and `K` forces every point of the `u`-slice to converge to `(0,0)`.

The fibers need not be small. `K` may be a fat Cantor set of positive Lebesgue measure and arbitrarily large diameter. No spectral narrowness, small duty cycle, or sparse-gate condition is assumed.

### Canonical genuinely moving example

Let `C` be the middle-thirds Cantor set in `[0,1]` and put

\[
K_*=2C-1\subset[-1,1].
\tag{5.4}
\]

Take

\[
a_*(r)=2+\frac12\sin r,
\qquad
b_*(r)=\sin(\sqrt2\,r).
\tag{5.5}
\]

Then every normalized slice is a compact perfect Cantor set, but its diameter breathes periodically while its center moves with an incommensurate frequency. The normalized space-time geometry has no nonzero logarithmic period.

## 6. Why this is a distinct metric family

Run 14 treated **static** compact normalized sets, especially fat-Cantor fans `D(r)\equiv K`. In (5.3), the normalized fiber itself moves. Undoing that motion is a time-dependent coordinate change; it is not one of the frozen equivalences (Brownian rescaling, reflection, translation, or mere parameter choice) because a time-dependent affine change does not preserve Brownian law or the FBM witness property.

For the canonical example (5.5), Brownian rescaling only translates `r=log u`; it cannot make the nonconstant scale `a_*(r)` and incommensurate translation `b_*(r)` constant. Reflection only changes signs. The pair of logarithmic frequencies `1` and `sqrt(2)` also cannot collapse to the static family under a time translation.

This is also not run 15's periodically gated disconnected fan: no components ever merge, no narrow connected gate occurs, and the canonical family is quasiperiodic rather than periodic. It is not run 30's Cantor-parity shutter: every fiber here is compact and totally disconnected, whereas run 30 alternates unbounded half-lines and full-space portal fibers. The obstruction below is topological conservation plus Brownian roughness, not killed-OU dissipation, sampled persistence, or fast transport.

Accordingly the frozen metric counts this as one new structural family. Different `K,a,b` choices inside (5.1) are **not** counted separately.

## 7. Method #1 — CHANGE THE CATEGORY

The direct stochastic-boundary view hides the invariant. Pass instead to the moving fiber coordinate. For a continuous path `X` define, whenever `u>0`,

\[
y(u)=\frac{X_{-u}}{\sqrt u},
\qquad
r=\log u,
\tag{7.1}
\]

and, on confinement to (5.3),

\[
z(r)
=
\frac{y(e^r)-b(r)}{a(r)}.
\tag{7.2}
\]

The stochastic space-time problem has become a purely topological problem: `z` is a continuous map from a connected interval into the compact totally disconnected space `K`.

**Outcome #1: success.** The right category is a lamination with a conserved leaf label, not a moving-boundary spectral problem.

## 8. Method #12 — FIND WHAT IS CONSERVED: the Cantor address

A connected subset of a totally disconnected set is a singleton. Hence if an eventually confined continuous path satisfies

\[
z([R,\infty))\subset K,
\tag{8.1}
\]

then there is one `c\in K` such that

\[
\boxed{z(r)\equiv c\qquad(r\ge R).}
\tag{8.2}
\]

Returning to physical time, every eventually confined continuous path must therefore lie on exactly one deterministic leaf:

\[
\boxed{
X_{-u}
=
F_c(u)
:=
\sqrt u\,[a(\log u)c+b(\log u)]
\qquad(u\ge e^R).
}
\tag{8.3}
\]

The leaf label `c` may depend on the sample path, but it cannot change with time.

Because `a,b\in C^1`, each `F_c` is `C^1` on every compact subinterval of `(0,\infty)`.

**Outcome #12: success.** The conserved quantity is the Cantor address / leaf label.

## 9. Brownian roughness lemma, proved directly

The final input is elementary but I record it on the page rather than citing it vaguely.

### Lemma 9.1

A standard Brownian path on `[0,1]` almost surely does not coincide with any `C^1` function on `[0,1]`.

### Proof

For Brownian motion `B`, let

\[
Q_n(B)
=
\sum_{k=0}^{2^n-1}
\left(
B_{(k+1)2^{-n}}-B_{k2^{-n}}
\right)^2.
\tag{9.1}
\]

The increments are independent `N(0,2^{-n})`, so

\[
\mathbb E Q_n(B)=1,
\qquad
\operatorname{Var}(Q_n(B))=2^{1-n}.
\tag{9.2}
\]

For every `epsilon>0`, Chebyshev gives

\[
\mathbb P(|Q_n(B)-1|>\epsilon)
\le
\frac{2^{1-n}}{\epsilon^2}.
\tag{9.3}
\]

The right side is summable. Borel–Cantelli, first for rational positive `epsilon` and then by intersection, gives

\[
\boxed{Q_n(B)\to1\quad\text{a.s.}}
\tag{9.4}
\]

If `f\in C^1([0,1])` and `M=\|f'\|_\infty`, then every dyadic increment has magnitude at most `M2^{-n}`, hence

\[
Q_n(f)
\le
2^n M^2 2^{-2n}
=M^2 2^{-n}\longrightarrow0.
\tag{9.5}
\]

Therefore any path equal to a `C^1` function would have dyadic quadratic variation tending to zero, whereas Brownian motion has limit one. QED.

Note that this proof automatically handles an uncountable or random choice of `C^1` leaf: the event “the Brownian path equals some `C^1` path” is contained in the pathwise event `Q_n(B)->0`, which has probability zero.

## 10. I0077-R07-T33 — moving totally disconnected lamination obstruction

**Theorem T33.** Let `K,a,b` satisfy (5.1). For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
(-u,X_{-u})\in\mathcal L(K,a,b)
\quad\forall u\ge R
\right)=0.
}
\tag{T33}
\]

In particular no FBM can be confined pointwise to `\mathcal L(K,a,b)` on the whole negative half-line.

### Complete proof

Let

\[
E_m
=
\left\{
(-u,X_{-u})\in\mathcal L(K,a,b)
\quad\forall u\ge m
\right\}.
\tag{10.1}
\]

The eventual-confinement event is the countable union `union_{m>=1} E_m`. Suppose it has positive probability. Then for some deterministic integer `m`,

\[
p:=\mathbb P(E_m)>0.
\tag{10.2}
\]

On `E_m`, Sections 7–8 imply that there is a sample-path-dependent but time-independent `c\in K` for which

\[
X_t
=
\sqrt{-t}\,[a(\log(-t))c+b(\log(-t))]
\qquad\forall t\le-m.
\tag{10.3}
\]

Let `(S_j)` be the FBM witness sequence. Since `S_j->-infinity` almost surely,

\[
\mathbf 1_{\{S_j+1\le-m\}}\longrightarrow1
\quad\text{a.s.}
\tag{10.4}
\]

and dominated convergence gives

\[
\mathbb P(E_m\cap\{S_j+1\le-m\})\longrightarrow p.
\tag{10.5}
\]

Choose one **deterministic** index `j` for which

\[
\mathbb P(E_m\cap\{S_j+1\le-m\})>p/2.
\tag{10.6}
\]

By the FBM definition,

\[
B^{(j)}_s=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{10.7}
\]

is standard Brownian motion. On the event in (10.6), the whole interval `[S_j,S_j+1]` lies inside `(-infinity,-m]`, so (10.3) says that `s\mapsto B^{(j)}_s` on `[0,1]` is the difference of two values of the `C^1` leaf (10.3). Hence it is itself `C^1` on `[0,1]`.

Lemma 9.1 says a standard Brownian motion has probability zero of being `C^1` on `[0,1]`. Therefore the event in (10.6) must have probability zero, contradicting `p/2>0`.

This proves T33. No independence between `S_j`, the leaf label `c`, and the Brownian witness is assumed. QED.

## 11. Method #20 — FIND WHY THE ALGORITHM FAILS

The obvious constructive algorithm for a moving Cantor slice is: when the current affine image of the Cantor set drifts, jump to a nearby Cantor address and keep following the union. The exact failure is now visible. A continuous confined path cannot jump between addresses because the inverse affine coordinate `z(r)` is continuous and `K` is totally disconnected. The only possible algorithm is “choose one address once and follow its leaf forever.” That turns the candidate FBM tail into a `C^1` path, which is incompatible with every Brownian witness.

**Outcome #20: success.** The obstruction is not small cross-sectional measure; it is the impossibility of leaf switching plus positive Brownian quadratic variation.

## 12. Concrete corollary

For the canonical `K_*,a_*,b_*` in (5.4)–(5.5), no FBM can eventually satisfy

\[
\boxed{
\frac{X_{-u}}{\sqrt u}
\in
\left(2+\frac12\sin(\log u)\right)K_*
+
\sin(\sqrt2\,\log u)
\qquad\forall u\text{ sufficiently large}.
}
\tag{12.1}
\]

Every normalized slice is an uncountable perfect compact set. Its diameter and center both move forever, and the motion is not log-periodic. Nevertheless the theorem is pathwise universal for all FBMs.

The same conclusion holds if `K_*` is replaced by any compact fat Cantor set of positive Lebesgue measure. Thus large slice measure does not rescue confinement.

## 13. Metric decision and relation to previous families

The metric moves

\[
\boxed{31\longrightarrow32}.
\]

Reason for counting exactly one new family:

- it is time-dependent in normalized coordinates, unlike run 14's static compact/Cantor fans;
- it has compact totally disconnected fibers at every time, unlike run 30's alternating half-lines/full-space portals;
- there are no narrow gates or positive-density killing phases as in runs 7, 8, 15, 16;
- there is no sampled-time restriction as in runs 24, 26–28;
- there is no forced fast transport between interval windows as in runs 19 or 31;
- the invariant is a conserved topological leaf label under a nontrivial time-dependent ambient motion.

Different Cantor sets, amplitudes, frequencies, and affine coefficients satisfying (5.1) are one family and are not counted separately.

Exiting metric: **32**.  
Exiting unchanged count: **0**.

## 14. What is and is not claimed

Claimed/proved here:

- the complete universal obstruction T33 for the whole affine moving-totally-disconnected class (5.1)–(5.3);
- the canonical quasiperiodic breathing/translating Cantor example (12.1);
- the dependence-safe FBM transfer using one deterministic witness index.

Not claimed:

- closure of the open-ended source Problem 7.8;
- a sharp theorem for **thickened** moving Cantor fibers `D(r)+[-delta,delta]`;
- publication novelty of the topological mechanism;
- that a bounded web search proves worldwide openness.

The most interesting next mathematical boundary is the thickened lamination: once each Cantor leaf has positive width, the conserved-address argument breaks because connected components of the thickening are intervals. The sharp transition between topological leaf locking and a genuinely diffusive moving-fiber phase is not settled here.

No exact-arithmetic checker was manufactured: T33 has no finite computational core. The quadratic-variation calculation is analytic and written in full above. A checker would be bookkeeping without testing a substantive finite claim.

## 15. Audit / closure status

T33 is a new theorem-sized claim and currently has **0/2 independent OTHER-track audits**. In particular it does not inherit audits of earlier R07 theorems. The source therefore remains **PARTIAL**, not closed, and no `paper_<name>/` closure package is created.

## 16. Model/reasoning and scheduler-control escalation

The GPT-6 configuration limitation is still present in the actual exposed control surface available to this run. The scheduler/task schema exposes prompt/title, schedule or start offset, enabled state, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains a prompt request here rather than an enforceable setting, and I do not claim it ran.

Repository policy also records native modification probes for P26, P01, and P03 returning `You cannot modify this task`. The legitimate workaround is not a worker-level bypass or duplicate task: the relevant task/account/workspace ownership must be resolved in an authorized owning/admin interface, or platform support must expose the needed model/reasoning controls and scheduler ownership. No scheduler mutation, permission bypass, or support request was attempted in this run.

## 17. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  source_id: I0077
  source: Burdzy-Scheutzow_2014_Problem_7_8
  metric_name: distinct_nonparabolic_shape_families_with_complete_source_appropriate_theorem
  before: 31
  after: 32
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: moving_totally_disconnected_affine_laminations
  new_claim_id: I0077-R07-T33
  claim_scope: universal_nonconfinement_for_affinely_moving_compact_totally_disconnected_normalized_fibers
  source_status: PARTIAL
  canonical_claim_file_status: PENDING_ADMISSION_not_READY_preserved
  independent_audits: 0/2
  finite_core: none
  checker: not_applicable
  novelty: UNVERIFIED
  methods: [1, 12, 20]
  previous_methods: [7, 13, 30]
  intake_read: targeted_partial_due_connector_truncation
  delivery: private_GitHub_master_only
```

## 18. Next route

Do **not** spend the next run adding a checker to T33. A genuinely new route is to investigate a thickened moving lamination

\[
D_\delta(r)=a(r)K+b(r)+[-\delta,\delta]
\]

where the topological conserved address disappears. The useful question is whether one can identify a nontrivial threshold using the geometry of the largest surviving Cantor gaps together with OU crossing, rather than treating `delta` as merely another parameter of T33. If that only reproduces the existing moving-interval or gate compilers, it must not be counted as a new family.
