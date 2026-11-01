Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but the available scheduler exposes no authenticated model/effort selector, so I do not claim GPT-6 maximum.**

# PROB10-10 — ten-local self-avoidance plus critical Chernoff envelope extends the certified reflected strict-triangle cone to slope 1.701

Status: **PARTIAL / OPEN** for the full source problem. This run proves a new restricted-direction strict-triangle theorem in the exact iid `Exp(1)`, nearest-neighbor, **undirected** `Z^2` model, with an explicit finite-to-infinite error. It does **not** prove global strict convexity and does **not** move the canonical axis/diagonal metric `c_*`.

## 1. Frozen target and before/after metrics

Let `T(x,y)` be ordinary undirected first-passage time on nearest-neighbor `Z^2` with iid rate-one exponential **physical-edge** weights, and let `mu` be the deterministic time-constant norm.

The primary source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in §2.5.1:

> Show that if `F` is a continuous distribution then the limit shape is strictly convex.

The canonical repository specialization fixes `F=Exp(1)` and source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

### Full-source metric

`Delta_12 = 2 mu(e1)-mu(1,1)` and

`c_* = sup{c>=0 : Delta_12>=c is rigorously proved in the canonical track}`.

- before: `c_*=0`;
- after: `c_*=0`.

So the full source problem remains **OPEN**.

### Restricted-direction source scope

The current canonical-owner report before this run covered `|y|>=1.714x`; after it, the neighboring P04 dependence-controlled seven-column carry theorem improved the best source-valid reflected cone to

`|y| >= (851/500)x = 1.702x`.

This run proves the same type of strict triangle inequality on the strictly larger region

\[
\boxed{|y|\ge {1701\over1000}x=1.701x,\qquad x>0.}
\]

Thus the best rigorously certified cone boundary available to this run moves

\[
\boxed{1.702\longrightarrow1.701.}
\]

At the new boundary the proved infinite-volume defect coefficient is

\[
\boxed{
\delta_{10}
={1973416083960923021874452401998106331461319398579762932822539086030736203
\over
40728440964182459862726508951394412059439107301863351352996476614656000000000}
=4.845302293049692\times10^{-5}>0.
}
\]

This is **PARTIAL**, not global strict convexity.

## 2. Continuity, ownership, handoff, and consumed state

The required pre-refocus HARD7-03 handoff was already written immutably and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`, blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`.

It preserves the actual Seppäläinen/D0025 particle-system target, four-step sign atlas, artifacts, and plateau half-width movement

`25000000/291978907 -> 250000000/2919788131`.

No D0025 file or claim is changed here.

State consumed before the mathematical attack:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- canonical `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical owner report `runs/prob10_2026-09-20/PROB10-10/20260920T0619Z__six-local-saw-cone-1714.md`;
- its artifact-readback erratum and authoritative reproducible six-local checker;
- newest neighboring P04 report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T06-53-21Z__strip7-carry-cone1702.md`;
- newest neighboring P20 report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T06-25-00Z__critical-chernoff-busemann-barrier.md`;
- R08 stuck report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md` and its earlier axis/diamond/transition chain;
- R07 neighboring KPZ report `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`, kept separate because fluctuation/overlap bounds are not curvature theorems.

The R08 failure history remains binding: shared bypasses invalidate multiplication of local surgery gains; positive-probability finite cylinders can have exact finite triangle equality; and the old fixed-corner blocks did not pay the axis/diagonal gap. None of those routes is restarted here.

Ownership remains nonduplicating. P04 owns the axis carry-lane block mechanism; P20 owns the Busemann/variational companion route. This run changes the **oblique self-avoiding-path entropy compiler** only and consumes P04's new axis theorem without relabeling it.

## 3. Current-source check

A bounded fresh literature check on 20 September 2026 recovered no theorem closing ordinary iid `Exp(1)` nearest-neighbor undirected `Z^2` strict convexity.

Relevant scope checks:

1. Auffinger--Damron--Hanson, arXiv:1511.03262, still states Question 4 as above and §2.8 treats strict convexity as conjectural.
2. Dembin--Elboim--Peled, arXiv:2204.02332, prove quantitative planar coalescence under the extra hypothesis that the limit shape has more than 32 extreme points; this does not establish the needed shape property for Exp(1).
3. Antonin Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants; that is not a direction-to-direction strict triangle inequality for the ordinary undirected norm.
4. Bakhtin--Dow, arXiv:2406.09652, concern different continuous-action FPP models.

This is bounded negative search evidence only, not an exhaustive novelty or priority claim.

## 4. Idea-before-code and three materially different attacks

