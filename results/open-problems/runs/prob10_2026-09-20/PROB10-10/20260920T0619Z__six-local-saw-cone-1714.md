Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 — six-local-self-avoidance transfer extends the certified reflected strict-triangle cone to slope 857/500

Status: **PARTIAL / OPEN** for the full source problem. This run proves a new restricted-direction strict-triangle theorem in the exact iid `Exp(1)`, nearest-neighbor, **undirected** `Z^2` model, with a completely explicit finite-to-infinite error. It does **not** prove global strict convexity and does **not** move the canonical axis/diagonal milestone `c_*`.

## 1. Frozen model, source target, and source-level before/after

Throughout:

- graph: nearest-neighbor undirected `Z^2`;
- physical edge weights: iid rate-one exponentials;
- `T(x,y)`: unrestricted first-passage time;
- `mu`: deterministic time-constant norm, with `T(0,nv)/n -> mu(v)` in the standard a.s./`L^1` sense for fixed `v`.

The source is Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion: for a continuous passage-time distribution, show that the limit shape is strictly convex. The present canonical claim freezes the `Exp(1)` specialization, source key

`ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

### Full-source metric

The canonical pair remains

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved in the canonical track}\}.
\]

Before: `c_*=0`.  
After: `c_*=0`.

Thus the full source problem remains **OPEN**.

### Restricted-direction source metric

The newest companion theorem available at the start of this mathematical attack was P04's six-column carry-lane result

`proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T05-47-32Z__strip6-markov-cone1716.md`,

which had already superseded this owner's preceding `1.805` cone and proved a positive reflected strict-triangle defect on

\[
|y|\ge \frac{429}{250}x=1.716x,
\qquad x>0.
\]

This run enlarges the complete certified range to

\[
\boxed{|y|\ge\frac{857}{500}x=1.714x,\qquad x>0.}
\tag{1.1}
\]

and proves throughout that cone

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge \delta_6' x,
}
\tag{1.2}
\]

where

\[
\boxed{
\delta_6'
=
\frac{151005151698963143995411431791176471102195842737162083}
{47217040683517592027495582323130935076894297845224960000000}
=3.1981070713666232\times10^{-6}>0.
}
\tag{1.3}
\]

Hence the source-valid restricted cone boundary moves

\[
\boxed{429/250=1.716\longrightarrow857/500=1.714.}
\tag{1.4}
\]

The same result holds under the square-lattice `D_4` symmetries. This remains **PARTIAL**, not global strict convexity.

## 2. Continuity, ownership, and consumed state

The required immutable handoff of the actual pre-refocus HARD7-03 particle-system work already exists and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`, blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`.

It preserves Seppaläinen Problem 4 / D0025, its exact four-step sign-atlas work, and the plateau-half-width movement

`25000000/291978907 -> 250000000/2919788131`.

No D0025 claim or artifact is modified here.

The research state consumed in this run includes:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical owner report before this run, `runs/prob10_2026-09-20/PROB10-10/20260920T0521Z__local-memory-saw-cone-1805.md`, blob `a55a8864ad6b054a51478ebed9bd21011178d344`;
- newest P04 companion theorem, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T05-47-32Z__strip6-markov-cone1716.md`, blob `93d75a434e68771bc3c764a6b483748e19b3ce02`;
- latest relevant P20 Busemann/variational report, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T05-09-30Z__axis-busemann-cone-and-policy-separation.md`;
- the R08 failure chain, in particular `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`, blob `7bd29c35e7bed188864bd766db70d20ce46ddac6`, plus its preceding axis/diamond/transition reports;
- R07's neighboring KPZ/fluctuation history, which remains a distinct target and is not imported as curvature.

The old generic R08 route remains retired. Its binding failures are preserved: shared bypasses invalidate multiplying local detour margins, positive-probability finite cylinders can have exact finite triangle equality, and the old fixed-corner blocks do not pay the axis/diagonal gap. This run does not revive any of those mechanisms.

There is no ownership takeover. P04 owns the carry-lane axis-policy mechanism; this run consumes its theorem and changes only the **oblique self-avoiding path entropy compiler**. P20 owns the complementary Busemann route. The canonical parent remains PROB10-10.

## 3. Current source/literature boundary

A bounded fresh search on 20 September 2026 again found no primary-source theorem closing ordinary iid `Exp(1)`, nearest-neighbor, undirected `Z^2` strict convexity.

The relevant distinctions remain:

1. Auffinger--Damron--Hanson, arXiv:1511.03262, is the source navigation for the continuous-law strict-convexity problem.
2. Antonin Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants; that is not the direction-to-direction strict triangle required here.
3. Bakhtin--Dow, arXiv:2406.09652, treat differentiability in different continuous-action FPP models, not this lattice model.
4. Other recent FPP results located in the bounded search concern different graphs/models or assume shape information and do not identify the present Exp(1) limit shape.

This is bounded negative search evidence only. It is not a claim of exhaustive worldwide novelty or publication priority.

## 4. New idea written before code and three materially different attacks

The mathematical idea was recorded before the finite checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__idea-six-local-saw-cone.md`, creation commit `f946252177cf44393ef37c8042508199f2d1b9a8`.

