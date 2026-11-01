# Late calculation — r44 reciprocal-fan rigidity

Keep the literal fleet03/B07 r44 crossing `K=A[I,J]`.  Write the squared singular values

`x1>=x2>=...>=0`,

`Z=e2(x)>=zeta:=2^-12`, `W=e3(x)<theta`,

and

`tau=sum_{j>=3}xj`, `R=e2(x3,x4,...)`.

The completed compound inequality already consumed by r44 gives

`tau Z <= 3W`, hence `tau<3theta/zeta`.                         (1)

The exact decomposition is

`Z=x1*x2+(x1+x2)*tau+R`,                                        (2)

with `R<=tau^2/2`.

Take the live high-ratio threshold

`theta=(2C3/rho)^6`, `C3=3*2^(4/3)*e^(1/3)`.

Throughout r44's inherited chamber `rho>=64 C3`, we have `theta<=2^-30`, so in particular

`(3theta/zeta)^2 <= zeta/2`.                                    (3)

## Theorem — `QFORM-R44-RECIPROCAL-FAN-RIGIDITY-v1`

Under (1)-(3), either

`boxed: (s1(K)s2(K))^2=x1*x2 >= zeta/2`,                         (4)

or all of the following hold:

`boxed: s1(K) > zeta/sqrt(24theta)`,                             (5)

`boxed: s2(K)^2=x2 < 8theta/zeta`,                               (6)

and, for the Frobenius tail beyond the top two directions,

`boxed:
 x1*tau
 > zeta/2 - (57/2) theta^2/zeta^2.
}`                                                               (7)

Equivalently,

`boxed:
 s1(K) ||K-K_2||_F
 > [zeta/2-(57/2)theta^2/zeta^2]^(1/2).
}`                                                               (8)

At `theta<=2^-30`, `zeta=2^-12`, the bracket in (8) is at least

`(1-57*2^-24) zeta/2`,

so the right side is greater than `0.0110485`.

Thus failure of two-volume retention by the rank-two carrier cannot make the discarded coefficient tail harmless: the leading singular spike and the discarded Frobenius tail have a uniformly positive reciprocal product.

### Proof

Assume (4) fails.  The sharper E2/E3 router in `MID_CALC.md` with `a=1/2` gives

`x1*tau > zeta/8`                                                (9)

and (5).  Since the triples `(1,2,j)`, `j>=3`, are part of `W`,

`W >= x1*x2*tau`.

Together with (9),

`x2 < 8theta/zeta`,

which is (6).

Now failure of (4) and `Z>=zeta` imply

`D:=Z-x1*x2 > zeta/2`.

From (2),

`x1*tau = D-x2*tau-R`.

Using (1), (6), and `R<=tau^2/2`,

`x2*tau < (8theta/zeta)(3theta/zeta)=24theta^2/zeta^2`,

`R < (1/2)(3theta/zeta)^2=(9/2)theta^2/zeta^2`.

Hence

`x1*tau > zeta/2-(24+9/2)theta^2/zeta^2`
`          = zeta/2-(57/2)theta^2/zeta^2`,

proving (7)-(8).  QED.

## Live-ratio scales

Substituting `theta=(2C3/rho)^6` into (5)-(6) gives

`boxed: s1(K) > 5.30476580567e-9 rho^3`,

`boxed: s2(K) < 1.70056479146e6 rho^-3`.

So the non-retention branch is not a generic "near rank two" state.  It is a quantitatively reciprocal fan: one singular direction diverges cubically in the slab ratio, every nonleading singular direction is operator-small at cubic inverse scale, yet the leading direction times the *discarded* top-two Frobenius tail stays order one by (8).

The Walsh-Hadamard reciprocal fan in `MID_CALC.md` realizes exactly this mechanism qualitatively: `E2->1`, `E3->0`, `||K-K_2||_F->0`, but asymptotically all E2 mass outside the top-two carrier comes from the giant first direction wedged with the vanishing fan.  Therefore any receiver for r44 must preserve exterior-volume interactions with the small tail; coefficient-Frobenius closeness alone is not a permissible deletion argument.