The idea was persisted before the checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0722Z__idea-seven-local-saw-critical-envelope.md`, creation commit `4e9ec4a8f70b968ae4b56c3df128caf01cf694da`.

The computational exploration immediately showed an important negation result: seven-local memory has essentially the same recurrent Perron obstruction as six-local memory and does not materially improve the optimized cone. I therefore did **not** file a renamed seven-local lemma. I pushed the memory length to ten, where new loop exclusions finally lower the certified transfer growth enough to move the theorem.

Three genuinely different attacks were considered:

### Attack A — higher-memory global path entropy / Perron extremal certificate: SUCCESS

Replace the six-local superset by the ten-local self-avoidance shift and optimize the source-relevant critical slope rather than the raw spectral radius. This produces the theorem below.

### Attack B — irreducible bridge/renewal decomposition: NOT CLOSED

A Hammersley--Welsh-style decomposition would count endpoint-directed self-avoiding competitors by irreducible bridges instead of a local Markov superset, potentially eliminating the large startup constant `K`. The obstruction is that the needed **explicit drift-sensitive generating-function bound** for irreducible bridges is not presently available with a certified numerical value sharp enough to combine with `a_7`. Replacing it by the ordinary connective-constant upper bound loses the endpoint tilt and is weaker than Attack A. No theorem is claimed from this route.

### Attack C — two-support Busemann residual density: NOT CLOSED

P20's exact cocycle residual identity and outer-cone barrier show that an axis-support residual metric has positive macroscopic cost in the already certified cone. To propagate strictness inward by interpolating a second support cocycle one needs a quantitative lower density of locations where the two zero-residual policies cannot coincide. Existing qualitative policy separation does not pay that density, and importing a curvature/coalescence hypothesis would be circular. No conditional strict-convexity statement is promoted.

Thus this run changed method after the seven-local negation test **within the same problem** and spent the main effort on the ten-local theorem, rather than filing another unchanged certificate.

## 5. Consumed axis theorem

P04's seven-column carry-lane construction proves

\[
\boxed{
\mu(e_1)\le a_7
={49279440150576815510877201378785240485589858515856075374192914164647729263797
\over
81456881928364919725453017902788824118878214603726702705992953229312000000000}
=0.6049757734885347\ldots .
}
\tag{5.1}
\]

More precisely, for every `N>=1`,

\[
\mathbb E T(0,7Ne_1)\le7Na_7+\pi_O,
\tag{5.2}
\]

with

\[
\pi_O={40379780780386028600356821383956979806106624
\over63945812674576825594122899689798242883976669}
=0.6314687247135412\ldots .
\tag{5.3}
\]

This is a consumed neighboring theorem, not new PROB10-10 work.

## 6. Ten-local self-avoidance transfer

Label directions `E,W,N,S`. A ten-step word is **10-local self-avoiding** when its eleven successive visited vertices, beginning at the origin, are all distinct. Let `S_10` be the set of such words. A direction sequence is 10-local-SAW if every consecutive ten-step window lies in `S_10`.

### Lemma 6.1 — every global SAW is 10-local-SAW

Every globally self-avoiding nearest-neighbor path is 10-local-SAW.

**Proof.** Any ten consecutive edges of a globally self-avoiding path visit eleven vertices of the global path, hence those eleven vertices are pairwise distinct. This holds for every window. QED.

The exact checker enumerates

\[
\boxed{|S_{10}|=44100}
\tag{6.1}
\]

with `120292` directed window transitions; `200` states are terminal dead ends, which are harmless because the Collatz vector below is strictly positive on **all** states.

Choose tilted step weights

\[
A={3889\over2000}=1.9445,
\qquad
B={27893\over10000}=2.7893,
\tag{6.2}
\]

and

\[
w_E=A,\quad w_W=A^{-1},\quad w_N=B,\quad w_S=B^{-1}.
\tag{6.3}
\]

Let `M` be the `S_10` transfer matrix whose transition appending direction `d` has weight `w_d`.

The checker uses floating arithmetic only to **propose** a positive integer vector `z`; every promoted inequality is then recomputed with exact rational arithmetic. It verifies

\[
z_i\ge1\quad\text{for every state }i,
\tag{6.4}
\]

and

\[
\boxed{Mz\le r z\quad\text{componentwise},
\qquad r={1993\over400}=4.9825.}
\tag{6.5}
\]

The exact worst component ratio is

\[
\boxed{
\max_i{(Mz)_i\over z_i}
={219062408375000\over43967001728347}
< {1993\over400},
}
\tag{6.6}
\]

with exact slack

\[
\boxed{{1271094595571\over17586800691338800}>0.}
\tag{6.7}
\]

No floating sign certifies (6.5).

For a state `sigma=(d_1,...,d_10)` put

\[
a_\sigma=\prod_{j=1}^{10}w_{d_j}.
\]

Let `L_m` be the total tilted weight of all length-`m` 10-local-SAW direction sequences. For `m>=10`, since `z>=1`,

\[
L_m
=a^TM^{m-10}{\bf1}
\le a^TM^{m-10}z
\le r^{m-10}a^Tz
=K_{10}r^m.
\tag{6.8}
\]

The checker separately enumerates genuine SAWs for `m=1,...,9` and verifies that the same constant covers startup. Therefore, for every `m>=1`,

\[
\boxed{L_m\le K r^m,}
\tag{6.9}
\]

with exact rational `K` generated by the checker and

`K = 1.0326732670567583e14...`.

The large `K` affects only the explicit finite scale, not the infinite-volume exponent.

## 7. Endpoint-count theorem

For positive integers `a,b,n`, let `N_m(n;a,b)` be the number of globally self-avoiding `m`-edge paths from `0` to `n(a,b)`.

By Lemma 6.1 each such path is in the 10-local class. Every path to `n(a,b)` has the same tilted product

\[
A^{an}B^{bn},
\tag{7.1}
\]

because `#E-#W=an` and `#N-#S=bn`. Hence its contribution to `L_m` is exactly that product. From (6.9),

