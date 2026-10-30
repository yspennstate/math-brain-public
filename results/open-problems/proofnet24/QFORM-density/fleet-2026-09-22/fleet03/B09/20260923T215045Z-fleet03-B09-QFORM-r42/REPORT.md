SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T21:50:45Z.
attacking: the grouped rank-two small-Delta survivor by replacing the fixed L4 kernel-derivative estimate with a full Lp family and optimizing p down toward the quadratic endpoint.

# fleet03/B09 — adaptive Lp kernel-derivative smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism  
Run: `20260923T215045Z-fleet03-B09-QFORM-r42`  
Status: **NEW SUPPORTING THEOREM, PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and current source state

The target is unchanged: for every finite n, independent original-coordinate real variables with densities at most one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal bound on the density of Q=X^TAX or give a valid counterexample. No moments, compact support, connected support, Gaussianity, log-concavity, iid hypothesis, diagonal-basis hypothesis, or post-rotation independence is introduced.


The immediate predecessor is fleet03/B09 r41:

`yspennstate/math-open-problems@39f45eeebf3d7a9609c4e26c14f2f8ad5b6b3fb1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T211657Z-fleet03-B09-QFORM-r41/REPORT.md`.

It proved, for a three-coordinate physical left bank and an arbitrary-width rank-two physical cross bank,

`||p_Q||_infinity <= C_4 Delta^(-2/5)||Pn||^(-1/5)`,

with

`C_4=5*6^(3/5)/2^(9/10)=7.85115874294336...`,

and the exact overlap identity

`V = Delta^2 ||Pn||^2`.

The open issue was the residual power loss in Delta when V stays order one but Delta becomes small. This run replaces the fixed exponent p=4 by a complete p>2 family. The resulting loss can be reduced from a power to a logarithm.

A second source reused exactly as in r41 is the reviewed orthonormal-product projection cap

`||p_{R^T Z}||_infinity <= 2^(r/2)`

for an r-dimensional orthonormal projection of an independent cap-one product law; only r=1 and r=2 are used. Source:

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The designated fleet04/B09 partner theorem is source-pinned at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that a literal invertible physical 3x3 cross block K gives

`||p_Q||_infinity <= 3 |det K|^(-1/3)`

with arbitrary dense same-side curvature and a continuous density.

## 2. Setup

Let L and J be disjoint sets of ORIGINAL coordinates with |L|=3 and J arbitrary. After conditioning on every original coordinate outside L union J, write

`Q = Y^T P Y + 2 Y^T C Z + G(Z) + ell^T Y + const`,          (2.1)

where Y=X_L is a three-dimensional product vector with joint density at most one, Z=X_J is the original-coordinate product bank, P=A[L,L], C=A[L,J], and G is an arbitrary real quadratic-affine polynomial on J.

Assume

`rank(C)=2`.                                                       (2.2)

Let n be a unit vector spanning ker(C^T), set

`a = P n`,                                                         (2.3)

and let

`Delta = sigma_1(C) sigma_2(C) = sqrt(pdet(CC^T)) > 0`.           (2.4)

The branch considered here is a != 0.

Choose an orthonormal 3x2 frame E spanning n^perp and analytically write

`Y = n x + E u`,  x in R, u in R^2.                               (2.5)

This is only a change of variables inside the integral; no independence is asserted in (x,u). The transformed left density rho(x,u) is still bounded by one and has mass one.

Because range(C)=n^perp, B=E^T C has full row rank two. Factor

`B = L_0 R^T`,                                                     (2.6)

where R^T R=I_2 and det(L_0)=Delta. Put V=R^T Z. The projection theorem gives

`||p_V||_infinity <= 2`.                                          (2.7)

Push the complex measure exp(it G(Z)) dP_Z to V. Its density b_t(v) obeys |b_t(v)|<=p_V(v), hence

`||b_t||_2 <= sqrt(2)`.                                           (2.8)

In the (n,E) basis write

`P -> [[d,p^T],[p,P_0]]`.

For fixed u the x-dependent polynomial is

`q_u(x)=d x^2 + (2 p^T u + beta)x`,                               (2.9)

where beta is the conditioned affine coefficient. Put

`h_u(x)=rho(x,u)`, `m(u)=int h_u`,

`F_u(t)=int h_u(x) exp(it q_u(x)) dx`,

`A(t)^2=int_R2 |F_u(t)|^2 du`.                                   (2.10)

The two-dimensional projection cap gives

`m(u)<=2`.                                                         (2.11)

The decisive derivative identity is still

`q_u'(x)=2d x+2p^T u+beta = 2(Pn)^T Y + beta = 2 a^T Y+beta`.     (2.12)

Thus the singular derivative is a genuine linear projection of the original independent physical triple.

## 3. New p>2 left-fiber estimate

