# Matching negative association with an arbitrary unmatched-terminal graph

2 October 2026. Complete derived corollary, awaiting its separate independent
audit. The major matroid log-concavity input is an established theorem and
is credited explicitly below. This does not solve the general forest
negative-association or pair-correlation conjecture. Historical novelty of
the derived restricted-family corollary remains unverified.

## 1. The extension

Take a three-vertex weighted core with arbitrary nonnegative edge
activities, and rank-one spokes `z_(j,i)=a_j b_i` with `a_j>=0,b_i>0`.
Choose an arbitrary matching of terminal edges. Its endpoints have no
other terminal edges. On all remaining terminals one may put an
**arbitrary weighted graph H**, of arbitrary size and arbitrary
nonnegative activities. Then the complete vector of matching indicators
is negatively associated, also under arbitrary positive fields and after
conditioning any matching indicators and/or any edges of H to specified
states of positive conditional probability.

The earlier theorem allowed only isolated unmatched terminals. The new
ingredient is a bound on the exact normalized transfer of arbitrary H.
It uses known log-concavity of ordinary weighted forest partition sums
along a one-parameter affine line. No assumption about pairwise negative
correlation of H is made.

The theorem concerns ONLY the matching indicator vector. H's own edge
indicators need not be claimed negatively associated here. Conditioning
arbitrary spoke or core edges is not included. No extra terminal edge is
allowed incident to a matching endpoint.

## 2. Precise prior theorem: ordinary versus normalized polynomials

The input is N. Anari, K. Liu, S. Oveis Gharan and C. Vinzant,
*Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for
Independent Sets of Matroids*, arXiv:1811.01600v1, 5 November 2018.
The complete primary PDF, including the displayed definition and theorem
below, was checked:

https://arxiv.org/pdf/1811.01600

Theorem 4.1 (page 8 of the PDF, printed page 8) establishes complete
log-concavity of

    g_M(y,z_1,...,z_n)
       =sum_(I independent in M) y^(n-|I|) product_(i in I) z_i.  (1)

The coefficients in (1) are one. There is NO factorial normalization and
no factor such as `(n-|I|)!` or its reciprocal. Setting y=1 therefore
gives exactly the ordinary independent-set partition polynomial.
For a graphic matroid, independent edge sets are precisely forests, so
this is exactly the ordinary weighted unrooted-forest partition sum.

Lemma 2.2 (pages 5-6 of the PDF, printed pages 5-6) establishes preservation
of complete log-concavity under an affine coordinate map that sends the
nonnegative orthant into the nonnegative orthant. We use only ordinary
log-concavity from this conclusion. The statements here reproduce their
mathematical formulas and paraphrase their prose; the underlying theorem
is not a result newly proved in this campaign.

In particular, for any graph with fixed nonnegative activities on some
edges and activities `B a_j` on a specified set of edges, its ordinary
forest partition Z(B) is log-concave for B>=0. To see the exact
specialization, use the affine map

    y=1,
    z_e=w_e for fixed edges,
    z_j=B a_j for the selected edges.

It maps B>=0 to nonnegative coordinates, and (1) specializes to Z(B).
Zero activities cause no problem because the theorem and affine lemma
hold on the closed nonnegative orthant; alternatively take positive
limits. Since Z(B)>0, its log has an ordinary second derivative at B>0,
and

    (log Z)''(B)<=0.                                 (2)

This does NOT assert that off-diagonal entries of the logarithmic Hessian
are nonpositive; that stronger pairwise claim remains outside the prior
theorem. The present proof only uses the scalar derivative in (2).

## 3. An apex representation for the exact scalar background

For a forest F in H, contract its components C. Put

    x_C=sum_(j in C)a_j,
    d(x)=1+Bx,
    alpha(x)=x^2/d(x),
    gamma(x)=x^3/d(x)^2,

    D_F=product_C d(x_C),
    U_F=sum_C alpha(x_C),
    G_F=sum_C gamma(x_C).

Let w_F be the product of the H-edge activities in F. Define

    Z(B)=sum_(F forest in H) w_F D_F.                 (3)

This is EXACTLY the ordinary forest partition sum of H with one new apex
and apex-to-j edge activity B a_j. To prove it, restrict an apex forest to
H, obtaining an acyclic F. Each F-component can have at most one selected
apex spoke, because two would make a cycle through that component.
Conversely, choose either no spoke or one spoke from each component;
the resulting graph remains acyclic. Those choices have total activity
`1+B sum_(j in C)a_j=d(x_C)`. Multiplying over components gives (3).
Thus (2) applies to (3) with its actual unrooted-forest coefficients.

Normalize `w_F D_F` to a probability nu_B. Let

    U=E_(nu_B) U_F,
    Gamma=E_(nu_B) G_F+B Var_(nu_B)(U_F).             (4)

The commuting three-core operators satisfy `P^2=2BQ` and
`PQ=QP=Q^2=0`, so direct truncated expansion gives the exact background
transfer

    sum_F w_F D_F exp[U_F P+G_F Q]
       =Z(B) exp[U P+Gamma Q].                       (5)

In particular Gamma>=0. The variance in (4) is essential and is not
dropped or treated as an independent-forest product.

## 4. The new closure bound from scalar log-concavity

