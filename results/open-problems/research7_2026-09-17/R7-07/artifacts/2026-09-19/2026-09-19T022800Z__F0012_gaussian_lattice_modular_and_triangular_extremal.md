Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 — Gaussian-lattice triangularization, split-prime invariants, and the extremal coordinate-triangular shear class

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 9, Conjecture 9.5. For the iid nonsymmetric Rademacher matrix `M_n`, the source conjectures

`P(Spec(M_n) subset Z[i]) = 2^{-(1+o(1)) n^2}`.

The R7-07 counterfamily already refutes this literal exponent and gives the frozen metric

`0 <= u_GI <= 1/2`,

where

`u_GI = liminf_n (-log_2 P(E_n))/n^2`,  `E_n={Spec(M_n) subset Z[i]}`.

This note does **not** move `u_GI`. It carries out the reserved methods **B12 / B24 / B8** and isolates a more arithmetic route to any matching `u_GI >= 1/2` theorem.

## 1. B12 — conserved arithmetic structure: integral Gaussian triangularization

### Idea before code

The previous run characterized `E_n` using complete `Q(i)`-rational invariant flags. That leaves an apparent denominator/height problem. Before trying to count rational flags, ask whether denominators are actually intrinsic. Because `Z[i]` is a Euclidean PID and every eigenvalue in the event lies in `Z[i]`, an eigenline can be chosen primitive and split off as a direct summand. Induction should therefore triangularize over `Z[i]` itself.

### Theorem 1.1 — unimodular triangularization over `Z[i]`

Let `R=Z[i]` and `K=Q(i)`. For `M in M_n(R)`, the following are equivalent:

1. `chi_M` splits into linear factors in `R[x]`;
2. there exists `U in GL_n(R)` such that `U^{-1} M U` is upper triangular over `R`.

In particular, for an ordinary integer matrix `M`,

`Spec(M) subset Z[i]`

if and only if `M` is triangularizable by a **Gaussian-unimodular** change of basis.

#### Proof

`(2) => (1)` is immediate from the diagonal entries.

For `(1) => (2)`, induct on `n`. Choose a root `lambda in R` of `chi_M`. Over the fraction field `K`, the kernel of `M-lambda I` is nonzero. Choose a nonzero vector in that kernel, clear denominators, and obtain `v in R^n\{0}` with

`Mv=lambda v`.

Divide all coordinates of `v` by their Gaussian gcd. The resulting eigenvector is **primitive**, meaning its coordinates generate the unit ideal of `R`. Over a PID, a primitive vector extends to an `R`-basis of `R^n`. Let `P in GL_n(R)` have this vector as its first column. Then

`P^{-1} M P = [[lambda, *],[0,B]]`

with `B in M_{n-1}(R)`. The characteristic polynomial of `B` is `chi_M(x)/(x-lambda)`, which again splits in `R[x]`. By induction, `B` is triangularizable by a matrix in `GL_{n-1}(R)`. Extending that change of basis by the first coordinate triangularizes `M` over `R`. QED.

### Corollary 1.2 — primitive invariant lattice flag

Every `M in E_n` preserves a complete flag

`0=L_0 < L_1 < ... < L_n=Z[i]^n`

in which each `L_j` is a rank-`j` free direct summand of `Z[i]^n`. Equivalently, the rational invariant flag from the previous run may always be chosen as the scalar extension of a **primitive integral Gaussian lattice flag**.

Thus uncontrolled rational denominators are not a genuine obstruction.

### Corollary 1.3 — split-prime local signatures

Let `M in E_n`.

* If `p == 1 (mod 4)` is a rational prime, choose either Gaussian prime `pi|p`. Reduction modulo `pi` sends `Z[i]` to `F_p`. Since the triangularizing `U` has Gaussian-unit determinant, its reduction is invertible. Therefore `M mod p` is triangularizable over `F_p`; in particular `chi_M mod p` splits completely into linear factors over `F_p`.
* If `p == 3 (mod 4)`, then `Z[i]/(p) = F_{p^2}`. The same argument triangularizes `M` over `F_{p^2}`. Hence over `F_p`, `chi_M` has no irreducible factor of degree greater than two.

These are exact necessary conditions at **every** rational prime, not generic-prime statements.

### Corollary 1.4 — discriminant is a signed square

Let `Delta(chi_M)` be the characteristic-polynomial discriminant. If `M in E_n`, then

