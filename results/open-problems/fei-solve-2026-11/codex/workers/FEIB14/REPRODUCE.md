# Reproduction

Run `python3 reproduce.py` from this folder. It compiles the C programs, reuses the read-only FEIB12 NPN files, and runs the calculations and audits sequentially at nice 10 with numerical libraries restricted to one thread. It saves each command, elapsed time in seconds, CPU time in seconds, peak resident bytes, exit code and log name in resources.json. It does not generate a new NPN census or write into a sibling folder.

Requirements are the existing Mac C compiler, Python 3, NumPy and mpmath. No package installation or network is needed for numerical reproduction. LITERATURE.md records the web sources examined for theorem scope. inherited_audit.py reads the supplied FSYM44 certificate bundle and the later FSYM47 manuscript. audit.json stores hashes of the reused NPN inputs.

The truth-table convention is bit x set iff f(x)=-1, with coordinate zero in the least significant input bit. Masks in saved `params[i][family]` refer to the compressed n-1 coordinates after deleting i, in increasing original-coordinate order. Each pair is [P,N]. Family order is parity, meets, both, size, count(N). Unused mask entries are zero. To restore a compressed mask t to original coordinates use (t & (2^i-1)) | ((t & ~(2^i-1)) << 1). The size family uses no mask.

`witness.c` computes exact integer Fourier numerators and squared masses, then binary64 entropies. Its masked Walsh transforms give every joint parity/meets cell without scanning every T for each mask pair. `audit.py` instead explicitly groups cells, and `audit_large.c` uses direct integer cell sums over all masks on the larger extremizers. `highprecision.py` optimizes the small extremizers again with high-precision logarithms; `final_audit.py` independently scores the larger selected partitions at high precision.

`experiments.py` writes seeded mixed, LTF and monotone draws and exact optimal masks. At n=11..14 it optimizes only parity and total size for LTFs. Other raw fields are valid but unoptimized unconditional bounds; optimized summary fields exclude them. The six-variable monotone arm is sampled, while the slice recursion exhausts all monotone functions through five variables.

`symmetric.c` computes the additional symmetric erasure census, using exact Gray-code coefficient updates. Its masks encode weight-value vectors, not truth tables. `structured.py` audits these against FEIB02's independent finite differences, computes the cardinality-dilution example, and scans every block size for majority. The large XOR and majority examples use spectral/cardinality formulas instead of exponential truth tables. FFT error and normalization diagnostics are saved.

The executable files are small local build artifacts. The runner writes no git state, external messages, deployments, shared memories or mesh entries. `STATUS.md` is updated during reproduction; after rerunning, read REPORT.md for the saved mathematical verdicts, since those are not rewritten by the runner.
