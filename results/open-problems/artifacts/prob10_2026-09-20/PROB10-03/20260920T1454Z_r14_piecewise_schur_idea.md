# PROB10-03 R14 idea note — piecewise Schur continuation before code

Status: exploratory mathematical route only; no endpoint claim.

The current third-full obstruction is not existence of a good floating root but a rigorous outward inclusion. The newest NM13-03 Schur theorem replaces the weakest four-dimensional direction by a 3D branch solve plus an RH sign crossing, but it asks for one uniform root tube over the whole m-interval. The new route for this bounded iteration is to prove a **piecewise validated Schur-continuation theorem**: cover an m-interval by finitely many overlapping slabs, certify a unique 3D root in a local z-box on each slab, and glue the local branches through overlap uniqueness. This should permit a materially wider crossing interval than m0 +/- 0.001 without requiring one oversized contraction box. The wider interval is useful only if the reconstructed alpha remains below the current rigorous upper endpoint; the purpose is to trade a modest alpha cap for a much larger rigorous RH endpoint sign margin.

Three attacks compared before coding:

1. **Piecewise Schur continuation (chosen):** prove the gluing theorem first, then numerically scout a cap-compatible m-window and local conditioning. This changes the proof architecture and can amplify RH sign margins while preserving a source-improving alpha cap.
2. **Direct 4D Krawczyk:** already known to mix the weakest Schur direction into the contraction block; newest reports measure much worse conditioning than the 3D subsystem. Do not spend this run rebuilding it.
3. **Entropy-cage-only sign certification:** matched-Gaussian/Stein cages are valuable for bounding c-sector terms, but a generic cage need not be narrow enough to resolve the small RH crossing sign. Quantify this obstruction after the theorem rather than assuming the cage closes the sign.

Negation tests planned after the proof: (i) continue the 3D branch both ways until the strict chart or solver fails; (ii) check whether alpha is actually capped on a useful wider interval rather than assuming monotonicity; (iii) compare GH orders and local 3D singular values; (iv) quantify the RH uncertainty induced by the existing entropy cage scale. None of these numerical tests will be promoted to a source endpoint.
