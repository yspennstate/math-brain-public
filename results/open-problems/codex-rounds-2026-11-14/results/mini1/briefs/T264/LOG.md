# T264 work log

Task: "push this problem forward by one checkable piece" (session opened 2026-11-14; local clock recorded below).

## Orientation and scope

Read the startup memory, brain index, compute state, and existing T264 memory cards. All writes stay in this folder. The folder-only instruction rules out invoking the brain/checklist/mesh commands that write outside it; no such commands were invoked. No git or subagents.

Compute-state snapshot: status `ok`, mode `owner_away_open`. Any numerical script will use `nice -n 15`, `OMP_NUM_THREADS=1`, and no numerical library needing parallel workers.

## Step 1: literature search begun

Used the web search tool with queries including `ReLU minimum norm interpolation fixed dimension tempered overfitting 2025 2026`, `ReLU networks benign tempered overfitting multivariate minimum norm 2024 2025`, `"minimum norm" "ReLU" "fixed dimension" "2026"`, and `"tempered overfitting" multivariate 2025 2026 minimum norm`.

Opened the arXiv pages for 2207.06569, 2307.15396, 2305.15141, 2410.06191, 2602.13910, and 2410.19092. Promising but different settings: growing-dimension regression, binary-weight minimum-size networks, and conditional stability of deep networks. Further scope checks follow. No complete resolution found so far.

## Candidate piece

An exact two-observation minimum-parameter-norm calculation for homogeneous two-layer ReLU regression on the sphere. Opposite noisy labels on nearly coincident points may force a large global linear component. The goal is to solve the convex atomic problem exactly and determine which fixed dimensions have infinite *training-set averaged* squared risk already at sample size two. This is a finite-sample obstruction, not an assertion about the n-to-infinity limit. The choice will be finalized after the short literature check.

## Step 1 complete (approximately six minutes)

No whole-problem solution located. Opened and checked these further primary sources:

- Junhyung Park, Patrick Blöbaum, Shiva Prasad Kasiviswanathan, *Benign Overfitting for Regression with Trained Two-Layer ReLU Networks*, arXiv:2410.06191, https://arxiv.org/html/2410.06191v1 . Assumption 1 explicitly includes `n exp(-2d) <= delta/6`; its dimension grows. This does not settle fixed-d interpolation.
- Ouns El Harzli, Yoonsoo Nam, Ilja Kuzborskij, Bernardo Cuenca Grau, Ard A. Louis, *Sufficient Conditions for Stability of Minimum-Norm Interpolating Deep ReLU Networks*, arXiv:2602.13910, https://arxiv.org/html/2602.13910v1 . Conditional stability via a stable subnetwork and a low-rank subsequent layer; no general fixed-d noisy interpolation classification.
- Itamar Harel, William M. Hoza, Gal Vardi, Itay Evron, Nathan Srebro, Daniel Soudry, *Provable Tempered Overfitting of Minimal Nets and Typical Nets*, arXiv:2410.19092, https://arxiv.org/abs/2410.19092 . Binary-weight deep classification with minimum size or random interpolation, rather than the specified two-layer parameter norm.
- Weizhao Li, Lei Shi, Hanfei Zhou, *Minimum-Norm Interpolation in Weighted Variation Spaces: Direct and Inverse Problems*, arXiv:2611.01105, https://arxiv.org/html/2611.01105v1 . Noise-free approximation of a target in a variation space; not the noisy-risk limit.
- Tin Sum Cheng, Aurelien Lucchi, Anastasis Kratsios, David Belius, *Characterizing Overfitting in Kernel Ridgeless Regression Through the Eigenspectrum*, arXiv:2402.01297, https://arxiv.org/abs/2402.01297 . Sub-Gaussian feature assumptions; the abstract explicitly cautions about feature independence. Not a theorem for learned minimum-variation-norm ReLU features on a sphere.
- Tongtong Liang, Dan Qiao, Yu-Xiang Wang, Rahul Parhi, *Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon*, NeurIPS 2025, https://proceedings.neurips.cc/paper_files/paper/2025/file/233c44cd680737f451afcd401a95150c-Paper-Conference.pdf . Bounds for flat/stable solutions, not the requested interpolation limit.

