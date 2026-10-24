SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T20:03:55Z.
attacking: near-singular transverse spectral-coloop routing via conditional slope-space slicing and L4-in-frequency Schur amplitudes.

# General one-hub / two-bank bilinear Schur-L4 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T200355Z-account01-B01-qform-auto11`  
Role: account01/B01 — oscillatory replacement  
Status: **PROVED SUPPORTING ANALYTIC THEOREM + STRICT-N3 TARGET FAMILY; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source correction

The target remains the full arbitrary-dimensional statement for independent scalar coordinates with density caps one and a real symmetric matrix with at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, log-concavity, connected support, diagonal-basis independence, or post-rotation independence is introduced.

The phase-aligned counterexample to law-uniform scalar pointwise Fresnel decay remains intact. For any prescribed `s>0` and sufficiently small `eta>0`, choose a finite measurable set of measure one inside

`{x : dist(s x^2,2*pi*Z)<=eta}`.

Its indicator is an admissible density and has `Re E exp(i s X^2)>=cos(eta)`. Nothing below asserts a pointwise `O(|t|^-1/2)` estimate. The replacement is again an integrated-frequency statement, but the new step is structural: it tolerates **arbitrary quadratic self-curvature on both two-dimensional banks and unequal hub couplings to the banks**.

Source controls consumed at run start: `yspennstate/math-research-brain@4c80cfff0aae4c7717bbf7b6d8194e6b85409469`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only. Required corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, the arbitrary-joint coarea counterexample, and the false conditional-cap interfaces in the live correction inbox.

Two previously proved inputs are used exactly at equations:

1. account02/B01 scalar square-phase `L^4(dt)` theorem, canonical source `yspennstate/math-open-problems@91dbcb0e8b3f6faa4af9629aaaff2f69d385695a`, which gives, for every scalar cap-one probability density, every `c!=0`, and every affine coefficient `ell`,

`int_R |E exp(it(cX^2+ell X))|^4 dt <= 27*pi/(2|c|)`.

Its cap-`K`, nonnormalized extension proved in the preceding B01 report `yspennstate/math-open-problems@a7345ba08be60f1fd5d02308fc68b23e2016ff51` is

`int |int g(x)e^{it(c x^2+ell x+c0)}dx|^4 dt <= [27*pi/(2|c|)] K^2 m^2`        (1.1)

for `0<=g<=K`, `m=int g`.

2. The reviewed two-dimensional product-projection cap from `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`: if a rank-two linear image of an independent cap-one product bank has Gram matrix `G>0`, then its two-dimensional density is at most `2/sqrt(det G)`.

## 2. Main theorem

Let `X` be scalar with density `f_X<=1`. Let `U,V` be independent `R^2`-valued random vectors, independent also of `X`, with probability densities

`p_U<=M_U`, `p_V<=M_V`.

Let `A,C` be arbitrary real symmetric `2x2` matrices, let `B` be an arbitrary **invertible** real `2x2` matrix (not assumed symmetric), let `p,q in R^2`, and let `a in R`. Arbitrary deterministic affine terms are allowed. Consider

`Q = a X^2 + 2X p^T U + 2X q^T V
     + U^T A U + 2 U^T B V + V^T C V
     + ell_x X + ell_U^T U + ell_V^T V + c0`.              (2.1)

Define the kernel-curvature scalar

`d_B = a - 2 p^T B^{-T} q + q^T B^{-1} A B^{-T} q`.        (2.2)

Equivalently, with

`v_B=(1,-B^{-T}q) in R x R^2`,
`K_XU=[[a,p^T],[p,A]]`,

one has the exact structural identity

`d_B = v_B^T K_XU v_B`.                                    (2.3)

Thus `d_B` is precisely the quadratic curvature along the one-dimensional kernel of the slope map `(x,u) -> B^T u+qx`.

