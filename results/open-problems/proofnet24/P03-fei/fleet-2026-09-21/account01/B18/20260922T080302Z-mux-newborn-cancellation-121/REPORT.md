# account01/B18 — exact newborn-entropy cancellation sharpens the MUX data boundary to 121

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated private GitHub sources were used, but no authenticated native brain retrieval/receiver context entered the derivation.  
**Publication priority:** unverified; no novelty claim.

## 0. Live candidate, conditional end-to-end argument, and first missing implication

The source-current all-gate candidate is
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
 a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\]
where `Gamma_0` is the committed h96 read-once potential.  For every finite Boolean gate `G` under an interior product bias `p`, write
\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]
The source-exact gate reformulation says that if one proves
\[
D_{\Gamma^\dagger}(P;p)\ge0
\tag{0.1}
\]
for every finite composition-prime Boolean gate `P` and every interior product bias, then the exact gate-composition cocycle extends (0.1) to every gate and yields
\[
H(f)\le C^\dagger I(f)
\]
for every uniform-cube Boolean function.  The universal prime-gate assertion (0.1) remains open.

The current explicit prime hard family is the one-address-bit MUX
\[
M=MUX(A;D_0,D_1),\qquad
p=\Pr(A=1),\quad x=\Pr(D_0=1),\quad y=\Pr(D_1=1).
\]
This report attacks the first surviving physical boundary inference for that exact live candidate.

## 1. Exact named peer theorem consumed