Let A=sum_j a_j, which is independent of F, and set

    W_F=sum_C x_C/d(x_C).

The identities

    U_F=(A-W_F)/B,
    U_F/B-G_F=sum_C x_C^2/[B d(x_C)^2]               (6)

follow term by term. Differentiating (3), using only its finite sum, gives

    (log Z)'=E W_F,
    (log Z)''=-E sum_C x_C^2/d(x_C)^2+Var(W_F).       (7)

Since `Var(U_F)=Var(W_F)/B^2`, equations (4),(6),(7) yield EXACTLY

    U/B-Gamma=-(log Z)''/B>=0.                       (8)

The inequality uses the credited prior theorem (2); all equalities use
the actual forest/apex partition (3). Consequently every arbitrary
unmatched-terminal graph gives a normalized background in the scalar
cone

    U>=0,  0<=Gamma<=U/B.                            (9)

The cone previously checked by a separate matching-mixture calculation
therefore holds for arbitrary H, including non-series-parallel H and
graphs with cycles of arbitrary size.

## 5. Applying the complete matching-vector proof

For clarity, the relevant steps of the previously completed proof are
recalled here with the new background substituted. Put

    B=b_1+b_2+b_3, J=b_1b_2b_3,
    S=1+p+q+r+pq+pr+qr,
    L=b_1b_2+b_1b_3+b_2b_3
       +p b_3(b_1+b_2)+q b_2(b_1+b_3)+r b_1(b_2+b_3).

Add every split matching endpoint to the normalized transfer (5). All
unmatched terminals, including isolated vertices, were already included
in H and must not be counted twice. Thus

    U_0=U+sum_(those terminals)alpha(a_j),
    Gamma_0=Gamma+sum_(those terminals)gamma(a_j),

with `0<=Gamma_0<=U_0/B`. Let D_0 be the positive scalar normalization,
including Z(B), and put

    F_0=S+LU_0+J Gamma_0+BJ U_0^2,
    M=L+2BJ U_0, K=2BJ.

For matching edge i with endpoint row weights a,b, define

    c_i=d(a+b)/[d(a)d(b)],
    delta_i=alpha(a+b)-alpha(a)-alpha(b),
    epsilon_i=gamma(a+b)-gamma(a)-gamma(b),
    theta_i=c_i w_i/(1+c_i w_i),
    t_i=delta_i theta_i,
    h_i=M+J epsilon_i/delta_i+BJ delta_i.

For positive endpoints the exact complete matching marginal has partition

    D_0 product_i(1+c_i w_i)
       [F_0+sum_i h_i t_i+K sum_(i<j)t_i t_j].        (10)

Thus it is the coordinatewise OR of an independent Bernoulli vector with
parameters theta_i and an independent forced subset Y of size at most
two, having weights

    Y empty: F_0,
    Y={i}: h_i t_i,
    Y={i,j}: K t_i t_j.

The established self-contained size-at-most-two lemma states that this
forced law is negatively associated if

    min_i h_i^2>=K F_0,
    2 min_i h_i>=max_i h_i.                          (11)

Its proof expands the two disjoint hit-event covariance numerators;
arbitrary increasing events reduce to singleton triggers because two
disjoint nontrivial events can co-occur on support<=2 only through one
triggering singleton each. The complete proof of that lemma and the
configuration-by-configuration OR identity is retained in
`forest_rank_one_core3_matching_negative_association_proof.md`, Sections
1,2,4; no general preservation conjecture is assumed.

For this graph, the original scalar verification is unchanged:

    0<delta_i<1/B^2,
    0<epsilon_i/delta_i<2/B,
    M<h_i<M+3J/B,
    BL>=9J,

    M^2-KF_0
      >=L^2-2BJ S+2J(BL-J)U_0+2B^2J^2U_0^2>0.

The last inequality uses (9) and the positive primitive-variable core
certificate from the completed proof. These bounds imply both (11).
The forced subset is therefore negatively associated. For increasing
functions on disjoint matching blocks, average first over the independent
Bernoullis; the two resulting functions of Y are increasing on disjoint
blocks. Applying its negative association proves the claimed inequality
for the matching vector. A zero endpoint produces an independent bridge
indicator and can be separated.

## 6. Conditioning, fields, and honest scope

Conditioning matching edges present contracts disjoint endpoint pairs and
sums their row weights; absent edges are deleted. The remaining matching
endpoints still have no other terminal edges. The contracted vertices can
be included as isolated vertices in the background graph. Conditioning
edges of H present contracts their acyclic required components and sums
row weights; absent edges are deleted. Parallel terminal edges aggregate,
and forbidden loops cannot be present under a positive-probability
conditioning. The resulting graph is again of the same type. The theorem
therefore applies after every indicated conditioning. Positive fields
merely change the permitted activities.

This strengthens the previous unbounded matching family by allowing an
arbitrary graph among its unmatched terminals. It does not put marked
matching edges in arbitrary positions of that graph and does not establish
negative association of H's indicators. In particular setting all spoke
rows small does not yield a solution of the general conjecture, because
the matching endpoints remain separated from all background terminal
edges by the explicit scope condition.

The log-concavity theorem, affine closure, and any special cases already
covered by known Rayleigh/SOS results are prior work. The new derived
corollary's historical priority and external review remain unverified.
