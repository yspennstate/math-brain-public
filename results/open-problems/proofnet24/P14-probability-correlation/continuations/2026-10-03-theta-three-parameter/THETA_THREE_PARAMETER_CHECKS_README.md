# Reproduce the three-parameter theta checks

With Python 3 and SymPy 1.14.0, run

    python random_cluster_research/theta_three_parameter_apex_stability_exact.py

The symbolic run takes roughly one minute. Expected output: `PASS`, 712
unit-weight augmented forests, 32 monomials, seven pair orbits, and 31 exact
identity/positive-form checks.
