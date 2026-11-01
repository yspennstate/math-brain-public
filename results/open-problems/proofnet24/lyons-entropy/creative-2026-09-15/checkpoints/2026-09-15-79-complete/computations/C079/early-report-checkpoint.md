# C079 — checkpoint: independent phases and centered four-site curvature

Date: 2026-09-15. **IN PROGRESS.** This draft preserves a concrete route; no final theorem is claimed until the uniform estimates and verifier below are complete. General Lyons concavity remains open.

## Improved family checkpoint

The first candidate below may overlap C071 after complementation, so the main result is being moved to the genuinely frustrated family `L=I+Q/4`, `Q_12=Q_13=Q_14=1`, `Q_23=exp(i a)`, `Q_24=-exp(i b)`, `Q_34=exp(i c)`, with independent `|a|,|b|,|c|<=1/20`. The direct normalized triangle 123 is wrong-sign throughout. For inverse odds, triangle 124 also remains wrong-sign throughout: its three signed center edges have magnitudes at least `4/11`, while the inverse-odds perturbation norm is at most `72/581<1/8`; their argument deviations are at most `atan(11/21)<pi/6`.

The completed uniform estimates currently give `-H'' >= (671/800) FI + (5350601/625000000)||A||_F^2`, hence the simpler `-H'' >= (4/5) FI + (1/128)||A||_F^2`. They use `t=3/80` for the centered pair allocation, cubic remainder at most `13883/500000`, and quartic remainder at most `733149/625000000`. The arithmetic and atom identities are being packaged in a standalone exact verifier.

At this frustrated center, `Q` has eigenvalues `+/-1,+/-sqrt(5)`. The centered log coefficients are `eta_plus=(1/2)log(125/132)`, `eta_minus=(1/2)log(243/220)`, `c=log(4096/4125)<0`; the minimum and maximum centered pair coefficients are `(1/4)log(3125/2673)` and `(1/4)log(2187/1375)`. Both triple signs and the negative quadruple coefficient are retained in the Fisher compensation. The main theorem does not require nonnegative log-Mobius coefficients.

The earlier route below is preserved only as working history and will be replaced by the final report.

The planned family is `L=I+Q/2`, where `Q_12=Q_13=Q_14=1`, `Q_23=exp(i alpha)`, `Q_24=exp(i beta)`, and `Q_34=exp(i gamma)`, with conjugate reverse edges. The three phases are independent. On the cube `|alpha|,|beta|,|gamma|<=1/10`, every normalized triangle activity of `C=-Q/2` has negative real part, placing the family outside C071's phase cone. The goal is a full-Hermitian Fisher-plus-coercivity bound at `K=L(I+L)^(-1)`.

For general equal edge magnitude `r`, set triangle angles `x=(alpha,beta,gamma,alpha+gamma-beta)` and four-cycle angles `y=(alpha+gamma,beta-gamma,beta-alpha)`. Exact principal minors are:

- Singleton: `1`.
- Pair: `1-r^2`.
- Triple `T`: `d_T=1-3r^2+2r^3 cos(x_T)`.
- Full set: `d_4=1-6r^2+2r^3 sum cos(x_T)+r^4(3-2 sum cos(y_j))`.
- Atom normalization: `Z=16-24r^2+4r^3 sum cos(x_T)+r^4(3-2 sum cos(y_j))`.

Thus every atom is its displayed principal minor divided by `Z`. These are exact phase-polynomial identities, retaining all independent phases.

Write the frozen log table as `sum a_ij 1_ij + sum b_T 1_T + c 1_1234` plus a constant/modular term. At `R=K-I/2`, its full frozen curvature is exactly

`2 sum alpha_ij det A_ij + 2 sum eta_T tr(R_T adj A_T) + c D^2 det(R)[A,A]`,

where `alpha_ij=a_ij+(1/2)sum_{T containing ij}b_T+c/4` and `eta_T=b_T+c/2`. The `alpha_ij` are averages of four nonnegative conditional pair log interactions, hence are nonnegative for every positive definite odds matrix. The complete entropy curvature is this expression minus full atom Fisher information.

For a Hermitian three-by-three `E`, the exact bound for `2 tr(E adj B)/||B||_F^2` is the largest eigenvalue of the zero-diagonal three-by-three matrix whose off-diagonal entries are the complementary eigenvalues of `E` (C045). For four-by-four `R`, the analogous exact bound for `c D^2 det(R)[A,A]/||A||_F^2` is the maximum of (i) the largest eigenvalue of the zero-diagonal four-by-four matrix with off-diagonal entry `c lambda_k lambda_l`, complementing `ij`, and (ii) all `-c lambda_k lambda_l`.

These remainders will be absorbed by the pair main term using the total-count Fisher score and the marginal-pair Fisher inequality. The prospective bound on the stated phase cube is `-H'' >= (4/5) FI + (1/64)||A||_F^2`; its exact constants remain to be checked.

At zero phase, `R_0=-I/6+2J/21`. The centered pair coefficient is `log(9/5)/4`, every centered triple coefficient is `-log(5/4)/2`, and `c_0=log(4096/3645)`. The cubic spectral constant at `-R_{0,T}` is `(sqrt(417)-5)/84 < 3/16`; the quartic constant at `R_0` is exactly `1/28`.

An exploratory numerical script is retained at `computations/C079/explore.py`; its samples are diagnostics only. The uniform proof will use `sum x_T^2=sum y_j^2`, elementary cosine bounds, rational logarithm bounds, and a resolvent perturbation estimate on the entire phase cube.
