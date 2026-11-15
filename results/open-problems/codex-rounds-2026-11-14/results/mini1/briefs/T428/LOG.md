# T428 work log

Task received: 14 November 2026, approximately 22:15 (+04, Asia/Tbilisi).
Request: push Conjecture 1.17 of arXiv:2609.15832 forward by one checkable piece.

## 22:16 — Orientation and literature search begun

All deliverables stay in this folder. No git, publishing, external messages,
subagents, or shared-state registration will be used. The folder-only instruction
overrides the general instructions to update the external checklist and mesh.

Read the startup memory index and compute-state JSON. Compute state was `warn`,
mode `owner_away_open`, with ample memory. No heavy computation is planned.
An attempted prescribed brain recall started an ONNX-backed search and was
interrupted; it produced no mathematical result. Subsequent work uses read-only
source inspection. `nice -n 15` prints `setpriority: Operation not permitted` in
this sandbox; short inspection programs still execute. This limitation will be
recorded rather than represented as a successful priority change.

Commands so far: `pwd`; `rg --files`; small `python3 -c` reads of the startup
memory and compute state; `date '+%Y-%m-%d %H:%M:%S %Z'`.
Output: working folder confirmed; local time 2026-11-14 22:16:00 +04.

Web searches: `"2609.15832"`; `"Conjecture 1.17" "stochastic heat"`.
Opened primary sources:

- Hindy Drillick, Jonathan Hou, Shalin Parekh,
  *A universality result for the critical 2d stochastic heat flow*,
  <https://arxiv.org/html/2609.15832v1>.
- Xue-Mei Li, Te-Chun Wang, *Near-optimal bounds for the critical 2d SHF and
  the delta-Bose gas*, <https://arxiv.org/abs/2611.03191> (2 November 2026).
  Its abstract concerns moment growth and ground-state energies, and does not
  announce the signed-kernel universality extension.
- Francesco Caravenna, Rongfeng Sun, Nikos Zygouras,
  *The Critical 2d Stochastic Heat Flow*,
  <https://arxiv.org/abs/2109.03766>.

No solved-elsewhere conclusion has been established. The literature check is
still in progress and is capped at ten minutes.

## 22:18 — Literature check concluded; choice of one piece

Additional searches: `"2609.15832" signed kernel conjecture`,
`"stochastic heat flow" "exponentially" universality 2026`,
`"Drillick" "Hou" "Parekh" universality signed`,
`"stochastic heat flow" "signed" kernel 2026 conjecture`,
`"Conjecture 1.17" Drillick Hou Parekh proof`,
`"2609.15832" universality extension November`, and
`"critical stochastic heat" "signed" "universality"`.
Opened the arXiv abstract and HTML for 2611.03191 and the current abstract
for 2609.15832. The latter lists only v1. The November paper contains no
match for `signed`; its announced result is a moment-growth bound.
Also opened Sudheesh Surendranath, *Continuous-time directed polymers to
the Critical SHF via moments*, <https://arxiv.org/abs/2608.11603>.
The attempted HTML URL returned 404; the abstract page was opened successfully.
It predates the target paper and is already discussed there as evidence.
No later resolution or substantial advance on this particular extension
was located. This is a bounded search result, not a proof of absence.
Elapsed literature check: approximately three minutes, below the ten-minute cap.

Chosen piece: prove that for the continuum Brownian gap process, a fixed
real signed exponentially decaying profile with strictly positive integral
has a unique dominant positive critical-tuning eigenvalue for large N;
derive its first correction and show that logarithmically growing spatial
cutoffs preserve the fine-tuning parameter. This addresses the spectral
definition and cutoff stability of Lambda_N, not convergence of the flow.

Why: the integrated planar heat kernel is explicit. Multiplication by
square roots of the absolute profile gives a compact operator that tends
in norm to a rank-one operator. The mass isolates its eigenvalue even
without positivity. This permits a complete argument without importing
the unsigned renewal probability construction, which fails for signed
weights. The additional fixed-profile and positive-mass assumptions will
be stated throughout.

