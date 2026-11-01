Model/effort: **GPT-5.6 Sol / reasoning effort UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# KHETAN-2026-EC6 — dilation-free spectral normal form and boundary audit

Target: Abhishek Khetan, *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2 (2026), especially the cardinality-six exception left open in the abstract/Section 3.5 and the spectral support input previously source-checked as Theorem 3.16.

Run-start snapshot for this iteration: `5415c81f1b8a69f15989ff6bbd4218afede6b29e`.
Fresh master immediately before this artifact write: `b6bae7308a5f6b4296f22744919850e41f78d3f4`.
Canonical owner: R7-02 / native id `6aabe797a39081919acc889f29f4c556`.
Frozen metric: `E_EC6=1` before this note and `E_EC6=1` after this note: **NO MOVEMENT**. This note simplifies and stress-tests the existing source-level proof candidate; it does not count as an independent audit.

Methods in this iteration: **B10 / B20 / B29**.

## 1. Idea before proof: remove every downstream dilation quantifier

The preceding R7-02 proof candidate used Khetan's family of dilated tiling identities indexed by integers `alpha` coprime to six. That family is valid according to the previously checked source interface, but it creates an unnecessary quantifier at exactly the point an independent auditor would be most likely to worry about a hidden prime-power dependency.

The new observation is that the entire six-cell argument after the finite spectral-kernel cover can be run using only the **original mask**

`M(xi) = sum_{a in F} chi_a(xi)`.

Thus the downstream argument needs no dilation theorem at all. The one-rich branch is a finite-alphabet spectral recurrence for a single translation. The two-rich branch needs only infinitely many zeros of `M` on two kernel components; restriction of this one Laurent polynomial to a component gives the section equations used to exclude `C6`.

This has two consequences.

1. The proof no longer needs to transfer Khetan's prime-square proof with the phrase “replace coprime-to-p by coprime-to-6.”
2. The only nontrivial source interfaces still needed downstream are the finite character-kernel cover already recovered from Khetan's Theorem 3.16 and the prime-cardinality one-dimensional tiling rigidity already recovered as Corollary 3.4. The row/column fibre decomposition is proved directly below.

The rest of this note proves this normal form carefully and checks the boundary cases that can otherwise hide in spectral shorthand.

## 2. Center first: the original mask annihilates the nonconstant spectral part

Let `X` be the orbit closure of an `F`-tiling `T`, and let `mu` be any ergodic invariant Borel probability measure on `X`. Write

`f(x)=x(0) in {0,1}`.

Every point of `X` is still an `F`-tiling. Indeed, for each fixed `v in Z^2`,

`Phi_v(x)=sum_{a in F} x(v-a)`

is a continuous cylinder function. It equals one on every translate of `T`, hence equals one on their closure. Thus

`sum_{a in F} U_a f = 1`

in `L^2(X,mu)`.

Taking expectations and using `|F|=6` gives

`6 E_mu f = 1`, hence `E_mu f=1/6`.

Set

`f_c=f-1/6`.

Then

`sum_{a in F} U_a f_c = 0`.

If `nu_c` is the spectral measure of `f_c`, the spectral theorem therefore gives

`M(xi)=0` for `nu_c`-almost every `xi`,

so

`support(nu_c) subset Z(M)`.

Moreover

`||f_c||_2^2 = Var_mu(f)=1/6-1/36=5/36>0`.

Thus `nu_c` is nonzero. This disposes of the degenerate “only a constant spectral atom remains” boundary case at the outset.

By the finite character-kernel cover supplied by the previously source-checked Khetan spectral interface, choose a finite set `Delta subset Z^2\{0}` such that

`support(nu_c) subset union_{g in Delta} ker chi_g`.

Choose `Delta` with minimum cardinality.

## 3. B20: a self-contained parallel-kernel compression lemma

The previous draft said that distinct elements of a minimum cover point in distinct directions. Here is the exact reason, so no geometric consequence is hidden inside that phrase.

