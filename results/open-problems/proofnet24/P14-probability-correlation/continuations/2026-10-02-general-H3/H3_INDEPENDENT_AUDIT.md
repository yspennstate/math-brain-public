# Independent audit of the global fourth Rayleigh coefficient

2 October 2026. Auditor: probability branch parent, independently of the
draft author and of the heat branch's original numerical conjecture.

**Verdict: PASS.** I read `H3_CONDITIONAL_WARD_DRAFT.md` line by line and
found no mathematical gap in the theorem it states. The conclusion is the
global H3 electrical sum of squares under H0=H1=H2=0. It is a partial result
on the forest negative-correlation conjecture, not a proof of that full
conjecture, and this audit does not certify historical novelty.

## Scope of the checked theorem

For the forest polynomial Z, evaluated after multivariate derivatives at
z_g=lambda*c_g, let

    R_ef=H0 lambda^(2n-4)+H1 lambda^(2n-5)
         +H2 lambda^(2n-6)+H3 lambda^(2n-7)+...

Use the unit-current equality geometry and harmonic response rows from the
general H2 theorem. If the first three coefficients vanish, define the
auxiliary e and f response potentials from eta_e,g and eta_f,h by the boundary
Green operator and harmonic extension. Shift each potential to vanish on
the opposite port set, obtaining alpha_g and beta_h. The checked theorem is

    H3=tau^2 sum_{g,h,k} c_g c_h c_k
             [alpha_g(x_k) beta_h(y_k)-alpha_g(y_k) beta_h(x_k)]^2 >= 0.

The sums run over original graph edges. No conductance factors c_e,c_f
belong outside this Rayleigh formula. Indicator covariance acquires those
factors separately through Cov(X_e,X_f)=−z_e z_f R_ef/Z^2.

## Independent analytic checks

1. **Feature identity at all orders.** In a principal-minor rooted forest,
   each chosen vertex feature selects one rooted component; each selected
   edge joins its two distinct rooted components. Disjoint selected edge
   endpoints make the joined component pairs disjoint. Thus each resulting
   nonroot component has exactly one feature, with net signed multiplicity
   its number of vertices minus its number of edges, namely one. Conversely,
   choosing a vertex or an edge in each nonroot tree and deleting the chosen
   edges gives exactly the rooted forests counted by the minor. This proves
   Q4=<V^3>/6 and the all-order forest identity, with the ground component
   unmarked. There is no missing root-size factor.

2. **Local raw Ward identity.** For left derivatives and q_i=barpsi_i psi_i,
   both odd operators sum_i(1−t q_i)partial_psi_i and its barred analogue kill
   the deformed edge q(x−y)−t q_x q_y. Integrating interiors preserves the
   boundary identity because (1+t q_i)(1−t q_i)=1, so the integration-by-parts
   coefficient is independent of the differentiated interior field. The
   local Gaussian denominator has a marked-independent Schur complement;
   its determinant derivative is a scalar. Consequently the marked log
   score, though not necessarily the whole normalized local partition,
   satisfies the exact Ward identity.

3. **Ground caveat.** A fixed zero root field cannot be silently included
   in a uniform Ward operator. The draft correctly chooses r in A\C when
   both response spaces are nonzero. H2zero implies |A intersect C|<=1,
   whereas each nonzero response needs at least two ports. The f-side Ward
   operator therefore has no grounded port. The e second-score covariance
   vanishes since all f response potentials are zero on A. A singleton
   port instead gives exact forest factorization at that vertex and zero
   mixed Rayleigh difference. This handles the exceptional case directly.

4. **Second-order Ward sign.** Expanding Q_t U_f(t)=0 yields
   Dpsi u_f2=sum_i q_i partial_psi_i u_f1. If u_f1=constant+barpsi B_f psi,
   the zero row/column sums give Dbar Dpsi u_f2=barpsi B_f psi. Covariance
   lowering is D1=−Dbar Dpsi, so D1 u_f2=−barpsi B_f psi. This identity has
   neither a factor two nor an omitted quartic contribution. For two ports,
   the explicit quartic −B_11 q_1 q_2 supplies exactly this contraction.

5. **Source/covariance signs.** In the positive Gaussian convention,
   adding s q(eta) changes covariance to (T^-1+s eta^T eta)^-1 and its
   derivative is −T eta^T eta T. Thus a response potential constant k on
   the other port set gives the second-score covariance +k^2 tr(T B_f).
   This positive term is subtracted in the Rayleigh coefficient.

6. **Quartic third cumulant.** With eta_e T eta_f^T=0, the two source
   updates are independent rank-one covariance subtractions. For boundary
   linear fields x,y, the mixed source derivative of det(K_{x,y}) is
   [a(x)b(y)−a(y)b(x)]^2. This is precisely the third joint cumulant of
   q(eta_e),q(eta_f),q(x)q(y). The sign is positive and the coefficient is
   one. The original interaction has a minus sign, giving the negative
   unshifted wedge energy in the logarithmic mixed derivative. A bilinear
   third cumulant vanishes because the two whitened PSD response matrices
   have product zero.

