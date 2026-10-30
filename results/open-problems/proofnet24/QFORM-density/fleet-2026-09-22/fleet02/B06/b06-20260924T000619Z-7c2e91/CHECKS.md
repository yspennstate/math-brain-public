# Deterministic sanity checks

The algebraic proof does not depend on these numerics. Running `check_run.py` on 1000 seeded random instances gave:

- `det T_h = det(T) d_h/s_h`: maximum absolute error `5.55e-13`;
- `det(E_J E_J^T)=det(EE^T)(1-alpha_h)`: maximum absolute error `1.71e-13`;
- `e_2((E_I^T T_h E_K)^T(E_I^T T_h E_K))=(det T_h)^2 det(E_I E_I^T)det(E_K E_K^T)`: maximum relative error `5.81e-12`.

For the explicit all-pivots-null prototype from the report:

- `alpha_h=0.8` exactly (`4/5` algebraically);
- `W=0.3125=5/16`, `W_h=0.0625=1/16`;
- the exact Schur residual has zero physical diagonal;
- the full unscaled prototype has rank four;
- the principal triple used in the proof has numerical eigenvalues `[-0.5, -0.2807764064..., 1.7807764064...]`, matching the exact characteristic polynomial `(2 lambda+1)(2 lambda^2-3 lambda-1)/4`;
- the full matrix scaled by four has four nonzero numerical eigenvalues approximately `[-5.1226577,-1.3352346,1.2734581,9.1844342]`, consistent with the exact target certification via the principal triple and interlacing.
