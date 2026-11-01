# Independent audit: rank-one weighted `K_{2,3}` apex stability

**Date:** 3 October 2026  
**Verdict:** **PASS.** The candidate theorem is correct for every
`p,q,a_2,a_3,a_4>0`. No counterexample or unhandled quadratic boundary was
found.

This audit was performed from the theorem statement only. It does not import
or rely on an author probe. The companion checker is
`theta_rank_one_apex_stability_k_independent.py` and its deterministic output
is `theta_rank_one_apex_stability_k_independent.json`.

## 1. The theorem audited

Let the endpoints of `K_{2,3}` be `0,1`, and let the three internal vertices
be `2,3,4`. For `j=2,3,4`, assign

    w_(0j)=p a_j,   w_(1j)=q a_j,

with all five parameters positive. Add one apex and give its five spokes
independent variables `z_0,...,z_4`. The claim is that the resulting
apex-spoke forest polynomial is real stable.

This is the rank-one activity family: the `2 x 3` matrix of backbone
activities is an outer product `(p,q)^T(a_2,a_3,a_4)`. Nothing in this audit
proves stability for a general positive `2 x 3` activity matrix.

## 2. Independent polynomial reconstruction

I enumerated the 64 backbone subsets, retained the 54 forests, and used the
component identity

    P(z)=sum_(A backbone forest) w(A)
           product_(C component of A)(1+sum_(i in C)z_i).               (1)

For a fixed backbone forest, an apex-spoke set is acyclic exactly when it
chooses at most one vertex from each backbone component, which proves (1)
directly. This construction produces all 32 spoke monomials. At
`p=q=a_2=a_3=a_4=z_i=1`, it counts 712 augmented forests.

Every spoke coefficient is a coefficientwise-positive polynomial in the
five backbone parameters. The checker also verifies exact equivariance under
simultaneously permuting the arm weights `a_2,a_3,a_4` and their spoke
variables `z_2,z_3,z_4`.

Consequently the ten spoke pairs reduce, under parameter/arm relabeling and
endpoint exchange `p<->q`, to three generic templates:

1. endpoint--endpoint;
2. endpoint--internal;
3. internal--internal.

The theorem is at fixed, possibly unequal arm weights, so this is not a
claim that all ten pairs lie in graph-automorphism orbits. Rather, each pair
is an instance of one of the three identities after relabeling the positive
parameters.

## 3. Two positive helper polynomials

Write

    s=p+q.

For two arm parameters `u,v`, define

    R(u,v)=(1+su)(1+sv)
      +pq[u^2+v^2+suv(u+v)].                           (2)

For three arms `a,b,c`, define

    Q(a,b,c)=(1+sa)(1+sb)(1+sc)
      +pq[a^2+b^2+c^2
           +s(a^2b+a^2c+ab^2+ac^2+b^2c+bc^2)
           +s^2abc(a+b+c)].                            (3)

Both are coefficientwise positive and hence strictly positive throughout
the parameter domain. They are the compact factors appearing in all four
binary-form determinants below.

In the generic templates let

    a=a_2, b=a_3, c=a_4.

Arm permutation then supplies the other cases.

## 4. Endpoint--endpoint template

Set

    X_b=z_3+sb+1,   X_c=z_4+sc+1.

Collect `Delta_01` as a quadratic in `z_2`. Independent differentiation of
(1) gives

    [z_2^2]Delta_01=pq Phi_(b,c)(X_b,X_c),              (4)

where

    Phi_(b,c)(X,Y)
      =c^2(cp+1)(cq+1)X^2
        +2pq b^2c^2XY
        +b^2(bp+1)(bq+1)Y^2.                           (5)

Its symmetric-matrix determinant is exactly

    det Phi_(b,c)=b^2c^2 R(b,c)>0.                     (6)

The first diagonal coefficient is positive, so `Phi_(b,c)` is positive
definite.

The discriminant is

    disc_(z_2)Delta_01
      =-4a^2p^2q^2 X_b^2X_c^2 Psi_(a;b,c)(X_b,X_c),   (7)

with

    Psi_(a;b,c)(X,Y)
      =c^2R(a,c)X^2
       +2pq b^2c^2(1+sa)XY
       +b^2R(a,b)Y^2.                                 (8)

Its determinant factors as

    det Psi_(a;b,c)
      =b^2c^2(ap+1)(aq+1)Q(a,b,c)>0.                  (9)

Thus the discriminant is nonpositive whenever the leading coefficient is
positive. The leading form vanishes only at `X_b=X_c=0`; exact substitution
there gives `Delta_01` identically zero in `z_2`. This covers the sole
degenerate point.

## 5. Endpoint--internal template and both axis boundaries

For `Delta_02`, collect in the opposite endpoint variable `z_1`. Exact
expansion gives

    [z_1^2]Delta_02
       =ap(ap+1)X_b^2X_c^2,                            (10)

and its discriminant is exactly the expression in (7). When both shifted
arm variables are nonzero, the usual positive-leading/nonpositive-
discriminant test proves nonnegativity.

The leading coefficient also vanishes when **either** shifted variable is
zero, so checking only their intersection would leave a real gap. The two
complete boundary expressions are

    Delta_02|_(X_b=0)
      =a b^2 p q^2(bq+1)[2+s(a+b)] X_c^2,             (11)

    Delta_02|_(X_c=0)
      =a c^2 p q^2(cq+1)[2+s(a+c)] X_b^2.             (12)

