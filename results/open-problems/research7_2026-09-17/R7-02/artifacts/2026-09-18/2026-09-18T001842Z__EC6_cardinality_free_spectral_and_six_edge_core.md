Model/effort: **GPT-5.6 Sol / reasoning effort UNVERIFIED** — this is not GPT-6 at maximum; GPT-6 / maximum reasoning was requested, but no authenticated runtime telemetry or binding model/effort selector is exposed.

# KHETAN-2026-EC6 — cardinality-free one-rich branch, intrinsic prime-product closure, and six-edge deterministic core

Target: Abhishek Khetan, *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2 (2026), especially Conjecture 2, Theorem 3.12, Theorem 3.16, Theorem 3.18, and Section 3.5.

Frozen source question: for every exact full-affine-span cluster `F subset Z^2` with `|F|=6` and every `F`-tiling `T`, must `cl(Z^2*T)` contain a one-periodic `F`-tiling?

This note does **not** claim protocol closure. It strengthens and modularizes the existing R7-02 proof candidate. The source remains OPEN in the checked primary version; independent P26 and distinct OTHER-track audits remain absent.

## 1. Idea before code

The six-cell candidate had three proof interfaces that were easy to conflate:

1. the spectral branch in which at most one support direction carries infinitely many common mask zeros;
2. the geometric/combinatorial branch in which two transverse directions do carry infinitely many common zeros;
3. the product-tiling endpoint after the six points have been forced into a `3 x 2` grid.

The key simplification is that these interfaces can be separated sharply.

* The one-rich spectral branch is **cardinality-free**: Khetan's proof uses only the general dilation lemma, the finite character-kernel cover, the irrational-phase lemma, and the periodic-cylinder theorem. Prime-square arithmetic is absent.
* In the two-rich six-cell branch, only the `alpha=1` common-phase equation is needed to rule out singleton sections and exclude the only non-product six-edge incidence graph `C6`.
* Once the incidence graph is `K_{2,3}`, exactness itself supplies the one-dimensional prime tilings. Thus the product endpoint needs no root-of-unity classification at all after the incidence step.

This also explains precisely why the elementary `alpha=1` incidence mechanism is special to six points: for every odd prime `q>=5` there is an explicit exact full-span `2q`-cell lattice tile with two transverse common phase-zero section systems and no singleton sections whose incidence graph is non-product.

## 2. B3 — the six-edge rigidity is sharp among `2q` semiprime sizes

### 2.1 Six-edge incidence classification

Let `G=(R,C;E)` be a finite simple bipartite graph with exactly six edges and minimum degree at least two on both sides.

Then `|R|,|C|<=3`. Neither side has size one, since simplicity would force degree at most one on the opposite side. If `|R|=2`, every vertex of `C` has degree exactly two, hence `|C|=3` and `G=K_{2,3}`. The transpose case is identical. If `|R|=|C|=3`, the sum of the degrees on each side is six and every degree is at least two, hence every degree is exactly two. A finite simple two-regular bipartite graph is a disjoint union of even cycles. On six vertices there is no decomposition into two cycles, because the shortest simple cycle has four vertices. Therefore `G=C6`.

So the only possibilities are

`K_{2,3}`, its transpose, or `C6`.

### 2.2 A family showing why this local mechanism does not extend from 6 to `2q`, `q>=5`

**Proposition.** For every odd prime `q>=5`, there is an exact full-affine-span cluster `F_q subset Z^2` of cardinality `2q` with the following properties.

1. Every nonempty horizontal section and every nonempty vertical section has at least two points.
2. There is a sixth root of unity `zeta=exp(2*pi*i/6)` such that every horizontal section `H` satisfies

   `sum_{(x,y) in H} zeta^x = 0`.

3. Every vertical section `V` satisfies

   `sum_{(x,y) in V} (-1)^y = 0`.

4. The horizontal/vertical section-incidence graph is not a complete bipartite product. In fact it is

   `K_{2,3} disjoint_union ((q-3)/2 copies of K_{2,2})`.

5. `F_q` tiles by the lattice `q Z x 2 Z`.

