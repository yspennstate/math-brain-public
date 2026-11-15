# T090 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 08:12:26 +04 (04:12:26 UTC). Prompt receipt time unavailable.

## Orientation and bounded status check

Read the reports and logs in the original, round-3, and round-4 folders, the round-3 and round-4 proofs, and both Python scripts. The original folder has no PROOF.md or computation script. Earlier folders are read-only. Read the brain navigation index and compute state without running utilities that write external logs. The task-specific restriction to this folder supersedes mesh, checklist, and brain mutations. No git, subagents, or external messages.

The compute governor reported `status: ok`, `mode: owner_away_open`, CPU 75.4%, free memory 33%. Only small standard-library calculations are planned, one thread, with the requested nice invocation. Initial orientation commands were file reads; numerical programs will use OMP_NUM_THREADS=1 and nice -n 15.

Status search began around 08:12 +04 and concluded within five minutes. Queries: `"2+1" KPZ strong coupling rigorous exponents 2026 proof`; `"2609.15832" KPZ`; `"2412.10311"`. Opened https://arxiv.org/abs/2610.31614, https://arxiv.org/abs/2609.15832, and https://arxiv.org/abs/2412.10311. No newer solution of the fixed-coupling problem was found. This bounded search is not an exhaustive absence claim. The critical-process paper is already covered by earlier work and does not settle the question here.

Primary sources actually opened:

- Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie, and Nikos Zygouras, *The Critical 2D KPZ Process*, arXiv:2610.31614v1 (22 October 2026), https://arxiv.org/abs/2610.31614.
- Hindy Drillick, Jonathan Hou, and Shalin Parekh, *A universality result for the critical 2d stochastic heat flow*, arXiv:2609.15832, https://arxiv.org/abs/2609.15832.
- Francesco Caravenna, Rongfeng Sun, and Nikos Zygouras, *The Critical 2d Stochastic Heat Flow and Related Models*, arXiv:2412.10311v3, https://arxiv.org/abs/2412.10311.

## Independent recheck before extension

The round-4 free resolvent is correctly normalized: the generator of the difference process is Delta, so G_E(r)=(4 pi)^(-1) integral exp(-u-E*r*r/(4u)) du/u. Splitting at sqrt(a) gives the global remainder bound used there. With X,Y distributed as R_s, |X-Y|^2/(8s) is unit exponential. Therefore a_s=E[(log(2)-Euler-log|X-Y|)/(2 pi)]=-[log(2s)+Euler]/(4 pi). The scalar Birman–Schwinger crossing gives log E=-4*pi/g+4*pi*a_s+O(g), recovering the claimed prefactor exp(-Euler)/(2s). The positive-eigenfunction lower bound and Duhamel/L2 upper bound correctly identify the spectral energy with the pointwise moment growth rate, including the non-L2 constant initial condition. No error found so far; rerun of the preceding audit follows.

## Chosen extension, recorded before carrying it out

Choose exactly the next step named in round 4: retain the first block-elimination correction c_s=||(I-P)A v||_2^2 and evaluate it for the Gaussian. Target an expansion gamma(b,s)=[exp(-Euler)/(2s)] exp(-4*pi/b^2) [1+C*b^2+O(b^4)] with explicit C, and the same first correction to the renewal lower-endpoint ratio. This quantifies the first gap above that lower bound and stays within the established annealed second-moment observable.

Audit plan: compute c_s through the variance of the radial Gaussian logarithmic potential, independently derive its integral through a second representation, and compare with small-coupling zero-energy radial ODE data. The ODE is a diagnostic, not a finite-coupling positive-energy eigenvalue solver. Check the sign, diffusion convention, uniformity in s, and that exponentially small resolvent errors cannot contaminate a power-series correction.