Every factor is positive except the displayed remaining square, so both
axes are globally nonnegative. At their intersection the value is zero.

For the endpoint-1 pair `Delta_12`, endpoint exchange gives

    [z_0^2]Delta_12=aq(aq+1)X_b^2X_c^2,               (13)

with the same discriminant (7), and boundaries

    Delta_12|_(X_b=0)
      =a b^2 p^2q(bp+1)[2+s(a+b)] X_c^2,

    Delta_12|_(X_c=0)
      =a c^2 p^2q(cp+1)[2+s(a+c)] X_b^2.              (14)

Equations (10)-(14) are the exact boundary checks requested in the task.
Arm relabeling proves all six endpoint--internal pairs.

## 6. Internal--internal template

For the pair of arms `a,b`, collect `Delta_23` in the unused arm spoke
`z_4`. Put

    U_0=z_0+p(a+b+c)+1,
    U_1=z_1+q(a+b+c)+1.

The leading coefficient is

    [z_4^2]Delta_23=ab Theta_(a,b)(U_0,U_1),           (15)

where

    Theta_(a,b)(X,Y)
      =q^2(aq+1)(bq+1)X^2
       +2abp^2q^2XY
       +p^2(ap+1)(bp+1)Y^2.                           (16)

Its determinant is

    det Theta_(a,b)=p^2q^2R(a,b)>0.                   (17)

The discriminant has the exact form

    disc_(z_4)Delta_23
      =-4a^2b^2c^2p^2q^2 Omega_(a,b,c)(U_0,U_1),      (18)

where `Omega` is a real binary quadratic. Writing

    Omega=q^2 E_q X^2+2pq KXY+p^2 E_pY^2,             (19)

the independent symbolic expansion finds 51 positive monomials in each of
`E_q` and `E_p`. The cross polynomial `K` need not be positive; determinant
positivity is the relevant condition. Exact factorization gives

    det Omega
      =p^2q^2[2+s(a+b)][2+s(a+c)][2+s(b+c)]Q(a,b,c)>0. (20)

Thus `Omega` is positive definite by Sylvester's criterion. The source
checker constructs `Omega` from (1), verifies that it has exactly the three
binary-quadratic monomials, verifies coefficient positivity of `E_q,E_p`,
and checks (20) as a polynomial identity over
`Q[p,q,a,b,c]`.

The leading form (15) degenerates only at `U_0=U_1=0`. At that point the
complete Rayleigh difference is

    Delta_23
      =abc^2p^2q^2[2+s(a+c)][2+s(b+c)]>0.             (21)

This proves the internal template, and arm permutations prove all three
internal--internal pairs.

## 7. Stability conclusion

For a real multiaffine polynomial, real stability is equivalent to

    Delta_ij(x)>=0

for every pair and every real specialization. Equations (4)-(21) establish
that property for all three generic templates, including every zero-leading
boundary. Arm permutations and endpoint exchange cover all ten pairs.
Therefore the rank-one weighted `K_{2,3}` apex-spoke polynomial is real
stable for every `p,q,a_2,a_3,a_4>0`.

## 8. Independent exact stress, roots, and marked graphs

In addition to the symbolic proof, the checker performs:

- 1,200 exact rational Rayleigh evaluations: 120 unrelated positive
  parameter choices, all ten spoke pairs, and real rational spoke
  specializations (including negative values). Every value is nonnegative;
  the smallest in this deterministic sample is `670453/62500000`.
- 24 exact rational profile-ray tests. Square-free factorization and Sturm
  counts find exactly one strictly negative root per positive profile entry,
  counting multiplicity.
- six directly enumerated proportional-four-row marked graphs. Four
  support-at-least-two profiles give strict marked Rayleigh inequality;
  support-one and support-zero profiles give equality.

The root consequence also follows analytically. Stability survives the
substitution `z_i=s beta_i`. The empty backbone supplies a positive
coefficient in every degree through the profile support size, so every real
root is strictly negative. The marked-pair consequence follows from the
previously audited four-core Stieltjes identity, which needs only this
negative-root factorization and not a cactus backbone.

## 9. Verification record

Run

    python random_cluster_research/theta_rank_one_apex_stability_k_independent.py

The deterministic result is:

| Check | Count |
|---|---:|
| generic symbolic identities | 18 |
| exact rational Rayleigh pair evaluations | 1,200 |
| exact profile/root cases | 24 |
| direct marked cases | 6 |
| strict marked cases | 4 |
| marked equality cases | 2 |
| counterexamples | 0 |

Artifact hashes at this checkpoint are:

    ba34c94053b68abe6ba02139d2d0c7ef35f9868d13fd678e1c373f3ffc5169d9  theta_rank_one_apex_stability_k_independent.py
    b30f557ad2b9816a9a7a903e19588e86b09c1354551c10c4e7a50091e4a53110  theta_rank_one_apex_stability_k_independent.json

## 10. Final assessment

**PASS.** The candidate theorem is valid. The endpoint--internal leading
coefficient does vanish on two full axes, but the exact expressions
(11)-(14) are nonnegative and close that potential gap. The
internal--internal discriminant form is positive definite by the explicit
factorization (20), including cases where its cross coefficient is negative.

No claim is made for a non-rank-one six-weight matrix. This is an internal,
computer-assisted exact audit, not an external novelty determination or peer
review.
