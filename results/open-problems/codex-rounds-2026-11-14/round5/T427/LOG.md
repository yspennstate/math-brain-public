# T427 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session date: 15 November 2026, Asia/Tbilisi; exact clock to be recorded below.

## Orientation and literature check

Read the initial and round 3 REPORT.md and LOG.md, and round 4 PROOF.md. The first folder has no PROOF.md or mathematical scripts. Remaining round 3/4 scripts and logs are being read before doing new mathematics. Read ~/.claude/brain_startup.md and the compute state: status ok, mode owner_away_open. No heavy computation is planned. The explicit instruction to write only in this folder overrides global brain/checklist/mesh commands that would write elsewhere; none are run. No git, subagents, or outside edits.

Initial read-only shell commands used pwd, rg --files, ls and cat. Subsequent mathematical programs will run under env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15, check actual niceness, impose a short CPU limit, and use small memory.

Web search tool queries: `"Random Matching Between Distinct Distributions in Two Dimensions" Xu`; `"random matching" "second-order" semidiscrete 2026 constant`. Opened https://arxiv.org/abs/2610.40509 and https://arxiv.org/html/2610.40509v1, Yunzong Xu, *Random matching between distinct distributions in two dimensions*. The record still shows the original 29 October 2026 version. This is the same preprint already identified in all three earlier folders, not a new resolution. No update changing that picture surfaced. Literature search is closed, within five minutes; further opening of that paper will be proof inspection.

The intended next step is the round 4 recommendation: audit the equal-mass semidiscrete-to-smoothing reduction, starting with a fresh derivation of its source-change identity and error. Before choosing its precise scope, recheck the preceding subdivision argument and its exponent computation independently.

## 09:17–09:20 +04 — previous result rechecked; ONE extension chosen

First saved clock: 15 November 2026, 09:17:31 +04 (05:17:31 UTC). Read all required earlier mathematical files and scripts. Round 3's log was read in two portions; the first folder has no proof or scripts. No earlier file was edited.

Rechecked round 4's load-bearing estimates directly. The sample covariance is applied before restricting to the concentration event. The retained reverse allocations preserve each cell's actual mass, and the cutoff kills normal flux. The rescaling is n(k/n)m^(-2)(d_k/k), followed by summation over m^2 cells, hence exactly E d_K(m^2 t), including K=0. Independently minimize the two squared-repair terms r and r^(-4) A n^(-1/6)log(en): equality gives r=n^(-1/30)log(en)^(1/5) up to A^(1/5), and the cost cross term is sqrt(r)log(en)=n^(-1/60)log(en)^(11/10). The global/cell heat discrepancy contributes n^(1/2)t^(3/4)sqrt(log(en))=n^(-1/8)sqrt(log(en)), which is smaller. The short-edge interpolation in the potential estimate has density at most C(1-u)^(-2); its square root is canceled by the Taylor weight 1-u. No flaw was found in the flat equal-mass argument; its stated bound holds under this recheck.

