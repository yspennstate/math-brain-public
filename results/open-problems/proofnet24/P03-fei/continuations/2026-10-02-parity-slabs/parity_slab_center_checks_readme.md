# Reproducing the slab spectral-center checks

The complete analytic theorem is
[parity_modulated_slabs_center_proof.md](parity_modulated_slabs_center_proof.md).
The original candidate is preserved. The separate local-method failure
is [parity_slab_local_minimum_obstruction.md](parity_slab_local_minimum_obstruction.md).

Run the standalone checker with Python and NumPy:

```bash
python verify_parity_slab_center_heat.py
```

It writes [parity_slab_center_heat_checks.json](parity_slab_center_heat_checks.json).
There are no local helper imports. The deterministic seed is 20261002.

The completed run passed:

| Check | Count |
|---|---:|
| Every Boolean function through four input variables, including n=0 | 65,814 |
| Generic entropy split, minority-density and gluing bounds | 262,948 pivots |
| Genuine weighted interval gates through ten input variables | 3,951 |
| Exact character spectral permutation and flip identities | 61,396 |

Every character is checked on each slab instance through six variables.
For dimensions seven through ten, four characters are sampled per
instance, and the minimizing character is always checked separately.
The interval windows are built from actual attained integer scores,
including singleton attained-score intervals and full-score intervals.
Equal-weight singleton layers are explicitly included, and positive
integer weights with varied magnitudes provide additional interval cases.

Physical influences are integer counts divided by the cube size.
Walsh numerators are computed with integer arithmetic. The high-influence
count, the two crossing-halfspace Chow-square inequalities, character
spectral permutations, centered influence and zero-center cases are
therefore checked exactly. The maximum observed high-influence count
was eight, but the analytic theorem uses the proved uniform bound fifteen.
The larger constant is not replaced by an empirical estimate.

Entropy evaluations and the split/gluing comparisons use floating point
and a stated tolerance. The actual generic inequality
H(centered g)≤average H(terminal restrictions)+4b I(centered g)
is checked directly. The script does not fit or insert a numerical value
for the existential ordinary-slab FEI constant C_slab; it does not assert
the main theorem from a finite entropy/influence ratio.

The result file includes exact failures of the shortcut budget comparison:
two-bit parity is a slab with I−Var=1 and center J=0; the four-bit middle
layer has all influences 3/4, I−Var=33/16 and J=1. The zero-entropy
two-bit example prevents any finite comparison of I−Var to J for the
whole slab class.

Finally, the script probes the separately proved local-minimum failure
for odd N=3,...,19. Its weights and scores are integers, endpoints are
half-integers, and the pivotal influence is asserted exactly as
1−2^(−N). The recorded entropy increments are numerical. The unbounded
ratio is justified by the full analytic Fourier-coefficient argument in
the obstruction proof, not by extrapolating the numerical table.

The separate standalone exact obstruction checker is
[verify_parity_slab_local_obstruction_exact.py](verify_parity_slab_local_obstruction_exact.py),
with [full output](parity_slab_local_obstruction_exact_checks.json). It
passed seven direct truth-table realizations through N=15, 33,125 exact
Fraction coefficient assertions over 250 odd dimensions N=15,...,513,
and 50 separately labeled 100-digit Decimal entropy checks N=3,...,101.
The physical sign-coordinate convention is explicitly converted from
the integer FWHT's (-1)^bit convention. This avoids assigning a wrong
global sign to the exact character permutation while preserving the
same squared-spectrum identity.
