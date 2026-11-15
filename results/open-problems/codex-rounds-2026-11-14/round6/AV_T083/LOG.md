# T083 continuation, round 6

Task: “Verify: has open problem T083 been settled by the OpenAI math release?” First clock: 15 November 2026, 09:46:55 +04; exact receipt time unavailable.

## 1. Orientation and earlier work
Read the startup memory index and compute state read-only. Compute state: ok, owner_away_open. All writes are restricted to this folder, so no external brain, mesh or checklist mutations, git, subagents or publishing. The `nice -n 15` launcher warns that priority cannot be changed; inherited nice=20 is independently confirmed by the earlier check script. Only small single-thread standard-library calculations are planned.

Read round-3, round-4 and round-5 REPORT.md, LOG.md and PROOF.md and the round-4 and round-5 scripts. The initial combined display was truncated; focused subsequent reads recovered the relevant proofs and scripts. Earlier results are conditional analytic reductions and finite row estimates, not T083.

## 2. Bounded literature refresh
Web searches included exact title, pointwise/triple/ergodic/2026, and OpenAI/mixing/error/correction variants. Opened the release history, arXiv:2608.27321, Christoph Thiele’s papers page and the OpenVerification front page. No later settlement of the arbitrary-system, all-k statement was found. The history still ends October 29; an uppercase HISTORY.md URL returned 404 before the correct lowercase history.md was opened. The arXiv paper concerns norm-variation; the papers page lists a pointwise theorem for two commuting transformations. The review search result raises multiple-mixing concerns; its JavaScript front page exposes no detailed case to verify, so no new refutation is inferred from that snippet. No SOLVED_ELSEWHERE.md is warranted. Literature refresh stopped within five minutes.

## 3. Independent recheck of round 5
Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/AV_T083/check_smooth_rows.py`. Passed 630 exact martingale orthogonality checks, 456 physical and 456 augmented contraction checks, 360 scheduled decompositions, 60 residue square sums, 51 geometric-tail checks, rational constant checks and 2,137 supplementary catalog-size checks. Peak RSS 16,285,696 bytes, elapsed 1.764 seconds, nice=20. No writes to the earlier folder (`-B`).

Independently rederived the essential improvement: residue classes partition output coordinates, so a uniform class bound b combines as sqrt(h+1)b, not (h+1)b. With weights 2^-h, Cauchy–Schwarz gives tail <=sqrt(h0+3)2^-h0. Multiplying the catalog logarithm by sqrt(h0+1) gives logarithmic exponent 3/2. Bounds h0+1<=11l, h0+3<=12l, l=log2(2d)>=2, and sqrt(d)2^-h0<=2^-19 give coefficient <(40/3)(21/2)=140. The round-5 result holds under its explicitly stated selected-array Bessel and fixed-carrier hypotheses.

## 4. ONE extension selected before starting it
Audit the assertion in candidate3-base.tex lines 553–569 that manuscript H supplies an ordinary joint Bessel bound for the selected fixed complete-carrier array with polynomial complexity. This is the next step explicitly named by round 5. Read the matching “A scale sum for one separated term” construction and its frequency-clump estimate, rather than assuming that the word Bessel supplies the needed hypotheses. Catalog size and fixed-carrier assertions will be tracked as parts of this one application audit.

## 5. Source construction opened and saved
Read-only GitHub fetch opened manuscript H’s directory, build/sections/base.tex, charts.tex and compression.tex. Saved these as sources/H-base.tex, H-charts.tex and H-compression.tex. H is OpenAI, “An L^3 bound for the trilinear Hilbert transform” (October 5, 2026); its main header was read in round 4’s saved source.

H-base.tex lines 171–209 constructs tensor mean-zero rows, asserts a joint Bessel norm, and sketches a demodulated-shell proof. Its two ingredients are per-scale center separation and a scale-count bound from “Height bins” (H-compression.tex lines 555–678). The argument is potentially sufficient: all centers are bounded-height rational evaluations of one fixed parameter vector, so adjoining the tested Fourier frequency still gives only polynomially many occupied scale ranges. H-charts.tex states the required fixed-parameter dependence and finite truncation. Those chart/Weyl/tail statements themselves are not yet verified.

Next write out the shell proof with explicit constants, prove the needed height-bin count directly, and audit the fixed-carrier/catalog transfer. The target is the ordinary selected-array Bessel premise, not the full separated-scale lemma.

## 6. Current source continuity and proof outline
Fetched and saved the three original introduction files, candidate1-inputs.tex, candidate3-base.tex and H’s main TeX using read-only GitHub calls. All five candidate files match round 5 unchanged (ignoring final newline). H’s title, author OpenAI and October 5, 2026 date are confirmed from its main file.

The Bessel statement can be derived with explicit squared bound 676 A^2 S, where A controls the bump and its first two scaled derivatives and S=p(ceil(log2(4p p! B^(p^2+p))))+2p for p=d+1. Centers are bounded-height evaluations of d fixed real parameters and separated by at least 1/r at scale r. A fixed arbitrary bounded multiplier is absorbed into the input. The proof will establish this statement, not the unverified scalar construction that produces its centers. The catalog has at most (3B^2)^d distinct frequencies.

## 7. Bessel proof saved
Wrote PROOF.md. Direct rational-dependence minors give at most p occupied magnitude ranges of ratio R_p=4p p! B^(p^2+p), hence S_p=p(ceil(log2 R_p)+2) possible scales per shell. At each such scale, separation gives at most 2(1+2^ell) centers. Low shells have norm <=4 pi A 2^ell by exact mean zero and local Poincaré; high shells have norm <=A/(4 pi^2) 2^(-2ell) by two antiderivatives. The summed norm is <26 A sqrt(S_p), so squared Bessel norm <=676 A^2 S_p. Catalog size <=(3B^2)^d.

All source-to-lemma hypotheses are made explicit: fixed parameters and multiplier; global center separation at each retained scale; exactly one row per interval-center pair; interior smooth tensors; and bounded rational coefficient height after the slope factor is absorbed. The argument checks the Bessel and catalog transfer conditional on those scalar premises. It does not verify the chart/Weyl/pooled-tail construction itself. Next: exact finite arithmetic and cancellation edge cases, then an adversarial audit of these hypotheses.

## 8. Independent arithmetic and edge-case checks
Added check_bessel.py (standard library, one thread, CPU limit 60 seconds, no writes). Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_bessel.py`. Passed: 26 exact height-range checks, 24 direct enumerations of all occupied scales, 243 globally separated center selections, 338 shell multiplicity checks, 15 exact polynomial bump/Poincaré/double-antiderivative checks, 128 exact finite geometric sums with remainders, rational constants 26 and 676, and 75 supplementary budget comparisons. Maximum 14 occupied bins and 4 greedy ranges occurred. Tests include zero vectors, exact center hits, negative parameters, frequencies 2^40 and nonzero cancellations below 2^-50. Five fresh source comparisons passed. Peak RSS 17,104,896 bytes, elapsed 0.878 seconds, nice=20.

