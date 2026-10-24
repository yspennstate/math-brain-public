SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-24T01:44:47Z.
attacking: spectral-tail normal-form receiver — exploit `EU=0` to prevent large carrier/physical-diagonal cancellation in the small-alignment survivor, and feed the designated partner compound currency into an actual inequality.

# account01/B08 r40 — spectral-tail carrier contraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING STRUCTURAL THEOREM + QUANTITATIVE SURVIVOR REDUCTION / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains **OPEN**. The unrestricted continuous-density conclusion also remains **OPEN**. Every stochastic coordinate remains an ORIGINAL independent coordinate with one-dimensional density bounded by one. No Gaussianity, log-concavity, moment, compact-support, connected-support, post-rotation independence, arbitrary-joint coarea, pointwise van-der-Corput estimate, or deletion of a small quadratic tail is used.

Fresh prepublication control was resolved at

`yspennstate/math-research-brain@67340898014b6d913e553869c3cf306b34b9ceef`,

with OWNER CONTROL revision `2026-09-22.15`, QFORM as the sole research target, and no pause on `account01/B08`. The live correction inbox was reread at that commit. In particular this argument does not use the refuted cross-minor-alone, local-cross-rank-three dichotomy, conditional-cap, arbitrary-joint coarea, post-rotation independence, pointwise quadratic-phase decay, Pluecker escape, or small-random-tail shortcuts.

## 1. Pinned mathematical inputs

### 1.1 Own r38 quantitative alignment decomposition

Source:

`yspennstate/math-open-problems@6691a29d20e3cfd119c67b7b6bc345c68f407712`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T234122Z-account01-B08-qform-r38/REPORT.md`.

For an orthonormal two-frame `U in R^(m x 2)`, with

`nu=max_i ||U_i||_2^2<1`,

and symmetric `H`, define the weighted leave-one-out alignment energy

`D_U(H)^2=sum_i (1-ell_i) dist(H[i,-i],row(U_-i^T))^2`,

where `ell_i=||U_i||_2^2`. Then there exist symmetric `R in R^(2x2)`, a physical diagonal `D_0`, and symmetric residual `F` with

`H=U R U^T+D_0+F`,

`||F||_F <= c_nu D_U(H)`,

`c_nu=sqrt(3/(1-nu))`.

At `nu<=1/48`,

`c_nu<=c_0:=12/sqrt(47)=1.7503798979747347...`.

### 1.2 Own r39 rigidity split

Source:

`yspennstate/math-open-problems@fce2b035e726fffd7cdbcbe6523a4193aa1a216b`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260924T003741Z-account01-B08-qform-r39/REPORT.md`.

For the spectral tail `E=E^T` satisfying the exact identity `EU=0`, diagonalize the carrier coefficient `R` as `O^T R O=diag(r_1,r_2)`, set `Delta=|r_1-r_2|`, and write rows of `UO` as `(x_i,y_i)`. Then

`Delta^2 sum_i x_i^2 y_i^2/(x_i^2+y_i^2) <= ||FU||_F^2`,

and with `r=(r_1+r_2)/2`,

`||E-(r U U^T+D_0)||_F <= ||F||_F+Delta/sqrt(2)`.

The r39 quantitative split used

`g(d)=sqrt(2 c_0 d)`, `d=D_U(E)/L`:

if `Delta/L<=g(d)`, the scalar-carrier approximation is at most

`[sqrt(c_0 d)+c_0 d]L`;

if `Delta/L>g(d)`, the frame is close to a two-column orthonormal frame with disjoint ORIGINAL-coordinate supports.

### 1.3 Designated partner account02/B08 r29

Completed source:

`yspennstate/math-open-problems@175ed537ecbeabeb27e98b49030c9b8ca846c5d7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260923T2307Z-auto11/REPORT.md`.

Its exact compound identity is

`Xi(M,S)=[s_1(M)s_2(M)]^2 D_M(S)^2`.

For the actual pair used here,

`M=U^T`, `S=E`,

both singular values of `U^T` equal one, its physical arm leverages are `ell_i=||U_i||^2`, and the leave-one-out row spaces agree with the definition of `D_U`. Therefore the completed partner identity gives the literal equality

`boxed: Xi(U^T,E)^(1/2)=D_U(E).`                        (1.1)

This algebraic identity is the designated-partner result actually applied below. I do **not** relabel `U^T` as two physical hub coordinates and do not import the partner's physical-hub density corollary outside its scope.

The newer account02/B08 Fresnel--Strichartz file `B08-20260923T234130Z-auto11b/EARLY_CALC.md` was also checked. It is explicitly an early calculation without a completed report, so it is **not** used as a premise here.

## 2. New theorem — carrier and diagonal cannot cancel arbitrarily

### Theorem `QFORM-SPECTRALTAIL-CARRIER-CONTRACTION-v1`

Let

`U in R^(m x r)`, `U^T U=I_r`,

and put

`nu=max_i ||u_i||_2^2<1`,

where `u_i^T` is row `i` of `U`. Let `E=E^T` satisfy the exact spectral orthogonality

