# C29 v2: complete logarithmic-cap depth20/32/64/128 data

Status: numerical evidence. Kind: special. Target: 1. This exact version is unaudited.
C29v1 remains an immutable separately audited16-root stage. Its PASS does not transfer to these added observations.

The C31v1 unequal-cap construction has its OWN exact-version PASS. That construction theorem does not validate numerical inherited error or supply positive linear mean growth.

The model is T3 ordinary motion with parent probability p, one resident, one incoming seed, absorbing recursive parent, persistent joint responses, and absolute-depth K_j=min{K>=1:4^K>=(j+2)^2}. Overflow retains ordinary motion and suppresses all waking until return; waking below horizon H is suppressed. Original origins are not cloned.

| p | H | independent reps | M per rep | mean R1 | between-run SD | mean PGF(1/2) | PGF between-run SD |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1/4 | 20 | 3 | 4000 | 2.689416667 | 0.1214645867 | 0.2554039307 | 0.01293060448 |
| 1/4 | 32 | 3 | 4000 | 5.84075 | 0.4245181828 | 0.06508069436 | 0.01088230407 |
| 1/4 | 64 | 3 | 4000 | 15.65616667 | 0.2624811104 | 0.01701425801 | 0.001050012022 |
| 1/4 | 128 | 3 | 4000 | 34.898 | 0.7998779985 | 0.01575051364 | 0.0006616804823 |
| 6/25 | 20 | 3 | 4000 | 1.538583333 | 0.02704664181 | 0.4392613932 | 0.006866447284 |
| 6/25 | 32 | 3 | 4000 | 1.75225 | 0.007403546447 | 0.3958763021 | 0.0007914171997 |
| 6/25 | 64 | 3 | 4000 | 2.234416667 | 0.08561700084 | 0.3161346029 | 0.01348834211 |
| 6/25 | 128 | 3 | 4000 | 3.96875 | 0.1623476209 | 0.1416168722 | 0.008454531736 |

These are floating point empirical-population observations, not exact-law bounds. Bars are sample SD across whole independent runs, not phase-confidence bounds. Conditional parent-sampling SE and replica SD both omit unbounded inherited empirical-child-law bias. Every row is a completed absolute-level0 root; no partial population is treated as a root.

## Exact plausibility envelopes (not sample confidence bounds)
For p=1/4, C30 gives E R_H<=(H+2)/3. A direct C26 refinement is E R_H<=((1-1/16)H+2)/3: on E, both initial first steps go upward, with probability1/16, R_H=2. All deeper all-active hit indicators are independent of E and have total mean H/3. Subtract E[C_H 1_E]=P(E)(2+H/3) from E C_H and add back E[R_H 1_E]=2P(E). At H128 this refined exact expectation ceiling is122/3, compared with the observed34.898. It is an expectation ceiling, not an almost-sure bound on an empirical average.
At p=6/25, beta=6/19 and3beta=18/19. Even all potential residents awake give E R_H<=beta+beta*sum_(n=0)^H(3beta)^n<120/19. The observed H128 mean3.96875 is below this exact expectation ceiling. An apparent growing finite-depth curve at this p cannot establish recurrence.

## Threshold and proof gap
The physical-p recurrence threshold of ANY genuine original-path T3 lower family is at least1/4: in the all-active full tree, sum_(m>=1)3^m beta^m is finite for p<1/4, and every individual reflected-root walk is transient. Thus a strict below-quarter threshold is impossible in this parametrization. This standard sanity check does not settle the boundary. No model threshold is estimated or bounded here beyond that general floor.
The sampled p=1/4 means grow through H128, but positive limsup E R_H/H for the EXACT law is still unproved. C30 would turn such a bound into full ordinary recurrence; C31 supplies the correct lower coupling. Neither supplies the missing inequality. The full ordinary T3/T4 problem remains OPEN.

## Reproduction and provenance
Run simulate_depth_dependent_excursions.py --ps 1/4,6/25 --depths 20,32,64,128 --runs 3 --samples 4000 --seconds 180 in resumable bounded chunks. The script checkpoints each absolute depth, checks memory and uses one CPU thread. Summarize with summarize_c29.py. The source-hashed raw directories and root summaries are indexed in the frozen stage.
Source SHA256: de781b2c091084b5a5fcfc10e902a7948f9d6f7c34be95f8ef941a5bbfcbe944
Frozen stage SHA256: 0cb660590dd5cab76696ae618bf0e5cca4a99936e03559ba8cbeddba81651f2a
Controls: C29_DIRECT_CONTROLS.json (independent direct finite trees, resident-once fault, scalar/batch and constant-cap compatibility); C29_DEGREE_CALIBRATION_RESULTS.json (d2 growth, d5 plateau, numerical only). A separate M16000 stability campaign is unfinished and is not silently included here.
Sources: owner-own-work; C29_STAGE_v2.json; C26v1/C30v1/C31v1 exact-version PASS in AUDITS_FROM_REVIEWER.tsv; HJJ arXiv:1404.6238 Theorem4 only for the ordinary zero-one implication after a true positive mean-growth bound.
