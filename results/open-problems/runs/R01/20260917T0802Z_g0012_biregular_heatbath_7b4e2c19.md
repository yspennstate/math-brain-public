Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so GPT-6 maximum is not claimed. **NO METRIC MOVEMENT: `alpha_univ = 1 -> 1`; G0012 unchanged count = 2. Section-B methods actually used: #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE.**

# R01 — G0012 Alon–Peres non-backtracking birthday conjecture — degree-free biregular theorem

Repository/branch: `yspennstate/math-open-problems` / `master`. Private GitHub only.

## 1. Continuity, exclusions, source, and metric

I continued from the newest complete R01 report

`runs/R01/20260917T0700Z_g0012_plan_irregular_9f31c2a7.md`,

not from either retired R01 source.

- `I0024` / Aldous–Fill Open Problem 3.44 remains **PROVED / INTERNAL-CLOSED** at exact distortion `C=1`, with its exact right-inverse flow formula, finite certificates, and distinct R20 and P26 PASS audits. It was not reopened.
- `I0113` / Salez Problem 2.7 remains **PARTIAL / PROVED-CANDIDATE / ROTATED** after its six-run gate at `M_3=3/3`. It was not reopened.
- `G0012` remains the create-only exclusive R01 successor under `operations/claims/G0012.md`.

Before research I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current owner directive, the G0012 claim, the newest own report, and the newest R02 neighboring report. The newest R02 package located is still an **OPEN / PARTIAL** I0095 discrepancy report, not a complete neighboring closure package, so no audit budget was spent.

### Source and current-literature refresh — 2026-09-17

Primary source: Benjamin Dozier, **“The Birthday Paradox for non-backtracking walks on regular graphs”**, arXiv:2608.26321v1 (26 August 2026), Conjecture 1.5. The source works with simple undirected graphs and states:

> for every `epsilon>0`, is there `C=C(epsilon)` such that every `n`-vertex graph of minimum degree at least `3`, every starting oriented edge, and every `k>C sqrt(n)` has simple-NBW probability below `epsilon`?

Dozier proves the fixed-`d` regular case. I checked the current arXiv abstract and PDF on 2026-09-17. The PDF still states Conjecture 1.5 in that unrestricted minimum-degree form and the proof still carries degree dependence through the regular-plan deviation count and the final reverse multiplicity `R_d(L+1)`.

Fresh bounded searches on 2026-09-17 included:

- `Benjamin Dozier Birthday Paradox non-backtracking walks regular graphs arXiv 2608.26321 Conjecture 1.5`;
- `Bencs Goldberg Jenssen Jerrum Pete Regts Yin non-backtracking self-intersection arXiv 2608.09729`;
- `"The Birthday Paradox for non-backtracking walks on regular graphs" citations follow-up`;
- `"Conjecture 1.5" "non-backtracking" birthday`;
- `"non-backtracking" "biregular" birthday walk`;
- `"Alon Peres" biregular non-backtracking birthday`.

The relevant neighboring primary paper remains Bencs–Goldberg–Jenssen–Jerrum–Pete–Regts–Yin, arXiv:2608.09729 (10 August 2026): fixed maximum degree gives `O(sqrt(n) log n)` expected self-intersection time, while regular uniform expanders give `O(sqrt(n))`. No later source-matching resolution of Conjecture 1.5 and no direct prior-art hit for the biregular theorem below surfaced in this bounded search. **This is not a novelty or priority certificate.** Noga Alon’s older draft on the birthday paradox was also surfaced; it does not supply the unrestricted square-root statement.

### Fixed metric

The frozen source-domain metric remains

`alpha_univ` = the smallest `alpha in [1/2,1]` for which R01 has a complete rigorous proof, uniformly over **all** minimum-degree-3 source graphs, that `k > C_epsilon n^alpha` forces simple-NBW probability below `epsilon`.

Before: `1`. After: `1`. **No movement.**