\[
N_m(n;a,b)A^{an}B^{bn}\le Kr^m,
\]

so

\[
\boxed{
N_m(n;a,b)\le Kr^mA^{-an}B^{-bn}.
}
\tag{7.2}
\]

This is an all-length theorem; it is not inferred from finite path sampling.

## 8. Exponential lower tail at slope 1.701

Choose

\[
s={398251\over100000}=3.98251,
\qquad
q={r\over1+s}={498250\over498251}<1,
\tag{8.1}
\]

and

\[
c={121\over200}=0.605,
\qquad
\rho_0={1701\over1000}=1.701.
\tag{8.2}
\]

Fix integers `a,b,n>0`, set `rho=b/a`, and write `M=an` for the horizontal displacement scale. For a fixed `ell`-edge self-avoiding path, its passage time is `Gamma(ell,1)`. Markov's inequality applied to `exp(-s Gamma)` gives

\[
\mathbb P(\Gamma(\ell,1)\le cM)
\le e^{scM}(1+s)^{-\ell}.
\tag{8.3}
\]

All passage times are positive, so a geodesic may be chosen globally self-avoiding. Every path to `n(a,b)` has `ell>=(a+b)n=(1+rho)M`. Union bound plus (7.2) yields

\[
\begin{aligned}
\mathbb P(T(0,n(a,b))\le cM)
&\le K A^{-M}B^{-\rho M}e^{scM}
\sum_{\ell\ge(1+\rho)M}q^\ell\\
&\le C\,[A^{-1}B^{-\rho}e^{sc}q^{1+\rho}]^M,
\end{aligned}
\tag{8.4}
\]

where

\[
C={K\over1-q}=5.145304879842969\times10^{19}\ldots .
\tag{8.5}
\]

Define

\[
\beta(\rho)=A^{-1}B^{-\rho}e^{sc}q^{1+\rho}.
\tag{8.6}
\]

Since `B>1` and `0<q<1`, `beta(rho)` is strictly decreasing in `rho`.

### Exact certification of `beta(rho_0)<2499/2500`

For `x>1`, put `z=(x-1)/(x+1)`. Then

\[
\log x=2\sum_{k\ge0}{z^{2k+1}\over2k+1}.
\tag{8.7}
\]

A finite partial sum is a rational lower bound. The positive tail after the term `2N+1` is at most

\[
{2z^{2N+3}\over(2N+3)(1-z^2)}.
\tag{8.8}
\]

The checker applies (8.7)--(8.8) with exact `Fraction` arithmetic to `A`, `B`, `1/q`, and `2500/2499`. It proves

\[
\log\beta(\rho_0)
\le -0.00046167234256995905\ldots
< -0.0004000800213397354\ldots
\le \log(2499/2500).
\tag{8.9}
\]

Thus

\[
\boxed{\beta(\rho)\le\beta(\rho_0)<{2499\over2500}}
\quad\text{for every }\rho\ge\rho_0.
\tag{8.10}
\]

Therefore

\[
\mathbb P(T(0,n(a,b))\le cM)
\le C(2499/2500)^M.
\tag{8.11}
\]

Since passage times are nonnegative,

\[
\mathbb ET(0,n(a,b))
\ge cM[1-C(2499/2500)^M].
\tag{8.12}
\]

Divide by `n` and let `n->infinity`. The exponential error vanishes, giving

\[
\boxed{\mu(a,b)\ge ca\qquad\text{whenever }b/a\ge1701/1000.}
\tag{8.13}
\]

By homogeneity this holds for rational positive directions, and by continuity of the time-constant norm it extends to every real `x>0`, `y/x>=1701/1000`. Reflection symmetry gives the same bound for negative `y`.

