# R19 / E0071 structural obstruction: doubly stochastic quotient walks

Date: 2026-09-18 UTC.

Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

## Exact printed question

For a measured group `(G,mu)`, a subgroup `H<G` acting ergodically on the Poisson boundary, and a left `G`-invariant metric `d` on `G/H`, the source asks whether

\[
A_n:=\frac1n\sum_{k=1}^n\int_G d(gH,H)\,d\mu^{*k}(g)\longrightarrow0.
\tag{P3}
\]

This note does not alter the already-complete explicit counterexamples. It identifies a structural reason the printed normalization fails for every nontrivial quotient equipped with a proper invariant metric.

## Theorem

Let `(G,mu)` be a countable measured group in the source convention: `supp(mu)` generates `G` as a semigroup. Let `H<G`, let `X=G/H`, and let `d` be a left `G`-invariant metric on `X`. Start the induced quotient walk at `o=H`, and write

\[
A_n=\frac1n\sum_{k=1}^n E_o[d(X_k,o)].
\]

Assume `X` is nontrivial.

1. If `X` is finite, then
   \[
   A_n\longrightarrow \frac1{|X|}\sum_{x\in X}d(x,o)>0.
   \]
2. If `X` is infinite and `d` is proper, meaning every closed ball about `o` is finite, then
   \[
   A_n\longrightarrow+\infty.
   \]

In particular, under these metric hypotheses the conclusion printed in Problem 3 is impossible, independently of whether `H` acts ergodically on the Poisson boundary. The Poisson-boundary assumption is not used.

The infinite-case statement is stronger than the explicit `Z` and product/diagonal examples already archived by R19: divergence is forced by doubly stochastic escape of Cesaro occupation mass, not by a special parity or local-limit computation.

## Proof

### 1. Move the problem to a Markov chain

For `x,y in X`, define

\[
P(x,y)=\int_G \mathbf 1_{\{gx=y\}}\,d\mu(g).
\tag{1}
\]

Each fixed `g in G` acts on `X` by a permutation. Therefore `P` is not only stochastic but doubly stochastic:

\[
\sum_yP(x,y)=1,\qquad \sum_xP(x,y)=1.
\tag{2}
\]

Because `supp(mu)` generates `G` as a semigroup and the `G`-action on `G/H` is transitive, `P` is irreducible.

Let

\[
\nu_n:=\frac1n\sum_{k=1}^n\delta_oP^k.
\tag{3}
\]

Then the printed quantity is exactly the first moment of the Cesaro occupation measure:

\[
A_n=\sum_{x\in X}d(x,o)\nu_n(x).
\tag{4}
\]

This is the representation that makes the obstruction transparent.

### 2. Infinite irreducible doubly stochastic chains have no stationary probability

We first record an elementary lemma.

**Lemma 1.** If `P` is an irreducible doubly stochastic transition matrix on an infinite countable state space `X`, then `P` has no stationary probability distribution.

**Proof.** Suppose `pi` is stationary. Since `pi in ell^1(X)`, the positive number

\[
M:=\sup_{x\in X}\pi(x)
\]

is attained at some `y`: if no value attained the positive supremum, infinitely many values would exceed (say) `M/2`, contradicting summability.

For every `m>=1`, stationarity and double stochasticity of `P^m` give

\[
M=\pi(y)=\sum_x\pi(x)P^m(x,y)
\le M\sum_xP^m(x,y)=M.
\tag{5}
\]

Thus equality holds term by term in the nonnegative deficit sum. Hence whenever `P^m(x,y)>0`, one has `pi(x)=M`. By irreducibility, for every `x` there exists some `m=m(x)` with `P^m(x,y)>0`; therefore `pi(x)=M` for every `x`. Since `X` is infinite and `M>0`, this contradicts `sum_x pi(x)=1`. ∎

### 3. Cesaro occupation mass vanishes on every fixed state in the infinite case

**Lemma 2.** Under the hypotheses of Lemma 1,

\[
\nu_n(x)\longrightarrow0\qquad\text{for every }x\in X.
\tag{6}
\]

**Proof.** Suppose not. Then for some `y`, some `epsilon>0`, and a subsequence `n_j`,

