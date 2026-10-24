Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 2500000/29648439 -> 2500000/29645831`. Methods tried: B15 / B25 / B3.**

# HARD7-03 — exact interior winner-max integration improves the D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, ownership, required reads, and current-source check

This execution resumes the existing exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

I re-read the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the D0025 claim/intake trail; the latest own checkpoint `20260919T1221Z__d0025-exact-mixed-sign-edge-kernel.md`; and the newest neighboring HARD7-02 / HARD7-04 states. The neighboring tracks remain on distinct non-Hermitian-matrix and growing-random-graph targets, so no canonical collision was found. Shared root ledgers were not modified.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, Problem 4, DOI `10.11606/resimeusp.v4i1.74889`, published 1 July 1999; arXiv `math/9906194`.

A fresh bounded literature check on 2026-09-19 used the exact source title and the queries `disordered K-exclusion plateau site disorder finite capacity K 2 exclusion flux`, `disordered asymmetric K-exclusion K=2`, and `partial exclusion disorder site rates asymmetric hydrodynamics flux plateau`. It recovered:

- Seppäläinen's primary 1999 source;
- Allan Sly, *Note on the flux for TASEP with general disorder*, arXiv `1609.06589`, which proves the iid site-disordered ordinary `K=1` TASEP plateau;
- Gonçalves–Hayashi–Sasada, arXiv `2405.15142`, on asymmetric partial-exclusion processes under a different product-rate / gradient-invariant setting;
- the 2013 low-current disordered simple-TASEP work that maps a singular binary-disorder limit to a partial-exclusion process, again not the source's iid site-disordered finite-capacity `K>=2` model.

No theorem closing the exact `K>=2` residual surfaced in this bounded search. This is **OPEN_BY_BOUNDED_SEARCH**, not a claim of exhaustive worldwide openness.

The frozen test case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\},
\]

with stable metric a rigorous lower bound `L <= Delta_2(Q)`.

The preceding certified value was

\[
G_1(0)\le \frac{29648439}{10000000}=2.9648439,
\qquad
L\ge \frac{2500000}{29648439}.
\tag{1.1}
\]

The inherited four-step Chernoff lemma and the previously proved D0025 transfer

\[
\Delta_2(Q)\ge \frac1{4G_1(0)}
\tag{1.2}
\]

are used below exactly as in the preceding checkpoint chain and are not re-derived here.

## 2. Idea-before-code and method rotation

Before writing the new checker I committed the route to

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1318Z__idea-exact-interior-mixed-max.md`

at commit `cadec3520ca8ca063ca0dd2ca5c70484f38c4716` and read it back successfully.

The preceding run used B29 / B27 / B21 and integrated the exact mixed-sign kernel only on the two edge triples. This run deliberately attacks the two remaining interior mixed-sign branch types.

- **B15 — break the symmetry on purpose.** First replace the lower competing maximum by a chosen anchor. This produces valid positive corrections and reveals that the best anchor depends on the branch, but it loses whenever another lower coordinate wins. Outcome: useful diagnostic, not the final bound.
- **B25 — count the same thing twice.** Replace the anchor by the exact winner expansion of the lower maximum's distribution. Outcome: successful; the entire lower maximum is integrated exactly.
- **B3 — prove something stronger.** Prove a reusable shifted-exponential chain-max transform for any finite lower competitor set, then specialize it to the near-edge and center branches. Outcome: successful; the new proof is stronger than the two needed special cases.

All thirty numbered methods have already appeared somewhere on this long D0025 track, so this is an explicit reuse after exhaustion, but the triple differs from the immediately preceding one and the mathematical role is new.

## 3. The exact mixed-sign residual inherited from the edge calculation

Write

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta,
\qquad \kappa=\frac{\theta}{bc}.
\]

For a strict mixed-sign predecessor pair `v<0<u`, the exact fresh-layer kernel beyond the global envelope is

\[
B_\theta(u,v)
=\theta e^v\left[
\frac{1-e^{-au}}{ab}-\frac{1-e^{-bu}}{bc}
\right].
\tag{3.1}
\]

Suppose a branch can be written

\[
U>T>M,
\tag{3.2}
\]

where `T` is the target predecessor, `U` the opposite predecessor that exceeds it, and `M` the maximum of all predecessors on the lower side. Then `u=U-T>0`, `v=M-T<0`. Multiplying (3.1) by the inherited factor `e^{theta T}` and expanding gives

\[
C_{\rm mix}
=\frac{\theta}{ab}(T_1-T_2)-\kappa(T_1-T_3),
\tag{3.3}
\]

where

\[
T_1=\mathbb E[e^{(\theta-1)T+M};U>T>M],
\tag{3.4}
\]

\[
T_2=\mathbb E[e^{-aU+M};U>T>M],
\tag{3.5}
\]

\[
T_3=\mathbb E[e^{-bU+T+M};U>T>M].
\tag{3.6}
\]

The edge checkpoint evaluated (3.4)--(3.6) when `M` is a single lower variable. The new obstacle is that in the interior branches `M` is a genuine maximum of two or three shifted exponentials.

