# T090 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 10:44:25 +04 (06:44:25 UTC); prompt receipt time unavailable.

## Orientation and bounded literature check

Read the original and rounds 3–5 reports, logs, proofs and Python audits (the original folder has no proof or script). Some batched output was truncated; the affected material is being reread in smaller pieces. Earlier folders are read-only. Read the existing memory index and brain navigation index. The restriction to writes inside this folder supersedes the global state-writing mesh, checklist, recall and memory commands. No git or subagents.

The compute governor reported status warn, mode owner_away_open, CPU 100.1%, free memory 55%. Only tiny single-threaded standard-library audits are planned, with the requested nice wrapper. No simulation or heavy computation.

The bounded status search used the web search tool with `"KPZ" "2+1" "2026" rigorous exponents strong coupling`, `"2610.31614"`, and `"two-dimensional KPZ" "November" "2026"`. It began at about 10:44 +04 and ended within five minutes. Opened these primary arXiv pages:

- Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie, and Nikos Zygouras, *The Critical 2D KPZ Process*, arXiv:2610.31614, https://arxiv.org/abs/2610.31614. This is the already identified critical, vanishing-coupling process, not a fixed-coupling growth-exponent theorem.
- Xue-Mei Li and Te-Chun Wang, *Near-optimal bounds for the critical 2d SHF and the delta-Bose gas*, arXiv:2611.03191 (submitted 2 November 2026), https://arxiv.org/abs/2611.03191. The abstract gives bounds on high moments of the critical heat flow and associated ground-state energies; it does not settle the height exponents in T090.
- Hindy Drillick, Jonathan Hou, and Shalin Parekh, *A universality result for the critical 2d stochastic heat flow*, arXiv:2609.15832, https://arxiv.org/abs/2609.15832. This also concerns critical heat-flow convergence.

No solution of the stated fixed-coupling problem was found. This is a bounded search, not an exhaustive absence claim. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of round 5

Write g=b^2, v=sqrt(R_s), P=|v><v|, Q=I-P and ell=-log(E)/(4*pi). The Gaussian free-resolvent finite part is A(x,y)=v(x)v(y)[log(2)-Euler-log|x-y|]/(2*pi). At the crossing mu(E)=1/g, exact block elimination gives ell=1/g-a_s-g*||QAv||^2+O(g^2), with a_s=-[log(2s)+Euler]/(4*pi). Thus the sign in the preceding logarithmic correction is positive.

Independently, angular averaging gives (QAv)/v=[log(2)-Ein(u)]/(4*pi), u=|x|^2/(4s). Under R_s, u is unit exponential. Expanding Ein by its defining Laplace integral gives Var(Ein(U))=integral_[0,1/2]^2 (1-xy)^(-1) dx dy=Li_2(1/4). Therefore the earlier coefficient Li_2(1/4)/(4*pi) holds by rederivation. A rerun of its audit follows before new computations.

## Chosen extension (recorded before computation)

Choose exactly the continuation named in round 5: retain the next block-inverse term and evaluate d=<h,QAQ h>, h=QAv. This determines the order-b^4 coefficient in log gamma, and the order-b^4 relative coefficient after exponentiation. The reason is that it is a concrete missing Gaussian integral with an exact spectral interpretation already established by the earlier work. No claim about centered log Z will be inferred.

Audit plan: derive the coefficient by both the exact crossing Schur complement and a reciprocal scalar Neumann expansion; evaluate the Gaussian integral in two independent representations; check it against the zero-energy radial ODE only as an asymptotic diagnostic. Inspect signs, factors of 4*pi, Gaussian tails, scale invariance, and the remainder order.

