Model/effort: **GPT-5.6 Sol / reasoning effort UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# KHETAN-2026-EC6 — source-specific finite-fibre normal form

Target: Abhishek Khetan, *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2 (2026), cardinality-six exception in the abstract and Section 3.5.

Frozen source question: if `F subset Z^2` is an exact cluster of full affine span with `|F|=6`, must the orbit closure of every `F`-tiling contain a 1-periodic `F`-tiling?

Frozen metric: `E_EC6 in {0,1}`. Before this run: `1`. After this run: `1` (**NO MOVEMENT**). The point of this recovery iteration is not to manufacture a larger binary metric, but to replace the only stale proof interface in the canonical package by a strictly source-specific argument and then adversarially stress the remaining finite endpoint.

Methods executed: **B4 / B12 / B26**.

## 1. B4 — prove only the exact 3 x 2 endpoint, completely

The preceding proof candidate had already reduced the two-rich branch to a unimodular product `A x B` with

- `|A|=3`, `A` a complete residue system modulo `3`, `gcd(A-A)=1`;
- `|B|=2`, `B` a complete residue system modulo `2`, `gcd(B-B)=1`.

An earlier paper draft then invoked a stronger distinct-prime product theorem whose first branch used a bi-infinite formal-series cancellation. That stronger statement has a finite-fibre repair in an earlier artifact, but the source does not need the stronger theorem. The cleanest recovery is therefore to prove exactly the `3 x 2` endpoint with no formal series and no Khetan Lemma 3.7.

### Theorem (source-specific 3 x 2 product periodicity)

Let `A,B subset Z` satisfy the four bullets above. If `T subset Z^2` tiles `Z^2` by `A x B`, then

`(3,0)+T=T` or `(0,2)+T=T`.

### Proof

For each `y,x in Z`, define row and column fibres

`S_y = {x : (x,y) in T}`,

`T_x = {y : (x,y) in T}`.

Khetan Lemma 3.6 gives for every `n,m in Z`

`R_n := disjoint_union_{b in B} S_{n-b}`,

`C_m := disjoint_union_{a in A} T_{m-a}`,

where `R_n` is an `A`-tiling of `Z` and `C_m` is a `B`-tiling of `Z`.

By Khetan Corollary 3.4, prime cardinality plus gcd one yields residues

`r_n in Z/3Z`, `s_m in Z/2Z`

with

`R_n = 3Z + r_n`, `C_m = 2Z + s_m`.

We split on the binary sequence `s`.

### Case 1: `s` is constant

Say `s_m=s` for every `m`. If `(x,y) in T`, then for every `a in A`,

`y in T_x subset C_{x+a}=2Z+s`.

Thus every nonempty row has index `y=s (mod 2)`.

Fix a nonempty row `S_y` and an element `b in B`, and put `n=y+b`. In

`R_n = disjoint_union_{b' in B} S_{n-b'}`,

any nonempty summand has `n-b'=s (mod 2)`. Since the chosen row has `n-b=y=s (mod 2)`, we obtain `b'=b (mod 2)`. Because `B` is a complete residue system modulo `2`, there is exactly one element of `B` in that residue, so `b'=b`.

Therefore every other summand is empty and

`S_y = R_n = 3Z+r_n`.

Every nonempty row is a full coset of `3Z`, hence is invariant under horizontal translation by `3`; empty rows are invariant trivially. Thus

`(3,0)+T=T`.

### Case 2: `s` is nonconstant

Since `s_m` takes values in `Z/2Z`, nonconstancy means

`Image(s)=Z/2Z`.

A row `y` is nonempty iff `y mod 2` lies in `Image(s)`:

- if `(x,y) in T`, then `y in C_{x+a}=2Z+s_{x+a}` for every `a in A`, so `y mod2` lies in the image;
- conversely, if `y=s_m (mod 2)`, then `y in C_m=disjoint_union_{a in A} T_{m-a}`, so some anchor lies in row `y`.

Hence in this case **every row is nonempty**.

Write `B={b_0,b_1}`. Since `gcd(B-B)=1`,

