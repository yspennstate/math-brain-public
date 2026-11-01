Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 at maximum. Metric moved `84 -> 85`; methods actually used: **#9 RANDOMIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R11 / I0054 — a quenched random interval-exchange compiler and C085

## Status

**Outside source:** David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.

**Source/campaign status after this run:** `PARTIAL`, not `CLOSED`. The canonical claim `operations/claims/I0054.md` still names R11 as provisional exclusive owner and still says `PENDING_ADMISSION, not READY`. A fresh bounded current-literature screen found no checked primary-source resolution of exact Open Problem 18, but that is only bounded negative evidence. The present package still lacks the required current-package P26 end-to-end PASS plus a second complete independent OTHER-track PASS.

**Frozen metric:** number of distinct nontrivial discrete model classes with a complete author-side proof of the required CTCS(infinity) limit under the fixed convention excluding deterministic leaf relabelings and positive global time rescalings of the source construction.

\[
\boxed{84\longrightarrow85.}
\]

New author-side claims:

- `R11-I0054-U067 = PROVED_AUTHOR_SIDE`: a **growing quenched logit-shuffle compiler**. A single global interval-exchange environment may be sampled once and shared by the whole finite tree, with its number of shuffled cells `M_N` tending to infinity. If `M_N=o(N)`, then every fixed finite restriction converges in whole-path total variation, uniformly over the quenched environment, to CTCS. Thus the environment need not refresh or self-average in time.
- `R11-I0054-C085 = PROVED_AUTHOR_SIDE`: take `L=2 log 2`, `M_N=max(2,floor(sqrt N))`, and one uniform permutation of the `M_N` equal logit cells sampled once for the whole tree. This gives a persistent quenched-disorder hierarchy with the full CTCS(infinity) limit. At `N=4` its annealed root holding time is an exact nontrivial mixture of two exponentials, so it is not a leaf relabeling or positive global time rescaling of source CTCS.

The mathematical route was archived **before checker code** in

`artifacts/R11/2026-09-20T05-38-26Z_u067-c085-quenched-logit-shuffle_idea.md`

at commit

`62d684b6dac288e8fb9ecab8a78d40a53bb088f0`.

The exact self-check was then archived at commits

- checker: `474110aaf0e3c4555f34d2162b2cc3491da4c7df`;
- output: `73724313840535ab23cbd36a9589fb54ba015602`.

It performed `146927` exact rational/integer assertions and ended `STATUS=ALL_EXACT_CHECKS_PASS`.

---

## 1. Continuity, source, ownership, exclusions, and prior attempts

Before new mathematics I reread or recovered the controlling surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the newest complete R11 report, `runs/R11/2026-09-20T04-42-24Z_i0054-logit-iet-u065-u066-c084-f19b.md`;
- current neighboring P13 material;
- exact I0054 audit and prior-attempt searches.

The compact root `RESULTS.md` still contains a stale historical R11 planar-self-avoiding-walk row and expressly warns that its R-series rows must not replace newer complete reports. The supported R11 baseline is therefore the immutable C084 report, `83 -> 84`. The old planar-SAW route remains retired and untouched.

The claim file still gives R11 the provisional exclusive I0054 reservation and says `PENDING_ADMISSION, not READY`. The current neighboring P13 stream says the earlier I0051/clade work is retired and has moved to a different LCS/reset-language project; no P13 source is reassigned here.

### Exact source and topology

I refreshed the authoritative arXiv v3 PDF on 20 September 2026. The PDF is dated 17 April 2025 and carries the arXiv v3 stamp of 18 April 2025. Printed page 58 states Open Problem 18:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source model's subordinator-approximation mechanism can arise in another discrete tree model.

The source defines CTCS(m) by splitting an `m`-leaf clade after an `Exponential(h_{m-1})` time, and Section 5.3 formalizes CTCS(infinity) through the consistent family of exchangeable partition restrictions. Open Problem 18 itself does not prescribe a named Skorokhod topology. R11 therefore retains the stronger frozen obligation used in the recent reports: for every fixed visible `k` and finite `T`, prove convergence of the **entire partition-valued path on `[0,T]` in total variation**. This implies finite-state Skorokhod `J_1` convergence, and the compatible finite restrictions then converge in the summable projective finite-restriction topology.

