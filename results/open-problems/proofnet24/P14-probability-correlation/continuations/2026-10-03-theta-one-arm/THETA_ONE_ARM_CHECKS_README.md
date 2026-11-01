# Reproduce the one-arm theta checks

With Python 3 and SymPy 1.14.0, run

    python random_cluster_research/theta_one_arm_apex_stability_exact.py

Expected: `status: PASS`, 712 unit-weight augmented forests, 32 polynomial
monomials, five Rayleigh pair orbits, and 22 exact identity/positivity checks.
The adjacent JSON is rewritten deterministically.