### Theorem 2.1 — `QFORM-ONEHUB-TWOBANK-GENERAL-BILINEAR-SCHUR-L4-v1`

If `d_B !=0`, then `phi_Q in L^1(R)`. Hence `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= C0 (M_U M_V)^(2/5) |det B|^(-2/5)|d_B|^(-1/5),
 C0=5(3sqrt(6)/8)^(4/5)
   =4.67149102355819... .`                                  (2.4)

The theorem is sign-free. `A` and `C` may be singular, definite, indefinite, or arbitrarily large. In particular, the self-curvature on either two-dimensional bank need not equal the cross matrix `B`; this is the extension beyond the preceding B01 `U+V` theorem.

### Scaling

Under multiplication of the whole quadratic form by `lambda`, `B` and `d_B` both scale by `lambda`, so the right-hand side of (2.4) scales by `|lambda|^{-1}`, exactly as a density must.

## 3. Proof: exact slope completion with arbitrary bank self-curvature

Define the two-dimensional slope

`r = B^T U + q X`.                                           (3.1)

For fixed `x`, the change of variables is

`u=B^{-T}(r-qx)`, `du=|det B|^{-1}dr`.                       (3.2)

The crucial exact cancellation is

`2u^T Bv + 2x q^T v = 2r^T v`.                              (3.3)

Put

`S=B^{-1} A B^{-T}`.                                         (3.4)

Substitution into the part depending on `(x,u)` gives

`u^T A u + 2x p^T u + a x^2 + ell_U^T u + ell_x x
 = r^T S r + ell_U^T B^{-T}r
   + d_B x^2 + beta(r)x`,                                    (3.5)

where

`beta(r)
 = 2[p^T B^{-T} - q^T B^{-1}AB^{-T}]r
   + ell_x - ell_U^T B^{-T}q`.                               (3.6)

The coefficient of `x^2` is independent of `r`; this is exactly why the scalar square-phase theorem can be spent despite arbitrary `A`.

For every frequency `t`, push the complex `(X,U)` measure through `r`. Its density is

`a_t(r)=|det B|^{-1}
        exp(it[r^T S r+ell_U^T B^{-T}r])
        int g_r(x) exp(it[d_B x^2+beta(r)x]) dx`,             (3.7)

where

`g_r(x)=f_X(x)p_U(B^{-T}(r-qx))`.                             (3.8)

For every `r`,

`0<=g_r<=M_U`.                                                (3.9)

If `m_r=int g_r`, then Fubini and the affine map (3.1) give the exact mass identity

`int_R2 m_r dr = |det B|`.                                   (3.10)

Let

`A_t = ||a_t||_{L^2(dr)}`.                                   (3.11)

By Minkowski in `L^2(dt)` applied to `A_t^2`, followed by (1.1),

`||A_.||_4^2
 <= |det B|^{-2}
    int_R2 ||int g_r(x)e^{it(d_Bx^2+beta(r)x)}dx||_4^2 dr`

`<= |det B|^{-2}
    [27*pi/(2|d_B|)]^(1/2) M_U int m_r dr`

`= [27*pi/(2|d_B|)]^(1/2) M_U |det B|^{-1}`.                (3.12)

Therefore

`boxed:
 ||A_.||_4
 <= (27*pi/2)^(1/4)
    M_U^(1/2)|det B|^(-1/2)|d_B|^(-1/4).`                   (3.13)

This is the averaged-frequency resource. Individual scalar transforms may still have order-one phase-aligned spikes.

Now put

`b_t(v)=p_V(v)exp(it[v^T C v+ell_V^T v+c0])`.                (3.14)

Its `L^2` norm satisfies `||b_t||_2<=M_V^(1/2)`. By (3.3),

`phi_Q(t)=int_R2 int_R2 a_t(r)b_t(v)e^{2it r^T v}drdv`.      (3.15)

With Fourier convention `hat b(xi)=int b(v)e^{i xi^T v}dv`, two-dimensional Plancherel gives, for `t!=0`,

