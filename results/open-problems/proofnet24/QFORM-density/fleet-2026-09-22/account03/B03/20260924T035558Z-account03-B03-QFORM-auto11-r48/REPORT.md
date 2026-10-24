SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T03:55:58Z.
attacking: the two-sided nested-rank-two aligned-curvature survivor — use a balanced physical cut to promote a non-rank-two four-mode carrier Hessian to a literal E3 crossing, then turn the resulting one-copy density payment into the assigned whole-copy time estimate.

# account03/B03 r48 — balanced carrier E3 funnel for two-sided nested rank-two curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW STRUCTURAL/ANALYTIC FUNNEL / CONTINUOUS PAID BRANCH / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Full-target continuity remains OPEN. This report does not assume moments, compact or connected support, Gaussianity, log-concavity, iid laws, a diagonal eigenbasis, or independence after rotating the random vector. All rotations below are deterministic coefficient calculations only. No nonzero coefficient tail is deleted as a random perturbation.

Fresh inherited frontier: account03/B20 r45 (`yspennstate/math-open-problems@9340f6ef0ba72023989f2fbd3cf2ff3bb47a60c4`) reduces one strong-crossing survivor to a finite-hub / two-sided-nested-rank-two packet. Its aggregate promoted-E3 theorem already pays every substantial component transverse to the relevant rank-two carrier plane. Therefore the next exact model to understand is the genuinely **carrier-aligned** two-sided curvature packet. The newest account02/B03 aligned-curvature family (`yspennstate/math-open-problems@c9a27b38fff24b31ff9a53fc96abbf1770d5b42a`) shows that aligned same-bank curvature can itself become the missing third crossing direction after a physical repartition. The theorem below makes that mechanism quantitative for an arbitrary four-mode aligned carrier.

The analytic receiver used after the deterministic promotion is account03/B04 r42 (`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`): for any literal disjoint original-coordinate cross block `B`,

`||p_Q||_infinity <= C_E3 E3(B)^(-1/6)`,

`C_E3 = 8.45302122552817687470491804598...`,                     (0.1)

and the paid branch has a continuous `C_0` density. Arbitrary same-bank terms, outside couplings, signs, affine terms and extra spectrum remain present.

## 1. Exact aligned four-mode carrier

Let `R,C` be disjoint original-coordinate banks. Let

`U in R^(R x 2)`, `V in R^(C x 2)`, `U^T U=V^T V=I_2`.             (1.1)

Let `H,K` be real symmetric `2x2` matrices and let `S` be an invertible real `2x2` matrix. Consider the exact carrier-aligned coefficients

`A[R,R] = U H U^T`,
`A[R,C] = U S V^T`,
`A[C,C] = V K V^T`.                                                (1.2)

Outside these banks the full matrix may contain arbitrary coefficients; the theorem below uses only a literal cross block extracted from `R union C`, so every outside term is retained by the receiver (0.1).

Choose physical partitions

`R=R_0 disjoint_union R_1`, `C=C_0 disjoint_union C_1`,             (1.3)

and define the four `2x2` frame Grams

`G_Ra=U[Ra]^T U[Ra]`, `G_Ca=V[Ca]^T V[Ca]`, `a=0,1`.              (1.4)

Assume a balanced carrier cut at scale `g>0`:

`G_R0,G_R1,G_C0,G_C1 >= g I_2`.                                   (1.5)

Since complementary Grams add to `I_2`, necessarily `g<=1/2`.

Define the four-mode carrier Hessian

`M_car = [[H, S],
          [S^T, K]]`.                                              (1.6)

The literal physical cut is

`L=R_0 union C_0`, `J=R_1 union C_1`,
`B=A[L,J]`.                                                        (1.7)

### Theorem 1.1 — `QFORM-BALANCED-CARRIER-E3-PROMOTION-v1`

Under (1.1)-(1.7),

