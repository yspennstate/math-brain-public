Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — affine-span conservation, exact cyclic surjection counts, and the growing-modulus barrier

Date: 2026-09-18 UTC.  
Slot: R7-07 Hard Problem New Methods, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Source-level target retained by the canonical claim: for every fixed `d>=3`,

\[
\Pr(A_{n,d}\text{ singular})=n^{-d+2+o(1)}.
\]

Frozen cubic metric:

\[
a_3:=\sup\{a:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative evidenced value before this artifact: `a_3 >= 1/4`.  
Value after this artifact: **`a_3 >= 1/4` — NO MOVEMENT.**  
Methods this iteration: **B5 ADD A PARAMETER AND DIFFERENTIATE IN IT / B12 FIND WHAT IS CONSERVED / B25 COUNT THE SAME THING TWICE.** The immediately preceding triple was B14/B21/B27.

Captured start snapshot: `700175f56e89122bb8b7e4e5c88f99683844818c`. Fresh master before delivery: `292f5b942c776142659c7e0582e26e06ce4b69bb`. The canonical `operations/claims/F0003.md` at the fresh master still names R7-07 exclusively.

## 1. Cumulative interface and idea before calculation

The previous run changed category from a single finite field to the integer cokernel. For squarefree `Q` it reduced real singularity to a mixed modular moment: if

\[
L_p(A):=\frac{|\ker(A\bmod p)|-1}{p-1},
\]

then for distinct primes `p_i`, real singularity implies `L_{p_i}(A)>=1` for every `i`, hence

\[
\mathbf 1_{\{\det A=0\}}\le \prod_iL_{p_i}(A).
\]

That observation made a product of four quarter-scale primes look attractive, but it left two questions mixed together:

1. which residue vectors are even *eligible* to be surjective modular kernel vectors of a regular symmetric adjacency matrix;
2. whether the random graph actually mixes sufficiently close to uniformly on those eligible vectors when the modulus grows with `n`.

This run separates them exactly. The first part has no hidden large-modulus entropy loss: regularity forces both a zero-sum law and full affine span, and the eligible cyclic vectors can be counted in closed form for every modulus. The real obstruction is therefore the second part, growing-modulus mixing. Reading the constants in Mészáros's fixed-group proof also identifies a natural `|V|^3 ~ n` obstruction inside that proof architecture.

## 2. B12 — two exact conservation laws for modular null vectors

Let `A=A(G)` be the adjacency matrix of a finite simple `d`-regular graph on `n` vertices. Let

\[
V=\mathbb Z/Q\mathbb Z,
\qquad \gcd(d,Q)=1.
\]

Regard a row vector `y=(y_1,...,y_n) in V^n` as a homomorphism `Z^n -> V`.

### Theorem 2.1 — zero sum and full affine span

If `yA=0` in `V^n` and `y` is surjective, then

\[
\boxed{\sum_{i=1}^n y_i=0\quad\text{in }V}
\]

and the smallest coset of a subgroup of `V` containing all coordinates `y_i` is the whole group `V`.

Equivalently, a surjective modular null vector is not merely group-generating; its coordinate set has **full affine span**.

#### Proof

Because `G` is `d`-regular,

\[
A\mathbf 1=d\mathbf 1.
\]

Multiplying `yA=0` by `1` on the right gives

\[
0=yA\mathbf 1=d\sum_i y_i.
\]

Multiplication by `d` is an automorphism of `V` because `gcd(d,Q)=1`, proving the zero-sum identity.

Now suppose all coordinates lie in a coset `gamma+H` of some subgroup `H<=V`. For every column `j`, exactly `d` entries of that column of `A` are `1`, so

\[
(yA)_j=\sum_{i\sim j}y_i\in d\gamma+H.
\]

Since `yA=0`, the coset `d gamma+H` contains `0`; hence `d gamma in H`. Again multiplication by `d` is invertible on `V`, so `gamma in H`. Therefore the purported coset is actually the subgroup `H`. If `H` were proper, all `y_i` would lie in a proper subgroup and could not generate `V`, contradicting surjectivity. Thus the minimal containing coset is `V`. QED.

This is the exact regular-graph conservation law that sits behind the `MinCos_q=V` condition in the finite-group mixing literature. It holds deterministically for every `d`-regular graph and every modulus prime to `d`; it is not an asymptotic statement.

### Theorem 2.2 — primitive real null vectors give many surjective modular null vectors

Let `A` be any singular integer `n x n` matrix and `Q>=2`. Then there exists a primitive integer row vector `x != 0` with

\[
xA=0,
\qquad
\gcd(x_1,...,x_n)=1.
\]

Its reduction `x mod Q` is a surjective homomorphism `Z^n -> Z/QZ`. Hence, if

\[
S_Q(A):=|\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/Q\mathbb Z)|,
\]

then

\[
\boxed{\mathbf 1_{\{\det A=0\}}\le \frac{S_Q(A)}{\varphi(Q)}}.
\]

#### Proof

Since `A` is singular over `Q`, its left kernel over `Q` contains a nonzero rational vector. Clearing denominators and dividing by the gcd of the resulting coordinates gives a primitive integral vector `x` with `xA=0`. Bézout gives integers `b_i` such that `sum_i b_i x_i=1`, so the residues of the coordinates of `x` generate `Z/QZ`. Thus `x mod Q` defines a surjective homomorphism annihilating the image of `A`, i.e. a surjection from `cok A` to `Z/QZ`.

For each unit `u in (Z/QZ)^*`, the row `ux mod Q` is another such surjective null vector. These `phi(Q)` vectors are distinct, because if `(u-v)x=0 mod Q`, applying the Bézout combination gives `u-v=0 mod Q`. Therefore `S_Q(A)>=phi(Q)` on singularity, proving the inequality. QED.

### Corollary 2.3 — the preceding four-prime mixed moment is exactly one cokernel moment

If `Q=prod_{j=1}^k p_j` is squarefree, then by the Chinese remainder theorem

\[
\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/Q\mathbb Z)
\cong
\prod_{j=1}^k
\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/p_j\mathbb Z)
\]

