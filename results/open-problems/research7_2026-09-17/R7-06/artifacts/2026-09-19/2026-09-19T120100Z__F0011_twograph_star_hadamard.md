Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — colored two-graph quotient, repeated-spectrum obstruction, and symmetric-Hadamard boundary family

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, Conjecture 9.4, integral spectrum of a symmetric Rademacher matrix.  
Methods: **B27 / B18 / B24**.

## 1. Setup and prior reduction

Let `M_n^sym` be the real symmetric `n x n` matrix whose upper-triangular entries, including the diagonal, are independent Rademacher signs.

Let `I_n` denote the number of representatives with integral spectrum after diagonal switching has normalized all first-row off-diagonal signs to `+1`. The previous R7-06 work proved

\[
\Pr(\operatorname{Spec}M_n^{\rm sym}\subset\mathbb Z)
=
\frac{I_n}{2^{n(n+1)/2-(n-1)}}.
\]

Hence Vu's conjecture is equivalent to

\[
I_n=2^{o(n^2)}. \tag{1.1}
\]

For an unordered integral spectrum `lambda`, let `F_n(lambda)` be the number of switching-normalized labeled matrices with that exact spectrum. Previous work also proved that the number `|S_n|` of possible integral spectra is only `exp(O(n))`, so (1.1) is equivalent to

\[
\max_{\lambda\in S_n}F_n(\lambda)=2^{o(n^2)}. \tag{1.2}
\]

This run quotients (1.2) by the remaining permutation symmetry.

## 2. B27 — swap the quantifiers: exact colored-two-graph quotient theorem

Write the diagonal signs of a symmetric sign matrix `M` as

\[
d_i=M_{ii}\in\{\pm1\},
\]

and its off-diagonal signs as `s_ij=M_ij`. For every unordered triple of distinct vertices define

\[
\tau_{ijk}=s_{ij}s_{jk}s_{ki}\in\{\pm1\}. \tag{2.1}
\]

### Lemma 2.1 — triangle products classify labeled diagonal-switching classes

Two symmetric sign matrices `M,N` on the same labeled vertex set are related by a diagonal sign conjugation

\[
N=DMD,\qquad D=\operatorname{diag}(\epsilon_1,\dots,\epsilon_n),\quad \epsilon_i\in\{\pm1\},
\]

if and only if

1. `M_ii=N_ii` for every `i`, and
2. `tau_ijk(M)=tau_ijk(N)` for every triple `{i,j,k}`.

#### Proof

Necessity is immediate: diagonal conjugation leaves `M_ii` unchanged and multiplies the three factors in (2.1) by

\[
(\epsilon_i\epsilon_j)(\epsilon_j\epsilon_k)(\epsilon_k\epsilon_i)=1.
\]

For sufficiency, fix vertex `1`, set `epsilon_1=1`, and for `i>1` set

\[
\epsilon_i=\frac{N_{1i}}{M_{1i}}\in\{\pm1\}.
\]

For distinct `i,j>1`, equality of the triangle products on `{1,i,j}` gives

\[
M_{1i}M_{ij}M_{j1}=N_{1i}N_{ij}N_{j1}.
\]

Using symmetry and the definition of `epsilon_i,epsilon_j`,

\[
N_{ij}=\epsilon_i\epsilon_j M_{ij}.
\]

The diagonal entries already agree, so `N=DMD`. QED.

The set of triples with `tau_ijk=-1` is the standard two-graph invariant of a Seidel switching class. Thus the only additional data carried by our model is the `+/-` color on each diagonal vertex. The underlying two-graph/switching equivalence is classical; this application is not being claimed as a new definition.

### Definition 2.2

For an integral spectrum `lambda`, let `K_n(lambda)` be the number of isomorphism classes of the colored two-graphs

\[
\left(\{1,\dots,n\},\ \{\{i,j,k\}:\tau_{ijk}=-1\},\ (d_i)_{i=1}^n\right)
\]

arising from symmetric sign matrices with spectrum `lambda`.

Equivalently, `K_n(lambda)` is the number of signed-permutation conjugacy classes in the exact spectral fiber.

### Theorem 2.3 — Vu 9.4 is equivalent to subquadratic entropy of colored two-graph spectral fibers

For every integral spectrum `lambda`,

