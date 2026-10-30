# Repaired five-singular-value manuscript: change and reconciliation record

The owner requested incorporation of the scheduled audits' corrections and a new round of audits of the repaired manuscript, explicitly including fleet04. This is a repaired audit candidate, not an assertion of formal verification or a newly completed independent fleet audit.

## Exact version

Canonical source: `paper.tex`, first committed at `4e530247ec0ef4101a6e5ecf621bd35a969c42aa` in this directory.

- Git blob: `98e45d53d106db9a205051a4dd4917fc39dc2e3a` (read back from GitHub and matched to the local source).
- SHA-256: `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`.
- 61,567 UTF-8 bytes; 683 actual source lines; 26 proof environments.
- Local reference compilation: 15 pages, 440,790 bytes; PDF SHA-256 `2a493f2dd3dc4eb126d965cc1d246c554f9a5c61bc9a4a9bd8ca0ab9e439cd09`.
- The PDF was compiled locally and supplied in the owner conversation. This record does not assert that a PDF binary has been uploaded to this directory. Compile the canonical source with the supplied build script; PDF bytes can vary with TeX version and timestamp.

Original: `../short/short.tex` at `ec211ba2d77a4a9850168c6af1574ea651feaa7c`, blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, SHA-256 `f4a4f4c6db7f0ad4feffbe04041af3cf1a759fb4cb51f4979b6fd884eba26037`. It has 675 actual source lines; splitting at its terminal newline creates an empty 676th field, not another physical line. The original source, PDF and peer audit artifacts remain unchanged.

## Preserved result and hypotheses

Independent real coordinates with densities at most K; real symmetric A; arbitrary affine terms, dimension, signature, remaining spectrum and rough coordinate laws. If s5(A) >= s > 0, the essential density bound is 270 K^2/s. The three-direction full negative-half-moment bound remains 77 K/sqrt(s). No support, moment, iid or smoothness condition was added. No global continuity or four-/three-direction density theorem is claimed.

## Repairs applied

Old line numbers below refer only to the original source. Auditors must use the new source's lines for new coverage.

1. C04, old L41: qualify random-sign extraction by the no-pivot hypothesis and m in {1,2,3}.
2. C07, old L62: replace the unverified current-open-status claim with the manuscript-local statement that this argument does not settle three or four directions. State essential density bounds and limited continuity explicitly.
3. C05, old L65: describe upper envelopes, not necessary singularities; distinguish the bounded definite-pair case.
4. Define nonnegative singular kernels at zero in the extended sense, including log+(c/|0|), and use capped Borel density versions.
5. State u > 0 explicitly in the half-moment envelope specialization.
6. C06/C10, old L148: replace 'Both' and handle s_j(T)=0, including padded indices, before invoking j nonzero right singular vectors.
7. Old L222: say each zero-beta factor is independent of the fiber variable and bounded by one, so all may be dropped. The cardinality reading that there is at most one zero-beta factor is rejected; this is a clarity repair, not a false projection lemma.
8. C12, old L224: handle p(y)=0 before logarithms and establish finiteness in the positive case.
9. Give the finite-partition total-variation domination argument for the complex pushforward.
10. C02, old L319-322: introduce the measurable conditional integral and explicitly apply |E F|^2 <= E|F|^2.
11. Fleet02/B14-R05, old L319-327: prove measurability of x -> ||nu_x||_2^2 by a fixed sequence of mollifiers BEFORE its expectation and BEFORE the terminal ell'=0 branch. This additional finding was not in the initial central corrections list. The later mollification uses the same density.
12. C08, old L398: give the scalar density formula for z != v, choose p(v)=0, and exclude an atom using P(Y=m)=0.
13. C01, old L412: use an open polar chart onto a slit plane, discard the null seam, use the absolute Jacobian, and explicitly discard the critical point.
14. C03, old L441: exclude the hyperbolic critical level, a union of two affine lines. Preserve the separate original-coordinate choices for the two tails.
15. C09, old L613: define J(d) for all real d as a nonnegative integral, with J(0)=infinity, before evaluating J(R-a).
16. C11, old L505: explicitly set the pair envelope h(0)=infinity.
17. Define the maximum off-diagonal modulus with zero adjoined, including an empty index family.
18. State the density scaling formula almost everywhere.
19. Add exact power comparisons proving C3 < 15 and C2 < 12.2 from e < 11/4.
20. Add the Gamma log-convexity certificate for the concentration coefficient < 19, with an exact rational fourth-power comparison.

The local repair script records 24 literal replacements; some of the twenty grouped items above involve multiple replacements. None changes the theorem's constant.

## Evidence read and disagreements reconciled

The editor read the pinned source and central CORRECTIONS, and retrieved substantive reports, summaries, issue records and repair records from the fleet01, fleet02 and fleet03 audit trees. The inventory snapshot at the start of this revision was brain commit `5705ee22d96c15b48d93208d78de8b7bd4436c6e`. Representative exact evidence blobs, including the later findings that changed the revision:

- fleet01/B01 complete pass 6: `461ab2f85bd288de282242f5924394f1b8cc7870`.
- fleet01/B12 padded-index/scalar-critical review: `e2c3ff7ae73cdbc96b72eb0f15b17bbd9352bb07`.
- fleet01/B07 corrected zero-beta interpretation: `147ba691656fa96e2f06103bab7918e89acea1dc`.
- fleet01/B19 repaired downstream regression: `24e9067385fb2afeeb42377a0bc924bcb5c09367`.
- fleet02/B02 two-pass summary: `cf058140a4dffeae1ce1245169faf7f3c96c0048`.
- fleet02/B03 independence and mollification review: `735cfb32ab639cca96a5439ae70e12bfdefc189f`.
- fleet02/B04 constant certificate and disagreement on Jensen severity: `d7fc3bf3387327892bfa38f66e927c6db09230b2`.
- fleet02/B05 consolidated findings: `3e8a0d36aeea3069e58a5a23ac1996007f0cf10e`.
- fleet02/B06 extended-real-domain issues: `422d6192c6b8c46ca41e2d200d64c30100288d35`.
- fleet02/B07 full source review: `ce296121cfad781f00fffd2f934cd0f1aa1cfbaf`.
- fleet02/B08 repair checks: `36909d843a54405f1bdfc562a2e73b30300b4573`.
- fleet02/B09 consolidated findings and zero-density issue: `2ccc9cc4adfba335aff8c8e425ee044bb22c4dff`, `942b39e55a1cb937cff6217a1e6f8eeb505f9787`.
- fleet02/B10 padded-index/scalar-critical findings: `01ea4d3e592bdafd4ed86ea458da27eeba2f56cf`.
- fleet02/B11 repair and Schur checks: `faf29080b5e48e7ed67d64bf4b9e86e423ce691e`.
- fleet02/B14 additional measurability issue: `dd5fe0049af875377a34093fe96ad1e8762e1005`, `b1b66b9ac79164d5a82e74fc7ceb0feb9df421fe`.
- fleet02/B15 consolidated P12 summary: `a7361701da15d91df885c988741188f1bfa857aa`.
- fleet02/B16 full P11 reconstruction: `d6e6c5e18ebcde6152cb9bb33ce38a287ef495d5`.
- fleet02/B19 issue/reconciliation records: `48153fa56abb1899a7a6e39f0330039d84bcf27b`, `9688f60bb9e1f007fd6eb155f7bff8ba60bfcbd6`.
- fleet02/B20 consolidated issues: `45df2e801300feecaf02179ffaa0f115c0e9df50`.
- fleet03/B05 review: `2e6e39fdd07a81a52787ac2d4fc453398a09b46e`.
- Further fleet03 reports/findings read include `d4869f545ff86e9b7520ce02b147fc3bf376dd34`, `4a23e603b3cdfb5753d6d2dd05afd28ac0a7c32b`, `f0d6eb9aa62738c36eea789133d2915c49adf777`, `df3e59feb071a22d7f71fe3f7dc0de3d1991cb47`, `0f3aa68a065f919eed0c4659224d06e50633519d`, `2b6d230c16204160e59b571d0956cf7c52d64271`, `35f63284bd01d878fa287a6764d7a4bf6e754fdc`, `c16bffb465e57702f5c7fd5137290d10f67cbe5b`, `dfe93aa51fbaf9eed027b2fee60610fe69ddac28`, `762ffe10c885a9dbb12c0702b2101494b96b9e61`, `51d12b72245bbda770a95d3d1e0656f8cc27bd3e`, `d0b63d60578063dd0636ee58046703b205bed023`, `bf256a913265852b665596b53782cfba5e701e87`.

The distinction between a clarity omission and a proof-text GAP differs between reviewers. The revision supplies the explicit justification in either case. The zero-beta cardinality objection is not adopted as a mathematical defect.

Reading limitation: this is not a certified exhaustive reading of every historical report and every large clause-coverage JSONL file across the moving fleet. The new audit order requires workers to reconcile the remaining evidence against this exact new source rather than assume the present ledger is exhaustive. The bibliography was not exhaustively reverified; the unsupported current-open-status assertion was removed instead of endorsed.

## Local checks and review status

Three pdflatex passes succeeded. All 15 rendered pages were inspected in a contact sheet and dense repaired pages were inspected at full size. A small 1.86403pt overfull-box warning remains in a paragraph; no clipping was observed. This is not a claim that every formula received an independent second visual proof audit.

Exact arithmetic checks include positive margins 40788279/1024 (C3), 4302512997281/390625 (C2), 39009533/78125 (concentration), 59/1250 (half-potential branch), 39/200 (scalar density branch), and 4469/16875 (indefinite density branch).

No fresh Lean compilation was performed. Old audits and formal results are evidence to reconcile, not completed audits of this new hash. New independent review coverage starts from zero. Preserve every new objection and do not silently weaken the hypotheses to make a proof pass.
