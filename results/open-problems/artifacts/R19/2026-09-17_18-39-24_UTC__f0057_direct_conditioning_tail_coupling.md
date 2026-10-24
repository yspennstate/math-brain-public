Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6/maximum attestation, so I do not claim otherwise. **F0057 direct-conditioning proof candidate; fixed metric `M_TV: 1 -> 1`; methods #3 PROVE SOMETHING STRONGER, #11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE.**

# F0057 — a direct conditioning/coupling proof of joint top-order-statistic TV

## 0. Why this artifact exists

A whole-repository search performed during this run recovered an older campaign handoff stating that an external/local file `JansonJointTV_author_proof.md` had already proved joint top-`J` total variation by a **rare-cloud Janossy/Bonferroni** argument. Therefore the first point-process/Janossy reconstruction written earlier in this run is useful as a repository-contained reconstruction, but it is **not a genuinely new route** and earns no novelty credit.

This artifact changes route. It proves the same stronger joint statement without Janossy inversion and without the interval sandwich. The central identity is a Radon–Nikodym formula for the rare tail cloud under conditioning on the total sum. The remaining `n-q` variables are distributed as the reference law conditioned to avoid the cloud; a triangular-array local CLT shows that this conditioning changes the probability of the global sum by a multiplicative `1+o(1)`, uniformly over every cloud configuration with bounded cardinality.

Status: **PROVED_CANDIDATE_STRONGER / DIRECT-CONDITIONING ROUTE / AUDIT_PENDING / NOVELTY-UNVERIFIED**.

---

## 1. Exact source scope and stronger target

Source: Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Theorem 19.7 and Problem 19.10 (Problem 18.10 in the intake/arXiv numbering).

The source asks whether, under Theorem 19.7's assumptions,

\[
d_{\rm TV}(Y_{(j)},\xi_{(j)})\to0
\qquad\text{for every fixed }j.
\tag{1.1}
\]

Immediately before the numbered problem Janson says he also believes the result extends to the **joint distribution of finitely many** order statistics.

We prove the stronger statement: for each fixed `r`,

\[
\boxed{
 d_{\rm TV}\!\left(
 (Y_{(1)},\ldots,Y_{(r)}),
 (\zeta_{n,(1)},\ldots,\zeta_{n,(r)})
 \right)\to0,
}
\tag{1.2}
\]

where `zeta_n=xi` in the fixed-law version and `zeta_n=xi^(n)` in the tuned version. Projection then gives (1.1) and every fixed finite subvector.

No stronger moment assumption, compact support, no-tie assumption, or changed allocation model is introduced.

---

## 2. Conditioned-allocation representation

After Janson's standard equivalent exponential tilt, let `p_n` denote the reference mass function and let

\[
Z_{n,1},\ldots,Z_{n,n}\stackrel{\rm iid}{\sim}p_n,
\qquad
S_n:=\sum_{i=1}^n Z_{n,i}.
\tag{2.1}
\]

The conditioned allocation satisfies the exact distributional identity

\[
(Y_1,\ldots,Y_n)
\overset d=
(Z_{n,1},\ldots,Z_{n,n})\mid\{S_n=m\}.
\tag{2.2}
\]

There are two cases.

- **Fixed law.** `p_n=p=L(xi)`, `m=lambda n+o(sqrt n)`, `0<lambda<=nu`, and `Var(xi)<infinity`.
- **Tuned law.** When `lambda<nu` and merely `m/n->lambda`, `p_n=L(xi^(n))` and `E Z_{n,1}=m/n` exactly. The source gives a uniform exponential tail and `p_n=>p`.

The proof of Theorem 19.7 provides an integer cutoff `U_n` with

\[
\mathbb P(Y_{(1)}>U_n)=o(1),
\qquad
n\mathbb P(Z_{n,1}>U_n)=o(1),
\tag{2.3}
\]

and `U_n=o(sqrt n)` in the fixed-law case, while `U_n=O(log n)` in the tuned case.

The same source local-CLT argument gives the following fixed-coordinate ratio, which will only be used for a tail-count estimate at the end: for every fixed `q`, uniformly for supported `k_1,...,k_q<=U_n`,

\[
\mathbb P(Y_1=k_1,\ldots,Y_q=k_q)
=(1+o(1))\prod_{a=1}^q p_n(k_a).
\tag{2.4}
\]

---

## 3. The genuinely different object: a rare cloud and its complement law

Let `D<infinity` be fixed. Let

\[
T_n\subseteq\{h_n,h_n+1,\ldots,U_n\}
\tag{3.1}
\]

be a moving high-value set such that

\[
a_n:=p_n(T_n),
\qquad
n a_n\le D,
\qquad
h_n\to\infty.
\tag{3.2}
\]

Define the tail cloud of the iid sample