## 9. Restricted strict-triangle theorem

### PROB10-10-TENLOCAL-CONE1701-1 — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and every real `y` satisfying

\[
|y|\ge {1701\over1000}x,
\]

one has

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge\delta_{10}x>0,
}
\tag{9.1}
\]

with `delta_10` displayed in §1.

**Proof.** Section 8 gives

\[
\mu(x,y)\ge cx,
\qquad
\mu(x,-y)\ge cx.
\]

The consumed P04 theorem gives

\[
\mu(2x,0)=2x\mu(e_1)\le2a_7x.
\]

Hence

\[
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge2(c-a_7)x
=\delta_{10}x>0.
\]

The checker verifies the exact rational positivity of `delta_10`. QED.

Square-lattice `D_4` symmetries give the corresponding rotated/reflected cones. This is a genuine infinite-volume strict triangle inequality for a complete directional range, but it is still only a restricted range and does not settle global strict convexity.

## 10. Explicit finite-to-infinite error

Let positive integers `a,b,n` satisfy `b/a>=1701/1000`, set `M=an`, and suppose `7|M`. Define

\[
R_{a,b,n}
=T(0,n(a,b))
+T(n(a,b),n(2a,0))
-T(0,n(2a,0)).
\tag{10.1}
\]

Translation/reflection makes the first two expectations equal. Equations (8.12) and the consumed finite P04 axis block estimate (5.2), with `2M` tiled by seven-column blocks, give

\[
\boxed{
{\mathbb E R_{a,b,n}\over M}
\ge
\delta_{10}
-2cC(2499/2500)^M
-{\pi_O\over M}.
}
\tag{10.2}
\]

This is the requested explicit finite-to-infinite error; no unproved convergence rate is inserted.

At

\[
\boxed{M=140000=7\cdot20000,}
\]

the exact checker proves the right-hand side of (10.2) is positive, specifically

\[
\boxed{
{\mathbb E R_{a,b,n}\over M}
\ge1.4509154468418064\times10^{-5}>0.
}
\tag{10.3}
\]

The sign is genuinely checked rather than hard-coded: at the nearby smaller multiple `M=138600`, the same displayed lower bound is still negative (`-7.637006200947267e-6`).

## 11. Tests actually run

Idea-before-code artifact:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0722Z__idea-seven-local-saw-critical-envelope.md`.

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0722Z__ten_local_saw_cone_exact.py`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0722Z__ten_local_saw_cone_exact.out`.

The checker actually executed. It verifies, with exact rational arithmetic after candidate generation:

- `44100` ten-local states, `120292` transitions and `200` dead-end states;
- the all-state Collatz inequality with exact worst ratio (6.6) and slack (6.7);
- startup SAW weights through length nine;
- the exact logarithmic inequality proving `beta(rho_0)<2499/2500`;
- positivity of `delta_10`;
- positivity of the explicit finite residual lower bound at `M=140000`;
- negativity of the same lower bound at `M=138600` as a nearby negation/sensitivity test.

Archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check, not an independent audit.

## 12. What changed and what did not

### Source-level

- Full strict convexity: **no closure**.
- Canonical axis/diagonal `c_*`: `0 -> 0`.
- Best certified reflected strict-triangle cone visible at the start of this run: boundary `1.702`.
- After: boundary `1.701`.

### Auxiliary/mechanism progress

- Six/seven-local recurrence was tested and found effectively saturated for this purpose; no redundant seven-local theorem was filed.
- Ten-local memory excludes additional finite loops and admits a fully exact all-state Collatz certificate with `r=4.9825`.
- New defect at slope `1.701`: `delta_10=4.845302293049692e-5`.
- Explicit finite normalized residual at `M=140000`: at least `1.4509154468418064e-5`.

## 13. Remaining full-scope gap

The full source problem is still wide open inside the uncovered central angular region. In particular this method does not prove

\[
2\mu(e_1)>\mu(1,1),
\]

so `c_*=0` remains the canonical axis/diagonal status.

For this entropy-plus-axis mechanism, merely increasing the local memory again is now a diminishing-return route: the finite-state transfer growth is already close to the optimized recurrent obstruction, and the missing angular distance to the diagonal is enormous compared with the latest `0.001` cone gain. A future unchanged run should therefore **not** simply file an eleven-local variant unless it gives a qualitatively larger movement. The two genuinely different unresolved routes are:

1. a drift-sensitive irreducible-bridge/renewal bound that beats the finite-memory path entropy by a macroscopic amount; or
2. a Busemann two-support disagreement-density theorem that converts P20's qualitative support separation into a paid positive density and can propagate strictness inward.

Status remains **PARTIAL / OPEN** pending complete source proof and independent validation.
