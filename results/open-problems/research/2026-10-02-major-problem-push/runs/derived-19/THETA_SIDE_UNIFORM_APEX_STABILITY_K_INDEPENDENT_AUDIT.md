# Independent audit: side-uniform `K_{2,3}` apex stability

**Date:** 3 October 2026  
**Verdict:** **PASS.** The two-parameter theorem, its four exact Rayleigh
certificates, the strong-Rayleigh spoke consequence, and the proportional-row
marked-pair consequence are correct within the stated scope.

This audit covers `theta_uniform_apex_stability_proof.md`,
`THETA_UNIFORM_APEX_SOURCE_AND_SCOPE.md`, and the author exact checker. I
constructed the polynomial independently and wrote
`theta_side_uniform_apex_stability_k_independent.py`; it imports no author
code and uses a different enumeration route.

## 1. Exact object and scope

The backbone is `K_{2,3}` with degree-three-side vertices `0,1` and internal
vertices `2,3,4`. The three edges incident with `0` have one common activity
`p>0`; the three incident with `1` have one common activity `q>0`. The five
edges from a new apex carry independent variables `z_0,...,z_4`.

The theorem is not about six arbitrary backbone activities. In particular,
the permutation symmetry of `2,3,4` is indispensable to the four-orbit
reduction. It does not prove arbitrary theta subdivisions, general
series-parallel closure, backbone-edge conditioning, or negative association
jointly involving backbone or marked edges. The source/scope note states all
of these boundaries accurately.

## 2. Independent reconstruction of the polynomial

I did not reuse the author's enumeration over all `2^11` augmented-edge
subsets. Instead, for each of the `2^6=64` backbone subsets I tested whether
it is a forest. For every accepted forest `A`, with component set `C(A)`, the
sum over allowable apex-spoke subsets is exactly

    product_(C in C(A)) (1 + sum_(i in C) z_i).          (1)

Indeed, adding apex spokes preserves acyclicity exactly when at most one
vertex is chosen from each backbone component. Thus the independently built
polynomial is

    P_(p,q)(z)=sum_(A backbone forest) w(A)
                    product_(C in C(A))(1+sum_(i in C)z_i).              (2)

There are 54 backbone forests, all 32 spoke monomials occur, and evaluating
`p=q=z_i=1` gives 712 augmented forests. These values agree with the author's
separate full-subset enumeration.

The polynomial is invariant under all permutations of `2,3,4`. At fixed
`p,q`, the endpoints generally cannot be swapped; swapping them is an
identity only together with `p<->q`. Therefore the ten unordered spoke pairs
have exactly four relevant orbits:

    (0,1), (0,2), (1,2), (2,3).                         (3)

The independent checker verifies these symmetries directly on (2).

## 3. Rayleigh criterion

For a real multiaffine polynomial `P`, the standard multivariate Rayleigh
criterion is

    P stable  iff  Delta_ij(x)>=0

for every pair and every real specialization, where

    Delta_ij=(partial_i P)(partial_j P)-P partial_ij P. (4)

Because `P` is multiaffine, `Delta_ij` is independent of `z_i,z_j`; hence the
proof is entitled to treat it as a quadratic in one remaining variable. By
(3), four representatives suffice. No positivity-of-coefficients assumption
is being smuggled into the criterion; nonnegative coefficients are used only
for the later probability interpretation.

## 4. Positivity of the four residual forms

Put `h=p+q+1`. The proof uses

    Phi_A=(p+1)(q+1)(X^2+Y^2)+2pqXY,
    Phi_Q=(2pq+p+q+1)(X^2+Y^2)+2pqXY,

    Phi_B=q^2(q+1)^2X^2+2p^2q^2XY+p^2(p+1)^2Y^2,

    Phi_R=3q^2(q+1)^2X^2
          +2pq(3pq-p-q-1)XY+3p^2(p+1)^2Y^2.           (5)

For `Phi_A` the eigenvalues are

    2pq+p+q+1,  h,

and for `Phi_Q` they are

    3pq+p+q+1,  (p+1)(q+1).

All four are positive. The diagonal terms of `Phi_B,Phi_R` are positive,
and their symmetric-matrix determinants simplify exactly to

    det Phi_B=p^2q^2 h(2pq+p+q+1),
    det Phi_R=8p^2q^2 h(3pq+p+q+1).                   (6)

These are positive for `p,q>0`. Sylvester's criterion therefore proves all
four forms positive definite. I expanded and refactored both determinants
independently; the factors and constants in (5)-(6) are exact.

## 5. The four Rayleigh differences

### 5.1 Endpoint--endpoint

Set `X_3=z_3+h`, `X_4=z_4+h`. Direct differentiation of the independently
constructed (2), followed by collection in `z_2`, gives

    [z_2^2]Delta_01=pq Phi_A(X_3,X_4),

    disc_(z_2)Delta_01
      =-4p^2q^2h X_3^2X_4^2 Phi_Q(X_3,X_4).            (7)

If `(X_3,X_4)` is nonzero, the leading coefficient is positive and the
discriminant is nonpositive. At the only leading-coefficient degeneracy,
`X_3=X_4=0`, direct substitution gives `Delta_01=0` identically in `z_2`.
Thus this orbit is globally nonnegative.

### 5.2 Endpoint 0--internal

Collecting `Delta_02` in `z_1` gives

    [z_1^2]Delta_02=p(p+1)X_3^2X_4^2,

    disc_(z_1)Delta_02
      =-4p^2q^2h X_3^2X_4^2 Phi_Q(X_3,X_4).            (8)

If one shifted variable vanishes, the complete boundary polynomials are

    Delta_02|_(X_3=0)=2pq^2(q+1)h X_4^2,
    Delta_02|_(X_4=0)=2pq^2(q+1)h X_3^2.               (9)

