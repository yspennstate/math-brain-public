# fleet02/B16 checkpoint — hub Schur remainder is uniformly diffuse rank two

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN. This is an early supporting calculation, not a final report.

Let `A=R Lambda R^T`, `R^T R=I_3`, all three eigenvalues of `Lambda` having modulus at least one. In the true-near-coloop chamber take the hub row `r_0=sqrt(c)e`, `c>63/64`, and write residual rows `r_j=s_j e+w_j`, `w_j perpendicular e`, with the inherited transverse bound `||w_j||^2<1/64`. Parseval gives `sum w_jw_j^T=I_2` and `sum s_jw_j=0`.

Write, in the splitting `e plus e^perp`,

`Lambda=[[alpha,b^T],[b,C]]`, so `A_00=c alpha`. Assume `A_00!=0`. With `W` the matrix of rows `w_j` and `l=A_{L0}=sqrt(c)(alpha s+Wb)`, the exact hub Schur complement is

`S=A_LL-l l^T/A_00 = W K W^T`,

`K=C-bb^T/alpha`.

Thus the longitudinal leakage `s` cancels identically from the Schur remainder. Since a nonzero scalar pivot reduces exact rank three to exact rank two, and the completed Schur-complement interlacing lemma preserves two eigenvalues of modulus at least one, the two eigenvalues of `K` have modulus at least one; hence `|det K|>=1`.

There is a deterministic leaf partition `I disjoint union J=L` with both transverse Grams quantitatively nondegenerate. Give each leaf an independent sign `epsilon_j` and put `H=sum epsilon_j w_jw_j^T`. Then

`E ||H||_F^2 = sum ||w_j||^4 <= (1/64) sum ||w_j||^2 =1/32`.

Hence some signing has `||H||op<=||H||F<=1/sqrt(32)<1/4`. For that signing,

`G_I=(I_2+H)/2 >=(3/8)I_2`, `G_J=(I_2-H)/2 >=(3/8)I_2`.

For the Schur cross block `M=S_IJ=W_I K W_J^T`, its two nonzero singular values satisfy

`s_1(M)s_2(M)=|det K| sqrt(det G_I det G_J) >=9/64`.

Applying the already-proved fleet02/B16 arbitrary-self-curvature rank-two cross estimate gives

`|phi_S(t)| <= min(1, (16 pi)/(3 |t|))`

and the pinned fractional-potential lemma from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives

`H_{1/2}(S) <= 8(64/9)^(1/4)=13.0639452948...`.

The pinned square-peel inequality therefore yields

`||p_Q||_infinity <=13.0639452949 / sqrt(|A_00|)`.

The point of the calculation is structural: in the true near-coloop branch with nonzero hub pivot, all transverse rank-two curvature and source diffuseness are already uniformly quantitative after the hub Schur complement. The only remaining singularity in this route is the scalar near-null factor `|A_00|^{-1/2}`. The final report will test whether that factor can be removed without translation-uniform peeling and will record the exact obstruction if not.
