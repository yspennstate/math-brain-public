# Every weighted cactus backbone: apex real-rootedness and a forest-correlation consequence

3 October 2026. Complete analytic derivation, subject to the fresh audit
stored beside this file. This strictly extends the preceding arbitrary
weighted-cycle and forest-backbone results, but it does **not** cover a
2-connected block with two independent cycles or the full forest
negative-correlation conjecture.

## Theorem

Let `H` be any finite weighted cactus graph: every two simple cycles have at
most one vertex in common, equivalently every 2-connected block is a single
edge or a cycle. All edge activities are finite and nonnegative. Give its
vertices arbitrary nonnegative profile weights `beta_x`. Add an apex with
spoke activity `s beta_x` at `x`, and let `D_H(s)` be the ordinary
unrooted-forest partition polynomial. Then every zero of `D_H` is real and
strictly negative, and its degree is exactly the number of positive profile
entries.

More strongly, with independent apex-spoke variables `z_x`, the complete
multivariate polynomial is real stable. Hence the marginal law of the whole
apex-spoke indicator vector is strongly Rayleigh and therefore negatively
associated, including after arbitrary spoke external fields and spoke
cylinder conditioning. This does not assert negative association jointly
with backbone edges.

Consequently, add four new vertices with proportional spoke rows
`a beta,b beta,c beta,d beta` into `H`, and let their only mutual edges be the
two disjoint marked edges joining the first pair and the second pair. The two
marked indicators are negatively correlated at every positive pair of
marked activities. The inequality is strict exactly when `abcd>0` and at
least two profile entries are positive.

Both conclusions survive arbitrary positive-probability cylinder
conditioning of backbone edges. After contracting forced-present edges and
deleting forced-absent edges, strictness is determined by whether at least
two contracted profile sums are positive. No claim is made for general
series-parallel or bicyclic blocks, nonproportional spoke rows, or negative
association of the backbone/marked-edge family.

The proof has three ingredients: the cycle transfer gives a profile-uniform
positive-definite determinant; a rank-one lift preserves it when a leaf is
adjoined; and a one-vertex-sum lemma glues two such representations at an
articulation vertex. The block tree then covers every cactus.

## 1. Determinantal apex representations

Say a weighted graph `G` has property `DR` if there are a positive constant
`c`, a Hermitian positive-definite matrix `K`, and vectors `q_x`, one for
every vertex, spanning the ambient vector space, such that for every
nonnegative profile `beta`,

    D_G(s;beta)=c det(K+s B_beta),
    B_beta=sum_x beta_x q_x q_x*.                        (1)

The data may depend on the backbone weights, but not on the profile.
Taking `s=1` and varying `beta` on an open positive orthant shows that (1)
is equivalently the full multivariate spoke identity with independent
variables `z_x`; that polynomial form is used in the gluing step.
Every such representation automatically satisfies

    q_x* K^(-1) q_x=1.                                  (2)

Indeed, the constant term is `c det K`. The coefficient of one apex spoke at
`x` is the same quantity, because that spoke can be added to every backbone
forest. Differentiating (1) at the zero profile proves (2).

Disjoint unions preserve `DR` by block-diagonal direct sum and multiplication
of constants. An isolated vertex has `c=K=q=1`.

Property `DR` also proves the multivariate assertion directly. If every
`Im z_x>0`, the imaginary part of
`K+sum_x z_x q_xq_x*` is positive definite because the vectors span. The
matrix is therefore nonsingular, so its determinant is real stable. The
polynomial is multiaffine (each coefficient matrix has rank one) and has
nonnegative coefficients from its forest definition. Thus its normalized
coefficient measure is strongly Rayleigh; the negative-association and
conditioning statements are the standard Borcea--Branden--Liggett
consequences.

## 2. A weighted cycle has `DR`

Take positive rim activities first and use the notation of
`weighted_cycle_apex_real_rooted_proof.md`. At a zero of the cycle apex
polynomial, the monodromy multiplier is one of the two fixed numbers
`rho,conjugate(rho)` satisfying

    rho^2-2 Lambda rho+delta=0,
    |rho|^2=delta=product_i lambda_i(1+lambda_i).

The quasi-periodic second-order equation is

    L_rho x=s diag(beta) x.                              (3)

With `m_0=1` and `m_(i+1)=m_i/[lambda_i(1+lambda_i)]`,
`L_rho` is Hermitian in the `m`-weighted inner product. Put
`S=diag(sqrt(m_i))` and `A=S L_rho S^(-1)`. Transfer reconstruction in both
directions gives

    D_C(s;beta)=0 iff det(A-s diag(beta))=0.              (4)

On the open dense set of profiles where the generalized eigenvalues are
simple, these degree-`n` polynomials are proportional. Their leading
coefficients are respectively `product beta_i` and
`(-1)^n product beta_i`; hence, first densely and then by polynomial
continuity,

    D_C(s;beta)=det(K+s diag(beta)),   K=-A.              (5)

The preceding cycle theorem makes every generalized eigenvalue in (4)
negative. Since `diag(beta)>0`, `A<0` and `K>0`. Thus (5) is `DR`, with
standard coordinate vectors; crucially, `K` depends only on rim activities,
not on the profile. A zero rim activity opens the cycle and is covered by
the tree construction or continuity below. The unequal parallel-edge
two-cycle is covered by the explicit coincident-neighbor calculation in the
cycle proof.

## 3. Rank-one leaf-lift lemma

Suppose `G` has `DR`, and form `G+v` by adjoining a new leaf `v` to a vertex
`u` with edge activity `w>=0`. Then `G+v` has `DR`.

Write `gamma=beta_v`. Splitting according to the new edge gives exactly

    D_(G+v)(s;beta,gamma)
      =(1+s gamma)D_G(s;beta)
         +w D_G(s;beta+gamma e_u).                      (6)