Thus the two no-singleton conditions plus common `alpha=1` phase vanishing in both directions do not force product structure for the next distinct-semiprime sizes. At `q=3`, the extra `K_{2,2}` blocks disappear and the incidence graph collapses exactly to `K_{2,3}`; this is the six-cell rigidity exploited below.

**Proof.** Partition the residue classes modulo `q` into one block of size three and `(q-3)/2` blocks of size two. Choose the size-three block to contain residue `0`, and choose one size-two block to contain residue `1`.

Assign to the three residues in the first block the phase residues `0,2,4 mod 6`. Assign to each size-two block a pair `a,a+3 mod 6`. For the block containing residue `1`, choose the phase of residue `1` to be `1 mod 6`; its mate therefore has phase `4 mod 6`. Because `gcd(q,6)=1`, the Chinese remainder theorem gives for every residue `r mod q` a unique class `x_r mod 6q` satisfying

`x_r = r (mod q)` and `x_r = phase(r) (mod 6)`.

Choose representatives so that `x_0=0` and `x_1=1`, which are already the CRT solutions for their assigned congruences.

Index the residue blocks by `j=0,...,(q-3)/2`. If `B_j` is the corresponding set of `x_r` values, define

`F_q = union_j [ B_j x {2j,2j+1} ]`.

There are two points for every one of the `q` residue classes, so `|F_q|=2q`.

For a horizontal row in the three-element block, its phase sum is

`1 + zeta^2 + zeta^4 = 0`.

For a horizontal row in a two-element block, its two phase residues differ by three, so

`zeta^a + zeta^(a+3)=0`.

Every vertical line `x=x_r` contains precisely the two points with heights `2j,2j+1` from its block, and therefore

`(-1)^(2j)+(-1)^(2j+1)=0`.

The incidence graph is consequently one `K_{2,3}` component plus one `K_{2,2}` component for every remaining pair block, proving the stated non-product geometry when `q>=5`.

Modulo the lattice `q Z x 2 Z`, each residue `r mod q` occurs once with even height and once with odd height. Hence `F_q` is a complete set of `2q` coset representatives and

`Z^2 = F_q direct_sum (q Z x 2 Z)`.

Thus `F_q` is exact.

Finally `(0,1) in <F_q-F_q>` because the two points above `x_0=0` have consecutive heights. Also the point above `x_1=1` differs from `(0,0)` by `(1,2j)` for some `j`; subtracting `2j(0,1)` gives `(1,0)`. Therefore `<F_q-F_q>=Z^2`, so `F_q` has full affine span. QED.

### B3 outcome

The six-cell incidence reduction is not an instance of a general `2q` product theorem derived merely from no-singleton sections and `alpha=1` phase vanishing. Six is the smallest distinct semiprime and is exceptional because six edges leave only `K_{2,3}` and `C6`; for every `2q`, `q>=5`, exact full-span non-product local phase geometries already exist.

This is a limitation of the local reduction, **not** a counterexample to Khetan's orbit-closure statement at size `2q`: the constructed `F_q` has the explicit periodic lattice tiling `qZ x 2Z`.

## 3. B15 — asymmetric product closure without post-incidence phase arithmetic

The preceding R7-02 theorem assumed from the start that `A` and `B` were complete residue systems modulo distinct primes. For the six-cell proof this hypothesis can be derived from exactness, so the endpoint can be stated intrinsically.

### Theorem (intrinsic distinct-prime product periodicity)

Let `p,q` be primes. Let `A,B subset Z` satisfy

`|A|=p`, `|B|=q`, `gcd(A-A)=gcd(B-B)=1`.

If `T` is an `(A x B)`-tiling of `Z^2`, then

`(p,0)+T=T` or `(0,q)+T=T`.

No complete-residue-system hypothesis on `A` or `B` is needed in the statement.

### Proof

Apply Khetan Lemma 3.6 to `T`. For every integer `n`, the row-fibre union

`R_n = disjoint_union_{b in B} S_{n-b}`

is an `A`-tiling of `Z`; for every integer `m`, the corresponding column-fibre union `C_m` is a `B`-tiling of `Z`.

Since `|A|=p` is prime and `gcd(A-A)=1`, Khetan Lemma 3.3 / Corollary 3.4 gives

`R_n = pZ + r_n`

