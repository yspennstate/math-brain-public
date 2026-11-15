VERDICT: PARTIAL quantitative empty-interval reduction for nearest-neighbour spacings

[PROOF.md](PROOF.md) proves a finite-window estimate and an asymptotic
equivalence for the nearest-neighbour part of T089. If N unfolded levels lie
in a window of length W, rho=N/W, and their cyclic empty-interval function
differs from the target integrated survival function by at most delta on
[0,S+h], then

\[
\sup_{0\leq s\leq S}|F_N^{\mathrm{int}}(s)-F(s)|
\leq \frac1N+
\frac{2\delta/h+\omega_F(h)+|\rho-1|}{\rho}.
\]

Here 0<h<=S and omega_F is the target CDF's modulus of continuity on the
relevant compact interval. The 1/N term removes the artificial cyclic gap.
Physical and cyclic empty probabilities differ by at most s/W. Both of these
edge constants are attained in the finite checks. A finite grid of mesh eta
adds at most eta to the empty-function error.

For a Lipschitz target, optimizing h gives an O(sqrt(delta)) bound. An explicit
family of exact finite spectra proves this exponent is optimal in the general
class: its CDF error is k/N and its empty-function error is (k/N)^2. This
sharpness example uses a uniform target, not GOE. No optimality claim specific
to GOE is made.

Weyl's law makes rho tend to one when the unfolding uses the symmetry sector's
own leading coefficient. Thus proving convergence of the microscopic
empty-interval function to the GOE integrated survival function is equivalent
to the spacing assertion. Full point-process convergence is not proved by
this reduction. The elementary identities are not claimed as new discoveries.

The exact audit is [check_reduction.py](check_reduction.py), with data in
[audit_data.json](audit_data.json) and captured output in
[audit_output.txt](audit_output.txt). Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_reduction.py > audit_output.txt 2>&1
```

Final run: exit status 0; 455 small configurations; independent geometric and
integrated-CDF checks; 17 exact sharpness cases; and 120 further theorem
checks using the full CDF supremum, including both signs of the density
error. Of the latter, 45 gave an internal-spacing bound below one. Runtime
was 2.628 seconds and peak RSS was 15,974,400 bytes, with inherited nice 20
and one process. All mathematical audit arithmetic uses rational numbers.

The sandbox rejected attempts to set OS memory limits and printed a warning
for `nice`; the process was independently verified to inherit nice 20. The
small audit instead used measured RSS/time guards. The initial launch failed
at the resource-limit call before any cases ran; no mathematical check failed.
The complete command history and relevant output are in [LOG.md](LOG.md).

The literature check found related random-family and mesoscopic advances,
recorded with opened primary references in
[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). It found no resolution of the
fixed-billiard microscopic problem within the ten-minute search limit.

What remains uncertain is the essential spectral estimate, not the finite
reduction: no chaotic billiard is shown here to satisfy the empty-interval
criterion. There is also no agreed genericity hypothesis. The next worker
should target equation (10) of PROOF.md for one explicitly specified symmetry
sector, or derive a certified finite-energy bound for that quantity. A smooth
variance estimate cannot simply be differentiated into the missing result.

Task: "push this problem forward by one checkable piece" — received
2026-11-14 approximately 20:54 Asia/Tbilisi (UTC+04).
