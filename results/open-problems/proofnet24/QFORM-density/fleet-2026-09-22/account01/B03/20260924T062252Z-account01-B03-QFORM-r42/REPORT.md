SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T06:22:52Z.
attacking: a critical two-hub plus conditional whole-copy collision compiler — keep the residual inside its true independent-copy weighted time budget and recover an L1 characteristic function without any pointwise quadratic-phase decay.

# account01/B03 r42 — conditional collision budget closes the critical two-hub endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: decoupled time integral  
Status: **NEW SUPPORTING COMPILER / DESIGNATED-PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **proved for the scoped compiler below; unrestricted continuity remains OPEN.**

## 0. Scope and correction boundary

The owner target is unchanged: independent original-coordinate inputs with scalar probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, or post-rotation independence is used.

The live correction against law-uniform pointwise quadratic van der Corput is preserved. The argument below uses no such pointwise decay. It also never splits a conjugate pair `(X-X',X+X')` and then conditionally recaps one member. Its new currency is an **already averaged whole-copy collision budget**.

The full conjecture remains open. The theorem below is a gluing result for a product-preserving decomposition; extracting such a decomposition from the bare three-eigenvalue hypothesis is still structural work.

## 1. Setup: the critical two-hub packet

Split ORIGINAL independent coordinates into

- two physical hubs `H=(H_1,H_2)`;
- a source-disjoint product bank `Y`;
- a source-disjoint product bank `W`.

Let

`S(Y)=B Y+d in R^2`,                                               (1.1)

where `B` has row rank two, and put

`P=||p_S||_2`.                                                     (1.2)

Allow an arbitrary symmetric hub self-block `C`, and let `R(Y)` be arbitrary measurable. The critical packet is

`H^T C H +2 H^T S(Y)+R(Y)`.                                      (1.3)

For each frequency `t`, push the complex measure

`exp(i t R(Y)) dP_Y`

through `S`. Its density `a_t(s)` satisfies

`|a_t(s)|<=p_S(s)`, hence `||a_t||_2<=P`.                         (1.4)

With Fourier convention `hat a(xi)=int exp(i xi dot s)a(s)ds`, two-dimensional Plancherel and the cap-one joint hub density give

`int |hat a_t(2t h)|^2 dP_H(h)
 <= int_R2 |hat a_t(2t h)|^2 dh
 = pi^2 |t|^-2 ||a_t||_2^2
 <= pi^2 P^2 |t|^-2.`                                             (1.5)

This is exactly the critical `|t|^-1` two-hub gain. By itself it is not integrable.

## 2. New theorem: hub-conditional whole-copy collision compiler

Let `Z=Z(H,W)` be a real residual. It may depend arbitrarily on the hub value, but its randomness after fixing `H=h` comes only from the source-disjoint bank `W`. Define

`psi_h(t)=E_W exp(i t Z(h,W))`,                                   (2.1)

`G(t)^2=E_H |psi_H(t)|^2`.                                       (2.2)

Assume the conditional whole-copy weighted collision budget

`K := int_R |t|^-1/2 G(t)^2 dt < infinity`.                       (2.3)

Consider

`Q=H^T C H+2H^T S(Y)+R(Y)+Z(H,W)`.                               (2.4)

### Theorem 2.1 — `QFORM-TWO-HUB-CONDITIONAL-COLLISION-L1-v1`

Under (1.1)-(2.4), `phi_Q in L1(R)`. Consequently `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= (5/pi) [pi P sqrt(K)/4]^(4/5).`                               (2.5)

Every interval `I` therefore satisfies the linear small-ball estimate

`P(Q in I) <= (5/pi)[pi P sqrt(K)/4]^(4/5) |I|`.                 (2.6)

### Proof

Condition on the hubs. Since `Y` and `W` are source-disjoint, the leaf packet and residual factor conditionally. Inserting the residual multiplier into Cauchy-Schwarz over the ORIGINAL hub law and using (1.5) gives

`|phi_Q(t)|
 <= pi P |t|^-1 G(t)`, `t!=0`.                                   (2.7)

For `T>0`, use Cauchy-Schwarz only after the weighted collision budget has been formed:

`int_(|t|>T) |t|^-1 G(t) dt
 =int_(|t|>T)|t|^-3/4 [|t|^-1/4 G(t)]dt`

`<= [int_(|t|>T)|t|^-3/2 dt]^(1/2)
    [int_R |t|^-1/2 G(t)^2dt]^(1/2)`

`=2 K^(1/2) T^-1/4.`                                              (2.8)

Together with `|phi_Q(t)|<=1` on low frequency,

`int_R |phi_Q(t)|dt
 <=2T+2 pi P K^(1/2) T^-1/4.`                                    (2.9)

The minimizer is

`T_*=[pi P sqrt(K)/4]^(4/5).`                                    (2.10)