\[
\eta_n:=\sum_{i=1}^n\mathbf1_{\{Z_{n,i}\in T_n\}}\delta_{Z_{n,i}}.
\tag{3.3}
\]

Let `p_n^c` be the reference law conditioned to avoid `T_n`:

\[
p_n^c(k)
:=\mathbb P(Z_{n,1}=k\mid Z_{n,1}\notin T_n)
=\frac{p_n(k)\mathbf1_{\{k\notin T_n\}}}{1-a_n}.
\tag{3.4}
\]

Write

\[
\mu_n:=\mathbb E Z_{n,1},
\qquad
\mu_n^c:=\mathbb E_{p_n^c} Z.
\tag{3.5}
\]

Because values removed by `T_n` are at most `U_n`,

\[
\left|\mu_n^c-\mu_n\right|
\le
\frac{a_n(|\mu_n|+U_n)}{1-a_n}
=O(U_n/n)
=o(n^{-1/2}).
\tag{3.6}
\]

Similarly,

\[
\left|\mathbb E_{p_n^c}Z^2-\mathbb E_{p_n}Z^2\right|
\le
\frac{a_n(O(1)+U_n^2)}{1-a_n}
=o(1),
\tag{3.7}
\]

because `U_n^2/n->0`. Hence the complement variance tends to the same positive source variance.

Moreover, `p_n^c=>p` and the family `p_n^c` is uniformly square-integrable:

- in the fixed-law case this follows because removing a set and renormalizing by `1+O(1/n)` cannot increase the tail second moment by more than that factor;
- in the tuned case the source's uniform exponential tail is inherited by the complement law.

Finally, the lattice span is eventually unchanged. Choose finitely many fixed support points whose gcd generates the source span `d`. Since `h_n->infinity`, all these points lie outside `T_n` eventually, so they remain in `p_n^c`; all support points still lie in the same `d`-lattice. Thus `span(p_n^c)=d` for all large `n`.

These are exactly the hypotheses needed for Janson's triangular-array local CLT, Lemma 14.1 with the uniform-square-integrability relaxation in Remark 14.2.

---

## 4. Uniform likelihood ratio for every bounded cloud configuration

Let `nu` be a possible realization of `eta_n` with exactly `q` points, where `q<=K` for some fixed `K`. List its atoms with multiplicity as

\[
x_1,\ldots,x_q\in T_n,
\qquad
s(\nu):=x_1+\cdots+x_q.
\tag{4.1}
\]

Conditionally on `eta_n=nu`, the `n-q` remaining coordinates are iid with law `p_n^c`, up to an irrelevant uniform choice of which labels carried the cloud points. Therefore

\[
\mathbb P(S_n=m\mid\eta_n=\nu)
=
\mathbb P\!\left(
S^{c}_{n-q}=m-s(\nu)
\right),
\tag{4.2}
\]

where `S^c_{n-q}` is a sum of `n-q` iid `p_n^c` variables.

### Lemma 4.1 — uniform bulk local ratio

For every fixed `K`,

\[
\boxed{
\sup_{\nu:\,|\nu|\le K}
\left|
\frac{\mathbb P(S_n=m\mid\eta_n=\nu)}
     {\mathbb P(S_n=m)}-1
\right|
\longrightarrow0.
}
\tag{4.3}
\]

#### Proof

For `q<=K`, `s(nu)<=K U_n=o(sqrt n)`. Also, using (3.6),

\[
\begin{aligned}
&(m-s(\nu))-(n-q)\mu_n^c\\
&= (m-n\mu_n)
   +(q\mu_n-s(\nu))
   -(n-q)(\mu_n^c-\mu_n).
\end{aligned}
\tag{4.4}
\]

In the tuned case the first term is zero; in the fixed-law case it is `o(sqrt n)` by hypothesis. The second term is `O(U_n)=o(sqrt n)`, uniformly for `q<=K`, and the third is also `O(U_n)=o(sqrt n)` by (3.6). Hence

\[
(m-s(\nu))-(n-q)\mu_n^c=o(\sqrt n)
\tag{4.5}
\]

uniformly over all cloud configurations with at most `K` points.

Apply Lemma 14.1/Remark 14.2 to the complement triangular array `p_n^c`. By (3.7), its variance tends to the same source variance `sigma^2`, and its span is `d`. Uniformly over (4.5),

\[
\mathbb P(S^c_{n-q}=m-s(\nu))
=\frac{d+o(1)}{\sqrt{2\pi\sigma^2 n}}.
\tag{4.6}
\]

The source denominator satisfies the identical asymptotic

\[
\mathbb P(S_n=m)
=\frac{d+o(1)}{\sqrt{2\pi\sigma^2 n}}.
\tag{4.7}
\]

