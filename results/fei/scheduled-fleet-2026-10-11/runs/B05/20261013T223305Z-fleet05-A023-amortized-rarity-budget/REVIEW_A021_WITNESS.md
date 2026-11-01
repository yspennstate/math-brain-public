# Independent reconstruction of the new A021 overlap obstruction

Source: A021-CONTROLLER-EXPOSURE-REFINEMENT@1, run 20261013T214613Z, DERIVATION.md sections "A five-bit counterexample" and "Balanced data-split identity" control-root specialization. Reviewer A023, no repair contributed. Verdict HOLDS for the five-bit witness and its arbitrary-balanced-core CONTROL-root transfer only. The tensor-selector prefix identities and all-680-controller closure are not accepted by this review; the source's whole claim remains pending review.

Construct the positive-literal controller A=x1x2 OR x1x3 OR x0x2x3 directly. Enumerate its 16 vertices and its edge boundary, rather than import A021's certificate/helper. EA=7/16 and I(1-2A)/2=3/4. With balanced dictator core z, F=1+A(z-1) is a five-bit actual Boolean sign. Query x0 and independently compute its integer Walsh coefficients and physical child product. The exact values are d=1/16 and I(F0F1)/2=1/4, with

    B-4d=(192log2(2)-432log2(3)+60log2(5)-98log2(7)
           +52log2(13)+82log2(41))/256>0.

The equality is an exact rational prime-log vector, checked against the displayed source formula. The positive sign uses outward Fraction bounds from a positive atanh series with exact tail, no decimal threshold. The full vector and interval are in out/witness.json and out/sign_certificates.json. The fixed control order has bad credit 1/4, whereas separator x1 first has zero control bad credit on this fixture.

For any independent balanced core g, each nonempty-core Fourier row multiplies the controller coefficients by ghat(T). The erasure kernel is homogeneous degree two, and sum_(T nonempty) ghat(T)^2=1. Its pure-controller row is unchanged. Thus B and d at a control query are EXACTLY the dictator-core values, for all such g. This analytic reconstruction is also checked on the separately built balanced bent4/flip core in code/check_separator.py. The face charge changes with I(g), as prescribed by I(F0F1)/2=e I(g)/2+J(D)/2; it must not be called invariant with the entropy.

This confirms the important objection to automatic three-event goodness and any function-independent control order. It does not contradict A023's two-event fresh-block theorem, nor prove that every selected order has a bad node. The new separator policy gives a model-specific remedy with one owned reserve; arbitrary-depth ownership remains open. Source versions/hashes and the exact independently executed outputs are saved locally.