### Fresh bounded literature screen, 20 September 2026

I searched the exact source/problem together with `CTCS`, `random environment`, `interval exchange`, `measure preserving`, `logit`, `alternative discrete model`, and `critical beta-splitting`, and refreshed the authors' current project page. The relevant current primary items recovered were:

1. Aldous--Janson, arXiv:2303.02529v3, still containing Open Problem 18;
2. Aldous--Janson Part III, arXiv:2412.09655, on the exchangeable-partition representation;
3. Brandenberger--Chin--Mossel, arXiv:2505.24821, on harmonic-descent asymptotics;
4. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), on homogeneous fragmentations and beta-splitting height asymptotics, resolving a different height problem;
5. Heng Ma, arXiv:2609.14329 (13 September 2026), explicitly answering Aldous--Janson Open Problem 4, not Open Problem 18.

The authors' current page still describes the Open Problems article as the dynamic v3 document. I found no checked primary-source announcement settling exact Open Problem 18 and no checked publication containing the U067/C085 construction. This is **bounded negative evidence only**, not a worldwide openness or novelty certificate.

Interval-exchange transformations, random interval exchanges, quenched random environments, bounded-variation quadrature estimates, and finite-state CTMC uniformization are classical. I make no novelty claim for those generic ingredients. The possible new content is only their specific assembly into the CTCS compiler below and the uniform quenched proof.

A current exact repository search still does not recover a present-package `P26-AUDIT-R11-I0054` end-to-end PASS together with a second complete independent OTHER-track PASS. Older scoped R10/P26 checks of earlier C00x/U00x pieces are not promoted to audits of U067/C085.

---

## 2. Runtime/model-control fact check

The actual runtime identifies as **GPT-5.6 Sol**, not GPT-6. The reasoning level is not exposed to this worker and is therefore **UNVERIFIED**. I do not claim maximum reasoning.

The exposed task-control schema still provides prompt/title, schedule, timing mode, enablement and relative-start controls, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-hour field and no authenticated completed-run model/reasoning attestation**. A real GPT-6/maximum fix requires platform-level persisted routing controls and completed-run telemetry; prompt text alone cannot enforce or attest it.

The historical P26 `You cannot modify this task` failure is authorization-context dependent. The root reconciliation records a later successful P26 update from an authorized P/C context, while another exposed context rejected R-series modifications. For any task still rejecting modification, the legitimate workaround is its authorized owning account/workspace/interface or platform support, not cloning or permission bypass. No scheduler modification was attempted in this run.

---

## 3. What the three new methods did

### #9 — RANDOMIZE

C084 used one fixed deterministic interval exchange in the conserved logit coordinate. Here I choose a random permutation of an increasing number of equal logit cells **once per finite tree** and then freeze it for that tree. The same hidden permutation is shared by every clade for the entire genealogy.

The key improvement is that the proof below is actually **uniform over every permutation**, so the random environment does not need to average itself out in time.

### #15 — BREAK THE SYMMETRY ON PURPOSE

Conditional on the frozen permutation, the hierarchy is an ordinary Markov branching paintbox process. After averaging over the one persistent hidden permutation, different clades are correlated through common quenched disorder and the finite tree is generally **not** Markov branching. In particular, at `N=4` the annealed root holding time is a genuine mixture of exponentials rather than exponential.

Thus leaf exchangeability is retained while branching independence and the finite-time Markov property are deliberately broken.

### #21 — ASK WHO ELSE HAS THIS SHAPE

The right language is quenched random environment plus interval exchange / discrepancy theory. Earlier R11 C020 also had a persistent environment, but there the stationary **average** generator was correct and a frozen environment failed on two leaves; fast refreshing was necessary. U067 is the opposite regime: **every individual environment already has the correct continuum split integrals**, and the only issue is uniform discretization error. Therefore even a completely frozen environment works.