The error in (4.6) is uniform because the deviation in (4.5) is uniformly `o(sqrt n)` and `K` is fixed. Dividing gives (4.3). ∎

### Corollary 4.2 — bounded-cardinality cloud laws are relatively identical

By Bayes' formula,

\[
\frac{\mathbb P(\eta_n=\nu\mid S_n=m)}
     {\mathbb P(\eta_n=\nu)}
=
\frac{\mathbb P(S_n=m\mid\eta_n=\nu)}
     {\mathbb P(S_n=m)}.
\tag{4.8}
\]

Thus for every fixed `K`, uniformly over `|nu|<=K`,

\[
\mathbb P(\eta_n=\nu\mid S_n=m)
=(1+o(1))\mathbb P(\eta_n=\nu).
\tag{4.9}
\]

This is the core mechanism: **conditioning on the global sum is asymptotically invisible to every bounded rare-cloud configuration**.

---

## 5. From bounded configurations to total variation of the whole cloud

Under the iid law,

\[
N_n:=|\eta_n|\sim\operatorname{Bin}(n,a_n),
\qquad
na_n\le D.
\tag{5.1}
\]

Hence, for every `K`,

\[
\mathbb P(N_n>K)
\le
\frac{\mathbb E(N_n)_{K+1}}{(K+1)!}
\le
\frac{D^{K+1}}{(K+1)!}.
\tag{5.2}
\]

For the conditioned allocation, let `N_n^Y` be the number of coordinates in `T_n`. The source fixed-coordinate ratio (2.4) gives

\[
\mathbb E(N_n^Y)_{K+1}
=(1+o(1))(n)_{K+1}a_n^{K+1}
\le(1+o(1))D^{K+1},
\tag{5.3}
\]

so

\[
\limsup_n\mathbb P(N_n^Y>K)
\le\frac{D^{K+1}}{(K+1)!}.
\tag{5.4}
\]

On the set `|nu|<=K`, (4.9) gives an `o(1)` contribution to the total-variation distance after summing over all configurations, because the relative error is uniform and their iid probabilities sum to at most one. Therefore

\[
\limsup_n
 d_{\rm TV}\bigl(
 \mathcal L(\eta_n\mid S_n=m),
 \mathcal L(\eta_n)
 \bigr)
\le
\frac{2D^{K+1}}{(K+1)!}.
\tag{5.5}
\]

Letting `K->infinity` proves

\[
\boxed{
 d_{\rm TV}\bigl(
 \mathcal L(\eta_n\mid S_n=m),
 \mathcal L(\eta_n)
 \bigr)\to0.
}
\tag{5.6}
\]

for every fixed bounded-intensity high cloud `T_n` of the form (3.1)–(3.2).

This proof contains no Janossy inversion and no partition of the value axis.

---

## 6. Reconstructing the top `r` order statistics

Fix `r` and `D>=2r`. Define

\[
\Lambda_n(h):=n\,\mathbb P(Z_{n,1}\ge h),
\tag{6.1}
\]

and let

\[
h_n:=\min\{h:\Lambda_n(h)\le D\}.
\tag{6.2}
\]

The cutoff (2.3) guarantees existence with `h_n<=U_n+1`; since the source support is unbounded (`omega=infinity`) and `p_n=>p` locally, `h_n->infinity`. Minimality gives

\[
\Lambda_n(h_n-1)>D.
\tag{6.3}
\]

Take the cloud band

\[
T_n=\{h_n,h_n+1,\ldots,U_n\}.
\tag{6.4}
\]

Its intensity is at most `D`, so (5.6) applies.

Let `Phi_{n,r}` list the `r` largest cloud atoms with multiplicity and, when fewer than `r` cloud atoms exist, pad every missing coordinate by `h_n-1`.

On

\[
G_n^Y:=\{Y_{(1)}\le U_n,\ Y_{(r)}\ge h_n-1\}
\tag{6.5}
\]

we have exactly

\[
(Y_{(1)},\ldots,Y_{(r)})
=\Phi_{n,r}(\eta_n^Y),
\tag{6.6}
\]

and analogously for the iid vector. This remains true through arbitrary ties and arbitrarily large mass at the boundary `h_n-1`.

Under the iid law, the number of observations at least `h_n-1` is binomial with mean greater than `D`. Since `D>=2r`, Chernoff gives

\[
\mathbb P(Z_{n,(r)}<h_n-1)\le e^{-D/8}.
\tag{6.7}
\]

Theorem 19.7(v) gives `d_K(Y_(r),Z_{n,(r)})->0`, hence

\[
\mathbb P(Y_{(r)}<h_n-1)
\le e^{-D/8}+o(1).
\tag{6.8}
\]

The upper-cutoff failures are `o(1)` by (2.3). Since total variation contracts under deterministic maps, (5.6), (6.6), and the triangle inequality yield

