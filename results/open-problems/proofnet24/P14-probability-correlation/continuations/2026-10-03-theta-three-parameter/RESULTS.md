# Derived-21 result: combined three-parameter theta stability

## Completed theorem

On `K_{2,3}` with endpoints `0,1` and internal vertices `2,3,4`, assign

    (w_02,w_03,w_04;w_12,w_13,w_14)=(pr,p,p;qr,q,q),

for arbitrary `p,q,r>0`. After adjoining an apex with five independent
spoke variables, the complete apex-spoke forest polynomial is real stable.

This simultaneously subsumes derived-19 (`r=1`, endpoint-side asymmetry)
and derived-20 (`p=q`, one distinguished arm). It is the strongest
non-cactus theorem in the campaign.

The spoke marginal is strongly Rayleigh and negatively associated under
spoke external fields and positive-probability spoke conditioning. Every
nonnegative profile ray has only strictly negative real roots. Combining
the theorem with the previously audited four-core identity yields negative
correlation of the two disjoint external marked edges with four proportional
rows at every positive pair of marked activities, strict exactly for four
positive row scalars and profile support at least two.

## Analytic mechanism

The remaining ordinary-arm swap leaves seven spoke-pair orbits. Each
Rayleigh difference is treated as a quadratic in one of the three unpaired
variables. Six explicit shifted binary forms control all leading
coefficients and discriminants. Their determinants factor as

    hN,
    (pr+1)(qr+1)hM,
    r^2(p+1)(q+1)hM,
    p^2q^2r^2L,
    p^2q^2hN,
    2p^2q^2T^2M,

where `h,N,T,L,M` are strictly positive and `L,M` are displayed
coefficientwise-positive polynomials. Every zero-leading boundary is
evaluated exactly.

The decisive move was to collect the difficult special--ordinary internal
Rayleigh difference in the unused ordinary spoke. Collecting it in an
endpoint produces a large quartic; the better variable exposes a binary
endpoint form with a manifestly positive determinant.

## Exact verification and independent audit

The author checker enumerates all 2,048 augmented subsets, retains 712
forests at unit weights, reconstructs all 32 spoke monomials, and verifies
31 exact symbolic identities covering seven orbit certificates and six
positive-form determinants.

The fresh independent audit **PASSes without correction**. Its checker
imports no author implementation and builds the polynomial from the 54
backbone forests and their component factors. It independently verifies all
31 symbolic identities, 24 exact rational profile/root cases, and six
directly enumerated full marked graphs (four strict and two equality), with
zero counterexamples.

## Exact boundary and open problem status

Not proved: three unrelated arm multipliers, six arbitrary edge activities,
general theta subdivisions, a two-terminal/series-parallel closure theorem,
backbone cylinder conditioning, nonproportional rows, or negative association
jointly involving backbone/marked edges. A prior 36,000,000-evaluation
six-weight search found no negative value, but remains numerical evidence.

The famous general forest negative-correlation conjecture remains open.
Full Boolean FEI, unrestricted ML10 Sidorenko, and Kaplansky/direct
finiteness also remain open in this campaign.

## Prior-art status

Classical strong-Rayleigh theory and the current weighted-forest primary
literature are credited. Targeted source searches did not locate this exact
three-parameter `K_{2,3}` theorem. This is a bounded search, not a novelty or
priority certification; external specialist review is absent.
