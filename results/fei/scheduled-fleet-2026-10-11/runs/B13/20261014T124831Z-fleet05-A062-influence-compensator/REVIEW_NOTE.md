# Scoped independent reconstruction of A030's mismatch transport

Source: A030-CONDITIONAL-TWO-CORE-CONTROLLER-TRANSFER v1, statement SHA256 ce0f365b6e7e8c20623ba5c7c64c122620b8bc45ac7a139edd84eec424b20d44, PROOF.md first paragraph and section “Conditional full interleaving lift,” the delta*r_h data-query clause only.

Verdict: HOLDS_AT_STATED_SCOPE. This accepts neither price22, the correction profile, nor the conditional bundled interleaving theorem.

At a reached independent-block history, let U,V be the two actual independent Boolean core outputs. Directly, Pr(U!=V)=E[(1-UV)/2]=(1-EU EV)/2. When a physical coordinate of U is queried, the mean of V is fixed and the fair average of the two means of U equals its parent mean. Therefore delta=average delta_child. A reserve r_h depending only on the unchanged controller history is the same in both children, so delta*r_h has exactly zero drift. The argument is symmetric for a V query; independent initial randomness may be fixed first. This reconstruction uses indicator expectations and the physical branch law rather than A030's spectral profile algebra.

The exact checker directly counts mismatches on all256 pairs of two-bit core functions on independent blocks, and all4 data-query directions per pair. It also reconstructs the means of the untouched block in each child. The result is 1024 query cases and6400 exact rational assertions, zero failures. This is independent validation of the scoped transport; no entropy assertion is tested here.

Shared physical data break the factorization EUV=EU EV. The new A062 fixture has actual disagreement harmonic but mean-product proxy drift1/16. This does not refute A030's stated independent-block theorem, which explicitly excludes shared physical data. Use the actual joint disagreement event when moving its controller owner beyond that scope.
