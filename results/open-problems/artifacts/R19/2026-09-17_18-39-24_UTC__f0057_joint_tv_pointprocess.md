Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6/maximum attestation, so I do not claim otherwise. **F0057 stronger proof candidate; fixed metric `M_TV: 1 -> 1`; methods #3 PROVE SOMETHING STRONGER, #11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE.**

# F0057 — joint total variation for finitely many largest boxes

## 0. Source, exact scope, and status

Source: Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), DOI `10.1214/11-PS188`, arXiv `1112.0510`, Theorem 19.7 and Problem 19.10 (Problem 18.10 in the intake/arXiv numbering).

Janson proves, under Theorem 19.7's assumptions, Kolmogorov convergence for every fixed order statistic and total-variation convergence for the maximum. He then asks whether

\[
 d_{\rm TV}(Y_{(j)},\xi_{(j)})\to0
 \qquad(j\text{ fixed})
\]

and immediately adds that he believes the result extends to the **joint distribution of finitely many** order statistics.

The preceding R19 artifact

`artifacts/R19/2026-09-17_17-37-27_UTC__f0057_full_proof_6c1e.md`

already gives a source-wide proof candidate for the numbered marginal problem and closes the campaign's explicit truncation gap `P30H-F001`. The present artifact does **not** restart that proof. It proves the stronger joint statement by a different mechanism.

Status here: **PROVED_CANDIDATE_STRONGER / JOINT-TV / AUDIT_PENDING / PUBLICATION-NOVELTY-UNVERIFIED**. This is not called closed before two independent outside-track audits.

---

## 1. Stronger theorem

Let

\[
Y_{(1)}\ge Y_{(2)}\ge\cdots
\]

be the ordered occupancies in Janson's conditioned allocation, and let

\[
\zeta_{n,(1)}\ge\zeta_{n,(2)}\ge\cdots
\]

be the order statistics of `n` independent copies of the reference law used in the corresponding version of Theorem 19.7: either the fixed law `xi`, or the tuned law `xi^(n)`.

### Theorem A — joint total variation

For every fixed `r>=1`, under each comparison regime in Theorem 19.7,

\[
\boxed{
 d_{\rm TV}\!\left(
 (Y_{(1)},\ldots,Y_{(r)}),
 (\zeta_{n,(1)},\ldots,\zeta_{n,(r)})
 \right)\longrightarrow0.
}
\tag{A}
\]

Concretely this includes:

1. the main fixed-law regime `omega=infinity`, `m=lambda n+o(sqrt(n))`, `0<lambda<=nu`, and `Var(xi)<infinity`;
2. when `lambda<nu`, arbitrary `m/n->lambda` with the tuned law `xi^(n)`;
3. when `lambda<nu` and `m/n=lambda+o(1/log n)`, the fixed-law comparison with `xi`.

By projection, (A) implies joint total variation for any fixed finite collection

\[
(Y_{(j_1)},\ldots,Y_{(j_s)})
\]

and in particular proves Janson's numbered Problem 19.10 for every fixed `j`.

The proof has two genuinely new ingredients relative to the preceding block-sandwich proof: a bounded-intensity **tail point-process TV lemma** and an exact **factorial-moment / Janossy inversion** argument.

---

## 2. Counterexample-first stress tests

Before proving (A), three failure modes were tested.

### 2.1 Kolmogorov convergence alone is hopeless

Janson's own Remark 19.6 gives integer-valued examples with Kolmogorov distance tending to zero but total-variation distance equal to one (a parity obstruction). Therefore neither the scalar result `d_K(Y_(j),xi_(j))->0` nor its multivariate analogue can by itself imply (A).

The proof below must use the stronger local conditioning structure, not only order-statistic CDFs.

### 2.2 A huge boundary atom can defeat a naive tail threshold

If one chooses a threshold `h_n` with `n P(zeta_n>=h_n)<=D`, the intensity can jump from much larger than `D` at `h_n-1` to very small at `h_n`. Thus one cannot assume that the restricted tail already contains the top `r` observations with high probability.

The proof below pads missing tail positions by the boundary value `h_n-1`. This turns a large boundary atom from an obstruction into an exact reconstruction rule.

### 2.3 Ties cannot be discarded

Several largest occupancies may be equal. Any argument based on distinct tail values silently changes the problem. The point process below is a **counting measure with multiplicities**. Its factorial measures select distinct coordinate indices, but the selected values may coincide. Hence ties are retained exactly.

None of these attacks produces a counterexample once the source's uniform local-ratio input is used.

---