Rerun command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T427/check_scaling.py
```

Exit 0. Relevant output: actual niceness 20; delta^2 has exponents (-1/6,1), r (-1/30,1/5), repair (-1/60,11/10), global heat cost comparison (-1/8,1/2); reassignment coefficient 169/1000 < 1. All independent balances and strict exponent margins passed. The wrapper prints `nice: setpriority: Operation not permitted` because inherited niceness is already 20. The process guard confirms the actual priority. Peak RSS and exact output will be recorded after the tool response.

Chosen ONE extension: give a self-contained proof of the equal-mass square/torus semidiscrete-to-smoothing reduction, including its quantitative linearization error. This is the missing piece explicitly named by round 4. It audits Proposition 3.1 of the existing preprint, not a new claim of solving the finite-constant problem. Use the flat map S(x)=x-grad f(x), whose source density is det(I-D^2 f), instead of the paper's flow. In two dimensions its density error relative to 1-Delta f is exactly det(D^2 f), a divergence with H^(-1) norm at most C||D^2 f||_infinity ||grad f||_2. Then prove the heat-potential Hessian concentration and rough cost bounds directly from Fourier/cosine series. This gives an independent route to the needed estimate without any matching asymptotic theorem. No value of beta_sd or c_square will be inferred.

The rerun's peak RSS was 13,647,872 bytes, and tool wall time was below 0.1 seconds. All required prior reports, proofs, logs and scripts have now been read.

## Deterministic reduction derived

Opened Appendix B.1–B.2.2 and Proposition 3.1 of Xu's existing paper using the web tool. The target estimate is the flat equal-mass specialization already stated there; the work here is an independent proof audit of that claim.

For H=D^2f, qhat=det(I-H)=q+div R, where q=1-Delta f and R=(cof H)grad f/2. The cofactor divergence vanishes. On a square face the Neumann condition forces both the normal derivative and its tangential derivative to vanish, hence R has zero normal component. Thus ||qhat-q||_-1 <= (gamma/2)sqrt(E), gamma=||H||_op,infinity. The source map S=I-grad f pushes qhat dx exactly to dx. For the square its coordinate bounds and strict convexity give a bijection of Q; for the torus use the periodic lift.

The pointwise quadratic-cost comparison is especially simple on the torus: apply Taylor's formula to every lattice lift h=y-x+k, then take the minimum. The term 2(f(y)-f(x))+|grad f(x)|^2 is independent of k, so the remainder is bounded by gamma d(x,y)^2 even at the cut locus. This avoids an unproved shortest-edge assumption. Integrating against arbitrary couplings and correcting qhat to q gives |L-D-2nu(f)+E| <= C gamma(L+E).

For the stochastic application, direct cosine/Fourier counting yields second-derivative kernel envelope and variance C/t, and third derivative Ct^(-3/2). Bernstein plus a net gives gamma <= K sqrt(log(en)/(nt)) except with probability Cn^(-12). The rough cost n E L <= C log(en) follows from smoothing at 1/n and the H^(-1) action estimate with constant background density 1. These estimates are independent of the matching theorem being audited.

No failure found so far. The proof and a small exact-arithmetic check of the determinant, normal flux, spectral moments and rate are being saved next.

## Proof saved; first verifier launch stopped at its resource guard

Saved PROOF.md with the full deterministic comparison, direct heat-series estimates, Bernstein concentration, an independent rough cost bound, and the exact spectral expectation. The proof also establishes an expected absolute remainder bound, before averaging the random spectral term. At t=n^(-5/6) its error is O(n^(-1/12)log(en)^(3/2)).

Added check_reduction.py using only Python's standard library and exact rational arithmetic. First command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_reduction.py
```

It exited 1 before any mathematical computation: setting RLIMIT_DATA to 256 MB raised `ValueError: current limit exceeds maximum limit`. An initial inference that the inherited hard limit was lower was wrong. The second attempt, using min(256 MB, inherited hard limit), failed at the same guard. A tiny read-only diagnostic under the same thread/priority wrapper printed `RLIMIT_DATA (9223372036854775807, 9223372036854775807)`, equal to this platform's RLIM_INFINITY; RSS 11,730,944 bytes and actual niceness 20. This platform rejects the attempted data-limit change despite the infinite reported limit. Removed that optional cap: the script uses only bounded tiny polynomial dictionaries and at most 64 enumerated samples at a time, and checks peak RSS below 1 GB. CPU limit remains 60 seconds. Neither failed launch reached a mathematical assertion.

## Exact verifier passed

Ran the same check_reduction.py command again after removing the unsupported optional data-limit setting. Exit 0. Complete output:

```text
nice: setpriority: Operation not permitted
niceness=20; exact rational arithmetic; one thread
Hessian operator-norm upper bound for test polynomial: 31/1250
PASS: Jacobian = 1-Delta f+det Hess f; divergence factor 1/2; independent trace identity.
PASS: Neumann condition, mixed face derivatives, normal flux, and Jacobian mass 1.
PASS: both integration-by-parts identities, including the sign of the source correction.
PASS: square and torus pointwise inequalities for 36 ordered pairs each.
      Pairs include seam crossings and cut-locus ties.
Enumerated spectral target 2F-F_2 = 947/1800
PASS: exhaustive sample expectations for n=1,2,3 agree with the spectral identity.
PASS: previous repair rate (-1/60,11/10); new reduction rate (-1/12,3/2).
Peak resident memory: 14139392 bytes
Elapsed time: 0.015 seconds
```

