# FEIB06 report

The brief is complete. No working potential was found. The census and programs are saved. The unweighted entropy family is classified and only returns the original root-bound problem; three other feature families are ruled out under a universal root budget. The fitted broader candidates have concrete killing examples. FEI remains open.

The exhaustive census covers all Boolean truth tables through four variables. The larger samples contain 9,668 five-variable and 11,783 six-variable truth tables, including 8,192 IID draws per dimension before deduplication and the structured additions documented in DATA.md. Every E/D order is represented by a shared squared-spectrum DAG. All requested features and up-ratio extrema are saved as compressed NumPy files. Counts and seeds are in census_summary.json and data/n*/metadata.json.

I minimized both the literal local C and the useful total C+Cprime, enforcing the census root and scalar-leaf conditions. Every-coordinate payment uses LP; best-coordinate payment uses a disjunctive MILP. The full tables are in RESULTS.md. The strongest non-diagnostic best-coordinate total increases from 1.372556 to 1.705037, 1.965556, and 2.225058 bits per influence as the dimension cap runs from three to six. At six its split is C=0.127621, Cprime=2.097437. The every-coordinate total is 2.345133. There is no stable winning family once root cost is counted.

The total-objective fits use coefficient box [-16,16]; doubling the box for the six nontrivial best-coordinate families changes objectives by at most 1.60568e-09. Best-coordinate optimality outside all finite boxes is not claimed. The root bounds are empirical constraints on census Boolean roots; no universal root bound follows from a fit.

PROOFS.md contains complete arguments. Every bounded dyadic real function is a permitted E-image of a Boolean function. On that node class, an unweighted entropy potential t Abar+s B+u N can work locally with finite C and admissible leaves only when u>=0, t>=u, s>=t+1. Those conditions already give C=0, but force Phi(f)>=B(f) at the root. Separate arguments rule out finite polynomial level-mass potentials, the B1/B2 family, and the level-profile/marginal-entropy family under a universal root budget. All arguments allow adaptive coordinate choice.

The brief's trivial-potential sign is reversed: +B makes (*) an identity; -B requires twice the J payment. I excluded both B gauges and the known H route from candidate conclusions. Raw H and A are retained through the normalized entropy basis plus N.

Every n=6 total-objective fit outside the excluded B diagnostics has an explicit local failure or root-budget failure. For example the best combined fit exceeds its Cprime budget on Boolean parity at 16 variables by 0.642550 bits per influence. The level-entropy fit fails locally on a product of AND_2 gates at 16 variables, at every coordinate. Full nodes, residuals and formulas are in proof_checks.json and PROOFS.md.

Verification passed. audit.py used direct character sums and scalar superset sums, checked 66,324 truth tables, and checked the recursion on every stored edge. verify_fits.py independently evaluated 200 saved fits, with 188,290,100 coordinate checks counting repetition across fits. Its maximum normalized local and root residuals are 1.23833e-10 and 1.62563e-09, below 2e-8 tolerance. proof_checks.py also tested the proved sufficient conditions on 13,553,056 coordinate cases, including the large samples, and materialized a 256-entry Boolean lift. Results are in audit.json, fit_verification.json and proof_checks.json.

The census is 131,322,091 bytes. Maximum recorded process RSS is 1,178,091,520 bytes, below the brief's 3 GiB limit. Numerical processes ran at nice 10 with one thread each and no more than two together. Source scripts, logs, NumPy data, proofs, tables and replay commands are all in this folder. DATA.md explains the schema and reproduction order.

Brain recall helped by surfacing the earlier failed induction and its root-budget issue. The default math-store command found no configured store. Shared-memory and mesh writes were omitted because the fleet rules prohibit writes outside this folder and reserve publishing for the launcher.

Open work: find a different potential with a universal root bound, or another proof of B=O(I). The finite census and the obstruction theorems do not resolve FEI.

Task: “Do the brief fully and carefully” — FEIB06; first recorded local clock 2026-11-10 01:29:26 +04.
