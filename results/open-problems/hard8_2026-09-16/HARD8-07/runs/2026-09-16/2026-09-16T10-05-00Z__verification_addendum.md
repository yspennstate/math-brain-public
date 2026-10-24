# HARD8-07 — verification addendum for signed-portal iteration

This append-only note records publication/readback receipts and deterministic finite-check results for the signed-portal iteration. It does not change the open status of the classical Littlewood conjecture.

## 1. Main report receipt

Path:

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T09-36-51Z__report.md`

Creation commit:

`84fd0a717386f3d81090797a75ba8bbcb6d192fc`

Exact-commit readback succeeded. Returned blob SHA:

`c97fb361d492266de97eb91d1f995e2c7032bd48`

Status: **VERIFIED**.

## 2. Scale-optimization strengthening receipt

Path:

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T09-58-00Z__report_part2_scale_optimization.md`

Creation commit:

`98c8511cb17883ea65792ca122210c49d45c1b28`

Exact-commit readback succeeded. Returned blob SHA:

`44d05feb4b596a6fe8983c1a937c9609d9efab2c`

Status: **VERIFIED**.

The strengthening is important: the first report's inherited Matala scale gives a signed coefficient range `R=o(D_n^(1/9))`; the free-scale re-optimization shows that the matched choice `B_{m+1} <= D_n < B_{m+2}` improves this to

\[
R=o(D_n^{1/3}).
\]

The full scale-free bound is

\[
q\|q\alpha\|\|q\beta\|
\le
4(A_\beta+2)R^2\rho_{m,n}(z,v)
+2(A_\beta+2)^2\frac{R^3D_n}{B_{m+1}^2}.
\]

## 3. First exact verifier receipt

Path:

`hard8_2026-09-16/HARD8-07/artifacts/2026-09-16T09-36-51Z__signed_portal_dirichlet_verifier.py`

Creation commit:

`ae396686909d90bd69e539cf893f30769d5b1d36`

Exact-commit readback succeeded. Returned blob SHA:

`d072581e71869c0eec3d7b816f3f6a86473688da`

Status: **VERIFIED**.

The deterministic exact checks corresponding to this source were executed locally with Python standard-library integer arithmetic and `fractions.Fraction` and returned:

```text
HARD8-07 signed-portal exact verifier: PASS
lemma_checks=207232
portal_checks=14000
modular_checks=14000
dirichlet_checks=250
```

The checks cover finite bounded continued fractions, the bounded-type signed-portal lower bound, the exact modular inverse identity, and the finite two-dimensional Dirichlet inequality. They are finite consistency checks, not independent verification of the universal conjecture.

## 4. Matched-scale exact verifier receipt

Path:

`hard8_2026-09-16/HARD8-07/artifacts/2026-09-16T09-58-00Z__matched_scale_verifier.py`

Creation commit:

`133e15504208ac9d4509c2b8b1bf31390432fd6e`

Exact-commit readback succeeded. Returned blob SHA:

`214d2d340f9a3d8b891a92b963e8fc243fdfcb26`

Status: **VERIFIED**.

The deterministic exact checks corresponding to this source were executed locally and returned:

```text
HARD8-07 matched-scale exact verifier: PASS
matched_scale_checks=54
modular_checks=14760
```

These verify the finite matched-scale denominator comparison and the centered modular coordinate identity on deterministic bounded-digit test families.

## 5. Last completed mathematical step

The run ended with the scale-free signed-portal inequality and its matched-scale consequence: a counterexample pair would have to make the structured rational torus points

\[
\Theta_n^*
=
\left(
\frac{D_nA_{m_*+1}}{B_{m_*+1}},
\frac{D_{n+1}A_{m_*+1}}{B_{m_*+1}}
\right)
\pmod1
\]
constant-factor extremizers of two-dimensional Dirichlet approximation on **every** coefficient scale

\[
R_n\to\infty,
\qquad
R_n=o(D_n^{1/3}).
\]

Equivalently, if along any such scale the best short character improves from the generic `O(R_n^-2)` bound to `o(R_n^-2)`, Littlewood follows for the pair.

The next attack should combine the modular short-character error with the much finer beta-tail factor `|v-z eta_n|` instead of using the crude worst-case `O(R^2)` beta cost. Pure cardinality/volume arguments are expected to remain critical, so a successful gain must use the continued-fraction recurrences.

The full classical Littlewood conjecture remains **OPEN**.