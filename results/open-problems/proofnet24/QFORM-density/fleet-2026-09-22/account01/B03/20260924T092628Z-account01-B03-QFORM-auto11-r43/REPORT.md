SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T09:26:28Z.
attacking: cross-coupled split hubs — retain the common slope environment while paying a deterministic physical U-V cross term by two one-sided Plancherel envelopes, then use the account02/B03 complementary-weight compiler to close the critical four-hub packet.

# Cross-coupled shared-slope Fourier theorem and critical weighted-time splice

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **new supporting analytic theorem / designated account02-B03 result applied at an actual inequality / exact target families / full QFORM OPEN / unrestricted continuity OPEN**.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. First missing implication

The preceding B03 theorem `QFORM-SHARED-SLOPE-SPLIT-HUB-L1-v1` allowed two physical hub groups to use arbitrarily dependent slope vectors from the same environment, but required the deterministic quadratic cross block between the two hub groups to vanish. The first unpaid analytic question was whether a term

`2 U^T E V`

can be retained without conditioning one slope on the other and without using the refuted mixed norm

`int |t|^(-1/2) ||G_t||_2 dt`.

There is a clean answer with an exact cost: a completely arbitrary cross block `E` reduces the direct marginal-Plancherel decay exponent by a factor two, but does not destroy it. In total hub dimension `d>4` the resulting one-copy characteristic function is still `L^1`. In the critical `d=4` case the packet has a finite positive-half weighted time budget, and the newest account02/B03 conditional-environment compiler combines that budget with one fresh negative-half packet to recover an `L^1` characteristic function and linear small-ball scaling.

No conditional density `p_(M|L)` or `p_(L|M)` is used anywhere.

## 2. Cross-coupled marginal-Plancherel theorem

### Theorem 2.1 — `QFORM-CROSS-HUB-MARGINAL-PLANCHEREL-v1`

Let `r,s>=1`, `d=r+s`. Let

- `U in R^r` and `V in R^s` be independent random vectors, independent also of an arbitrary random object `Y`;
- the joint densities `f_U,f_V` satisfy `0<=f_U<=1`, `0<=f_V<=1` and have total mass one. In particular this includes disjoint blocks of original independent cap-one coordinates;
- `L=L(Y) in R^r` and `M=M(Y) in R^s` have marginal Lebesgue densities with
  `||p_L||_infinity<=K_L` and `||p_M||_infinity<=K_M`;
- no independence or joint-density assumption is imposed on `(L,M)`;
- `C,D` are arbitrary symmetric matrices of sizes `r,s`, `E` is an arbitrary real `r x s` matrix, and `R(Y)` is arbitrary measurable.

Define

`Q = U^T C U + V^T D V + 2 U^T E V + 2 U^T L(Y) + 2 V^T M(Y) + R(Y).`

Then, for every `t!=0`,

`boxed: |phi_Q(t)|^2 <= min{1, pi^(d/2) (K_L K_M)^(1/2) |t|^(-d/2)}.`        (2.1)

Consequences:

1. If `d>4`, then `phi_Q in L^1(R)`, `Q` has a continuous `C_0` density, and

`boxed: ||p_Q||_infinity <= [d/(d-4)] (K_L K_M)^(1/d).`                    (2.2)

2. If `d>1`, the assignment-specific negative-half whole-copy budget obeys

`boxed: A_-(Q):=int |t|^(-1/2)|phi_Q(t)|^2 dt`
`       <= [4d/(d-1)] sqrt(pi) (K_L K_M)^(1/(2d)).`                        (2.3)

3. If `d>3`, the positive-half time budget obeys

`boxed: A_+(Q):=int |t|^(1/2)|phi_Q(t)|^2 dt`
`       <= [4d/(3(d-3))] pi^(3/2) (K_L K_M)^(3/(2d)).`                     (2.4)

The theorem is uniform in the size, rank, sign and condition number of `E,C,D`.

### Proof

For fixed `t`, define the one-block transforms

`F_t(z)=E_U exp{i t[U^T C U+2U^T z]}`,
`G_t(z)=E_V exp{i t[V^T D V+2V^T z]}`.

For fixed slope values `(l,m)`, the full hub kernel is

`K_t(l,m)`
` = E_(U,V) exp{i t[U^T C U+V^T D V+2U^T E V+2U^T l+2V^T m]}`.

Integrating `U` first gives

`K_t(l,m)=E_V[ exp{i t(V^T D V+2V^T m)} F_t(l+EV) ].`

Cauchy--Schwarz with respect to the probability law of `V` yields

