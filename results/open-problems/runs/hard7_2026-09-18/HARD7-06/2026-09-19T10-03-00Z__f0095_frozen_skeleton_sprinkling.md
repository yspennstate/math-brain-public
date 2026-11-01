Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** **No movement:** `W_3: 0.656514 -> 0.656514`. Methods actually tried: **B3 / B18 / B20**.

# HARD7-06 run 14 — frozen-skeleton sprinkling: a deterministic route from cluster compression to the BGT exponential tail

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does not prove existence of the constant ordinary Erdős–Rényi 3-colourability threshold. It replaces the raw-colouring sprinkling obstruction from run 13 by a deterministic quotient theorem: if proper colourings admit a subexponential cover by linear-size common equality skeletons, then any linear edge sprinkling kills 3-colourability with exponentially high probability. An explicit sparse family proves that this quotient can succeed even when both the raw-colouring union bound and a raw VC-dimension route are exponentially useless.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and source status

I resumed the already admitted canonical target `F0095`, owned by HARD7-06 in `operations/claims/F0095.md`. I did **not** restart random 3-SAT: the owner prompt says later runs resume the admitted target, and the earlier CKS/random-3-SAT lifecycle was already exhausted and handed off before F0095 was admitted.

I reread the controlling HARD7 files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the canonical F0095 claim, the newest HARD7-06 checkpoint, and the neighbouring CSP ownership state. No canonical F0095 release, conflicting owner, posted equivalent, or settled campaign entry was found.

The exact source target remains Alan Frieze's ICM 2014 chromatic-number conjecture, with frozen small case `k=3`:

> **Conjecture:** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

For this track, F0095 means the existence of a **constant location** of the ordinary sparse Erdős–Rényi 3-colourability transition, not merely Achlioptas--Friedgut sharpness around an `n`-dependent threshold sequence.

### Bounded current-literature check, 2026-09-19

I rechecked the exact route rather than assuming the previous negative search remained current.

- Bayati--Gamarnik--Tetali, *Combinatorial approach to the interpolation method and scaling limits in sparse random graphs*, Ann. Probab. 41 (2013), DOI `10.1214/12-AOP816`, states that for colouring there is a sharp sequence `c_N^*`, proves existence of `lim N^{-1} log p(c,N)`, and isolates the missing strengthening: exponentially small colourability probability a fixed linear distance above the moving sharp threshold. Their Conjecture 1 says this exponential strengthening, together with their scaling-limit theorem, would imply the constant satisfiability/colourability threshold.
- Amin Coja-Oghlan, *Upper-Bounding the k-Colorability Threshold by Counting Covers*, EJC 20(3) (2013), DOI `10.37236/3337`, uses a physics-inspired **cover** count to improve the large-`k` non-colourability bound. This is prior art for quotienting raw colourings, but its theorem does not by itself supply the fixed-`k=3` conditional skeleton estimate formulated below.
- Michael Molloy, *The freezing threshold for k-colourings of a random graph*, STOC 2012, DOI `10.1145/2213977.2214060`, rigorously studies linear frozen-variable sets in random graph colourings. Its published abstract is close in shape to the needed object, but I did not recover from it the specific `q=3`, near-moving-threshold, exponentially-good **cover-number** estimate required below. I therefore do not cite it as closing this route.
- Mizgerd--Perkins--Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, first published 6 June 2026, DOI `10.1002/rsa.70081`, proves sharp scaling-window results for a **triangle-free conditioned model**. It is not the ordinary `G(n,d/n)` target.
- A bounded search for 2025--2026 ordinary `q=3` constant-threshold results again found no proof of F0095. This is bounded negative evidence, not a worldwide openness certificate.

No exact match for the deterministic frozen-skeleton sprinkling lemma below was found in the bounded search. Because cover/whitening/frozen-core mechanisms are established literature, I make **no global novelty claim** for the lemma without a deeper citation audit.

## 2. Frozen metric: no movement

The source-relevant quantity remains

\[
W_3=U_3-L_3.
\]

The verified endpoints carried from run 13 are

