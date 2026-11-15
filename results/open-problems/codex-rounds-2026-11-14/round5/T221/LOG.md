# T221 round 5 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started: 2026-11-15 08:38:55 +04.

All writes stay in this folder. The task-specific restriction supersedes global instructions to update the shared mesh, checklist and brain; those would write elsewhere. No git or subagents. Startup memory index and compute state were read without mutation. Compute state reported ok / owner_away_open; all programs run single-process under nice -n 15 with OMP_NUM_THREADS=1. The wrapper reports setpriority denied because the inherited process already has priority 20; numerical scripts will assert that priority.

## 1. Literature check (under five minutes)

Used web search queries: `"Rokhlin" "Bernoulli" "2026" entropy` and `"RBS" "Seward" entropy solved`. Opened:

- Brandon Seward, *Krieger's finite generator theorem for actions of countable groups II*, arXiv:1501.03367v4, https://arxiv.org/abs/1501.03367v4 . The abstract states the conditional universal result.
- Zongrui Hu, Leiye Xu, Shuhao Zhang, *Positive Rokhlin Entropy Implies Infinite L^1-Orbit Multiplicity: A Negative Answer to Thouvenot's Question*, arXiv:2607.11549, https://arxiv.org/abs/2607.11549 . The abstract concerns amenable groups and a consequence of positive entropy.
- Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize cosoficity of invariant random subgroups*, arXiv:2511.06586v1, https://arxiv.org/html/2511.06586v1 . The abstract concerns a non-cosofic IRS with an RBS analogue.

No resolution found. This bounded search does not prove absence of later work. No SOLVED_ELSEWHERE.md is warranted.

## 2. Choice recorded before extension

Recheck the preceding finite information inequality and completion lemma, then reconstruct its 103 admissible types independently and recompute the fair-base costs. Extend exactly one piece: add the proposed stationarity constraints on the triple projections (1,a,b), (a,aa,ab), (b,ba,bb), formulate the resulting finite linear program and seek a certified effect or obstruction.

Reason: single-root completions omit compatibility across roots, and these constraints are the smallest proposed next step. The old unrestricted AND cap cannot improve under stationarity alone: the two-point transposition and three-point cyclic models attain its two branches at every root. This fact will be checked and stated even if the LP gives no improvement. Additional defect constraints or a stationary but impossible distribution may reveal what the relaxation misses.

## 3. Independent predecessor recheck passed

Read REPORT.md, LOG.md, PROOF.md and scripts in all three predecessor folders. The chain rule gives nH(p) <= sum_v [H(Z_v)+H(U_v|N_v)] because Z is a function of U and each N_v is a subtuple of Z. On the prefix classes, equality preservation and reflection make each prescribed generator map an injective partial map, which extends by pairing unused sources and targets. Thus the previous main claims hold.

This independent script constructs set partitions by block insertion, tests all pairwise equality equivalences on the generator edges, and computes rational probabilities with entropy as rational combinations of logarithms of primes. All 103 types and 515 predecessor costs matched; maximum floating discrepancy 1.1102230246251565e-15. Exact integer-product comparisons verify every analytic cap, and explicit C2/C3 models attain both cap branches at every root for all five bases.