`|K_t(l,m)|^2 <= H_t(l),`

where

`H_t(l):=E_V |F_t(l+EV)|^2.`                                               (2.5)

Symmetrically,

`|K_t(l,m)|^2 <= J_t(m),`

where

`J_t(m):=E_U |G_t(m+E^T U)|^2.`                                            (2.6)

Hence pointwise

`|K_t(l,m)|^2 <= min(H_t(l),J_t(m)) <= sqrt(H_t(l)J_t(m)).`                 (2.7)

This is the key replacement for the unavailable exact factorization when `E!=0`.

Now

`phi_Q(t)=E_Y[ exp(i t R(Y)) K_t(L(Y),M(Y)) ]`.

Jensen followed by (2.7) and Cauchy--Schwarz over the common `Y` gives

`|phi_Q(t)|^2`
` <= E |K_t(L,M)|^2`
` <= E sqrt(H_t(L)J_t(M))`
` <= [E H_t(L)]^(1/2) [E J_t(M)]^(1/2).`                                  (2.8)

The two expectations can be bounded using only the marginal slope caps. Because `L` is independent of `V`, conditioning on `V=v` merely translates its density:

`E H_t(L)=E_(L,V)|F_t(L+EV)|^2`
` <= K_L int_R^r |F_t(z)|^2 dz.`                                           (2.9)

Put `h_t(u)=f_U(u) exp(i t u^T C u)`. With Fourier convention

`hat h(xi)=int h(u)exp(i xi^T u)du`,

one has `F_t(z)=hat h_t(2tz)`, so Plancherel gives

`int |F_t(z)|^2 dz`
` =(2|t|)^(-r)(2pi)^r int |h_t(u)|^2du`
` <= pi^r |t|^(-r),`                                                       (2.10)

because `int f_U^2<=||f_U||_infinity int f_U<=1`. Thus

`E H_t(L) <= pi^r K_L |t|^(-r).`                                           (2.11)

Exactly the same argument gives

`E J_t(M) <= pi^s K_M |t|^(-s).`                                           (2.12)

Substitution in (2.8) proves (2.1).

Set

`B=pi^(d/2)(K_LK_M)^(1/2),`
`T=B^(2/d)=pi(K_LK_M)^(1/d).`

Then

`|phi_Q(t)| <= min{1,B^(1/2)|t|^(-d/4)}.`

For `d>4`,

`int_R |phi_Q(t)|dt`
` <=2[T+B^(1/2)int_T^infinity t^(-d/4)dt]`
` =2pi [d/(d-4)](K_LK_M)^(1/d),`

which proves (2.2) by Fourier inversion and also gives continuity and vanishing at infinity.

For the negative-half budget,

`A_- <=2[int_0^T t^(-1/2)dt+B int_T^infinity t^(-(d+1)/2)dt]`
`    =[4d/(d-1)]T^(1/2),`

which is (2.3). For the positive-half budget (`d>3`),

`A_+ <=2[int_0^T t^(1/2)dt+B int_T^infinity t^(-(d-1)/2)dt]`
`    =[4d/(3(d-3))]T^(3/2),`

which is (2.4). QED.

## 3. Independent-copy interpretation

The only independent-copy identity used is the dependence-safe whole-output identity

`|phi_Q(t)|^2 = E exp(i t(Q-Q'))`,                                          (3.1)

where `Q'` is an independent copy of the entire scalar output. No coordinatewise pair `X_i-X_i'` is separated from `X_i+X_i'`, no such pair is declared independent, and no conditional cap is assigned to either member.

Using

`int_R |t|^(-1/2)e^(itx)dt = sqrt(2pi)|x|^(-1/2)`

in the regularized Riesz sense, (2.3) implies

`boxed: E|Q-Q'|^(-1/2)`
` <= [2sqrt(2)d/(d-1)] (K_LK_M)^(1/(2d)).`                                 (3.2)

The stronger one-copy `L^1_t` conclusion (2.2), not the collision estimate alone, is what yields linear small-ball scaling when `d>4`.

## 4. Dense-cross exact target family

The theorem is nontrivial even with maximal source overlap and a dense nonzero physical cross block.

Take independent cap-one coordinates

`U=(U_1,U_2,U_3), V=(V_1,V_2), Y=(Y_1,Y_2,Y_3)`

and set

`L=Y,       M=(Y_1,Y_2),`
`E=(1/10) J_(3x2),`

with `C=D=0`, and

`Q_dense = 2 U^T Y + 2 V_1Y_1+2V_2Y_2 + 2 U^T E V.`                        (4.1)

