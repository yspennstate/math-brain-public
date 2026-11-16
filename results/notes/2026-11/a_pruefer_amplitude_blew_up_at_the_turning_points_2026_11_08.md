---
name: a_pruefer_amplitude_blew_up_at_the_turning_points_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 12:2x: an equidistribution test weighted levels by a Pruefer amplitude R^2 = (...)/sin^2 psi; at the levels just inside BOTH turning points sin psi -> 0 and one level took 59 percent of the weight, faking a 0.54 harmonic. Excluding the Airy zones removed every spike."
metadata:
  node_type: memory
  type: feedback
  status: verified
  modified: 2026-11-08T17:24:10.970Z
---

In sym_crossover_equid.py the phase of a three-term-recurrence sequence was read off as (k_s, k_{s+1}) = R (cos Th, cos(Th + psi)), so R^2 = (k_s^2 + k_{s+1}^2 - 2 cos psi k_s k_{s+1}) / sin^2 psi.

- Near a turning point cos psi -> 1. At n = 16384, c = 12 the heaviest level had cos psi above 0.99 and carried 59 percent of the weight. Every harmonic read 0.54, which looked like a failure of equidistribution. A milder version (0.03 at c = 8) had first looked like a real stationary-phase effect.
- sym_equid_diag.py printed the five heaviest levels. They sat at BOTH ends, near d^2/N and near N - d^2/N. My first cut only removed the bottom zone, so it could not have fixed this.
- Counting levels with sin^2 psi < 4 (d^2/N)^{-2/3} as outside the band removed every spike (sym_crossover_equid_airy.out).
- The same run first used the wrong weight, f's spectrum C(N,s) a_s^2. That weight sits on the bottom levels, so the harmonics did not fall at all. The right weight is the I-share averaged over the phase.

**Why:** a ratio whose denominator vanishes at the edge of the region turns one boundary level into the whole sum. A three-term recurrence has a turning point at each end of its oscillatory band.

**How to apply:** when a weighted sum jumps, print its heaviest few terms before theorising. Check both ends of the oscillatory band. Linked: [[fei_bulk_bound_for_any_edge_count_by_alternating_charge_energy_2026_11_08]], [[a_fast_fourier_sum_dropped_the_level_zero_term_near_the_middle_2026_11_08]].