\[
L_3=4.03,
\qquad
U_3=4.686514,
\qquad
W_3=0.656514.
\]

The upper endpoint is the same-degree consequence of the already-certified strict Ayre--Coja-Oghlan--Greenhill variational witness. This run does not improve either endpoint, so

\[
\boxed{W_3:0.656514\longrightarrow0.656514\quad\text{(no movement).}}
\]

This is the first unchanged F0095 run after the preceding metric movement, so Section I is not triggered.

## 3. B18 — say it in another language: colour clusters as a hitting-set cover

Run 13 showed why sprinkling a linear number of edges is potentially powerful but why union-bounding over all proper colourings pays the internal entropy of each cluster. The right deterministic object is not a chosen clustering metric. It is a **cover by partial equality partitions**.

Let `G=(V,E)` be a 3-colourable graph on `n` vertices. Write

\[
U=\binom V2\setminus E,
\qquad
M=|U|=\binom n2-|E|.
\]

A **3-skeleton** is a pair `S=(K,pi)` where `K subseteq V` and `pi` is a partition of `K` into at most three cells. A proper colouring `sigma:V->{1,2,3}` **extends** `S` if for every `u,v in K`,

\[
\sigma(u)=\sigma(v)
\quad\Longleftrightarrow\quad
u,v\text{ lie in the same cell of }\pi.
\tag{3.1}
\]

The common forbidden-edge set of `S` is

\[
F(S)=\{\{u,v\}\subset K:u,v\text{ lie in the same cell of }\pi\}.
\tag{3.2}
\]

If a proper colouring extends `S`, then necessarily `F(S) subseteq U`.

For `0<=delta<1`, put

\[
K_\delta=\lceil(1-\delta)n\rceil
\]

and define the **frozen-skeleton cover number** `C_delta(G)` to be the least number of 3-skeletons `S_1,...,S_J`, each with `|K_j|>=K_delta`, such that every proper 3-colouring of `G` extends at least one `S_j`. This is always finite when `G` is colourable: one may take one full-vertex skeleton for each equality partition induced by a proper colouring.

For an integer `k>=0`, let

\[
B_3(k)=\min_{a_1+a_2+a_3=k}\sum_{i=1}^3\binom{a_i}{2}.
\tag{3.3}
\]

If `k=3a+r`, `r in {0,1,2}`, convexity gives the exact formula

\[
B_3(k)=r\binom{a+1}{2}+(3-r)\binom a2.
\tag{3.4}
\]

Thus every 3-skeleton on at least `K_delta` vertices has

\[
|F(S)|\ge B_3(K_\delta).
\tag{3.5}
\]

The entire cluster geometry is now a random hitting problem for the deterministic set family `F(S_1),...,F(S_J)`.

## 4. B3 — prove something stronger: deterministic exponential sprinkling from skeleton compression

Choose a uniformly random `t`-subset `T` of the missing-edge set `U` and write `G+T` for the graph after sprinkling.

### Proposition 4.1 — frozen-skeleton sprinkling inequality

For every 3-colourable graph `G`, every `0<=delta<1`, and every `0<=t<=M`,

\[
\boxed{
\mathbb P_T\{G+T\text{ is 3-colourable}\}
\le
\min\left\{1,
\mathcal C_\delta(G)
\frac{\binom{M-B_3(K_\delta)}{t}}{\binom Mt}
\right\}.}
\tag{4.1}
\]

The binomial numerator is interpreted as zero when `M-B_3(K_delta)<t`. In particular,

\[
\boxed{
\mathbb P_T\{G+T\text{ is 3-colourable}\}
\le
\min\left\{1,
\mathcal C_\delta(G)
\exp\left(-\frac{tB_3(K_\delta)}{M}\right)
\right\}.}
\tag{4.2}
\]

#### Proof

Take a minimum skeleton cover `S_1,...,S_J`, where `J=C_delta(G)`. If `G+T` has a proper colouring `sigma`, then `sigma` was already a proper colouring of `G`, so it extends some `S_j`. Every pair in `F(S_j)` is monochromatic under `sigma`, hence none can belong to `T`. Therefore

