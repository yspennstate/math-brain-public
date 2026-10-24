# Full Fourier Hessian on an explicit atom-ratio domain

17 September 2026. **PARTIAL; unrestricted Lyons conjecture OPEN.** This removes the direction restriction on the entire nonnegative-imbalance region and a further variance-controlled negative-imbalance region of the four-eigenvalue Fourier family. It is a written analytic proof with exact self-checks, not an independent audit or a historical-priority claim. The separate three-site `B_Phi` remains UNMEASURED. Model and reasoning settings are not independently exposed.

## 1. Statement

Let

    K(a,b,x,y)=F diag(a+x,b+y,a-x,b-y) F*,
    F[j,k]=i^(jk)/2,

and suppose the four eigenvalues lie strictly between zero and one. If

    x^2+y^2 >= (a-b)^2,                              (1)

then the **full four-variable entropy Hessian** in `(a,b,x,y)` is negative semidefinite. All four parameters can move independently; there is no sign condition on the direction.

Consequently entropy is concave along every affine segment contained in this region, and on every convex subset of it. The region itself is not asserted to be convex. Boundary-segment assertions follow by the regularization given below.

This is concavity within the fixed-Fourier commuting family, not in the entire sixteen-dimensional Hermitian space.

Section 6 proves the stronger combined pointwise criterion

    Var(N) log(P/O) <= 8/5,

where `N` is the DPP total count. In particular every strict Fourier kernel with `O/P>=1/4` is covered in all four directions.

## 2. Shift the three actual atom logarithms

Use the exact orbit probabilities and count notation of `FOURIER_ALL_MEANS.md`. In particular `f_2=4P+2O`, `O<=2P`, and

    8(O-P)=2[x^2+y^2-(a-b)^2].

Under (1), put `ell=log(O/P)`, so

    0<=ell<=log 2.

Instead of the previous three logarithms alpha, use

    A_0=alpha_0-ell=log[c_1^2/(f_0 O)],
    A_1=alpha_1-ell=log[P^2/(c_1c_3)],
    A_2=alpha_2-ell=log[c_3^2/(f_4 O)].              (2)

Every `A_k` is nonnegative by Hadamard-Fischer for the actual DPP atoms. For `A_0`, use the two singleton sets of an opposite pair; for `A_1`, use two adjacent pairs sharing a vertex; for `A_2`, use two triples whose intersection is an opposite pair.

Let `L_k=log[f_(k+1)^2/(f_k f_(k+2))]`. The previously proved bounds `L_k-alpha_k>=log 2` imply

    0<=A_k<=L_k-log 2.                              (3)

We deliberately use a uniform weaker bound here; the additional `ell` in the available margin is not needed.

## 3. A quantitative local count lemma

**Lemma.** For the four-trial count derivative quantities `Q_k,h_k`, every coefficient satisfying `0<=A<=L_k-log 2` obeys

    Q_k-h_k A >= (2/5)Q_k.                         (4)

Proof: if `h_k<=0`, the left side is at least `Q_k`. If `h_k>=0`, put

    rho=sqrt(f_k f_(k+2))/f_(k+1),  L_k=-2log rho.

The exact all-real-slope Hillion-Johnson local inequality gives

    h_k(1-rho^2)<=rho Q_k.

It suffices to prove

    rho[-2log rho-log 2] <= (3/5)(1-rho^2)         (5)

for `0<rho<1`. Set `rho=exp(-s)`. After dividing by rho, (5) is

    (6/5)sinh s-2s+log 2 >= 0.

The derivative vanishes only at `cosh s=5/3`, that is, `s=log 3`, and the second derivative is nonnegative. The global minimum on `s>=0` is

    8/5-log(9/2)>0.

For an entirely explicit last comparison,

    exp(8/5)>1+8/5+(8/5)^2/2+(8/5)^3/6
             =1711/375>9/2.

Thus (5) holds. Applying it to `h_k A<=rho A Q_k/(1-rho^2)` proves (4). This derivation uses the source inequality in its stated arbitrary-slope regime, not a monotone-slope version.

## 4. The remaining term depends only on the total mean

Write `w=(c,d,u,v)=(a',b',x',y')`. Its four Bernoulli slopes are `(c+u,d+v,c-u,d-v)`. From their definition,

    sum_(k=0)^2 h_k
       =(sum_i lambda_i')^2-sum_i(lambda_i')^2
       =2c^2+2d^2+8cd-2u^2-2v^2.                  (6)

