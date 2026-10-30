SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T06:05:57Z.
attacking: convert the strict-N3 small-diagonal hypothesis into a global off-diagonal frequency currency, then compare it against the newest local rank-two packet receiver before any tiny packet is inverted.

# Early substantive checkpoint

Status: SUPPORTING IMPLICATION PROVED; full QFORM remains OPEN.

## Universal quarter-Riesz estimate in the small-diagonal target class

Let `A` be real symmetric with at least three singular values at least one (equivalently at least three eigenvalues of modulus at least one), and suppose

`max_i |A_ii| <= delta < 1`.

For independent real `X_i` with densities at most one, put `Q=X^T A X` and

`H_1/4(Q)=sup_s E |Q-s|^(-1/4)`.

Using fleet01/B01's completed aggregate off-diagonal theorem

`H_1/4(X^T C X) <= C_off F(C)^(-1/8)`, `F(C)=sum_(i!=j) C_ij^2`,

`C_off=5.095453495355205...`,

one gets

`H_1/4(Q) <= C_off [3(1-delta)^2]^(-1/8)`.

Proof: let `D=diag(A)`. Mirsky's singular-value inequality gives

`||A-D||_F^2 >= sum_j (s_j(A)-s_j(D))^2 >= 3(1-delta)^2`,

because `s_1(A),s_2(A),s_3(A)>=1` and every singular value of `D` is at most `delta`. But

`||A-D||_F^2=sum_(i!=j) A_ij^2=F(A)`.

Therefore the aggregate off-diagonal theorem applies directly. In particular, throughout the standard small-diagonal N3 regime `delta<=1/2`,

`H_1/4(Q) <= 5.2820217398...`,

and hence for every `r>0`,

`sup_s P(|Q-s|<=r) <= 5.2820217398 r^(1/4)`.

This is a frequency-averaged/distribution-function estimate for the whole small-diagonal target class. It does not assert any law-uniform scalar pointwise Fresnel decay and therefore does not conflict with the phase-aligned-density counterexample.

Next: apply the newest fleet03/B01 logarithmic rank-two packet receiver on the previous diffuse strict-N3 family and quantify the separation between vanishing local packet currency and the uniform global quarter-Riesz currency.