### Lemma 3.1 (parallel kernels compress)

Let `h in Z^2` be primitive and let `m,n` be nonzero integers. Put `L=lcm(|m|,|n|)`. Then

`ker chi_{m h} union ker chi_{n h} subset ker chi_{L h}`.

Consequently a cardinality-minimal finite cover by character kernels cannot contain two parallel vectors.

### Proof

If `xi in ker chi_{m h}`, then `m <h,xi>` is an integer modulo the defining torus lattice. Since `L/m` is an integer up to sign,

`L<h,xi>=(L/m)m<h,xi>`

is also an integer, so `xi in ker chi_{Lh}`. The same argument applies to `n`. Replacing two parallel kernels by the single kernel `ker chi_{Lh}` preserves the cover and decreases its cardinality, contradicting minimality. QED.

Thus any two distinct members of `Delta` give transverse directions.

## 4. Dilation-free rich/non-rich dichotomy

Call `g in Delta` **M-rich** when

`ker chi_g intersect Z(M)`

is infinite. This definition involves only the original mask, not any family of dilates.

There are two cases.

1. At most one member of `Delta` is M-rich.
2. At least two members are M-rich.

The two cases exhaust the proof candidate.

## 5. B10: at most one M-rich kernel implies periodicity by a finite-alphabet recurrence

Assume at most one member `g_0 in Delta` is M-rich. If none is rich, choose any `g_0 in Delta`; this is possible because `nu_c` is nonzero and hence the finite cover is nonempty.

For every `h in Delta\{g_0}`, the set

`ker chi_h intersect Z(M)`

is finite. Since `support(nu_c) subset Z(M)`, there is therefore a finite set `S` such that

`support(nu_c) subset ker chi_{g_0} union S`.

We now normalize this statement so that every point of `S` is a genuine non-torsion spectral atom.

### Lemma 5.1 (minimal finite residual normalization)

Among all positive multiples `k g_0` and finite residual sets `S_k` satisfying

`support(nu_c) subset ker chi_{k g_0} union S_k`, 

choose one minimizing `|S_k|`. Rename the selected multiple `g` and residual set `S`, and remove from `S` all points already in `ker chi_g`. Then:

1. every `s in S` lies in `support(nu_c)`;
2. every `s in S` is an atom of `nu_c`;
3. `gamma_s:=chi_g(s)` is not a root of unity.

### Proof

A point not in the support can be removed from `S`, contradicting minimality, so (1) holds. The set `S` is finite and disjoint from the closed set `ker chi_g`. Hence each `s in S` is isolated in the support: choose a small neighbourhood avoiding the kernel and all other points of `S`. Because `s` belongs to the support, that neighbourhood has positive spectral measure, and its intersection with the support is `{s}`; therefore `nu_c({s})>0`, proving (2).

For (3), suppose `gamma_s` has finite order `q`. Then `s in ker chi_{qg}` and `ker chi_g subset ker chi_{qg}`. Replacing `g` by `qg` absorbs `s` while preserving the old kernel part, so the necessary finite residual has smaller cardinality, contradiction. QED.

Group the points of `S` by equal values of `gamma_s`. Let the distinct values be `gamma_1,...,gamma_m`, and let `phi_j` be the inverse spectral projection of `f_c` onto the atoms whose `g`-eigenvalue equals `gamma_j`. Let `f_0` be the projection of `f_c` to `ker chi_g`. Then

`f = 1/6 + f_0 + sum_{j=1}^m phi_j`,

`U_g f_0=f_0`,

`U_g phi_j=gamma_j phi_j`,

where the `gamma_j` are pairwise distinct and none is a root of unity.

The next lemma is elementary and removes the need for an irrational-phase lemma or a separate periodicity-transfer theorem.

### Lemma 5.2 (finite alphabet kills non-torsion eigenmodes)

Let `U` be an invertible measure-preserving transformation. Suppose a finite-valued function has a decomposition

