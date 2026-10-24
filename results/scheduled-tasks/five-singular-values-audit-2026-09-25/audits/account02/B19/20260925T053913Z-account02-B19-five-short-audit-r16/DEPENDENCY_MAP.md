# account02/B19 r16 dependency reconstruction

1. **Theorem 1.1 (L54–60, L618–639).** Normalize (K=s=1). Exhaustive cases are no pivot,
   diagonal pivot, or pair pivot with all diagonals small. No pivot uses Proposition 7.1(a).
   A diagonal pivot uses Lemmas 5.1 and 2.4 plus Proposition 7.2 on the one-coordinate Schur
   complement. A definite pair uses Lemma 5.2 and conditioning. An indefinite pair uses Lemma 5.3,
   Lemma 5.4 on its Schur-complement critical value, and conditioning. Rescale (Y=KX) and (A/s).
2. **Proposition 7.2 (L598–616).** No-pivot branch is Proposition 7.1(b). Pair branch is Lemma 5.6.
   Diagonal branch completes the square, uses the one-coordinate Schur loss from Lemma 2.6,
   the square-root density envelope from Lemma 5.1, conditional domination Lemma 2.4,
   kernel bound Lemma 5.5, and Lemma 5.4's no-atom/log-moment estimate.
3. **Proposition 7.1 (L586–596).** Proposition 6.4 supplies (E_3>gamma_3^6) or
   (E_2>gamma_2^4); Corollary 4.4 converts these to density or negative-half-moment bounds.
4. **Proposition 6.4 (L560–580).** No-pivot gives (|a_{ii}|<eta), (|a_{ij}|<a_0).
   Compress (A) to (2m-1) eigendirections, use Lemma 6.3 to choose a sign pattern with small
   Frobenius perturbation, Lemma 2.5 for perturbation/compression, Lemma 6.2 for duplicated
   crossing singular values, and Lemma 2.7 for (E_m).
5. **Corollary 4.4 (L380–391).** Theorem 4.1 gives (|phi|^2) decay. Lemma 2.2 integrates
   (t^{-3/2}) decay for a density; Lemma 2.3 integrates the (t^{-1}) envelope against
   (|t|^{-1/2}) for the half moment.
6. **Theorem 4.1 (L243–379).** Greedy row promotion creates a hub (H) whose residual
   (ell)-volume marginals are diffuse. Lemma 4.3 pays that hub. The ratio of hub constants
   decreases, so the worst case is (H=arnothing).
7. **Lemma 4.3 (L271–371).** Gram factorization (Lemma 2.7) produces residual volumes and weights.
   Step 1 decouples (X_J) with an independent copy. Step 2 treats physical hub coordinates by
   Plancherel against a complex measure dominated by the projected-product density; C02 supplies
   the omitted Jensen step. Mollification makes the (L^2)-norm measurable and returns to physical
   coordinates. Step 3 applies weighted Hölder. Step 4 uses Lemma 3.2 on the projected difference
   vector and Lemma 3.3 with exponent (1/alpha_ige2). Step 5 is exactly Lemma 4.2 entropy.
8. **Projection layer (L175–242).** Theorem 3.1 is proved by heat flow: the BL frame makes
   (partial_	au F-Delta Fge0); Gaussian bounds justify differentiation/integration by parts,
   the large-time limit gives the Gaussian extremizer, and the small-time limit uses Fatou.
   Lemma 3.2 applies it to fibers of an orthogonal projection; zero-(eta) factors are harmless
   values (le1). Lemma 3.3 combines difference-density (le1), Plancherel and Lemma 3.2.
9. **Linear algebra layer (L140–174).** Lemma 2.5 follows from approximation numbers after the
   padded-index repair. Lemma 2.6 uses the Schur inverse block plus Cauchy interlacing, followed by
   an (arepsilon I) limit. Lemma 2.7 is characteristic-polynomial minors/Cauchy-Binet plus a
   Gram Schur complement.
10. **One/two-coordinate layer (L393–512).** Lemma 5.1 is the two-branch scalar change of variables
    (C08 only fixes the critical-point representative). Lemma 5.2 is elliptic polar integration
    after deleting the seam (C01). Lemma 5.3 is a hyperbolic chart in original coordinates;
    separate (i,i') pay the two tails, and C03 adds the null critical level. Lemma 5.4 gets a
    19(sqrt{ho/L}) small-ball estimate either from a diagonal coefficient or a random physical
    cut plus Corollary 4.4(c); layer cake gives (L_0). Lemma 5.5 is an exact kernel integral plus
    one-dimensional rearrangement. Lemma 5.6 combines Lemmas 5.2/5.3/5.5.
11. **Fourier/conditioning base (L80–139).** Lemma 2.1 uses the stated transform normalization,
    Gaussian inversion and Fubini. Lemma 2.2 integrates a power envelope. Lemma 2.3 uses the Gamma
    representation and Tonelli. Lemma 2.4 is measure domination under independence.

All conditioning is on original coordinates. Orthogonal changes appear only inside deterministic
linear-algebra/change-of-variable arguments; no independence after rotation is assumed.