The theorem proved below is a genuinely irregular, unbounded-degree partial result, but it is restricted to bipartite biregular graphs and therefore does not move the frozen unrestricted metric.

---

## 2. Input retained from the previous run

For any graph, at each vertex `v` choose independently a uniform derangement `pi_v` of its incident neighbors. On incoming edge `(u,v)`, the plan exits along `(v,pi_v(u))`. The previous run proved that for every fixed simple path the plan probability is exactly the corresponding NBW probability, because its internal vertices are distinct and

\[
P(\pi_v(u)=w)=\frac1{d(v)-1}.
\]

Therefore

\[
\boxed{
P_{\rm plan}(\text{first }k\text{ edges simple})
=
P_{\rm NBW}(\text{first }k\text{ edges simple}).
}
\tag{2.1}
\]

For a `k`-simple base plan `rho` with path `v_0,...,v_k`, define

\[
W(\rho)=\sum_{i=1}^{k-1}(d(v_i)-2).
\tag{2.2}
\]

This is the number of raw deviations `(i,beta)`: at index `i`, there are `d(v_i)-2` outgoing non-backtracking choices different from the plan’s actual continuation.

The previous run also isolated the naive irregular obstruction: non-returning `L`-simple deviation trajectories have disjoint final `L` oriented edges, so there are at most `2m/L` of them. Dividing by `W(rho)` gives only

\[
\frac{2m}{L W(\rho)},
\tag{2.3}
\]

which is useless if the base path stays in a sparse region while the graph has a huge dense reservoir.

This run attacks exactly that obstruction and the degree-dependent reverse multiplicity in Dozier’s Lemma 2.3.

---

## 3. Method #11 — DUALIZE: a reversible heat-bath deviation removes the `R_d` multiplicity loss

Fix a vertex of degree `d>=3`. Let `D_d` be the set of derangements of its `d` incident neighbors, and write

\[
R_d=|D_d|,
\qquad
R'_d=\#\{\pi\in D_d:\pi(a)=c\}
\]

for any fixed `a` and any fixed `c ne a`. By symmetry,

\[
R_d=(d-1)R'_d.
\tag{3.1}
\]

Suppose the current local derangement is `pi`, the used incoming label is `a`, and `b=pi(a)`. Instead of replacing the whole local derangement by one deterministic contingency, define the following changed-image heat bath:

1. choose `c` uniformly from the `d-2` labels in `V\{a,b}`;
2. choose `pi'` uniformly from the `R'_d` derangements satisfying `pi'(a)=c`.

For two local derangements `pi,pi'` with `pi'(a) != pi(a)`, the transition probability is exactly

\[
K_a(\pi,\pi')=rac1{(d-2)R'_d}.
\tag{3.2}
\]

This is symmetric in `pi,pi'`. Moreover, for each `pi` there are `(d-2)R'_d` targets, so the row sum is one. Thus:

### Lemma 3.1 — local heat-bath reversibility

The changed-image heat-bath kernel is reversible with respect to uniform measure on `D_d`.

This is the useful dualization: a deviation can now be viewed as one step of a symmetric Markov kernel on plan space rather than as a many-to-one deterministic map whose reverse multiplicity costs a factor `R_d`.

There is no hidden walk dependence in the unused entries of `pi'`: until the altered trajectory revisits this vertex, only the value `pi'(a)=c` matters. If it revisits the vertex, the altered walk is already non-simple. Hence the classification of a deviation as `L`-simple depends on the selected changed image `c` and subsequent plan coordinates, not on the other values of the resampled derangement.

This observation will let the incoming probability of all possible simple sources at one deviation index sum to `(d-2)/W`, with **no factor `R_d`**.

---

## 4. Methods #15 and #25 — break regular symmetry, then double-count by edge balance

I deliberately moved to the most basic genuinely irregular class for which the global packing denominator can still be understood exactly.

Let `G=(A,B,E)` be an `n`-vertex simple bipartite `(a,b)`-biregular graph:

- every vertex in `A` has degree `a>=3`;
- every vertex in `B` has degree `b>=3`.

The degrees `a,b` may grow with `n` and their ratio may diverge. No fixed maximum degree is assumed.

Let `x=|A|`, `y=|B|`, and `m=|E|`. Edge balance gives

\[
xa=yb=m,
\qquad
n=x+y=m\left(\frac1a+\frac1b\right),
\]

hence

\[
2m=\frac{2nab}{a+b}.
\tag{4.1}
\]

Along **every** simple path the internal degrees alternate between `a` and `b`. Therefore the deviation count `W(rho)` depends only on the path length and starting parity, not on the particular simple plan. Write this common value as `W`.

For `k>=4`, among the `k-1` internal vertices each side occurs at least `(k-2)/2` times up to the harmless parity rounding. Thus

\[
W
\ge
\frac{k-2}{2}(a+b-4)
\ge
\frac{k}{4}(a+b-4).
\tag{4.2}
\]

Combining (4.1) and (4.2),

\[
\frac{2m}{W}
\le
\frac{8nab}{k(a+b)(a+b-4)}.
\]

Since `ab <= (a+b)^2/4` and `(a+b)/(a+b-4)<=3` for `a,b>=3`,

\[
\boxed{
\frac{2m}{W}\le\frac{6n}{k}.
}
\tag{4.3}
\]

This is the key double count. The dangerous global `m` from the previous run cancels against the equally large number of available deviations along a biregular path. It does so with an absolute constant independent of `a`, `b`, and `a/b`.

---

## 5. Degree-free version of Dozier’s bad-deviation lemma on the biregular class

Fix a `k`-simple base plan and an integer `L>=1`. A raw deviation class means a pair `(i,c)`, where `i` is an internal path index and `c` is one of the `d(v_i)-2` changed outgoing images. As in Dozier, call such a deviation `L`-simple if the altered walk remains simple for `L` steps after deviation.

There are exactly `W` raw deviation classes.

### 5.1 Non-returning `L`-simple classes

If two non-returning deviations are both `L`-simple, their last `L` oriented edges are disjoint: the plan is injective, so a shared oriented edge would force the same backward plan history and hence a return to the base path. There are `2m` oriented edges. Therefore

\[
N_{\rm nonreturn,L-simple}\le\frac{2m}{L}.
\]

By (4.3), their fraction among all raw classes is at most

\[
\boxed{
\frac{N_{\rm nonreturn,L-simple}}W
\le \frac{6n}{Lk}.
}
\tag{5.1}
\]

Hence if

\[
L\ge\frac{48n}{k},
\tag{5.2}
\]

this fraction is at most `1/8`.

### 5.2 Returning to the initial endpoint

A deviation that returns to a vertex of the base path at or before its departure index is already non-`L`-simple, exactly as in Dozier’s case split.

### 5.3 Returning to the final endpoint

For the exceptional final-endpoint case, at most `d(v_k)-1` changed outgoing images can give that endpoint. Since `d(v_k)<=max(a,b)<=a+b`, (4.2) gives

\[
\frac{d(v_k)-1}{W}
\le
\frac{4(a+b)}{k(a+b-4)}
\le
\frac{12}{k}.
\tag{5.3}
\]

Thus for `k>=96` this exceptional fraction is at most `1/8`.

### 5.4 Middle-returning classes: excursion reversal is degree-blind

For a middle-returning deviation, take the first return of its altered walk to the base path. Apply Dozier’s excursion-reversal operation: invert the local derangement at each interior excursion vertex and make the corresponding return-vertex contingency. This operation is an involution on the raw deviation classes.

The regularity of the graph is not used in the involution itself. At a vertex of any degree `d>=3`, the inverse of a derangement is again a derangement, and inversion preserves the uniform local plan measure. The path is bipartite but the reversed excursion visits the same vertices, so all local degrees match exactly.