## 4. B25/B3 lemma: exact shifted-exponential chain-max transform

Let

\[
Y_i=s_i+E_i,\qquad E_i\stackrel{\rm iid}{\sim}\mathrm{Exp}(1),
\]

and let `L` be a finite lower set,

\[
M=\max_{j\in L}Y_j,\qquad m=\max_{j\in L}s_j.
\]

For `y>=m`, independence gives

\[
F_M(y)=\prod_{j\in L}(1-e^{s_j-y}).
\tag{4.1}
\]

Expanding (4.1), differentiating, multiplying by `e^z`, and integrating from `m` to `y` yields exactly

\[
\boxed{
\mathbb E[e^M;M<y]
=\sum_{\varnothing\ne S\subseteq L}
(-1)^{|S|+1}|S|e^{\sum_{j\in S}s_j}h_{|S|}(y;m),
}
\tag{4.2}
\]

with

\[
h_1(y;m)=y-m,
\tag{4.3}
\]

and, for `n>1`,

\[
h_n(y;m)=\frac{e^{-(n-1)m}-e^{-(n-1)y}}{n-1}.
\tag{4.4}
\]

Now take `U=s_U+E_U`, `T=s_T+E_T`, assume pointwise `s_U<=s_T`, and define

\[
\mathcal T_{p,q}
=\mathbb E[e^{pU+qT+M};U>T>M].
\tag{4.5}
\]

Let

\[
y_0=\max(s_T,m),\qquad \lambda=2-p-q.
\]

For `p<1` and `lambda>0`, because `y>=y_0>=s_T>=s_U`,

\[
\mathbb E[e^{pU};U>y]
=\int_y^\infty e^{pu}e^{s_U-u}\,du
=\frac{e^{s_U-(1-p)y}}{1-p}.
\tag{4.6}
\]

The target density contributes `e^{s_T-y}`, so conditioning on `T=y` gives the exact identity

\[
\boxed{
\mathcal T_{p,q}
=\frac{e^{s_U+s_T}}{1-p}
\int_{y_0}^{\infty}e^{-\lambda y}
\mathbb E[e^M;M<y]\,dy.
}
\tag{4.7}
\]

Every subset term in (4.7) is elementary. For `|S|=1`,

\[
\int_{y_0}^{\infty}e^{-\lambda y}(y-m)\,dy
=e^{-\lambda y_0}\left(\frac{y_0-m}{\lambda}+\frac1{\lambda^2}\right),
\tag{4.8}
\]

while for `|S|=n>1`,

\[
\int_{y_0}^{\infty}e^{-\lambda y}h_n(y;m)\,dy
=\frac1{n-1}\left[
\frac{e^{-(n-1)m-\lambda y_0}}{\lambda}
-\frac{e^{-(\lambda+n-1)y_0}}{\lambda+n-1}
\right].
\tag{4.9}
\]

Equations (4.1)--(4.9) prove the chain-max transform on the page. In the present four-step LPP calculation every shift `s_i` is a maximum of a subset of the three first-layer exponentials. On each of their six strict order cones, `s_U,s_T,m,y_0` are order statistics. Thus (4.8)--(4.9) reduce to exact exponential-spacing moments, hence rational functions of rational `theta`. No simulation or finite path sampling is involved.

## 5. The two previously discarded interior mixed-sign branches

With the inherited notation

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{5.1}
\]

the near-edge strict mixed branch is

\[
Y_{-1}>Y_0>\max(Y_1,Y_2).
\tag{5.2}
\]

Here

\[
U=Y_{-1},\quad T=Y_0,\quad M=\max(Y_1,Y_2),
\]

and the deterministic shifts satisfy

\[
\max(A_{-1},A_0)\le\max(A_{-1},A_0,A_1),
\]

so the hypothesis `s_U<=s_T` in (4.6) is automatic. Reflection gives the other near-edge branch.

For the center, one orientation is

\[
Y_2>Y_1>\max(Y_{-2},Y_{-1},Y_0),
\tag{5.3}
\]

with

\[
U=Y_2,\quad T=Y_1,\quad
M=\max(Y_{-2},Y_{-1},Y_0).
\]

Again `s_U=A_1<=max(A_0,A_1)=s_T`. The reflected central orientation is disjoint from (5.3): (5.3) forces `Y_1>Y_{-1}`, while its reflection forces `Y_{-1}>Y_1`. Hence both reflected corrections can be added without double-counting.

Specializing (4.5) to

\[
(p,q)=(0,\theta-1),\quad (-a,0),\quad (-b,1)
\tag{5.4}
\]

produces exactly the three transforms in (3.4)--(3.6).

## 6. Exact rational certificate and metric movement

Take

\[
\theta=\frac{117261}{200000}=0.586305.
\tag{6.1}
\]

The exact `Fraction` checker reconstructs the inherited global-envelope correction and the exact edge correction, verifies the inherited closed-form `P2` identity, and then evaluates the two new chain-max branches. It obtains

