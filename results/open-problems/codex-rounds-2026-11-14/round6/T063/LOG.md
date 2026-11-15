# T063 log, round 6

Task: “take the NEXT checkable step on this problem, building on that work”, received 15 November 2026, approximately 10:19 Asia/Tbilisi. Shell clock checked at 10:20:12 +04.

All writes are restricted to this folder. In particular, the task-specific restriction supersedes the global instructions to mutate the brain, checklist and mesh stores. No subagents, git, external messages or publications.

## Literature check (under five minutes)

Used the web search tool for `six vertex Gaussian free field 2026 Averous Duminil Copin He Lammers Manolescu`, `"2611.00291" Pei six vertex`, and `"six-vertex" "Gaussian free field" November 2026`.

Opened Yan Ru Pei, *Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*, November 2026, https://hexagonmath.org/pdf/2611.00291v1 (hexagon identifier, not arXiv). Also opened the arXiv record https://arxiv.org/abs/2610.07454 and the September OpenAI manuscript landing page https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/ . These are the same updates already recorded by the earlier workers. No newer full-range solution was certified. Continue with the finite audit rather than treating the September claim as established.

Read the startup memory index and compute governor state read-only. Governor reports warn/cpu_saturated, owner_away_open; the planned runs are small standard-library exact enumerations, one thread under nice -n 15. Earlier reports and proofs have been opened; further detailed reads follow.

## Earlier result independently rechecked

Read the available reports, logs, proofs and scripts in all four earlier folders. The original folder has no PROOF.md or scripts. Re-derived the round 5 load-bearing identity in h coordinates: with opposite difference signs separated across a diagonal and D=ell on the perpendicular pair, the equality sum changes by +2; a separated same-sign saddle changes it by -2. Hence the pair-weight factor c^(+/-2) is cancelled precisely by changing the closed-saddle probability q=c^(-2). The sign-fiber argument is valid because H and |D-ell| determine the pair once a sign is chosen on each component. This independently confirms the main finite theorem, including c=1 by q=1 with no geometric distribution.

Ran the unchanged round 5 script, read-only with bytecode disabled:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T063/check_binary_swaps.py
```

All tests passed: 5,184 local admissibility checks; local changes {-2:32, 0:2360, 2:32}; 4,976 exact mass checks; 10,368 level covariance checks; 37,452 domain states; 32,184 sign fibers; 51,660 swap images. Peak RSS 49,430,528 bytes, elapsed 2.706 seconds, effective nice 20. The launcher's priority warning is inherited nice 20, not elevated compute. The earlier result holds.

## Choice of one extension (before doing it)

Audit the all-level local reconstruction and its entropy consequence (Pei Lemmas 4.4–4.5), the next step named by round 5. Keep geometric residuals explicit. Prove the deterministic reconstruction for the actual infinite-cluster band index, and verify it with independent finite wired component tests. Also test whether the boundary cost can be slightly sharpened: replace the paper's clipping threshold M+2+2 diam by M+diam+1, and count boundary labels using a spanning tree, giving at most 2*3^(b-1)*(2(M+diam+1)+1) possibilities. The entropy consequence is a finite-box estimate only; no infinite-volume uniqueness or GFF assertion will be inferred.

## First all-level computation and a decoder correction

Created check_fold.py with finite wired minus components defined independently by reachability at every band level, the height fold, explicit residual shifts, and separate forward and reverse decoders. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_fold.py
```

The exhaustive 2x2 cases passed (41,472), but the first larger-domain run failed the reverse decoder's completeness assertion. The implementation incorrectly stopped at the largest boundary band. Interior bands can exceed every boundary band (a finite height mountain). This is a script error, not an error in Pei's induction, which has no such stopping rule. Corrected the reverse stopping bound to max(boundary k)+diameter, using NN Lipschitz continuity; corrected the forward stopping bound to max(max(boundary k), floor(max D/M)), above which every face is minus and connected to a seed. This missing case is explicitly included in the proof and will be retained as a regression fixture.

## Corrected all-level run and proof

Reran the command above with `python3 -u check_fold.py`. Output:

```text
OMP_NUM_THREADS=1; effective_nice=20
exhaustive 2x2 cases=41472 PASS
wired 3x3: profiles=82 cases=1800 PASS
wired 4x3: profiles=374 cases=1800 PASS
wired 3x4: profiles=374 cases=1800 PASS
counts={'cases': 46872, 'constant': 33921, 'large_residual': 6, 'nonconstant': 12951, 'quotient_shift': 5400, 'residual_delta_-1': 397, 'residual_delta_0': 138859, 'residual_delta_1': 1288, 'saturated_minus': 448, 'saturated_plus': 548}
peak_RSS_bytes=16056320; elapsed_seconds=3.747
```

Wrote PROOF.md with all-level graph definitions and a proof of their nestedness; derivation of the band index and every local band transition; admissibility and invariant residual exponents; both parities of the image graph correspondence; both reconstruction directions, including saturated data; and the countable-alphabet entropy chain rule under explicit finite first-moment assumptions. The boundary cost is `(b-1)log 3+log 2+log(2M+2 diameter+3)`. This follows from the smaller clipping threshold L=M+diameter+1 and a rooted boundary spanning tree. It is an absolute free-energy difference bound, so it also implies the one-sided estimate in Pei's Lemma 4.5.