\[
\{G+T\text{ is 3-colourable}\}
\subseteq
\bigcup_{j=1}^J\{T\cap F(S_j)=\varnothing\}.
\tag{4.3}
\]

For a fixed set `F subseteq U` of size `f`,

\[
\mathbb P(T\cap F=\varnothing)
=
\frac{\binom{M-f}{t}}{\binom Mt}.
\tag{4.4}
\]

By (3.5), `f>=B_3(K_delta)`, and the ratio in (4.4) decreases as `f` grows. A union bound proves (4.1). Finally,

\[
\frac{\binom{M-f}{t}}{\binom Mt}
=
\prod_{i=0}^{t-1}\left(1-\frac{f}{M-i}\right)
\le
\left(1-\frac fM\right)^t
\le e^{-tf/M},
\tag{4.5}
\]

which yields (4.2). `square`

### Corollary 4.2 — a precise sufficient condition for the BGT upper-tail conjecture

Let `m_n=O(n)` and `t_n=tau n+o(n)` for a fixed `tau>0`. Let `G_n=G_{n,m_n}` and condition on `G_n` being 3-colourable. Suppose that for some fixed `delta<1`, some `eta_n->0`, and some `gamma>0`,

\[
\mathbb P\left\{
\log \mathcal C_\delta(G_n)>\eta_n n
\,\middle|\,
G_n\text{ is 3-colourable}
\right\}
\le e^{-\gamma n}.
\tag{4.6}
\]

Then under the usual monotone coupling from `G_{n,m_n}` to `G_{n,m_n+t_n}`,

\[
\boxed{
\mathbb P\{G_{n,m_n+t_n}\text{ is 3-colourable}\}
\le
e^{-\gamma n}
+
\exp\left[-\left(
\frac{\tau(1-\delta)^2}{3}-\eta_n+o(1)
\right)n\right].}
\tag{4.7}
\]

#### Proof

Because `m_n=O(n)`,

\[
M=\binom n2-m_n=\frac{n^2}{2}+O(n).
\]

From (3.4), with `K_delta=(1-delta)n+O(1)`,

\[
B_3(K_\delta)=\frac{(1-\delta)^2}{6}n^2+O(n),
\]

so

\[
\frac{t_nB_3(K_\delta)}{M}
=
\left(\frac{\tau(1-\delta)^2}{3}+o(1)\right)n.
\tag{4.8}
\]

On the good conditional event in (4.6), apply (4.2) and `log C_delta(G_n)<=eta_n n`; on the bad event use the trivial bound one. If `p_m=P(G_{n,m}\text{ 3-colourable})`, monotonicity gives exactly

\[
p_{m_n+t_n}
=p_{m_n}\,\mathbb E[q_{t_n}(G_n)\mid G_n\text{ 3-colourable}]
\le
\mathbb E[q_{t_n}(G_n)\mid G_n\text{ 3-colourable}],
\]

where `q_t(G)` is the conditional sprinkling-survival probability. This yields (4.7). `square`

### Source-level meaning

Let `M_n^*` be the moving sharp-threshold location in the Bayati--Gamarnik--Tetali/Friedgut formulation. If (4.6) can be proved at `m_n=M_n^*` (or at an asymptotically equivalent reference location) for one fixed `delta<1`, then sprinkling any fixed positive linear number of edges gives exponential decay. Since `M_n^*=Theta(n)` in the 3-colouring regime, a multiplicative displacement `(1+epsilon)M_n^*` corresponds to `tau n+o(n)`. Thus (4.6) is a concrete **sufficient geometric condition** for the colouring part of BGT Conjecture 1, and BGT's theorem would then imply the constant-location conclusion F0095.

This does **not** prove (4.6). The source-level problem is now concentrated into a specific conditional cluster-compression statement rather than another decimal upper-bound optimisation.

## 5. B20 — find why the obvious algorithms fail

I tested two plausible shortcuts. Both fail for an exact reason, and the same sparse family shows why the skeleton quotient is the right correction.

