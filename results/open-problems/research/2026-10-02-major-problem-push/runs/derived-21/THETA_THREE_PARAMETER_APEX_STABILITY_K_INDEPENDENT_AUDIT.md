# Independent audit: three-parameter theta apex stability

**Date:** 3 October 2026  
**Verdict:** **PASS.** All seven orbit certificates, six positive-form
determinants, boundary degeneracies, and stated consequences are correct. No
patch was required.

This audit covers `theta_three_parameter_apex_stability_proof.md`, its exact
checker/results, source/scope note, and route log. The independent checker
`theta_three_parameter_apex_stability_k_independent.py` imports no author
implementation and constructs the polynomial by a different method.

## 1. Precise theorem and limits

On `K_{2,3}`, with endpoints `0,1` and internal vertices `2,3,4`, the six
backbone activities are

    (w_02,w_03,w_04;w_12,w_13,w_14)=(pr,p,p;qr,q,q),

where `p,q,r>0`. Five independent variables weight the spokes from a new
apex. The theorem claims real stability of this spoke polynomial, hence a
strongly-Rayleigh spoke marginal and strictly negative roots on every
nonzero nonnegative profile ray. It also invokes the already audited
four-core identity for the proportional-row, two-marked-edge corollary.

The theorem contains the side-uniform family at `r=1` and the
one-distinguished-arm family at `p=q`. It does not cover three unrelated arm
multipliers, six arbitrary edge activities, theta subdivisions,
series-parallel closure, backbone conditioning, nonproportional rows, or
joint negative association involving backbone or marked edges. The proof,
source/scope note, and route log consistently respect this boundary.

## 2. Independent component-factor reconstruction

Instead of enumerating all `2^11` augmented-edge subsets as the author
checker does, I enumerated the 64 backbone subsets. For each backbone forest
`A`, the sum over allowable apex-spoke subsets is

    product_(C component of A)(1+sum_(i in C)z_i).       (1)

Indeed, an apex-spoke set creates no cycle precisely when it chooses at most
one vertex from each component of `A`. Thus

    P_(p,q,r)(z)=sum_(A backbone forest)w(A)
                       product_(C)(1+sum_(i in C)z_i).  (2)

This independently gives 54 backbone forests, all 32 spoke monomials, and
712 augmented forests at `p=q=r=z_i=1`. Every spoke coefficient is a
coefficientwise-positive polynomial in `p,q,r`.

At fixed parameters the only nontrivial vertex automorphism is `3<->4`.
The checker verifies this symmetry directly. Its ten unordered spoke pairs
therefore split into exactly seven orbits:

    (0,1),(0,2),(1,2),(0,3),(1,3),(2,3),(3,4).         (3)

## 3. Rayleigh criterion

For a real multiaffine polynomial, real stability is equivalent to

    Delta_ij=(partial_iP)(partial_jP)-P partial_ijP >=0 (4)

for every pair and every real specialization. Since `P` is multiaffine,
`Delta_ij` is independent of the paired variables. It is therefore valid to
collect each orbit representative as a quadratic in one unused variable.

Put

    h=p+q+1,  h_s=r(p+q)+1,
    h_0=p(r+2)+1,  h_1=q(r+2)+1,
    T=(p+q)(r+1)+2,  N=2pq+p+q+1.                     (5)

The displayed polynomials `L` and `M` in the proof are coefficientwise
positive, so `L,M>0` on the parameter domain.

## 4. Positive-definite forms

I expanded the symmetric-matrix determinant of each of the six forms from
the independently reconstructed polynomial. The exact factorizations are

    det Phi_A  =hN,
    det Phi_01 =(pr+1)(qr+1)hM,
    det Phi_03 =r^2(p+1)(q+1)hM,
    det Phi_23 =p^2q^2r^2L,
    det Phi_34 =p^2q^2hN,
    det Phi_E  =2p^2q^2T^2M.                           (6)

All factors are strictly positive. The first diagonal coefficients are

    (p+1)(q+1),
    L,
    hN,
    q^2r(q+1)(qr+1),
    q^2(q+1)^2,
    q^2(qr+1)E_q,                                      (7)

respectively. `E_q` is coefficientwise positive. Hence Sylvester's
criterion proves all six forms positive definite. The potentially negative
cross coefficient `K` of `Phi_E` causes no problem; the argument correctly
uses (6), not coefficientwise positivity of that form.

## 5. Seven exact orbit identities

All identities in this section were obtained by differentiating (2), not by
importing the author checker.

### 5.1 Endpoint pair `(0,1)`

Set `X_3=z_3+h`, `X_4=z_4+h`. Collecting in `z_2` gives

    [z_2^2]Delta_01=pq Phi_A(X_3,X_4),

    disc_(z_2)Delta_01
      =-4p^2q^2r^2X_3^2X_4^2 Phi_01(X_3,X_4).          (8)

Away from `(X_3,X_4)=(0,0)`, the leading coefficient is positive and the
discriminant nonpositive. At that unique leading-form degeneration,
`Delta_01` is identically zero as a polynomial in `z_2`.

### 5.2 Special-arm endpoint pairs `(0,2)` and `(1,2)`

Collecting in the opposite endpoint variable gives leading coefficients

    pr(pr+1)X_3^2X_4^2,
    qr(qr+1)X_3^2X_4^2,                                (9)

and both discriminants equal (8). On `X_3=0` or `X_4=0`, the complete
boundary polynomial is the square of the remaining shifted variable times

    pq^2r(q+1)T