at the level of choices, so cardinalities multiply. Since

\[
|\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/p\mathbb Z)|
=|\ker(A^T\bmod p)|-1
=(p-1)L_p(A),
\]

we get the exact identity

\[
\boxed{
S_Q(A)=\varphi(Q)\prod_{p\mid Q}L_p(A).
}
\]

Consequently the B27 target from the previous run is not merely analogous to a cokernel moment; it *is* the normalized squarefree cyclic surjection moment:

\[
\boxed{
\mathbb E\prod_{p\mid Q}L_p(A)
=
\frac{\mathbb E S_Q(A)}{\varphi(Q)}.
}
\]

Thus any bound `E S_Q(A)<=n^{o(1)}` for a growing squarefree modulus immediately converts into a polynomial real-singularity bound of order `1/phi(Q)`.

## 3. B25 — exact count of all source-compatible cyclic test vectors

The Nguyen–Wood fixed-group argument counts surjective vectors satisfying the symmetric regularity constraints and obtains `|V|^{n-1}+o(|V|^n)` for fixed `V`; the displayed proof explicitly allows the little-o constant to depend on `|V|`. For a cyclic target group, the relevant candidate count can instead be evaluated exactly for every growing `Q`.

For `y in (Z/QZ)^n`, let `MinCos(y)` be the smallest coset of a subgroup containing all coordinates. Define

\[
N_{\rm aff}(Q,n)
:=
#\left\{y\in(\mathbb Z/Q\mathbb Z)^n:
\sum_i y_i=0,\;\operatorname{MinCos}(y)=\mathbb Z/Q\mathbb Z\right\}.
\]

### Theorem 3.1 — exact affine-span count

For every `Q,n>=1`,