Planned independent audit: derive the heat-kernel constant both by the
exponential integral and by a split time integral; compute the correction
for the signed positive-definite profile 2 phi_1 - phi_2 both from Gaussian
logarithmic moments and from a one-dimensional heat overlap integral.

## Proof drafted

Wrote `PROOF.md`. The main bound is a weighted Hilbert--Schmidt expansion
of the integrated Brownian heat kernel into a rank-one operator plus a
term of size 1/log N and a remainder of size 1/(N log N). It gives a
dominant real simple eigenvalue, an explicit correction, and uniform
control of normalized spatial operator powers. The cutoff corollary uses
R_N=kappa log log N, kappa>1/a, to preserve theta.

The explicit signed covariance example is f=2 phi_1-phi_2. Its mass is one,
and the claimed correction is I(f)=log(81/32)/(4 pi). This has been
derived symbolically two ways in the proof, but numerical checks are
still pending. These checks will be independent of any spatial
discretization of the singular integral operator.

Environment check command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -c '<version, RSS, module availability>'`.
Output: Python 3.13.2; startup RSS 11,780,096 bytes;
mpmath/numpy/scipy all installed. `nice` issued the sandbox priority warning.
The verification will use only mpmath and the standard library, one thread.

## First audit run: environment failure, no mathematical output

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py`

Exit 1 immediately: `resource.setrlimit(resource.RLIMIT_AS, ...)` raised
`ValueError: current limit exceeds maximum limit`. The numerical code had
not started. Removed that unsupported address-space cap; retained a
90-second CPU cap. The script uses scalar quadrature and reports actual
peak RSS. No large arrays or parallel workers are used.

## Successful audit run

Exact command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0. Stderr: `nice: setpriority: Operation not permitted`.
The script's direct libc check reports inherited nice priority **20**, with
errno zero. Thus the process already had a lower scheduling priority than
the requested nice 15; the attempted further increment was refused.
Measured peak RSS: 21,512,192 bytes. Scalar quadrature took 0.102 seconds.
The complete stdout is saved verbatim as `verification.json`; its numerical
output is:

```text
precision_digits: 45
I_closed:                   0.073904652375245286251900741971234977965
I_log_moment_quadrature:    0.073904652375245286251900741971234977965
I_heat_overlap_quadrature:  0.073904652375245286251900741971234977965
tuning_shift_4piI:          0.92871325187271221849482034039921997821
moment_vs_closed_abs_error: 2.1895288505075266733183274738904939551e-47
heat_vs_closed_abs_error:   0.0

r=0.7, N=13:
direct_vs_E1_error: 0.0
remainder:  0.00074810182025755459511317524489795203126
upper_bound:0.00074986463572142994737262542358203882112

r=2, N=1000:
direct_vs_E1_error: 0.0
remainder:  0.000079557581598203023024438375290612853612
upper_bound:0.000079577471545947667884441881686257181017

N=10:    renormalized_heat_overlap=0.074263905388638087252685349549710433323
         error_from_I=0.00035925301339280100078460757847545535804
N=100:   renormalized_heat_overlap=0.073908591518484692404556059409304592873
         error_from_I=0.0000039391432394061526553174380696149084875
N=1000:  renormalized_heat_overlap=0.073904692124197386272523469170568497342
         error_from_I=0.000000039748952100020622727199333519377708665
N=10000: renormalized_heat_overlap=0.073904652773092855744120253762330800092
         error_from_I=0.00000000039784756949221951179109582212722280931
```

All four thread environment variables were `1`. The numerical work checks
the constants, not the infinite-dimensional spectral theorem. Its finite-N
overlap is a matrix element and must not be mistaken for Lambda_N itself.

## Adversarial proof audit

- Re-derived the coefficient 1/(4 pi) from the gap generator Delta and
  checked the time integral begins at zero. Starting at 1 would change the
  first correction. The E_1 substitution and split-time derivation give
  the same g and the same bound |z|^2/(16 pi N).
