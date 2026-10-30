SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T06:26:39Z.
attacking: convert transverse distance from a strong physical hub to the top-two carrier plane of an actual rank-two crossing into a one-hub Fourier-L1 resource, then sharpen the global spectral-window hub scale and splice the two results into the live near-rank-two packet.

# fleet03/B02 r48 — top-two carrier-angle Fourier theorem and 1/18 spectral-window funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING FOURIER THEOREM + STRONGER TARGET-RELEVANT FUNNEL / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, post-rotation independence, arbitrary-joint coarea, conditional-density cap, or deletion of a small nonzero quadratic term is used.

## 1. Source-pinned inputs actually used

### 1.1 One-hub projected-two-volume Fourier theorem

The completed theorem used analytically is `QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1`, present at

`yspennstate/math-open-problems@343750e0bd888523ca52f424f46de7a25d070930`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

For one literal original hub `Y`, disjoint original-coordinate banks `I,J`, arbitrary hub phase `F(Y)`, arbitrary same-bank quadratic curvature and outside affine terms, let `m=A[J,Y]` be the hub-to-`J` star and

`C=A[I,J](I-P_m)`, `Z2=e2(CC^T)`.

If `m!=0` and `Z2>0`, then the full ambient law has a continuous `C0` density with

`||p_Q||inf <= C_E2 (||m||^2 Z2)^(-1/6)`,                      (1.1)

`integral_R |phi_Q(t)|dt <= 2*pi*C_E2 (||m||^2 Z2)^(-1/6)`,     (1.2)

where

`C_E2=3*2^(7/6)*exp(1/3)=9.39913188784886...`.                  (1.3)

Retracing the same proof gives the safe global high-frequency envelope already source-pinned in B02 r38,

`|phi_Q(t)| <= min{1,K_h (||m||^2 Z2)^(-1/4)|t|^(-3/2)}`,       (1.4)

`K_h=2^(7/4)*pi^(3/2)*exp(1/2)=30.87980451778735...`.           (1.5)

No row-marginal gate remains in this theorem.

### 1.2 Same-slot parametric spectral window and live packet

The immediate same-slot predecessor is

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T045848Z-fleet03-B02-qform-r47/REPORT.md`.

Its proved parametric spectral-window theorem says: with

`P_eta=1_{|A|>=eta}`,
`delta=1/2-eps-sqrt(2eps)`,
`sigma=delta-eta`,                                                 (1.6)

if `max_i(P_eta)_ii<=eps`, `sigma>0`, and

`(sqrt(eps/delta)+sqrt(6)*eta/sigma)^2<1/2`,                     (1.7)

then the full law has a continuous `C0` density and

`||p_Q||inf <=9sqrt(3e)/(2sigma)`,                                (1.8)

`integral |phi_Q| <=9pi sqrt(3e)/sigma`.                          (1.9)

The same predecessor retains a literal full physical cut

`N=A[L,R]`, `L union R=[n]`,                                     (1.10)

whose squared singular values `x1>=x2>=...` satisfy

`x1*x2 > kappa0:=247/576`.                                       (1.11)

This run sharpens the global spectral-window constants and then attacks the strong off-diagonal hub branch of this exact packet.

### 1.3 Designated partner fleet04/B02

The completed designated partner result is

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

Whenever a nonsingular literal physical principal triple `H0` has one zero diagonal entry, it gives the full-law Fourier credit

`L:=integral_R |phi_Q(t)|^2dt
 <=6*pi*2^(2/3)|det H0|^(-1/3)`.                                 (1.12)

Section 6 combines (1.12) with the new carrier-angle high-frequency estimate at an actual inequality.

## 2. Exact top-two carrier-angle identity

Let `M` be any real `p x q` literal ORIGINAL-coordinate cross block with at least two nonzero singular values. Write an SVD

`M=U diag(sigma_1,sigma_2,...) V^T`,

`x_j=sigma_j^2`, `x1>=x2>0`.                                     (2.1)

Let `m in R^q`, `m!=0`, be a literal physical hub star to the `q`-coordinate bank, let `mhat=m/||m||`, and define

`P_m=I-mhat mhat^T`, `C=M P_m`, `Z2=e2(CC^T)`.                   (2.2)

Set

`z_j=<v_j,mhat>`,                                                 (2.3)

where `v_j` are the right singular vectors. Then:

### Lemma 2.1 — exact projected E2 formula

`boxed:
 Z2 = sum_(p<q) x_p x_q (1-z_p^2-z_q^2).
