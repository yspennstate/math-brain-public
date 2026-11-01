# Derived-20 result: one distinguished theta arm

## Completed theorem

Let `K_{2,3}` have endpoints `0,1` and internal vertices `2,3,4`. Give both
edges of the arm through `2` activity `rt`, and the other four backbone edges
activity `t`, for arbitrary `r,t>0`. After adjoining an apex with five
independent spoke variables, the full apex-spoke forest polynomial is real
stable.

This is a second completed theorem beyond cactus backbones. It is
incomparable with derived-19: that checkpoint permits endpoint-side
asymmetry `p,q` but treats all three arms equally; this checkpoint permits
one independently weighted arm while keeping the endpoints symmetric.

Consequently the spoke marginal is strongly Rayleigh and negatively
associated under spoke external fields and positive-probability spoke
conditioning. Every nonnegative profile specialization has only strictly
negative real roots. The audited four-core transfer again gives negative
correlation for two disjoint external marked edges with four proportional
rows, at every positive pair of marked activities, with strictness exactly
for four positive row scalars and profile support at least two.

## Exact analytic certificate

Endpoint exchange and ordinary-arm exchange leave five spoke-pair orbits.
Each Rayleigh difference is collected as a quadratic in a carefully chosen
remaining variable. After shifts by

    2t+1,  2rt+1,  t(r+2)+1,

all leading coefficients and negative discriminants reduce to five explicit
positive-definite binary forms. The shared positive factor

    S=2r^2t^3+r^2t^2+4rt^3+4rt^2+2rt+2t^2+2t+1

is coefficientwise positive. The five matrix determinants factor as

    (2t+1)(2t^2+2t+1),
    (2t+1)(rt+1)^2 S,
    r^2(t+1)^2(2t+1)S,
    (rt+t+1)(2rt^2+rt+t+1),
    8(rt+t+1)^2 S.

All zero-leading-coefficient boundary polynomials are evaluated explicitly.
The multiaffine Rayleigh characterization therefore gives global real
stability at every real specialization.

## Verification and independent audit

The author checker enumerates all 2,048 augmented-edge subsets, retains 712
forests at unit weights, reconstructs all 32 spoke monomials, and verifies
22 exact coefficient, discriminant, boundary, and positivity identities.

The fresh independent audit **PASSes with no correction required**. Its
checker imports no author code and instead enumerates the 64 backbone
subsets, retains 54 backbone forests, and expands their component factors.
It independently verifies all 22 symbolic certificates, 24 exact rational
profile/root cases, and six directly enumerated full marked graphs (four
strict and two equality), with zero counterexamples.

## Failed and open extensions

The three-parameter family with weights `pr,p,p,qr,q,q`, combining endpoint
and arm asymmetry, was expanded exactly. Several pair orbits retain binary
forms, but the special--ordinary internal pair leaves a genuine bivariate
quartic after the obvious square factors. No SOS and no exact negative
witness were obtained; that family remains open here.

Two-terminal determinant gluing also remains unresolved because the
normalized off-diagonal terminal Gram entry depends on the network. Six
unrelated activities, arbitrary theta subdivisions, series-parallel closure,
backbone conditioning, nonproportional rows, and joint backbone/marked
negative association are not proved. The full famous forest conjecture,
full Boolean FEI, unrestricted ML10 Sidorenko, and Kaplansky/direct
finiteness remain open.

## Prior-art status

Classical strong-Rayleigh theory and current weighted-forest results are
credited. Targeted primary-source searches did not locate this precise
one-distinguished-arm theorem, but bounded search is not a novelty
certification. Historical priority and external specialist review remain
unverified.