At the minimizer the tail term equals `8T_*`, so

`int |phi_Q| <=10T_*`.                                            (2.11)

Fourier inversion gives (2.5), and `phi_Q in L1` gives continuity and vanishing at infinity. QED.

### Dependence-safe meaning of K

For each fixed `h`, let `W'` be an independent copy of the **whole W-bank**, with the same fixed hub value. Then

`|psi_h(t)|^2
 =E_(W,W') exp{i t[Z(h,W)-Z(h,W')]}.`                        (2.12)

Thus (2.3) is genuinely an independent-copy time integral. No coordinatewise difference is ever declared independent of its conjugate sum. When the positive half-Riesz identity is applicable, `K` is exactly the averaged half-Riesz potential of these conditional whole-output differences.

## 3. Dual theorem: bank-conditional collision is equally free

The same constant survives when the residual depends on the slope-bank value instead of the hub value.

Let `Z=Z(Y,W)` and define

`psi_y(t)=E_W exp(i t Z(y,W))`.                                   (3.1)

Assume the uniform conditional collision budget

`ess sup_y int_R |t|^-1/2 |psi_y(t)|^2 dt <=K`.                  (3.2)

Put

`Q=H^T C H+2H^T S(Y)+R(Y)+Z(Y,W)`.                               (3.3)

### Theorem 3.1 — `QFORM-TWO-HUB-BANK-CONDITIONAL-COLLISION-L1-v1`

The same conclusion (2.5)-(2.6) holds, with the same `P,K`, and the density is continuous `C_0`.

### Proof

Push the complex measure

`exp(i t R(Y)) psi_Y(t)dP_Y`

through `S`. Its density is

`a_t(s)=p_S(s) E[exp(i tR(Y))psi_Y(t)|S=s]`.                      (3.4)

Jensen gives

`||a_t||_2^2
 <=E[p_S(S(Y)) |psi_Y(t)|^2].`                                   (3.5)

Integrate with weight `|t|^-1/2` and use (3.2):

`int |t|^-1/2 ||a_t||_2^2 dt
 <=K E[p_S(S(Y))]
 =K int p_S(s)^2 ds
 =K P^2.`                                                         (3.6)

The hub Plancherel step now gives

`|phi_Q(t)|<=pi |t|^-1 ||a_t||_2`.                               (3.7)

Cauchy-Schwarz on the high-frequency tail with (3.6) yields exactly

`int_(|t|>T)|phi_Q(t)|dt
 <=2 pi P sqrt(K) T^-1/4`,                                       (3.8)

and the optimization is identical to Section 2. QED.

This theorem is important structurally: a residual W-bank may have arbitrary affine coefficients depending on the slope bank Y. In a quadratic form, that means **all Y-W bilinear couplings are allowed**. They become affine terms in W after conditioning on Y and cost nothing provided the W-quadratic packet has the uniform collision budget.

There is a symmetric hub-conditional version allowing arbitrary H-W bilinear couplings when the W residual is source-disjoint from Y. What is not covered is the genuinely mixed case in which the same residual W-bank couples simultaneously to both H and Y; then the multiplier depends on both sides of the critical Fourier transform.

## 4. Designated account02/B03 result applied at the actual inequality

The newest completed designated-partner theorem is account02/B03

`QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`,

canonical mathematics

`yspennstate/math-open-problems@5e5366b98337d13ba24bf666f4e42155553de7c2`.

For a symmetric coefficient matrix `A_W` on the source-disjoint W-bank, define its disjoint third exterior mass `E_0(A_W)` as in that report. It proves the whole-output collision estimate

`boxed:
 int_R |t|^-1/2 |phi_Z(t)|^2dt
 <=K_0 E_0(A_W)^(-1/12),`

`K_0=29.1511643034760...`,                                       (4.1)

whenever `E_0(A_W)>0`. The physical-E3 receiver behind (4.1) retains arbitrary affine terms and outside couplings; hence after conditioning on one side, (4.1) is uniform in the resulting affine coefficients.

Therefore Theorem 3.1 applies to the actual quadratic decomposition

`Q=H^T C H+2H^T(BY+d)+R(Y)`

`  + W^T A_W W +2 W^T(LY+e)+c`,                                 (4.2)

where the three original groups `H,Y,W` are source-disjoint, `rank(B)=2`, and **the Y-W coupling matrix L is arbitrary**. The only excluded cross block in this orientation is H-W.

Let

`D=det(BB^T)>0`.                                                   (4.3)

The completed two-dimensional product-projection estimate gives

`P=||p_(BY+d)||_2 <=sqrt(2) D^-1/4.`                             (4.4)

Insert (4.1) and (4.4) into (2.5):

`boxed:
 ||p_Q||_infinity
 <= C_mix D^-1/5 E_0(A_W)^-1/30,`                                (4.5)

