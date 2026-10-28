SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T03:53:19Z.
attacking: phase-aware mixed-volume descent after the r39 absolute-TT* barrier; identify the exact two-line source transversality currency that a pair-log realignment can consume, and compare it with the bounded-projection zero-pivot receiver.

# account03/B16 r40 — two-line phase realignment and projection-bank compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T035319Z-account03-B16-QFORM-r40`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW QUANTITATIVE STRUCTURAL COMPILER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Regularity: the new pair-log branch proves absolute continuity and an essential density bound. Continuity is not claimed from this argument; full-target continuity remains OPEN.

## 1. Fresh source boundary and mechanism change


The live corrections are retained: no post-rotation independence, no law-uniform pointwise quadratic Fourier decay, no arbitrary-joint indefinite coarea bound, no conditional projection-height supremum inferred from a marginal projection cap, and no deletion of a small random quadratic term.

The immediate B16 predecessor is account03/B16 r39, which showed that order-one mixed Pluecker volume does not rescue the old absolute `int |Phi_J Phi_K|` TT* kernel. A fresh cross-check also found account01/B16's superseding supplement, commit `693038c0d6b33564a32bba0665e0b2b342236765`: its first conditional pair-log theorem was already contained in the earlier account01/B11 overlap-safe theorem, and it paid the r39 sharp barrier family by a special physical-pair realignment. I therefore do not repeat or claim novelty for that special family.

The analytic input used below is the completed account01/B11 theorem `QFORM-OVERLAP-SAFE-SQUARE-LOG-v1`, source

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T101016Z-account01-B11-QFORM-auto11/REPORT.md`.

For an independent cap-one pair with invertible indefinite coefficient block `B`, `D=|det B|`, `kappa=sigma_min(B)`, and a translated square remainder `d(W-a)^2+c` whose scalar source has density cap one, it gives

`||p||_infinity <= 8*2^(1/4) (D kappa |d|)^(-1/4).`          (1.1)

The completed zero-pivot trace theorem is used only for comparison in Section 5. The designated partner actually applied in Section 7 is account04/B16 r3, commit

`c1bf7fd07ac10b105686d96c96344a1a2274f5d9`,

theorem `QFORM-FRESH-OR-TRANSVERSE-PAIRCAP-DICHOTOMY-v1`.

## 2. Exact phase algebra for two source lines

Let `X,Y,W` be mutually independent real random variables with probability densities bounded by one. Let

`l_1=(a,b)`, `l_2=(c,d)`,
`Delta=ad-bc`,                                                     (2.1)

and assume

`lambda !=0`, `nu!=0`, `Delta!=0`.                               (2.2)

Consider the homogeneous three-source phase

`F = lambda (aX+bY)^2 + 2 nu W(cX+dY).`                           (2.3)

The point is that the two projected lines in `(X,Y)` need not be coordinate axes. Their determinant `Delta` is the exact phase-transversality currency.

Choose first the orientation `c!=0` and use the genuinely independent pair `(X,W)`, leaving `Y` as the square smoother. In the ordering `(X,W,Y)`, the coefficient matrix is

`M = [[lambda a^2, nu c,       lambda ab],
     [nu c,        0,          nu d],
     [lambda ab,   nu d,       lambda b^2]].`                    (2.4)

Its pair block and pair-to-remainder column are

`B_c=[[lambda a^2,nu c],[nu c,0]],`
`C_c=[lambda ab,nu d]^T`.                                        (2.5)

The pair is automatically indefinite because

`det B_c=-nu^2 c^2<0`.                                           (2.6)

A direct inverse calculation gives

`B_c^(-1) C_c
 = [d/c, lambda a(bc-ad)/(nu c^2)]^T`,                           (2.7)

and the exact scalar Schur remainder is

`lambda b^2-C_c^T B_c^(-1)C_c
 = lambda (ad-bc)^2/c^2
 = lambda Delta^2/c^2.`                                          (2.8)

Equivalently,

`det M=-lambda nu^2 Delta^2`.                                    (2.9)

Thus the mixed source-line determinant survives completion exactly as a genuine third square; it is not lost in the pair translation.

Define

`kappa_c
 :=sigma_min(B_c)
  =(sqrt(lambda^2 a^4+4nu^2c^2)-|lambda|a^2)/2.`                 (2.10)

The overlap-safe theorem (1.1), with pair `(X,W)` and square source `Y`, yields

`||p_F||_infinity
 <=8*2^(1/4)
   [ |lambda| nu^2 Delta^2 kappa_c ]^(-1/4).`                    (2.11)

All factors `c^2` cancel between `|det B_c|` and the Schur-square coefficient. The only residual orientation cost is the true pair conditioning `kappa_c`.

If instead `d!=0`, choosing the pair `(Y,W)` gives

`kappa_d
 :=(sqrt(lambda^2 b^4+4nu^2d^2)-|lambda|b^2)/2`          (2.12)

and the analogous bound with `kappa_d`. Since `Delta!=0`, at least one of `c,d` is nonzero.

### Theorem 2.1 — `QFORM-TWOLINE-PHASE-REALIGNMENT-v1`

Under (2.1)-(2.3), put

`kappa_*:=max(kappa_c,kappa_d)`,                                  (2.13)

with a zero entry omitted if the corresponding coefficient `c` or `d` vanishes. Then `F` has an absolutely continuous law and

`boxed:
 ||p_F||_infinity
 <=8*2^(1/4)
   [ |lambda| nu^2 Delta^2 kappa_* ]^(-1/4).