`E U=0`.                                                       (2.1)

Suppose one has **any** decomposition

`E=U R U^T+D+F`,                                               (2.2)

where `R=R^T`, `D=diag(d_i)` is physical diagonal, and `F=F^T`. Define

`epsilon=||E||_op`, `delta=||F||_op`.

Then

`boxed: (1-nu)||R||_op <= epsilon+2 delta`,                    (2.3)

and

`boxed: (1-nu)||D||_op <= epsilon+(1+nu) delta`.               (2.4)

For `r=2`, if `Delta` is the eigenvalue gap of `R`, then also

`boxed: Delta <= 2(epsilon+2 delta)/(1-nu)`.                   (2.5)

If `delta_F=||F||_F`, then

`boxed:
 ||E-diag(E)||_F
 <= sqrt(r) [epsilon+2 delta_F]/(1-nu)+delta_F.`                (2.6)

The point of (2.3)-(2.4) is that a small spectral tail `E` cannot be represented as a huge diffuse carrier plus a huge physical diagonal which cancel only after summation, unless the actual non-aligned residual `F` is comparably large. This is exactly the cancellation freedom left uncontrolled by r38-r39.

### Proof

Since `EU=0`,

`0=U^T E U=R+U^T D U+U^T F U`.                                (2.7)

Taking the physical diagonal of (2.2) gives for every `i`

`d_i=E_ii-u_i^T R u_i-F_ii`.                                  (2.8)

Substituting (2.8) into `U^TDU=sum_i d_i u_i u_i^T`, define

`T(R):=sum_i (u_i^T R u_i) u_i u_i^T`.

Equation (2.7) becomes the exact identity

`R-T(R)
 =-sum_i E_ii u_i u_i^T
  +sum_i F_ii u_i u_i^T
  -U^T F U`.                                                   (2.9)

For every unit vector `z in R^r`,

`|z^T T(R) z|
 <= ||R||_op sum_i ||u_i||^2 (u_i^T z)^2
 <= nu ||R||_op sum_i (u_i^T z)^2
 =nu ||R||_op`,                                                (2.10)

because `sum_i u_i u_i^T=I_r`. Thus

`||T(R)||_op<=nu ||R||_op`.                                    (2.11)

Also `|E_ii|<=epsilon`, so, using again `sum_i u_i u_i^T=I_r`,

`||sum_i E_ii u_i u_i^T||_op<=epsilon`.                        (2.12)

Likewise

`||sum_i F_ii u_i u_i^T||_op<=delta`,

and

`||U^T F U||_op<=delta`.                                       (2.13)

Taking operator norms in (2.9) and using (2.11)-(2.13),

`||R||_op<=nu||R||_op+epsilon+2delta`,

which proves (2.3).

From (2.8),

`|d_i|<=epsilon+nu||R||_op+delta`.

Insert (2.3):

`|d_i|
 <=epsilon+delta+nu(epsilon+2delta)/(1-nu)
 =[epsilon+(1+nu)delta]/(1-nu)`.

Taking the maximum proves (2.4). For symmetric `R`, the gap between any two eigenvalues is at most `2||R||_op`, giving (2.5).

Finally, because `D` is diagonal,

`E-diag(E)=offdiag(U R U^T+F)`.

Deleting a diagonal can only decrease Frobenius norm, hence

`||E-diag(E)||_F
 <=||U R U^T||_F+||F||_F
 =||R||_F+delta_F
 <=sqrt(r)||R||_op+delta_F`.

Use `delta<=delta_F` in (2.3) to obtain (2.6). QED.

## 3. Actual application of the partner compound currency

Now return to the actual B08 spectral tail from r38. It has `r=2`, and r38 supplies a decomposition (2.2) with

`||F||_F<=c_nu D_U(E)`.

Apply the completed partner identity (1.1):

`D_U(E)=Xi(U^T,E)^(1/2)`.

Therefore (2.3)-(2.4) become the intrinsic compound inequalities

`boxed:
 ||R||_op
 <= [||E||_op+2 c_nu Xi(U^T,E)^(1/2)]/(1-nu),`                (3.1)

`boxed:
 ||D||_op
 <= [||E||_op+(1+nu)c_nu Xi(U^T,E)^(1/2)]/(1-nu).`            (3.2)

This is an inequality-level use of the designated partner theorem: the partner's three-volume compound currency now directly controls the amount of carrier/diagonal cancellation allowed by the exact spectral equation `EU=0`.

## 4. Concrete current B08 constants

Use the current diffuse deletion scales

`nu<=1/48`,

`epsilon=||E||_op=s_3(C)<=L/130`,

and, purely as the current inherited small-alignment benchmark,

`d:=D_U(E)/L<=eta`,

`eta=0.0037987340155334467`.

This value is the `eta_619` alignment scale appearing in the completed partner r29 report. Here it is used only as a quantitative benchmark for `D_U(E)`; no physical-hub density conclusion is imported for `M=U^T`.

Since

`c_0=12/sqrt(47)=1.7503798979747347...`,

r38 gives