As in Dozier’s argument, the two members of a middle-returning reversal pair cannot both be `L`-simple: if the original return hits a base-path vertex no later than the departure point then the original is already non-simple; if it returns later and the original is `L`-simple, the reversed excursion forces the reversed deviation to hit the departure vertex within the relevant window. Therefore at most half of the middle-returning raw classes are `L`-simple.

Combining (5.1), (5.3), and the reversal pairing gives:

### Lemma 5.1 — absolute bad-deviation fraction

If

\[
k\ge96,
\qquad
L\ge48n/k,
\]

then at least `1/4` of all `W` raw deviation classes of every `k`-simple plan are not `L`-simple.

Indeed, at most `1/8` are non-returning and `L`-simple; among returning classes the final-endpoint exceptional part is at most `1/8`, and at most half of the remainder can be `L`-simple. The resulting upper bound on all `L`-simple classes is at most `3/4`.

---

## 6. Restrict deviations to occur early enough to force a `k`-step self-intersection

To turn Lemma 5.1 into a comparison of `k`-simple and non-simple plans, only use departure indices

\[
i\le k-1-L.
\]

At most the final `L` indices are discarded. Their total raw weight is at most

\[
L\max(a-2,b-2)\le L(a+b).
\]

By (4.2), the discarded fraction is at most

\[
\frac{L(a+b)}W
\le
\frac{4L(a+b)}{k(a+b-4)}
\le
\frac{12L}{k}.
\tag{6.1}
\]

If

\[
L\le k/96,
\tag{6.2}
\]

then the discarded fraction is at most `1/8`. Since Lemma 5.1 gives at least `1/4` bad raw classes before the restriction, at least

\[
\boxed{1/8}
\tag{6.3}
\]

of the total raw deviation mass consists of **early bad** classes. Every early bad class produces a plan whose associated walk has self-intersected by time `k`.

---

## 7. Heat-bath reverse bound: no degree constant survives

Let `S` be the set of `k`-simple plans with the fixed starting edge, and `T` all plans with that starting edge. From each `rho in S`, make a proposal as follows:

1. choose one of its `W` raw deviation pairs `(i,c)` uniformly;
2. at the departure vertex, resample the local derangement uniformly conditional on sending the used incoming label to `c`.

By (6.3), at least `1/8` of the proposal probability from each `rho in S` lands in `T\S`, provided (5.2), (6.2), and `k>=96` hold.

Now fix a target plan `rho' in T\S` and let `j` be the first index at which its associated walk is non-simple. If `rho'` is an early bad proposal from a simple source `rho` at index `i`, then necessarily

\[
j-L\le i\le j.
\tag{7.1}
\]

Reason: if `i>j`, source and target agree through the first collision, contradicting simplicity of the source; if `i<j-L`, then the target remains simple for more than `L` steps after departure, contradicting that the proposal was bad.

Fix one candidate index `i` in (7.1), of degree `d_i`. For any exact source local derangement and exact target local derangement, the proposal probability is

