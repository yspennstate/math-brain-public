# fleet04/B18 — a genuine unequal-data MUX tube for the stable FEI gate candidate

**Classification:** `ESSENTIAL_STEP_APPLIED / JOINT_MUX_TUBE`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and exact predecessor

The current owner target is the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The source gate-reformulation theorem proves that one symmetric nonnegative finite-cap `Gamma` satisfying (0.1) for every Boolean gate and every interior product bias implies full uniform-cube FEI. The current fixed candidate is

\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=0.268204856,
\tag{0.2}
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\tag{0.3}
\]

with `Gamma_0` the committed h96 read-once candidate.

This run consumes substantively the newest fleet01/B18 result

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`,
observed blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`.

For the one-bit MUX
\[
M(a,x_0,x_1)=(1-a)x_0+a x_1,
\]
it proves that for
\[
0<q\le\frac12,
\qquad
q_0=q,\ q_1=1-q,
\qquad
\left|t-\frac12\right|\le {q^2\over8192},
\tag{0.4}
\]
we have the quantitative reserve
\[
\boxed{D_{\Gamma^\dagger}(M;t,q,1-q)>{89\over4096}q.}
\tag{0.5}
\]
The first missing inference stated there is to remove the complementary-data relation `q_1=1-q_0`. The theorem below does that on an explicit source-valid neighborhood while simultaneously retaining the address perturbation (0.4).

The source facts on `Gamma_0` used below are the same ones already source-bound in fleet01/B18 and the preceding fleet04/B18 report: on the small side `u=2^{-x}`,
\[
\Gamma_0(u)=uG(x),
\]
with
\[
2.22922< G(x)-4.9096x <8.62812,
\qquad |G'(x)|<31,
\tag{0.6}
\]
and `1/ln 2<3/2`. The h96 output gives the wobble range, and the committed transformed slope bound `|Ghat'|<=30.080` gives the deliberately weakened derivative bound above.

## 1. Exact biased spectrum and Poincare currency of a general one-bit MUX

Let the independent input biases be
\[
\Pr[a=1]=t,\qquad \Pr[x_0=1]=q_0,\qquad \Pr[x_1=1]=q_1,
\]
and set
\[
r=(1-t)q_0+tq_1,
\quad V_t=4t(1-t),\quad V_j=4q_j(1-q_j).
\]
For either sign convention of the Boolean output, the six squared biased-Walsh masses are
\[
\boxed{
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_a&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_0,\\
w_1&=t^2V_1,\\
w_{a0}&={V_tV_0\over4},\\
w_{a1}&={V_tV_1\over4}.
\end{aligned}}
\tag{1.1}
\]
They sum to one.

