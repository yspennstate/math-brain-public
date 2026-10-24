SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T21:28:42Z.
attacking: the high-physical-diagonal branch; prove two-stage scalar-Schur singular-value persistence, pay every non-small second pivot, and reduce the remaining branch to a fixed-energy top-four scalar-Schur cross tube.

# account03/B01 — two-stage Schur persistence and high-diagonal routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T212842Z-auto11`  
Role: oscillatory replacement / quantitative inequalities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW TARGET-LEVEL ROUTING THEOREM + PAID HIGH-SECOND-PIVOT AND DIFFUSE-SCHUR SUBBRANCHES / FULL QFORM OPEN**

## 1. Target and correction boundary

The target is unchanged: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A` with `s_3(A)>=1`, and no moment, support, iid, Gaussian, log-concavity, connected-support, or diagonal-basis assumption. The desired universal `L^infinity` density bound remains open; continuity is separate.

Fresh owner control and the current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` were read. The current correction boundary is respected: no law-uniform pointwise quadratic-phase decay; no independence after rotation; no arbitrary-joint coarea cap; no deletion of small random quadratic tails on unbounded inputs; no use of the corrected-away individual-bank conclusion in account04/B01 Corollary 4.1.

The phase-aligned fragmented-support obstruction is preserved in Section 8.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner account04/B01 — exact overlap-two identity

Source:
`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

For a literal physical pair `(X,Y)` with

`B=[[a,b],[b,c]]`, `a!=0`,

complete only `X` and write

`delta=c-b^2/a`,
`ell=v-(b/a)u`,
`M=C-a^{-1}uu^T`.

For the second scalar completion put

`S=M-delta^{-1} ell ell^T` when `delta!=0`.

The partner identity is

`W2=a^2 sum_(k!=l)(delta M_kl-ell_k ell_l)^2`
`  =a^2 delta^2 F(S)`,                                           (2.1)

where

`F(S)=sum_(k!=l) S_kl^2`.                                       (2.2)

Only this exact identity is used below.

### 2.2 Determinant-free W2 quarter-Riesz receiver

Previous account03/B01 source:
`yspennstate/math-open-problems@26f7f13da915bad3b848ea49a91320c01c81cb1c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T203127Z-auto11/REPORT.md`.

For `a!=0`, `delta!=0`, `W2>0`,

`||p_Q||_infinity <= K_W |a|^(-1/4) W2^(-1/8)`,                 (2.3)

with

`K_W=77.02149767209895...`.                                     (2.4)

This bound is determinant-free after the exact cancellation in (2.1).

### 2.3 Rank-two affine half-Riesz receiver

Source:
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a literal two-coordinate quadratic block with determinant `Delta!=0`, arbitrary affine terms, and independent cap-one coordinates,

`sup_t E |Q_2-t|^(-1/2) <=128 |Delta|^(-1/4)`.                  (2.5)

The theorem is orientation-free in its proved scope and does not rotate the input law.

### 2.4 Fifth-volume and grouped-rank-three cross receivers

Applied through the source-pinned account04/B20 compiler
`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T142031Z-account04-B20-QFORM-r10/REPORT.md`.

For an original-coordinate cross block `N` of a quadratic form on independent cap-one variables, with

`Z5=e_5(N^T N)`,

one has

`||p||_infinity <=5 sqrt(2e) Z5^(-1/10)`.                       (2.6)

Also, if `s_3(N)>0`,

`||p||_infinity <=3e [s_1(N)s_2(N)s_3(N)]^(-1/3)`.              (2.7)

Both retain arbitrary same-bank curvature and affine terms in the cited scope.

### 2.5 Designated partner account04/B01 — signed Fejer equivalence

Source:
`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law `mu`,

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                     (2.8)

in the bounded-density sense, where `D_T` is the nonnegative triangular Fejer average. Thus every density bound below is also an averaged-frequency bound. No absolute Fourier `L^1` statement is asserted.

## 3. Rank-one perturbation lemma for scalar Schur complements

The first new observation is elementary but strong enough to survive arbitrary dimension.

