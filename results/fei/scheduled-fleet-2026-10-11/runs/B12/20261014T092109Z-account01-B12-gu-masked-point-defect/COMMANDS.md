# Commands and deterministic scope

Primary verification command, run from this directory:

`python3 CHECK.py`

The output is preserved byte-for-byte in `CHECK.out`.  There is no random
search and no seed.  Direct Walsh arithmetic uses exact `Fraction` values;
only the final base-two logarithms are floating point.  The all-dimensional
bound is analytic in `PROOF.md`; the dimension-100 scalar sweep is a
reconstruction control, not extrapolation.

The designated positive collision control uses the immutable three-bit
truth tables from the preceding B12 posterior/collision runs.