\[
\begin{aligned}
C_{\rm edge}&\approx0.134583598517958,\\
C_{\rm near}&\approx0.086221715508408,\\
C_{\rm center}&\approx0.046153728082406.
\end{aligned}
\tag{6.2}
\]

The exact rational values are archived in the output; each is strictly positive. With reflection, the total fourth-step subtraction becomes

\[
H_{\rm new}
=H_{\rm base}+2C_{\rm edge}+2C_{\rm near}+2C_{\rm center}
\approx6.623730016570913.
\tag{6.3}
\]

Consequently the inherited four-step exponential-moment formula gives the exact rational upper bound `U_4` archived by the checker, numerically

\[
U_4\approx1045.864852929623794.
\tag{6.4}
\]

Now choose

\[
A=\frac{29645831}{10000000}=2.9645831,
\qquad
x=4\theta A
=\frac{3476299788891}{500000000000}.
\tag{6.5}
\]

For `x>0`,

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x.
\]

The checker proves in exact rational arithmetic

\[
S_{32}(x)-U_4>0,
\qquad
S_{32}(x)-U_4
\approx1.518637331087315\times10^{-4}.
\tag{6.6}
\]

Thus

\[
U_4<S_{32}(x)<e^{4\theta A}.
\]

The already established four-step block Chernoff argument therefore yields

\[
\boxed{G_1(0)\le\frac{29645831}{10000000}=2.9645831.}
\tag{6.7}
\]

Applying the inherited plateau transfer (1.2),

\[
\boxed{
\Delta_2(Q)\ge\frac{2500000}{29645831}
\approx0.084328889279575.
}
\tag{6.8}
\]

Hence the frozen metric moves rigorously from

\[
\frac{2500000}{29648439}
\quad\text{to}\quad
\frac{2500000}{29645831},
\]

with exact gain

\[
\boxed{
\frac{2500000}{29645831}-\frac{2500000}{29648439}
=\frac{6520000000}{878952612007809}>0.
}
\tag{6.9}
\]

This remains a quantitative theorem for the frozen `K=2` binary environment only. It is **PARTIAL** for the source's general-capacity Problem 4.

## 7. Exact artifacts and readback

Idea before code:

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T1318Z__idea-exact-interior-mixed-max.md`
- commit `cadec3520ca8ca063ca0dd2ca5c70484f38c4716`
- read back successfully.

Exact checker:

- `artifacts/hard7_2026-09-18/HARD7-03/exact_interior_mixed_max_20260919T1318Z.py`
- commit `357f61b7d387ef2b0e254026ceb080403c0d1e7e`
- read back successfully, including the final exact assertions.

Executed output:

- `artifacts/hard7_2026-09-18/HARD7-03/exact_interior_mixed_max_20260919T1318Z.out`
- commit `444ffef5999e32aa65f5ea96f3f89a563c84b3e9`
- read back successfully.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

These are self-checks, not independent closure audits.

## 8. What the three methods changed

- **B15 succeeded diagnostically:** a deliberately asymmetric single-anchor lower bound immediately exposed recoverable near-edge and center mass, but also showed why any fixed anchor is structurally lossy.
- **B25 succeeded decisively:** expanding the CDF of the lower maximum counts every possible winner and removes the anchor loss exactly.
- **B3 succeeded:** the stronger lemma (4.7)--(4.9) handles an arbitrary finite lower set of shifted exponentials, so the two needed branches are instances of one reusable transform rather than two ad hoc integrations.

A next route should not repeat another coefficient tweak. The largest obvious remaining kernel loss is the **both-positive predecessor-gap regime**, where the global envelope still uses only `kappa` although the exact kernel is strictly larger away from the origin. A distinct route is to move from four-step blocks to a transfer-operator formulation that keeps these branch transforms symbolically instead of re-optimizing one Chernoff point at a time.

## 9. Model / scheduler capability honesty

The available task interface still exposes scheduling metadata and enabled state but **no enforceable model selector, reasoning-effort selector, or guaranteed execution-duration field**. GPT-6 maximum is therefore prompt-requested only. This execution actually ran as **GPT-5.6 Sol / reasoning UNVERIFIED**. Enforcing GPT-6 maximum would require the platform to expose model and reasoning fields to the scheduler/runtime rather than only prompt text.

The current root ledger also records that P26's full prompt update succeeded in one authorized P/C context, while historical permission-denied observations existed in another context. This worker did not attempt to modify P26 or any other schedule. If a native task returns `You cannot modify this task`, there is no legitimate worker-side bypass: the owning account/workspace must perform the edit or platform/support must repair the ownership/permission state. Creating a duplicate would violate the owner directive.

## 10. Ledger delta for the shared-root maintainer

```text
track: HARD7-03
target: D0025 / Seppalainen Problem 4
status: PARTIAL
metric: L <= Delta_2(Q)
before: 2500000/29648439
after: 2500000/29645831
movement: +6520000000/878952612007809
methods: B15,B25,B3
unchanged_run_count: 0
stuck: false
shared_roots_modified: none
```

No closure is claimed, so no paper folder or closure-audit request is triggered.