\[
\boxed{
N_{\rm aff}(Q,n)
=
\sum_{g\mid Q}\mu(g)\,\gcd(n,g)\left(\frac Qg\right)^{n-1}.
}
\]

If `Q` is squarefree this factors as

\[
\boxed{
N_{\rm aff}(Q,n)
=Q^{n-1}
\prod_{p\mid Q}
\left(1-\frac{\gcd(n,p)}{p^{n-1}}\right).
}
\]

In particular, if no prime divisor of `Q` divides `n`,

\[
N_{\rm aff}(Q,n)
=Q^{n-1}\prod_{p\mid Q}(1-p^{-(n-1)}).
\]

#### Proof

Choose integer representatives of the coordinates and put

\[
D(y):=\gcd\bigl(Q,y_2-y_1,\ldots,y_n-y_1\bigr).
\]

The coordinates lie in a coset of the subgroup `g Z/QZ` iff `g` divides every difference, i.e. iff `g|D(y)`. Hence `MinCos(y)=Z/QZ` exactly when `D(y)=1`. By Möbius inversion,

\[
\mathbf 1_{D(y)=1}=\sum_{g\mid D(y)}\mu(g).
\]

Fix `g|Q`. Count zero-sum tuples for which `g|D(y)`. Such a tuple has all coordinates congruent to one residue `a mod g`; write uniquely

\[
y_i=a+gz_i,
\qquad
z_i\in\mathbb Z/(Q/g)\mathbb Z,
\]

with `a in {0,...,g-1}`. The zero-sum constraint is

\[
na+g\sum_i z_i\equiv0\pmod Q.
\]

It is solvable exactly when `g|na`. There are `gcd(n,g)` residues `a mod g` with that property. Once `a` is fixed, one linear equation in the `n` variables `z_i` over `Z/(Q/g)Z` leaves exactly `(Q/g)^{n-1}` choices. Therefore

\[
#\{y:\sum y_i=0,\;g|D(y)\}
=\gcd(n,g)(Q/g)^{n-1}.
\]

Summing with the Möbius weights gives the first formula.

If `Q` is squarefree, `gcd(n,g)` is multiplicative as a function of squarefree divisors `g`, so the divisor sum factors prime by prime:

\[
\sum_{g|Q}\mu(g)\gcd(n,g)g^{-(n-1)}
=
\prod_{p|Q}
\left(1-\gcd(n,p)p^{-(n-1)}\right).
\]

Multiplying by `Q^{n-1}` proves the second formula. QED.

### Corollary 3.2 — candidate entropy is not the large-modulus obstruction

If the prime divisors of squarefree `Q=Q_n` tend to infinity and their number is `n^{o(1)}`, then

\[
\frac{N_{\rm aff}(Q,n)}{Q^{n-1}}=1-o(1)
\]

uniformly, even when `Q` itself grows polynomially (or much faster) with `n`.

Indeed every factor differs from one by at most `p^{-(n-2)}`. Thus the space of deterministic source-compatible surjective test vectors has exactly the expected `Q^{n-1}` scale. There is no hidden factor such as `Q^{cQ}` coming from proper-coset aliases.

For the actual modular kernel problem, Theorem 2.1 says every surjective null vector belongs to this affine-span class. Therefore a growing-modulus proof may restrict to exactly the vectors counted by Theorem 3.1, without paying for any other surjective vectors.

## 4. The one-line pointwise-mixing reduction

For a random `d`-regular adjacency matrix `A`, define

\[
\rho_Q(n):=
\sup_{y:\,\sum y_i=0,\,\operatorname{MinCos}(y)=V}
Q^{n-1}\Pr(yA=0).
\]

(The supremum is over `V=Z/QZ`; impossible parity/graph constraints may simply give probability zero.)

### Proposition 4.1

For `gcd(d,Q)=1`,

\[
\boxed{
\mathbb E S_Q(A)
\le
\rho_Q(n)\frac{N_{\rm aff}(Q,n)}{Q^{n-1}}
\le \rho_Q(n).
}
\]

