# T132 round 5 verification log

Started 2026-11-15T07:32:39.410478+04:00.

1. Read prior reports, logs and proof files (initial combined output truncated; remaining reads follow). Current folder initially contained codex.log, PROMPT.md and run.pid. Folder-only rule overrides global mesh/checklist/brain writes; none invoked. Brain recall was attempted as startup orientation; it invoked an ONNX runtime, so no further semantic recall is planned. Compute state warn, owner_away_open, CPU saturated. Local work remains tiny and single-threaded. Commands request OMP_NUM_THREADS=1 nice -n 15; inherited priority is 20, already lower scheduling priority than requested. No git or external mutations.

2. Initial web search (exact metric title + error/correction/November; OpenAI planar maps metric refutation; tree-weighted planar maps metric November) and opened arXiv 2610.10501, 2610.10505 and metric-paper community page. No later solution or primary error report found; community page still says No notes yet. Initial sweep completed within five minutes. Read-only GitHub fetch re-opened certificates.tex. Copied round-4 sources and VERIFY.md into this folder as inherited material, and its proof to PRIOR_PROOF.md. Earlier folders remain read-only.

3. Read round-3 proof and audit script and round-4 audit script, PROOF.md and selected certificate reconstruction sections. Fresh read-only GitHub certificates.tex fetch agrees modulo trailing newline (exact comparison follows). Choice: audit the interior-only lifting used in nonzero_local_cost. It is the next unverified geometric step named by round 4, and unlike the entire locality construction it may admit a direct deterministic localization argument. First independently recheck the round-4 tail estimate; then prove or find an obstruction to this single lifting step.

4. Independent re-derivation of round-4 moment claim: write S^k=P+Q with pure P=sum_iY_i^k and mixed Q. Independence and u=k/(k-1) imply ||Q||_u <= m^(k-kp), while E P <= m^(1-kp). Holder plus Markov yields E[X^k;X>R] <= m^(1-kp)+m^(k-kp)/R. Balancing m^(k-1)=R and rounding downward dyadically gives theta=(kp-1)/(k-1), C=1+2^(kp-1), exactly the earlier result. The higher-moment tail integration is also valid. This recheck holds conditional on the stated retained independent interval structure; it does not validate geometry. Fresh certificates source differs only by apply_patch-added terminal newline; removed that newline, now byte-for-byte equal to inherited source.

5. Reopened background.tex and all three theorem-bearing introductions through read-only GitHub fetch. All agree byte-for-byte with inherited sources after removing the one added final newline. Read background.tex cell-interior preimage argument (lines 187–211) and the full reconstruction proof (certificates.tex lines 412–618), nonzero_local_cost (1298–1362), certificate definitions/approximation and bootstrap maximizing zoom. A direct alternative for the interior-only clause uses raw time ranges and the exact sewing witness intervals; it does not require reconstructing field-local chart kernels. Writing this deterministic localization implication with explicit assumptions, then testing its indispensable hypotheses.

6. Wrote PROOF.md: deterministic localization from full raw ranges, a positive spatial/time margin, and exact axial-walk witnesses; area-parametrization derivation of the no-outside-preimage property; conditional nonzero-local-cost deduction with remaining joining/modulus/zero-cost inputs explicit. Found and repaired a document-generation escaping error in inline mathematics before validation; source TeX was unaffected. Identified two necessary geometric hypotheses and a one-step vertical-edge boundary case to test.

7. Wrote provisional REPORT.md and bounded standard-library audit.py. The script independently implements exact first-coordinate minimum equivalence/stack unions and second-coordinate minimum matches/stack pairing, enumerates every axial walk through length seven and every subinterval, checks the terminal-step boundary case, and rechecks earlier tail exponents and theorem quotations. Proof construction was audited against arbitrarily many crossings, exact witness footprints, missing outside fibers, and boundary compacts. No stronger chart realization or uniform spatial construction is assumed implicitly.

8. First audit run completed all mathematical/source checks: 21,844 walks, 730,604 subintervals, 3,779,478 first-coordinate pairs, 99,204 internal vertical-match occurrences; 40 rational moment-exponent cases; four exact theorem quotations; five unchanged source hashes. Exit 1 came from Markdown-link validation against the then-malformed proof, not a mathematical assertion. Rewrote PROOF.md with literal TeX strings, fixing inline escape and link corruption. Reopened lean/docs/211.md and ComparatorChallenges/FKCRT.lean; q>4/CRT scope unchanged. Preserved the round-3 normalization proof as PRIOR_PROOF.md and round-4 moment proof as ROUND4_PROOF.md; adjusted historical proof links.

9. Appended the round-5 verification record, exact sources reopened, independent moment recheck, interior-lifting Spot check, limits and three-sentence recommendation to VERIFY.md. The original main-theorem statements and parameter/model comparisons remain intact. Reopened arXiv abstract pages to confirm author names and only-v1 histories; the community page is updated 14 November and still has no contributed notes. Re-ran audit.py after repairing document generation; result pending. Report verdict narrowed explicitly to actual sewing-path approximants, not arbitrary chart outputs or changing-law continuum realization.

10. Second audit run passed with exit 0. Command: OMP_NUM_THREADS=1 nice -n 15 python3 audit.py. Output:

```text
OMP_NUM_THREADS=1; process priority=20
Exhaustive axial walks of lengths 1..7: 21844
All subintervals including singleton intervals: 730604
First-coordinate equivalence pairs checked: 3779478
Internal vertical match occurrences checked: 99204
Boundary trap: representatives 0,2 are internal but step ending at 3 is outside
Earlier tail estimate: exact rational exponent/rounding checks in 40 cases
All four exact main theorem quotations agree with freshly opened TeX
SHA256 bc4826b62aa9fc383aca319c28db03dc4ba66f6d367500ae483afde684be84b4 metric-introduction.tex
SHA256 3b11009a3415f83309b45d312d0c90b1d905809900c6d697998cf699119131c6 critical-introduction.tex
SHA256 f3037597fa46851ad0f91719599d16aabc0cccaab23df66a0244a4be7d491714 clock-introduction.tex
SHA256 e9753ad862702d3837afdc911466e4ef68d38c1bb471de968d7060b1a4898938 background.tex
SHA256 f856fa05b811f2a6fce12e420c337553d5c32ceaa4c417e5454fc1fe11751167 certificates.tex
Peak resident memory bytes: 19038208
Elapsed seconds: 3.378
All checks passed; continuum construction and upper-certificate closure are not verified.
```

11. Final scope audit: the new deterministic implication concerns actual path approximants, with full raw representative ranges. Neither arbitrary chart realization nor field-local kernel construction is certified. The nonzero-local-cost consequence explicitly retains its joining, joint modulus and zero-local-cost inputs. The source boundary-edge trap is handled by its positive-margin hypothesis and is not a counterexample to the preprint. The latest recommendation has three sentences, names the metric preprint and date, and retains PARTIAL-CLAIMED for the row. No solved-elsewhere conclusion, full proof verification, positive-q exponent or uniform-vertex measure result is asserted. All new artifacts are inside this folder; prior folders are read-only. No git, posting, accounts, messages, subagents, GPU, torch or heavy computation was used; startup semantic recall was attempted once as recorded above.

Task: “Verify: has open problem T132 been settled by the OpenAI math release?” — first recorded local time 15 November 2026, 07:32 Asia/Tbilisi.

12. Final bounded document check passed: required verdict prefix, seven deliverable files, no stray control characters, all local Markdown links resolved, latest replacement exactly three sentences. Mathematical checks were not rerun after the successful audit because only report/verification prose changed.