Search and author metadata were checked on opened pages. This is a bounded search, not a proof of absence. No `SOLVED_ELSEWHERE.md` is warranted.

## Step 2: chosen piece, before proof or numerical implementation

Prove the exact minimum-norm two-sample homogeneous ReLU interpolant with opposite labels on the sphere, its risk formula, and its risk-tail exponent. Extend the moment threshold to penalized hidden biases and to a full-dimensional annulus in the homogeneous case. Reason: this is an exactly solvable close-pair mechanism that makes the distinction between conditional/typical and training-averaged risk concrete. The claimed output is finite-sample only, with no extrapolation to n tending to infinity.

The norm is one half the sum of squared parameters in both layers; width is unrestricted (two units suffice), and there is no free linear skip or free output intercept. The bias extension penalizes hidden biases in the same Euclidean norm. Expected threshold anticipated: infinite averaged squared risk in d=2,3; finite in d>=4. All load-bearing formulas will be verified independently.

Local task clock: `date '+%Y-%m-%d %H:%M:%S %Z'` printed `2026-11-14 21:26:07 +04`. Work began approximately 21:23 +04.

## Step 3: proof written

Wrote `PROOF.md`. The proof uses an explicit two-constraint dual certificate, equality cases to identify every minimizer, and a separately derived spherical ReLU product integral. For opposite labels the exact homogeneous risk is `[pi-sin(theta)+theta*cos(theta)]/[pi*d*sin(theta)^2]` for acute sample angles. Its leading term is `1/(d*theta^2)`. The random-angle density is proportional to `sin(theta)^(d-2)`, giving the risk-moment threshold `q < (d-1)/2`.

The penalized-bias case has a second explicit minimizer and pointwise bounds between one half and all of a particular linear function. Its leading risk coefficient is identical. A radial homogeneity reduction transfers the homogeneous result to a bounded-density annulus, with risk multiplier `E[rho^2]=7/3`. This extension explicitly uses heteroscedastic noise.

Next: independent quadrature, exhaustive planar pricing, moment/tail constants, and checks of equal labels, angle endpoints, bias scaling, and the distinction between fixed n and asymptotic n.

## Step 4: first numerical audit

Created the standard-library-only `verify_two_point.py`, with a 120-second wall alarm, 90-second CPU limit, OMP single-thread assertion, and an actual process-priority assertion. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_two_point.py > verification_output.txt
```

First run exited 1 at the independent S^2 quadrature tolerance (3e-5), after all eight planar pricing/interpolation/exact-risk checks had passed. The initial surface grid was 160 by 512; increased to 256 by 2048 and added diagnostic values to the assertion. This is a quadrature resolution check, not a change in the proposed theorem.

The sandbox printed `nice: setpriority: Operation not permitted`, but the script's actual-priority assertion (`getpriority >= 15`) passed before any computations. Thus it inherited a compliant priority. The next run records the actual nice value. No attempt is made to change sandbox permissions.

Second run of the same command passed all assertions. Actual nice value: 20; OMP threads: 1; peak RSS: 15,482,880 bytes; wall time inside script: 1.59 seconds. Maximum relative error between direct circle integration and the exact risk formula was 2.86135e-9. Independent three-dimensional surface quadrature and biased pointwise bounds passed. The angular normalization was independently recovered by an integration-by-parts recurrence for d=2 through 8.

The conditional d=5 mean approached 0.21484375. Rather than guessing the rational from this decimal, reflected the obtuse-angle integral into the acute half and integrated the resulting sine powers by parts. This proves the exact conditional mean `55/256` for d=5, and `3/8+1/(3*pi)-13/(9*pi^2)` for d=4. Added every algebraic step to `PROOF.md`, and added independent checks against the existing original-angle quadrature. A final rerun is required because these assertions are new.

## Final numerical audit

Reran exactly the command above after adding the finite-mean checks; exit status 0. Complete stdout is saved in `verification_output.txt`; numerical data are in `verification_data.json` and `angle_checks.csv`. Output:

```text
PASS: interpolation, explicit dual pricing, and planar atom grid
Maximum relative gap below exact dual price: 1.4092e-05
Maximum relative circle-risk error: 2.86135e-09
PASS: independent S^2 surface quadrature and bias pointwise bounds
PASS: gamma normalizers equal sine-integral recurrence, d=2..8
Conditional opposite-label truncated squared risks:
  d=2 epsilon=1e-01 mean=1.785664668
  d=2 epsilon=1e-02 mean=16.11430404
  d=2 epsilon=1e-03 mean=159.3542295
  d=2 epsilon=1e-04 mean=1591.748765
  d=3 epsilon=1e-01 mean=0.6194179053
  d=3 epsilon=1e-02 mean=1.003313771
  d=3 epsilon=1e-03 mean=1.387079333
  d=3 epsilon=1e-04 mean=1.770843521
  d=4 epsilon=1e-01 mean=0.3188354031
  d=4 epsilon=1e-02 mean=0.3331589196
  d=4 epsilon=1e-03 mean=0.3345913249
  d=4 epsilon=1e-04 mean=0.3347345566
  d=5 epsilon=1e-01 mean=0.2140944075
  d=5 epsilon=1e-02 mean=0.2148362448
  d=5 epsilon=1e-03 mean=0.2148436799
  d=5 epsilon=1e-04 mean=0.2148437469
