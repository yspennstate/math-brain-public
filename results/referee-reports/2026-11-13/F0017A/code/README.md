# Reproducing the F0017 experiment

Run from the project root. The two C++ programs use one thread and require an inherited nice value of at least 10. The managed shell here already has nice 10. No external numerical libraries are used by the experiments.

```sh
clang++ -O3 -std=c++17 code/enumerate.cpp -o code/enumerate
clang++ -O3 -std=c++17 code/integer_fourier.cpp -o code/integer_fourier
python3 code/validate.py
python3 code/run_experiments.py
python3 code/audit_large.py
python3 code/analyze.py
```

If your shell is not already at nice 10, run the commands at that priority using your operating system's supported mechanism. The experiment runner skips completed dimensions; deleting a data file deliberately reruns that dimension. No task is scheduled or detached.

`enumerate exhaustive n` enumerates equally weighted off-diagonal representatives for n<=6. `integer_fourier n` reproduces the same histogram using an independent integer-only permutation expansion and Walsh transform. `enumerate monte n count seed` samples uniform independent off-diagonal signs and checks the entire diagonal cube for every sample. All random bits use the least significant bit of successive `std::mt19937_64(seed)` outputs, in row-major order, skipping the diagonal. The run plan and seeds are explicit in `run_experiments.py`.

`enumerate values n row_bits...` emits every determinant, indexed by the absolute diagonal mask, for n<=10. Bit i=1 means diagonal +1. `enumerate audit n row_bits...` re-enumerates a saved off-diagonal matrix through n=24 and emits zero and nonzero witnesses. In row_bits[i], bit j=1 means off-diagonal entry +1, and bit j=0 means -1; bit i is ignored. No original random diagonal is needed because full stubbornness is invariant under its choice.

The main program evaluates the determinant's multilinear polynomial by recursive diagonal branching and exact Schur complements in the field with prime modulus 2^61-1. A 2x2 block or ordinary row-pivoting fallback handles zero pivots. The field calculation recovers the exact signed integer determinant, not merely its zero status: Hadamard's bound is below half the prime for all n<=24. Every sample checks both Fourier identities from the report. The large witness audit also checks selected zero/nonzero determinants by independent Python integer Bareiss elimination.

The implementation retains only recursion matrices and aggregate statistics. There is no exponential array in the Monte Carlo runs. macOS in this sandbox rejects setrlimit; allocation is bounded by the explicit dimension limit and fixed arrays, and the witness audit records peak child RSS. The source downloader keeps PDFs in memory only and writes extracted text with explicit PDF-page markers. It requires `requests` and `pypdf`; it never writes a PDF file.

`analyze.py` produces complete count distributions, descriptive statistics, Wilson intervals, a finite-size fit and an original SVG plot. Quantiles use linear interpolation between ordered observations; confidence intervals concern independent sampled off-diagonal matrices, not the dependent diagonal assignments within a matrix.
