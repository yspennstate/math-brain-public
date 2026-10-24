Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P04 T10 — exact ladder transfer plus non-backtracking entropy gives a positive wide-cone strict-triangle defect

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Parent source: Auffinger–Damron–Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4.  
Model: nearest-neighbor **undirected** FPP on `Z^2`, iid physical-edge weights `Exp(1)`.  
Status after this run: **PARTIAL / OPEN** for full strict convexity, with a new proved positive strict-triangle defect on an explicit continuum family of direction pairs.

## 0. Immutable handoff of the actual preceding P04 target

The preceding P04 assignment was not an FPP problem. Its last immutable state is

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T13-49-33Z__rotation-stop-disabled.md`.

That report preserves intake `I0101`, Bandeira Randomstrasse Conjecture 27, as **PARTIAL / source OPEN**, with exact finite prime frontier `4177` and retained tested domain

`{149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177}`.

Its six-run rotation was complete. The earlier personal squared-ridge/kernel package is retired and is not reopened here. The 20 September owner directive explicitly reassigns P04 to T10, block-to-infinite-volume FPP curvature transfer. This section is the handoff; no old claim is overwritten or duplicated.

There was no substantive T10 report under `proofnet24/P04-progress-curvature` before this run, as also recorded by the latest P20 reports. Thus this is the first substantive P04 report under the new root.

## 1. Source-level before/after and the P04 metric

Write `T(x,y)` for unrestricted passage time and `mu(v)` for the deterministic time constant. The full ADH target asks for strict convexity of the whole limit shape. That remains open here.

The canonical PROB10-10 owner has tracked the axis/diagonal defect

`Delta_12 = 2 mu(e1) - mu(1,1)`.

The current canonical value remains `c_*=0`; this report does **not** claim movement of that separate frozen pair.

P04's complementary metric in this assignment is the largest proved normalized strict-triangle defect together with its finite-to-infinite error and covered direction regime. Define

\[
\delta_{\mathrm{cone}}
:=\inf_{x>0,\ |y|\ge 2x}
\frac{\mu(x,y)+\mu(x,-y)-\mu(2x,0)}{x}.
\]

Convexity alone gives the baseline lower bound `0`.

**Before this run:** `delta_cone >= 0`; no positive P04 T10 defect was proved.  
**After this run:**

\[
\boxed{
\delta_{\mathrm{cone}}
\ge
\delta_0
:=
\frac{4205821060533084403286315129903}
{98851960802417339252736000000000}
=0.04254666297353036\ldots
>
\frac1{24}.
}
\tag{1.1}
\]

Thus, in particular,

\[
\boxed{
\mu(1,2)+\mu(1,-2)-\mu(2,0)>\frac1{24}.
}
\tag{1.2}
\]

By the `D_4` symmetries of iid square-lattice FPP, the same theorem holds for all simultaneous rotations/reflections of these pairs. This is a **restricted-direction PARTIAL theorem**, not full strict convexity.

The finite-to-infinite ingredients have explicit errors:

1. the axis ladder-block upper transfer has **zero asymptotic/interface error in expectation**: for every `N>=1`,
   \[
   \frac{\mathbb E T(0,6N e_1)}{6N}\le a_0,
   \tag{1.3}
   \]
   with exact `a_0` below;
2. the cone lower transfer has the explicit exponential failure estimate
   \[
   \mathbb P\!\left(T(0,n(a,b))\le \frac23 an\right)
   \le C_0\,\beta_+^{an}
   \tag{1.4}
   \]
   for every integer `a>=1`, `b>=2a`, `n>=1`, where
   \[
   C_0=\frac{27865448}{206955}<135,
   \qquad
   \beta_+
   =\frac{713425217726611388616507115106921327}
   {740604339057582092285156250000000000}
   <0.963302<1.
   \tag{1.5}
   \]

The rest of the report proves these statements completely.

## 2. Essential continuity and nonduplication

I read the current canonical claim `operations/claims/PROB10-10.md`, the current `POSTED.md` exclusions, the latest PROB10-10 report

`runs/prob10_2026-09-20/PROB10-10/20260920T0218Z__frontier-carry-synchronization-obstruction.md`,

and the latest P20 companion report

`proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T03-10-00Z__two-terminal-jensen-semigroup.md`.

The current PROB10-10 lane has an exact asynchronous-frontier diagnosis, a certified auxiliary axis lower bound `mu(e1)>=0.3002823`, and a diagonal upper bound `mu(1,1)<=0.758507818076`; those do not cross the axis/diagonal threshold. P20 has an exact two-terminal residual representation, an all-`theta` local Exp(1) Bellman Jensen modulus, an outside-star continuation-span coercivity estimate, and deterministic min-plus Jensen accumulation. Its unresolved interface is a controlled factorization of unrestricted undirected FPP through fresh asynchronous blocks.

This report does **not** duplicate either route. It changes the directional regime and uses a complementary two-sided estimate:

- an **upper** bound on the axis time constant from an exactly optimized finite undirected ladder block, transferred without any independence assumption between adjacent blocks;
- a **lower** bound in a wide direction cone from an exponentially tilted count of all possible self-avoiding competitors, upper-bounded by a rational non-backtracking transfer matrix.

The historical R08 failures are preserved rather than reset:

- many local deletion savings can share one bypass, so naive multiplication of local surgeries is invalid;
- positive-probability finite cylinders can exhibit exact finite triangle equality, so pointwise finite strictness is impossible;
- fixed-corner square blocks through size three did not cross the old axis/diagonal threshold;
- the old axis/diagonal strict-gap metric remained zero.

R07's FPP work was a fluctuation/KPZ lane and explicitly treated imported strict convexity/curvature assumptions as unavailable; it is not used as a curvature theorem here.

## 3. New theorem

### P04-T10-WIDE-CONE-STRICT-TRIANGLE-01

Let `mu` be the time-constant norm of iid rate-one exponential nearest-neighbor undirected FPP on `Z^2`. Put

\[
a_0
:=
\frac{127596793342690034600361684870097}
{197703921604834678505472000000000}
=0.6453933351799015\ldots .
\tag{3.1}
\]

Then:

**(A) Axis block bound.**
\[
\boxed{\mu(e_1)\le a_0.}
\tag{3.2}
\]
Moreover (1.3) holds for every `N`.

**(B) Wide-cone lower bound.** For every real `x>=0` and `y` with `|y|>=2x`,
\[
\boxed{\mu(x,y)\ge \frac23 x.}
\tag{3.3}
\]
For integer `a>=1`, `b>=2a`, the finite-scale lower-tail error is explicitly (1.4)--(1.5).

**(C) Strict triangle defect.** For every real `x>0`, `|y|>=2x`,
\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge \delta_0 x
>\frac{x}{24}.
}
\tag{3.4}
\]

This proves a positive strict-triangle inequality on a continuum family of noncollinear pairs. It does not prove strict convexity for pairs outside this regime.

## 4. Proof of (A): dependence-controlled exact ladder optimization

Let

\[
R=[0,6]\times[-1,1]\cap\mathbb Z^2
\]

with every nearest-neighbor undirected physical edge whose endpoints lie in `R`. Let `M` be the FPP distance **inside this finite graph** from `(0,0)` to `(6,0)`.

The exact finite computation in

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T03-46-21Z__cone-defect-exact.py`

