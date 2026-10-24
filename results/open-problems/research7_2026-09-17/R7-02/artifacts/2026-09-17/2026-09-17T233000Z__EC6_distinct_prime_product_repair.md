Model/effort: **GPT-5.6 Sol / reasoning effort UNVERIFIED** — this is not GPT-6 at maximum; GPT-6 / maximum reasoning was requested, but no authenticated runtime information or binding model/effort selector is exposed.

# KHETAN-2026-EC6 — distinct-prime product theorem and source-interface certification

Target: Abhishek Khetan (2026), *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2. The source leaves the full-affine-span exact-cluster case `|F|=6` open in the abstract and Section 3.5.

Frozen source statement for R7-02: if `F subset Z^2` is an exact cluster of full affine span with `|F|=6`, then every `F`-tiling has a one-periodic `F`-tiling in its orbit closure.

This note is a **self-review/research artifact, not an independent audit**. Its main new theorem repairs the stronger distinct-prime product statement that the previous draft had attempted with an invalid formal-series cancellation. The repair is purely by fibres and uses exactly Khetan's Lemma 3.6, Corollary 3.4 and Lemma 3.7.

## 1. B6 — deform the repaired 3 x 2 fibre proof back to the full distinct-prime product statement

The preceding run proved the `3 x 2` case directly. The same mechanism in fact proves the intended theorem for two arbitrary primes and removes the defective cancellation entirely.

### Theorem 1 (distinct-prime product periodicity)

Let `p,q` be primes. Let `A,B subset Z` satisfy

- `A` is a complete residue system modulo `p` and `gcd(A-A)=1`;
- `B` is a complete residue system modulo `q` and `gcd(B-B)=1`.

If `T subset Z^2` is an `(A x B)`-tiling of `Z^2`, then `T` has a nonzero coordinate period. More precisely,

`(p,0)+T=T` or `(0,q)+T=T`.

The primes need not be equal.

### Proof

For every integer `y`, define the row fibre

`S_y={x in Z:(x,y) in T}`,

and for every integer `x`, define the column fibre

`T_x={y in Z:(x,y) in T}`.

Khetan's fibre decomposition, Lemma 3.6, applies to arbitrary finite one-dimensional factors `A,B`. Therefore, for every `n,m in Z`,

`R_n := disjoint_union_{b in B} S_{n-b}`

is an `A`-tiling of `Z`, and

`C_m := disjoint_union_{a in A} T_{m-a}`

is a `B`-tiling of `Z`.

Since `|A|=p` is prime and `gcd(A-A)=1`, Khetan's Corollary 3.4 gives a residue `r_n in Z/pZ` such that

`R_n=pZ+r_n`.

Likewise, since `|B|=q` is prime and `gcd(B-B)=1`, there is a residue `s_m in Z/qZ` such that

`C_m=qZ+s_m`.

We split according to the sequence `s=(s_m)`.

### Case 1: `s` is constant

Suppose `s_m=s` for every `m`. If `(x,y) in T`, then for every `a in A` one has

`T_x subset C_{x+a}=qZ+s`,

because `T_x` is the `a`-indexed summand of `C_{x+a}`. Hence every nonempty row has index

`y=s (mod q)`.

Fix a nonempty row `S_y` and choose any `b in B`. Put `n=y+b`. The decomposition

`R_n = disjoint_union_{b' in B} S_{n-b'}`

contains `S_y` as the `b`-summand. If another summand `S_{n-b'}` is nonempty, its row index must also be `s mod q`; thus

`n-b' = s (mod q)`.

But `n-b=y=s (mod q)`, so `b'=b (mod q)`. Because `B` is a complete residue system modulo `q`, exactly one element of `B` has that residue. Therefore `b'=b` and every other summand is empty. Consequently

`S_y=R_n=pZ+r_n`.

Thus every nonempty row is individually invariant under translation by `p`, while empty rows are invariant trivially. Hence

`(p,0)+T=T`.

### Case 2: `s` is nonconstant

Let

`I=Image(s) subset Z/qZ`.

Since `s` is nonconstant, `|I|>=2`.

We first identify the nonempty rows exactly. A row `y` is nonempty if and only if `y mod q` belongs to `I`.

- If `S_y` is nonempty, choose `(x,y) in T`. For any `a in A`, `y in T_x subset C_{x+a}=qZ+s_{x+a}`, so `y mod q` lies in `I`.
- Conversely, if `y mod q=s_m` for some `m`, then `y in C_m=qZ+s_m`. Since `C_m` is the disjoint union of the fibres `T_{m-a}`, some `T_{m-a}` contains `y`, and therefore row `y` contains the anchor `(m-a,y)`.

Now fix `y` with `y mod q in I`. Then `S_y` is nonempty. For every `b in B`,

`S_y subset R_{y+b}=pZ+r_{y+b}`.

A nonempty set cannot lie in two distinct cosets of `pZ`, so

`r_{y+b}=r_{y+c}`

