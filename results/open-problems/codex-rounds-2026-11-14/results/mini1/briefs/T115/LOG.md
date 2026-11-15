# T115 work log

Task received: 14 November 2026, approximately 21:17 Asia/Tbilisi
(17:17 UTC). “Push this problem forward by one checkable piece.”

## Step 1: orientation and literature check

All writes are confined to this folder, as required by the task-specific
instructions. The global memory index and compute-state file were read;
brain recall, mesh registration and checklist commands were not run because
they would write outside this folder. No subagents or git operations.
Compute state: status warn, mode owner_away_open, about 74% memory free.

Read-only shell inspection: `pwd`, `ls -la`, and `rg`/`sed` on the memory
index and brain navigation views. A targeted read-only search found a prior
T115 memory; it is a lead to check against the papers, not evidence by itself.

Web searches (tool: web.run):

- `"Gotsman" "Linial" "2026" sensitivity`
- `"Gotsman Linial" conjecture polynomial threshold functions average sensitivity recent`
- `arxiv 2604.08095`

Result: a primary-source candidate for a complete solution, OpenAI,
*Average sensitivity of polynomial threshold functions*, 25 September 2026,
in the public openai/math preprint release. Its stated bound is
`I(f) <= 8 d sqrt(n)` uniformly in degree and dimension.

Opened the GitHub PDF landing page and a secondary HTML rendering to locate
the theorem; the raw primary PDF and source must still be opened before
concluding. Also opened https://arxiv.org/abs/2604.08095 : version 3,
26 October 2026, explicitly refers to the conjecture as recently solved by
OpenAI. Its own result still concerns Boolean surface area.

Choice: check whether this candidate really settles the entire stated
problem. If confirmed, use the requested SOLVED_ELSEWHERE route and stop;
otherwise select a separate mathematical piece before proceeding.

## Step 2: corroboration and retrieval issues

Read the prior memory `t115_gotsman_linial_asymptotic_proof_checked_in_full_2026_11_12.md`
without modifying it. It points to the same paper and reports an earlier
audit, but no earlier numerical tests are claimed as this session's work.

Opened https://arxiv.org/html/2604.08095v3 . The introduction independently
prints `AS[f] <= 8 d sqrt(n)` as equations (1.6) and (1.15) and attributes it
to OpenAI. The authors are Fan Chang, Joseph Slote, Chun-Kai Tseng,
Alexander Volberg and Haonan Zhang.

Raw PDF retrieval through web.run failed with unsupported content type;
the guessed `main.tex` URL returned 404. The actual source is in a `build`
subdirectory, discovered by following the HTML rendering's source link.
Proceeding to read that primary source using the connected GitHub read tool.

## Step 3: primary source opened; complete statement confirmed

Connected tool: `mcp__codex_apps__github_fetch({url: URL})`.
Read the primary paper's `build/main.tex` and all five proof sections at
https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build .
The section files are `01-introduction.tex`, `02-coupling.tex`,
`03-weighted-grading.tex`, `04-edge-recovery.tex`, `05-parity-coupling.tex`.
The introduction file's GitHub blob SHA is
`16ade5e4d1fe086adc8f7ebb012b759601471af1`.

Output that matters: main.tex names the author OpenAI and date September 25,
2026. Theorem 1 has exactly the uniform-cube total-influence definition in
the task and proves `I(f) <= 8 d sqrt(n)` for all `1 <= d <= n`, including
zeros with sign(0)=1. The final proof section assembles that bound with no
fixed-degree hypothesis. This settles the entire requested asymptotic form.

Also read `lean/docs/127.md` and
`lean/ComparatorChallenges/GotsmanLinial.lean` through the same tool.
The latter explicitly defines influence by a sum of sensitive-vertex counts
divided by `2^n`; its statement matches the paper. It is a challenge
statement containing `sorry`, not the implementation proof. No Lean build
or independently verified formal certification is claimed here.

Additional web searches: `"Average sensitivity of polynomial threshold functions" "OpenAI" arxiv`
and `"Average sensitivity of polynomial threshold functions" erratum error gap`.
No arXiv identifier for the solution or specific erratum was identified.
This is a bounded search, not a guarantee against an unindexed correction.

## Step 4: attempt to break the identification

Checked the primary proof's five sections, especially the edge normalization,
one-sided support condition and zero perturbation. Independent scope and
constant checks are recorded in SOLVED_ELSEWHERE.md. The later, separately
authored arXiv paper prints the same numerical bound in its own notation.
No computation, numerical experiment, installation or background process
was necessary. All shell operations were read-only inspections; all writes
used apply_patch in this folder.

Decision: stop under step 1's complete-solution exception. No new special-case
theorem or counterexample search is represented as this session's result.

## Step 5: final artifacts

Read the primary `lean/OAI/Combinatorics/GotsmanLinial/Main.lean`: the
final theorem has no auxiliary grading hypotheses, handles zeros, and
implies the challenge statement. The fetched file contains no `sorry`;
this says nothing by itself about its imports. No build was run.

Wrote SOLVED_ELSEWHERE.md and REPORT.md. The verdict explicitly attributes
the proof elsewhere. The scope audit covers d=0, d>n, n=0, nonmultilinear
inputs and both fixed choices for the sign of zero. Independently checked
the ordered-edge conversion and binomial variance by counting identities.
No new research claim is made. Literature check and identification took
less than ten minutes, starting at 17:17:48 UTC.

Final artifact check (read-only, no mathematical computation):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -c 'from pathlib import Path; names=("LOG.md", "SOLVED_ELSEWHERE.md", "REPORT.md"); [(print(name, len(Path(name).read_bytes()), "bytes")) for name in names]; first=Path("REPORT.md").read_text().splitlines()[0]; assert first.startswith("VERDICT: PROVED "); print(first); print("Artifact checks passed.")'
```

Output before this final log append:

```text
nice: setpriority: Operation not permitted
LOG.md 5711 bytes
SOLVED_ELSEWHERE.md 3997 bytes
REPORT.md 1698 bytes
VERDICT: PROVED T115's O(d sqrt(n)) bound, elsewhere (OpenAI, 2026)
Artifact checks passed.
```

The environment rejected nice's priority adjustment but allowed the tiny
file check to complete. No heavier program was launched. Final artifact
checks passed; the priority adjustment itself is not claimed successful.
