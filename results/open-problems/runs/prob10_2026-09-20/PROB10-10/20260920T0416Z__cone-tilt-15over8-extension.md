Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 — a certified strict-triangle cone extension from slope 2 to slope 15/8

Status: **PARTIAL / OPEN** for the full source problem. This run has genuine restricted-direction source movement but does **not** prove global strict convexity and does **not** move the separate frozen axis/diagonal milestone `c_*`.

## 1. Frozen source target and before/after

Model throughout:

- nearest-neighbor **undirected** FPP on `Z^2`;
- iid rate-one exponential weight on each physical edge;
- unrestricted passage time `T(x,y)`;
- deterministic time-constant norm `mu` in the normalization `T(0,nv)/n -> mu(v)`.

Canonical source: Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4, specialized to the iid `Exp(1)` square-lattice case. Full source closure is strict convexity of the entire limit shape.

The canonical claim remains `operations/claims/PROB10-10.md`, source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

Two metrics must be kept separate.

### Full-source / canonical axis-diagonal metric

`Delta_12 = 2 mu(e1)-mu(1,1)` and

`c_* = sup{c>=0 : Delta_12>=c has been rigorously proved in the canonical track}`.

Before: `c_*=0`.  
After: `c_*=0`.

So there is **no movement on the axis/diagonal pair and no global strict-convexity closure**.

### Restricted-direction source metric

The newest complementary P04 theorem, proved in

`proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T03-46-21Z__wide-cone-strict-triangle.md`,

establishes a positive reflected strict-triangle defect for the cone

`|y| >= 2x`, `x>0`.

This run strictly enlarges that proved direction range to

\[
\boxed{|y|\ge \frac{15}{8}x,\qquad x>0.}
\]

Thus the certified cone-boundary slope moves

\[
\boxed{2\longrightarrow 15/8=1.875.}
\]

For the larger cone we prove the explicit defect

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge \delta_1 x,
}
\]
where

\[
\boxed{
\delta_1
=
\frac{21088053230750374920491129903}
{98851960802417339252736000000000}
=0.0002133296401970277\ldots>0.
}
\]

This is a **restricted-direction PARTIAL theorem**, not full strict convexity.

## 2. Continuity, ownership, and consumed evidence

The required immutable handoff of the actual pre-refocus HARD7-03 particle-system target already exists and was re-read rather than duplicated:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`.

It preserves D0025 / Seppalainen Problem 4 and HARD7-03's exact four-step-atlas state. Nothing in that predecessor claim was overwritten.

Consumed repository state:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical report before this run: `runs/prob10_2026-09-20/PROB10-10/20260920T0218Z__frontier-carry-synchronization-obstruction.md`, creation commit `a784be963d58943e91611086bceaf400d91abaab`;
- newest P20 companion report: `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T03-10-00Z__two-terminal-jensen-semigroup.md`;
- newest P04 companion report: `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T03-46-21Z__wide-cone-strict-triangle.md`.

The old R08 generic strict-convexity route remains retired. Its binding failures are not reset: shared bypasses invalidate naive independent local surgery, finite cylinder events can exhibit exact finite triangle equality, and the old fixed-corner blocks did not cross the axis/diagonal threshold. R07 was a fluctuation/KPZ lane and is not imported as curvature.

There is no claim collision with P04: P04 proved the stated `|y|>=2x` cone theorem; this run consumes that theorem and proves a strictly larger `|y|>=15x/8` range with a different rational tilt certificate. No P04 file or claim is overwritten.

## 3. Source/current-literature check

A bounded fresh search on 20 September 2026 again found no theorem closing ordinary iid `Exp(1)` undirected nearest-neighbor `Z^2` strict convexity.

Relevant distinctions checked:

1. Auffinger--Damron--Hanson remains the source navigation and still treats strict convexity as an open shape question.
2. Lalley (2003) gives sufficient conditions involving geodesic straightness and mean-zero passage-time limits; those hypotheses are not verified here and do not close this model.
3. Jacquet (arXiv:2412.20779) proves strict unrestricted-versus-directed time-constant comparison, not the reflected direction-to-direction strict triangle proved below.
4. Alm--Parviainen (CPC 2002) gives lower/upper time-constant methods and numerical results for the exponential law, including transition-matrix ideas. The publicly accessible abstract does not certify this exact `15/8` reflected-cone theorem, but because its full numerical tables were not exhaustively reconstructed here **no publication-priority or novelty claim is made** for the present restricted theorem.
5. Recent continuous-space, long-range, directed, and correlated FPP models are not aliases of this iid undirected square-lattice statement.

Thus this report records a source-valid repository advance, not a worldwide novelty certificate.

## 4. Required method change and the three attacks tried

The preceding canonical report was the third source-unchanged iteration. It proved an exact synchronization obstruction: a `k`-vertex frontier that discards relative arrival labels pays mean one-level toll `H_k/2`, and a successful frontier compiler must preserve asynchronous relative labels. This run therefore does **not** continue that mechanism.

The idea was written before code in

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0416Z__idea-cone-tilt-extension.md`,

