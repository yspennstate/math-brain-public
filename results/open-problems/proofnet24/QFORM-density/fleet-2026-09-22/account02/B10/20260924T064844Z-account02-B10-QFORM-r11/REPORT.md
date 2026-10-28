SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-24T06:48:44Z.
attacking: the exact-rank-three near-coloop two-sheet survivor via an endpoint-stable hyperbolic-Fresnel representation; determine whether the remaining hub/leaf absolute-value receiver can be uniform without losing original-coordinate product provenance.

# account02/B10 r11 — exact hyperbolic-Fresnel normal form and a logarithmic absolute-receiver obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case, complementary constructions/source-valid counterexamples  
Status: `NEW_EXACT_PHASE_REPRESENTATION / NEW_ROUTE_COUNTEREXAMPLE / RULED_SIDE_APPLIED / PARTNER_CURVATURE_CONSUMED / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`.

## 1. First unpaid implication and source boundary

The first unpaid implication is now

`QFORM-HYPERBOLIC-FRESNEL-PHASE-RECEIVER-v1`:

> For the diffuse exact-rank-three near-coloop survivor
> 
> `Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`, `0<rho<1/64`, `c=1-rho`,
> 
> with `(z,r,y)` an orthonormal coefficient frame on the ORIGINAL leaf coordinates and arbitrary independent cap-one source laws, prove a universal endpoint estimate while retaining the mixed hyperbolic phase before absolute values. Equivalently, in the exact representation proved below, control the `t`-integral of the oscillatory three-variable receiver uniformly in `rho`; the absolute three-frequency majorant is not allowed, because it is shown below to grow at least logarithmically on an admissible uniform source.


Required pinned source actually used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The completed ruled theorem there will be spent at an actual density inequality in Section 6, rather than reproved.

Current partner input consumed: account03/B10 r32, exact calculation

`yspennstate/math-open-problems@c97e404492dc02e28ee6c465c4328df3afe22d70`

