# T053 work log

Task: “Diffusion in the random Lorentz gas at fixed density”; session began 14 November 2026, 20:46 +04:00.

Scope: all writes stay in this folder. The earlier global requests to update the shared brain, checklist, and mesh are superseded by the task’s folder-only rule; no such writes were made. No git or subagents. Startup memory and compute state were read; compute status was ok.

## Step 1: literature check (started 20:46 +04:00)

Web search queries: `random Lorentz gas fixed density central limit theorem 2024 2025 2026`; `Poisson Lorentz gas invariance principle recurrence fixed scatterer density recent`.

A potentially substantial update was found: arXiv:2506.18539, “Improved geometric and recollision estimates for the invariance principle of the random Lorentz gas”. Opening its arXiv page and full paper to check the precise theorem before deciding whether the literature-stop instruction applies. Also opening the original arXiv:1812.11325 to compare the actual parameters. Search snippets alone are not evidence.

Local read command: `OMP_NUM_THREADS=1 nice -n 15 python3 -` (a short standard-library script reading startup memory and compute state). The wrapper printed `nice: setpriority: Operation not permitted`; checking actual inherited priority before further computation. No substantial computation was run.

## Step 2: verified substantial literature advance

Opened https://arxiv.org/abs/2506.18539 and the published paper https://orca.cardiff.ac.uk/id/eprint/185473/1/Matthies_2026_Nonlinearity_39_035003.pdf . Authors: Karsten Matthies and Raphael Winter. Publication: Nonlinearity 39 (2026), 035003, published 5 March 2026; DOI 10.1088/1361-6544/ae4602. The introduction restricts the model to R^3 and explicitly improves the joint-limit condition from T(r) r^2 |log r|^2 -> 0 to T(r) r^2 |log r| -> 0. The original arXiv:1812.11325 page independently confirms the older condition.

Decision: this is a substantial advance beyond the supplied status paragraph, so apply step 1’s instruction to write SOLVED_ELSEWHERE.md and REPORT.md, then stop. The filename will not be used to imply that fixed-density T053 was solved. No new proof or computation will be claimed. Checking the exact theorem and related quenched update before finalizing.

Priority check command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, using `os.getpriority(os.PRIO_PROCESS, 0)`. Output: `nice value: 20`. The inherited process is already at lower priority than requested; the wrapper warning does not mean a high-priority job. Memory note on macOS relative nice stacking corroborates this behavior.

## Step 3: exact theorem and scope audit

Opened the complete arXiv HTML versions https://arxiv.org/html/2506.18539v2 and https://arxiv.org/html/2501.00519v2, plus Tóth's own publication page https://www.mdpi.com/1099-4300/27/4/397 and arXiv abstract https://arxiv.org/abs/2501.00519 . Additional search query: `"Semi-quenched invariance principle" "Tóth" arxiv`.

Read Matthies–Winter Theorem 3.1 and Tóth Theorems 2 and 3. The latter's almost-sure conclusion requires a summable extractor sequence; its in-probability conclusion is distinct. The models remain three-dimensional and in a simultaneous kinetic/diffusive limit. Did not assume the newer annealed time window also holds semi-quenched. The Matthies–Winter reference list gives 1053 for Tóth; his own publisher page gives article 397, which is used in the deliverable. PMC access returned a browser challenge; switched to the publisher and arXiv full text.

Independent check of the logarithmic improvement: take L=|log r| and T=r^(-2)L^(-3/2). Then T r^2 L=L^(-1/2)->0, whereas T r^2 L^2=L^(1/2)->infinity. Recompute using r=exp(-s), T=exp(2s)s^(-3/2): the same products are s^(-1/2) and s^(1/2). This verifies strict improvement. Holding any fixed r in (0,1) instead makes T r^2|log r| diverge as T->infinity, exposing the missing fixed-density case. No diffusion coefficient normalization was asserted beyond the paper's Wiener normalization.

Created SOLVED_ELSEWHERE.md and REPORT.md with `OMP_NUM_THREADS=1 nice -n 15 python3 -` (standard-library text writes). No PROOF.md: the literature-stop branch applies. No claim of an original theorem. No simulation and no heavy process.

Literature check and report drafted at 2026-11-14T20:48:24.434591+04:00.

## Step 4: final verification and stop

Final audit command (run from this folder):

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os,pathlib,datetime; p=pathlib.Path("."); names=("LOG.md","SOLVED_ELSEWHERE.md","REPORT.md"); print("priority",os.getpriority(os.PRIO_PROCESS,0)); print("report_first_line",(p/"REPORT.md").read_text().splitlines()[0]); [(print(n,"bytes",(p/n).stat().st_size)) for n in names]; assert (p/"REPORT.md").read_text().startswith("VERDICT: PARTIAL "); assert all((p/n).stat().st_size>0 for n in names); assert "fixed-density T053 remains open" in (p/"SOLVED_ELSEWHERE.md").read_text(); print("audit PASS",datetime.datetime.now().astimezone().isoformat())'
```

Output:

```text
nice: setpriority: Operation not permitted
priority 20
report_first_line VERDICT: PARTIAL substantial post-2020 advances verified; fixed-density T053 not solved
LOG.md bytes 4362
SOLVED_ELSEWHERE.md bytes 2686
REPORT.md bytes 2438
audit PASS 2026-11-14T20:48:32.759179+04:00
```

The byte counts precede this log append. A final web `find` for `Theorem 3.1.` in the published PDF returned its complete statement: the improved time condition and averaged-quenched convergence match the arXiv statement. Literature checking finished within three minutes, below the ten-minute cap. Stopping under task step 1.
