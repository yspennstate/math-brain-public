SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T15:44:25Z.
attacking: exact entropy-optimal third-volume weighting on a dense permutation-symmetric spiked cross block, with sharp Hausdorff--Young constants retained instead of the generic e^3 relaxation.

# Early substantive checkpoint

Full QFORM target remains OPEN. This checkpoint records the first new calculation before the full report.

Let `M` be an original-coordinate cross block and let `Z=E3(M)>0`. In the canonical squared-3x3-minor law, write `alpha_i` and `beta_j` for row/column inclusion marginals. Repeating the proved q=1 Brascamp--Lieb/Hausdorff--Young calculation but **not** replacing the marginal products by `e^(3/2)` gives

`|phi_Q(t)|^2 <= R(alpha,beta) * pi^3 * Z^(-1/2) * |t|^(-3)`,

where

`R(alpha,beta)=prod_i (1-alpha_i)^(-(1-alpha_i)/2) * prod_j (1-beta_j)^(-(1-beta_j)/2)`.

Hence, with `K=R^(1/2) pi^(3/2) Z^(-1/4)`,

`|phi_Q(t)| <= min(1,K|t|^(-3/2))`,

so exact integration gives

`||p_Q||_infinity <= 3 R(alpha,beta)^(1/3) Z^(-1/6)`.

This applies whenever all row marginals are <=1/2, and supplies a continuous C0 density. In the doubly balanced six-by-six case `alpha_i=beta_j=1/2`, one has `R=8`, hence

`||p_Q||_infinity <= 6 Z^(-1/6)`.

Stress family: `u=1_6/sqrt(6)` and

`M=s I_6 +(L-s) u u^T`, with `L>s>0`.

Permutation symmetry makes every physical 3-row volume equal; the canonical row and column marginals are exactly 1/2. The squared singular values are `L^2,s^2,...,s^2`, so

`Z=10 s^4 (L^2+s^2)`.

At `s=2,L=8`, `M=2I_6+J_6`, every 3-row Gram determinant is `544`, hence `Z=20*544=10880`, and the new exact-HY certificate is

`||p_Q||_infinity <= 6*10880^(-1/6) = 1.274617179932979...`.

The generic 3e relaxation would give `1.732384359226765...`; the exact marginal factors matter.

Remaining tasks in this run: prove global entropy optimality of the canonical weight under the q=1 gate, show the newest projection-tail sufficient condition fails on this same block, apply fleet02/B04's completed support-defect exit after conditioning two physical rows, and build a fully dense indefinite target-valid A with exact spectrum.
