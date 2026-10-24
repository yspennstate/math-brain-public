# account02/B14 early calculation — subprobability homogeneity for the overlap-slope compiler

Run `20260924T020607Z-account02-B14-QFORM-auto11`.

The first unpaid implication attacked here is:

> **QFORM-DIFFUSE-SLOPE-ANCHOR-OR-AGGREGATE-BEFORE-LOCALIZE-v1.** In the overlap-preserving hub receiver, arbitrary localization of a slope bank is zero-tax if an undecomposed original-coordinate anchor subbank retains a uniform fraction of the slope `l2` norm. A fixed-cardinality anchor cannot be substituted in a diffuse bank.

Start from account03/B14's proved overlap compiler. Its slice side supplies `||G_t||_2 <= sqrt(pi A)|t|^{-3/4}`. Replace the probability law of the slope bank by a finite positive submeasure `tau` of mass `m`. Assume its pushforward by the slope `S` has density cap `L`. Weighting by the arbitrary phase `exp(itR)` produces a complex pushforward density `g_t` satisfying

`||g_t||_1 <= m`, `||g_t||_infinity <= L`, hence `||g_t||_2^2 <= mL`.

The second Plancherel identity therefore gives

`||K_t||_2 <= sqrt(pi m L)|t|^{-1/2}`,

and the output submeasure `eta` obeys

`|eta_hat(t)| <= min(m, pi sqrt(A m L)|t|^{-5/4})`.

For `C=pi sqrt(A m L)`, the exact integral is

`int_R min(m,C|t|^{-5/4}) dt = 10 C^{4/5} m^{1/5}`.

Thus `eta` has a continuous density and

`||p_eta||_infinity <= 5 pi^{-1/5} A^{2/5} m^{3/5} L^{2/5}`.

This is the key homogeneity. If a countable positive localization has masses `m_j` and slope caps `L_j <= M0 m_j`, then each contribution is at most

`5 pi^{-1/5} A^{2/5} M0^{2/5} m_j`,

and summing over the pieces costs exactly zero:

`||p_Q||_infinity <= 5 pi^{-1/5}(A M0)^{2/5}`.

For a product slope bank `Z=(Z_H,Z_C)` and `S=a_H^T Z_H+a_C^T Z_C`, keep the anchor bank `H` whole and decompose the complementary law of `Z_C` arbitrarily into positive submeasures of masses `m_j`. Ball--Rogozin on the whole anchor gives

`||p_{a_H^T Z_H}||_infinity <= sqrt(2)/||a_H||_2`.

Convolution with a complementary submeasure of mass `m_j` yields

`L_j <= m_j sqrt(2)/||a_H||_2`.

Hence arbitrary remote/countable localization of the entire complement is zero-tax, with final bound

`||p_Q||_infinity <= 5 pi^{-1/5}[A sqrt(2)/||a_H||_2]^{2/5}`.

No support radius, fragment count, moment, centering, log-concavity, or post-rotation independence is used. The phase `R(Z_H,Z_C)` may be arbitrary because only `|exp(itR)|=1` enters the complex pushforward domination.