They are nonnegative and independent of the nominal quadratic variable, so
there is no unhandled linear degeneration.

### 5.3 Endpoint 1--internal

Collecting `Delta_12` in `z_0` gives

    [z_0^2]Delta_12=q(q+1)X_3^2X_4^2,                 (10)

with the same discriminant as (8), while the two boundary polynomials are

    2p^2q(p+1)h X_4^2,  2p^2q(p+1)h X_3^2.            (11)

This fourth orbit is necessary when `p!=q`; it cannot be inferred from a
fixed-parameter endpoint automorphism. The proof includes it correctly.

### 5.4 Internal--internal

Set

    U_0=z_0+3p+1,  U_1=z_1+3q+1.

Collection of `Delta_23` in `z_4` gives

    [z_4^2]Delta_23=Phi_B(U_0,U_1),

    disc_(z_4)Delta_23
      =-4p^2q^2h^2 Phi_R(U_0,U_1).                    (12)

Positive definiteness settles every nonzero `(U_0,U_1)`. At the unique
degenerate point, direct substitution gives

    Delta_23=4p^2q^2h^2>0.                            (13)

Equations (7)-(13) cover every real specialization. The Rayleigh criterion
therefore proves real stability of `P_(p,q)`.

The independent checker derives and verifies all 18 coefficient,
discriminant, boundary, and positive-form identities directly from (2).

## 6. Strong-Rayleigh and univariate consequences

The forest definition makes `P` real, multiaffine, and coefficientwise
nonnegative. Normalizing its coefficients therefore gives a strongly
Rayleigh probability measure on the **five apex-spoke indicators**. The
standard Borcea--Branden--Liggett consequences give negative association and
closure under nonnegative diagonal rescaling, external fields, and
positive-probability spoke conditioning.

This conclusion is not a statement about the joint law of spokes with
backbone edges, nor about a law including the later marked edges.

For a nonnegative profile `beta`, diagonal specialization `z_i=s beta_i`
preserves stability. A real univariate stable polynomial has only real
zeros: any nonreal lower-half-plane zero would bring its conjugate into the
forbidden upper half-plane. If `k` profile entries are positive, the degree
is exactly `k`, since all `k` corresponding spokes with an empty backbone
form a forest. More strongly, every coefficient from degree `0` through `k`
is positive by choosing the corresponding spoke subset and empty backbone.
Consequently zero and nonnegative real numbers cannot be roots, and all `k`
roots are strictly negative.

As a separate computational check, 24 seeded rational choices of `p,q,beta`
were specialized exactly. Square-free factorization plus exact Sturm root
counts found precisely `k` negative roots counting multiplicity in every
case.

## 7. Marked-pair deduction

The previously audited four-core transfer identity requires only the
one-apex factorization

    D(s)=D(0) product_(j=1)^k(1+s xi_j), xi_j>0,        (14)

not a forest or cactus backbone. The theta theorem supplies (14), so its two
Stieltjes brackets are nonnegative. The first is strict for `k>=2`; the
unscaled marked Rayleigh difference has the factor `abcd` from the four row
scalars. For a **positive pair of marked-edge activities**, covariance is
therefore nonpositive and is strict exactly when `abcd>0` and `k>=2`.

The positivity qualification on marked-edge activities is essential: at
zero activity the corresponding indicator is deterministic and covariance
is zero. This qualification is present in the final proof. The independent
checker directly enumerates six full four-row marked graphs at rational
`p,q`: four rank-at-least-two cases are strict, and rank-one/rank-zero cases
give equality.

## 8. Boundary and wording corrections made during audit

Three small issues were corrected; none affects the analytic theorem.

1. The first draft omitted positivity of the two marked-edge activities from
   the strictness sentence. The final theorem now says “every positive pair.”
2. Spoke conditioning was clarified to mean positive-probability
   conditioning.
3. The author checker docstring said “three” pair orbits after the theorem
   had expanded to four, and the route log retained the old uniform shifts
   `2t+1,3t+1`. They now say four orbits and the correct shifts
   `p+q+1,3p+1,3q+1`.

No coefficient, discriminant, boundary identity, positivity certificate, or
scope statement required mathematical correction.

## 9. Verification record

Running

    python random_cluster_research/theta_side_uniform_apex_stability_k_independent.py

reports:

| Independent exact check | Count |
|---|---:|
| symbolic certificate identities | 18 |
| rational univariate profile/root cases | 24 |
| directly enumerated marked cases | 6 |
| strict marked cases | 4 |
| marked equality cases | 2 |
| counterexamples | 0 |

The independent implementation uses 54 accepted backbone forests and their
component factors, rather than the author's 2,048 augmented-edge subsets.
The author checker was also rerun after inspection and reports PASS: 712
augmented forests, 32 monomials, four pair orbits, and 18 exact identities.

Independent artifact hashes at this audit checkpoint are:

    1728a7476e7f7da5020eaacfe8dc3018cd6b0a936474da5abd9628a8258fe024  theta_side_uniform_apex_stability_k_independent.py
    1e6481f300da1aa7efc5da88c3bf8a7ce6bbac7737e6c3890a6156d7bb30105e  theta_side_uniform_apex_stability_k_independent_results.json

## 10. Final assessment

The proof is complete for the stated side-uniform two-parameter family. The
four-orbit reduction is exact, all degeneracies of the quadratic argument
are covered, the multiaffine Rayleigh criterion applies, and the probability
consequences are scoped correctly. **PASS**, with no remaining required
correction and no counterexample found.

This is an internal mathematical audit and exact corroboration, not an
external novelty determination or peer review.
