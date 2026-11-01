# Independent audit: weighted cactus apex real-rootedness and marked-pair consequence

**Date:** 3 October 2026  
**Verdict:** **PASS**, after the now-incorporated clarification that the two
copies of an articulation vertex carry distinct side variables whose sum is
the final shared variable. No mathematical counterexample or remaining proof
gap was found.

This audit concerns `cactus_apex_real_rooted_proof.md`, its dependence on the
weighted-cycle and four-core arguments, and the stated scope in
`CACTUS_APEX_SOURCE_AND_SCOPE.md`. I rederived the determinant and
one-vertex-sum algebra and wrote a separate exact checker,
`cactus_apex_real_rooted_k_independent.py`. It imports no author code.

## 1. Precise result audited

For a finite weighted cactus backbone `H`, nonnegative finite backbone
activities, and a nonnegative vertex profile `beta`, let `D_H(s;beta)` be the
forest partition polynomial after adjoining one apex and giving its spoke to
`x` activity `s beta_x`. The proof claims:

1. `D_H` has degree equal to the number of positive profile entries and all
   of its zeros are strictly negative;
2. the full multivariate apex-spoke polynomial is real stable, so its
   normalized spoke marginal is strongly Rayleigh and negatively associated;
3. the two disjoint external marked edges in the proportional four-row
   construction are negatively correlated, strictly exactly when all four
   row factors are positive and the contracted profile rank is at least two;
4. these conclusions persist under positive-probability cylinder
   conditioning of backbone edges.

The argument does **not** claim a determinant for an arbitrary graph, a
two-connected block with two independent cycles, nonproportional external
rows, or negative association jointly involving backbone or marked edges.

## 2. The normalization identity is exact

Property `DR` is

    D_G(z)=c det(K + sum_x z_x q_x q_x*),

with `c>0`, `K` Hermitian positive definite, and the `q_x` spanning the
ambient space. At `z=0`, the constant coefficient is `c det K`.

For any fixed vertex `x`, the coefficient of the single spoke `z_x` in the
literal forest polynomial is also the entire backbone forest partition
function: adding just that one edge to the new apex cannot make a cycle.
Jacobi's formula on the determinant side gives

    [z_x]D_G = c det(K) q_x* K^(-1) q_x.

Consequently

    q_x* K^(-1) q_x = 1.

There is no missing graph-dependent factor. This identity also survives a
congruence normalization. Explicitly,

    K + sum z_x q_xq_x*
      = K^(1/2) [I + sum z_x r_xr_x*] K^(1/2),
    r_x=K^(-1/2)q_x,

so the new positive constant is `c det K`, and `||r_x||^2=1`.

The independent checker builds 20 exact rational iterated leaf-lift systems
and verifies `q_x^T K^(-1)q_x=1` for every vertex in every system.

## 3. Cycle and leaf ingredients

### 3.1 Cycle block

For positive rim weights the monodromy root `rho` is independent of the
profile, and the quasi-periodic recurrence is similar, by the positive
diagonal weight `S`, to a Hermitian pencil

    A - s diag(beta).

The boundary adjointness condition is exactly

    |rho|^2 = product_i lambda_i(1+lambda_i),

so no profile enters `A`. Transfer reconstruction gives equality of the zero
sets of the two degree-`n` polynomials. On the open dense simple-spectrum
set their leading coefficients fix the proportionality; polynomial
continuity in the profile gives

    D_C(s;beta)=det(-A+s diag(beta)).

The previously proved negativity of every generalized eigenvalue forces
`A<0`, hence `K=-A>0`. This is a profile-uniform `DR` representation with
the coordinate vectors. The leading coefficient is exactly
`product beta_i`, because choosing every spoke and no rim edge is one forest;
there is therefore no omitted scalar.

A positive two-cycle is the parallel-edge case handled by the coincident-
neighbor cycle calculation. A zero rim activity deletes that edge and opens
the cycle into a forest. A one-cycle is a loop and never belongs to a forest,
so discarding it is exact.

### 3.2 Rank-one leaf lift

If a leaf `v` of edge activity `w` is attached at `u`, splitting on that edge
gives exactly

    D_(G+v)=(1+s gamma)D_G(beta)+wD_G(beta+gamma e_u).

With

    K'=diag(K,1+w),
    q'_v=(sqrt(w/(1+w))q_u,1),

the determinant lemma yields

    c det(K'+sB')
      =(1+w)D_G+s gamma[D_G+w c det(M)q_u*M^(-1)q_u],
    M=K+sB_beta.

