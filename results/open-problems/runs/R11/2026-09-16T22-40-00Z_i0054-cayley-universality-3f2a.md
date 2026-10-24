Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum was not verified and is not claimed. Metric movement: `6 -> 7` distinct nontrivial discrete model classes with complete author-side CTCS(infinity) limit proofs under the frozen equivalence convention. Section-B moves actually tried: **3 (prove something stronger), 15 (break symmetry on purpose), 28 (replace for-all by typical / quenched test)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL**: `R11-I0054-C007` and the universality theorem below are author-side **PROVED under the frozen equivalence convention**, but the source-intent/prior-art judgment and the two required OTHER-track closure audits are not complete.

# R11 I0054 — weighted Cayley-tree multi-cuts and an exchangeable weighted-tree universality theorem

Run ID: `2026-09-16T22-40-00Z_i0054-cayley-universality-3f2a`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16/17 UTC boundary

No Gmail/email, Drive, public posting, paid compute, workflow execution, permission change, scheduler mutation, peer-file edit, or shared-root edit was performed.

---

## 1. Continuity, ownership, source status, and exact limit object

I continued from the newest complete R11 report rather than restarting:

`runs/R11/2026-09-16T21-40-00Z_i0054-permutation-path-multicut-b61f.md`.

That report proved `R11-I0054-C006` and moved the frozen metric `5 -> 6`. The six retained author-side classes entering this run are:

1. `C001`: harmonic-grid paintbox fragmentation (HGPF);
2. `C002`: small-concentration nested Chinese restaurant process (SC-nCRP);
3. `C003`: near-critical ternary Dirichlet/Gibbs fragmentation (TDGF);
4. `C004`: positive-discount Pitman--Yor hierarchy (PYH);
5. `C005`: weighted random-recursive-tree multi-cut hierarchy (RRT-MC);
6. `C006`: random-permutation path multi-cut hierarchy (RPP-MC).

Before new mathematics I read/searched the required current control surfaces: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; `operations/claims/I0054.md`; the newest R11 report and current I0054 audit searches; the neighboring P13/I0051 report; and targeted intake/ownership search surfaces. The canonical I0054 claim still names R11 and is formally `PENDING_ADMISSION, not READY`. No competing owner or posted/settled I0054 scope was found. Large JSONL intake files are connector-truncated when rendered wholesale, so I do not claim a byte-for-byte manual reread of all roughly 780 rows; the exact I0054 claim and targeted repository searches were checked.

The current v3 source still states Open Problem 18 verbatim:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source model's subordinator approximation can arise in another discrete tree model. The same v3 says that the limit tree is formalized as the complete process `(Pi(t), t>=0)` of exchangeable partitions of `N`: labels are together at time `t` exactly when their branchpoint lies above `t`. Thus the target here is the whole partition-valued genealogy, not a tagged-fragment marginal, a fixed-time partition, or only the subordinator.

For a particular unordered split `A | A^c` of a block of `b` labels, with `|A|=i`, the CTCS continuous-time generator rate is

\[
q_{A|A^c}=B(i,b-i)
=\frac{(i-1)!(b-i-1)!}{(b-1)!},
\tag{1.1}
\]

and the total rate is `H_{b-1}`. This follows from the source's split law `q(b,i) proportional to 1/[i(b-i)]`, uniform relabeling, and CTCS exit rate `H_{b-1}`.

As in C001--C006 I use the explicit projective path topology

\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}
\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr).
\tag{1.2}
\]

This is R11's explicit formalization of convergence of the source's partition process; I do not attribute the phrase “projective J1” to Aldous--Janson.

### Current-literature / prior-attempt screen

