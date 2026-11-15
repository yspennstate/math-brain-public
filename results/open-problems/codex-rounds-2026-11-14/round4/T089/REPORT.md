VERDICT: PARTIAL GOE target remainder below 10^-6 at order 58 instead of 390

The earlier target-only comparison and its order-390 bound hold. An independent
exact checker verified 6,561 binomial identities, 36,125 comparisons for
85 rational count laws, and the old remainder by both a direct factorial
formula and a recurrence. Rare large clusters were included.

The new result is proved in [PROOF.md](PROOF.md). If Z_s is the unit-intensity
GOE bulk interval count and b_k(s)=E binom(Z_s,k), then

\[
\sup_{s\leq R}b_k(s)\leq
\frac{R^k}{k!}\left[k\left(k+\frac{\pi^2}{12}(k-1)\right)\right]^{k/4}.
\]

The proof combines the orthogonal sine kernel, the elementary inequalities
|I|<=1/2 and S^2+3D^2/pi^2<=1, and Hadamard's determinant bound after a
determinant-one diagonal congruence. The kernel was checked in Alexander I.
Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point
Processes*, [arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.
No novelty is claimed for these general linear-algebra ingredients.

At R=2 this gives the exact rational certificate

\[
\sup_{s\leq2}b_{58}(s)\leq913317/10^{12}<10^{-6}.
\]

It replaces the earlier certificate's order 390 by 58 without an empirical
count-tail assumption. Thus

\[
\sup_{s\leq2}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{j=1}^{58}\sup_{s\leq2}|a_j(s)-b_j(s)|+913317/10^{12}.
\]

The proof also gives the corresponding grid and spacing certificates. The
first even orders for the rational upper-bound formula to reach 10^-6 are
14,26,58 at R=1/2,1,2. These are thresholds of the bound, not of the actual
GOE moments.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_round3.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_remainder.py > remainder_output.txt 2>&1
```

Both commands passed. The new audit checks 150 exact factorial/product
evaluations and 120 rational matrix cases, comparing determinants and
Pfaffians independently and checking the scale change and row bounds.
Its exact constants are in [remainder_data.json](remainder_data.json).
The runs took 0.631 and 0.068 seconds, with measured peak RSS below 16 MB,
one process, standard-library arithmetic and inherited nice 20. The sandbox
prints a nice warning; each script independently checks its actual priority.
Measured memory/time guards were used; no OS-enforced cap is claimed.

No mathematical check failed. A second Cauchy–Schwarz proof verified the
kernel inequality. Partial sine lobes, negative arguments, I's jump at zero,
the diagonal contribution and the determinant square-root exponent were
checked separately. Two log-append patches failed without changing files;
their replacements succeeded. Details and outputs are in [LOG.md](LOG.md).

The under-five-minute web check found no resolution of the fixed-billiard
microscopic spacing problem. Opened primary sources and their precise scopes
are recorded in the log. This is a bounded search result.

No chaotic billiard moment error was estimated, no billiard eigenvalues were
computed, and no certified GOE moment tables were produced. The central BGS
obstacle is unchanged. The bound is still conservative; it discards most
repulsion between nearby points.

Next worker: retain the target-only comparison and construct certified GOE
factorial-moment tables on a finite grid in [0,2], or reduce the remainder
order further by retaining the near-diagonal repulsion in the Pfaffian. The
concrete analytic target is b_20(2)<=10^-6; the present bound does not show
this. Any numerical integration needs a rigorous error bound, not a Monte
Carlo estimate. Estimating a_j-b_j for one symmetry sector remains essential.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 04:46 Asia/Tbilisi (UTC+04).
