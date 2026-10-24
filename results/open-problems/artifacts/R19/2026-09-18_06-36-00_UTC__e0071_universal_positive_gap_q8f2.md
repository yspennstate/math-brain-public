# R19 / E0071 — universal positive-gap obstruction for Björklund Problem 3

Date: 2026-09-18 UTC.  
Repository: `yspennstate/math-open-problems`, branch `master`.

## Source and scope

Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

The source defines a measured group `(G,mu)` by requiring `supp(mu)` to generate `G` as a semigroup. Problem 3 asks, for a subgroup `H<G` acting ergodically on the Poisson boundary and a left `G`-invariant metric `d` on `G/H`, whether

\[
A_n:=\frac1n\sum_{k=1}^n\int_G d(gH,H)\,d\mu^{*k}(g)\longrightarrow0.
\tag{P3}
\]

The current arXiv HTML was reread on 2026-09-18 and still prints exactly this Cesàro average of **unnormalized** distances. No later primary erratum or explicit resolution was located in the bounded dated searches recorded in the run report. This is negative search evidence only; novelty remains unverified.

## New result

The printed conclusion is not merely false for particular examples. It is impossible for **every nontrivial quotient** under the source's measured-group hypothesis.

### Theorem

Let `(G,mu)` be a countable measured group in Björklund's convention, let `H<G`, put `X=G/H` and `o=H`, and let `d` be any left `G`-invariant metric on `X`. Assume `X` is nontrivial. Then there exists `s in supp(mu)` with `so != o`. Put

\[
p:=\mu(s)>0,\qquad r:=d(so,o)>0.
\]

For every `n>1/p`, with `A_n` as in (P3),

\[
\boxed{
A_n\ge
\frac{r\,(p-1/n)}{(1+\sqrt p)^2}.
}
\tag{1}
\]

Consequently

\[
\boxed{
\liminf_{n\to\infty}A_n
\ge
\frac{pr}{(1+\sqrt p)^2}>0.
}
\tag{2}
\]

Thus Problem 3 is false as printed for every nontrivial quotient `G/H`. The Poisson-boundary ergodicity assumption is irrelevant to this obstruction.

The statement remains valid if some `A_n=+infinity`; then (1) is automatic for those `n`.

## Proof

Let `P` be the Markov kernel on `X=G/H` induced by left multiplication with a `mu`-distributed group element:

\[
P(x,E)=\sum_{g\in G}\mu(g)\,\mathbf 1_{\{gx\in E\}}.
\]

Let

\[
\nu_n:=\frac1n\sum_{k=1}^n\delta_oP^k.
\tag{3}
\]

Then

\[
A_n=\int_X d(o,x)\,d\nu_n(x).
\tag{4}
\]

Because `supp(mu)` generates `G` as a semigroup and `X` is nontrivial, not every element of `supp(mu)` can fix `o`; otherwise the generated semigroup would lie in `H`. Hence we may choose `s in supp(mu)` with `so != o`, and therefore `p=mu(s)>0` and `r=d(so,o)>0`.

Fix a parameter `a in (0,1)` and define

\[
U_a:=\{x\in X:d(o,x)<ar\},
\qquad
V_a:=\{y\in X:d(o,y)>(1-a)r\}.
\tag{5}
\]

If `x in U_a`, left invariance and the triangle inequality give

\[
d(o,sx)
\ge d(o,so)-d(so,sx)
=r-d(o,x)
>(1-a)r,
\tag{6}
\]

because `d(so,sx)=d(o,x)`. Thus `sx in V_a`, and the single atom `s` of the transition law already yields

\[
P(x,V_a)\ge p\qquad(x\in U_a).
\tag{7}
\]

Integrating against `nu_n`,

\[
(\nu_nP)(V_a)\ge p\,\nu_n(U_a).
\tag{8}
\]

On the other hand, (4) and Markov's inequality imply

\[
\nu_n(U_a)
\ge1-\frac{A_n}{ar},
\tag{9}
\]

and

\[
\nu_n(V_a)
\le\frac{A_n}{(1-a)r}.
\tag{10}
\]

The Cesàro occupation measure is asymptotically stationary in total variation by the exact telescoping identity

\[
\nu_nP-\nu_n
=\frac{\delta_oP^{n+1}-\delta_oP}{n}.
\tag{11}
\]

Hence, for every event `E subset X`,

\[
|\nu_nP(E)-\nu_n(E)|\le\frac1n.
\tag{12}
\]

Apply (12) to `V_a` and combine (8)--(10):

\[
p\left(1-\frac{A_n}{ar}\right)
\le (\nu_nP)(V_a)
\le \nu_n(V_a)+\frac1n
\le \frac{A_n}{(1-a)r}+\frac1n.
\tag{13}
\]

Rearranging,

\[
A_n\ge
\frac{r\,(p-1/n)}{p/a+1/(1-a)}.
\tag{14}
\]

The denominator is minimized over `a in (0,1)` when

\[
a=\frac{\sqrt p}{1+\sqrt p},
\tag{15}
\]

for which

\[
\frac pa+\frac1{1-a}=(1+\sqrt p)^2.
\tag{16}
\]

Substitution gives (1), and `n -> infinity` gives (2). This proves the theorem. ∎

## Interpretation

This subsumes all preceding R19 E0071 witnesses, including the simple walk on `Z`, the source-suggested product/diagonal example, the finite-quotient obstruction, and the proper-infinite-quotient escape theorem.

The mechanism is local and does not use recurrence, Liouville theory, properness, finite quotient size, parity, a CLT, or Poisson-boundary ergodicity. A single support atom that moves the base coset forces a uniformly positive one-step fraction of any near-base Cesàro mass away from the base. But the Cesàro occupation measures are `O(1/n)`-stationary by telescoping. Concentration of their first moment at zero is therefore impossible.

This also sharpens the normalization diagnosis without asserting authorial intent: the source's surrounding drift theory uses the usual single-time `1/n` normalization, while literal Problem 3 averages unnormalized distances. The result above addresses only the printed statement.

## Method mapping

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce the radius split `a in (0,1)` and optimize it; the optimization yields the explicit constant `(1+sqrt(p))^{-2}`.
- **#11 DUALIZE:** replace the unbounded distance moment by the two bounded indicator tests `U_a` and `V_a`; the exact Cesàro stationarity defect is then controlled in total variation.
- **#27 SWAP THE QUANTIFIERS:** instead of producing another counterexample, prove a uniform negation for every nontrivial quotient and every invariant metric.

## Status discipline

This is a self-check / strengthening by R19. It does **not** count as either required independent audit. The source metric `C_E0071` was already `1`, so this theorem earns no additional metric unit. Publication novelty is not claimed.