### Theorem 3.1 — `QFORM-GROUPED-RANK2-LP-FAMILY-v1`

For every p>2,

`||A||_p <= K_p ||a||^(-1/p)`,                                   (3.1)

where

`K_p=(4*pi)^(1/p) 2^(1/2-1/(2p)) sqrt(p/(p-2))`.                 (3.2)

This specializes at p=4 to the exact r41 bound

`||A||_4 <= 2^(11/8) pi^(1/4)||a||^(-1/4)`.

### Proof

Let

`r=p/(p-1) in (1,2)`, `gamma=2/p`.                               (3.3)

For almost every u, q_u is nonconstant and has at most two inverse branches. Let nu_u be the pushforward density of h_u(x)dx under q_u. Coarea and

`(s+t)^r <= 2^(r-1)(s^r+t^r)`

give

`||nu_u||_r^r
 <= 2^(r-1) I_r(u)`,                                             (3.4)

where

`I_r(u)=int h_u(x)^r |q_u'(x)|^(-(r-1)) dx`.                     (3.5)

With the angular Fourier convention, Hausdorff--Young gives

`||F_u||_p <= (2*pi)^(1/p)||nu_u||_r`,

hence after squaring and using (3.4),

`||F_u||_p^2 <= (4*pi)^(2/p) I_r(u)^(2/r)`.                      (3.6)

Since h_u<=1,

`I_r(u) <= J(u):=int h_u(x)|q_u'(x)|^(-1/(p-1)) dx`.             (3.7)

Normalize the fiber by h_u/m(u). Because 2/r>1, Jensen yields

`J(u)^(2/r)
 <= m(u)^(2/r-1)
    int h_u(x)|q_u'(x)|^(-2/p) dx`.                              (3.8)

Using m(u)<=2 and integrating over u,

`int I_r(u)^(2/r) du
 <= 2^(1-2/p) E |2a^T Y+beta|^(-2/p)`.                           (3.9)

The one-dimensional projection W=(a/||a||)^T Y has density cap sqrt(2). Therefore T=2a^T Y+beta has density cap

`S_T <= 1/(sqrt(2)||a||)`.                                       (3.10)

For any probability density f<=S and 0<gamma<1, the exact bathtub bound is

`E|T|^(-gamma) <= (2S)^gamma/(1-gamma)`.                         (3.11)

Indeed the extremizer is S times the indicator of the centered interval of length 1/S. With gamma=2/p and (3.10),

`E |2a^T Y+beta|^(-2/p)
 <= 2^(1/p) [p/(p-2)] ||a||^(-2/p)`.                             (3.12)

Now Minkowski in L^(p/2) gives

`||A||_p^2
 = || int |F_u(t)|^2 du ||_(p/2)
 <= int ||F_u||_p^2 du`.                                         (3.13)

Combining (3.6), (3.9), and (3.12),

`||A||_p^2
 <= (4*pi)^(2/p) 2^(1-1/p) [p/(p-2)] ||a||^(-2/p)`,             (3.14)

which is exactly (3.1)-(3.2). QED.

Remarks. The p>2 restriction is the exact integrability threshold of the inverse derivative moment gamma=2/p<1. No pointwise quadratic-phase decay has been used. When d=0, the exceptional affine line 2p^T u+beta=0 has two-dimensional Lebesgue measure zero because a!=0 forces p!=0.

## 4. Bilinear Plancherel and the full density family

As in r41, after absorbing all u-only and v-only terms into unit-modulus phases,

`phi_Q(t)=int int F_u(t)b_t(v) exp(2it u^T L_0 v) du dv`.         (4.1)

Two-dimensional Plancherel and (2.8) give, for t!=0,

`|phi_Q(t)|
 <= pi sqrt(2) Delta^(-1/2)|t|^(-1) A(t)`.                       (4.2)

Also |phi_Q(t)|<=1.

Let q=p/(p-1). For T>0, Holder on |t|>T and (3.1) yield

`int_{|t|>T}|phi_Q(t)|dt
 <= H_p Delta^(-1/2)||a||^(-1/p) T^(-1/p)`,                      (4.3)

where

`H_p = pi sqrt(2) K_p [2(p-1)]^((p-1)/p)`.                       (4.4)

The head contributes at most 2T. Optimizing

`2T + H_p Delta^(-1/2)||a||^(-1/p)T^(-1/p)`                     (4.5)

gives

`T_* = [H_p/(2p) Delta^(-1/2)||a||^(-1/p)]^(p/(p+1))`.          (4.6)

At this optimum the tail equals 2p T_*, so Fourier inversion gives the following theorem.

### Theorem 4.1 — adaptive grouped rank-two density family

For every p>2,

`boxed:
 ||p_Q||_infinity
 <= C_p Delta^(-p/[2(p+1)]) ||Pn||^(-1/(p+1)),`                  (4.7)

