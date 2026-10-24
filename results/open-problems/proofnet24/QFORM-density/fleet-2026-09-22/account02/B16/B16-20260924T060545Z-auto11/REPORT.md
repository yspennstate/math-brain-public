SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T06:05:45Z.
attacking: partner-r41's punctured majority-sign root-numerator debt by using a leaf-dependent density-preserving physical-hub shear before the two-dimensional product/Fresnel step, and identifying the exact residual sign/leverage branch.

# account02/B16 — a density-preserving shear is not a product-preserving cap

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B16-20260924T060545Z-auto11`  
Role: Projection-product interaction / complementary constructions and source-valid counterexamples  
Status: **NEW SOURCE-INTERFACE CORRECTION + STRICT TARGET STRESS FAMILY / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; native runtime memory receiver use was not available/verified).  
Regularity: no new full-line continuity conclusion is claimed.

## 1. Source boundary

Fresh `math-research-brain/main` control was resolved during this invocation. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole research target and no account02/B16 pause or redirect is present. The live corrections are retained: no post-rotation independence, no arbitrary-joint indefinite coarea bound, no worst conditional projection-height cap, no law-uniform pointwise quadratic-phase decay, and no deletion of a small quadratic term for unbounded inputs.

The required pinned package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`. Two completed facts are used below:

1. for every cap-one probability density `f` and every complex `g` with `|g|<=f`, the pinned Lemma 1 gives

`integral |g_hat(xi)|^p dxi <= 4*pi/sqrt(p),  p>=2`;               (1.1)

2. the pinned ruled one-sheet theorem gives, for every strict rank-three signature `(+,+,-)` target with spectral magnitudes at least one,

`p_Q(s) <= pi*sqrt(2)` for almost every `s>=0`.                    (1.2)

The latest compatible designated partner is account03/B16 r41,

`yspennstate/math-open-problems@1d7d398aa8b3e0c60cef4381619491faad6565a7`,

which proves the exact nonzero-pivot Schur/range-leverage normal form and isolates `QFORM-PUNCTURED-MAJORITY-ROOT-NUMERATOR-v1`.

A newer account01/B16 report,

`yspennstate/math-open-problems@4cc097c9bc5e49f71cbb75a85a5a8b54b96ca4d5`,

proposes a density-preserving shear followed by a mixed-Fresnel/product factorisation. The calculation below finds a missing source-provenance step in that proof. This is a correction to the proof interface, not a counterexample to its final theorem and not a QFORM counterexample.

## 2. First unpaid implication — stated early

`QFORM-PUNCTURED-SHEARED-HUB-AMPLITUDE-v1`:

> In partner r41's exact-rank-three majority-sign collar, a leaf-dependent triangular shear of the literal physical hub is algebraically legitimate and has unit Jacobian, but after the shear the hub density becomes a factor of the form
>
> `f_H(h-c L(x)-eta P(x))`.
>
> Prove a mixed Fourier/Brascamp--Lieb estimate that retains this factor jointly with the original leaf-product density, or obtain an equivalent phase-aware `TT*` estimate. It is not valid to replace this factor by its pointwise cap and simultaneously keep the product characteristic-function cancellation of the leaf variables.

The rest of this report proves the obstruction precisely and places it inside a strict target-valid r41 family.

## 3. Partner r41 normal form and the tempting shear

Use the partner notation. Let an exact-rank-three real symmetric matrix have an ORIGINAL physical hub `h` with

`A=[[a,b^T],[b,C]],  a!=0`,

and Schur complement

`S=C-bb^T/a`, `rank S=2`.                                         (3.1)

Write

`b=b_R+b_0`, `b_R in ran S`, `b_0 in ker S`,
`rho=||b_R||`, `tau=||b_0||`,                                    (3.2)

and, when nonzero,

`ell=b_R/rho`, `p=b_0/tau`.

Choose unit `v in ran S` orthogonal to `ell`; put

`L=<ell,X_J>`, `V=<v,X_J>`, `P=<p,X_J>`.                          (3.3)

These three projections are generally dependent because they come from the same original-coordinate product bank. The physical hub `H=X_h` is genuinely independent of the residual bank.

Partner r41 proves the exact identity

`Q=a(H+(rho L+tau P)/a)^2 + (L,V) S_2 (L,V)^T`.                  (3.4)

It also proves

`q_h=a^2/(a^2+tau^2)`,                                            (3.5)

and, if `Delta_A` is the product of the three nonzero eigenvalues and `Delta_S=det S_2`,