`|phi_Q(t)|
 <= ||a_t||_2 [int |hat b_t(2tr)|^2dr]^(1/2)
 = pi |t|^{-1} A_t ||b_t||_2`

`<= pi M_V^(1/2)|t|^{-1}A_t`.                               (3.16)

Hence

`|phi_Q(t)|<=min{1, pi M_V^(1/2)|t|^{-1}A_t}`.              (3.17)

For every `T>0`, Holder with exponents `4` and `4/3` gives

`int_R |phi_Q(t)|dt
 <=2T + pi M_V^(1/2)
   [int_|t|>T |t|^(-4/3)dt]^(3/4)||A_.||_4`

`=2T + D0 T^(-1/4)`,                                         (3.18)

where

`D0=3sqrt(6) pi^(5/4)
    (M_U M_V)^(1/2)|det B|^(-1/2)|d_B|^(-1/4)`.             (3.19)

The minimum occurs at `T=(D0/8)^(4/5)` and equals `10(D0/8)^(4/5)`. Fourier inversion yields (2.4). Since `phi_Q in L^1`, its inverse Fourier transform is a continuous `C_0` density. QED.

## 4. Symmetric orientation and the exact remaining zero-curvature gate

The theorem may also be run with the banks reversed. Defining

`d_B^(V)
 = a - 2 q^T B^{-1}p
   + p^T B^{-T} C B^{-1}p`,                                  (4.1)

one gets the same bound with `M_U,M_V` interchanged and `d_B` replaced by `d_B^(V)`.

Consequently, for an invertible cross block `B`, the only scalar-curvature endpoint not covered by this compiler is the simultaneous state

`d_B=0` and `d_B^(V)=0`.                                     (4.2)

This is an exact structural narrowing: arbitrary bank self-curvature is harmless unless it cancels the one-dimensional slope-kernel curvature in **both** product-preserving orientations. Near-zero versions remain quantitatively delicate because (2.4) pays `|d|^{-1/5}`.

## 5. Strict-N3 target family with arbitrary same-bank curvature

This family shows that the theorem is not merely the preceding special `(U+V)^T M(U+V)` case and is not a good physical-pivot argument.

Let `m>=4` be even. Choose flat orthonormal vectors `r,s in R^m` with each coordinate of magnitude `m^{-1/2}`. Use one original scalar coordinate `X`, a disjoint bank `Y in R^m`, and a disjoint bank `Z in R^m`, and define

`U=(<r,Y>,<s,Y>)`,
`V=(<r,Z>,<s,Z>)`.                                            (5.1)

The two bank Grams are both `I_2`, so the reviewed product-projection theorem gives

`M_U<=2`, `M_V<=2`.                                           (5.2)

On the five-dimensional spectral coordinates `(X,U_1,U_2,V_1,V_2)` take

`a=0`, `p=0`, `q=(2,0)^T`,
`A=diag(4,0)`, `B=2I_2`, `C=0`.                              (5.3)

Thus

`K=
 [[0,0,0,2,0],
  [0,4,0,2,0],
  [0,0,0,0,2],
  [2,2,0,0,0],
  [0,0,2,0,0]]`.                                             (5.4)

The characteristic polynomial factors exactly as

`(lambda-2)(lambda+2)(lambda^3-4lambda^2-8lambda+16)`.       (5.5)

The explicit eigenvalues are approximately

`-2.34017297, -2, 1.37778437, 2, 4.96238861`,                (5.6)

so this is a valid target packet with five eigenvalues, at least three of modulus at least one.

The frame from `(X,Y,Z)` to `(X,U,V)` has orthonormal columns, so the nonzero physical spectrum is exactly (5.6). Yet every physical diagonal is at most `4/m`. Every physical `2x2` principal determinant has magnitude at most `4/m` for `m>=4`: hub-`Z` pairs have determinant exactly `-4/m`; hub-`Y` pairs vanish; `Y-Y` and `Z-Z` pairs vanish; and a `Y-Z` pair has determinant magnitude at most `16/m^2`. Hence every scalar and pair pivot tends to zero as `m->infinity`.