`||F||_F/L<=c_0 eta=0.006649227658542589...`.                  (4.1)

The new theorem gives

`boxed: ||R||_op <0.0214373749883162 L`,                       (4.2)

`boxed: ||D||_op <0.0147881473297736 L`,                       (4.3)

and hence

`boxed: Delta<0.0428747499766323 L`.                           (4.4)

Moreover

`boxed:
 ||E-diag(E)||_F
 <0.0369662541086971 L.`                                       (4.5)

Thus the r39 normal form cannot hide coefficients of arbitrary size behind cancellation: at the current small-alignment scale the entire carrier coefficient is below `0.02144L`, the entire physical diagonal coefficient below `0.01479L`, and the physical off-diagonal Frobenius mass of the tail below `0.03697L`.

These are coefficient statements only; (4.5) is **not** used to delete the tail from the random quadratic phase.

## 5. The r39 two-bank alternative is confined to a much thinner alignment layer

The new gap estimate materially sharpens r39's normal-form split. Put

`x=1/130`,

and for `d=D_U(E)/L` define

`barDelta(d)=2[x+2 c_0 d]/(1-1/48)`,                            (5.1)

`g(d)=sqrt(2 c_0 d)`.                                          (5.2)

By (2.5),

`Delta/L<=barDelta(d)`.

The equation `barDelta(d)=g(d)` has the two positive roots

`d_-=7.544307417596869*10^(-5)`,

`d_+=0.0639984260192407`.                                      (5.3)

The checker beside this report verifies the exact quadratic arithmetic. Since

`d_-<eta<d_+`,

for every

`boxed: d_- <= D_U(E)/L <= eta`,                               (5.4)

one automatically has

`Delta/L<=g(d)`.

Therefore the **near-disjoint two-bank branch of r39 is impossible throughout (5.4)**: every such state lies in r39's scalar-carrier branch. In particular,

`||E-(r U U^T+D_0)||_F
 <=[sqrt(c_0 d)+c_0 d]L
 <=0.0881920241432266 L`.                                      (5.5)

The only region in which r39's non-scalar/two-bank alternative can still occur below the inherited alignment scale is now

`boxed: 0<D_U(E)<7.54431*10^(-5)L`.                            (5.6)

There r38 already gives the much stronger residual size

`boxed: ||F||_F<1.32054040479033*10^(-4)L`.                    (5.7)

This shrinks the possible non-scalar approximate-alignment layer by a factor exceeding fifty relative to `eta L`. At the exact endpoint `D_U(E)=0`, r38 already pays the full diffuse deletion branch by its exact carrier-plus-diagonal crossing theorem; no continuity-in-coefficients argument is asserted for the punctured layer (5.6).

## 6. Relation to the newest disjoint-bank localization result

During this run I also reread the newly posted account03/B14 theorem

`QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1`

at

`yspennstate/math-open-problems@e78cfe724f32f648f57e566922afd3b7d9cf9309`.

It gives a dimension-free density bound once three exact disjoint original-coordinate banks factor all active within-bank and exterior couplings. It is relevant to the tiny layer (5.6), because r39 makes the two carrier columns nearly disjoint there. I do **not** apply it yet: the deleted-hub transverse star and the remaining `F` need not factor through three exact disjoint banks. Treating near-disjoint support as exact would violate the product-preserving scope.

## 7. What is newly removed and what remains

Before this run, the r39 approximate-alignment branch allowed the normal-form pieces `URU^T` and `D_0` to be individually huge and cancel to leave the small true spectral tail `E`. That possibility is now excluded quantitatively by the exact spectral identity `EU=0`.

The first unpaid implication is now

`QFORM-CARRIER-CONTRACTION-RECEIVER-v1`:

1. **moderate alignment** `d_-<=D_U(E)/L<=eta`: exploit the forced scalar-carrier normal form (5.5), while retaining its explicit nonzero residual and all conditioning-generated affine terms;
2. **ultra-small alignment** `0<D_U(E)/L<d_-`: exploit the near-disjoint original-coordinate bank geometry together with (5.7), or build a receiver genuinely stable to that residual without treating it as a small random perturbation;
3. retain the already-paid exact endpoint `D_U(E)=0` and the existing large-alignment/projected-crossing routers separately.

The full target is **OPEN**. No counterexample is claimed. The new result itself is deterministic coefficient geometry, so it proves neither an additional density branch nor continuity by itself.

## 8. Checks and integrity

`CHECKS.py` and `CHECKS.txt` beside this report verify the displayed constants and the two roots in (5.3); the output ends

`QFORM_B08_R40_CARRIER_CONTRACTION_CHECK_PASS`.

The proof is the exact algebra in Section 2; the finite computation is only a constant check.

Changed-file privacy review: the run directory contains mathematical text and deterministic constants only; no credentials, scheduler IDs, signed URLs, machine paths, or private source excerpts are included.

Repository use and native learned-memory ingestion remain different. Authenticated repository retrieval and use occurred, but no authenticated native receiver-memory ingestion was observed; execution remains `WITHOUT_VERIFIED_BRAIN`.