Consequently

\[
\boxed{
\Pr(\det A=0)\le\frac{\rho_Q(n)}{\varphi(Q)}.
}
\]

#### Proof

Write the expected number of surjective modular null rows as

\[
\mathbb ES_Q(A)
=
\sum_{y\;\mathrm{surjective}}\Pr(yA=0).
\]

By Theorem 2.1, a term can be nonzero only if `sum y_i=0` and `MinCos(y)=V`. There are exactly `N_aff(Q,n)` such candidates, and by definition each has probability at most `rho_Q(n)Q^{-(n-1)}`. This proves the first display; Theorem 2.2 gives the second. QED.

This isolates the sharp missing theorem in its smallest form: one does **not** need a full cokernel distribution for growing `Q`. It is enough to prove

\[
\rho_Q(n)=n^{o(1)}
\]

for one modulus `Q` of the desired polynomial size.

## 5. B5 — add the modulus-growth exponent and read the active barrier

Write

\[
Q=n^{\theta+o(1)}
\]

with `Q` squarefree, odd and prime to `d`, and assume `phi(Q)=Qn^{o(1)}` (true, for example, for a fixed number of polynomial-size primes). Proposition 4.1 gives the implication

\[
\rho_Q(n)=n^{o(1)}
\quad\Longrightarrow\quad
\Pr(A_{n,3}\text{ singular})\le n^{-\theta+o(1)}
\quad\Longrightarrow\quad
a_3\ge\theta.
\]

Thus the modulus exponent `theta` is a literal continuation parameter for the frozen metric. The cumulative one-prime proof reaches `theta=1/4`; the source endpoint would require total modulus `Q=n^{1-o(1)}` with controlled mixed modular dependence.

Now inspect the closest classical finite-group machinery rather than assuming it is uniform. Mészáros, *The distribution of sandpile groups of random regular graphs* (arXiv:1806.03736, 2020), explicitly fixes the finite group `V`: Section 2 states that the constants may depend on `V` and that no uniformity over `V` is claimed; Section 6 supplies uniformity in the degree `d`, not in `|V|`.

Two displayed steps expose what happens if one nevertheless tries to make that architecture uniform in `Q=|V|`.

### 5.1 Occupancy obstruction in the undirected matching construction

Mészáros Lemma 7.7 assumes

\[
m_q(c)>10|V|^2=10Q^2
\qquad\text{for every }c\in V.
\]

A balanced/typical vector has

\[
m_q(c)=\frac nQ+o(n/Q).
\]

Therefore this step itself requires, asymptotically,

\[
\frac nQ\gg Q^2,
\qquad\text{i.e.}\qquad
\boxed{Q^3\ll n.}
\]

So the proof mechanism cannot simply be pushed unchanged to the four-quarter-prime modulus `Q=n^{1-o(1)}` proposed last run. Its natural edge is `theta=1/3`.

### 5.2 Non-typical union-bound obstruction

Earlier in the proof, Mészáros fixes

\[
\tfrac12<\alpha<\beta<\gamma<\tfrac23.
\]

The non-typical estimate contains suppression

\[
\exp\{-c n^{2\eta-1}\}
\]

while the number of permutation equivalence classes is bounded on the `n^{Q+1}` scale. Making this union bound uniform would require at least

\[
(Q+1)\log n=o(n^{2\eta-1}).
\]

Since `eta<alpha<2/3`, the largest possible exponent on the right is strictly below `1/3`. Hence this part of the proof again points to

\[
Q\le n^{1/3-o(1)}
\]

as the outer edge of the unchanged fixed-group architecture.

These are **necessary conditions for directly uniformizing those displayed proof steps**, not a theorem that the whole Mészáros argument is uniform up to `n^{1/3}`. Several constants elsewhere are explicitly allowed to depend on `V`, so claiming sufficiency would be circular and is not done here.

### 5.3 What survives from the previous four-prime plan

