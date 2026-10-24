Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — critical-edge speed asymptotic beyond the minimum-degree singularity

**Status:** PROVED PARTIAL (new repository theorem candidate; not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains unresolved).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Old D0047 history is preserved. Canonical ownership was checked at assignment and is not reopened here.

**Captured master immediately before successful write attempt:** `37092199c3060797c8ad6aa13efc9480f4d142d7`.

## 1. Source normalization and why this is a genuine pivot

Let `nu` be the offspring variable of a supercritical Galton–Watson tree without leaves,

\[
P(\nu=0)=0,\qquad m=E\nu>1.
\]

This report uses the standard parent-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+\nu(x)},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)}.
\]

Thus increasing `lambda` pushes toward the root, and the Lyons–Pemantle–Peres conjecture asks that the speed `ell_lambda` be nonincreasing throughout the transient interval `0<lambda<m`.

Current source continuity was refreshed before this proof:

* Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, old high-outward-bias theorem;
* Aïdékon, *Speed of the biased random walk on a Galton--Watson tree*, arXiv:1111.4313, exact speed representation;
* Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, differentiability/analyticity in ballistic regimes, without a general sign theorem;
* Song–Wang–Xiang, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`, proving strict decrease for minimum offspring `d>=2` on

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\]

A bounded 20 September 2026 literature refresh found no checked source-wide resolution and no checked paper stating the critical-edge asymptotic proved below. This is bounded negative evidence, not a novelty certificate.

The latest own reports (`harmonic-tail-stieltjes-extension` and `core-tail-gini-extension`) made real progress for `lambda<d`, but their pointwise logarithmic-sensitivity control contains `(d-lambda)^{-1}` and therefore cannot cross `lambda=d`. P03-B's latest coupling report instead isolates an outward-selection variance debt and a selected-ancestor return-stack obstruction; that result is consumed here only as evidence that another local coupling certificate would be duplicative.

This run therefore changes category: it attacks the **opposite end of the transient interval**, `lambda\uparrow m`, directly through the escape-probability smoothing transform. In particular the argument does not use a positive minimum degree and therefore reaches no-leaf laws with `P(nu=1)>0`, which are outside the `d>=2` source-uniform theorem.

The fixed full-source metric remains

`R_full: 1 -> 1`.

## 2. Escape recursion and notation

Let `B_lambda` denote the quenched probability, from a child-root, of never hitting its parent. With iid copies `B_1,B_2,...` and

\[
S_k:=\sum_{i=1}^k B_i,
\]

the standard recursion is

\[
\boxed{B_\lambda\ \stackrel d=\ \frac{S_\nu}{\lambda+S_\nu}.}
\tag{2.1}
\]

Write

\[
e:=E B_\lambda,\qquad s:=E B_\lambda^2,\qquad t:=E B_\lambda^3,
\]

and the offspring factorial moments

\[
f_2:=E[\nu(\nu-1)],\qquad
f_3:=E[\nu(\nu-1)(\nu-2)].
\]

For the new theorem assume

\[
E\nu^3<\infty.
\tag{2.2}
\]

At the critical bias `lambda=m` the walk is recurrent, hence the escape probability is zero. Since `B_lambda` decreases in `lambda`, monotone convergence gives

\[
B_\lambda\downarrow0\quad\text{a.s.},\qquad e\downarrow0,
\qquad \lambda\uparrow m.
\tag{2.3}
\]

No minimum-offspring lower bound beyond `P(nu=0)=0` is used below.

## 3. Moment closure near the critical bias

Choose once and for all `lambda_0<m` sufficiently close to `m` that

\[
\lambda_0^2>m,\qquad \lambda_0^3>m.
\tag{3.1}
\]

This is possible because `m>1`. Work on `lambda in [lambda_0,m)`.

### Lemma 3.1 — `s=O(e^2)` and `t=O(e^3)`

From `B=S_nu/(lambda+S_nu)<=S_nu/lambda`,

\[
s\le \frac{E S_\nu^2}{\lambda^2}
=\frac{m s+f_2e^2}{\lambda^2}.
\]

Therefore

\[
\boxed{s\le \frac{f_2}{\lambda^2-m}e^2=O(e^2).}
\tag{3.2}
\]

Similarly,

\[
t\le \frac{E S_\nu^3}{\lambda^3}
=\frac{m t+3f_2se+f_3e^3}{\lambda^3},
\]

so (3.1) and (3.2) imply

\[
\boxed{t\le
\frac{3f_2se+f_3e^3}{\lambda^3-m}=O(e^3).}
\tag{3.3}
\]

This elementary closure is the main reason a third offspring moment is enough for the first-order critical asymptotic.

### Lemma 3.2 — the normalized second escape moment has an exact limit

For every `x>=0`,

\[
0\le \frac{x^2}{\lambda^2}-\frac{x^2}{(\lambda+x)^2}
=\frac{x^3(2\lambda+x)}{\lambda^2(\lambda+x)^2}
\le \frac{2x^3}{\lambda^3}.
\tag{3.4}
\]

Applying this with `x=S_nu`, and using

\[
E S_\nu^2=ms+f_2e^2,
\qquad
E S_\nu^3=mt+3f_2se+f_3e^3=O(e^3),
\]
we get

\[
s=\frac{ms+f_2e^2}{\lambda^2}+O(e^3).
\tag{3.5}
\]

Hence

\[
\frac{s}{e^2}
=\frac{f_2}{\lambda^2-m}+O(e),
\]
so

\[
\boxed{
\frac{s}{e^2}\longrightarrow
\kappa:=\frac{f_2}{m^2-m}
=\frac{f_2}{m(m-1)}.
}
\tag{3.6}
\]

For a deterministic `m=d` tree this gives `kappa=1`, as it should.

## 4. Exact first-order scale of the mean escape probability

Use the exact algebraic identity

\[
\frac{x}{\lambda+x}
=\frac{x}{\lambda}
-\frac{x^2}{\lambda^2}
+\frac{x^3}{\lambda^2(\lambda+x)}.
\tag{4.1}
\]

The remainder is between `0` and `x^3/lambda^3`. Taking expectations in (2.1) and using Lemma 3.1 gives

\[
e
=\frac{me}{\lambda}
-\frac{ms+f_2e^2}{\lambda^2}
+O(e^3).
\tag{4.2}
\]

Put `delta=m-lambda`. Rearranging and dividing by `e>0`,

\[
\frac{\delta}{\lambda}
=\frac{m(s/e^2)+f_2}{\lambda^2}\,e+O(e^2).
\tag{4.3}
\]

By (3.6),

\[
m\kappa+f_2
=\frac{f_2}{m-1}+f_2
=\frac{mf_2}{m-1}.
\]

Therefore

\[
\boxed{
\frac{e}{m-\lambda}
\longrightarrow
\frac{m-1}{f_2}.
}
\tag{4.4}
\]

Equivalently,

\[
\boxed{
E B_\lambda
=\frac{m-1}{f_2}(m-\lambda)
+o(m-\lambda).
}
\tag{4.5}
\]

This is already a useful bridge through the old `lambda=d` singularity: the escape scale is controlled by the **mean criticality defect** `m-lambda`, not by `d-lambda`.

## 5. Critical expansion of Aïdékon's escape tilt

The inherited exact speed representation uses, conditional on current offspring `n`,

\[
c_n(\lambda)
:=\frac1{n+1}
E\left[
\frac{S_{n+1}}{\lambda-1+S_{n+1}}
\right],
\tag{5.1}
\]

and the escape-tilted offspring mean

\[
C:=\sum_n p_nc_n,
\qquad
H:=\sum_n n p_nc_n,
\qquad
M:=\frac{H}{C}.
\tag{5.2}
\]

Aïdékon's formula, in the present normalization, is

\[
\boxed{\ell_\lambda=\frac{M-\lambda}{M+\lambda}.}
\tag{5.3}
\]

Set `a=lambda-1`. Since `lambda\uparrow m>1`, `a` stays bounded away from zero. For every `x>=0`,

\[
\frac{x}{a+x}
=\frac{x}{a}-\frac{x^2}{a^2}
+\frac{x^3}{a^2(a+x)}.
\tag{5.4}
\]

If `N=n+1`, then

\[
\frac1N E S_N=e,
\]

\[
\frac1N E S_N^2=s+n e^2,
\]

and

\[
\frac1N E S_N^3
=t+3nse+n(n-1)e^3.
\]

Consequently

\[
\boxed{
c_n
=\frac e a-rac{s+n e^2}{a^2}+r_n,}
\tag{5.5}
\]

with

\[
0\le r_n\le
\frac{t+3nse+n(n-1)e^3}{a^3}.
\tag{5.6}
\]

Averaging (5.5) over `nu`, Lemma 3.1 gives

\[
C
=\frac e a-rac{s+m e^2}{a^2}+O(e^3).
\tag{5.7}
\]

Multiplying first by `n` and then averaging, the finite third offspring moment gives

\[
H
=\frac{m e}{a}
-\frac{m s+E[\nu^2]e^2}{a^2}
+O(e^3).
\tag{5.8}
\]

The `O(e^3)` remainder in (5.8) is legitimate because (5.6), after multiplication by `n`, contains only moments through order three of `nu`.

Divide (5.8) by (5.7). Since `s=\kappa e^2+o(e^2)`, the common `kappa` contribution cancels and yields

\[
\boxed{
M
=m-\frac{\operatorname{Var}(\nu)}{m-1}\,e+o(e).
}
\tag{5.9}
\]

Using (4.4),

\[
\boxed{
M-m
=-\frac{\operatorname{Var}(\nu)}{f_2}(m-\lambda)
+o(m-\lambda).
}
\tag{5.10}
\]

The cancellation is important: near criticality the escape tilt lowers the effective offspring mean by exactly `Var(nu)/f_2` times the criticality defect, to first order.

## 6. Main theorem: exact critical-edge slope of the speed itself

Because

\[
f_2=E[\nu(\nu-1)]
=\operatorname{Var}(\nu)+m^2-m,
\]
we have

\[
1-\frac{\operatorname{Var}(\nu)}{f_2}
=\frac{m(m-1)}{f_2}.
\tag{6.1}
\]

Combining (5.3), (5.10), and `lambda=m-delta`,

\[
M-\lambda
=\frac{m(m-1)}{f_2}\,\delta+o(\delta),
\]
while `M+lambda ->2m`. Therefore:

### Theorem 6.1 — critical-edge speed asymptotic

Assume `P(nu=0)=0`, `E nu=m>1`, and `E nu^3<infinity`. In the parent-bias convention above,

\[
\boxed{
\ell_\lambda
=\frac{m-1}{2f_2}(m-\lambda)
+o(m-\lambda),
\qquad \lambda\uparrow m,
}
\tag{6.2}
\]

where `f_2=E[nu(nu-1)]`.

Equivalently,

\[
\boxed{
\lim_{\lambda\uparrow m}
\frac{\ell_\lambda}{m-\lambda}
=\frac{m-1}{2E[\nu(\nu-1)]}>0.
}
\tag{6.3}
\]

This theorem reaches laws with minimum offspring one and biases strictly above the minimum degree; it is not subject to the `(d-lambda)^{-1}` singularity of the previous P03-A sensitivity route.

### Sanity check: regular tree

For `nu=d` deterministically,

\[
f_2=d(d-1),
\]
so (6.2) gives coefficient `1/(2d)`. The exact regular-tree speed is

\[
\ell_\lambda=\frac{d-\lambda}{d+\lambda},
\]
whose critical expansion is indeed `(d-lambda)/(2d)+O((d-lambda)^2)`.

## 7. Genuine monotonicity information that follows without an unproved derivative interchange

Theorem 6.1 by itself is a **speed asymptotic**, not yet a proof that `ell'_lambda<0` on a whole terminal interval. It is important not to smuggle that stronger claim through an unjustified differentiation of an `o(delta)` remainder.

