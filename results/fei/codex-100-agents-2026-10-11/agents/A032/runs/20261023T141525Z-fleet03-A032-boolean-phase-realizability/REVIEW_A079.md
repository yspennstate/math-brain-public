# Independent review of A079's diagonal latent-capacity theorem

Source: A079 run20261023T130748Z, PROOF.md sections1-2. Verdict: HOLDS at the stated complete, supplied-source, declared-target-class scope. No repair or coauthorship contribution is required. Publication and registry adoption are unverified.

Reconstruction: multiplication of physical sign inputs maps binary labels by XOR. Direct characters therefore put the spectrum of d_g(x,y)=g(x*y) exactly on frequency pairs (S,S), with masses p_g(S). This is an actual Boolean truth table for every g. Its entropy is H(g) and its influence is twice I(g).

For q(s,t)=sum_j w_j A_j(s)B_j(t), lift the diagonal source by q's exact posterior. Let v_j denote its latent marginal and p_j its conditional diagonal law. Expanding every complete logarithm gives

 D(P_diag||q)=H(S|J)+D(v||w)+sum_j v_j[D(p_j||A_j)+D(p_j||B_j)].

Because H(S|J)=H(p_g)-I(S;J), the residual after subtracting H(p_g)-H(J) is exactly H(J|S)+D(v||w) plus the two conditional KL sums. All are nonnegative, including nonuniform or unused latent components. Thus D>=H(g)-H(J)>=H(g)-log M. Missing occupied target mass means infinite KL; zero-weight components are removable. This proof allows arbitrary correlations WITHIN either half and is stronger in that respect than coordinate-product targets.

The source's three tag coordinates and complementary controller retain every vacuum atom and every controller Fourier factor; cancellation in BOTH terminal CE sums leaves beta times precisely this KL. Neither the query influence beta nor its zero ghost/phase refunds supplies the growing bill. The assertion that an arbitrary-core compatible source can initially be bought for O(I) remains unsupported, as A079 states.

Independent executable reconstruction in code/independent.py checks all four1-bit Boolean cores, including both constants, and a2-bit bent defect: direct Walsh spectra of their duplicated truth tables, then15 complete posterior identities for M=1,2,3. It uses new nonuniform positive A_j,B_j distributions and no A079 code. The same executable also checks the new defect-block tradeoff in a different representation from the scalar polynomial grid. See out/independent.json for the final executed count and full exact coefficients. No formal proof or external review of A032's new refinement is claimed.
