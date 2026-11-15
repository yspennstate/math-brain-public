# T078 work log

Task: “push this problem forward by one checkable piece.” Session began 2026-11-14 at 20:52 +04 (Asia/Tbilisi); exact user-message time was not supplied.

## 20:52 +04 — Orientation and literature search

Read the local memory index and brain navigation/protocol as read-only orientation. The task-specific rule forbids writes outside this folder, so did not invoke memory, checklist, or mesh commands that would write their stores outside it. No subagents, git, or external writes.

Initial read commands: `pwd`, `rg --files -g 'AGENTS.md' -g 'MEMORY.md' -g 'LOG.md' -g 'REPORT.md' -g 'PROOF.md'`, `date '+%Y-%m-%d %H:%M:%S %Z'`, and read `~/.claude/compute/compute_state.json`. Governor reported `status: warn`, `mode: owner_away_open`, CPU saturation. No numerical computation is planned unless necessary.

Subsequent shell reads were launched with `OMP_NUM_THREADS=1 nice -n 15`. The sandbox printed `nice: setpriority: Operation not permitted`; its shell still executed. `ps` was also denied. Therefore the requested priority could not be verified. No numerical program or heavy computation was run, and none will be needed if the literature result is confirmed.

Used the web search tool with queries:

- `quantum Heisenberg ferromagnet spontaneous magnetization open problem 2025 2026 proof`
- `Heisenberg ferromagnet long range order Z3 positive temperature proof random interchange 2024 2025 2026`
- `"Spontaneous magnetization in the quantum Heisenberg ferromagnet" 2026`
- `"Heisenberg" "ferromagnet" "2026" proof OpenAI magnetization`

Search returned a September 24, 2026 manuscript by OpenAI claiming precisely the requested spontaneous-magnetization result, plus October 5 companion claims. This predates the brief's November status check, so the discrepancy needs direct primary-source verification. Secondary pages are discovery leads, not evidence of validity.

Decision before further work: follow task step 1 and inspect the primary manuscript and stated theorem. If confirmed, write SOLVED_ELSEWHERE.md and REPORT.md and stop; do not start a separate mathematical subtask.

## Primary-source checks (within the ten-minute search window)

Opened the primary GitHub PDF landing page, the release's `lean/docs/271.md`, `lean/ComparatorChallenges/Heisenberg.lean`, and `lean/OAI/MathematicalPhysics/Heisenberg/Main.lean`, all through the web tool.

The scope note states order for all the required dimensions and spins. The comparator defines the nearest-neighbor Hamiltonian with the ferromagnetic minus sign and each edge once. It encodes spin as an integer `ell = 2S` and concludes magnetization at least `ell/8 = S/4`. Its theorem ends with `sorry`: this is the challenge statement, not the purported proof. The separate implementation `Main.lean` has a proof body for `spontaneous_magnetization`, invoking `dynamics_converges` and `ordered_state_exists`. This checks the claimed formal statement a second way; it is not an audit of imported dependencies or a local Lean compilation.

Access failures: raw `paper.tex` returned 404; the PDF landing page supplies no parsed manuscript text; raw PDF was rejected as unsupported `application/octet-stream`; alternate GitHub raw routes returned cache-miss/robots errors. Continuing briefly to locate the primary TeX. No claim of having read the PDF is made.

## Manuscript located and stopping rule applied

Followed the manuscript link from the community catalogue to its readable copy:
`https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf`.
The web tool opened the 54-page PDF. Inspected the title/author/date, equation (1.1), Theorem 1.1, and the formulation caveat in Section 1.2. This resolves the earlier PDF-access failure. Also requested screenshots of PDF pages 1 and 3; the title-page screenshot returned cache miss, so relied on the parsed PDF text.

Cross-check result: the model has the required sign and edge convention, and the paper covers d = 3 and S = 1/2 as well as the remaining required cases. Independently compared the formal theorem's integer-spin parametrization: (2S)/8 = S/4, giving 1/8 at S = 1/2. No simulation or temperature-limit extrapolation enters this check.

Opened a community comparator-log landing page; a text search for `accepted` found no match, so no locally verified comparator-success claim is made. No attempt was made to build Lean, download a large repository, or certify the proof. Primary manuscript metadata do not supply an arXiv identifier for this preprint; none is invented.

Created SOLVED_ELSEWHERE.md and REPORT.md with `apply_patch`. Chose a PARTIAL verdict because a matching solution claim was located and its scope checked, while its correctness was not independently audited. All literature activity stayed within the initial ten-minute allowance. No separate research piece was begun, in accordance with step 1.

## 20:54:35 +04 — Final file check

Command: `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'head -n 3 REPORT.md; wc -c LOG.md SOLVED_ELSEWHERE.md REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'`.

Output: REPORT.md starts with the required `VERDICT: PARTIAL ...` line. All three files exist (before this log append: 4,981, 2,317, and 2,015 bytes respectively). Timestamp 2026-11-14 20:54:35 +04, approximately two minutes after starting. `nice` again reported priority-setting denied. This log append is the final mutation.