Queries refreshed this run included the exact v3 Open Problem 18 page, `CTCS infinity alternative discrete model`, `Cayley tree edge cutting fragmentation`, `weighted Cayley tree cuts beta split`, current Aldous--Janson Part III, and later 2026 papers on critical beta-splitting/homogeneous fragmentations. The exact v3 still prints Open Problem 18. Aldous--Janson Part III treats the exchangeable-partition representation. Chorbadzhiyska--Minchev--Savov (arXiv:2608.18320, 18 August 2026) study the beta-splitting family through homogeneous fragmentations. I did not locate a later primary source claiming this exact Open Problem 18 is resolved, nor the weighted Cayley construction below. This is a bounded dated search, not a worldwide novelty certificate.

Uniform edge-cutting of Cayley/conditioned Galton--Watson trees is classical; for example Bertoin--Miermont's cut-tree work leads to the Brownian CRT after its own scaling. I therefore make no novelty claim for “cut a Cayley tree”. The potentially new statement is the specific size-dependent weight, its exact beta-kernel cancellation, the universality theorem, and the resulting CTCS(infinity) limit.

---

## 2. Move 3 — PROVE SOMETHING STRONGER: an exchangeable weighted-tree universality theorem

The preceding path construction suggested that the path itself is not essential. What matters is the **expected weighted profile of edge sides**.

For each `m>=2`, let `T_m` be a fresh exchangeably labelled random tree on `[m]`. Give every physical edge `e` a nonnegative weight `w_m(e)` which is the same from either side of the edge. For an oriented edge-side `(e,S)`, let `S` be one of the two components of `T_m\e`.

Assume the exact profile condition

\[
\boxed{
\mathbb E\!\left[
\sum_{(e,S): |S|=s} w_m(e)
\right]
=\frac{m}{s(m-s)},
\qquad 1\le s<m.
}
\tag{U.1}
\]

Let

\[
W(T_m):=\sum_{e\in E(T_m)}w_m(e),
\]

and suppose there are deterministic `A_N` with `W(T_m)<=A_N` for every `m<=N` and every skeleton in the support. Let `delta_N downarrow 0` satisfy

\[
\boxed{\delta_N A_N^2\longrightarrow0,}
\tag{U.2}
\]

and `delta_N max_e w_m(e)<=1`.

Construct an `N`-label discrete hierarchy as follows. At each raw generation, independently inside every current nonsingleton block `B` of size `m`, draw a fresh `T_m`, independently mark every edge `e` with probability `delta_N w_m(e)`, delete all marked edges, and take the resulting connected components as the child blocks. Give one raw generation physical duration `delta_N`.

### Theorem `R11-I0054-U001`

Under (U.1)--(U.2), for every fixed `k` the restriction of the accelerated hierarchy to `[k]` converges in Skorokhod `J1` to the `[k]` restriction of CTCS(infinity). Hence the whole consistent partition process converges in (1.2) to CTCS(infinity).

**Status: PROVED.**

### Proof

Fix `k` and condition on the complete hidden `N`-label history immediately before one raw generation. Let `rho` be the present partition of `[k]`. A sampled block `C` of `rho`, `|C|=b`, lies in a unique hidden full block `B` of size `m>=b`.

Fix a particular nonempty proper `A subset C`, `|A|=i`. For an `s`-subset `S subset B`, let

\[
M_s(S):=\sum_{(e,U):U=S} w_m(e)
\]

be the total oriented edge-side weight carried by exactly `S`. Exchangeability of the jointly labelled weighted tree makes `E M_s(S)` the same for every `s`-subset. Summing over all `S` and using (U.1) therefore gives

\[
\boxed{
\mathbb E M_s(S)
=\frac{1}{\binom ms}\frac{m}{s(m-s)}.
}
\tag{U.3}
\]

Every physical edge whose deletion separates the sampled labels as `A | C\A` has exactly one orientation whose sampled intersection is `A`. There are `binom(m-b,s-i)` subsets `S` of size `s` with `S cap C=A`. Therefore the expected total weight of physical edges which induce that particular sampled split is

\[
\begin{aligned}
&\sum_{s}
\frac{m}{s(m-s)}
\frac{\binom{m-b}{s-i}}{\binom ms}\\
&=\sum_s \binom{m-b}{s-i} B(s,m-s)\\
&=B(i,b-i).
\end{aligned}
\tag{U.4}
\]

