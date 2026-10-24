# B14 — analytic tail closure for the recursive shared-core FEI obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED / SHARED_GRAFT_TAIL_CLOSED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live owner target and exact source-to-next-arrow use

The later owner control revision `2026-09-22.2` supersedes this slot's older posterior-crossing wording and converges all FEI workers on the all-gate inequality

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

The exact equivalence between a finite-cap symmetric nonnegative `Gamma` satisfying (G) for every Boolean gate/product bias and full FEI is in

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, observed blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

The old read-once `Gamma` and AND/decomposable extremality are already rigorously refuted by the newer shared-coordinate gates, so this run does not repeat that falsification. Instead it consumes the exact recursive shared-graft recurrence from account01/B18

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`,

and the certified `F_3,F_4` extension from account03/B18

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`, blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`.

The exact old missing implication stated by that peer was a tail theorem for the recurrence: stop certifying one enormous rational round at a time, prove an invariant interval for the singleton coefficient, bound the target functional uniformly, and decide all future increments. This report closes that implication.

The account02/B17 composition cocycle remains an inherited structural input: disjoint composition cannot manufacture a larger normalized gate margin than a prime factor. Nothing below revives the known false prescribed-coordinate erasure/payment statements.

## 1. Exact recurrence rewritten as a convex relaxation

For the balanced shared-core family, write

\[
R_t=\frac{H(F_t)}{I(F_t)-1},
\qquad I_t=I(F_t),
\qquad c_t=\text{designated singleton Fourier coefficient}.
\]

The peer recurrence is

\[
I_{t+1}=\frac{261}{128}+\frac9{256}(I_t^4-1),
\tag{1.1}
\]

\[
c_{t+1}=\frac{57}{256}+\frac{c_t^4}{256},
\tag{1.2}
\]

and

\[
R_{t+1}-R_t=
\frac{K(c_t^4)-\frac{133}{128}R_t}
     {\frac9{256}I_t^4+\frac{257}{256}},
\tag{1.3}
\]

where

\[
K(b)=H_{core}(b)+\frac9{256}\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\qquad \phi(x)=-x\log_2x.
\tag{1.4}
\]

Since the denominator in (1.3) is exactly `I_{t+1}-1`, define

\[
T(c):=\frac{128}{133}K(c^4),
\qquad
w_t:=\frac{133/128}{I_{t+1}-1}.
\tag{1.5}
\]

Then (1.3) is exactly

\[
\boxed{R_{t+1}=(1-w_t)R_t+w_tT(c_t).}
\tag{1.6}
\]

Thus every round is a relaxation of the current ratio toward a one-dimensional target `T(c_t)`. The tail problem is therefore to separate all future `R_t` from all future `T(c_t)` by a fixed gap while showing that the total relaxation weight is summable.

## 2. The singleton coefficient enters a tiny invariant interval forever

The certified source starts with

\[
c_1=\frac{14593}{65536}.
\]

Let

\[
f(c)=\frac{57}{256}+\frac{c^4}{256}.
\]

The exact recurrence gives `c_{t+1}=f(c_t)`. Put

\[
L=0.22266585228,
\qquad U_c=0.22266585229.
\tag{2.1}
\]

Exact rational evaluation gives

\[
L<c_5<c_4<U_c,
\qquad f(L)>L,
\qquad f(U_c)<U_c.
\tag{2.2}
\]

Because `f` is increasing on `[0,1]`, (2.2) proves by induction that

\[
\boxed{c_t\in[L,U_c]\quad\text{for every }t\ge4.}
\tag{2.3}
\]

This replaces the numerical observation that the singleton coefficients rapidly stabilize by a permanent rational trapping interval.

## 3. Uniform rigorous enclosure of the target functional

The inherited source representation reconstructs the validated balanced 18-bit seed with complete truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

For the fixed nine-bit core and host indicators,

\[
H_{core}(b)
=
\sum_{S\subseteq[9]}
\phi\!\left(
\left[\widehat a(S)+b\sum_j\widehat Q_j(S)\right]^2
\right).
\tag{3.1}
\]

On `b in [L^4,U_c^4]`, every squared normalized coefficient appearing in (3.1) is strictly below `1/16`. Hence `phi(x)=-x log_2 x` is increasing on the entire coefficient range used here. Each Fourier coefficient is affine in `b`, so its squared magnitude has exact endpoint/zero-crossing bounds. Applying these coefficientwise, and enclosing every logarithm by the rational atanh series after dyadic range reduction, yields the uniform interval

\[
\boxed{
6.52185116734757174868453197881704600
< T(c) <
6.52185116734807310136112294366428472
}
\tag{3.2}
\]

for every `c in [L,U_c]`.

In particular the deliberately coarser rational barriers

\[
B=6.52185116,
\qquad U=6.52185118
\tag{3.3}
\]

satisfy

\[
\boxed{B<T(c)<U\quad(t\ge4).}
\tag{3.4}
\]

This is the decisive all-future target bound.

## 4. The future relaxation weights are summable by a huge margin

The exact influence recurrence (1.1) gives

\[
w_4=0.004506745715925654769277184504\ldots,
\]

\[
w_5=0.000000010280311016077675552965\ldots .
\tag{4.1}
\]

Moreover `I_5>200`. For every `x>=200`,

\[
\frac9{256}x^4+\frac{257}{256}\ge2(x-1),
\tag{4.2}
\]

because it holds at `x=200` and the derivative of the left side minus the right side is

\[
\frac{36}{256}x^3-2>0.
\]

Therefore for every `t>=5`,

\[
I_{t+1}-1\ge2(I_t-1),
\qquad
w_{t+1}\le\frac12w_t.
\tag{4.3}
\]

Hence

\[
\boxed{
\sum_{t\ge4}w_t
\le w_4+2w_5
<0.004506766276547686924628290436.
}
\tag{4.4}
\]

The quartic influence explosion therefore makes the entire infinite future perturbation finite and extremely small.

## 5. First-crossing argument: every future shared-graft round improves the ratio

The consumed account03/B18 certificate gives

\[
R_4\in[
6.5218509485644448965490881329959858569477358114202361,
\]
\[
6.5218509485644448965496895824490791318643557898359042].
\tag{5.1}
\]

In particular `R_4<B`. Suppose for contradiction that `m>4` is the first index with `R_m>=B`. Before that first crossing, (3.4) and (1.6) imply every increment is positive, so `R_t>=R_{4,lo}`. At every such step,

\[
R_{t+1}-R_t
=w_t(T(c_t)-R_t)
\le w_t(U-R_{4,lo}).
\]

Using (4.4), the total possible future motion before a crossing is therefore at most

\[
\boxed{
(\sum_{t\ge4}w_t)(U-R_{4,lo})
<1.043025954934326488248\times10^{-9}.
}
\tag{5.2}
\]

But the certified gap from the upper endpoint of `R_4` to `B` is

\[
\boxed{
B-R_{4,hi}
>2.11435555103450310417550\times10^{-7},
}
\tag{5.3}
\]

more than two hundred times larger. This contradicts the first crossing.

Consequently

\[
\boxed{R_t<B<T(c_t)\quad\text{for every }t\ge4,}
\tag{5.4}
\]

and therefore by (1.6)

\[
\boxed{R_{t+1}>R_t\quad\text{for every }t\ge4.}
\tag{5.5}
\]

This is the tail theorem requested by the preceding peer report: the exact recursive shared-core Boolean construction increases the balanced excess ratio at **every future round**, not merely through `F_4`.

## 6. A new finite lower bound and a rigorous limit trap

Using only `T(c_4)>=B` in the exact convex-update formula gives a certified fifth-round lower endpoint

\[
\boxed{
R_5>
6.5218509495173311787059282417417271320120.
}
\tag{6.1}
\]

Each `F_t` is a genuine finite balanced monotone Boolean function by the inherited self-composition and shared-core construction. Balanced disjoint self-composition of any fixed `F_t` has ordinary `H/I` tending to `R_t`. Hence (6.1) yields the source-valid FEI lower bound

\[
\boxed{
C_{FEI}>
6.5218509495173311787059282417417271320120.
}
\tag{6.2}
\]

The gain over the prior `F_4` lower endpoint is numerically tiny; the important point is that it follows from an all-future theorem rather than a one-round extrapolation.

Combining (5.2) with the upper endpoint of (5.1) also gives the rigorous infinite-family trap

\[
\boxed{
R_5<R_\infty<
6.5218509496074708514840160706969912973269.
}
\tag{6.3}
\]

Thus this exact shared-graft recurrence has a finite limiting obstruction very near `6.5218509496...`; it does **not** keep forcing the center cap upward without bound. Future work should not spend separate runs certifying `F_6,F_7,...` from this same recurrence.

## 7. Exact status and next arrow

The old AND/decomposable extremality claim for the read-once potential remains **refuted**. This report adds a different result: it closes the entire tail of the strongest currently shared recursive-graft lower-bound mechanism.

A replacement all-gate potential must therefore have center strictly above (6.2). However, this construction alone does not force a center above the upper trap in (6.3). The next decisive all-gate question is consequently either:

1. construct a distinct source-valid prime/shared-coordinate interference mechanism exceeding the trap (6.3), or
2. build and prove an all-prime/all-bias gate inequality for a finite-cap potential above the now-saturated shared-graft envelope.

Neither arrow is proved here. Full FEI remains **OPEN / NOT PROVED**. No prescribed-coordinate payment, every-coordinate restriction bound, or posterior-crossing universal claim is asserted.

## 8. Calculation certificate and limitation

A standard-library rational checker was executed locally. It reconstructs the source truth table and checks the expected SHA-256, the invariant interval (2.3), the coefficientwise interval evaluation of (3.2), the influence-weight summability (4.4), the first-crossing budget (5.2)-(5.3), the finite lower bound (6.1), and the limit bound (6.3).

Checker SHA-256:

`f09abae4b07423842a5f83e1d1dbf85ce8a1d4f4e65eedc68130aa6c0019485e`.

Captured output SHA-256:

`0c5efa9aa77aeb2bcdefafdbd039eb902a2e9e711b58016f7881413d0791f8f8`.

The checker-source upload was blocked by the platform safety layer in this invocation. I did not retry it through encoding, renaming, another account, or another tool. Therefore the executable is **not remotely delivered by this run**; the analytic proof and exact numerical certificates are preserved in this report, but independent reproduction of the checker requires a later permitted source handoff.

No benchmark gold, unrelated private data, email/Drive material, remote compute, paid API/model call, workflow dispatch, or notification enabling was used.
