# fleet02/B04 r26 — exact obstruction to an E2-only density endpoint

Run: `20260924T141659Z-fleet02-B04-fixedmult-auto11-r26`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **NEW SOURCE-VALID COUNTEREXAMPLE TO A TEMPTING INTERMEDIATE RECEIVER / NEW SPECIAL-CASE BILINEAR RECEIVER / MULTIPLICITY EIGHT STILL OPEN**.

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

The current multiplicity-eight terminal reduction supplies a literal physical `E_2` packet together with extra overlap-one/two-sided provenance. This note stress-tests whether the extra provenance can be discarded and the branch paid from `E_2>0` alone. The answer is **no**.

## 1. Positive control: a genuinely bilinear two-by-two block is already a density endpoint

Let `Y=(Y_1,Y_2)` and `Z=(Z_1,Z_2)` be disjoint original-coordinate banks, with all four coordinates independent and each density bounded by one. Let `B` be an invertible real `2 x 2` matrix. For arbitrary measurable finite `F(Y)`, arbitrary `beta in R^2`, and arbitrary constant `c`, consider

`Q = F(Y) + 2 Y^T B Z + beta^T Z + c`.

Then

`boxed: ||p_Q||_infinity <= sqrt(pi e) |det B|^(-1/2).`          (1.1)

The symmetric statement holds with the roles of `Y` and `Z` reversed. Thus arbitrary same-bank curvature is harmless on the bank that is conditioned first; the genuinely dangerous configuration is simultaneous quadratic curvature on both banks.

### Proof

Condition on `Y=y`. The remaining dependence on the independent product vector `Z` is the scalar linear form

`(2B^T y+beta).Z`

plus a deterministic shift. The baseline product-projection lemma gives its conditional density cap

`sqrt(e)/|2B^T y+beta|`

whenever the coefficient is nonzero. The unique exceptional `y` solving `2B^T y+beta=0` has probability zero because `Y` has a density, so the following measure-domination calculation is legitimate.

Put

`U=B^T Y+beta/2`.

Since the joint product density of `Y` is at most one, `U` has density `rho` with

`rho<=M:=|det B|^(-1)`, `int rho=1`.

For every such probability density on `R^2`, layer cake gives

`int rho(u)/|u| du
 =int_0^infinity [int_{|u|<1/t} rho(u)du] dt
 <=int_0^infinity min(1, M*pi/t^2)dt
 =2 sqrt(pi M).`                                                (1.2)

Averaging the conditional density therefore yields

`||p_Q||_infinity
 <= (sqrt(e)/2) int rho(u)/|u|du
 <= sqrt(pi e) |det B|^(-1/2)`.

No rotation of random coordinates is used. QED.

Numerically `sqrt(pi e)=2.922282365322278...`.

## 2. Counterexample: positive physical E2 does not imply bounded density with arbitrary curvature on both banks

Fix any `0<delta<eta=1/100`; for definiteness take

`delta=1/200`.

Let `Y_1,Y_2,Z_1,Z_2` be independent uniforms on `[-1/2,1/2]`, each with density exactly one. Put

`C=delta diag(1,-1)`,
`B=delta I_2`,
`D=delta diag(1,-1)`,

and define the symmetric four-coordinate quadratic form

`Q_delta = Y^T C Y + 2Y^T BZ + Z^T D Z`.

Equivalently,

`boxed: Q_delta
 = delta[(Y_1+Z_1)^2-(Y_2-Z_2)^2].`                            (2.1)

The literal physical cross block is `B=delta I_2`, so

`det B=delta^2>0`,

and its second crossing volume is

`boxed: E_2(B)=det(BB^T)=delta^4>0.`                            (2.2)

Nevertheless `Q_delta` has **unbounded density**.

### Exact density singularity

Let

`U=Y_1+Z_1`, `V=Y_2-Z_2`.

The pairs of original coordinates used in `U` and `V` are disjoint, so `U,V` are independent. Each has the triangular density

`g(u)=1-|u|`, `|u|<1`.

For `W=U^2`, the two inverse branches give

`h(w)=w^(-1/2)-1`, `0<w<1`.                                    (2.3)

Hence for `R=U^2-V^2=W_1-W_2` and `t>0`,

`p_R(t)=int_0^(1-t) h(v+t)h(v)dv`.