## Earlier audit rerun: holds

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T090/check_correction.py
```

The script passed. Variance by radial quadrature 0.267652639082734; covariance integral and Li_2(1/4) series 0.267652639082733. C1=0.021299120270804. Nine Ein checks and five covariance scales passed. The last-two-coupling ODE extrapolation error was -2.855e-08. Runtime 0.241 s, peak RSS 12.344 MiB. CPU soft limit 60 s installed. Darwin rejected address-space limiting. The nice wrapper warned that an incremental adjustment was denied; the script directly confirmed inherited niceness 20, already more polite than requested. No mathematical failure.

## Next coefficient reduced analytically

At the crossing, the inverse in the exact block formula is g*(I-g*QD_EQ)^(-1), D_E=A+B_E. Its next term gives ell=1/g-a_s-c*g-d*g^2+O_s(g^3), d=<h,A h>, h=QAv. The O(sqrt(E)) resolvent error is smaller than every power of g. Therefore the new logarithmic coefficient is 4*pi*d, with no extra a_s*c term. A reciprocal Neumann expansion will independently check this cancellation.

Put H(u)=log(2)-Ein(u), F(t)=integral_0^t exp(-u)H(u)du. Angular averaging and the zero mean of H give

    d = J/(64*pi^3),
    J = -E[H(U)H(V) log(max(U,V))]
      = integral_0^infinity F(t)^2 dt/t,

where U,V are independent unit exponentials. The boundary terms vanish and F is positive because

    F(t)=integral_0^1 [exp(-t)-exp(-(1+p)*t)] dp/[p*(1+p)].

Tonelli and the elementary four-exponential integral give the independent compact representation

    J = integral_[0,1/3]^2 -log(1-xy) dx dy/[xy*(1+x)*(1+y)]
      = sum_(n>=1) I_n^2/n,
    I_n = integral_0^(1/3) x^(n-1)/(1+x) dx.

The positive series tail after N terms is at most (1/9)^(N+1)/[(N+1)^3*(1-1/9)]. Alternating rational expansions of each I_n can give certified bounds on J independently of floating-point quadrature. This also proves that the new coefficient is strictly positive. A local script will compare this series with the radial F integral and a direct logarithmic-kernel integral.

## New audit saved and passed

Created standard-library-only check_next_term.py. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_next_term.py
```

Output:

```text
nice: setpriority: Operation not permitted
CPU soft limit: 60 s; effective niceness: 20
certified J: [0.08383727095123180283, 0.08383727095123180284]
exact rational interval width < 1.110e-24
certified d=<h,QAQ h>: [0.00004224813485733012, 0.00004224813485733013]
certified C2 (log coefficient): [0.00053090572038263670, 0.00053090572038263671]
F vs positive mixture: 8 cases PASS; max error 4.163e-15
J positive rational series: 0.0838372709512318
J radial F^2 integral:     0.0838372709512456
J direct log-max kernel:   0.0838372709515297
J compact double integral: 0.0838372709512318
C1=0.0212991202708040; C2=0.0005309057203826
relative order-g^2 coefficient C2+C1^2/2=0.0007577319825377
zero-energy diagnostic: (residual-C1*g)/g^2 -> C2
g        adjusted coefficient    difference from C2    step difference
0.5      0.000538379034  7.473e-06 8.242e-13
0.25     0.000534615617  3.710e-06 2.592e-11
0.125    0.000532753956  1.848e-06 7.276e-12
0.0625   0.000531827242  9.215e-07 1.441e-09
linear extrapolation: 0.000530900527; error -5.193e-09
elapsed seconds: 0.213; peak RSS MiB: 14.000
PASS: exact rational enclosures and independent floating-point diagnostics
```

The rational bounds use N=20 terms for J, 60 alternating terms per I_n, and a positive tail bound. Pi is enclosed using exact rational alternating series and Machin's identity; the displayed decimal endpoints are rounded outward using integer division. These three intervals are certified by rational arithmetic. The quadrature and ODE values are floating-point diagnostics, not enclosures. The largest of the three independent J quadrature discrepancies is about 3e-13. The ODE extrapolation is within 5.2e-9 of C2. It is not a finite-coupling eigenvalue solver.

The script is single-threaded, has constant/small rational storage and a 60-second CPU limit. It inherited niceness 20 and used 14 MiB peak RSS. No address-space limit was requested in the new script because the earlier run established that this Darwin sandbox rejects it. No mathematical or numerical failure occurred.

## Proof saved and attacked

Saved PROOF.md with the spectral/pointwise identification, global Gaussian resolvent bound, exact-crossing expansion, Gaussian radial calculation, positive series and rational certificates. The result is

    log gamma = -4*pi/g - log(2*s) - Euler
                + Li_2(1/4)*g/(4*pi) + J*g^2/(16*pi^2) + O(g^3),
    J = sum_(n>=1) [integral_0^(1/3) x^(n-1)/(1+x) dx]^2/n.