uses only `Fraction` arithmetic and obtains

\[
\boxed{
\mathbb E M
=
\frac{127596793342690034600361684870097}
{32950653600805779750912000000000}.
}
\tag{4.1}
\]

### 4.1 Why the finite recursion is exact

For completeness, start infection at `(0,0)` in the finite graph `R`. If `S` is the currently infected vertex set and the target is not in `S`, let `b(S)` be the number of physical edges from `S` to its complement. For an outside vertex `v`, let `r_S(v)` be the number of those boundary edges ending at `v`.

Conditional on the entire infection history up to `S`, exponential memorylessness makes the residual clocks on the `b(S)` boundary edges independent `Exp(1)`. Therefore the next infection time has mean `1/b(S)`, and the probability the next infected vertex is `v` is `r_S(v)/b(S)`. If `E(S)` is the expected additional time to hit the target,

\[
E(S)
=
\frac1{b(S)}
+
\sum_{v\notin S}\frac{r_S(v)}{b(S)}E(S\cup\{v\}),
\tag{4.2}
\]

with `E(S)=0` when the target is infected. This recursion strictly increases `|S|`, so backward induction uniquely determines the exact expectation. The executed checker evaluates 64,501 reachable recursion states on the 21-vertex graph and gives (4.1).

### 4.2 Block-to-infinite-volume transfer, with dependence allowed