This distinction is the main mechanism learned in this run.

---

# 4. U067 — growing quenched logit-shuffle compiler

Fix a constant `L>0`. Write

\[
\sigma(y)=\frac{e^y}{1+e^y},
\qquad
\ell(x)=\log\frac{x}{1-x}.
\tag{4.1}
\]

Let `M_N>=2` be integers satisfying

\[
\boxed{M_N=o(N).}
\tag{4.2}
\]

Put

\[
h_N=\frac{L}{M_N}
\]

and partition `[0,L)` into the equal half-open cells

\[
I_{N,r}=[r h_N,(r+1)h_N),
\qquad 0\le r<M_N.
\tag{4.3}
\]

For any permutation `pi` of `{0,...,M_N-1}`, define the logit interval exchange

\[
S_{N,\pi}(r h_N+u)=\pi(r)h_N+u,
\qquad 0\le u<h_N,
\tag{4.4}
\]

and set

\[
S_{N,\pi}(y)=y
\quad\text{for }y\notin[0,L).
\tag{4.5}
\]

This is a Lebesgue-measure-preserving bijection of the line. Define its paintbox pullback

\[
\tau_{N,\pi}(x)
=\sigma(S_{N,\pi}(\ell(x))).
\tag{4.6}
\]

For each finite leaf count `N`, sample one environment `Pi_N` from **any probability law** on the `M_N!` permutations, and keep that environment fixed for the entire tree. Uniform sampling is not needed for the theorem.

Conditional on `Pi_N=pi`, every active nonsingleton clade has independent Poisson proposal clocks indexed by

\[
s=1,\ldots,N-1
\]

with rates

\[
\lambda_{N,s}
=\frac{N}{2s(N-s)}
=\frac{1}{2N x_s(1-x_s)},
\qquad x_s=\frac{s}{N}.
\tag{4.7}
\]

At a ring of clock `s`, independently color every label in the active clade red with probability

\[
p_{N,s,\pi}=\tau_{N,\pi}(x_s),
\tag{4.8}
\]

blue otherwise, and make the binary split if and only if both colors occur. After a split, descendant clocks and colors are fresh and independent conditional on the same global `pi`.

This is a finite discrete-state random-tree mechanism at every `N`; only branch lengths use the continuous clock embedding, as in CTCS itself.

## 4.1 Exact specified split rates conditional on the environment

Fix a visible clade and a specified unordered split `A|B` with

\[
|A|=i\ge1,
\qquad |B|=j\ge1.
\]

Conditional on `pi`, its exact rate is

\[
q_{N,\pi}(i,j)
=\sum_{s=1}^{N-1}\lambda_{N,s}
\left[
 p_{N,s,\pi}^i(1-p_{N,s,\pi})^j
 +p_{N,s,\pi}^j(1-p_{N,s,\pi})^i
\right].
\tag{4.9}
\]

Equivalently,

\[
q_{N,\pi}(i,j)
=\frac1N\sum_{s=1}^{N-1}F_{N,\pi;i,j}(s/N),
\tag{4.10}
\]

where

\[
F_{N,\pi;i,j}(x)
=\frac{
 \tau_{N,\pi}(x)^i(1-\tau_{N,\pi}(x))^j
 +\tau_{N,\pi}(x)^j(1-\tau_{N,\pi}(x))^i
}{2x(1-x)}.
\tag{4.11}
\]

## 4.2 The continuum integral is exactly CTCS for every environment

Let

\[
\Phi_{i,j}(y)
=\frac12\left[
 \sigma(y)^i(1-\sigma(y))^j
 +\sigma(y)^j(1-\sigma(y))^i
\right].
\tag{4.12}
\]

Since

\[
dx=x(1-x)\,dy,
\]

(4.11) gives

\[
\int_0^1F_{N,\pi;i,j}(x)\,dx
=
\int_{\mathbb R}\Phi_{i,j}(S_{N,\pi}(y))\,dy.
\tag{4.13}
\]

Every `S_{N,pi}` preserves Lebesgue measure, hence