Let `K'=diag(K,1+w)`, lift old vectors by `q'_x=(q_x,0)`, and put

    q'_v=(sqrt[w/(1+w)] q_u,1).                          (7)

For `B'=sum_x beta_x q'_x q'_x*+gamma q'_v q'_v*`, the matrix determinant
lemma gives

    c det(K'+sB')
      =(1+w)D_G+s gamma[D_G
        +w c det(K+sB_beta)q_u*(K+sB_beta)^(-1)q_u].     (8)

The same lemma in (1) gives

    D_G(s;beta+gamma e_u)=D_G
      +s gamma c det(K+sB_beta)q_u*(K+sB_beta)^(-1)q_u.  (9)

Thus (8) equals (6), as a polynomial identity also at singular values.
Moreover `K'>0`; the lifted old vectors span the old space and `q'_v` has
last coordinate one. This proves every clause of `DR`.

## 4. One-vertex sums preserve `DR`

Let `G` be the one-vertex sum of `G_1,G_2`, identifying `u_1,u_2` as `u`,
with otherwise disjoint vertices and edges. If both sides have `DR`, then so
does `G`.

Normalize each side at its shared vertex. Congruence by `K_i^(-1/2)` makes
`K_i=I`; by (2), the transformed `q_(u_i)` is a unit vector, so a unitary
change makes it the first standard vector. Congruence changes only the
positive constant. Split the shared profile arbitrarily as
`beta_u=beta_u^(1)+beta_u^(2)` and write the two pencils as

    A_i=[[a_i,b_i*],[b_i,C_i]].

Identify their first coordinates. Embed each nonshared vertex vector in its
side and use the single common vector `q_u=e_0`. The resulting pencil is

    A=[[a_1+a_2-1,b_1*,b_2*],
       [b_1,          C_1, 0],
       [b_2,          0, C_2]].                         (10)

Its constant matrix is the identity, hence positive definite. The embedded
vectors span: on each side, the projections of the nonshared vectors span
the complement of `e_0`, and the common vector supplies `e_0`.

It remains to match the forest polynomial. Give the two copies of the shared
vertex **distinct** side variables `z_u^(1),z_u^(2)` with
`z_u^(1)+z_u^(2)=z_u`; this is the variable version of the profile split
above. Let `D_i` be the multivariate apex polynomial of side `i` in its own
variables, and `E_i=partial_(z_u^(i))D_i`. For each fixed
side forest, `E_i` deletes the factor for the component containing `u_i`, so
it counts configurations in which that component has no apex spoke. After
identification, at most one of the two such components may contain a spoke.
Therefore

    D_G(z_u^(1)+z_u^(2))
      =D_1(z_u^(1))E_2+E_1D_2(z_u^(2))-E_1E_2.          (11)

The Schur complement of (10) gives

    det A=det C_1 det C_2
      [(a_1-b_1*C_1^(-1)b_1)
       +(a_2-b_2*C_2^(-1)b_2)-1].                       (12)

Since `c_i det A_i=D_i` and `c_i det C_i=E_i`, multiplying (12) by
`c_1c_2` gives exactly (11). Polynomial continuity removes the temporary
inverse assumption. This proves `DR` for a one-vertex sum.

## 5. All cactus graphs and all profiles

A cactus is obtained by arranging edge blocks and cycle blocks in a block
tree and repeatedly taking one-vertex sums. A single edge has `DR` by one
leaf lift from an isolated vertex; every cycle has `DR` by Section 2.
Section 4 therefore proves `DR` for every connected weighted cactus, and
direct sums handle disconnected cacti. Zero activities simply delete edges.
A loop may be discarded because no forest contains it.

For a positive profile, (1) has `K>0` and `B_beta>0`, so every zero is
strictly negative. With zero profile entries, positive perturbation and
coefficient limits preserve real-rootedness. The degree is exactly the
number `k` of positive entries: the empty backbone permits all `k` spokes,
so their positive product occurs in the leading coefficient. Positive
coefficients exclude zero and nonnegative roots. Hence

    D_H(s)=D_H(0) product_(j=1)^k(1+s x_j),  x_j>0.      (13)

## 6. Marked pair and conditioning

The four-core transfer identity in
`forest_disjoint_rank_one_attachment_forest_backbone_proof.md` is valid for
an arbitrary backbone. It reduces `EF-AC` to two explicit Stieltjes brackets
depending only on (13). The first is
`sum_(i!=j) alpha_i tau_j`; the second is the sum of the three nonnegative
families in equations (11)-(12) of that proof. Thus `EF-AC>=0`, strictly
exactly when `abcd>0` and `k>=2`. The standard two-marked-edge calculation
gives the asserted negative covariance.

The cactus class is minor-closed. Deleting forced-absent backbone edges and
contracting forced-present ones therefore leaves a cactus after loops are
discarded. Contraction adds profile weights on identified vertices. The same
proof applies after every positive-probability backbone cylinder
conditioning, and (13) gives strictness from positive contracted blocks.

## Verification, scope, and failed stronger inference

The companion exact verifier checks the leaf lift coefficient-by-coefficient
against literal forests, exact rational Sturm multiplicities on unicyclic,
disconnected-pseudoforest and genuine multi-cycle cactus cases, full marked
graphs, and recorded conditionings. A separate fresh audit rederives the
one-vertex-sum step and uses an independent checker. Finite calculations are
corroboration, not the proof.

The one-vertex sum glues blocks only at articulations. It does not cover a
2-connected block with cyclomatic number at least two, such as a theta graph,
because that requires an edge between already constructed vertices. Earlier
countersearch on denser graphs is numerical evidence only and cannot fill
this structural gap. The full famous forest negative-correlation problem
remains open.
