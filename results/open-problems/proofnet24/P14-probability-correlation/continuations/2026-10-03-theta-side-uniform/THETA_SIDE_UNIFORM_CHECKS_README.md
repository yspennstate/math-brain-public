# Reproducing the side-uniform theta exact checks

Run from the repository root with Python 3 and SymPy 1.14.0:

    python random_cluster_research/theta_uniform_apex_stability_exact.py

Expected result: `status: PASS`, 712 enumerated forests, 32 polynomial
monomials, four Rayleigh pair orbits, and 18 exact symbolic identity checks.
The script rewrites
`theta_uniform_apex_stability_exact_results.json` deterministically.

The computation verifies the algebra in the proof; the proof of global
nonnegativity is the positive-eigenvalue and quadratic-discriminant argument
written in the note.