## 3. Source inputs and the uniform finite-coordinate ratio

We work after Janson's standard replacement by an equivalent probability weight sequence. Let `p_n(k)` denote the independent reference mass function:

- in the main fixed-law case, `p_n(k)=P(xi=k)`;
- in the tuned case, `p_n(k)=P(xi^(n)=k)`.

Let `zeta_n` have mass function `p_n`.

The proof of Theorem 19.7 supplies an integer cutoff `U_n` such that

\[
\mathbb P(Y_{(1)}>U_n)=o(1),
\qquad
n\mathbb P(\zeta_n>U_n)=o(1),
\tag{3.1}
\]

and

\[
U_n=o(\sqrt n)
\tag{3.2}
\]

in the fixed-law regime, while in the tuned regime one can take

\[
U_n=O(\log n).
\tag{3.3}
\]

The source explicitly proves the one-coordinate uniform ratio below the cutoff and then says the same factorial-moment argument works at every fixed order. We record the precise multi-coordinate form because it is what the point-process proof needs.

### Lemma 3.1 — uniform fixed-coordinate factorization

For every fixed integer `q>=1`, there is `epsilon_{n,q}->0` such that, uniformly over supported integers

\[
0\le k_1,\ldots,k_q\le U_n,
\]

\[
\boxed{
\mathbb P(Y_1=k_1,\ldots,Y_q=k_q)
=
\bigl(1+\theta_n(k_1,\ldots,k_q)\bigr)
\prod_{a=1}^q p_n(k_a),
\qquad
|\theta_n|\le\epsilon_{n,q}.
}
\tag{3.4}
\]

#### Proof

Let `s=k_1+...+k_q`. The exact conditioned-allocation identity is

\[
\mathbb P(Y_1=k_1,\ldots,Y_q=k_q)
=
\prod_{a=1}^q p_n(k_a)
\frac{\mathbb P(S^{(n)}_{n-q}=m-s)}
     {\mathbb P(S^{(n)}_n=m)},
\tag{3.5}
\]

where `S_t^(n)` is the sum of `t` independent copies of the reference variable. Equivalent exponential tilting does not change the conditioned allocation, so (3.5) is valid in both source versions.

In the fixed-law regime,

\[
(m-s)-(n-q)\lambda
=(m-n\lambda)+(q\lambda-s).
\tag{3.6}
\]

The first term is `o(sqrt(n))`, while `0<=s<=qU_n=o(sqrt(n))` uniformly because `q` is fixed. Thus the numerator in (3.5) lies uniformly in the central `o(sqrt(n))` window of the same lattice local limit theorem used in Janson's equations (19.15), (19.21), and his higher-factorial-moment calculation. The denominator lies in the same window. Their ratio is `1+o(1)` uniformly.

In the tuned regime, `E zeta_n=m/n` exactly, so

\[
(m-s)-(n-q)\mathbb E\zeta_n
=q\,m/n-s=O(U_n)=O(\log n)=o(\sqrt n)
\tag{3.7}
\]

uniformly. Janson's triangular-array local limit argument used for (19.45), together with `tau_n->tau`, gives the same uniform ratio. The support/span is unchanged by the equivalent tilting, so no hidden lattice class is introduced. This proves (3.4). ∎

---

## 4. Change of language: bounded tail point processes

Fix `D<infinity`. Let

\[
T_n\subseteq\{0,1,\ldots,U_n\}
\]

be any moving set satisfying

\[
\lambda_n:=n\,p_n(T_n)\le D.
\tag{4.1}
\]

Define the conditioned and independent restricted counting measures

\[
\eta_n^Y:=\sum_{i=1}^n \mathbf1_{\{Y_i\in T_n\}}\,\delta_{Y_i},
\qquad
\eta_n^0:=\sum_{i=1}^n \mathbf1_{\{\zeta_{n,i}\in T_n\}}\,\delta_{\zeta_{n,i}}.
\tag{4.2}
\]

These are finite point processes on the finite/countable space `T_n`, with all multiplicities retained.

### Theorem B — bounded-intensity tail-process total variation

Under Lemma 3.1 and (4.1),

\[
\boxed{
 d_{\rm TV}\bigl(\mathcal L(\eta_n^Y),\mathcal L(\eta_n^0)\bigr)\to0.
}
\tag{4.3}
\]

This statement is uniform in the choice of the moving set `T_n` as long as its reference intensity is at most `D`.

The proof is the dualization step: instead of partitioning the value axis and bounding every order-statistic event separately, we invert the factorial moment measures to recover the whole bounded tail point-process law.

---