## Earlier audit rerun: holds

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T090/check_prefactor.py
```

Output: five covariance-scale checks passed; maximum log-distance discrepancy 1.110e-14; s=1 prefactor 0.28072974178344. Direct heat-resolvent quadrature recovered -2*Euler with residual -8.660e-15 at a=1e-30. All zero-energy ODE diagnostics passed, largest step discrepancy 6.040e-13. Runtime 0.112 s, peak RSS 12.656 MiB. CPU limit 60 s installed; Darwin rejected address-space limiting. The earlier main result holds under independent algebraic rederivation and rerun.

`nice` printed `setpriority: Operation not permitted`. A separate requested-wrapper run of `python3 -B -c 'import os; print("effective process niceness:", os.getpriority(os.PRIO_PROCESS, 0))'` returned 20. Thus the process already inherits niceness 20, more polite than 15; the warning is not evidence of ordinary priority.

## Correction term derived

Write ell=-log(E)/(4*pi), Q=I-P, and c_s=||QAv||^2. The exact block equation and a norm-convergent inverse expansion give mu(E)=ell+a_s+c_s/ell+O_s(ell^(-2))+O_s(sqrt(E)). At mu(E)=1/g, ell=1/g+O(1), so ell=1/g-a_s-c_s*g+O_s(g^2). Hence log gamma=-4*pi/g+4*pi*a_s+4*pi*c_s*g+O_s(g^2).

For L_s(x)=integral R_s(y) log|x-y| dy and u=|x|^2/(4s), angular averaging gives L_s(x)=[log(4s)-Euler+Ein(u)]/2, Ein(u)=integral_0^1 (1-exp(-tu)) dt/t. For U unit exponential, E Ein(U)=log 2 and c_s=Var(Ein(U))/(16*pi^2). The scale-dependent additive constant cancels.

The covariance integral is Var(Ein(U))=integral_[0,1]^2 dt dq/[(1+t+q)(1+t)(1+q)]. Substitute x=t/(1+t), y=q/(1+q). It becomes integral_[0,1/2]^2 dx dy/(1-xy)=sum_(n>=1) 4^(-n)/n^2=Li_2(1/4). Thus C=4*pi*c_s=Li_2(1/4)/(4*pi)>0. This supplies the candidate first relative correction b^2*C. Full proof and independent numerical audit are being saved next.

## New computation saved and passed

Created check_correction.py (Python standard library only; no threads or subprocesses). Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_correction.py
```

Relevant complete output:

```text
soft limit CPU seconds: 60
soft limit address space unavailable: current limit exceeds maximum limit
effective niceness: 20
Ein vs defining integral: 9 cases PASS; max error 3.109e-15
E Ein(U): 0.693147180559947; log(2): 0.693147180559945
Var Ein(U), radial quadrature: 0.267652639082734
covariance double integral:    0.267652639082733
Li_2(1/4), positive series:    0.267652639082733
c=||QAv||^2: 0.001694930137304
relative/log correction C=4*pi*c: 0.021299120270804
Gaussian logarithmic-potential variance: 5 scale checks PASS
zero-energy ODE diagnostic only; adjusted residual / g -> C
g        residual/g         error from C       step-halving difference
0.5      0.021568309788  2.692e-04 4.121e-13
0.25     0.021432774175  1.337e-04 6.480e-12
0.125    0.021365714515  6.659e-05 9.095e-13
0.0625   0.021332359473  3.324e-05 9.004e-11
0.03125  0.021315725598  1.661e-05 1.091e-11
last two couplings, linear extrapolation: 0.021299091723
extrapolation error from C: -2.855e-08
elapsed seconds: 0.245; peak RSS MiB: 12.031
PASS: floating-point audits; the theorem does not depend on them
```

The nice wrapper again emitted the denied incremental-priority warning, but the script directly confirmed niceness 20. Runtime and storage are far below the task bounds. The three variance calculations differ by about 1e-15. The radial Ein routine was separately checked against its defining integral, including zero, both sides of its branch point at 1, and u=80. All quoted decimals are floating-point checks, not certified enclosures. No numerical failure occurred.

The ODE uses w=log(r^2/(4s)), F''=-[g/(4*pi)] exp(w-exp(w)) F, and extracts F=A+B*w at the outer cutoff. It prints [A/B+4*pi/g-Euler+log 2]/g. This diagnostic approaches C and does not substitute a zero-energy scattering calculation for an actual finite-g eigenvalue solve. The proof uses only the resolvent expansion.

## Complete proof and independent algebraic audits

Saved PROOF.md with the global free-resolvent estimate, spectral/pointwise rate equality, retained block term, radial covariance evaluation, uniform spatial scaling, renewal-root comparison, and general-diffusion normalization. The theorem is

    gamma(b,s) = exp(-Euler)/(2s) * exp(-4*pi/b^2)
                 * [1 + Li_2(1/4)*b^2/(4*pi) + O(b^4)].

The same bracket is the ratio to x_(b^2)/(2s). No height exponent is asserted.

An independent analytic variance derivation uses Laguerre polynomials with generating function (1-z)^(-1) exp(-uz/(1-z)). Direct integration of two generating functions proves orthonormality in L2(exp(-u)du). Integrating the single generating function from z=0 to z=1/2 gives log 2-Ein(u)=sum_(n>=1) L_n(u)/(n*2^n). Its squared norm is sum 4^(-n)/n^2. This rederives the load-bearing constant without the covariance change of variables.