Independent arithmetic checks so far: the exhaustive count is 2 band widths * 6² profile pairs * 9 offsets * 2⁴ boundary choices * 2² residual choices = 41,472; the larger tests add 3*1,800=5,400. The residual update (A'-A)/2 agrees with exact invariance of 2n-A at every diagonal, independently confirming all c_v>1 simultaneously. The refined clipping argument uses |D'(b0)|≤M+diameter whenever bands change; a saturated value has constant bands and all image differences beyond the inner clipping interval. No claim about existence or frequency of I^-=Z has been made.

## Independent entropy check, regression fixtures and final run

Added the explicit 3x3 interior mountain to the script: h1=(0,-1,0,-1,-2,-1,0,-1,0), h2=-h1, M=2, n_d=7, all boundary seed thresholds zero. Direct wired reachability gives boundary band 0 and centre band 1; both decoders must recover it. Added nine restrictions of actual infinite affine-height configurations h1=-x+y, h2=x+y+2 offset, with M=2,3,4 and offsets -5,0,5. Their infinite minus sets are half-planes, so their band labels can be computed a second way as floor((x+offset)/M); the finite wired construction agrees exactly.

Added a finite distribution test: collect 11,520 generated states (with multiplicities), calculate FE(X) and FE(Y) directly, and independently compute the difference of conditional entropies from joint counters. Exact rational c=3/2 weights agree for every record; the entropy values use floating-point logarithms only to test the analytically proved identity. Joint support maps are checked in both directions. Command is the same, with `python3 -u`.

```text
OMP_NUM_THREADS=1; effective_nice=20
exhaustive 2x2 cases=41472 PASS
entropy: records=11520 X=576 Y=880 XB=1168 YB=1168 FE_difference=0.128141507453 chain_difference=0.128141507453 bound=log(594) PASS
wired 3x3: profiles=82 cases=1800 PASS
wired 4x3: profiles=374 cases=1800 PASS
wired 3x4: profiles=374 cases=1800 PASS
regression: boundary bands all 0, centre band 1, both decoders PASS
infinite affine-height restrictions: 9 half-plane-band fixtures PASS
counts={'cases': 46882, 'constant': 33921, 'interior_above_boundary': 32, 'large_residual': 7, 'nonconstant': 12961, 'quotient_shift': 5400, 'residual_delta_-1': 397, 'residual_delta_0': 139155, 'residual_delta_1': 1288, 'saturated_minus': 448, 'saturated_plus': 548}
peak_RSS_bytes=27492352; elapsed_seconds=3.058
```

Second count derivations: 41,472+5,400+1+9=46,882 cases; 33,921+12,961=46,882 constant/nonconstant cases; 448+548=996 saturated cases of both signs. There are 41,472*2+1,800*(8+12+12)+8+9*32=140,840 internal diagonal updates, agreeing with 397+139,155+1,288=140,840. The entropy records number 6²*5*16*4=11,520; their X support has 6²*4 residue classes*4 residual assignments=576 elements. For the 2x2 entropy box b=4, M=2, diameter=2, the bound is 2*3^3*(2*(2+2+1)+1)=594. Direct FE and conditional-entropy calculations agree within the script's 1e-11 tolerance, and print the same 0.128141507453.

Attempts to break the proof covered negative bands, both parities, large offsets, both saturation signs, closed saddles with n=1 becoming n'=0, monotone diagonals becoming saddles with n'=n+1, residuals larger than one, interior bands exceeding the whole boundary, finite mountains, and genuine infinite half-plane examples. The script checks the exact invariant exponent rather than fitting a variance or truncating a geometric distribution. Proof assumptions were checked separately: M>=2 is used to exclude diagonal band jumps of two and in bridge inversion; c_v>1 is needed for a normalizable geometric residual law; finite residual means make the entropy manipulations finite; I^-=Z is an explicit input, not an established property of a six-vertex state.

The corrected tests all pass. The only mathematical-looking failure was the decoder stopping rule, now corrected and covered by the mountain regression. The nice launcher still warns because inherited effective nice is 20. No external writes, git, subagents or publication were used.

## Final deliverable audit

Saved REPORT.md with the required first-line PROVED verdict restricted to local reconstruction and the perimeter free-energy bound. Read-only final audit used the same single-thread/nice environment with a short standard-library Python command: parsed the script with ast, checked all four deliverables, checked the refined constants and the independent total-count arithmetic, and checked that no SOLVED_ELSEWHERE.md was created. Output: `PASS: script syntax, deliverables, refined constant, count audits and limited theorem scope`; effective nice 20. The next handoff is pressure normalization and the residual-independence/Gibbs steps (Pei 4.6–4.9), not an assertion that uniqueness follows already.

Completed approximately 10:33 Asia/Tbilisi, 15 November 2026. All durable results remain in this folder for the coordinator.
