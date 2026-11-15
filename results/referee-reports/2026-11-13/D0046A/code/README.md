# D0046 computations

Run from the parent directory with the existing Python 3 environment:

```sh
python3 code/audit_math.py
python3 code/simulate.py --pilot
python3 code/simulate.py
python3 code/analyze.py
python3 code/validate.py
```

Dependencies: NumPy, SciPy, threadpoolctl, Matplotlib. No installation was needed.
The launcher must supply nice 10 or greater; the simulation checks this and
refuses a less polite priority. Library thread limits are set to one before
NumPy/SciPy imports. There are no parallel workers. The matrix size is capped at
2048. The program checks the compute governor and preserves flushed CSV output
if distress is reported. Peak memory and requested thread limits are saved.

`simulate.py` uses Hermitian Brownian increments with diagonal variance dt and
E|off-diagonal increment|^2=dt. It samples at Brownian times
u=exp(2*s*n^(-1/3)), beginning at u=1, then divides eigenvalues by sqrt(u).
This is the exact stationary matrix OU clock of the report. It separately
simulates stationary independent-entry tridiagonal OU with chi radii, using
exact noncentral chi-square transitions. Each path gives the two top edge-scaled
eigenvalues at s=0,0.25,1,3. Replicates are independent; observations at the four
times within a replicate are coupled. RNG streams are separated by model and
matrix size with NumPy SeedSequence. Raw samples are CSV, not matrix dumps.

`analyze.py` computes paired-time Pearson correlations, 500-resample percentile
bootstrap intervals, mean squared increments and their standard errors, and a
standalone SVG figure. The same random seed reproduces the summaries. The
n=2048 dense run has only 12 replicates and must be interpreted as a pilot.

`audit_math.py` checks matrix normalization and radial transition moments
independently, compares the eigenvalue noise-energy formula with derivatives
in the full Gaussian coordinate representation, checks deterministic
min-max/Sobolev inequalities on samples, and checks the Airy Laplace powers.

`fetch_text.py URL NAME` fetches a PDF into memory and streams it through
pdftotext, retaining only sources/NAME.txt and a plain-text metadata file.
No source PDF, screenshot or scan is written. `fetch_core_sources.py` downloads
the initial core set; the remaining exact URLs are in the metadata files.
`index_sources.py` rebuilds the text/source theorem index. PDF page numbers are
one-based form-feed segments. `format_report_math.py` records a one-time repair
of the initial inline math formatting and is not needed to reproduce results.
