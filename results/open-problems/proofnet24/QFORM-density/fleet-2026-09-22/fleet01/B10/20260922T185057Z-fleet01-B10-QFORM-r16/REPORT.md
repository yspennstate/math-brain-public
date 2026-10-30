SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B10, 2026-09-22T18:50:57Z.
attacking: the one-macro-nullrow leakage step; test whether conditioning on the scalar leakage and paying a positive conditional pair-density moment can remove the logarithm.

# fleet01/B10 — exact-rank-three scalar-leakage obstruction and product-chart closure

Run `20260922T185057Z-fleet01-B10-QFORM-r16`.

**Outcome:** `ESSENTIAL_STEP_APPLIED + REFUTED_INTERMEDIATE_MECHANISM / FULL_TARGET_OPEN`.

The full quadratic-form bounded-density conjecture remains OPEN. This report does not claim continuity. Execution label: `WITHOUT_VERIFIED_BRAIN`.


## 1. Conditional end-to-end route being tested

The previous B10 run reduced an exact heavy zero pivot to a one-log small-ball bound. A natural attempted upgrade is:

1. isolate the physical null variable;
2. condition on the one-dimensional product-linear leakage that contaminates the hyperbolic partner;
3. apply the dependence-tolerant hyperbolic-square theorem conditionally;
4. average the resulting `H(t)^(2/3)` conditional pair-height bound.

This report proves that Step 4 is not dimension/law-uniform, already for one fixed exact-rank-three target matrix and one scalar leakage variable. The same target family is nevertheless uniformly paid by the completed **fleet02/B10** physical hyperbolic-square theorem *before* that conditioning. Thus the obstruction is genuinely in the proof interface, not in QFORM.

## 2. A fragmented cap-one product source

Fix an integer `N>=2`, put `ell=1/N`, and choose rapidly separated centers

`B_k=10^k`, `1<=k<=N`.

Define

`E_N = union_{k=1}^N [B_k,B_k+ell]`,

and let `f_N=1_{E_N}`. Since `|E_N|=N ell=1`, this is a probability density with `0<=f_N<=1`.

Let `X_1,X_2` be iid with density `f_N` and set

`T=(X_1+X_2)/sqrt(2)`,  `Y=(X_1-X_2)/sqrt(2)`.

The map `(X_1,X_2)->(T,Y)` is orthogonal, so its Jacobian is one. Hence the joint density of `(T,Y)` is

`h_N(t,y)=f_N((t+y)/sqrt(2)) f_N((t-y)/sqrt(2))`,

which takes only the values `0,1`. Write

`m_N(t)=p_T(t)=int h_N(t,y)dy`.

On every nonempty slice,

`p_{Y|T=t}(y)=h_N(t,y)/m_N(t)`,

and therefore

`||p_{Y|T=t}||_infinity = 1/m_N(t)`.          (2.1)

Let `Z` be independent Uniform[0,1]. Then, conditionally on `T=t`, the pair `(Y,Z)` has density cap

`H_N(t)=||p_{(Y,Z)|T=t}||_infinity = 1/m_N(t)`.    (2.2)

No conditional independence is asserted beyond the genuine independence of `Z` from `(X_1,X_2)`.

## 3. Exact divergence of the conditional `2/3` height moment

Let `g_N=f_N*f_N` be the density of `S=X_1+X_2`. If

`tau_ell = 1_[0,ell] * 1_[0,ell]`,

then

`int tau_ell(s)^(1/3) ds = 2 int_0^ell u^(1/3)du = (3/2) ell^(4/3)`.   (3.1)

The centers `10^k` have distinct unordered pair sums; because the component intervals are much shorter than their separations, all unordered-pair sum supports are disjoint. Thus `g_N` consists of:

- `N` diagonal triangular components of height profile `tau_ell`;
- `N(N-1)/2` off-diagonal unordered components of profile `2 tau_ell`.

Therefore

`int g_N(s)^(1/3) ds`
`= (3/2) ell^(4/3) [N + 2^(1/3) N(N-1)/2]`.       (3.2)

Since `T=S/sqrt(2)`,

`m_N(t)=sqrt(2) g_N(sqrt(2)t)`.

Using (2.2),

`E H_N(T)^(2/3)`
`= int m_N(t)^(1/3) dt`
`= 2^(-1/3) int g_N(s)^(1/3) ds`
`= 3 [N-1+2^(2/3)] / [4 N^(1/3)]`.                (3.3)

Consequently

`E H_N(T)^(2/3) ~ (3/4) N^(2/3) -> infinity`.      (3.4)

Thus **even one scalar product-linear leakage variable can make the positive `2/3` conditional pair-height moment arbitrarily large** under admissible cap-one fragmented product laws.

## 4. Exact embedding into one fixed heavy-null rank-three target

Take the four physical spectral rows

`u_0=(1/sqrt(2),0,0)`,
`u_1=(1/2,1/sqrt(2),0)`,
`u_2=(1/2,-1/sqrt(2),0)`,
`u_3=(0,0,1)`.

They satisfy

`sum_{i=0}^3 u_i u_i^T = I_3`.

Let

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are exactly `{1,-1,1}`. Hence `A=U Lambda U^T` is a fixed exact-rank-three target matrix satisfying the owner's spectral hypothesis. The physical row `u_0` has leverage `1/2` and exact diagonal pivot

`A_00=u_0^T Lambda u_0=0`.

Let `X_0` be any independent cap-one input, take `X_1,X_2` as in Section 2, and let `X_3=Z` be Uniform[0,1]. The three spectral coordinates are