`a Delta_S=q_h Delta_A`.                                          (3.6)

In the live collar `q_h>=63/64`, `0<|a|<=s/64`, `|mu_j|>=s`, r41 further gives

`rho^2 >=(62/63)s^2`, `tau<=|a|/sqrt(63)`.                       (3.7)

The algebraic shear

`h_1=h+(tau/a)P`                                                   (3.8)

has unit Jacobian for each fixed residual source point and removes `P` from the phase in (3.4). If one subsequently performs another real shear

`h_2=h_1+cL`,                                                      (3.9)

the literal hub density becomes

`f_H(h_2-cL-(tau/a)P)`.                                           (3.10)

Equation (3.10), not merely its bound by one, is the source information that must survive if one wants to retain Fourier cancellation over the original leaf coordinates.

## 4. The exact mask counterexample

### Theorem `QFORM-SHEARED-HUB-CAP-DOES-NOT-FACTOR-v1`

There is no valid rule that, after a leaf-dependent shear, replaces the translated hub density by its `L^infinity` cap while preserving the unweighted characteristic-function factor of the leaf source.

Already take two genuinely independent cap-one variables

`H,X ~ Uniform[0,1]`.                                              (4.1)

Set

`f_H=f_X=1_[0,1]`, `w=0`, `c=-2`.                                (4.2)

Then the sheared hub factor is

`f_H(w-cX)=1_[0,1](2X)=1_[0,1/2](X)`.                            (4.3)

At frequency `xi=2*pi`, the unweighted leaf transform vanishes:

`integral_0^1 exp(i 2*pi*x) dx=0`.                               (4.4)

But the correctly retained sheared amplitude gives

`integral_0^1 f_H(2x) exp(i 2*pi*x) dx
 =integral_0^(1/2) exp(i 2*pi*x) dx
 = i/pi`,                                                         (4.5)

hence its modulus is

`boxed: 1/pi>0`.                                                   (4.6)

Therefore an implication of the form

`|integral f_X(x) f_H(w-cx) exp(i xi x) dx|
 <= ||f_H||_infinity |f_X_hat(xi)|`                               (4.7)

is false even for two independent unit-interval uniforms.

More generally, for every nonzero `c`, by translating `w` one can make the set

`{x in [0,1]: 0<=w-cx<=1}`                                       (4.8)

have any prescribed length in a nontrivial interval; choosing a Fourier zero of `1_[0,1]` again produces a nonzero masked transform. Thus this is not a special feature of the numerical value `c=-2`.

### Consequence for the proposed shear proof

The account01/B16 report cited above obtains a factor

`a_t(w'-cL(x))`, `|a_t|<=M`,                                     (4.9)

after a density-preserving shear, and then passes to a product of the original-coordinate twisted transforms while paying only `M`. The mask calculation (4.1)-(4.6) shows that the pointwise cap in (4.9) does not justify that product factorisation. A bounded multiplier depending on a leaf projection can select a phase-aligned subset of the leaf law and destroy a Fourier zero.

This identifies a gap in the displayed transition from the bounded sheared amplitude to the product-transform integral in that report. It does **not** establish that the final density theorem stated there is false; a different argument could still prove it.

## 5. Why Fourier-expanding the mask is not a cap-one repair

One natural attempt is to Fourier-expand the translated hub factor before taking absolute values. For the admissible hub law

`f_H=1_[0,1]`,                                                    (5.1)

its characteristic function is

`psi_H(xi)=exp(i xi/2) * 2 sin(xi/2)/xi`.                          (5.2)

Hence

`integral_R |psi_H(xi)| dxi = infinity`.                          (5.3)

Indeed on every interval around an odd multiple of `pi`, `|sin(xi/2)|` is bounded below by an absolute positive constant, so the absolute integral dominates a harmonic series.

This is exactly where the required pinned completed result is informative. Lemma 1 at `e5f71d79...` gives, for this same admissible source and every `p>=2`,

`integral |psi_H|^p <=4*pi/sqrt(p)`.                              (5.4)

Thus strong law-uniform `L^p`, `p>=2`, control is available, while the `L^1` Wiener norm required by the naive absolute Fourier expansion can be infinite. The missing shear estimate has to combine the hub transform with the leaf factors before absolute integration; it cannot pay an isolated `||psi_H||_1`.

This is a concrete use of the pinned Fourier result at a real obstruction, not a restatement of the pointwise-decay correction.

## 6. Strict r41 target family with nonzero hidden leakage