creation commit `c47cdaebe33d88a2149cd6c0bd2e23d2ba3ac693`.

Three materially different routes were compared:

1. **Tilted non-backtracking cone optimization — SUCCESS.** Starting from P04's exact axis ladder upper bound, re-optimize the rigorous entropy/Chernoff lower bound for oblique directions. A rational certificate pushes the cone boundary from slope `2` to `15/8` and produces an explicit exponential finite-scale error.
2. **Two-terminal Busemann/Jensen accumulation — NOT CLOSED.** P20 now has an exact two-target residual metric, all-`theta` local Exp(1) Jensen curvature and deterministic min-plus accumulation. Its remaining missing input is still a controlled factorization of unrestricted FPP through fresh asynchronous blocks. I did not convert this conditional interface into a theorem.
3. **Asynchronous frontier average-cost Bellman — DEFERRED AFTER EXACT OBSTRUCTION.** The canonical run has identified the correct relative-label state, but no finite-support invariant state or rigorous truncation error is yet available. Continuing with another synchronized or rounded frontier certificate would be another version of the stalled route, so it was not pursued here.

The negation test for route 1 was the exact boundary inequality `beta(15/8)^8<1`. It passes by exact rational arithmetic in Section 7.

## 5. Input theorem from P04: exact axis upper bound

The P04 report proves, by an exact infection recursion on the finite undirected ladder `[0,6]x[-1,1]` and a dependence-safe block concatenation,

\[
\boxed{
\mu(e_1)\le a_0,
}
\]
where

\[
a_0
=
\frac{127596793342690034600361684870097}
{197703921604834678505472000000000}
=0.6453933351799015\ldots .
\tag{5.1}
\]

That theorem is consumed here as a proved neighboring update; this run does not re-label its finite ladder computation as new work.

## 6. New oblique lower bound on the enlarged cone

### Theorem 6.1

For every real `x>=0` and every real `y` satisfying

\[
|y|\ge \frac{15}{8}x,
\]

we have

\[
\boxed{
\mu(x,y)\ge \frac{1291}{2000}x.
}
\tag{6.1}
\]

For integer `a>=1`, integer `b` with `b/a>=15/8`, and every integer `n>=1`, there are explicit constants `C<infinity` and `0<\widehat\beta<1`, independent of `a,b,n`, such that

\[
\boxed{
\mathbb P\!\left(
T(0,n(a,b))\le \frac{1291}{2000}an
\right)
\le C\,\widehat\beta^{an}.
}
\tag{6.2}
\]

One exact choice is

\[
C=
\frac{26633487052538711}{2329665975000}
=11432.3200571\ldots,
\tag{6.3}
\]

and the exact certificate in Section 7 gives

\[
\widehat\beta<0.999774.
\tag{6.4}
\]

### Proof

It is enough first to take `a,b>0`; negative `b` follows by reflection.