\[
\limsup_{n\to\infty}
 d_{\rm TV}\!\left(
 (Y_{(1)},\ldots,Y_{(r)}),
 (Z_{n,(1)},\ldots,Z_{n,(r)})
 \right)
\le2e^{-D/8}.
\tag{6.9}
\]

Let `D->infinity`. This proves (1.2) for the main fixed-law regime and the arbitrary-rate tuned regime. ∎

---

## 7. Returning from `xi^(n)` to fixed `xi` in the weakened-rate regime

Assume `lambda<nu` and

\[
m/n=\lambda+o(1/\log n).
\tag{7.1}
\]

The argument above first proves joint TV between the conditioned allocation and the top-`r` vector from `xi^(n)`.

Janson's equation (19.46) gives

\[
p_n(k)=(1+o(1))p(k)
\tag{7.2}
\]

uniformly for `k<=U_n=O(log n)`, and both laws have tail `o(1/n)` beyond `U_n`.

Choose the adaptive threshold using the fixed law `p`:

\[
h_n:=\min\{h:nP(\xi\ge h)\le D\}.
\tag{7.3}
\]

On the cloud band `[h_n,U_n]`, (7.2) and the negligible upper tails imply

\[
n\sum_{k=h_n}^{U_n}|p_n(k)-p(k)|=o(1).
\tag{7.4}
\]

Hence one can maximally couple `n` iid `p_n` variables and `n` iid `p` variables so that their restricted cloud point processes agree with probability `1-o(1)` (a union bound over the per-coordinate coupling error in the cloud category suffices).

At the boundary `h_n-1`, the fixed-law expected count is greater than `D`; (7.2) gives the same lower bound up to `1+o(1)` for the tuned sample. Thus each sample has at least `r` observations at or above `h_n-1` except with probability `O(e^{-cD})`. Padding as in Section 6 therefore yields

\[
\limsup_n d_{\rm TV}\!\left(
(\xi^{(n)}_{(1)},\ldots,\xi^{(n)}_{(r)}),
(\xi_{(1)},\ldots,\xi_{(r)})
\right)
\le C e^{-cD}.
\tag{7.5}
\]

Let `D->infinity`, and combine with the tuned comparison. This proves (1.2) in the source's weakened fixed-law regime as well. ∎

---

## 8. Why this route survives the obvious attacks

**Parity/lattice effects.** The argument compares exact lattice local probabilities under the conditioned sum; it never infers TV from Kolmogorov convergence alone. The source span is explicitly retained by the complement law.

**Large boundary atoms.** The cloud begins one level above the padding value. A huge atom at `h_n-1` helps rather than hurts: it makes the boundary-underflow event even smaller.

**Ties.** The cloud is a counting measure with multiplicity; no distinctness assumption occurs.

**Moving cutoff.** The rare cloud is contained below the source cutoff `U_n`, while all failures above `U_n` are absorbed in the single global `o(1)` event from Theorem 19.7.

**Tuned triangular array.** The complement law remains uniformly square-integrable (indeed uniformly exponentially integrable in the source's `lambda<nu` regime), converges to the same limit law, has the same eventual span, and differs in mean by only `O(U_n/n)`. Thus the source's Lemma 14.1/Remark 14.2 applies without a stronger third-moment hypothesis.

---

## 9. Relation to the older archived joint proof

The older campaign handoff says `JansonJointTV_author_proof.md` proves joint top-`J` TV using rare-cloud Janossy/Bonferroni inversion and that repeated values/combinatorial factors were independently checked. That older local file was not directly available as a repository path in this run, so this artifact does not claim a line-by-line comparison.

What is new in the present route is the **conditioning likelihood ratio** (4.3)–(4.9): given the entire bounded rare cloud, the remaining coordinates are iid from the complement law, and a triangular-array local CLT makes the global-sum conditioning asymptotically invisible. Janossy inversion is unnecessary.

This is therefore an independent route to the same stronger theorem, not merely another certificate for the preceding interval proof.

---

## 10. Status and audit targets

The fixed source metric remains

\[
\boxed{M_{\rm TV}:1\to1,}
\]

because it is binary and had already moved on the preceding R19 run. The stronger theorem is mathematical progress but not metric movement.

No finite checker is appropriate: this is an analytic asymptotic theorem with no finite computational core. The proof itself exposes the exact audit points.

Two independent outside-track audits are still required before closure. They should attack:

1. the exact cloud-conditioning identity (4.2);
2. uniform applicability of Lemma 14.1/Remark 14.2 to the complement laws `p_n^c`, especially eventual span and uniform square integrability;
3. the uniformity in `|nu|<=K` in (4.6);
4. the conditioned cloud tail bound (5.3);
5. the boundary-padding reconstruction and the `xi^(n)->xi` return step.

No self-check here is counted as an audit.
