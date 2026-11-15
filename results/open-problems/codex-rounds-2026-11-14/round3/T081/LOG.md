# T081 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded session clock: 15 Nov 2026, 01:18:37 Asia/Tbilisi.

## 1. Orientation

Read the earlier REPORT.md, PROOF.md, LOG.md, and complete check_averaging.py from `~/codex_op_1114/briefs/T081`; those files remain unchanged. Consulted startup memory and brain navigation read-only. The present folder-only instruction excludes writing mesh, checklist, recall logs, and brain memories outside this folder. No git, subagents, or external publication.

The compute governor reports `warn`, `owner_away_open`, CPU saturation. Only tiny single-thread standard-library checks are planned, under `nice -n 15`, with time and memory limits. The earlier checker writes beside itself, so it must not be run in its original directory.

## 2. Bounded literature check

Started immediately after reading the earlier report. Searched the web for `"liquid vapor" "translation invariant" "2026" pair potential`, `"hexagonmath" "2610.00734"`, and `"2510.24825" liquid vapor`. Opened arXiv 2510.24825 abstract and HTML, Hexagon landing page and full manuscript, and the atlas page for the earlier radial temperature-singularity claim. The latter does not target finite-range density coexistence.

Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled still use the fixed boxed interaction: https://arxiv.org/html/2510.24825v1 . The recent claim requiring attention remains the Hexagon manuscript *Density coexistence for hard spheres with a long-range attractive pair interaction*: https://hexagonmath.org/2610.00734v1 and https://hexagonmath.org/pdf/2610.00734v1 . It is not an arXiv identifier. No verified newer solution has been identified in this bounded check. Next: independently re-derive the earlier obstruction, then audit one explicit lemma in the Hexagon argument, as the earlier report recommends.

The new-result search ended within five minutes of starting; subsequent source reads are the mathematical audit of the already identified claim. System clock during orientation: `2026-11-15 01:18:37 +04` (Asia/Tbilisi).

## 3. Independent check of the earlier result

Created a new checker, `recheck_previous.py`, using uniform midpoint-grid integration rather than the earlier coordinate-cut algorithm. All cube crossings of these configurations occur on grid edges, so the rational grid averages are exact. It imports no earlier code.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 recheck_previous.py > recheck_output.txt`.

Exit 0; effective nice 20; 48 exact excess checks passed (dimensions 2,3; separations 3,9,101; aligned/staggered; q=2,3,5,7). Exact distant-pair histograms passed for n=1,...,12. Peak RSS 14,614,528 bytes. `nice` reported `setpriority: Operation not permitted`; inherited nice 20 is already lower priority than required.

The earlier main claim holds. Independent algebra: the aligned pair weight is a random variable taking 1 and q with probabilities 1/2; the four-particle excess is its variance `(q-1)^2/4`. For n pairs, `F=-nj+log(2)/beta-log(1+exp(-n*beta*j))/beta` and mean energy is `-nj/2`; division by 2n gives `-j/4`. The opposite shift gives negative excess, as before. The averaged tent formula and stability derivations were also checked algebraically against the earlier proof; no error found.

## 4. Choice before the extension

Chosen piece: audit the exact contour replacement in Section 5.2 of the Hexagon manuscript, specifically the interior phase appearing in its equation (5.3). This is the first step the earlier report recommends, and it precedes any microscopic-background cluster expansion. A concrete test is a three-by-three (or three-by-three-by-three) dense block in an empty exterior. Its incorrect-cell shell has dilute exterior type but a dense bounded interior. Determine whether the stated numerator counts this positive-measure physical sector, and check the formula directly in the PDF rather than relying on text extraction.

Initial observation, to be tested: (5.3) uses `Z_{D_j}^c` in both numerator and denominator, whereas the physical interior collar has phase `c_j`, which may differ from exterior type c. The later cancellation argument uses `c_j` in its numerator. No conclusion about a corrected manuscript is drawn from this observation.

### Extraction error rejected by checking source

The apparent interior-phase inconsistency is **not present in the TeX source**. PDF text extraction dropped the subscript j: the source numerator is `Z_{D_j}^{c_j}`, and the denominator is `Z_{D_j}^{c}`. The same extraction also lost the integer floor in the fine-cell definition and altered a numerator/denominator word later in the proof. Therefore the proposed droplet contradiction is rejected, not a result. This is why source verification matters here.

Opened the actual source through the manuscript landing page → Browse source files → `liquid-solid.tex`: https://hexagonmath.org/api/v1/works/2610.00734v1/source?path=liquid-solid.tex . Relevant source lines 482–515 and 770–792 agree on the interior phases. Screenshots through the web tool did not expose usable images; a local download attempt failed DNS resolution (`curl: (6) Could not resolve host`), so no local PDF was obtained. The TeX resolves the ambiguity without screenshots.

Continue the same chosen piece, the exact contour replacement, using the source definitions rather than the faulty extracted formulas. A direct proof or finite-state stress test of the microscopic-background integration is now needed.

### Precise result to establish

The extension remains the audit of Section 5.2. Prove the replacement identity by induction on finite domains, assuming explicit contour geometry (constant collars, separated complementary components, and disjoint-or-nested filled supports). Keep each activity conditional on the microscopic exterior until integration is complete. This will verify the algebraic part of the claimed exact replacement, rather than a phase transition or all its geometric inputs. Stress-test it using a finite-state hierarchy with nested supports, two interiors per support, and boundary-dependent microscopic weights. This is separate from averaging activities independently; shared microscopic states must be retained.

## 5. Proof and exact checks

Wrote PROOF.md with the explicit geometry/locality hypotheses and an induction on finite-domain volume. Regroup auxiliary contour families by maximal filled support, integrate their nested interiors first, recover the physical same-phase interior partition functions in the denominator, then use the conditional equality `W*D=N`. Microscopic background variables shared by different activities are retained. The proof therefore checks the conditional replacement algebra under stated hypotheses; it does not prove the full continuum contour geometry or the claimed coexistence theorem.

Created `check_replacement.py`. It compares physical-state enumeration, recursive conditional ratios, and auxiliary pure-background integration, all with exact rational arithmetic. It includes binary trees with one, three, and seven supports, two phases, two microscopic states, two exteriors, and strictly positive boundary-dependent weights. In selected cases the compatible-family subset sum is explicitly enumerated separately. A geometric check independently computes incorrect cells for dense cube blocks in dimensions 2 and 3 and flood-fills their bounded complementary component.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_replacement.py > replacement_output.txt`.