for some residue `r_n`, and in particular forces `A` itself to contain exactly one representative of every residue modulo `p`: reducing the exact identity `A direct_sum R_n=Z` modulo `p`, where `R_n` is one coset of `pZ`, leaves exactly one representative from `A` in every residue class. Thus `A` is a complete residue system modulo `p`. The identical argument shows that `B` is a complete residue system modulo `q`.

All hypotheses of the already proved R7-02 distinct-prime product-periodicity theorem are now satisfied. That theorem, using Khetan Lemma 3.7 with arbitrary codomain, gives the stated period `(p,0)` or `(0,q)`. QED.

### Corollary (the `K_{2,3}` endpoint needs no root-of-unity classification)

Let `F` be an exact full-affine-span six-point cluster. Suppose two transverse line families cut `F` with incidence graph `K_{2,3}` (or its transpose). Then every `F`-tiling is one-periodic.

**Proof.** Let `u,v` be primitive direction vectors of the two line families. Since all six intersections of two lines with three transverse lines are occupied lattice points, translating one intersection to the origin writes

`F = {a u + b v : a in A, b in B}`

with `|A|=3`, `|B|=2` (or swapped). The subgroup generated by differences is

`<F-F> = gcd(A-A) Z u + gcd(B-B) Z v`.

Its index in `Z^2` is

`|det(u,v)| gcd(A-A) gcd(B-B)`.

Full affine span makes this index one, hence `|det(u,v)|=1` and both gcds are one. The unimodular change of coordinates sends `F` to `A x B`; apply the intrinsic distinct-prime theorem with `(p,q)=(3,2)`. QED.

### B15 outcome

After the six-edge incidence graph becomes `K_{2,3}`, **all phase arithmetic can stop**. Exactness plus full affine span alone reduce the endpoint to prime one-dimensional tilings and the distinct-prime fibre theorem. This removes the earlier need to infer “three phases form an equilateral triple” and “two phases are opposite” in order to prove the residue-system hypotheses.

## 4. B27 — swap the quantifiers: isolate a deterministic six-edge theorem

The two-rich spectral branch can be separated from spectral theory almost completely.

### Lemma (weighted six-edge incidence)

Let `G=(R,C;E)` be a finite simple bipartite graph with six edges and minimum degree at least two. Suppose there are nonzero complex numbers `lambda_i` for `i in R` and nonzero complex numbers `z_j` for `j in C` such that for every `i in R`,

`lambda_i * sum_{j adjacent to i} z_j = 0`.

Then `G=K_{2,3}` or its transpose; in particular `G` is not `C6`.

**Proof.** The six-edge classification above leaves only `K_{2,3}`, its transpose, and `C6`. If `G=C6`, label the three vertices on each side so row `i` misses column `i`. Since `lambda_i` is nonzero, the three equations are

`z_2+z_3=0`,
`z_1+z_3=0`,
`z_1+z_2=0`.

The first two give `z_1=z_2`; the third gives `2z_1=0`, contradicting `z_1!=0`. QED.

### Theorem (deterministic six-section closure criterion)

Let `F subset Z^2` be an exact full-affine-span cluster with `|F|=6`. Suppose there are two transverse directions `u,v` such that:

1. every nonempty section of `F` by a line parallel to `u` or to `v` contains at least two points;
2. for the `u`-parallel sections, there is a nonzero rank-one phase factorization on the section-incidence grid: at the intersection of row `i` and column `j`, the coefficient is `lambda_i z_j` with `lambda_i,z_j != 0`, and every row coefficient sum is zero.

Then **every `F`-tiling is one-periodic**.

**Proof.** Build the simple bipartite incidence graph of nonempty `u`-parallel and `v`-parallel sections, with the six points of `F` as edges. Hypothesis 1 gives minimum degree at least two. Hypothesis 2 and the weighted six-edge lemma exclude `C6`; hence the graph is `K_{2,3}` or its transpose. The preceding B15 corollary then gives one-periodicity of every `F`-tiling. QED.

This statement is deliberately independent of where the phase factors came from.

## 5. Cardinality-free one-rich spectral theorem

The other half of Khetan's Theorem 3.18 does not use prime-square arithmetic at all. Making that explicit removes the most important remaining source-interface ambiguity in the six-cell candidate.

