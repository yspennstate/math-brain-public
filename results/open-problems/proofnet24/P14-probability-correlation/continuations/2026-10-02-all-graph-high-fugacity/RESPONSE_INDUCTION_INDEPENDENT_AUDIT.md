# Independent audit of the response absorption induction

2 October 2026. This checkpoint audits the proposed local propagation lemma.
It does not assert that a famous conjecture has been solved or certify novelty.
The H2/H3 statements and their exact conventions are those in
`GENERAL_H2_SOS_PROOF.md`, `GENERAL_H3_SOS_PROOF.md`, and
`H3_WARD_IDENTITY_HEAT.md`. The local lemma below passes this independent
analytic audit. A complete global theorem should still be assembled and read
as a single proof before any public claim.

## 1. Intrinsic local setup avoids the grounding trap

Let I be a local interior and A=N(I) its full geometric port set. Keep every
port field free. Define the local Gaussian conditional partition

    M_I(t;psi_A)=<exp(t V_I)|psi_A>_I,
    U_I(t)=partial_e log M_I(t;psi_A),

where V_I contains vertex terms at I and quartic edge terms for every original
edge incident to I. The covariance is L_II^{-1}; the harmonic port rows are the
full rows on A. No global root is used in this definition. Assume the original
marked current is supported in I. Then every harmonic extension has equal
values at the endpoints of e, so varying e leaves the local Schur complement
and harmonic rows fixed.

The raw integral has the weighted vertex measure product_(i in I)(1+t q_i)
and the edge exponent sum_(xy incident I) c_xy F_xy(t), with

    F_xy(t)=(barpsi_x-barpsi_y)(psi_x-psi_y)-t q_x q_y.

The integration-by-parts argument in the Ward checkpoint works verbatim for
this arbitrary I. Hence the complete marked score obeys both deformed
translation identities Qpsi_t U=Qbar_t U=0 on the full free port variables.
One must not silently apply these identities across a grounded zero field.
Defining the local polynomial intrinsically first avoids that problem; global
grounding is performed only after the local identity has been established.

Suppose the first boundary-dependent coefficient is at order ell:

    U_I(t)=C(t)+t^ell Q_B+t^(ell+1)P+O(t^(ell+2)),
    Q_B=barpsi_A B psi_A,

where C(t) is scalar, B is PSD, B1=0, and range(B) is the full contrast space
on A. The already audited initial score supplies this hypothesis at ell=1.

## 2. Ward gives the next coefficient without a factorial

The coefficient equations of Q_t=Q_0-t sum_i q_i partial_psi_i give

    Qpsi_0 P=sum_i q_i partial_psi_i Q_B,

and the barred counterpart. Thus

    P=sum_(i<j) B_ij q_i q_j + R,

where R is invariant under both ordinary uniform odd translations on A.
There is no ell multiplier: these are ordinary coefficients of t^ell in the
score, and the deformed translation has exactly one factor of t. All scalar
coefficients drop out of these equations.

## 3. Absorb the response supports

Write B=sum_rho rho rho^T, with each rho an old-port contrast. The decomposition
can be any real Gram decomposition; no M-matrix property is required.
Assume the global equality geometry has supplied physical response potentials
a_rho satisfying

    L a_rho=rho on A,   a_rho=0 outside its response support W_rho.

The source is extended by zero off A. Let W=union_rho W_rho and I'=I union W,
and let A'=N(I') be the new geometric port set. Boundary values z on A' have
harmonic extension h into I'. Integration by parts gives

    rho^T h_A=sum_x a_rho(x)(Lh)(x)=0.

Indeed every nonzero a_rho lies in I', where Lh=0. Since the rho span every old
port contrast, all old port harmonic rows coincide with one row pi:

    p_s=pi for every s in A.

This argument remains valid if a zero-response old port is not absorbed.
The old interior harmonic rows are also pi by the maximum principle.

