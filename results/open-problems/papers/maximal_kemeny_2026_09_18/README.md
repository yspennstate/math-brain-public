# The maximal Kemeny constant of an n-vertex graph

**Yitzchak Shmalo**  
Einstein Institute of Mathematics, The Hebrew University of Jerusalem  
Preprint, 18 September 2026 — 12 pages.

[Read the complete PDF](paper/main.pdf) · [LaTeX source](paper/main.tex) · [Exact checker](checks/check_kemeny.py) · [Recorded output](checks/check_kemeny_output.json) · [Large-order checks](checks/large_order_checks.py) · [Lean certificate](checks/lean/ScalarGap.lean) · [Audit, 18 September](AUDIT_2026_09_18.md)

## Named open problem and main theorem

The paper proves the Kemeny-constant / tau_0 assertion in **Aldous–Fill Open Problem 6.13** for all connected simple unweighted n-vertex graphs, with the usual discrete-time simple random walk:

`max_G K(G) = n^3/54 + O(n^(19/7))`.

The relaxation-time / tau_2 assertion was already proved by Aksoy–Chung–Tait–Tobin (2018); recovering it is not counted as a new open-problem resolution. This is not Aldous–Fill 4.49(ii), the already-posted flow/diameter paper. The regular-graph Kemeny assertion in Open Problem 6.14 and exact finite-order extremizers are not settled here.

Original source: https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch6.S3.html

## Additional results in this version

- The refined cluster count improves the earlier repository remainder `O(n^(11/4))` to `O(n^(19/7))`.
- An asymptotic stability theorem forces two almost-complete vertex sets of size `(1/3+o(1))n` and total edge count `(1/9+o(1))n^2`. A connected spanning subgraph, after `O(n^(12/7))` deletions, has a bridge path of length `(1/3+o(1))n` between the large blocks. The path-bridge assertion is about that subgraph, not necessarily the original graph.
- A general induced-edge capacity theorem gives, for fixed r, maximal Kemeny constant and relaxation time `(r-1)n^3/(54r)+O_r(n^(19/7))` on connected `K_(r+1)`-free graphs, and on graphs of chromatic number at most r. The bipartite and triangle-free constants are `1/108`.

The additional theorems solve related extremal optimization problems. They are not presented as additional named conjectures without an exact source posing those statements.

## Build

All bibliography entries are embedded in the TeX source; no external bibliography or figures are needed. On Overleaf select `paper/main.tex` as the main document. Locally:

```sh
cd paper
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The private repository has a narrowly scoped build workflow for changes to this paper's main.tex. Run 35344601373 completed successfully and committed the compiled PDF. A GitHub-built PDF and the locally compiled, emailed PDF may differ in build metadata; they use the same verified TeX bytes.

## Additional checks (18 September)

`python checks/large_order_checks.py` (numpy only, 3 s) evaluates the balanced complete barbell at orders 30 to 1,440 by the spectral formula, pinned to an exact rational computation on one instance: 54K/n^3 falls from 1.157 to 1.0021 and the barbell itself is n^3/54 + 0.056 n^2 + o(n^2). The best block fraction is exactly 1/3 at every order tested; the exact maximum of K over every connected graph of order 2 to 7 is attained by a barbell at every order; two balanced complete bipartite blocks joined by a path give 108K/n^3 = 1.0095 at n = 960. Recorded output: `checks/large_order_output.json`.

`lean checks/lean/ScalarGap.lean` (Lean 4.34.0, no Mathlib) checks identity (3.13), 1/54 − s^2(1−s)/8 = (3s−2)^2(3s+1)/216, over the rationals and in cleared form over the integers; exit code 0.

## Reproduce the finite checks

Python 3.10+ is required, with NetworkX and SymPy. The recorded run used Python 3.13.5, NetworkX 3.6.1 and SymPy 1.14.0.

```sh
python -m pip install networkx==3.6.1 sympy==1.14.0
python checks/check_kemeny.py > checks/recheck.json
```

Recorded result: `ALL_FINITE_CHECKS_PASS`.

The run covers 995 connected Graph Atlas graphs of orders 2–7, 995 bridge identities, 158 independent fundamental-matrix comparisons, 1,942 connected edge-deletion comparisons, 995 refined internal-resistance bounds, 39,692 incident-energy comparisons, 995 clique-capacity checks, and 15 multipartite-barbell test instances. One barbell instance is deliberately repeated by the parameter loop; the count is tests, not distinct graphs. All arithmetic in these checks is exact. Finite checks do not prove the asymptotic theorem, the cited decomposition theorem, or novelty.

## Provenance and review status

The source proof was developed in the R04 reports:

- `runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`, blob `14e4aa8569cf171b0bb7411aa0d9f75a37c0eb45`;
- `runs/R04/20260916T2312Z_i0027_quantitative_rate.md`, blob `db97cd6baa5e842c766282b14e0d9b9b4822d575`.

The earlier source-level proof has the recorded R03 audit `R03-AUDIT-R04-I0027-C8-08`. The additional R03 audit `R03-AUDIT-R04-I0027-C11-09` concerns the earlier quantitative upgrade conditional on the retained dependency chain. These are not two different reviewers. No missing P26 pass is manufactured by this manuscript upload.

The new 19/7 refinement, stability theorem and clique-free extensions were derived and self-reviewed in the manuscript-preparation session, with the accompanying checks. Later on 18 September the manuscript was read line by line by Anthropic's Claude (Fable 5.1): every proof step re-derived, the decomposition theorem checked against arXiv:1711.06530, Open Problem 6.13 checked against the Aldous–Fill page, the exact checker re-run, the large-order and exhaustive checks in `checks/large_order_checks.py` added, and identity (3.13) machine-checked in `checks/lean/ScalarGap.lean` (Lean 4.34, core only). The report is `AUDIT_2026_09_18.md`; its verdict is that the proof is correct as written. That pass rewrote the declaration, data-availability and funding sections and changed no mathematics. No independent human peer review is claimed. The bounded literature check included the original Aldous–Fill source, Alev et al.'s induced-resistance decomposition, the 2018 relaxation-time theorem, barbell formulas, and September 2026 adjacent papers. It is not exhaustive publication-priority certification.

This folder is a manuscript delivery, not a silent update to fleet audit counts, scheduler state or peer ownership. Existing research reports and successor assignments are preserved.

## Integrity

The audited version of main.tex (18 September, after the declaration rewrite) has 42,859 bytes, Git blob SHA `5a78adc45efc7b695ce26571f31952bb21b0aaf4`, and SHA-256 `5d49c102da3a97343a74a3ff9de73f59769ae27a2b63eaa40bf01cf81511c190`; the mathematical content is byte-identical to the creation version, blob `8c3b2a798c6da57eebd74db5d519ffa339b5a92f`, SHA-256 `1ad23fd3f8db11bc094068f70296284b97334df0b05316e0eef7e7527be5b760`, creation commit `21255723c237739289c8eacfadb8723f9142bf2c`. Hashes are of the LF-normalised blob, which is what Git stores; a Windows checkout with CRLF endings will hash differently on disk.

The checker has Git blob SHA `e2b3097ddede98334dc8f73da779b9eef30ee95c` and SHA-256 `f126458ac6ccf47ad7c3d83ea355d078c35006a5509703c09c3ae58ee588192b`. The output is JSON; whitespace formatting does not affect its recorded values.

## Public-repository status

The owner requested a separate public, paper-only repository named `maximal-kemeny-constant`. The current GitHub connector supports writes to existing repositories but exposes no repository-creation action. No public repository is claimed to have been created. This copy is in the existing **private** `math-open-problems` repository. The author receives a ready-to-publish source/PDF bundle separately; no ResearchGate, arXiv, website posting or visibility change was made by this delivery.
