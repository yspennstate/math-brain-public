Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector/receipt, so I do not claim otherwise. **F0057 adversarial recovery self-check; fixed metric `M_TV: 1 -> 1`; methods #15 BREAK THE SYMMETRY, #26 HUNT THE SPORADIC CASE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# F0057 — adversarial stress test of the weak fixed-law transfer

## Scope

This artifact executes the `REFUTE INSTEAD OF PROVE` recovery selected in the preceding R19 stuck report. It does **not** claim an independent audit and it does **not** add a new source case. Its only purpose is to attack the most audit-sensitive branch of the existing F0057 proof candidate:

- fixed rank `j=2` (the proof below in fact works for every fixed `j`);
- `lambda < nu`;
- the weak fixed-law regime
  \[
  m/n=\lambda+o(1/\log n);
  \]
- arbitrary lattice span, including `d>1`;
- ties / repeated atoms;
- moving, `n`-dependent subsets of the extreme tail, including the total-variation positive set.

The conclusion of the stress test is **NO SOURCE-VALID FAILURE FOUND**. More strongly, the exact estimates printed in Janson's source yield a short transfer lemma that plugs the suspected interface directly. This is a self-check only; F0057 still requires two independent OTHER-track end-to-end audits.

Primary source: Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1 / Probability Surveys 9 (2012), Problem 18.10 in the arXiv numbering (Problem 19.10 in the published numbering).

---

## 1. What must be stress-tested

Let `p(k)=P(xi=k)` denote the fixed reference law after Janson's standard equivalent-weight normalization, so that `tau=1`, `Phi(1)=1` and `E xi=lambda`. Let

\[
\lambda_n:=m/n,\qquad \tau_n:=\Psi^{-1}(\lambda_n),
\]

and let the tuned law be

\[
p_n(k):=P(\xi^{(n)}=k)
=\frac{\tau_n^k}{\Phi(\tau_n)}w_k.
\tag{1.1}
\]

For `lambda<nu`, Janson proves the arbitrary-`m/n -> lambda` form of Theorem 18.7 with the tuned variables `xi^(n)`. In the weaker fixed-law regime

\[
\lambda_n=\lambda+o(1/\log n),
\tag{1.2}
\]

his displayed estimate (18.46) states that for the logarithmic cutoff `B_n=O(log n)`,

\[
\sup_{0\le k\le B_n,\ p(k)>0}
\left|\frac{p_n(k)}{p(k)}-1\right|\to0.
\tag{1.3}
\]

He also proves

\[
P(Y_{(1)}\ge B_n)\to0,
\qquad
P(\xi^{(n)}\ge B_n)=o(n^{-1}),
\qquad
P(\xi\ge B_n)=o(n^{-1}).
\tag{1.4}
\]

The suspected failure mode was that (1.3), although uniform pointwise, might be too weak to transfer the **moving-set**, higher-rank Poisson-count comparison used by the current R19 proof. The rest of this note attacks exactly that possibility.

---

## 2. Fixed-coordinate local ratios transfer uniformly

### Lemma 2.1 — weak fixed-law `q`-coordinate ratio

Fix `q>=1`. Uniformly over all supported

\[
0\le k_1,\ldots,k_q\le B_n,
\]

we have

\[
P(Y_1=k_1,\ldots,Y_q=k_q)
=(1+o(1))\prod_{i=1}^q p(k_i).
\tag{2.1}
\]

The error is uniform in the entire supported `q`-tuple.

### Proof

Conditioning iid tuned variables on their sum gives the exact identity

\[
P(Y_1=k_1,\ldots,Y_q=k_q)
=
\left(\prod_{i=1}^q p_n(k_i)\right)
\frac{P(S^{(n)}_{n-q}=m-s)}{P(S^{(n)}_n=m)},
\tag{2.2}
\]

where

\[
s=k_1+\cdots+k_q.
\]

By construction,

\[
E\xi^{(n)}=m/n.
\]

Hence the residual target differs from the residual mean by

\[
\begin{aligned}
(m-s)-(n-q)E\xi^{(n)}
&=(m-s)-(n-q)m/n\\
&=q\,m/n-s.
\end{aligned}
\tag{2.3}
\]

For fixed `q` and `k_i<=B_n=O(log n)`, the right side is `O(log n)=o(sqrt n)`, uniformly in the tuple. Janson's triangular-array lattice local CLT, together with Remark 13.2, therefore yields

\[
P(S^{(n)}_{n-q}=m-s)
=
\frac{d+o(1)}{\sqrt{2\pi\sigma^2(n-q)}},
\tag{2.4}
\]

uniformly over the supported tuple, while