\[
K_n(\lambda)\le F_n(\lambda)\le n!\,K_n(\lambda). \tag{2.2}
\]

Consequently Vu's Conjecture 9.4 is equivalent to

\[
\boxed{\max_{\lambda\in S_n}K_n(\lambda)=2^{o(n^2)}.} \tag{2.3}
\]

#### Proof

Diagonal switching has kernel `{+I,-I}` on the off-diagonal complete signed graph, so each diagonal-switching orbit has exactly `2^{n-1}` matrices and exactly one first-row-normalized representative. Permuting coordinates acts on these switching classes. By Lemma 2.1, the orbits of this induced `S_n` action are exactly the colored-two-graph isomorphism classes counted by `K_n(lambda)`.

Every `S_n` orbit contains between `1` and `n!` switching-normalized labeled classes. Summing the orbit sizes gives (2.2).

If (2.3) holds, then using the already-proved `|S_n|=exp(O(n))`,

\[
I_n=\sum_{\lambda\in S_n}F_n(\lambda)
\le |S_n|\,n!\,\max_\lambda K_n(\lambda)
=2^{o(n^2)}.
\]

Conversely, `K_n(lambda)<=F_n(lambda)<=I_n`, so (1.1) implies (2.3). QED.

**B27 outcome.** The source conjecture has been reduced without loss to a uniform isomorphism-class bound inside one colored-two-graph spectral fiber. The quotient removes the `n!` labeling entropy exactly; `log_2(n!)=o(n^2)`.

## 3. B18 — signed-graph / star-complement language, and why the newest simple-spectrum machinery misses F0011

### 3.1 Exact repeated-spectrum obstruction

The earlier parity theorem says:

- if `n` is even and the spectrum is integral, every eigenvalue is even;
- if `n` is odd and the spectrum is integral, exactly one eigenvalue is odd.

This forces repeated eigenvalues in every asymptotic F0011 instance.

### Proposition 3.1

No integral-spectrum symmetric sign matrix has simple spectrum when `n` is even and `n>=4`, or when `n` is odd and `n>=7`. In particular, every integral-spectrum instance with `n>=6` has discriminant zero.

#### Proof: even case

Write `n=2m`. If the `2m` eigenvalues were distinct even integers, the least possible sum of their squares would be obtained from

\[
0,\ \pm2,\ \pm4,\dots,\pm2(m-1),\ \text{and one of }\pm2m.
\]

Hence

\[
\sum_i\lambda_i^2
\ge
8\sum_{k=1}^{m-1}k^2+4m^2
=
\frac{8m^3+4m}{3}. \tag{3.1}
\]

But every symmetric sign matrix satisfies

\[
\sum_i\lambda_i^2=\operatorname{tr}M^2=n^2=4m^2.
\]

Thus

\[
\frac{8m^3+4m}{3}\le4m^2
\iff
(2m-1)(m-1)\le0,
\]

forcing `m<=1`. Therefore simple integral spectrum is impossible for even `n>=4`.

#### Proof: odd case

Write `n=2m+1`. Simple integral spectrum would require `2m` distinct even eigenvalues and one odd eigenvalue. The minimum square sum is therefore at least

\[
\frac{8m^3+4m}{3}+1.
\]

Comparing with `(2m+1)^2` gives

\[
\frac{8m^3+4m}{3}+1\le(2m+1)^2
\iff
(2m+1)(m-2)\le0.
\]

Hence `m<=2`, so simple integral spectrum is impossible for odd `n>=7`. QED.

Alexander Van Werde's August 2026 work on finding all cospectral mates over a fixed number field is directly relevant modern machinery, but its discriminant/simple-spectrum regime cannot directly cover the F0011 event asymptotically: Proposition 3.1 puts every target instance with `n>=6` on the zero-discriminant boundary. This is a mathematical obstruction, not a criticism of that paper.

### 3.2 Star complements expose the scale that a one-eigenvalue reconstruction can save

Let an eigenvalue `theta` of a symmetric matrix `M` have multiplicity `m`. Since `rank(M-theta I)=n-m` and a real symmetric matrix has a nonsingular principal minor of order its rank, there is a principal submatrix `C` of order `n-m` for which `C-theta I` is nonsingular. Partition

\[
M=
\begin{pmatrix}
A&B\\
B^T&C
\end{pmatrix},
\]