For each integer `j>=0`, translate `R` by `6j e_1` and let `M_j` be its internal passage distance from `6j e_1` to `6(j+1)e_1`. Concatenating one minimizing block path from each translated ladder gives a walk from `0` to `6N e_1`; erasing any loops can only lower its cost because all weights are positive. Hence pathwise

\[
T(0,6N e_1)\le\sum_{j=0}^{N-1}M_j.
\tag{4.3}
\]

Adjacent translated ladders share a boundary column, so the random variables `M_j` need not be independent. **No independence is used.** Translation invariance gives `E M_j=E M`, and linearity of expectation gives

\[
\frac{\mathbb E T(0,6N e_1)}{6N}
\le\frac{\mathbb E M}{6}=a_0
\tag{4.4}
\]

for every `N`. This is the advertised zero-interface-error expectation transfer. Standard `L^1` time-constant convergence for Exp(1) FPP now yields (3.2).

## 5. Proof of (B): a rational non-backtracking entropy/Chernoff certificate

It suffices first to treat integer vectors `(a,b)` with `a>=1`, `b>=2a`. Let

\[
A=\frac95,\qquad B=3,
\]

and assign to steps `E,W,N,S` the positive weights

\[
w=(A,A^{-1},B,B^{-1})
=\left(\frac95,\frac59,3,\frac13\right).
\tag{5.1}
\]

Let `M_nb` be the `4x4` non-backtracking transfer matrix

\[
(M_{\rm nb})_{ij}
=\mathbf 1\{j\ne -i\}\,w_j.
\tag{5.2}
\]

Thus a direction sequence receives the product of the weights of its steps and an immediate reversal is forbidden.

Take the positive rational vector

\[
z=\frac1{1000}(2164,1571,2269,1000)^T
\tag{5.3}
\]

and

\[
r=\frac{511}{100}.
\tag{5.4}
\]

The exact component ratios are

\[
\frac{(M_{\rm nb}z)_i}{z_i}
\in
\left\{
\frac{165533}{32460},
\frac{72118}{14139},
\frac{520874}{102105},
\frac{229559}{45000}
\right\},
\tag{5.5}
\]

and the checker verifies each is at most `511/100`. Hence, componentwise,

\[
M_{\rm nb}z\le rz.
\tag{5.6}
\]

Since every component of `z` is at least one, if `W_m` denotes the total tilted weight of all length-`m` non-backtracking direction sequences, then

\[
W_m
\le (w^Tz)r^{m-1}
=K r^m,
\qquad
K:=\frac{w^Tz}{r}.
\tag{5.7}
\]

Now fix endpoint `n(a,b)`. Every path with this endpoint has tilted step product exactly

\[
A^{an}B^{bn}.
\tag{5.8}
\]

Every self-avoiding path is non-backtracking. Therefore the number `N_m(n;a,b)` of self-avoiding length-`m` paths from `0` to `n(a,b)` satisfies

\[
N_m(n;a,b)
\le K r^m A^{-an}B^{-bn}.
\tag{5.9}
\]

A geodesic is self-avoiding almost surely because Exp(1) weights are strictly positive. Consequently, if

\[
T(0,n(a,b))\le \frac23 an,
\]

then some self-avoiding path of length `m>=(a+b)n` has total weight at most `(2/3)an`.

For a fixed self-avoiding path its `m` physical edges are distinct, so its weight is a sum `S_m` of `m` independent rate-one exponentials. For every `s>0`, exponential Markov gives

\[
\mathbb P\left(S_m\le\frac23 an\right)
\le
\exp\!\left(\frac23 san\right)(1+s)^{-m}.
\tag{5.10}
\]

Choose

\[
s=\frac{21}{5},
\qquad
q:=\frac{r}{1+s}=\frac{511}{520}<1.
\tag{5.11}
\]

