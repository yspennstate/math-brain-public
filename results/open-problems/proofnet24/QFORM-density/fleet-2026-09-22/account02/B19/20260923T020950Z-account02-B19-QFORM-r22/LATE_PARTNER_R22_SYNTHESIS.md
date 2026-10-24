# Late source refresh: account03/B19 r22 closes the internally diffuse part of its new residual

Fresh designated-partner handoff after the main report is account03/B19 r22, canonical mathematics `yspennstate/math-open-problems@d0d68512c0e8ddaa3893134fdfc03e2214a751aa`, theorem `QFORM-O3-ONE-RANK1-TWO-RANK2-ROUTING-v1`.

Its exact one-rank-one / two-rank-two frame geometry is

`S_H=lambda vv^T`, `S_1+S_2=I-lambda vv^T`,                      (1)

where `G_1,G_2` are disjoint original-coordinate rank-two source banks. Its grouped currencies satisfy

`D_1+D_2+mu=|det M| lambda`.                                      (2)

When `lambda>=1/64` and some `D_j>=mu/4`, partner r22 proves

`||p_Q||_infinity<2805`.                                          (3)

When both grouped exits fail, it proves the exact transverse skeleton

`m>2/3`, `|r-s|>1/sqrt(3)`.                                      (4)

The account02/B19 theorem `QFORM-O3-TWO-RANK2-TRANSVERSE-DIFFUSE-v1` from the main report now applies directly to the same two banks whenever their internal normalized row leverages satisfy

`u_i^T S_j^+u_i<=1/2`, `i in G_j`, `j=1,2`.                      (5)

Indeed the combined active Gram is exactly

`S_1+S_2=I-lambda vv^T`,

so

`det(S_1+S_2)=1-lambda`.                                         (6)

The variational leverage monotonicity from the main report gives every active row combined leverage at most `1/2`, and Claude Theorem F therefore yields the real target-level inequality

`boxed: ||p_Q||_infinity
 <=12[|det M|(1-lambda)]^(-1/3)
 <=12(1-lambda)^(-1/3).`                                         (7)

Consequences at fixed numerical thresholds:

- Partner r22's secondary small-rank-one-mass corner `lambda<1/64` is **fully paid whenever the two rank-two banks are internally diffuse**, with

  `||p_Q||_infinity <12(64/63)^(1/3)=12.0631591...`.             (8)

- In partner r22's no-grouped-exit near-complementary skeleton, if the two rank-two banks are internally diffuse and `lambda<=63/64`, then

  `||p_Q||_infinity<=48`.                                         (9)

Thus, after combining the newest partner result with the main report, the one-rank-one/two-rank-two residual is strictly smaller than either source alone: a surviving state must either

1. have a grouped determinant exit already paid by partner r22;
2. have an **internally heavy** rank-two bank (some normalized physical-row leverage `>1/2`); or
3. lie in the **near-coloop** strip `lambda>63/64` inside the partner's near-complementary skeleton.

In the `lambda<1/64` corner, only the internally-heavy subcase survives. No assertion is made that (4) itself forces (5), and no small coefficient is deleted perturbatively.

This late application supersedes the main report's statement that account03/B19 r21 was the newest designated partner. The main theorems remain valid; only the proof graph and first residual are sharpened.

The first unpaid one-rank-one/two-rank-two implication is now:

`QFORM-O3-R22-COHEAVY-OR-NEARCOLOOP-TRANSDUCER-v1`: in partner r22's no-grouped-exit near-complementary skeleton, pay states with an internally heavy rank-two bank or with `lambda>63/64`, unless an already-paid pivot/ridge/cross/grouped/null-coloop exit applies. The general top-level gate remains `N3(tau,C0)`, and arbitrary-extra-spectrum descent remains separate.