\[
\int_{\mathbb R}\Phi_{i,j}(S_{N,\pi}(y))\,dy
=
\int_{\mathbb R}\Phi_{i,j}(y)\,dy.
\tag{4.14}
\]

With `p=sigma(y)` in the last integral,

\[
\begin{aligned}
\int_{\mathbb R}\Phi_{i,j}(y)\,dy
&=\frac12\int_0^1
\left[p^{i-1}(1-p)^{j-1}
+p^{j-1}(1-p)^{i-1}\right]dp\\
&=B(i,j)\\
&=\frac{(i-1)!(j-1)!}{(i+j-1)!}.
\end{aligned}
\tag{4.15}
\]

Therefore the continuum specified split rate is **exactly CTCS for every permutation**, not merely on average over the random environment.

This is why no temporal refresh is needed.

## 4.3 Uniform bounded-variation estimate as `M_N` grows

The new issue is that `S_{N,pi}` now has `M_N` pieces, so the fixed-map U066 error constant cannot simply be treated as fixed.

Let

\[
J_L=[\sigma(0),\sigma(L)]=[1/2,\sigma(L)].
\]

Outside `J_L`, `S_{N,pi}` is the identity, so `F_{N,pi;i,j}` equals the fixed beta-polynomial integrand

\[
F_{0;i,j}(x)
=\frac12\left[x^{i-1}(1-x)^{j-1}
+x^{j-1}(1-x)^{i-1}\right],
\tag{4.16}
\]

which has finite variation independent of `N` and `pi`.

Inside a logit cell, (4.4) has the form

\[
S_{N,\pi}(y)=y+d_r,
\qquad
 d_r=(\pi(r)-r)h_N,
\]

with

\[
|d_r|\le L.
\tag{4.17}
\]

Consequently on the corresponding `x`-interval,

\[
\tau_{N,\pi}(x)
=
\frac{e^{d_r}x}{1-x+e^{d_r}x}.
\tag{4.18}
\]

For fixed `i,j,L`, substitute (4.18) into (4.11). As a function of `(d,x)`, the resulting expression is `C^1` on the compact set

\[
[-L,L]\times J_L.
\]

Hence there are finite constants `A_{i,j,L},B_{i,j,L}` such that, on every cell interior,

\[
|F_{N,\pi;i,j}(x)|\le A_{i,j,L},
\qquad
|\partial_xF_{N,\pi;i,j}(x)|\le B_{i,j,L}
\tag{4.19}
\]

uniformly in `N`, `pi`, and the cell.

The sum of smooth variation over all cell interiors is therefore at most

\[
B_{i,j,L}|J_L|.
\]

There are at most `M_N+1` boundary jumps, including the two ends of the compact rearrangement region, and each jump is at most `2A_{i,j,L}`. Adding the fixed outside variation gives

\[
\boxed{
\operatorname{Var}(F_{N,\pi;i,j})
\le C_{i,j,L}(1+M_N)
}
\tag{4.20}
\]

for a constant independent of `N` and `pi`.

## 4.4 Uniform quadrature error

For any bounded-variation function `f` on `[0,1]`, the right-endpoint rectangle sum satisfies

\[
\left|
\frac1N\sum_{s=1}^{N}f(s/N)-\int_0^1f(x)\,dx
\right|
\le \frac{\operatorname{Var}(f)}N.
\tag{4.21}
\]

Our sum omits the `s=N` endpoint, contributing only `|f(1)|/N`. Applying (4.20)--(4.21) to (4.10), and using (4.15), yields

\[
\boxed{
\sup_{\pi}
|q_{N,\pi}(i,j)-B(i,j)|
\le
C'_{i,j,L}\frac{1+M_N}{N}.
}
\tag{4.22}
\]

Because `M_N=o(N)`, every fixed specified split rate converges to its CTCS rate **uniformly over the quenched environment**.

## 4.5 Strong lumpability of finite restrictions, conditional on `pi`

Fix visible labels `[k]`. Conditional on `pi`, the full `N`-leaf hierarchy is Markov.

