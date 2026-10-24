# Rigor check — account02/B15 bounded-localization obstruction

1. **Target spectrum.** `A_m=J_m/m \oplus J_m/m \oplus (-J_m/m)` has exactly three nonzero eigenvalues `1,1,-1`, since every `J_m/m` has spectrum `{1,0,...,0}`. Thus every `A_m`, `A_{m,0}`, and `A_{m,e}` with `0<e<1` satisfies the owner hypothesis.

2. **Principal blocks.** If a physical set contains `k_j` coordinates from bank `j`, the three bank blocks are exactly `J_{k_j}/m`. Hence the nonzero bank eigenvalues are `k_1/m,k_2/m,-k_3/m`. The third absolute eigenvalue is `min(k_1,k_2,k_3)/m`; maximizing the minimum subject to `k_1+k_2+k_3=r` gives `floor(r/3)/m`. This proves the exact localization formula, not only an asymptotic estimate.

3. **Complement.** The complementary bank counts are `m-k_j`, so the complementary third curvature is `1-max_j k_j/m`, hence at least `1-r/m` whenever that lower bound is positive. Thus an `o(m)` physical carrier cannot absorb the three global unit directions.

4. **Perturbed physical blocks.** For `A_{m,e}=A_m\oplus[e]`, a physical principal block has up to four nonzero eigenvalues `k_1/m,k_2/m,-k_3/m,e`. If the third largest comes from three bank eigenvalues it is at most `floor(r/3)/m`; if it uses `e` as the third one it is at most `e`. Therefore `s_3<=max(floor(r/3)/m,e)`.

5. **Bank projection density.** Each normalized bank sum has a unit coefficient vector, so the one-dimensional Rogozin/Ball product-projection theorem gives density cap `sqrt(2)`. Squaring produces the bound `sqrt(2)s^{-1/2}`. The beta integral is exact: `int_0^t [u(t-u)]^{-1/2}du=pi`. Thus two same-sign bank squares have density cap `2pi`; convolution with the independent third signed square preserves that cap.

6. **Required-source application.** In e5f71d79... Theorem F choose `I` equal to all bank coordinates and residual `B=0`. The spectral-frame Gram matrix is `G_I=I_3`, every normalized leverage is `1/m<=1/2`, and `|lambda_1lambda_2lambda_3|=1`. The theorem therefore yields the claimed full-law bound `12`.

7. **Remote-support perturbation.** With iid bank uniforms, `Y_j` lies in `[-sqrt(m)/2,sqrt(m)/2]`; therefore `Q_{m,0}` is supported in `[-m/4,m/2]`, length `3m/4`. For `X_0~Unif[R,R+1]`, `Z=eX_0^2` has density `1/(2sqrt(ez))` and height `1/(2eR)`. Setting `R=L/(2e)` makes this height exactly `1/L`.

8. **TV separation modulo translations.** `Q_{m,e}=Q_{m,0}+Z` has density cap `1/L`. Every translate has the same cap, so it places at most `(3m/4)/L` mass on the support interval of `Q_{m,0}`. Taking `L>=3m/(4eta)` yields total-variation distance at least `1-eta` from `Q_{m,0}`, uniformly over all deterministic translations.

9. **Not a QFORM counterexample.** The base output has height at most `2pi`; the perturbed output has height at most `1/L`. The construction refutes only bounded-localization plus operator-norm continuity/truncation as a universal proof interface.

10. **Rough ruled bridge.** Mollification is in original coordinates, preserves the cap, and converges in product `L^1` by telescoping. Square completion for an invertible active physical block is an original-coordinate translation. Restriction to the fixed sheet and deterministic pushforward contract total variation. Therefore the smooth ruled interval bound passes with the same constant; continuity is not part of the height argument.

No hidden moments, bounded supports (except in the deliberate obstruction witness), log-concavity, spectral-coordinate independence, or continuity premise is used in the universal statements.