for `Delta_02`, and

    p^2qr(p+1)T

for `Delta_12`. These multipliers are positive and cover both coordinate
axes, including their intersection. There is no missed linear case.

### 5.3 Ordinary-arm endpoint pairs `(0,3)` and `(1,3)`

Set `X_2=z_2+h_s` and retain `X_4`. Collecting in the opposite endpoint
variable gives leading coefficients

    p(p+1)X_2^2X_4^2,
    q(q+1)X_2^2X_4^2.                                 (10)

Both discriminants are

    -4p^2q^2X_2^2X_4^2 Phi_03(X_2,X_4).               (11)

For `Delta_03`, the `X_2=0` and `X_4=0` boundary multipliers are

    pq^2r^2(qr+1)T,  2pq^2(q+1)h,

and for `Delta_13` they are

    p^2qr^2(pr+1)T,  2p^2q(p+1)h.                     (12)

Each multiplies the square of the other shifted variable. All are strictly
positive, so every zero-leading degeneration is handled.

### 5.4 Special--ordinary internal pair `(2,3)`

Set `U_0=z_0+h_0`, `U_1=z_1+h_1`. Collecting in the unused ordinary spoke
`z_4` gives the decisive simplification

    [z_4^2]Delta_23=Phi_23(U_0,U_1),

    disc_(z_4)Delta_23
      =-4p^2q^2r^2h Phi_E(U_0,U_1).                   (13)

The leading form degenerates only at `U_0=U_1=0`, where direct substitution
gives

    Delta_23=2p^2q^2rhT>0.                            (14)

Thus the difficult orbit is a quadratic with a positive leading form, not
an unresolved quartic. The route log accurately explains why changing the
collected variable removes the earlier obstruction.

### 5.5 Ordinary--ordinary internal pair `(3,4)`

Collecting in `z_2` gives

    [z_2^2]Delta_34=Phi_34(U_0,U_1),                   (15)

the same discriminant as (13), and at the unique leading degeneration

    Delta_34=p^2q^2r^2T^2>0.                          (16)

Equations (8)-(16) prove every representative globally nonnegative by the
positive-leading/nonpositive-discriminant criterion. With (3)-(4), this
proves real stability.

The independent checker verifies 25 coefficient, discriminant, and boundary
identities plus all six determinant factorizations, totaling 31 exact
symbolic checks.

## 6. Profile roots and strongly-Rayleigh scope

The forest definition makes `P` real, multiaffine, and coefficientwise
nonnegative. Its normalized coefficient measure on the five **spoke
indicators** is therefore strongly Rayleigh. Standard consequences give
negative association under spoke external fields and positive-probability
spoke conditioning. The statement does not include backbone or marked edges
in this strong-Rayleigh family.

Substitution `z_i=s beta_i` with `beta_i>=0` preserves stability. A real
univariate stable polynomial has only real roots, since a nonreal root and
its conjugate cannot both avoid the upper half-plane. If exactly `k` profile
entries are positive, the empty backbone permits every subset of those
spokes. Therefore every coefficient in degrees `0,...,k` is positive and
the degree is `k`; zero and nonnegative real roots are excluded. All `k`
roots are strictly negative. For `k=0`, the polynomial is a positive
constant and the claim is vacuous.

The independent checker tests 24 seeded rational choices of `p,q,r,beta`.
Exact square-free factorization and Sturm counts find exactly `k` negative
roots counting multiplicity in every case.

## 7. Marked-pair transfer

The audited four-core identity only needs the one-apex negative-root
factorization; it does not require a cactus backbone. Its two Stieltjes
brackets are nonnegative here, and the first is strict for profile support
at least two. The unscaled marked Rayleigh difference also contains the
factor `abcd` from the four proportional row scalars. Consequently, at
positive marked-edge activities, covariance is nonpositive and is strict
exactly when all four row scalars are positive and profile support is at
least two.

Six full marked graphs were also enumerated directly at rational `p,q,r`.
Four support-at-least-two cases give strict inequality; support-one and
support-zero cases give equality.

## 8. Verification record

Running

    python random_cluster_research/theta_three_parameter_apex_stability_k_independent.py

reports:

| Independent exact check | Count |
|---|---:|
| symbolic identities | 31 |
| rational profile/root cases | 24 |
| direct marked cases | 6 |
| strict marked cases | 4 |
| marked equality cases | 2 |
| counterexamples | 0 |

The author checker was separately inspected and rerun. It reports PASS with
712 unit-weight augmented forests, 32 spoke monomials, seven pair orbits,
and 31 exact symbolic identities.

Independent artifact hashes at this checkpoint are:

    b4a554a4b730d53346f8a173b18de05b738ed84c0816924fe6fdb14cb13ab4ed  theta_three_parameter_apex_stability_k_independent.py
    aed09ae5abe4d724b910cdb5d0331e0fa82d4426a68b13e3cb1bcd19d77def80  theta_three_parameter_apex_stability_k_independent_results.json

## 9. Final assessment

The seven-orbit reduction, all six positive-definite forms, the complete set
of quadratic degeneracies, the Rayleigh criterion, strong-Rayleigh scope,
profile-root deduction, marked-pair corollary, and stated boundary are
correct. No proof, checker, source/scope, or route-log patch was necessary.

**PASS**, with no remaining required correction and no counterexample found.
This is an internal mathematical audit, not external peer review or a
novelty certification.