## 5. Factorial measures are close in L1

For `q>=1`, let `alpha^Y_{n,q}` and `alpha^0_{n,q}` be the ordered factorial moment measures on `T_n^q`. For `x=(x_1,...,x_q) in T_n^q`,

\[
\alpha^Y_{n,q}(x)
=(n)_q\,\mathbb P(Y_1=x_1,\ldots,Y_q=x_q),
\tag{5.1}
\]

and, for the independent process,

\[
\alpha^0_{n,q}(x)
=(n)_q\prod_{a=1}^q p_n(x_a).
\tag{5.2}
\]

The coordinates `x_a` may be equal; `(n)_q` selects distinct **indices**, not distinct values.

By Lemma 3.1,

\[
\begin{aligned}
\|\alpha^Y_{n,q}-\alpha^0_{n,q}\|_1
&\le
\epsilon_{n,q}(n)_q\,p_n(T_n)^q\\
&\le \epsilon_{n,q}D^q
\longrightarrow0
\end{aligned}
\tag{5.3}
\]

for every fixed `q`.

Moreover,

\[
\alpha^0_{n,q}(T_n^q)=(n)_q p_n(T_n)^q\le D^q,
\tag{5.4}
\]

and hence

\[
\limsup_n\alpha^Y_{n,q}(T_n^q)\le D^q.
\tag{5.5}
\]

---

## 6. Janossy inversion with an explicit remainder

Let `N_n^Y=eta_n^Y(T_n)` and `N_n^0=eta_n^0(T_n)`. For either process, write `alpha_q` for its ordered factorial measure and define the ordered Janossy measure

\[
J_q(A):=
\mathbb E\!\left[
\mathbf1_{\{N=q\}}\eta^{[q]}(A)
\right],
\qquad A\subseteq T_n^q,
\tag{6.1}
\]

where `eta^[q]` sums over ordered `q`-tuples of distinct point **indices**.

### Lemma 6.1 — exact inversion

For a process with at most `n` points,

\[
\boxed{
J_q
=
\sum_{s=0}^{n-q}\frac{(-1)^s}{s!}
\alpha_{q+s}(\,\cdot\,\times T_n^s).
}
\tag{6.2}
\]

#### Proof

Fix one realization with `N` points and one ordered selected `q`-tuple of distinct indices. The term of order `s` chooses `s` further ordered distinct indices from the remaining `N-q`, and division by `s!` changes `(N-q)_s` into `binom(N-q,s)`. Thus the tuple receives total weight

\[
\sum_{s=0}^{N-q}(-1)^s\binom{N-q}{s}
=\mathbf1_{\{N=q\}}.
\tag{6.3}
\]

Summing over selected tuples and averaging proves (6.2). ∎

### Lemma 6.2 — truncation remainder

If (6.2) is truncated after `s=R`, then its remainder `R_{q,R}` satisfies

\[
\boxed{
\|R_{q,R}\|_1
\le
\frac{\alpha_{q+R+1}(T_n^{q+R+1})}{(R+1)!}.
}
\tag{6.4}
\]

#### Proof

For `t=N-q>0`, the alternating partial binomial sum obeys

\[
\left|\sum_{s=0}^R(-1)^s\binom ts\right|
=\binom{t-1}{R}
\le\binom t{R+1}
\tag{6.5}
\]

when `R<t`, and is zero when `R>=t`. Hence the total absolute residual weight over all ordered selected `q`-tuples is at most

\[
(N)_q\binom{N-q}{R+1}
=\frac{(N)_{q+R+1}}{(R+1)!}.
\tag{6.6}
\]

Expectation gives (6.4). ∎

### Lemma 6.3 — fixed-order Janossy measures converge in L1

For each fixed `q`,

\[
\|J^Y_{n,q}-J^0_{n,q}\|_1\to0.
\tag{6.7}
\]

#### Proof

Fix `R`. By Lemmas 6.1–6.2,

\[
\begin{aligned}
\|J^Y_{n,q}-J^0_{n,q}\|_1
&\le
\sum_{s=0}^R\frac1{s!}
\|\alpha^Y_{n,q+s}-\alpha^0_{n,q+s}\|_1\\
&\quad+
\frac{\alpha^Y_{n,q+R+1}(T_n^{q+R+1})
+\alpha^0_{n,q+R+1}(T_n^{q+R+1})}{(R+1)!}.
\end{aligned}
\tag{6.8}
\]

For fixed `R`, the finite sum tends to zero by (5.3). By (5.4)–(5.5),

