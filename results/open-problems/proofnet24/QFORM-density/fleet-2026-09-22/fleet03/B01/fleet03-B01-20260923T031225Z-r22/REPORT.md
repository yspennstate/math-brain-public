SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T03:12:25Z.
attacking: optimized signed-Fejer closure for the robust grouped 2+1 near-null branch, using the sharp two-dimensional product-projection cap and a scale-normalized split.

# fleet03/B01 r22 — optimized averaged-frequency payment for the robust grouped 2+1 packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE TARGET-LEVEL BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, live correction boundary, and source pins

The unrestricted target remains open: for every dimension, arbitrary independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal finite essential bound on the density of `Q=X^T A X`, or give a target-valid counterexample. No moments, compact support, connected support, log-concavity, Gaussianity, identical-law assumption, or independence after spectral rotation is used. Continuity is tracked separately.

This run preserves the source corrections. In particular:

* there is no law-uniform pointwise `|t|^{-1/2}` Fresnel bound for arbitrary cap-one one-dimensional laws;
* general rotations do not preserve input independence;
* a two-dimensional projection-density cap alone does not control an arbitrary nonlinear indefinite pushforward unless the additional transverse resource required below is retained;
* an absolute-Wiener `L^1` characteristic-function obligation is stronger than the target and can fail even when the output density is bounded.

The immediate structural/analytic predecessor is fleet03/B19 r21,

`yspennstate/math-open-problems@207a77337f6b3587233055160a27b317b2491342`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T010143Z-fleet03-B19-QFORM-r21/REPORT.md`.

The near-null analytic input is fleet01/B16
`QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`,

`yspennstate/math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T003846Z/REPORT.md`.

The nonzero-pivot fractional input is
`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`,

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

The designated partner fleet04/B01 signed-Fejer theorem used in Section 6 is

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

The current Claude synthesis has checked the Livshyts--Paouris--Pivovarov product-marginal theorem in the needed scope: an orthogonal two-dimensional marginal of a product of cap-one one-dimensional densities has joint density at most `2`. This is a joint-density bound, not independence of the projected coordinates.

## 2. Structural packet inherited from fleet03/B19 r21

The B19 predecessor produces, in its robust grouped exact-rank-three O3 chamber, two disjoint original-coordinate source banks. After the source-valid normalization one has:

1. a scalar `X_0` with probability density at most one;
2. a two-dimensional random vector

   `Z=U^T X_G`, `U^T U=I_2`,

   which is an orthogonal projection of an independent cap-one original-coordinate bank `X_G`;
3. genuine independence between `X_0` and the full pair `Z`, because their source banks are disjoint;
4. after conditioning every unused original coordinate, an active quadratic-plus-affine polynomial whose quadratic matrix is

   `B=[[a,b^T],[b,C]]`,

   with

   `s:=s_min(B)>=1/12`, `D:=|det B|>=1/12`.                    (2.1)

The outside conditioning creates only deterministic affine and constant terms in `(X_0,Z)`. Both analytic inputs used below are uniform in those affine terms, so the conditional estimate can be averaged back without any worst-fiber density assertion.

The B19 derivation bounded the joint density of `Z` by `e` using an internal affine-fiber theorem. Because here `U^TU=I_2`, the sharper checked two-dimensional product-marginal theorem applies directly:

`boxed: ||p_Z||_infinity <=2.`                                  (2.2)

This is the first quantitative improvement in the present run.

## 3. A scale-normalized two-envelope compiler

Write

`r=|a|/s`.                                                       (3.1)

### 3.1 Near-null envelope

Assume `0<=r<1`. The scale-correct transverse-resource lemma proved in B19 r21 says that, after rotating only inside the receiver plane so that `b=(beta,0)` and writing the transverse diagonal entry as `e`,

`P:=beta^2 |e| >=(1-r)D`.                                      (3.2)

No rotation mixes the independent scalar with the receiver pair.

Fleet01/B16 proves, for a cap-one independent scalar and a two-dimensional receiver with joint density cap `M_2`,

`||p_Q||_infinity
 <=103680^(1/3) M_2^(2/3)(DP)^(-1/6)`.                         (3.3)

Using (2.2), (3.2), and `D>=1/12`,

`||p_Q||_infinity
 <=N_0(1-r)^(-1/6)`,                                           (3.4)

where

`N_0:=103680^(1/3) 2^(2/3)12^(1/3)`.                          (3.5)

The envelope (3.4) is increasing in `r`. It includes the exact null value `a=0` without division by the pivot.

### 3.2 Nonzero-pivot envelope

Assume `a!=0`. Complete the square only in the genuinely independent physical scalar `X_0`. If

`S=C-bb^T/a`,                                                   (3.6)

then

`|det S|=D/|a|`.                                                (3.7)

The cap-one scalar square kernel gives, uniformly in the output translation,

`p_Q(t)
 <=|a|^(-1/2)
   E|Z^T S Z + ell^T Z+c-t|^(-1/2)`.                           (3.8)

Because `Z=U^T X_G` is an actual two-dimensional orthogonal projection of the untouched product bank, the sharper in-range case of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` applies:

`sup_t E|Z^T S Z+ell^T Z+c-t|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)`.                                 (3.9)

Combining (3.7)--(3.9),

`||p_Q||_infinity
 <=16sqrt(30)|a|^(-1/4)D^(-1/4)`.                              (3.10)

Since `|a|=rs`, `s>=1/12`, and `D>=1/12`,

`||p_Q||_infinity
 <=F_0 r^(-1/4)`,                                              (3.11)

where

`F_0:=16sqrt(30)sqrt(12)=96sqrt(10)`.                           (3.12)

The envelope (3.11) is decreasing in `r` and is valid for every `r>0`, including `r>=1`.

Thus the dependence-safe proof has reduced this whole grouped packet to the minimum of two complementary scalar envelopes, without a false pointwise oscillatory estimate:

`near(r)=N_0(1-r)^(-1/6)` for `0<=r<1`,

`far(r)=F_0 r^(-1/4)` for `r>0`.                               (3.13)

## 4. Exact rational split gives a clean universal constant 306

Choose the rational threshold

`r_0=4849/5000=0.9698`.                                        (4.1)

If `0<=r<=r_0`, use the increasing near envelope:

`||p_Q||_infinity
 <=N_0(1-r_0)^(-1/6)<306`.                                    (4.2)

This inequality is certified by exact integer arithmetic. From (3.5),

`N_0^3=103680*4*12=4,976,640`,                                 (4.3)

while

`1-r_0=151/5000`.                                              (4.4)

Taking sixth powers, (4.2) is equivalent to

`4,976,640^2 *5000 <306^6 *151`,                               (4.5)

and the two integers are

`123834728448000000 <123966832950161856`.                      (4.6)

If `r>=r_0`, then `a!=0`, so use the decreasing far envelope:

`||p_Q||_infinity
 <=96sqrt(10) r_0^(-1/4)<306`.                                 (4.7)

Taking fourth powers, this is equivalent to

`96^4 *100*5000 <306^4 *4849`,                                 (4.8)

namely

`42467328000000 <42514579705104`.                              (4.9)

The exact checker in this run records both positive margins.

### Theorem 4.1 — `QFORM-GROUPED-2PLUS1-OPTIMIZED-v1`

Every robust grouped `1+2` packet satisfying the source-valid hypotheses of fleet03/B19 r21, hence in particular (2.1), has for every admissible cap-one product input law and every affine perturbation generated by outside original-coordinate conditioning

`boxed: ||p_Q||_infinity <306.`                                (4.10)

All signatures are allowed. The exact null scalar pivot belongs to the near envelope; every nonzero pivot is covered by at least the far envelope. No moment or support assumption enters. This improves the predecessor's `<362` bound on the same structural packet and removes its arbitrary `|a|=1/24` split.