`                                                                    (2.14)

This is a structural compiler around the already-proved overlap-safe analytic theorem. Its new content is the exact general two-line completion (2.7)-(2.9) and the quantitative orientation optimization (2.13), extending the special `(X+Y),(X-Y)` realignment in the account01/B16 supplement to arbitrary source-line angle.

## 3. Uniform normalized corollary

Assume now

`a^2+b^2=c^2+d^2=1`,
`|lambda|>=1`, `|nu|>=1`,                                        (3.1)

and write `delta=|Delta|`.

At least one of `|c|,|d|` is at least `1/sqrt(2)`. Suppose it is `|c|`; the other case is identical. For

`x=|lambda|a^2`, `y=|nu c|`,

`kappa_c=2y^2/(sqrt(x^2+4y^2)+x)`.                               (3.2)

More usefully,

`|lambda| kappa_c
 =2y^2/[sqrt(a^4+4y^2/|lambda|^2)+a^2].`                         (3.3)

The right side is increasing in `|lambda|` and in `y`, and decreasing in `a^2`. Hence under (3.1) and `|c|>=1/sqrt(2)`,

`|lambda| kappa_c
 >=(sqrt(3)-1)/2
 =0.3660254037844386... .`                                       (3.4)

Since `nu^2>=1`, Theorem 2.1 gives

### Corollary 3.1 — normalized phase-angle receiver

`boxed:
 ||p_F||_infinity
 <= C_phase delta^(-1/2),
 C_phase
 =8*2^(1/4)[(sqrt(3)-1)/2]^(-1/4)
 =12.231217212260074... <12.232.
`                                                                    (3.5)

Thus an arbitrarily small source-line angle costs only `delta^(-1/2)` through pair-log realignment.

## 4. Disjoint product-bank projection corollary

The same calculation can consume actual bounded-density projections, rather than literal coordinates.

Let `I,J,K` be disjoint ORIGINAL-coordinate banks. Let

`X=u^T X_I`, `Y=v^T X_J`, `W=w^T X_K`,                           (4.1)

where `||u||=||v||=||w||=1`. The three scalars are genuinely independent because their source banks are disjoint. The sharp one-dimensional product-projection theorem gives

`||p_X||_infinity, ||p_Y||_infinity, ||p_W||_infinity <=sqrt(2).` (4.2)

Therefore

`X'=sqrt(2)X`, `Y'=sqrt(2)Y`, `W'=sqrt(2)W`                       (4.3)

are independent cap-one scalar laws. In the primed variables, (2.3) has

`lambda'=lambda/2`, `nu'=nu/2`,                                  (4.4)

with the same unit line vectors and the same `delta`.

If `|lambda|,|nu|>=1`, the same monotonicity calculation as in Section 3, now with `|lambda'|,|nu'|>=1/2`, gives

`|lambda'|(nu')^2 kappa_*'
 >=(sqrt(3)-1)/32.`                                               (4.5)

Hence:

### Corollary 4.1 — `QFORM-THREEBANK-TWOLINE-PROJECTION-PAIRLOG-v1`

For the source-valid three-bank packet (4.1), with the phase (2.3), unit line vectors, `|lambda|,|nu|>=1`, and `delta=|ad-bc|>0`,

`boxed:
 ||p_F||_infinity
 <=C_bank delta^(-1/2),
 C_bank
 =8*2^(1/4)[(sqrt(3)-1)/32]^(-1/4)
 =24.462434424520147... <24.463.
`                                                                    (4.6)

This is a direct projection-product interaction theorem: the scalar projection caps are used only on disjoint original-coordinate banks, and the nonlinear pair-log/square integration is then performed before any source dependence is collapsed. No independence of coordinates inside a multidimensional rotated projection is asserted.

## 5. Dual zero-pivot receiver and the angle crossover

For the literal cap-one scalar version in Section 2, the invertible map

`(X,Y) -> (L,V)=(cX+dY,aX+bY)`                                    (5.1)

has Jacobian `|Delta|`. Therefore its exact joint density obeys

`||p_(L,V)||_infinity <= |Delta|^(-1).`                           (5.2)

