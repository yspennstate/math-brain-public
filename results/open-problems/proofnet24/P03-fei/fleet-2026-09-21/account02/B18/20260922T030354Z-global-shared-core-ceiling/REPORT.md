# B18 — global signed-singleton ceiling for the source-bound nine-host shared-core FEI amplifier

**Classification:** `ESSENTIAL_STEP_APPLIED / MECHANISM_CLOSED_FOR_FIXED_SOURCE_CORE`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and mathematical source artifacts were read directly; no installed/native mathematical-brain package or verified receiver-context was used.

## 1. Fresh control and why this is the live target

Fresh `math-research-brain` main was resolved at invocation start, and `AGENTS.md`, `scheduled_tasks/README.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, and `scheduled_tasks/PROTOCOL.md` including the OWNER MESSAGE were read. The active OWNER CONTROL is revision `2026-09-22.2`: B12--B18 remain on FEI, but the later all-gate/full-proof convergence directive supersedes incompatible older Campaign-C compiler wording. Thus the old signed-current NET route is not reopened here.

Fresh `math-open-problems` master and `proofnet24/P03-fei/README.md` were also read. Full FEI remains open. The exact current all-gate formulation is the gate inequality
\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{1.1}
\]
for one finite-center symmetric nonnegative potential and every Boolean gate/product-bias vector. At a balanced uniform gate this forces
\[
R(G):=\frac{H(G)}{I(G)-1}\le \Gamma(1/2).
\tag{1.2}
\]
So source-valid balanced gates remain exact lower-bound obstructions to any universal potential center.

## 2. Named OTHER-account result consumed

The principal completed other-account input is account04/B15:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`.

It consumes the source-bound shared-core recurrence and proves, on the reachable interval `0<=b<=1/4`, that
\[
M:=\sup_{0\le b\le1/4}\frac{K(b)}{d_0}
< M_+
:=6.52185121301287772365150440023918196647146413881,
\tag{2.1}
\]
with
\[
d_0=\frac{133}{128},\qquad
K(b)=H_{\rm core}(b)+\frac9{256}\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\quad \phi(t)=-t\log_2t.
\tag{2.2}
\]
It also proves strict concavity of `K` on `[0,1/4]` and localizes the unique maximum there near `b=0.002713295...`.

I also use the exact transform from account01/B18

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`.

For a balanced source gadget with excess ratio `R`, influence `I>=1`, and selected singleton coefficient `c`, take any integer self-composition depth `d>=1` and then the same nine-host graft. With
\[
\alpha=\frac9{256},\qquad B=\frac{257}{256},\qquad D_d=\alpha I^d+B,
\]
the exact actual-Boolean recurrence is
\[
\boxed{
R'_d=\left(1-\frac{d_0}{D_d}\right)R
      +\frac{d_0}{D_d}\frac{K(c^d)}{d_0}.
}
\tag{2.3}
\]
The new selected singleton after grafting is
\[
\boxed{c'=\frac{57}{256}+\frac{c^d}{256}.}
\tag{2.4}
\]
The previous ceiling theorem only needed the forward-reachable range `0<=c^d<=1/4`. The missing natural question was whether changing the seed singleton, while retaining exactly the same host/core geometry, could escape the ceiling.

## 3. Exact source classes

From the source checker of account01/B18, the 512 Walsh coordinates of the core are grouped by the exact numerator pair
\[
(A_s,Q_s),\qquad
p_s(b)=\frac{(A_s+bQ_s)^2}{512^2},
\tag{3.1}
\]
into the following 19 classes, with multiplicities:

```text
(-18,-2):72   (2,2):72      (0,0):46      (-16,0):36
(16,0):36     (10,-6):36    (4,4):36      (-4,-4):36
(-2,-2):36    (44,-4):18    (-44,4):18    (-6,10):18
(38,6):12     (114,2):9     (8,8):9       (-8,-8):9
(4,-12):6     (-4,12):6     (2,18):1
```

They satisfy
\[
\sum_s 1=512,
\qquad
\sum_s\frac{Q_s^2}{512^2}=\frac9{256}=\alpha.
\tag{3.2}
\]
No surrogate spectrum is used below.

## 4. New theorem: the local scalar target is globally capped for every signed singleton

### Theorem 4.1 — full `[-1,1]` source-core ceiling

For the exact source-bound nine-host core above,
\[
\boxed{
\sup_{-1\le b\le1}\frac{K(b)}{d_0}
=
\sup_{0\le b\le1/4}\frac{K(b)}{d_0}
=M<M_+.
}
\tag{4.1}
\]
More precisely, `K` is strictly increasing on `[-1,0]` and strictly decreasing on `[1/4,1]`. The location and value of its maximum on `[0,1/4]` are therefore exactly the ones certified by account04/B15.

#### Proof

Define
\[
\psi(x):=-x\left(\log_2\frac{x^2}{512^2}+\frac1{\ln2}\right),
\qquad \psi(0):=0.
\tag{4.2}
\]
The continuous extension at zero is valid because `x log x^2 ->0`. For one exact Walsh class `(a,q)` of multiplicity `m`, its contribution to `H_core'(b)` is
\[
D_{a,q,m}(b)
=\frac{2mq}{512^2}\psi(a+bq).
\tag{4.3}
\]
For `x!=0`,
\[
\psi'(x)
=\frac{\ln(512^2/x^2)-3}{\ln2}.
\tag{4.4}
\]
Hence
\[
D_{a,q,m}'(b)
=\frac{2mq^2}{512^2}\psi'(a+bq),
\tag{4.5}
\]
so the sign of a class derivative is controlled only by the magnitude of its actual affine Walsh numerator.

