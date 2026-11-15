# T305 work log

Task received: 14 November 2026, approximately 21:30 Asia/Tbilisi.
Task: “push this problem forward by one checkable piece.”

## 2026-11-14 21:32 +04 — orientation and chosen piece

Read PROMPT.md, the startup memory, the compute governor snapshot, and the
mesh protocol. A brain recall for “Metropolized HMC operator norm Hessian
Lipschitz T305” returned no relevant memory (explicitly: no memory contained
“metropolized”). No subagents, git operations, or external messages are used.
The task-specific instruction to write only in this folder takes precedence
over global mesh/checklist/brain writes; those global state changes are omitted.
The recall command attempted its own usual logging/refresh, so no further brain
commands will be run in this task.

Commands/read results:

- `pwd && rg --files ...`: only PROMPT.md initially present.
- `cat ~/.claude/compute/compute_state.json`: status `ok`, mode
  `owner_away_open`; shared machine busy. No heavy computation planned.
- `nice -n 15 env OMP_NUM_THREADS=1 python3 ~/.claude/dreaming/brain.py recall
  "Metropolized HMC operator norm Hessian Lipschitz T305"`: completed, no
  relevant result. `nice` reported `setpriority: Operation not permitted`.
  Check inherited process priority before any numerical work.

Literature search started at about 21:30. Opened the current arXiv page for
2304.04724, which lists Yuansi Chen, Khashayar Gatmiry, and Minhui Jiang,
version 3 dated 11 February 2026. Also opened the HTML of 2608.05022:
its section 4 explicitly assumes a Frobenius-Lipschitz Hessian and uses a
different sampler. No full settlement found so far; finish targeted search
within the ten-minute limit. Full references and scope will go in REPORT.md.

Chosen piece, before proof work: prove an exact stationary variance identity
and an O(d) bound for the leading modified-Hamiltonian coefficient of
kick–drift–kick leapfrog,

    A(x,p) = p^T (Hessian V(x)) p / 12 - |gradient V(x)|^2 / 24.

Why: a naive differentiation of `trace Hessian V` incurs large third-derivative
norms. Integration by parts may cancel this loss. If successful, this isolates
the finite-step remainder, rather than the leading stationary fluctuation, as
the remaining obstacle. The intended result is a reduction/partial result,
not a mixing theorem. Derive the coefficient directly and audit it on a
harmonic oscillator; do not assume that a formal expansion is uniform in d
or over this regularity class.

## 2026-11-14 21:32 +04 — literature check complete; algebraic result

Targeted web searches used the phrases “Metropolized Hamiltonian” with
“Hessian”, “2025”, “2026”, “operator-norm”, and “Lipschitz”, and the source
arXiv identifier. Opened the current HTML of 2304.04724v3, its section 2.4
and Table 1, the arXiv page and section 4 of 2608.05022, and the arXiv page
of 2607.12902. No settlement of the stated operator-norm leapfrog problem
was located. The July 2026 paper analyzes exact randomized Hamiltonian
trajectories, not the gradient complexity of Metropolized leapfrog.
This search took less than ten minutes and is now finished.

Priority check command:

    nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -c 'import os,resource; print("inherited_nice",os.getpriority(os.PRIO_PROCESS,0)); print("maxrss",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'

Output: `nice: setpriority: Operation not permitted`, `inherited_nice 20`,
`maxrss 11763712`. Thus the child already has lower priority than nice 15;
the wrapper's warning does not mean normal-priority compute. All numerical
scripts will verify this inherited priority, use one thread and bounded size.

Derived candidate exact identity (notation g=gradient V, K=Hessian V):

    576 Var(A) = 12 E tr(K^2) - 4 E[g^T K g] + Var(|g|^2).

The Brascamp–Lieb variance inequality gives
`Var(|g|^2) <= 4 E[g^T K g]`, hence

    E tr(K^2)/72 <= Var(A) <= E tr(K^2)/48 <= L^2 d/48.

No Hessian-Lipschitz constant enters. Next: write the integration-by-parts
proof, derive the leapfrog coefficient without citing a formal expansion,
and independently check constants/signs on Gaussian and non-Gaussian cases.

## 2026-11-14 — extension within the chosen piece: explicit warm tails

The stationary leading-coefficient result can be strengthened beyond variance.
Write `D=tr K`, `S=|g|^2`, `F=D-S`, and `Q=p^T K p-D`.
The map `x -> x+u g(x)` and its Jacobian give

    log E exp(t F) <= 4 d L^2 t^2,  |t| <= 1/(4L).

The needed auxiliary bound is `E exp(a S) <= (1-2La)^(-d/2)`.
Combining this with Gaussian quadratic-form tails and strong-convexity
concentration of `|g|` yields, for `s>=1` and `kappa=L/m`, the candidate bound

    P(|A-EA| > L(sqrt(kappa*d*s)+kappa*s)) <= 6 exp(-s).

For the exact Hamiltonian flow Phi_T and an M0-warm phase-space start, a union
bound then gives, with probability at least `1-delta`,

    |A(Z)-A(Phi_T Z)| <= 2L(sqrt(kappa*d*s)+kappa*s),
    s=log(12 M0/delta).

