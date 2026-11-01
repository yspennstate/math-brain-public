Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `40 -> 41` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate.

# R07 CLOSABLE OUTSIDE — run 41: locally finite critical Hölder forests

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0825Z_i0077_critical_holder_braids_40_c40h5e.md`,

which moved `39 -> 40` and used moves `#3,#18,#26`. The present triple is different. All thirty Section-B moves have already appeared somewhere in the long I0077 chain, so the literal instruction to choose three globally never-before-used numbers is exhausted; I do not invent a false history. What is new here is the route, obstruction, theorem, and shape family.

Before new mathematics I reread/recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 chain, with special attention to runs 33, 34, 39 and 40 because the present theorem separates finite critical webs from genuinely countable ones;
- the newest neighboring R15 report, `runs/R15/20260918_0726Z_successor_admission_f0111_homogeneous_k2_h52b.md`; R15’s original Burdzy–Scheutzow Problem 7.2 / I0076 remains a separate `OPEN / PARTIAL / RETIRED-HANDOFF` target, so there is no I0077 collision;
- C29’s latest duplicate-exclusion record, which explicitly says `proposed_I0077: EXCLUDED_FROM_C29` and `I0077_owner: R07`;
- targeted intake/source searches for `I0077`, `1302.6958`, `Problem 7.8`, the exact source wording, and later/citing literature.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 closure. `QUEUE.md` lists I0077 separately from 7.2 and 7.5. `operations/claims/I0077.md` still reserves this exact target to R07 and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared operational label while following the current owner assignment. The old R07 KPZ route remains preserved in immutable handoff/history and is not reopened or deleted. No shared root or peer file is edited in this run.

The intake JSONL collections are too large to render byte-for-byte through this connector without truncation. The admission reread is therefore honestly targeted to exact I0077 source text, ownership, exclusions, current neighboring state, and the relevant prior attempts. I do not claim a literal reread of every unrelated intake row.

Entering metric: **40**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

