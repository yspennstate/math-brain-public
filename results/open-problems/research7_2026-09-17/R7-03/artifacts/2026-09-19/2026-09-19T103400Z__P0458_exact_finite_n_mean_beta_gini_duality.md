Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# P0458 — exact finite-`n` mean degree via a Beta Gini identity, complement duality, and the sharp mean-asymptotic boundary

Canonical target: `P0458`, Dabirian–Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), §1.1 first additional question. The source asks for the limiting law of the standardized degree `(D-E[D])/sqrt(Var(D))`; this target was already solved at source scope in the preceding R7-03 runs. This artifact is a proof-hardening result: it computes `E[D]` **exactly for every finite `n,k`**, exposes a `k <-> n-1-k` complement duality of the deficit, and extends the source's three-term mean expansion from `k=o(n^(1/3))` to the sharp natural range `k=o(sqrt(n))` for that uncorrected expansion.

Source URL checked 2026-09-19:

- https://www.cambridge.org/core/journals/journal-of-applied-probability/article/connectivity-of-a-family-of-bilateral-preference-random-graphs/0A1D5D7560AB2DC6C8255F1522DC3BB2

The source's Theorem 7 gives an asymptotic mean for `k=o(sqrt(n))`; Theorem 8 gives the three-term expansion only under `k=o(n^(1/3))`. The exact identity below is not stated there.

Methods in this run:

- **B5 — INTRODUCE A PARAMETER:** use the complement budget `r=n-1-k` symmetrically with `k` and retain it through the exact finite-`n` calculation;
- **B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** identify the mean degree deficit with one half of the Gini mean difference of a `Beta(k,r)` order statistic;
- **B26 — HUNT THE SPORADIC CASES:** resolve the extreme dense complements `r=1,2,3`, the sparse extreme `k=1`, and the balanced center, then use them to expose an exact complement symmetry and unimodality law.

These are different from the immediately preceding P0458 triple B18/B3/B16.

---

## 1. Model and notation

Work with the equivalent low-weight convention. To every undirected edge `{i,j}` of `K_n` attach an independent `U_{ij}=U_{ji} ~ Uniform(0,1)`. Each vertex proposes the `k` incident edges of **smallest** weight. An edge survives in `LK(n,k)` iff both endpoints propose it.

Fix a root `0`, and let `D=D_{n,k}` be its degree. Put

\[
 r:=n-1-k,
 \qquad m:=n-1=k+r.
\]

Thus every vertex proposes `k` incident edges and rejects exactly the `r` largest incident edges. We assume throughout the nondegenerate range

\[
 1\le k\le n-2,
 \qquad 1\le r\le n-2.
\]

Define the deficit

\[
 H:=k-D.
\]

It counts root-proposed edges that are rejected by the opposite endpoint.

---

## 2. B17: exact one-edge reduction to a Beta Gini mean difference

Fix a candidate edge `e={0,i}` and write `U=U_{0i}`. Remove `e` from the incident edge sets at its endpoints. There remain

\[
 N:=n-2
\]

other edges at the root and `N` other edges at `i`.

Let `T_0` be the `r`th largest weight among the `N` other root edges, and let `T_i` be the `r`th largest weight among the `N` other edges incident to `i`.

The two collections of edges used to define `T_0` and `T_i` are disjoint: they are respectively

\[
 \{\{0,j\}:j\notin\{0,i\}\}
 \quad\text{and}\quad
 \{\{i,j\}:j\notin\{0,i\}\}.
\]

Hence `T_0` and `T_i` are independent. They are also independent of `U`.

Because a vertex rejects exactly its `r` largest edges,

- the root proposes `e` iff at least `r` of its other incident edges exceed `U`, equivalently `U<T_0`;
- endpoint `i` rejects `e` iff at most `r-1` of its other incident edges exceed `U`, equivalently `U>T_i`.

Therefore

\[
 \{e\text{ contributes to }H\}=\{T_i<U<T_0\}.
\]

Conditioning on `(T_0,T_i)` and using that `U` is uniform gives

\[
 \mathbb P(e\text{ contributes to }H\mid T_0,T_i)
 =(T_0-T_i)_+.
\]

Since `T_0,T_i` are iid,

\[
 \mathbb E[(T_0-T_i)_+]
 =\frac12\mathbb E|T_0-T_i|.
\tag{2.1}
\]

Now `T_0` is the `r`th largest among `N=n-2` uniforms, hence the `N-r+1=k`th smallest. Therefore

\[
 T_0,T_i\stackrel{\rm iid}{\sim}\operatorname{Beta}(k,r).
\tag{2.2}
\]