where

`C_mix
 =(5/pi)[(pi/4)sqrt(2)sqrt(K_0)]^(4/5)
 =6.670623008323879... .`                                        (4.6)

The density is continuous and vanishes at infinity. In particular

`P(Q in I)<=6.670624 D^-1/5 E_0(A_W)^-1/30 |I|`                 (4.7)

for every interval `I`.

The scale check is exact: `D` has coefficient degree four and `E_0` degree six, so

`D^-1/5 E_0^-1/30`

has total degree `-4/5-1/5=-1`, exactly the density scaling required under `A -> sA`.

This is the required designated-partner theorem used at an actual inequality, not only cited as background.

### Symmetric orientation

Theorem 2.1 gives the same bound when the W-bank couples arbitrarily to H but has no coupling to Y: after conditioning on `H=h`, the W quadratic coefficient remains `A_W` and account02/B03's collision bound is uniform in the h-dependent affine term.

Thus **one-sided leakage of the partner-paid residual is free at the decoupled-time level**. Only simultaneous coupling of that same residual bank to both sides of the two-hub Fourier packet remains outside this compiler.

## 5. Useful density-to-collision corollary

If, more generally, each conditional residual `Z_u` has a density bounded by the same number `M`, then its whole-copy difference has density cap at most `M`, and the standard bathtub plus positive half-Riesz identity gives

`int |t|^-1/2 |phi_(Z_u)(t)|^2dt <=4 sqrt(pi M).`                 (5.1)

Hence the compiler yields the clean estimate

`boxed:
 ||p_Q||_infinity
 <=5*2^(-4/5) P^(4/5) M^(1/5)
 =2.87174588749... P^(4/5) M^(1/5).`                             (5.2)

This is a posterior use of an actual one-copy density payment to furnish the collision currency. It does not reverse a collision estimate into an L-infinity claim.

## 6. Exact stress family and scale cancellation

Take two physical hubs and two physical slope variables with

`B=k I_2`, `k>=1`, so `D=k^4`.                                   (6.1)

On six additional source-disjoint W coordinates take

`A_W=c [[0,I_3],[I_3,0]]`.                                       (6.2)

Its nonzero spectrum is three copies each of `+c,-c`. A direct 3-subset enumeration gives

`E_0(A_W)=8 c^6`.                                                  (6.3)

The full matrix already has four eigenvalues `+/-k` from the two hub-slope crossings, so it is owner-target-valid for `k>=1`, regardless of the small residual. Let

`c=k^-4`.                                                         (6.4)

Then (4.5) gives the **k-independent** bound

`||p_Q||_infinity
 <=C_mix * k^-4/5 * (8 k^-24)^-1/30
 =C_mix 8^-1/30
 =6.223911340870686... .`                                        (6.5)

Arbitrary Y-W bilinear couplings may be inserted without changing this analytic constant, provided the final matrix remains in the target when that concrete perturbation is considered. Equation (6.5) is only a stress test of the compiler's exact scaling; it is not used as evidence for the unrestricted conjecture.

## 7. Relation to previous fleet theorems

The earlier account01/B01 theorem glues a critical two-hub packet to a source-disjoint residual with an `L^2` **density** norm. Account03/B01 later allows one-sided hub- or bank-dependent residuals with a uniform conditional `L^r` density budget. The present theorem uses a different currency:

`int |t|^-1/2 |conditional characteristic function|^2 dt`.

That distinction matters because B03's exterior/crossing machinery naturally outputs exactly this whole-copy weighted collision integral. No intermediate density norm or pointwise oscillatory envelope has to be manufactured.

A repository search found the preceding weighted-frequency/L2-residual and conditional-Lr compilers, but no prior source-matching theorem with the collision hypothesis (2.3)/(3.2) and bound (2.5). This report therefore records the collision formulation explicitly rather than relabeling the older result.

## 8. What remains

This does not solve full QFORM. The new theorem removes one analytic interface:

`critical rank-two hub-slope packet + source-disjoint B03-paid collision residual`

now gives a continuous bounded density even when the residual has arbitrary bilinear leakage into **one** side of the packet.

The first analytic interface not covered by this argument is the both-sides-entangled residual: the same W variables enter both the hub slopes and the Y-dependent residual coefficients. There the multiplier depends simultaneously on the Fourier variable `h` and the slope-bank variable `y`, so neither Section 2 nor Section 3's Plancherel placement applies directly.

At the full-target level, the larger structural debt also remains: the bare condition `s_3(A)>=1` must still be routed product-preservingly into one of the already-paid disjoint-E3, overlap-two pair, finite-hub, grouped-carrier, or new collision-gluing exits without demanding one uniformly large individual minor.

Full QFORM: **OPEN**.  
Unrestricted continuity: **OPEN**.