**Negative side.** For every varying source class and every `b in [-1,0]`, direct endpoint inspection of the exact table gives
\[
|a+bq|\le114.
\tag{4.6}
\]
We need `512^2/114^2>e^3`. This is elementary and exact. The exponential series gives
\[
e<\sum_{k=0}^6\frac1{k!}+\frac1{7!}\frac1{1-1/8}
=\frac{31967}{11760}<\frac{68}{25},
\tag{4.7}
\]
and direct rational arithmetic gives
\[
\frac{512^2}{114^2}>\left(\frac{68}{25}\right)^3.
\tag{4.8}
\]
Thus `psi'(x)>0` throughout every source class on `[-1,0]`, including through zeros by continuity. Therefore every `D_{a,q,m}` and hence `H_core'` is strictly increasing there.

Write the non-core correction as
\[
C(b)=\alpha[-\phi(b^2)+16(1-b^2)].
\]
Then
\[
C'(b)=2\alpha b\left(\log_2 b^2+\frac1{\ln2}-16\right),
\tag{4.9}
\]
so `C'(b)>=0` on `[-1,0]`. Moreover
\[
C''(b)=2\alpha\left(\log_2b^2+\frac3{\ln2}-16\right)<0
\tag{4.10}
\]
for `0<|b|<=1`, since `ln2>1/2` makes `3/ln2<6`.

To retain a quantitative strict margin instead of relying on floating point, split `[-1,-1/128]` into the dyadic intervals
\[
[-1,-3/4],[-3/4,-1/2],[-1/2,-1/4],[-1/4,-1/8],\ldots,[-1/64,-1/128].
\]
Because `H_core'` increases and `C'` decreases, on `[l,u]`
\[
K'(b)\ge H_{\rm core}'(l)+C'(u).
\tag{4.11}
\]
The exact rational-log checker certifies the eight lower bounds
\[
0.2554070,\ 0.1766482,\ 0.0559040,\ 0.0448030,\ 0.0324568,
\ 0.0230472,\ 0.0159514,\ 0.0113125,
\]
all strictly positive. Finally it certifies
\[
H_{\rm core}'(-1/128)>0.0000555609,
\tag{4.12}
\]
and since `H_core'` increases while `C'>=0`, this proves `K'(b)>0` on `[-1/128,0]` as well. Hence `K` is strictly increasing on `[-1,0]`.

