# G0008 — full `NC(4)` association plus cross-parameter stochastic order still does not force the first-step sign

Target: Campos--de Lima square-lattice axis-connectivity monotonicity, first milestone `tau_2(p) <= tau_1(p)` for every `0<p<1`.

Status of this note: **PARTIAL / finite relaxation obstruction**, not a Bernoulli-percolation counterexample and not a solution of the source problem.

This note implements the final STUCK2 recovery selected in the preceding R7-06 report. It changes category from six scalar orbit inequalities to the complete finite poset `NC(4)` of noncrossing boundary partitions, exhausts every increasing event exactly, and then constructs an extremal sparse ordered pair of associated laws that still has the wrong first-step sign at `p=1/3`.

## 1. The `NC(4)` state space and the six orbit coordinates

Let the four neighbours of the deleted central star be labelled cyclically `1,2,3,4`. The boundary connectivity partition is an element of the 14-element noncrossing partition lattice `NC(4)`, ordered by refinement: `pi <= rho` means every block of `pi` is contained in a block of `rho`.

Under `D_4` symmetry the 14 states split into six orbits, with probability **per specified partition**

`theta=(sigma,alpha,beta,gamma,delta,epsilon)`

and orbit sizes

`(1,4,2,2,4,1)`:

- `sigma`: `1|2|3|4`;
- `alpha`: one adjacent pair and two singletons;
- `beta`: one opposite pair and two singletons;
- `gamma`: two disjoint adjacent pairs;
- `delta`: one triple block and one singleton;
- `epsilon`: `1234`.

Thus

`(N)  sigma+4 alpha+2 beta+2 gamma+4 delta+epsilon=1`.

For the retained first-step functional,

\[
\begin{aligned}
F_p(\theta)={}&p\sigma+2p(3-2p)\alpha+(2p-1)\beta\\
&+2p(1-p)(2-p)\gamma\\
&+(2p^3-7p^2+8p-2)\delta-(1-p)^3\epsilon.
\end{aligned}
\tag{1.1}
\]

The exact reduction from the earlier punctured-star work is

\[
\tau_1(p)-\tau_2(p)=(1-p)F_p(\theta_p).
\tag{1.2}
\]

Hence `M_axis>=1` would follow from `F_p(theta_p)>=0` for every `p`.

For the exact detour conservation law define

\[
L_\theta(r)=\sigma+2(1+r)\alpha+(1+r)\beta+2r\gamma+(1+3r^2)\delta+r^3\epsilon.
\tag{1.3}
\]

The actual punctured-star laws satisfy the previously proved scalar relation

\[
L_{\theta_p}(1-p)+L_{\theta_{1-p}}(p)=1.
\tag{1.4}
\]

## 2. B1 — change category: use the complete finite association structure

The connectivity partition is a coordinatewise increasing function of the independent edge states. Therefore its law is positively associated: for every pair of increasing functions `f,g` on `NC(4)`,

\[
\operatorname{Cov}(f,g)\ge0.
\tag{2.1}
\]

On a finite poset it is enough to check indicator functions of all up-sets. Indeed an increasing real function is a constant plus a nonnegative linear combination of indicators of its strict super-level up-sets. Bilinearity then reduces (2.1) to

\[
\mu(U\cap V)\ge \mu(U)\mu(V)
\tag{2.2}
\]

for every pair of up-sets `U,V`.

The exact checker attached to this note generates all 14 noncrossing partitions, constructs the refinement relation, and finds exactly

\[
\boxed{234}
\]

up-sets. It then checks all

\[
\boxed{234\cdot235/2=27495}
\]

unordered up-set pairs for each proposed law, using `fractions.Fraction` only.

This is strictly stronger than the preceding report's four pair-connectivity FKG inequalities: it is the entire positive-association requirement visible from the boundary-partition random variable.

There is a second source-valid finite-poset constraint which the preceding relaxed pair had omitted. If `p<q`, the standard monotone coupling of Bernoulli percolation gives