### 5.1 A sparse family where raw colour-count sprinkling is exponentially useless

For `r>=3`, define `H_r` on vertices

\[
\{x,y,z,w_1,\ldots,w_{r-3}\}
\]

by taking the triangle `xyz` and, for every `i`, adding only the two edges `xw_i,yw_i`. Then

\[
|E(H_r)|=3+2(r-3)=2r-3.
\tag{5.1}
\]

Every proper 3-colouring of the triangle uses all three colours, and each `w_i` is forced to take the colour of `z`. Hence

\[
Z(H_r)=6.
\tag{5.2}
\]

Now let

\[
G_{r,s}=H_r\sqcup I_s,
\qquad n=r+s,
\tag{5.3}
\]

where `I_s` is a set of `s` isolated vertices. Then exactly

\[
\boxed{Z(G_{r,s})=6\cdot3^s.}
\tag{5.4}
\]

Nevertheless all these exponentially many colourings share one equality skeleton on the `r`-vertex core: the cells are

\[
\{x\},\quad\{y\},\quad\{z,w_1,\ldots,w_{r-3}\}.
\tag{5.5}
\]

Thus whenever `delta>=s/n`,

\[
\mathcal C_\delta(G_{r,s})=1,
\tag{5.6}
\]

and this one skeleton has

\[
|F|=\binom{r-2}{2}.
\tag{5.7}
\]

Take `s=delta n+o(n)` and `t=tau n+o(n)`. Since `|E(G_{r,s})|=O(n)`, the skeleton bound gives

\[
q_t(G_{r,s})
\le
\exp\big[-(\tau(1-\delta)^2+o(1))n\big].
\tag{5.8}
\]

By contrast, the raw-colouring union bound from run 13 pays the factor `Z(G)=6*3^s` and a worst-case per-colouring survival factor asymptotic to `(2/3)^t`. Its exponent is

\[
\delta\log3-\tau\log(3/2)+o(1).
\tag{5.9}
\]

Therefore for every

\[
0<\tau<\frac{\delta\log3}{\log(3/2)},
\tag{5.10}
\]

the raw bound is exponentially larger than one and hence completely trivial, while (5.8) still gives exponential decay. This is an exact deterministic demonstration that **internal flexible entropy can destroy the colouring-count union bound even when one common frozen skeleton is enough**.

The family is sparse (`2r-3` edges), so this is not an artefact of a dense uniquely-colourable core.

### 5.2 Raw VC dimension is also the wrong compression statistic

A second idea was to apply an epsilon-net/VC argument directly to the family of monochromatic-pair sets

\[
\mathcal F_G=\{F(\sigma):\sigma\text{ a proper 3-colouring of }G\}.
\]

This cannot have sublinear VC dimension in general, even for the sparse family (5.3). Pair up `2 floor(s/2)` isolated vertices into `floor(s/2)` disjoint pairs. For any prescribed subset of those pairs, colour the endpoints of each selected pair equally and the endpoints of each unselected pair differently; the choices are independent because all these vertices are isolated. Hence the selected pair-coordinates are shattered:

\[
\boxed{\operatorname{VCdim}(\mathcal F_{G_{r,s}})\ge\lfloor s/2\rfloor.}
\tag{5.11}
\]

So raw VC compression can remain linear precisely because of variables that a cluster quotient should forget. This kills that shortcut before spending a run developing it.

The frozen-skeleton cover number removes both failures: it ignores the isolated-vertex entropy and remembers only common forbidden pairs large enough for sprinkling to hit.

## 6. What the three moves accomplished

**B3 (prove something stronger).** Instead of trying only to show w.h.p. non-colourability at another fixed decimal degree, Proposition 4.1 targets the stronger exponential survival decay that BGT identified as sufficient for constant threshold location. Corollary 4.2 turns one explicit cluster-compression property into that exponential tail.

**B18 (say it in another language).** Proper-colouring clusters were replaced by a finite set-cover/hitting problem on common monochromatic-pair sets. No metric definition of “cluster” is needed for Proposition 4.1; only common equality skeletons matter.

