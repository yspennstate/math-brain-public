Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-05 route note — break the edge symmetry and dualize the survival operator

New mathematical route written before any checker for this run.

The incoming certified point uses the symmetric edge comparator

\[
Y_j=(U_j+U_{j-1})/\sqrt{2(1+r)},\qquad r=q=7/8,
\]

whose covariance is `((1+r)/2) r^{k-1}` and whose persistence operator is self-adjoint. The symmetry `1,1` is convenient but need not be optimal for the ratio "survival cost per Lamperti mesh length".

This run deliberately breaks that symmetry. For `a>0`, let

\[
Y_j^{(a)}=\frac{U_j+aU_{j-1}}{\sqrt{1+a^2+2ar}},
\]

with `(U_j)` stationary Gaussian AR(1), `Cov(U_0,U_k)=r^{|k|}`. Then for every `k>=1`,

\[
C_k(a,r)=A(a,r)r^{k-1},\qquad
A(a,r)=\frac{(r+a)(1+ar)}{1+a^2+2ar}.
\]

For `a=1` this is the previous comparator. For `a\ne1`, the survival transfer operator

\[
(K_{a,r}f)(x)=\int_{y<-ax}p_r(x,dy)f(y)
\]

is no longer self-adjoint. The key B11 dual move is therefore not to estimate its spectral radius directly but to use

\[
\Pr\{Y_1^{(a)}<0,\ldots,Y_n^{(a)}<0\}
 =\langle 1,K_{a,r}^n1\rangle
 \le \|K_{a,r}\|^n,
\]

and

\[
\|K_{a,r}\|^2=\|K_{a,r}^*K_{a,r}\|,
\]

where `K^*K` is positive self-adjoint. Thus a rigorous operator-norm upper bound is enough for the persistence comparison; self-adjointness of `K` itself is unnecessary.

The counterexample-first question is whether the nonnormality penalty `||K||-rho(K)` destroys every gain from making the edge condition more one-sided. I will test this before promoting any theorem. A successful point must satisfy both:

1. exact all-lag source covariance domination `R(q^k)<=A(a,r)r^{k-1}` with the existing `R(u)<=u` tail certificate used only in its proved domain; and
2. a certified bound `||K_{a,r}|| < q^{4c}` with `c>8071/50000`, because `Delta=-4 log q` gives `theta_{2,1/4}>=-log||K||/Delta`.

Methods for this run: **B6** (deform continuously away from the solved `a=1` comparator), **B11** (dualize through `K^*K`), **B15** (break the symmetric edge weights on purpose). If the operator-norm penalty is fatal, that failure itself identifies why the symmetric comparator is structurally privileged and the run will pivot to a different route rather than manufacture another certificate.