Assign the four step directions `E,W,N,S` the positive tilted weights

\[
w=(A,A^{-1},B,B^{-1}),
\qquad
A=\frac{189}{100},
\qquad
B=\frac{291}{100}.
\tag{6.5}
\]

Let `M` be the `4x4` non-backtracking transfer matrix

\[
M_{ij}=\mathbf 1\{j\neq -i\}w_j.
\tag{6.6}
\]

Use the positive rational vector

\[
z=
\left(
\frac{2095936}{10^6},
\frac{1469509}{10^6},
\frac{2181303}{10^6},
1
\right)^T
\tag{6.7}
\]

and

\[
r=\frac{5083}{1000}.
\tag{6.8}
\]

The exact checker verifies componentwise

\[
Mz\le rz.
\tag{6.9}
\]

The four exact component ratios `(Mz)_i/z_i` are

\[
\frac{309989303407}{60991737600},
\quad
\frac{13692463648609}{2694050849700},
\quad
\frac{209533503553}{41226626700},
\quad
\frac{582356870377}{114581250000},
\tag{6.10}
\]

and each is strictly below `5083/1000`.

Because every component of `z` is at least one, if `W_m` is the total tilted weight of all length-`m` non-backtracking direction sequences, then

\[
\begin{aligned}
W_m
&=w^T M^{m-1}{\bf 1}\\
&\le w^T M^{m-1}z\\
&\le (w^Tz)r^{m-1}
=K r^m,
\end{aligned}
\tag{6.11}
\]

where

\[
K=
\frac{20954749844641}{9318663900000}.
\tag{6.12}
\]

Now fix an endpoint `n(a,b)` and let `N_m(n;a,b)` denote the number of self-avoiding nearest-neighbor paths of length `m` from `0` to that endpoint. Every such path is non-backtracking. Moreover every path with this displacement has exactly the same tilted step product

\[
A^{an}B^{bn},
\tag{6.13}
\]

because `#E-#W=an` and `#N-#S=bn`. Therefore

\[
N_m(n;a,b)
\le K r^m A^{-an}B^{-bn}.
\tag{6.14}
\]

A path of length `m` that is self-avoiding uses `m` distinct physical edges, so its weight is a sum `S_m` of `m` independent rate-one exponentials. For any `s>0` and `t>0`, exponential Markov gives

\[
\mathbb P(S_m\le t)
\le e^{st}(1+s)^{-m}.
\tag{6.15}
\]

Take

\[
s=\frac{1021}{250},
\qquad
c=\frac{1291}{2000},
\qquad
q:=\frac{r}{1+s}=\frac{5083}{5084}<1.
\tag{6.16}
\]

If `T(0,n(a,b))<=can`, loop erasure of any realizing path gives a self-avoiding competitor with no larger passage time. Every such path has length at least `(a+b)n`. By the union bound, (6.14), and (6.15),

\[
\begin{aligned}
\mathbb P(T(0,n(a,b))\le can)
&\le
K A^{-an}B^{-bn}e^{scan}
\sum_{m\ge(a+b)n}q^m\\
&=
\frac{K}{1-q}
\left[
A^{-1}B^{-b/a}e^{sc}q^{1+b/a}
\right]^{an}.
\end{aligned}
\tag{6.17}
\]

Put

\[
\beta(\rho)
=A^{-1}B^{-\rho}e^{sc}q^{1+\rho}.
\tag{6.18}
\]

Since `B>1` and `0<q<1`, `beta(rho)` is strictly decreasing in `rho`. Hence for every `b/a>=15/8`,

\[
\beta(b/a)\le\beta(15/8).
\tag{6.19}
\]

The exact artifact proves

\[
\beta(15/8)^8
=A^{-8}B^{-15}e^{8sc}q^{23}<1.
\tag{6.20}
\]

Indeed, with

\[
x=8sc=\frac{1318111}{62500}
\]

and `m_0=8000`, the elementary inequality