`Delta(chi_M) in {+q^2,-q^2 : q in Z}`.

Repeated roots correspond to `q=0`.

Indeed, if the roots are `lambda_1,...,lambda_n in Z[i]`, then

`D=prod_{r<s}(lambda_r-lambda_s) in Z[i]`

and `Delta=D^2 in Z`. Write `D=a+bi`. Since `D^2=(a^2-b^2)+2abi` is rational integral, `ab=0`; hence `D^2` is either a nonnegative or a nonpositive integer square.

### Why this does not yet prove `u_GI >= 1/2`

A single split-prime condition is much too weak asymptotically: even for uniform random matrices over a finite field, complete splitting of a characteristic polynomial costs on the order of a factorial rather than `2^{Theta(n^2)}`. The value of Corollary 1.3 is instead that it supplies **many simultaneous arithmetic shadows of the same integral flag**. A successful upper bound would need to use consistency of those shadows across primes, not a union bound at one prime.

The exact small-dimensional computation in Section 3 shows that the pair of split primes `5` and `13` already happens to separate the true event through `n=4`; that coincidence is finite evidence only.

## 2. B24 — extremal object inside all coordinate-triangular shear constructions

### Idea before derivation

The original block-shear refutation used two triangular diagonal blocks with opposite coordinate orders. Determine whether that choice was just convenient or is actually extremal among **all** constructions in which the two ternary diagonal blocks become triangular after coordinate permutations.

Fix `n=2m` and the shear

`S=[[I,0],[I,I]]`.

Write

`M=[[A,B],[C,D]]`

in `m x m` sign blocks and impose the zero-lower-block equation

`C+D=A+B`.

Define

`X=(A+B)/2`,  `Y=(D-B)/2`.

Then `X,Y` have entries in `{-1,0,1}`. Entrywise, the equation `c+d=a+b` gives exactly five possible `(x,y)` states:

`(-1,0), (1,0), (0,-1), (0,1), (0,0)`.

The first four each have one sign-quadruple preimage `(a,b,c,d)` and `(0,0)` has two. Thus `supp(X)` and `supp(Y)` are disjoint and a pair `(X,Y)` has exactly

`2^{m^2-|supp X|-|supp Y|}`

sign-matrix preimages. Moreover

`S^{-1}MS = [[2X,B],[0,2Y]]`.

Hence any compatible pair for which `X` and `Y` have Gaussian-integral spectra generates exceptional sign matrices.

### Theorem 2.1 — exact two-order partition function

Let `sigma,tau` be permutations of `[m]`. Require `X` to be upper triangular in order `sigma` and `Y` to be upper triangular in order `tau`. Let `D(sigma,tau)` be their Kendall inversion distance, i.e. the number of unordered vertex pairs that the two orders orient oppositely. Then the exact weighted number of compatible `(X,Y)` pairs is

`Z(sigma,tau)`
`= 6^m * 12^{binom(m,2)-D(sigma,tau)} * 16^{D(sigma,tau)}`.      (2.1)

#### Proof

The weighted count factors over matrix positions.

At each diagonal position, both `X_ii` and `Y_ii` are allowed, with disjoint support. The weighted local sum is

`2 + 1 + 1 + 1 + 1 = 6`,

where the `2` is the multiplicity of `(0,0)`.

Now fix an unordered pair `{i,j}`.

* If `sigma` and `tau` order the pair the same way, one directed matrix position permits both `X` and `Y`, giving weighted sum `6`, while the reverse position permits neither and contributes `2`. Product: `12`.
* If they order the pair oppositely, at one directed position only `X` may be nonzero, giving weighted sum `2+1+1=4`; at the reverse position only `Y` may be nonzero, again `4`. Product: `16`.

Multiplying over the diagonal and all unordered pairs proves (2.1). QED.

### Corollary 2.2 — reverse orders are the unique extremal pattern up to ties of labels

Because `16>12`, `Z(sigma,tau)` is maximized exactly when

`D(sigma,tau)=binom(m,2)`,

i.e. when the two coordinate orders are reverses of one another. The maximum is

`T_m = 6^m 16^{binom(m,2)}`
`    = 4^{m(m-1)} 6^m`.                                      (2.2)

This recovers the first R7-07 fixed-shear family and shows that its opposite-order choice was **extremal in the entire two-permutation triangular class**, not an arbitrary design choice.

