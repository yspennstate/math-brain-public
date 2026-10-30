SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T22:21:29Z.
attacking: QFORM-ZEROPIVOT-CHIRP-STRICHARTZ-L1-v1 — integrate the fleet02/B02 nonzero-tail chirp kernel in time before taking the worst modulation, replacing its pointwise-critical |t|^{-1} envelope by a genuine L1_t bound.

# fleet01/B02 r39 — integrated chirp/Strichartz bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T222129Z-fleet01-B02-qform-auto11-r39`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN-NOT-REFUTED**

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional densities at most one; arbitrary real symmetric A; at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, diagonal-basis, or post-rotation independence assumption is introduced.

## 1. Fresh control and dependency actually used

Fresh `math-research-brain/main` was resolved at run start. Owner control remains revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`, QFORM-only. The live correction package was consumed: no law-uniform scalar pointwise Fresnel decay, no post-rotation independence, no arbitrary-joint coarea cap, no worst conditional-density cap, no one-minor shortcut.

Designated partner result used at equation level:

- `yspennstate/math-open-problems@612be1591c1aa5edaeb29bb6eceec7963ddbef55`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T212459Z-fleet02-B02-qform-auto11/EARLY.md`.

That source derives the exact nonzero-tail operator

`(T_delta f)(y)=int k_t(alpha y+beta z) exp(i 2t delta yz) f(z) dz`

and proves that, with zero hub quadratic coefficient,

`||T_delta||_(2->2)=sqrt(pi/(|t delta|)) U((alpha beta/delta)t)`,

where

`U(s)=sup_eta |int g(h) exp(-i(s h^2+eta h)) dh|`,

`0<=g<=1`, `int g=1`, and it also retains the transverse bilinear factor

`||S_sigma||_(2->2)=sqrt(pi/(|t sigma|))`.

The partner correctly observes that replacing U by its pointwise cap 1 gives only the critical, nonintegrable envelope `pi |t|^-1 |delta sigma|^-1/2`. The result below integrates in t before taking a law-uniform pointwise bound.

## 2. The one-dimensional maximal parabola estimate

Define, for `g in L2(R)`,

`E g(s,eta)=int_R g(h) exp(-i(s h^2+eta h)) dh`,

and

`U_g(s)=sup_eta |E g(s,eta)|`.

There is a universal finite constant `C_Str` such that

`boxed: ||U_g||_(L4(ds)) <= C_Str ||g||_2.`        (2.1)

This is the one-dimensional `(q,r)=(4,infinity)` Schrödinger/extension estimate. For completeness, it follows directly by TT*: the kernel of `E E*` is the Fresnel kernel

`int exp(i((s-s')xi^2+(eta-eta')xi)) dxi`,

whose modulus is `sqrt(pi)|s-s'|^-1/2`; the one-dimensional Hardy--Littlewood--Sobolev map `L^(4/3)_s -> L^4_s` for convolution with `|s|^-1/2`, together with the `L1_eta -> Linfinity_eta` dispersive bound, gives (2.1). No regularity, moment, or support assumption on g is needed.

For a cap-one probability density, `||g||_2<=1`; hence for every nonzero `a`,

`boxed: ||U_g(a .)||_4 <= C_Str |a|^-1/4.`          (2.2)

This is exactly the averaging information missing from the partner's pointwise-critical calculation.

## 3. Three-bank integrated chirp theorem

Let `H`, `Y=(Y1,Y2)`, and `Z=(Z1,Z2)` be independent ORIGINAL-coordinate banks after any within-bank volume-preserving linear changes already justified by a source theorem. Assume:

- H has a scalar density `f_H<=1`;
- Y and Z have joint densities bounded by `M_Y` and `M_Z`;
- the hub scalar quadratic coefficient is zero (an arbitrary affine hub term is allowed);
- arbitrary real within-Y and within-Z quadratic/affine phases are allowed.

For nonzero real `alpha,beta,delta,sigma`, consider the cross part

`2H(alpha Y1+beta Z1)+2 delta Y1 Z1+2 sigma Y2 Z2`.       (3.1)

### Theorem `QFORM-ZEROPIVOT-CHIRP-STRICHARTZ-L1-v1`

The full ambient characteristic function satisfies

`boxed:
 int_R |phi_Q(t)| dt
 <= C_ch (M_Y M_Z)^(2/5)
    |alpha beta delta sigma^2|^(-1/5),`                 (3.2)

where

`C_ch = [10/4^(4/5)] [pi 3^(3/4) C_Str]^(4/5)`          (3.3)

is universal. Consequently

`boxed:
 ||p_Q||_infinity
 <= [C_ch/(2pi)] (M_Y M_Z)^(2/5)
    |alpha beta delta sigma^2|^(-1/5),`                 (3.4)

and this branch has a continuous density vanishing at infinity.

### Proof

Absorb all within-bank phases into the complex bank amplitudes. Their L2 norms obey

`||a_t||_2<=sqrt(M_Y)`, `||b_t||_2<=sqrt(M_Z)`.

The cross-kernel factors as the tensor product of the partner's `T_delta` on `(Y1,Z1)` and `S_sigma` on `(Y2,Z2)`. Therefore the exact partner formulas give

`|phi_Q(t)|
 <= sqrt(M_Y M_Z) pi |t|^-1 |delta sigma|^-1/2
    U_g((alpha beta/delta)t).`                           (3.5)

An arbitrary affine hub term only translates the modulation eta and hence does not change U_g.