The finite tests supplement the all-parameter proof; they do not establish the chart or ergodic theorem. Next audit all source hypotheses against the actual application, and add a failure example outside the fixed-multiplier hypothesis so its role is explicit.

## 9. Adversarial audit and provisional report
Checked the source uses global clumps at each scale (Q is fixed), not independent per-interval center sets. The slope factor is at most 3 and can be included in the height bound; epsilon<=1/3 supplies separation >=1/r. The complete multiplier is fixed on the common birth root. Its roughness costs nothing, because it is absorbed into one input before Fourier projection. Smoothness through order two is available for the tensor bumps, even though round 5’s abstract estimate required only one derivative.

Added a negative control outside the theorem’s hypotheses: for the same mean-zero C2 bump at each interval, allowing psi_I=sign(omega_I) gives squared output h*c^2 at h complete depths on f=1. Exact integration gives c=1/2048, independently rederived from w=-(t^4(1-t)^4)'/8. This proves the fixed-multiplier condition cannot simply be dropped; it is not a counterexample to the source. Saved REPORT.md with a narrowly scoped PROVED verdict.

Reopened OSVerify’s actual H report: it lists the same endpoint, augmented predictor and role-order concerns, with proposed repairs, not a refutation. Current lean/formalization.yaml has no ergodic/pointwise/slopes entry; its only mixing hits concern unrelated declarations. The docs listing has 245 entries and no 154.md. Reopened the actual Lean README and docs/145.md through the connector after the web renderer returned mainly navigation; 145 concerns multiple mixing. Saved the catalogue and parsed doc names, not the large raw directory listing. No Lean compilation.

## 10. Final verification and handoff
Wrote VERIFY.md with all three exact main-theorem environments, the wider internal triple lemma, the model/range/quantity/strength comparison, sources actually opened and a three-sentence recommended status. It distinguishes PARTIAL-CLAIMED for the literature question from REPORT.md’s PROVED verdict for one finite analytic implication.

Final command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_bessel.py`. Output: height-range checks=26; direct scale enumerations=24; global separated-center selections=243; shell multiplicity checks=338; maximum occupied bins=14; maximum greedy ranges=4; exact C2 bump A=1080; 15 cancellation/Poincaré/double-antiderivative checks; variable-multiplier negative control c=1/2048; 128 exact geometric-sum/remainder checks; rational 26 and 676 checks; 75 supplementary budget comparisons; three exact theorem quotation checks; five unchanged-source comparisons. Peak RSS=16,875,520 bytes, elapsed=0.849 seconds, nice=20. No mathematical failure.

The last document audit initially failed because it demanded the literal strings “per-interval” and “common multiplier”, while the proof states those hypotheses in different words. This was an audit-text predicate error, not a missing hypothesis or mathematical failure. Replaced those predicates with the actual statement phrases; the audit then passed verdict scope, exact quotations, the three-sentence recommendation and presence of all 11 saved source artifacts. No mathematical document change was needed for that correction.

Every load-bearing step was checked in writing: integer coefficients in minimal dependence; scale-interval integer count; global center multiplicity; zero-frequency null sets; disjoint intervals for the per-scale norms; correct 2pi factors; compact-support boundary terms; shell norm summability; and fixed multiplier absorption before Fourier projection. Constants 26 and 676 were checked by rational bounds independently of their decimal magnitudes. The negative-control integral was independently checked by a derivative identity. The source’s upstream chart/Weyl/pooled-tail claims and projected-input compression remain open checks.

Next worker: H-compression.tex lines 273 onward (Lemma Compression), compared with candidate3-base.tex lines 584–622 and its required catalog/support hypotheses. This session verifies the raw ordinary Bessel premise from stated scalar hypotheses; it does not close the full separated-scale proof. All new files remain in this folder; earlier folders were read only, and no git, subagents, external state mutations or publishing occurred.

Completed 2026-11-15T09:59:17.545781+04:00. Task: “Verify: has open problem T083 been settled by the OpenAI math release?” First clock 15 November 2026, 09:46:55 +04; exact receipt time unavailable.
