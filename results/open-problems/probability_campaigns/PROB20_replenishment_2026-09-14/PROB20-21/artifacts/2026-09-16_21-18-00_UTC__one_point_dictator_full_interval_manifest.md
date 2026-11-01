# PROB20-21 coverage manifest — one-point dictator perturbation

Status: **PARTIAL relative to the source conjecture; COMPLETE for this named special function.**

Target function in `{0,1}` coding:

`f(x)=x_1` except `f(1,1,1,1,1,1,1)=0`.

Equivalent `{-1,+1}` form: `f_tilde(x)=x_1-2*1_{x=1^7}`.

Certified new interval in this artifact pair: `alpha in [1/5000,67/135]`.

Prior durable all-function endpoint certificates already cover `[0,1/5000]` and `[67/135,1/2]`. Therefore this one named seven-bit function is now certified for the complete interval `alpha in [0,1/2]`.

This does **not** certify all seven-bit Boolean functions on the middle interval and therefore does **not** move the frozen task metric. Frozen metric remains `n=6` for complete all-function/full-noise certification.

Checker: `2026-09-16_21-18-00_UTC__one_point_dictator_full_interval_cert.py`.

Executed output: `2026-09-16_21-18-00_UTC__one_point_dictator_full_interval_cert.out` ending `PASS`.

Proof split:
- `[1/5000,37/100]`: exact rational interval enclosure on 740 cells of width `1/2000`; smallest certified lower bound approximately `4.006871253409505e-05` nats.
- `[37/100,67/135]`: Pinsker/chi-square endpoint reduction plus exact degree-16 Bernstein negativity on the stronger correlation domain `rho in [0,13/50]`.

Review level: self-review plus executed exact-arithmetic certificate. No P26 or distinct OTHER-task audit of this special-case claim is recorded here.