with `A` of order `m`. The Schur complement identity shows that multiplicity at least `m` forces

\[
\boxed{
A-\theta I=B(C-\theta I)^{-1}B^T.
} \tag{3.2}
\]

Thus `C` and `B` determine `A`.

This is useful but not yet enough. The previous spectral-square argument gives only `O(n^{2/3})` distinct integral eigenvalues in general, hence guarantees only one multiplicity `m=Omega(n^{1/3})`. Encoding arbitrary signs in `C` and `B` costs at most

\[
\frac{(n-m)(n-m+1)}2+m(n-m)
=
\frac{n(n+1)-m(m+1)}2
\]

bits. The guaranteed saving is therefore only `Omega(n^{2/3})`, far below the `Omega(n^2)` saving needed to prove (2.3). A star-complement proof must exploit simultaneous constraints from many eigenvalues or the colored-two-graph quotient; one repeated eigenvalue alone cannot close the entropy gap.

Zoran Stanić's 2026 monograph *Spectra of Signed Graphs* has dedicated chapters on star complements and on integrality/cospectrality, so this is the right existing language. The calculation above identifies the quantitative obstruction to using it naively.

**B18 outcome.** We obtained an exact zero-discriminant theorem for every asymptotic target matrix and a precise reason why single-eigenvalue star-complement reconstruction does not by itself produce a subquadratic fiber bound.

## 4. B24 — extremal object: exact colored-two-graph census through n=8

The accompanying exact checker enumerates the complete switching-normalized sample space through `n=8`, using only integer traces and exact graph-isomorphism tests on the colored-two-graph incidence object.

It recovers the previous integral counts and adds the exact quotient counts:

| n | `I_n` | realized spectra | total colored-two-graph classes in integral event | `max_lambda K_n(lambda)` | `max_lambda F_n(lambda)` |
|---:|---:|---:|---:|---:|---:|
|1|2|2|2|1|1|
|2|2|2|2|1|1|
|3|10|6|6|1|3|
|4|10|5|5|1|6|
|5|154|14|14|1|30|
|6|274|14|14|1|45|
|7|15,446|44|50|2|1,575|
|8|111,290|33|53|5|24,360|

Thus every realizable integral spectral fiber through `n=6` is a single signed-permutation orbit. At `n=7`, the maximum is only two. At `n=8`, the maximum is only five.

Exactly two `n=8` spectra attain `K_8(lambda)=5`:

\[
(-4,-4,-2,-2,0,2,2,4),
\qquad
(-4,-2,-2,0,2,2,4,4).
\]

Each has `F_8(lambda)=24,360`, and each decomposes into signed-permutation orbit sizes

\[
\boxed{10080,\ 5040,\ 5040,\ 2520,\ 1680}
=
\boxed{\frac{8!}{4},\frac{8!}{8},\frac{8!}{8},\frac{8!}{16},\frac{8!}{24}}.
\]

The finite data therefore say that essentially all of the large labeled fiber seen at `n=8` is explained by permutation orbit size; the number of genuinely different colored two-graphs is tiny. This is evidence for (2.3), not an asymptotic proof.

### 4.1 Exact finite certification mechanism

The checker is exact for the following reasons.

1. Diagonal switching gives one first-row-normalized representative per switching class.
2. The residual off-diagonal pattern is a graph on `n-1` vertices. NetworkX's graph atlas contains all unlabeled graphs through seven vertices, hence covers all residual patterns through `n=8`.
3. Each atlas graph `G` is weighted by `(n-1)!/|Aut(G)|`; the script asserts the weighted total equals the complete normalized sample space.
4. All `2^n` diagonal sign patterns are enumerated.
5. Integrality is decided from exact integer traces `tr(M^k)`, `1<=k<=n`, matched to all integer candidate spectra. Newton identities make equality of these power sums an exact characteristic-polynomial certificate.
6. Lemma 2.1 makes isomorphism of the colored-two-graph incidence graph an exact signed-permutation-equivalence test.

The checker ends `ALL_EXACT_ASSERTIONS_PASS`.

## 5. B24 boundary family — symmetric Hadamard matrices show a deep subproblem already sits inside the fixed-fiber theorem

Let `H` be a symmetric Hadamard matrix of square order `n=q^2`. Then

\[
HH^T=nI,\qquad H^T=H,
\]

