Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; the requested GPT-6 / maximum routing is not authenticated on the exposed runtime.

# E0071 / Björklund Problem 3 — an explicit symmetric counterexample to the printed normalization

## 1. Source statement

Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3, asks the following. Let `(G,mu)` be a measured group and let `H<G` act ergodically on the Poisson boundary of `(G,mu)`. If `d` is a left `G`-invariant metric on `G/H`, is

\[
\lim_{n\to\infty}\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)=0?
\tag{P3}
\]

The current arXiv-v2 HTML still prints exactly this Cesaro normalization. The surrounding paragraph presents the question as a homogeneous-space analogue of the Karlsson--Ledrappier drift theorem.

## 2. Counterexample

Take

\[
G=\mathbb Z,\qquad
H=\{0\},\qquad
\mu=\tfrac12(\delta_{-1}+\delta_{+1}),
\]

and equip `G/H = Z` with the usual metric

\[
d(aH,bH)=|a-b|.
\]

Then every hypothesis of Problem 3 is satisfied, but the displayed limit is not zero.

### 2.1 Measured-group and metric hypotheses

`G=Z` is countable. The support `{-1,+1}` generates all of `Z` as a semigroup, so `(G,mu)` is a measured group in the source's sense. In fact `mu` is symmetric.

The subgroup `H={0}` has infinite index. The metric is left `G`-invariant because

\[
d((c+a)H,(c+b)H)=|a-b|=d(aH,bH).
\]

It is `mu`-integrable, indeed

\[
\int_G d(gH,H)\,d\mu(g)=1.
\]

Thus the example does not exploit a non-symmetric law, a finite quotient, an exotic metric, or failure of the first-moment assumption.

### 2.2 The Poisson boundary is trivial

Let `f:Z -> C` be bounded and left `mu`-harmonic. Since `mu` is symmetric and `Z` is abelian, the source's left-harmonic equation is

\[
f(n)=\frac{f(n-1)+f(n+1)}2,
\qquad n\in\mathbb Z.
\]

Hence

\[
f(n+1)-f(n)=f(n)-f(n-1)
\]

for every `n`; all first differences are equal to one constant `c`. Therefore

\[
f(n)=f(0)+cn.
\]

Boundedness on all of `Z` forces `c=0`, so every bounded `mu`-harmonic function is constant.

By the Poisson-boundary representation used in the source, this means the Poisson boundary of `(Z,mu)` is trivial (a one-point probability space). The trivial subgroup `H={0}` acts ergodically on a one-point space. Thus the boundary-ergodicity hypothesis of Problem 3 is satisfied.

### 2.3 The printed Cesaro quantity is bounded away from zero

Let

\[
S_k=\varepsilon_1+\cdots+\varepsilon_k,
\qquad
P(\varepsilon_i=1)=P(\varepsilon_i=-1)=\tfrac12.
\]

Then `mu^{*k}` is the law of `S_k`, and therefore

\[
\int_G d(gH,H)\,d\mu^{*k}(g)=\mathbb E|S_k|.
\]

For every odd `k`, the integer `S_k` is odd, hence it can never equal zero. Consequently

\[
|S_k|\ge1\quad\text{a.s. for odd }k,
\]

and so

\[
\mathbb E|S_k|\ge1\quad\text{for odd }k.
\]

It follows for every `n` that

\[
\frac1n\sum_{k=1}^n\mathbb E|S_k|
\ge
\frac{\#\{1\le k\le n:k\text{ odd}\}}{n}
=
\frac{\lceil n/2\rceil}{n}.
\]

Thus

\[
\boxed{
\liminf_{n\to\infty}
\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)
\ge\frac12>0.
}
\]

In particular the limit asserted in `(P3)` cannot equal zero.

This already gives a complete source-valid counterexample. One can strengthen the conclusion using the classical growth `E|S_k| asymp sqrt(k)`, which makes the displayed Cesaro quantity diverge like `sqrt(n)`, but that asymptotic is unnecessary for the refutation and is not used.

## 3. Verdict

**Björklund Problem 3 is false as printed in arXiv:1406.0763v2.** The counterexample is the simple symmetric nearest-neighbor random walk on `Z`, with trivial subgroup and the ordinary word metric.

This is robust against two natural hidden-scope concerns:

1. the measure is already symmetric;
2. the subgroup already has infinite index, matching the surrounding discussion.

Therefore adding either of those restrictions does not repair the printed statement.

The failure is specifically tied to the displayed Cesaro normalization in the source. A differently normalized drift question (for example the ordinary single-time drift `n^{-1} E d(X_nH,H)`) is a different mathematical statement and is **not** claimed resolved here.

## 4. Prior attempt and current-literature check

The intake's prior attempt `E0071-A001` discussed Poisson-boundary/Liouville methods but did not identify a source-level proof or counterexample. The present counterexample is therefore new relative to the recovered repository attempt history.

Dated search: **2026-09-18 UTC**. I checked the current arXiv-v2 source, exact wording/formula, title plus `Problem 3`, homogeneous-space drift / Poisson-boundary terms, later Björklund work, and nearby citing literature. The source still prints the formula above. The bounded search did not surface a later primary paper or erratum explicitly correcting or resolving this exact printed Problem 3. This negative search is not a worldwide novelty certificate. The later 2017 Björklund paper *Random walks on countable groups* develops the drift/Liouville and Poisson-boundary results but the bounded search did not recover a correction of this Appendix-II formula.

## 5. Metric and closure status

Frozen R19 target metric:

`C_E0071 = 1` iff R19 has a complete source-valid proof deciding the exact printed Problem 3, with all hypotheses checked.

This artifact moves

\[
\boxed{C_{E0071}:0\to1.}
\]

Mathematical status: **REFUTED_CANDIDATE / SOURCE-MATCHING / AS-PRINTED**.

Fleet closure is still pending the protocol's two independent end-to-end audits: one P26 audit and one distinct OTHER-track audit. No finite computational core is used, so there is no exact-arithmetic checker or Lean obligation for this proof.

## 6. Methods used

- **#2 ATTACK THE NEGATION FIRST:** instead of trying to prove the homogeneous-space analogue, test the smallest Liouville quotient.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** the source asks for an affirmative extension; the symmetric `Z` example answers the printed question negatively.
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** odd times alone already force a uniform positive contribution, avoiding CLT/local-limit machinery entirely.