`                                                                  (2.4)

Every coefficient in (2.4) is nonnegative. In particular, if `V_2=span(v_1,v_2)`,

`boxed:
 ||m||^2 Z2 >= x1*x2*dist(m,V_2)^2.
}`                                                                  (2.5)

#### Proof

In the left singular basis,

`CC^T = D-aa^T`,
`D=diag(x_j)`, `a_j=sigma_j z_j`.                                 (2.6)

Use

`e2(H)=1/2[(tr H)^2-tr(H^2)]`.                                   (2.7)

Writing `S=sum_j x_j`, `A=sum_j x_j z_j^2`, `B=sum_j x_j^2 z_j^2`, direct expansion gives

`e2(D-aa^T)=e2(D)-S A+B`.                                        (2.8)

Regroup the right side pairwise:

`e2(D)-S A+B
 =sum_(p<q)x_p x_q(1-z_p^2-z_q^2)`.                              (2.9)

Because `sum_j z_j^2<=1`, each factor `1-z_p^2-z_q^2` is nonnegative. Keeping only `(p,q)=(1,2)` gives

`Z2>=x1x2(1-z1^2-z2^2)`.                                         (2.10)

Finally

`||m||^2(1-z1^2-z2^2)=dist(m,V_2)^2`,                            (2.11)

which proves (2.5). QED.

This is an exact rank-one downdate identity. It does not select any tiny physical minor and it is valid with arbitrary higher singular directions present.

## 3. New integrated-Fourier receiver

### Theorem 3.1 — `QFORM-ONEHUB-TOP2-CARRIER-ANGLE-L1-v1`

Let `Y`, `X_I`, `X_J` be disjoint ORIGINAL coordinates. Consider the full ambient quadratic form after conditioning every other original coordinate. Let

`M=A[I,J]`,
`m=A[J,Y]`,                                                       (3.1)

and let `x1,x2` and `V_2` be the top two squared singular values and right carrier plane of `M`. Put

`d=dist(m,V_2)`.                                                   (3.2)

If `x1*x2*d^2>0`, then the full, unconditioned quadratic law has a continuous `C0` density satisfying

`boxed:
 ||p_Q||inf <= C_E2 (x1*x2*d^2)^(-1/6),
}`                                                                  (3.3)

`boxed:
 integral_R |phi_Q(t)|dt
 <=2*pi*C_E2 (x1*x2*d^2)^(-1/6).
}`                                                                  (3.4)

Moreover

`boxed:
 |phi_Q(t)|
 <=min{1,K_h (x1*x2*d^2)^(-1/4)|t|^(-3/2)}.
}`                                                                  (3.5)

All hub self-curvature `A_YY`, the hub star to `I`, same-bank curvature on `I,J`, outside couplings, affine terms, signs, and extra spectrum are unrestricted.

#### Proof

Apply the exact identity (2.5) to `M` and the hub star `m`. It gives

`||m||^2 e2(M(I-P_m)M^T)
 >=x1*x2*d^2`.                                                     (3.6)

The left side is exactly the resource in the completed one-hub projected-E2 theorem (1.1)-(1.5). Substitution proves (3.3)-(3.5), uniformly in the conditioned outside coordinates. The source theorem already performs the outside averaging and proves the continuous `C0` representative. QED.

### Why this matters

A strong `l2` physical hub star need not contain a single large edge and one-heavy-edge absorption is refuted. The new theorem instead says that, in the presence of an actual rank-two crossing, **any fixed transverse distance of that whole star from the top-two carrier plane is already a genuine Fourier-L1 exit**. The only surviving star geometry is carrier alignment, not coordinatewise concentration.

## 4. A sharper global spectral window: eta=1/18

Use the already-proved parametric theorem (1.6)-(1.9) with

`eta=1/18`, `eps=2/153`.                                          (4.1)

Then

`delta=149/306-2/sqrt(153)`,
`sigma=delta-1/18`.                                                (4.2)

A fully rational certificate for (1.7) is as follows. Since

`309/25 < sqrt(153)`,                                              (4.3)

we have

`delta >149/306-50/309=10247/31518`,                              (4.4)

and hence

`sigma>10247/31518-1/18=472/1751`.                                (4.5)

Also

`eps/delta < 412/10247 < (201/1000)^2`,                           (4.6)

because `10247*40401=413989047>412000000`. Further, using `sqrt(6)<49/20`,

`sqrt(6)*eta/sigma
 <85799/169920 <101/200=505/1000`,                                (4.7)

where `17161920>17159800` certifies the last inequality. Therefore

`sqrt(eps/delta)+sqrt(6)*eta/sigma
 <706/1000`,                                                       (4.8)

and

`(706/1000)^2=0.498436<1/2`.                                     (4.9)

Thus:

### Corollary 4.1 — `QFORM-1OVER18-SPECTRAL-WINDOW-L1-v1`

If

`boxed: max_i(P_{1/18})_ii <=2/153,`                              (4.10)

then the full target law has a continuous `C0` density with

`boxed: ||p_Q||inf <47.651,`                                      (4.11)

`boxed: integral_R |phi_Q(t)|dt <299.398.`                        (4.12)

For a certificate using only the rational lower bound (4.5), the slightly weaker values are `<47.673` and `<299.533`.

If (4.10) fails, some ORIGINAL coordinate `i` has

`||Ae_i||^2>(1/18)^2*(2/153)=1/24786`.                            (4.13)

Since

`||Ae_i||^2=A_ii^2+||A[i,i^c]||^2`,                              (4.14)

and

`2/223^2=2/49729 <1/24786`                                       (4.15)

(the integer comparison is `49572<49729`), failure of the diffuse branch forces

`boxed:
 |A_ii|>1/223
 OR
 ||A[i,i^c]||>1/223.
}`                                                                  (4.16)

This improves the r47 physical-hub scale `1/228` while keeping a larger spectral cutoff `1/18`.

## 5. Splice the carrier-angle theorem into the live balanced near-rank-two packet

Work on the literal full cut `N=A[L,R]` from (1.10)-(1.11). Suppose the diffuse spectral-window branch (4.10) is not already paid and take a strong off-diagonal hub from (4.16):

`||A[i,i^c]||>a0`, `a0:=1/223`.                                  (5.1)

Assume `i in L`; the transpose case is identical. Let `U_2` be the top-two left singular frame of the FULL crossing `N`, and set

`ell_i=||U_2(i,:)||^2`.                                           (5.2)

If `ell_i>3/4`, retain the same near-coloop branch as before. Assume henceforth

`ell_i<=3/4`.                                                      (5.3)

Delete the hub row and form the actual punctured crossing

`M=N[L\{i},R]`.                                                    (5.4)

Let its top two squared singular values be `y1>=y2`, with carrier planes `U_M,V_M`. Write the two parts of the physical hub star as

`c=A[L\{i},i]`, `r=A[i,R]`.                                      (5.5)

### Lemma 5.1 — puncturing preserves a fixed rank-two product

`boxed:
 y1*y2 >= x1*x2(1-ell_i) > kappa0/4=247/2304.
}`                                                                  (5.6)

#### Proof

Write the full SVD as top-two plus tail. After deleting row `i`,

`M=M_2+M_tail`,
`M_2=U_2^{(-i)} diag(sqrt(x1),sqrt(x2)) V_2^T`.                    (5.7)

The right singular spaces of `M_2` and `M_tail` remain orthogonal, so

`MM^T=M_2M_2^T+M_tail M_tail^T >= M_2M_2^T`                       (5.8)

in Loewner order. The product of the two nonzero eigenvalues of `M_2M_2^T` is

`x1*x2*det((U_2^{(-i)})^T U_2^{(-i)})
 =x1*x2*det(I-U_2(i,:)^T U_2(i,:))
 =x1*x2(1-ell_i)`.                                                (5.9)

Eigenvalue monotonicity under (5.8) proves (5.6). QED.

This point is useful: **no small singular tail has been discarded**. The actual punctured block `M` is used, and the tail is positive semidefinite after multiplying by its transpose.

### Theorem 5.2 — parametric strong-hub carrier funnel

Fix any `0<theta<1/sqrt(2)` and put

`d_R=dist(r,V_M)`, `d_L=dist(c,U_M)`.                              (5.10)

Then one of the following holds:

1. `ell_i>3/4` (the finite near-coloop branch); or
2. the full law has a genuine Fourier-L1 exit with resource

   `R_theta=(247/2304)*theta^2*a0^2`,                              (5.11)

   and hence

   `||p_Q||inf <=C_E2 R_theta^(-1/6)`,
   `integral|phi_Q|<=2pi C_E2 R_theta^(-1/6)`;                    (5.12)

3. both physical stars are carrier aligned at scale `theta a0`,

   `d_R<theta a0`, `d_L<theta a0`,                                (5.13)

   and their combined carrier component obeys

   `boxed:
   [||P_(V_M)r||^2+||P_(U_M)c||^2]^(1/2)
   > a0 sqrt(1-2theta^2).
   }`                                                               (5.14)

#### Proof

Under (5.3), Lemma 5.1 gives `y1y2>247/2304`. If `d_R>=theta a0`, apply Theorem 3.1 with hub `X_i`, `I=L\{i}`, `J=R`, crossing `M`, and hub-to-`J` star `r`. If `d_L>=theta a0`, transpose the orientation and apply Theorem 3.1 to `M^T`, with hub-to-`L\{i}` star `c`. Either case gives (5.11)-(5.12).

If neither transverse exit occurs, orthogonal projection gives

`||P_(V_M)r||^2+||P_(U_M)c||^2
 =||r||^2+||c||^2-d_R^2-d_L^2
 >a0^2-2theta^2 a0^2`,                                           (5.15)

because `||r||^2+||c||^2=||A[i,i^c]||^2>a0^2`. This proves (5.14). QED.

### Concrete theta=1/4 scale

Take `theta=1/4`. Then

`R_(1/4)=247/1833209856
        =1.34736347391752e-7`.                                   (5.16)

Therefore every non-coloop strong off-diagonal hub either gives

`boxed: ||p_Q||inf <131.273,`                                    (5.17)

`boxed: integral |phi_Q| <824.810,`                               (5.18)

with a continuous `C0` density, or satisfies the stronger two-sided carrier alignment

`boxed:
 [||P_(V_M)r||^2+||P_(U_M)c||^2]^(1/2)
 >sqrt(7/8)/223
 =0.00419468316903... .
}`                                                                  (5.19)

The previous r47 aligned scale was `1/(228sqrt(2))=0.0031013...`; the new survivor is both geometrically sharper (alignment to the ACTUAL punctured carrier planes) and quantitatively larger.

### Updated unpaid list on this fork

After the diffuse `1/18` window and the carrier-angle Fourier exits, the live near-rank-two fork is reduced to:

1. the fixed overlap-one `V1` grouped-pivot packet inherited from earlier B02 work;
2. a physical diagonal `|A_ii|>1/223`;
3. a two-sided carrier-aligned strong hub satisfying (5.19);
4. the finite near-coloop branch `ell_i>3/4` (at most four coordinates across the two sides of the full cut).

No nonzero crossing tail was dropped in reaching this list.

## 6. Equation-level application of designated partner fleet04/B02

On the exact overlap with a nonsingular physical zero-diagonal triple `H0`, combine the partner's low-frequency credit (1.12) with the new one-hub carrier-angle high-frequency envelope (3.5).

Write

`R=x1*x2*d^2`,                                                     (6.1)

so

`|phi_Q(t)|<=K_h R^(-1/4)|t|^(-3/2)` at high frequency.           (6.2)

For every `T>0`, Cauchy-Schwarz on `|t|<=T` and direct integration outside give

`integral |phi_Q|
 <=sqrt(2LT)+4K_h R^(-1/4)T^(-1/2)`.                             (6.3)

Optimizing at `T=4K_h R^(-1/4)/sqrt(2L)` gives

`||p_Q||inf
 <=9.83947303316740
   |det H0|^(-1/12) R^(-1/8)`.                                   (6.4)

This is the designated fleet04/B02 theorem applied to the new carrier-angle resource, not a citation-only dependency.

At the concrete target-scale exit (5.16),

`boxed:
 ||p_Q||inf
 <71.086354595 |det H0|^(-1/12).
}`                                                                  (6.5)

Continuity on this overlap comes already from Theorem 3.1; it is not inferred from Fourier `L2` alone.

## 7. Deterministic verification

A seeded deterministic regression (`seed=20260924`) checked 2,000 dense rectangular matrices of dimensions 2 through 8 for the exact identity (2.4) and lower bound (2.5): zero violations, maximum relative identity error `5.6863e-14`, and minimum observed ratio `Z2/[x1*x2(1-z1^2-z2^2)] =0.999999999999754` on nonzero denominators.

A second seeded regression (`seed=2026092402`) checked 2,000 dense physical cuts for Lemma 5.1: zero violations; maximum relative error in the exact rank-two-core product formula (5.9) was `7.8031e-14`, and the minimum observed actual-puncture ratio `y1*y2/[x1*x2(1-ell_i)]` was `0.999999999999926`.

These computations are corroborative only. The proof is the trace identity, SVD rank-one downdate, Cauchy/interlacing-Loewner argument, and the already-completed one-hub Fourier theorem.

## 8. Scope, correction boundary, and next exact debt

The **full unrestricted QFORM conjecture remains OPEN**. Full-target continuity remains OPEN. A universal target-wide unweighted `integral|phi_Q|` bound remains **OPEN / not refuted**; no exact-target counterexample to that stronger criterion was found.

This run does not use law-uniform scalar pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea, a conditional projection-density cap, fiber-sup integration, one-good-minor forcing, coordinatewise heavy-edge extraction, or probabilistic deletion of a small coefficient tail. SVDs are coefficient algebra only. The one-hub theorem is applied only to literal original-coordinate product banks, and all full ambient quadratic terms permitted by its theorem are retained.

The next B02 edge is

`QFORM-CARRIERALIGNED-HUB-PLUS-R2-KERNELCURVATURE-L1-v1`:

on the survivor (5.19), combine the large two-sided carrier component with the physical diagonal / same-bank quadratic restriction to produce either (i) a nonzero kernel-curvature packet paid by the completed 3x2 theorem, (ii) a grouped-pivot `V1/V2` Fourier receiver, or (iii) a finite near-coloop core. The key remaining danger is exact Schur/kernel-curvature cancellation; it must be routed, not treated as a small perturbation.
