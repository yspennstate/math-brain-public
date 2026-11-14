P0133 (Schramm 2006 Problem 6.2, UST torus dual theta): OPEN, numerics. 14 Nov 2026, an agent.
- Figure-eight core vanishes; superbase law converges and depends on tau only (five moduli, two meshes each).
- Rotation test passed: tori placed at an angle to the lattice give the PSL2(Z)-mapped law within 1-2 se (one 2.8 se gap is mesh, see NOTE finding 4).
- Million-sample GPU runs (ust_metal.swift): finer rotation pairs agree to 0.34 se; limit values to ~3 digits (square torus 0.475 per top superbase, 0.0125 per next; 0.5+i top 0.714), NOTE finding 5.
- Close to C exp(-0.9 sum|v|^2/Im tau) but not exact. Samples: data/p0133_samples_2026_11_14.tar.gz, data/m_*.tsv.gz. Not audited.
- Weight as a function of shape (NOTE finding 6, 49-modulus grid, data/grid/): a polynomial in (e1, e3) needs degree 4 to fit (chi2/dof 1.25) and the needed degree grows with the range of shapes; the quartic predicts six held-out meshes at 1.02. No closed form found (best 2.58).