An independent algebraic check expands the rank-one eigenvalue equation at the crossing directly in g: ell=1/[g*<v,(I-gD_E)^(-1)v>]. The Neumann series gives ell=1/g-a_s+g*(a_s^2-<v,A^2v>)+O(g^2)=1/g-a_s-c_s*g+O(g^2), agreeing with block elimination and fixing the positive sign in log gamma.

## Attempts to break the result

1. Rechecked the diffusion coefficient from both Itô's moment PDE and the variance of the difference Brownian motion. The normalized equation has pair generator Delta and exponent -4*pi/g. For SHE diffusion d, time change gives correction Li_2(1/4)*b^2/(8*pi*d) and exponent -8*pi*d/b^2. At d=1/2 these reduce to the theorem; at d=1 they give the prompt's normalization.
2. Recomputed a_s using the Gaussian difference distribution and using the radial potential plus E Ein(U)=log 2. Both give -[log(2s)+Euler]/(4*pi). Recomputed c_s using the covariance integral and the orthogonal-series identity. Both give Li_2(1/4)/(16*pi^2), positive. The direct Neumann calculation checks that this positive variance raises log gamma; there is no missing minus sign or factor of two.
3. Checked all perturbative orders: the inverse error in the block calculation is O(ell^(-2)), and at the crossing ell=1/g+O(1). The free-resolvent error O(sqrt(E)) is exponentially small, hence smaller than O(g^2). Exponentiating adds only O(g^2) to the stated bracket. The renewal root has an exponentially small relative error, so it introduces no additional order-g term in the ratio.
4. The additive log(s) term in the Gaussian logarithmic potential vanishes under Q. Although intermediate fixed-s operator bounds depend on s, exact Brownian scaling transports the s=1 relative estimate to every s>0 with identical error constants. This avoids an unjustified claim of uniform operator estimates as s tends to zero or infinity.
5. Checked zero and negative b, the excluded s=0 boundary, the non-L2 constant initial condition, Gaussian tails, and the logarithmic diagonal. Every term used is integrable and the positive-energy threshold is attained. The result makes no assertion for a different covariance or nonflat initial data.
6. Numerical radial integration stops at u=80. Since Ein(u)<=u, the omitted first/second-moment tails are bounded by elementary polynomial times exp(-80) integrals, below 2e-31 for the centered-square tail used here. No such cutoff enters the proof. ODE endpoint and step errors are floating-point diagnostics, not interval estimates. No finite-coupling eigenvalue or height fluctuation was inferred from them.

No counterexample or gap was found in the stated expansion. The literature search does not establish wider novelty. The connection from these annealed moments to typical centered log Z remains missing.

## Read and resource details

Some initial batched read output was truncated; exact ranges from the round-3 proof and round-4 log were subsequently reread. An attempted startup-memory filename was absent; the existing MEMORY.md and brain navigation index were read instead. Those read failures changed no files. Every new file and modification remains in this folder. State-writing mesh/checklist/recall tools were not invoked, and no git or subagent was used.

The only numerical programs run were the earlier prefactor script, the niceness query, and check_correction.py. Both audits ran below one second and below 13 MiB peak RSS, single-threaded under inherited niceness 20, with a 60-second CPU limit. Darwin address-space limiting was unavailable. No heavy workload was started.

## Report saved

Created REPORT.md with the required first-line verdict, the new coefficient and O(b^4) relative remainder, reproduction commands, numerical evidence, failed resource-limit operations, unresolved scope, and a concrete possible next coefficient. No SOLVED_ELSEWHERE.md was created because the stated fixed-coupling problem was not found solved. All task outputs are local: REPORT.md, PROOF.md, LOG.md, and check_correction.py.

## Final artifact check

At 15 November 2026, 08:20:33 +04, ran `OMP_NUM_THREADS=1 nice -n 15 head -1 REPORT.md`, `OMP_NUM_THREADS=1 nice -n 15 wc -lc REPORT.md PROOF.md LOG.md check_correction.py`, and targeted `rg` checks for the coefficient, remainder, failures, limitations, next worker, and task clock. The exact first line is `VERDICT: PROVED first relative correction to the Gaussian second-moment weak-coupling asymptotic`. All four files were nonempty, about 38 KB in total before this final entry; the proof has 31 numbered equations. The selected continuation is proved and independently checked. The original fixed-coupling KPZ exponent and height-law problem remains unresolved here.
