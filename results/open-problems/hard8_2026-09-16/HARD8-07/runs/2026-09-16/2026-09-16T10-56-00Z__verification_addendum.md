# HARD8-07 — verification addendum for anisotropic portal iteration

This append-only note records exact GitHub readback receipts and deterministic finite-check outputs for the 10:38Z/10:50Z research iteration. It does not change the open status of the classical Littlewood conjecture.

## 1. Main mathematical report

Path:

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T10-38-04Z__report.md`

Creation commit:

`71eb75abd1c2c10b5d0cd7a9dc7992078f6d4e8c`

Exact-commit readback succeeded. Returned blob SHA:

`3453c6aa65ec4ea3aea9742dcadc6f1058cf6dff`

Status: **VERIFIED**.

The report proves the anisotropic signed-portal estimate
\[
q\|q\alpha\|\|q\beta\|
\le
2(A_\beta+2)R\,|v-z\eta_n|\,\rho_{m,n}(z,v)
+(A_\beta+2)^2R^2D_n\frac{|v-z\eta_n|}{B_{m+1}^2},
\]
and derives the thin-strip criterion, strip-population lemma, pairwise phase-separation theorem under a hypothetical counterexample, and exact modular-zero lattice determinant identity.

## 2. Adjacent beta-frame conjugacy strengthening

Path:

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T10-50-00Z__report_part2_coordinate_conjugacy.md`

Creation commit:

`801b8f43e0103c4538a1272fedf72d6e8c44af9d`

Exact-commit readback succeeded. Returned blob SHA:

`f47b94cfa7169da29419072e9fe70271831128e4`

Status: **VERIFIED**.

The strengthening proves the exact unimodular transition
\[
T_n(z,v)=(v-d_{n+2}z,z),
\]
with
\[
q_{n+1}(T_nu)=q_n(u),
\qquad
\ell_{n+1}(T_nu)=-\eta_{n+1}\ell_n(u),
\]
and exact invariance of every fixed-alpha modular phase. Therefore the beta continued-fraction recurrence by itself cannot create an independent cross-scale packing constraint; genuine new information must enter through alpha-frame changes or a frame-free dynamical invariant.

## 3. Exact anisotropic verifier

Path:

`hard8_2026-09-16/HARD8-07/artifacts/2026-09-16T10-38-04Z__anisotropic_portal_verifier.py`

Creation commit:

`a67b8d01ffc38f58d3573a7cc607d76a8804ed4f`

Exact-commit readback succeeded. Returned blob SHA:

`513567c5af872d99801ae5c018480f6d8130c150`

Status: **VERIFIED**.

The source was executed locally with Python standard-library exact integer arithmetic and `fractions.Fraction`. Output:

```text
HARD8-07 anisotropic portal verifier: PASS
portal_checks=2880
tail_identity_checks=60
phase_difference_checks=790
modular_zero_checks=222
strip_population_checks=264
```

The checks cover exact finite continued-fraction reconstructions, the tail identity, the anisotropic inequality, the tail-convergent identity, phase-difference identity, exact modular-zero determinant/lower-bound checks, and deterministic strip-population instances. They are finite consistency checks, not independent verification of the universal conjecture.

## 4. Exact adjacent-frame conjugacy verifier

Path:

`hard8_2026-09-16/HARD8-07/artifacts/2026-09-16T10-50-00Z__adjacent_frame_conjugacy_verifier.py`

Creation commit:

`b53256037cf0583bf5893db72d80f07ad56d9aa4`

Exact-commit readback succeeded. Returned blob SHA:

`a5793891f0367ef45e7eaa6454fac7a0391836e2`

Status: **VERIFIED**.

Exact execution output:

```text
HARD8-07 adjacent-frame conjugacy verifier: PASS
coordinate_checks=5616
phase_checks=44928
norm_distortion_checks=5616
```

## 5. Last completed mathematical step

The strongest new necessary condition is now two-layered.

First, if
\[
\Lambda=\liminf_{q\to\infty}q\|q\alpha\|\|q\beta\|>0,
\]
then every admissible near-tail strip containing \(\asymp RS\) portals must map under the matched alpha modular phase to a circle packing with pairwise spacing \(\gg1/(RS)\). This remains true in almost-linear coefficient ranges when the beta-tail strip is thin.

Second, adjacent beta frames are exactly conjugate. Therefore repeated critical packing at consecutive beta indices is not by itself an additional constraint. The next genuine target is simultaneous near-critical packing under **successive alpha modular phases** for the same beta-resonant q-set, or an equivalent frame-free diagonal-flow statement.

The classical Littlewood conjecture remains **OPEN**.