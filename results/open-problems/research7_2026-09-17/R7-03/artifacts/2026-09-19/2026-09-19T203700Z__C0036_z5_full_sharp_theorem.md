# C0036 admission-stage mathematics: full sharp Lyons 5.7 on `Z/5Z`

Date: 2026-09-19 UTC  
Worker: `R7-03 Boundary-Case Research`  
Canonical candidate: `C0036`  
Outside source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Conjecture 5.7, §5.2  
Status: **PARTIAL relative to the all-group source; complete for `Gamma=Z/5Z`**  
Methods: **B6 / B20 / B24**

## 1. Statement proved in this run

Let `Gamma=Z/5Z`, and let `Q` be any `Gamma`-equivariant positive contraction on `ell^2(Gamma)`. Then

\[
\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes\Gamma}
\preccurlyeq P^Q
\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes\Gamma},
\]

and both Bernoulli parameters are optimal.

Combined with the preceding R7-03 theorem for all finite groups of order at most four, this proves the full sharp conjecture for every finite group of order at most five. It does **not** prove Lyons's all-group Conjecture 5.7.

The proof below uses only results already proved in the immediately preceding R7-03 artifacts and re-states every reused ingredient needed for this order-five closure.

## 2. Reused exact order-five reduction

Write the Fourier eigenvalues of the circulant kernel `Q` as

\[
0\le \lambda_0,\ldots,\lambda_4\le1,
\qquad
p=(\lambda_0\lambda_1\lambda_2\lambda_3\lambda_4)^{1/5}
=\operatorname{FK}(Q).
\]

Translation averaging reduces stochastic domination between the invariant measures to translation-invariant increasing tests. The translation quotient of `2^(Z/5Z)` has eleven upper sets. Seven are cardinality thresholds, already proved for every finite group by the preceding all-cardinality theorem. The four remaining upper sets are two pair-orbit events and two triple-orbit events.

Put

\[
\alpha=\frac{5-\sqrt5}{50},\qquad
\beta =\frac{5+\sqrt5}{50}.
\]

Then

\[
\alpha+\beta=\frac15,
\qquad
\alpha\beta=\frac1{125},
\qquad
\beta-\alpha=\frac{\sqrt5}{25}=\sqrt{\alpha\beta}.
\tag{2.1}
\]

For either of the two pair-frequency weight systems `w` on unordered pairs of `Z/5Z`, define

\[
D_w(x):=\sum_{0\le i<j\le4}w_{ij}x_i x_j,
\tag{2.2}
\]

where one system has weight `alpha` on adjacent pairs and `beta` on distance-two pairs, and the other system swaps `alpha,beta`. In either system the weights sum to one and every vertex has total incident weight `2/5`.

The previous exact Cauchy--Binet calculation showed that for the matched spatial pair/triple orbit,

\[
D=p^2D_w(a^{-1}),\qquad
T=p^3D_w(a),\qquad
D_4=p^4\,\frac15\sum_i a_i,
\tag{2.3}
\]

once

\[
a_i:=\frac p{\lambda_i},\qquad \prod_i a_i=1.
\tag{2.4}
\]

The four non-cardinality lower-domination inequalities are exactly

\[
D-T\ge p^2(1-p),
\qquad
T-D_4\ge p^3(1-p)
\tag{2.5}
\]

for the two choices of `w`.

The previous radial-boundary theorem says it is enough to prove (2.5) when

\[
\max_i\lambda_i=1.
\tag{2.6}
\]

Indeed each normalized orbit gap is nonincreasing under common scaling of all `lambda_i`, so the largest admissible scale is hardest. We henceforth assume all eigenvalues are positive and (2.6) holds; zero eigenvalues follow by continuity at the end.

Under (2.6),

\[
r:=\min_i a_i=p.
\tag{2.7}
\]

After a cyclic relabeling take `a_0=r`. Define the two normalized gap functionals

\[
F_T(a):=D_w(a)-1-r\left(\frac15\sum_i a_i-1\right),
\tag{2.8}
\]

