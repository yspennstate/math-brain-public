Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — removing Huang's sparse finite-field class improves the cubic exponent to 1/8

Date: 2026-09-18 UTC.  
Target: Van Vu, *Recent progress in combinatorial random matrix theory* (2020), Section 5 immediately after Theorem 5.2.  
Primary technical source reused: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465v2 (2018), Section 4.  
Frozen R7-07 metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ is singular})\le n^{-a+o(1)}\}.
\]

Previous evidenced value: `a_3 >= 1/9`.  
New proved-candidate value in this artifact: **`a_3 >= 1/8`**.

Methods this iteration: **B15 BREAK THE SYMMETRY ON PURPOSE / B24 FIND THE EXTREMAL OBJECT / B5 ADD A PARAMETER AND DIFFERENTIATE IN IT**. The immediately preceding R7-07 triple was B14/B27/B10.

## 1. Idea before code

Huang's undirected finite-field proof has two numerically different restrictions on the auxiliary prime `p`.

1. The equidistributed local-CLT calculation is valid for
   \[
   p\ll n^{1/8},
   \]
   with relative error `O(p^4 (log n)^(3/2)/sqrt(n))`.
2. His final non-equidistributed estimate is stated only for
   \[
   p\ll n^{(d-2)/(5d-6)}.
   \]
   In the cubic case this is `p << n^(1/9)` and is exactly what produces the currently tracked `1/9` singularity exponent.

Inspecting Section 4.2 shows that the `1/9` restriction comes from one very special non-equidistributed class: vectors with only

\[
r=n-n_0(M)\le \mathfrak b p^3\log n/d
\]

nonzero coordinates. Huang counts these vectors value-by-value and obtains an `O(p^(2d))/n^(d-2)` contribution. But R7-07's preceding theorem already controls the **existence** of every kernel vector with support between 3 and a fixed linear fraction of `n`, uniformly over the coefficient field. Support two is exactly the twin obstruction in a simple regular graph.

So instead of paying Huang's `p^(2d)` multiplicity factor for this sparse class, remove the class from the finite-field first moment and bound its existence directly by support geometry. The other Huang classes remain valid all the way to the local-CLT scale `p << n^(1/8)`.

That sieve moves the cubic exponent from `1/9` to `1/8`.

## 2. Recovered Huang interfaces, with no strengthening hidden in the citation

The following are the only published interfaces used.

### 2.1 Equidistributed class

Huang Proposition 4.1 states, for fixed `d>=3`, prime `p` with `gcd(p,d)=1`, and `p << n^(1/8)`, that the normalized total number of finite-field null vectors belonging to the equidistributed class is

\[
1+\mathbf 1_{p=2}+O\!\left(\frac{p^4(\log n)^{3/2}}{\sqrt n}\right).
\]

We will take `p` odd. Therefore this contribution is `1+o(1)`.

### 2.2 Non-equidistributed classes other than the sparse class

In the proof of Proposition 4.2, Huang separates the non-equidistributed terms near the zero-dominant corner into several regimes. The second near-corner regime has total contribution

\[
\exp\{-\mathfrak b c(\varepsilon)p^2\log n+O(p^2\log n)\}=o(n^{-(d-2)})
\]

once `\mathfrak b` is sufficiently large. The far class has contribution

\[
\exp\{-c(\delta)n/p^2+O(p^2\log n)\}.
\]

For `p << n^(1/8)` this is superpolynomially smaller than `n^{-(d-2)}`. The remaining near-equidistributed non-equidistributed regime is likewise exponentially small in `p^2 log n`; its proof does not invoke the later `p << n^{(d-2)/(5d-6)}` restriction.

### 2.3 The unique source of the old cubic `1/9` restriction

For Huang's third class he defines

\[
r=n-n_0(M)
\]

and explicitly sums over

\[
2\le r\le \mathfrak b p^3\log n/d.
\]

His equation (4.43) bounds the total contribution by

\[
\frac{O(p^{2d})}{n^{d-2}},
\]

and the very next line imposes

\[
p\ll n^{(d-2)/(5d-6)}.
\]

For `d=3` this is `p << n^(1/9)`. Thus this sparse class, not the local CLT, is the step responsible for the tracked `1/9` barrier.

Nothing below invokes Huang Proposition 4.2 wholesale outside its published hypotheses. We reuse its class-by-class estimates only where their displayed derivations remain valid at `p << n^(1/8)`.

## 3. Field-independent support obstruction

We restate the preceding R7-07 support lemma because it is the bridge between real and finite-field kernel vectors.

### Lemma 3.1 — every kernel support is unique-neighbour-bad over every field

Let `G` be a finite simple graph, let `K` be any field, and suppose `0 != x in K^{V(G)}` satisfies `A(G)x=0`. Put

\[
S=\operatorname{supp}x.
\]

Then no vertex in `V(G)\S` has exactly one neighbour in `S`.

#### Proof

If `v notin S` had exactly one neighbour `u in S`, then the `v`-th row equation would be

\[
0=(Ax)_v=\sum_{w\sim v}x_w=x_u,
\]