The primary PDF was reopened on 2026-09-18 and Definition 2.1, Definition 2.2, Theorem 4.3, and the open-problem page were rechecked.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` a.s. such that for every **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces stopped at finite stopping times.

For a static parabolic normalized interval `[c_1,c_2]`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the source’s universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM confined pointwise to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh 2026-09-18 current-status / prior-art pass

A bounded fresh search covered:

- exact `"Forward Brownian Motion" "Problem 7.8"` and `"other space-time shapes"` wording;
- Burdzy/Scheutzow together with Hölder curves, moving boundaries, and later citing papers;
- continuous selectors of countable smooth/Hölder families;
- Brownian critical `1/2`-Hölder regularity;
- the exact Hausdorff dimension of the classical Weierstrass graph.

The search recovered the original Burdzy–Scheutzow paper and no accessible later paper explicitly resolving exact Problem 7.8 or stating the locally finite critical-web theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

Nearby prior art is real and is not claimed as new. Brownian motion is classically locally Hölder for every exponent below `1/2` but not at `1/2`; the needed endpoint failure is proved directly below. The classical Weierstrass graph dimension theorem of Weixiao Shen gives

\[
\dim_H \operatorname{graph}\!\left(\sum_{n\ge0}\lambda^n\cos(2\pi b^n r)\right)
=2+\frac{\log\lambda}{\log b}
\]

for integer `b>=2` and `lambda in (1/b,1)`. For `b=2`, `lambda=2^{-1/2}`, this equals `3/2`. Continuous-selection and moving-boundary literature found in the search concerns different hypotheses/objects. The elementary finite closed-cover intersection-graph mechanism below may be folklore topology; I do not claim that mechanism itself as new.

## 4. Method #2 — attack the naive countable extension first

Run 40 proved that a continuous selector of **finitely many** locally `1/2`-Hölder sheets is itself `1/2`-Hölder. The obvious next conjecture would simply replace “finite” by “countable.” That conjecture is false, even for globally affine sheets.

### Proposition 4.1 — exact countable affine-selector counterexample

For `n>=1`, set

\[
t_n=2^{-n},\qquad \delta_n=2^{-4n},\qquad a_n=2^{-n}.
\]

The intervals

\[
J_n=[t_n,t_n+2\delta_n]
\]

are pairwise disjoint. Define a continuous triangular-spike function `h:[0,1]->R` by `h=0` off the union of the `J_n`, and on each `J_n`,

\[
h(t)=
\begin{cases}
\dfrac{a_n}{\delta_n}(t-t_n),&t_n\le t\le t_n+\delta_n,\\[1ex]
a_n-\dfrac{a_n}{\delta_n}(t-t_n-\delta_n),&t_n+\delta_n\le t\le t_n+2\delta_n.
\end{cases}
\tag{4.1}
\]

For every `n`, let `ell_{n,+}` and `ell_{n,-}` be the two affine functions appearing in (4.1), extended to all of `[0,1]`, and include the zero sheet `ell_0=0`. Then at every time

\[
h(t)\in\{\ell_0(t),\ell_{1,+}(t),\ell_{1,-}(t),\ell_{2,+}(t),\ldots\}.
\]

Thus `h` is a continuous selector from a countable family of globally Lipschitz, hence `1/2`-Hölder-on-compacts, sheets. But

\[
\frac{|h(t_n+\delta_n)-h(t_n)|}{\sqrt{\delta_n}}
=\frac{a_n}{\sqrt{\delta_n}}
=2^n\longrightarrow\infty.
\]

Therefore `h` is not `1/2`-Hölder.

The disjointness is exact: for every `n>=1`,

\[
2^{-(n+1)}+2\,2^{-4(n+1)}<2^{-n}.
\]

**Outcome #2: success as a falsification.** Countability alone is not the right replacement for finiteness. The failure mechanism is migration through sheets whose local slopes/complexity explode at accumulating times. This refutes a proposed extension of the run-40 selector lemma, **not** Burdzy–Scheutzow Problem 7.8.

## 5. Method #7 — take the finite theorem to its correct locally finite limit

The counterexample shows what must survive in the countable limit: every compact time window must see only finitely many candidate sheets. This leads to a clean theorem with no global bound on the number of sheets.

### Definition 5.1 — locally finite critical Hölder forest

Let

\[
\{(I_k,g_k):k\in\mathbb N\}
\]

be a countable deterministic family such that:

1. every `I_k` is a closed interval (possibly a ray) relative to `(0,infinity)`;
2. `g_k:I_k->R` is continuous and locally `1/2`-Hölder;
3. the family is **time-locally finite**: for every compact `J subset (0,infinity)`, only finitely many `k` satisfy `I_k cap J != emptyset`.

Define

\[
\mathcal W
=
\bigcup_{k\ge1}\{(-u,g_k(u)):u\in I_k\},
\tag{5.1}
\]

with `(0,0)` adjoined when needed to close the shape at the origin.

No uniform bound on the number of active branches is assumed; it may tend to infinity arbitrarily fast as `u->infinity`.

### Lemma 5.2 — local finite-selector certificate

Fix a compact age interval `J`. Let `K_J={k:I_k cap J != emptyset}` and `m_J=|K_J|<infinity`. Suppose a continuous function `h:[0,1]->R` satisfies, for some `U` with `[U-1,U] subset J`,

\[
h(s)\in\{g_k(U-s):k\in K_J,\ U-s\in I_k\}
\qquad(0\le s\le1).
\tag{5.2}
\]

Then `h` is `1/2`-Hölder on `[0,1]`.

#### Proof

For each active `k`, define the closed set

\[
A_k=\{s\in[0,1]:U-s\in I_k,\ h(s)=g_k(U-s)\}.
\]

The finitely many `A_k` cover `[0,1]`.

Fix arbitrary `0<=s<t<=1` and now **restrict the cover to `[s,t]`**. Form the finite graph whose vertices are the nonempty sets `A_k cap [s,t]`, joining two labels when their restricted sets intersect. This graph is connected: otherwise the unions over two graph components would be disjoint nonempty closed subsets whose union is the connected interval `[s,t]`.

Choose an endpoint label `i_0` at `s`, an endpoint label `i_q` at `t`, and a simple graph path

\[
i_0,i_1,\ldots,i_q,
\qquad q\le m_J-1.
\]

For `1<=ell<=q`, choose a junction

\[
r_\ell\in A_{i_{\ell-1}}\cap A_{i_\ell}\cap[s,t],
\]

and put `r_0=s`, `r_{q+1}=t`. Because all involved ages lie in the fixed compact `J`, each active sheet has a finite `1/2`-Hölder constant there. Let `L_J` be their maximum.

At each junction the adjacent sheets agree with `h`. Hence the exact telescoping identity along the sheet path gives

\[
|h(t)-h(s)|
\le
\sum_{\ell=0}^{q}
L_J\,|r_{\ell+1}-r_\ell|^{1/2}.
\]

The junctions need not be chronologically ordered, but every `r_ell` lies in `[s,t]`, so every distance is at most `t-s`. Therefore

\[
\boxed{|h(t)-h(s)|\le m_JL_J\sqrt{t-s}.}
\tag{5.3}
\]

Since `s,t` were arbitrary, `h` is `1/2`-Hölder. `QED`

The restriction to `[s,t]` is explicit here; this removes any possible ambiguity in using an intersection graph built on a larger interval.

## 6. Brownian endpoint roughness, proved on the page

### Lemma 6.1 — standard Brownian motion is not `1/2`-Hölder

Let `B` be standard Brownian motion on `[0,1]`. Then

\[
\mathbb P(B\text{ is }1/2\text{-Hölder on }[0,1])=0.
\tag{6.1}
\]

#### Proof

For integer `M>=1`, let `H_M` be the event

\[
|B_t-B_s|\le M|t-s|^{1/2}
\qquad\forall s,t\in[0,1].
\]

If `H_M` occurs, then at every dyadic level `n`, all `2^n` normalized increments obey

\[
2^{n/2}|B_{(j+1)2^{-n}}-B_{j2^{-n}}|\le M.
\]

For a fixed level those normalized increments are independent `N(0,1)`. If `p_M=P(|Z|<=M)<1`, then

\[
P(H_M)\le p_M^{2^n}\to0.
\]

Thus `P(H_M)=0` for every integer `M`, and the countable union over `M` proves (6.1). `QED`

## 7. Main theorem — countably many globally, finitely many per compact age window

### I0077-R07-T47 — locally finite critical-Hölder-forest obstruction

Let `mathcal W` be a locally finite critical Hölder forest in the sense of Definition 5.1. Then for **every** forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal W
\quad\forall u\ge R
\right)=0.
}
\tag{T47}
\]

#### Proof

Assume the displayed event has positive probability. By a countable union over integer radii, choose a deterministic integer `R>=1` such that

\[
E_R:=\{(-u,X_{-u})\in\mathcal W\ \forall u\ge R\}
\]

has probability `p>0`.

Let `S_j` be the FBM witness times. Since `S_j->-infinity` a.s., choose one **deterministic witness index** `j` with

\[
P(A_j)>1-p/2,
\qquad
A_j:=\{S_j+1\le-R\}.
\tag{7.1}
\]

Then

\[
P(E_R\cap A_j)\ge p/2>0.
\tag{7.2}
\]

Fix an outcome in this intersection and put `U=-S_j`. For `0<=s<=1`, the age `U-s` lies in the compact interval `[U-1,U] subset (0,infinity)` and is at least `R`. Event `E_R` therefore gives

\[
h(s):=X_{S_j+s}
\in\{g_k(U-s):U-s\in I_k\}.
\tag{7.3}
\]

By time-local finiteness, only finitely many sheets meet `[U-1,U]`. Lemma 5.2 therefore implies that the realized path `h` is `1/2`-Hölder on `[0,1]`, with a finite constant that may depend on the outcome through `U`.

Subtracting `h(0)` preserves this property, so

\[
B^{(j)}(s)=X_{S_j+s}-X_{S_j}
\]

is `1/2`-Hölder on `[0,1]` on `E_R cap A_j`. But for this fixed deterministic index `j`, Definition 2.1 says `B^{(j)}` is unconditionally standard Brownian motion. Lemma 6.1 says the path-only event “`B^{(j)}` is `1/2`-Hölder on `[0,1]`” has probability zero. This contradicts (7.2).

No conditioning on `S_j` and no independence assumption between `S_j` and its Brownian witness path is used. `QED`

**Outcome #7: success.** The finite critical web theorem survives the countable limit exactly under time-local finiteness, with no global branch-count bound.

## 8. Method #19 — the proof is an explicit local certificate algorithm

The deterministic core of T47 is constructive. Given a witness window `[U-1,U]` and a continuous selector:

1. enumerate the finitely many sheets meeting that compact age interval;
2. on each query interval `[s,t]`, form the restricted closed-cover intersection graph;
3. take a simple path from a sheet realizing the selector at `s` to one realizing it at `t`;
4. telescope through the junction values;
5. output the certificate `|h(t)-h(s)| <= m_J L_J sqrt(t-s)`.

The only way this algorithm can fail is precisely what Proposition 4.1 exposes: infinitely many sheets may accumulate in one compact time window, letting the selector pass through an unbounded cascade of labels and critical constants.

**Outcome #19: success.** The surviving construction is an algorithmic proof and isolates the exact obstruction to the naive countable extension.

## 9. Concrete new family earning metric point 41: proliferating critical Weierstrass forests

Set

\[
W(r)=\sum_{m=0}^{\infty}2^{-m/2}\cos(2\pi2^m r),
\tag{9.1}
\]

and

\[
F(u)=\sqrt u\,W(\log(1+u)),\qquad u>0.
\tag{9.2}
\]

A standard frequency split proves directly that `W` is `1/2`-Hölder. Indeed, for `d=|x-y|` choose `N` with `2^{-N-1}<d<=2^{-N}`. For `m<=N`, the mean-value theorem gives a total `O(d sum_{m<=N}2^{m/2})=O(sqrt d)` contribution; for `m>N`, the geometric tail is `O(2^{-N/2})=O(sqrt d)`. Thus

\[
|W(x)-W(y)|\le C|x-y|^{1/2}.
\tag{9.3}
\]

On every compact age interval `[a,b] subset (0,infinity)`, `u->log(1+u)` and `u->sqrt u` are Lipschitz with bounded factors. Hence `F` is locally `1/2`-Hölder.

Now define the countable family

\[
g_0(u)=0,\qquad I_0=(0,\infty),
\]

and for every integer `k>=1`,

\[
I_k=[k,\infty),
\qquad
g_k(u)=kF(u).
\tag{9.4}
\]

Let

\[
\mathcal F
=
\{(-u,0):u>0\}
\cup
\bigcup_{k=1}^{\infty}
\{(-u,kF(u)):u\ge k\}
\cup\{(0,0)\}.
\tag{9.5}
\]

On a compact age interval `[a,b]`, only `k<=b` can be active, so the family is time-locally finite. T47 gives

\[
\boxed{
P\left(
\exists R:\ (-u,X_{-u})\in\mathcal F\ \forall u\ge R
\right)=0
}
\tag{T48}
\]

for every FBM.

This forest is not merely countably infinite in name; its local branching complexity diverges. The number of active branches at age `u` is `floor(u)+1`.

It also has arbitrarily remote high-degree mergers and splits. Since

\[
W(0)=\frac1{1-2^{-1/2}}>0
\]

and, because `2^m mod 3` alternates between `1` and `2`,

\[
W(1/3)
=-\frac1{2(1-2^{-1/2})}<0,
\]

there is `r_* in (0,1/3)` with `W(r_*)=0`. Periodicity yields merger ages

\[
u_n=e^{r_*+n}-1\to\infty,
\]

at which `F(u_n)=0` and **all** currently active branches coalesce at the single point `x=0`; the merger degree is `floor(u_n)+1->infinity`.

At the split ages

\[
v_n=e^n-1,
\]

we have `W(n)=W(0)` and therefore

\[
F(v_n)=\sqrt{v_n}\,W(0)\to\infty.
\]

The active branch values `0,F(v_n),2F(v_n),...,floor(v_n)F(v_n)` are pairwise separated by a gap tending to infinity, while their number also tends to infinity.

Finally, Shen’s theorem gives

\[
\dim_H\operatorname{graph}(W)=3/2.
\]

On every fixed logarithmic slab bounded away from the origin, the map

\[
(r,y)\mapsto(e^r-1,\,k\sqrt{e^r-1}\,y)
\]

is bi-Lipschitz for fixed `k>=1`. Consequently each nonzero branch of (9.5) is itself a critical rough graph of Hausdorff dimension `3/2` (and the direct `1/2`-Hölder estimate gives the matching upper bound).

## 10. Why this is a genuinely new metric family

Point 41 is not a parameter recoding of run 40. Run 40 had a **globally fixed finite number** of critical sheets. Here the global family is countably infinite and the number of simultaneously active sheets grows without bound, while every compact age window still sees only finitely many. Brownian rescaling, reflection, and constant translation preserve the finite-versus-unbounded local branch-count distinction; they cannot turn (9.5) into a fixed finite web.

It is also distinct from:

- run 34’s countably accumulating BV web: those branches have summable finite variation on compacts and may be infinitely active at one time; the present nonzero branches are critical `1/2`-Hölder fractal graphs of dimension `3/2`, and the mechanism is local finiteness rather than a variation budget;
- run 38’s proliferating positive-width braided ribbon forest: that result is an entropy/Gaussian-hit argument for regions with interior and a quantitative growth condition; T47 is zero-width, critical-rough, and imposes **no quantitative upper rate at all** on branch proliferation, only compact-time local finiteness;
- run 39’s strict Hausdorff-dimension barrier: that theorem is silent at dimension `3/2`, exactly where every nonzero branch here lives.

The exact countable affine counterexample in Section 4 also shows that this distinction is mathematically necessary, not just nomenclature: unrestricted countable critical webs can support selectors rougher than the finite-web modulus argument permits.

Metric after this run: **41**.  
Unchanged count after this run: **0**.

## 11. Validation, audits, and honest status

There is no finite arithmetic/combinatorial core in T47/T48, so I did **not** manufacture an exact-arithmetic checker merely to create an artifact. The theorem-sized claim has a full written proof on this page. Proposition 4.1 is an exact symbolic construction and its decisive ratio is computed explicitly.

Independent OTHER-track audits for the new theorem: **0/2**. In particular, neither a P26 source-level audit nor a second distinct OTHER-track full-proof audit has yet been obtained. Therefore the source is **not closed** under Section G.

Honest source label: **PARTIAL**.  
New theorem labels: `I0077-R07-T47`, `I0077-R07-T48`.  
Publication novelty: **UNVERIFIED**.  
No paper folder is created before the required audits.

## 12. Next mathematical frontier

T47 identifies the correct boundary sharply. Local finiteness can now be dropped only by controlling how many sheets can participate **at the Brownian resolution scale** inside a compact time window. Proposition 4.1 shows that unrestricted accumulation defeats a uniform critical-Hölder selector bound.

The next route should therefore quantify the restricted intersection-graph complexity. If `N(delta)` bounds the number/chain complexity of sheets distinguishable on a time interval of length `delta`, the natural comparison is with Brownian’s endpoint modulus

\[
\sqrt{\delta\log(1/\delta)}.
\]

A theorem of the schematic form

\[
N(\delta)\,L(\delta)=o(\sqrt{\log(1/\delta)})
\]

for a suitable critical-sheet complexity `L(delta)` would extend T47 to genuinely infinitely active compact windows. That would no longer follow from local finiteness and would be a new entropy/geometry frontier rather than another finite reduction.

## 13. Model / scheduler-control status

The requested first-line model string remains prompt-only. The exposed task-control schema provides title/prompt, schedule or start-offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution control, and no authenticated completed-run model telemetry**. Therefore I cannot truthfully claim GPT-6 maximum.

The repository’s current RESULTS record also clarifies the historical P26 `You cannot modify this task` issue: P26 was later successfully updated from a different authorized context, so that denial was authorization-context-specific rather than a permanent mathematical/task failure. The legitimate route for any still-denied task is the owning/authorized account or workspace context, an authorized ownership/admin change, or platform support. A repository edit, duplicate job, or permission bypass is not a scheduler repair. This run was explicitly prohibited from scheduler changes, and none were attempted.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260918T0925Z_i0077_locally_finite_critical_forests_41_lf41
  source:
    authors: Krzysztof Burdzy; Michael Scheutzow
    work: Forward Brownian Motion
    arxiv: 1302.6958
    locator: Problem 7.8
    intake: I0077
  target: generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families
  fixed_metric: number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem under the frozen equivalence convention
  before: 40
  after: 41
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [2, 7, 19]
  new_claims:
    - I0077-R07-T47: locally finite critical-Hölder-forest obstruction
    - I0077-R07-T48: proliferating critical Weierstrass forest corollary
    - Proposition 4.1: unrestricted countable affine-selector extension is false
  source_status: PARTIAL
  claim_status_shared: PENDING_ADMISSION, not READY
  ownership: R07 exclusive provisional reservation; C29 exclusion rechecked; R15 owns distinct 7.2 history
  prior_art_search: bounded fresh 2026-09-18 search; no accessible exact later resolution found; novelty UNVERIFIED
  finite_checker_required: false
  independent_other_track_audits: 0/2
  paper_package: not created; closure requirements unmet
  shared_roots_modified: false
  peer_files_modified: false
  old_kpz_handoff_preserved: true
  scheduler_modified: false
```