## 4. First stationarity run

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 stationarity_audit.py`. Exit 0, 1.132 s, 72,859,648 bytes peak RSS, priority 20. Reconstructed all 103 types, matched 515 earlier costs within 1.111e-15; exact cap comparisons passed. The ten triple-stationarity rows plus normalization have exact rank 5. Fair-base LP minimum is log 2 and maximum is (3/2)log 2. All 617 generator assignments on 1--4 points (2421 roots) satisfy the stationarity equations and the information inequality by exact signs.

The first hoped-for counterexample to sufficiency did not appear: stationarity removes the isolated fair-AND cost below log 2. This is potentially a useful positive result for this finite relaxation. Next derive an exact dual certificate, rather than treating the floating solver optimum as a proof of the lower bound.

## 3. Independent predecessor recheck passed

Read REPORT.md, LOG.md, PROOF.md and scripts in all three predecessor folders. The chain rule gives nH(p) <= sum_v [H(Z_v)+H(U_v|N_v)] because Z is a function of U and each N_v is a subtuple of Z. On the prefix classes, equality preservation and reflection make each prescribed generator map an injective partial map, which extends by pairing unused sources and targets. Thus the previous main claims hold.

This independent script constructs set partitions by block insertion, tests all pairwise equality equivalences on the generator edges, and computes rational probabilities with entropy as rational combinations of logarithms of primes. All 103 types and 515 predecessor costs matched; maximum floating discrepancy 1.1102230246251565e-15. Exact integer-product comparisons verify every analytic cap, and explicit C2/C3 models attain both cap branches at every root for all five bases.

## 5. Exact dual and missing compatibility

The second full run of the same command passed in 1.155 s with 73,089,024 bytes peak RSS. Exact certificate: for each admissible type pi,

    C_pi >= log 2 + alpha A_pi + beta B_pi,

where A is root-minus-a-child frequency of triple pattern (0,1,1), B is root-minus-b-child frequency of (0,0,1),

    alpha = (1/2)log 2 -(3/4)log 3 -(7/16)log 7 +(11/16)log 11,
    beta  = -log 2 -(5/8)log 5 +(7/8)log 7.

All 103 inequalities have exact nonnegative signs; three are exact equalities. The coefficients are fixed exact log combinations reconstructed from tight types, not rounded solver duals. Stationarity cancels A and B. The one-point model attains log 2; the two-point model attains (3/2)log 2. This certifies both extrema.

A limitation is explicit: the singleton distribution on pi=(0,1,2,3,0,4,5) is admissible and satisfies all triple-stationarity constraints. But it asserts ab=e and ba!=e at every root, contradicting equality of fixed-point counts of the conjugate permutations T_ab and T_ba. Thus triple stationarity is not sufficient for realizability, even though its AND entropy minimum is correct. This singleton also satisfies the AND information inequality (cost about 0.917523 > log 2).

The 617 small finite models separately satisfy both stationarity and the missing conjugacy constraint. Next: write the proof with the exact table certificate and rederive the laws by inclusion-exclusion in an independent standard-library verifier.

## 6. Independent verification and proof audit

Wrote PROOF.md with the exact finite certificate, the rank-four argument, both attainable extrema and the stationary-but-impossible singleton. The first draft reused Q_0 for both root and output coordinate sets in the inclusion-exclusion formula; corrected the notation to Q_R,Q_E,Q_A,Q_B. No mathematical claim changed.

Independent command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_certificate.py`. Final exit 0. It re-enumerates types by restricted-growth strings rather than block insertion, tests partial maps rather than pairwise equalities, and computes laws by inclusion-exclusion rather than class-label assignments. It checks each stationarity column from the triple restrictions, each exact slack, all six grouped minima, both attainable extrema and the rank-four determinant by its permutation expansion.

Final output: 103 types; 515 costs; maximum earlier-cost discrepancy 2.220446049250313e-16; 103 exact nonnegative slacks, 3 zero; rank 4; minor determinant 1; 17137664 bytes RSS; 0.200 seconds; priority 20.

Second derivations of load-bearing quantities: rank at most four follows from four identically zero rows and two row sums; a determinant-one minor gives rank at least four. The upper entropy cap follows directly by conditioning on the root, independently of the LP. The lower bound follows from all 103 exact dual inequalities, independently of the solver optimum. The alpha tight law has joint counts (7,1,4,3,1)/16 and name counts (11,1,3,1)/16; the beta tight law gives h(1/8)+(5/8)h(1/5). These reproduce the exact coefficients. The singleton counterexample was also realized at one root by explicit six-point permutations, while its global obstruction follows from conjugacy.

Cases challenged: repeated output names and coordinate sets; fully collapsed and fully distinct types; zero-mass conditioning events; degenerate bases p=0,1; right versus left word order; stationarity versus realizability; rounded optimization versus exact certificate signs. Inclusion-exclusion handles repeated sets without assuming independence of outputs. No positive-gap group example is inferred from a low-cost individual rooted type. No check failed.

## 7. Final report

Wrote REPORT.md with a PARTIAL verdict. The new checkable result is the stationarity certificate and its exact limitation. RBS remains open in this session. The next step is the explicit conjugacy row (14), followed by other visible word-conjugacy tests. No earlier folder, git state, shared memory, external application or account was mutated.

Final artifact read-back passed: required verdict header, balanced mathematical delimiters, 15 consecutive equation tags, matching 103-row tables, three exact equality cases, determinant-one rank witness. The independent formulas sum_(n=1)^4 (n!)^2=617 and sum_(n=1)^4 n(n!)^2=2421 reproduce the exhaustive model and root counts.