Equivalently the relative order-b^4 coefficient is (J+Li_2(1/4)^2/2)/(16*pi^2), approximately 0.0007577319825377. The logarithmic coefficient is approximately 0.00053090572038263670 and is strictly positive.

Independent checks and attempts to break the argument:

1. Re-derived the expansion using the exact Schur complement at mu=1/g and separately the reciprocal scalar Neumann expansion. With m2=a^2+c and m3=a^3+2*a*c+d, the order-g^2 reciprocal coefficient is -a^3+2*a*m2-m3=-d. Thus an apparent a*c contribution cancels; adding it would produce a false dependence on covariance scale.
2. Counted every factor of 4*pi directly in the radial integral: h=v*H/(4*pi); the averaged A kernel, after removing its two factors v, is [-2*Euler-log(s)-log(max(u,w))]/(4*pi). The zero mean of H kills the constants. This gives d=J/(64*pi^3), and multiplying by 4*pi in log E gives C2=J/(16*pi^2). It agrees independently with the ODE residual after subtraction of C1*g.
3. Checked endpoint terms in the integration by parts: F(t)=O(t) at zero, and zero total integral gives F(t)=O((1+t)*exp(-t)) at infinity. Therefore F(t)^2*log(t) vanishes at both endpoints. Signed integrals before integration by parts are absolutely integrable. Tonelli is used only after obtaining the nonnegative mixture for F.
4. Rechecked the compact change of variables p=2*x/(1-x). The measure dp/[p*(1+p)] becomes dx/[x*(1+x)], and the logarithm becomes -log(1-x*y). The upper endpoint is 1/3, not the 1/2 used in round 5's different variance integral. This distinction is important for the coefficient.
5. Audited perturbative orders: the inverse remainder is O(g^3), the errors from B_E are O_s(sqrt(E)), and sqrt(E)=O_s(exp(-2*pi/g)). Thus the log remainder is O_s(g^3), not merely o(g^2). Exponentiation adds C1^2/2 at order g^2. Exact Brownian scaling gives a uniform relative/log remainder for all s>0; fixed-s operator estimates alone would not justify that claim.
6. Re-derived the pair generator as Delta from two independent Brownian motions of generator Delta/2. General SHE diffusion d0 changes C2 to J/(64*pi^2*d0^2) and the leading exponential constant to 8*pi*d0. At d0=1/2 these return the theorem. The variable d in the block calculation is a coefficient, not this diffusion parameter.
7. Certified the decimal endpoints with exact fractions and outward integer rounding. The pi enclosure uses alternating arctangent sums and Machin's identity, whose tangent calculation is included in PROOF.md. Floating-point quadrature/ODE tolerances do not enter these certificates.
8. Checked b<0 (only g=b^2 appears), b=0 (Z=1, gamma=0, excluded from the logarithmic expansion), s=0 (excluded), the non-L2 constant initial condition (handled by Duhamel and a bounded positive eigenfunction), Gaussian tails, the logarithmic diagonal, and radial symmetry of h. No extension to a different covariance or initial condition is claimed.

No mathematical counterexample or gap was found in this coefficient calculation. It is new relative to round 5; priority in the weak-bound-state literature is not asserted. It still supplies no variance bound for centered log Z and no KPZ exponent.

Read audit: the truncated round-4 proof passages and round-5 proof tail were reread in exact ranges. Two attempted startup-memory paths did not exist; the existing memory index and brain navigation were read instead. No external state-writing utilities were run. No file outside this folder was modified.

## Report and final artifact check

Saved REPORT.md with the exact required PROVED verdict, the new logarithmic and relative coefficients, commands, certified bounds, diagnostic limitations, failed resource operations and the next operator coefficient. T090 itself remains open. No SOLVED_ELSEWHERE.md was created.

At 15 November 2026, 10:53:20 +04, ran a tiny read-only Python artifact check under `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B`. It confirmed inherited niceness 20, the exact report first line, all four nonempty files, and the required failure/uncertainty/next-worker/task statements. At that point REPORT.md had 53 lines/3949 bytes, PROOF.md 421 lines/14896 bytes, LOG.md 125 lines/12159 bytes, and check_next_term.py 207 lines/7404 bytes. All checks passed. No further mathematical or numerical changes were needed after the successful audit.
