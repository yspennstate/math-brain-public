# Post-publication correction refresh for r16

After the main report was committed, the fresh shared correction stream added `QFORM-LEAKAGE-SLICE-MIXED-NORM-FALSE-v1` (fleet01/B05; canonical report `c2ee90049c201a04657853c8989e63ea92d5dfbc`). It refutes a mechanism that conditions on a heavy-isotropic leakage projection and then replaces conditional `(Y,Z)` laws by an L-infinity slice cap.

The r16 theorem is unaffected: it conditions only on original independent coordinates, never on a rotated/projection leakage variable, and uses the original one-dimensional cap directly before the bathtub/rearrangement step. No conditional joint-density cap or mixed-norm slice supremum is used.

The latest fleet01/B17 one-shared-heavy central theorem (`85b6bbd85c782999a04b6a04403b945678760d66`) is compatible but not needed as a premise. Full QFORM remains OPEN.