PASS: unconditional risk-tail constants, d=2..5, thresholds=1e4,1e6,1e8
PASS: d=4 opposite-label mean: quadrature=0.334750472085, exact=0.334750474578
PASS: d=5 opposite-label mean: quadrature=0.214843747651, exact=0.21484375
theta=0.1: 2*theta^2*R=1.003233659, with_bias=1.066400373
theta=0.01: 2*theta^2*R=1.000033228, with_bias=1.006393308
theta=0.001: 2*theta^2*R=1.000000333, with_bias=1.000636891
PASS: annulus radial multiplier 2.3333333325, exact 7/3=2.33333333333
All assertions passed. Data: verification_data.json, angle_checks.csv
Resources: {'elapsed_seconds': 1.5732312079635449, 'peak_rss_bytes': 15826944, 'nice': 20, 'OMP_NUM_THREADS': '1'}
```

The sandbox again denied the attempted priority adjustment, while the actual priority remained nice 20 (lower priority than required). No special permissions were requested.

## Attempt to break the result

- Re-derived the acute risk singularity through the odd part of the minimizer: its exact linear component has risk `1/[2*d*(1-cos(theta))]`. This independently recovers `1/(d*theta^2)` and locates the global source of the blow-up.
- Checked both sides of the right-angle transition, the antipodal limit, interpolation signs, and direct normalized-atom pricing. Both risk formulas agree at pi/2; the antipodal homogeneous risk tends to `2/d`.
- Equality in the dual certificate forces the two claimed atom directions, including all ambient dimensions, so selecting a different exact optimizer cannot remove the opposite-label singularity. Equal-label minimizers need not be analyzed for uniqueness: the uniform cost bound controls all of them.
- For penalized biases, checked the explicit interpolant and the pointwise bound over a disk, then integrated the actual affine ReLU units independently on S^1 and S^2. The lower bound uses `m(x)>=0` and therefore uses the specified sphere support.
- Verified the angular normalizing constant two ways (gamma ratio and sine-integral recurrence), and checked the risk-tail coefficient by solving the threshold and integrating spherical caps. The Rademacher opposite-label probability is exactly one half.
- The d=4 and d=5 conditional means were derived by integration by parts and independently compared to original-angle numerical integration; the exact d=5 rational was not inferred from decimal agreement.
- Full-dimensionality of the annulus is explicit in its Lebesgue density. Its radial risk factor was checked by midpoint quadrature independently of the antiderivative. Its noise is bounded but heteroscedastic.
- Tried the tempting inference from infinite two-sample expectation to catastrophic n-to-infinity behavior: it does not follow. Additional constraints can change the optimal atoms and their cancellation. No such inference is used.
- The norm convention excludes free linear skips and output intercepts. No claim is made for arbitrary GD training, classification losses, or a different bias penalty. The sphere's intrinsic dimension is d-1; the annulus extension is what supplies a full-dimensional design for the homogeneous result.

## Completion

`REPORT.md` records the finite-sample result, reproduction command, failed first quadrature check, limitations, and the next research step. No resolution of the full large-sample problem is claimed. Task: T264, "push this problem forward by one checkable piece", 2026-11-14 approximately 21:23 +04.
