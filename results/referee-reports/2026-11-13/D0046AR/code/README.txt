Independent D0046 referee checks. No claim_files/code module is imported or copied.

Environment: Python 3.13, NumPy, SciPy, requests, threadpoolctl, Matplotlib; Poppler
pdftotext is required for sources. All numerical runs must start at nice >=10.
The supplied launcher already provides nice 10 in this sandbox. The scripts
assert it rather than claiming that a prohibited renice succeeded.

Set OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, VECLIB_MAXIMUM_THREADS=1 and
MKL_NUM_THREADS=1 when launching each Python command.

python3 code/fetch_sources.py
  Fetches primary papers and converts PDF bytes through stdin to text. Retains
  only sources/*.txt and data/source_manifest.json. Does not retain PDF files.

python3 code/independent_simulation.py
  Exact OU and radial OU transitions. Seed 460811132026. Top two eigenvalues at
  edge times 0.25 and 1; tridiagonal paths use a 16-step time grid. Sizes through
  4096 for tridiagonal, through 2048 for dense Hermitian matrices. Outputs raw
  pairs, summary and run metadata. Approximate memory maximum below 1 GB.
  Raw grid_sup_abs is the maximum up to the row's time. Summary
  mean_grid_sup_squared is the maximum over the entire [0,1] grid, repeated in
  both lag rows; only interpret it as the [0,1] sampled maximum. It is never a
  continuous-time supremum estimate.

python3 code/check_math.py
  Finite-difference eigenvalue gradients, independent small-time clock checks,
  and a Lanczos orbit-fiber numerical check. Output data/independent_math_checks.json.

python3 code/audit_data.py
  Scalar math.fsum reconstruction of all submitted and independent summary
  correlations and mean squared increments; records hashes of claim artifacts.
  Produces data/independent_edge_increments.svg. Cache paths stay in data/.

python3 code/audit_resources.py
  macOS libproc polling of native thread counts during the same eigensolver
  kernels. This is a separate resource audit, not retrospective measurement
  of the entire simulation. It includes its own monitoring thread.

Dense matrix OU is exactly a time-changed normalized Hermitian Brownian motion:
G(t)=exp(-t) B(exp(2t)), with B(1) GUE. Thus the OU experiment compares precisely
the Brownian evolution requested, after tracking the moving deterministic edge.
For fixed edge time s, t=s*n^(-1/3). Standard Airy time in this normalization is s.