The obstruction is not confined to an off-target toy normal form. Take four residual original coordinates and choose three orthonormal Walsh vectors

`ell,v,p in R^4`,                                                  (6.1)

each entry of magnitude `1/2`. Then

`ell_i^2+v_i^2=1/2`                                                (6.2)

for every leaf coordinate, exactly at the diffuse two-plane leverage gate.

Let the physical hub `H` be a fifth independent cap-one source and set

`a=1/64`, `tau=1/512`, `q=a^2/(a^2+tau^2)=64/65`,                (6.3)

`K=64`,

`rho^2=a(K-a)=4095/4096`,                                         (6.4)

and

`S=-K ell ell^T + K v v^T`,
`b=rho ell+tau p`,
`C=S+bb^T/a`.                                                      (6.5)

Define

`A=[[a,b^T],[b,C]]`.                                              (6.6)

Then `rank A=3` because the Schur complement at the hub is exactly the rank-two matrix `S`. Moreover

`q=64/65>63/64`, `0<a=1/64`,                                     (6.7)

so this is literally in the punctured near-coloop collar. Its Schur determinant is

`Delta_S=-K^2=-4096`,                                             (6.8)

and (3.6) gives

`Delta_A=a Delta_S/q=-65`.                                        (6.9)

The vector `v` is an eigenvector of `A` with eigenvalue `64`. On `span(H,ell,p)` the matrix has rank two, trace

`T=a+rho^2/a-K+tau^2/a=1/4096`,                                  (6.10)

and the product of its two nonzero eigenvalues is

`Delta_A/64=-65/64`.                                               (6.11)

Hence those two eigenvalues are the roots of

`z^2-(1/4096)z-65/64=0`.                                          (6.12)

At `z=1` the polynomial equals `-65/4096<0`; at `z=-1` it equals `-63/4096<0`. Since the leading coefficient is positive, the positive root is `>1` and the negative root is `<-1`. Therefore

`boxed: A has nonzero spectrum {64, lambda_+, lambda_-}, with lambda_+>1 and lambda_-<-1.}`   (6.13)

This is a strict instance of the owner target with genuine nonzero Schur-kernel leakage `tau P`.

Because its signature is `(+,+,-)`, the completed ruled one-sheet theorem in the required pinned `COUNTEREXAMPLE_SEARCH.md` applies directly and gives the actual target inequality

`boxed: p_Q(s)<=pi*sqrt(2) for almost every s>=0.}`                 (6.14)

This half-line estimate is source-valid: it spends the two-dimensional product marginal as a joint line-integral bound and never declares projected coordinates independent.

On the opposite side, the partner r41 root formula retains the two translated values of the literal hub density. Performing the algebraic shear (3.8) is legitimate, but the mask theorem above shows why capping the resulting factor `f_H(h-(tau/a)P-cL)` before leaf-product averaging is not a valid route to a global mixed-Fresnel factorisation.

## 7. Exact interface statement

The correct distinction is now:

- **algebraic shear:** valid; the triangular change in the physical hub has Jacobian one;
- **density cap after shear:** valid pointwise, `f_H(h-shift(x))<=1`;
- **product factorisation after using only that cap:** invalid in general, by (4.1)-(4.6);
- **post-shear projected independence:** not asserted and not available;
- **Fourier restoration by an isolated hub Wiener norm:** nonuniform and may be infinite, by (5.3);
- **two-dimensional product marginal on a ruled curved integral:** valid in the pinned one-sheet theorem and used at (6.14).

This is the exact projection-product interface the B16 assignment asks to test.

## 8. Sharpened next step

The first mathematical debt is therefore not merely “perform a density-preserving shear”. It is the mixed estimate

`QFORM-SHEARED-HUB-BL-OR-TTSTAR-v1`:

> Starting from (3.10), retain the translated original hub density as an additional source datum and prove an integrable `|t|^{-3/2}`-scale estimate jointly with the diffuse `(L,V)` leaf plane, without paying `||psi_H||_1`, a worst conditional projection cap, or post-rotation independence.

A viable proof would have to place the hub factor inside the Brascamp--Lieb/TT* geometry rather than remove it before the leaf oscillatory integral. In the r41 collar the quantitative currencies remain favorable: `rho>=s sqrt(62/63)` and `|tau/a|<=1/sqrt(63)`. The obstruction proved here says precisely which shortcut cannot spend them.

The heavy two-plane branch `max_i(ell_i^2+v_i^2)>1/2` and arbitrary additional nonseparable spectrum remain separate interfaces. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**; full-target continuity remains open.