`f=f_0+sum_{j=1}^m phi_j`

with `Uf_0=f_0` and `U phi_j=gamma_j phi_j`, where the `gamma_j` are pairwise distinct nonzero complex numbers and no `gamma_j` is a root of unity. Then every `phi_j=0` almost surely and `Uf=f` almost surely.

### Proof

Discard a countable union of null sets so that all translated eigenfunction identities hold pointwise for all integers. Fix a remaining point `x` and put

`a_n=f(U^n x)=f_0(x)+sum_{j=1}^m gamma_j^n phi_j(x)`, `n in Z`.

The sequence takes values in a finite alphabet. It satisfies the linear recurrence whose characteristic polynomial is

`Q(z)=(z-1) product_{j=1}^m (z-gamma_j)`.

Both the leading and constant coefficients of `Q` are nonzero. Therefore any block of `m+1` consecutive values determines uniquely both the next value and the preceding value. There are only finitely many possible length-`m+1` blocks because the alphabet is finite. Hence two blocks repeat, say at positions `r<s`. Forward and backward determinism then imply

`a_{n+L}=a_n` for every `n in Z`, where `L=s-r>0`.

Subtracting the two spectral expressions gives

`sum_{j=1}^m phi_j(x)(gamma_j^L-1) gamma_j^n=0`

for every integer `n`. Taking `n=0,...,m-1` gives a Vandermonde system in the coefficients

`c_j=phi_j(x)(gamma_j^L-1)`.

The `gamma_j` are distinct, so the Vandermonde matrix is invertible and every `c_j=0`. Since no `gamma_j` is a root of unity, `gamma_j^L-1 !=0`; hence every `phi_j(x)=0`. This holds almost surely. QED.

Apply Lemma 5.2 with `U=U_g`. We obtain `U_g f=f` in `L^2`.

For each `v in Z^2`, translations commute, so

`U_g(U_v f)=U_v(U_g f)=U_v f`.

Taking a countable intersection of the corresponding full-measure sets, for almost every configuration `x in X` and every `v in Z^2`,

`x(v+g)=x(v)`.

Such an `x` is a one-periodic configuration. Section 2 already proved that every `x in X` is an `F`-tiling. Hence `X` contains a one-periodic `F`-tiling.

### B10 outcome

The at-most-one-rich branch is now deterministic after the finite spectral cover and uses only the original mask. It no longer needs Khetan Theorem 3.12, Lemma 3.1, or Theorem 3.11 downstream.

## 6. Two M-rich directions: one Laurent polynomial gives every section equation needed

Assume there are two M-rich elements `g_0,g_1 in Delta`. By Lemma 3.1 their directions are transverse.

Fix one rich vector `g=n h`, where `h` is primitive. The kernel `ker chi_{nh}` is a union of finitely many one-dimensional subtorus components on which `<h,xi>` is fixed modulo `1/n`. Since `ker chi_g intersect Z(M)` is infinite, one component contains infinitely many zeros of `M`.

Choose a point `xi_0` on that component and parameterize it by

`xi(t)=xi_0+t h^perp`,

where `h^perp=(-h_2,h_1)`. Then

`M(xi(t)) = sum_{a in F} exp(2 pi i <a,xi_0>) z^{<a,h^perp>}`, `z=exp(2 pi i t)`,

is a Laurent polynomial in `z`. It has infinitely many unit-circle zeros, hence it is the zero Laurent polynomial. Grouping coefficients by the integer `<a,h^perp>` gives:

### Lemma 6.1 (no singleton section from one mask)

For every nonempty section `E` of `F` by a line parallel to `h`,

`sum_{a in E} exp(2 pi i <a,xi_0>)=0`.

In particular every such section contains at least two points.

Apply this to both rich transverse directions. Construct the simple bipartite incidence graph whose left and right vertices are the nonempty sections in the two directions and whose six edges are the six points of `F`. Every vertex has degree at least two.

