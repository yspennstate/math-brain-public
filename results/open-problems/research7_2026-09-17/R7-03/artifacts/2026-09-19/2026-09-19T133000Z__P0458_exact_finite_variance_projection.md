Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed. Methods: **B3 / B15 / B27**.

# P0458 — exact finite-`n` variance formula and a uniform cutoff-projection theorem

Canonical target: `P0458`  
Worker: `R7-03`  
Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, J. Appl. Probab. 63(2), 552–579 (2026), §1.1 first additional question.  
Frozen metric: `R_unresolved=0`; this artifact strengthens the solved source endpoint but does **not** manufacture a new metric.

The previous R7-03 runs proved the full limiting-law classification. This note goes in a different direction: it computes the finite-`n` variance exactly as a one-dimensional beta projection plus one explicit shared-edge correction, and then shows that the entire graph-dependent conditional-noise contribution differs from the already-known exact mean deficit by only a universal `O(1)` term. The result directly addresses the source's comment that even `Var(D)` is difficult because of dependence.

## 1. Setup

Write

\[
r:=n-1-k,\qquad 2\le k\le n-2,\qquad r\ge1.
\]

Use the smaller-score-is-preferred realization of `LK(n,k)`. Fix a root vertex and let `D=D_{n,k}` be its degree. Let

\[
H:=k-D
\]

be the number of root-proposed edges rejected by their opposite endpoints.

Let `S` be the root's `k` preferred neighbors and let `X` be the root's `(k+1)`st order statistic among its `n-1` incident iid `Uniform(0,1)` scores. Then

\[
X\sim\operatorname{Beta}(k+1,r).
\]

Conditional on `(X,S)`, the `k` root-edge scores into `S` are iid `Uniform(0,X)`. For a selected neighbor, if `T` is the `k`th order statistic among its other `n-2` incident scores, then

\[
T\sim\operatorname{Beta}(k,r)
\]

and is marginally independent of `X`.

Let

\[
F(x):=\Pr(T\le x)=I_x(k,r),
\qquad
Q(x):=\frac1x\int_0^x F(u)\,du.
\tag{1.1}
\]

Thus `Q(x)` is exactly the conditional rejection probability of one root-proposed edge and

\[
M(x):=\mathbb E(H\mid X=x)=kQ(x).
\tag{1.2}
\]

Let `f_X` denote the `Beta(k+1,r)` density.

The exact mean deficit from the earlier beta-Gini theorem is

\[
\delta_{n,k}:=\mathbb EH=k-\mathbb ED
=\frac{2B(n-1,n-1)}{B(k,k)B(r,r)}.
\tag{1.3}
\]

## 2. The shared-edge projection, exactly

Take two distinct selected neighbors `i,j in S`. Their rejection indicators `R_i,R_j` share exactly one non-root random edge, with score `W=U_{ij}`. Conditional on `(X,W)`, they are independent because all remaining edge variables entering the two endpoint decisions are disjoint.

The earlier ANOVA calculation gives

\[
\operatorname{Cov}(R_i,R_j\mid X=x)
=b(x),
\]

where, after removing an additive constant that does not affect variance,

\[
b(x)
=\frac{\operatorname{Var}_{W\sim U(0,1)}([F(x)-F(W)]_+)}{x^2(n-2)^2}.
\tag{2.1}
\]

Because `F` is increasing, define

\[
J_1(x):=\int_0^x\{F(x)-F(w)\}\,dw,
\]

\[
J_2(x):=\int_0^x\{F(x)-F(w)\}^2\,dw.
\]

Then the variance over a uniform `W in [0,1]` is exactly

\[
\boxed{
 b(x)=\frac{J_2(x)-J_1(x)^2}{x^2(n-2)^2}.
}
\tag{2.2}
\]

No independence approximation appears here.

## 3. B3 — exact finite-`n` variance formula

Conditional exchangeability gives

\[
\operatorname{Var}(H\mid X=x)
=kQ(x)(1-Q(x))+k(k-1)b(x).
\tag{3.1}
\]

Apply the law of total variance. Since `M=kQ(X)`,

\[
\operatorname{Var}(D)=\operatorname{Var}(H)
=\operatorname{Var}(M)+\mathbb E\operatorname{Var}(H\mid X).
\]

Using `E[M]=delta_{n,k}` and collecting terms gives the following exact identity.

### Theorem 3.1 (exact finite-`n` variance)

For every `n>=4` and `2<=k<=n-2`, with `r=n-1-k`,

\[
\boxed{
\operatorname{Var}(D_{n,k})
=\delta_{n,k}-\delta_{n,k}^2
+k(k-1)\int_0^1\bigl(Q(x)^2+b(x)\bigr)f_X(x)\,dx.
}
\tag{3.2}
\]

Equivalently, if

\[
V_{\rm cut}:=\operatorname{Var}(M(X)),
\qquad
C_{n,k}:=k(k-1)\mathbb E b(X),
\]

