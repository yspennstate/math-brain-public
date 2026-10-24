Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — notation correction for the affine-span/surjection artifact

This immutable note corrects one notation ambiguity exposed on exact-SHA readback of

`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T140843Z__F0003_affine_span_surjection_count_and_modulus_barrier.md`

at creation commit `cbe7de5dcab4414cbc7a27399ed3aed76dce2750`.

In the proof of Theorem 2.2, the sentence

> Since `A` is singular over `Q`, its left kernel over `Q` contains a nonzero rational vector.

uses `Q` ambiguously immediately after `Q` was used for the modulus. It must read:

> Since `A` is singular over **the rational field `\mathbb Q`**, its left kernel over `\mathbb Q` contains a nonzero rational vector.

Nothing else in the proof changes: clearing denominators gives a nonzero integer left-null vector, dividing by the coordinate gcd makes it primitive, and Bézout then shows its reduction modulo the integer modulus `Q>=2` is a surjection `Z^n -> Z/QZ`. Hence the proved inequality

\[
\mathbf 1_{\{\det A=0\}}\le
\frac{|\operatorname{Sur}(\operatorname{cok}A,\mathbb Z/Q\mathbb Z)|}{\varphi(Q)}
\]

is unchanged.

This is a notation-only correction, not new metric movement.