\[
\frac{1}{W R'_{d_i}}.
\tag{7.2}
\]

How many source local derangements can feed this exact target at this fixed index? The source used image can be any of the `d_i-2` values other than the target changed image and the forbidden backtracking image, and for each such used image there are exactly `R'_{d_i}` source derangements. Therefore, after summing over **all** possible simple sources at this index, the incoming proposal probability is at most

\[
\frac{(d_i-2)R'_{d_i}}{W R'_{d_i}}
=
\frac{d_i-2}{W}.
\tag{7.3}
\]

This is where the heat-bath dualization cancels the derangement number exactly.

There are at most `L+1` candidate indices from (7.1), so the total incoming early-bad proposal mass to a fixed `rho'` is at most

\[
\frac{(L+1)\max(a-2,b-2)}W
\le
\frac{12(L+1)}{k}.
\tag{7.4}
\]

Summing proposal mass in two ways now gives

\[
\frac{|S|}{8}
\le
|T\setminus S|\frac{12(L+1)}k.
\]

Hence

\[
\boxed{
\frac{|S|}{|T|-|S|}
\le
\frac{96(L+1)}k.
}
\tag{7.5}
\]

In particular,

\[
\frac{|S|}{|T|}
\le
\frac{96(L+1)}k.
\tag{7.6}
\]

By the exact variable-degree plan representation (2.1), the left side is exactly the probability that the length-`k` NBW is simple.

---

## 8. A universal square-root theorem for bipartite biregular graphs

Choose

\[
L=\left\lceil\frac{48n}{k}\right\rceil.
\tag{8.1}
\]

If `k>=n`, the simple-walk probability is zero, so suppose `k<n`. Then `n/k>1`, and

\[
L\le \frac{49n}{k},
\qquad
L+1\le\frac{50n}{k}.
\tag{8.2}
\]

If

\[
k^2\ge4704n,
\tag{8.3}
\]

then `49n/k <= k/96`, so the upper restriction (6.2) also holds. Since a simple graph of minimum degree at least three has `n>=4`, (8.3) also makes `k>=96`, so all previous estimates apply.

Substituting (8.2) into (7.6) yields

\[
\boxed{
P(\text{length-}k\text{ NBW is simple})
\le
4800\,\frac{n}{k^2}
}
\tag{8.4}
\]

for every bipartite `(a,b)`-biregular simple graph with `a,b>=3`, every starting oriented edge, and every `k` satisfying (8.3). The constants are intentionally loose.

Therefore:

### Theorem 8.1 — degree-free birthday paradox for bipartite biregular graphs

For every `epsilon in (0,1)` and every simple bipartite `(a,b)`-biregular `n`-vertex graph with `a,b>=3`, with **no upper bound on `a`, `b`, or their ratio**, every starting oriented edge satisfies

\[
k>\sqrt{\frac{4800}{\epsilon}}\sqrt n
\quad\Longrightarrow\quad
P(\text{length-}k\text{ NBW is simple})<\epsilon.
\tag{8.5}
\]

If `k>=n`, the conclusion is trivial; otherwise (8.5) implies (8.3) and (8.4).

This includes arbitrary-degree regular bipartite graphs as the special case `a=b=d`, with a constant independent of `d`. More importantly, it includes genuinely irregular families with `a/b -> infinity` or `b/a -> infinity`.

### What this proves about the obstruction

**Degree imbalance by itself is not the missing phenomenon.** The previous run already ruled out complete bipartite graphs as a counterexample. Theorem 8.1 now shows that even arbitrary sparse/dense biregular alternation obeys the correct square-root birthday law with an absolute constant.

The real unrestricted obstruction is pathwise: in a general graph a simple trajectory can spend a long time in vertices of small excess degree `d(v)-2` while a remote dense reservoir makes `m` huge. Then `W(rho)` can be much smaller than `k m/n`, and the deterministic biregular cancellation (4.3) disappears.

A useful extremal diagnostic is therefore not “large degree ratio” but

\[
\frac{m}{W(\rho)}
\]

under the **simple-plan measure**. The next proof should either show that plans with abnormally large `m/W(rho)` already have exponentially small total mass, or replace global edge packing by local reachable volume.

---

## 9. Method #15 stress test: sparse corridor plus dense reservoir

To break the symmetry as hard as possible, I examined the qualitative extremal geometry suggested by (2.3): a long sparse minimum-degree-three corridor joined through a narrow gateway to a very dense core. A simple path can then have

\[
W(\rho)\asymp k
\]

while the graph has `m` of much larger order, so the old global-packing inequality is maximally bad.

This does **not** yet give a counterexample. A walk that remains in the sparse corridor must repeatedly make restricted forward choices, while entering the dense core supplies many alternatives but also enormous collision opportunity. I found no source-valid family in this geometry whose simple probability stays bounded away from zero for `k/sqrt(n)->infinity`.

I do not promote that observation to a theorem. Its value is diagnostic: the next attack should target the measure of low-`W` simple paths, not degree ratio in isolation.

---

## 10. Why there is no checker this run

There is no finite enumeration claim in Theorem 8.1. The proof is analytic and all constants are derived on the page. An exact-arithmetic checker would only replay elementary inequalities and would spend the run on certificate production rather than the new route. Under the 90/10 rule, no artifact was manufactured.

The theorem is marked **PARTIAL** relative to Conjecture 1.5 because it treats a restricted graph class. It does not move `alpha_univ`.

---

## 11. Neighbor audit budget

The newest complete R02 report recovered is still

`runs/R02/20260917T045029Z_5c7a9d31.md`,

with source status **OPEN / PARTIAL** on I0095 and metric still `7/sqrt(17)`. Its all-order-24-Hadamard result and cyclic-22 exclusion are interesting finite partial results, but the package is not a complete neighboring closure/paper package. I therefore supplied no second audit.

---

## 12. Next three genuinely different methods

Do not repeat `#11/#15/#25` next run.

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** choose deviations with weight `(d(v_i)-2)^theta` rather than raw uniform weight, and optimize `theta`. The goal is to make both the non-returning packing term and the reverse heat-bath mass depend on a common degree moment, potentially eliminating `m/W(rho)` on arbitrary graphs.
- **#12 FIND WHAT IS CONSERVED:** exploit the uniform stationary measure on oriented edges and edge-flux conservation to relate the simple-plan average of `sum_i(d(v_i)-2)` to a local reachable-volume quantity. The target is an averaged replacement for deterministic biregular identity (4.3).
- **#24 FIND THE EXTREMAL OBJECT:** formulate the worst degree profile/path profile for the heat-bath double count as an optimization problem under undirected edge-balance constraints. If the extremizer is a sparse corridor plus dense reservoir, prove that geometry itself forces a collision; if not, identify the true extremal profile.

This is unchanged run 2 on G0012, so the section-I stuck protocol has not yet fired.

---

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  source: "Benjamin Dozier (2026), arXiv:2608.26321, Conjecture 1.5 (Alon-Peres)"
  intake: G0012
  metric_name: alpha_univ
  metric_before: 1
  metric_after: 1
  metric_direction: smaller_is_stronger
  movement: no
  unchanged_count: 2
  status: "OPEN / PARTIAL"
  tried_moves: [11, 15, 25]
  new_partial_result: "Universal degree-free sqrt(n) birthday bound on all simple bipartite (a,b)-biregular graphs with a,b>=3: P(simple)<=4800 n/k^2 for k^2>=4704 n."
  remaining_obligation: "Extend the heat-bath/local-packing argument to every minimum-degree-3 graph, improve alpha_univ below 1 and ultimately to 1/2, or produce a source-valid counterexample. The exact obstruction is low pathwise excess-degree W(rho) relative to global edge volume, not degree ratio itself."
  evidence:
    - "operations/claims/G0012.md"
    - "runs/R01/20260917T0700Z_g0012_plan_irregular_9f31c2a7.md"
    - "Dozier arXiv:2608.26321 source/PDF checked 2026-09-17"
    - "Bencs et al. arXiv:2608.09729 checked 2026-09-17"
  audit_ids: []
```

## 14. Model / scheduler escalation status

The model-control limitation remains unchanged in this runtime. The exposed task-management surface provides prompt/title/schedule/timing/enabled-state controls but no authenticated model selector, reasoning-effort selector, completed-run model telemetry, or guaranteed full-hour execution control. GPT-6 maximum can therefore be requested in prompt text but cannot be enforced or verified here.

The historical `You cannot modify this task` event on one P26 management context is an authorization-context boundary. The lawful workaround is an owner-authorized management context or platform/support ownership migration; duplicate jobs or permission bypass are not valid workarounds.

No scheduler change, email, Drive action, public posting, purchase, permission change, shared-root edit, or peer-track edit was performed.