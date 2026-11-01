# Independent audit: arbitrary positive weights on `K_{2,3}`

**Date:** 3 October 2026  
**Verdict:** **PASS.** For every six positive backbone activities, the full
five-variable apex-spoke forest polynomial of `K_{2,3}` is real stable.

This audit was reconstructed independently from the candidate statement.
It does not import or rely on the author probe. The exact checker and results
are `theta_six_weight_apex_stability_k_independent.py` and
`theta_six_weight_apex_stability_k_independent.json`.

## 1. Polynomial and reduction to three templates

Write the six activities as

    (w_02,w_03,w_04;w_12,w_13,w_14)=(a,b,c;d,e,f),

all strictly positive. I enumerated the 64 backbone subsets, retained the 54
forests, and constructed

    P(z)=sum_(A backbone forest)w(A)
          product_(C component of A)(1+sum_(i in C)z_i).                (1)

For a fixed backbone forest, the component factor is exact because at most
one apex spoke may be chosen from each component. The result has all 32
spoke monomials and gives 712 augmented forests when every activity and
spoke variable equals one.

Column permutations and simultaneous permutation of `z_2,z_3,z_4`, together
with row/endpoint exchange, reduce the ten spoke-pair checks to three generic
identities:

1. endpoint--endpoint;
2. endpoint--internal;
3. internal--internal.

This is an equivariant parameter-template reduction, not a claim that a
fixed generic six-weight graph has those automorphisms.

For later use define the coefficient-positive polynomial

    H(u,v;r,s)=uvr+uvs+uv+urs+ur+us+u
               +vrs+vr+vs+v+rs+r+s+1.                 (2)

## 2. Endpoint--endpoint template

Put

    X=z_3+1+b+e,   Y=z_4+1+c+f.

Collecting `Delta_01` in `z_2` gives the leading form

    [z_2^2]Delta_01=Phi(X,Y),                           (3)

where

    Phi=cf(c+1)(f+1)X^2+2bcefXY+be(b+1)(e+1)Y^2.

Its determinant is

    det Phi=bcef H(b,c;e,f)>0.                         (4)

The first diagonal coefficient is positive, hence `Phi` is positive
definite.

The discriminant is

    disc_(z_2)Delta_01=-4ad X^2Y^2 Psi(X,Y),           (5)

with

    Psi=cf H(a,c;d,f)X^2
         +2bcef(a+d+1)XY
         +be H(a,b;d,e)Y^2.                            (6)

Direct expansion gives

    det Psi=bcef(a+1)(d+1)Q(a,b,c,d,e,f),              (7)

where `Q` has 54 monomials, all with positive integer coefficients. The
checker constructs `Q` as the exact determinant quotient and verifies every
coefficient. Thus `Psi` is positive definite. At the sole leading-form
degeneration `X=Y=0`, exact substitution gives `Delta_01` identically zero
in `z_2`.

## 3. Endpoint--internal boundaries

For `Delta_02`, collected in `z_1`,

    [z_1^2]Delta_02=a(a+1)X^2Y^2,                      (8)

and its discriminant is exactly (5). The leading coefficient vanishes on
either complete axis, so the two boundaries must be checked separately.

Define, for columns `(u,r)` and `(v,s)`,

    T(u,v;r,s)
      =us(u+1)(s+1)+vr(v+1)(r+1)-2uvrs.               (9)

The crossed placement of `r,s` in (9) is essential. The exact boundary
expressions are

    Delta_02|_(X=0)=e(e+1)T(a,b;d,e)Y^2,
    Delta_02|_(Y=0)=f(f+1)T(a,c;d,f)X^2.              (10)

For endpoint `1`,

    [z_0^2]Delta_12=d(d+1)X^2Y^2,

    Delta_12|_(X=0)=b(b+1)T(a,b;d,e)Y^2,
    Delta_12|_(Y=0)=c(c+1)T(a,c;d,f)X^2.              (11)

Every `T` is strictly positive. Indeed, its first two terms are positive and
AM--GM gives

    us(u+1)(s+1)+vr(v+1)(r+1)
      >=2 sqrt[uvrs(u+1)(v+1)(r+1)(s+1)]
      >2uvrs,                                          (12)

because `(u+1)(v+1)(r+1)(s+1)>uvrs`. Therefore (10)-(11)
close both axis degeneracies. Column permutations prove all six
endpoint--internal pairs.

## 4. Internal--internal template

