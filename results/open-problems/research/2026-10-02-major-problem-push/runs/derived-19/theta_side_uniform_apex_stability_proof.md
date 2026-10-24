# A first non-cactus block: side-uniform `K_{2,3}` has a stable apex polynomial

3 October 2026. Exact analytic proof, independently audited beside this
file. This goes strictly beyond the cactus closure theorem: `K_{2,3}` is a
2-connected theta graph with two independent cycles. It is **not** a proof
for six arbitrary edge activities, all theta graphs, or the general forest
negative-correlation conjecture.

## Theorem

Let `H=K_{2,3}`, with degree-three-side vertices `0,1` and other vertices
`2,3,4`. Give the three edges incident with `0` common activity `p>0` and
the three incident with `1` common activity `q>0`. Add an apex `o`, give its
five spokes independent variables `z_0,...,z_4`, and define

    P_(p,q)(z)=sum_F product_(e in F intersect E(H)) w_e
                         product_(oi in F) z_i,          (1)

where the sum is over all forests of `H+o`, and `w_e` is `p` or `q` as
above. Then `P_(p,q)` is real stable.

Consequently, after arbitrary nonnegative spoke rescaling, normalization,
spoke external fields, and positive-probability spoke cylinder conditioning,
the marginal law of the five apex-spoke indicators is strongly Rayleigh and
negatively associated. For every nonnegative profile `beta`,

    D_(p,q)(s;beta)=P_(p,q)(s beta_0,...,s beta_4)       (2)

has only strictly negative real zeros and degree equal to the number of
positive profile entries.

The proportional-four-row, two-disjoint-marked-edge construction from the
cactus checkpoint therefore also has negative correlation for this
backbone at every **positive pair** of marked-edge activities. It is strict
exactly when all four row scalars are positive and at least two profile
entries are positive.

No assertion is made after conditioning on arbitrary **backbone** edges:
contractions of a theta block need not remain in the proved class.

## 1. Rayleigh reduction

For a real multiaffine polynomial, the multivariate Rayleigh criterion says
that real stability is equivalent to

    Delta_ij=(partial_i P)(partial_j P)-P partial_ij P >=0                (3)

for every pair `i,j` and every real specialization of the other variables.
The side-uniform graph retains the permutations of `2,3,4`, but generally
not the swap of `0,1`. Thus there are four pair orbits:

    (0,1),  (0,2),  (1,2),  (2,3).                     (4)

The exact forest enumeration in the companion checker constructs all 32
coefficients of (1) and verifies every identity below in `Q[p,q,z]`.

## 2. Four positive quadratic forms

Write `h=p+q+1`. For real `X,Y`, put

    Phi_A=(p+1)(q+1)(X^2+Y^2)+2pq XY,
    Phi_Q=(2pq+p+q+1)(X^2+Y^2)+2pq XY,                 (5)

    Phi_B=q^2(q+1)^2 X^2+2p^2q^2 XY+p^2(p+1)^2 Y^2,

    Phi_R=3q^2(q+1)^2 X^2
          +2pq(3pq-p-q-1)XY+3p^2(p+1)^2 Y^2.          (6)

The eigenvalues of the symmetric forms in (5) are respectively

    Phi_A: 2pq+p+q+1, h;
    Phi_Q: 3pq+p+q+1, (p+1)(q+1),                     (7)

so both are positive definite. The diagonal coefficients of `Phi_B` are
positive and its determinant is

    p^2q^2 h(2pq+p+q+1)>0.                             (8)

The diagonal coefficients of `Phi_R` are also positive, while its
determinant is

    8p^2q^2 h(3pq+p+q+1)>0.                            (9)

Hence all four forms are positive definite for `p,q>0`.

We use the elementary fact that a real quadratic
`Lr^2+Mr+N` is nonnegative on the real line if `L>0` and its discriminant
is nonpositive. Every degenerate leading coefficient is handled explicitly.

## 3. Endpoint--endpoint pair

Set

    X_3=z_3+h,  X_4=z_4+h.

Regard `Delta_01` as a quadratic in `z_2`. Exact expansion gives

    [z_2^2] Delta_01=pq Phi_A(X_3,X_4),                 (10)

    disc_(z_2)(Delta_01)
      =-4p^2q^2 h X_3^2 X_4^2 Phi_Q(X_3,X_4).          (11)

