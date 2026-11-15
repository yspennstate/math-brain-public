# T111 work log

Started 2026-11-14 21:17 Asia/Tbilisi (17:17 UTC). Task: “push this problem forward by one checkable piece.”

All writes stay in this folder. No git, subagents, external publication, or shared brain/mesh/checklist mutations: the task-specific confinement rule takes precedence over the global shared-state routines. Read startup memory and compute state. Compute state was `warn`, `owner_away_open`, 74% free memory; computations will be small, single-threaded, under `nice -n 15`, with `OMP_NUM_THREADS=1`.

## Step 1: literature check (in progress)

Web searches: `"Berry–Esseen" "2026" "constant" "He" "Cheng"`; `"2609.06358"`; `Berry Esseen optimal constant conjecture solved 2026 0.4097`.

Opened https://arxiv.org/abs/2609.06358v3: Hengzhi He and Guang Cheng, *The Berry-Esseen Constant Conjecture is Eventually True*, revised 30 September 2026. Its abstract confirms the uniform threshold supplied in the prompt, not all sample sizes.

Opened https://teorth.github.io/optimizationproblems/constants/19a.html: lists 0.4690 as a published upper bound and 0.4395/0.423 as unverified repository claims. Also found a purported exact solution on Hexagon; https://hexagonmath.org/2610.00590 initially failed to open. Opened https://hexagonmath.org/2610.00147v2 (superseded): *Moment defects and sharp iid Berry–Esseen bounds*, contributors Kacper Rodziewicz and Bartosz Kołodziejek; this makes stronger finite-index claims but needs checking against the latest paper. No conclusion from search snippets.

Read-only shell commands: `cat` startup MEMORY.md and compute_state.json; `ls -la`; `rg` for Berry–Esseen memories. The broad memory search was too noisy (849 paths); do not repeat it.

Opened the latest primary claim https://hexagonmath.org/2610.00590v1 and its 159-page PDF https://hexagonmath.org/pdf/2610.00590v1. PDF authors: Bartosz Kołodziejek and Kacper Rodziewicz, dated 27 October 2026, posted 29 October. It claims the whole conjecture, with an analytic reduction and a thirteen-role certificate suite. This is a Hexagon identifier, NOT an arXiv identifier. Opened its public repository read-only. No independent validation established in this search, and the constants list still marks the problem open. Record the claim without treating an author-run `ESTABLISHED` flag as a proof audit. Search finished within ten minutes.

## Step 2: chosen piece

Prove an explicit rare-contamination limit for a three-point triangular array: start with a Bernoulli law on {0,2}, insert mass lambda/n at its midpoint 1, then center and standardize. Compute the limiting normalized Kolmogorov ratio, including the parity mixture, and optimize over the Bernoulli parameter. This addresses the nonuniform transition from the extremal two-point lattice to a genuine three-point law: fixed-law lattice asymptotics alone miss the n-dependent boundary layer. Supply a direct binomial expansion proof and independently check the formula using exact finite convolutions and high-precision arithmetic. This is a special-family result, not a claim of a new universal upper bound or novelty over all literature.

Environment probe command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B -c 'import sys, importlib.util; print(sys.version); print({m: importlib.util.find_spec(m) is not None for m in ["numpy", "scipy", "mpmath"]})'`. Output: Python 3.13.2; numpy, scipy, mpmath all available. `nice` reported `setpriority: Operation not permitted`; inspect effective priority before computation, rather than assume the request succeeded. `ps` is blocked by the sandbox. Read the existing macOS nice-priority memory; it warns that relative nice can stack and that `os.getpriority`, not `os.nice(0)`, is the safe probe.

Additional opened primary arXiv pages: Anatolii Zolotukhin, Sergei Nagaev, Vladimir Chebotarev, arXiv:1810.09681; Irina Shevtsova, arXiv:1111.6554. No additional literature searches after selection of the mathematical piece.

## Step 3: derivation and implementation

Wrote PROOF.md: condition on the midpoint count J~Bin(n,lambda/n), retain the exact parity expectation `(1-2 lambda/n)^n`, derive a uniform first-order binomial CDF expansion from Stirling and the trapezoidal rule, and take both sides of every jump. Candidate result:

`R(p,lambda) = (|1-2p|/6 + (1+exp(-2lambda))/4) / (sqrt(2pi)*(p^2+(1-p)^2))`.

The optimized value is `(B+sqrt(B^2+4))/(12 sqrt(2pi))`, `B=3(1+exp(-2lambda))`. Independently derived the optimization by completing a square. This returns Esseen's constant at lambda=0 and is strictly smaller for every lambda>0.

Wrote check_midpoint.py: deterministic conditional-binomial finite convolutions; separate exact integer polynomial multiplication plus 90-digit CDF arithmetic; reflection, symmetric-center, and optimization audits. First command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_midpoint.py`. Failed before numerical work: macOS rejected `RLIMIT_AS` with `ValueError: current limit exceeds maximum limit`. Made this unsupported hard cap optional; arrays remain small and peak RSS is measured. CPU time and wall time retain 600s/900s limits. Effective nice is **20**, verified with `os.getpriority`: the nice warning is caused by the already low-priority environment, not execution at normal priority.

## Step 4: independent checks