Let C be the covariance on the outer variables after eliminating I and before
conditioning on the new ports. Extended by zero at old ports that remain on
the new boundary, it has

    a_rho(x)=Cov(chi_x,rho^T chi_A),
    rho^T C_AA rho=sum_edges c_xy(a_rho(x)-a_rho(y))^2=:R_rho.

The second identity follows from the physical equation La_rho=rho and from
a_rho being zero outside I'. Charges at an unabsorbed old port do not cause a
problem: its potential is zero and its contribution to rho^T a is zero.

## 4. Conditional normalization and the exact next Gram

Successive Gaussian elimination gives M_I' as the conditional expectation of
M_I times the remaining interaction exponential. The outer Gaussian kernel is
fixed under variation of e because the old local Schur complement is fixed.
Equivalently,

    det L_I'I'=det L_II * det(outer Schur block),

and the second factor has zero marked derivative. Thus the enlarged score is
the tilted conditional average of the old score; there is no missing
boundary-dependent normalization term. Its coefficient at ell+1 is

    E[P]+Cov(Q_B,W_1),

up to a scalar, where W_1 is the first coefficient of the total interaction
tilt after eliminating I. Earlier scalar score coefficients remain scalar.

Because every old-port harmonic row is pi, Q_B is purely an interior
fluctuation bilinear; its conditional expectation is scalar. Likewise the
ordinary-translation-invariant remainder R is independent of the new boundary
fields: substituting psi_s=chi_s+pi psi_A' is exactly a uniform odd translation
on the old ports. Its conditional expectation is scalar at this order.

The Ward quartic contributes the new-boundary bilinear

    sum_(i<j) B_ij(C_ii+C_jj-2C_ij) Q_pi
      =-tr(C_AA B) Q_pi
      =-sum_rho R_rho Q_pi.

Here Q_pi=(barpsi_A' pi^T)(pi psi_A'), and the identity uses B1=0. Its fully
uncontracted quartic vanishes because Q_pi^2=0.