Summing the identical one-edge contributions over all `n-1=m` neighbors yields the structural identity

\[
 \boxed{
 \mathbb EH
 =\frac{m}{2}\,\mathbb E|X-Y|,
 \qquad X,Y\stackrel{\rm iid}{\sim}\operatorname{Beta}(k,r).
 }
\tag{2.3}
\]

Thus the finite-graph mean deficit is exactly a scaled **Gini mean difference** of a beta law.

The standard beta Gini identity is

\[
 \mathbb E|X-Y|
 =\frac{4}{k+r}
 \frac{B(k+r,k+r)}{B(k,k)B(r,r)}.
\tag{2.4}
\]

Since `m=k+r`, inserting (2.4) into (2.3) cancels `m` completely.

---

## 3. Exact finite-`n` mean theorem

### Theorem 3.1

For every `n>=3` and every `1<=k<=n-2`, with `r=n-1-k`,

\[
 \boxed{
 k-\mathbb E D_{n,k}
 =\mathbb EH
 =\frac{2B(n-1,n-1)}{B(k,k)B(r,r)}.
 }
\tag{3.1}
\]

Equivalently,

\[
 \boxed{
 \mathbb E D_{n,k}
 =k-
 \frac{2(n-2)!^2(2k-1)!(2r-1)!}
 {(2n-3)!(k-1)!^2(r-1)!^2}.
 }
\tag{3.2}
\]

A particularly transparent central-binomial form is

\[
 \boxed{
 \delta_{n,k}:=k-\mathbb ED_{n,k}
 =\frac{kr}{k+r}
 \frac{\binom{2k}{k}\binom{2r}{r}}
 {\binom{2(k+r)}{k+r}}.
 }
\tag{3.3}
\]

#### Proof

Equation (2.3) was derived directly from the graph construction, without approximation or independence assumptions between different root-neighbor survival indicators. Equation (2.4), the beta Gini mean-difference identity, gives

\[
 \mathbb EH
 =\frac{k+r}{2}\cdot
 \frac{4}{k+r}
 \frac{B(k+r,k+r)}{B(k,k)B(r,r)},
\]

which is (3.1). For positive integers,

\[
 B(a,a)=\frac{(a-1)!^2}{(2a-1)!},
\]

which gives (3.2). Finally

\[
 B(a,a)=\frac{2}{a\binom{2a}{a}},
\]

and substitution in (3.1) gives (3.3). Since `H=k-D`, the degree formula follows. ∎

### Independent exact finite-sum representation

The theorem can also be checked without using (2.4). If `q=1-U`, then conditional on `q`, the counts of other endpoint edges exceeding `U` are independent `Bin(N,q)` variables. Hence for one candidate edge

\[
 p_{n,k}
 =\int_0^1
 \Pr\{\operatorname{Bin}(N,q)\ge r\}
 \Pr\{\operatorname{Bin}(N,q)\le r-1\}\,dq,
\]

and

\[
 \mathbb EH=(n-1)p_{n,k}.
\tag{3.4}
\]

Expanding the binomial probabilities gives the exact rational double sum

\[
 \mathbb EH
 =(n-1)
 \sum_{a=r}^{N}\sum_{b=0}^{r-1}
 \binom Na\binom Nb
 B(a+b+1,2N-a-b+1).
\tag{3.5}
\]

The archived rational checker verifies that (3.5), (3.1), and (3.3) agree identically for all `741` pairs `(n,k)` with `3<=n<=40`, `1<=k<=n-2`.

---

## 4. B5: an exact complement duality and unimodality theorem

Formula (3.3) is symmetric under interchange of `k` and `r=n-1-k`. Therefore

\[
 \boxed{
 \delta_{n,k}=\delta_{n,n-1-k}.
 }
\tag{4.1}
\]

This is an exact finite-`n` duality for the **degree deficit**, even though the degrees themselves differ by the deterministic proposal budgets. Equivalently,

\[
 \boxed{
 \mathbb ED_{n,k}-\mathbb ED_{n,r}=k-r,
 \qquad r=n-1-k.
 }
\tag{4.2}
\]

There is also an exact adjacent-ratio formula. Holding `n` fixed and replacing `(k,r)` by `(k+1,r-1)`,

\[
 \boxed{
 \frac{\delta_{n,k+1}}{\delta_{n,k}}
 =\frac{(2k+1)(r-1)}{k(2r-1)}.
 }
\tag{4.3}
\]

