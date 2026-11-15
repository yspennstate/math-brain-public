# T347 work log

Task: “push this problem forward by one checkable piece.”
Start: 2026-11-14T22:14:15.607041+04:00

## Orientation and constraints
Read the prompt, brain navigation index, and compute governor state. The governor reports warn/cpu_saturated, with owner away. No heavy computation is planned. All writes stay in this folder; therefore global brain recall logging, checklist registration, and mesh registration (which write outside this folder) are not run. No git and no agents.

Commands so far: `pwd`; `rg --files -g '!\.git' -g 'AGENTS.md' -g '*.md' -g '*.py' .`; a short Python read of compute_state.json and startup-memory candidates. Only PROMPT.md was initially present.

The requested `OMP_NUM_THREADS=1 nice -n 15 python3 ...` prefix reports `nice: setpriority: Operation not permitted` in this sandbox. This affects priority setting; only short read/write and scalar calculations will be used, with no simulation or numerical sweep. Actual priority is recorded below.

## Literature search, bounded to ten minutes
Started web searches for rigorous Hopfield capacity results, including 2025/2026 and Feng–Shcherbina–Tirozzi. Results and opened references to follow.

Actual Python priority: 20.

## Step 1: initial literature finding
Opened https://hexagonmath.org/2611.00105v1 (Yuwen Zhou, THE CRITICAL CAPACITY OF THE HOPFIELD MODEL, version 1, Nov 5 2026; history lists initial deposit Nov 4). It claims a capacity interval [0.138198129, 0.13820106] for a constrained-free-energy well definition, and references a new arXiv paper 2611.03306. The Hexagon paper is explicitly mainly AI generated; its claim is not taken as verified. PDF direct open failed once. Checking the actual theorem scope and primary dependency before deciding whether the stop rule applies.
Opened https://arxiv.org/abs/math-ph/0012038: J. Feng, M. Shcherbina, B. Tirozzi, On the Critical Capacity of the Hopfield Model. Its abstract explicitly states alpha <= 0.113 and agreement of small-alpha retrieval errors with replica predictions. Full theorem not yet checked.

Priority audit: os.getpriority returned 20, already lower scheduling priority than requested 15, so the nice warning is an attempted priority increase from inherited 20 to 15. Retaining inherited priority 20 satisfies the compute intent.

## Step 2: stop-rule decision and scope audit
Opened https://arxiv.org/abs/2611.03306 and its HTML https://arxiv.org/html/2611.03306v1. Read Theorem 1.1, Theorem 1.4, Corollary 1.5, the replica-symmetry discussion, and related-work discussion. This is a substantial new Bernoulli-pattern free-energy result, so the user's first-step stop condition applies. No original subproblem is selected.
Also opened https://arxiv.org/abs/2610.32618: Francesco Camilli, Pierluigi Contucci, Emanuele Mingione, The solution of the Hopfield model with Gaussian patterns. This is a different disorder ensemble and is not used to settle binary-pattern retrieval.
Followed the Hexagon PDF link successfully. Read definitions (1.11)–(1.12), Theorems 1.1–1.4, and Section 1.5. Searched its text for “fixed point”: no match; this is a search observation, not evidence that no dynamical consequence exists. The claimed endpoints match its abstract and Theorem 1.4(c), independently of their mathematical correctness. Screenshot requested for PDF page index 4. No certificate run or independent proof audit.

Web tool operations: search_query with “Hopfield model storage capacity 0.138 rigorous proof 2025 2026” and “Hopfield model rigorous retrieval capacity 0.113 Feng Shcherbina Tirozzi”; open the URLs above and math-ph/0012038; click the PDF/source and HTML links; find theorem labels, “retrieval”, “replica”, “Bernoulli”, and “fixed point”; open relevant introductory theorem sections.

Normalization audit: their (1.2) is N^{-1} log E_sigma exp[beta |X^T sigma|^2/(2N)], with E_sigma uniform. This equals the pressure for the energy in the prompt, minus log 2 if counting measure is used instead. An all-load equilibrium formula alone does not identify metastable retrieval thresholds.

## Step 3: saved deliverables
Command prefix for all Python file writes: `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'` (short standard-library scripts). Wrote SOLVED_ELSEWHERE.md and REPORT.md. No simulation, numerical capacity estimate, new theorem, git operation, outside-folder write, or external publication. Stopping under the literature rule.