Take any two full-tree states with the same visible partition. For a visible block of size `m` and any specified visible binary split `A|A^c`, the instantaneous rate of producing that visible transition is exactly `q_{N,pi}(|A|,m-|A|)`, independent of how many hidden labels share the full clade and independent of their identities. If a full split separates only hidden labels while all visible labels remain together, exactly one daughter carries the visible block and that daughter restarts with the same global `pi` and fresh clocks/colors. Thus hidden-only events do not alter any future visible transition rate.

Therefore the projection to `[k]` is strongly lumpable conditional on `pi`: it is itself a finite-state CTMC whose generator is obtained by assigning the rates (4.9) to every specified split of every current visible block.

## 4.6 Uniform whole-path total-variation convergence

Let `Q_{N,pi}^{(k)}` be this conditional `[k]` generator and `Q_CTCS^{(k)}` the CTCS generator. The visible state space is finite and contains only finitely many specified binary transitions. Equation (4.22) therefore implies

\[
\delta_{N,k}
:=
\sup_{\pi}
\max_{\xi}
\sum_{\eta\ne\xi}
|Q_{N,\pi}^{(k)}(\xi,\eta)
-Q_{\rm CTCS}^{(k)}(\xi,\eta)|
\le
C_{k,L}\frac{1+M_N}{N}
\longrightarrow0.
\tag{4.23}
\]

Use common uniformization / maximal coupling of the two finite-state CTMCs. Before the first discrepancy, the total mismatch hazard is at most a fixed constant multiple of `delta_{N,k}`. Hence for every finite `T`, after absorbing that harmless finite-state convention into `C_{k,L}`,

\[
\boxed{
\sup_{\pi}
\left\|
\mathcal L(\Pi_{N,\pi}^{[k]}|_{[0,T]})
-
\mathcal L(\Pi_{\rm CTCS}^{[k]}|_{[0,T]})
\right\|_{\rm TV}
\le
T C_{k,L}\frac{1+M_N}{N}
\to0.
}
\tag{4.24}
\]

This is stronger than a root-split law, a fixed-time marginal, or generator convergence.

Finally average over **any** law of the once-sampled environment `Pi_N`. Convexity of total variation gives

\[
\begin{aligned}
&\left\|
\mathcal L(\Pi_N^{[k]}|_{[0,T]})
-
\mathcal L(\Pi_{\rm CTCS}^{[k]}|_{[0,T]})
\right\|_{\rm TV}\\
&\qquad\le
\mathbb E\left[
\left\|
\mathcal L(\Pi_{N,\Pi_N}^{[k]}|_{[0,T]})
-
\mathcal L(\Pi_{\rm CTCS}^{[k]}|_{[0,T]})
\right\|_{\rm TV}
\right]\\
&\qquad\le
T C_{k,L}\frac{1+M_N}{N}
\to0.
\end{aligned}
\tag{4.25}
\]

Thus the annealed persistent-disorder model has whole-path TV convergence on every fixed finite restriction. In particular it has finite-state `J_1` convergence. Since all lower restrictions are deterministic restrictions of the `[K]` path, the standard finite-prefix/tail argument for the summable projective metric gives