Nevertheless it gives two exact consequences.

### Corollary 7.1 — fixed-ratio terminal comparisons

Fix any `r in (0,1)`. Then there exists `delta_r>0` such that for every `0<delta<delta_r`,

\[
\boxed{
\ell_{m-\delta}>\ell_{m-r\delta}.
}
\tag{7.1}
\]

Indeed, if `c=(m-1)/(2f_2)>0`, then

\[
\ell_{m-\delta}-\ell_{m-r\delta}
=c(1-r)\delta+o(\delta)>0.
\]

Thus monotonicity holds asymptotically across every fixed multiplicative contraction of the distance to criticality. This is weaker than interval monotonicity, but it is a genuine cross-`lambda=d` speed comparison.

### Corollary 7.2 — derivative values with the correct negative critical coefficient occur arbitrarily close to `m`

For finite-support no-leaf laws, Peres–Zeitouni give ballisticity/CLT throughout `lambda<m`, and Bowditch–Tokushige give differentiability (indeed analyticity in the ballistic regime). Extend `ell_m:=0`. For each `delta>0`, the mean-value theorem gives some

\[
\xi_\delta\in(m-\delta,m)
\]
with

\[
\ell'_{\xi_\delta}
=\frac{\ell_m-\ell_{m-\delta}}{\delta}.
\]

