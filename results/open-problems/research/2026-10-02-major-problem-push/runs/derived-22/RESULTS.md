# Derived-22 result: full rank-one theta stability

## Completed theorem

On `K_{2,3}` with endpoint vertices `0,1` and arm vertices `2,3,4`, assign

    (w_02,w_03,w_04;w_12,w_13,w_14)=(pa,pb,pc;qa,qb,qc)

for arbitrary `p,q,a,b,c>0`.  After adjoining an apex with five independent
spoke variables, the complete apex-spoke forest polynomial is real stable.

This is the full positive rank-one `2 x 3` edge-weight matrix and strictly
subsumes derived-21 (`a=r,b=c=1`).  The spoke marginal is strongly Rayleigh
and negatively associated under spoke fields and positive-probability spoke
conditioning.  Every nonzero nonnegative profile ray has strictly negative
real roots.  The previously audited four-core transfer consequently supplies
the same proportional-row disjoint-marked-edge NC corollary.

## Analytic mechanism

With no generic arm symmetry there are ten spoke pairs, but parameter
permutation reduces them to three exact templates: endpoint--endpoint,
endpoint--internal, and internal--internal.  Natural partition-function
shifts turn each Rayleigh difference into a quadratic in one unused spoke.

Four binary forms control the leading coefficients and discriminants.  The
hard internal--internal discriminant has a mixed coefficient of indefinite
sign, so coefficientwise positivity fails.  Its `2 x 2` determinant instead
factors as

    p^2 q^2 (2+(p+q)(a+b)) (2+(p+q)(a+c))
            (2+(p+q)(b+c)) S(a,b,c),

where `S` is an explicitly displayed coefficientwise-positive polynomial.
Every vanishing-leading-coefficient boundary is evaluated exactly.

## Exact verification and independent audit

The author checker constructs the 32-term polynomial from 54 backbone
forests (712 augmented forests at unit weights), verifies thirteen structural
identities and four positive-definite binary-form certificates, including a
411-term expanded determinant.  All ten pairs are covered by exact parameter
symmetries.

The fresh independent audit **PASSes**.  Its independently written checker
reconstructs the polynomial separately and verifies 18 symbolic identities,
1,200 exact rational all-pair evaluations, 24 exact profile-root cases, and
six direct marked graphs (four strict, two equality), with zero
counterexamples.  In particular it checks both endpoint--internal axes and
the signed-mixed-coefficient internal determinant.

## Exact boundary and open problem status

Not proved: six arbitrary independent edge activities (the two endpoint
weight rows need not be proportional), theta subdivisions, a general
two-terminal/series-parallel closure, backbone cylinder conditioning,
nonproportional external marked rows, or joint backbone/marked negative
association.  The famous general forest negative-correlation conjecture
remains open.  Full Boolean FEI, unrestricted ML10 Sidorenko, and
Kaplansky/direct finiteness also remain open in this campaign.

## Prior-art status

Grimmett--Winkler, Erickson, Huang, and the 2026 work of Çiçeksiz--
Ravichandran were checked.  Targeted searches did not locate this exact
rank-one real-stability theorem.  Historical novelty and priority remain
unverified, and there has been no external specialist review.