\[
F_P(a):=D_w(a^{-1})-1-r\bigl(D_w(a)-1\bigr).
\tag{2.9}
\]

By (2.3),

\[
T-D_4-p^3(1-p)=p^3F_T(a),
\tag{2.10}
\]

\[
D-T-p^2(1-p)=p^2F_P(a).
\tag{2.11}
\]

Thus it remains to prove `F_T(a)>=0` and `F_P(a)>=0` for both weight systems.

## 3. B20: why arbitrary pair smoothing is the wrong algorithm

A natural extremal strategy is to preserve `prod a_i=1` and repeatedly replace two coordinates by their geometric mean. That operation is **not** monotone for the pair gap.

For the adjacent-`alpha` weight system take

\[
a=(1/4,1/4,1,2,8).
\]

The product is one and the minimum is still `r=1/4`. Geometrically average coordinates 1 and 2:

\[
a'=(1/4,1/2,1/2,2,8).
\]

An exact calculation gives

\[
F_P(a')-F_P(a)
=\frac{3(9\sqrt5-17)}{128}>0.
\tag{3.1}
\]

So indiscriminate multiplicative smoothing need not move the functional toward its minimum. The missing structure is the dihedral symmetry of the five-cycle about a coordinate attaining the minimum. That observation leads to the successful deformation below.

## 4. B6/B24: reflection-compatible geometric symmetrization

Reflect the five-cycle about vertex `0`, pairing `1<->4` and `2<->3`. Write

\[
a_1=Xe^s,\quad a_4=Xe^{-s},\qquad
 a_2=Ye^t,\quad a_3=Ye^{-t},
\tag{4.1}
\]

where

\[
X=\sqrt{a_1a_4},\qquad Y=\sqrt{a_2a_3}.
\]

Because every `a_i>=r`,

\[
X\ge r,\qquad Y\ge r.
\tag{4.2}
\]

The product-one constraint is

\[
rX^2Y^2=1.
\tag{4.3}
\]

Let

\[
a^*:=(r,X,Y,Y,X)
\tag{4.4}
\]

be the reflected geometric symmetrization. We prove that **both** gap functionals can only decrease under `a -> a^*`.

### 4.1 Triple-gap functional

First use the weight system with `alpha` on adjacent pairs and `beta` on distance-two pairs. Direct expansion gives

\[
\begin{aligned}
F_T(a)-F_T(a^*)
={}&2XY\{\alpha(\cosh(s+t)-1)+\beta(\cosh(s-t)-1)\}\\
&-2rX\beta(\cosh s-1)-2rY\alpha(\cosh t-1).
\end{aligned}
\tag{4.5}
\]

By (4.2), `rX<=XY` and `rY<=XY`. Hence the right side is at least `2XY H(s,t)`, where

\[
\begin{aligned}
H(s,t):={}&\alpha(\cosh(s+t)-1)+\beta(\cosh(s-t)-1)\\
&-\beta(\cosh s-1)-\alpha(\cosh t-1).
\end{aligned}
\tag{4.6}
\]

Put

\[
u=\sinh(s/2),\qquad v=\sinh(t/2).
\]

Using (2.1) and the half-angle addition formulas,

\[
\boxed{
\frac{H(s,t)}2
=\left(\sqrt\alpha\,u\sqrt{1+v^2}
-\sqrt\beta\,v\sqrt{1+u^2}\right)^2
+(\alpha+\beta)u^2v^2\ge0.
}
\tag{4.7}
\]

Therefore `F_T(a)>=F_T(a^*)`.

For the second weight system, `alpha,beta` are swapped. Its analogue of `H(s,t)` is exactly `H(s,-t)`, so (4.7) proves the same conclusion.

### 4.2 Pair-gap functional

For the same first weight system, expansion of `F_P` gives a stronger cancellation. The mixed `s+-t` terms cancel identically because (4.3) implies

\[
\frac1{XY}=rXY=\sqrt r.
\tag{4.8}
\]

The remaining difference is

\[
\boxed{
\begin{aligned}
F_P(a)-F_P(a^*)={}&
2\alpha\left(\frac1{rX}-r^2X\right)(\cosh s-1)\\
&+2\beta\left(\frac1{rY}-r^2Y\right)(\cosh t-1).
\end{aligned}}
\tag{4.9}
\]

Each coefficient is nonnegative. For example,

\[
\frac1{rX}-r^2X=\frac{1-r^3X^2}{rX},
\qquad
r^3X^2=\frac{r^2}{Y^2}\le1
\tag{4.10}
\]

by (4.2)--(4.3); the `Y` coefficient is identical. Swapping `alpha,beta` proves the second pair orbit as well.

Hence

\[
\boxed{F_T(a)\ge F_T(a^*),\qquad F_P(a)\ge F_P(a^*)}
\tag{4.11}
\]

for both orbit types. Therefore any counterexample would have a palindromic counterexample of the form (4.4). This is the extremal-object reduction supplied by B24.

## 5. Palindromic reduction: two nonnegative variables

Write

\[
X=r+u,
\qquad
Y=r+v,
\qquad u,v\ge0.
\tag{5.1}
\]

From (4.3), after taking the positive square root,

\[
(r+u)(r+v)=r^{-1/2}.
\tag{5.2}
\]

Define

\[
S=u+v,
\qquad
P=uv,
\qquad
c:=r^{-1/2}-r^2.
\tag{5.3}
\]

Then (5.2) is exactly

\[
P+rS=c.
\tag{5.4}
\]

## 6. Triple-orbit inequalities

For the first weight system, direct expansion of (2.8) at `(r,X,Y,Y,X)` gives

\[
F_T
=\beta u^2+\alpha v^2+\frac25uv+\frac{2r}{5}(u+v)-(1-r).
\tag{6.1}
\]

The second weight system swaps `alpha,beta`; the lower bound below is symmetric in that swap.

Using (5.4),

\[
F_T
=\beta u^2+\alpha v^2+\frac25c-(1-r).
\tag{6.2}
\]

Weighted Cauchy and (2.1) give

\[
\beta u^2+\alpha v^2
\ge \frac{\alpha\beta}{\alpha+\beta}(u+v)^2
=\frac{S^2}{25}.
\tag{6.3}
\]

Also (5.2) and AM--GM imply

\[
S+2r=(r+u)+(r+v)\ge2r^{-1/4},
\]

so

\[
S\ge2(r^{-1/4}-r).
\tag{6.4}
\]

Put

\[
q:=r^{1/4}\in(0,1].
\tag{6.5}
\]

Combining (6.2)--(6.4),

\[
\begin{aligned}
F_T
&\ge \frac4{25}(q^{-1}-q^4)^2
+\frac25(q^{-2}-q^8)-(1-q^4)\\
&=\boxed{
\frac{(1-q)^3}{25q^2}
\left(6q^7+18q^6+36q^5+60q^4+65q^3+59q^2+42q+14\right)
}\ge0.
\end{aligned}
\tag{6.6}
\]

Thus both triple-orbit inequalities are proved.

## 7. Pair-orbit inequalities: exact one-dimensional certificate

For the first pair orbit, a direct expansion using (5.4) yields

\[
F_P
=B+\frac{\sqrt5}{25}P(u-v),
\tag{7.1}
\]

while for the second orbit

\[
F_P
=B-\frac{\sqrt5}{25}P(u-v),
\tag{7.2}
\]

where

\[
B:=\frac{cS}{5}+\frac25(r^{1/2}-r^3)+r-1.
\tag{7.3}
\]

It is therefore enough to prove

\[
B\ge \frac{\sqrt5}{25}P|u-v|.
\tag{7.4}
\]

Continue with `r=q^4`. From (5.4),

\[
c=q^{-2}-q^8,
\qquad
P=c-q^4S,
\tag{7.5}
\]

and

\[
(u-v)^2=S^2-4P=S^2+4q^4S-4c.
\tag{7.6}
\]

The actual admissible `S` lies in

\[
S_{\min}=2(q^{-1}-q^4)
\le S\le
q^{-6}-q^4=:S_{\max}.
\tag{7.7}
\]

The lower endpoint is (6.4), while the upper endpoint follows from `P=uv>=0` in (7.5).

### 7.1 First prove `B>=0`

Define

\[
\begin{aligned}
H_q(S):={}&S(q^8+q^6+q^4+q^2+1)\\
&+2q^{12}+2q^{10}+2q^8+2q^6-3q^4-5q^2.
\end{aligned}
\tag{7.8}
\]

Then

\[
25B=\frac{5(1-q)(1+q)}{q^2}H_q(S).
\tag{7.9}
\]

The coefficient of `S` in `H_q` is positive. At the left endpoint,

\[
\boxed{
H_q(S_{\min})
=\frac{(1-q)^2}{q}
(2q^6+4q^5+8q^4+7q^3+8q^2+4q+2)
}\ge0.
\tag{7.10}
\]

Thus `B>=0` throughout the admissible interval.

### 7.2 Square the remaining inequality

Since `B>=0`, (7.4) follows from

\[
\Delta(q,S):=(25B)^2-5P^2(u-v)^2\ge0.
\tag{7.11}
\]

For `q=1`, the spectrum is scalar and equality is immediate. Assume `0<q<1`. The interval width factors as

\[
S_{\max}-S_{\min}
=\frac{(1-q)^2(q^4+q^3+q^2+q+1)^2}{q^6}.
\tag{7.12}
\]

Write

\[
y:=\frac{S-S_{\min}}{S_{\max}-S_{\min}}\in[0,1].
\tag{7.13}
\]

Exact expansion gives

\[
\Delta(q,S(y))=\frac{N_q(y)}{q^{16}},
\tag{7.14}
\]

where `N_q` has degree four in `y`. Write it in the degree-four Bernstein basis,

\[
N_q(y)=\sum_{j=0}^4 b_j(q)\binom4j y^j(1-y)^{4-j}.
\tag{7.15}
\]

The exact coefficients are as follows:

\[
\begin{aligned}
b_0={}&25q^{10}(1-q)^6(1+q)^2
(2q^6+4q^5+8q^4+7q^3+8q^2+4q+2)^2,
\end{aligned}
\tag{7.16}
\]

\[
b_1=\frac52q^5(1-q)^6P_{24}(q),
\tag{7.17}
\]

\[
b_2=\frac53(1-q)^6(1+q)^2P_{32}(q),
\tag{7.18}
\]

\[
\begin{aligned}
b_3={}&\frac{25}{2}(1-q)^6(1+q)^4(q^2+1)^3(q^8+3q^4+1)P_{16}(q),
\end{aligned}
\tag{7.19}
\]

\[
b_4=25(1-q)^6(1+q)^6(q^2+1)^6(q^8+3q^4+1)^2.
\tag{7.20}
\]

Here

\[
\begin{aligned}
P_{24}(q)={}&8q^{24}+48q^{23}+168q^{22}+423q^{21}+858q^{20}+1523q^{19}\\
&+2488q^{18}+3883q^{17}+5788q^{16}+8123q^{15}+10498q^{14}+12313q^{13}\\
&+13008q^{12}+12313q^{11}+10498q^{10}+8123q^9+5788q^8+3883q^7\\
&+2488q^6+1523q^5+858q^4+423q^3+168q^2+48q+8,
\end{aligned}
\tag{7.21}
\]

\[
\begin{aligned}
P_{32}(q)={}&2q^{32}+8q^{31}+24q^{30}+56q^{29}+116q^{28}+238q^{27}+464q^{26}+880q^{25}\\
&+1507q^{24}+2432q^{23}+3612q^{22}+5092q^{21}+6797q^{20}+8612q^{19}\\
&+10312q^{18}+11482q^{17}+11982q^{16}+11482q^{15}+10312q^{14}+8612q^{13}\\
&+6797q^{12}+5092q^{11}+3612q^{10}+2432q^9+1507q^8+880q^7+464q^6\\
&+238q^5+116q^4+56q^3+24q^2+8q+2,
\end{aligned}
\tag{7.22}
\]

and

\[
\begin{aligned}
P_{16}(q)={}&q^{16}+2q^{15}+4q^{14}+6q^{13}+9q^{12}+14q^{11}+20q^{10}+28q^9\\
&+27q^8+28q^7+20q^6+14q^5+9q^4+6q^3+4q^2+2q+1.
\end{aligned}
\tag{7.23}
\]

Every displayed factor is nonnegative for `0<q<=1`; `P_16,P_24,P_32` have strictly positive coefficients. Therefore

\[
b_j(q)\ge0\qquad(0\le j\le4).
\]

Every degree-four Bernstein basis function in (7.15) is nonnegative on `[0,1]`, hence `N_q(y)>=0`, so `Delta(q,S)>=0`. By `B>=0`, (7.4) follows, and therefore both signs (7.1)--(7.2) are nonnegative.

Thus both pair-orbit inequalities are proved.

## 8. Conclusion of the lower stochastic domination

Sections 4--7 show all four non-cardinality invariant upper-set inequalities on `Z/5Z`. The preceding all-finite cardinality theorem covers the seven cardinality upper sets. By the already-proved translation-averaging/layer-cake reduction,

\[
\boxed{
\operatorname{Ber}(p)^{\otimes\Gamma}\preccurlyeq P^Q,
\qquad p=\operatorname{FK}(Q),
\qquad \Gamma=\mathbb Z/5\mathbb Z.
}
\tag{8.1}
\]

We proved this for positive eigenvalues. If one or more eigenvalues vanish, approximate `Q` within the compact finite-dimensional cone by positive contractions with positive spectrum; all finitely many event probabilities and `FK(Q)` are continuous, so (8.1) passes to the boundary. Equivalently, when `FK(Q)=0`, the lower product measure is the deterministic empty configuration and the domination is immediate.

## 9. Upper stochastic domination and sharpness

Apply (8.1) to `I-Q`. Since `I-Q` is again a `Z/5Z`-equivariant positive contraction,

\[
\operatorname{Ber}(\operatorname{FK}(I-Q))^{\otimes\Gamma}
\preccurlyeq P^{I-Q}.
\]

Complementing configurations reverses the order and transforms `P^{I-Q}` into the complement of `P^Q`. Hence

\[
\boxed{
P^Q\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes\Gamma}.
}
\tag{9.1}
\]

