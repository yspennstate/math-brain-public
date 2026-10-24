# Independent audit: one-distinguished-arm theta apex stability

**Date:** 3 October 2026  
**Verdict:** **PASS.** No mathematical error, missing degeneration, or scope
overreach was found.

This audit covers `theta_one_arm_apex_stability_proof.md`,
`THETA_ONE_ARM_SOURCE_AND_SCOPE.md`, the route log, and the author exact
checker/results. I independently reconstructed the forest polynomial and
wrote `theta_one_arm_apex_stability_k_independent.py`, which imports no
author code.

## 1. Claim and exact boundary

The backbone is `K_{2,3}` with endpoints `0,1` and internal vertices
`2,3,4`. Both edges in the arm through `2` have activity `rt`; the other four
backbone edges have activity `t`, with `r,t>0`. The five apex spokes carry
independent variables.

The claimed conclusions are:

1. the five-variable apex-spoke forest polynomial is real stable;
2. the normalized spoke marginal is strongly Rayleigh and negatively
   associated, including under spoke external fields and positive-probability
   spoke conditioning;
3. every nonnegative profile-ray specialization has only strictly negative
   real roots (with the constant zero-profile case vacuous);
4. the previously audited proportional-four-row construction has negative
   correlation between its two disjoint external marked edges at positive
   marked activities, strict exactly for four positive row scalars and
   profile support at least two.

The proof does not claim simultaneous endpoint-side and arm asymmetry, six
unrelated backbone weights, arbitrary theta subdivisions, two-terminal or
series-parallel closure, backbone-edge conditioning, nonproportional marked
rows, or joint negative association involving backbone/marked edges. The
source/scope file records these limitations accurately.

## 2. Independent polynomial construction

The author checker enumerates all 2,048 subsets of the eleven augmented
edges. My checker instead enumerates only the 64 backbone subsets. For each
backbone forest `A`, with components `C(A)`, the complete spoke contribution
is

    product_(C in C(A)) (1+sum_(i in C)z_i).             (1)

This follows because an apex-spoke set is acyclic over `A` exactly when it
contains at most one vertex from every component of `A`. Hence

    P_(t,r)(z)=sum_(A backbone forest)w(A)
                    product_(C in C(A))(1+sum_(i in C)z_i).              (2)

The independent construction finds 54 backbone forests, all 32 possible
spoke monomials, and 712 augmented forests at `r=t=z_i=1`. Every coefficient
is a polynomial in `r,t` with positive coefficients. These facts agree with
the author's structurally different enumeration.

## 3. Pair orbits and applicability of the criterion

At fixed `r,t`, (2) is invariant under endpoint exchange `0<->1` and under
the ordinary-arm exchange `3<->4`. These two involutions give exactly five
orbits among the ten unordered pairs:

    (0,1), (0,2), (0,3), (2,3), (3,4).                 (3)

The independent checker verifies both generating symmetries directly.

For a real multiaffine polynomial, real stability is equivalent to

    Delta_ij(x)=(partial_iP)(partial_jP)-P partial_ijP >=0               (4)

for every pair and every real specialization. Because `P` is multiaffine,
`Delta_ij` is independent of the two paired variables. Therefore it is valid
to regard each representative as a quadratic in one of the three remaining
variables. Proving the five orbit representatives globally nonnegative is
sufficient.

## 4. The five positive forms

Let

    h=2t+1,  h_s=2rt+1,  h_e=t(r+2)+1,

and

    S=2r^2t^3+r^2t^2+4rt^3+4rt^2+2rt+2t^2+2t+1.       (5)

Every monomial in `S` is nonnegative and its constant term is one, so
`S>0` for `r,t>0`.

I independently expanded the symmetric-matrix determinants of all five
binary forms in the proof. They factor exactly as

    det Phi_A  =(2t+1)(2t^2+2t+1),
    det Phi_01 =(2t+1)(rt+1)^2 S,
    det Phi_03 =r^2(t+1)^2(2t+1)S,
    det Phi_23 =(rt+t+1)(2rt^2+rt+t+1),
    det Phi_E  =8(rt+t+1)^2S.                           (6)

Their first diagonal coefficients are respectively

    (t+1)^2,
    (rt+t+1)(2rt^2+rt+t+1),
    (2t+1)(2t^2+2t+1),
    (t+1)(rt+1),
    (rt+1)(2rt^2+3rt+4t^2+6t+3),                       (7)

all strictly positive. Equations (6)-(7) prove positive definiteness by
Sylvester's criterion. This also handles `Phi_E` correctly: its cross
coefficient `(rt+2t+1)(2rt^2-rt-1)` can be negative, so coefficientwise
positivity would be invalid, but the determinant proof is unaffected.

## 5. Independent reconstruction of the five Rayleigh certificates

All identities below were obtained by differentiating (2), not copied from
the displayed proof.

### 5.1 Endpoint pair `(0,1)`

Put `X_3=z_3+h`, `X_4=z_4+h` and collect `Delta_01` in `z_2`. The leading
coefficient and discriminant are exactly

    [z_2^2]Delta_01=t^2 Phi_A(X_3,X_4),

    disc_(z_2)Delta_01
      =-4r^2t^4X_3^2X_4^2 Phi_01(X_3,X_4).             (8)

Positive definiteness gives a positive leading coefficient except at
`X_3=X_4=0`; away from that point the discriminant is nonpositive. Direct
substitution at the unique degeneration gives the zero polynomial in
`z_2`, so no linear boundary case is omitted.

### 5.2 Endpoint--special pair `(0,2)`