Combining (5.9)--(5.11) and summing over every admissible path length gives

\[
\begin{aligned}
\mathbb P\left(T(0,n(a,b))\le\frac23 an\right)
&\le
K A^{-an}B^{-bn}e^{(14/5)an}
\sum_{m\ge(a+b)n}q^m\\
&=
\frac{K}{1-q}
\left[e^{14/5}\frac{q}{A}\right]^{an}
\left[\frac qB\right]^{bn}.
\end{aligned}
\tag{5.12}
\]

Because `q/B<1` and `b>=2a`,

\[
\mathbb P\left(T(0,n(a,b))\le\frac23 an\right)
\le
C_0\,\beta^{an},
\tag{5.13}
\]

where

\[
C_0=\frac{K}{1-q}=\frac{27865448}{206955}
\tag{5.14}
\]

and

\[
\beta=e^{14/5}\frac5{81}\left(\frac{511}{520}\right)^3.
\tag{5.15}
\]

### 5.1 Rigorous certification that `beta<1`

No floating exponential evaluation is used for the proof. For `x=14/5`, write the positive Taylor series for `e^x` through order 20. If `t_k=x^k/k!`, then for every `k>=21`,

\[
\frac{t_{k+1}}{t_k}=\frac{x}{k+1}\le\frac{x}{22}<1.
\]

Thus the entire omitted positive tail is bounded by its first term times the corresponding geometric series. The exact rational upper bound produced by the checker is

\[
e^{14/5}
<
E_+
:=
\frac{5346699252199868176494787217}
{325133116364479064941406250}.
\tag{5.16}
\]

Hence

\[
\beta
<
\beta_+
:=E_+\frac5{81}\left(\frac{511}{520}\right)^3
=
\frac{713425217726611388616507115106921327}
{740604339057582092285156250000000000}
<1.
\tag{5.17}
\]

This proves the explicit error bound (1.4).

The right side is summable in `n`. Borel--Cantelli therefore implies that almost surely, for all sufficiently large `n`,

\[
T(0,n(a,b))>\frac23 an.
\]

The standard shape/time-constant theorem gives `T(0,n(a,b))/n -> mu(a,b)` almost surely, hence

\[
\mu(a,b)\ge\frac23 a.
\tag{5.18}
\]

Positive homogeneity gives the same inequality for rational `(x,y)` with `x>=0`, `y>=2x`; continuity of the norm extends it to every real point of this closed cone. Reflection in the horizontal axis gives `|y|>=2x`. This proves (3.3).

## 6. Proof of (C): strict triangle defect on a continuum cone

Square-lattice reflection symmetry gives

\[
\mu(x,y)=\mu(x,-y),
\tag{6.1}
\]

and homogeneity gives

\[
\mu(2x,0)=2x\mu(e_1).
\tag{6.2}
\]

For `x>0` and `|y|>=2x`, combine (3.2), (3.3), (6.1), and (6.2):

\[
\begin{aligned}
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
&\ge \frac43x-2a_0x\\
&=\delta_0 x.
\end{aligned}
\tag{6.3}
\]

Substituting the exact rational value (3.1) yields

\[
\delta_0
=
\frac{4205821060533084403286315129903}
{98851960802417339252736000000000}
>
\frac1{24},
\tag{6.4}
\]

verified by exact integer arithmetic in the executed artifact. This proves (3.4) and the theorem.

## 7. What this does and does not settle

This is source-relevant movement because (3.4) is an actual strict triangle inequality for the **same undirected iid Exp(1) FPP norm**, transferred to infinite volume with explicit errors. It is not a directed model, sampled curvature, or an unproved finite-to-limit extrapolation.

It still does **not** prove ADH Question 4. In particular:

- the canonical axis/diagonal pair `2 mu(e1)-mu(1,1)` remains unresolved here;
- the path-entropy certificate is deliberately coarse and presently covers the symmetric wide cone `|y|>=2x`, not small angular separations;
- the ladder upper bound is direction-specific to the axis and is used only as one side of the symmetric cone chord;
- no claim of external novelty is made for the general first-moment/non-backtracking technique.

