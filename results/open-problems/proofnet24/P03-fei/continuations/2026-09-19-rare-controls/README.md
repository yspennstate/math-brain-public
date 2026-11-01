# Rare controls and affine entropy excess

Full FEI remains OPEN. Read `REPORT.md` for the complete proofs and restrictions. Run `python verify_rare_controls.py --part all --output verification.json` with the included unchanged `prior_exact_entropy.py`. Compare parsed JSON values rather than formatting; elapsed time may differ. The archived output is compact-formatted from an actual successful execution.

Main result: for Phi_C=H-C M, any Boolean input f, c>=4 fresh controls, and arbitrary quadratic Q on all old/new variables,

    Phi_C((-1)^Q Gamma_c f) <= 2^(-c) Phi_C(f),
    C >= 17/4 + 1/(2 ln2) < 5.

Starting from proved seeds, this yields a constant below five under arbitrarily many controlled-quadratic stages, disjoint products and surjective affine maps. High-degree terms can share the control blocks. The operation ADDS new bits and is NOT the fixed-domain multiplicative-derivative chain.

The new rank bound M(g(-1)^Q)>=M(g)+(1/2-4delta)rank(B_Q) holds for EVERY Boolean base of negative density delta<=1/8. No clause factorization is needed. For delta<=1/16, quadratic twisting cannot increase H-CM when C>=4. Its coefficient is sharp on one-point bases.

The report also treats unstructured exponentially rare errors around quadratics, and proves why arbitrary unknown seeds behind a fixed rare gate still retain the full FEI difficulty. Do not drop freshness, seed certification, rarity, or joint-surjectivity hypotheses. No universal FEI, independent audit, Lean proof, or novelty clearance is claimed.

Script SHA256: 854933ec5a344b94574125d83016834999857ad84fd4747d843bb96306ec357e.
Dependency SHA256: 9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab.