\[
P(S^{(n)}_n=m)
=
\frac{d+o(1)}{\sqrt{2\pi\sigma^2 n}}.
\tag{2.5}
\]

Thus the ratio in (2.2) is `1+o(1)` uniformly. Finally (18.46), i.e. (1.3), gives for fixed `q`

\[
\prod_{i=1}^q p_n(k_i)
=(1+o(1))\prod_{i=1}^q p(k_i)
\tag{2.6}
\]

uniformly. Combining (2.2)--(2.6) proves (2.1). ∎

### Why the lattice does not break the argument

Exponential tilting changes probabilities but **not support**. Thus `p_n(k)>0` iff `p(k)>0`. If the common span is

\[
d=\gcd\{k:p(k)>0\},
\]

then every supported `k_i` is a multiple of `d`. On every admissible allocation subsequence, `m` is in the corresponding lattice class, so `m-s` remains in the admissible class for the `n-q` residual sum. The same lattice factor `d` occurs in numerator and denominator in (2.4)--(2.5) and cancels. There is therefore no hidden parity or span mismatch.

This directly stress-tests method #15: breaking aperiodicity does not break the proof.

---

## 3. Arbitrary moving tail sets inherit the same factorial moments

### Lemma 3.1 — moving-set fixed-law Poissonization input

Fix `r,q>=1`. For every `n`, let

\[
E_{1,n},\ldots,E_{r,n}\subseteq\{0,1,\ldots,B_n\}
\]

be pairwise disjoint **arbitrary moving sets**. Write

\[
N_{a,n}=\#\{i:Y_i\in E_{a,n}\}.
\]

For every fixed multi-index `(a_1,...,a_r)` with `a_1+...+a_r=q`,

\[
E\prod_{u=1}^r(N_{u,n})_{a_u}
=
(1+o(1))
\prod_{u=1}^r\left(nP(\xi\in E_{u,n})\right)^{a_u},
\tag{3.1}
\]

uniformly over all choices of the moving sets.

### Proof

Expand the left side over ordered `q`-tuples of distinct coordinate indices. Exchangeability reduces it to `(n)_q` times a sum of joint probabilities of the form on the left of (2.1). The whole summation domain lies under `B_n`, and Lemma 2.1 has a **uniform relative error**. Because all summands are nonnegative, that relative error may be pulled through the sum without any cardinality loss. The remaining sum factorizes into the fixed-law probabilities of the sets. Finally `(n)_q/n^q ->1`. ∎

### Corollary 3.2 — arbitrary moving count vectors

If, along a subsequence,

\[
nP(\xi\in E_{u,n})\to\theta_u<\infty,
\]

then

\[
(N_{1,n},\ldots,N_{r,n})
\Rightarrow
(\operatorname{Po}(\theta_1),\ldots,\operatorname{Po}(\theta_r))
\tag{3.2}
\]

with independent coordinates. The iid fixed-`xi` count vector has the same limit.

This is exactly the moving-set input used in the existing R19 rank-`j` count sandwich. In particular, the sets may depend on the TV-positive set

\[
S_n=\{k:P(Y_{(j)}=k)>P(\xi_{(j)}=k)\};
\]

no fixed-set assumption has entered.

---

## 4. The global cutoff transfers too

The tuned proof gives

\[
P(Y_{(1)}\ge B_n)\to0,
\qquad
nP(\xi^{(n)}\ge B_n)\to0.
\]

Janson's weak fixed-law transfer states in the same passage that also

\[
nP(\xi\ge B_n)\to0.
\tag{4.1}
\]

Therefore

\[
P\left(\max_{i\le n}\xi_i\ge B_n\right)
\le nP(\xi\ge B_n)\to0.
\tag{4.2}
\]

Consequently, truncating **every** moving set at the same cutoff changes every conditioned count event only on `{Y_(1)>=B_n}` and every iid count event only on `{max xi_i>=B_n}`. The truncation loss is one global `o(1)` on each side, not one error per point or per moving set.

Thus the old campaign gap `P30H-F001` does not reappear in the weak fixed-law branch.

---

## 5. Ties do not create a sporadic rank-two failure

The `j=2` order statistic can have ties. The R19 source proof never assumes otherwise: on an interval `J`, it records exact counts in three disjoint sets

\[
A_n=S_n\cap J,\qquad C_n=J\setminus S_n,\qquad B_n^+=(\max J,\infty).
\]

Rank membership is encoded by integer inequalities among

\[
N_{A_n},\ N_{C_n},\ N_{B_n^+},
\]

not by strict inequalities among sample values. Lemma 3.1 applies to these moving sets with atoms of any size. Hence repeated values and boundary ties are already part of the count event and create no exceptional `j=2` configuration.