For `0<t<1/16` and `2t<=v<=1/8`, both `v` and `v+t` are at most `1/4`, so

`h(s)=s^(-1/2)-1 >= (2 sqrt(s))^(-1)`.

Also `v+t<=3v/2`. Therefore

`p_R(t)
 >= [1/(4 sqrt(3/2))] int_(2t)^(1/8) dv/v
 = [1/(4 sqrt(3/2))] log(1/(16t)).`                             (2.4)

Thus `p_R(t)->infinity` as `t downarrow0`, and since `Q_delta=delta R`,

`boxed: ||p_(Q_delta)||_infinity=infinity.`                     (2.5)

This is an essential-supremum divergence on neighborhoods, not merely an infinite value at a single point.

### The witness is inside the manuscript's no-pivot chamber

The coefficient matrix, in the order `(Y_1,Y_2,Z_1,Z_2)`, is

`A_delta=[[C,B],[B^T,D]]`.

Every diagonal entry has modulus `delta<eta`. The two principal pairs `(Y_1,Z_1)` and `(Y_2,Z_2)` have determinant zero, while every other principal two-coordinate determinant has modulus at most `delta^2<eta`. Hence `A_delta` has **no eta-pivot**.

For `delta=1/200`,

`delta^2=1/40000=2.5e-5<eta`,
`E_2(B)=delta^4=6.25e-10>0`.

The example has rank two, so it is not a counterexample to the fixed-multiplicity theorem and is not a multiplicity-eight target matrix. Its purpose is narrower and exact: it falsifies the local analytic implication

`positive/invertible physical two-by-two crossing + arbitrary same-bank curvature => bounded density`.

Indeed it falsifies any finite bound depending only on `E_2(B)>0` for this class.

## 3. Why this matters for the current s8 collar

The current terminal multiplicity-eight reduction has already produced a three-color cut with a dimension-free positive `E_2` packet and hence a uniform full half-potential. Equation (2.5) shows that this interface is genuinely only a half-potential interface: one cannot close the density endpoint by inventing a generic `E_2` density theorem while allowing arbitrary quadratic curvature on both banks.

The counterexample identifies the algebraic cancellation explicitly. Here

`D=B^T C^(-1)B`,

so the full four-variable block has Schur complement zero and rank two. In fact

`Q_delta = (Y+C^(-1)BZ)^T C (Y+C^(-1)BZ)`,

which is the physical product-law realization of the classical opposite-sign rank-two logarithmic singularity.

Therefore any valid multiplicity-eight receiver must retain at least one of the pieces that the three-color `E_2` reduction forgets:

- the shared physical overlap-one coordinate and its bordered residual square;
- the two-sided determinant-chain provenance;
- or an independently paid third smoothing/principal-curvature channel.

This matches the aggregate overlap-one identity currently available in the terminal branch. The relevant source-preserving shear for a seed `(S,T)` and common physical coordinate `h` is

`2X_S^T B X_T+2H c^T X_S+2H d^T X_T+aH^2
 =2(X_S+H B^(-T)d)^T B(X_T+H B^(-1)c)
 +(2D_h-a)H^2`,

where `D_h=a-d^T B^(-1)c`.

Unlike the counterexample (2.1), the terminal collar supplies a quantitatively large bordered residual on selected heavy common coordinates. The remaining difficulty is to spend that shared-source square without pretending the sheared variables are independent and without discarding arbitrary same-bank curvature.

## 4. Status and next exact obligation

**Proved here:**

1. a bilinear `2 x 2` physical crossing with arbitrary curvature on only the conditioned bank is a genuine bounded-density endpoint, (1.1);
2. positive `E_2` alone is not a density endpoint once both banks may carry arbitrary same-bank curvature, even for independent uniform cap-one inputs and even in the manuscript's no-pivot chamber, (2.1)--(2.5).

**Not proved:** multiplicity eight. The next exact obligation remains a dependence-safe overlap-one/two-sided-collar receiver that uses the common physical coordinate before absoluteization, or a dichotomy that forces a separate third smoothing channel.

The unrestricted three-eigenvalue conjecture remains OPEN.

No Gaussian, moment, support-size, log-concavity, diagonal-basis, post-rotation-independence or conditional-density shortcut is used. No task/schedule/state, notification, permission, authentication, public-release, paid-call or remote-workflow state was changed.