\[
\nu_{n_j}(y)\ge\epsilon.
\]

By diagonal extraction on the countable set `X`, pass to a further subsequence such that `nu_{n_j}(x)` converges for every `x`; call the pointwise limit `nu(x)`. Fatou gives

\[
0<\epsilon\le\nu(y),\qquad \sum_x\nu(x)\le1.
\tag{7}
\]

The Cesaro measures are asymptotically stationary. Indeed,

\[
\nu_nP-\nu_n
=\frac{\delta_oP^{n+1}-\delta_oP}{n},
\tag{8}
\]

so every coordinate of the left side tends to zero.

Fix `z`. Because the `z`-th column of `P` sums to one and `0<=nu_n(x)<=1`, dominated convergence with weights `P(x,z)` yields

\[
\lim_j(\nu_{n_j}P)(z)
=\sum_x\nu(x)P(x,z)=(\nu P)(z).
\tag{9}
\]

Combining (8) and (9) gives `nu P=nu`. Its total mass `s=sum_x nu(x)` lies in `(0,1]`; therefore `pi=nu/s` is a stationary probability distribution, contradicting Lemma 1. ∎

Consequently, for every finite set `F subset X`,

\[
\nu_n(F)\to0.
\tag{10}
\]

### 4. Proper metrics force divergence

Assume now that `X` is infinite and `d` is proper. For every `R>0`, the ball

\[
B_R:=\{x:d(x,o)<R\}
\]

is finite. By (10), `nu_n(B_R)->0`. Therefore

\[
A_n
=\sum_xd(x,o)\nu_n(x)
\ge R\,\nu_n(X\setminus B_R)
=R(1-\nu_n(B_R)).
\tag{11}
\]

Hence

\[
\liminf_{n\to\infty}A_n\ge R.
\]

Since `R>0` is arbitrary,

\[
\boxed{A_n\to+\infty.}
\tag{12}
\]

This proves part 2.

### 5. Finite quotients force a positive limit

If `X` is finite, irreducibility and double stochasticity imply that the unique stationary probability is the uniform law

\[
u(x)=\frac1{|X|}.
\]

The Cesaro distributions of every finite irreducible chain converge to stationarity, even when the chain is periodic. Thus

\[
\nu_n(x)\to\frac1{|X|}
\]

for each `x`, and by (4)

\[
A_n\longrightarrow\frac1{|X|}\sum_{x\in X}d(x,o).
\tag{13}
\]

Because `X` is nontrivial and `d` is a metric, the right side is strictly positive. This proves part 1. ∎

## Consequences for the source problem

The printed Problem 3 therefore has a broad structural obstruction:

- on every nontrivial finite quotient, the Cesaro average tends to a positive uniform mean distance;
- on every infinite quotient with a proper invariant metric, the same quantity diverges to `+infinity`;
- neither conclusion uses the Poisson-boundary ergodicity assumption.

The source's surrounding drift theorem uses a single-time `1/n` normalization, while Problem 3 as printed takes a Cesaro average of unnormalized distances. The theorem above strengthens the diagnosis that this is probably a normalization issue, but it does **not** establish what correction the author intended.

## Method accounting

This run used three new Section-B moves for E0071:

- **#1 CHANGE THE CATEGORY:** replace the group-boundary formulation by an irreducible doubly stochastic quotient Markov chain.
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the displayed quantity as the first moment of the Cesaro occupation measure `nu_n`.
- **#29 ADD THE POINTS AT INFINITY:** show that on an infinite quotient every fixed finite set loses all Cesaro mass; properness then converts escape to infinity into divergence of the first moment.

No checker is appropriate: this is an analytic theorem, not a finite exhaustive claim. The full proof is on this page.

## Prior-art caution

The Markov-chain ingredients (double stochasticity, Cesaro escape on an infinite irreducible chain, and finite-state convergence to the uniform law) are standard/folklore-level mechanisms. This note does **not** claim novelty for them. A dated 2026-09-18 bounded search of the exact Problem 3 wording, later Björklund work, homogeneous-space drift, and related random-walk literature did not surface an explicit later correction or published resolution of the exact printed formula. That is negative evidence only; publication novelty remains **UNVERIFIED**.
