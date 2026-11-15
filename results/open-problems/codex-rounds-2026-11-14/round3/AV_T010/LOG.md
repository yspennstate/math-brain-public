# T010 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.” Session began 2026-11-15 00:50 Asia/Tbilisi (2026-11-14 20:50 UTC).

## 1. Orientation and earlier work

Read the previous folder's REPORT.md, LOG.md, and VERIFY.md with `OMP_NUM_THREADS=1 nice -n 15 python3` using pathlib. PROOF.md and Python scripts are absent. Earlier result is a scope verdict: the planar preprint claims pure-point spectrum for uniform potentials, expressly without claiming exponential eigenfunction decay; the local analytic-lemma spot check was conditional on earlier screening/thinning inputs.

Read compute_state.json: warn, owner_away_open, CPU saturated. Only small text reads and symbolic reasoning are planned. The nice wrapper reports `setpriority: Operation not permitted`, but Python `os.getpriority(os.PRIO_PROCESS,0)` independently reports effective niceness 20, stricter than the requested 15. Every shell program uses OMP_NUM_THREADS=1 and nice -n 15. No numerical workloads, git, subagents, or external writes. The folder-only restriction precludes mesh/checklist/brain operations that write outside this folder; orientation used read-only files.

## 2. Five-minute update search begun

Web search queries: exact planar title; `"openai/math" "Anderson" error`; `two dimensional Anderson localization all disorder 2026 proof`. Results include the same manuscript and secondary catalogs, but no newly identified solution or specific refutation. Search snippets are leads only. Next: open the current primary sources and check the claim independently.

## 3. Update search closed; independent recheck

Within five minutes, searched the planar title with `arxiv refutation correction November 2026`, `"Anderson" "OpenAI" "gap" "2026"`, and `"two-dimensional" "Anderson" "localization" "November" "2026" proof`. Opened current raw introduction.tex, README.md, repository history.md, and lean/docs/261.md. The introduction's actual model, theorem, and scope paragraph independently confirm the earlier verdict: iid uniforms on [-h,h], every fixed h>0, pure-point type, no asserted exponential eigenfunction decay. The Lean documentation expressly excludes pure-point type from its target. History still ends October 29 and lists no Anderson withdrawal; this is not proof of absence of errors.

Opened arXiv:2609.24426: Xujie Lai and Fan Yang, v4 remains dated November 8, 2026, already covered earlier. Opened arXiv:2611.03286: Habib Ammari, Xin Fu, Wenjia Jing, Jiayu Qiu, Alexander Uhlmann, “Anderson localisation in infinite and finite resonator crystals with long-range interactions,” November 2, 2026. Its abstract concerns random capacitance operators with exponentially decaying interactions and spectral-edge localization; it does not solve our nearest-neighbor, all-energy, arbitrary-law problem. No solved-elsewhere finding or new specific refutation was found in this bounded search. No SOLVED_ELSEWHERE.md is warranted.

## 4. One extension selected

Choice: check the bounded-twist law change and the claim that recomputing the potential-dependent hierarchy leaves retained ports unchanged, in vanishing.tex lines 612–682. The earlier spot check explicitly left hierarchy-status invariance unverified; this is the input needed to transport the small-trace estimate under the analytic closure. First verify the density bound independently, then compare every retained-status dependency against hierarchy.tex. A conditional density estimate alone will not be reported as verification of the full vanishing proposition.

Opened vanishing.tex at lines 420 and 610. Its law change has T_s(v)=v+s theta(v), changes O(M_0^2 R^2) sites with s=O(1/R), and proposes an L2 density bound independent of R. It excludes invalid large-ancestor labels both before and after the change. The possible weak point is whether validity gates exhaust all ancestor dependence; this will be checked against the actual rules.

## 5. Dependency check and independent density calculation

Opened hierarchy.tex lines 0–205 and 221–355, vanishing.tex geometry (27–67), annular probes (236–263), and law change (612–698), plus matrix.tex. The acceptance formula has selector eligibility, valid own/ancestor labels, and a local likelihood; the likelihood explicitly uses no other ancestor data. The open port's strength and reference are local to its tile. Stage n uses accepted roots at levels at least n, with true potentials restored at removed roots. These definitions support the claimed locality, including changes in accepted cells that have already been removed in the gap.

Independent density derivation: put a=s theta'(x), with |a|<=1/2. A change of variables gives integral r_s^2 dmu = integral 1/(1+a) dmu. The exact identity 1/(1+a)=1-a+a^2/(1+a), and integral theta'=0 from the endpoint values, give integral r_s^2 <=1+2s^2 integral (theta')^2. This obtains the quadratic cost directly, without merely asserting cancellation of an O(s) bound. A second derivation uses integral(r_s-1)^2 and the same substitution, obtaining exactly the same integral of a^2/(1+a). Tensorization gives exp(2J N_C s^2), J=integral(theta')^2, not exp(O(N_C |s|)).

Rechecked geometric scales: R=L_*/M_0^2, L_* between exp(b_m^2) and 3exp(b_m^2), tau=C_0/R. Thus b_m/R tends to zero and N_C s^2 is bounded for |s|<=W tau. A changed ancestor of a retained tile must span a gap of order R. At each level its number is bounded by C_M0(1+R/b_l)^2. The small-box probability yields a geometric tail in b_l=3^l, hence O_M0(R^(-K_0)) before the shift and O_W(R^(-K_0/2)) after Cauchy–Schwarz. No independence of these ancestor events is used.

## 6. Deliverables saved

Wrote PROOF.md with the full bounded-twist lemma, the exact second-moment identity, product density, annular geometry, all candidate-acceptance dependencies, small-box and ancestor counting, closure sign, and the resulting trace probability bound. This is a local verification with the input expectation left explicit, not a correctness judgment on the whole manuscript. Chose REPORT.md verdict PARTIAL to avoid confusing this result with a solution of T010.

Reopened the actual entry TeX and introduction of all three candidates. Authors are OpenAI; dates are September 23, September 23, and October 5, 2026. Copied main theorem bodies into the new VERIFY.md. It includes the independent scope comparison, current-source record, a three-sentence replacement status, and the new spot check. This session did not reopen every secondary source the earlier worker read; VERIFY.md distinguishes inherited context from current opens.

Next proposed check: whether the sign of the adaptive first variation remains measurable without inspecting each still-hidden root draw throughout the complementary pass. That is outside the single chosen bounded-twist check and is left for the next worker.

## 7. Independent audit and completion

Ran `OMP_NUM_THREADS=1 nice -n 15 python3` to read back all four deliverables, compare the three exact theorem blocks against the earlier record, inspect report format, and count TeX delimiters. All three theorem blocks match the earlier opened-source transcription byte for byte; they also agree with this session's current raw-source views. Code fences and displayed-math delimiters balance. Effective niceness again measured 20. Audit clock: 2026-11-15 00:56 Asia/Tbilisi.

Re-derived the closure phase sign from z/(1-z) and the Woodbury denominator; checked the support endpoints, both signs of s, torus boundaries, random geometric conditioning, absence of additional probes after closure, and both creation and destruction of retained candidates. The single-site quadratic cost and geometric-series exponent were each obtained two ways. Corrected a transpose typesetting typo and made positivity of C_0 and K explicit. No local mathematical error was found; the proof's input expectation and earlier screening/good-event assertions remain explicitly unproved. No computation script was needed because the extension is a finite symbolic argument.

Finished REPORT.md, VERIFY.md, PROOF.md, and this log, all inside the authorized folder. The full row is still not claimed by the identified theorem. No solved-elsewhere file was created because no such result was found.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15 00:50 Asia/Tbilisi.