Indeed this follows immediately from the factorial form (3.2). Subtracting numerator and denominator in the comparison with `1`,

\[
 (2k+1)(r-1)-k(2r-1)=r-k-1.
\]

Consequently:

- if `r>k+1`, then `delta_{n,k+1}>delta_{n,k}`;
- if `r=k+1`, the two neighboring deficits are equal;
- if `r<k+1`, the deficit decreases.

Thus the deficit is exactly symmetric and unimodal in the proposal budget. It is maximized at the balanced complement point:

- if `n-1` is even, uniquely at `k=r=(n-1)/2`;
- if `n-1` is odd, at the two central values `k=(n-2)/2` and `k=n/2` (integers interpreted as the two adjacent central budgets).

No asymptotics are used in this statement.

---

## 5. B26: dense sporadic complements `r=1,2,3`

Write `N=n-2`. For fixed complement `r`, (3.1) can be reorganized as

\[
 \boxed{
 \delta_{n,n-1-r}
 =\mu_r
 \frac{\Gamma(N+1)\Gamma(N-r+3/2)}
 {\Gamma(N-r+1)\Gamma(N+3/2)},
 }
\tag{5.1}
\]

where

\[
 \mu_r
 =r\frac{\binom{2r}{r}}{4^r}
 =\frac{\Gamma(r+1/2)}{\sqrt\pi\,\Gamma(r)}.
\tag{5.2}
\]

Equivalently,

\[
 \delta_{n,n-1-r}
 =\mu_r\,
 \frac{2^r N^{\underline r}}
 {\prod_{j=0}^{r-1}(2N+1-2j)}.
\tag{5.3}
\]

This gives the first dense boundaries explicitly:

### `r=1`

\[
 \boxed{
 \delta_{n,n-2}=\frac{n-2}{2n-3}.
 }
\tag{5.4}
\]

This exactly agrees with the independent all-factorial-moment derivation from the preceding R7-03 run.

### `r=2`

\[
 \boxed{
 \delta_{n,n-3}
 =\frac{3(n-2)(n-3)}{(2n-5)(2n-3)}.
 }
\tag{5.5}
\]

### `r=3`

\[
 \boxed{
 \delta_{n,n-4}
 =\frac{15}{2}
 \frac{(n-2)(n-3)(n-4)}
 {(2n-7)(2n-5)(2n-3)}.
 }
\tag{5.6}
\]

For every fixed `r`, (5.1) immediately yields

\[
 \boxed{
 \delta_{n,n-1-r}
 =\mu_r\left(1-\frac{r}{2(n-2)}+O_r(n^{-2})\right).
 }
\tag{5.7}
\]

The sparse extreme `k=1` follows from complement symmetry:

\[
 \delta_{n,1}=\delta_{n,n-2}=\frac{n-2}{2n-3},
\]

and because `D_{n,1}` is Bernoulli,

\[
 \mathbb ED_{n,1}=\frac{n-1}{2n-3}.
\tag{5.8}
\]

The complete-graph endpoint `k=n-1` has `r=0`, lies outside the beta formula, and is separately deterministic: `D=n-1`.

---

## 6. Interior two-parameter asymptotics

Let

\[
 m=n-1=k+r.
\]

From the standard central-binomial expansion

\[
 \binom{2a}{a}
 =\frac{4^a}{\sqrt{\pi a}}
 \left(1-\frac{1}{8a}+O(a^{-2})\right),
\]

formula (3.3) gives, whenever `k->infinity` and `r->infinity`,

\[
 \boxed{
 \delta_{n,k}
 =\sqrt{\frac{kr}{\pi(k+r)}}
 \left[
 1+\frac{1}{8(k+r)}-\frac{1}{8k}-\frac{1}{8r}
 +O\!\left(k^{-2}+r^{-2}\right)
 \right].
 }
\tag{6.1}
\]

In particular,

\[
 \boxed{
 k-\mathbb ED_{n,k}
 \sim\sqrt{\frac{kr}{\pi(k+r)}}.
 }
\tag{6.2}
\]

This exact finite-`n` route independently explains the mean scaling used in the earlier P0458 interior fluctuation theorem.

---

## 7. Sharp extension of the source's Theorem-8 mean expansion

Suppose

\[
 k\to\infty,
 \qquad k=o(\sqrt n).
\]

Then `r=n-1-k` and `m=n-1`, so

\[
 \sqrt{\frac{kr}{m}}
 =\sqrt{k}\left(1-\frac{k}{2m}+O(k^2/m^2)\right).
\]

Also

\[
 \frac1{8m}-\frac1{8r}=O(k/m^2).
\]

