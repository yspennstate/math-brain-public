---
name: a_ratio_already_in_bits_was_divided_by_ln2_again_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 09:2x: a new scan divided ratio_multi (already in bits) by ln 2 and printed 5.76 bits for a square wave at n = 513, a fake break of the 4.8723 bound. A brute-force Walsh-Hadamard check at n = 11-15 found the factor 1.4427 = 1/ln 2; the true value is 3.99 bits."
metadata:
  node_type: memory
  type: feedback
  status: verified
  modified: 2026-11-08T14:30:26.754Z
---

On 8 Nov, measured in an earlier session, sym_wave_offset_scan.py printed Delta_1/I_1 = 5.76 bits for a J = 16, d = 4 square wave at n = 513. That would have broken the conjectured 4.8723 for symmetric f (see [[fei_bottom_band_mass_proved_by_noise_operator_alternating_sum_2026_11_08]]).

- ratio_multi in fei_sym_54e83a7b/sym_band_mass_multi.py already returns bits, and the new script divided by log(2) once more.
- The independent brute force (sym_brute_check.py, which builds f on {0,1}^n and runs a Walsh-Hadamard transform) differed from it by exactly 1.4427 = 1/ln 2 on every table. With that factor removed the two agree to six digits.
- The true value is 3.998 bits.

**Why:** a number that breaks a conjecture is a bug until an independent route agrees with it. Here the second route found the bug within one run.

**How to apply:**
- Before converting units, read what a helper returns.
- When a result would beat a published bound, run the brute-force route at small n first.
- When a ratio is off by exactly 1.4427 or 0.6931, look for a double or missing ln 2.
