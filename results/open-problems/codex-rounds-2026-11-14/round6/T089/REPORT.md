VERDICT: PARTIAL nine-moment GOE certificate from exact Vandermonde integration

The round 5 bound holds. An independent derivation and exact arithmetic audit
confirmed its order-10 and order-20 constants, 72 formula-versus-envelope
comparisons, and its stated even-order thresholds.

The new result in [PROOF.md](PROOF.md) integrates the preceding Vandermonde
envelope exactly. For the unit-intensity GOE bulk count Z_s, put
b_k(s)=E binom(Z_s,k). It gives

\[
\sup_{s\leq2} b_9(s)<\frac{55771279}{10^{15}}<10^{-6},
\qquad
\sup_{s\leq2} b_{10}(s)<\frac{8253203}{10^{18}}<10^{-11}.
\]

The order-10 bound improves the predecessor's bound by a factor greater than
60,000. The first successful order of the new bound at R=2 is 9; the old
bound exceeds 10^-6 at every order through 9, including odd orders.
These are thresholds of explicit upper bounds, not of the actual moments.

The exact identity used is

\[
\int_{0<x_1<\cdots<x_k<1}\prod_{i<j}(x_j-x_i)\,dx
=\frac1{k!}\prod_{i<j}\frac{j-i}{i+j}.
\]

The proof includes both parities, the determinant-to-Pfaffian integration
identity, and the Pfaffian product evaluation. No novelty is claimed for
these standard identities. The GOE kernel input was checked in Alexander I.
Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point
Processes*, [arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.

Adjacent inclusion-exclusion sums also work at odd orders. Thus, for any
empirical interval count with moments a_j(s) and void probability V(s),

\[
\sup_{s\leq2}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{j=1}^{9}\sup_{s\leq2}|a_j(s)-b_j(s)|
+\frac{55771279}{10^{15}}.
\]

No empirical count-tail assumption is needed. The grid version adds target
table errors and the maximum grid step. The earlier spacing reduction then
applies unchanged.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_integration.py > integration_output.txt 2>&1
```

Both passed. The integration audit compares 54 exact determinant integrals
by signed monomial integration, recursive Pfaffian expansion, and pair
products, including ordinary dimensions 1 through 14, odd dimensions,
reversed exponents and repeated rows. It also checks 100 bound evaluations
against an entrywise envelope, 14 uncancelled integral evaluations, and
38,988 target-only comparisons for 57 rational count laws, including rare
count-64 clusters. Exact data are in [integration_data.json](integration_data.json).

The two runs took 0.103 and 0.888 seconds, with measured peak RSS below
18 MB, one process, standard-library arithmetic and actual nice=20.
The sandbox emits a nice warning; each script independently checks its
inherited priority. RSS/time guards are measured, not OS-enforced caps.

What failed: order 8 still does not reach a 10^-6 remainder at R=2.
No mathematical check failed. One log-formatting patch missed its context
and changed no files. Factorials, odd-order signs, the dummy atom, scaling,
coincident nodes, R=0 and k=1 were checked separately in [LOG.md](LOG.md).

The under-five-minute literature check found no resolution of the stated
fixed-billiard microscopic problem; opened papers and their scope are in
the log. This is a bounded search result.

No billiard moment errors, billiard eigenvalues or GOE moment tables were
computed. BGS remains unresolved. The new bound still loses information
in the pointwise derivative and Hadamard estimates. Its numerical constants
are certified bounds, not approximations to the moments themselves.

Next worker: construct certified GOE target tables for b_2,...,b_8 on a
rational grid in [0,2]. Here b_1(s)=s exactly, and b_9 can use the enclosure
0<=b_9(s)<=55771279/10^15 in the grid certificate. A first checkable table
is b_2, whose two-point kernel reduces the integral to one dimension.
Estimating the empirical moment errors for a specified chaotic-billiard
symmetry sector remains the central missing spectral input.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 10:40 Asia/Tbilisi (UTC+04).