For the pair `(2,3)`, collect in the unused spoke `z_4` and put

    U=z_0+1+a+b+c,   V=z_1+1+d+e+f.

The leading coefficient is the binary form

    [z_4^2]Delta_23=Theta(U,V),                         (13)

where

    Theta=de(d+1)(e+1)U^2+2abdeUV+ab(a+1)(b+1)V^2.

Its determinant is

    det Theta=abde H(a,b;d,e)>0,                       (14)

so `Theta` is positive definite.

Normalize the discriminant by writing

    disc_(z_4)Delta_23=-4 Omega(U,V).                  (15)

The coefficients of `Omega` are signed polynomials, so coefficientwise
positivity is unavailable. Exact determinant expansion and factorization
instead gives

    det Omega
      =abcdef T(a,b;d,e)T(a,c;d,f)T(b,c;e,f)Q.         (16)

Every factor is strictly positive by (7), (9), and (12); hence the
determinant never vanishes anywhere on the positive orthant.

The candidate shorthand used the unnormalized form `-disc=4 Omega`. Scaling
a two-dimensional form by four multiplies its determinant by `4^2=16`, so
its determinant is

    16abcdef T(a,b;d,e)T(a,c;d,f)T(b,c;e,f)Q,

exactly matching that normalization.

### Continuity argument

Determinant positivity alone would allow either positive or negative
definiteness. The remaining continuity step is valid:

1. `Omega` is a continuous real symmetric `2 x 2` matrix-valued function of
   the six weights.
2. By (16), it is nonsingular throughout the positive orthant.
3. The positive orthant is connected, so the inertia cannot change without
   an eigenvalue crossing zero.
4. At `a=b=c=d=e=f=1`, the checker obtains

       Omega=108 I,   det Omega=11664.

Therefore `Omega` is positive definite everywhere. This is the precise
logical use of continuity; it does not infer positive definiteness from a
positive determinant alone.

At the only degeneration of the leading form, `U=V=0`, direct substitution
gives

    Delta_23=T(a,c;d,f)T(b,c;e,f)>0.                  (17)

Thus the internal template is globally nonnegative. Column permutations
cover all three internal--internal pairs.

## 5. Stability conclusion

For a real multiaffine polynomial, real stability is equivalent to

    Delta_ij(x)>=0

for every pair and every real specialization. Sections 2--4 prove the three
generic templates, including every zero-leading case. Parameter relabeling
covers all ten pairs. Hence the full five-variable apex-spoke polynomial is
real stable for arbitrary positive `(a,b,c;d,e,f)`.

## 6. Independent exact corroboration

The checker additionally performs:

- 17 generic symbolic identities, including both determinant
  factorizations and all boundary formulas;
- 1,000 exact rational Rayleigh evaluations covering all ten pairs at 100
  unrelated positive six-weight choices and real rational spoke values;
- 24 exact rational profile-ray cases, all with the predicted number of
  strictly negative roots by square-free/Sturm counting;
- six full proportional-four-row marked graphs, with four strict
  support-at-least-two cases and rank-one/rank-zero equality cases.

The root and marked consequences follow analytically as in the earlier
audits: diagonal profile specialization preserves stability, while the
empty backbone supplies positive coefficients in every surviving degree;
the audited four-core identity then gives the two-marked-edge inequality.

## 7. Reproduction and hashes

Run

    python random_cluster_research/theta_six_weight_apex_stability_k_independent.py

Expected summary:

| Check | Count |
|---|---:|
| symbolic identities | 17 |
| exact Rayleigh pair evaluations | 1,000 |
| exact profile/root cases | 24 |
| direct marked cases | 6 |
| strict marked cases | 4 |
| equality marked cases | 2 |
| counterexamples | 0 |

Artifact hashes at this checkpoint are:

    6c104ccbd7404983222fdce642a250efc28776759904e3056eb9272f59b8db80  theta_six_weight_apex_stability_k_independent.py
    100a4aefa5dd4038fdc663da342e3259d444b975c0ae193af75a73066654e723  theta_six_weight_apex_stability_k_independent.json

## 8. Final assessment

**PASS.** The endpoint--internal proof requires both separate axis formulas,
and they are exactly the positive expressions (10)-(11). The internal
discriminant form is positive definite by the nonvanishing determinant
factorization plus a valid connected-domain inertia argument based at
`108 I`. The normalization-dependent factor `16` is accounted for exactly.

No assertion here extends beyond `K_{2,3}` itself. This is an internal,
computer-assisted exact audit, not an external novelty determination or peer
review.