Only the quartic part of W_1 can give a boundary-dependent covariance with
Q_B. After eliminating the old I, its physical form is minus
sum_(xy incident I') c_xy q(tilde_psi_x)q(tilde_psi_y), where tilde_psi_x is the
old harmonic field if x belongs to I and the actual outer field otherwise.
On subsequently splitting the outer Gaussian these fields have new harmonic
part p_x psi_A' and fluctuation part chi_x. The earlier contractions contribute
a bilinear or scalar tilt. Wick differentiation in covariance direction
-a_rho a_rho^T gives the new-boundary bilinear

    sum_(rho,xy) c_xy delta_(rho,xy)^T delta_(rho,xy),
    delta_(rho,xy)=a_rho(x)p_y-a_rho(y)p_x.

A bilinear tilt gives only a scalar covariance because Q_B has no harmonic
boundary part. Consequently the entire new boundary-dependent coefficient is
the bilinear with matrix

    B'=sum_(rho,xy) c_xy delta_(rho,xy)^T delta_(rho,xy)
          -sum_rho R_rho pi^T pi.                    (1)

For a fixed rho and boundary h, the flow

    j_xy=c_xy(a_rho(x)h_y-a_rho(y)h_x)

has divergence (pi z)rho, because h is harmonic where a_rho is nonzero and
h has the value pi z at every old source port. The electrical flow
i_xy=c_xy(a_rho(x)-a_rho(y)) has divergence rho. Thus j-(pi z)i is a
circulation, orthogonal in the flow-energy inner product to i. Formula (1)
therefore equals

    B'=sum_(rho,xy) c_xy eta_(rho,xy)^T eta_(rho,xy),
    eta_(rho,xy)=a_rho(x)p_y-a_rho(y)p_x
                 -(a_rho(x)-a_rho(y))pi.             (2)

This proves PSD and shows that the first possible new nonconstant coefficient
is an ordinary bilinear at order ell+1. No factorial, marked conductance
factor, or unproved positive off-diagonal property is used.

## 5. The new matrix has the full geometric contrast range

For new boundary values z put k=h-pi z. If z is in ker(B'), every summand in
(2) is zero, so

    a_rho(x)k_y-a_rho(y)k_x=0 at every original edge.

On a connected component of the nonzero a_rho set, k/a_rho is constant.
Every such component meets an old source port A: if it did not, a_rho would
be harmonic there with zero boundary and hence zero by the maximum principle.
At that old port k=0. Thus k=0 throughout W_rho, and hence throughout W.
Every new port adjacent to W then has k=0 by an edge with nonzero a_rho.

Any remaining new port is adjacent to I but not W, and therefore belongs to
the old port set A. It already has k=0 because all old rows are pi. This is the
key point: it is unnecessary to prove that every new geometric port is
directly adjacent to the actual response-support union.

Hence z is constant on A'. Conversely constant values on A' have constant
harmonic extension on I', so all eta evaluations vanish. Therefore

    ker(B')={new boundary values constant on A'},
    range(B')=the full contrast space on A',
    rank(B')=|A'|-1.

The proof covers disconnected I' as long as its Dirichlet problem exists.
In the intended nontrivial marked-support recursion I' is connected anyway:
the old I is connected, and every response component meets a source port
adjacent to I.

## 6. Strict enlargement, one-port termination, and root check

If B is nonzero, some response a_rho is nonzero at an old port. Otherwise it
would vanish on all A and be harmonic on every component off A, and the
maximum principle would force it to vanish everywhere, contradicting its
nonzero charge. That old port lies outside I, so I' strictly contains I.

For a connected I', if an old port s remains on A', its row is the coordinate
identity e_s; all old rows equal pi=e_s. Positive harmonic exit probabilities
from any absorbed old port to every new geometric port then force A'={s}.
Thus in every continuing branch with |A'|>=2 all old ports were absorbed.
This also supplies the root choice requested in the direct grounded proof:
a new interface root is outside both old port sets. The intrinsic full-port
derivation above does not need this auxiliary root argument.

If A' is a singleton, the exact one-port Ward identity makes the entire marked
score boundary-constant: (1-tq_s)partial_psi_s U=0, and 1-tq_s is invertible in
the exterior algebra, as is its barred analogue. This is also the familiar
forest factorization at a one-vertex interface. It is an all-orders stop,
not merely vanishing of the latest response coefficient.

If both marked sides are propagated under vanishing cross trace and shifted
wedge, the audited support geometry makes the enlarged sides disjoint with
no edge between them. Each nonzero side strictly grows. Therefore a finite
graph admits only finitely many continuing enlargements before a positive
cross response or a one-port factorization occurs. This finite argument is
conditional on applying the cross-coefficient identities with the exact
intrinsic local score setup at every step; a complete global theorem must
explicitly state that invariant rather than invoke termination alone.

## 7. Independent direct local-score checks

`response_induction_local_audit.py` computes conditional marked scores from
explicit Fraction exterior algebra, Gaussian determinant moments, and a
rank-one marked covariance derivative. It does not use formula (2) to obtain
the scores. Five nested two-port examples pass:

| Complete bipartite layers | Interior rungs | First nonconstant order | Nonzero response eigenvalue |
|---|---|---|---|
| 1 | None | 1 | 1/8 |
| 2 | None | 2 | 1/128 |
| 2 | Conductance 2 | 2 | 1/512 |
| 3 | None | 3 | 1/2048 |
| 3 | Conductances 2,3 | 3 | 1/51200 |

In every case the leading nonconstant coefficient is exactly a positive
two-port contrast bilinear, all earlier coefficients are scalar, and the
next coefficient's quartic is exactly B_01 q_0 q_1 as required by Ward. Exact
outputs are in `response_induction_local_audit.json`.

These are finite tests, not a substitute for the general lemma or an external
review. No counterexample or algebraic gap was found in this audit. The most
important conditions to retain in the assembled proof are: full free local
port variables, full geometric contrast range, physical zero-sum source
charges, a fixed marked Schur complement, and the exact one-port stop rule.
