# account02/B12 early checkpoint — orthogonal-completion stable-rank carrier

Programme QFORM-DENSITY-3EIG-20260922. Full target OPEN.

First unpaid implication: derive from bare `s3(A)>=1` either a bounded original-coordinate carrier/crossing certificate or an already-paid hub/ridge/grouped-bank/physical-core/Schur exit. The calculation below is only a supporting compiler; it does not force its carrier hypothesis.

Let `A=A0+R+T` with `A0,R` symmetric, `A0 R=0`, and `||T||op<=delta`. Fix an original-coordinate set `H`, `|H|=m>=6`, and put `C0=A0[:,H]`. Define

`g0^2 = ( ||C0||F^2 - 5 ||C0||op^2 )_+ /(m-5)`.

Since the singular values of `C0` satisfy

`sum_{j>=6} s_j(C0)^2 >= ||C0||F^2-5||C0||op^2`

and the tail has `m-5` terms, each at most `s6(C0)^2`,

`s6(C0)>=g0`.

For `A*=A0+R`, orthogonality gives `A*^2=A0^2+R^2>=A0^2`. With `C*=A*[H,H]` and `M*=A*[H,Hc]`, account03/B12 r37 gives, for every `p+q=7`,

`s_p(C*)^2+s_q(M*)^2 >= lambda_6((A0^2)[H,H])=s6(C0)^2>=g0^2`.

Weyl under the genuinely dense tail `T` gives `s_p(C*)<=s_p(C)+delta` and `s_q(M*)<=s_q(M)+delta`, where `C=A[H,H]`, `M=A[H,Hc]`. Therefore

`(s_p(C)+delta)^2+(s_q(M)+delta)^2 >= g0^2`.          (E1)

In particular, if `s2(C)<b` and `b+delta<g0`, then

`s5(M) >= sqrt(g0^2-(b+delta)^2)-delta`.              (E2)

When the right side is positive, the pinned `e5f71d79...` D5 theorem applies to the actual final original-coordinate cross block and gives

`||p_Q||inf <= 5 sqrt(2e)/[sqrt(g0^2-(b+delta)^2)-delta]`.  (E3)

No post-rotation independence and no claim that `X^T T X` is small are used. The arbitrary orthogonal spectral completion `R` is magnitude-free and may contain arbitrarily many eigenvalues of either sign.

Sources consumed: account03/B12 r37 `math-open-problems@3d6d9699d94146c3d2cbc475936dacd74109f913`; pinned D5 source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