Collecting in `z_1` gives

    [z_1^2]Delta_02=rt(rt+1)X_3^2X_4^2,                (9)

and exactly the same discriminant as (8). The leading coefficient can
vanish on either coordinate axis, not only at their intersection. The two
complete boundary identities are

    Delta_02|_(X_3=0)=2rt^3(t+1)(rt+t+1)X_4^2,
    Delta_02|_(X_4=0)=2rt^3(t+1)(rt+t+1)X_3^2.         (10)

They are nonnegative and independent of `z_1`, covering every degeneration.

### 5.3 Endpoint--ordinary pair `(0,3)`

Put `X_2=z_2+h_s`, retain `X_4=z_4+h`, and collect in `z_1`. Exact expansion
gives

    [z_1^2]Delta_03=t(t+1)X_2^2X_4^2,

    disc_(z_1)Delta_03
      =-4t^4X_2^2X_4^2 Phi_03(X_2,X_4).                (11)

The axis boundaries are exactly

    Delta_03|_(X_2=0)=2r^2t^3(rt+1)(rt+t+1)X_4^2,
    Delta_03|_(X_4=0)=2t^3(t+1)(2t+1)X_2^2.            (12)

Thus this quadratic is also globally nonnegative.

### 5.4 Special--ordinary internal pair `(2,3)`

Put `U_0=z_0+h_e`, `U_1=z_1+h_e` and collect in `z_4`. One gets

    [z_4^2]Delta_23=rt^2 Phi_23(U_0,U_1),

    disc_(z_4)Delta_23
      =-4r^2t^6(2t+1)Phi_E(U_0,U_1).                  (13)

The positive-definite leading form degenerates only at `U_0=U_1=0`, where

    Delta_23=4rt^4(2t+1)(rt+t+1)>0.                   (14)

### 5.5 Ordinary--ordinary internal pair `(3,4)`

Collecting in `z_2` gives

    [z_2^2]Delta_34=t^2 Phi_A(U_0,U_1),                (15)

the same discriminant as (13), and at the only degeneration

    Delta_34=4r^2t^4(rt+t+1)^2>0.                     (16)

For a real quadratic, positive leading coefficient and nonpositive
discriminant imply global nonnegativity. Equations (8)-(16), including every
zero-leading boundary, establish (4) on all five orbits. The multiaffine
Rayleigh criterion therefore proves the theorem.

The independent checker verifies 17 coefficient/discriminant/boundary
identities plus the five determinant identities in (6), for 22 exact checks.

## 6. Probability and root deductions

The forest polynomial is real, multiaffine, stable, and has nonnegative
coefficients. After normalization, its coefficient measure on the five
**spoke indicators** is strongly Rayleigh. Standard closure and implication
results yield negative association under spoke external fields and
positive-probability spoke cylinder conditioning. This does not include the
backbone or later marked edges in the strongly-Rayleigh family.

For a nonnegative profile `beta`, substituting `z_i=s beta_i` preserves
stability. A real univariate stable polynomial can have no nonreal zero,
because conjugation would place one conjugate in the upper half-plane. If
`k` profile entries are positive, the empty backbone permits every subset of
those spokes. Thus the specialized polynomial has degree `k` and a positive
coefficient in every degree `0,...,k`. Its real roots can be neither zero nor
nonnegative; all are strictly negative. The `k=0` polynomial is a positive
constant and has no roots.

The independent checker tests 24 seeded rational choices of `r,t,beta`.
Exact square-free factorization and Sturm counts find exactly `k` negative
roots counting multiplicity in every case.

## 7. Marked-pair deduction

The audited four-core identity applies to any backbone once its one-apex
specialization has a factorization into negative linear roots. It does not
require the backbone itself to be a cactus. Applying it to the factorization
just proved makes both Stieltjes brackets nonnegative. The unscaled marked
Rayleigh difference has the factor `abcd`; its first bracket is strict for
profile support at least two. At a positive pair of marked-edge activities,
the covariance is therefore nonpositive, and strict exactly when all four
row scalars are positive and the profile support has size at least two.

I also directly enumerated six complete four-row marked graphs at rational
`r,t`. Four support-at-least-two cases give a strictly positive marked
Rayleigh difference; support-one and support-zero cases give equality.

## 8. Exact verification record

Running

    python random_cluster_research/theta_one_arm_apex_stability_k_independent.py

reports:

| Independent check | Count |
|---|---:|
| exact symbolic certificates | 22 |
| exact rational profile/root cases | 24 |
| direct marked cases | 6 |
| strict marked cases | 4 |
| marked equality cases | 2 |
| counterexamples | 0 |

The author checker was separately inspected and rerun. It reports PASS with
712 unit-weight augmented forests, 32 monomials, five pair orbits, and 22
exact identities.

The independent artifacts have SHA-256 hashes:

    8075eb2063a0a63a64ad6fe85db794404e26d0ff27eeb5b68ee6045c08137998  theta_one_arm_apex_stability_k_independent.py
    3b8f365d068d9274fe4a4eece5f78ab39ff07534960016cfd7e63137ef9bcc3f  theta_one_arm_apex_stability_k_independent_results.json

## 9. Final assessment

The five orbit reduction, positive-definite forms, discriminant signs,
degenerate boundaries, Rayleigh criterion, strong-Rayleigh interpretation,
profile-root claim, marked-pair transfer, and scope are all correct. No patch
to the proof, source/scope note, route log, or author checker was necessary.

**PASS**, with no remaining required correction and no counterexample found.
This is an internal mathematical audit, not external peer review or a
novelty certification.
