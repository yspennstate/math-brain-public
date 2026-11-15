VERDICT: PROVED positive midpoint curvature and a local convex-side collar for the disordered candidate curve when gamma <= u < pi-gamma

This is a deterministic result about the candidate formulas, not a proof
of T133. The parameters are Delta=cos(gamma), 0<gamma<pi/2,
delta=pi-gamma, and T=delta-u.

New beyond round 3: [PROOF.md](PROOF.md) proves C(0)>0 whenever
gamma<=u<delta. In particular it covers equal weights u=T=delta/2
throughout the omitted interval 1/2<Delta<1. Continuity extends the sign
to a neighborhood of the midpoint boundary parameter.

An exact decomposition gives the sign. With h=pi/delta,
R=a''(0)/a(0), q=1/(1-cos T), qh=1/(1-cos(hT)), and
E=cot(T/2)-h cot(hT/2),

\[
2\pi C(0)=E(R-q)+h\cot(hT/2)(h^2q_h-q)>0.
\]

Both trigonometric differences are positive; R-q is nonnegative in
the stated weight range. The proof includes an explicit positive lower
bound. It also shows that the small-B critical branch enters the locally
convex side of the candidate envelope and gives one-to-one coordinates
on a neighborhood on that side. This supplies local uniqueness of small-B
critical parameters, which round 3 left open. It does not exclude other,
distant critical points.

The earlier expansion survives an independent check using scalar Neumann
iteration, composite Gauss quadrature and finite differences. Its two
quadratic constants were also recovered from even moments. Neither script
imports or executes code in the earlier directories.

Reproduce:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py
~~~

The geometry audit passes 40 derivative/decomposition/curvature checks
and three finite-B displacement comparisons. Quadratic-coefficient
extrapolation errors are at most 5.49e-7. Detailed data are in
[geometry_checks.json](geometry_checks.json); commands and material output
are in [LOG.md](LOG.md). Runs take under two seconds each, use under
20 MiB measured peak RSS, and confirm effective nice 20.

What failed: midpoint quadrature initially obscured the smaller
free-fermion residual; fourth-order Gauss quadrature resolves it.
Near a pole, 70-digit arithmetic lost enough precision to fail the
1e-55 identity tolerance; 100 digits resolves it without relaxing that
tolerance. The shell cannot raise the inherited priority from nice 20
to 15. Outside u>=gamma the first sign summand can be negative, so
this sufficient-condition proof does not extend there.

Literature: the bounded check found no newer complete proof. Alexey
Bufetov's [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576)
still presents an announcement, with the interval 1/2<Delta<1 omitted.
No absence claim beyond that bounded search is made.

Remaining gaps: the sign along the whole southwest arc, weights u<gamma,
endpoint control, global critical-point classification, and identification
with the model's limiting height remain unproved here. The collar is
geometric; no probabilistic liquid-region assertion follows from it.
No antiferroelectric extension is claimed.

Next worker: prove C(theta)>0 away from the midpoint. A useful reformulation
is C=-a[(b/a)']^2 d^2(e/a)/d(b/a)^2; thus strict concavity of e/a as a
function of b/a would extend the sign and the same collar argument along
the arc. First address u<gamma at theta=0, where the displayed
decomposition remains exact but its first summand has the opposite sign.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 04:56 Asia/Tbilisi.
