# r57 deterministic checks

The algebraic diagnostic in `check_r57.py` uses fixed seed 0. It samples random invertible symmetric `3 x 3` matrices `B`, unit hub-null candidates `w`, constructs the physical hub diagonal so `(B+D_H)w=0`, and places arbitrary tail columns in `(Bw)^perp`.

For every admissible instance it checks the exact global-null equations and the weighted Gram/Pluecker identity

`det G_i = ||Z^T e_i||_2^2 + (1-n_i^2) pdet_+(ZZ^T)`.

A local execution over 10,000 attempted instances (all three deletion indices on each admitted instance) produced a maximum normalized discrepancy of approximately `1.70e-14` and no failed null equations. This is a floating-point sanity check only. The proof in `REPORT.md` is the exact null algebra plus Cauchy--Binet and does not depend on the finite test.
