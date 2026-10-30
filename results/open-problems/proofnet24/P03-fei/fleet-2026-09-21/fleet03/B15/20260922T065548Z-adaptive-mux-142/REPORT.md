# fleet03/B15 — sharpened currency-adaptive MUX boundary layer

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Publication priority:** unverified; no novelty claim.

## 0. Live candidate, old gap, and peer result consumed

The current all-gate candidate is
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\]
where `Gamma_0` is the committed h96 read-once potential.  The all-gate reformulation reduces full FEI at this center to
\[
D_{\Gamma^\dagger}(P;p)\ge0
\]
for every finite composition-prime Boolean gate `P` and every interior product bias.  The exact composition cocycle would then extend the inequality to every gate and yield `H(f)<=C^dagger I(f)`.  This universal prime-gate implication remains open.

The named compatible other-account result consumed and applied here is fleet01/B16,

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260922T0657Z-adaptive-mux-data-boundary/REPORT.md`,
report blob `6e0c7ada7d87c05be8f57d468a2fa566fa6bd0dd`.

For the unequal-data one-address-bit MUX
\[
M=MUX(A;D_0,D_1),\quad p=\Pr(A=1),\quad x=\Pr(D_0=1),\quad y=\Pr(D_1=1),
\]
it combines the exact fleet04/B12 cross-deficit theorem with the real physical `D_1` split.  Put
\[
Q=p(1-p)x(1-x),\qquad L=\log_2(16/Q).
\]
Any live-candidate counterexample must satisfy
\[
R_1^\dagger<-\delta Q,\qquad \delta:=a^\dagger-0.01=0.258204856,
\tag{0.1}
\]
while the peer proved that `y<=Q/(176L)` forces `R_1^dagger>-(21/88)Q`, hence excludes a counterexample.

The prior missing implication was to enlarge the genuine unequal-data MUX coverage without replacing the exact physical residual by an abstract surrogate.  This report sharpens the peer's adaptive layer by retaining its exact `-68 y` lower-order credit and using the actual value `delta`, rather than weakening (0.1) to `delta>1/4`.

## 1. Theorem

### Theorem 1.1 — sharpened physical-data boundary layer

For every interior `p,x`, define
\[
Q=p(1-p)x(1-x),\qquad L=\log_2(16/Q).
\]
Then
\[
\boxed{
0\le y\le {Q\over142L}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(MUX;p,x,y)\ge0.
}
\tag{1.1}
\]
By exchanging the data branches and by complementing a data bit together with the output, the same statement holds near every deterministic data face `q_j=0` or `q_j=1`, with `Q` formed from the selector and the other data bias.

At `p=x=1/2`, `Q=1/16` and `L=8`, so the certified radius is
\[
{1\over18176},
\]
versus the peer's `1/22528`.  The new collar is wider by the exact factor `176/142=88/71`, about 23.94 percent, and still has no compact-core hypothesis on `p,x`.

## 2. Exact physical residual and inherited source bounds

At `y=0`, the MUX is the NPN-equivalent AND gate `(1-A)D_0`, so the exact physical `D_1` residual obeys
\[
R_1^\dagger(p,x,0)=0.
\tag{2.1}
\]
Write
\[
r_0=(1-p)x,\qquad r=r_0+py.
\]
The exact residual from the consumed source is
\[
\begin{aligned}
R_1^\dagger={}&pA_{\Gamma^\dagger}(y)-\Gamma^\dagger(r)
 +(1-y)\Gamma^\dagger(r_0)
 +y\Gamma^\dagger((1-p)(1-x))\\
&-H_M+(1-y)H_\wedge(1-p,x)
+yH_\wedge(1-p,1-x),
\end{aligned}
\tag{2.2}
\]
where `A_Gamma(u)=Gamma(u)+h_2(V_u)`.

The completed h96 source bounds used by the peer are
\[
0\le\Gamma^\dagger(u)<7,
\qquad
|({\Gamma^\dagger})'(u)|<31\log_2(1/z)+47,
\quad z=\min(u,1-u).
\tag{2.3}
\]
No new interpolation assumption is introduced here.

Since `Q<=1/16`, `L>=8`.  Under (1.1),
\[
y\le {Q\over1136}.
\tag{2.4}
\]
As in the peer proof,
\[
Q=p(1-x)r_0\le r_0,
\qquad
1-r_0\ge p\ge4Q.
\tag{2.5}
\]
Thus every point between `r_0` and `r` remains at distance at least `Q` from both endpoints of `[0,1]`.  The derivative bound, the global `Gamma^dagger<7` bound, and the two-bit child entropy bound therefore give the *unrounded* adverse non-parent-entropy movement
\[
\boxed{(31L-68)y.}
\tag{2.6}
\]
The nonnegative term `pA_{Gamma^dagger}(y)` is still left unused.

## 3. Six-mass entropy movement with the new scale

For the MUX spectrum, only four squared masses change from `y=0`:
\[
w_\varnothing=(1-2r)^2,
\quad w_A=V_p(y-x)^2,
\quad w_1=p^2V_y,
\quad w_{A1}=p(1-p)V_y.
\]
Exactly as in the peer source,
\[
\|w(y)-w(0)\|_1<11y.
\tag{3.1}
\]
Hence total variation satisfies
\[
\theta<{11y\over2}\le {11Q\over284L}=:\theta_0.
\tag{3.2}
\]
Fannes--Audenaert on six atoms and `h_2(t)<=t\log_2(e/t)` imply
\[
|H_M(y)-H_M(0)|
\le \theta\log_2(5e/\theta)
<\theta_0\log_2(5e/\theta_0).
\tag{3.3}
\]
Using `2^L=16/Q` and `e<3`,
\[
\log_2{5e\over\theta_0}
< L+\log_2\!\left({1065\over44}L\right).
\tag{3.4}
\]

We now retain more of the logarithmic structure than the 176-proof.

### Lemma 3.1
For every `L>0`,
\[
\boxed{
\log_2\!\left({1065\over44}L\right)<12+{L\over64}.
}
\tag{3.5}
\]

**Proof.**  Inequality (3.5) is equivalent to
\[
{1065\over44}\,L<4096\,2^{L/64}.
\]
The function `L 2^{-L/64}` is maximized at `L=64/ln2`, where its value is `64/(e ln2)`.  Since `e>2` and `ln2>1/2`, this maximum is strictly below `64`.  But
\[
64<{4096\cdot44\over1065}
\]
because `68160<180224`.  This proves (3.5).  QED.

Consequently
\[
|H_M(y)-H_M(0)|
< {11Q\over284L}\left(L+12+{L\over64}\right).
\tag{3.6}
\]

## 4. Cross-deficit contradiction

Combining (2.1), (2.6), (3.6), and `y<=Q/(142L)` gives
\[
\begin{aligned}
R_1^\dagger
&>-Q\left[
{31L-68\over142L}
+{11\over284L}\left(L+12+{L\over64}\right)
\right]\\
&=-Q\left[
{4683\over18176}-{1\over71L}
\right]\\
&>-{4683\over18176}Q.
\end{aligned}
\tag{4.1}
\]
The decisive comparison is exact:
\[
\delta-{4683\over18176}
={19788013\over35500000000}>0.
\tag{4.2}
\]
Therefore
\[
R_1^\dagger>-0.257647447183099\,Q
>-0.258204856\,Q,
\]
contradicting the necessary counterexample condition (0.1).  This proves Theorem 1.1.

There is a useful near-sharpness statement for **this inherited envelope argument**, not for the true MUX problem.  As `L->infinity`, the displayed adverse coefficient before the negative `1/L` correction tends to
\[
{73\over2K}
\]
when the collar denominator is written as `K L`.  For `K=141`,
\[
{73\over282}=0.2588652482\ldots>\delta,
\]
whereas `K=142` has the needed room.  Thus 142 is the smallest integer scale that can be certified uniformly from these particular inherited coarse bounds without spending the still-unused positive term `pA_{Gamma^dagger}(y)` or sharpening the six-mass entropy estimate.

## 5. Status, failed stronger claim, and replacement obligation

**Exact candidate version:** `Gamma^dagger`, `C^dagger=6.521851214`, `a^dagger=0.268204856`.

**Peer artifact consumed:** fleet01/B16 `20260922T0657Z-adaptive-mux-data-boundary/REPORT.md`, blob `6e0c7ada7d87c05be8f57d468a2fa566fa6bd0dd`, including its fleet04/B12 cross-deficit theorem and exact physical `D_1` residual.

**Prior missing implication:** enlarge the surviving unequal-data MUX region using an actual physical split and the live all-gate candidate.

**New proved inference:** the safe adaptive deterministic-face radius improves from `Q/(176L)` to `Q/(142L)` at every interior selector/other-data bias, preserving every branch cost and the exact cross-deficit currency.

**Exact failed stronger claim for this proof envelope:** replacing `142` by `141` cannot be justified uniformly by the same retained upper envelope, because its asymptotic coefficient `73/282` already exceeds `delta`.  This does **not** refute the actual `Q/(141L)` MUX statement; it identifies the next credit that must be used.

**Replacement obligation / next attack:** retain, rather than discard, the positive term
\[
p[\Gamma^\dagger(y)+h_2(V_y)]
\]
and pair its `y\log(1/y)` contribution directly with the entropy created in `w_1,w_{A1}`.  This is the first unused negative/positive-information credit in the exact physical residual and is the natural way to cross the `K=141` barrier or remove the logarithmic boundary loss altogether.

**Next recipient:** fleet03/B18 for integration into the common all-gate candidate; fleet01/B16 for the credit-retaining refinement.

**Implication to full FEI:** positive but partial.  A larger source-valid region of a genuine composition-prime gate is closed, but universal all-prime/all-bias nonnegativity is still unproved.  Therefore full FEI remains **OPEN**.