If `(X_3,X_4)` is nonzero, (7), (10), and (11) prove nonnegativity for
every real `z_2`. At `(X_3,X_4)=(0,0)`, direct substitution gives
`Delta_01 identically 0`. Thus `Delta_01>=0` everywhere.

## 4. The two endpoint--internal pairs

Regard `Delta_02` as a quadratic in `z_1`. Its leading coefficient and
discriminant are

    [z_1^2] Delta_02=p(p+1)X_3^2X_4^2,                 (12)

    disc_(z_1)(Delta_02)
      =-4p^2q^2 h X_3^2X_4^2 Phi_Q(X_3,X_4).           (13)

When `X_3X_4` is nonzero, this proves nonnegativity. The boundary identities
are

    Delta_02|_(X_3=0)=2pq^2(q+1)h X_4^2,
    Delta_02|_(X_4=0)=2pq^2(q+1)h X_3^2.               (14)

They cover every degenerate case.

For the other orbit, regard `Delta_12` as a quadratic in `z_0`. One obtains

    [z_0^2] Delta_12=q(q+1)X_3^2X_4^2,                 (15)

the same discriminant (13), and

    Delta_12|_(X_3=0)=2p^2q(p+1)h X_4^2,
    Delta_12|_(X_4=0)=2p^2q(p+1)h X_3^2.               (16)

Therefore both endpoint--internal Rayleigh differences are nonnegative.

## 5. Internal--internal pair

Set

    U_0=z_0+(3p+1),  U_1=z_1+(3q+1).

Regard `Delta_23` as a quadratic in `z_4`. Exact expansion gives

    [z_4^2] Delta_23=Phi_B(U_0,U_1),                    (17)

    disc_(z_4)(Delta_23)
      =-4p^2q^2 h^2 Phi_R(U_0,U_1).                    (18)

Equations (8), (9), (17), and (18) settle every nonzero `(U_0,U_1)`. At
the only degenerate point,

    Delta_23|_(U_0=U_1=0)=4p^2q^2h^2>0.                (19)

Thus the last orbit is nonnegative. The Rayleigh criterion and (4) prove
the theorem.

## 6. Consequences and strict roots

The polynomial is multiaffine with nonnegative coefficients by definition.
Real stability makes its normalized coefficient measure strongly Rayleigh.
Standard closure under nonnegative diagonal rescaling, specialization, and
conditioning gives the spoke-marginal conclusions.

For a profile with `k` positive entries, (2) preserves real-rootedness. Its
degree is exactly `k`, because the empty backbone and all `k` positive
spokes form a forest and give a positive leading coefficient. All surviving
coefficients are positive, so zero and nonnegative roots are impossible:

    D_(p,q)(s;beta)=D_(p,q)(0;beta)
                       product_(j=1)^k(1+s xi_j), xi_j>0.                (20)

The already audited four-core transfer identity applies to any backbone
whose one-apex polynomial has (20). It writes the marked Rayleigh difference
as sums of nonnegative Stieltjes brackets, strict for a positive pair of
marked activities exactly when the four row scalars are positive and
`k>=2`. This proves the marked-pair corollary without claiming strong
Rayleigh behavior of the marked or backbone edges.

## Verification and honest boundary

`theta_uniform_apex_stability_exact.py` enumerates all `2^11` edge subsets,
retains the 712 forests, reconstructs the 32-term polynomial, and checks 18
coefficient, discriminant, boundary, and positive-form identities exactly.
The adjacent JSON records a clean SymPy 1.14.0 run. A separate checker and
line-by-line audit were produced independently.

The three `p` edges and three `q` edges must each be equal. This symmetry is
used in (4) and in the shifted positive forms. An earlier numerical search
at `p=q=1` found no negative Rayleigh value; it merely suggested the exact
calculation and is not part of the proof. A two-terminal determinant-gluing
route stalled because its normalized terminal Gram matrix is not universal,
unlike the one-terminal block in cactus gluing. Six independent activities,
theta subdivisions, series-parallel closure, and the full famous forest
negative-correlation conjecture remain open.
