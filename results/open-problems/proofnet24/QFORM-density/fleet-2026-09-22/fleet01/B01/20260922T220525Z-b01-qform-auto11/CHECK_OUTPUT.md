# Exact symbolic checks

The following identities were checked with SymPy using exact integer matrices.

```text
G = Matrix([[3,1,1],[1,2,0],[1,0,2]])
charpoly(G) = (lambda - 4)*(lambda - 2)*(lambda - 1)
eigenvalues(G) = {4:1, 2:1, 1:1}

M = Matrix([[2,1,1],[1,2,1],[1,1,1]])
charpoly(M) = (lambda - 1)*(lambda**2 - 4*lambda + 1)
eigenvalues(M) = {1:1, 2-sqrt(3):1, 2+sqrt(3):1}
det(M) = 1
M - J_3 = diag(1,1,0)
2-sqrt(3) = 0.2679491924311227...
STATUS=PASS
```

These computations verify only the finite-dimensional algebra used in the report; the proof of the structural obstruction is the analytic argument in `REPORT.md`.