Combining these with (6.1) gives

\[
 \delta_{n,k}
 =\sqrt{\frac{k}{\pi}}
 \left(
 1-\frac1{8k}-\frac{k}{2(n-1)}
 +O\!\left(k^{-2}+k^2/n^2+1/n\right)
 \right).
\tag{7.1}
\]

The finite-population correction has absolute size

\[
 \asymp \frac{k^{3/2}}{n}.
\]

It is `o(k^{-1/2})` exactly when `k^2/n -> 0`, i.e. `k=o(sqrt n)`. Therefore throughout the full range

\[
 k\to\infty,
 \qquad k=o(\sqrt n),
\]

we obtain

\[
 \boxed{
 \mathbb ED_{n,k}
 =k-\sqrt{\frac{k}{\pi}}
 +\frac{1}{8\sqrt{\pi k}}
 +o(k^{-1/2}).
 }
\tag{7.2}
\]

The source states this three-term expansion under the stronger hypothesis `k=o(n^(1/3))`. The exact formula therefore extends the same expansion to `k=o(sqrt n)`.

Moreover, the condition is the natural boundary for retaining **that exact uncorrected three-term form**: at `k` of order `sqrt n`, the finite-population term `k^(3/2)/n` is itself of order `k^{-1/2}` and must be retained. Thus the exact formula identifies why `sqrt n` is the correct transition scale for the mean expansion.

This is a mean theorem, not a replacement for the source-level fluctuation result already proved in previous P0458 runs.

---

## 8. Relation to earlier P0458 work

The preceding R7-03 interior theorem used

\[
 s_n^2=\frac{k(n-k)}{n}
\]

and proved

\[
 \frac{k-D}{s_n}\Longrightarrow g(Z),
 \qquad g(z)=\phi(z)+z\Phi(z),
\]

when `k->infinity` and `n-k->infinity`. Since

\[
 \frac{kr}{k+r}
 =\frac{k(n-1-k)}{n-1}
 \sim \frac{k(n-k)}{n}
\]

in that regime, (6.2) matches the previously proved limiting mean `s_n/sqrt(pi)`.

For fixed complement `r`, (5.7) tends to `mu_r`, exactly the mean of the mixed-Poisson boundary variable `H_r` from the fixed-complement theorem. Thus one finite-`n` identity now connects all three previous asymptotic regimes:

1. fixed `k` (published EWT sparse regime),
2. `k,r->infinity` (R7-03 interior non-Gaussian law),
3. fixed `r` (R7-03 mixed-Poisson dense boundary).

The identity also gives the exact mean centering needed in any future independent audit of the standardized laws.

---

## 9. Exact checker and what it does not prove

The companion checker evaluates the independent beta-binomial sum (3.5) using Python `Fraction`, and compares it to both closed forms (3.1) and (3.3). It checks all `741` pairs `(n,k)` with `3<=n<=40`, verifies complement symmetry, and verifies the adjacent-ratio formula and its unimodality sign.

This is exact finite arithmetic and is useful evidence against an algebra/transcription error. It is **not** a substitute for the proof above and is **not** an independent P26/OTHER audit.

---

## 10. Literature boundary, checked 2026-09-19

The current Cambridge journal version still states in §1.1 that the standardized degree limit is open and that even the variance is hard because of the dependence structure. Its Theorem 7 gives only an asymptotic mean formula under `k=o(sqrt n)`, and Theorem 8 gives the displayed three-term expansion under `k=o(n^(1/3))`.

A bounded search on 2026-09-19 for the exact paper title, `LK(n,k)` degree distribution/variance, and later Dabirian/Subramanian bilateral-preference work recovered the final source and older EWT/fixed-`k` work, but no later paper giving this exact finite-`n` beta-Gini formula or the full P0458 regime classification. This is **negative evidence only** and does not certify novelty or worldwide openness.

The beta mean-absolute-difference formula itself is standard statistics; it is not claimed as new. The potentially new contribution here is its exact identification with the finite `LK(n,k)` degree deficit and the consequences (3.1)–(7.2).

---

## 11. Status

Frozen P0458 source metric remains

\[
 R_{\rm unresolved}=0.
\]

This artifact therefore makes **no numerical movement** in the source metric. It materially hardens the solved source package by providing exact centering for every finite parameter pair and a sharper source-mean theorem.

Mathematical P0458 source status remains **PROVED** internally. Protocol status remains **NOT CLOSED** until an actual P26 full-proof PASS and one distinct OTHER-track full-proof PASS exist for the P0458 package.