The exact full curvature identity, with no discarded acceleration terms, is

    -H''=I_measured-sum_k h_k alpha_k+4cd ell.

Substitute `alpha_k=A_k+ell` and use (6). The result is

    -H''=I_measured-sum_k h_k A_k
                       +2ell[u^2+v^2-(c+d)^2].     (7)

The adverse interaction of the two pair means has become a penalty only in the total-mean direction.

The exact count Fisher rearrangement gives

    I_count=g_0^2/f_1+g_3^2/f_3+sum_k Q_k.

Using (4), and retaining the nonnegative excess `I_excess=I_measured-I_count`, equation (7) yields

    -H'' >= (2/5)I_count + I_excess
                       +2ell[u^2+v^2-(c+d)^2].     (8)

The boundary Fisher terms had coefficient one and are only reduced to `2/5` in this step; no term with an unknown sign was discarded.

## 5. Count information pays for total-mean motion

For the count law of four independent Bernoulli trials,

    (E N)'=sum_i lambda_i'=2(c+d),
    Var(N)=sum_i lambda_i(1-lambda_i)<=1.

Cauchy-Schwarz between the centered count and its score gives

    I_count >= ((E N)')^2/Var(N) >=4(c+d)^2.        (9)

Combining (8)-(9) gives the explicit lower bound

    -H'' >= (8/5-2ell)(c+d)^2
                         +2ell(u^2+v^2)+I_excess >=0.  (10)

The last inequality uses `0<=ell<=log 2<4/5`. For example, `exp(4/5)>1+4/5+(4/5)^2/2>2` verifies this last scalar comparison. This proves the full four-variable Hessian assertion.

The bound need not be strict in the opposite-mean direction `(c,d,u,v)=(c,-c,0,0)`. Equation (10) does not claim those directions are flat; it only supplies a nonnegative bound, which is sufficient for concavity.

For boundary segments lying in (1), contract each endpoint kernel toward `I/2` by the same factor `1-epsilon`. Then `a-b,x,y` all scale by that factor, so the sign in (1) is preserved. The regularized segment is strict. Integrate its Hessian inequality and pass to the original segment by continuity of entropy.

## 6. A further negative-imbalance region

The same quantitative lemma applies to the original `alpha_k`, since they too satisfy `0<=alpha_k<=L_k-log 2`. Without any imbalance assumption, equation (13) of `FOURIER_ALL_MEANS.md` therefore gives

    -H'' >= (2/5)I_count+I_excess+4cd ell.           (11)

Set `V_N=Var(N)>0`. Use `I_count>=4(c+d)^2/V_N` and `4cd=(c+d)^2-(c-d)^2`. For `ell<=0` this yields

    -H'' >= [8/(5V_N)+ell](c+d)^2
                              -ell(c-d)^2+I_excess.  (12)

Both displayed coefficients are nonnegative whenever

    V_N log(P/O)<=8/5.                             (13)

The variance is the explicit polynomial

    V_N=2[a(1-a)+b(1-b)-x^2-y^2].

For `ell>=0`, the previously proved theorem applies, and (13) holds automatically because its left side is nonpositive. Thus (13) is a sufficient full four-variable Hessian criterion throughout the strict physical domain.

Since `V_N<=1` and `log 4<8/5`, the simpler condition `O/P>=1/4` is sufficient. Criterion (13) also covers many kernels with much smaller `O/P`, because their count variance is small. For an arbitrary segment in the strict domain on which (13) holds at every point, integrating its Hessian inequality proves the corresponding chord inequality. No convexity of the full set (13), and no boundary regularization preserving (13), is assumed. The boundary-segment argument in Section 5 applies to the nonnegative-imbalance subregion as stated there.

## 7. Remaining region

The new theorem settles all Fourier bases satisfying (13). The favorable-direction proof from `FOURIER_ALL_MEANS.md` also handles every negative-imbalance base when `a'b'<=0`, including the fixed-diagonal cone theorem. The only Fourier directions still missing are therefore

    Var(N) log(P/O)>8/5   and   a'b'>0.             (14)

In words, the pair means move in the same direction at bases with a sufficiently strong deficit of opposite-pair atoms. The single scalar criterion in `FOURIER_ONE_SCALAR.md` remains available for this region. The full Lyons conjecture is not solved by these restricted advances.

`verify_fourier_positive.py` checks the rational comparisons in the local lemma, the slope-sum polynomial identity, and the full atom curvature against (10) and (12) at exact rational bases and directions, including previously adverse opposite-mean directions and variance-controlled negative-imbalance bases. These are self-checks of the written analytic proof.
