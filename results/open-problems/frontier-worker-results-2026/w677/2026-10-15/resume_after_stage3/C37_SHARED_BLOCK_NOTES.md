# C37: complete shared-site block screen

Status: numerical evidence. Kind: route-failure. Target: 2. No independent audit.

Ordinary T3 and T4 remain OPEN. This is a screen, not a finite-cap
obstruction theorem and not an all-height claim.

A height-L block contains levels 0 through L of T4. All awakenings within
one episode share the same awake set. Residents wake once, including when
descendants of different frogs collide. Frogs follow ordinary walks until
exiting the block; there is no particle cap or time truncation. TOP starts
with two frogs at the block root and its resident already consumed. BOTTOM
starts with one frog at a leaf and the whole leaf-to-root spine already warm,
with those residents absent. ROOT is BOTTOM with degree four at the global
root. Fresh block copies on exits still forget discoveries between episodes;
the family therefore does not retain all-scale sharing. The infinite upper
coupling is the C33 candidate, still awaiting independent audit.

Write U_T,D_T,U_B,D_B for expected up/down exits. The bulk two-type weighted
matrix is [[D_T*t,U_T/t],[D_B*t,U_B/t]], where t=z^(L+1). Its minimum spectral
radius is sqrt(D_T*U_B)+sqrt(U_T*D_B). A root-aware certificate is additionally
required even if that bulk number is below one. None was obtained here.

| Height L | Sites | Trials per context | Bulk estimate | Delta standard error |
|---|---|---|---|---|
| 2 | 21 | 12000 | 1.254315 | 0.004810 |
| 3 | 85 | 15000 | 1.303163 | 0.008081 |
| 4 | 341 | 15000 | 1.345118 | 0.013126 |
| 5 | 1365 | 10000 | 1.400182 | 0.032421 |
| 6 | 5461 | 6000 | 1.523157 | 0.087529 |

The height-two connected-subset formulas give 1.25732317700830466789
at both 60- and 100-digit Decimal precision. Neither is an enclosure.
There are 126 TOP and 224 BOTTOM/ROOT rooted-subset classes. The triangular
exact-set closure sums all subsets and shares the resident mask; it does not
multiply independent activation probabilities. Probability masses sum to one
to the working precision and no significantly negative atom was found.

An independent queue-based implementation uses explicit walk exits for
12,000 trials per context at height two; each of its four measured means is
within one standard error of the formula. The larger-block implementation
instead sums harmonic exit weights over activated residents: a vertex at
level j has probability h_j=(4^(L+1-j)-1)/(4^(L+2)-1) to exit upward. Its path
is unused until activation, so that probability contributes to its expected
exit count. For TOP the two seed contributions are 2*h_0; for BOTTOM the seed
contribution is h_L and warm-spine residents are absent. Downward contribution
is the number of activated frogs minus the harmonic upward sum. This gives
an unbiased mean estimator, not a pathwise upper bound. ROOT upward mean is
zero. Covariances of the two estimates are included in the delta error bar.

All bars are descriptive Monte Carlo standard errors. The nonlinear estimate
can have finite-sample bias; rare clusters can dominate its variance, especially
at height six. The observed ROOT/BOTTOM downward ordering at height six differs
by less than one combined standard error. Neither an asymptotic confidence
statement nor a certified spectral inequality is claimed. No threshold was
measured. Source hashes, sample counts, variances and elapsed times are saved.

The tested point estimates move away from contraction as blocks increase.
Do not extend this into another finite-block obstruction proof. The remaining
target2 gap is a useful SITE-counting comparison sharing discoveries across
block entries and split lineages, with a rigorous summability certificate.