Applying the same lemma to `D_G(beta+gamma e_u)` proves the displayed forest
recurrence coefficient by coefficient. Both sides are polynomial, so the
temporary inverse causes no singular-value exception. `K'>0`, and the last
coordinate of `q'_v` proves the required spanning property.

## 4. One-vertex sums

This is the new step, and I checked it in three independent ways: literal
component factors, block determinant algebra, and exact rational examples.

### 4.1 Shared-variable convention

After normalizing both sides to `K_i=I`, their shared vectors are unit and
may be rotated to the first coordinate. The final shared activity must be
split as

    z_u=z_u^(1)+z_u^(2).

This convention is essential. If the full same variable were inserted on
both sides, even gluing two isolated one-vertex graphs would incorrectly
produce `1+2z` instead of `1+z`. The final proof now states the distinct side
variables and their sum explicitly, so this former ambiguity is resolved.

For a fixed forest on side `i`, write its component factor at the shared
vertex as `P_i=1+z_u^(i)+X_i` and the product of all other factors as `R_i`.
Then `D_i=P_iR_i` and

    E_i=partial_(z_u^(i))D_i=R_i.

After identification the two shared components become one, with factor

    1+z_u^(1)+z_u^(2)+X_1+X_2=P_1+P_2-1.

Thus, forest by forest and then after summation,

    D_G=D_1E_2+E_1D_2-E_1E_2.

The subtraction is therefore exactly one copy of the configuration in which
neither side's shared component takes a spoke.

### 4.2 Schur determinant and constants

Write the normalized side pencils as

    A_i = [[a_i,b_i*],[b_i,C_i]].

Coordinate identification produces

    A = [[a_1+a_2-1,b_1*,b_2*],
         [b_1,C_1,0],
         [b_2,0,C_2]].

The `-1` removes the second copy of the common constant coordinate. At zero
activity, `a_i=1`, `b_i=0`, and `C_i=I`, so the constant matrix of `A` is
exactly the identity, not merely positive semidefinite.

Taking Schur complements gives

    det A = det C_1 det C_2
      [(a_1-b_1*C_1^(-1)b_1)
       +(a_2-b_2*C_2^(-1)b_2)-1].

The derivative with respect to the shared side variable changes only the
first diagonal coordinate, hence

    c_i det A_i=D_i,       c_i det C_i=E_i.

Multiplication by `c_1c_2` gives the component identity above with every
constant correct. Clearing denominators, or polynomial continuation, removes
the temporary invertibility assumption on the `C_i`.

The spanning assertion is also valid. If a vector in the complement of the
common coordinate is orthogonal to all projected nonshared side vectors, it
is orthogonal to those vectors and to the shared vector. Since the original
side vectors span, it must vanish. The two side complements together with
the common coordinate therefore span the glued space.

The independent checker verifies 12 abstract normalized Schur constructions
by exact determinant permutation expansion and 12 unrelated literal
cycle-at-articulation identities, including zero and nonzero splits of the
shared profile.

## 5. Cactus and disconnected closure

Every connected cactus has a block tree whose blocks are bridges or cycles.
A bridge block follows by one leaf lift from an isolated vertex, a cycle
block has `DR`, and repeated one-vertex sums attach the blocks. Disconnected
components use block-diagonal direct sums; the common-apex forest polynomial
factors because no backbone path connects distinct components. The constants
multiply and the embedded vectors still span.

For a positive profile, spanning gives

    B_beta=sum beta_x q_xq_x* > 0.

Thus every generalized root of `det(K+sB_beta)` is strictly negative. Zero
profile coordinates follow by a positive-profile limit; real-rootedness is
closed under coefficient limits. The degree is exactly the number `k` of
positive entries: no higher spoke degree exists, while the forest consisting
of all `k` positive spokes and no backbone edge gives a strictly positive
degree-`k` coefficient. The positive constant coefficient excludes zero,
and all positive coefficients exclude a nonnegative real root. Hence every
surviving root is strictly negative, including all boundary profiles.

The checker found the full degree and exactly that many negative real roots,
counting multiplicity by exact Sturm/gcd layers, in 12 genuine connected
multi-cycle cactus cases (figure-eight, chain, and three-cycle block-tree
shapes). These computations use literal forest partitions, not a constructed
cycle determinant.

## 6. Multivariate stability and its exact scope

For independent spoke variables in the open upper half-plane,

    Im(K+sum_x z_xq_xq_x*)=sum_x Im(z_x)q_xq_x*.

