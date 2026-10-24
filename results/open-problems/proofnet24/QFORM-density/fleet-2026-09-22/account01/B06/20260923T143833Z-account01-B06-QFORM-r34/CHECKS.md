# account01/B06 r34 checks

These are finite algebra/scaling checks for `REPORT.md`; they are not probabilistic evidence for the conjecture.

## 1. Rank-one triple determinant

For

`M=[[sigma,0,c],[0,0,d],[c,d,r]]`,

expansion along the first row gives

`det M = sigma*(0*r-d^2) + c*(0*d-0*c) = -sigma d^2`.

Thus, after a deterministic orthogonal basis change in a rank-one physical pair, each principal triple determinant is exactly `-sigma d_k^2`.

## 2. Parseval/Pluecker sum

For the exact-rank-three Parseval frame with rows `r_k`, `sum_k r_k r_k^T=I_3`. If `w=r_i cross r_j`, then

`sum_k det([r_i;r_j;r_k])^2 = sum_k <w,r_k>^2 = w^T I_3 w = ||r_i wedge r_j||^2`.

Combined with check 1 and `det A_K=det(Lambda) det(R_K)^2`, this verifies

`|sigma| delta^2 = |det Lambda| tau_I`.

## 3. Scaling

Under `A -> alpha A`, the rank-one-pair data scale as

`sigma -> alpha sigma`, `delta -> |alpha| delta`.

Hence `( |sigma| delta )^(-1/2)` scales as `|alpha|^(-1)`, exactly the scaling of a one-dimensional density.

For the pure bilinear receiver, `C -> alpha C` gives

`Delta=sqrt(det(CC^T)) -> alpha^2 Delta`,

so `Delta^(-1/2)` again scales as `|alpha|^(-1)`.

## 4. Constants

`2 sqrt(pi e) = 5.844564730644556...`

`2^(9/4) e^(1/4) = 6.1078886454775825...`

If `tau_I >= 1/262144=1/512^2`, the exact-rank-three endpoint gives

`2^(9/4)e^(1/4)*512 = 3127.238986484522...` times `1/s`.

## 5. Product-structure check

The proof of the rank-one parabolic receiver never treats the rotated pair `(S,W)` as independent. Its joint density is retained explicitly as

`g(s,w)=f_1(u_1 s+v_1 w) f_2(u_2 s+v_2 w)`.

Only one original factor is discarded using `f_j<=1`, while the other is integrated exactly along the parabolic fiber using Lemma 2.1. This is compatible with the live correction forbidding post-rotation independence.

`QFORM_B06_R34_CHECK_PASS`