Treating `W` as the fresh zero-pivot scalar and applying the completed zero-pivot conditional trace theorem to

`F=2nu W L+lambda V^2`                                           (5.3)

gives the distinct estimate

`||p_F||_infinity
 <= C_0 |Delta|^(-2/3)|nu^2 lambda|^(-1/3),
 C_0=3*2^(2/3)=4.762203155904598... .`                            (5.4)

For normalized unit lines and `|lambda|,|nu|>=1`, the two source-preserving mechanisms therefore give the envelope

`||p_F||_infinity
 <=min(4.762204 delta^(-2/3), 12.231218 delta^(-1/2)).`            (5.5)

The pair-log realignment becomes quantitatively better in the very small-angle regime

`delta < delta_* :=(C_0/C_phase)^6
 =0.003483609274615295... .`                                     (5.6)

This is useful for the current mixed-volume programme because it separates two different losses: a projection-height/Jacobian loss `delta^(-2/3)` and an indefinite-pair plus Schur-square loss `delta^(-1/2)`. The latter is the correct route to try when the phase lines become nearly parallel.

This comparison does **not** claim that a bounded projected joint density alone controls a general indefinite quadratic pushforward. Equation (5.4) works because the fresh scalar enters as an actual zero pivot in the same common quadratic phase.

## 6. Relation to r39 and what is genuinely new here

For the r39 sharp barrier family, after conditioning/rearranging sources one gets the special line pair `(X+Y),(X-Y)`. Account01/B16's fresh supplement already pays that exact family by the earlier overlap-safe theorem, with a sharper constant `<7.588`; account02/B11 independently pays it by a zero-pivot physical trace with constant `3`. Those family closures are therefore source matches, not new claims of this run.

The new contribution here is instead the arbitrary-angle compiler (2.14), its exact determinant identity

`det M=-lambda nu^2(ad-bc)^2`,                                   (6.1)

the orientation-optimized `kappa_*`, and the dimension-free disjoint-product-bank consequence (4.6). This identifies a precise source quantity that a future phase-aware mixed-Pluecker extraction may target: not total mixed volume alone, but a source-separated two-line determinant together with one well-conditioned indefinite pair orientation.

## 7. Required designated-partner application at an actual inequality

Apply account04/B16 r3 `QFORM-FRESH-OR-TRANSVERSE-PAIRCAP-DICHOTOMY-v1` to five independent original cap-one variables

`H,Z_1,Z_2,Z_3,Z_4`.

Set

`L=(Z_1+Z_2-Z_3-Z_4)/2`,
`V=(Z_1+Z_2+Z_3+Z_4)/2`.                                        (7.1)

Their coefficient rows are orthonormal in `R^4`, and every normalized two-frame physical row leverage is exactly

`(1/2)^2+(1/2)^2=1/2.`                                          (7.2)

The partner transverse Gram is

`G=det Gram(ell,v)=1.`                                           (7.3)

For

`Q=2HL+V^2`,                                                     (7.4)

the partner theorem has `gamma=1`, `kappa=1`, `T=alpha=delta=0`, and gives the actual full-line inequality

`boxed: ||p_Q||_infinity <=12 [G |gamma^2 kappa|]^(-1/3)=12.`     (7.5)

This is a strict owner-target packet: in the orthonormal carrier `(H,L,V)` the coefficient matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                    (7.6)

with eigenvalues `{-1,1,1}`. Thus all three nonzero eigenvalues have modulus one. The application uses the partner's genuine bounded-density projection theorem on the actual four-source two-frame, with the leverage gate checked exactly; it is not a generic citation.

## 8. First remaining B16 implication

The sharpened live target is now

`QFORM-MIXED-PLUECKER-TO-PHASE-LINE-CURRENCY-v1`:

> In the generic majority-sign near-coloop survivor, use the already-proved mixed Pluecker masses and the actual quadratic coefficient matrix to force either (i) disjoint original-source banks supporting two scalar projection lines with `|lambda|nu^2 Delta^2 kappa_*` bounded below, so Theorem 2.1/Corollary 4.1 pays the packet, or (ii) a genuinely cancellation-preserving TT*/Hilbert receiver. Total mixed volume without this phase alignment is not enough, by r39.

The new theorem shows exactly what must be extracted in branch (i). It does not yet prove that the generic mixed-volume packet always contains such a source partition, and it does not address arbitrary additional nonseparable spectrum. Therefore the full QFORM conjecture remains OPEN.

## 9. Verification and scope

`CHECK.py` verifies the determinant/Schur identities symbolically and the constants numerically. `CHECK_OUTPUT.txt` records `STATUS=PASS`.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or spectral-coordinate-independence assumption is used. No Monte Carlo claim is used. Continuity is not proved by the new branch; only absolute continuity plus an essential density bound are claimed.
