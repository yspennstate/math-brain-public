# account03/B03 r52 checks

Run: `20260924T095801Z-account03-B03-QFORM-auto11-r52`.

## Algebraic determinant check

For

    B = [[a,e,0],[e,k,b],[0,b,0]],

expansion along the last row/column gives

    det B = -a b^2.

Thus the determinant-homogeneous factor in the theorem is exactly

    |a|^(-1/3)|b|^(-2/3)=|det B|^(-1/3).

## Near/far optimizer

The proof obtains

    F(delta)=A sqrt(delta)+B/delta,
    A=8 M sqrt(N/(|ab|)),
    B=N/(2|b|).

Setting x=sqrt(delta) gives F=Ax+B/x^2. The stationary equation is

    A-2B/x^3=0,
    x^3=2B/A.

Therefore

    F_min
      = A^(2/3) B^(1/3) [2^(1/3)+2^(-2/3)]
      = 3*2^(-2/3) A^(2/3)B^(1/3)
      = 6 M^(2/3)N^(2/3)|a|^(-1/3)|b|^(-2/3).

## Half-Riesz cap check

For a probability density p<=K, the decreasing rearrangement gives the extremal centered interval density

    p_*(x)=K 1_{|x|<=1/(2K)}.

Then

    integral |x|^(-1/2)p_*(x) dx
      = 2K integral_0^(1/(2K)) x^(-1/2)dx
      = 2 sqrt(2K).

For `2brV`, the density cap is K=N/(2|br|), so the half-Riesz bound is exactly

    2 sqrt(N/(|br|)).

The integral over `|r|<=delta` is

    integral_{-delta}^{delta}|r|^(-1/2)dr = 4 sqrt(delta),

producing the near term `8 M sqrt(N delta/(|ab|))`.

## Strict target matrix

Take

    B_* = [[3,2,0],[2,5,3],[0,3,0]].

Direct determinant expansion gives `det B_*=-27`.

The characteristic polynomial is

    lambda^3 - 8 lambda^2 + 2 lambda + 27.

Sign evaluations:

    p(-2)=-17, p(-1)=16,
    p(2)=7, p(3)=-12,
    p(7)=-8, p(8)=43.

Because B_* is real symmetric, all eigenvalues are real. The three sign changes on disjoint intervals force exactly one eigenvalue in each of

    (-2,-1), (2,3), (7,8).

Thus all three have modulus strictly larger than one.

Numerical eigenvalues, used only as a check, are

    -1.57782646, 2.37612607, 7.20170039.

## Product-law constant check

With same-bank orthonormal pair cap `M<=2`, physical scalar cap `N<=1`, and `|det B_*|=27`,

    H = 6*2^(2/3)*27^(-1/3)
      = 2*2^(2/3)
      = 3.1748021039363987...

and

    4 sqrt(pi H) = 12.632614909877057...

for the whole-copy weighted time integral.

## Partner r4 application check

For the frame

    s=(1/sqrt2,1/sqrt2,0,0),
    t=(1/sqrt6,-1/sqrt6,2/sqrt6,0),
    v=e4,

the nonzero squared 3x3 Plucker weights are all `1/3` on `124,134,234`. For `H={1,4}`,

    q_H=2/3,
    r_H=2/9,
    q_H^2-r_H=2/9.

With `Delta=27`,

    J_2(H)=27^2*(2/9)=162.

The completed account04/B03 r4 inequality then gives

    129.924435862525374 * 162^(-1/6)
      = 55.64656197133566...

and the generic whole-copy conversion gives

    4 sqrt(pi*55.64656197133566)
      = 52.88762884254536...

## Scope audit

- No pointwise oscillatory decay used.
- No independence after rotating the same-bank pair used.
- No conditional density cap for conjugate sum/difference variables used.
- The only rotation is inside a two-dimensional variable whose **joint density cap** is assumed/known; orthogonal Jacobian one preserves that cap.
- The independent scalar remains an original disjoint source/projection until only translations by functions of the same-bank `R` are used inside the proof; the near-region integration uses that these translations do not depend on `S`.
- The theorem proves an essential L-infinity density bound and linear small-ball scaling; continuity is not established.
- The full QFORM conjecture remains open.

`QFORM_B03_R52_CHECK_PASS`