The previous run's four-prime idea remains algebraically exact through Corollary 2.3, but the literature route proposed for controlling it is now ruled out in that form. The useful revised milestone is:

> Establish `rho_Q(n)=n^{o(1)}` for one squarefree cyclic modulus `Q=n^{1/3-o(1)}` directly in the **uniform simple cubic graph** model.

By Proposition 4.1 this would move the frozen metric from `1/4` to `1/3-o(1)` without requiring full cokernel convergence, and `1/3` is the first growth scale suggested by the closest matching-model architecture after the exact candidate count has been removed from the problem.

## 6. Literature reconciliation, dated 2026-09-18

1. **Vu (2020/2021).** The source sharp-rate problem remains distinct from the already solved `o(1)` nonsingularity conjecture. The public MathDB record refreshed in September 2026 likewise distinguishes solved nonsingularity from the still-unknown sharp rare-event rate.
2. **Huang (2018).** The published finite-field route gives a polynomial singularity bound; R7-07's cumulative artifacts strengthen the cubic exponent internally to `1/4`, but no claim is made that this strengthening is in the literature.
3. **Mészáros (2018/2020).** The finite-group mixing theorems are stated for fixed `V`. The paper explicitly says no uniformity over `V` is claimed; its later uniformity section concerns degree `d`. Lemma 7.7 contains the `m_q(c)>10|V|^2` hypothesis used above.
4. **Nguyen–Wood (2018).** Their cokernel-moment calculation uses Mészáros mixing. For odd cyclic `V`, `wedge^2 V` is trivial, so the symmetric target set has size `|V|^{n-1}`; their count of source-compatible surjections is `|V|^{n-1}+o(|V|^n)` with the little-o constant allowed to depend on `|V|`. Theorem 3.1 above replaces that particular counting step by an exact growing-`Q` formula, but does not supply growing-`Q` mixing.
5. A bounded search on 2026-09-18 did not locate a later theorem proving Vu's sharp undirected exponent `d-2`. This is negative evidence only, not an openness certificate.

## 7. Exact failures / remaining gap

- **B5 outcome:** the growth parameter `theta=log Q/log n` converts any growing-modulus pointwise mixing theorem directly into the same lower bound on `a_3`, but inspection of the closest fixed-group proof shows an intrinsic `Q^3<<n` barrier before all constants are even tracked. No metric movement.
- **B12 outcome:** proved deterministic zero-sum and full-affine-span laws for every surjective modular kernel row, plus the primitive-null-vector inequality `1_sing <= S_Q/phi(Q)`.
- **B25 outcome:** exactly counted the source-compatible affine-spanning cyclic vectors, eliminating proper-coset candidate entropy as the multi-prime obstruction.

The unresolved object is now a single quantity:

\[
\boxed{
\rho_Q(n)=
\sup_y Q^{n-1}\Pr(A_{n,3}y=0)
}
\]

on zero-sum, full-affine-span `y`, for a polynomially growing squarefree cyclic modulus. The current one-prime machinery controls the aggregate first moment through `Q=n^{1/4-o(1)}`; this artifact does not prove `rho_Q(n)=n^{o(1)}` beyond that scale.

## 8. Next nonrepeating attack

Use **B3 / B20 / B28** next:

- **B3 PROVE SOMETHING STRONGER:** seek a switching theorem uniform over *every* zero-sum full-affine-span `y` at `Q<=n^{1/3-epsilon}`, which is stronger than the needed averaged moment but may induct on switch exposure.
- **B20 FIND WHY THE ALGORITHM FAILS:** run the natural sequential pairing/matching exposure analytically and identify the exact first residue profile where conditional mixing loses a polynomial factor.
- **B28 REPLACE FOR ALL WITH TYPICAL:** if the pointwise theorem is false, prove `rho_Q`-quality mixing outside an explicitly counted exceptional family and show that family contributes `n^{-1+o(1)}` or less.

No source-level closure is claimed. The target remains **PARTIAL / OPEN**.