then

\[
\boxed{
\operatorname{Var}(D)
=V_{\rm cut}+\delta_{n,k}-\frac{\mathbb E[M(X)^2]}{k}+C_{n,k}.
}
\tag{3.3}
\]

#### Proof

From (3.1),

\[
\mathbb E\operatorname{Var}(H\mid X)
=k\mathbb E[Q(X)(1-Q(X))]+C_{n,k}.
\]

Because `M=kQ(X)`,

\[
k\mathbb E Q(X)=\delta_{n,k},
\qquad
k\mathbb E Q(X)^2=\frac{\mathbb E M(X)^2}{k}.
\]

Therefore

\[
\mathbb E\operatorname{Var}(H\mid X)
=\delta_{n,k}-\frac{\mathbb E M^2}{k}+C_{n,k}.
\]

Adding `Var(M)=E M^2-delta^2` yields (3.2) and (3.3). ∎

### Exact rational computability

For integer `k,r`, the beta cdf is the polynomial

\[
F(x)=\sum_{j=k}^{n-2}\binom{n-2}{j}x^j(1-x)^{n-2-j}.
\tag{3.4}
\]

Hence `Q`, `J_1`, `J_2`, and `b` are polynomials (the numerator in (2.2) is divisible by `x^2`). The outer beta-weighted integrals in (3.2) therefore reduce to finite sums of beta integrals with integer arguments. In particular, `Var(D_{n,k})` is exactly rational and is algorithmically computable for every finite `(n,k)` without simulation.

This is stronger than an asymptotic variance statement: the dependence obstacle is reduced to a finite exact expression.

## 4. B27 — a simultaneous nonasymptotic projection inequality

The exact shared-edge formula implies the already-proved finite bound

\[
0\le C_{n,k}\le \frac{n-1}{4(n-2)}.
\tag{4.1}
\]

We now control the only negative correction in (3.3) uniformly.

Let

\[
N:=n-1=k+r,
\qquad
\mu:=\mathbb ET=\frac{k}{N}.
\]

By Jensen and `(x-T)_+^2 <= (x-T)^2`,

\[
M(X)^2
=\frac{k^2}{X^2}\left(\mathbb E[(X-T)_+\mid X]\right)^2
\le
\frac{k^2}{X^2}\mathbb E[(X-T)^2\mid X].
\tag{4.2}
\]

For `T~Beta(k,r)`,

\[
\operatorname{Var}(T)=\frac{kr}{N^2(N+1)}.
\]

For `X~Beta(k+1,r)`,

\[
\mathbb E X^{-1}=\frac Nk,
\qquad
\mathbb E X^{-2}=\frac{N(N-1)}{k(k-1)}.
\tag{4.3}
\]

Therefore

\[
\mathbb E\frac{(X-\mu)^2}{X^2}
=1-2\mu\mathbb EX^{-1}+\mu^2\mathbb EX^{-2}
=\frac{r}{N(k-1)}.
\tag{4.4}
\]

Combining (4.2)--(4.4),

\[
\begin{aligned}
\mathbb E M^2
&\le
k^2\operatorname{Var}(T)\mathbb EX^{-2}
+k^2\mathbb E\frac{(X-\mu)^2}{X^2}\\
&=
\frac{k^2r(N-1)}{N(N+1)(k-1)}
+\frac{k^2r}{N(k-1)}\\
&=\boxed{\frac{2k^2r}{n(k-1)}}.
\end{aligned}
\tag{4.5}
\]

Insert this and (4.1) into (3.3).

### Theorem 4.1 (uniform cutoff-projection expansion)

For all `n>=4`, `2<=k<=n-2`,

\[
\boxed{
\operatorname{Var}(D)
=V_{\rm cut}+\delta_{n,k}+\varepsilon_{n,k},
}
\tag{4.6}
\]

with the explicit two-sided bound

\[
\boxed{
-\frac{2kr}{n(k-1)}
\le \varepsilon_{n,k}
\le \frac{n-1}{4(n-2)}.
}
\tag{4.7}
\]

In particular, uniformly over every admissible `(n,k)`,

\[
-4<\varepsilon_{n,k}<\frac12.
\tag{4.8}
\]

Thus the full graph-dependent conditional-noise variance is the exact mean deficit plus only a bounded additive correction.

A second useful form follows because

\[
\operatorname{Var}(D)-V_{\rm cut}
=\mathbb E\operatorname{Var}(H\mid X)\ge0.
\]

If `B,B'` are iid `Beta(k,r)`, the beta-Gini identity gives

\[
\delta_{n,k}=\frac N2\mathbb E|B-B'|.
\]

By Cauchy--Schwarz,

\[
\delta_{n,k}
\le \frac N2\sqrt{2\operatorname{Var}(B)}
=\sqrt{\frac{kr}{2n}}.
\tag{4.9}
\]

Let