This is positive definite because every imaginary part is positive and the
vectors span. The pencil is nonsingular, proving real stability. Rank-one
coefficient matrices make the determinant multiaffine, and its forest
interpretation gives nonnegative real coefficients. The normalized spoke
coefficient measure is therefore strongly Rayleigh. The standard
Borcea--Branden--Liggett implication gives negative association, and the
class is preserved by positive spoke external fields and spoke coordinate
conditioning.

This statement is only about the spoke marginal after summing over backbone
forests. It does not establish negative association jointly with backbone
edges, with the two external marked edges, or for the four-row augmentation.
The proof and scope file now distinguish these claims correctly.

## 7. Four-core transfer and strictness

Sections 2--4 of
`forest_disjoint_rank_one_attachment_forest_backbone_proof.md` use only a
sum over backbone forests and their component masses; they never use the
assumption that the backbone graph itself is acyclic. Once

    D_H(s)=D_H(0) product_(j=1)^k(1+s x_j),  x_j>0,

is available, the Stieltjes expansions apply verbatim. The derivative
normalization also remains exact for an arbitrary backbone:
`D_H'(0)/D_H(0)=sum_x beta_x`, since a single apex spoke can be added to
every backbone forest.

The two Rayleigh brackets are sums of nonnegative terms. The first contains
`sum_(i!=j) alpha_i tau_j` and is strict exactly when `k>=2`. The unscaled
Rayleigh difference has the factor `abcd`. Therefore the marked-pair
inequality is strict exactly when `abcd>0` and `k>=2`; positive marked-edge
activities only contribute the standard positive covariance denominator and
do not change the sign.

The independent checker directly enumerates the full four-core augmentation
of a weighted figure-eight cactus and obtains a strictly positive Rayleigh
difference for a rank-two profile.

## 8. Backbone conditioning and minor closure

For a positive-probability cylinder event, the forced-present edges form a
forest. Their activity product is a common positive factor. Contracting
them and deleting forced-absent edges gives the conditional forest model;
parallel spokes created by contraction combine by addition, so the new
profile at a contracted vertex is the sum of the original profiles.

Cacti are minor-closed in the relevant multigraph convention. Deleting an
edge either preserves a block or opens a cycle. Contracting a bridge joins
two block trees at one vertex; contracting a cycle edge shortens that cycle,
possibly producing a parallel-edge two-cycle or loops. Loops are discarded
because no forest can contain them. None of these operations creates a
two-connected block with two independent cycles.

Consequently the cactus `DR`, stability, and marked-pair arguments apply to
every positive-probability conditioned minor. The strictness parameter is
the number of positive contracted profile sums. The independent checker
exhausts all `3^4=81` cylinder specifications of a compact cactus consisting
of two parallel-edge two-cycles sharing one articulation: 64 have positive
probability (32 strict, 32 equality), and 17 forced-cycle events are correctly
skipped as zero probability.

## 9. Exact verification record

Running

    python random_cluster_research/cactus_apex_real_rooted_k_independent.py

reports:

| Independent exact check | Cases |
|---|---:|
| `q_x^*K^-1q_x=1` leaf-lift systems | 20 |
| abstract Schur one-vertex sums | 12 |
| literal split-profile one-vertex sums | 12 |
| genuine multi-cycle cactus Sturm cases | 12 |
| full figure-eight marked graph | 1 |
| positive-probability cactus conditionings | 64 |
| zero-probability forced-cycle events skipped | 17 |
| counterexamples | 0 |

The author checker was also executed independently after inspection. It
reports 24 tree lifts, 24 unicyclic cases, 8 disconnected-pseudoforest cases,
12 one-vertex formulas, 12 multi-cycle cactus cases, 10 marked cases, 78
positive-probability conditionings, and 3 zero-probability events skipped.

At the time of this audit the independent artifacts have SHA-256 hashes:

    e4e16de27efd9349de095e1b72813141345dce9c25f31dab9b604edac224a23d  cactus_apex_real_rooted_k_independent.py
    bf2704d9073eeb2e5f9a2315e2ec3b5934b056b457ebd9c4e413b04f2cbb1e3a  cactus_apex_real_rooted_k_independent_results.json

## 10. Final assessment

The normalization, leaf recurrence, one-vertex coalescence, Schur constants,
spanning argument, cactus block-tree construction, multivariate stability,
four-core transfer, and conditioning closure are all correct. The sole issue
found during adversarial review was the potential same-variable reading of
the articulation formula; the proof has been patched to specify distinct
side variables summing to the final shared activity. With that correction,
the weighted-cactus theorem and its stated consequences pass this audit.

Finite exact checks corroborate but do not replace the analytic proof. This
is an internal mathematical audit, not an external priority determination or
peer review.