### Corollary 2.3 — permutation-triangular routes cannot beat the half exponent

A ternary matrix is permutation-upper-triangular exactly when its off-diagonal support digraph is acyclic. Every such matrix has integral spectrum because its eigenvalues are its ternary diagonal entries.

There are at most `(m!)^2` pairs of topological orders. Therefore the entire union of compatible pairs in which both `X` and `Y` are permutation-triangularizable has weighted cardinality at most

`(m!)^2 T_m`
`= 2^{2m^2 + O(m log m)}`.                                   (2.3)

The ambient `2m x 2m` sign cube has size `2^{4m^2}`. Thus **no construction confined to permutation-triangularizable ternary diagonal blocks can improve the leading source exponent below `1/2`**. Allowing all `2^m` signed diagonal shears from the preceding run changes (2.3) by at most another factor `2^m`, still `2^{o(m^2)}`.

This is a route-level no-go, not an upper bound on the full event `E_{2m}`. To beat the half exponent constructively, one must use diagonal blocks with genuinely cyclic support and Gaussian-integral spectrum, or leave the shear mechanism entirely.

## 3. B8 — exact discretization through `n=4` and exact ternary shear partitions through `m=3`

### Idea before code

The B12 split-prime invariants and B24 extremal theorem suggest two exact finite tests:

1. compare the true event with complete characteristic-polynomial splitting modulo the first split primes `5` and `13`;
2. count the full weighted ternary pair partition, not only its permutation-triangular subfamily, to see whether cyclic Gaussian-spectrum blocks actually appear at the smallest sizes.

All computations below are exact integer arithmetic. The checker is archived separately and was executed before this note was packaged for delivery.

### 3.1 Exact global exceptional counts

For all sign matrices of orders `1` through `4`, the exact counts are

| `n` | `#E_n` | total | exact probability |
|---:|---:|---:|---:|
| 1 | 2 | 2 | `1` |
| 2 | 12 | 16 | `3/4` |
| 3 | 256 | 512 | `1/2` |
| 4 | 18864 | 65536 | `1179/4096` |

The checker does not use numerical eigenvalues. It computes the characteristic polynomial by Newton identities and compares it with the exact set of monic integer polynomials whose roots are Gaussian integers inside the Gershgorin disk.

### 3.2 Split-prime filters

Let `S_p(n)` denote the sign matrices whose characteristic polynomial splits completely over `F_p`. Corollary 1.3 gives

`E_n subset S_p(n)`

for every prime `p == 1 mod 4`.

Exact enumeration gives:

| `n` | `#S_5(n)` | `#S_13(n)` | `#(S_5 cap S_13)` | `#E_n` |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 12 | 12 | 12 | 12 |
| 3 | 256 | 344 | 256 | 256 |
| 4 | 20592 | 26288 | 18864 | 18864 |

Thus, **for `n<=4` only**, the two-prime test `p=5,13` happens to be exact:

`E_n = S_5(n) cap S_13(n)` for `n<=4`.                       (3.1)

No asymptotic inference is claimed. An irreducible polynomial over `Q(i)` can split modulo many primes, so a fixed finite prime set cannot be promoted to a global theorem without a new arithmetic argument.

### 3.3 Full fixed-shear ternary partition

Let `G_m` be the ternary `m x m` matrices with Gaussian-integral spectrum and define

`W_m = sum 2^{m^2-|supp X|-|supp Y|}`,                       (3.2)

where the sum is over `X,Y in G_m` with disjoint supports.

By the local sign-quadruple correspondence above, `W_m` is exactly the number of sign matrices in the **sufficient fixed-shear subclass** obtained by requiring both diagonal blocks `2X,2Y` to come from Gaussian-spectrum ternary matrices.

Exact values are

| `m` | ternary matrices in `G_m` | `W_m` | reverse-order `T_m` |
|---:|---:|---:|---:|
| 1 | 3 | 6 | 6 |
| 2 | 61 | 1160 | 576 |
| 3 | 7911 | 6580992 | 884736 |

In normalized form,

`W_1 / 2^(2*1^2) = 3/2`,

`W_2 / 2^(2*2^2) = 145/32`,

`W_3 / 2^(2*3^2) = 25707/1024`.                              (3.3)

The full finite partition is already larger than the single reverse-order triangular extremizer once `m>=2`.