The mechanism is quantitative rather than cosmetic: it spends the full sharp two-dimensional product-marginal cap and balances the null-safe cross-transverse resource directly against the orientation-free rank-two half-Riesz estimate.

## 5. Why this remains compatible with the oscillatory corrections

The phase-aligned counterexample remains untouched. For any prescribed `s!=0` and sufficiently small `delta>0`, the set

`E(s,delta)={x: dist(sx^2,2pi Z)<=delta}`

has infinite Lebesgue measure. Choose a measurable subset `E` of measure one and take `f=1_E`. Then

`Re int exp(isx^2)f(x)dx >=cos(delta)`.                         (5.1)

Hence no uniform positive pointwise power decay can hold over all cap-one one-dimensional laws. Nothing in Sections 2--4 assumes such decay. The near estimate is a direct density/small-ball transducer with a geometric determinant resource, while the far estimate uses a translation-uniform fractional potential. Both retain original-coordinate product provenance.

The argument also does not require `int |phi_Q(t)|dt<infinity`. This matters because the live correction ledger contains bounded-density examples whose characteristic functions fail the absolute-Wiener criterion.

## 6. Assigned fleet04/B01 result applied to the actual new inequality

The designated partner fleet04/B01 proves the exact signed-Fejer equivalence. For a probability law `mu`, define

`D_T mu(y)
 =(1/(2pi)) int_{-T}^T (1-|t|/T)
   Re(exp(-ity) muhat(t)) dt`.                                  (6.1)

Its theorem states that a bounded density satisfies

`||p_mu||_infinity = sup_{T>0,y in R} D_T mu(y)`,               (6.2)

with the converse implication as well.

Apply (6.2) to the new bound (4.10). On the entire robust grouped `1+2` packet,

`boxed:
 sup_{T>0,y in R} D_T law(Q)(y) <306.`                          (6.3)

This is an actual frequency-averaged inequality for a current no-pivot/exact-rank-three survivor. It is signed and phase-sensitive; it is neither a hidden pointwise Fresnel estimate nor an absolute Fourier `L^1` estimate.

## 7. Continuity and exact scope

Theorem 4.1 proves absolute continuity and an **essentially bounded** density. A continuous representative is **not proved by this assembly**. The near-null fleet01/B16 theorem supplies essential boundedness, and the signed-Fejer identity does not upgrade that by itself. This is recorded separately from the height bound.

The full QFORM conjecture is still open. The structural packet used here is an exact-rank-three grouped O3/N3 subbranch produced by fleet03/B19. What remains globally includes, in particular:

1. the product-preserving structural routing of every remaining strict N3 state into a paid packet;
2. the splice from exact-rank-three core arguments to arbitrary additional spectrum without treating a small matrix tail as a uniformly small random quadratic perturbation on unbounded inputs;
3. the remaining concentrated-volume/high-leverage states not covered by the current grouped packet.

So (4.10) is a quantitative branch closure, not a declaration of the full theorem.

## 8. Arithmetic and reproducibility

Files in this immutable run directory:

* `CHECKPOINT.md` — the early substantive derivation;
* `CHECK.py` — exact rational/integer verification of the threshold;
* `CHECK_OUTPUT.txt` — actual in-run arithmetic output;
* `REPORT.md` — this proof.

The check terminates

`QFORM_B01_R22_EXACT_SPLIT_CHECK_PASS`.

The integer check is only arithmetic verification of Section 4; the mathematical proof is Sections 2--6.

## 9. First unpaid implication for B01

The next oscillatory obligation is not to improve `306` marginally. It is to derive a **signed-Fejer / fractional-potential payment before structural localization** for a remaining concentrated-volume N3 state, preferably one in which the third exterior mass is pinned to an opposite-side row/column star. The correct object should aggregate the star mass before paying a reciprocal local coefficient, or else route the concentrated volume to an already-paid mixed-hub/grouped-source theorem. The law-uniform pointwise phase envelope remains forbidden.