I substantively use account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T065548Z-adaptive-mux-142/REPORT.md`,

immutable commit `61bae1f3e67af6b8d07fb599e5d1ceaa1775686a`.  Put
\[
Q=p(1-p)x(1-x),\qquad L=\log_2{16\over Q},
\qquad \delta=a^\dagger-0.01=0.258204856.
\tag{1.1}
\]
The peer applies the exact physical `D_1` split and the account04/B12 cross-deficit theorem.  A live-candidate counterexample must satisfy
\[
R_1^\dagger<-\delta Q.
\tag{1.2}
\]
At `y=0`, the MUX is an NPN-equivalent AND gate and
\[
R_1^\dagger(p,x,0)=0.
\tag{1.3}
\]
The exact residual is
\[
\begin{aligned}
R_1^\dagger={}&pA_{\Gamma^\dagger}(y)-\Gamma^\dagger(r)
 +(1-y)\Gamma^\dagger(r_0)
 +y\Gamma^\dagger((1-p)(1-x))\\
&-H_M+(1-y)H_\wedge(1-p,x)
+yH_\wedge(1-p,1-x),
\end{aligned}
\tag{1.4}
\]
where
\[
r_0=(1-p)x,\qquad r=r_0+py,\qquad
A_\Gamma(u)=\Gamma(u)+h_2(V_u).
\]
The same source supplies the h96 bounds
\[
0\le\Gamma^\dagger(u)<7,
\qquad
|({\Gamma^\dagger})'(u)|<31\log_2(1/z)+47,
\quad z=\min(u,1-u).
\tag{1.5}
\]
The peer proved the safe layer `y<=Q/(142L)` but explicitly identified the unused positive term `p A_{Gamma^dagger}(y)` as the next credit to retain.  The derivation below retains its Shannon part exactly instead of sending it through Fannes--Audenaert.

I also apply account03/B14

`proofnet24/P03-fei/fleet-2026-09-21/account03/B14/20260922T073515Z-mux-data-block-selector/REPORT.md`, immutable commit `0fa21049824c4077170a5e39b8289d0ee4acd8f4`, only at the end to state the strengthened residual region: its terminal two-data-bit split gives the independent necessary margin filter (7.2) below.

## 2. New theorem

### Theorem 2.1 — `121` boundary layer

For every interior `p,x`, with `Q,L` as in (1.1),
\[
\boxed{
0\le y\le {Q\over121L}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(MUX;p,x,y)\ge0.
}
\tag{2.1}
\]
By exchanging the two data branches and complementing the data/output orientation, the same conclusion holds near each deterministic data face `q_j=0` or `q_j=1`, with `Q` formed from the selector and the other data bias.

At `p=x=1/2`, `Q=1/16` and `L=8`, so (2.1) gives
\[
y\le {1\over15488},
\]
versus the previous `1/18176`.  The uniform adaptive radius is enlarged by the exact factor
\[
{142\over121}=1.173553719\ldots.
\]

## 3. Geometry and the non-parent terms

Because `Q<=1/16`, one has `L>=8`.  Under (2.1),
\[
y\le {Q\over968}\le {1\over15488}.
\tag{3.1}
\]
Moreover
\[
Q=p(1-x)r_0\le r_0,
\qquad
1-r_0\ge p\ge4Q.
\tag{3.2}
\]
Hence every point of `[r_0,r_0+py]` remains at distance at least `Q` from both endpoints of `[0,1]`.  Applying (1.5),
\[
|\Gamma^\dagger(r)-\Gamma^\dagger(r_0)|
<py[31\log_2(1/Q)+47]
=py(31L-77).
\tag{3.3}
\]
The convex-combination potential term changes by at worst `7y`, and the two-input AND child entropy by at worst `2y`.  Therefore all terms in (1.4) other than `pA_{Gamma^dagger}(y)` and the parent spectral-entropy change have the lower bound
\[
\boxed{
-p(31L-77)y-9y.
}
\tag{3.4}
\]
This is the source-valid form of the peer's `(31L-68)y` estimate, with the factor `p` retained.

## 4. Exact cancellation of the newborn spectral entropy

Let
\[
\phi(t)=t\log_2(1/t),\qquad \phi(0)=0,
\quad V=V_y=4y(1-y),\quad A=V_p=4p(1-p).
\]
The six nonzero MUX spectral masses are
\[
(1-2r)^2,\quad A(y-x)^2,\quad (1-p)^2V_x,\quad p^2V,
\quad p(1-p)V_x,\quad p(1-p)V.
\tag{4.1}
\]
Only the first two old masses move, and the last two `D_1` masses are born from zero.  Thus, with `a_0=1-2r_0`,
\[
\begin{aligned}
H_M(y)-H_M(0)={}&
[\phi((a_0-2py)^2)-\phi(a_0^2)]\\
&+[\phi(A(x-y)^2)-\phi(Ax^2)]\\
&+\phi(p^2V)+\phi(p(1-p)V).
\end{aligned}
\tag{4.2}
\]
This identity is the point of the refinement: the newborn entropy can be paired exactly with the positive leaf term `p h_2(V)`.

### Lemma 4.1 — the newborn pair costs only `O(py)`

One has
\[
\boxed{
 p h_2(V)-\phi(p^2V)-\phi(p(1-p)V)
\ge -{25\over4}py.
}
\tag{4.3}
\]

**Proof.** Direct expansion cancels the entire `V log(1/V)` term:
\[
\begin{aligned}
&p h_2(V)-\phi(p^2V)-\phi(p(1-p)V)\\
&=p(1-V)\log_2{1\over1-V}
-pV\left[(1+p)\log_2{1\over p}+(1-p)\log_2{1\over1-p}\right].
\end{aligned}
\tag{4.4}
\]
The bracket equals `h_2(p)+p log_2(1/p)`.  Since `h_2(p)<=1` and
\[
p\log_2(1/p)\le {1\over e\ln2}<{9\over16},
\tag{4.5}
\]
(the last inequality follows from `e>8/3` and `ln2>2/3`), the bracket is below `25/16`.  Since `V<=4y`, dropping the first nonnegative term in (4.4) proves (4.3).  QED.

### Lemma 4.2 — the two moving old atoms are Lipschitz without a Shannon logarithm

Let `X(s)=phi(s^2)`.  The source-used elementary bound
\[
|X'(s)|<{21\over4}\qquad(|s|\le1)
\tag{4.6}
\]
gives
\[
|\phi((a_0-2py)^2)-\phi(a_0^2)|
<{21\over2}py.
\tag{4.7}
\]
For fixed `A in [0,1]`, put `F_A(s)=phi(A s^2)`.  If `t=As^2`, then
\[
|F_A'(s)|
={2\sqrt{At}\over\ln2}|\ln(1/t)-1|
\le {2\over\ln2}\sqrt t\,|\ln(1/t)-1|.
\]
Writing `u=ln(1/t)>=0`, the function `e^{-u/2}|u-1|` is at most `1`; hence
\[
|F_A'(s)|\le {2\over\ln2}<3.
\tag{4.8}
\]
Therefore
\[
|\phi(A(x-y)^2)-\phi(Ax^2)|<3y.
\tag{4.9}
\]

Combining (4.2)--(4.9),
\[
\boxed{
 p h_2(V)-[H_M(y)-H_M(0)]
> -\left({67\over4}p+3\right)y.
}
\tag{4.10}
\]
No Fannes--Audenaert logarithm remains.

## 5. Proof of Theorem 2.1

Split
\[
pA_{\Gamma^\dagger}(y)=p\Gamma^\dagger(y)+p h_2(V).
\]
The first term is nonnegative by (1.5), so combine (3.4) with (4.10):
\[
\begin{aligned}
R_1^\dagger
&>-[p(31L-77)+9]y-\left({67\over4}p+3\right)y\\
&=-\left(31pL+12-{241\over4}p\right)y.
\end{aligned}
\tag{5.1}
\]
Under `y<=Q/(121L)`,
\[
R_1^\dagger
>-{Q\over121}
\left[31p+{12-(241/4)p\over L}\right].
\tag{5.2}
\]
For `L>=8`, the bracket is increasing in `p`, because
\[
31-{241\over4L}>31-{241\over32}>0.
\]
At `p=1` it is
\[
31-{193\over4L}<31.
\]
Consequently
\[
\boxed{
R_1^\dagger>-{31\over121}Q.
}
\tag{5.3}
\]
The comparison with the exact counterexample threshold is
\[
\delta-{31\over121}
={30348447\over15125000000}>0.
\tag{5.4}
\]
Thus (5.3) contradicts the necessary condition (1.2).  This proves (2.1).

The proof still leaves the entire nonnegative term `p Gamma^dagger(y)` unused.  It also uses only the coarse global constants `31`, `7`, and the two-bit entropy cap; no unavailable h96 certificate bytes are inserted.

## 6. What changed, what failed, and why `120` is not claimed

**Old missing implication.**  The peer theorem certified `y<=Q/(142L)` and explicitly left the positive leaf-information term unused.

**New proved inference.**  Exact pairing of `p h_2(V_y)` with the two newborn Fourier atoms removes the Fannes `y log(1/y)` loss and improves the universal adaptive denominator from `142` to `121`.

The same envelope does **not** certify denominator `120`: after all lower-order terms vanish relative to `L`, (5.1) has limiting coefficient `31/120=0.258333...`, which is larger than `delta=0.258204856`.  This is a limitation of this proof envelope, not a counterexample to the actual `120` statement and not evidence against FEI.  Crossing `120` requires spending some of `p Gamma^dagger(y)` or improving the source derivative constant.

## 7. New exact residual MUX region

The independent account03/B14 terminal two-data-bit theorem gives, with `V_j=4q_j(1-q_j)`,
\[
W_M={t(1-t)(V_0+V_1)\over4}
\tag{7.1}
\]
and every live-candidate MUX counterexample must satisfy
\[
\boxed{
\bar c_D(t,q_0,q_1)>
0.268204856+{4V_0V_1\over\ln2\,(V_0+V_1)}.
}
\tag{7.2}
\]
Combining that exact physical margin filter with Theorem 2.1 and the already-proved selector tube, any surviving MUX counterexample must simultaneously:

1. lie outside the selector tube `|q_1-q_0|<=m/224`, `|t-1/2|<=1/464`, where `m=min(q_0+q_1,2-q_0-q_1)`;
2. lie outside every deterministic-data adaptive layer (2.1) after the data/output symmetries; and
3. satisfy the strict data-block margin condition (7.2).

This is now the first explicit MUX residual to attack.  Closing it would close this composition-prime family only; the universal composition-prime gate quantifier in (0.1) would still remain.

**Implication to full FEI:** positive but partial.  The theorem removes a larger source-valid physical region of a genuine prime gate.  It is not a full FEI proof and does not replace the remaining all-prime/all-bias obligation.
