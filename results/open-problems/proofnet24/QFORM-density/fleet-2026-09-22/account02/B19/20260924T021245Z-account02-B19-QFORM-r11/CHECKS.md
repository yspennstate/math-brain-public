# account02/B19 r11 deterministic checks

All values below are arithmetic consequences of the proved formulas in REPORT.md; no numerical experiment is used as proof.

- `zeta=2^-18=0.000003814697265625`.
- `sqrt(zeta)=2^-9=0.001953125`.
- With `delta0=2/9`, the bilateral rank-one-defect product threshold is
  `[(4 zeta^2)/(delta0^2)]^(1/4)=3/512=0.005859375`.
- The implied one-sided threshold is
  `sqrt(3/512)=0.07654655446197431...`.
- In the distinct-anchor bordered block, if `E3(B)<2^-18` and `|b|sqrt(E2(N))<2^-9`, then
  `F<(2*2^-9)/(2/9)=9/512=0.017578125`.
- At `b=0`, the exact bordered-star term gives
  `F<2^-9/(2/9)=9/1024=0.0087890625`.
- The owner-pinned D5 gate at `E5>=2^-20` gives
  `5 sqrt(2e)*(2^-20)^(-1/10)=20 sqrt(2e)=46.63287963194249...`.

Algebra sanity for Lemma 4.1 after coefficient-space orthogonal normalization `u=alpha e1`, `v=beta f1`: for each bordered minor indexed by row pair `I`, column pair `J`,

`det [[N[I,J],u_I],[v_J^T,b]] = b det N[I,J]-v_J^T adj(N[I,J])u_I`.

The second term vanishes unless `1 in I` and `1 in J`; for `I={1,i}`, `J={1,j}` it equals `-alpha beta N_ij`. Thus its squared aggregate norm is exactly

`alpha^2 beta^2 sum_(i>1,j>1) N_ij^2
 =delta^2 ||P_e^perp N P_f^perp||_F^2`,

while the first aggregate norm is `b^2 E2(N)`. Triangle/reverse triangle yields REPORT (4.3).

Terminal marker: `QFORM_B19_R11_BILATERAL_TWOSTAR_CHECK_PASS`.