for all `b,c in B` whenever `y mod q in I`.

Apply Khetan's Lemma 3.7 with prime `q`, complete residue system `B`, the set `I` of size at least two, and the function

`r: Z -> X`, `X=Z/pZ`.

The lemma explicitly permits an arbitrary codomain `X`. Its hypotheses are exactly the equalities just proved, and `gcd(B-B)=1`. Hence `r_n` is constant; write `r_n=r` for every `n`.

It follows that every anchor column has index `r mod p`: if `(x,y) in T`, then for any `b in B`,

`x in S_y subset R_{y+b}=pZ+r`.

Fix a nonempty column `T_x` and choose any `a in A`. Put `m=x+a`. In the decomposition

`C_m = disjoint_union_{a' in A} T_{m-a'}`,

any nonempty summand has column index `m-a' = r (mod p)`. Since `x=m-a` is nonempty and `x=r (mod p)`, the element `a` has the required residue `m-r mod p`. Because `A` is a complete residue system modulo `p`, it is the unique element of `A` with this residue. Therefore all other column-fibre summands are empty and

`T_x=C_m=qZ+s_m`.

Thus every nonempty column is invariant under translation by `q`, and empty columns are invariant trivially. Hence

`(0,q)+T=T`.

The two cases exhaust the possibilities. QED.

### Consequence

The defective formal-series route from the first proof draft is no longer needed even for the stronger distinct-prime theorem. In particular, the source-specific `p=3,q=2` product branch is closed by a theorem that is at least as strong as the intended proposition, but whose proof never cancels a finite convolution mask on a bi-infinite sequence.

## 2. B14 — full-affine-span normalization has no hidden arithmetic hypothesis

The six-cell two-rich branch produces a product in two primitive lattice directions. The exact normalization can be stated without reference to the spectral argument.

### Lemma 2 (index formula for an affine product)

Let `u,v in Z^2` be linearly independent primitive vectors, and let `A,B subset Z` be finite nonempty sets. Put

`F=x_0+{a u+b v:a in A,b in B}`.

Set

`d_A=gcd(A-A)`, `d_B=gcd(B-B)`.

Then

`<F-F> = d_A Z u + d_B Z v`,

and therefore

`[Z^2:<F-F>] = |det(u,v)| d_A d_B`.

In particular, if `F` has full affine span, then

`|det(u,v)|=1`, `d_A=1`, and `d_B=1`.

### Proof

Every difference of two points of `F` is

`(a-a')u+(b-b')v`,

so `<F-F>` is contained in `d_A Z u+d_B Z v`. Conversely, fix any `b_0 in B`. Differences between points with the same `b_0` generate

`<A-A>u=d_A Z u`.

Similarly, fixing any `a_0 in A` gives `d_B Z v`. Hence equality holds.

The lattice `Z u+Z v` has index `|det(u,v)|` in `Z^2`. Passing from `Z u+Z v` to `d_A Z u+d_B Z v` multiplies the index by `d_A d_B`, proving the displayed index formula. Full affine span makes the left-hand index equal to one. All three factors on the right are positive integers, so all are one. QED.

### Outcome

The `GL_2(Z)` change of coordinates in the R7-02 proof is fully justified by the source's full-affine-span hypothesis. It does not silently assume the desired periodicity conclusion or an extra gcd condition. In the `K_{2,3}` branch, full affine span itself forces the basis to be unimodular and both one-dimensional factors to have gcd one.

## 3. B22 — exact reason Khetan's prime-square section lemma does not directly extend to six cells

The source's prime-square proof uses a genuinely prime-power step that cannot simply be quoted at cardinality six.

For `|F|=p^2`, the dilation theorem provides the spectral vanishing equations for every integer `alpha` coprime to `p^2`, equivalently for every `alpha` coprime to `p`. Khetan's Lemma 3.15 assumes exactly that family. On a rational circle component with parameter `r=c/d`, the proof writes `p^m` for the highest power of `p` dividing `d` and chooses

`beta=d/p^m`.

By construction `beta` is coprime to `p`, so it is one of the available dilation indices. Substituting `alpha=beta` produces a primitive `p^m`-root-of-unity vanishing and hence `p`-divisible sections.

For `|F|=6`, the dilation theorem instead supplies only indices coprime to `6`. If one tries to imitate Lemma 3.15 with `p=2`, the same `beta=d/2^{v_2(d)}` may be divisible by `3` and therefore is not an allowed dilation. If one tries `p=3`, the analogous `beta=d/3^{v_3(d)}` may be even and is again unavailable. Thus the prime-square proof's section-divisibility engine has a real arithmetic mismatch at the mixed-prime cardinality `6`; one cannot infer `2`- or `3`-divisible sections by merely replacing `p^2` with `6`.

