# fleet01/B16 — adaptive physical-data boundary layer for the live MUX obstruction

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated private repository sources were used directly, but no authenticated native brain retrieval/context entered the derivation.  
**Publication priority:** unverified; no novelty claim.

## 0. Exact live candidate and conditional end-to-end deduction

This run binds to the current all-gate candidate used by the FEI convergence campaign:
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\]
where `Gamma_0` is the committed h96 read-once potential. For a Boolean gate `G` under product bias `p`,
\[
D_\Gamma(G;p)=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The compact conditional chain is unchanged and explicit:

1. prove `D_{Gamma^dagger}(P;p)>=0` for every composition-prime finite Boolean gate `P` and every interior product bias;
2. the exact nonnegative gate-composition cocycle extends this to every finite Boolean gate;
3. the all-gate reformulation then gives
   \[
   H(f)\le C^\dagger I(f)
   \]
   for every uniform-cube Boolean function.

Step 1 remains open. This run attacks the closest explicit prime family, the one-address-bit unequal-data MUX, and removes an adaptive neighborhood of every deterministic data face.

## 1. Exact other-account theorem consumed and applied

The named other-account input is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0452Z-unequal-mux-cross-deficit/REPORT.md`, report blob `59ea7f1466e7abeff9d9756654fd6c4efa2bda98`.

For
\[
M=MUX(A;D_0,D_1),\qquad
p=\Pr(A=1),\quad q_0=\Pr(D_0=1),\quad q_1=\Pr(D_1=1),
\]
it proves the exact Poincare currencies
\[
Q_0=p(1-p)q_0(1-q_0),\qquad
Q_1=p(1-p)q_1(1-q_1),
\]
and, crucially, the following necessary condition for a live-candidate counterexample:
\[
D_{\Gamma^\dagger}(M)<0
\Longrightarrow
R_1^\dagger<-(a^\dagger-c_{\rm RO})Q_0,
\qquad c_{\rm RO}=0.01,
\tag{1.1}
\]
where `R_1^dagger` is the exact physical residual obtained by revealing the original data coordinate `D_1`. Numerically
\[
a^\dagger-c_{\rm RO}=0.258204856>\frac14.
\tag{1.2}
\]

The residual itself is source-exact:
\[
\begin{aligned}
R_1^\dagger={}&pA_{\Gamma^\dagger}(q_1)-\Gamma^\dagger(r)
 +(1-q_1)\Gamma^\dagger((1-p)q_0)
 +q_1\Gamma^\dagger((1-p)(1-q_0))\\
&-H_M+(1-q_1)H_\wedge(1-p,q_0)
+q_1H_\wedge(1-p,1-q_0),
\end{aligned}
\tag{1.3}
\]
with `r=(1-p)q_0+pq_1` and `A_Gamma(u)=Gamma(u)+h_2(V_u)`.

I also use the source-current h96 bounds already established in the completed MUX work:
\[
0\le\Gamma^\dagger(u)<7,
\tag{1.4}
\]
and, with `z=min(u,1-u)`,
\[
|({\Gamma^\dagger})'(u)|<31\log_2(1/z)+47
\tag{1.5}
\]
on every source interpolation segment. Continuity makes the resulting segmentwise estimate a global Lipschitz bound on any interval staying a fixed distance from `0,1`.

## 2. New theorem — boundary-adaptive physical data block

Orient the data so
\[
q_0=x\in(0,1),\qquad q_1=y\in[0,1),
\]
and put
\[
Q:=p(1-p)x(1-x),\qquad
L:=\log_2\frac{16}{Q}.
\tag{2.1}
\]
For interior `p,x`,
\[
0<Q\le\frac1{16},\qquad L\ge8.
\tag{2.2}
\]

### Theorem 2.1
If
\[
\boxed{
0\le y\le {Q\over176\,L}
={p(1-p)x(1-x)\over176\log_2(16/[p(1-p)x(1-x)])},
}
\tag{2.3}
\]
then
\[
\boxed{D_{\Gamma^\dagger}(MUX;p,x,y)\ge0.}
\tag{2.4}
\]
For `y>0` the proof gives a strict contradiction to the counterexample condition (1.1); `y=0` is the read-once AND/OR boundary. By the Boolean symmetries exchanging the two data branches and complementing a data bit together with the output, the same conclusion holds near **either** deterministic face `q_j=0` or `q_j=1`, with `Q` computed from the other data coordinate.

This removes the compact-core restrictions `p,x in [1/8,7/8]` from the earlier fixed-width data-boundary collar. The permitted width automatically shrinks with the exact physical currency `Q` as another bias approaches its own boundary.

## 3. Proof: lower-bound the exact physical residual

At `y=0`, the MUX is `(1-A)D_0`, an NPN-equivalent AND gate, and the `D_1` residual is exactly
\[
R_1^\dagger(p,x,0)=0.
\tag{3.1}
\]
Set
\[
r_0=(1-p)x,\qquad r=r_0+py.
\]
Because
\[
Q=p(1-x)r_0\le r_0,
\tag{3.2}
\]
and
\[
1-r_0\ge p\ge4Q,
\tag{3.3}
\]
while (2.3) and `L>=8` imply
\[
y\le {Q\over1408},
\tag{3.4}
\]
every point `u` on the segment `[r_0,r]` satisfies
\[
\min(u,1-u)\ge Q.
\tag{3.5}
\]
Indeed the lower distance only increases from `r_0>=Q`, while the upper distance decreases by at most `py<=y<Q/1408` from a value at least `4Q`.

Applying (1.5) on this segment,
\[
|\Gamma^\dagger(r)-\Gamma^\dagger(r_0)|
\le py\,[31\log_2(1/Q)+47]
\le y[31(L-4)+47].
\tag{3.6}
\]
The convex-combination potential movement satisfies by (1.4)
\[
y[\Gamma^\dagger((1-p)(1-x))-\Gamma^\dagger(r_0)]\ge-7y.
\tag{3.7}
\]
The first term `p A_{Gamma^dagger}(y)` in (1.3) is nonnegative and can be retained as unused positive reserve.

The child-entropy mixture changes from its `y=0` value by
\[
y\,[H_\wedge(1-p,1-x)-H_\wedge(1-p,x)]\ge-2y,
\tag{3.8}
\]
because each two-input AND spectral entropy is at most two bits.

Combining (3.6)--(3.8), all non-parent-entropy adverse movement is bounded by
\[
[31(L-4)+47+7+2]y=(31L-68)y<31Ly.
\tag{3.9}
\]

## 4. Exact six-mass entropy movement

Use the exact MUX squared spectrum. Relative to `y=0`, only four groups move:
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_p(y-x)^2,\\
w_1&=p^2V_y,\\
w_{A1}&=p(1-p)V_y.
\end{aligned}
\]
The other two masses are fixed. From `y<1/1408`,
\[
|\Delta w_\varnothing|\le4y+4y^2,
\qquad
|\Delta w_A|\le2y+y^2,
\]
while
\[
w_1+w_{A1}=pV_y\le4y.
\]
Thus, deliberately rounding upward,
\[
\boxed{\|w(y)-w(0)\|_1<11y.}
\tag{4.1}
\]
Let `theta` be total variation. Then
\[
\theta<{11y\over2}
\le {11Q\over352L}=:\theta_0.
\tag{4.2}
\]
Fannes--Audenaert on the six-point alphabet and the elementary inequality `h_2(theta)<=theta log_2(e/theta)` give
\[
|H_M(y)-H_M(0)|
\le \theta\log_2{5e\over\theta}
\le\theta_0\log_2{5e\over\theta_0}.
\tag{4.3}
\]
The last function is increasing throughout this range.

Now `2^L=16/Q`, hence
\[
{5e\over\theta_0}
={160eL\over Q}
=10eL\,2^L.
\]
Since `e<3`,
\[
\log_2{5e\over\theta_0}
<L+5+\log_2 L.
\tag{4.4}
\]
For `L>=8`,
\[
5+\log_2 L\le L,
\tag{4.5}
\]
(the two sides agree at `L=8` after replacing the strict constant bound above by `5`, and the right derivative thereafter is larger). Therefore
\[
\boxed{|H_M(y)-H_M(0)|<{11Q\over176}.}
\tag{4.6}
\]

## 5. Cross-deficit contradiction

From (2.3) and (3.9),
\[
31Ly\le {31Q\over176}.
\tag{5.1}
\]
Combining (3.1), (3.9), and (4.6),
\[
\boxed{
R_1^\dagger>-
\left({31\over176}+{11\over176}\right)Q
=-{21\over88}Q.
}
\tag{5.2}
\]
Since
\[
{21\over88}<\frac14<0.258204856=a^\dagger-c_{\rm RO},
\tag{5.3}
\]
(5.2) is incompatible with the necessary counterexample condition (1.1), which would require
\[
R_1^\dagger<-0.258204856Q<-\frac14Q.
\]
Hence no live-candidate MUX counterexample can satisfy (2.3), proving Theorem 2.1.

The residual proof leaves an explicit safety reserve of at least
\[
\left(\frac14-\frac{21}{88}\right)Q={Q\over88}
\tag{5.4}
\]
before even using the additional gap `0.258204856-1/4` or the nonnegative term `pA_{Gamma^dagger}(y)`.

## 6. What this changes and what remains open

The preceding fleet01/B14 theorem had a fixed near-deterministic data collar only when the selector and other data bias were both in `[1/8,7/8]`. The new theorem replaces that compact-core condition by the adaptive scale (2.3), valid for **all interior** `p,x`. At the most symmetric point `p=x=1/2`,
\[
Q={1\over16},\quad L=8,
\quad {Q\over176L}={1\over22528},
\]
which is more than five times the previous fixed radius `2^{-17}`.

**Old missing implication:** close the residual MUX cube after the zero-credit/complementary tubes and fixed compact-core data-boundary collar.

**New proved inference:** every deterministic data face has a source-valid, physical, currency-adaptive neighborhood on which a counterexample is impossible, with no compact-core hypothesis on the other biases.

**New first missing implication:** the genuinely interior residual MUX region in which both data biases lie outside their adaptive boundary layers and outside the already-proved zero-credit/complementary/same-cell tubes. The exact fleet04/B12 scalar target
\[
R_0^\dagger+R_1^\dagger\ge-0.258204856(Q_0+Q_1)
\]
remains a natural sufficient inequality there. Closing MUX is still strictly weaker than proving the all-prime-gate implication.

**Implication to full FEI:** positive but partial. The live candidate survives a larger genuine prime-gate region; the all-arity/all-bias prime-gate quantifier remains open.

## 7. Scope and provenance

The proof uses only the current private FEI source, the exact fleet04/B12 cross-deficit theorem, and source-current h96 bounds already consumed by the completed MUX work. It does not rerun the settled read-once certificate. No credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email/Drive action, public posting, paid/remote compute, workflow dispatch, notification change, or permission change is included.