\[
\limsup_{n\to\infty}
\|J^Y_{n,q}-J^0_{n,q}\|_1
\le
\frac{2D^{q+R+1}}{(R+1)!}.
\tag{6.9}
\]

Now send `R->infinity`. ∎

---

## 7. From Janossy measures to total variation of the process

For either process, if `N>K`, then

\[
(N)_{K+1}\ge(K+1)!,
\]

so

\[
\mathbb P(N>K)
\le
\frac{\mathbb E(N)_{K+1}}{(K+1)!}
=
\frac{\alpha_{K+1}(T_n^{K+1})}{(K+1)!}.
\tag{7.1}
\]

Consequently,

\[
\limsup_n\mathbb P(N_n^Y>K)
\le\frac{D^{K+1}}{(K+1)!},
\qquad
\mathbb P(N_n^0>K)
\le\frac{D^{K+1}}{(K+1)!}.
\tag{7.2}
\]

Conditional on `N=q`, the point-process law is the pushforward, under the map from an ordered `q`-tuple to its counting measure, of `J_q/q!`. Therefore

\[
\begin{aligned}
d_{\rm TV}(\mathcal L(\eta_n^Y),\mathcal L(\eta_n^0))
&\le
\mathbb P(N_n^Y>K)+\mathbb P(N_n^0>K)\\
&\quad+
\frac12\sum_{q=0}^K\frac1{q!}
\|J^Y_{n,q}-J^0_{n,q}\|_1.
\end{aligned}
\tag{7.3}
\]

For fixed `K`, the finite sum vanishes by Lemma 6.3. Thus

\[
\limsup_n d_{\rm TV}(\mathcal L(\eta_n^Y),\mathcal L(\eta_n^0))
\le
\frac{2D^{K+1}}{(K+1)!}.
\tag{7.4}
\]

Let `K->infinity`. This proves Theorem B. ∎

---

## 8. Recovering the top `r` vector from a bounded tail

Fix `r>=1` and choose `D>=2r`. Define

\[
\mu_n(h):=n\,\mathbb P(\zeta_n\ge h).
\tag{8.1}
\]

Because `mu_n(0)=n>D`, while by (3.1)

\[
\mu_n(U_n+1)=n\mathbb P(\zeta_n>U_n)=o(1),
\]

there is, for large `n`, a smallest integer

\[
h_n:=\min\{h:\mu_n(h)\le D\}
\in\{1,\ldots,U_n+1\}.
\tag{8.2}
\]

By minimality,

\[
\mu_n(h_n-1)>D.
\tag{8.3}
\]

Take

\[
T_n:=\{h_n,h_n+1,\ldots,U_n\}.
\tag{8.4}
\]

Its reference intensity is at most `D`, so Theorem B applies.

Define a deterministic map `Phi_{n,r}` on counting measures on `T_n`: list the atoms in decreasing order with multiplicity, retain the first `r`, and if there are fewer than `r` atoms, pad all missing positions with the boundary value `h_n-1`.

On the event

\[
G_n^Y:=\{Y_{(1)}\le U_n,\ Y_{(r)}\ge h_n-1\},
\tag{8.5}
\]

we have the **exact identity**

\[
(Y_{(1)},\ldots,Y_{(r)})
=\Phi_{n,r}(\eta_n^Y).
\tag{8.6}
\]

Indeed, every value strictly above `h_n-1` is recorded in `T_n`; if fewer than `r` such values occur, the assumption `Y_(r)>=h_n-1` forces every missing top position to equal exactly `h_n-1`. The same statement holds for the iid vector and `eta_n^0`.

The reference number of observations at least `h_n-1` is binomial with mean `mu_n(h_n-1)>D`. Since `D>=2r`, the standard lower-tail Chernoff bound gives

\[
\mathbb P(\zeta_{n,(r)}<h_n-1)
\le e^{-D/8}.
\tag{8.7}
\]

For the conditioned vector, Theorem 19.7(v) gives

\[
d_K(Y_{(r)},\zeta_{n,(r)})\to0,
\tag{8.8}
\]

so, evaluating the CDF at the moving integer `h_n-2`,

\[
\mathbb P(Y_{(r)}<h_n-1)
\le e^{-D/8}+o(1).
\tag{8.9}
\]

(The event is empty if the boundary is below zero.) The upper-cutoff failures in (8.5) are `o(1)` by (3.1).

Total variation contracts under measurable maps. Hence Theorem B, (8.6), and a triangle inequality imply

