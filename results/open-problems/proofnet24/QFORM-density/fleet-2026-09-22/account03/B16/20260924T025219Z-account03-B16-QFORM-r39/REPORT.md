SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T02:52:19Z.
attacking: QFORM-MIXED-VOLUME-OVERLAP-TTSTAR-v1 — convert the two-bank mixed Pluecker volume in the punctured near-coloop collar into a dependence-safe nonlinear density receiver, using the fresh-or-transverse partner dichotomy at an actual inequality.

# account03/B16 r39 — mixed-volume absolute-TT* barrier and a sharp-frame same-sign closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T025219Z-account03-B16-QFORM-r39`  
**Role:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW SOURCE-VALID MECHANISM BARRIER + NEW STRICT-TARGET FAMILY CLOSURE / FULL QFORM OPEN`  
**Regularity:** the closure family below has a continuous `C_0` density with a universal height bound. No continuity conclusion is claimed for the barrier family from the argument in this report. Global continuity remains open.

## 1. Source boundary and corrections retained

The owner target remains the unrestricted statement: independent real original coordinates with scalar probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, centering, or post-rotation independence assumption is added.

Fresh controls were read from `yspennstate/math-research-brain/main`; at the final pre-write refresh the branch head was `bd27a6750c52510f9ad307e5ed3249e14883be9e` and OWNER CONTROL remained revision `2026-09-22.15`, with QFORM as the sole research target and no B16 pause. The live corrections are retained: no law-uniform pointwise quadratic stationary-phase bound, no worst conditional projection-density cap, no arbitrary-joint indefinite coarea estimate, no naive fiber-sup argument, and no independence after rotation.

The completed mathematical inputs actually used are:

1. **Preceding same-slot r38 mixed-volume compiler**, `yspennstate/math-open-problems@892c21d69f78bcf2fdc089addc1695bcf5b67aad`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T012049Z-account03-B16-QFORM-r38/REPORT.md`.
   It proves that in the slope-dominant balanced near-coloop packet the normalized pure-bank three-volume can vanish while the two mixed orientations each carry order-one volume; its sharp innovation-free frame has mixed masses exactly `1/2,1/2`.
