SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T11:07:22Z.
attacking: diffuse-chamber output Hölder regularity from the completed Fresnel envelope, sharpness at the leverage endpoint, and joint source/output stability via account02/B15 submass control.

# account01/B15 — sharp one-half output Hölder regularity in the diffuse Fresnel chamber

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260924T110722Z-account01-B15-QFORM-auto11`.
Status: `NEW_SUPPORTING_REGULARITY_THEOREM / PARTNER_APPLIED / FULL_QFORM_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and dependencies

The unrestricted owner target remains open: for independent cap-one input densities and symmetric `A` with at least three eigenvalues of modulus at least one, no source consumed here proves one universal density height for every matrix.

This report uses two completed sources in their exact scopes.

1. Fresnel--Brascamp--Lieb Theorem F:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
   For
   `A=sum_{k=1}^3 lambda_k v_k v_k^T+B`, an ORIGINAL-coordinate set `I` with `B_II` diagonal, `rho_i=((v_1)_i,(v_2)_i,(v_3)_i)`, `G_I=sum_{i in I}rho_i rho_i^T`, and normalized leverages `rho_i^T G_I^{-1}rho_i<=1/2`, it proves
   `|phi_Q(t)| <= (4 pi)^(3/2)|t|^(-3/2)(|lambda_1 lambda_2 lambda_3| det G_I)^(-1/2)`
   and
   `||p_Q||_infinity <=12(|lambda_1 lambda_2 lambda_3| det G_I)^(-1/3)`.
   The product factorization is performed in the original independent coordinates; no independence after spectral rotation is asserted.