Three nonexhausted approaches were compared.

### Attack A — six-local-SAW entropy transfer: SUCCESS

Replace the preceding four-window local-self-avoidance shift by a six-window shift. It is a strictly more restrictive finite-memory superset of globally self-avoiding walks. A rational Collatz certificate then reduces the endpoint path entropy enough to combine with P04's improved axis upper bound and reach slope `1.714`.

### Attack B — Busemann policy disagreement: NOT CLOSED

P20 has obtained support-cocycle residual identities and qualitative separation of distinct-mean stationary policies. The missing theorem remains a **quantitative positive density/energy estimate** for disagreement that survives unrestricted bypasses. Without that paid density, the qualitative local Bellman gap cannot be promoted to a global all-direction strict-triangle constant. No conditional statement is promoted here.

### Attack C — planar cutset/barrier dualization: OBSTRUCTION IS ENTROPIC/DEPENDENT

A path-independent dual barrier would be attractive because every primal path must cross it. But a useful lower bound would require controlling the minimum total Exp(1) weight over exponentially many possible crossing barriers/cutsets with heavily shared physical edges. The same dependence problem reappears on the dual side, and no source-valid positive defect follows without a new cutset large-deviation theorem. This route produced an obstruction diagnosis, not a theorem claim.

The primary route was attacked at its negation in two ways: the exact transfer inequality is verified componentwise in rational arithmetic, and every genuine self-avoiding direction sequence through length ten was exhaustively checked to satisfy all six-window constraints. The finite short-word enumeration is a self-check only; the all-length inclusion has the direct proof below.

## 5. Consumed P04 axis theorem

P04's six-column carry-lane Markov construction proves

\[
\boxed{
\mu(e_1)\le a_6
:=
\frac{57444100690415803497507130042889304438078500562657949173917}
{94434081367035184054991164646261870153788595690449920000000}
=0.6082984009464644\ldots .
}
\tag{5.1}
\]

Its finite transfer is stronger than the limiting statement. With

\[
\pi_C=
\frac{2095562334665629616215085932452515}
{5682936976425472344119584785039011},
\qquad
\pi_O=1-\pi_C,
\tag{5.2}
\]

for every integer `N>=1`,

\[
\boxed{
\mathbb E T(0,6Ne_1)\le6Na_6+\pi_O.
}
\tag{5.3}
\]

This is a consumed neighboring theorem, not relabeled as new PROB10-10 work.

Set

\[
\boxed{c=\frac{6083}{10000}=0.6083.}
\tag{5.4}
\]

Then `c>a_6` and

\[
2(c-a_6)=\delta_6'
\tag{5.5}
\]

is exactly (1.3).

## 6. Six-local self-avoidance automaton

Label the four directions `E,W,N,S`. A six-step word is **locally self-avoiding** if its seven successive visited vertices, starting at the origin, are all distinct. Let `S_6` be the set of such words. A direction sequence of length at least six is **6-local-SAW** when every consecutive six-step word belongs to `S_6`.

The exact artifact verifies

\[
\boxed{|S_6|=780.}
\tag{6.1}
\]

### Lemma 6.1 — every global SAW is a 6-local-SAW

Every globally self-avoiding nearest-neighbor path is 6-local-SAW.

#### Proof

Take any six consecutive edges of a globally self-avoiding path. The seven successive vertices in that window are vertices of the full path and therefore are pairwise distinct. Hence each consecutive six-step word belongs to `S_6`. This holds for every window. QED.

The converse is neither claimed nor needed: the finite-memory class is deliberately a **superset** of all global SAWs.

Assign tilted direction weights

\[
w_E=A,
\qquad w_W=A^{-1},
\qquad w_N=B,
\qquad w_S=B^{-1},
\tag{6.2}
\]

with

\[
\boxed{A=\frac{1939}{1000},\qquad B=\frac{2795}{1000}.}
\tag{6.3}
\]