As proved and exactly checked in earlier R7-02 work, a simple bipartite graph with six edges and minimum degree at least two is, up to swapping sides, either `K_{2,3}` or `C6`.

To exclude `C6`, use the phase equation from just one rich direction. If the two affine line families have intersection points `a_ij`, then linearity gives affine product coordinates

`a_ij=a_*+s_i v+t_j h`

for suitable real scalars on the occupied intersections. Therefore the first-direction phase factors as

`exp(2 pi i <a_ij,xi_0>) = lambda_i z_j`

with nonzero factors `lambda_i,z_j`. In a `C6`, label rows so row `i` misses column `i`. The three row equations from Lemma 6.1 become, after cancelling `lambda_i`,

`z_2+z_3=0`,
`z_1+z_3=0`,
`z_1+z_2=0`.

The first two give `z_1=z_2`; the third gives `2z_1=0`, impossible because `z_1` is a nonzero complex phase. Hence `C6` is impossible and the incidence graph is `K_{2,3}` or its transpose.

No dilation identity and no root-of-unity classification is used here.

## 7. Product endpoint with only one imported one-dimensional theorem

A `K_{2,3}` incidence pattern in two primitive transverse lattice directions writes, after translation,

`F={a u+b v : a in A, b in B}`

with `|A|=3`, `|B|=2` (or swapped). Put

`d_A=gcd(A-A)`, `d_B=gcd(B-B)`.

Then

`<F-F>=d_A Z u+d_B Z v`,

whose index in `Z^2` is

`|det(u,v)| d_A d_B`.

Full affine span forces all three positive integer factors to equal one. Thus `(u,v)` is unimodular and `d_A=d_B=1`. After changing coordinates, the tile is `A x B` with `|A|=3`, `|B|=2`, and both difference gcds equal to one.

The row/column fibre statement can be proved directly, so no source citation is necessary for it. For an `(A x B)`-tiling `T`, define

`S_y={x:(x,y) in T}`, `T_x={y:(x,y) in T}`.

For fixed `n`, unique representation of every `(x,n)` gives the exact disjoint one-dimensional tiling

`Z = A direct_sum R_n`, where `R_n=disjoint_union_{b in B} S_{n-b}`.

Likewise, for fixed `m`,

`Z = B direct_sum C_m`, where `C_m=disjoint_union_{a in A} T_{m-a}`.

Now use the previously source-checked prime-cardinality one-dimensional rigidity only for the three-point factor: since `|A|=3` and `gcd(A-A)=1`, each `R_n` is a coset `3Z+r_n`. Reducing the exact tiling modulo three shows that `A` is a complete residue system modulo three.

For `B`, `|B|=2` and `gcd(B-B)=1` force its two elements to differ by one. After translation `B={0,1}`, and the equation

`1_C(k)+1_C(k-1)=1`

shows directly that each `B`-tiling `C_m` is one parity class `2Z+s_m`.

The source-specific residue-profile argument from the preceding run now finishes:

- if the binary profile `s_m` is constant, every occupied row is a complete `3Z` coset, so `(3,0)` is a period;
- if `s_m` is nonconstant, it uses both parities, hence every row is occupied; the two consecutive shifts in `B` force `r_n=r_{n+1}` for every `n`, so `r_n` is constant, and then every occupied column is a complete `2Z` coset, so `(0,2)` is a period.

Thus the given tiling itself is one-periodic in the two-rich case.

## 8. B29: explicit boundary-case ledger

The proof normal form above survives the boundary cases that were previously hidden in phrases such as “including the origin if necessary” or “choose a minimal exceptional set.”

### 8.1 The trivial character

Centering first removes it from the spectral equation: `f_c=f-1/6` satisfies `M(U)f_c=0`, while `M(0)=6`. The constant part is handled separately and never enters the residual set.

### 8.2 Empty kernel cover

Impossible for `nu_c`: `||f_c||_2^2=5/36>0`. Thus the nonconstant spectral measure is nonzero and must be covered by at least one kernel under the recovered finite-cover theorem.

