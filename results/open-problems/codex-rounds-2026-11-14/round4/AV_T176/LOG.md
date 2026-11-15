# T176 verification log

Task: “take the NEXT checkable step on this problem, building on that work.” Session date: 2026-11-15 (Asia/Tbilisi); initial workspace listing 04:24.

## Step 1 — orientation

Read the two earlier REPORT.md files with `OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...` and listed this folder with the same prefix. Both reports restrict the claimed optimal mixing result to powers of two. Round 3 checks conditional flows and averaged marginals and recommends Lemma 5.1 and the eight-factor/sign comparison next.

The sandbox reports `nice: setpriority: Operation not permitted` even for these small read-only commands. No substantial computation will run under that unresolved restriction. All writes stay in this folder; global mesh/checklist/brain writes are excluded by the task's explicit scope. No git or subagents.

## Step 2 — earlier records and bounded literature search

Read both earlier LOG.md and REPORT.md files, the first session's VERIFY.md, round 3's complete PROOF.md, and the short preprint's saved source. `find ... -maxdepth 2 -type f` confirms the first session has no PROOF.md or scripts and round 3 has no computation scripts. Read the startup memory index and compute-state JSON: status `warn`, mode `owner_away_open`, CPU saturated; no heavy work planned.

Web search queries: `"Thorp shuffle" "2026" mixing OpenAI correction`, `"Optimal-order mixing of the Thorp shuffle"`, `"Thorp" "Jiang" "2610.18884"`, `"Thorp shuffle" "November" "2026" correction error even`, and `"Thorp shuffle" "OpenAI" refutation`. Opened repository history.md, arXiv:2610.18884 and the repository issues page. History lists no Thorp correction; the opened arXiv page still describes Jiang's dyadic subquadratic bound. No new all-even solution was found in this brief, under-five-minute search; no SOLVED_ELSEWHERE.md is warranted. Search results alone were not treated as opened papers or validation.

## Step 3 — independent recheck; chosen extension

Re-derived the previous local claim without using its induction formula: a free/occupied edge creates a dipole of squared norm w²/2, each subsequent unused transverse-coordinate average halves that norm, giving the coefficient 2^(-j). With beta=1/16, the infinite delay kernel at gamma=31/32 has mass (15/16)/(2gamma-1)=1; the additive fixed point is eta/beta=32exp(-n/256). For the rate, log(32/31)>1/32 and log 2<3/4 imply 198log_2(32/31)>198/24>8, so the marginal bound is O(n^(-5/2)). The earlier calculation holds at this independent recheck; the random-input average remains essential.

Chosen single extension: audit the remaining representation-theoretic completion of the short paper, centered on Lemma 5.1 (reciprocal representation degrees), and trace its use through the previously checked orbit bound into the final eight-factor/sign comparison. This is exactly the next unresolved input named by round 3. An explicit finite-s majorant will make the convergence argument checkable without a partition enumeration or Lean build. This checks local source arguments, not independent peer review of the whole theorem.

## Step 4 — primary sources reopened and saved

Reopened the short paper's current build/main.tex, both long papers' build/main.tex and build/sections/00-introduction.tex, lean/docs/238.md, and lean/OAI/Probability/ThorpShuffle/Main.lean using read-only `github_fetch` URLs. Saved their returned text in this folder as *-source.tex, lean-scope-238.md and lean-thorp-main.lean. Web fetch succeeded for the short paper and Lean scope, but gave cache misses for the two long introductions; the connector supplied those exact sources. All three author/date headers are OpenAI / September 26, 2026. `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/cmp optimal-source.tex ~/codex_op_1114r3/briefs/AV_T176/optimal-main.tex` returned exit 0: the audited source is unchanged.

Extracted all five relevant theorem/corollary environments directly from the returned source strings. The current Lean main states `full_mixing` at 1600*d and the order theorem; no build was run. The scope note explicitly excludes Compatibility's regular-moment theorem and Routing's changed later statements from those selected companion formalizations. These are repository scope claims, not a new proof-check certificate.

## Step 5 — representation completion checked

Wrote PROOF.md. Its new finite-s majorant splits diagrams into a bounded tail u≤K, the summable tail 2sum_(u>K) exp(3sqrt(u))3^(-u), a middle contribution exp(3sqrt(s))2^(-floor(s/16)), and a hook contribution exp(3sqrt(s))(e/4)^s. Sending s to infinity first and then K to infinity proves Lemma 5.1 without relying on a stronger cited theorem. Checked that row-order truncation is a Young subdiagram and that every retained tableau extends.

Traced that lemma through the common trimming, orbit bound and eight-factor Fourier comparison. Re-derived A²=32C_1 and the final exponent 2-16(5/16)=-3 by two norm calculations. Rechecked unnormalized Plancherel to rule out a missing group-size factor. The trim loses r≤16epsilon_n, its TV error is exactly r, its sign coefficient is at most r/(1-r), and convolution comparison costs at most 8r. PROOF.md records the resulting explicit conditional TV estimate with trimming term 128epsilon_n and Fourier constant (32C_1)^8. No defect found locally; the full preprint and Lean dependency graph are not certified.

Tried boundary cases u=1, u=s/4, L=s/8, partial last retained rows, self-transpose diagrams, s=1 and parity-dependent trimming. The cases do not break the argument. No numerical experiment, partition enumeration or heavy local program was run.

## Step 6 — deliverables and formatting audit

Saved REPORT.md with the continuation task's PARTIAL prefix, then VERIFY.md with all five exact source environments, comparison of every clause, opened follow-ups and Lean scope, the three-sentence recommended status, and the new spot check. Re-read REPORT.md and the tail of VERIFY.md. This caught escaped-math corruption in the generated VERIFY.md footer; corrected it with a raw-string replacement. A guessed `/usr/bin/rg` path did not exist; repeated the author/date check with `rg` from PATH. Read the startup-index note about stacked nice levels as a possible explanation for the priority warning, but did not infer an actual process priority from it.

## Step 7 — final audit

Re-read both authored mathematical files from disk. Tool-orchestration JavaScript verified all five quoted theorem environments against the freshly opened source strings: five exact matches. Both markdown files contain no unexpected control characters; the final LaTeX formula is intact. Current Compatibility and Routing introduction snapshots also match round 3 byte for byte (`cmp` exit 0 for both). Re-read the actual Lean main: its theorem includes 1600d convergence, worst-start equality, the support lower bound and IsTheta(log(2^d)). No build or full dependency audit is claimed.

Rechecked the bound in PROOF.md: removed mass ≤16epsilon_n, eight replacements ≤128epsilon_n, A^16=(32C_1)^8, sign contribution raised to 16, nonsign exponent −3. The finite-s majorant uses s→infinity before K→infinity, and handles initial small sizes separately. REPORT.md retains the required continuation verdict and names precisely what remains unchecked. All authored files and source snapshots are in this folder; no git, external mutation, brain/mesh writes, or subagents were used.