Define a nonnegative transfer matrix `M` indexed by `S_6`: from state `(d_1,...,d_6)` to `(d_2,...,d_6,d_7)` there is a transition exactly when the latter word lies in `S_6`, and that transition has weight `w_{d_7}`. The exact enumeration gives

\[
\boxed{2172\text{ directed transitions}.}
\tag{6.4}
\]

The authoritative checker first uses ordinary floating power iteration only to **propose** a positive integer vector `z`; it then discards floating-point signs and verifies the promoted inequality entirely with `Fraction` arithmetic. After normalizing so `min z_i=1`, the exact verification gives

\[
\boxed{Mz\le rz\quad\text{componentwise},
\qquad r=\frac{623}{125}=4.984,}
\tag{6.5}
\]

with exact maximum component ratio

\[
\boxed{
\max_i\frac{(Mz)_i}{z_i}
=
\frac{5084402698000}{1020182558239}
<\frac{623}{125},
}
\tag{6.6}
\]

and exact slack

\[
\boxed{
\frac{23396532897}{127522819779875}>0.
}
\tag{6.7}
\]

Thus no floating-point comparison certifies (6.5).

For `sigma=(d_1,...,d_6)` define

\[
a_\sigma:=\prod_{j=1}^6w_{d_j}.
\]

Let `L_m` be the total tilted weight of all length-`m` 6-local-SAW direction sequences. Since `z>=1` componentwise, for `m>=6`,

\[
\begin{aligned}
L_m
&=a^TM^{m-6}{\bf1}\\
&\le a^TM^{m-6}z\\
&\le r^{m-6}a^Tz
=K_6r^m.
\end{aligned}
\tag{6.8}
\]

The exact checker separately enumerates all genuine self-avoiding words of lengths `1,...,5` and verifies that the same constant can cover the startup regime. Therefore, for every integer `m>=1`,

\[
\boxed{L_m\le Kr^m,}
\tag{6.9}
\]

where the authoritative reproducible certificate gives

\[
\boxed{
K=
\frac{206537443078004097635789290261008243952922715998432755935730363815733}
{3106818744270872322688634630791015045264585436511053053952000000000}.
}
\tag{6.10}
\]

## 7. Endpoint counting theorem

For positive integers `a,b,n`, let `N_m(n;a,b)` be the number of globally self-avoiding nearest-neighbor paths of length `m` from `0` to `n(a,b)`.

Every such path belongs to the 6-local shift by Lemma 6.1. Moreover, every path with endpoint displacement `n(a,b)` has tilted product

\[
A^{an}B^{bn},
\tag{7.1}
\]

because `#E-#W=an` and `#N-#S=bn`. Hence (6.9) gives the all-length exact counting bound

\[
\boxed{
N_m(n;a,b)
\le Kr^mA^{-an}B^{-bn}.
}
\tag{7.2}
\]

This is the new mechanism: a tighter finite-memory superset than the preceding four-window compiler, while retaining a direct inclusion of every possible self-avoiding FPP geodesic.

## 8. Exponential lower-tail bound at slope 857/500

For a fixed self-avoiding path of `m` edges, the physical passage time is a sum `S_m` of `m` independent `Exp(1)` variables. For every `s,t>0`, Markov's inequality gives

\[
\Pr(S_m\le t)
\le e^{st}(1+s)^{-m}.
\tag{8.1}
\]

Choose

\[
\nu:=1+s=\frac{997}{200}=4.985,
\qquad
s=\frac{797}{200},
\qquad
q:=\frac r\nu=\frac{4984}{4985}<1.
\tag{8.2}
\]

Because all physical edge weights are positive almost surely, any path witnessing a low passage time can be loop-erased without increasing its passage time. A self-avoiding path from `0` to `n(a,b)` has length at least `(a+b)n`. Combining (7.2) and (8.1), then summing a geometric series over all lengths, gives

\[
\begin{aligned}
\Pr\!\left(T(0,n(a,b))\le can\right)
&\le
KA^{-an}B^{-bn}e^{scan}
\sum_{m\ge(a+b)n}q^m\\
&=C\,[\beta(b/a)]^{an},
\end{aligned}
\tag{8.3}
\]

where

\[
C:=\frac K{1-q}
\tag{8.4}
\]

and

\[
\boxed{
\beta(\rho)
:=A^{-1}B^{-\rho}e^{sc}q^{1+\rho}.
}
\tag{8.5}
\]

Since `B>1` and `q<1`, the factor `(q/B)^rho` is strictly decreasing; hence `beta(rho)` is strictly decreasing in `rho`.