### Theorem (one-rich spectral branch for arbitrary finite cardinality)

Let `F subset Z^2` be any finite exact cluster, let `N=|F|`, and let `T` be an `F`-tiling. Form the orbit closure `X`, choose an ergodic invariant probability measure `mu`, let `f` be the origin-cylinder indicator, and let `nu` be its spectral measure as in Khetan Section 3.4. Let `Delta` be a minimum-cardinality finite set supplied by Khetan Theorem 3.16,

`supp(nu) subset union_{g in Delta} ker chi_g`.

For every integer `alpha` coprime to `N`, let

`M_alpha(xi)=sum_{a in F} chi_{alpha a}(xi)`.

Call `g in Delta` rich when

`ker chi_g intersect intersection_{gcd(alpha,N)=1} Z(M_alpha)`

is infinite.

If at most one member of `Delta` is rich, then `X` contains a one-periodic `F`-tiling; in fact the origin cylinder is invariant modulo `mu` under a nonzero lattice translation, and Khetan Theorem 3.11 makes `mu`-almost every point of `X` one-periodic.

### Proof

Khetan's dilation lemma, Theorem 3.12, is stated for arbitrary finite `F`: every `F`-tiling is also an `alpha F`-tiling whenever `gcd(alpha,N)=1`. Transporting the tiling identity through the spectral isometry gives, for each such `alpha`,

`M_alpha = kappa * 1_{ {0} }`

in `L^2(T^2,nu)` for the appropriate constant `kappa`. Since `M_alpha` is continuous and vanishes `nu`-almost everywhere away from the origin,

`supp(nu) subset [intersection_{gcd(alpha,N)=1} Z(M_alpha)] union {0}`.

Assume first that exactly one member `g_0 in Delta` is rich. If none is rich, choose any `g_0 in Delta`; the same argument only becomes stronger. For every `h in Delta\{g_0}`, the set

`S_h = ker chi_h intersect intersection_{gcd(alpha,N)=1} Z(M_alpha)`

is finite. Therefore

`supp(nu) subset ker chi_{g_0} union S`

for some finite `S` (including the origin if necessary).

Among all positive multiples `k g_0` and finite sets `S` for which

`supp(nu) subset ker chi_{k g_0} union S`, 

choose one minimizing `|S|`, relabel the multiple as `g_0`, and discard points of `S` lying in `ker chi_{g_0}`.

Every `s in S` lies in `supp(nu)`, or else it could be removed. Because `S` is finite and disjoint from the closed kernel, each such `s` is isolated in the support and hence has positive `nu`-mass. Moreover `chi_{g_0}(s)` is not a root of unity: if it had order `k'`, then `s in ker chi_{k'g_0}`, while `ker chi_{g_0} subset ker chi_{k'g_0}`; replacing `g_0` by `k'g_0` and removing `s` would contradict minimality of `|S|`.

Partition `S` into classes `E` on which `chi_{g_0}` has the same value `gamma_E`, and let `phi_E` be the inverse spectral images of the corresponding indicators. Writing `f^{g_0}` for the projection of `f` onto the `g_0`-invariant subspace, the spectral decomposition gives for every integer `n`

`(n g_0).f - f = sum_E (gamma_E^n - 1) phi_E`.

Take a common full-measure set on which these countably many identities hold pointwise for all `n>=0`. The left side is integer-valued because `f` and its translates are `{0,1}`-valued. Thus for every point of that full-measure set,

`sum_E (gamma_E^n - 1) phi_E(y) in Z` for all `n>=0`.

Every `gamma_E` is irrational in Khetan's terminology (not a root of unity). Khetan Lemma 3.1 therefore forces the displayed expression to be zero for every `n`. Taking `n=1` gives

`g_0.f = f`

in `L^2(X,mu)`. Hence the origin cylinder is `g_0`-periodic modulo null sets. Khetan Theorem 3.11 then implies that `mu`-almost every point of `X` is one-periodic, so in particular `X` contains a one-periodic `F`-tiling. QED.

### Why this matters for six cells

For `N=6`, the correct common-zero equations are simply indexed by `gcd(alpha,6)=1`. The proof above remains unchanged. It never invokes Lemma 3.15, prime-power cyclotomy, section divisibility, or an equality `N=p^2`.