Exit 0; tool wall time about 0.60 seconds. Output and exact rational data are in replacement_output.txt and replacement_checks.json. In two hand-checkable shared-boundary examples, the conditional identity gives 160 and 128 respectively, while independently averaging the activities gives 144 in both. The discrepancies +16 and -16 follow independently from covariance +1 or -1, multiplied by baseline mass 8 and root factor 2. This confirms that common-background dependence is preserved, rather than silently factorized.

## 6. Adversarial audit

Checked the maximal-family regrouping carefully: activities of maximal contours depend only on retained exterior variables, their filled supports do not interact directly, and inner auxiliary families belong precisely to the bounded-component catalogs. The bijection of compatible families and the unique physical external-contour decomposition are explicit hypotheses. The conditional theorem does not claim these properties for every conceivable contour definition.

Added two deliberately incorrect operations to the checker and proof. In the aligned three-support example the true denominator is 80; replacing it by the pure-background denominator 8 produces 880 instead of 160. Forbidding root/leaf nesting produces 88 instead of 160. The script asserts both failures. Re-ran the same command after these changes; exit 0. These checks supplement the positive and negative covariance tests and prevent a hidden omission of nested families.

All 44 rational comparisons passed. The geometric shell counts agree by two methods (local correctness enumeration and cube-volume subtraction): dimensions 2 and 3 give 24 and 124 support cells for radius-one dense blocks, and 56 and 604 for radius-three blocks. Flood-fill independently finds interiors of sizes 1,1,25,125 respectively. In the larger blocks, a nested support has its entire one-cell enlargement inside the bounded component and is nonadjacent to the outer support. This checks examples, not the general geometry theorem.

The full output is preserved in replacement_output.txt. First run peak RSS: 17,088,512 bytes; runtime reported by the script: 0.697 seconds. The small rerun remains far below the resource limits. No failed exact checks occurred. The apparent PDF inconsistency failed source verification and was discarded. No coexistence result or general contour-geometry proof is claimed.

## 7. Final artifact audit

Wrote REPORT.md with the required first-line PARTIAL verdict, the new conditional result, commands, failed hypotheses, limitations, and next step. Read the saved data independently, checked all 44 comparisons and both covariance examples, checked the four shell/interior counts, parsed both scripts with `ast.parse`, verified every required deliverable is nonempty, and checked that no SOLVED_ELSEWHERE.md was created. The final check ran through `OMP_NUM_THREADS=1 nice -n 15 python3` with an inline read-only Python body; its output is in artifact_audit.txt.

Audit passed. Final checker run: 0.636 seconds and 17,252,352 bytes peak RSS (exact values retained in JSON). Files in the earlier worker's directory were only read. All new artifacts are in this folder; no git, external state changes, background workers, or subagents were used.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 Nov 2026, 01:18:37 Asia/Tbilisi (first recorded session clock).