The first successful run finished in 1.854 seconds, peak RSS 109,215,744 bytes, 80 finite rows and 48 exact-integer/90-digit independent cases. Added direct checks of both uniform CDF expansions, the variance and mean formulas, and a compact-parameter stability corollary; reran because those checks were new. The final run is reproduced verbatim below.

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_midpoint.py
```

Stderr: `nice: setpriority: Operation not permitted`; the script independently verifies effective nice 20 before numerical work. Stdout:

```text
{
  "finite_rows": 80,
  "independent_exact_cases": 48,
  "max_mass_error": 1.4588330543574557e-13,
  "max_omitted_tail": 1.381205554665212e-43,
  "max_independent_pmf_error": 5.134781488891349e-16,
  "max_independent_ratio_error": 7.605027718682322e-15,
  "reflection_pmf_error": 1.8735013540549517e-16,
  "effective_nice": 20,
  "address_space_hard_cap_supported": false,
  "peak_rss_bytes": 128696320,
  "elapsed_seconds": 1.9369792499928735,
  "optimized_constants": [
    {
      "lam": 0.0,
      "maximizing_p": 0.41886116991581035,
      "K": 0.4097321837023964,
      "grid_max": 0.4097321835031603
    },
    {
      "lam": 0.1,
      "maximizing_p": 0.41124831153628244,
      "K": 0.3745865640296369,
      "grid_max": 0.37458656402549567
    },
    {
      "lam": 1.0,
      "maximizing_p": 0.36405286097212186,
      "K": 0.2445449773432545,
      "grid_max": 0.24454497733579914
    },
    {
      "lam": 4.0,
      "maximizing_p": 0.3486544259696941,
      "K": 0.2196641047910368,
      "grid_max": 0.21966410477526935
    }
  ],
  "worst_scaled_cdf_residual_by_n": {
    "128": 0.03216367675300817,
    "512": 0.015784973859630937,
    "2048": 0.007842789850519363,
    "8192": 0.0039080641672447165,
    "32768": 0.0019502285557495983
  },
  "final_n_optimized_rows": [
    {
      "lam": 0.0,
      "label": "optimized",
      "p": 0.41886116991581035,
      "n": 32768,
      "finite_ratio": 0.4097311739310221,
      "limit_ratio": 0.40973218370239645,
      "difference": -1.009771374349544e-06,
      "k": 27450,
      "side": "right",
      "mu": 0.8377223398316207,
      "variance": 0.973665961010276,
      "rho": 1.0401206986639557,
      "mass_error": 6.661338147750939e-16,
      "omitted_tail": 0.0
    },
    {
      "lam": 0.1,
      "label": "optimized",
      "p": 0.41124831153628244,
      "n": 32768,
      "finite_ratio": 0.37457962610341394,
      "limit_ratio": 0.3745865640296368,
      "difference": -6.937926222860824e-06,
      "k": 26950,
      "side": "right",
      "mu": 0.8224971647698821,
      "variance": 0.9684896917274574,
      "rho": 1.0481530684082205,
      "mass_error": 3.552713678800501e-15,
      "omitted_tail": 1.6978259771978666e-83
    },
    {
      "lam": 1.0,
      "label": "optimized",
      "p": 0.36405286097212186,
      "n": 32768,
      "finite_ratio": 0.24454262389596937,
      "limit_ratio": 0.2445449773432545,
      "difference": -2.35344728513609e-06,
      "k": 23858,
      "side": "right",
      "mu": 0.728114019499116,
      "variance": 0.926047496028948,
      "rho": 1.1159748323623802,
      "mass_error": 2.220446049250313e-15,
      "omitted_tail": 6.068970339321828e-54
    },
    {
      "lam": 4.0,
      "label": "optimized",
      "p": 0.3486544259696941,
      "n": 32768,
      "finite_ratio": 0.21966565812671712,
      "limit_ratio": 0.21966410479103682,
      "difference": 1.5533356803043574e-06,
      "k": 22850,
      "side": "right",
      "mu": 0.697345801542423,
      "variance": 0.9082783658435016,
      "rho": 1.145369344325742,
      "mass_error": 6.661338147750939e-16,
      "omitted_tail": 1.381205554665212e-43
    }
  ]
}
All assertions passed.
```

Data: midpoint_data.csv (80 finite rows); midpoint_audit.json (48 exact arithmetic checks, 12 symmetric-center checks, 80 uniform CDF expansion residuals); computation.out (full final stdout). Finite computations are floating numerical checks, not interval-certified upper bounds. The proof is analytic.

An important falsification check: at lambda=4 and the limiting optimizing p, the n=32768 ratio is 0.21966565812671712, which EXCEEDS its limit 0.21966410479103682 by 0.0000015533356803043574. Thus the limiting formula must not be used as a finite-n upper bound. Both parities, both sides of jumps, p above and below 1/2, lambda=0, symmetry, and exact probability normalization were checked.

## Step 5: final analytic audit and report

Added AUDIT.md with an independent derivation of the leading lattice mass from the characteristic function's two saddles at 0 and pi, rather than the conditional-binomial argument. Rechecked the third cumulant, mean cancellation, Gaussian/Hermite supremum, both jump limits, and the reflected Esseen parameter. The proof includes a stability corollary uniform on compact p and bounded lambda, with those restrictions stated explicitly. Wrote REPORT.md with the exact special-family verdict, resource measurements, numerical limits, failure modes, the unverified full-solution claim, and a concrete next step. No universal sharp upper bound or finite-n certificate is claimed.

Final read-only artifact audit ran under `env OMP_NUM_THREADS=1 nice -n 15 python3 -B -` with an inline pathlib/csv/json check: all nine deliverables exist and are nonempty; REPORT.md has the required exact verdict line; CSV has 80 rows; JSON has 48 independent exact cases and 80 CDF-expansion checks. Output: `Artifact audit passed.` No files outside this folder were edited; no git, subagents, accounts, or external writes were used.