This keeps the warm factor explicit and logarithmic for the leading term.
It says nothing yet about the numerical remainder. Include the derivations
and audit them rather than infer a finite-step acceptance or mixing bound.

## 2026-11-14 21:39 +04 — proof and independent computation saved

Wrote PROOF.md. It proves the exact variance identity and exponential
concentration for A under only `mI <= Hessian V <= LI`, transfers the bound
to the exact Hamiltonian flow from an explicit M0-warm start, and derives
the fixed-problem leading leapfrog limit for C4 potentials. Section 7
defines the missing uniform remainder precisely.

Wrote and ran audit.py (standard library only; no parallel workers or
numerical libraries). Exact command:

    nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1

Output, copied from audit_output.txt:

```text
nice: setpriority: Operation not permitted
PASS: exact rational local expansion, Gaussian variance, and Gaussian invariant/remainder
PASS: nonproduct 2D integration-by-parts identities; max absolute residual 6.939e-18
PASS: 128 -> 256 Simpson refinement; max moment change 0.000e+00
Nonproduct Var(A): 0.0512802297651; proven interval [0.0398837802345, 0.0598256703518]
PASS: generator mgf inequalities at four positive/negative t values
Leapfrog coefficient errors (n=16,32,64,128,256): 2.309e-04, 5.769e-05, 1.442e-05, 3.605e-06, 9.013e-07
Resources: {"elapsed_seconds": 0.20855770900379866, "max_rss_bytes_macos": 17498112, "nice": 20, "python_threads": 1}
Data: audit_data.json
```

The data file contains all moments, both grid resolutions, positive and
negative generator-mgf checks, exact rational coefficient checks, the
Gaussian invariant calculation, and the leapfrog convergence table. The
two independent RK4 reference resolutions differ by 5.551e-15 in their
endpoint. These floating-point checks are audits, not certified enclosures.

Second derivations / attempts to break the argument:

1. Independently of the generator/Bochner proof, integration by parts of
   the vector fields `g D` and `K g` gives

       E D^2 - E(D S) = E tr(K^2) - E(g^T K g).

   Substitute this into the direct conditional Gaussian fourth-moment
   formula `576 E A^2 = 4 E D^2 + 8 E tr(K^2) - 4 E(DS) + E S^2` and
   subtract `(E S)^2` to recover the same variance identity.
2. For a Gaussian coordinate of precision lambda, direct independent
   Gaussian-square variances give `Var(A)=5 lambda^2/288`. Exact leapfrog
   preserves `p^2+lambda*(1-h^2 lambda/4)*x^2`. This also gives exactly
   `Delta(H+h^2 A)=h^4 lambda^3 Delta(x^2)/48`, confirming the sign and
   factors in the proof without a Taylor expansion.
3. The numerical target is genuinely coupled and asymmetric:
   `V(x,y)=(x^2+y^2)/2+0.4*(1-cos(x)cos(y))+0.2*(sin(x)-x)`.
   Its Hessian is between 0.4I and 1.6I. Thus the audit is not confined
   to independent coordinates or reflection-symmetric distributions.
4. Checked both signs of the generator mgf parameter; the transport map
   is invertible for negative as well as positive u because `|u|L<1`.
5. The warm-start event concerns a fixed deterministic exact-flow time.
   It makes no assertion for state-dependent trajectory stopping times
   or for the law at a numerical leapfrog endpoint.
6. Mollification preserves the spectral Hessian bounds, allowing the
   concentration statements for C2 potentials. The leapfrog asymptotic
   identification is stated only for C4 potentials. No C4 remainder
   constant is claimed to be controlled by the original assumptions.
7. A second bound from ordinary Poincare and `|grad S|<=2L|g|` is
   `Var(S)<=4 L^3 d/m`; it separately verifies the O(d) dimension count
   before using Brascamp–Lieb to obtain the sharper constant 1/48.

Unsuccessful route: deriving a finite-step mixing theorem directly from
the modified-energy expansion. Its compact-set constants can depend on
higher derivatives and dimension, so the expansion does not control the
remainder uniformly at `h ~ d^(-1/4)`. This gap is retained explicitly.

## 2026-11-14 — final algebra/coverage audit

Independently rechecked the generator Chernoff constants by choosing
`t=min(sqrt(s)/(2L sqrt(d)),1/(4L))`. If `s<=d/4`, the mgf bound is at most
`s` and `t*(4L sqrt(ds)+4Ls)>=2s`. If `s>d/4`, the exponent gained is
`sqrt(ds)+s-d/4>=s`. This separately confirms (20) with the same constants.
For the conditional Gaussian quadratic form, substitution in its exact
product mgf gives the Chernoff exponent exactly `s` at the stated threshold.
The final A constants are checked by
`12+2 sqrt(2 kappa)<=15 sqrt(kappa)` and `12+3 kappa<=15 kappa` for kappa>=1.

REPORT.md now records the proved piece, the missing uniform remainder,
the reproducible command, audit limitations, and the three opened papers.
No SOLVED_ELSEWHERE.md is warranted by the bounded literature search.
