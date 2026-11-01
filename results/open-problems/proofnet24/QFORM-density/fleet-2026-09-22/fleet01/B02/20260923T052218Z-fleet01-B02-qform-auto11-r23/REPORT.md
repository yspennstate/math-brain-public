SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T05:22:18Z.
attacking: integrated Fourier estimate — combine the designated fleet02/B02 three-sample volume compiler and its endpoint stability theorem with the exact-rank-three physical cross-block Fourier theorem, in order to remove the previous h<3/4 volume-marginal barrier.

# fleet01/B02 r23 — every non-coloop third-volume cross block has an explicit L1 Fourier bound

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Partner:** `fleet02/B02`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.  
**Continuity:** proved on the new physical-cross-block branch below; full-target continuity remains open.

The full target is unchanged: independent real coordinates with probability densities at most one and a real symmetric matrix with at least three eigenvalues of absolute value at least one. No moment, Gaussian, log-concavity, support, diagonal-basis, or post-rotation-independence assumption is introduced.

## 1. Source results actually used

### 1.1 Designated partner fleet02/B02

I apply the completed partner result

`QFORM-TRIPLE-DISJOINT-VOLUME-COMPILER-v1`

from

`yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T050831Z-fleet02-B02-QFORM-auto11-f98b4bb5/REPORT.md`.

Let `M=A[I,J]` be an ORIGINAL-coordinate physical cross block, let

`Z=E3(M)=e3(M^T M)>0`,

and let `mu` be the row-triple marginal of the determinant-squared three-volume law. If `R1,R2,R3` are iid with law `mu`, put

`delta3=P(R1 cap R2 cap R3=empty)`.

The partner proves that if `delta3>0`, then the full quadratic form (with arbitrary same-bank phases and outside couplings retained) has an integrable characteristic function and

`||p_Q||inf <= (9 sqrt(3)e/2) delta3^(-1/6) Z^(-1/6)`.       (1.1)

Tracking the same integrable envelope used in that proof gives

`int_R |phi_Q(t)| dt
 <= 9 pi sqrt(3)e delta3^(-1/6) Z^(-1/6)`.                   (1.2)

The same partner run proves the quantitative endpoint theorem `QFORM-TRIPLE-INTERSECTION-STABILITY-v1`. If

`h=max_i P_mu(i in R)`,

fix `0<eps<1`, define

`eta=delta3/eps`,
`tau=eta/[2(eps-eta)^2]`,

and assume `eta<eps`, `tau<=1/2`. Then either a row has inclusion probability greater than `1-eps` (equivalently its deletion leaves less than `eps Z` third volume), or, when `h<=1-eps`, there is a set `H` of at most four physical rows with

`E3(M[H,J]) >= (1-rho)Z`,
`rho=eta+5tau`.                                               (1.3)

This is an aggregate statement; no individual tiny minor has been inverted.

### 1.2 Exact-rank-three Fourier theorem

