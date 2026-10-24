# Conditional selected-kernel law and the multiplier family

Status: PROVED within the two-input mixed-cone theorem in `agents/f03_cone.md`; no external priority claim. Here rho=-c, 0<c<1, R1<0<R2, gamma>0 is fixed before width tends to infinity. Write nu for the law of V=XU, which has an everywhere positive density. The primitive marked Poisson measure N is independent of (F,C), hence of R=y-F and C.

For a>0 define

\[
p_2(a)=\nu\{v_2>0\}+\nu\{v_1>0,v_2\le0,
 v_2+ca\lceil v_1/a\rceil>0\},
\]

and define p1(a) by exchanging coordinates. Boundaries have zero nu measure. These are probabilities, not densities. Conditional on (R,C), the selected masses P1 and P2 are independent infinitely divisible positive variables: P1 uses only negative z atoms and P2 only positive z atoms. Their Levy measures, expressed in squared mass w=z^2, are

\[
\Pi_{2,R}(dw)=\frac{\alpha c_\alpha}{2}
w^{-1-\alpha/2}p_2(\gamma\sqrt w\,|R_1|)\,dw,
\quad
\Pi_{1,R}(dw)=\frac{\alpha c_\alpha}{2}
w^{-1-\alpha/2}p_1(\gamma\sqrt w\,R_2)\,dw.
\]

In particular

\[
E[e^{-\lambda P_2}\mid R,C]
=\exp\left[-\alpha c_\alpha\int_0^\infty
(1-e^{-\lambda z^2})z^{-1-\alpha}
p_2(\gamma z|R_1|)\,dz\right],\qquad\lambda\ge0.
\]

The analogous formula holds for P1. Proof: condition on R,C, restrict N to its independent positive/negative half-lines, deterministically thin by the selector, and apply the Poisson exponential formula. The change of variables w=z^2 gives the factor 1/2. Integrability follows from 1-e^{-lambda z^2}<=min(1,lambda z^2), 0<alpha<2. Conditional independence does not assert unconditional independence, because both masses depend on R.

## Fine and very coarse multiplier limits

Define p2(0)=nu{v2>0}+nu{v1>0,v2<=0,v2+cv1>0}, with the mirrored p1(0). This is the generic continuous frozen entrance selector. Since

\[
v_1\le a\lceil v_1/a\rceil<v_1+a\quad(v_1>0),
\]

every continuously escaping atom also escapes at every finite gamma. For each fixed z and generic mark the selector converges to the continuous one as gamma decreases to zero. Thus, on the same N and R,

\[
P_j^\gamma\longrightarrow P_j^0\quad\hbox{almost surely as }\gamma\downarrow0.
\]

This follows by dominated convergence against the random finite measure z^2 N; no uniform entrance-time bound is needed. It is an iterated limit of the already selected laws, not a theorem for a simultaneous m-dependent gamma_m. The corresponding output paths converge uniformly on every finite horizon by continuity of the matrix exponential.

For every fixed a>0, p2(a)>p2(0): on any open cell ((n-1)a,na), the nonempty strip -cna<v2<-cv1 has positive nu mass. This also holds for p1. Hence for every gamma>0 and lambda>0 each conditional Laplace transform above is strictly smaller than its gamma=0 counterpart. This does not require finite moments of Pj.

As gamma tends to infinity, for each fixed nonzero z and finite mark, a exceeds any opposing positive coordinate eventually. The selected atom escapes iff at least one projected coordinate is positive. Dominated convergence again gives a finite a.s. limit Pj^infinity. Its thinning probability is p_infinity=nu{v1>0 or v2>0}, independent of z; both gamma=0 and infinity endpoint masses are alpha/2-stable with Laplace exponent

\[
c_\alpha\Gamma(1-\alpha/2)p_j(0)\lambda^{\alpha/2},
\quad\hbox{or}\quad
c_\alpha\Gamma(1-\alpha/2)p_\infty\lambda^{\alpha/2},
\]

respectively. Indeed alpha/(2*(alpha/2))=1 when evaluating the Levy integral. The initial factor-of-two calculation error is recorded in DIRECTIONS.md; the formula here is corrected.

For finite positive gamma, p_j(gamma sqrt(w) times residual) tends to p_j(0) as w decreases to zero and to p_infinity as w increases to infinity. These limits differ strictly by the positive-density region {opposing coordinate>0, supporting coordinate+c opposing coordinate<0}. Thus the Levy density is not homogeneous and Pj is not an exact positive stable variable. It remains infinitely divisible.

## Nested grids, not arbitrary monotonicity

If gamma_c=n gamma_f with positive integer n, then
gamma_c ceil(t/gamma_c)>=gamma_f ceil(t/gamma_f) for t>0: the coarse grid is a subset of the fine grid. The entrance criterion therefore gives Pj^gamma_c>=Pj^gamma_f atomwise. Strictness for 1 versus .1 holds on the open mark box in `agents/f01_entrance.md`. For arbitrary nonnested multipliers no such ordering holds: the central mark escapes at .13 and dies at .2. The distinct marginal output-path law proof is in `reviews/MARGINAL_LAW_REVIEW.md`.