Hence Theorem 6.1 implies

\[
\boxed{
\ell'_{\xi_\delta}\longrightarrow
-\frac{m-1}{2f_2}<0.
}
\tag{7.2}
\]

So negative derivative is not merely a low-bias phenomenon: the correct negative derivative scale occurs arbitrarily close to the critical bias. What remains is to turn this sequence statement into a uniform terminal interval.

## 8. Explicit two-point example beyond the old singular line

Take

\[
P(\nu=2)=P(\nu=3)=\frac12.
\]

Then

\[
m=\frac52,
\qquad
f_2=\frac12\cdot2+\frac12\cdot6=4.
\]

Therefore

\[
\boxed{
\ell_\lambda
=\frac3{16}\left(\frac52-\lambda\right)
+o\!\left(\frac52-\lambda\right),
\qquad \lambda\uparrow\frac52.
}
\tag{8.1}
\]

In particular, for every fixed `r in (0,1)` and sufficiently small `delta`,

\[
\ell_{5/2-\delta}>\ell_{5/2-r\delta},
\]
which lies entirely in the region `lambda>2` once `delta<1/2`. The preceding P03-A pointwise-sensitivity machinery stopped before `lambda=2`; this critical-edge expansion therefore reaches a genuinely new part of the source interval by a different mechanism.

