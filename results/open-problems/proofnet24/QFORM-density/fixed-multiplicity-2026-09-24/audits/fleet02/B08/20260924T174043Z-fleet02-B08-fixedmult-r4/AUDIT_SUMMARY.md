# fleet02/B08 fixed-multiplicity audit r4

Historical source pin: 7c0d6e60946b19423e6400a12d34b473cf0591e2 / blob 183ccd294763214e6a707e8d4749ff9a8cf7006d / SHA256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.

Standalone-nine source pin: eeb752c8943536541b34b42b8bf48e924f4d3d2f / blob 19fb119877426b640b2c0dae19ec2f78a399fe11 / SHA256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

Verdict: historical 17 and standalone nine are theorem-level PASS after one local source repair. Historical lines 472-474 and nine lines 598-600 reuse the positive-tail coordinate in the negative-tail cutoff. Choose separate original coordinates for the positive and negative exponential coefficients; both have norm rho0, so the same cutoff and constants follow. All other historical source ranges were rechecked PASS, including nonsymmetric interpolation, global rank <=3r, and restricted rank <=r.

The separate nine reconstruction at commit d3b12e27dc682a7fac0aa7edc1bd70de59cba8b1 has the same notational issue at line 462 and otherwise agrees.

The advertised five-value main.tex remains absent from current master, so that lower claim is UNCHECKED at source level here.

Unrestricted three-eigenvalue QFORM remains OPEN.