### 8.3 Empty finite residual `S`

If `support(nu_c) subset ker chi_g`, then directly `U_g f_c=f_c`, hence `U_gf=f`; the recurrence lemma is unnecessary.

### 8.4 Residual point already in the kernel

Remove it. It is not genuinely exceptional.

### 8.5 Torsion residual eigenvalue

If `chi_g(s)` has finite order `q`, replacing `g` by `qg` enlarges the kernel and absorbs `s`. Minimizing residual cardinality therefore rules torsion out exactly, rather than assuming it away.

### 8.6 Coincident eigenvalues

Group residual atoms with the same value of `chi_g`. The recurrence uses distinct eigenvalues `gamma_j`, not distinct torus points.

### 8.7 Limiting support points

After residual minimization the finite set `S` is separated from the closed kernel. Any residual support point is isolated and therefore an actual atom. Any accumulation of support must lie in the kernel part and is already handled by the invariant projection.

### 8.8 Parallel rich kernels

They cannot both occur in a cardinality-minimal cover by Lemma 3.1. Thus the two-rich incidence graph genuinely comes from transverse section families.

### 8.9 Orbit-closure points that might fail to tile

Impossible because every local tiling equation is a closed cylinder condition, as proved in Section 2.

### B29 outcome

No boundary case forces a change in the source-level proof candidate.

## 9. Resulting proof dependency graph

Conditional only on the two source interfaces already checked in prior R7-02 work:

1. **finite spectral-kernel cover** for the centered origin indicator (Khetan spectral setup / Theorem 3.16 interface);
2. **prime-cardinality one-dimensional rigidity** for the three-point factor (Khetan Corollary 3.4 interface),

the remaining six-cell proof is now self-contained in R7-02:

- center the indicator and use the original mask;
- choose a minimum kernel cover and compress parallel kernels;
- at most one M-rich kernel -> finite residual -> absorb torsion -> finite-alphabet recurrence -> periodic configuration;
- two M-rich kernels -> Laurent restriction -> no singleton sections -> six-edge classification -> rank-one phase exclusion of `C6` -> `3 x 2` product;
- full affine span -> unimodular/gcd-one factors;
- direct fibre decomposition + prime 3-point rigidity + elementary 2-point rigidity -> coordinate period.

In particular the downstream proof no longer uses Khetan Theorem 3.12 (dilation), Lemma 3.1 (irrational phases), Theorem 3.11 (periodicity transfer), or Lemma 3.6 (product fibres). Removing those imports is a proof-risk reduction, not a new source-level metric value.

## 10. Dated source/literature status and nonclaims

Fresh checks on 2026-09-18 still return Khetan's arXiv:2607.09830 as the current primary source; its abstract explicitly says cardinality six is the possible exception below eight and is left open. Khetan's current research page still lists the paper as a 2026 preprint. Bounded exact-title, arXiv-id, author/cardinality-six, and orbit-closure searches did not surface a later explicit six-cell resolution. This is **negative evidence only**, not a proof of novelty or global openness.

This note is self-review. It does not count as P26 or OTHER-track independent audit evidence. Protocol status therefore remains `AUDIT OPEN`, with P26 `0/1` and distinct OTHER-track `0/1` unless a coordinator later records real independent audits.

## 11. What could still break the candidate

The remaining mathematically substantive audit surface is now concentrated in two imported source interfaces rather than six:

1. verify that the exact finite-kernel cover theorem applies to the centered spectral measure in precisely the form reused here (this should follow because centering only removes the trivial eigenspace, but an independent auditor should check the source statement line by line);
2. verify the exact one-dimensional prime-cardinality conclusion used for every `A`-tiling with `|A|=3` and `gcd(A-A)=1`.

If those two interfaces are confirmed, no additional unproved lemma is identified in this normal form. That statement is still a self-review conclusion, not an independent audit result.