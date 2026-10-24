# The maximal Kemeny constant of an n-vertex graph

Verification code accompanying the paper by Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

## Lean certificate

`lean/ScalarGap.lean` contains two declarations: the denominator-cleared scalar identity over the integers and identity (3.10) over the rationals. It uses Lean core only, without Mathlib. The manuscript's recorded compiler version is Lean 4.34.0, pinned independently in `lean/lean-toolchain` so this certificate does not alter the repository's other projects.

From this directory, with Lean installed through elan:

```sh
cd lean
lean ScalarGap.lean
```

The certificate does not formalize the effective-resistance decomposition, the graph arguments, the real-variable inequality, or the full asymptotic theorem. The equation number in its comments has been aligned with the paper; the theorem statements and proofs are unchanged.

## Computational checks

With Python 3.10 or later, from this directory:

```sh
python -m pip install -r requirements.txt
python check_kemeny.py > check_kemeny_output.json
python large_order_checks.py > large_order_output.json
```

`check_kemeny.py` performs exact rational checks of finite resistance and hitting-time identities, the bridge identity, edge-deletion comparisons, the refined resistance bound, the exponent balance, and multipartite barbells. `large_order_checks.py` performs floating-point spectral calculations, including an exhaustive small-order graph search and one exact rational cross-check. Its small-order maximum calculations are floating-point, not exact-arithmetic certificates.

The JSON files retain the recorded results supplied with the manuscript. They are not a claim of a new execution on publication of this directory. Finite numerical checks do not prove the all-order theorems.

No manuscript, audit reports, research logs, or unrelated private materials are included here.
