# P0282 rankwise-cutoff route — idea recorded before production checking

The current `3129/5129` theorem uses one affine good-parent cutoff `r_s=ceil(s/5+8)`. Its asymptotic deterministic loss is controlled by the cutoff slope, while its finite-rank bad mass is controlled by the intercept. Those are competing jobs and one affine cutoff need not be optimal.

New route for this invocation: **swap the cutoff optimization and the rank quantifier**. For each finite `s=j-1`, use the exact Plancherel first-row tail from the already validated Gessel/Toeplitz machinery and choose the integer cutoff `r` that maximizes the literal lower bound

`B(j,K,r-1) * (1 - Pl_s(mu_1>=r)/rho_0^2)`.

For the eventual tail only, switch to a lower-slope analytic envelope, initially `r_s=ceil(s/6+b)`, whose asymptotic threshold is governed by `c(c-1/6)>2` when `K~c j`. This makes constants near `c=3/2` plausible, corresponding to `k/n` near `3/5`, while the exact finite optimizer is intended to pay for the seam where the crude union bound is too weak.

Candidate first target for exact testing: `K >= (153/100) j + 1`, equivalently `253 n?` No: since `K=n-j+1`, this is exactly `100 n >= 253 j`, hence `k/n >= 153/253 ~= 0.6047430830`, which would strictly improve the retained `3129/5129 ~= 0.6100604406` long-LIS fraction.

Section-B routes instantiated here: **#27 SWAP THE QUANTIFIERS** (rankwise finite cutoff before global envelope), **#28 REPLACE FOR ALL WITH FOR TYPICAL** (good/bad Plancherel split with a thinner typical window), and **#30 DO ONE SCALE AT A TIME** (exact finite seam plus asymptotic residue-class contraction). All are recycled because all 30 methods were previously used on P0282, but this triple differs from the preceding run's #5/#20/#26.

No theorem is claimed in this note. The next step is exact arithmetic: determine whether every finite seam rank admits a cutoff with the literal source lower bound above one, then prove the eventual union-bound regime separately.