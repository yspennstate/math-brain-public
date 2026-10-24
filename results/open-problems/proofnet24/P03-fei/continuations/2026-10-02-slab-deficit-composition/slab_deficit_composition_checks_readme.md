# Reproduce the deficit and parity checkpoint

Python3 and NumPy are sufficient. No script imports a campaign helper.

    python independent_universal_split_check.py
    python verify_parity_modulation.py

The first script exhausts all65,814 Boolean functions from dimension0
through4 and all262,948 coordinate pivots. Walsh, influence, variance and
deficit identities use integers; entropy is a double-precision sanity
check with stated tolerance2e-11. It includes signed mean-zero derivatives
and nonconstant derivatives of influence one. The universal analytic
inequality is proved in the full report, not inferred from enumeration.

The second exhausts all7,778 monotone functions through dimension5 and
all245,470 output character modulations. It verifies the entire squared
spectral permutation and each physical influence identity EXACTLY, with
integer arithmetic. Entropy invariance follows from the exact permutation;
no entropy tolerance or fitted FEI constant is used. The influence-budget
comparison is also integer exact. A two-bit parity checks the boundary
of the generic high-influence hypothesis.

Root read both scripts in full and reran them with exit status zero.
Their JSON outputs are included. The complete signed-split theorem has
separate adversarial and root analytic audits. The parity theorem has a
separate heat-entropy analytic audit. The disjoint-product theorem has a
separate adversarial audit; its exact tensorization argument needs no
numerical experiment.

Read the full proofs and the previous strong LTF and slab proofs for the
class-wide constants. Numerical checks do not establish those constants,
the full FEI conjecture, novelty or external acceptance.
