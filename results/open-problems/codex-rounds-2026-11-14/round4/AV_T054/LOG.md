# T054 continuation log

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” Session date: 15 November 2026, Asia/Tbilisi.

## 1. Orientation and scope

Listed both earlier folders and this folder with `rg --files`; read the local compute state. This folder initially contains PROMPT.md only. The earlier folders contain reports, verification notes, source snapshots and, in round 3, PROOF.md and two audit scripts. Reading those files is the next step. All writes will stay in this folder; no git or external posting. The later task-specific restriction against edits elsewhere prevents running the brain/checklist/mesh commands that persist state outside this folder; orientation is read-only.

Commands use `OMP_NUM_THREADS=1 nice -n 15`; the environment reports `nice: setpriority: Operation not permitted` and continues. Niceness will be checked before any substantive computation. Compute state says `warn`, `owner_away_open`; no heavy computation is planned.

## 2. Earlier work and bounded literature check

Read both REPORT.md and LOG.md files, all of round 3 PROOF.md, audit_permutation.py and audit_sources.py. The first folder has no PROOF.md or scripts. Read the earlier proof's martingale increment identity, multiplicity argument and averaging over label permutations independently: the bound `epsilon + 2N^2 exp(-N s^2/(32 L^8))` follows with the stated all-vectors-in-each-eigenspace hypothesis. The projection identity `Q(i,i)=sup |u_i|^2`, `tr Q=m` gives `m<=L^2`; entry-to-operator conversion multiplies by at most m. Substituting `s=L^4 sqrt(32(D+2)log(N)/N)` gives exactly `2N^(-D)`. No error found. A separate exact computation will recheck this, rather than only rerunning the same script.

Used the web search tool with queries on fixed-degree QUE (2026), the exact GOE title plus errors, and arXiv:2610.08127. Opened the arXiv abstract, Huang–Yau 2102.00963v3 full HTML, current OpenAI history.md and the clean GOE introduction. The bounded check found no later result changing round 3: He–Huang–Wang is still v1 (6 October 2026); repository history still ends 29 October and gives no named correction of these candidates. The clean main theorem has no spatial QUE clause. This is a limited negative search, not a certification that no other work exists. No newly discovered settlement warrants SOLVED_ELSEWHERE.md.

## 3. One chosen extension, before doing it

Prove relative equidistribution on each prescribed deterministic shrinking vertex set S, uniformly over all eigenvectors. The earlier absolute bounded-test result is insufficient when |S|/N tends to zero. Reveal only the |S| sampled labels and concentrate the compressed eigenspace matrices by a finite-sampling martingale. Target: failure at most `epsilon + 2N^2 exp(-k r^2/(8 L^8))` for relative error r on a set of size k (and a refinement using min(k,N-k)). Thus sets with `k/(L^8 log N)` tending to infinity have relative QUE. This uses only published complete delocalization and label symmetry, not any unverified OpenAI proof step. It is not claimed as a novel literature result.

Independent checks planned: exhaustive exact rational subset enumeration and conditional expectations, the finite-population variance formula, a separate two-point covariance derivation, repeated-eigenspace projection and a localized test obstruction. All computations will be tiny, one thread and memory-limited.

## 4. Fresh source snapshots and resource check

Read round 3 VERIFY.md in full, the startup memory index (read-only) and the brain navigation index. `os.getpriority` reports inherited niceness 20; peak RSS for that check is about 12 MB. Clock at this check: 2026-11-15 04:17 +04; session began approximately 04:15 +04.

Read-only GitHub connector `github_fetch` opened the exact three theorem-source files, lean/docs/ directory and lean/formalization.yaml. Saved fresh source text and Lean scope-note names here. Fresh inventory: 245 scope notes, 218.md present, 219.md absent. Web also opened lean/README.md, 218.md, formalization.yaml and the community GOE page: no contributed notes, automated notes explicitly unreviewed. The family-218 formalization is a finite-graph likelihood comparison for a different companion, not the quoted conformal-universality theorem. No claimed Lean verification of the three main theorems was found. These retrievals are source documentation, not an extended search for a new settlement.

## 5. Proof, preliminary report and independent audit saved