This executes method #26: the plausible sporadic cases are lattice span, ties, and a moving positive set. None survives the exact count formulation.

---

## 6. An explicitly solvable periodic stress family

To make the parity issue concrete, take

\[
P(\xi=2r)=(1-a)a^r,\qquad r=0,1,2,\ldots,
\quad 0<a<1.
\tag{6.1}
\]

Then the support has span `d=2`, the law is unbounded, and

\[
\lambda=E\xi=\frac{2a}{1-a}<\nu=\infty.
\]

For admissible even `m`, conditioning on the sum has no parity ambiguity. The tuned law remains even-geometric:

\[
P(\xi^{(n)}=2r)=(1-b_n)b_n^r,
\tag{6.2}
\]

where

\[
b_n=\frac{m/n}{m/n+2}.
\tag{6.3}
\]

Under `m/n=lambda+o(1/log n)`, we have `b_n-a=o(1/log n)`. Hence for `r=O(log n)`,

\[
\frac{P(\xi^{(n)}=2r)}{P(\xi=2r)}
=\frac{1-b_n}{1-a}\left(\frac{b_n}{a}\right)^r
=1+o(1)
\tag{6.4}
\]

uniformly. This is an exact model of the source's (18.46) mechanism with nontrivial span and abundant ties. The attempted parity/tie counterexample therefore collapses to the same uniform transfer rather than breaking it.

No finite checker is required for (6.1)--(6.4): these are exact algebraic identities, not a finite enumeration claim.

---

## 7. Consequence for the existing F0057 proof candidate

The suspected weak-interface gap was:

> Could the source's one-point comparison (18.46) fail to transfer an `n`-dependent TV-positive set and higher-rank moving occupancy counts from `xi^(n)` back to fixed `xi`?

Lemmas 2.1 and 3.1 answer this stress question **no**. For every fixed number of exposed coordinates, the exact conditioned-sum formula plus the source local CLT gives a uniform joint ratio below the logarithmic cutoff. The uniform pointwise tuned/fixed ratio (18.46) then passes through arbitrary nonnegative sums over moving sets. The global tail cutoff passes as well. Nontrivial span and ties remain inside the exact formulas.

Thus the source-wide fixed-`j` proof candidate survives the weakest source branch tested here. This does **not** upgrade its protocol status:

- `M_TV` stays `1`;
- this artifact is a **SELF-CHECK**, not an independent audit;
- closure still requires two independent end-to-end audits by OTHER tracks;
- novelty remains unverified despite bounded current-literature searches.

---

## 8. Method outcomes

### #15 BREAK THE SYMMETRY ON PURPOSE

I forced a nontrivial lattice span (`d=2`) rather than silently using an aperiodic reference law. The residual-sum lattice class is preserved because tilting preserves support and exposed supported values are multiples of `d`. The local-CLT factor cancels. **No failure.**

### #26 HUNT THE SPORADIC CASE

I targeted `j=2`, ties, moving TV-positive sets, and the weak `o(1/log n)` fixed-law transfer. The rank event is count-based and the moving-set factorial moments inherit a uniform relative error. **No sporadic failure found.**

### #30 ONE SCALE / ONE DIRECTION AT A TIME

I isolated the only delicate scale: `k<=B_n=O(log n)`. On that scale, `tau_n-1=o(1/log n)` makes the exponential tilt uniformly invisible, while the residual-sum displacement is `O(log n)=o(sqrt n)`, exactly inside Remark 13.2. Above the cutoff both models have negligible maximum tails. **The two scales glue.**

---

## 9. Prior-art check, 2026-09-18 local date

Fresh searches used exact or near-exact combinations of:

- `"Problem 18.10" Janson total variation order statistics random allocations`;
- `"Problem 19.10" Janson total variation random allocations`;
- `"Does d_TV(Y_(j), xi_(j))" Janson`;
- `conditioned random allocations order statistics total variation Janson`;
- `random allocations total variation order statistics`.

The searches recovered Janson's source and unrelated/general order-statistic TV literature, including fixed-rank extreme-value work and 2026 induced-order-statistic rates, but no later primary theorem explicitly resolving this exact conditioned-allocation Problem 18.10/19.10 was located. This is **bounded negative evidence only**, not a novelty certificate.

---

## 10. Remaining obligation

The mathematical stress target chosen by the stuck report survived. The remaining closure obstruction is unchanged:

\[
\boxed{
\#\{\text{independent OTHER-track end-to-end PASS audits of R19/F0057}\}<2.
}
\]

R19 must not manufacture those audits. One further unchanged source-metric run would reach the six-unchanged CLOSABLE rotation threshold.