because every other neighbour lies outside `S` and hence has coordinate zero. This contradicts `u in supp x`. No property of `K` was used. QED.

### Theorem 3.2 — preceding R7-07 linear-support suppression

For every fixed `d>=3` there is a constant `delta_d>0` such that a uniformly random simple `d`-regular graph obeys

\[
\Pr\!\left(\exists K,\ 0\ne x\in K^n:\ A x=0,\ 3\le |\operatorname{supp}x|\le \delta_d n\right)
=o(n^{2-d}),
\]

provided `K` is any one prescribed field (in particular `F_p`, even when `p=p_n` varies with `n`).

The proof in the preceding artifact actually bounds the field-free event that there exists a vertex set `S` of such a size with no outside unique neighbour. Hence it is uniform in `K` and in `p`; no union over fields is being taken here.

For completeness, the field-free estimate obtained there is

\[
\Pr(U_k)\le dk\left[K_d\left(\frac{k}{n}\right)^{d/2-1}\right]^k,
\]

and summing `3<=k<=delta_d n` gives `o(n^{2-d})`.

## 4. Support two is exactly the twin mechanism in the simple model

### Lemma 4.1

Let `G` be a simple `d`-regular graph and let `K` be a field. If `p=char(K)` does not divide `d`, then a nonzero kernel vector supported on exactly two vertices `u,v` forces `u,v` to be nonadjacent twins; conversely nonadjacent twins give the kernel vector `e_u-e_v` over every field.

#### Proof

Write the two nonzero coordinates as `a,b`. The row equation at `u` is `b` if `u~v` and zero otherwise, so `u` and `v` cannot be adjacent. For any `w notin {u,v}`, the row equation is one of `0,a,b,a+b` according to whether `w` sees neither, only `u`, only `v`, or both. Since `a,b` are nonzero, no outside vertex can see exactly one of the pair. Regularity then gives identical neighbourhoods. For a common neighbour, the row equation gives `a+b=0`; hence the kernel line is generated by `e_u-e_v`. The converse is immediate. QED.