`boxed: E3(B) >= g^6 E3(M_car).`                                   (1.8)

Since the off-diagonal carrier `S` is invertible,

`boxed: E3(M_car) >= |det S|^2 s_3(M_car)^2,`                      (1.9)

where `s_3` denotes the third singular value. Hence

`boxed:
 E3(B) >= g^6 |det S|^2 s_3(M_car)^2.`                            (1.10)

Consequently, whenever `s_3(M_car)>0`, the **full ambient quadratic law** has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_E3 g^(-1) |det S|^(-1/3) s_3(M_car)^(-1/3).`                (1.11)

Every interval `I` therefore satisfies the genuine linear small-ball bound

`P(Q in I) <= C_E3 g^(-1)|det S|^(-1/3)s_3(M_car)^(-1/3)|I|.`      (1.12)

#### Proof

Because the four Grams in (1.5) are positive definite, define orthonormal restriction frames

`P_Ra = U[Ra] G_Ra^(-1/2)`,
`P_Ca = V[Ca] G_Ca^(-1/2)`.                                      (1.13)

Set

`P_L=diag(P_R0,P_C0)`, `P_J=diag(P_R1,P_C1)`,                      (1.14)

and

`D_L=diag(G_R0^(1/2),G_C0^(1/2))`,
`D_J=diag(G_R1^(1/2),G_C1^(1/2))`.                                (1.15)

Then `P_L,P_J` have orthonormal columns and the exact physical cross block factors as

`B = P_L D_L M_car D_J P_J^T`.                                    (1.16)

Thus its nonzero singular values are those of `D_L M_car D_J`. On third exterior powers,

`wedge^3(D_L M_car D_J)
 = (wedge^3 D_L)(wedge^3 M_car)(wedge^3 D_J)`.                    (1.17)

Every singular value of `D_L,D_J` is at least `sqrt(g)`, so every singular value of `wedge^3 D_L` and `wedge^3 D_J` is at least `g^(3/2)`. Hence the Frobenius norm obeys

`||wedge^3 B||_F
 >= g^3 ||wedge^3 M_car||_F`.                                     (1.18)

By Cauchy-Binet / compound-matrix notation,

`E3(T)=||wedge^3 T||_F^2`,                                        (1.19)

and squaring (1.18) proves (1.8).

For (1.9), `det S` is a literal `2x2` minor of `M_car`. Therefore

`s_1(M_car)s_2(M_car)=||wedge^2 M_car||_op >= |det S|`.            (1.20)

Since `E3(M_car)` is the sum of squared triple singular products, in particular

`E3(M_car)
 >= [s_1(M_car)s_2(M_car)s_3(M_car)]^2
 >= |det S|^2 s_3(M_car)^2`.                                      (1.21)

This proves (1.9)-(1.10). Apply the completed literal-cross E3 receiver (0.1) to the **actual** physical block `B`; substituting (1.10) gives (1.11). The same receiver provides `phi_Q in L1`, hence a continuous `C_0` density. QED.

## 2. Assigned whole-copy decoupled-time estimate

Put

`H_0 = C_E3 g^(-1)|det S|^(-1/3)s_3(M_car)^(-1/3)`.               (2.1)

Theorem 1.1 proves `||p_Q||_infinity<=H_0`. Let `Q'` be an independent copy of the **whole scalar output**. Then `Q-Q'` has density cap at most `H_0`. For any scalar density cap `H`, the standard layer-cake estimate gives

`E|Y|^(-1/2) <= 2 sqrt(2H)`.                                      (2.2)

Using only the whole-copy identity

`|phi_Q(t)|^2 = E exp(it(Q-Q'))`                                  (2.3)

and the positive half-Riesz Fourier identity

`int_R exp(itx)|t|^(-1/2)dt = sqrt(2pi)|x|^(-1/2)`,               (2.4)

we obtain

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= 4 sqrt(pi C_E3)
    g^(-1/2)|det S|^(-1/6)s_3(M_car)^(-1/6).`                     (2.5)

No coordinatewise `X-X'` is separated from its conjugate `X+X'`; (2.3) is used only for the entire output. Linear one-copy small-ball scaling was proved first in (1.12), so (2.5) is a consequence rather than an invalid attempt to infer `L^infinity` from collision energy.

## 3. Robust deterministic version — no coefficient tail is discarded

The exact carrier calculation has a useful perturbative formulation at the **coefficient** level. This is not a random perturbation argument.

Suppose the literal physical cross block has the decomposition

`B = P_L D_L M_car D_J P_J^T + E`,                                (3.1)

with the same balanced frames as above and an arbitrary deterministic error matrix satisfying

`||E||_op <= epsilon`.                                             (3.2)

Weyl's singular-value inequality and (1.5) imply, for `j=1,2,3`,

`boxed:
 s_j(B) >= [g s_j(M_car)-epsilon]_+.`                             (3.3)

Therefore

`boxed:
 E3(B) >= product_(j=1)^3 [g s_j(M_car)-epsilon]_+^2.`            (3.4)

In particular, if a live near-carrier packet provides lower bounds

`s_2(S)>=kappa`, `s_3(M_car)>=delta`,                              (3.5)

then `s_1(M_car),s_2(M_car)>=kappa` because `S` is a compression of `M_car`; hence, whenever `epsilon<g min(kappa,delta)`,

`boxed:
 E3(B) >= (g kappa-epsilon)^4 (g delta-epsilon)^2.`               (3.6)

Equations (3.3)-(3.6) keep the complete actual block `B`. They do not set `E=0` in the probability law. The only use of smallness is the deterministic singular-value inequality for the **actual coefficient matrix**, after which the receiver is applied to that actual block.

This is directly compatible with the current correction forbidding deletion of a small nonzero random quadratic tail.

## 4. Exact residue when the carrier does not produce E3

Theorem 1.1 identifies the algebraic endpoint exactly.

### Proposition 4.1 — `QFORM-CARRIER-RANK2-SCHUR-RIGIDITY-v1`

Assume `S` is invertible. Then

`rank M_car <=2`                                                   (4.1)

if and only if `H` and `K` are invertible and

`boxed: K = S^T H^(-1) S`                                        (4.2)

(equivalently `H=S K^(-1)S^T`). In that case `rank M_car=2` exactly and

`M_car
 = [[I],[S^T H^(-1)]] H [[I, H^(-1)S]].`                         (4.3)

#### Proof

Because the `2x2` block `S` is invertible, `rank M_car>=2`. If `rank M_car=2`, the first two block-columns `[H;S^T]` are independent, so the last two block-columns `[S;K]` are their linear combinations: there is a `2x2` matrix `T` with

`[S;K]=[H;S^T]T`.                                                  (4.4)

The top equation is `S=HT`. Since `S` is invertible, both `H` and `T` are invertible and `T=H^(-1)S`. The bottom equation then gives (4.2). Conversely (4.2) gives factorization (4.3), hence rank two. QED.

Thus an exact aligned two-sided carrier has the exhaustive deterministic fork:

1. `s_3(M_car)>0`: a balanced physical cut promotes the carrier to literal E3 and the complete ambient law is paid continuously by (1.11); or
2. `s_3(M_car)=0`: the entire four-mode carrier Hessian is exactly rank two and satisfies the rigid Schur relation (4.2).

Quantitatively, because `s_1(M_car)s_2(M_car)>=|det S|`,

`boxed:
 dist_op(M_car, rank<=2)=s_3(M_car)
 <= E3(M_car)^(1/2)/|det S|.`                                     (4.5)

So failure of the E3 payment funnels the aligned packet to a genuinely near-rank-two **four-mode carrier**, rather than leaving arbitrary same-bank curvature.

## 5. Concrete application: the newest aligned-curvature family

Apply Theorem 1.1 to the exact target-valid account02/B03 family at

`yspennstate/math-open-problems@c9a27b38fff24b31ff9a53fc96abbf1770d5b42a`.

For its balanced halves,

`G_R0=G_R1=G_C0=G_C1=(1/2)I_2`, so `g=1/2`.                       (5.1)

Its carrier matrices are

`H=K=diag(1,0)`, `S=I_2`.                                        (5.2)

Hence

`M_car=[[H,I],[I,H]]`                                             (5.3)

has eigenvalues

`{-1,0,1,2}`,                                                     (5.4)

so singular values `{2,1,1,0}` and

`E3(M_car)=4`.                                                     (5.5)

The exact balanced physical cut therefore has

`E3(B) = (1/2)^6 * 4 = 1/16`,                                    (5.6)

and the marginal-free E3 receiver gives the full ambient law

`boxed:
 ||p_Q||_infinity
 <= C_E3 * 16^(1/6)
 = 13.418334785712947... .`                                       (5.7)

The density is continuous and vanishes at infinity. The assigned whole-copy estimate is

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= 4 sqrt(pi * 13.418334785712947...)
 =25.970734910265183... .`                                        (5.8)

This is a hub-free payment of the same aligned-curvature witness: the two same-bank rank-one terms and the rank-two main crossing already manufacture the third crossing direction after the balanced product-preserving repartition. The hub may remain outside the cut with all its couplings untouched.

The point is not the small constant improvement over that report's hub-including cut; the structural gain is the exact criterion `s_3(M_car)>0` and the rank-two Schur rigidity (4.2) when it fails.

## 6. Designated partner account04/B03 applied at equation level

The latest completed designated partner theorem read this run is account04/B03 r3,

`yspennstate/math-open-problems@19345adf8bb78f11da95a556d6fdcc47af957b19`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T021651Z-account04-B03-hyperbola-fourvolume-r3/REPORT.md`.

On its literal zero-diagonal hyperbolic-pair/four-coordinate determinant branch it proves

`||p_Q||_(infinity,ess) <= 8 Delta^(-1/4)`.                        (6.1)

Apply the same whole-copy layer-cake step used in Section 2 to this actual inequality. Since the difference law has the same density cap,

`E|Q-Q'|^(-1/2) <= 8 Delta^(-1/8)`,                               (6.2)

and therefore

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= 8 sqrt(2pi) Delta^(-1/8).`                                    (6.3)

For the partner's concrete `Delta=1` control block, (6.3) is

`<=20.053026197048002...`.                                        (6.4)

This is an actual quantitative application of the designated partner result to the B03 objective. No dependent sum/difference pair is treated as independent.

## 7. What changed and what remains

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

New substantive implication proved here:

> In a two-sided exact carrier-aligned rank-two packet, once both physical banks admit a quantitatively balanced split in the carrier frames, arbitrary aligned same-bank curvature is no longer an analytic obstruction unless the combined four-mode carrier Hessian is itself rank two (or quantitatively near rank two). If it has a third singular direction, a literal physical cut has target-scale E3 and the full law is paid continuously.

This directly complements account03/B20 r45: r45 removes aggregate curvature transverse to the carrier plane; the present theorem removes carrier-aligned curvature whose **combined** four-mode matrix is not rank two. The surviving exact algebra is the rigid relation `K=S^T H^(-1)S`.

The first remaining implication on this route is therefore sharper:

`QFORM-BALANCED-CARRIER-RANK2-RESIDUE-PAYMENT-v1`:

1. produce a balanced physical carrier split (or route its failure to the finite heavy-hub alternatives already isolated by B20/B02); and
2. pay the near-rank-two four-mode Schur-rigid residue while retaining the actual nonzero carrier/tail errors, outside couplings, and product provenance.

No scheduler state, notification state, permission, public-release state, paid model/API action, installation, or cross-account authentication is changed by this report.