For (5.3),

`det B=4`,
`d_B=q^T B^{-1}AB^{-T}q=4`.                                  (5.7)

Theorem 2.1 and (5.2) therefore give, for **every** admissible cap-one product law,

`boxed:
 ||p_Q||_infinity
 <= C0 * 4^(2/5) * 4^(-2/5) * 4^(-1/5)
 = C0*4^(-1/5)
 = 3.540328167355882... .`                                   (5.8)

The density is continuous and vanishes at infinity.

The preceding B01 theorem required the same matrix to govern both bank self-curvatures and their cross term, namely a form in `U+V`. Here `A=diag(4,0)`, `B=2I_2`, `C=0`, so that hypothesis fails maximally; the present theorem reattaches such same-bank quadratic curvature exactly.

## 6. Designated-partner theorem applied to an actual inequality

The newest **completed** account02/B01 result available at run start is `QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`, source-pinned in `yspennstate/math-open-problems@339c1fdf3bc65a79f5be126e730dd3b251320e66`.

After a scalar completion `a(X_0+h)^2`, with residual one-hub slope vector `m` and projected crossing `C`, it proves

`||p_Q||_infinity <= 8 |a|^(-1/2)(||m|| ||C||_F)^(-1/4)`      (6.1)

without a projected-row marginal restriction.

On its strict-N3 stress family,

`a=epsilon`, `||m||=epsilon^(-1)`, `||C||_F=epsilon^(-1)`,    (6.2)

so (6.1) gives the actual equation

`8 epsilon^(-1/2)(epsilon^(-2))^(-1/4)=8`.                   (6.3)

Its heavy-row subbranch sharpens this to `2^(11/4)=6.727171322...`. This result is complementary to Theorem 2.1: (6.1) spends a nonzero projected crossing after an original scalar square completion, while Theorem 2.1 spends an invertible **two-bank** cross block plus a nonzero slope-kernel curvature and permits arbitrary quadratic self-curvature on both banks.

The foundational account02/B01 scalar `L^4` theorem is also used directly in (3.12), not merely cited qualitatively.

## 7. What is actually gained, and what remains open

The new theorem removes a real restriction from the prior B01 spectral-coloop compiler: additional quadratic spectrum living **inside either of the two independent banks** no longer has to be absent or match the cross matrix. The only algebraic quantity from the `(X,U)` self block that survives into the analytic estimate is the exact one-dimensional slope-kernel curvature `d_B`.

The first unpaid implication is now

`QFORM-TWOBANK-SIMULTANEOUS-ZEROKERNEL-OR-NEARSINGULAR-CROSS-ROUTING-v1`:

Starting from the remaining high-leverage / coloop configurations, quantitatively route either

1. to two disjoint two-dimensional banks with invertible cross block `B` and at least one orientation having target-scale kernel curvature `|d_B|` or `|d_B^(V)|`, now paid by Theorem 2.1; or
2. when `B` is singular/nearly singular or both kernel curvatures vanish/nearly vanish, into an already-paid hyperbolic/pair-Schur, projected-crossing half-Riesz, grouped-square, ridge, volume, or zero-self-block slope-slicing receiver.

The simultaneous exact equations `d_B=d_B^(V)=0` are a sharply identified algebraic endpoint, not a proof that such states are harmless. Quantitative near-zero routing also remains open. The unrestricted conjecture therefore remains **OPEN**. Full-target continuity is also **OPEN**; continuity is proved only for the scoped theorem above.

No Monte Carlo histogram, post-rotation independence claim, arbitrary-joint coarea bound, or scalar pointwise quadratic decay is used anywhere in this report.