The constants are optimal. If product density `theta` is stochastically dominated by `P^Q`, applying the full-set event gives

\[
\theta^5\le\det Q=\operatorname{FK}(Q)^5,
\]

so `theta<=FK(Q)`. Applying the analogous empty-set event to an upper product bound forces its density to be at least `1-FK(I-Q)`.

This completes the sharp two-sided theorem on `Z/5Z`.

## 10. Exact self-check scope

The companion exact SymPy self-check verifies:

1. the algebraic identities (2.1);
2. the exact B20 counterexample (3.1) to arbitrary pairwise smoothing;
3. the reflection/palindromic identities used in Sections 4--7;
4. the triple lower-bound factorization (6.6);
5. the `B>=0` factorization (7.9)--(7.10);
6. the denominator `q^16`, degree four, and all five exact Bernstein coefficient formulas (7.16)--(7.23).

It ends `ALL_EXACT_CHECKS_PASS`. This is **owner-track self-validation**, not a P26 or OTHER-track independent audit.

## 11. Scope and next obstruction

This run raises the largest finite group order for which R7-03 has a complete sharp proof from `4` to `5`. Since the unique group of order five is `Z/5Z`, there is no missing order-five group.

The source remains much broader. The next finite order is six, with two nonisomorphic groups, `Z/6Z` and `S_3`. The order-five proof depended on a very special fact: after the radial reduction, choosing a minimum coordinate and reflecting the five-cycle leaves exactly two geometric-mean variables and produces the identity `beta-alpha=sqrt(alpha beta)`, which makes the triple symmetrization a square. At order six there are more subset-orbit types and this one-reflection reduction need not close all invariant upper sets. Therefore this artifact is **PARTIAL relative to C0036**, not a source-level closure claim.