\[
\boxed{
\Pi_N\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{4.26}
\]

This proves U067.

---

# 5. C085 — square-root quenched logit shuffle

Take

\[
\boxed{L=2\log2,}
\tag{5.1}
\]

\[
\boxed{M_N=\max\{2,\lfloor\sqrt N\rfloor\},}
\tag{5.2}
\]

and sample `Pi_N` uniformly from all `M_N!` cell permutations **once for the whole tree**.

Then

\[
\frac{M_N}{N}\to0,
\]

so U067 applies and gives the complete CTCS(infinity) projective limit.

The environment complexity tends to infinity, but it remains completely frozen in time. This is qualitatively opposite to the earlier C020 fast-refresh construction: C020 required temporal averaging because individual frozen environments had the wrong two-leaf survival law, whereas every C085 environment has the exact CTCS continuum split integrals before the harmonic grid is discretized.

## 5.1 Exact finite non-equivalence witness at `N=4`

At `N=4`,

\[
M_4=2.
\]

There are exactly two environments, each with probability `1/2`.

### Environment 0: identity

The biases are

\[
\left(\frac14,\frac12,\frac34\right),
\]

and the harmonic clock rates are

\[
\left(\frac23,\frac12,\frac23\right).
\]

Exact calculation gives

\[
q_{\rm id}(1,3)=\frac7{32},
\qquad
q_{\rm id}(2,2)=\frac5{32},
\]

hence total proper root-split rate

\[
\boxed{\Lambda_{\rm id}=\frac{43}{32}.}
\tag{5.3}
\]

### Environment 1: the adjacent-cell swap

Because `L=2 log 2`, this is exactly the C084 swap of `[0,log2)` and `[log2,2log2)`. The biases are

\[
\left(\frac14,\frac23,\frac35\right),
\]

and the independently recomputed exact rates are

\[
q_{\rm sw}(1,3)=\frac{722693}{3240000},
\qquad
q_{\rm sw}(2,2)=\frac{560707}{3240000},
\]

so

\[
\boxed{\Lambda_{\rm sw}=\frac{4572893}{3240000}.}
\tag{5.4}
\]

The two root rates are unequal.

Conditional on the quenched environment, the root holding time is exponential. After averaging over the one environment sampled at tree birth,

\[
\boxed{
\Pr(T_{\rm root}>t)
=\frac12e^{-\Lambda_{\rm id}t}
+\frac12e^{-\Lambda_{\rm sw}t}.
}
\tag{5.5}
\]

This is not exponential. Indeed put

\[
a=\Lambda_{\rm id}^{-1}=\frac{32}{43},
\qquad
b=\Lambda_{\rm sw}^{-1}=\frac{3240000}{4572893}.
\]

Then

\[
E[T]=\frac{a+b}{2},
\qquad
E[T^2]=a^2+b^2,
\]

and therefore

\[
\boxed{
E[T^2]-2E[T]^2
=\frac{(a-b)^2}{2}
=\frac{24588111077888}{38665086870091201}>0.
}
\tag{5.6}
\]

For source CTCS(4), the root holding time is a single exponential with rate

\[
H_3=\frac{11}{6},
\]

so exactly

\[
E[T^2]=2E[T]^2.
\tag{5.7}
\]

The equality (5.7) is preserved by every positive global time rescaling, and leaf relabeling does not affect root holding time. Therefore no deterministic relabeling and no positive global time rescaling can identify C085 with source CTCS.

The same witness also separates C085 from the deterministic C084/U066 class: deterministic finite-environment compilers have a single exponential root holding time, while C085 has the nontrivial quenched mixture (5.5).

For a second scale-free witness, the exact conditional balanced-root probabilities are

\[
P_{\rm id}(2|2)=\frac{15}{43},
\qquad
P_{\rm sw}(2|2)=\frac{1682121}{4572893}.
\]

Thus the annealed probability is

\[
\boxed{
P_{085}(2|2)=\frac{70462299}{196634399},
}
\tag{5.8}
\]

which differs from the source CTCS(4) value `3/11`.

---

## 6. Exact self-check

The exact checker is

`artifacts/R11/2026-09-20T05-38-26Z_u067-c085-quenched-logit-shuffle_check.py`.

It uses only Python integer arithmetic and `Fraction`. It verifies:

1. harmonic clock normalization for `N=2,...,30`;
2. the exact identity-grid split-rate algebra for all small split types through six visible labels;
3. every equal-cell permutation through `M=7` is a bijection preserving the discrete equal-cell measure, including inverse checks and complete target-cell coverage;
4. the complete `N=4` identity and swap environments and all four specified rates used above;
5. the two exact total root rates and their inequality;
6. the exact mixture-of-exponentials moment defect (5.6);
7. invariance of the normalized second-moment ratio under several exact positive global scalings;
8. the source CTCS(4) exponential equality;
9. the exact two conditional and one annealed balanced-root probabilities;
10. the exact square-root schedule identities and a broad finite scan of `M_N/N` bounds.

The archived output is

`artifacts/R11/2026-09-20T05-38-26Z_u067-c085-quenched-logit-shuffle_check.out`.

It ends

`STATUS=ALL_EXACT_CHECKS_PASS`

with

\[
\boxed{146927\text{ exact assertions}.}
\]

This is a **self-check**, not an independent audit.

---

## 7. Why this is not just C084 with one more random choice

At the continuum integral level, C084 and each C085 environment use the same conservation law. But the finite tree laws differ qualitatively.

- C084 has one deterministic map and, after hidden labels are lumped out, every finite restriction is Markov.
- C085 samples one latent permutation at tree birth and shares it across all clades. Conditional on the permutation the restriction is Markov; annealed over the latent permutation it generally is not.
- C085's finite root holding law is already non-exponential at `N=4`, whereas C084's is exponential.
- Yet U067 proves that this persistent quenched dependence disappears at the **whole fixed-restriction path-law level** because the conditional approximation is uniform in the environment.

The useful principle is therefore stronger than “random disorder averages out”: **quenched-uniform generator convergence makes temporal averaging unnecessary**.

---

## 8. Honest verdict and remaining obligations

The author-side mathematical result of this run is

\[
\boxed{\texttt{R11-I0054-U067 = PROVED\_AUTHOR\_SIDE}},
\]

\[
\boxed{\texttt{R11-I0054-C085 = PROVED\_AUTHOR\_SIDE}},
\]

and the frozen metric moves

\[
\boxed{84\to85.}
\]

I do **not** call Aldous--Janson Open Problem 18 closed under the campaign protocol. The canonical claim remains `PENDING_ADMISSION, not READY`; the fresh literature screen is bounded rather than a novelty certificate; and the required present-package P26 full-proof PASS plus a second independent OTHER-track full-proof PASS remain absent. The honest source/campaign status is therefore **PARTIAL**.

The next nonrepeating methods are **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #27 SWAP THE QUANTIFIERS**. The highest-value next target is to classify which growing finite permutation groups acting on logit cells admit **uniform** CTCS compilation when cell lengths are non-equal: instead of assuming equal cells and arbitrary permutations, ask for the sharp discrepancy condition on a weighted partition and prove a necessary-and-sufficient quenched criterion. That would turn U067 from one growing-shuffle family into a structural universality theorem.

---

## ledger_delta

```yaml
track: R11
target: I0054
source: Aldous-Janson arXiv:2303.02529v3 Open Problem 18
metric: distinct nontrivial discrete model classes with complete author-side CTCS-infinity limit proof under frozen equivalence convention
before: 84
after: 85
movement: +1
status: PARTIAL
stagnation_count: 0
methods_used: [9, 15, 21]
new_claims:
  - id: R11-I0054-U067
    status: PROVED_AUTHOR_SIDE
    statement: growing quenched logit-shuffle compiler; M_N=o(N) gives uniform quenched whole-path TV convergence on every fixed finite restriction
  - id: R11-I0054-C085
    status: PROVED_AUTHOR_SIDE
    model: one global uniform permutation of M_N=max(2,floor(sqrt(N))) equal cells in [0,2 log 2), frozen for the whole tree
    finite_non_equivalence: N=4 annealed root holding time is a nontrivial mixture of exponentials; exact positive exponential-moment defect
source_closure: false
canonical_claim: PENDING_ADMISSION_NOT_READY
external_novelty: UNVERIFIED_BOUNDED_NEGATIVE_SEARCH_ONLY
p26_current_package_audit: ABSENT
second_other_current_package_audit: ABSENT
self_check: PASS_146927_EXACT_ASSERTIONS
idea_before_code_commit: 62d684b6dac288e8fb9ecab8a78d40a53bb088f0
checker_commit: 474110aaf0e3c4555f34d2162b2cc3491da4c7df
checker_output_commit: 73724313840535ab23cbd36a9589fb54ba015602
next_methods: [3, 14, 27]
```