\[
s_n^2:=\frac{k(n-k)}n=\frac{k(r+1)}n.
\]

Since `kr/n <= s_n^2`, (4.1) and (4.9) yield the simultaneous bound

\[
\boxed{
0\le \operatorname{Var}(D)-V_{\rm cut}
\le \frac{s_n}{\sqrt2}+\frac{n-1}{4(n-2)}.
}
\tag{4.10}
\]

Equivalently,

\[
\boxed{
\left\|\frac{H-M(X)}{s_n}\right\|_2^2
\le
\frac{1}{\sqrt2\,s_n}
+\frac{n-1}{4(n-2)s_n^2}.
}
\tag{4.11}
\]

This is a quantitative finite-`n` version of the conditional-noise negligibility used in the limiting-law proof.

## 5. B15 — break symmetry: the bound does not deteriorate at extreme aspect ratio

The old proof had to split off a bad lower-tail event for `X`, which made very sparse and very dense interior sequences look potentially different. The exact projection bound shows that this was a proof artifact.

Let

\[
m:=\min(k,r).
\]

The symmetric harmonic scale

\[
t^2:=\frac{kr}{k+r}
\]

satisfies `t^2>=m/2`. Also

\[
s_n^2=\frac{k(r+1)}{k+r+1}\ge \frac{kr}{k+r}=t^2.
\]

Hence `s_n^2>=m/2`, and (4.11) gives

\[
\boxed{
\left\|\frac{H-M(X)}{s_n}\right\|_2^2
\le \frac1{\sqrt m}+\frac1m.
}
\tag{5.1}
\]

Therefore there is **no hidden `k/r` or `r/k` blow-up** in the graph-dependent remainder. The only interior bottleneck is the smaller budget `m=min(k,r)` itself.

This covers, with the same finite inequality,

- sparse growth `k/r -> 0`,
- proportional growth `k/r -> lambda in (0,infinity)`, and
- near-complete growth `r/k -> 0`,

as long as `m->infinity`.

## 6. A new second-order asymptotic

Equation (4.6) is also strong enough to identify the first subleading contribution that comes from the conditional Bernoulli/dependence noise.

The exact beta-Gini mean theorem gives, uniformly along every interior sequence `k->infinity`, `r->infinity`,

\[
\delta_{n,k}
\sim \sqrt{\frac{kr}{\pi(k+r)}}.
\tag{6.1}
\]

Moreover

\[
\frac{s_n^2}{kr/(k+r)}
=\frac{(k+r)(r+1)}{r(k+r+1)}
=1+\frac{k}{r(k+r+1)}
\longrightarrow1
\]

whenever `r->infinity`. Thus `delta_{n,k}~s_n/sqrt(pi)`. Since `epsilon_{n,k}=O(1)` by (4.7),

\[
\boxed{
\mathbb E\operatorname{Var}(H\mid X)
=\frac{s_n}{\sqrt\pi}+o(s_n)
}
\tag{6.2}
\]

for **every** interior sequence, without an aspect-ratio restriction.

Equivalently,

\[
\boxed{
\operatorname{Var}(D)
=V_{\rm cut}+\frac{s_n}{\sqrt\pi}+o(s_n).
}
\tag{6.3}
\]

The leading `v s_n^2` variance from the earlier theorem therefore comes entirely from root-cutoff randomness. The internal edge-array contributes only the universal next scale `s_n/sqrt(pi)`, up to smaller error relative to `s_n`.

This does **not** yet identify the order-`s_n` correction inside `V_cut` itself. Consequently the strongest honest finite approximation to the already-known constant `v` from this route is

\[
\boxed{
|\operatorname{Var}(D)-v s_n^2|
\le
|V_{\rm cut}-v s_n^2|
+\frac{s_n}{\sqrt2}+\frac{n-1}{4(n-2)}.
}
\tag{6.4}
\]

The remaining quantitative-CLT problem is now purely one-dimensional: bound `V_cut` for a beta order statistic. No graph-dependence estimate remains in that task.

## 7. Relation to the source question

The source explicitly says that even `Var(D)` is hard to calculate because of dependence. The source-level limiting-law question was already proved internally by prior R7-03 runs. The new contribution here is stronger finite structure:

1. an exact finite-`n` variance formula, (3.2);
2. exact rational computability for integer `(n,k)`;
3. a simultaneous finite projection inequality, (4.10)--(4.11);
4. the uniform second-order conditional-noise asymptotic, (6.2).

These are theorem-level strengthening results, not a replacement metric and not an independent audit.

## 8. Validation target

Because (3.2) is a finite exact claim, the companion self-check evaluates the polynomial/beta integrals using Python `Fraction` arithmetic. It checks:

- the exact formula against the previously independently derived `r=1` variance formula for every `4<=n<=30`;
- the exact formula against exhaustive enumeration of all `6!=720` edge-orderings of `K_4` at `k=2`.

The checker is self-validation only; it is neither P26 nor an OTHER-track audit.
