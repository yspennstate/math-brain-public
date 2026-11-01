# fleet04/B12 — address-thickened complementary-data MUX tube

**Classification:** `ESSENTIAL_STEP_APPLIED / COMPLEMENTARY_MUX_ADDRESS_TUBE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Native `math_brain` and `brain` imports both failed with `ModuleNotFoundError`; no authenticated mathematical-brain receiver context entered the derivation.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and exact peer inputs

Fresh owner control revision `2026-09-22.2` supersedes the stale row-coding mechanism for substantive work and directs every FEI worker to the all-gate inequality
\[
D_\Gamma(G;p)\ge0.
\]
This report stays on the same fixed candidate
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]

Two newest compatible **fleet02** results are consumed source-exactly.

1. `fleet02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md` proves for the balanced-address complementary-data MUX
\[
M(a,x_0,x_1),\qquad t=\Pr(a=1)=1/2,\qquad q_0=q,\ q_1=1-q,
\]
that
\[
F(q):=D_{\Gamma^\dagger}(M;1/2,q,1-q)>0
\]
for every `0<q<1`. More quantitatively, for `0<q<=2^-11`, its source-tail/four-generation lower envelope is `>2.913692716 q`, hence in particular
\[
F(q)>\frac{29}{10}q,
\tag{0.1}
\]
while on `2^-11<=q<=1/2` its exact rational interval certificate has minimum lower bound `>0.0161555`, hence in particular
\[
F(q)>\frac1{64}.
\tag{0.2}
\]

2. The newly completed `fleet02/B14` three-dimensional zero-credit MUX tube proves, from the h96 source representation, that throughout the center window used below the live potential is `60`-Lipschitz:
\[
|\Gamma^\dagger(1/2+x)-C^\dagger|\le60|x|
\qquad (|x|\le2^{-14}).
\tag{0.3}
\]
Its exact implication used here is only this source-valid center Lipschitz bound; no Fannes estimate from that report is reused.

The fleet04/B18 mixed-curvature identity remains preserved as a separate valid interface-B input. Nothing below assumes, uses, or implies
\(\sum_k d_k=O(J)\).

## 1. Exact complementary-data spectrum at an unbalanced address

By complement symmetry take `0<q<=1/2` and put
\[
q_0=q,\qquad q_1=1-q,\qquad
t=\frac12+\tau,\qquad |\tau|<\frac12.
\]
Set
\[
V:=4q(1-q),\qquad A:=(1-2q)^2=1-V,\qquad
d:=1-\frac V2,\qquad z:=4\tau^2.
\]
The exact six biased-Walsh masses are
\[
\boxed{
\begin{aligned}
w_\varnothing&=zA,\\
w_a&=(1-z)A,\\
w_0&=V(1/2-\tau)^2,\\
w_1&=V(1/2+\tau)^2,\\
w_{a0}&=V(1/4-\tau^2),\\
w_{a1}&=V(1/4-\tau^2).
\end{aligned}}
\tag{1.1}
\]
They sum to one identically. The output bias is
\[
r=\frac12+\tau(1-2q).
\tag{1.2}
\]
By symmetry of the input potential,
\[
(1-t)B(q)+tB(1-q)=B(q),
\qquad B(u):=\Gamma^\dagger(u)+h_2(V_u),
\tag{1.3}
\]
so the only new source price relative to `tau=0` is the address term and the shifted output potential.

## 2. Exact entropy cancellation: no six-letter Fannes loss

Normalize the four data-bearing masses in (1.1) by their total mass `V`:
\[
\rho_\tau=
\left(
(1/2-\tau)^2,\,
(1/2+\tau)^2,\,
1/4-\tau^2,\,
1/4-\tau^2
\right).
\tag{2.1}
\]
This is a probability vector. Splitting the address-only mass `A` into `zA` and `(1-z)A` gives the exact identity
\[
\boxed{
\widetilde H_\tau-\widetilde H_0
=A\,h_2(z)+V\,[H(\rho_\tau)-2].
}
\tag{2.2}
\]
Since a four-point entropy is at most two bits,
\[
\boxed{
\widetilde H_\tau-\widetilde H_0\le A\,h_2(z).
}
\tag{2.3}
\]
This is the key new mechanism: the linear movement of the two data atoms cancels inside their four-point Shannon block. The only possible positive entropy increase is the binary split of the address-only atom.

## 3. Address-thickening inequality

From the exact gate slack and (1.3),
\[
D_\tau-F(q)
=d\,[B(t)-C^\dagger]
-\bigl[\Gamma^\dagger(r)-C^\dagger\bigr]
-\bigl[\widetilde H_\tau-\widetilde H_0\bigr].
\tag{3.1}
\]
For `|tau|<=2^-14`, (0.3), symmetry, and (1.2) give
\[
\Gamma^\dagger(t)-C^\dagger\ge-60|\tau|,
\]
\[
-\bigl[\Gamma^\dagger(r)-C^\dagger\bigr]
\ge-60(1-2q)|\tau|.
\tag{3.2}
\]
Also \(V_t=1-z\), hence \(h_2(V_t)=h_2(z)\). Using (2.3),
\[
\begin{aligned}
D_\tau-F(q)
&\ge
-60d|\tau|+d\,h_2(z)
-60(1-2q)|\tau|
-A\,h_2(z)\\
&=
-60|\tau|\,[d+1-2q]+(d-A)h_2(z).
\end{aligned}
\tag{3.3}
\]
The two coefficients collapse exactly:
\[
d+1-2q=2(1-q)^2,\qquad
d-A=\frac V2.
\tag{3.4}
\]
Therefore
\[
\boxed{
D_{\Gamma^\dagger}(M;1/2+\tau,q,1-q)
\ge
F(q)-120(1-q)^2|\tau|+\frac V2 h_2(4\tau^2).
}
\tag{3.5}
\]
In particular,
\[
\boxed{D_\tau\ge F(q)-120|\tau|.}
\tag{3.6}
\]
Equation (3.5) is strictly stronger than a generic continuity/Fannes collar: it retains the exact complementary-data Shannon cancellation and a nonnegative `V h_2(4 tau^2)/2` refund.

## 4. New theorem — a two-dimensional physical tube

### Theorem 4.1

For the fixed live candidate \(\Gamma^\dagger\), let
\[
q_1=1-q_0,\qquad
m:=\min(q_0,1-q_0)\in(0,1/2].
\]
Then
\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)>0
\]
throughout the following address tube:

* if \(0<m\le2^{-11}\),
\[
\boxed{\left|t-\frac12\right|\le\frac m{64}},
\tag{4.1}
\]
and in fact
\[
\boxed{D_{\Gamma^\dagger}>\frac{41}{40}m;}
\tag{4.2}
\]

* if \(2^{-11}\le m\le1/2\),
\[
\boxed{\left|t-\frac12\right|\le2^{-14}},
\tag{4.3}
\]
and in fact
\[
\boxed{D_{\Gamma^\dagger}>\frac{17}{2048}.}
\tag{4.4}
\]

**Proof.** By data/output complement symmetry take `m=q<=1/2`.

For the small branch, (0.1) and (3.6) give
\[
D_\tau>
\frac{29}{10}q-120\frac q{64}
=
\left(\frac{29}{10}-\frac{15}{8}\right)q
=\frac{41}{40}q.
\]
Here \(q/64\le2^{-17}<2^{-14}\), so the source Lipschitz window is valid.

For the compact branch, (0.2), (3.6), and \(|\tau|\le2^{-14}\) give
\[
D_\tau>
\frac1{64}-\frac{120}{2^{14}}
=
\frac{32-15}{2048}
=\frac{17}{2048}.
\]
This proves the theorem. `square`

## 5. Owner-comparable gate margin

For the MUX the exact Poincare denominator is
\[
W_M=\frac{V_t(V_{q_0}+V_{q_1})}{16}
=\frac{V_tV}{8}>0.
\tag{5.1}
\]
Relative to the base potential \(\Gamma_0\), the owner's comparable quadratic gate margin is
\[
c_M
=
a^\dagger-\frac{D_{\Gamma^\dagger}(M)}{W_M}.
\tag{5.2}
\]

On the compact branch, \(W_M\le1/8\), so (4.4) gives
\[
\boxed{
c_M<a^\dagger-\frac{17}{256}
=0.201798606.
}
\tag{5.3}
\]
On the small branch \(V\le4m\), hence \(W_M\le m/2\), and (4.2) gives the much stronger
\[
c_M<a^\dagger-\frac{41}{20}<0.
\tag{5.4}
\]
Thus the entire new complementary-data address tube has the uniform owner-margin bound
\[
\boxed{c_M<0.201798606.}
\tag{5.5}
\]
This is a restricted MUX theorem only; it neither proves decomposable/AND extremality nor full FEI.

## 6. What this changes and what remains open

The balanced complementary-data MUX line was already closed by fleet02/B12. The new result thickens **every point of that entire line in the physical address direction**. Near the singular data endpoints the allowed address width scales as `m/64`; away from the endpoints there is a uniform `2^-14` tube. The proof uses exact entropy cancellation rather than an ambient-alphabet continuity payment.

The one-selector MUX cube is still not fully closed, and arbitrary composition-prime gates remain open. A natural next step is to combine this address tube with the fleet02/B14 zero-credit tube and fleet04/B18's sharpened balanced-address unequal-data collars, then attack the remaining compact MUX complement with a source-exact interval certificate for the fixed \(\Gamma^\dagger\).

No claim of full FEI, publication priority, or \(\sum_k d_k=O(J)\) is made.
