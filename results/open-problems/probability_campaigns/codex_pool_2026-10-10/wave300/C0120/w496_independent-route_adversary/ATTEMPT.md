# C0120 independent route, before paired-proof access

Written 2026-10-10 before reading w495's proof.

Initial route to check against the prior attempts: study the Gaussian chaos spectrum of the centered log partition function. An Ornstein-Uhlenbeck covariance integral converts noise decay into a variance bound, and the relevant missing input may be the low-degree chaos mass rather than a product of conditionally small row events. This route applies only if the recovered model is Gaussian, or admits a separately justified replacement theorem. It is not yet an argument for the target.

First obstruction: n/log(n) cannot be converted into n^(1-delta) for a fixed positive delta by changing constants (CLAIMS.jsonl, w496-C0120-001). For now the exact source assumptions and current openness are UNKNOWN.

The primary statement has now been recovered: the cited theorem concerns a free-endpoint Gaussian ground-state maximum on the east/north Z^2 lattice. SOURCE_STATUS.json records the correction, independently recomputed primary PDF hash, and UNKNOWN current openness. The older H/I and Lean targeted searches found no additional C0120 proof; the intake attempt invokes quantitative chaos without supplying its rate.

The resulting independent work is in INDEPENDENT_DERIVATION.md (a polynomial-chaos cutoff and a jointly independent layer-average split) and GAUSSIAN_FAN_OBSTRUCTION.md (a rigorous Gaussian path-maximum control with qualitative chaos and no power variance gain). The fan proof uses Gaussian quantiles and bivariate tail bounds, rather than the prior attempt's unproved transversal exponent. All new claims are pending review. The fan is outside the fixed lattice and its degree grows with n.

After those derivations were saved, w495's originator proof was read and checked in AUDIT_W495_PROOF.md. Its bounded-degree binary-tree control instead targets first-chaos smallness; our fan retains an explicit vanishing-noise chaos assertion, and our source-model layer split records the harmonic Gaussian component. These scopes are complementary and neither supplies the polynomial lattice input.

NEXT: Independently review the six w496 claims, retaining the unproved lattice chaos-mass estimate through degree ceil(n^delta) as the single parent-problem gap.
