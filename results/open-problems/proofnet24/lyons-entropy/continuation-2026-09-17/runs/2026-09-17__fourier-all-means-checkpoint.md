# Continuation checkpoint: full coupling rectangles and joint common mean

Model/reasoning setting not independently exposed. PARTIAL; unrestricted Lyons OPEN. Frozen `B_Phi`: UNMEASURED -> UNMEASURED, no movement. Restricted coverage does move: every fixed pair of means, all physical couplings; additionally all three affine parameters in the common-mean family. Moves 4, 14, 25 continue.

`FOURIER_ALL_MEANS.md` contains the proof. The six measured orbit probabilities give three nonnegative atom logarithms alpha, each at most the corresponding count logarithm. The all-sign local Shepp-Olkin inequality therefore controls their signed acceleration. The exact correction for independent pair-mean motion is only `4 a' b' log(O/P)`.

This proves all fixed-mean coupling rectangles without an imbalance restriction. It also proves joint concavity in `(t,x,y)` for `K=F diag(t+x,t+y,t-x,t-y) F*`, because the correction is then nonnegative. The full four-parameter case still requires payment for the adverse sign cone; equation (14) of the report states the exact remaining inequality.

Executed `verify_fourier_all_means.py`: PASS, 21 exact rational polynomial identities and 36 exact rational curvature cases with rigorous logarithm enclosures. These are self-checks, not independent audits. The source local inequality was read directly in Hillion-Johnson arXiv:1503.01570, Proposition 2.4. The earlier verifier supplies 34 polynomial identities and 70 exact Fourier minor entries.

Bounded literature queries in this continuation: `"entropy concavity" "exclusion" Bernoulli`, `"Lyons" "entropy" "circulant" concavity`, and `"entropy" "random transpositions" "concavity"`. They did not locate a resolution or the present restricted statement. This is not a complete prior-art review and establishes no novelty claim. The supplied X088 and C075 reports were read in full before the new proof.

Exploration files retain the negative-imbalance and adverse-cone searches as numerical evidence only. Neither a favorable scan nor a failed lower bound is called a source-theorem resolution.