### 3.4 Exact acyclic-support subpartition

The checker also sums over **all** pairs where each ternary support digraph is acyclic, not merely one chosen pair of orders. The weighted values are

`W_1^DAG = 6`,

`W_2^DAG = 1008`,

`W_3^DAG = 4326912`.

Hence

`W_2^DAG/W_2 = 126/145`,

`W_3^DAG/W_3 = 5634/8569`.

So genuinely cyclic-support Gaussian-spectrum blocks already contribute positive weight at `m=2`, and their relative contribution is larger at `m=3`. A concrete witness is a two-cycle block such as

`[[0,1],[-1,0]]`,

whose eigenvalues are `+i,-i` and which cannot be made triangular by a coordinate permutation.

This is exactly the type of finite structure that escapes Corollary 2.3. It does **not** establish that the cyclic contribution has a larger `m^2` entropy exponent.

### 3.5 A useful block supermultiplicativity identity

The weighted partitions satisfy

`W_{a+b} >= 16^{ab} W_a W_b`.                               (3.4)

To see this, choose good compatible diagonal pairs of sizes `a` and `b`. Make `X` block upper triangular and `Y` block lower triangular. For each of the `ab` cross-block coordinate pairs, the upper rectangle contributes weighted sum `4` and the lower rectangle contributes `4`, hence `16`. Both resulting matrices are block triangular, so their spectra are the unions of the good diagonal spectra.

Equivalently, if

`D_m = W_m / 2^{2m^2}`,

then

`D_{a+b} >= D_a D_b`.                                       (3.5)

The exact `m=3` value gives `D_3=25707/1024`. Repeating a fixed finite block improves only the **linear** correction to the `n^2/2` exponent, not the frozen `n^2`-scale metric. In particular, (3.5) by itself cannot prove `u_GI<1/2` from any fixed `m` computation.

This explains precisely what a successful B8 continuation would need: a family of block sizes `m->infinity` for which

`log_2 W_m >= (2+delta)m^2`

for a fixed `delta>0`, or an upper argument showing no such `delta` is possible.

## 4. What moved mathematically, and what did not

The frozen source metric is unchanged:

`0 <= u_GI <= 1/2  ->  0 <= u_GI <= 1/2`.

So this is **NO SOURCE-METRIC MOVEMENT**.

The run nevertheless establishes three new exact facts:

1. the rational flag may always be upgraded to a primitive complete `Z[i]`-lattice flag, giving exact split-prime and signed-square-discriminant invariants;
2. the opposite-order triangular shear is exactly extremal among all pairs of coordinate triangularizations, and the entire permutation-triangular route is incapable of beating the half exponent at the `n^2` scale;
3. exact finite enumeration identifies the first cyclic-support escape from that no-go and shows `p=5,13` split tests exactly characterize the event through `n=4`.

The remaining global upper-bound problem is now sharper: either control the arithmetic entropy of primitive Gaussian lattice flags simultaneously across primes, or control the cyclic-support part of the ternary shear partition at growing `m`.

## 5. Prior-art boundary, checked 2026-09-19

The live arXiv record for Vu's survey still exposes only `v1` (6 May 2020). Fresh exact-title/conjecture/Gaussian-integral-spectrum searches did not surface a published source-matching refutation. This is negative evidence only; novelty remains **UNVERIFIED**.

Adjacent results checked:

* Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, DOI `10.1007/s00493-020-4657-0`, proves conditional-on-ERH high-probability irreducibility / large Galois group for iid sign matrices. It does not give the `2^{-Theta(n^2)}` exceptional-event rate here.
* Carla Groenland and Tom Johnston, *Intersection sizes of linear subspaces with the hypercube*, JCTA 170 (2020), 105142, arXiv:1810.02729, classifies large possible cube/subspace intersection sizes. It is directly relevant to fixed-linear-stratum extremality but does not control the union over arithmetic invariant flags.

No claim of novelty is based on search failure.

## 6. Exact checker

The executed exact checker and output are archived alongside this note. It uses only integer/rational arithmetic for every asserted count and ends with

`ALL_EXACT_F0012_DISCRETIZATION_CHECKS_PASS`.

Because the frozen metric is now unchanged for the **third consecutive ordinary research run**, the next R7-07 run is protocol-forced **STUCK1 thinking-only diagnosis** rather than a fourth ordinary lemma run.