Wrote PROOF.md, REPORT.md and audit_subsets.py before running the audit. The exact increment is `(N-q)/(N-j) * (x-mu)` when revealing a uniform q-subset in random order. Since j<=q<N, its absolute value is at most 2b for weights in [-b,b]; this produces denominator `8q b^2`. Complementation gives q=min(k,N-k). Compressing to every eigenspace and substituting `b=L^2/N`, `t=k r/(N L^2)` gives denominator `8q L^8` and numerator `k^2 r^2` as stated.

The proof includes a full permutation-invariant, simple-spectrum matrix ensemble with L=sqrt(2) that fails singleton QUE: a pairwise row rotation of a Walsh orthogonal basis. This strengthens the earlier single-vector obstruction by verifying every eigenvector of the ensemble is delocalized. It is an abstract counterexample, not a random regular graph. The audit checks actual rational matrices and their eigenvector equations, as well as exact subset variances and prefix conditional expectations. Run next: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_subsets.py` (90-second wall alarm, 80-second CPU cap, no numerical libraries or threads).

## 6. Exact audit passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_subsets.py`.

Output: niceness 20; OMP_NUM_THREADS 1; PASS 189 subset cases, 6,132 subset instances, 7,032 conditional-prefix checks; PASS 6,078 independent subset instances checking the earlier permutation-variance formula; PASS four Walsh matrix ensembles of sizes 2,4,8,16, with 340 eigenvector-coordinate equations and singleton discrepancies checked; PASS 538 repeated-eigenspace subset compressions. Peak RSS 15,351,808 bytes; internal elapsed time 0.23 seconds; exit code 0. No failures.

The earlier variance was rechecked with binary mean-zero tests by independently enumerating subsets rather than the earlier full-permutation-prefix script. The new variance was checked both from direct subset enumeration and the covariance formula; the martingale identity was compared to expectations obtained by summing every remaining completion, not by reusing its closed form.

## 7. Verification document and report completed

Opened all three current READMEs using the read-only GitHub connector: authors OpenAI, dates match the prompt, no correction notices. Reopened the existing Latent Seminar exposition (which disclaims a full proof verification), Lee's November mesoscopic paper abstract and the original BHY abstract. These are previously known source-trail checks, not a newly found solution. Web lean/ root open failed with cache miss; connector lean/docs/ listing already succeeded.

Wrote VERIFY.md with all three fresh exact theorem environments, clause-by-clause comparison, opened-source register, three-sentence replacement status and Spot check. Updated REPORT.md with the completed exact audit and remaining limits. The report uses the later continuation verdict format; VERIFY.md separately records the unchanged release-scope PARTIAL-CLAIMED assessment. No SOLVED_ELSEWHERE.md is warranted: no newly discovered outside result changes the earlier report.

## 8. Final audit and handoff

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_artifacts.py` (30-second wall alarm). Exit code 0. Main theorem environments match fresh sources and both earlier snapshots exactly: GOE 385 characters, Anderson 800, Ising 1,624. Lean catalogue contains none of the three exact main-theorem titles; fresh scope-note inventory confirmed. REPORT.md has the requested continuation verdict and three reason lines; VERIFY.md's proposed row update has exactly three sentences. All checked documents and scripts contain no invalid control characters. Peak RSS 17,678,336 bytes; one thread; niceness 20.

Final non-log artifact hashes from that check: VERIFY.md `e526fdcf797f8f01c68daa5e108ba937693d185a7e444370b244d3f596308216`; PROOF.md `b2d109baec67dd39e6cdf820ea61e2d76713c4b8cd529f23443a2e6e0e7f7463`; REPORT.md `f09cf06f00570fec621637da3bcb4c30d0e55e436cd1931126c46d2c68f5b57c`.

No computation or artifact check failed. The only tool limitations were the inherited-niceness warning, one unavailable alternate startup-index path and a web cache miss for the Lean root listing; successful alternatives are recorded above. No Git operations, external writes, subagents, GPU or numerical-library workers were used. No earlier folder was edited. Local scripts are standard-library-only and all observed local processes stayed below 18 MB RSS.

Next checkable step: specify the stronger intended QUE observable class if one is desired. If retaining prescribed deterministic sets, the proof's scalar variance bound suggests replacing bounded-increment concentration by a variance-sensitive finite-sampling inequality to reduce the unoptimized L^8 logarithmic threshold; that sharpening is not claimed here. The output already resolves relative QUE on prescribed sufficiently large polylogarithmic sets from the published delocalization input.

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” — session start approximately 15 November 2026, 04:15 +04.