\[
\boxed{\theta_p\preceq_{\rm st}\theta_q,}
\tag{2.3}
\]

meaning `theta_q(U)>=theta_p(U)` for **every** increasing up-set `U` of `NC(4)`.

The old STUCK2 `q=2/3` fake law violated (2.3). The simplest violated up-set is the event that at least one opposite terminal pair is connected. Its probability is

\[
O(\theta)=2\beta+4\delta+\epsilon.
\tag{2.4}
\]

For the old pair, `O(theta_{1/3})=3/4` while `O(theta_{2/3}^{old})=551/738`, a deficit of `5/1476`. Thus the old pair was not even ordered in the same direction as the genuine punctured percolation family.

## 3. B24 — extremal sparse replacement that saturates the missing order constraint

Keep the exact `p=1/3` negative law from STUCK2:

\[
\boxed{
\theta^-=
\left(\frac14,0,\frac{19}{108},0,\frac1{27},\frac14\right).
}
\tag{3.1}
\]

It has

\[
O(\theta^-)=\frac34.
\tag{3.2}
\]

Seek the sparsest possible `q=2/3` partner by imposing

\[
\alpha^+=\beta^+=\gamma^+=0,
\tag{3.3}
\]

and put the omitted stochastic-order event exactly on its boundary,

\[
O(\theta^+)=\frac34.
\tag{3.4}
\]

Because only `sigma,delta,epsilon` remain, (3.4) and normalization force

\[
\sigma^+=\frac14.
\tag{3.5}
\]

Finally impose the exact scalar primal/dual conservation with the retained lower law,

\[
L_{\theta^+}(1/3)=\frac8{27}.
\tag{3.6}
\]

The two linear equations

\[
\frac14+4\delta^++\epsilon^+=1,
\qquad
\frac14+\frac43\delta^++\frac1{27}\epsilon^+=\frac8{27}
\tag{3.7}
\]

have the unique solution

\[
\boxed{
\theta^+=
\left(\frac14,0,0,0,\frac1{64},\frac{11}{16}\right).
}
\tag{3.8}
\]

This is the new extremal relaxed pair.

## 4. B19 — exact algorithmic feasibility certificate

The attached exact checker establishes simultaneously:

1. `theta^-` is a probability law on `NC(4)` and satisfies **all 27,495** up-set association inequalities. There are 483 zero margins; the smallest strictly positive margin is `1/54`.
2. `theta^+` is a probability law on `NC(4)` and satisfies **all 27,495** up-set association inequalities. There are 467 zero margins; the smallest strictly positive margin is `175/1024`.
3. `theta^- <=_st theta^+` on the **entire 234-up-set poset**. There are 27 equality up-sets; the smallest strictly positive dominance margin is `19/108`.

Thus this is not merely a pair that passes the six elementary connection-event inequalities: both laws are associated for **every** increasing boundary-partition statistic, and the higher-parameter law stochastically dominates the lower-parameter law in the strongest finite-poset sense.

For `theta^+` the association can also be seen directly. Its support is the bottom partition with mass `1/4`, the four triple-block coatoms with mass `1/64` each, and the top partition with mass `11/16`. Every proper nonempty up-set has probability `(44+k)/64`, where `k` is the number of triple-block coatoms it contains. If two such up-sets contain `a` and `b` coatoms with intersection size `c`, then `c>=max(0,a+b-4)` and their association margin, multiplied by `4096`, is

\[
64(44+c)-(44+a)(44+b)
=880+64c-44(a+b)-ab.
\tag{4.1}
\]

The minimum over `0<=a,b<=4` and `c>=max(0,a+b-4)` is `700`, attained at `a=b=2,c=0`; hence the minimum positive margin is exactly

\[
700/4096=175/1024.
\tag{4.2}
\]

The lower-law association and the full stochastic-order statement are finite exhaustive exact claims certified by the checker.

## 5. The stronger relaxed pair still has the wrong source sign