7. **Activity powers.** An activity derivative is lambda^-1 times a
   conductance derivative. Rayleigh is minus Z squared times the mixed
   logarithmic derivative. Under H0=H1=H2=0 the first mixed log term is
   order t^3, so the multiplier F(t)^2 contributes only its constant term.
   The resulting power is lambda^(2n−7), with factor tau^2. The t^3
   coefficient is exactly the two second-score covariances plus the first
   tilt's third cumulant.

8. **General-source electrical square.** The auxiliary Laplacian charges
   are zero-sum contrasts supported on A and C. With root in A, b=0 on A
   and a=k on C. The wedge flow j=c(a_x b_y−a_y b_x) has divergence −k Lb.
   The b electrical flow i=c(b_x−b_y) has energy R and inner product
   <j,i>=−kR. Hence energy(j)−k^2R=energy(j+k i), which is exactly the
   shifted wedge square. This uses no dipole-only assumption and no
   nonpositive-off-diagonal assumption on either response matrix.

These checks agree with the child's independently written
`H3_CONDITIONAL_CUMULANT_INDEPENDENT_AUDIT.md` and
`LOCAL_MARKED_SCORE_WARD_INDEPENDENT_AUDIT.md`. The child's line-by-line
audit of both the full draft and `GENERAL_H3_ZERO_GEOMETRY_LEMMA.md` also
reported PASS.

## Independent finite exact certificates

`H3_response_wedge_heat.py/.json` checks seven full forest cases by exact
acyclic subset enumeration: K4 chains with four and five twin pairs, three
rational scaled-profile gadgets over a rank-one interface, a five-boundary
case, and a non-twin mirror-path support. The checks distinguish positive
H3 from a genuine H3zero case.

I added `H3_non_M_matrix_audit.py/.json`. Its e active region has four
vertices and three ports, with unequal conductances and a positive
off-diagonal response entry. A rank-one core connects it to a separate
two-port f region. Exact forest subset enumeration gives

    n=11, unmarked edges=24,
    tau=3582436804800,
    H0=H1=H2=0,
    H3=83106928972800000.

The electrical shifted-wedge formula gives exactly the same H3. The full
four polynomial coefficient arrays and the entire Rayleigh polynomial are
stored in the JSON, not merely the matching leading coefficient.

This audit uses a separately compiled DSU subset enumerator,
`forest_subset_integer_audit.cpp`. Forest coefficients are exact signed
128-bit integers; the invoking script proves the conservative bound
2^24*30^10<2^127 before calling the program. Coefficient convolution uses
Python arbitrary-precision integers. Thus no floating-point tolerance,
overflow assumption, Grassmann recurrence, or leading-coefficient identity
enters the forest side of this check.

The heat branch independently checked another n=11 non-M-matrix example
with 29 unmarked edges, using an exact frontier-connectivity forest dynamic
program independently cross-checked against subset enumeration. It obtained
H3=42689908537165440000, again matching the shifted wedge across all common
zero roots and several marked-edge weights. See
`H3_positive_offdiag_audit_heat.py/.json`.

Thus nine reported finite graph cases pass, with additional root/weight
variants. These tests verify examples and normalization; the general claim
rests on the algebraic proof above and in the final theorem file.

## Current source boundary and novelty status

The primary preprint by R. Altar Ciceksiz and Mohan Ravichandran,
*Negative Correlation for Forests and the q<1 Random-Cluster Model*,
arXiv:2610.00549v1, dated 30 September 2026,
<https://arxiv.org/html/2610.00549v1>, was reopened during this audit.
Its abstract and Section 4 analyze the two leading Rayleigh coefficients
H0,H1 and classify their joint zero geometry. Its Section 4.2 leaves the
H2 and higher degenerate regime for investigation; K4 chains exhibit
arbitrarily many leading zeros. Those prior H0/H1 results and equality
geometry are prerequisites, not contributions of the present continuation.

The forest Grassmann representation and orthosymplectic symmetry are also
established prior tools. Relevant primary sources include Caracciolo et al.,
*Fermionic field theory for trees and forests* (2004),
<https://arxiv.org/abs/cond-mat/0403271>, and Caracciolo, Sokal and Sportiello,
*Spanning forests and OSP(N|2M)-invariant sigma-models* (2017),
<https://discovery.ucl.ac.uk/10025167/1/forests_ON_v3gA.pdf>.
The direct Ward calculation in the proof is included for self-containment;
it should not be advertised as discovery of supersymmetry itself.

Targeted searches on 2 October 2026 for forest Rayleigh third/fourth
coefficients and arboreal-gas high-fugacity correlation did not locate this
specific H3 formula. Negative search evidence does not certify novelty.
An expert literature review is still needed before a publication claim.

**Proved scope after audit:** H3 is nonnegative whenever H0,H1,H2 vanish,
with the stated global SOS. A positive coefficient gives sufficiently-large
activity negative correlation. **Open remainder:** cases where all four
coefficients vanish, subsequent coefficients, and all positive activities.