The polynomial is f=[x^2(1-x)^2 y^2(1-y)^2-1/900]/10000. Its exact Hessian row-sum bound is 31/1250<1/8. The script computes the Jacobian directly as a two by two determinant, checks its discrepancy both by cofactor differentiation and by the trace identity, integrates every polynomial exactly, and tests the pointwise transport inequalities using rational coordinates. Its periodic extension is C^2; this suffices for the tested Taylor inequalities. The seam and cut-locus tests are finite checks supporting the written all-lifts proof, not a replacement for that proof. The spectral test uses three orthonormal zero-mean functions on four states; exhaustive enumeration for n=1,2,3 yields the independently specified value 947/1800 for n E(2nu(f)-E). All arithmetic is rational; no rounding or interval issue is present.

## Adversarial proof audit

Re-derived det(H)=div[(Delta f)grad f-grad(|grad f|^2/2)]/2. The third derivatives cancel, leaving ((Delta f)^2-tr(H^2))/2. This independently checks the discrepancy sign and the factor 1/2. Checked the two reference cases nu=dx and nu=qdx: (5) gives respectively -D+E and L-E, consistent with the usual quadratic-energy approximation. The heat displacement factor 4t is both the trace of covariance 2tI and the solution of d/dt E|Z_t|^2=Delta|x|^2=4.

The torus proof minimizes over all lattice lifts before selecting a cost-minimizing coupling. It remains valid for cut-locus ties, without any short-edge assumption. The square source map is onto by a strictly convex minimization with inward boundary derivatives; face preservation alone would not have justified onto. The determinant flux vanishes face by face, including its limiting values at corners. Singular targets are harmless because the proof transports arbitrary couplings through a source diffeomorphism; it never differentiates an optimal allocation.

The Hessian variance is estimated by orthogonality, giving C/t rather than the squared envelope C/t^2. The net has at most C delta^(-2)t^(-3) points. In the entire allowed time range its prefactor is <=Cn^3; exponential suppression can therefore be chosen uniformly. The covariance identities are never conditioned on the good event. On its complement the deterministic remainder is O(log(en)), so its scaled expectation is O(n^(-11)log(en)); neither the source comparison nor a positive lower bound on qhat is used there.

The quantitative reduction error has a second derivation: delta log(en), with delta^2=K^2 log(en)/(nt), is exactly K sqrt(log(en)^3/(nt)). At t=n^(-5/6) this is n^(-1/12)log(en)^(3/2). The correction moment is 2F(t)-F(2t), checked both by independent sample enumeration and by the continuum eigenfunction covariance calculation. The combination of logarithms is 2log(1/t)-log(1/(2t))=log(2/t). No factor from the two-sample problem appears.

No mathematical counterexample was found. The only failed executions were the two optional resource-limit guards described above. The unknown finite constant is untouched: the remaining missing audit is the sample-size/time de-randomization and convergence argument, not this reduction.

## 09:25 +04 — report saved

Wrote REPORT.md with the required verdict, the precise reduction and rate, commands, failed resource-limit attempts, scope limitations and handoff. A final read-only governor check still reports status ok, mode owner_away_open. The only mathematical workload used 14.2 MB and 0.015 seconds; no heavy work, background processes, installations, git, outside writes or subagents were used. No new SOLVED_ELSEWHERE.md is appropriate: the relevant preprint is exactly the one already known in all earlier reports, and its remaining proof is being audited rather than reported as a new discovery.

## Final file validation

Ran an inline read-only Python validator under the same OMP/BLAS environment, nice -n 15, python3 -B wrapper. It checked actual niceness >=15, imposed a 30-second CPU limit, asserted the exact working directory, checked trailing newlines and the exact verdict, parsed the verifier with ast.parse, checked equation labels 1–30 and balanced display/inline math delimiters, and checked absence of __pycache__. Exit 0; wall time below 0.1 seconds. Output before this append:

```text
nice: setpriority: Operation not permitted
PROOF.md: 450 lines; 16792 bytes
LOG.md: 93 lines; 12848 bytes
REPORT.md: 32 lines; 3686 bytes
check_reduction.py: 172 lines; 7269 bytes
PASS: required deliverables, exact verdict, equation labels 1-30, balanced math delimiters, script syntax, no bytecode files.
```

Final audit conclusion: the independently derived flat reduction has a complete proof and exact algebraic checks. The previous subdivision estimate survives its recheck. This does not certify the preprint's separate sample-size convergence argument or assign any numerical matching constant.
