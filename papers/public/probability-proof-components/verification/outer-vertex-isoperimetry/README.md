# Outer vertex-isoperimetry of regular plane tessellations

Verification files accompanying the paper by Yitzchak Shmalo.
Paper: https://github.com/yspennstate/outer-vertex-isoperimetry

## Lean

From this directory, run `cd formal`, `lake build`, and `lake env lean AxiomCheck.lean`.
The local `lean-toolchain` pins this project independently of the other projects in this repository.
The development contains finite integer-arithmetic statements for boundary-update formulas,
defect descent, conditional terminal transfer, and threshold and quadrangular algebra.
It is not a formalization of the infinite-graph theorems or a certification of novelty.
See the source comments for the exact encoded assumptions.

## Exact-arithmetic checks

From this directory, run `python -m pip install -r checks/requirements.txt` and
`python checks/check.py`. The JSON file is the previously recorded output distributed
with the manuscript; copying it is not a fresh execution of the checker.
Finite computations do not replace the proofs in the paper.

The Lean sources, configuration, Python checker, recorded output, and MIT license
were copied without changes from the paper repository.