`S = X_0/sqrt(2) + (X_1+X_2)/2 = X_0/sqrt(2)+T/sqrt(2)`,
`Y = (X_1-X_2)/sqrt(2)`,
`Z = X_3`,

so

`Q=2 S Y + Z^2`.                                      (4.1)

Conditioning on `T=t`, (4.1) becomes

`Q = sqrt(2) X_0 Y + sqrt(2)tY + Z^2`.

Apply the completed dependence-tolerant hyperbolic-square theorem to the isolated original variable `X_0` and the conditional pair `(Y,Z)`. In its notation `a=1/sqrt(2)`, `b=1`, and the conditional pair density cap is `H_N(t)`. Hence

`||p_{Q|T=t}||_infinity <= 6 H_N(t)^(2/3)`.           (4.2)

Averaging this *conditional supremum bound* gives only

`||p_Q||_infinity <= 6 E H_N(T)^(2/3)`
`= (9/2) [N-1+2^(2/3)] / N^(1/3)`,                  (4.3)

which diverges like `(9/2)N^(2/3)`.

Equation (4.3) is not a lower bound on the true density. It proves that this scalar-conditioning/positive-height-moment route cannot provide a universal QFORM constant.

## 5. The same family is uniformly paid by the designated partner theorem

Now do **not** condition on the leakage `T`. Expanding (4.1) in the original physical variables gives

`Q = X_0 X_1 - X_0 X_2 + (X_1^2-X_2^2)/sqrt(2) + X_3^2`.      (5.1)

Condition only on the original coordinate `X_2`. In the remaining independent physical variables `(X_0,X_1,X_3)`, (5.1) has

- zero `X_0^2` coefficient;
- coefficient `1` on `X_0 X_1`, i.e. matrix entry `A_01=1/2`;
- no `X_0 X_3` term;
- square coefficient `A_33=1`;
- arbitrary allowed linear term `-X_2 X_0`, plus the allowed `X_1^2/sqrt(2)` and conditioned constant.

Therefore the completed **fleet02/B10** theorem `QFORM-HYPERBOLIC-SQUARE-v1` (canonical source commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`) applies exactly, with `a=1/2` and `b=1`, and yields

`boxed(||p_Q||_infinity <= 4/sqrt((1/2)*1) = 4 sqrt(2))`.       (5.2)

The bound is uniform in `N` and in the fragmented laws above. This is an actual application of the designated OTHER-account partner result to the target inequality.

Thus the family simultaneously has:

`true target density cap <=4sqrt(2)`,

while the scalar-leakage conditional-height payment in (4.3) diverges.

## 6. Consequence for the one-macro-nullrow obstruction

The previous B10 endpoint estimate

`P(Q in I) <= 2 epsilon [1+log(1/(2epsilon))]`

cannot in general be upgraded by conditioning on the scalar leakage and then bounding a positive moment of the conditional pair sup-density. Fragmented product laws make that height moment arbitrarily large even for the fixed heavy-null exact-rank-three matrix above.

The surviving mechanism must keep the **translations and overlap of the conditional profiles active before the output supremum is taken**. Equivalently, one should aggregate in original product coordinates before any conditional-height or reciprocal-minor payment. This is consistent with the later fleet02/B15 correction on scalar-Q' conditional moments, but the present calculation is tailored to the exact-rank-three B10 leakage geometry.

A precise next implication is:

`QFORM-HEAVY-NULL-TRANSLATION-UNIFORM-TRACE-v1`:
construct a translation-uniform fractional-trace / grouped-coordinate estimate for

`2( sqrt(c) X_i + T )Y + R(Y,Z)`

under the exact Parseval orthogonality constraints, without taking `sup` of the conditional `(Y,Z)|T=t` density before averaging over `t`.

The partner closure (5.2) shows the kind of product-chart reorganization that can succeed: choose a physical chart in which one untouched coordinate supplies the hyperbolic affine variable and another untouched coordinate supplies the square, and only then average the remaining original coordinates.

## 7. Secondary check of the current rank-two affine Schur synthesis

The current interactive theorem `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1` uses the exact identity `det N=c det M/a`. I independently checked the algebra relevant to B10.

Write the selected spectral row as `v_i=sqrt(c)e` and, in an orthonormal basis `(e,E)`,

`M=[[m,q^T],[q,C]]`, with `m=a/c`.

Completing the square in the physical coordinate removes the rank-one spectral piece `(c/a)Mee^TM`, so on `e^perp` the Schur matrix is

`N=C-qq^T/m`.

The block determinant formula gives

`det M = m det N`, hence

`det N = c det M/a`.

For the residual original rows, `V_C^T V_C=I-cee^T`, so `W=V_C E` satisfies `W^TW=I_2`. Outside-coordinate conditioning contributes only an arbitrary original-coordinate affine term, which is exactly within the stated rank-two affine theorem. No post-rotation independence is used. This algebraic component of the synthesis passes the B10 check; it does not by itself remove the outer zero-pivot branch addressed above.

## 8. Status

- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full arbitrary exact-rank-three orientation: **OPEN**.
- New scalar-leakage positive conditional `2/3` height-moment interface: **REFUTED**, by the exact formula (3.3).
- Same fixed rank-three target family: **uniformly controlled** by fleet02/B10 with `||p_Q||_infinity<=4sqrt(2)`.
- Rank-two affine Schur determinant/frame identity used by the current synthesis: **B10 algebra check passed**.
- Continuity: not proved by the new argument.

No Gaussianity, log-concavity, moments, compact support, connected support, or spectral-coordinate independence is assumed. No pointwise van-der-Corput estimate, arbitrary-joint coarea bound, conditional-density-cap surrogate, or fiber-sup argument is used.