- Re-derived log(81/32)/(4 pi) using logarithmic Gaussian moments and
  independently the rational heat-overlap integral. Quadrature verifies
  both to better than 1e-36. The covariance example really changes sign;
  its Fourier transform 2q-q^2 remains nonnegative.
- Checked the nonnormal operator issue: the unsymmetrized operator need
  not approach a rank-one operator in unweighted L^2 norm. The proof
  applies only to the weighted operator, then transfers its nonzero
  spectrum by an explicit XY/YX factorization. No self-adjointness or
  Perron--Frobenius assertion is used for a signed operator.
- Checked the all-k bound: the complementary operator has norm O(1/log N),
  which controls every power. The operator statement excludes k=0;
  the scalar statement includes it because its k=0 value is exactly one.
- Checked uniformity of cutoff errors: all absolute moments are bounded by
  those of |f| and m_R>=m/2 eventually. The rate in (4) has a 1/log^2 N
  floor; it is sufficient for preserving theta, but is not a fixed-N
  cutoff convergence rate.
- Tested the omitted mass-zero case logically: the limiting rank-one
  operator becomes nilpotent, so the spectral isolation proof fails.
  No inference about that case or the full conjecture is made.
- A fixed cutoff radius changes the leading mass and cannot in general
  preserve the original beta_N. A growing radius is necessary here.
  Growing supports do not meet a uniform compact-support hypothesis.
  Also, a hard cutoff need not preserve positive definiteness of a
  covariance, so it does not automatically define an approximating noise.
- No estimate was proved for time-resolved signed renewal kernels or for
  higher moments. Spatially integrated powers cannot replace that work.

No counterexample to the stated lemma was found in this audit. Novelty of
this elementary spectral lemma is not asserted.

## Exact successful stdout and final artifact check

The following block is the complete stdout of the successful verification run.

```json
{
  "precision_digits": 45,
  "I_closed": "0.073904652375245286251900741971234977965",
  "I_log_moment_quadrature": "0.073904652375245286251900741971234977965",
  "I_heat_overlap_quadrature": "0.073904652375245286251900741971234977965",
  "tuning_shift_4piI": "0.92871325187271221849482034039921997821",
  "checks": {
    "moment_vs_closed_abs_error": "2.1895288505075266733183274738904939551e-47",
    "heat_vs_closed_abs_error": "0.0"
  },
  "heat_kernel_checks": [
    {
      "r": "0.7",
      "N": "13.0",
      "direct_vs_E1_error": "0.0",
      "remainder": "0.00074810182025755459511317524489795203126",
      "upper_bound": "0.00074986463572142994737262542358203882112"
    },
    {
      "r": "2.0",
      "N": "1000.0",
      "direct_vs_E1_error": "0.0",
      "remainder": "0.000079557581598203023024438375290612853612",
      "upper_bound": "0.000079577471545947667884441881686257181017"
    }
  ],
  "finite_N_overlap_checks": [
    {
      "N": 10,
      "renormalized_heat_overlap": "0.074263905388638087252685349549710433323",
      "error_from_I": "0.00035925301339280100078460757847545535804"
    },
    {
      "N": 100,
      "renormalized_heat_overlap": "0.073908591518484692404556059409304592873",
      "error_from_I": "0.0000039391432394061526553174380696149084875"
    },
    {
      "N": 1000,
      "renormalized_heat_overlap": "0.073904692124197386272523469170568497342",
      "error_from_I": "0.000000039748952100020622727199333519377708665"
    },
    {
      "N": 10000,
      "renormalized_heat_overlap": "0.073904652773092855744120253762330800092",
      "error_from_I": "0.00000000039784756949221951179109582212722280931"
    }
  ],
  "getpriority": 20,
  "getpriority_errno": 0,
  "thread_environment": {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1"
  },
  "wall_seconds": 0.102,
  "max_rss_bytes_macos": 21512192,
  "scope": "Constant checks only; no numerical proof of an operator limit."
}
```

Final check: REPORT first-line verdict, output JSON, peak RSS below 1 GB, inherited nice 20, and all four thread settings equal to 1 passed. Read-only artifact audit; no rerun of numerical work was necessary.