where

`C_p = (p+1)/pi [H_p/(2p)]^(p/(p+1))`.                           (4.8)

The characteristic function is in L1, so this branch has a continuous density. The same coefficient multiplies interval length:

`P{Q in I} <= C_p Delta^(-p/[2(p+1)])||Pn||^(-1/(p+1)) |I|`.    (4.9)

At p=4, direct algebra gives exactly

`C_4 = 5*6^(3/5)/2^(9/10)=7.85115874294336...`,                 (4.10)

so r41 is recovered exactly rather than merely qualitatively.

At p=3,

`C_3 = 6.87156667535726...`.                                     (4.11)

As p=2+epsilon tends to two from above,

`boxed:
 C_{2+epsilon} = (3 sqrt(2)+o(1)) epsilon^(-1/3).`               (4.12)

The asymptotic follows directly from (3.2), (4.4), and (4.8):

`H_{2+epsilon}/[2(2+epsilon)]
 ~ 2^(3/4) pi^(3/2) epsilon^(-1/2)`,

whose power 2/3, multiplied by (p+1)/pi ->3/pi, gives 3sqrt(2) epsilon^(-1/3).

## 5. The overlap currency and logarithmic loss instead of a power loss

The r41 exact exterior identity remains

`V = Delta^2 ||Pn||^2`.                                          (5.1)

Define the scale-invariant anisotropy ratio

`R = ||Pn||^2 / Delta`.                                          (5.2)

Under scaling A -> sA, both numerator and denominator scale by s^2, so R is dimensionless. Equation (4.7) becomes

`boxed:
 ||p_Q||_infinity
 <= C_p V^(-1/6) R^((p-2)/[6(p+1)]).`                            (5.3)

Thus the old p=4 estimate pays the power R^(1/15), equivalently Delta^(-1/5) at fixed V. Sending p down toward two turns that power loss into a logarithm.

### Corollary 5.1 — explicit logarithmic anisotropy bound

For every branch satisfying the hypotheses above,

`boxed:
 ||p_Q||_infinity
 <= 8.824 V^(-1/6) [1+log_+ R]^(1/3).`                           (5.4)

The same bound multiplies |I| for interval probabilities, and the density is continuous.

Proof. If R<=e^6, choose p=3. Then R^(1/24)<=e^(1/4), so (5.3) and (4.11) give

`||p_Q||_infinity
 <= C_3 e^(1/4) V^(-1/6)
 = 8.8232662636... V^(-1/6)`.                                    (5.5)

If R>e^6, put

`epsilon=6/log R in (0,1)`, `p=2+epsilon`.                        (5.6)

Then

`R^((p-2)/[6(p+1)]) = exp(1/(p+1)) <= e^(1/3)`.                 (5.7)

For 0<epsilon<=1, the exact formula (4.8) admits the elementary bound

`C_{2+epsilon} <= 9.839 epsilon^(-1/3)`.                         (5.8)

For completeness: after extracting epsilon^{-p/[2(p+1)]}, the residual epsilon exponent differs from -1/3 by only -epsilon/[6(3+epsilon)]; using epsilon log(1/epsilon)<=1/e gives a factor <=exp(1/(18e)). The remaining p-dependent factors on 2<=p<=3 are bounded by

`(4/pi) [2^(17/12) pi^(3/2)]^(3/4)`,

and the product is 9.838391409... <9.839. Therefore (5.6)-(5.8) imply

`||p_Q||_infinity
 < 9.839 (e/6)^(1/3) V^(-1/6)(log R)^(1/3)
 < 7.557 V^(-1/6)(log R)^(1/3)`.                                 (5.9)

Combining (5.5) and (5.9) gives (5.4). QED.

The asymptotically optimized coefficient from the exact C_p formula is smaller:

`3 sqrt(2)(e/6)^(1/3)=3.25849703177...`                          (5.10)

in front of `V^(-1/6)(log R)^(1/3)` as R->infinity. The explicit 8.824 in (5.4) is deliberately coarse and fully elementary.

## 6. Target-valid stress family: R is genuinely unbounded

The bare three-large-eigenvalue hypothesis does not bound R. This is important because it means the remaining logarithm cannot be removed merely by proving a spectral upper bound on the anisotropy ratio.

For 0<epsilon<1, take five physical coordinates ordered as (x1,x2,x3,z1,z2), and let

`P_epsilon = [[0,0,epsilon^(-1)],
              [0,1,0],
              [epsilon^(-1),0,0]]`,

`C_epsilon = [[1,0],
              [0,epsilon],
              [0,0]]`,

with zero right self-block. Thus

`A_epsilon = [[P_epsilon,C_epsilon],
              [C_epsilon^T,0_2]]`.                               (6.1)

The cross singular values are 1 and epsilon, so

