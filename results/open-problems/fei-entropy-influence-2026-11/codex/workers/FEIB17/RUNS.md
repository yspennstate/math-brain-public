# Reproduction

Run from FEIB17 with Python 3, NumPy and SciPy. Set OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and VECLIB_MAXIMUM_THREADS=1. The processes inherited nice 10; audit_results.json, reductions.json, path_census.json and final_checks.json record the actual priority. No language-model workers or subagents were started.

Each command below writes its JSON receipt and can be redirected to the matching .log file. The supplied five-variable representatives remain read-only in ../FEIB11/npn5.txt; source_provenance.json and vertex_lp.json record the hash. The script checks that representative file; it does not regenerate NPN coverage.

| Command | Output | Purpose |
|---|---|---|
| python3 audit.py | audit_results.json | All four-variable functions; mixed samples at n=6,7,8; direct restrictions, JS, edge, pair and block identities |
| python3 path_census.py | path_census.json | Two adaptive policies and exact random-order integral, exhaustive n=4 |
| python3 reductions.py | reductions.json | Exact switches on all n=4 bases, random-order samples, block counterexample |
| python3 exact_families.py | exact_families.json | Bent product formula, exact majority influences, AND, tribes greedy proxy, complex product formulas |
| python3 vertex_lp.py | vertex_lp.json | Candidate LP on supplied five-variable representatives; independent threshold holdouts |
| python3 witnesses.py | witnesses.json | Majority blocks, adjacent low levels, singleton budget and constants |
| python3 extra_checks.py | extra_checks.json | Explicit convolutions, exact tribes pair formula, direct complex transforms |
| python3 records.py | records.json | Best-coordinate census, balanced record construction, tribes and address checks |
| python3 edge_budget.py | edge_budget.json | Boolean weighted edge-budget candidates on independent banks |
| python3 singular_examples.py | singular_examples.json | Boolean families defeating both raw KL shortcuts |
| python3 record_precision.py | record_precision.json | Independent integer-transform and high-precision record check |
| python3 final_checks.py | final_checks.json | Receipt assertions, actual composed truth table, counterexamples and provenance |

The only solver warning is SciPy reporting that the threads=1 option is forwarded to HiGHS. It is intentional. Earlier transient NumPy matmul warnings were removed by replacing these tiny products with explicit elementwise sums before the saved final audit run. There are no final NaNs or failed assertions.

Brain orientation used brain.py recall with refresh disabled, followed by the full card fei_most_influential_coordinate_fails_by_composition_2026_09_24. That card helped by warning that balanced composition had already refuted largest-influence selection, so the construction here is treated as a referee verification rather than a new discovery. math_recall.py returned “math store not found”. No math was supplied by it. Test-rigor cards were read; this is a mathematical checker, not a brain/no-brain model benchmark.

The primary literature check was Theorem 1.3 of Kelman–Kindler–Lifshitz–Minzer–Safra, linked in PROOFS.md. It was used to avoid misstating a concentration result as a total-entropy bound; it was not used to prove any new bound.