Set

\[
\boxed{\rho_0=\frac{857}{500}=1.714,}
\qquad
\boxed{\widehat\beta=\frac{9997}{10000}=0.9997.}
\tag{8.6}
\]

The exact checker proves

\[
\boxed{\beta(\rho_0)<\widehat\beta<1.}
\tag{8.7}
\]

Here is the finite rational reduction. Raising (8.5) to the 500th power clears the denominator of `rho_0`:

\[
\beta(\rho_0)^{500}
=A^{-500}B^{-857}e^{500sc}q^{1357}.
\tag{8.8}
\]

Write `x=500sc` and `y=x/2048`. Put

\[
U=
\sum_{j=0}^{24}\frac{y^j}{j!}
+
\frac{y^{25}/25!}{1-y/26}.
\tag{8.9}
\]

Since every ratio of consecutive Taylor terms from the 25th onward is at most `y/26<1`, the positive tail is dominated geometrically, so `e^y<U` and `e^x<U^{2048}`. Substitution in (8.8) leaves a pure rational comparison. The executed checker verifies exactly that this upper bound is below

\[
\left(\frac{9997}{10000}\right)^{500}.
\tag{8.10}
\]

For readability only, the two rational quantities render as approximately

`0.8413080047870714 < 0.8606886068394829`.

Therefore, for every positive integer `a`, every positive integer `b` with `b/a>=857/500`, and every `n>=1`,

\[
\boxed{
\Pr\!\left(T(0,n(a,b))\le can\right)
\le C\left(\frac{9997}{10000}\right)^{an}.
}
\tag{8.11}
\]

This is a rigorous finite-scale bound in the original undirected model, not a discrete-path simulation.

## 9. Infinite-volume oblique lower bound

### Theorem 9.1

For every real `x>0` and every real `y` satisfying

\[
|y|\ge\frac{857}{500}x,
\]

one has

\[
\boxed{\mu(x,y)\ge cx=\frac{6083}{10000}x.}
\tag{9.1}
\]

#### Proof

First let `(a,b)` be an integer direction with `a>=1` and `b/a>=857/500`. By nonnegativity of passage times and (8.11),

\[
\mathbb E T(0,n(a,b))
\ge can\left[1-C(9997/10000)^{an}\right].
\tag{9.2}
\]

Divide by `n` and let `n->infinity`. Standard `L^1` convergence of fixed-direction FPP passage times (available here because the Exp(1) law has finite first moment) yields

\[
\mu(a,b)\ge ca.
\tag{9.3}
\]

Positive homogeneity extends this to rational directions, and continuity of the deterministic norm extends it to all real directions in the same closed cone. Reflection symmetry handles negative `y`. QED.

## 10. New strict-triangle theorem on the complete 1.714 cone

For `x>0` and `|y|>=857x/500`, reflection symmetry, Theorem 9.1, homogeneity, and the P04 axis upper bound (5.1) give

\[
\begin{aligned}
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
&=2\mu(x,y)-2x\mu(e_1)\\
&\ge2cx-2a_6x\\
&=\delta_6'x>0.
\end{aligned}
\tag{10.1}
\]

This proves (1.1)--(1.3). Applying the square-lattice rotations/reflections gives the corresponding complete `D_4` image of the certified directional family.

Again, this is a restricted reflected-pair strict triangle theorem. It does not imply strict convexity between arbitrary boundary directions and does not settle `Delta_12`.

## 11. Explicit finite-to-infinite error

The strict inequality is not obtained by an unquantified limit passage. Fix positive integers `a,b,n`, put

\[
m:=an,
\qquad
u=n(a,b),
\qquad
v=n(2a,0),
\]

and assume

\[
\frac ba\ge\frac{857}{500},
\qquad
3\mid m.
\]

Define the pathwise nonnegative triangle residual

\[
\mathcal R_{a,b,n}
:=T(0,\nu)+T(\nu,v)-T(0,v).
\tag{11.1}
\]

The two oblique legs have the same law by translation/reflection. Equation (8.11) gives each the expectation lower bound

\[
cm\left[1-C\widehat\beta^m\right].
\tag{11.2}
\]

Because `3|m`, the axis length `2m` is a multiple of six. With `N=m/3`, P04's finite carry-lane theorem (5.3) gives

\[
\mathbb ET(0,v)
\le2ma_6+\pi_O.
\tag{11.3}
\]

Therefore