**B20 (find why the algorithm fails).** The sparse `H_r disjoint union I_s` family proves two naive routes fail for structural rather than technical reasons: raw colouring counts pay `Theta(n)` flexible entropy, and raw monochromatic-pair VC dimension can be `Theta(n)`. The same family is compressed to one skeleton, showing exactly what the quotient must remove.

## 7. Remaining obligation and next route

The source conjecture remains OPEN. The new exact obstruction is now:

\[
\boxed{
\text{Prove, near the moving 3-colourability threshold, an exponentially-good bound }
\log\mathcal C_\delta(G)=o(n)
\text{ for some fixed }\delta<1,
}
\tag{7.1}
\]

conditional on colourability, with the exceptional conditional probability itself exponentially small as in (4.6).

Existing freezing results concern frozen variables for typical colourings, while existing cover counts were developed principally for threshold upper bounds. Neither source checked this run was verified to imply the **uniform cover-number plus exponentially-small exceptional set** in (7.1) for ordinary `q=3` at the moving sharp threshold.

The next run must use a different triple. The most useful candidates are:

- **B6 — deform to a point you can solve:** begin with a random planted/conditioned model where a frozen core is explicit, then track the Radon--Nikodym cost of returning to uniform colourable `G_{n,m}`;
- **B14 — find the group acting:** quotient global `S_3` relabelling and local Kempe/flexible components before counting skeletons;
- **B28 — replace for-all with typical:** seek (4.6) under the conditional law of a uniformly random colourable graph rather than every colourable graph, because Proposition 4.1 already tolerates an exponentially rare bad set.

No Section-I stuck report is due yet: F0095 moved in the immediately preceding run and this is the first no-movement checkpoint after that movement.

## 8. Verification / artifact policy

No finite exhaustive claim was introduced. Propositions 4.1 and Corollary 4.2 are theorem-sized symbolic statements with full proofs on the page, and the sparse family is a symbolic construction valid for all `r,s`. A checker would only re-evaluate binomial identities and would violate the 90/10 rule, so no new arithmetic artifact was created.

The previous exact ACG witness and its archived `Fraction` output remain the finite certificate underlying `U_3=4.686514`; that output already ended `ALL_EXACT_CHECKS_PASS = True`.

## 9. Capability honesty

The actual runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed scheduled-task interface still offers schedule/prompt/title/enabled/timing fields but no model selector, no reasoning-effort selector, and no guaranteed execution duration. GPT-6 maximum remains text-requested only. A guaranteed change would require the platform to expose and honor model/reasoning fields for scheduled executions, or to provide authenticated runtime controls/telemetry.

The policy history records native modification probes returning `You cannot modify this task` for P26/P01/P03 in one context; current `RESULTS.md` records that P26 was later successfully updated in another authorized context while other IDs can remain denied by context. The permitted remedy for a denied task is to resolve task/account/workspace ownership through the authorized interface or platform support. Creating a duplicate schedule, bypassing permissions, or treating a repository edit as a scheduler repair is not an allowed workaround.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  target: F0095
  target_status: OPEN
  worker_status: PARTIAL
  metric: W_3 = U_3 - L_3
  before: 0.656514
  after: 0.656514
  movement: no movement
  L_3: 4.03
  U_3: 4.686514
  methods: [B3, B18, B20]
  new_route: frozen-skeleton cover / random hitting formulation
  deterministic_result: frozen-skeleton sprinkling inequality
  source_reduction: exponentially-good subexponential skeleton cover implies BGT exponential upper tail
  obstruction_1: raw coloring entropy can be exponential while skeleton cover number is 1
  obstruction_2: raw monochromatic-pair VC dimension can be linear due to flexible isolated vertices
  closure: false
  new_exact_artifact: none warranted
  unchanged_streak_on_F0095_since_last_movement: 1
  next_methods: [B6, B14, B28]
```

No shared root ledger was edited by this worker; this delta is for the designated reconciler.