Put `p=1/3`, `q=2/3`. Exact arithmetic gives

\[
L_{\theta^-}(2/3)=\frac{19}{27},
\qquad
L_{\theta^+}(1/3)=\frac8{27},
\tag{5.1}
\]

so

\[
\boxed{L_{\theta^-}(2/3)+L_{\theta^+}(1/3)=1.}
\tag{5.2}
\]

The corresponding detour probabilities have the correct source-side directions:

\[
D(1/3)=1-\frac{19}{27}=\frac8{27}<\frac13,
\qquad
D(2/3)=1-\frac8{27}=\frac{19}{27}>\frac23.
\tag{5.3}
\]

The retained finite-energy leaf-surgery inequalities also hold. At the lower law,

\[
\delta^- - \frac{(2/3)^3}{2}\epsilon^-=0,
\tag{5.4}
\]

while at the upper law

\[
\delta^+ - \frac{(1/3)^3}{2}\epsilon^+=\frac5{1728}>0.
\tag{5.5}
\]

The complete elementary terminal FKG family and the retained BK inequality continue to hold. Writing

\[
S=\alpha+\gamma+2\delta+\epsilon,
\qquad
T=\beta+2\delta+\epsilon,
\tag{5.6}
\]

for the upper law one has `S=T=23/32`, and the five margins from the preceding report are

\[
\frac{191}{1024},\quad
\frac{175}{1024},\quad
\frac{191}{1024},\quad
\frac{175}{1024},\quad
\frac{529}{1024},
\tag{5.7}
\]

all nonnegative. The lower law retains its previously recorded nonnegative margins.

Nevertheless the first-step functional at the lower parameter is still strictly wrong:

\[
\boxed{F_{1/3}(\theta^-)=-\frac{37}{729}<0.}
\tag{5.8}
\]

For completeness,

\[
F_{2/3}(\theta^+)=\frac{133}{864}>0.
\tag{5.9}
\]

## 6. Consequence: the selected full-association recovery is exhausted

The following information is therefore **not sufficient** to force `tau_1(p)>=tau_2(p)`:

- exact `D_4`-symmetric noncrossing-partition normalization;
- positive association for **every** increasing event of `NC(4)` at both parameters;
- the full finite-poset stochastic monotonicity `theta_{1/3} <=_st theta_{2/3}`;
- the complete pairwise terminal FKG inequalities;
- the retained adjacent-pair BK inequality;
- both finite-energy leaf-surgery inequalities;
- the exact scalar primal/dual detour conservation law;
- the correct subcritical/supercritical detour directions.

The witness (3.1),(3.8) is only a pair of abstract boundary-partition laws. It is **not** claimed to be realizable by independent bond percolation on the punctured square lattice. Its role is to prove a no-go theorem for a whole proof architecture.

The genuinely missing information must distinguish actual product-measure connectivity laws from arbitrary associated, stochastically ordered `NC(4)` laws. Candidates include a geometry-sensitive deletion/contraction identity with the correct dual wired annulus, Russo-type derivative constraints tying the whole one-parameter family together, or disjoint-occurrence inequalities that depend on edge witnesses rather than only on the terminal partition.

In particular, adding more scalar FKG inequalities on the same boundary partition is now an exhausted route: the full association cone has already been passed by an exact negative relaxed pair.

## 7. Exact certificate

Checker:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T085600Z__G0008_nc4_association_order_checker.py`

Archived output:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T085600Z__G0008_nc4_association_order_checker.out`

The checker uses exact rational arithmetic only and ends with `ALL_EXACT_CHECKS_PASS`.

## 8. Scope

This note does **not** move the frozen source metric `M_axis`: no all-`p` proof of the `n=1` comparison has been obtained. It is a rigorous obstruction to the final selected recovery route. Under the R7-06 HARD-target protocol, the two stuck recoveries are therefore exhausted and this target must be handed off/retired for this slot rather than given a third recovery cycle.