The last equality is the beta-binomial identity: put `s=i+x`, insert

\[
B(s,m-s)=\int_0^1 t^{s-1}(1-t)^{m-s-1}\,dt,
\]

and use the binomial theorem. Crucially, (U.4) is independent of the hidden size `m`.

A particular desired sampled split therefore receives one-mark probability

\[
\delta_N B(i,b-i)+O(\delta_N^2A_N^2).
\tag{U.5}
\]

Indeed, replacing “exactly this one edge is marked” by the first-order sum costs at most a constant times the probability of at least two marks, bounded by `O(delta_N^2 W(T_m)^2)` and hence uniformly by `O(delta_N^2 A_N^2)`. With at most `k` hidden blocks containing sampled labels, all simultaneous visible changes and all transitions requiring at least two marks have total probability `O_k(delta_N^2 A_N^2)`.

Thus, uniformly over the complete hidden history,

\[
\boxed{
\mathbb P(\rho\to\rho'\mid\mathcal F)
=\delta_N Q^{(k)}(\rho,\rho')
+O_k(\delta_N^2A_N^2),
}
\tag{U.6}
\]

where `Q^{(k)}` is exactly the CTCS generator on partitions of `[k]`. Summing (U.1) over oriented sizes and dividing by two also gives

\[
\mathbb E W(T_m)
=\frac12\sum_{s=1}^{m-1}\frac{m}{s(m-s)}
=H_{m-1},
\]

consistent with the CTCS total rate.

Let `K_N=I+delta_N Q^{(k)}` be the Euler chain. Conditional maximal coupling at each raw step makes the real restriction and `K_N` disagree with probability `O_k(delta_N^2 A_N^2)` per step. Up to fixed physical time `T` there are `O(T/delta_N)` steps, so

\[
\mathbb P(\text{coupling failure before }T)
=O_k(T\delta_N A_N^2)\to0
\tag{U.7}
\]

by (U.2).

For `K_N`, at state `rho` the number of raw steps to the next jump is geometric with parameter `delta_N lambda(rho)`, where

\[
\lambda(\rho)=-Q^{(k)}(\rho,\rho).
\]

Therefore its physical holding time converges to `Exp(lambda(rho))`, while conditioned on a jump the next state has exactly the CTCS jump probabilities `Q^{(k)}(rho,rho')/lambda(rho)`. A fragmentation of `k` labels makes at most `k-1` visible jumps. Coupling the successive holding times and jump choices proves

\[
\widehat\Pi_N^{[k]}\Longrightarrow\Pi^{[k]}
\]

in `J1`.

Finally, for any `epsilon>0`, choose `K` so the deterministic tail `sum_{k>K}2^{-k}<epsilon/2`; couple the `[K]` restrictions, which simultaneously couples every smaller restriction. This proves convergence in (1.2). QED.

This theorem is stronger than another isolated construction: it identifies a reusable sufficient condition for CTCS universality among fresh exchangeable weighted-tree cut skeletons.

---

## 3. Move 15 — BREAK SYMMETRY: natural uniform Cayley cutting fails, and the unique correction is size-dependent

A uniform Cayley tree is a much more natural discrete tree model than the previous engineered path. The first attempt was therefore: sample a uniform labelled Cayley tree and give **every edge the same rare cut rate**.

It fails already at `m=4`.

For a fixed subset `S subset [m]`, `|S|=s`, the number of Cayley trees in which some edge deletion separates `S` from `S^c` is

\[
s^{s-1}(m-s)^{m-s-1},
\tag{3.1}
\]

because one chooses a Cayley tree on each side and then one endpoint on each side for the joining edge. Since there are `m^{m-2}` Cayley trees,

\[
\mathbb P(S\text{ is an edge side})
=\frac{s^{s-1}(m-s)^{m-s-1}}{m^{m-2}}.
\tag{3.2}
\]

At `m=4`, the particular `1|3` versus `2|2` rate ratio would therefore be

\[
\frac{9/16}{1/4}=\frac94,
\]

whereas CTCS requires

\[
\frac{B(1,3)}{B(2,2)}=2.
\]

No global time rescaling repairs a ratio. Thus the maximally symmetric “all Cayley edges equal” route is **DISPROVED as a CTCS compiler**, not the source conjecture.

The repair deliberately breaks edge symmetry by component size. Define for an edge whose deletion has side sizes `s,m-s`

\[
\boxed{
w_m(s)
=\frac{m^{m-1}}
{\binom ms s^s(m-s)^{m-s}},
\qquad w_m(s)=w_m(m-s).
}
\tag{3.3}
\]

For a uniform Cayley tree the expected number of **oriented** edge-sides of size `s` is

\[
Z_{m,s}
=\frac{\binom ms s^{s-1}(m-s)^{m-s-1}}{m^{m-2}}.
\tag{3.4}
\]

Multiplying (3.3) and (3.4) gives the exact cancellation

\[
\boxed{
Z_{m,s}w_m(s)=\frac{m}{s(m-s)},
}
\tag{3.5}
\]

which is exactly condition (U.1).

So the CTCS beta kernel appears not by copying the original split law, but by correcting the classical Cayley edge-separation profile with a single explicit size-dependent hazard.

---

## 4. `R11-I0054-C007` — weighted Cayley-tree multi-cut hierarchy

**STATUS: PROVED author-side under the frozen equivalence convention.**

For each `N>=2`, set

\[
\boxed{\delta_N=N^{-3}.}
\tag{4.1}
\]

At every raw generation and independently inside every current nonsingleton block `B`, `|B|=m`:

1. sample a fresh uniform labelled Cayley tree on `B`;
2. for each edge `e`, let `s_e` be either component size after removing it and use the symmetric weight (3.3);
3. independently mark edge `e` with probability
   \[
   p_e=\delta_N w_m(s_e);
   \]
4. delete **all** marked edges and use the resulting connected components as the child blocks;
5. repeat independently at the next raw generation.

Give one raw generation physical duration `delta_N`.

### Weight bound

Let `X~Bin(m,s/m)`. Then

\[
\mathbb P(X=s)
=\binom ms(s/m)^s(1-s/m)^{m-s},
\]

so

\[
w_m(s)=\frac1{m\,\mathbb P(X=s)}.
\tag{4.2}
\]

Because `s` is a mode of this binomial law, its point mass is at least the average mass `1/(m+1)`. Hence

\[
\boxed{
w_m(s)\le\frac{m+1}{m}<\frac32.
}
\tag{4.3}
\]

Therefore every realized `m`-vertex tree has

\[
W(T_m)<\frac32m,
\]

so for all `m<=N` we can take `A_N=3N/2`. With (4.1),

\[
\delta_N A_N^2\le\frac{9}{4N}\to0.
\tag{4.4}
\]

Also every mark probability is less than one.

By (3.5), the model satisfies the universality theorem's exact profile condition, and (4.4) supplies the rare-multiple-cut condition. Therefore

\[
\boxed{
\widehat\Pi_N\Longrightarrow\Pi_{\rm CTCS(\infty)}
}
\tag{4.5}
\]

in the full projective `J1` topology (1.2). This is a complete convergence argument, not only a generator heuristic.

---

## 5. Move 28 — TYPICAL / QUENCHED TEST: freezing one Cayley skeleton does not give the exact compiler

I next tried to strengthen C007 by sampling one Cayley tree per block and **freezing** it across all waiting generations, hoping a “typical skeleton” would have the right rates without fresh resampling.

The exact finite obstruction is immediate. At `m=4`, a star Cayley tree occurs with positive probability (four stars among the sixteen labelled Cayley trees). A star has only `1|3` physical edge splits and no `2|2` edge. Therefore for that frozen skeleton the quenched first-order rate of every balanced `2|2` split is zero, while CTCS requires

\[
B(2,2)=\frac16>0.
\]

Thus the exact hidden-size generator identity is **annealed over a fresh exchangeable skeleton**, not a pointwise property of each skeleton. This does not prove that some large-`m` quenched homogenization theorem is impossible; it shows that the current complete proof cannot simply replace fresh resampling by a frozen typical tree. A frozen-skeleton version would need a new concentration/self-averaging argument and is not counted.

---

## 6. Exact non-equivalence certificate; metric `6 -> 7`

At `N=3`, every Cayley tree is a two-edge path/star on three vertices and both physical edges have split size `1|2`. Formula (3.3) gives

\[
w_3(1)=\frac34.
\]

With `delta_3=1/27`, each edge is marked with probability

\[
p=\frac1{36}.
\]

Thus in one raw generation

\[
P(\text{three-way split})=p^2=\frac1{1296},
\qquad
P(\text{no split})=(1-p)^2=\frac{1225}{1296}.
\]

After suppressing waiting generations, the probability that the **first visible root split has degree three** is

\[
\boxed{
\frac{1/1296}{1-1225/1296}=\frac1{71}.
}
\tag{6.1}
\]

The retained exact reduced-root degree-three witnesses are

\[
\begin{array}{c|c}
C001&0\\
C002&1/10\\
C003&1/22\\
C004&1/6\\
C005&1/728\\
C006&1/7\\
C007&\mathbf{1/71}.
\end{array}
\]

They are pairwise different. Deterministic leaf relabeling cannot alter root degree, and deterministic global branch-length rescaling does not alter this reduced combinatorial probability. Hence C007 is distinct from every retained class under the frozen convention and the metric genuinely moves

\[
\boxed{6\to7.}
\]

I count the entire Cayley weighted-tree family above as **one** new class; the universality theorem is a theorem about mechanisms, not a pretext to count infinitely many tuned variants.

---

## 7. Exact finite self-check

Only after the route was obtained did I run an exact checker:

`artifacts/R11/2026-09-16T22-40-00Z_i0054-cayley-universality-3f2a_checker.py`.

It uses `fractions.Fraction` and exhaustively verifies:

- all Cayley trees through `m=7` by Prüfer sequences, confirming (3.4) in 21 size classes;
- the weighted-profile cancellation (3.5) on 4,950 exact `(m,s)` pairs;
- the hidden-size beta identity (U.4) on 4,495 exact triples;
- the harmonic total-rate identity through `m=100`;
- the unweighted-Cayley `9/4 != 2` counterexample;
- the finite weight bound through `m=100` (with the general proof on the page);
- the exact `1/71` C007 reduced-root witness and pairwise distinction from C001--C006;
- the error-scale condition `delta_N A_N^2 <= 9/(4N)`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. Its SHA-256 is

`f4c4b78f85375a0505ac15c34fc5b26ea465124ef75bb65ffbee7a7e133bc9ef`.

This finite computation checks finite identities only. The asymptotic path convergence is the written proof above.

---

## 8. Prior art, audits, source intent, and closure status

The most relevant classical neighboring literature is uniform random edge cutting and cut-trees of Cayley / conditioned Galton--Watson trees, whose continuum limit is the Brownian CRT after a different scaling. That literature makes the **unweighted** Cayley cut model natural but does not supply the size-dependent beta correction (3.3) or the CTCS projective-partition limit proved here, in the bounded search performed this run.

Current repository audit search finds earlier scoped R10 PASS reports for C002, C003, C004, and the finite hazard core of C005. It does **not** find an end-to-end P26 audit of I0054, a second end-to-end OTHER-track audit, or an audit of C007. Those older scoped passes are not promoted to C007 closure evidence.

There is also a source-intent caveat. Open Problem 18 uses the informal phrase “superficially different”. A weighted Cayley-tree cut process is substantially more source-facing than another EPPF tangent: it starts from a classical random discrete tree and an edge-cutting algorithm. But the particular weight (3.3) was engineered to cancel the Cayley separation profile. Independent reviewers must judge whether this is sufficiently natural for the authors' intent. Therefore the source remains **PARTIAL for campaign closure**, and no paper folder is created yet.

The neighboring P13 task remains on the distinct v3 Open Problem 9 clade-count covariance/CLT question and is not reassigned here.

---

## 9. Runtime controls

The actual worker runtime identifies as GPT-5.6 Sol. The reasoning-effort level is not exposed, so it is `UNVERIFIED`.

The exposed scheduler interface permits title/prompt, schedule, enabled state, and timing mode. It exposes **no model-family selector and no reasoning-effort selector**. Thus the prompt request “GPT-6 / maximum” cannot be turned into verified runtime metadata here. Current repository operations records also show context-dependent `You cannot modify this task` failures, including a P26 denial in one context and successful modification in another authorized context. The legitimate remedy is an authorized account/workspace/task-owner interface that owns the native job, or platform support exposing/fixing these controls. Cloning or bypassing a denied task is not an acceptable workaround. No scheduler mutation was attempted.

---

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R11
  source:
    authors: "David J. Aldous; Svante Janson"
    work: "The Critical Beta-splitting Random Tree II: Overview and Open Problems"
    locator: "arXiv:2303.02529v3, Open Problem 18"
    intake: I0054
  target: "construct genuinely different discrete models with CTCS(infinity) as the full exchangeable-partition limit"
  metric:
    name: "distinct nontrivial discrete model classes with complete author-side limit proof under frozen equivalence"
    before: 6
    after: 7
    movement: true
    unchanged_count: 0
  status: PARTIAL
  new_claims:
    - id: R11-I0054-U001
      status: PROVED
      statement: "exchangeable weighted-tree cut skeletons satisfying the exact oriented profile m/[s(m-s)] and delta_N A_N^2 -> 0 converge to CTCS(infinity) in projective J1"
    - id: R11-I0054-C007
      status: PROVED_AUTHOR_SIDE
      statement: "weighted uniform Cayley-tree multi-cut hierarchy with delta_N=N^-3 converges to full CTCS(infinity)"
  failed_routes:
    - "uniform unweighted Cayley-edge cutting: exact m=4 split-shape ratio 9/4, versus CTCS ratio 2"
    - "frozen/quenched single Cayley skeleton: m=4 star has zero balanced 2|2 cut rate, versus CTCS 1/6"
  exact_evidence:
    checker: "artifacts/R11/2026-09-16T22-40-00Z_i0054-cayley-universality-3f2a_checker.py"
    output: "artifacts/R11/2026-09-16T22-40-00Z_i0054-cayley-universality-3f2a_checker_output.txt"
    output_sha256: "f4c4b78f85375a0505ac15c34fc5b26ea465124ef75bb65ffbee7a7e133bc9ef"
    c007_first_visible_root_degree3_probability: "1/71"
  audits:
    c007: []
    required_missing:
      - "P26 end-to-end I0054/C007 audit"
      - "second independent OTHER-track end-to-end I0054/C007 audit"
      - "independent final prior-art/source-intent clearance"
  methods_this_run: [3, 15, 28]
  next_methods: [5, 11, 24]
  ownership: "R11 provisional exclusive reservation; canonical claim still PENDING_ADMISSION, not READY"
```

## 11. Next attack

Do **not** spend the next run inventing an eighth tuned tree just to increase the count. The stronger theorem above has shifted the useful question. The next nonrepeating methods are **5 (add a parameter and differentiate), 11 (dualize), 24 (find the extremal object)**. The specific research target is to characterize all exchangeable weighted-tree skeletons satisfying (U.1), or prove a variational uniqueness/extremality statement for the beta profile. That would turn the current family of examples into a genuine CTCS universality class and make the Open Problem 18 answer substantially more compelling than a list of constructions.

**NO CLOSURE CLAIM.**