`b_1-b_0 = +/- 1`.

For every `y`, the nonempty set `S_y` lies in both

`R_{y+b_0}=3Z+r_{y+b_0}` and `R_{y+b_1}=3Z+r_{y+b_1}`.

Two distinct cosets of `3Z` are disjoint, so

`r_{y+b_0}=r_{y+b_1}` for every `y`.

The indices differ by one. Therefore `r_n` is constant, say `r_n=r`.

Now every anchor has first coordinate `r (mod 3)`: if `(x,y) in T`, then for any `b in B`,

`x in S_y subset R_{y+b}=3Z+r`.

Fix a nonempty column `T_x`, choose `a in A`, and set `m=x+a`. In

`C_m = disjoint_union_{a' in A} T_{m-a'}`,

any nonempty column has index `m-a'=r (mod 3)`. Since the chosen nonempty column has `x=m-a=r (mod 3)`, we get `a'=a (mod 3)`. Because `A` is a complete residue system modulo `3`, this forces `a'=a`. Thus all other summands are empty and

`T_x=C_m=2Z+s_m`.

Every nonempty column is a full coset of `2Z`, hence invariant under vertical translation by `2`. Therefore

`(0,2)+T=T`.

The two cases are exhaustive. QED.

### Outcome

This proves precisely the product endpoint needed by the six-cell source. It is shorter than the previous stronger proposition and removes both audit-sensitive ingredients from the new part:

1. no cancellation of a finite mask against a bi-infinite formal Laurent series;
2. no invocation of Khetan Lemma 3.7.

The only imported product-fibre inputs are Khetan Lemma 3.6 and Corollary 3.4, both already checked directly against arXiv:2607.09830v2.

## 2. B12 — identify the conserved residue profile

The preceding proof is driven by an exact finite invariant rather than by analytic cancellation.

The one-dimensional prime-tiling theorem compresses every horizontal fibre union `R_n` to a residue `r_n in Z/3Z`, and every vertical fibre union `C_m` to a residue `s_m in Z/2Z`. These two residue profiles are not independent.

The exact dichotomy is:

- if `Image(s)` has size `1`, every occupied row is already an entire `3Z` coset;
- if `Image(s)` has size `2`, every row is occupied, and the two elements of `B` differ by one, so containment of the same row in two `R`-cosets forces `r_n=r_{n+1}` for all `n`.

Thus at least one of the two coordinate fibre systems collapses to a full periodic coset structure. This is the source-specific conserved object:

`binary vertical residue profile <-> horizontal residue rigidity`.

It also explains why cardinality six is easier than a general `p x q` product. For `q>2`, a nonconstant `s:Z->Z/qZ` need not hit every residue, so the statement "every row is nonempty" fails and the adjacent-index propagation no longer follows automatically. The six-cell `3 x 2` endpoint is a genuine sporadic simplification, not evidence for an unsupported general composite-cardinality theorem.

## 3. B26 — exhaustive sporadic-case hunt in the finite bridge

I rechecked the exact finite bridge for exceptional geometries rather than adding another checker.

### 3.1 Incidence graph

The previously executed exact certificate `paper_khetan_ec6/incidence_check.txt` enumerates all simple six-edge bipartite graphs whose two sides each have size two or three and whose vertex degrees are at least two. It leaves only:

- `K_{2,3}` / `K_{3,2}`;
- six labelled copies of `C6`.

No other finite incidence type exists under the proved hypotheses.

### 3.2 The C6 phase equations have no root-of-unity exception

After row/column factorization, the three row equations are

`z_2+z_3=0`,
`z_1+z_3=0`,
`z_1+z_2=0`,

with each `z_j` a nonzero complex phase. The first two give `z_1=z_2`; the third gives `2 z_1=0`, impossible over `C`. This contradiction does not depend on the order of the root of unity, distinctness of the phases, or an orthogonal coordinate choice. Hence there is no sporadic phase order that resurrects `C6`.

### 3.3 Nonorthogonal primitive directions cause no exception

