VERDICT: COMPUTED edge-diversion stochastic monotonicity for all 256 directed cuts of the 2-by-2 square at lambda=1.

Every redirection of one remaining directed internal edge to the sink weakly decreases the stationary total sleeping population in stochastic order. The computation covers 1024 single-edge comparisons and all 4096 associated tail inequalities. There are 1792 zero differences and 2304 positive differences. No counterexample occurs in this family.

The jump kernel retains four equally likely lattice directions at each vertex. An edge redirected to the sink retains its original probability 1/4 conditional on a jump. All vertices have at least two sink directions. Driving adds a particle at a uniformly chosen vertex and stabilizes.

The comparison also implies a finite superadditivity case: the unmodified square stochastically dominates the independent sum of the stationary populations of its two isolated rows. Each row has law (99,216,112)/427 on populations 0,1,2. All four tail inequalities in this particular comparison are strict.

For the unmodified square the stationary mean population is 205775624/96025977, giving density 51443906/96025977. These are finite-volume quantities; no bound on the infinite-volume critical density is inferred.

## Files and reproduction

- `PROOF.md`: model, finite equations, absorption and stationary-law identification, and hand derivation of the two-site check.
- `exact_square.py`: exhaustive exact solver and independent continuous-time audit.
- `verify_square_data.py`: standard-library audit of saved data, stochastic orders, symmetries and hand-derived cases.
- `square_data.json`: all 256 exact population laws, all 256 independent full stable-configuration laws, and comparison data.
- `square_run.txt`, `square_verify.txt`: captured command output.
- `LOG.md`: choices, commands, outputs and failed launch guard.

Run in this folder with Python 3 and SymPy installed:

```
OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --audit-all --output square_data.json > square_run.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 verify_square_data.py > square_verify.txt 2>&1
```

The exhaustive run completed in 119.715 seconds and used 71,401,472 bytes peak RSS. It ran at inherited nice 20 with one interpreter and thread limits set to one. macOS rejects the additional relative `nice` adjustment and prints a warning; the script verifies that its actual priority is already at least 15.

## Checks and failures

The first solver uses a fixed legal instruction schedule and fraction-free integer elimination. Every law was independently rederived using the actual continuous-time rates and a separate Python `Fraction` Gaussian elimination. Both solvers verify their exact equation residuals. The continuous-time audit checks invariance of the complete stable-configuration law under addition at each of four vertices, yielding 1024 stationarity checks. A finite irreducibility argument in `PROOF.md` identifies this law uniquely for uniform driving.

The data verifier independently enumerates the mask comparisons through lower cumulative probabilities, checks 2048 dihedral relabelings, and matches two hand-derived cases: all-sink Binomial(4,1/2), and the independent two-row law. In particular, asymmetric cuts, the extreme kernels and every tail threshold were included.

An initial attempt to set a 900 MB address-space limit failed before calculation: macOS reported an infinite hard limit but rejected lowering the soft limit. The final script retains the CPU and wall-clock limits, bounds state counts, and measures RSS. Actual memory stayed well below the requested limit. No mathematical counterexample was found. A stronger claim that all tail inequalities are strict fails on this data.

## Literature and scope

The literature search finished within the ten-minute allowance. No later solution of the density conjecture on Z^d for d>=2 was found. All papers cited here were opened. The recent [Tobias Johnson, Matthew Junge, Josh Meisel, *Stationary activated random walk: regularity, heavy tails, and remixing*, arXiv:2609.31843](https://arxiv.org/abs/2609.31843) strengthens one-dimensional stationary regularity, and the [Matthew Junge, Harley Kaufman, Josh Meisel complete-graph result, arXiv:2604.04747](https://arxiv.org/abs/2604.04747) concerns another graph sequence. Both precede the supplied November status check.

The precise original density conjecture equates the limiting mean stationary density in growing killed boxes with the infinite-volume fixed-energy fixation threshold. [Christopher Hoffman, Tobias Johnson, Matthew Junge, *The density conjecture for activated random walk*, arXiv:2406.01731v2](https://arxiv.org/abs/2406.01731) also identifies the one-dimensional point-source and cycle thresholds. For the point source, the density is source mass divided by the number of sites visited during stabilization. Using just the final occupied support would give density one, since a stable occupied site contains exactly one sleeper.

This finite calculation addresses an explicit proposed ingredient: whether diverting a directed edge to the sink decreases the final population. That question is raised in Section 2.5 of [Nicolas Forien, *A new proof of superadditivity and of the density conjecture for Activated Random Walks on the line*, arXiv:2502.02579v2](https://arxiv.org/html/2502.02579v2). The search did not establish whether this particular finite case has appeared previously.

The result gives no conclusion for other sleep rates or larger boxes. Even a general superadditivity theorem would still require an argument identifying its density limit with the fixation threshold. The next useful step is to derive symbolic laws on this same four-vertex graph as functions of lambda, and test whether every tail difference has a nonnegative polynomial numerator for lambda>0. The current exact rational system is a small starting instance for that calculation.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 20:50 Asia/Tbilisi.