Here `K_L<=1`, `K_M<=1`, while `M` is literally a coordinate projection of `L`, so the slopes are maximally source-overlapping. Every entry of `E` is nonzero. Theorem 2.1 with `d=5` gives

`boxed: ||p_(Q_dense)||_infinity <=5,`                                     (4.2)

and `p_(Q_dense)` is continuous `C_0`.

This is inside the owner target. At `E=0` the symmetric coefficient matrix has nonzero eigenvalues

`{+sqrt(2),+sqrt(2),+1,-1,-sqrt(2),-sqrt(2)}`

(the crossing singular values are `sqrt(2),sqrt(2),1`). Turning on `E=(1/10)J_(3x2)` adds a symmetric perturbation of operator norm

`||E||_op=sqrt(6)/10<1/4.`

By Weyl, the two largest eigenvalues remain at least `sqrt(2)-sqrt(6)/10>1`, and the two most negative remain at most `-sqrt(2)+sqrt(6)/10<-1`. Thus (4.1) has at least four eigenvalues of modulus greater than one for every admissible input law.

## 5. Applying the completed account02/B03 result: critical d=4 cross packet

The newest completed designated partner result used here is

`yspennstate/math-open-problems@54243d0668be2be7879ae467ed9cb6b962f24652`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260924T081949Z-account02-B03-QFORM-auto11-r52/REPORT.md`,

claim `QFORM-CONDITIONAL-ENVIRONMENT-WEIGHTED-TIME-COMPILER-v1`.

Its exact inequality is: if, conditional on a physical environment `W`, two fresh packets factor as

`phi_Q(t)=E_W[F_W(t)G_W(t)]`,

with

`A_-(w)=int |t|^(-1/2)|F_w(t)|^2dt`,
`A_+(w)=int |t|^( 1/2)|G_w(t)|^2dt`,

then

`||p_Q||_infinity <= (2pi)^(-1)[E A_-]^(1/2)[E A_+]^(1/2).`                (5.1)

The same partner report supplies, for a scalar fresh-hub packet,

`A_-(w)<=8sqrt(pi M_-(w)/|gamma|).`                                        (5.2)

Apply (5.1) to a fresh scalar packet `S` and a cross-coupled packet `T` governed by Theorem 2.1. For the latter, (2.4) gives conditionally, whenever `d=r+s>=4`,

`A_+^T(w) <= [4d/(3(d-3))]pi^(3/2)`
`              *[K_L(w)K_M(w)]^(3/(2d)).`                                 (5.3)

Therefore

`boxed: ||p_Q||_infinity`
` <= sqrt(8d/[3(d-3)])`
`    *[E sqrt(M_-(W)/|gamma|)]^(1/2)`
`    *[E (K_L(W)K_M(W))^(3/(2d))]^(1/2).`                                  (5.4)

This is an actual equation-level use of the completed account02/B03 result. It closes the **critical four-hub cross-coupled packet** after adding one complementary negative-half fresh packet, even though Theorem 2.1 by itself only gives a borderline `|phi_T(t)|=O(|t|^-1)` envelope when `d=4`.

Under uniform caps `M_-<=K_-`, `K_LK_M<=K_x`, (5.4) becomes

`boxed: ||p_Q||_infinity`
` <= sqrt(8d/[3(d-3)]) (K_-/|gamma|)^(1/4) K_x^(3/(4d)).`                   (5.5)

At `d=4` the constant is exactly

`sqrt(32/3)=4sqrt(2/3)=3.265986323710904... .`                              (5.6)

## 6. Exact-target critical family with a nonzero U-V cross block

Take nine genuine independent cap-one coordinates

`H_0, Z, W, U_1,U_2,V_1,V_2,Y_1,Y_2`

and define

`Q_* = 2H_0(Z+W)`
`    + 2U_1(Y_1+W)+2U_2Y_2`
`    + 2V_1Y_1+2V_2Y_2`
`    + 2U_1V_1+2U_2V_2.`                                                   (6.1)

Condition on the original physical coordinate `W`. Then

`S_W=2H_0(Z+W)`

uses only fresh `(H_0,Z)`, while

`T_W=2U^T L_W+2V^T M+2U^T V`

uses only fresh `(U,V,Y)`, with

`L_W=(Y_1+W,Y_2),    M=(Y_1,Y_2),    E=I_2.`

Thus the packets are conditionally independent given `W`. The scalar slope `Z+W` has cap one, so (5.2) applies with `M_-=1`, `gamma=1`. Both two-dimensional slope marginals have cap one, although they are maximally dependent (`L_W` is a translate of `M`). The cross block is the nonzero invertible matrix `I_2`. Equation (5.5) at `d=4` gives

`boxed: ||p_(Q_*)||_infinity <=4sqrt(2/3)=3.265986323710904... .`            (6.2)

Hence for every interval `I`,

`boxed: P(Q_* in I)<=4sqrt(2/3)|I|.`                                       (6.3)

The proof is through an `L^1` characteristic function, so `Q_*` has a continuous `C_0` density.

The family satisfies the exact spectral target. The physical principal submatrix on

`(U_1,V_1,Y_1,U_2,V_2,Y_2)`

is the direct sum of two `3x3` matrices with zero diagonal and all three off-diagonal entries equal to one. Each has spectrum `{2,-1,-1}`. Thus the principal six-dimensional spectrum is

`{2,2,-1,-1,-1,-1}`.

Cauchy interlacing for the full nine-dimensional symmetric matrix gives two full eigenvalues at least `2` and one full eigenvalue at most `-1`. Therefore the full matrix has at least three eigenvalues of absolute value at least one. No diagonal-basis argument or rotation of the input law is used.

## 7. Whole-copy time integral for the critical family

The partner conditional factorization also gives a direct assignment-specific whole-copy estimate. Since `|G_W(t)|<=1`,

`|phi_(Q_*)(t)|^2`
` <= E_W |F_W(t)G_W(t)|^2`
` <= E_W |F_W(t)|^2.`

Integrating and applying (5.2) with `M_-=|gamma|=1`,

`boxed: int |t|^(-1/2)|phi_(Q_*)(t)|^2dt <=8sqrt(pi)`
`       =14.179630807244127... .`                                          (7.1)

By the whole-output identity (3.1),

`boxed: E|Q_*-Q_*'|^(-1/2) <=4sqrt(2)=5.656854249492381... .`               (7.2)