(The condition `p\nmid d` is not actually needed for this two-support argument, but it is already part of Huang's finite-field setup.)

### Lemma 4.2 — twin probability at the source scale

For fixed `d`, in a uniformly random simple `d`-regular graph,

\[
\Pr(\text{there is a nonadjacent twin pair})=O(n^{2-d}).
\]

#### Proof

For each fixed ordered or unordered pair, exposing one vertex's `d` neighbours first, the probability that the other vertex has exactly the same `d`-set is `O(n^{-d})` for fixed `d`; the simple-configuration switching/counting constants are uniform. Union over `O(n^2)` pairs gives `O(n^{2-d})`. QED.

This upper bound is enough for the new exponent. No Poisson asymptotic or sharp twin constant is used.

## 5. B15 — sieve out Huang's sparse third class as an event

Let `p` be an odd prime with `p\nmid d`, and consider a uniformly random **simple** `d`-regular graph. Let `E_sp(p)` be the event that there exists a nonzero `F_p` kernel vector in Huang's third non-equidistributed class. Huang's parameter in that class is exactly

\[
r=n-n_0(M)=|\operatorname{supp}x|,
\]

and his summation range is

\[
2\le r\le R_n:=\mathfrak b p^3\log n/d.
\]

Assume

\[
p\ll n^{1/8}.
\]

Then

\[
R_n=O(p^3\log n)=n^{3/8+o(1)}=o(n),
\]

so for all sufficiently large `n`, `R_n<=delta_d n`.

Split according to support size.

* `r=2`: Lemmas 4.1–4.2 give probability `O(n^{2-d})`.
* `3<=r<=R_n`: Theorem 3.2 gives probability `o(n^{2-d})`.

Therefore

\[
\boxed{\Pr(E_{sp}(p))=O(n^{2-d})}
\]

uniformly for `p << n^(1/8)`.

This is the key replacement for Huang's vector-count estimate `O(p^(2d)) n^{2-d}`. We need only the probability that this sparse obstruction occurs, not the number of its scalar multiples and residue assignments.

## 6. Non-sparse finite-field null vectors have bounded expected count at p << n^(1/8)

Huang works first in the undirected configuration model. Let `Simple` be the event that the pairing gives a simple graph. For fixed `d`,

\[
\Pr_{conf}(Simple)\to c_d>0.
\]

Let `N_ns(G)` denote the number of nonzero `F_p` kernel vectors **not** belonging to Huang's sparse third class.

From the published class-by-class bounds in Section 4:

1. Proposition 4.1 contributes `1+o(1)` for odd `p << n^(1/8)`;
2. non-equidistributed classes 1, 2 and 4 have total contribution `o(1)` in the same range, by their displayed exponential estimates.

Hence

\[
\mathbb E_{conf}N_{ns}=O_d(1).
\]

We do not need the limiting constant. Conditioning on simplicity gives

\[
\mathbb E[N_{ns}\mid Simple]
\le \frac{\mathbb E_{conf}N_{ns}}{\Pr_{conf}(Simple)}
=O_d(1).
\]

This conditioning step is why no claim about two-support vectors in configuration multigraphs is needed.

## 7. Finite-field singularity after the sparse sieve

On a simple graph outside `E_sp(p)`, if `A` is singular over `F_p`, then its nonzero kernel has at least `p-1` vectors and **none** is in the sparse class. Therefore

\[
(p-1)\mathbf 1_{\{A\text{ singular over }F_p\}\cap E_{sp}(p)^c}\le N_{ns}(G).
\]

Taking expectations under the uniform simple graph law,

\[
\Pr(A\text{ singular over }F_p)
\le \Pr(E_{sp}(p))+\frac{\mathbb E[N_{ns}\mid Simple]}{p-1}.
\]

Using Sections 5–6,

\[
\boxed{
\Pr(A\text{ singular over }F_p)
\le O(n^{2-d})+O_d(p^{-1})
}
\]

for every odd prime `p\nmid d` with `p<<n^(1/8)`.

Finally, the adjacency matrix has integer entries. If it is singular over `R`, its determinant is the integer zero, hence it is singular modulo every prime. Thus

\[
\boxed{
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O(n^{2-d})+O_d(p^{-1}).
}
\]

## 8. B5 — optimize the finite-field scale

Parameterize

\[
p=n^{\theta}/L(n),
\]

where `L(n)->infinity` slowly.

After the sparse-class sieve, the relevant constraints are:

* equidistributed local CLT: `theta < 1/8` (at the endpoint use a slowly varying loss), because its relative error is `p^4(log n)^(3/2)/sqrt(n)`;
* sparse support range is still sublinear whenever `theta<1/3`;
* Huang's far large-deviation class is negligible throughout `theta<1/4`;
* the other near-corner classes are exponentially small in `p^2 log n`.

Hence the first active barrier is now the local CLT at `theta=1/8`, not the sparse class at `theta=1/9`.

Take

\[
x_n=\frac{n^{1/8}}{(\log n)^2}.
\]

By Bertrand's postulate, for large `n` there is a prime `p_n in [x_n,2x_n]`. Since `d` is fixed, eventually `p_n>d` and therefore `p_n\nmid d`. Also

\[
p_n\ll n^{1/8},\qquad p_n=n^{1/8-o(1)}.
\]

Consequently

\[
\Pr(A_{n,d}\text{ singular})
\le O(n^{2-d})+n^{-1/8+o(1)}.
\]

For `d=3`, this gives the promised metric movement:

\[
\boxed{
\Pr(A_{n,3}\text{ singular})\le n^{-1/8+o(1)},
\qquad a_3\ge\frac18.
}
\]

The previous supported exponent was `1/9`, so this is a strict source-matching improvement.

## 9. B24 — what the extremal sparse object says

Huang's third class was the only class whose vector-count estimate forced `p<<n^(1/9)` in the cubic case. The support theorem shows that, at the source polynomial scale, its only surviving sparse geometry is support two, i.e. a twin pair. The p-dependent `p^(2d)` factor in (4.43) therefore reflects the cost of counting many finite-field labels rather than a p-dependent family of genuinely likely singular graphs.

This does **not** show twins are the only singularity mechanism overall. It says only that every other source-scale mechanism must use a kernel vector of support greater than `delta_d n`, exactly as established in the preceding run.

## 10. What failed / what remains

1. **This does not solve Vu's source problem.** For cubic graphs the conjectured exponent is `1`, while this run reaches only `1/8`.
2. The new active analytic bottleneck is Huang Proposition 4.1. Its undirected local-CLT error is
   \[
   O\!\left(p^4(\log n)^{3/2}/\sqrt n\right),
   \]
   which becomes non-negligible beyond the `n^(1/8)` scale.
3. Destroying one kernel certificate by switchings is still not equivalent to increasing rank; this run deliberately avoided that stalled route.
4. Nguyen–Pan's `n^{-1/3+o(1)}` improvement is for the **directed** fixed-degree model. It is a technique source, not a transferable theorem for F0003.
5. A bounded 2026-09-18 literature search did not reveal the sharp `d-2` exponent for the undirected fixed-degree model or this exact sparse-class sieve. That is negative evidence only. Publication novelty is **UNVERIFIED**.

## 11. Next attack

The next nonrepeating triple should attack the now-isolated `1/8` bottleneck rather than return to sparse support counting:

* **B21 — import the analogous-field technique:** dissect Nguyen–Pan's inverse-Kneser/characteristic-function improvement and identify the first step that truly uses directed row independence.
* **B7 — take the limit:** expand Huang's undirected characteristic function one order further and determine whether symmetry cancels the cubic term enough to replace the crude `p^4/sqrt(n)` error.
* **B30 — localize the gluing failure:** isolate one residue block / one pairing constraint and seek a conditional local CLT whose errors tensorize without paying the full `p^4` dimensional factor.

No new checker is warranted yet: the movement here is theorem-sized and is supplied by a written proof plus literal source-equation verification rather than a finite arithmetic certificate.