Set `M=sqrt(M_Y M_Z)` and

`B=M pi 3^(3/4) C_Str
    |delta|^-1/4 |sigma|^-1/2 |alpha beta|^-1/4.`       (3.6)

For `T>0`, Holder with exponents 4 and 4/3, followed by (2.2), yields

`int_T^infinity |phi_Q(t)| dt
 <= M pi |delta sigma|^-1/2
    (int_T^infinity t^(-4/3)dt)^(3/4)
    ||U_g((alpha beta/delta).)||_4
 <= B T^-1/4.`                                          (3.7)

Since Q is real, `|phi_Q(-t)|=|phi_Q(t)|`, while trivially `|phi_Q(t)|<=1`. Hence

`int_R |phi_Q(t)|dt <= 2T+2B T^-1/4.`                  (3.8)

Optimizing at `T=(B/4)^(4/5)` gives

`int_R |phi_Q(t)|dt
 <= [10/4^(4/5)] B^(4/5),`                              (3.9)

which is exactly (3.2), because

`B^(4/5)
 =(M pi 3^(3/4) C_Str)^(4/5)
  |alpha beta delta sigma^2|^(-1/5)`.

Fourier inversion gives (3.4) and the continuous `C0` density conclusion. QED.

## 4. What this does to the partner obstruction

The partner's section 3 had the exact pointwise product bound

`||T_delta tensor S_sigma||_(2->2)
 <= pi |t|^-1 |delta sigma|^-1/2`,                      (4.1)

and therefore identified a pointwise-critical `|t|^-1` barrier. Theorem (3.2) shows that **this is not an integrated-Fourier barrier**: every nonzero `delta` realization of that exact kernel already has `phi_Q in L1`, uniformly over all cap-one hub laws, after integrating in t before taking the maximal modulation.

Thus the nonzero-tail chirp mechanism has the following exhaustive local status:

- `delta=0`: the partner's exact-rank-one theorem gives the stronger `|t|^-3/2` envelope and finite L1;
- `delta!=0`: the new maximal-parabola theorem gives finite L1 by (3.2).

The remaining issue is **uniformity as `delta -> 0`**, not finiteness of the integrated Fourier norm on either side. Formula (3.2) blows only like `|delta|^-1/5`, strictly milder than taking the pointwise law-uniform chirp norm and then integrating (which does not integrate at all).

## 5. Equation-level application to the partner heavy-hub packet

The same partner source records, from the newest three-bank compiler, a heavy-hub inequality

`D_h >= (8/3125) V1`.                                    (5.1)

Whenever the realized near-rank-one coordinates have a core fraction

`(alpha beta sigma)^2 >= theta D_h`                      (5.2)

for some explicit `theta>0`, (3.2) and (5.1) give the actual quantitative inequality

`boxed:
 int |phi_Q|
 <= C_ch (M_YM_Z)^(2/5)
    theta^(-1/10) (8/3125)^(-1/10)
    V1^(-1/10) |delta sigma|^(-1/5).`                    (5.3)

In particular, on the mesoscopic-tail subbranch

`|delta sigma| >= kappa V1^(1/3)`,                       (5.4)

one gets the scale-correct target-form estimate

`boxed:
 int |phi_Q|
 <= C_ch (M_YM_Z)^(2/5)
    theta^(-1/10) (8/3125)^(-1/10) kappa^(-1/5)
    V1^(-1/6).`                                          (5.5)

This is a genuine unweighted Fourier-L1 exit. For the same orthonormal two-dimensional bank projections used in the partner rank-one theorem, `M_Y,M_Z<=2`, so the bank-density factor is at most `4^(2/5)`.

The hypothesis (5.2) is deliberately recorded rather than silently assumed. At the exact rank-one endpoint it holds with `theta=1`; in a quantitative near-rank-one implementation it must be supplied by the chosen singular-core decomposition. No claim is made that (5.2) follows from the bare global spectral hypothesis without that decomposition.

## 6. Remaining exact debt

The first unpaid local implication is now narrower:

`QFORM-ZEROPIVOT-CHIRP-UNIFORM-ENDPOINT-GLUE-v1`.

One must glue the `delta=0` exact-rank-one `|t|^-3/2` estimate to the `delta!=0` Strichartz-integrated estimate **uniformly as delta->0**, or show that the branch `|delta sigma| << V1^(1/3)` automatically produces enough quantitative rank-one core mass for a separate paid receiver. Pointwise operator interpolation cannot do this, as the partner's sharp phase-aligned obstruction shows.

No exact-target counterexample to a universal `int |phi_Q|` bound was found. Target-wide Fourier-L1 remains `OPEN_NOT_REFUTED`. Full bounded density remains OPEN. Full-target continuity remains OPEN; continuity is proved only on branches with an actual L1 characteristic-function estimate, including the theorem above.

## 7. Integrity checks

- No general rotation of the independent input vector is used.
- Within-bank linear changes are invoked only where the bank source theorem supplies a joint-density cap; no independence is claimed inside a transformed bank.
- No moment or support assumption appears in the Strichartz step.
- No pointwise law-uniform Fresnel decay is used.
- The hub quadratic coefficient is explicitly zero; this is the live zero-pivot branch. An affine hub term is harmless, but a nonzero hub square changes the chirp parameter and is not silently included.
- The theorem is homogeneous: `alpha beta delta sigma^2` has coefficient degree five, so the `-1/5` exponent has the correct inverse-Q scale.
