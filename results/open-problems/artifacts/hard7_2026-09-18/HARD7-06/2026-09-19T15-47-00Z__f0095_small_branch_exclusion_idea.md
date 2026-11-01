# HARD7-06 idea checkpoint — exclude the small-positive-mass cavity branch

Runtime model for this run: **GPT-5.6 Sol; reasoning level UNVERIFIED, not GPT-6 maximum.**

Target remains the admitted F0095 ordinary sparse Erdős–Rényi 3-colourability threshold problem. Frozen metric remains `W_3=0.6565076662`; this idea is structural rather than another decimal optimisation.

Previous HARD7-06 work derived, for an infinite-support convex-mixture local minimizer of the q=3 ACG functional in the transformed coordinate `lambda=(1-alpha)/(2+alpha)`, the exact cavity RDE

\[
\Lambda\stackrel d= T:=\frac{1-2P+Q}{2-P},\qquad
P=\prod_i(1-\Lambda_i),\quad Q=\prod_i(1-2\Lambda_i),
\]

with a Poisson(d) cloud of iid incoming messages, and the atom equation

\[
q:=\Pr(\Lambda>0)=1-e^{-dq}(1+dq).
\]

At `d=4.6865076662` the previous exact certificate left two nonzero branches, `q in (0.1388,0.1389)` and `q in (0.9319,0.9320)`.

This run changes method triple to **B5 / B20 / B24**.

## B5 — add a scalar order parameter: the first moment

Let `m=E Lambda`. Since `2-P>=1`,

\[
T\le 1-2P+Q.
\]

The Poisson generating functional gives

\[
E P=e^{-dm},\qquad E Q=e^{-2dm}.
\]

Therefore every nontrivial cavity fixed point must satisfy

\[
m\le (1-e^{-dm})^2<d^2m^2,
\]

hence

\[
m>1/d^2.
\]

This is a necessary lower bound on the mean of any nonzero fixed point.

## B24 — extremize the outgoing message at fixed positive-input count

For one coordinate `x`, holding the other products

\[
A=\prod_{j\ne i}(1-\lambda_j),\qquad B=\prod_{j\ne i}(1-2\lambda_j),
\]

the derivative of `T` has numerator

\[
AB+3A-4B.
\]

Because `0<=B<=A^2<=1`, this is at least

\[
A^3+3A-4A^2=A(A-1)(A-3)>=0.
\]

Thus `T` is coordinatewise increasing. Conditional on exactly `K=k` positive inputs, the largest possible output occurs when all positive inputs equal `1/2`, giving

\[
t_k=\frac{2^k-2}{2^{k+1}-1},
\]

so `t_2=2/7`, `t_3=2/5`, and `t_k<1/2` for all `k>=4`.

If the positive-input mass is `q`, then `K~Poisson(dq)` and hence

\[
m\le \frac27\Pr(K=2)+\frac25\Pr(K=3)+\frac12\Pr(K\ge4)=:\overline M(dq).
\]

## B20 — use the obstruction against the small branch

The small scalar branch has `q<0.1389<0.14`. Since the displayed count-envelope is monotone in the Poisson mean, it is enough to test `q=0.14`. At the current exact `d`, preliminary exact-rational algebra with a rigorous Taylor upper bound on `e^{dq}` indicates

\[
\overline M(0.14d)<1/d^2.
\]

If the exact checker confirms this strict inequality, it contradicts the B5 lower bound and **eliminates the entire small-q cavity branch**. Combined with the previous exhaustive root count for the scalar atom equation, every infinite-support local minimizer would then be forced onto the large branch `q in (0.9319,0.9320)`, equivalently

\[
p_0=\Pr(\alpha=1)\in(0.0680,0.0681).
\]

This would not prove global minimization or the F0095 source conjecture, but it would remove one of the two structural infinite-support alternatives without finite sampling.