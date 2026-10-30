# fleet01/B12 — selector-weight cancellation widens the unequal-MUX deterministic-face collar

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Common candidate:** `LIMIT-PRIME-GATE-LIFT-v1`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact candidate and named peer result consumed

The campaign candidate used in this run is the current lifted all-gate potential
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
 a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]
The remaining target is still
\[
D_{\Gamma^\dagger}(P;p)\ge0
\]
for every finite composition-prime Boolean gate and every interior product bias.  The composition cocycle plus the all-gate reformulation would then give full FEI.  This report does not prove that universal statement.

The exact compatible other-account theorem consumed and extended is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T065548Z-adaptive-mux-142/REPORT.md`,
report blob `65012580ffd1844e2a316138f54e35948f55beb7`.

For the genuine one-address-bit unequal-data MUX
\[
M=MUX(A;D_0,D_1),\qquad p=\Pr(A=1),\quad x=\Pr(D_0=1),\quad y=\Pr(D_1=1),
\]
it records the exact physical `D_1` residual
\[
\begin{aligned}
R_1^\dagger={}&pA_{\Gamma^\dagger}(y)-\Gamma^\dagger(r)
 +(1-y)\Gamma^\dagger(r_0)
 +y\Gamma^\dagger((1-p)(1-x))\\
&-H_M+(1-y)H_\wedge(1-p,x)
+yH_\wedge(1-p,1-x),
\end{aligned}\tag{0.1}
\]
where
\[
r_0=(1-p)x,\qquad r=r_0+py,\qquad
A_\Gamma(u)=\Gamma(u)+h_2(V_u),
\]
and the exact cross-deficit necessary condition
\[
D_{\Gamma^\dagger}(M)<0
\Longrightarrow
R_1^\dagger<-\delta Q,
\qquad
\delta:=a^\dagger-0.01=0.258204856,
\tag{0.2}
\]
with
\[
Q=p(1-p)x(1-x).
\]
It also imports the source-current bounds
\[
0\le\Gamma^\dagger(u)<7,
\qquad
|({\Gamma^\dagger})'(u)|<31\log_2(1/z)+47,
\quad z=\min(u,1-u).
\tag{0.3}
\]
The peer theorem used (0.1)--(0.3) to prove the deterministic-face collar
\[
y\le {Q\over142\log_2(16/Q)}.
\tag{0.4}
\]
Its proof deliberately dropped the selector factor `p` in several movements.  The new step below retains that factor simultaneously in the potential, child-entropy and six-mass Shannon movements.

The current campaign lead `fleet03/B18/20260922T062639Z-rare-gating-nonamplification/REPORT.md`, blob `fd5041b1ff948f566ce001ad3e226876f0279800`, uses the same `C^dagger/Gamma^dagger` and leaves the all-prime/all-bias implication open.

## 1. New theorem

Because complementing the address and exchanging the data branches are NPN symmetries, near a chosen deterministic data face we may orient the selector so that the probability of selecting that near-deterministic branch obeys
\[
0<p\le\frac12.
\]
Put
\[
Q=p(1-p)x(1-x),\qquad L=\log_2{16\over Q}.
\]
Then `Q<=1/16` and `L>=8`.

### Theorem 1.1 — selector-weight adaptive MUX collar

For every interior `p,x` with `p<=1/2`,
\[
\boxed{
0\le y\le {Q\over 288\,p\,L}
={ (1-p)x(1-x)\over288\log_2(16/[p(1-p)x(1-x)])}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(MUX;p,x,y)\ge0.
}
\tag{1.1}
\]
By the same NPN symmetries, the statement applies near every deterministic data face; the factor `p` in (1.1) is the selection probability of that chosen near-deterministic branch after orienting it to be at most `1/2`.

Combined with the peer's (0.4), the certified safe width is therefore at least
\[
\boxed{
{Q\over L}\max\left\{\frac1{142},\frac1{288p}\right\}.
}
\tag{1.2}
\]
The new term is strictly wider whenever
\[
p<{71\over144}=0.493055\ldots .
\]
In particular, unlike (0.4), it does not collapse linearly as `p->0`: its width tends to
\[
{ x(1-x)\over288\log_2(16/Q)}
\]
up to the slowly varying logarithm.

## 2. Keep the selector factor in both potential movements

At `y=0`, the MUX is NPN-equivalent to a two-input AND and the exact residual satisfies
\[
R_1^\dagger(p,x,0)=0.
\tag{2.1}
\]
The positive term `p A_{Gamma^dagger}(y)` in (0.1) will not be used.

Assume (1.1).  Then
\[
py\le {Q\over288L}.
\tag{2.2}
\]
On the segment from `r_0=(1-p)x` to `r=r_0+py`, every point is at distance at least `Q` from `0` and `1`.  Indeed `r_0>=Q`; also
\[
1-r\ge 1-x-py\ge4Q-{Q\over2304}>Q,
\]
because `Q<= (1-x)/4` and `L>=8`.  Hence (0.3) gives
\[
|\Gamma^\dagger(r)-\Gamma^\dagger(r_0)|
\le py(31L-77).
\tag{2.3}
\]

For the convex-combination potential term use symmetry:
\[
\Gamma^\dagger((1-p)(1-x))
=\Gamma^\dagger(p+(1-p)x).
\]
The interval between `(1-p)x` and `p+(1-p)x` has length exactly `p`; its distance from both endpoints of `[0,1]` is again at least `Q`.  Therefore
\[
|\Gamma^\dagger((1-p)(1-x))-\Gamma^\dagger((1-p)x)|
\le p(31L-77).
\tag{2.4}
\]
Multiplying (2.4) by `y` and combining with (2.3), the total adverse potential movement is at most
\[
\boxed{py(62L-154).}
\tag{2.5}
\]
This is the first place where the peer's `O(yL)` envelope is replaced by the source-exact `O(pyL)` scale.

## 3. The child-AND entropy difference is also `O(pL)`

For `AND(1-p,b)`, the four squared biased Fourier masses are
\[
(1-2(1-p)b)^2,
\quad4p(1-p)b^2,
\quad4(1-p)^2b(1-b),
\quad4p(1-p)b(1-b).
\tag{3.1}
\]
Under `b=x` versus `b=1-x`, the last two masses are unchanged and the first two exchange exactly the amount
\[
d=4p(1-p)|2x-1|.
\]
Thus `d` is the total-variation distance between the two child spectra.

If `p<=1/4`, then `d<=3/4`, so Fannes--Audenaert on four atoms and
`h_2(d)<=d log_2(e/d)` give
\[
|H_\wedge(1-p,1-x)-H_\wedge(1-p,x)|
\le d\log_2{3e\over d}
\le4p\log_2{3e\over4p}.
\]
Since `Q<=p/4`,
\[
L\ge6+\log_2(1/p),
\]
and `3e/4<4`, so the last display is strictly below `4pL`.  If `p>1/4`, the entropy difference is at most two bits while `4pL>=8`.  Hence in every case
\[
\boxed{
|H_\wedge(1-p,1-x)-H_\wedge(1-p,x)|<4pL.
}
\tag{3.2}
\]
Its contribution to (0.1) is therefore bounded adversely by `4pLy`.

## 4. Six-mass Shannon movement keeps the same selector factor

From the exact MUX spectrum, only four mass groups change when `y` moves from `0`:
\[
w_\varnothing=(1-2r)^2,
\quad w_A=V_p(y-x)^2,
\quad w_1=p^2V_y,
\quad w_{A1}=p(1-p)V_y.
\]
Consequently
\[
\|w(y)-w(0)\|_1
\le16py+4p^2y^2.
\tag{4.1}
\]
The condition (1.1) implies `p y<1/2304`; in particular
\[
16py+4p^2y^2
< {129\over8}py.
\]
Therefore the total variation `theta` satisfies
\[
\boxed{
\theta<{129\over16}py
\le {129Q\over4608L}=:\theta_0.
}
\tag{4.2}
\]
This is below `5/6`, so Fannes--Audenaert on the six-point spectrum gives
\[
|H_M(y)-H_M(0)|
\le h_2(\theta)+\theta\log_2 5
\le\theta\log_2{5e\over\theta}.
\tag{4.3}
\]
The last function is increasing in the present range, so use `theta_0`.  Since `Q=16\,2^{-L}`,
\[
{5e\over\theta_0}
={480e\over43}\,L\,2^L.
\tag{4.4}
\]
For every `L>0`,
\[
\boxed{
\log_2\!\left({480e\over43}L\right)<11+{L\over64}.
}
\tag{4.5}
\]
Indeed `L2^{-L/64}` is maximized at `64/(e ln2)`, so the left side of the exponential form of (4.5) is at most
\[
{480e\over43}{64\over e\ln2}
={30720\over43\ln2}
< {92160\over86}<2048,
\]
using the elementary bound `ln2>2/3`.

Combining (4.2)--(4.5),
\[
\boxed{
|H_M(y)-H_M(0)|
< {Q\over288}
\left({8385\over1024}+{1419\over16L}\right).
}
\tag{4.6}

## 5. Cross-deficit contradiction

Using (2.1), dropping only the nonnegative `pA_{Gamma^dagger}(y)`, and applying (2.5), (3.2), and (4.6),
\[
\begin{aligned}
R_1^\dagger
&> -py(66L-154)
 -{Q\over288}
\left({8385\over1024}+{1419\over16L}\right)\\
&\ge -{Q\over288}
\left[
66-{154\over L}+{8385\over1024}+{1419\over16L}
\right]\\
&=-{Q\over288}
\left[
{75969\over1024}-{1045\over16L}
\right]\\
&>-{75969\over294912}Q.
\end{aligned}
\tag{5.1}
\]
The decisive comparison is exact:
\[
\delta-{75969\over294912}
={38782659\over64000000000}>0.
\tag{5.2}
\]
Thus
\[
R_1^\dagger>-0.257598876953125\,Q
>-0.258204856\,Q,
\]
which contradicts the necessary counterexample condition (0.2).  This proves Theorem 1.1.

The integer `288` is close to the barrier of this particular retained envelope: its asymptotic adverse coefficient is `75969/1024 = 74.1884765625`, so this proof architecture alone would require an integer denominator strictly above approximately `287.324`.  This is a limitation of the envelope, not a counterexample to a wider true collar.

## 6. Obstruction checks and status

This theorem uses the exact addressing/MUX primitive rather than an abstract row law.  It is compatible with all previously identified obstructions:

- at `p=1/2`, the peer's `142` collar remains slightly stronger, so no old certificate is weakened;
- as `p->0`, the new proof keeps the selector factor and therefore avoids the artificial linear collapse of the older collar;
- the deterministic faces are genuine AND/OR boundaries, so no unsupported critical-core or coverage assumption enters;
- the complementary-data and balanced-address slices already proved elsewhere remain separate exact closures;
- no per-coordinate erasure estimate, sign-free profile, tensor assumption, or circular potential payment is used.

**Old missing implication.**  The fleet03/B15 theorem closed `y<=Q/(142L)` but lost the selector weight in the physical movements, leaving the small-selector/deterministic-data corner unnecessarily thin.

**New proved inference.**  The same source-exact residual, with the selector weight retained through the two potential terms, the child-AND entropy difference, and the six-mass Shannon movement, proves the larger collar (1.1).  Combined with the peer result, the safe width is (1.2).

**New first missing implication.**  The genuinely interior unequal-MUX region outside the union of these deterministic-face collars and the already-proved common/complementary/zero-credit tubes.  Even a complete MUX proof remains strictly weaker than `LIMIT-PRIME-GATE-LIFT-v1`, which still quantifies over every composition-prime gate and every product bias.

**Classification:** `ESSENTIAL_STEP_APPLIED`.  Full FEI remains **OPEN / NOT PROVED**.

Scoped privacy review: only FEI mathematics, logical fleet labels, source-bound private-repository paths/hashes, and nonsecret constants are included.  No credentials, scheduler IDs, machine paths, unrelated private data, email/Drive action, workflow dispatch, paid compute, public posting, or permission change is included.
