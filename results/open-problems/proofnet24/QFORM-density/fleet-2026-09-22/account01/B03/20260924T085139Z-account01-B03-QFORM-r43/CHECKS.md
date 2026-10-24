# CHECKS — account01/B03 r43

Run: `20260924T085139Z-account01-B03-QFORM-r43`.

## 1. Weighted-time constant algebra

From the negative packet

`A_- <= c_k sqrt(pi) D^(-1/(2k))`, with `c_k=8k/(2k-1)` and `D=|det B|`.

From account02/B03 r52

`A_+ <= (16/3) pi^(3/2) E[M_+^(3/4)]` after averaging over the common environment.

Therefore

`sqrt(A_- A_+) /(2pi)
 = [sqrt(c_k) pi^(1/4) D^(-1/(4k))]
   [(4/sqrt(3)) pi^(3/4) (E M_+^(3/4))^(1/2)] /(2pi)
 = 2 sqrt(c_k/3) D^(-1/(4k))(E M_+^(3/4))^(1/2)
 = 2 sqrt(8k/[3(2k-1)]) D^(-1/(4k))(E M_+^(3/4))^(1/2).`

At `k=1`, this is `4sqrt(2/3)|e|^(-1/4)(E M_+^(3/4))^(1/2)`.

Numerically at `e=1, M_+=1`:

`4sqrt(2/3)=3.265986323710904`.

The associated `L1_t` characteristic-function budget is

`2pi * 4sqrt(2/3) = 8pi sqrt(2/3) = 20.520797282589825`.

## 2. Direct whole-copy weighted budget

For `k=1,e=1`, the pointwise squared envelope is

`|F_w(t)|^2 <= min(1, pi/|t|)`.

Thus

`int_R |t|^(-1/2)|F_w(t)|^2 dt
 = 2[int_0^pi t^(-1/2)dt + pi int_pi^infty t^(-3/2)dt]
 = 8sqrt(pi)
 = 14.179630807244127.`

Dividing by `sqrt(2pi)` through the half-Riesz identity gives

`E|Q-Q'|^(-1/2) <= 4sqrt(2)=5.656854249492381`.

## 3. Exact target spectrum

For variable order `(Z,X,W,H1,Y1,H2,Y2)`, the coefficient matrix of

`Q_*=2XZ+2XW+2H1(Y1+W)+2H2Y2`

is

```
A = Matrix([
[0,1,0,0,0,0,0],
[1,0,1,0,0,0,0],
[0,1,0,1,0,0,0],
[0,0,1,0,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,1],
[0,0,0,0,0,1,0]])
```

This is `P5 direct_sum K2`. Hence the eigenvalues are

`2cos(j pi/6), j=1,...,5`, together with `+1,-1`, i.e.

`{sqrt(3),1,0,-1,-sqrt(3),1,-1}`.

A direct SymPy check returned multiplicities

`{1:2, -1:2, -sqrt(3):1, sqrt(3):1, 0:1}`.

Therefore six eigenvalues have modulus at least one.

## 4. Scope checks

- `W` is conditioned in an original-coordinate basis; no rotation of independent inputs is used.
- Conditional on `W=w`, the negative packet `(X,Z)` and positive packet `(H1,H2,Y1,Y2)` are independent because they are disjoint original-coordinate blocks.
- The positive slope `(Y1+w,Y2)` has density `f_{Y1}(l1-w)f_{Y2}(l2)` and therefore joint density cap at most one.
- The negative packet estimate is uniform in the affine translation `2wX`.
- The copy identity is used only for the full scalar output, or internally through the coupled ambiguity factors of r36; no conditional cap is asserted for a conjugate copy sum/difference.

Marker: `QFORM_B03_CROSSPAIR_WEIGHTED_SPLICE_CHECK_PASS`.
