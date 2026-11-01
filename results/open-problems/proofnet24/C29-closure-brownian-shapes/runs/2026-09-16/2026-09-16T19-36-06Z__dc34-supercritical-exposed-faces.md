Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but this runtime and the exposed scheduler provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **no movement — frozen C29 fallback metric 2 -> 2; unchanged-run count 2; Section-B moves tried: 7, 11, 14.**
Problem/source: Chiara Meroni, Randomstrasse 101 (2026), Conjecture 34 on non-semialgebraic functional directional-convex hulls; fallback claim `RS-2026-DC34`. The owner's proposed Burdzy--Scheutzow Problem 7.8 / intake I0077 remains excluded from C29 because R07 owns the canonical reservation and its newest report has now moved its own source-family metric to 3. C29 remains **CLAIMED / PENDING_ADMISSION / NOT READY** on the fallback target.

# C29 — supercritical exposed faces, a face-localization lemma, and the residual 3D obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, permission change, shared-ledger edit, peer-file edit, or new schedule.

## 1. Continuity, ownership, and frozen metric

I continued from the newest durable C29 report

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T18-37-17Z__dc34-fivepoint-spike-threshold.md`

rather than restarting from the Brownian proposal or the old MUB attack. Before the new attack I reread/queried campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, canonical claims `operations/claims/I0077.md` and `operations/claims/RS-2026-DC34.md`, the newest C29 fallback report, the newest R07 Problem-7.8 report, the newest C30 report for the directed audit duty, and the newest visible legacy `proofnet24/C29-mub-six` reports for reserve continuity only. Large intake JSONL surfaces were queried by the relevant IDs rather than falsely described as manually rendered byte-for-byte.

### I0077 remains excluded

The canonical claim `operations/claims/I0077.md` still reserves Burdzy--Scheutzow Problem 7.8 to R07 and labels it `PENDING_ADMISSION, not READY`. R07's newest report, `runs/R07/20260916T1925Z_i0077_pure_power_phase_03.md`, now records metric movement `2 -> 3` by adding a complete pure-power phase portrait to its two earlier nonparabolic families. Therefore there is even less basis for C29 to duplicate I0077. Problem 7.5 remains separately answered/excluded and was not reopened.

### Fallback metric stays frozen at 2

The create-only C29 claim `RS-2026-DC34` freezes the fallback metric to the number of pairwise distinct affine boundary patches proved for **one fixed four-point lifted irrational-parallelogram candidate**. The exact four-point theorem already proved that this value is `2`: the two maximal affine lower-boundary patches lie in `z=0` and `z=s+t-1`, while the remaining two-dimensional boundary pieces are curved. This run studies the centered supercritical **five-point extension** as a route-finding experiment. Its extra facets are auxiliary information and are not allowed to inflate the frozen four-point metric. Thus the honest before/after remains

\[
\boxed{2\longrightarrow2}.
\]

This is the second consecutive unchanged frozen-metric run. The remaining obligation changed materially, so no stuck-recovery report is yet triggered; a third unchanged metric run will require the protocol's stuck check.

## 2. MUB HARD RESERVE remains untouched

The old six-dimensional MUB existence attack stays in **HARD RESERVE**. Preserve without reinterpretation:

- unrestricted/global normalized residual lower bound: `0`;
- `11/756`: an **upper** benchmark from an explicit configuration, not a positive lower bound and not a nonexistence proof;
- all exact phase examples, restricted auxiliary bounds, atlas reductions, and failed proof routes.

I did not restart that target and did not count any reserve-only report as progress on the live C29 metric.

## 3. Current source and prior-art check — 16 September 2026

Fresh bounded searches used:

1. `"Directional Convexity" Meroni Randomstrasse Conjecture 34 2026`;
2. `"non-semialgebraic" "D-convex hull" directional convexity`;
3. `"Semialgebraic rank-one convex hulls" Meroni Raita 2509.07541`;
4. `"Computing D-convex hulls in the plane" Franek Matousek 2009`;
5. `"On directional convexity" Matousek 2001`.

The current Randomstrasse page still states Conjecture 34: a finite set may have a non-semialgebraic functional `D`-convex hull, with the concrete three-plane/common-line cone singled out. Meroni--Raiţă's current arXiv paper `2509.07541` proves semialgebraicity in the triangular rank-one setting, gives explicit five-point constructions, and explicitly presents more general directional convexity as the place where a similar description may fail. Chiara Meroni's current research page lists that paper as forthcoming in *Communications in Analysis and Geometry*.

For the planar reduction used below, Franěk--Matoušek (2009) give a polynomial-time algorithm for the functional `D`-convex hull of a finite planar point set for arbitrary finite `D`. Matoušek (2001) also shows that directional hulls can be highly nonrobust, so a pointwise/parameter limit of input data does **not** automatically justify convergence of the full hull. That warning is relevant to move 7 below.

The bounded search did not surface a later paper resolving Randomstrasse Conjecture 34 or the centered supercritical five-point family below. This is dated bounded-search evidence only, **not** a worldwide openness or novelty certificate.

## 4. Recovered exact normal form

Use the already-fixed quotient coordinates

\[
D_2=\mathbb R(1,0)\cup\mathbb R(0,1)\cup\mathbb R(1,-\alpha),
\qquad \alpha>1,
\]

and let `D` be the union of the corresponding three vertical planes in `R^3` (equivalently, the lift of `D_2` with arbitrary vertical component). The canonical four points are

\[
A_{00}=(0,0,0),\quad
A_{10}=(1,0,0),\quad
A_{01}=(0,1,0),\quad
A_{11}=(1,1,1).
\]

The exact previous theorem is

\[
\operatorname{conv}_D(K_4)
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le st\},
\tag{4.1}
\]

where

\[
h(s,t)=\max\left\{
0,\ st-\alpha^{-1}t(1-t),\ s+t-1
\right\}.
\tag{4.2}
\]

The preceding run added a spike

\[
P_{a,b,\delta}=(a,b,ab+\delta)
\]

and proved that the coordinate-bilinear upper envelope stays fully `D_2`-concave exactly through

\[
\delta\le\delta_c(a,b):=\min\{a(1-b),(1-a)b\}.
\tag{4.3}
\]

Moreover `\sup\delta_c=1/4`, uniquely at the centered point `a=b=1/2`. Hence the cleanest first supercritical object is

\[
C_\delta=\left(\frac12,\frac12,\frac14+\delta\right),
\qquad \delta>\frac14.
\tag{4.4}
\]

Set

\[
H:=\frac14+\delta,
\qquad
p:=2H=\frac12+2\delta>1.
\tag{4.5}
\]

Let

\[
K_5:=K_4\cup\{C_\delta\}.
\]

This run asks what *must* already be true of the supercritical hull before attempting an infinite alternating-concavification argument.

## 5. Move 11 — DUALIZE: global affine supports and exact exposed-face localization

The first useful dual objects are four affine functions

\[
L_L(s,t)=ps,
\qquad
L_B(s,t)=pt,
\tag{5.1}
\]

\[
L_R(s,t)=t+(p-1)(1-s),
\qquad
L_T(s,t)=s+(p-1)(1-t).
\tag{5.2}
\]

Because `p>1`, each is a global majorant of the five input heights. Their contact sets are exactly

\[
\begin{aligned}
L_L &: \{A_{00},A_{01},C_\delta\},\\
L_B &: \{A_{00},A_{10},C_\delta\},\\
L_R &: \{A_{10},A_{11},C_\delta\},\\
L_T &: \{A_{01},A_{11},C_\delta\}.
\end{aligned}
\tag{5.3}
\]

For example `L_L(C_delta)=p/2=H`, while `L_L(A_10)=p>0` and `L_L(A_11)=p>1`; the other cases follow by symmetry or direct substitution. Since every affine function is `D`-convex, `z-L_i` is a valid separating `D`-convex function. Therefore

\[
\boxed{z\le \min\{L_L,L_B,L_R,L_T\}}
\qquad\text{on }\operatorname{conv}_D(K_5).
\tag{5.4}
\]

The following lemma is the more reusable part of this move.

### Lemma `C29-EXPOSED-FACE-LOCALIZATION-07`

Let `K` be finite, let `D` be any direction cone, and let `a` be affine with `a\le0` on `K`. Put

\[
K_0:=\{k\in K:a(k)=0\}.
\]

Then

\[
\boxed{
\operatorname{conv}_D(K)\cap\{a=0\}
=\operatorname{conv}_D(K_0).
}
\tag{5.5}
\]

#### Proof

Monotonicity gives `conv_D(K_0) subset conv_D(K)`. Since both `a` and `-a` are affine and therefore `D`-convex and vanish on `K_0`, every point of `conv_D(K_0)` lies in `a=0`.

For the reverse inclusion, suppose `x in conv_D(K)`, `a(x)=0`, but `x notin conv_D(K_0)`. By the functional definition of the hull there is a `D`-convex function `g` with

\[
g(x)>\max_{K_0}g.
\]

Subtract `c=max_{K_0}g`; then `g-c\le0` on `K_0` but `(g-c)(x)>0`. Because `K` is finite and `a(k)<0` for every `k in K\setminus K_0`, choose `M>0` so large that

\[
(g-c)(k)+Ma(k)\le0
\qquad\forall k\in K\setminus K_0.
\]

The function `g-c+Ma` is still `D`-convex, is nonpositive on all of `K`, and is positive at `x` because `a(x)=0`. This contradicts `x in conv_D(K)`. Hence (5.5). `square`

Applied to `a_i=z-L_i`, this says each globally exposed upper face is **exactly** the `D`-convex hull of its three input contact points. Inside the affine graph `z=L_i(s,t)`, the intersections with the three vertical direction planes project to the three planar direction lines in `D_2`. Thus each such face is affinely equivalent to a finite planar functional `D_2`-hull. That is exactly the class covered by the Franěk--Matoušek planar polynomial-time algorithm.

Consequently, any genuinely wild behavior in this centered five-point experiment cannot be blamed merely on the existence of these four globally exposed support faces. The unresolved mechanism has to live in the residual, non-globally-exposed boundary generated by alternating directional concavification.

## 6. Move 14 — FIND THE GROUP ACTING: one involution generates half the geometry

The centered configuration has the affine involution

\[
F(s,t,z)=(1-s,1-t,z+1-s-t).
\tag{6.1}
\]

Its linear part sends the planar component `(u,v)` to `(-u,-v)`, so it preserves each of the three unoriented direction lines in `D_2`; the extra vertical shear is harmless because each source direction plane contains the vertical line. Hence `F` preserves `D`-convexity and `D`-lamination.

Moreover

\[
A_{00}\leftrightarrow A_{11},
\qquad
A_{10}\leftrightarrow A_{01},
\qquad
F(C_\delta)=C_\delta.
\tag{6.2}
\]

Thus it suffices to build the left and bottom exposed pieces explicitly; the right and top pieces follow automatically.

## 7. New auxiliary theorem: four exact supercritical affine upper patches

### Theorem `C29-DC34-SUPERCRITICAL-EXPOSED-06 = PROVED (PARTIAL)`

For every `alpha>1` and every centered spike with `delta>1/4`, the functional `D`-convex hull of `K_5` contains four pairwise distinct, positive-area affine upper-boundary patches, one in each of the planes

\[
z=L_L,\quad z=L_B,\quad z=L_R,\quad z=L_T.
\tag{7.1}
\]

More explicitly, their horizontal projections contain the triangles

\[
R_L=\operatorname{conv}\left\{
(0,\tfrac12),(0,1),(\tfrac1{2\alpha},\tfrac12)
\right\},
\tag{7.2}
\]

\[
R_B=\operatorname{conv}\left\{
(\tfrac12,0),(\tfrac12,\tfrac12),(\tfrac12+\tfrac1{2\alpha},0)
\right\},
\tag{7.3}
\]

and `R_R`, `R_T` are the images under `(s,t) -> (1-s,1-t)`. Each triangle has area `1/(8 alpha)`, so the four explicitly certified upper affine pieces have total planar area

\[
\frac1{2\alpha}.
\tag{7.4}
\]

The exact lower boundary remains the old function `h` from (4.2). Therefore the five-point supercritical hull has **at least six pairwise distinct two-dimensional affine boundary patches**: the two old lower patches and the four new upper patches.

This count `6` is **AUXILIARY** and is not C29's frozen metric, which remains the exact four-point value `2`.

#### Proof: left face

The segment between `A_00` and `A_01` is allowed in the `(0,1)` direction, so the entire left edge

\[
(0,t,0),\qquad0\le t\le1,
\]

lies in the hull. In particular

\[
B_L=(0,\tfrac12,0)
\]

lies in the hull. The segment from `B_L` to `C_delta` is allowed in the `(1,0)` direction and gives

\[
X_s=(s,\tfrac12,ps),
\qquad0\le s\le\tfrac12.
\tag{7.5}
\]

Now fix `0\le s_0\le1/(2 alpha)`. The point

\[
Y_{s_0}=(0,\tfrac12+\alpha s_0,0)
\]

lies on the already-generated left edge. The horizontal displacement from `Y_{s_0}` to `X_{s_0}` is

\[
(s_0,-\alpha s_0)=s_0(1,-\alpha),
\]

so that segment is also an allowed `D`-lamination. Every point on it satisfies `z=ps`, because the two endpoints do. Varying `s_0` fills exactly the triangle `R_L` in (7.2). Therefore the graph of `L_L` over `R_L` lies in the hull.

The separator `z-L_L\le0` from (5.4) proves these points are on the **exact upper boundary**, not merely somewhere inside the hull.

#### Proof: bottom face

The bottom edge between `A_00` and `A_10` lies in the hull. Let

\[
B_B=(\tfrac12,0,0).
\]

The vertical-in-quotient `(0,1)` segment from `B_B` to `C_delta` gives

\[
X_t=(\tfrac12,t,pt),
\qquad0\le t\le\tfrac12.
\tag{7.6}
\]

For `0\le t_0\le1/2`, put

\[
Y_{t_0}=(\tfrac12+t_0/\alpha,0,0),
\]

which lies on the bottom edge because `alpha>1`. The displacement

\[
X_{t_0}-Y_{t_0}=(-t_0/\alpha,t_0,pt_0)
\]

has horizontal component proportional to `(1,-alpha)`, so the connecting segment is an allowed `D`-lamination. It lies in `z=pt` and the union fills `R_B`. The separator `z-L_B\le0` again makes the patch exact.

#### Right and top faces

Apply the `D`-preserving involution `F` from (6.1). It maps the left patch to an upper patch in

\[
z=L_R=t+(p-1)(1-s)
\]

over

\[
R_R=\operatorname{conv}\left\{
(1,\tfrac12),(1,0),(1-\tfrac1{2\alpha},\tfrac12)
\right\},
\]

and maps the bottom patch to an upper patch in

\[
z=L_T=s+(p-1)(1-t)
\]

over

\[
R_T=\operatorname{conv}\left\{
(\tfrac12,1),(\tfrac12,\tfrac12),(\tfrac12-\tfrac1{2\alpha},1)
\right\}.
\]

The four support planes are pairwise distinct for `p>1`, and their triangle interiors are disjoint for `alpha>1`.

#### Lower boundary does not move

The old four-point hull is contained in the five-point hull, so every old lower point `(s,t,h(s,t))` is still attained. Conversely the previous four-point proof established that `h-z` is `D`-convex. At the added centered point,

\[
h(\tfrac12,\tfrac12)
=\frac14-\frac1{4\alpha}
<\frac14
<H,
\]

so `h-z\le0` also holds on the fifth input point. Hence it separates the entire five-point hull from below. Therefore the exact lower boundary is still `h`. In particular its two positive-area affine pieces `z=0` and `z=s+t-1` remain boundary patches. `square`

## 8. Move 7 — TAKE THE LIMIT: the high-spike four-facet skeleton

Let `delta -> infinity` with `alpha` fixed and normalize only the vertical coordinate by `delta`. Since

\[
\frac p\delta=2+\frac1{2\delta}\longrightarrow2,
\]

the four exact affine support functions converge locally and uniformly to

\[
2s,\qquad2t,\qquad2(1-s),\qquad2(1-t).
\tag{8.1}
\]

Thus every normalized hull obeys the global upper bound

\[
\frac z\delta
\le
\min\left\{
\frac{L_L}{\delta},
\frac{L_B}{\delta},
\frac{L_R}{\delta},
\frac{L_T}{\delta}
\right\},
\]

whose limit is the four-facet tent

\[
2\min\{s,t,1-s,1-t\}.
\tag{8.2}
\]

On the four fixed triangles `R_L,R_B,R_R,R_T`, the normalized boundary is already known exactly and converges to the corresponding facet of (8.2). This is a useful solvable limiting skeleton.

I **do not** claim that the entire normalized functional `D`-convex hull converges to that tent. Matoušek's nonrobustness examples show why such a global continuity inference is unsafe without a separate theorem. The limit move therefore narrows the next attack rather than pretending to finish it: study the residual region between the four exposed faces and ask whether its alternating third-direction concavifications terminate or generate an infinite scale cascade.

## 9. What changed about the obstruction

The previous run only knew that `delta>1/4` forces the third direction to become active somewhere. This run separates the geometry into two qualitatively different parts:

1. **four global exposed faces** are rigid, explicit, finitely generated, and reducible by (5.5) to planar finite-point `D_2`-hulls;
2. any possible non-semialgebraicity must therefore come from the **residual non-globally-exposed boundary**, where support planes are created recursively rather than inherited from a fixed contact subset of the original five points.

This rules out a tempting but false route: simply counting the global support planes generated by the spike can never by itself establish Conjecture 34 for this family.

The next concrete route is to break the centered symmetry slightly and track one residual third-direction patch through repeated coordinate concavification, looking for a genuine return map on slopes. If that return map is fractional-linear with irrational rotation/continued-fraction data, it could explain the infinite-grid heuristic. If instead every orbit reaches one of the four exposed faces after finitely many steps, that would prove semialgebraicity for this five-point family. Suggested next untried moves: **15 (break symmetry deliberately), 17 (look for the slope sequence elsewhere), 30 (localize one scale/direction at a time).**

No checker was manufactured this run. The new claims are analytic/geometric and their finite-lamination proofs are written on the page; there is no finite arithmetic core whose verification would add information.

## 10. Directed C30 audit — actual newest claim

The newest C30 report contains the analytic theorem `C30-CUBIC-TENSOR-ZERO-02`, not merely the earlier rank-two theorem. I independently audited that claim.

### `C29-AUDIT-C30-CUBIC-TENSOR-ZERO-02 = PASS (claim-scoped)`

C30 assumes a finite bipartite graph `F` with maximum degree at most three and a bounded symmetric nonnegative 1-regular finite-rank kernel

\[
A(x,y)=1+\sum_{i=1}^r\lambda_i f_i(x)f_i(y),
\]

where the nonconstant `f_i` are real orthonormal mean-zero eigenfunctions, together with

\[
\int f_i f_j f_k=0
\qquad\forall i,j,k.
\tag{10.1}
\]

Expand `t_F(A)` by choosing on each edge either the constant term or one spectral color `i`. At a vertex:

- nonconstant degree `1` gives `\int f_i=0` and vanishes;
- nonconstant degree `2` gives `\int f_i f_j=\delta_{ij}`, so the two incident colors must agree;
- nonconstant degree `3` vanishes by (10.1).

Because `Delta(F)<=3`, every surviving nonconstant selected component is therefore 2-regular: a disjoint union of cycles. The degree-two orthogonality condition forces a single spectral color around each cycle. Because `F` is bipartite, every cycle is even, and its weight is `lambda_i^{2m}>=0`. The all-constant choice contributes exactly `1`. Every other surviving term is nonnegative, hence

\[
\boxed{t_F(A)\ge1}.
\]

This independently reproduces C30's mechanism and normalization. The PASS is limited to the finite-rank, cubic-tensor-zero theorem. It does **not** certify infinite-rank kernels, C30's separate order-eleven sparse-host theorem, the full fixed `H=K_{5,5}\setminus C_{10}` Sidorenko conjecture, or source-level closure.

## 11. Ledger delta for P26

P26 should reconcile only the following supported delta from this immutable report; C29 did not edit shared ledgers itself.

- track: `C29`;
- active fallback claim: `RS-2026-DC34`;
- source: Randomstrasse 101, Conjecture 34;
- status: `PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY`;
- frozen metric: exact affine-boundary-patch count for the fixed four-point candidate;
- before: `2`;
- after: `2`;
- unchanged-run count: `2`;
- new auxiliary theorem: `C29-DC34-SUPERCRITICAL-EXPOSED-06 = PROVED (PARTIAL)`, giving at least four explicit upper affine faces and at least six total affine boundary patches for the **different five-point supercritical extension**; do not use `6` as the frozen metric;
- new structural lemma: `C29-EXPOSED-FACE-LOCALIZATION-07 = PROVED`;
- I0077 exclusion: canonical owner remains R07; newest R07 report has its own metric `2 -> 3`; C29 must not duplicate it;
- MUB attack: HARD RESERVE, unrestricted residual lower bound remains `0`, and `11/756` remains only an upper benchmark;
- directed audit: `C29-AUDIT-C30-CUBIC-TENSOR-ZERO-02 = PASS (claim-scoped)`;
- no source-level Conjecture-34 closure and no READY certification.

## 12. Model / scheduler control check

The actual task-control surface exposed in this run still contains title, prompt, schedule, timing mode, enabled state, timezone/notification metadata, but **no model selector and no reasoning-effort selector**. GPT-6/maximum therefore remains requested only, not enforceable from this worker. Enforcing it requires scheduler/backend support or an authorized enclosing runtime that exposes and pins those fields.

The historical `You cannot modify this task` failure is an ownership/permission-context boundary. The legitimate workaround is modification by an authorized owner/admin/coordinator from the task's owning context. Permission bypass or duplicate schedules are not appropriate.

## 13. Status

C29 remains **PARTIAL / PENDING_ADMISSION / NOT READY**. The frozen metric did not move. The five-point supercritical experiment did, however, isolate the genuinely three-dimensional residual obstruction much more sharply: four global support faces are now exactly exposed and locally planar, so any wildness must be generated recursively away from those faces.