**Positive tail.** For every varying class except `(114,2)` and every `b in [1/4,1]`, the exact table gives
\[
|a+bq|\le44.
\tag{4.13}
\]
Since
\[
\frac{512^2}{44^2}>27>e^3
\]
(using `e<3`), `psi'>0` for all those classes, so their `D` terms increase. For the one exceptional class,
\[
x=114+2b\ge\frac{229}{2},
\qquad
\frac{512^2}{x^2}<20.
\tag{4.14}
\]
The exponential lower series gives `e>163/60`, and `(163/60)^3>20`, hence `psi'(x)<0`; that one class decreases.

Because `C'` also decreases, on each positive interval `[l,u]` a rigorous upper bound is obtained by taking every nonspecial class at `u`, the exceptional class at `l`, and `C'` at `l`. On
\[
[1/4,1/2],\quad[1/2,3/4],\quad[3/4,1],
\]
the exact checker gives respectively
\[
K'(b)\le
-0.009797850180586092049849674738942484,
\tag{4.15}
\]
\[
K'(b)\le
-0.104348374980752370875158526169339511,
\tag{4.16}
\]
\[
K'(b)\le
-0.196384255680332064987126165919980205.
\tag{4.17}
\]
Thus `K` is strictly decreasing on `[1/4,1]`.

The account04/B15 theorem already proves the unique maximum on `[0,1/4]`. Since the entire negative side rises only to `K(0)`, and the entire positive tail decreases from `K(1/4)`, neither can exceed the maximum in `[0,1/4]`. This proves (4.1). `square`

## 5. New compiler-level consequence for the actual Boolean transform

### Corollary 5.1 — same-core grafts cannot amplify past `max(seed,M)`