\[
\begin{aligned}
&d_{\rm TV}\!\left(
 (Y_{(1)},\ldots,Y_{(r)}),
 (\zeta_{n,(1)},\ldots,\zeta_{n,(r)})
 \right)\\
&\qquad\le
 d_{\rm TV}\bigl(\mathcal L(\eta_n^Y),\mathcal L(\eta_n^0)\bigr)
 +\mathbb P((G_n^Y)^c)+\mathbb P((G_n^0)^c).
\end{aligned}
\tag{8.10}
\]

Therefore, for each fixed `D>=2r`,

\[
\limsup_{n\to\infty}
 d_{\rm TV}\!\left(
 (Y_{(1)},\ldots,Y_{(r)}),
 (\zeta_{n,(1)},\ldots,\zeta_{n,(r)})
 \right)
\le2e^{-D/8}.
\tag{8.11}
\]

Finally send `D->infinity`. This proves (A) in the main fixed-law regime and in the tuned regime. ∎

---

## 9. The weakened fixed-law regime `m/n=lambda+o(1/log n)`

Assume `lambda<nu` and

\[
m/n=\lambda+o(1/\log n).
\tag{9.1}
\]

Theorem 19.7 first compares the conditioned allocation to the tuned law `xi^(n)`. The argument above therefore gives

\[
d_{\rm TV}\!\left(
(Y_{(1)},\ldots,Y_{(r)}),
(\xi^{(n)}_{(1)},\ldots,\xi^{(n)}_{(r)})
\right)\to0.
\tag{9.2}
\]

Janson's equation (19.46) gives, uniformly for `k<=U_n=O(log n)`,

\[
\mathbb P(\xi^{(n)}=k)
=(1+o(1))\mathbb P(\xi=k),
\tag{9.3}
\]

and both laws have tail probability `o(1/n)` beyond `U_n`.

Apply the bounded-tail point-process proof once more, now to two **independent** samples, one from `xi^(n)` and one from `xi`. On every tail set of intensity at most `D`, (9.3) makes the factorial measures `o(1)`-close in L1 exactly as in (5.3); the same boundary-padding argument applies. Consequently

\[
d_{\rm TV}\!\left(
(\xi^{(n)}_{(1)},\ldots,\xi^{(n)}_{(r)}),
(\xi_{(1)},\ldots,\xi_{(r)})
\right)\to0.
\tag{9.4}
\]

Combining (9.2) and (9.4) proves (A) in the weakened fixed-law regime as well. ∎

---

## 10. What this proves relative to F0057

The source's numbered Problem 19.10 asks only for one fixed marginal `Y_(j)`. Theorem A proves the stronger statement Janson explicitly says he believes immediately before the problem: joint total-variation convergence of any finite collection of largest occupancies.

No stronger moment assumption, compact-support assumption, changed allocation model, or no-tie assumption was introduced.

This does **not** increase R19's frozen F0057 metric, because that metric was already binary and the preceding source-wide marginal proof moved it from `0` to `1`. Thus the honest metric update for this run is

\[
\boxed{M_{\rm TV}:1\to1.}
\]

The mathematical status is strengthened, but repository closure still requires two independent full-proof audits.

---

## 11. Dated prior-art check and access limits

On 2026-09-17 I searched the current web/primary-source index for the exact phrases and combinations around:

- `Problem 19.10` + Janson + total variation;
- `d_TV(Y_(j), xi_(j))`;
- `joint distribution of finitely many Y_(j)`;
- fixed-`j` total variation for conditioned random allocations.

The search recovered Janson's original source and its still-printed open statement, but no later primary paper explicitly resolving either the exact marginal problem or the stronger joint-TV statement. This is a **bounded negative search, not a novelty certificate**.

The primary PDF itself was located at the journal/author mirrors. Direct PDF opening in the current web runtime timed out/cache-missed, so no claim is made of a successful page-image inspection in this run. Indexed primary-source text exposed the exact theorem/problem wording, the cutoff/local-ratio proof, and the tuned-law equations used above.

---

## 12. Audit obligations

No self-check is counted as an independent audit. A P26 audit and one distinct OTHER-track audit should attack the following exact points:

1. Lemma 3.1, especially fixed-`q` uniformity of the local limit ratio and the tuned triangular-array version;
2. the Janossy inversion (6.2) and explicit remainder (6.4);
3. the process-TV passage (7.3), including multiplicities/ties;
4. the boundary-padding identity (8.6) when the threshold has a large atom;
5. the replacement `xi^(n)->xi` in the weakened fixed-law regime.

Until both independent audits pass, the correct label remains **PROVED_CANDIDATE_STRONGER / AUDIT_PENDING**, not CLOSED.