### Lemma 3.1 — scalar Schur persistence

Let

`A=[[a,r^T],[r,C]]`, `a!=0`,

and define its scalar Schur complement

`H=C-a^{-1}rr^T`.                                                (3.1)

Then for every `k>=1`,

`s_(k+1)(A) <= s_k(H)`.                                          (3.2)

In particular,

`s_3(A)>=1  =>  s_2(H)>=1`.                                     (3.3)

#### Proof

Let

`w=(1,r/a)^T`.

Then exactly

`A=diag(0,H)+a w w^T`.                                           (3.4)

The second term has rank one. The standard rank-one singular-value interlacing inequality

`s_(k+1)(X+R)<=s_k(X)` for `rank(R)<=1`

applied to `X=diag(0,H)` gives (3.2). Since the nonzero singular values of `diag(0,H)` are those of `H`, (3.3) follows. QED.

Apply the same argument to a second nonzero scalar pivot of `H`. Write, after relabelling one remaining original coordinate as `Y`,

`H=[[delta,h^T],[h,C_2]]`, `delta!=0`,

and

`S=C_2-delta^{-1}hh^T`.                                         (3.5)

Then

`H=diag(0,S)+delta v v^T`                                       (3.6)

for an explicit vector `v`, hence

`s_1(S)>=s_2(H)>=1`.                                             (3.7)

No rotation or probabilistic assertion is involved.

## 4. Every non-small second scalar pivot is paid

Fix `0<alpha,beta<1`. Assume

`s_3(A)>=1`,                                                     (4.1)

and choose an original coordinate `X` with

`|a|=|A_XX|>=alpha`.                                             (4.2)

Let `H` be the scalar Schur complement (3.1). By Lemma 3.1,

`s_2(H)>=1`.                                                      (4.3)

Suppose some remaining original coordinate `Y` satisfies

`|delta|=|H_YY|>=beta`.                                          (4.4)

Let `S` be the second Schur complement (3.5). By (3.7),

`||S||_op>=1`.                                                    (4.5)

Put

`S=D+E`, `D=diag(S)`, `E=S-D`,

and

`F(S)=||E||_F^2`.                                                 (4.6)

There are two cases.

### Case A: `F(S)>=1/4`

By the designated account04/B01 identity (2.1),

`W2=a^2 delta^2 F(S) >= a^2 delta^2/4`.                          (4.7)

Apply the determinant-free W2 receiver (2.3):

`||p_Q||_infinity`
` <=K_W |a|^(-1/4)(a^2 delta^2 F)^(-1/8)`
` =K_W |a|^(-1/2)|delta|^(-1/4)F^(-1/8)`
` <=K_W 2^(1/4) alpha^(-1/2) beta^(-1/4)`.                      (4.8)

Numerically the prefactor is

`K_W 2^(1/4)=91.590...`.                                         (4.9)

### Case B: `F(S)<1/4`

Then

`||E||_op<=||E||_F<1/2`.                                         (4.10)

Since `||S||_op>=1`,

`||D||_op>1/2`.                                                   (4.11)

Hence some literal remaining original coordinate `Z_k` has

`|d_k|=|S_kk|>1/2`.                                              (4.12)

Before the second completion, the `(Y,Z_k)` physical block in the first residual has determinant exactly

`delta d_k`.                                                      (4.13)

