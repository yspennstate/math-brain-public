Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT on `VDH-8.3-DUALITY`: `Delta_dual,n -> 0` before and after; source-level movement: the unique-largest conditioning obstruction is removed by a new giant-scale subcritical theorem. Methods actually used: #5 ADD A PARAMETER, #11 DUALIZE, #28 REPLACE FOR ALL WITH TYPICAL.**

# R14 HARD OUTSIDE — VDH giant-conditioning erasure by truncated susceptibility

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / stronger source-level discrete-duality proof candidate / no closure claim / 0 independent audits for the new R14 theorem.**

## 1. Continuity and ownership

I followed current repository continuity rather than the stale native title. The negative-margin spherical-perceptron target was already handed off by R14, P0157 was subsequently terminally handed off after both allowed recovery cycles, and the current canonical exclusive claim is

`operations/claims/VDH-8.3-DUALITY.md`,

owner `R14`, status **SOURCE OPEN / PARTIAL / EXCLUSIVELY REASSIGNED TO R14**.

Before new mathematics I recovered/read the required control and state surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling owner directive it references;
- the current `VDH-8.3-DUALITY` claim;
- the latest R14 report `runs/R14/2026-09-19T18-01-23Z_p0157_terminal_handoff_vdh_conditional_duality_a19c.md`;
- the inherited HARD7-04 VDH proof chain, especially the 14:30 collared lower-bound recovery and 15:30 weighted-histogram duality report;
- current neighboring HARD random-graph / ownership reports returned by repository search;
- the intake/queue records around the van-der-Hofstad family, including the old `I0049` alias. `I0049` is a different uniformly-grown-graph problem and remains recorded as known/resolved in its queued scope; it is not this target.

No competing owner, posted source-matching resolution, or release of the R14 VDH claim surfaced.

## 2. Primary source and current-literature check — 19 September 2026

The primary source was reopened directly:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255,

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The page still states that the 2019 work with Janson and Luczak does not investigate the second-largest component in the supercritical regime and asks:

> “Does the discrete duality principle still hold?”

The exact retained source regime is the deterministic-degree configuration model with finite-third-moment critical limiting degree law and

\[
\nu_n=1+\varepsilon_n,
\qquad
\varepsilon_n\downarrow0,
\qquad
\varepsilon_n n^{1/3}\to\infty.
\tag{2.1}
\]

Fresh bounded searches dated 19 September 2026 again recovered the closest primary results:

1. van der Hofstad--Janson--Luczak, *Component structure of the configuration model: Barely supercritical case*, RSA 55 (2019), DOI `10.1002/rsa.20837`: precise barely-supercritical giant asymptotics, not the requested second-largest/discrete-duality theorem;
2. Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`: sharp subcritical CM upper bounds under additional hypotheses such as `Delta |Q|=o(R)` in the sharp regime;
3. older/model-specific discrete-duality results such as the supercritical 2D Hamming-graph second-largest theorem, which do not settle this deterministic-degree CM question.

No 2024--2026 paper closing the exact source statement was found in the bounded searches `"Does the discrete duality principle still hold" configuration model`, `barely supercritical configuration model second largest component 2026`, and `configuration model discrete duality barely supercritical`. This is **bounded negative evidence only**, not a worldwide novelty certificate.

The elementary path-count mechanism proved below may itself be folklore. I make no novelty claim for it.

## 3. Frozen metric and carry-in obstruction

The canonical inherited metric is

\[
\Delta_{\rm dual,n}
=
\left|
\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1
\right|.
\tag{3.1}
\]

HARD7-04 had already reached its mathematical floor

\[
\Delta_{\rm dual,n}\to0.
\tag{3.2}
\]

Therefore this run necessarily records

`Delta_dual,n: 0 -> 0` — **NO FIXED-METRIC MOVEMENT**.

The preceding R14 run nevertheless isolated a genuinely different source-mathematical obstruction. For a deterministic candidate giant set `S`, `T=V\S`, it proved the exact identity

\[
\mathcal L(X_T\mid S\text{ is unique largest})
=
\mathcal L\left(
CM(d|_T)\mid L_1(CM(d|_T))<|S|
\right),
\tag{3.3}
\]

and hence

\[
\boxed{
 d_{\rm TV}\left(
 \mathcal L(X_T\mid S\text{ is unique largest}),
 CM(d|_T)
 \right)
 =
 \mathbb P_{CM(d|_T)}(L_1\ge |S|).
}
\tag{3.4}
\]

So the exact remaining issue was not another sharp second-largest calculation. It was to show that a **fresh subcritical CM on the post-giant degrees is overwhelmingly unlikely to contain a component as large as the deleted giant**.

The sharp Coulson--Perarnau theorem cannot simply be invoked under the source assumptions: earlier HARD7-04 work proved source-valid residual-hub families for which the extra sharp-regime max-degree relation fails. This run therefore targets only the much weaker scale needed by (3.4).

## 4. Idea before validation

The new idea is to stop trying to control `L_1` directly.

Introduce a graph-distance parameter `r` and the truncated susceptibility

\[
\chi_r(G)=\frac1n\sum_v |B_r(v)|.
\tag{4.1}
\]

The discrete derivative `chi_r-chi_{r-1}` is bounded by the number of simple length-`r` paths. In a subcritical configuration model the exact pairing probability for a prescribed simple path gives a factor `(1-delta)^{r-1}`; the finite-pairing denominator costs only `exp(O(r^2/ell))`. Up to `r=c delta ell`, the subcritical decay wins.

A component of size at least `r+1` forces every vertex in that component to have at least `r+1` vertices in its `r`-ball. Thus one weak first-moment estimate for `chi_r` is enough to exclude components on the `n delta` scale.

This is the scale separation the previous route did not use.

## 5. #5 + #11 theorem: a universal giant-scale subcritical bound

Let `d=(d_1,...,d_n)` be any deterministic degree sequence with even half-edge count

\[
\ell=\sum_i d_i,
\qquad
\mu=\ell/n,
\qquad
\nu=\frac1\ell\sum_i d_i(d_i-1)=1-\delta,
\quad 0<\delta\le1/2.
\tag{5.1}
\]

Assume only that for fixed constants

\[
0<m\le\mu\le M<\infty.
\tag{5.2}
\]

### Theorem 5.1

For every integer

\[
1\le K\le\frac{\delta\ell}{16},
\tag{5.3}
\]

there is a constant `C=C(M)` such that

\[
\boxed{
\mathbb E\chi_K(CM(d))\le1+\frac{C}{\delta}
}
\tag{5.4}
\]

and

\[
\boxed{
\mathbb P(L_1(CM(d))\ge K+1)
\le
\frac{Cn}{\delta(K+1)^2}.
}
\tag{5.5}
\]

Consequently, for any such sequence with

\[
n\delta_n^3\to\infty,
\tag{5.6}
\]

we have

\[
\boxed{
L_1(CM(d^{(n)}))=o_p(n\delta_n).
}
\tag{5.7}
\]

**No maximum-degree assumption, fourth moment, Cramer collar, or sharp extreme-value theorem is used.**

### Proof

For `k>=1`, let `P_k(v)` count half-edge-labelled simple vertex paths of length `k` starting from `v`. If `U` is a uniform vertex, every point of `B_K(U)` is reached by at least one such path, so

\[
|B_K(U)|\le1+\sum_{k=1}^K P_k(U).
\tag{5.8}
\]

For distinct vertices `v_0,...,v_k`, the number of half-edge choices realizing the ordered path is

\[
d_{v_0}d_{v_k}\prod_{j=1}^{k-1}d_{v_j}(d_{v_j}-1).
\tag{5.9}
\]

A uniform perfect matching contains any fixed set of `k` prescribed disjoint pairs with probability

\[
\frac1{(\ell-1)(\ell-3)\cdots(\ell-(2k-1))}.
\tag{5.10}
\]

Summing over distinct vertex sequences and then dropping distinctness gives

\[
\begin{aligned}
\mathbb EP_k(U)
&\le
\frac1n
\frac{\ell^2\left(\sum_vd_v(d_v-1)\right)^{k-1}}
{(\ell-1)(\ell-3)\cdots(\ell-(2k-1))}\\
&=
\mu(1-\delta)^{k-1}
\prod_{j=1}^k
\left(1-\frac{2j-1}{\ell}\right)^{-1}.
\end{aligned}
\tag{5.11}
\]

For `k<=K<=delta ell/16`,

\[
\log\prod_{j=1}^k
\left(1-\frac{2j-1}{\ell}\right)^{-1}
\le
\frac{2k^2}{\ell}
\le
\frac{\delta k}{8},
\tag{5.12}
\]

while

\[
(1-\delta)^{k-1}\le e^{-\delta(k-1)}.
\tag{5.13}
\]

Hence

\[
\mathbb EP_k(U)
\le
\mu e^{\delta}e^{-7\delta k/8}.
\tag{5.14}
\]

Summing over `k` proves (5.4).

If a connected component `C` has at least `K+1` vertices, then for every `v in C`, either its `K`-ball already equals `C`, or a geodesic of length `K` from `v` supplies `K+1` distinct vertices. Thus

\[
|B_K(v)|\ge K+1
\quad\text{for every }v\in C,
\tag{5.15}
\]

so on `{L_1>=K+1}`,

\[
\chi_K\ge\frac{(K+1)^2}{n}.
\tag{5.16}
\]

Markov gives (5.5).

Finally choose any fixed `a<m/32` and `K=floor(a n delta)`. Then (5.3) holds for large `n`, `K>=a n delta/2`, and

\[
\mathbb P(L_1\ge a n\delta)
\le
\frac{C'}{a^2n\delta^3}\to0.
\tag{5.17}
\]

Running this with an arbitrarily small fixed `a` gives (5.7). `square`

A full self-contained version is archived in

`artifacts/R14/vdh_giant_scale_truncated_susceptibility.md`

creation commit

`05da5aac9ea18a4e84a36744e610798ec568aad8`.

I read the artifact back at that exact commit.

## 6. #28 application: the random post-giant profile only has to be typical

Return to the source regime (2.1). Let

\[
T_n=V\setminus C_{1,n},
\qquad
d_n^{out}=d|_{T_n}.
\]

The inherited 2019/HARD7-04 chain supplies, in the admitted source regime,

\[
|C_{1,n}|=\gamma_*n\varepsilon_n(1+o_p(1)),
\qquad \gamma_*>0,
\tag{6.1}
\]

residual mean degree bounded above and below away from zero, and

\[
\delta_n^{out}:=1-\nu_n^{out}
=\varepsilon_n(1+o_p(1)).
\tag{6.2}
\]

Choose a fixed `a>0` small compared with both the limiting residual mean degree and `gamma_*`. On the high-probability event where the fixed-factor forms of (6.1)--(6.2) hold, set

\[
K_n=\lfloor a|T_n|\delta_n^{out}\rfloor.
\tag{6.3}
\]

Then `K_n<|C_{1,n}|`, and Theorem 5.1 applies **conditionally to the realized random degree sequence**. Uniformly on that good event,

\[
\boxed{
\mathbb P_{CM(d_n^{out})}
\left(L_1\ge |C_{1,n}|\right)
=O\left(\frac1{n\varepsilon_n^3}\right)
=o(1).
}
\tag{6.4}
\]

This proves exactly what (3.4) needed. No sharp control at the true `epsilon^{-2} log(n epsilon^3)` extreme scale enters.

## 7. Literal pairing-law discrete duality

Let `T_n` retain its vertex labels. Construct `\widetilde G_n` by first sampling `T_n` with the **same marginal law** as the actual complement of the giant, and then, conditional on `T_n`, sampling a fresh independent `CM(d|_{T_n})`.

For each deterministic candidate complement, (3.4) says that the conditional total-variation distance equals the fresh-CM probability of containing a component at least as large as the deleted giant. Averaging (6.4) over the high-probability good class therefore gives

\[
\boxed{
 d_{\rm TV}\left(
 \mathcal L(T_n,G_n[T_n]),
 \mathcal L(T_n,\widetilde G_n)
 \right)
 \longrightarrow0.
}
\tag{7.1}
\]

So deleting the unique giant leaves **no asymptotically surviving pairing-law tilt**. Up to `o(1)` total variation, the complement is a fresh configuration model on its realized residual degrees.

This combines with the inherited HARD7-04 weighted histogram theorem

\[
\sum_d(1+d)
|N_{n,d}^{out}-n_d\xi_n^d|
=o_p(n\varepsilon_n)
\tag{7.2}
\]

and reflected criticality (6.2). Thus the source now has a precise random-degree-sequence duality statement:

\[
\boxed{
\text{delete giant}
\Longrightarrow
\text{fresh subcritical CM on residual degrees}
\quad\text{in }o(1)\text{ TV},
}
\tag{7.3}
\]

while those residual degrees are the extinction tilt to first order.

The earlier HARD7-04 collared tree-census chain separately gives the candidate source-size asymptotic

\[
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
\tag{7.4}
\]

The present run removes a distinct graph-law/selection objection to interpreting that result as discrete duality.

## 8. Method outcomes

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT: **success**

The parameter is the graph-distance cutoff `r` in `chi_r`. The discrete increment is dominated by the number of simple paths of length `r`. Its exact pairing expectation exhibits geometric subcritical decay up to `r=Theta(n delta)`. This converts a global conditioning question into a one-parameter path-growth calculation.

### #11 — DUALIZE: **success**

Rather than prove a sharp largest-component theorem, dualize the event `L_1>=K` into a deterministic lower bound on truncated susceptibility. First moments of simple paths then suffice. This eliminates every max-degree/fourth-moment hypothesis that obstructed direct use of the sharp subcritical literature.

### #28 — REPLACE FOR ALL WITH TYPICAL: **success**

The random complement need not satisfy a sharp theorem uniformly over every degree profile. The deterministic lemma is uniform on a coarse class (`mu` bounded, reflected drift `delta`), and the inherited post-giant results put the actual residual sequence in that class with probability `1-o(1)`.

## 9. What is and is not proved now

This run gives a complete on-page proof candidate for the giant-conditioning-erasure theorem (7.1). It is a **self-check**, not an independent audit.

The source should still be labelled **PARTIAL / SOURCE OPEN** under repository protocol because:

1. the collared upper/lower extreme-component chain giving (7.4) has not received the two required OTHER-track audits;
2. the new R14 theorem (5.1)/(7.1) has 0 independent audits;
3. the phrase “discrete duality principle” has a possible stronger interpretation requiring a deterministic-profile graph-law comparison or full component point-process convergence, whereas (7.1) is a fresh-CM comparison on the *random realized residual degree sequence*;
4. bounded searches do not certify worldwide novelty.

The remaining **mathematical** source gap is now much narrower: decide whether the source requires more than random-residual-sequence pairing-law duality plus the sharp `C_2` asymptotic. If yes, the next useful target is stability of the entire large-component point process under replacement of the random residual profile by the deterministic extinction-tilted profile; if no, the problem is mathematically candidate-complete and should move to independent audits rather than more research lemmas.

The frozen metric remains at its floor. Counting only the fresh R14 VDH assignment, this is the **second consecutive `0 -> 0` run**. One more unchanged fixed-metric run would trigger Section I for this fresh route under the owner's literal three-run rule.

The next fresh method triple, if a genuine source-mathematical obligation survives, is **#3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS**. It should target point-process/profile-replacement stability, not revisit the sharp collar route already exhausted by HARD7-04.

## 10. Model-control / permissions status

The scheduler-control limitation is still unchanged. The exposed task update surface provides title/prompt, schedule or relative start, timing mode, enabled state, and task identity/update fields. It exposes **no binding model-family selector and no reasoning-effort selector**, so the requested GPT-6/maximum setting remains prompt text only. This run actually identifies as GPT-5.6 Sol and exposes no reasoning-effort telemetry, hence `UNVERIFIED`.

Changing that would require an authorized product/workspace/API/admin execution surface that actually exposes and persists model-family and reasoning-effort fields (ideally with per-run attestation). A repository edit cannot create such a control.

The historical P26 `You cannot modify this task` event is an authorization-context boundary, not a mathematical or GitHub problem. `RESULTS.md` records that P26 was later editable from another authorized context. The compliant workaround is the task's owning/admin-authorized context or platform support; there is no permission bypass from this worker context. No scheduler or permission state was changed in this run.

No email, Drive, public posting, purchases, workflow execution, shared-root edit, peer-file edit, or scheduler change was performed.

### ledger_delta

```yaml
track: "R14 HARD OUTSIDE"
target: "VDH-8.3-DUALITY"
owner: "R14"
source_status: "OPEN"
research_status: "PARTIAL_STRONGER_DISCRETE_DUALITY_PROOF_CANDIDATE"
runtime_model: "GPT-5.6 Sol"
reasoning_level: "UNVERIFIED"
requested_model_only: "GPT-6 maximum"
metric:
  name: "lim Delta_dual,n"
  before: 0
  after: 0
  movement: "NO_FIXED_METRIC_MOVEMENT"
  r14_fresh_target_consecutive_unchanged: 2
methods: [5, 11, 28]
new_result:
  type: "theorem_sized_self_check"
  deterministic_statement: "If nu=1-delta, mean degree is bounded above/below, and n delta^3 -> infinity, then L1(CM(d))/(n delta) -> 0 without a max-degree hypothesis."
  source_consequence: "The unique-largest conditioning on the post-giant pairing is o(1) in total variation; the complement is asymptotically a fresh CM on its realized residual degrees."
artifact:
  path: "artifacts/R14/vdh_giant_scale_truncated_susceptibility.md"
  creation_commit: "05da5aac9ea18a4e84a36744e610798ec568aad8"
independent_audits: 0
closure: false
remaining_obligation: "Source-scope reconciliation: whether random-residual-degree-sequence TV duality plus the existing sharp C2 proof candidate is source-complete; if a stronger interpretation is intended, prove point-process/profile-replacement stability. Then obtain two OTHER-track audits."
next_methods: [3, 12, 27]
```