with verifier output through `c1b9d3e30df05f6b27df2b0bc0431475448a0a57`. For

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`, `sigma_min(M)>=1`, `|alpha|<1`,

it proves

`(alpha^2+s^2-1)(d^2-1)>=(1-alpha^2)k^2`, hence `|d|>=1`.            (1.1)

The latest completed full partner report used for source geometry is account03/B10 r29,

`yspennstate/math-open-problems@fa694dbcc9a8e70293a5120263fabe67e5f1465b`,

which proves the endpoint-stable hard transverse square and nondegenerate hub pencil in the near-coloop collar. The construction below saturates the hard-square floor; its obstruction is therefore not weak transverse curvature.

## 2. The exact target-valid harmonic survivor

Fix `m=123`, put

`theta_j=2*pi*j/m`, `j=0,...,m-1`,

and define ORIGINAL leaf coefficient vectors

`z_j=sqrt(2/m) cos(2 theta_j)`,
`r_j=sqrt(2/m) cos(theta_j)`,
`y_j=sqrt(2/m) sin(theta_j)`.                                      (2.1)

Discrete Fourier orthogonality gives

`||z||_2=||r||_2=||y||_2=1`,
`z perp r`, `z perp y`, `r perp y`.                                (2.2)

For `0<rho<1/64`, let `c=1-rho` and take physical spectral rows

`u_0=sqrt(c)e_1`,
`u_j=sqrt(rho) z_j e_1+r_j e_2+y_j e_3`.                           (2.3)

Thus the `(m+1) x 3` matrix `R` with rows `u_i` has orthonormal columns. With

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (2.4)

`A=R M_0 R^T` has exactly the three nonzero eigenvalues `{1,-1,1}`. Moreover

`r_j^2+y_j^2=2/m=2/123<1/61`,                                      (2.5)

so this lies in the genuinely diffuse near-coloop chamber.

For arbitrary independent ORIGINAL inputs of density at most one, set

`H=X_0`, `Z=z.X_L`, `L=r.X_L`, `V=y.X_L`.

Then, exactly,

`boxed: Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2.`                             (2.6)

No independence is asserted among `Z,L,V`; they use the same leaf bank. Only the physical hub `H` is independent of the entire leaf vector.

In the partner's adapted core this family has

`alpha=0`, `s=1`, `b=k=0`, `d=1`.                                  (2.7)

Hence the partner inequality (1.1) is attained at its endpoint: the transverse square is already as hard as the spectral hypothesis can force, `|d|=1`, with no positive `d^2-1` surplus available to absorb source overlap.

## 3. Exact endpoint-stable hyperbolic-Fresnel representation

Write the characteristic functions of the hub and leaves as

`psi_H(u)=E exp(iuH)`, `psi_j(u)=E exp(iuX_j)`,

and put

`Phi(p,q,w)=E exp(i(pZ+qL+wV))
            =prod_j psi_j(p z_j+q r_j+w y_j)`.                     (3.1)

The product in (3.1) is in ORIGINAL coordinates; this is the only factorisation used.

For `t!=0`, the elementary oscillatory identities are

`exp(i 2 a t z l)
 =(4*pi*|a t|)^(-1) int_R2 exp(-i p q/(2 a t)) exp(i p z+i q l) dp dq`, (3.2)

with `a>0`, and

`exp(i t v^2)
 =omega_t (4*pi*|t|)^(-1/2) int_R exp(-i w^2/(4t)) exp(iwv) dw`,     (3.3)

where `|omega_t|=1`. Both formulas may be justified first with Gaussian damping and then by the standard oscillatory limit.

Apply (3.2) to `2 sqrt(rho) ZL` and (3.3) to `V^2`. For fixed hub value `h`, the remaining hub phase `exp(i2sqrt(c)t h L)` shifts the `q` argument of `Phi` by `2sqrt(c)t h`. Shift the integration variable back. The hyperbolic kernel then contributes

`exp(i p sqrt(c/rho) h)`,

so averaging the ORIGINAL hub produces `psi_H(p sqrt(c/rho))`. Finally set `p=sqrt(rho) xi`. The apparent `rho^(-1/2)` Jacobian cancels exactly.

### Theorem 3.1 — `QFORM-ENDPOINT-STABLE-HYPERBOLIC-FRESNEL-REPRESENTATION-v1`

For every `t!=0`, in the Gaussian-regularised oscillatory sense,

`boxed:
 phi_Q(t)
 =omega_t/(8*pi^(3/2)*|t|^(3/2))
  int_R3 exp(-i xi q/(2t)) exp(-i w^2/(4t))
          psi_H(sqrt(c) xi)
          Phi(sqrt(rho) xi,q,w)
  dxi dq dw,`                                                       (3.4)

with `|omega_t|=1`.

The crucial feature is that the prefactor in (3.4) has **no power of `rho`**. The longitudinal leakage appears only as the shear `sqrt(rho) xi` inside the genuine leaf product transform. Thus the near-null geometry itself admits an endpoint-stable phase representation.

This formula also identifies the exact coefficient frame in frequency space: the hub contributes the row `(sqrt(c),0,0)` and leaf `j` contributes `(sqrt(rho)z_j,r_j,y_j)`. These rows form a Parseval three-frame. The hub row has leverage `c>63/64`, while all transverse leaf rows are diffuse. Therefore a direct one-shot Theorem-F/Brascamp-Lieb use is outside its `L^p`, `p>=2`, gate on the hub row; this is the same near-coloop difficulty seen from the exact transform rather than from a rotated probabilistic coordinate.

## 4. The natural absolute three-frequency receiver is not uniform

If one takes absolute values inside (3.4), the resulting quantity is

`J_rho
 :=int_R3 |psi_H(sqrt(c) xi)| |Phi(sqrt(rho)xi,q,w)| dxi dq dw`.    (4.1)

Whenever `J_rho<infinity`, (3.4) gives the formal large-frequency majorant

`|phi_Q(t)| <= J_rho/(8*pi^(3/2)|t|^(3/2))`.                        (4.2)

The next theorem shows that no universal bound on (4.1) is possible, even in the fixed target-valid harmonic family and with the simplest cap-one laws.

Take **every** ORIGINAL input, hub and leaves, uniform on `[-1/2,1/2]`. Then

`psi_0(u)=sin(u/2)/(u/2)`.                                         (4.3)

Let

`a_0:=sin(1/16)/(1/16)>0.999`.                                     (4.4)

Consider the box

`|q|<=1/8`, `|w|<=1/8`, `|xi|<=1/(4 sqrt(rho))`.                   (4.5)

For every leaf index, using `|z_j|,|r_j|,|y_j|<=sqrt(2/m)`,

`|sqrt(rho) z_j xi+r_j q+y_j w|
 <=sqrt(2/m)(1/4+1/8+1/8)
 =sqrt(2/m)/2
 <1/8`                                                             (4.6)

because `m=123`. Hence throughout (4.5),

`|Phi(sqrt(rho)xi,q,w)|>=a_0^m=a_0^123>0.923`.                     (4.7)

The `(q,w)` box has area `1/16`, so

`J_rho
 >=a_0^123/16 * int_{|xi|<=1/(4sqrt(rho))}
                  |psi_0(sqrt(c)xi)| dxi`.                         (4.8)

Put `T=sqrt(c)/(8sqrt(rho))`. By the change of variables `x=sqrt(c)xi/2`,

`int_{|xi|<=1/(4sqrt(rho))}|psi_0(sqrt(c)xi)| dxi
 =(4/sqrt(c)) int_0^T |sin x|/x dx`.                               (4.9)

On every interval

`[k*pi+pi/6, k*pi+5pi/6]`,

`|sin x|>=1/2`; comparing `x` there with `(k+1)pi` gives a lower contribution at least `1/[3(k+1)]`. Summing these disjoint intervals up to `T` yields

`int_0^T |sin x|/x dx >= (1/3) log T-O(1)`.                         (4.10)

Since `T` is a fixed positive multiple of `rho^(-1/2)`, (4.8)-(4.10) give

`boxed: J_rho >= C_0 log(1/rho)-C_1 -> infinity as rho downarrow 0`, (4.11)

for absolute constants `C_0>0,C_1` (already with fixed dimension `124`).

### Theorem 4.1 — `QFORM-HYPERBOLIC-FRESNEL-HUB-L1-BARRIER-v1`

The endpoint-stable representation (3.4) cannot be closed uniformly by taking the full three-frequency absolute value `J_rho`. In fact an admissible compactly supported cap-one product source forces its absolute majorant to grow at least logarithmically as the physical leakage `rho` tends to zero.

This is a counterexample to that **proof interface**, not to QFORM. It is stronger than merely observing that `psi_H` may fail to be `L^1`: the leaf product transform does regularise the hub frequency for every fixed positive leakage, but the amount of regularisation disappears logarithmically at the endpoint.

## 5. What the obstruction says about the remaining receiver

The failure in Section 4 is exactly what the current geometry predicts. If one first fixes `xi` and applies a two-dimensional product-marginal/Brascamp-Lieb bound in `(q,w)`, the bound is translation-uniform in the leaf arguments but leaves an `int |psi_H(sqrt(c)xi)| dxi` payment. Uniform `[-1/2,1/2]` already makes that payment divergent. Keeping the small `sqrt(rho)z_j xi` shear regularises it only at scale `|xi|~rho^(-1/2)`, generating the logarithm (4.11).

Therefore a valid endpoint proof cannot perform either of the following operations before the final integration:

1. freeze `xi`, pay the `(q,w)` product transform absolutely, and then integrate `|psi_H|`; or
2. take the full absolute value in (3.4) and hope for an endpoint-stable geometric Brascamp-Lieb constant.

At least the mixed phase

`exp(-i xi q/(2t))`                                                  (5.1)

must remain coupled to the hub and leaf transforms until after the `xi,q` integration, or one needs a different real-space cancellation carrying the same information. This is the phase-sensitive content missing from the previous clean-square and exact-regression interfaces.

A concrete sufficient next lemma is now explicit. Define

`K_rho(t)
 :=int_R3 exp(-i xi q/(2t)) exp(-i w^2/(4t))
             psi_H(sqrt(c)xi) Phi(sqrt(rho)xi,q,w)
             dxi dq dw`.                                           (5.2)

Since `|phi_Q(t)|=|K_rho(t)|/(8*pi^(3/2)|t|^(3/2))`, a bound

`boxed:
 sup_{0<rho<1/64}
 int_1^infinity t^(-3/2)|K_rho(t)| dt < infinity`                   (5.3)

for arbitrary cap-one ORIGINAL product laws and the live diffuse coefficient geometry would close the high-frequency Fourier part of the harmonic survivor. The low-frequency interval is free from `|phi|<=1`. Crucially, (4.11) proves that (5.3) cannot follow by replacing `|K_rho(t)|` with `J_rho`.

## 6. Required ruled-side theorem spent at an actual inequality

The pinned `COUNTEREXAMPLE_SEARCH.md` proves the ruled level-set theorem for signature `(2,1)`: if the three spectral eigenvalue moduli are at least one, then on the majority-sign one-sheet side

`p_Q(s)<=pi sqrt(2)`.                                                (6.1)

The matrix (2.4) has positive-positive-negative signature after ordering and exact moduli one. Hence, for the **same family** on which the absolute hyperbolic-Fresnel receiver fails,

`boxed: p_Q(s)<=pi sqrt(2)<4.443 for every s>=0.`                   (6.2)

No step of the source theorem is reproved. Its proof uses line integrals of genuine product-measure marginals and does not assert independence after spectral projection.

Thus the logarithmic failure of `J_rho` is demonstrably a proof-interface loss: half of the level set is already uniformly paid by an independent completed theorem. The unresolved target content for this family is the genuine two-sheet side `s<0`.

## 7. Partner result applied at the obstruction

Account03/B10 r32 proves the hard-square inequality (1.1). For the present harmonic core (2.7),

`alpha^2+s^2-1=0`, `k=0`, `d=1`,                                  (7.1)

so (1.1) is attained with equality. Consequently there is no latent gain from strengthening the transverse curvature coefficient: the exact spectral floor `|d|=1` is already present while the absolute receiver still loses `log(1/rho)`.

Account03/B10 r29 also proves that the near-coloop hub pencil and a disjoint star/transverse certificate stay uniformly nondegenerate. The present computation shows why that deterministic nondegeneracy still does not license an absolute frequency split: the obstruction is source-provenance/phase coupling rather than a collapsing matrix coefficient.

## 8. Status and next step

New proved supporting lemma: `QFORM-ENDPOINT-STABLE-HYPERBOLIC-FRESNEL-REPRESENTATION-v1`, equation (3.4).

New source-valid proof-interface counterexample: `QFORM-HYPERBOLIC-FRESNEL-HUB-L1-BARRIER-v1`, equation (4.11), already for fixed dimension `124` and iid Uniform[-1/2,1/2] inputs.

Required source theorem applied: `p_Q(s)<=pi sqrt(2)` for all `s>=0` in the same target-valid harmonic family.

Partner hard-square result applied: the family saturates `|d|=1`, proving that the new logarithm is not caused by weak transverse curvature.

Full exact rank three remains OPEN. Full QFORM remains OPEN. No counterexample to QFORM is claimed.

The next mathematical attack should be phase-sensitive: prove (5.3), or an equivalent two-sheet real-space estimate, without replacing the mixed `(xi,q)` phase by an absolute majorant, without moments/support/log-concavity, and without post-rotation independence.
