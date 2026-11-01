# Reproduction

Use Python3.12 and NumPy2.3.5 (the actual run versions), with OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and MKL_NUM_THREADS=1. No other package is needed.

Run the following sequentially. Evaluation caps were reached in the actual runs, before their wall-time caps.

    python search_blocks.py --width 2 --pairs 8 --seconds 1200 --evals 500000
    python search_blocks.py --width 3 --pairs 5 --seconds 1200 --evals 500000
    python search_blocks.py --width 4 --pairs 4 --seconds 900 --evals 350000
    python compressed_search.py --width 2 --blocks 24 --seconds 900 --evals 3000000
    python compressed_search.py --width 3 --blocks 10 --seconds 900 --evals 3000000
    python compressed_search.py --width 3 --blocks 16 --seconds 600 --evals 2000000
    python scan_balanced_towers.py --width 2 --blocks 3 --seconds 60
    python scan_balanced_towers.py --width 2 --blocks 4 --seconds 120
    python scan_balanced_towers.py --width 2 --blocks 5 --seconds 420

The seed defaults to20260930. Timings vary across machines, and floating tie-breaking can be platform-dependent. The supplied candidate definitions and exact certificates are sufficient for mathematical replay even if a search trajectory differs.

Certify each supplied *_best.json with:

    python certify_compressed.py FILE_best.json

For the full-table candidates, the supplied full_*_compressed_best.json contains the exact orbit coefficients extracted from the saved full Walsh vector. The certificate reconstructs them directly from the Boolean orbit definition, so the temporary NPY files need not be distributed.

RESULTS.json is a compact factual extraction of the actual completed run outputs. It preserves evaluation counts, restart counts, timings, the best-score histories, candidate references and all balanced-enumeration best definitions. Exact candidate certificate files are separate. Search timing fields are not expected to be byte-identical on replay; exact Walsh data, Parseval/influence identities and mathematical interval endpoints are deterministic.

## Executable source availability

The four executable scripts are proposed in draft PR [#13](https://github.com/yspennstate/math-open-problems/pull/13), pinned at commit 60d3a823b0f55ab46df5916d0cbed87208c187a6. They are not yet merged into master. For replay, obtain those four scripts from that commit and place the candidate JSON files alongside them. Research results and data are archived on master separately.