Let `h` be any balanced Boolean source to which the account01/B18 nine-host transform applies, with total influence `I>=1`, excess ratio `R=H/(I-1)`, and **any signed selected singleton coefficient** `c in [-1,1]`. For any integer self-composition depth `d>=1`, let `R'_d` be the ratio after the same source-bound nine-host graft. Then
\[
\boxed{R'_d\le \max\{R,M\}<\max\{R,M_+\}.}
\tag{5.1}
\]

Indeed `b=c^d in [-1,1]`, so Theorem 4.1 gives `K(b)/d_0<=M`. Since `I>=1`,
\[
D_d=\alpha I^d+B\ge\alpha+B=d_0,
\]
and (2.3) is a genuine convex combination of `R` and `K(b)/d_0`.

After one graft the next selected coefficient satisfies, by (2.4),
\[
\frac{56}{256}\le c'\le\frac{58}{256},
\tag{5.2}
\]
so it remains in `[-1,1]`. Induction yields the stronger iterative statement:
\[
\boxed{
R_r\le\max\{R_{\rm seed},M\}
}
\tag{5.3}
\]
for every finite sequence of same-core grafts with arbitrary history-dependent integer self-composition depths.

Thus changing only the seed singleton sign/magnitude or the depth schedule cannot make this exact nine-host geometry a ratio amplifier above its scalar ceiling. Any stronger lower-bound obstruction must either start from an already stronger seed gate, change the host/core geometry, or leave this balanced transform setting (for example through a genuinely biased product point). This is a mechanism theorem, not a universal FEI upper bound.

For scale, the certified finite `F_7` lower bound retained from the other-account chain is
\[
R(F_7)>
6.5218509495504481848401605388605115013503296799038586768578,
\tag{5.4}
\]
so the entire remaining room between that source-valid gate and the global same-core ceiling is less than
\[
2.63462429538811343861378670465121135\times10^{-7}.
\tag{5.5}
\]
The point of this run is not the tiny numerical gap: it is that the ceiling now applies to **every signed source singleton** in the exact transform, rather than only the previously reachable nonnegative interval.

## 6. Small honest full-proof dependency chain

The current full-proof checklist is:

1. **PROVED:** all-gate inequality (1.1) for one finite-center symmetric nonnegative potential implies unrestricted FEI; balanced uniform gates force the center lower bound (1.2). Source: gate-reformulation continuation.
2. **PROVED:** actual source-bound nine-host shared-core transform and exact recurrence (2.3)--(2.4). Source: account01/B18.
3. **PROVED:** exact adaptive-depth scalar ceiling on `[0,1/4]`. Source consumed here: account04/B15.
4. **PROVED THIS RUN:** exact extension of that same scalar ceiling to all `b in [-1,1]`; hence the transform never exceeds `max(seed ratio,M)`.
5. **OPEN / UNPAID:** construct one finite-center potential satisfying (1.1) for **every** Boolean gate and **every** product bias, or an equivalent universal argument. The known explicit prime/balanced obstructions and all-block-bad minimal violations show that the old read-once-plus-scalar-lift safe-restriction mechanism is insufficient below the forced margin.

No item in steps 2--4 is promoted into step 5. Therefore full FEI remains **OPEN / NOT PROVED**.

## 7. Before/after relative to the last three substantive B18 reports

**FULL-PROBLEM CHANGE:** none. No dimension-independent universal upper constant is proved.

**MECHANISM CHANGE:** yes. The last owner-aligned B18 runs moved from (i) a restriction-minimal balanced gate obstruction to (ii) a depth-dependent recurrence and then (iii) a fixed-depth/shared-core tail ceiling. Before this run, the strongest analytic source-core ceiling required the forward-reachable local parameter `b<=1/4`. After this run, the exact same source core is globally capped for every signed `b in [-1,1]`, and every repeated same-core transform obeys the invariant max bound (5.3).

This closes a genuine escape route: `change the initial singleton or its sign, but keep the same nine-host core`. It does **not** close `change the host/core geometry`, `find a stronger prime seed`, or `solve the all-bias gate potential`.

## 8. Exact checker and scope

`CHECKER_GLOBAL.py` is a standard-library exact-rational certificate. It uses the same atanh-series logarithm enclosure as the source family, with an explicit rational remainder; no floating-point sign decision is used. It checks the exact class multiplicities, `sum Q_s^2/512^2=9/256`, the elementary exponential bounds used in the monotonicity proof, all negative-side derivative lower bounds, and all positive-tail derivative upper bounds.

Executed checker SHA-256:
`1fce5b344cf9e36e2cff5a46607f9372f7ae6bd2db154052901dfc4a99108a9b`.

Captured output SHA-256:
`dfe5ead8002578a9004d86e564ad2eb7a73b1767f58ade9c40e4aede9e1790f0`.

The checker is a finite certificate for explicit scalar endpoint inequalities **after** the analytic monotonicity reduction; it is not finite-dimensional extrapolation to FEI.

## 9. Current literature boundary

Fresh September 22 searches checked current arXiv-facing FEI results. Potapov, arXiv:2609.21563 (September 18, 2026), proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2, not unrestricted Boolean functions. González--MacManus--Pereyra, arXiv:2606.00246, explicitly retain a key universal restriction inequality as a conditional step toward full FEI. Li--Han, arXiv:2512.03117, prove the sharp profile inequality
\[
H[\widehat f]\le I(f)+\sum_i I_i(f)\log\frac1{I_i(f)},
\]
which still contains the coordinate influence-profile term and is not unrestricted FEI. A bounded search miss is not used as an openness or novelty proof.

## 10. Exact remaining attack

The next source-valid B18 target should no longer spend a run tuning the singleton or self-composition depth of this same nine-host core. The smallest honest universal target is one of:

- derive a finite-cap all-prime/all-bias potential satisfying (1.1), with the explicit shared-graft and all-block-bad obstructions built into its envelope; or
- construct/analyze a genuinely different shared-coordinate host/core geometry and determine its exact local target before treating it as a candidate extremal family.

A same-core depth/singleton modification is now analytically exhausted by (5.3).

No novelty or publication-priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, email/Drive data, paid computation, workflow execution, or permission changes enter this report.