The R7-02 proof bypasses this exact obstruction rather than pretending it disappears. Its rich-direction lemma uses only `alpha=1`, which is always an allowed dilation. On a rational circle component containing infinitely many common zeros, the `alpha=1` Laurent polynomial has infinitely many unit-circle zeros and is identically zero. Grouping coefficients by parallel sections gives, for one common root of unity `zeta`,

`sum_{a in E} zeta^{<a,h>}=0`

for every nonempty section `E` in that rich direction. This is weaker than prime-power divisibility but is enough to forbid singleton sections. With only six points and two transverse rich directions, “every section has size at least two” forces the six-edge incidence graph into the finite alternatives `K_{2,3}` or `C_6`. That is exactly where the six-cell proof gains leverage unavailable in a general composite-cardinality argument.

This explains both why the source left six cells outside the prime-square theorem and why the present proof need not extend the full prime-power cyclotomic lemma to composite cardinality.

## 4. Primary-source interface certification performed in this run

The following imported interfaces were checked directly against arXiv:2607.09830v2, rather than against the older draft's paraphrases.

1. **Dilation theorem.** Khetan Theorem 3.12 states for arbitrary finite `F subset Z^2`: if `T` is an `F`-tiling, then the same `T` is an `alpha F`-tiling for every `alpha` coprime to `|F|`. Lemma 3.13 consequently gives all spectral vanishing equations for every such `alpha` on one common conull set. No prime-square hypothesis is present in Theorem 3.12 itself.

2. **Finite character-kernel cover.** Khetan Theorem 3.16 states for the spectral measure of a tiling that there is a finite `Delta subset Z^2\{0}` with support contained in `union_{g in Delta} ker chi_g`. The statement is not restricted to prime-square cardinality. The proof of the prime-square theorem then chooses a minimum such cover and separates the “at least two rich directions” and “at most one rich direction” cases.

3. **Prime one-dimensional fibre theorem.** Khetan Lemma 3.3 says that for a prime-cardinality tile `A subset Z`, any `A`-tiling is invariant under `p(A-A)`. Corollary 3.4 specializes `gcd(A-A)=1` to the exact conclusion that every `A`-tiling is one coset of `pZ`. This is precisely the form used above to write `R_n=pZ+r_n` and `C_m=qZ+s_m`.

4. **Fibre decomposition.** Khetan Lemma 3.6 is stated for arbitrary finite `A,B subset Z`, not just equal prime sizes. It gives the disjoint row- and column-fibre decompositions used in Theorem 1.

5. **Rigidity lemma with arbitrary codomain.** Khetan Lemma 3.7 fixes one prime `p`, a complete residue system `B mod p` with gcd one, a residue set `I` of size at least two, and explicitly permits `r:Z -> X` for **any set `X`**. Therefore in the distinct-prime theorem it is legitimate to use prime `q` and codomain `X=Z/pZ`; equality of the two primes is not a hidden hypothesis.

These checks remove the three source-interface uncertainties named in the previous R7-02 report. They are still self-review, not either required independent audit.

## 5. Status after this theorem

The repaired source-level architecture is now:

- dilation plus finite spectral-kernel cover;
- direct finite-spectrum recurrence in the at-most-one-rich branch;
- alpha=1 no-singleton-section theorem in each rich direction;
- exact six-edge incidence classification `K_{2,3}` or `C_6`;
- exact phase factorization excluding `C_6`;
- full-affine-span index normalization and rich-section phase forcing complete residue systems modulo `3` and `2`;
- Theorem 1 above, which closes the surviving product branch.

The frozen metric remains `E_EC6=1`: this run strengthens and source-certifies the already complete candidate but does not create a second value beyond source-level decision. Mathematical label remains **PROVED CANDIDATE** and protocol label remains **AUDIT OPEN**. Independent audits remain P26 `0/1` and distinct OTHER-track `0/1` unless a separate independent report appears after this artifact's snapshot.

The existing `paper_khetan_ec6/main.tex` should be treated as **superseded at its old distinct-prime formal-series step** until this fibre proof is integrated. The invalid cancellation identified in the previous run must not re-enter the final package. This artifact is the canonical replacement argument for that step.

## 6. Next mathematical attacks

The next ordinary research run, if still on this target, should not repeat B6/B14/B22. Three worthwhile new directions are B3/B15/B27:

- **B3, prove something stronger:** formulate and prove the strongest semiprime-cardinality two-rich theorem actually implied by “no singleton sections,” identifying exactly which part is special to six points.
- **B15, break symmetry deliberately:** stress the `K_{2,3}` phase argument in a completely nonorthogonal unimodular basis and with all row/column labels asymmetric, looking for a hidden dependence on an accidental coordinate choice.
- **B27, swap quantifiers:** prove a deterministic six-point theorem saying that any full-affine-span set carrying two transverse common section-vanishing phases has the `3 x 2` residue-product structure, independent of how those phases arose spectrally.

If that ordinary run again leaves `E_EC6` unchanged, the unchanged counter reaches three and the following run must be the protocol's thinking-only stuck diagnosis rather than another routine proof-interface pass.