so

\[
H^2=nI=q^2I.
\]

Therefore every eigenvalue is `+q` or `-q`, hence every such `H` is an F0011 success.

### Proposition 5.1

Vu's Conjecture 9.4 implies that the number of labeled symmetric Hadamard matrices of every square order `n` is `2^{o(n^2)}` along those orders.

#### Proof

The total number of symmetric sign matrices is `2^{n(n+1)/2}`. Vu's conjectured probability is `2^{-(1/2+o(1))n^2}`, so the total number of integral-spectrum matrices is `2^{o(n^2)}`. Symmetric Hadamard matrices of square order form a subset by the calculation above. QED.

For a symmetric Hadamard matrix the spectrum is determined by the multiplicity `r` of `+q`, so there are at most `n+1` possible spectra. Thus any hypothetical quadratic-entropy family of symmetric square-order Hadamards would already force a single fixed integral spectrum to have quadratic entropy.

This shows that the uniform fixed-fiber theorem is strong enough to subsume a difficult design-counting problem. Ferber–Jain–Zhao proved the first nontrivial general upper bound

\[
H(n)\le 2^{(1-c_H)n^2/2}
\]

for all Hadamard matrices and conjectured the much smaller `H(n)=2^{O(n\log n)}`. Their paper explicitly notes that even proving `2^{o(n^2)}` for general Hadamard matrices would require new ideas. The symmetric-square-order subclass is narrower, but a bounded 2026 search did not locate an asymptotic subquadratic counting theorem for it. Tuomo Valtonen's September 2026 revision classifies symmetric Hadamard matrices only through order 32. This is a boundary obstruction, not a proof that Vu 9.4 is equally hard as the full general-Hadamard counting conjecture.

**B24 outcome.** The exact small cases strongly favor the colored-two-graph quotient, while symmetric square-order Hadamards identify a serious structured family that any uniform fixed-fiber proof must control.

## 6. Dated literature check — 2026-09-19

Fresh bounded checks this run recovered:

- Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), source Conjecture 9.4.
- Kevin Costello and Parker Williams, *On the number of integral graphs*, Linear Algebra Appl. 493 (2016), with the `2^{-c n^{3/2}}` graph-integrality upper-bound scale.
- C. L. Mallows and N. J. A. Sloane, *Two-Graphs, Switching Classes and Euler Graphs are Equal in Number*, SIAM J. Appl. Math. 28 (1975), for the classical two-graph/switching equivalence.
- Aida Abiad, Nils van de Berg, Robin Simoens, *Switching methods of level 2 for the construction of cospectral graphs*, available online 2026-08-26, DOI 10.1016/j.laa.2026.08.030.
- Zoran Stanić, *Spectra of Signed Graphs*, Cambridge University Press, 2026; chapters on star complements and integrality/cospectrality.
- Alexander Van Werde, *Finding all cospectral mates over a number field*, arXiv:2608.12410, submitted 2026-08-11.
- Asaf Ferber, Vishesh Jain, Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, Combin. Probab. Comput. 31 (2022).
- Tuomo Valtonen, *Classification of Symmetric Hadamard Matrices Up to Order 32*, arXiv:2608.06920v2, revised 2026-09-10.

The bounded search did not surface a paper proving Vu's `2^{-(1/2+o(1))n^2}` conjecture, nor an asymptotic `2^{o(n^2)}` count specifically for symmetric square-order Hadamard matrices. Those are search misses only, not certified openness or novelty.

## 7. What moved mathematically, and what did not

The frozen metric is still

`N_exact = largest n exhaustively classified with exact integral/non-integral counts`.

It remains `8`. No attempt was made to manufacture an `n=9` checker merely to move the metric.

The actual mathematical progress is instead structural:

1. source closure is equivalent to a colored-two-graph fixed-spectrum entropy theorem (2.3);
2. all asymptotic target matrices lie in the repeated-spectrum / zero-discriminant regime;
3. one-eigenvalue star-complement reconstruction is quantitatively too weak at the guaranteed multiplicity scale;
4. the exact quotient fiber multiplicity is only `1,1,1,1,1,1,2,5` through `n=8`;
5. symmetric square-order Hadamards form a deep structured boundary family inside the fixed-spectrum problem.

Status remains **PARTIAL / source OPEN under bounded current checks**.