I also use the completed theorem `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1` from

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T230126Z-fleet03-B02-QFORM-r17/REPORT.md`.

If an ORIGINAL-coordinate cross block `C` has exact rank three and the product of its three nonzero singular values is `Gamma`, then, with all same-bank quadratic terms and outside couplings arbitrary,

`int_R |phi_Q(t)|dt <=12 pi Gamma^(-1/3)`,
`||p_Q||inf <=6 Gamma^(-1/3)`,                                (1.4)

and the density is continuous and vanishes at infinity.

No projected-coordinate independence is asserted in either source theorem.

## 2. New four-row closure lemma

### Lemma 2.1 — `QFORM-FOURROW-VOLUME-TO-EXACTRANK3-v1`

Suppose a physical cross block `M=A[I,J]` has `Z=E3(M)>0` and some set `H subset I`, `|H|<=4`, satisfies

`E3(M[H,J]) >= theta Z`,                                      (2.1)

for `theta>0`. Then the full quadratic form has an integrable characteristic function and

`int_R |phi_Q(t)|dt <=12 pi (4/(theta Z))^(1/6)`,             (2.2)

`||p_Q||inf <=6 (4/(theta Z))^(1/6)`.                         (2.3)

In particular the density is continuous and vanishes at infinity.

#### Proof

Cauchy--Binet, summed first over column triples, gives the exact row decomposition

`E3(M[H,J])
 = sum_{R subset H, |R|=3} det(M[R,J] M[R,J]^T)`.             (2.4)

There are at most four summands. Hence one physical row triple `R subset H` satisfies

`det(M[R,J]M[R,J]^T) >= theta Z/4`.                           (2.5)

The determinant is positive, so the 3-by-|J| ORIGINAL-coordinate block `C=M[R,J]` has exact rank three. Its nonzero singular-value product therefore obeys

`Gamma^2=det(CC^T)>=theta Z/4`.                               (2.6)

Apply (1.4) to the physical cut `R | J`, putting every other original coordinate, including `I\R`, into the outside bank. The exact-rank-three theorem explicitly permits all those outside couplings and arbitrary same-bank phases. Equations (2.2)--(2.3) follow. QED.

This lemma is the first essential missing implication from the partner's near-four-row alternative: concentration of aggregate third volume on four physical rows is already enough for a genuine unweighted L1 Fourier estimate. No coefficient-space rotation of the random inputs is used.

## 3. Main new theorem: any quantitative non-coloop is paid

### Theorem 3.1 — `QFORM-NONCOLOOP-THIRDVOLUME-L1-v1`

Let `M=A[I,J]` be any ORIGINAL-coordinate physical cross block with

`Z=E3(M)>0`.

Let `mu` be its determinant-squared row-triple law and set

`h=max_i P_mu(i in R)`.

If `h<1`, write

`eps=1-h in (0,1]`.                                           (3.1)

Then the full quadratic form has a continuous density vanishing at infinity and

`boxed{
 int_R |phi_Q(t)|dt
 <= 9 pi sqrt(3)e 6^(1/6) eps^(-1/2) Z^(-1/6)
 <179.449 eps^(-1/2) Z^(-1/6).
}`                                                               (3.2)

Consequently

`boxed{
 ||p_Q||inf
 <= (9 sqrt(3)e/2) 6^(1/6) eps^(-1/2) Z^(-1/6)
 <28.561 eps^(-1/2) Z^(-1/6).
}`                                                               (3.3)

Thus the old sharp-HY D' threshold `h<3/4` is removed completely: every fixed positive gap from an exact third-volume coloop gives a genuine unweighted integrated-Fourier bound. The quantitative price is only `(1-h)^(-1/2)`.

#### Proof

Let `delta3` be the partner's three-sample empty-common-intersection probability.

**Case 1: `delta3 >= eps^3/6`.** Apply the designated partner theorem (1.1)--(1.2):

`delta3^(-1/6) <= 6^(1/6) eps^(-1/2)`,                       (3.4)

which gives exactly (3.2)--(3.3).

**Case 2: `delta3 < eps^3/6`.** Apply the partner stability theorem with its parameter `epsilon` equal to the present `eps=1-h`. Since by definition `h=1-eps`, the theorem is in its four-row alternative, not its `h>1-eps` near-coloop alternative.

Its auxiliary parameters satisfy

`eta=delta3/eps < eps^2/6`,                                   (3.5)

and

`eps-eta > eps(1-eps/6) >=5eps/6`.                            (3.6)

Hence

`tau=eta/[2(eps-eta)^2]
 < (eps^2/6)/(2(25eps^2/36))
 =3/25`.                                                       (3.7)

Therefore

`rho=eta+5tau <1/6+3/5=23/30`,                                (3.8)

so some set `H` of at most four physical rows carries

`E3(M[H,J]) >(7/30)Z`.                                        (3.9)

Lemma 2.1 with `theta=7/30` gives

`int |phi_Q|
 <12pi(120/7)^(1/6) Z^(-1/6)
 <60.536 Z^(-1/6)`,                                           (3.10)

and

`||p_Q||inf
 <6(120/7)^(1/6) Z^(-1/6)
 <9.635 Z^(-1/6)`.                                            (3.11)

Since `eps<=1`, the right sides of (3.10)--(3.11) are smaller than the bounds asserted in (3.2)--(3.3). This completes both cases. QED.

## 4. Exact endpoint and qualitative all-rank>=3 cross-block theorem

The endpoint `h=1` is also paid, but by a different mechanism and with no blow-up.

If one row `i` belongs to every positive-volume row triple, then

`E3(M[I\{i},J])=0`,                                          (4.1)

so `rank M[I\{i},J]<=2`. Adding the single row `i` shows `rank M<=3`. Since `Z>0`, `rank M>=3`; hence `rank M=3`. For an exact-rank-three matrix,

`Gamma^2=E3(M)=Z`.                                            (4.2)

The exact-rank-three Fourier theorem therefore gives

`int |phi_Q| <=12pi Z^(-1/6)`,
`||p_Q||inf <=6 Z^(-1/6)`.                                   (4.3)

Combining this endpoint with Theorem 3.1 yields the following qualitative consequence.

### Corollary 4.1 — `QFORM-ANY-PHYSICAL-CROSSRANK3-L1-v1`

If **any** ORIGINAL-coordinate physical cross block `A[I,J]` has rank at least three, then

`phi_Q in L1(R)`

and the law of `Q` has a bounded continuous density vanishing at infinity.

No three-large-eigenvalue hypothesis is needed for this qualitative conclusion. The quantitative bound is (3.2) when `h<1`, and (4.3) when `h=1`.

This does **not** solve the owner's target because the constants in (3.2) depend on the block scale `Z` and on the coloop gap `1-h`, and exact-target families are known in which every physical cross cut has rank at most two. The result instead isolates the full Fourier obstruction more sharply: any remaining failure of a target-wide universal L1 estimate must come from quantitative degeneration toward a coloop/low-cross-rank geometry or from matrices whose relevant physical cuts never reach rank three at a universal scale.

## 5. Symmetric two-orientation form

The same theorem applies after transposing the cross block. Let `h_row` and `h_col` be the maximum third-volume marginals in the two orientations and set

`eps_* = max(1-h_row,1-h_col)`.                                (5.1)

If `eps_*>0`, choose the better orientation and obtain

`int |phi_Q|
 <=9pi sqrt(3)e 6^(1/6) eps_*^(-1/2) Z^(-1/6)`.              (5.2)

If `eps_*=0`, either orientation has an exact coloop and the rank-three endpoint argument applies. Thus a rank-at-least-three physical cross block is never a qualitative obstruction to absolute Fourier integrability; only uniform quantitative extraction remains.

## 6. Relation to the exact target and first unpaid implication

The full conjecture remains OPEN. No target-valid counterexample to the stronger target-wide statement

`int_R |E exp(it X^T A X)|dt <= C`

was found.

The new theorem closes the partner's `near four-row support` alternative completely and removes the previous fixed `h<3/4` Fourier barrier. The first unpaid implication is now

`QFORM-UNIFORM-COLOOP-SCALE-OR-LOW-CROSSRANK-CLOSURE-v1`:

starting only from the three-large-eigenvalue hypothesis, either extract a physical cross block for which

`Z^(1/6) sqrt(1-h)`

is bounded below by a universal constant (then Theorem 3.1 is a universal L1 certificate), or route the quantitative near-coloop / all-cross-rank-at-most-two geometry into the already-paid exact-rank-three, rank-two-affine, pair-log, grouped-square, grouped-bilinear, ridge, or mixed-hub mechanisms. One must aggregate before reciprocal minor payment; the live corrections rule out assuming a uniformly good fixed minor or post-rotation independence.

The theorem also records separately that continuity is proved on its cross-rank>=3 scope but remains open for the unrestricted target.

## 7. Correction audit

This argument uses no law-uniform scalar pointwise van-der-Corput estimate, no arbitrary-joint coarea bound, no conditional-density cap after a sum/difference transform, no post-rotation independence, no fixed-good-minor inference, and no deletion of a small dense coefficient tail. The only rotations appearing in the cited exact-rank-three theorem are used to analyze deterministic coefficient subspaces together with published product-marginal density bounds; independence is retained only in the original-coordinate banks.

The partner result is applied at the actual inequality `delta3 >= eps^3/6`; its stability theorem is applied at the complementary inequality `delta3 < eps^3/6`, and its four-row output is converted to the exact-rank-three L1 theorem via Lemma 2.1.

## 8. Status

- `QFORM-NONCOLOOP-THIRDVOLUME-L1-v1`: proved supporting theorem in this report.
- `QFORM-FOURROW-VOLUME-TO-EXACTRANK3-v1`: proved supporting lemma in this report.
- `QFORM-ANY-PHYSICAL-CROSSRANK3-L1-v1`: proved qualitative corollary in this report.
- Full universal bounded-density conjecture: OPEN.
- Full universal unweighted L1 characteristic-function bound: OPEN_NOT_REFUTED.
- Full-target continuity: OPEN; continuity is proved on the stated cross-rank>=3 scope.

MODEL: GPT-5.6 Sol. THINKING LEVEL: UNKNOWN / not exposed; maximum supported was requested. Provider reasoning-token and provider-thinking-time counters: NOT_EXPOSED. Brain status: WITHOUT_VERIFIED_BRAIN.