Condition on every other remaining original coordinate. All couplings to them become affine terms, while `Y` and `Z_k` remain independent cap-one variables. Apply the rank-two affine half-Riesz theorem (2.5):

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)`
` <=128 |delta d_k|^(-1/4)`
` <=128 2^(1/4) beta^(-1/4)`.                                   (4.14)

Completing only the outer original coordinate `X`, conditional on all other variables, gives

`p_Q(t)<=|a|^(-1/2) E|R-t|^(-1/2)`.                             (4.15)

Therefore

`||p_Q||_infinity`
` <=128 2^(1/4) alpha^(-1/2) beta^(-1/4)`.                       (4.16)

Combining both cases proves:

### Theorem 4.1 — `QFORM-HIGHDIAG-HIGH-SCHURDIAG-PAID-v1`

Under (4.1)-(4.4), `Q` has an essentially bounded density and

`boxed:
||p_Q||_infinity
 <=128 2^(1/4) alpha^(-1/2) beta^(-1/4).`                        (4.17)

At `alpha=beta=1/64`,

`boxed: ||p_Q||_infinity <3444.312.`                             (4.18)

This theorem is sign-free, dimension-free, keeps every additional quadratic coefficient, and uses only literal original-coordinate conditioning.

## 5. If all second pivots are small, the scalar-Schur residual has a fixed cross-energy packet

Continue with `|a|>=alpha`, but now assume

`max_j |H_jj|<beta`.                                             (5.1)

Write

`H=D+O`, `D=diag(H)`, `diag(O)=0`.                               (5.2)

Then `||D||_op<beta`. By (4.3) and singular-value perturbation,

`s_2(O)>1-beta`.                                                  (5.3)

Since `s_1(O)>=s_2(O)`,

`||O||_F^2 >= s_1(O)^2+s_2(O)^2`
`           >2(1-beta)^2`.                                      (5.4)

Randomly two-color the remaining ORIGINAL coordinates into `J,K`. Because `O` is symmetric with zero diagonal, each unordered off-diagonal edge is separated with probability `1/2`; hence

`E ||O[J,K]||_F^2 = (1/4)||O||_F^2`.                            (5.5)

Therefore some deterministic original-coordinate cut satisfies

`boxed:
E_N:=||N||_F^2 > (1/2)(1-beta)^2,`
`N=H[J,K]=O[J,K].`                                               (5.6)

At `beta=1/64`,

`E_N > E_0:=3969/8192=0.4844970703125`.                          (5.7)

This is a strong fixed-energy packet in the actual scalar-Schur residual, not in rotated eigen-coordinates.

## 6. Two residual payments and the surviving top-four tube

Take now

`alpha=beta=1/64`,

and the cut `N` from (5.7). Let `x_r=s_r(N)^2`, ordered decreasingly, and

`E=sum_r x_r=||N||_F^2>E_0`,
`S_4=x_1+x_2+x_3+x_4`.                                           (6.1)

### 6.1 Diffuse fifth-volume branch

If

`S_4 <=(63/64)E`,                                                (6.2)

then the elementary five-distinct-draw estimate used in account04/B20 gives

`e_5(N^T N) >= (1/64)^4 E^5/120`.                               (6.3)

The fifth-volume receiver (2.6) applied to the residual quadratic form `R` therefore yields a continuous residual density with

`||p_R||_infinity`
` <=5 sqrt(2e) 120^(1/10) 64^(2/5) E_0^(-1/2)`
` <142.685.`                                                     (6.4)

Now use the following dependence-safe outer-square compiler, whose proof is included because the completed-square translation may depend on the same variables that generate `R`.

If

`Q=a(X+h(V))^2+R(V)`,                                            (6.5)

`X` is independent of `V`, `f_X<=1`, and `p_R<=M`, then

`p_Q(t)<=|a|^(-1/2) E|R-t|^(-1/2)`.                             (6.6)

Moreover

`P(|R-t|<rho)<=min(1,2M rho)`.                                  (6.7)

Layer cake gives

`E|R-t|^(-1/2)`
` <=int_0^infinity min(1,2M u^(-2)) du`
` =2 sqrt(2M)`.                                                   (6.8)

Thus

`boxed:
||p_Q||_infinity <=2 sqrt(2)|a|^(-1/2)M^(1/2).`                 (6.9)

Using `|a|>=1/64` and (6.4),

`boxed: ||p_Q||_infinity <270.286.`                              (6.10)

No independence between the shift `h(V)` and `R(V)` is assumed.

### 6.2 Rank-three cross branch

Suppose instead

`S_4 >(63/64)E`.                                                 (6.11)

If also

`s_3(N)>=1/256`,                                                 (6.12)

then

`x_1 >=S_4/4 >(63/256)E >(63/256)E_0`,                          (6.13)

while `x_2,x_3>=1/65536`. Hence

`s_1(N)s_2(N)s_3(N)`
` >sqrt((63/256)E_0)/65536`
` =5.2688512660583475e-6... .`                                   (6.14)

The grouped rank-three receiver (2.7) gives

`||p_R||_infinity <468.645`.                                    (6.15)

Applying (6.9),

`boxed: ||p_Q||_infinity <489.843.`                              (6.16)

### 6.3 Only surviving high-diagonal branch

Therefore, if `s_3(A)>=1` and some physical diagonal satisfies `|A_ii|>=1/64`, then either

`boxed: ||p_Q||_infinity <3444.312`,                             (6.17)

or after scalar completion at that literal coordinate there is an original-coordinate cut `J,K` of the residual Schur matrix `H` satisfying simultaneously

`boxed:
||H[J,K]||_F^2 >3969/8192,`                                     (6.18)

`boxed:
s_1(H[J,K])^2+...+s_4(H[J,K])^2 >(63/64)||H[J,K]||_F^2,`        (6.19)

and

`boxed:
s_3(H[J,K])<1/256.`                                             (6.20)

Thus the entire high-physical-diagonal part of the target is reduced to one fixed-energy, top-four-concentrated, effectively rank-two scalar-Schur cross tube. This is strictly narrower than the original arbitrary-matrix high-diagonal branch.

## 7. Relation to the global proof graph

The account04/B20 physical-cut theorem already treats the complementary regime in which every original physical diagonal is `<1/64` by producing a strong physical cross cut. The present theorem addresses the opposite regime rather than duplicating that low-diagonal work.

The next missing implication for B01 is therefore:

`QFORM-HIGHDIAG-SCHUR-TOP4-R2-TUBE-PAYMENT-v1`:

pay (6.18)-(6.20) after the outer completed square, retaining arbitrary same-bank curvature and the dependence between the outer square shift and the Schur residual. The natural mechanisms are a rank-two-cross fractional-potential estimate at the residual level or a hub/ridge promotion of the two dominant singular directions. Small operator residuals cannot simply be deleted because no input moment bound exists.

This does not solve the unrestricted conjecture. It does remove all non-small second-pivot states and both diffuse/high-rank residual cross states from the high-diagonal branch.

## 8. Phase-aligned scalar counterexample remains valid

Fix any prescribed frequency `s>0` and `0<eta<pi/2`. The set

`E={x: dist(s x^2,2pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite measurable union `E_0 subset E` of total measure one and let `f=1_(E_0)`. Then `f<=1` is a probability density and

`Re E exp(i s X^2) >=cos eta`.                                   (8.1)

Therefore no law-uniform estimate `|E exp(i sX^2)|<=C|s|^-gamma`, `gamma>0`, is available. The present theorem instead uses scalar-Schur geometry, fractional potentials, density small-ball estimates, and the signed-Fejer interface.

## 9. Averaged-frequency conclusion

By the designated account04/B01 signed-Fejer identity (2.8), each paid bound above is automatically an averaged-frequency estimate. In particular, throughout the high-second-pivot branch,

`boxed:
sup_(T>0,y) D_T law(Q)(y)
 <=128 2^(1/4) alpha^(-1/2) beta^(-1/4).`                        (9.1)

At `alpha=beta=1/64` this is `<3444.312`. The diffuse fifth-volume and rank-three residual payments give `<270.286` and `<489.843`, respectively.

No claim is made that `int |phi_Q|` is finite uniformly in this full scope.

## 10. Continuity, checks, and status

The fifth-volume and grouped-rank-three residual receivers supply continuous residual densities, but after the dependence-safe outer completed-square compiler this report proves only an essentially bounded density for the full `Q`. The high-second-pivot branch also establishes only essential boundedness. Full-target continuity remains open.

Deterministic checks in sibling `CHECKS.txt` verify the numerical constants, scaling, and 1,852 random two-stage Schur instances. The random checks are diagnostics only; the proof is the rank-one perturbation argument above.

Full QFORM status: **OPEN**.