Thus the “at most one rich direction” half of the R7-02 candidate is now a standalone theorem under exactly the general source tools that are valid at cardinality six.

## 6. Two-rich six-cell branch from only `alpha=1`

It remains to connect two rich directions to the deterministic theorem of Section 4 without importing the prime-power part of Khetan Lemma 3.15.

Let `g=n h` with `h` primitive be rich. Khetan Lemma 3.2 writes `ker chi_g` as a finite union of one-dimensional circles. Since the common-zero set on this kernel is infinite, one such circle contains infinitely many common-zero points. Parameterize it as

`xi(t)=r h + t h^perp (mod Z^2)`.

Use only the allowed dilation `alpha=1`. Along this circle,

`M_1(xi(t)) = sum_{a in F} exp(2*pi*i*r<a,h>) z^{<a,h^perp>}`, `z=exp(2*pi*i*t)`,

is a Laurent polynomial with infinitely many unit-circle zeros, hence is identically zero. Grouping by the exponent `<a,h^perp>` shows that every nonempty section `L` of `F` parallel to `h` satisfies

`sum_{a in L} exp(2*pi*i*r<a,h>) = 0`.

In particular no such section is a singleton.

Now suppose two distinct rich directions `h_0,h_1` occur. Minimality of Khetan's `Delta` makes distinct members pairwise linearly independent, so these directions are transverse. Applying the preceding argument in both directions gives the two no-singleton section families required in the deterministic theorem.

For the rank-one phase condition, use the first direction. On the affine grid formed by the two line families, write an intersection point as

`a_{ij}=a_0+s_i h_1+t_j h_0`

with real scalars `s_i,t_j`. Then its first-direction phase factors as

`exp(2*pi*i*r<a_{ij},h_0>)
 = lambda_i z_j`,

where

`lambda_i = exp(2*pi*i*r(<a_0,h_0>+s_i<h_1,h_0>))`

and

`z_j = exp(2*pi*i*r t_j |h_0|^2)`.

Both factors are nonzero, and the common section equation is exactly

`lambda_i sum_{j adjacent to i} z_j = 0`.

The deterministic six-section theorem now forces the incidence graph to be `K_{2,3}` or its transpose and, by B15, every `F`-tiling is one-periodic.

Therefore the two-rich branch at cardinality six is closed without using the prime-power cyclotomic divisibility statement.

## 7. Combined source-level proof architecture after this run

For an exact full-affine-span six-cell cluster `F` and any `F`-tiling `T`:

1. Use Khetan's general spectral setup, dilation lemma, and minimum character-kernel cover `Delta`.
2. If at most one direction is rich for the full family `gcd(alpha,6)=1`, apply the cardinality-free one-rich theorem: the orbit closure contains a one-periodic tiling.
3. If at least two directions are rich, use only `alpha=1` to obtain no-singleton sections and the rank-one phase equations in two transverse directions.
4. Six-edge incidence leaves `K_{2,3}` or `C6`; the rank-one row equations exclude `C6`.
5. `K_{2,3}` gives a unimodular `3 x 2` product by full affine span.
6. Exactness plus one-dimensional prime rigidity makes the two factors complete residue systems, and the distinct-prime fibre theorem makes the given tiling itself one-periodic.

This architecture avoids the mixed-prime failure of Khetan Lemma 3.15 altogether.

It remains a **PROVED CANDIDATE / AUDIT OPEN**, not a protocol-closed result. Independent P26 and distinct OTHER-track audits are still required, and the existing paper package must replace its superseded formal-series product argument with the valid fibre proof before it can be called the final closure package.

## 8. Failure modes and exact scope

* The semiprime family in Section 2 is not a source counterexample; it has an explicit lattice tiling. Its purpose is to show the local `alpha=1` incidence rigidity is genuinely six-edge-specific.
* The two-rich proof does not assert Khetan Lemma 3.15 for `|F|=6`. It deliberately bypasses that prime-power lemma.
* The one-rich theorem uses the complete family of dilation masks indexed by integers coprime to `N`; it is not an `alpha=1` statement.
* No literature search miss is treated as a novelty certificate.
* No self-review in this note counts as P26 or OTHER-track audit evidence.
