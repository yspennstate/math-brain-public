# R7-02 mathematical correction — prior borderline Tauberian inference

Model/effort: **UNVERIFIED** — no authenticated runtime model/effort telemetry is exposed.

This immutable correction concerns Section 7.1 of

`research7_2026-09-17/R7-02/runs/2026-09-17/2026-09-17T153136Z__report.md`

(created at `79243342ed8dbb870397158421bd5b7784791737`). It does **not** modify that historical report.

## Correction

The earlier report claimed that eventual monotonicity of a positive sequence `epsilon_n`, together with

\[
\sum_{j\le n}\varepsilon_j=c\log n+O(1),
\]

would imply

\[
n\varepsilon_n\to c.
\]

That borderline Tauberian implication is **false**. Consequently, the conditional theorem in that section — whose last step used only this implication — is **withdrawn as proved**. In particular, the previously stated condition

\[
\liminf \pi_n/\varepsilon_n^2>1/2
\]

still gives eventual monotonicity through the exact endpoint recurrence, but the argument on file does **not** by itself complete Conjecture 4(b).

## Exact abstract counterexample to the Tauberian step

Fix `c>0`. For every integer `k>=0` and

\[
2^k\le n<2^{k+1},
\]

define

\[
a_n:=\frac{c\log 2}{2^k}.
\]

Then `a_n` is positive and nonincreasing, and `a_n=Theta(1/n)`. Each complete dyadic block contributes exactly

\[
\sum_{n=2^k}^{2^{k+1}-1}a_n=c\log2.
\]

Writing `n=2^k+j` with `0<=j<2^k`, the partial-block contribution is

\[
\frac{jc\log2}{2^k},
\]

whereas

\[
c\log n=ck\log2+c\log(1+j/2^k).
\]

Thus the difference between `sum_{i<=n}a_i` and `c log n` is uniformly bounded: it is a fixed initial constant plus

\[
c\left[(j/2^k)\log2-\log(1+j/2^k)\right],
\]

which is bounded for `0<=j/2^k<1`. Hence

\[
\sum_{i\le n}a_i=c\log n+O(1).
\]

But

\[
na_n=c\log2\,(n/2^k)
\]

oscillates between values approaching `c log2` and `2c log2`; it does not converge. This directly invalidates the monotone-density step used in the earlier proof.

## What remains valid

The exact endpoint increment identity, the exact two-point critical obstruction to global monotonicity, and the implication from `liminf pi_n/epsilon_n^2>1/2` to **eventual monotonicity** remain valid. Only the final inference from eventual monotonicity plus a logarithmic partial-sum law to the pointwise coefficient is withdrawn.

The newer report

`research7_2026-09-17/R7-02/runs/2026-09-17/2026-09-17T172448Z__report.md`

(created at `94bc9882ad71ed69b8f8bca7f699b811b95ec9a8`) explicitly avoids this same borderline inference for the monotone tilted second moment `M_n`; its new autonomous tilted-law, Lyapunov, dual-moment, and reciprocal-harmonic identities are not affected by this correction.

A valid route to pointwise Conjecture 4(b) now needs **additional dynamical regularity** beyond eventual monotonicity and the bounded-remainder logarithmic sum, for example a sufficiently sharp bound on relative one-step variation or on the coercive moment increments from the new tilted-law formulation.

Status impact: `C_D0059` remains `0/2`; no source-level closure is claimed.
