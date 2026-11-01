# Deterministic checks for `QFORM-N3-THREEHUB-DIAGONAL-COMPLEMENT-v1`

These checks support arithmetic and the explicit family; they are not independent proofs of the analytic source theorems.

Using `tau=1/128`:

- `tau = 0.0078125`
- `eta=sqrt(tau+tau^2) = 0.08873294290312927`
- `b=tau+2eta = 0.18527838580625855`
- `c=1-b = 0.8147216141937415`
- `q0=6 eta^2/c^2 = 0.07117091432392135`
- `rho0=1-2q0 = 0.8576581713521573`
- `2 sqrt(e) 3^(1/4)/(c rho0^(1/4)) = 5.535027140807025`
- newest-volume `q=1` constant `3e = 8.154845485377136`.

For the explicit `m=129` family with three disjoint flat cross columns, direct symmetric-matrix diagonalization gave nonzero eigenvalues

`[-1.0000000000000013, -1.0, -1.0, 1.0, 1.0, 1.0000000000000013]`.

The largest absolute physical `2 x 2` principal determinant is

`1/129 = 0.007751937984496125 < 1/128`,

and all physical diagonals vanish, so the family is inside strict `N3(1/128)`.

The exact symbolic reason for the spectrum is stronger than the numerical check: `M^T M=I_3`, so the pure symmetric cross matrix `[[0,M^T],[M,0]]` has nonzero eigenvalues `+1,+1,+1,-1,-1,-1`.