\[
e^x<(1-x/m_0)^{-m_0}
\tag{6.21}
\]

follows from `-log(1-u)>u` for `0<u<1`. Replacing `e^x` in (6.20) by this larger rational quantity gives an **exact rational upper bound** `\widehat\beta^8<1`; the executed checker evaluates its decimal only for readability as

\[
\widehat\beta^8=0.9981899661002902\ldots,
\qquad
\widehat\beta=0.9997735663911542\ldots .
\tag{6.22}
\]

No floating-point number is used in the asserted inequality.

With `C=K/(1-q)`, equations (6.17)--(6.22) prove (6.2).

Letting `n->infinity`, the right-hand side of (6.2) tends to zero exponentially. Standard time-constant convergence for iid Exp(1) FPP gives

\[
\mu(a,b)\ge ca
\tag{6.23}
\]

for every integer pair in the cone. Positive homogeneity extends this to rational directions, continuity of the deterministic norm `mu` extends it to all real directions with `y>=15x/8`, and lattice reflection gives negative `y`. This proves (6.1). QED.

## 7. Strict-triangle defect on the enlarged cone

### Corollary 7.1

For every real `x>0` and `|y|>=15x/8`,

\[
\boxed{
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge\delta_1 x>0,
}
\tag{7.1}
\]

with `delta_1` as in Section 1.

### Proof

Theorem 6.1 gives

\[
\mu(x,y)+\mu(x,-y)
\ge 2cx.
\tag{7.2}
\]

The consumed P04 axis theorem (5.1) and homogeneity give

\[
\mu(2x,0)=2x\mu(e_1)\le2a_0x.
\tag{7.3}
\]

Subtracting,

\[
\mu(x,y)+\mu(x,-y)-\mu(2x,0)
\ge2(c-a_0)x.
\tag{7.4}
\]

Exact arithmetic gives

\[
2(c-a_0)
=
\frac{21088053230750374920491129903}
{98851960802417339252736000000000}
>0.
\tag{7.5}
\]

QED.

## 8. Exact artifacts and actual tests

Idea-before-code:

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0416Z__idea-cone-tilt-extension.md`

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-10/cone_tilt_15over8_exact_20260920T0416Z.py`

Executed output:

`artifacts/prob10_2026-09-20/PROB10-10/cone_tilt_15over8_exact_20260920T0416Z.out`

The checker uses `Fraction` arithmetic for every asserted inequality. It verifies:

- all four Collatz inequalities `Mz<=rz`;
- `q=5083/5084<1`;
- the exact rational exponential upper-bound domain;
- the exact inequality `widehat_beta^8<1`;
- `c>a0` and hence `delta_1>0`.

The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 9. What moved and what remains

### Source-valid progress this run

A proved positive strict-triangle defect now holds on the explicit continuum family

\[
\boxed{x>0,\quad |y|\ge 15x/8,}
\]

strictly enlarging the previously proved `|y|>=2x` range. The finite-to-infinite transfer includes the explicit exponential error (6.2)--(6.4).

### What did not move

The canonical axis/diagonal defect remains

`c_*: 0 -> 0`.

The theorem does not cover slopes below `15/8`, does not prove strictness for arbitrary noncollinear pairs, and therefore does not prove strict convexity of the full limit shape.

### Next mathematical obligation

The promising quantitative question is whether the same exact non-backtracking tilt optimization plus improved finite ladder upper bounds can push the cone boundary substantially below `15/8`. The limiting obstruction is no longer dependence bookkeeping but the gap between an oblique large-deviation lower bound and a rigorous axis upper bound. A next run should either (i) optimize a larger finite axis strip and redo the exact cone certificate, or (ii) combine P20's two-terminal residual semigroup with a cone-certified positive span to attack directions nearer the diagonal. It should not return to synchronized frontier resets unless a rigorous asynchronous truncation theorem is first supplied.

Full source closure still requires a proof for the entire limit shape plus the repository's independent validation standard.