2. **Designated partner account04/B16**, `yspennstate/math-open-problems@c1bf7fd07ac10b105686d96c96344a1a2274f5d9`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T021703Z-account04-B16-QFORM-r3/REPORT.md`.
   Its theorem `QFORM-FRESH-OR-TRANSVERSE-PAIRCAP-DICHOTOMY-v1` gives, in the shared-bank transverse branch,
   `||p_Q||_infinity <= 12 [G |gamma^2 kappa|]^(-1/3)` under its stated two-frame leverage gate.
3. **Phase-weighted punctured two-bank receiver**, account02/B16 at `yspennstate/math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`, whose proof uses the absolute frequency kernel
   `S_t(zeta)=integral_R2 |Phi_A(xi,nu,zeta) Phi_B(xi,nu,zeta)| dxi dnu`.
   It is valid when each source bank has the required two- and three-dimensional projection energies; the sharp r38 survivor violates the individual three-dimensional bank hypothesis.

This report does not treat any source-valid theorem as stronger than its written hypotheses.

## 2. The sharp mixed-volume Parseval frame

Let `X_1,X_2,X_3,X_4` be independent cap-one real variables. Define the three orthonormal original-coordinate linear forms

`L=(X_1-X_3)/sqrt(2)`,
`S=(X_2+X_4)/sqrt(2)`,
`P=(X_1+X_3)/sqrt(2)`.                                           (2.1)

In the `(L,S,P)` coefficient coordinates the four physical columns are

`c_1=(1/sqrt(2),0,1/sqrt(2))`,
`c_2=(0,1/sqrt(2),0)`,
`c_3=(-1/sqrt(2),0,1/sqrt(2))`,
`c_4=(0,1/sqrt(2),0)`.                                           (2.2)

They satisfy

`sum_i c_i c_i^T=I_3`.                                           (2.3)

Split the original sources into disjoint banks

`J={1,2}`, `K={3,4}`.                                             (2.4)

Each bank has rank exactly two. The pure-bank three-volume is therefore zero. The only nonzero mixed triple determinants are

`det(c_1,c_2,c_3)^2=1/2`,
`det(c_1,c_3,c_4)^2=1/2`.                                        (2.5)

Thus

`M_JJK=M_JKK=1/2`,                                                (2.6)

exactly the innovation-free endpoint identified in r38. This is not a numerical approximation.

The key question is whether the order-one mixed volume can simply replace the missing individual-bank three-dimensional density in the already-completed absolute-value TT* proof. The answer is no.

## 3. New obstruction: mixed Pluecker volume does not control the old absolute TT* kernel

Take now the strict target quadratic family

`Q_bar,theta
 = theta H^2 + 2 sqrt(2) H L + 2 P^2 + 4 L S`,                  (3.1)

where `H` is a fifth independent cap-one original source. In the orthonormal carrier basis `(H,L,P,S)` its matrix is

`A_bar,theta =
 [[theta, sqrt(2), 0, 0],
  [sqrt(2), 0,       0, 2],
  [0,       0,       2, 0],
  [0,       2,       0, 0]].`                                    (3.2)

The `(L,S)` principal `2 x 2` block has eigenvalues `+2,-2`. By Cauchy interlacing the `(H,L,S)` block has one eigenvalue at least `2` and one at most `-2`. The orthogonal `P` direction is an eigenvector with eigenvalue `2`. Hence, for **every real theta**, `A_bar,theta` has at least three eigenvalues of modulus at least `2`. Every member of (3.1) is therefore a strict instance of the owner target.

### Theorem `QFORM-MIXED-PLUCKER-ABSOLUTE-TTSTAR-BARRIER-v1`

Even with the maximal mixed-volume packet (2.6), the absolute frequency kernel used in the completed punctured two-bank proof can be infinite. In particular, take

`X_1,X_2,X_3,X_4 ~ Uniform[-1/2,1/2]` independently.               (3.3)

Let

`psi(s)=2 sin(s/2)/s`, `psi(0)=1`,                                (3.4)

be their common characteristic function. Regard the quadratic roles in (3.1) as the triple `(L,P,S)`, i.e. `P` is the square variable and `S` is the puncture/twist variable. The two bank transforms, with no same-bank phase, are

`Phi_J(xi,nu,zeta)
 = psi((xi+nu)/sqrt(2)) psi(zeta/sqrt(2))`,                        (3.5)

`Phi_K(xi,nu,zeta)
 = psi((-xi+nu)/sqrt(2)) psi(zeta/sqrt(2))`.                       (3.6)

Consequently the exact absolute kernel is

`S(zeta)
 = integral_R2 |Phi_J Phi_K| dxi dnu
 = |psi(zeta/sqrt(2))|^2 [integral_R |psi(u)| du]^2`.              (3.7)

The linear change

`u=(xi+nu)/sqrt(2)`, `v=(-xi+nu)/sqrt(2)`                           (3.8)

is orthogonal, so no Jacobian constant is hidden in (3.7).

But

`integral_R |psi(u)| du = infinity`.                               (3.9)

Indeed, with `w=u/2`,

`integral_0^infinity |psi(u)|du
 =2 integral_0^infinity |sin w|/w dw`,                             (3.10)

and on every interval

`[k pi+pi/6, k pi+5pi/6]`, `k>=1`,                                (3.11)

we have `|sin w|>=1/2`, giving a contribution at least

`2/[3(k+1)]`.                                                      (3.12)

The harmonic series diverges. Therefore

`boxed: S(zeta)=infinity`

for every `zeta` with `psi(zeta/sqrt(2)) != 0`, in particular at `zeta=0`. (3.13)

### Interpretation

This is a **proof-mechanism obstruction, not a QFORM counterexample**. The matrix family is target-valid and the source laws are the simplest interval laws, while the mixed Pluecker masses are exactly `1/2,1/2`. Thus no theorem can extend the completed punctured receiver to the innovation-free mixed-volume endpoint merely by replacing the missing per-bank 3D cap by `M_JJK+M_JKK` while retaining the same absolute kernel `integral |Phi_J Phi_K|`.

Cancellation in the crossing frequencies must be kept longer, or the nonlinear phase must be reorganized in original coordinates before that absolute value is taken. This sharpens the r38 successor: **mixed volume is necessary geometric currency in the slope collar, but it is not by itself an absolute-TT* norm bound.**

## 4. A phase-aligned sister orientation is completely paid

The same geometric frame has a strikingly different nonlinear orientation. Define

`Q_ctl,theta
 = theta H^2 + 2 sqrt(2) H L + 2 S^2 + 4 L P`.                  (4.1)

Its matrix in `(H,L,P,S)` is

`A_ctl,theta =
 [[theta, sqrt(2), 0, 0],
  [sqrt(2), 0,       2, 0],
  [0,       2,       0, 0],
  [0,       0,       0, 2]].`                                    (4.2)

Exactly the same interlacing argument shows that every `theta in R` gives at least one eigenvalue `>=2`, one `<=-2`, and the decoupled eigenvalue `2`. Hence this is also a strict owner-target family for all hub pivots.

### Theorem `QFORM-SHARP-MIXED-FRAME-SAMESIGN-CLOSURE-v1`

For **arbitrary** independent original sources `H,X_1,...,X_4` with scalar densities at most one and every real `theta`, the law of (4.1) has a continuous density vanishing at infinity and

`boxed: ||p_(Q_ctl,theta)||_infinity <= pi/sqrt(2)
       =2.2214414690... .`                                        (4.3)

### Proof

Expand (4.1) in the original coordinates using (2.1):

`2 sqrt(2) H L =2H(X_1-X_3)`,
`2S^2=(X_2+X_4)^2`,
`4LP=2(X_1^2-X_3^2)`.                                             (4.4)

Therefore

`Q_ctl,theta
 = theta H^2
   +2(X_1+H/2)^2
   -2(X_3+H/2)^2
   +(X_2+X_4)^2`.                                                 (4.5)

Condition on `H=h`. Then

`A_h=X_1+h/2`, `B_h=X_3+h/2`, `Z=X_2+X_4`                          (4.6)

are mutually independent. The translated laws of `A_h,B_h` retain density cap one. Also

`p_Z=f_2*f_4`, hence `||p_Z||_infinity<=1`                         (4.7)

by Young's inequality.

For any cap-one real `Y` and `a>0`, the density of `aY^2` satisfies

`g_(aY^2)(y)<=1/sqrt(a y)`, `y>0`.                                (4.8)

Thus the two **same-sign** independent terms

`2A_h^2` and `Z^2`                                                 (4.9)

have convolution density bounded by

`integral_0^t [2u]^(-1/2) [t-u]^(-1/2) du
 = pi/sqrt(2)`.                                                    (4.10)

Convolution with the independent reflected square `-2B_h^2` cannot increase an `L^infinity` norm, and adding the constant `theta h^2` merely translates the density. Hence for almost every `h`,

`||p_(Q_ctl,theta | H=h)||_infinity <= pi/sqrt(2)`.                (4.11)

Averaging in `h` proves (4.3).

For regularity, each square pushforward is an `L^1` density. The convolution of the two positive square densities is in `C_0(R)`; convolving with the third `L^1` square density stays in `C_0`. Thus each conditional density can be chosen continuous, and (4.11) provides a uniform dominating bound. Dominated convergence in `h` shows that the unconditional density is continuous. The same argument at infinity shows it vanishes there. QED.

This theorem uses only original-coordinate independence. No rotated coordinate is asserted independent.

## 5. Designated partner account04/B16 applied at an actual inequality

The control family (4.1) also gives a literal application of the newest completed designated partner theorem at `theta=0`.

Use the partner notation with the four leaf originals as its product bank `X`,

`ell = coefficient vector of L`,
`v   = coefficient vector of S`,
`V=S`, `sigma=0`,
`T=2P`,
`gamma=sqrt(2)`, `kappa=2`, `alpha=delta=0`.                      (5.1)

The two vectors `ell,v` are orthonormal, so

`G=det Gram(ell,v)=1`.                                             (5.2)

Their Gram-normalized two-frame has physical row leverages exactly `1/2` on each of the four leaves, so the partner leverage gate is met exactly. The fresh coefficient branch is unavailable because `sigma=0`, but its shared-bank transverse estimate gives

`||p_(Q_ctl,0)||_infinity
 <=12 [G |gamma^2 kappa|]^(-1/3)
 =12 * 4^(-1/3)
 =7.5595262993... <7.56`.                                         (5.3)

This is an actual source-valid target inequality, not a copied theorem statement. The new conditional same-sign argument then strengthens the same family to `pi/sqrt(2)` and extends it uniformly through **every** real hub-square coefficient `theta`.

The actual orthonormal two-dimensional projection theorem would also improve the intermediate pair cap from the partner's conservative `4/sqrt(G)` to `2` here, giving `3*2^(2/3)=4.7622031559...`; this sharpening is not needed for the new closure.

## 6. What the two sister families show

The barrier family (3.1) and the closure family (4.1) have:

- the **same** underlying orthonormal three-row leaf frame;
- the **same** disjoint banks `J,K`;
- the **same** pure-bank rank defect;
- the **same** mixed Pluecker masses `1/2,1/2`;
- the same universal target-level spectral interlacing.

Yet merely exchanging which transverse row is used as the square direction and which is the `LP` direction changes the available nonlinear proof mechanism completely. In one orientation the old absolute TT* kernel is already infinite for interval laws; in the other, original-coordinate conditioning exposes two same-sign independent squares and gives `pi/sqrt(2)` uniformly through the hub pivot.

Therefore the next B16 implication cannot be a scalar lower bound on total mixed volume alone. It must be **phase-aware**:

`QFORM-PHASE-AWARE-MIXED-VOLUME-DESCENT-v1` (OPEN): in the general slope-dominant near-coloop packet, use the mixed orientations together with the actual quadratic coefficient matrix to obtain either

1. two source-separated same-sign square resources after conditioning on the physical hub, so the beta-convolution argument closes the branch; or
2. a cancellation-preserving two-bank TT*/Fourier estimate that pairs the mixed-bank transforms before taking absolute values and yields an integrable common-time majorant.

The absolute product kernel of r37 is now ruled out as the universal innovation-free bridge. The mixed-volume algebra from r38 remains valid and useful; what is missing is its **phase-aligned** nonlinear conversion.

Arbitrary additional spectrum beyond this exact-rank-three structural packet remains a separate full-target interface.

## 7. Status

- `QFORM-MIXED-PLUCKER-ABSOLUTE-TTSTAR-BARRIER-v1`: **PROVED mechanism obstruction on a strict target family**. It refutes only the proposed absolute-kernel extension, not QFORM.
- `QFORM-SHARP-MIXED-FRAME-SAMESIGN-CLOSURE-v1`: **PROVED supporting theorem**, arbitrary cap-one source laws, all real hub pivots, continuous `C_0` density, `||p||_infinity<=pi/sqrt(2)`.
- Designated partner account04/B16: **applied to (5.3)**.
- Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full global continuity: **OPEN**.
