# Primary literature audit for fleet01/B18 r35

## Juškevičius--Lee: exact transfer used

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190 (2015), Theorem 1. Their theorem assumes independent random vectors with density maxima bounded by prescribed constants `K_i` and compares the probability that their sum lies in an arbitrary measurable set with the corresponding sum of centered uniform-ball variables having the same density maxima. In one dimension the comparator for cap `K_i` is uniform on `[-1/(2K_i),1/(2K_i)]`.

For `Y_j=g_j Z_j` with arbitrary independent owner-admissible inputs `||p_(Z_j)||_infinity<=1`, `K_j<=1/|g_j|`; hence the comparison variable is exactly `g_j U_j^*` in law, with `U_j^*~Uniform[-1/2,1/2]`. Taking the measurable set to be the translated interval `(-eta-r,-eta+r)` gives

`P(|eta+sum g_j Z_j|<r)<=P(|sum g_j U_j^*|<r)`.

No moment, iid, support, log-concavity, smoothness, centering or symmetry assumption is imported. This is the primary theorem used in `REPORT.md`.

## Livshyts--Paouris--Pivovarov: valid but coarser here

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016). For a cap-one product density every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. For `k=1` this gives the profile-blind cap `sqrt(2)` for a normalized linear statistic. Its hypotheses also match the owner source class without moments or iid assumptions, but it loses the coefficient profile. The latest fleet02/B18 random-slope average used this cap to obtain `6e^(-1/3)(|a| ||g||_2^2)^(-1/3)`; the Juškevičius--Lee layer-cake transfer is sharper on the partner's two-flat slope.

## Herry--Malicet--Poly: quadratic-form regularity does not match the owner quantifiers

R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488 (2023). The paper studies quadratic forms in an iid sequence under the additional structural hypothesis that one input can be represented as a sufficiently smooth function of a Gaussian field. Its emblematic strong-density convergence result further centers and variance-normalizes the iid inputs and assumes a sequence of quadratic-form operators with Hilbert--Schmidt normalization, zero diagonal, and spectral radius tending to zero.

Those hypotheses do not match the owner target, which permits arbitrary non-iid cap-one densities, fragmented/unbounded supports, no moments, no Gaussian-functional representation, arbitrary diagonals, and only the lower spectral requirement that at least three eigenvalues have modulus at least one. Therefore this source is not an exact prior solution and was not imported into the proof.

## Literature status

The exact external theorem used here is Juškevičius--Lee Theorem 1. The other checked primary results either give only linear-marginal control (Livshyts--Paouris--Pivovarov) or impose materially stronger distribution/operator assumptions (Herry--Malicet--Poly). No exact prior theorem was identified in this targeted audit that directly proves the unrestricted owner statement. This is a hypothesis comparison only, not a novelty claim from absence.
