VERDICT: PARTIAL GOE target remainder below 10^-6 at order 10 instead of 58

The round 4 bound and its order-58 constant hold. An independent audit
checked 150 exact evaluations by two formulas, 2,145 binomial identities,
and 16,245 target-only comparisons for 57 rational count laws, including
a rare count-64 cluster. The main claim was also re-derived analytically.

The new result is a Vandermonde bound for every GOE bulk factorial moment,
proved in [PROOF.md](PROOF.md). If Z_s counts the unit-intensity GOE bulk
points in (0,s] and b_k(s)=E binom(Z_s,k), it gives

\[
\sup_{0\leq s\leq2}b_{10}(s)
\leq\frac{517386}{10^{12}}<10^{-6},
\qquad
\sup_{0\leq s\leq2}b_{20}(s)<10^{-89}.
\]

Thus the predecessor's proposed order-20 target is proved. The preceding
target-only comparison now needs ten empirical moment errors:

\[
\sup_{s\leq2}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{j=1}^{10}\sup_{s\leq2}|a_j(s)-b_j(s)|
+\frac{517386}{10^{12}}.
\]

The grid version adds its target-table errors and grid mesh as before.
The first even orders for this new rational bound to reach 10^-6 are
6,8,10 at R=1/2,1,2. These are thresholds of the bound, not of the
actual GOE moments.

The proof applies Newton divided differences only to the smooth rows and
columns of the orthogonal sine Pfaffian. Their congruence extracts a full
Vandermonde factor. Fourier derivative bounds control the remaining rows;
monic Chebyshev polynomials bound the Vandermonde on an interval. The
discontinuous sine-integral block is left untouched. The kernel convention
was checked in Alexander I. Bufetov, Pavel P. Nikitin, Yanqi Qiu,
*On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.
No novelty is claimed for the standard interpolation or determinant tools.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_repulsion.py > repulsion_output.txt 2>&1
```

Both passed. The new audit compares 72 exact fourth-power evaluations
against an independently constructed entrywise envelope matrix. It checks
20 polynomial-kernel congruences, including reversed and tightly clustered
nodes, 440 recursive versus barycentric divided differences, 40 determinant
versus Pfaffian identities, and 72 exact Vandermonde matrix cases. The
polynomial models check algebra; they are not GOE samples. Exact constants
are in [repulsion_data.json](repulsion_data.json).

The runs took 0.563 and 0.329 seconds, with measured peak RSS below 18 MB,
one process, standard-library arithmetic, and inherited nice=20. The sandbox
prints a setpriority warning; each script independently verifies its actual
priority. Measured memory/time guards were used; no OS-enforced cap is claimed.

The crude estimate |Vandermonde|<=R^(k(k-1)/2) was too weak at order 20.
The Chebyshev bound supplies the missing interval factor. No mathematical
check of the final result failed. The discontinuous block, coincident-node
null set, smooth-block diagonal, normalization powers and k=1 endpoint
were checked separately; details and commands are in [LOG.md](LOG.md).

The under-five-minute literature check found no resolution of the fixed
chaotic-billiard microscopic spacing problem. The opened papers and their
scopes are recorded in the log. This is a bounded search result.

No billiard moment error was estimated, no billiard eigenvalues were
computed, and no certified GOE moment tables were produced. The BGS
conjecture remains unresolved. The new bound still loses information in
both Hadamard inequalities and the maximum bound on the Vandermonde.

Next worker: construct certified GOE target tables b_1,...,b_10 on a finite
grid in [0,2], using integration with rigorous error bounds, then insert
them into this ten-moment certificate. An alternative is to evaluate the
ordered Vandermonde integral rather than its maximum to sharpen (2).
Controlling empirical moment errors for a specified billiard symmetry
sector remains the central missing spectral input.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 08:09 Asia/Tbilisi (UTC+04).