For the surviving `K_{2,3}` geometry, write

`F=x_0+{a u+b v : a in A, b in B}`

in primitive transverse lattice directions. If `d_A=gcd(A-A)` and `d_B=gcd(B-B)`, then

`<F-F> = d_A Z u + d_B Z v`,

whose index in `Z^2` is

`|det(u,v)| d_A d_B`.

Full affine span makes this index one, so

`|det(u,v)|=d_A=d_B=1`.

Thus a skew/nonorthogonal lattice basis is harmless: it is automatically unimodular.

### 3.4 The factor residues have no sporadic alternative

For the two-point factor, gcd one forces its two points to differ by `+/-1`, hence it is a complete residue system modulo `2`.

For the three-point factor, the rich-section phase gives

`z^{a_1}+z^{a_2}+z^{a_3}=0`.

Three unit vectors sum to zero only as an equilateral triple. Hence their pairwise ratios are cube roots of unity, and at least one is primitive. From `z^{3(a_i-a_j)}=1` for all differences and `gcd(A-A)=1`, Bezout gives `z^3=1`; the sum excludes `z=1`. Therefore the three residues modulo `3` are distinct. No exceptional arithmetic pattern remains.

### 3.5 The at-most-one-rich branch was checked against the current source text

Khetan's written second case (Theorem 3.18 proof) uses the finite character-kernel cover, the common dilation-zero set, minimal finite exceptional set, Lemma 3.1, and Theorem 3.11. Its final step depends only on each exceptional phase being a non-root of unity; Lemma 3.1 explicitly handles multiplicative relations among the phases. No prime-power section-divisibility theorem is used after the case split. Replacing the dilation index family `gcd(alpha,p)=1` by the source-valid family `gcd(alpha,6)=1` therefore preserves the argument.

### B26 outcome

No source-valid sporadic exception was found. The finite bridge now has a smaller audit surface than before: six-edge classification, elementary phase exclusion, lattice-index normalization, the equilateral three-phase fact, and the finite `3 x 2` fibre theorem above.

## 4. Canonical package repair performed in this run

`paper_khetan_ec6/main.tex` was rewritten so that the theorem used at the product endpoint is the exact `3 x 2` result above. The obsolete formal-series paragraph was removed. `paper_khetan_ec6/README.md` was updated to describe only the current proof normal form and to preserve the distinction between mathematical proof candidate and protocol closure.

The package remains **PROVED CANDIDATE / AUDIT OPEN**. The mathematical metric stays `E_EC6=1`; this recovery removes a stale proof-object ambiguity but does not count as an independent audit or a second mathematical decision.

## 5. Fresh dated source check

Checked 2026-09-18:

- arXiv:2607.09830 remains v2, last revised 18 July 2026;
- the abstract still explicitly says that cardinality six is the possible exception below eight and is left open;
- Khetan's current research page still lists this preprint and no later six-cell resolution;
- bounded exact-title, arXiv-id, author-plus-cardinality-six and orbit-closure searches did not surface a later explicit source-matching resolution.

The last item is negative evidence only. It is not a novelty certificate and does not prove global current openness.

## 6. Remaining obligations and next methods

Known mathematical gap in the normalized source-level proof: **none identified by this self-review**.

Protocol obligations still missing:

- actual independent P26 end-to-end audit: `0/1`;
- actual distinct OTHER-track end-to-end audit: `0/1`.

This run is ordinary research, so with no binary-metric movement the ordinary unchanged count advances `3 -> 4`.

If the target remains active next run, do not repeat B4/B12/B26. Next useful methods: **B10 / B20 / B29**:

- B10 derandomize / make explicit: remove spectral shorthand from the rich-section bridge wherever possible and state every deterministic implication in audit order;
- B20 find why the obvious proof could fail: adversarially reconstruct the full source proof from only the imported theorem statements and locate any hidden measure/support quantifier mismatch;
- B29 add the points at infinity: inspect closure/support boundary cases (`nu({0})`, empty exceptional set, kernel intersections) as compactification edge cases rather than generic points.
