from pathlib import Path
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('For a positive-definite A in the admissible Gamma_3^+ class of Melchionna\'s Theorem 4.3','For a positive-definite A in Gamma_3^+ lying in the fundamental domain corresponding to (x,y) in [0,2]^2, as required in section 4 of Melchionna\'s paper (in particular 0<lambda_1<=1<lambda_2), covered by Theorem 4.3')
s+=r'''
## 10. Computations and hostile-referee audit

Exact implementation: experiments.py uses legal bulk topplings with a deque and a per-site queued flag. A bulk toppling at height h performs floor(h/4) ordinary legal topplings. Four-neighbor boundary edges go to the sink. For point-source experiments the box half-width is ceil(sqrt(n))+3; this choice is NOT used as a theoretical radius estimate. In each run, total final mass equals n and no boundary site toppled, verifying that this finite computation also represents the infinite lattice. Experiments were saved line by line to experiments.jsonl.

Point-source n=256,1024,4096,16384 were counted in the scaled balls (center,radius) ((0,0),.2), ((0,0),.5), and ((.25,.25),.1). For the first ball the four frequencies at n=16384 were approximately (.0820,.1747,.2969,.4464). Across these sizes the frequencies fluctuate; this is no evidence of either convergence or nonconvergence at infinity.

For wired squares with L=9,18,36,72 nonsink vertices per side, the candidate identity was computed as stabilize(6-stabilize(6)), with sitewise constants. It was then checked independently to be idempotent under addition/stabilization and to pass Dhar's burning test with every nonsink site toppling once. The latter proves recurrence, and a recurrent idempotent is the group identity. Thus these finite identities were validated; no continuum limit follows from finitely many values. At L=72 the whole-square frequencies were approximately (.0980,.0324,.3711,.4985). The run took about 19 seconds, with small arrays far below 1 GB.

finite_checks.py verifies the exact one-dimensional configuration and odometer formulas for n=1,...,200, enumerates all 511 nonempty subsets of a 3-by-3 wired square for each of the two recurrent obstruction patterns, and checks the factorial-moment inversion on all 624 nonzero four-tuples of weights in {0,...,4} using Fraction arithmetic. independent_checks.py compares the deque implementation with a synchronous parallel toppling implementation at n=16,64,256,1024, and checks the full discrete Laplacian/odometer identity.

MomentChecks.lean imports only Mathlib.Data.Rat.Defs and Mathlib.Tactic.Ring. It formalizes the factorial-moment inversion and a mass/mean-preserving direction over Q. Final command: lake env lean ~/brain_workers/TRIO_1011/op/C0100/MomentChecks.lean, from ~/lean_verify, timeout 3600 seconds; exit 0. The first run failed because PowerShell had inserted a UTF-8 BOM; Python rewrote the file without it, and the final run succeeded. There is no sorry, axiom declaration, native_decide, or unverified placeholder in the checked file. The algebraic check is kernel-checked; the analytic reductions are handwritten proofs using the cited external theorems, not formalized analytic theorems.

Potential failure points and resolutions:

1. Confusing mean convergence with nonlinear indicator convergence: explicitly blocked by the recurrent checkerboard example and the two missing factorial moments.
2. Counting a separately translated pattern at each site: invalid. A full-period window and double counting are used, so arbitrary phase changes cannot bias the limiting histogram away from the periodic histogram.
3. Summing infinitely many boundary layers: avoided. Section 4 first retains finitely many compact boxes and uses the Jordan remainder; no uniform control of the entire gasket is asserted.
4. Using the wrong toppling cutoff: tracked by the integer polynomial q, with Delta q=1. Pattern-stability witnesses have bound 2; original heights are Delta v+1 and take values 0,...,3.
5. Assuming recurrence of the source odometer globally: false. A finite-domain recurrence comparison is proved from least action only inside a strictly positive odometer region away from the source; Theorem 10's proof uses that local property via its local Lemma 14.
6. Obtaining height equality from odometer equality without neighboring sites: corrected by losing one unit of matching radius before taking Laplacians.
7. Applying pattern stability with a large arbitrary linear slope: Lemma 13 fits the slope by a translated witness with O(R) error, which is negligible compared with N^2.
8. Needing an odometer convergence rate: not necessary for section 5; fixed pattern-radius r and h_n=o(N) suffice. In section 8 the order of limits is n->infinity for fixed rho, then rho->0; no interchange of limits is made.
9. Treating a.e. viscosity Hessians as isolated maximal Hessians: NOT justified; this is the remaining substantive assumption in section 8, rather than a step claimed as proved.
10. Mistaking the bound-2 square-domain theorem for the standard identity: the paper explicitly says Delta u_n+1 is equivalent to all ones, while the identity is equivalent to all zeros. A threshold shift changes the boundary data and does not identify the two equivalence classes.
11. Treating ellipse or Sierpinski results as wired-square results: neither has the requested objects. Section 9 retains the ellipse paper's fundamental-domain and positive-definiteness hypotheses.
12. Treating successful finite stabilization as infinite-lattice stabilization: conservation and zero boundary topplings certify that no sink effect reached the computed point-source pile. Independent legal schedules are checked on small sizes.
13. Claiming numerical trends solve the problem: expressly not done.

## 11. Remaining gaps and final assessment

No complete proof or counterexample for the planar point-source height-fraction question was obtained, and no exact solution in print was located. The most useful reduction is section 8: prove the isolated-maximal-Hessian condition almost everywhere at intermediate limiting densities, or supply some different mechanism that identifies the two missing factorial moments. The existing Apollonian structure theorem and viscosity constraint do not prove this assumption. A positive-measure set of non-maximal Hessians could require a different approach; its existence or absence has not been proved here.

The standard identity on wired square grids has not been identified. The 2020 paper's square model is a different recurrent class; the later ellipse theorem supplies only the special case in section 9. The source asks for understanding that limit without prescribing a unique topology; at minimum its weak-* limit and geometry would need to be established. No claim of doing so is made.

Literature coverage is bounded rather than exhaustive: arXiv and Crossref queries succeeded, and GitHub repositories were screened. OpenAlex source resolution and citation-list retrieval could not be completed because the unauthenticated shared-IP daily quota was exhausted; Semantic Scholar search and citations returned 429. These failures are saved in LITERATURE.md and search_log.json. Thus the correct verdict is PARTIAL, not SOLVED or SOLVED_IN_LITERATURE. This attempt is complete with the above gaps stated for a future continuation.
'''
p.write_text(s,encoding='utf8')
