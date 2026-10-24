SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T17:14:30Z.
attacking: the exact-zero-edge endpoint inside the heavy null-hub branch left by account04/B18 r4; use a primary product-marginal bound plus conditional linear+square smoothing, without post-rotation independence.

# Early mathematical checkpoint

Current status: substantive calculation found; full proof audit and source refresh still in progress. Full QFORM remains OPEN.

The live null-hub normal form is

    Q = 2 (X0 + ell.X_L)(g.X_L) + d (beta.X_L)^2,
    ||beta||_2 = 1,  beta.g = 0,
    gamma = ||g||_2 > 0,  |d| gamma^2 = h D.

For a heavy anchor i with q_i=beta_i^2+g_i^2/gamma^2>1/2, the current designated partner account04/B18 r4 pays |g_i|>=1/64 in N3(1/64), but explicitly leaves tiny |g_i|, including g_i=0.

At the exact endpoint g_i=0, q_i=beta_i^2>1/2. Condition on all leaves except i. Writing

    G = g_- . X_-,
    a = d beta_i^2,

and allowing arbitrary affine terms from outside conditioning, the active two independent original coordinates have the form

    T = 2 (G+c) X0 + a Xi^2 + B(X_-) Xi + C(X_-).

For fixed X_- and H=G+c !=0, convolution of the scaled X0 density with the quadratic pushforward of Xi gives

    ||p_{T|X_-}||_infty
      <= min( 1/(2|H|), sqrt(2)/(sqrt(|a|)|H|^(1/2)) ).        (E1)

The second bound follows from the exact quadratic pushforward envelope

    p_{a Xi^2+b Xi}(y) <= [|a| |y-y0|]^(-1/2)

on its one-sided support and the bathtub estimate for a probability density capped by 1/(2|H|).

The primary Livshyts--Paouris--Pivovarov product-marginal theorem gives the translated linear statistic H a density cap

    M <= sqrt(2)/gamma.                                           (E2)

For F(x)=min((2|x|)^(-1), sqrt(2)|a|^(-1/2)|x|^(-1/2)), the one-dimensional bathtub principle gives

    E F(H) <=
      4 sqrt(M/|a|),                         if |a|M >= 4,
      M [2 + log(4/(|a|M))],                 if |a|M < 4.          (E3)

Optimizing (E3) over gamma after substituting M=sqrt(2)/gamma yields the dimension-free closed form

    E F(H) <= 6 e^(-1/3) (|a| gamma^2)^(-1/3).                    (E4)

Since |a| gamma^2=beta_i^2 hD, this suggests the new exact-zero-edge bound

    ||p_Q||_infty
      <= 6 e^(-1/3) (beta_i^2 hD)^(-1/3).                         (E5)

In the target-normalized r>=1/2 compiler, h>=1/5, D>=1 and beta_i^2>1/2, so (E5) is

    ||p_Q||_infty < 6 (10/e)^(1/3) = 9.2623194719... .            (E6)

The fixed-X_- conditional density is a convolution of two L1 densities and is C0; (E3) is an integrable dominating function, so dominated convergence should also give a continuous C0 unconditional density. This continuity step and every constant will be checked before the final report.

This endpoint uses no arbitrary-joint coarea, no conditional-cap-as-independence step, no pointwise quadratic-phase decay, no fixed-good-minor selection, and no probabilistic rotation. The remaining punctured branch after splicing with account04/B18 r4 would be 0<|g_i|<1/64.