After the stronger one-copy density bound (6.2) is known, convolution gives `||p_(Q_*-Q_*')||_infinity<=4sqrt(2/3)`. The elementary cap-to-half-Riesz estimate then improves (7.2) to

`E|Q_*-Q_*'|^(-1/2)`
` <=4sqrt(2)(2/3)^(1/4)=5.111544833970179... ,`                             (7.3)

and correspondingly

`int |t|^(-1/2)|phi_(Q_*)(t)|^2dt`
` <=8sqrt(pi)(2/3)^(1/4)=12.812742807873674... .`                           (7.4)

Again this collision estimate is a consequence / companion of the stronger one-copy argument; it is not reversed into a density theorem.

## 8. Scope, obstruction and next step

The unrestricted conjecture is **not solved**.

This run removes the previous absolute obstruction “any nonzero physical U-V cross block breaks the shared-slope Plancherel method.” What remains is quantitative dimension / structural extraction:

- with only marginal slope caps and an arbitrary dense cross block, the present universal envelope has half the no-cross exponent and gives a one-copy density directly only when total hub dimension `d>4`;
- at the critical `d=4` endpoint, one additional complementary negative-half packet closes the time integral through the completed account02/B03 environment compiler;
- the truly hard target can still present only three immediately visible smoothing directions, or can distribute slope-density resources over grouped carriers in a way that does not expose either five cross-coupled hubs or a four-plus-one complementary-weight architecture.

The next B03 implication is therefore:

`QFORM-CROSS-HUB-CRITICAL-3D-TTSTAR` — for a `2+1` physical split with a nonzero cross block and arbitrarily dependent marginally bounded slopes, determine whether a dependence-safe integrated TT* estimate improves the generic half-exponent enough to make the time integral finite, or exhibit a source-valid obstruction forcing a grouped-carrier / pivot / ridge exit.

Full universal essential boundedness: **OPEN**.
Full-target continuous density: **OPEN**.

## 9. Sources and correction ledger


Partner theorem actually applied: `yspennstate/math-open-problems@54243d0668be2be7879ae467ed9cb6b962f24652`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260924T081949Z-account02-B03-QFORM-auto11-r52/REPORT.md`, especially equations (2.2), (3.1).

Relevant live corrections consumed include:

- `QFORM-POINTWISE-DECAY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`;
- `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`;
- `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`;
- the arbitrary-joint coarea and conditional positive-moment corrections recorded in `CURRENT_RESEARCH.md`.

No Gaussian, log-concavity, compact support, moment, connected-support, conditional-density-cap, rotated-independence, or diagonal-basis assumption is used. A manual scoped privacy review of this report found only mathematical/control-source content and no credentials, account secrets, unrelated private data, signed URLs or public-release material.