For finite-support laws, there are derivative points `xi_delta\uparrow5/2` with

\[
\ell'_{\xi_\delta}\to-\frac3{16}.
\tag{8.2}
\]

## 9. What this changes, and what it does not

### New proved mathematics

1. The second escape moment satisfies

\[
E B_\lambda^2
\sim \frac{f_2}{m(m-1)}(E B_\lambda)^2.
\]

2. The mean escape probability has the explicit critical scale

\[
E B_\lambda
\sim \frac{m-1}{f_2}(m-\lambda).
\]

3. The Aïdékon effective degree has the first-order critical expansion

\[
M-m
\sim -\frac{\operatorname{Var}(\nu)}{f_2}(m-\lambda).
\]

4. The speed has the explicit critical-edge asymptotic (6.2).

5. This yields fixed-ratio terminal speed comparisons and, for finite-support laws, derivative points arbitrarily close to `m` converging to the strictly negative coefficient `-(m-1)/(2f_2)`.

### Not proved

* I do **not** claim that `ell'_lambda` is negative at every sufficiently near-critical `lambda` from (6.2) alone. Differentiating an `o(m-lambda)` remainder without a `C^1` remainder estimate would be invalid.
* I do **not** claim the full Lyons–Pemantle–Peres conjecture.
* I do **not** claim external novelty; later independent literature and proof review are still required before publication use.

The full-source metric remains `R_full: 1 -> 1`.

## 10. Exact remaining analytic gap and next attack

The critical singularity has been moved from a false pointwise `d-lambda` denominator to a precise regularity question.

The missing lemma is a `C^1` upgrade of the expansions above. A sufficient target is

\[
\boxed{
\partial_\lambda
\left[
\ell_\lambda
-\frac{m-1}{2f_2}(m-\lambda)
\right]
=o(1)
\quad(\lambda\uparrow m).
}
\tag{10.1}
\]

That would immediately prove a full terminal monotonicity interval

\[
\ell'_\lambda<0
\quad\text{for all }\lambda\in(m-\varepsilon,m)
\]
for some `epsilon>0`, including minimum-offspring-one laws under the moment assumptions.

The next attack should differentiate the **normalized moment system**, not the pointwise escape floor. Let

\[
u=-e'(\lambda),\qquad h=-\tfrac12 s'(\lambda)=E[B_\lambda(-B_\lambda')].
\]

Differentiate the exact recursions only after factoring out the unstable scalar `e`: the quantity `s/e^2` already has a finite limit `kappa`. The desired estimate is

\[
\frac{d}{d\lambda}\left(\frac{s}{e^2}\right)=O(1)
\tag{10.2}
\]
near criticality. Together with the third-moment closure, (10.2) should turn (4.3) into

\[
e'(\lambda)=-\frac{m-1}{f_2}+O(m-\lambda),
\]
and then (5.7)--(5.8) should give

\[
M'(\lambda)=\frac{\operatorname{Var}(\nu)}{f_2}+O(m-\lambda),
\]
so that

\[
\lambda M'-M
\to -\frac{m^2(m-1)}{f_2}<0.
\]

This is the cleanest current route to an actual terminal interval and it is analytically distinct from P03-B's selected-ancestor return-stack coupling.

## 11. Source links used this run

* Ben Arous–Fribergh–Sidoravicius: https://arxiv.org/abs/1111.5865
* Aïdékon speed representation: https://arxiv.org/abs/1111.4313
* Bowditch–Tokushige differentiability: https://arxiv.org/abs/1906.07913
* Bowditch–Tokushige analyticity: https://arxiv.org/abs/2006.03433
* Peres–Zeitouni critical/ballistic CLT: https://arxiv.org/abs/math/0606625
* Song–Wang–Xiang 2025 low-bias monotonicity: https://doi.org/10.1017/jpr.2024.113

## 12. Delivery discipline

One immutable mathematics-first report only. No peer files, historical D0047 files, claim files, email, Drive, publication state, or scheduler identities were modified. No force push was used. The commit returned by GitHub must be read back before delivery is claimed.