The next mathematical target should be to reduce the cone aperture. With the same proof template, one may optimize the rational tilt `(A,B)`, Collatz vector, Chernoff parameter, and finite axis ladder jointly. A meaningful next metric is the smallest rigorously covered slope `sigma` in `|y|>=sigma x`, holding a positive exact defect after all interval errors. That is a different concrete optimization problem from P20's asynchronous Bellman/Jensen route.

## 8. Current literature boundary checked 20 September 2026

The bounded current search recovered no source-matching theorem closing strict convexity of ordinary iid Exp(1) nearest-neighbor undirected FPP on `Z^2`. This is search evidence only, not a worldwide priority or novelty certificate.

- Auffinger--Damron--Hanson, arXiv:1511.03262, remains the source navigation for the continuous-law strict-convexity question.
- Jacquet, arXiv:2412.20779, proves a strict comparison between unrestricted and directed FPP time constants; that is not a direction-to-direction strict triangle inequality in the undirected norm and is not used here.
- Dembin--Elboim--Peled, arXiv:2204.02332, obtain quantitative coalescence under a hypothesis that the limit shape has more than 32 extreme points, so that theorem cannot be used to manufacture the missing full shape property.
- Bakhtin--Dow, arXiv:2406.09652, prove differentiability results for different continuous-action/Riemannian FPP models, not the iid edge model here.
- Haßler, arXiv:2411.13030, studies a simplified `1+1`-dimensional model with deterministic vertical weights, again a different model.

No directed-integrable constant, simulation, or sampled-curvature fit enters the proof above.

## 9. Exact artifacts and sanity checks

Executed exact code:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T03-46-21Z__cone-defect-exact.py`

Archived output:

`proofnet24/P04-progress-curvature/artifacts/2026-09-20/2026-09-20T03-46-21Z__cone-defect-exact.out`

The output ends `ALL_EXACT_CHECKS_PASS` and records:

- 21 rectangle vertices;
- 64,501 exact Richardson recursion states;
- the exact finite block expectation (4.1);
- the exact axis upper bound (3.1);
- the exact defect (1.1);
- all four Collatz ratios and their comparison to `511/100`;
- `q=511/520`;
- the rational Taylor upper bound for `e^(14/5)`;
- `beta_+<1`;
- the explicit probability prefactor `C_0`.

## 10. Before/after summary and residual obligation

**Original problem:** full strict convexity of the Exp(1) square-lattice FPP limit shape.  
Before: OPEN.  
After: OPEN / **PARTIAL**; no full closure claimed.

**Source-valid proved directional scope:**  
Before: P04 had no T10 positive strict-triangle theorem.  
After: every pair `u=(x,y)`, `v=(x,-y)` with `x>0`, `|y|>=2x` has

\[
\mu(u)+\mu(v)-\mu(u+v)>\frac{x}{24},
\]

plus its simultaneous `D_4` images.

**Mechanism gain:** exact finite undirected ladder optimization + a dependence-free expectation concatenation + an explicit exponentially small non-backtracking/Chernoff lower-tail transfer. The shared-bypass problem is avoided rather than assumed away: the upper construction never multiplies local savings, and the lower bound union-counts all self-avoiding competitor paths.

**Residual obstruction:** extend the strict inequality toward nearby directions. In this route, that means optimizing the tilt and finite block until the certified cone aperture is reduced substantially; in P20's complementary route, it remains positive-density continuation-state separation with controlled undirected reentry.

This is the first substantive P04 T10 run, so no three-unchanged-run recovery trigger applies.

### ledger_delta

```text
P04 | T10 Exp(1) undirected Z2 FPP strict convexity | full source status OPEN -> OPEN/PARTIAL; canonical axis/diagonal c_* remains 0; P04 cone defect lower bound 0 -> delta_0=4205821060533084403286315129903/98851960802417339252736000000000 > 1/24 on all symmetric pairs (x,y),(x,-y), x>0, |y|>=2x (and D4 images); axis block transfer error 0 in expectation; cone lower-tail error <= (27865448/206955)*beta_+^(a n), beta_+<0.963302 | new proved dependence-controlled block-to-infinite transfer and positive strict-triangle regime; full strict convexity unresolved
```

**End of complete run report.**