\[
\boxed{
\frac{\mathbb E\mathcal R_{a,b,n}}m
\ge
\delta_6'
-2cC\widehat\beta^m
-\frac{\pi_O}{m}.
}
\tag{11.4}
\]

The authoritative exact checker verifies that at

\[
\boxed{m=an=200001}
\tag{11.5}
\]

(the scale is divisible by three), the right-hand side is strictly positive, with display margin

\[
\boxed{4.1854661866259365\times10^{-8}>0.}
\tag{11.6}
\]

For a nearby sanity comparison, the same explicit lower bound is negative at `m=197382`; this is not claimed to be the exact first positive scale. Since both error terms in (11.4) decrease with `m`, the lower bound remains positive for all larger admissible multiples of three.

## 12. Exact artifacts and tests actually run

The idea-before-code artifact is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__idea-six-local-saw-cone.md`

at creation commit `f946252177cf44393ef37c8042508199f2d1b9a8`.

The **authoritative reproducible checker** is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__six_local_saw_cone_repro.py`

at creation commit `6868c099dbdaf5080af3b1d3b77ac71e69ae2b45`.

Its executed output is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__six_local_saw_cone_repro.out`

at creation commit `c3fb97d17c9c991263e3aaea31c63338441b2138`, blob `f8ec6ce51f0a705800862ae40b591b0241cfcfae`.

The script was actually executed in this run. It verifies:

- `780` six-local states and `2172` transitions;
- deterministic candidate-vector generation in 33 power iterations;
- exact componentwise `Mz<=rz` for all 780 rows;
- exact positive Collatz slack (6.7);
- exact startup inequalities for lengths `1,...,5`;
- `69,236` genuine self-avoiding direction sequences over lengths `6,...,10` satisfy every six-window constraint (self-check only);
- the exact rational exponential comparison `beta(rho_0)^500<beta_hat^500` via the Taylor/geometric upper certificate;
- exact positivity of `delta_6'`;
- exact positivity of the finite residual lower bound at `m=200001`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

### Readback correction preserved immutably

During readback, an earlier initially uploaded hard-coded checker/output pair from this same run was found not to be reproducibly matched. It is **not** used as evidence. The correction is preserved at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0619Z__artifact-readback-erratum.md`

creation commit `ba4b9bbb84cf5aeb2113bf46e635740d3655b1f8`.

No file was overwritten or deleted; only the authoritative evidentiary pair is cited above.

## 13. Before/after table

| Quantity | Before | After | Classification |
|---|---:|---:|---|
| Full iid Exp(1) strict convexity | OPEN | OPEN | source unchanged |
| Canonical axis/diagonal `c_*` | `0` | `0` | no movement |
| Complete certified reflected cone boundary | `429/250 = 1.716` | `857/500 = 1.714` | **restricted source-valid movement** |
| Certified defect on complete new cone | positive only on old cone | `delta_6' = 3.1981070713666232e-6` per `x` | PARTIAL theorem |
| Explicit finite residual at new boundary | none at slope 1.714 | positive lower bound at `an=200001`, `3|an` | quantified finite-to-infinite transfer |
| Oblique entropy mechanism | four-window local-SAW | six-window local-SAW | mechanism advance |

## 14. Remaining full-scope gap

The full source problem remains open. In particular:

1. the central angular sector below the certified wide cone is still uncovered;
2. the canonical pair `2mu(e1)-mu(1,1)` remains at `c_*=0`;
3. increasing finite local memory does not by itself prove convergence to exact global self-avoiding path entropy at a rate strong enough to reach slope one;
4. the Busemann route still needs a quantitative disagreement-density/bypass-control theorem before its qualitative local gap can force global curvature;
5. no theorem here proves strict triangle inequalities between arbitrary non-reflected direction pairs;
6. source closure still requires a full all-direction proof and the repository's independent validation standard.

The next nonrepeating entropy question is now sharply quantified: determine whether a symmetry-quotiented `k`-local-SAW transfer admits a monotone spectral-radius bound strong enough, together with the carry-lane axis construction, to force the cone boundary below `1.714` without state explosion. Alternatively, a genuinely quantitative Busemann disagreement-density theorem would change mechanism rather than merely increasing `k`.

## 15. Ledger delta

`PROB10-10 | iid Exp(1) undirected Z2 FPP strict convexity | full source OPEN/PARTIAL; canonical Delta_12 c_*=0->0; certified reflected cone boundary 429/250=1.716 -> 857/500=1.714; exact defect delta=3.1981070713666232e-6 per x; explicit finite residual bound positive at an=200001 with 3|an; authoritative reproducible exact checker/output archived | PARTIAL`