2. Designated partner account02/B15:
   `yspennstate/math-open-problems@084356368f3e6a4de2486d6fccc60e0a3f157524`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T100100Z-account02-B15-QFORM-auto11/REPORT.md`.
   Its `QFORM-FRESNEL-DIFFUSE-L1-STABILITY-v1` theorem says, in the exact-rank-three diffuse frame `A=D+R Lambda R^T`, `R^T R=I_3`, `c_i=|R_{i,*}|^2<=1/2`, `L=|det Lambda|`, that for two cap-one product inputs with `delta_i=||f_i-g_i||_1`,
   `||p_f-p_g||_infinity <=12 L^(-1/3) sum_i c_i^(-c_i/3) delta_i^(1-2c_i/3)`.

The live corrections are preserved: no law-uniform pointwise quadratic Fourier decay is claimed; the pointwise decay below is only the completed Theorem-F chamber estimate. No rotated-independence step and no projection-only/X-ray shortcut occurs.

## 2. Qualitative absolute continuity is a weaker issue

Let `F dx` be any absolutely continuous joint law on `R^n` and let
`q(x)=x^T A x+b^T x+c`
be nonconstant. Then `q(X)` is absolutely continuous.

Indeed `grad q(x)=2Ax+b`. The critical set is empty or an affine translate of `ker A`, hence Lebesgue-null unless `A=0`; if `A=0` and `b!=0`, it is empty. For a null set `N subset R`, put
`E_k=q^{-1}(N) intersect {|grad q|>=1/k}`.
Coarea gives
`int_{E_k}|grad q(x)| dx = int_N H^{n-1}(q^{-1}(t) intersect {|grad q|>=1/k}) dt=0`,
so `|E_k|=0`. Adding the null critical set gives `|q^{-1}(N)|=0`, and the absolutely continuous input law assigns it probability zero.

This proves density existence only. It neither uses nor implies a universal height bound, and it does not invoke the refuted arbitrary-joint bounded coarea estimate.

## 3. A Fourier-to-Hölder compiler

### Lemma 1 — `QFORM-FOURIER-ALPHA-TO-HOLDER-v1`

Let a probability law on `R` have characteristic function `phi`. Suppose for some `1<alpha<2` and `B<infinity`,

`|phi(t)| <= B |t|^(-alpha)` for every `t!=0`.

Then the law has a density `p in C_0(R)` and

`[p]_{C^{0,alpha-1}}
 <= [2^(2-alpha)/pi] [1/(2-alpha)+1/(alpha-1)] B.`                 (3.1)

In particular, for `alpha=3/2`,

`boxed( |p(x+h)-p(x)| <= (4 sqrt(2)/pi) B sqrt(|h|). )`             (3.2)

### Proof

Because also `|phi(t)|<=1`, the envelope `min(1,B|t|^(-alpha))` is integrable, so Fourier inversion gives a canonical density `p in C_0`. For `h!=0`,

`|p(x+h)-p(x)|
 <=(1/(2pi)) int_R |e^{-ith}-1||phi(t)|dt
 <=(B/pi) int_0^infinity min(2,|h|t)t^(-alpha)dt.`

Split at `T=2/|h|`. The two pieces are

`|h| int_0^T t^(1-alpha)dt =2^(2-alpha)|h|^(alpha-1)/(2-alpha)`,

`2 int_T^infinity t^(-alpha)dt =2^(2-alpha)|h|^(alpha-1)/(alpha-1)`.

This is (3.1), and `alpha=3/2` gives (3.2).

The lemma does not say that such a Fourier envelope holds throughout QFORM. The phase-aligned-density correction rules that out. It is used only after a structural theorem has genuinely paid the envelope.

## 4. New target-level regularity theorem in the Theorem-F chamber

### Theorem 2 — `QFORM-FRESNEL-HALF-HOLDER-v1`

Under the completed Theorem-F hypotheses, put

`M=|lambda_1 lambda_2 lambda_3| det G_I`.

Then the output density satisfies, separately,

`boxed( ||p_Q||_infinity <=12 M^(-1/3), )`                          (4.1)

and

`boxed( p_Q in C_0(R),
        |p_Q(x+h)-p_Q(x)| <=32 sqrt(2 pi) M^(-1/2) sqrt(|h|). )`     (4.2)

### Proof

Equation (4.1) is the already-completed Theorem-F height estimate. It is paid before any continuity argument. Its characteristic-function estimate has `alpha=3/2` and

`B=(4pi)^(3/2) M^(-1/2)`.

Substitute this `B` into Lemma 1:

`(4sqrt(2)/pi)(4pi)^(3/2)=32sqrt(2pi)`.

This proves (4.2).

Thus, within this diffuse/product-preserving chamber, continuity is strictly downstream of the central essential-height payment. The theorem gives a quantitative output modulus, but only under the leverage/diagonal-residual gate of Theorem F; it is not an owner-wide modulus.

## 5. The exponent one-half is sharp at the leverage endpoint

The `1/2` in Theorem 2 cannot be improved uniformly even inside the exact-rank-three leverage-endpoint chamber.

Let `X_1,...,X_6` be iid `Unif[-1/2,1/2]`, define

`Y_1=(X_1+X_2)/sqrt(2)`,
`Y_2=(X_3+X_4)/sqrt(2)`,
`Y_3=(X_5+X_6)/sqrt(2)`,

and

`Q=Y_1^2+Y_2^2+Y_3^2`.

The matrix is `A=RR^T`, where `R^T R=I_3` and every row leverage is exactly `1/2`. Its nonzero eigenvalues are `{1,1,1}`, so this is an exact owner-target matrix and exactly the endpoint `max c_i=1/2` of Theorem F.

The triangular density of each `Y_k` is

`p_Y(y)=sqrt(2)(1-sqrt(2)|y|),  |y|<1/sqrt(2)`.

Therefore `S=Y_k^2` has

`h(s)=sqrt(2)s^(-1/2)-2,  0<s<1/2`.

For `0<t<1/2`, all three simplex variables remain below `1/2`, so the convolution is exact. Writing `k(s)=s^(-1/2)1_{s>0}` and `u(s)=1_{s>0}`, and using

`k*k=pi`,
`k*k*k=2pi sqrt(t)`,
`k*u*u=(4/3)t^(3/2)`,
`u*u*u=t^2/2`,

one obtains

`boxed( p_Q(t)=4sqrt(2)pi sqrt(t)-12pi t+16sqrt(2)t^(3/2)-4t^2,
        0<t<1/2. )`                                                (5.1)

The continuous representative has `p_Q(0)=0` and

`boxed( lim_{t downarrow0} p_Q(t)/sqrt(t)=4sqrt(2)pi. )`            (5.2)

Hence this family is not `C^{0,beta}` at zero for any `beta>1/2`. The half-Hölder exponent is therefore sharp for a universal regularity statement at the Theorem-F leverage endpoint, even though the height itself is uniformly finite.

This also reinforces the logical separation: bounded density, continuity, and stronger Hölder regularity are distinct assertions.

## 6. Designated account02/B15 partner applied to a genuinely coupled exact-target inequality

Take the orthogonal matrix with rows

`u_1=(1,2,2)/3`,
`u_2=(2,1,-2)/3`,
`u_3=(2,-2,1)/3`.

Let the six rows of `R` be successively
`+u_1/sqrt(2), -u_1/sqrt(2), +u_2/sqrt(2), -u_2/sqrt(2), +u_3/sqrt(2), -u_3/sqrt(2)`.
Then `R^T R=I_3` and every row leverage is `c_i=1/2`. Put

`Lambda=diag(1,2,4)`,
`A_*=R Lambda R^T`.

Explicitly,

`A_*=(1/18) *
 [[ 25,-25,-10, 10,  2, -2],
  [-25, 25, 10,-10, -2,  2],
  [-10, 10, 22,-22, -8,  8],
  [ 10,-10,-22, 22,  8, -8],
  [  2, -2, -8,  8, 16,-16],
  [ -2,  2,  8, -8,-16, 16]].`

Its nonzero eigenvalues are exactly `{1,2,4}`. Thus it is an exact owner-target matrix, and it is nonseparable in the original coordinates. No claim is made that the three spectral linear forms are independent.

Let `f=(f_i)` and `g=(g_i)` be any two cap-one product laws on these six original coordinates, set

`delta_i=||f_i-g_i||_1`, `Delta=sum_i delta_i`.

Apply the completed account02/B15 theorem with `L=8`, `c_i=1/2`:

`||p_f-p_g||_infinity
 <=6*2^(1/6) sum_{i=1}^6 delta_i^(2/3)
 <=6sqrt(2) 3^(1/3) Delta^(2/3).`                                  (6.1)

The last step is concavity: `sum delta_i^(2/3)<=6^(1/3)Delta^(2/3)`.
Numerically the coefficient in (6.1) is `<12.238`.

The completed Theorem F separately pays the central height for this matrix,

`boxed( ||p_f||_infinity, ||p_g||_infinity <=6. )`                  (6.2)

The new Theorem 2 gives the output half-Hölder modulus

`boxed( |p_f(s)-p_f(t)| <=16sqrt(pi)|s-t|^(1/2), )`                 (6.3)

because `32sqrt(2pi)/sqrt(8)=16sqrt(pi)`.

Combining the partner estimate with (6.3) produces the actual joint source/output inequality

`boxed(
 |p_f(s)-p_g(t)|
 <=6sqrt(2)3^(1/3) Delta^(2/3)+16sqrt(pi)|s-t|^(1/2).
)`                                                                   (6.4)

This is a dimension-free quantitative regularity statement for a genuinely coupled exact-target matrix. Its first term is a direct application of the completed designated-partner result; its second term is the new output-variable regularity theorem.

## 7. Exact implication ledger

Qualitative absolute continuity: already true for every nonconstant affine quadratic of an absolutely continuous joint law, with no cap-one or three-eigenvalue hypothesis.

Essential boundedness: the hard quantitative layer. The full universal owner theorem remains open. In the Theorem-F chamber it is paid by (4.1).

Continuous density: in the Theorem-F chamber it follows from the integrable characteristic function and costs no increase in the already-paid height. A separate fixed-Hessian theorem (`account03/B15`, `math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`) gives a canonical `C_0` density for every fixed rank-at-least-three affine Hessian under arbitrary rough cap-one product inputs, but with a matrix-dependent height; that does not solve the universal owner bound.

Quantitative output regularity: Theorem 2 gives a universal one-half Hölder exponent inside the diffuse Theorem-F chamber, with explicit matrix parameter `M`; Section 5 proves that the exponent is sharp at the leverage endpoint. This does not contradict the already-known absence of a target-wide universal continuity modulus: the coefficient in (4.2) depends on the structural Fresnel determinant parameter.

The first unpaid implication remains structural rather than regularity-theoretic: starting only from `s_3(A)>=1`, obtain a product-preserving universal height receiver without assuming the Theorem-F leverage/diagonal-residual gate, without reciprocal tiny-minor loss, and without conditioning to a bad worst fibre.

No FEI work, scheduler mutation, email, push notification, public release, permission expansion, cross-account authentication, paid call, or remote workflow is used here.