The normalized influence prices are
\[
\boxed{
{\operatorname{It}_a\over V_t}=d:=q_0+q_1-2q_0q_1,
\qquad
{\operatorname{It}_0\over V_0}=1-t,
\qquad
{\operatorname{It}_1\over V_1}=t.}
\tag{1.2}
\]
Consequently
\[
D_{\Gamma^\dagger}(M)
=dB(t)+(1-t)B(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
\tag{1.3}
\]
where
\[
B(u):=\Gamma^\dagger(u)+h_2(V_u).
\]

There is also a useful exact bridge to fleet04/B12's child-slack/Poincare recursion. Splitting on the address leaves two literals, so all child Poincare currencies vanish. Its exact `Q`-formula therefore gives
\[
\boxed{
W_M:={I(M)\over4}-r(1-r)
=t(1-t)\bigl[q_0(1-q_0)+q_1(1-q_1)\bigr]
={V_t(V_0+V_1)\over16}.}
\tag{1.4}
\]
Thus the MUX is an especially clean all-gate test: its whole margin is the one Shannon-split residual, with no hidden child slack.

## 2. Source-valid derivative bounds needed for a data perturbation

Write
\[
L=\log_2(1/q)\ge1.
\]
The tube below has `|eta|<=q^2/2^18`, hence every point between `q` and `q-eta` has smaller symmetric representative at least `q/2`. Therefore its logarithmic coordinate obeys `x<=L+1`.

From (0.6),
\[
|G(x)|<4.9096x+8.62812.
\]
Since
\[
\Gamma_0'(u)=G(x)-{G'(x)\over\ln2},
\]
we obtain throughout that interval
\[
|\Gamma_0'(u)|
<4.9096x+8.62812+{93\over2},
\]
and the quadratic lift contributes at most `a^dagger`. Hence
\[
\boxed{|(\Gamma^\dagger)'(u)|<5L+61.}
\tag{2.1}
\]

For the entropy part, put `z=|1-2u|`, so `V_u=1-z^2`. Direct differentiation gives
\[
\left|{d\over du}h_2(V_u)\right|
=4z\left|\log_2{z^2\over1-z^2}\right|.
\tag{2.2}
\]
If `z^2>=1-z^2`, the right side is at most `4 log_2(1/V_u)<=4 log_2(1/v)`, where `v=min(u,1-u)`. If `z^2<1-z^2`, it is at most `8z log_2(1/z)<8`, while `4(L+1)>=8`. Therefore in both cases
\[
\boxed{
\left|{d\over du}h_2(V_u)\right|\le4(L+1).}
\tag{2.3}
\]
Combining (2.1)-(2.3),
\[
\boxed{|B'(u)|<9L+65.}
\tag{2.4}
\]

Near the center, the same source estimates give the coarse but sufficient bound
\[
|({\Gamma^\dagger})'(u)|<66
\tag{2.5}
\]
throughout every point encountered below. Since `Gamma^dagger(1/2)=C^dagger` and the address tube has `|t-1/2|<=1/32768`, this also gives
\[
\boxed{B(t)<8.}
\tag{2.6}

## 3. Perturb the second data bias away from complementarity

Keep `t` and `q_0=q` fixed and write
\[
q_1=1-q+\eta.
\tag{3.1}
\]
The complementary reference point is `eta=0`. Let `w^\eta,w^0` be the six spectral laws from (1.1).

Only three groups of masses change. First, the empty coefficient mean changes by `-2t eta`, so
\[
|w_\varnothing^\eta-w_\varnothing^0|<3|\eta|.
\tag{3.2}
\]
Second,
\[
|w_a^\eta-w_a^0|
=V_t\left|(1-2q+\eta)^2-(1-2q)^2\right|
<3|\eta|.
\tag{3.3}
\]
Third, the two atoms using `V_1` have total coefficient
\[
t^2+{V_t\over4}=t,
\]
and
\[
|V(q-\eta)-V(q)|<5|\eta|.
\]
Since the address tube gives `t<0.501`, their total `l1` change is `<3|eta|`. Thus
\[
\boxed{\|w^\eta-w^0\|_1<9|\eta|,
\qquad \delta_{TV}<5|\eta|.}
\tag{3.4}
\]

Fannes--Audenaert on the six-point alphabet, and monotonicity of `x log(5e/x)` in this tiny range, yield
\[
|H(w^\eta)-H(w^0)|
\le h_2(\delta)+\delta\log_2 5
<5|\eta|\log_2{3\over|\eta|}.
\tag{3.5}
\]

The remaining terms in (1.3) change as follows.

* `d` changes by `(1-2q)eta`, so by (2.6) the address-price loss is `<8|eta|`.
* By symmetry `B(q_1)=B(q-eta)`. Equations (2.4) and `t<0.501` give data-price loss
  \[
  <(5L+33)|\eta|.
  \tag{3.6}
  \]
* The output bias changes by `t eta`; (2.5) gives output-potential loss `<34|eta|`.

Therefore, relative to the already-proved complementary point at the same address bias,
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)
>
D_{\Gamma^\dagger}(M;t,q,1-q)
-(5L+75)|\eta|
-5|\eta|\log_2{3\over|\eta|}.}
\tag{3.7}

## 4. Joint address-and-data tube theorem

Assume
\[
\boxed{
0<q\le\frac12,
\qquad
\left|t-\frac12\right|\le{q^2\over8192},
\qquad
|\eta|\le {q^2\over2^{18}},
\qquad
q_0=q,\quad q_1=1-q+\eta.}
\tag{4.1}
\]
The last condition keeps `q_1` interior because `|eta|<q`.

The function `x log(3/x)` is increasing on the entire allowed `eta` range, so (3.7) and (4.1) imply a total perturbation loss at most
\[
{q^2\over2^{18}}
\left[15L+165+5\log_2 3\right].
\tag{4.2}
\]
Now
\[
qL=q\log_2(1/q)\le h_2(q)\le1,
\tag{4.3}
\]
and
\[
\log_2 3<{8\over5}
\tag{4.4}
\]
because `3^5=243<256=2^8`. Since `q<=1/2`, (4.2) is strictly less than
\[
{q\over2^{18}}\left(15+{165+8\over2}\right)
={101.5\over262144}q
<{q\over2500}.
\tag{4.5}
\]

Insert fleet01/B18's base reserve (0.5):
\[
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)
>
\left({89\over4096}-{1\over2500}\right)q.
\]
Since
\[
{89\over4096}-{1\over2500}-{1\over48}
={3803\over7680000}>0,
\]
we have proved:

### Theorem 4.1 — genuinely unequal-data MUX tube

For every parameter tuple satisfying (4.1),
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)>{q\over48}>0.}
\tag{4.6}
\]
By exchanging the two data labels, the symmetric `q>1/2` form follows. Boundary values follow by continuity.

This is a genuine three-parameter non-unate prime-gate family: the address may move off `1/2`, and the two data biases are no longer required to be complementary.

The owner requests gate margins rather than incomparable raw defects. Let `c_M` denote the margin demanded relative to the base `Gamma_0`, so
\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger W_M,
\qquad
c_M=a^\dagger-{D_{\Gamma^\dagger}\over W_M}.
\tag{4.7}
\]
Within (4.1), `V_0<=4q` and `V_1<=4(q+|eta|)<5q`, so (1.4) gives
\[
W_M<{9q\over16}.
\tag{4.8}
\]
Combining (4.6)-(4.8),
\[
\boxed{
c_M<a^\dagger-{1\over27}
=0.2311678189629629\ldots<a^\dagger.}
\tag{4.9}
\]
Thus this unequal-data tube lies a definite margin below the current lift.

## 5. Integration with the current FEI proof chain

**PROVED here:** the fleet01/B18 complementary-data address tube extends to the genuinely unequal-data tube (4.1), with explicit positive defect and gate-margin reserve. This is an actual application of the newest peer result, not a parallel reproof of its midline.

**PROVED earlier and preserved:**

* the exact gate reformulation and nonnegative composition cocycle reduce a fixed candidate to arbitrary composition-prime gates;
* fleet04/B12's exact child-slack/Poincare recursion remains valid, and for MUX specializes to the exact currency identity (1.4);
* fleet04/B13's current EQ boundary collar, fleet04/B14's physical two-face selector/orientation dichotomy, the mixed-curvature law, and the exact zero-depth one-point classification remain compatible local resources;
* all known refuted bridges remain refuted, including blind arity induction, old AND/decomposable extremality, fixed-coordinate payment, and treating ordinary depth as `O(J)`.

**Still unpaid:** (4.6) is not the full unequal-data MUX theorem. It does not cover large `|q_0+q_1-1|`, large address displacement, or arbitrary composition-prime gates. Therefore it is not an unconditional all-gate closure and does not prove FEI.

The smallest immediate continuation is now to enlarge the data-asymmetry radius by using the exact six-mass formula (1.1) rather than only Fannes continuity, or to produce a source-valid MUX bias outside the tube with negative `D_{Gamma^dagger}`. Either outcome directly attacks the same live all-gate implication.

## 6. Verification and provenance

`CHECKER.py` checks (1.1) and (1.4) over an exact-rational bias grid, Parseval exactly, the tube arithmetic constants, and the margin conversion. These checks support the algebra; the source-potential derivative bounds and the inherited reserve (0.5) are analytic/source-bound premises stated above, not inferred from the finite checker.

No benchmark gold, email/Drive, paid or remote compute, workflow dispatch, notification change, permission change, unrelated private data, or public release entered this run. No novelty or publication-priority claim is made.