`Delta=epsilon`, `n=e3`, `Pn=epsilon^(-1)e1`.                    (6.2)

Hence

`V=Delta^2||Pn||^2=1`,

`R=||Pn||^2/Delta=epsilon^(-3) -> infinity`.                      (6.3)

The spectrum is explicit. On span{x1,x3,z1}, the eigenvalues are

`+sqrt(1+epsilon^(-2)), 0, -sqrt(1+epsilon^(-2))`.               (6.4)

On span{x2,z2}, they are

`lambda_+ = [1+sqrt(1+4epsilon^2)]/2 >1`,

`lambda_- = [1-sqrt(1+4epsilon^2)]/2`.                            (6.5)

Therefore A_epsilon has at least three eigenvalues of absolute value >=1 for every 0<epsilon<1. This is a genuine target-valid family.

At fixed V=1, the r41 p=4 estimate grows like epsilon^(-1/5). The adaptive bound grows only logarithmically. Numerically:

- epsilon=1e-2: p_adapt=2.43429448, adaptive bound 9.4701 versus p=4 bound 19.7212.
- epsilon=1e-4: p_adapt=2.21714724, adaptive bound 10.9241 versus 49.5375.
- epsilon=1e-6: p_adapt=2.14476483, adaptive bound 12.1185 versus 124.4325.
- epsilon=1e-12: p_adapt=2.07238241, adaptive bound 14.7683 versus 1972.1219.

Thus the power-loss mechanism has been removed. What remains is only the endpoint logarithm associated with p downarrow 2.

### Structural correction extracted from the stress family

`QFORM-RANK2-ANISOTROPY-RATIO-BOUNDED-FALSE-v1`:

> The three-large-eigenvalue hypothesis does not imply a universal bound on `||Pn||^2/Delta` in a grouped rank-two physical cross packet, even when the packet's scale-invariant overlap currency V=Delta^2||Pn||^2 equals one identically.

This refutes only that intermediate structural shortcut, not QFORM.

## 7. Designated fleet04/B09 partner applied at an actual inequality

Use the six-coordinate target-valid matrix

`A_partner = [[0,K],[K,0]]`, `K=diag(2,1,1)`.                     (7.1)

Its spectrum is

`{-2,-1,-1,1,1,2}`,                                              (7.2)

so it satisfies the target hypothesis. The literal disjoint physical 3x3 cross block is K with det K=2. The completed fleet04/B09 theorem therefore gives

`boxed:
 ||p_Q||_infinity <= 3*2^(-1/3)
                  = 2.38110157795...`,                           (7.3)

and

`P{Q in I} <= 3*2^(-1/3)|I|`,                                   (7.4)

with a continuous density. This is a direct application of the partner's completed theorem, not an inferred extension.

## 8. What is and is not closed

This run closes the specific **power-loss** version of the r41 small-Delta problem: one no longer needs to pay Delta^{-1/5} at fixed overlap currency. The exact Lp family gives an adaptively chosen exponent and the universal logarithmic estimate (5.4).

It does **not** remove the final logarithm. The remaining same-target B09 endpoint is therefore sharper:

`QFORM-GROUPED-RANK2-ENDPOINT-LOG-REMOVAL-OR-PAID-ROUTING-v1`.

A successful next step must do one of the following without rotating the random variables into a dependent basis and without deleting the residual quadratic phase:

1. prove an endpoint Lorentz/dyadic replacement for Theorem 3.1 strong enough to pass p=2 with no logarithmic loss; or
2. exploit the target spectral structure to route the high-anisotropy regime R>>1 into an already-paid physical pivot, ridge, third-volume, or finite-core receiver.

The stress family in Section 6 proves that the second route cannot consist merely of bounding R by a universal number from the three-large-eigenvalue condition.

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**. Continuity is proved only for the branch of Theorem 4.1/Corollary 5.1 because the resulting characteristic function is L1.

## 9. Deterministic checks performed in this run

The accompanying checker verifies:

- the exact p=4 reduction to r41's constant;
- the p downarrow2 asymptotic constant 3sqrt(2);
- the explicit logarithmic constant used in (5.4);
- the adaptive numerical comparisons in Section 6;
- the exact target-valid eigenvalue formulas for the stress family;
- the fleet04/B09 partner numerical constant.

These finite checks support arithmetic and algebra only; they are not universal proof certificates.

## 10. Source pins and status

- Live correction inbox blob consumed: `47b2ff15d8ca6acfe35d9fd3de3b6281a86439f3`.
- r41 predecessor: `yspennstate/math-open-problems@39f45eeebf3d7a9609c4e26c14f2f8ad5b6b3fb1` at the path stated in Section 1.
- Designated fleet04/B09 partner: `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682` at the path stated in Section 1.
- Execution label: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not native learned-memory ingestion.
