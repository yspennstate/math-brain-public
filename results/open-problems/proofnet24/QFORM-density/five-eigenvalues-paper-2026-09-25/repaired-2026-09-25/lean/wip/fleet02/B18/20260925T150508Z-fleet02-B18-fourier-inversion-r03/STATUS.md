# fleet02/B18 — Lemma 2.1(b) inversion WIP

Target: exact repaired source commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa, blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

Fresh LEAN_COVERAGE.md records 226 matching compiled theorem entries. Lemma 2.4 is now fully verified, so the preceding B18 conditioning WIP is obsolete.

This run takes Lemma 2.1(b), the first remaining item in the coverage order. FourierInverseCandidate.lean formalizes the exact paper-normalized inverse candidate, its explicit integral formula, continuity under Integrable φ, an L1 uniform bound, and the specialization to MeasureTheory.charFun μ.

This file is UNCOMPILED WIP and adds zero kernel-verified theorems. The permitted runtime has no lean or lake executable; owner controls prohibit installation and remote workflows.

Smallest mathematical blocker after these candidate sublemmas: prove measure identification. For a probability measure μ with integrable characteristic function, show μ equals Lebesgue measure with the inverse-Fourier density. Mathlib's function Fourier inversion cannot be applied circularly by assuming a density. The repaired paper's Gaussian-smoothing route remains the faithful bridge.
