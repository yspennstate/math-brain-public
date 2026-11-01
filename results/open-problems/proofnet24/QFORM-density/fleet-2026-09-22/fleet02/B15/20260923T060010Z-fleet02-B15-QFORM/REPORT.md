SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T06:00:10Z.
attacking: a quantitative rough-source L1-to-output C^{0,alpha} stability bridge for the live integrated-Fourier volume classes; independently preserve the ruled one-sheet bound through rough original-coordinate limits without using continuity for height.

# fleet02/B15 — quantitative rough-source stability and active-block-only ruled limiting

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Method:** complementary constructions / source-valid limiting tests  
**Partner:** fleet03/B15  
**Status:** `ESSENTIAL_STEP_APPLIED / ROUGH_VOLUME_Calpha_STABILITY / RULED_ACTIVE-BLOCK_LIMIT_CHECKED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted owner theorem remains OPEN. Absolute continuity itself is already paid for every nonzero symmetric `A`, but the universal height

`sup ||p_(X^T A X)||_infinity < infinity`

over all target matrices and arbitrary independent cap-one sources is still unpaid.

In the current proof map, volume-certified branches already obtain height directly from an integrable Fourier envelope. The precise B15 obligation is to justify passage from smooth/padded original-coordinate sources to arbitrary rough product laws without using output continuity as a surrogate for the height. This report gives a quantitative bridge: a common Fourier envelope turns source `L1` error into output `L-infinity` and `C^{0,alpha}` error. Separately, the ruled one-sheet theorem passes to rough inputs by total variation after smoothing only the three active ORIGINAL coordinates; it yields essential boundedness of that submeasure and no continuity claim.

## 2. Sources actually applied

Required Claude source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

I use two completed pieces from that source at equations below:

1. the determinant-volume Fourier route, whose relaxed D' gate gives an integrable power envelope when the row-volume marginals are below `3/4`; and
2. Theorem C, the rank-three signature `(2,1)` ruled one-sheet bound.

Current quantitative volume source:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Latest compatible assigned-partner result actually applied:

fleet03/B15 `20260923T052713Z-fleet03-B15-qform-auto13`, report blob
`4655d7ae48fdbf735d6637e2ccd43d8c68e2cd66`. It records that for the current original-coordinate volume branch

`|phi_Q(t)| <= min(1,K |t|^{-b})`,
`b=3/(2q)>1`,
`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q))`,
`Z=e3(M^T M)`,

and at `q=4/3`, `b=9/8`. It also compiles this into individual Holder regularity. The new result below is different: it controls the **difference of two output densities** in terms of the `L1` distance between their rough product sources, which is the missing quantitative limiting bridge.

## 3. General common-envelope source-stability theorem

Let

`F(x)=prod_i f_i(x)`, `G(x)=prod_i g_i(x)`

be two probability densities for the same measurable real-valued map `Q(x)`; in the application `Q` is the same quadratic-plus-affine form. Put

`Delta=||F-G||_1`.

For product laws,

`Delta <= min(2, sum_i ||f_i-g_i||_1)`                                      (3.1)

by telescoping.

Assume the two output characteristic functions obey the **same** envelope

`|phi_F(t)|, |phi_G(t)| <= min(1,K |t|^(-b))`, `b>1`.                       (3.2)

This is exactly the situation in the volume theorems: `K,b` are paid by the matrix/volume certificate, not by smoothness or support of the one-dimensional marginals.

### Theorem 3.1 — source L1 to output L-infinity

Under (3.1)-(3.2), both outputs have `C_0` densities and

`boxed{
 ||p_F-p_G||_infinity
 <= [b/(pi(b-1))] (2K)^(1/b) Delta^(1-1/b).
}`                                                                           (3.3)

#### Proof

Because the phase has modulus one,

`|phi_F(t)-phi_G(t)|
 <= int |F-G|
 = Delta`.                                                                   (3.4)

Also (3.2) gives

`|phi_F(t)-phi_G(t)| <= 2K |t|^(-b)`.                                       (3.5)

Hence

`|Delta phi(t)| <= min(Delta,2K |t|^(-b))`.                                 (3.6)

The right side is integrable for `b>1`. Put

`T=(2K/Delta)^(1/b)`

when `Delta>0`; the zero case is trivial. Direct integration yields

`int_R min(Delta,2K|t|^(-b)) dt`
` =2[Delta T + 2K T^(1-b)/(b-1)]`
` =2 Delta T * b/(b-1)`
` =2b/(b-1) (2K)^(1/b) Delta^(1-1/b)`.                                     (3.7)

Fourier inversion and the `1/(2pi)` factor give (3.3). Integrability of each individual envelope in (3.2) gives the `C_0` representatives directly; continuity is not used to infer (3.3). QED.

### Theorem 3.2 — source L1 to output Holder seminorm

For every

`0<alpha<min(1,b-1)`,                                                        (3.8)

one has

`boxed{
 [p_F-p_G]_(C^{0,alpha})
 <= [2^(1-alpha)/pi]
    [1/(alpha+1)+1/(b-alpha-1)]
    (2K)^((alpha+1)/b)
    Delta^(1-(alpha+1)/b).
}`                                                                           (3.9)

#### Proof

For `0<=alpha<=1`,

`|exp(-ith)-1| <= 2^(1-alpha)|t h|^alpha`.                                  (3.10)

Applying inversion to `Delta p=p_F-p_G` and using (3.6),

`[Delta p]_(C^{0,alpha})`
` <= 2^(1-alpha)/(2pi) * J`,                                                (3.11)

where

`J=int_R |t|^alpha min(Delta,2K|t|^-b)dt`.

At the same threshold `T`,

`J=2 Delta T^(alpha+1)
     [1/(alpha+1)+1/(b-alpha-1)]`.                                          (3.12)

Substitute `T=(2K/Delta)^(1/b)` into (3.11)-(3.12) to get (3.9). QED.

The exponents are positive exactly because `alpha<b-1`.

## 4. Current q=4/3 volume branch: explicit rough-source modulus

Apply the latest assigned-partner envelope with

`q=4/3`, `b=9/8`,

`K=e^(9/8)(4/3)^(-9/16) pi^(9/8) Z^(-3/16)`.                               (4.1)

Equation (3.3) simplifies exactly to

`boxed{
 ||p_F-p_G||_infinity
 <= (9 sqrt(3)e/2) 2^(8/9)
    Z^(-1/6) Delta^(1/9)
 <39.233 Z^(-1/6) Delta^(1/9).
}`                                                                           (4.2)

Thus the output height is Holder-stable of exponent `1/9` in the product-source `L1` metric on every fixed matrix branch carrying the current q=4/3 certificate.

Take now `alpha=1/16<b-1=1/8`. Equation (3.9) gives

`boxed{
 [p_F-p_G]_(C^{0,1/16})
 <= C_stab Z^(-17/96) Delta^(1/18),
}`                                                                           (4.3)

with

`C_stab
 =(288/17) 2^(271/144) e^(17/16)
   (4/3)^(-17/32) pi^(1/16)
 =166.5717485...`.                                                           (4.4)

This is stronger than merely knowing that every individual output is Holder: it gives a quantitative **rough-source convergence theorem**.

For the current near-diffuse certificate, `s3(M)>=15a/16` and hence

`Z=e3(M^T M)>=s1(M)^2 s2(M)^2 s3(M)^2 >=(15a/16)^6`                         (4.5)

when only the uniform lower bound by the third singular value is used. Therefore

`boxed{
 ||p_F-p_G||_infinity
 <41.849 a^(-1) Delta^(1/9),
}`                                                                           (4.6)

and

`boxed{
 [p_F-p_G]_(C^{0,1/16})
 <178.395 a^(-17/16) Delta^(1/18).
}`                                                                           (4.7)

All same-bank quadratic terms, outside couplings and affine terms retained by the current volume theorem remain present.

## 5. Precise rough-input limiting consequence

Let an arbitrary cap-one product source `F=prod f_i` lie in one of the volume-certified matrix classes above. Define original-coordinate Gaussian mollifications

`f_i^(eta)=f_i*gamma_eta`.

They remain probability densities with `||f_i^(eta)||_infinity<=1` and

`||f_i^(eta)-f_i||_1 ->0`.                                                   (5.1)

For fixed finite dimension,

`Delta_eta=||prod f_i^(eta)-prod f_i||_1
 <=sum_i ||f_i^(eta)-f_i||_1 ->0`.                                          (5.2)

The matrix volume certificate is unchanged by mollification, so the same `K,b` apply to every padded source and to the limit. Equations (4.2)-(4.3) imply

`||p_eta-p||_infinity ->0`,                                                  (5.3)

`[p_eta-p]_(C^{0,1/16}) ->0`.                                               (5.4)

If one starts from a proof of the envelope only for smooth inputs, (3.6) and dominated convergence give the same conclusion: product `L1` convergence implies `phi_eta(t)->phi(t)`, the common integrable envelope passes to the limit, and Fourier inversion identifies the limit law. Equivalently, total-variation convergence of the source products passes through the deterministic quadratic map, while uniform convergence on compact test functions identifies the uniform density limit.

Consequently a smooth theorem of the form `||p_eta||_infinity<=H` passes to the rough law with the **same** bound `||p||_infinity<=H`. This payment is obtained before and independently of the continuity statement. Continuity is an additional conclusion of the common integrable envelope / Holder convergence.

The required Claude D' route is a direct beneficiary: whenever its row-volume gate gives `b>1`, Theorems 3.1-3.2 make its original-coordinate Gaussian padding passage quantitative. In particular the `h=2/3` / `q=4/3` regime has the `Delta^(1/9)` height stability and, at `alpha=1/16`, `Delta^(1/18)` Holder stability (with the envelope constant of that version of D').

## 6. Independent check of the e5 ruled one-sheet rough bridge — smooth only the active triple

The completed e5 `COUNTEREXAMPLE_SEARCH.md` Theorem C treats the exact rank-three signature `(2,1)` form

`q(y)=lambda_1 y_1^2+lambda_2 y_2^2-mu y_3^2`,                              (6.1)

and on the majority side `s>=0` gives

`p_q(s) <= C_+(lambda_1,lambda_2,mu)`,                                      (6.2)

where

`C_+=(lambda_1 lambda_2 mu)^(-1/2)
     int_0^(2pi)
      [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2 dtheta`.       (6.3)

If all three eigenvalue magnitudes are at least `kappa`, then

`C_+<=pi sqrt(2)/kappa`.                                                     (6.4)

I recheck the rough ambient passage in a way that leaves every outside marginal untouched.

Let `S` be three **physical original coordinates** whose principal block `B` is invertible of signature `(2,1)`. Condition on all outside original coordinates `W=w`. The conditional form is

`Q_w(x_S)=x_S^T B x_S+2 d(w)^T x_S+c_0(w)`.                                 (6.5)

Completing the square gives

`Q_w(x_S)=(x_S+B^(-1)d(w))^T B (x_S+B^(-1)d(w))+c(w)`.                      (6.6)

The translation is in the original coordinates, so the three active variables remain independent and each translated density is still bounded by one. No independence after diagonalising `B` is asserted; Theorem C's product-projection argument is precisely what handles the rotated spectral geometry.

Now mollify only the active marginals:

`f_i^(eta)=f_i*gamma_eta`, `i in S`,                                        (6.7)

and leave the arbitrary rough outside law of `W` unchanged. Put

`delta_eta=||prod_(i in S) f_i^(eta)-prod_(i in S) f_i||_1
 <=sum_(i in S)||f_i^(eta)-f_i||_1 ->0`.                                    (6.8)

For each fixed `w`, translations in (6.6) preserve (6.8), hence the conditional active laws differ by at most `delta_eta` in `L1`, uniformly in `w`. Deterministic pushforward and restriction to the majority half-line

`[c(w),infinity)`                                                           (6.9)

cannot increase total variation. Thus the padded conditional majority submeasures `nu_(eta,w)^+` converge to `nu_w^+` in total variation uniformly in `w`.

For every interval `I`, Theorem C gives

`nu_(eta,w)^+(I) <= C_B |I|`,                                               (6.10)

`C_B=C_+(|eig(B)|)<=pi sqrt(2)/kappa`,                                      (6.11)

with no dependence on `w` or `eta`. Letting `eta->0` in the same measurable interval yields

`boxed{ nu_w^+(I) <= C_B |I| }`                                             (6.12)

for almost every `w`. Averaging over the completely unsmoothed outside law gives the ambient submeasure inequality

`boxed{
 P(Q in I, Q>=c(W)) <= C_B |I|.
}`                                                                           (6.13)

Therefore the majority-side submeasure of an arbitrary rough product input is absolutely continuous with essential density at most `C_B`. This is the requested ruled/rough-input bridge. It uses only three-coordinate source `L1` approximation; no moments, support conditions, log-concavity, smooth outside trace, or post-rotation independence appear.

Most importantly, (6.13) is an essential-boundedness statement. It makes **no** claim that the rough majority-side density is continuous.

For target-normalised exact rank three, `kappa>=1`, so the completed e5 result has now been applied to the concrete rough inequality

`boxed{
 P(Q in I, majority side) <= pi sqrt(2) |I|.
}`                                                                           (6.14)

This is a real paid term in the owner small-ball functional. The minority/two-sheet term remains unpaid and the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids replacing it by a generic X-ray-cap argument.

## 7. Exact logical ledger: AC, essential boundedness, continuity

### 7.1 Target absolute continuity is already direct

Let `F=prod_i f_i` and `q(x)=x^T A x` with `A!=0`. For a null set `N subset R`, local coarea on balls gives

`int_(q^{-1}(N)) F(x)|grad q(x)| dx=0`.                                     (7.1)

Since `grad q(x)=2Ax`, it is nonzero off `ker A`, while `ker A` is a Lebesgue-null proper subspace. Hence

`int_(q^{-1}(N))F(x)dx=0`.                                                   (7.2)

Thus every target law is absolutely continuous. Rank three is not needed for this qualitative implication.

### 7.2 Formal implications are strictly weaker than the owner target

A bounded density implies absolute continuity by definition, and a continuous density also implies absolute continuity. Neither qualitative property formally pays the other quantitative statements:

- AC does not imply essential boundedness: `X~Unif[0,1]`, `X^2` has density `1/(2sqrt(t))` on `(0,1)`.
- Essential boundedness does not imply a continuous representative: iid `X,Y~Unif[0,1]` give `X^2+Y^2`, whose density is `pi/4` immediately to the right of zero and zero to the left.
- Continuity alone does not imply essential boundedness for probability densities on `R`. For example, let `w_n=2^(-n)/n` and
  `p(x)=sum_(n>=1) n(1-|x-n|/w_n)_+`.
  The supports are disjoint, the triangle areas sum to `sum 2^(-n)=1`, `p` is continuous, but `p(n)=n`, so `p` is unbounded.

These are logical controls, not counterexamples to the rank-three QFORM target.

### 7.3 What is actually established on current target branches

- Full target: absolute continuity is proved by (7.1)-(7.2); the universal `L-infinity` bound is OPEN; the canonical full continuous-representative assertion remains a separate question in the live shared claim state.
- Volume-certified branch: an integrable Fourier envelope pays `L-infinity` and `C_0`/Holder regularity from the same analytic estimate. The height does not follow from continuity; both follow from Fourier integrability. The new Theorems 3.1-3.2 justify the rough-source limit quantitatively.
- Ruled majority submeasure: (6.13) pays essential boundedness directly and deliberately does not assert continuity.

So no step in this report uses continuity to smuggle in the owner height.

## 8. Remaining gap and next mechanism

The first unpaid implication after the ruled payment is the product-provenance-sensitive minority/two-sheet interval or tent estimate. The free-center obstruction means punctured kernels and generic X-ray norms do not solve it. Globally, one must also cover matrices without a uniformly conditioned physical `(2,1)` block by the current volume/high-leverage/low-tail structural alternatives.

For the volume branches, the rough-input issue is no longer a gap: any future branch yielding a common envelope `min(1,K|t|^-b)` with `b>1` automatically receives (3.3), and every `alpha<b-1` receives (3.9). The next useful B15 task is therefore not another continuity proof; it is to attach this stability compiler to a genuinely new no-pivot certificate, or to find a source-valid rough trace obstruction in an unpaid low-volume/two-sheet class.

## 9. Scope and corrections respected

No moment, bounded-support, log-concavity, Gaussian-input, identical-law, diagonal-basis, or post-rotation-independence assumption is used. I do not use any refuted arbitrary-joint coarea height lemma, worst conditional projection cap, positive moment of such caps, worst scalar-remainder conditional density, uniformly good single physical minor, law-uniform pointwise quadratic-phase decay, or generic two-sheet X-ray-only estimate. Gaussian convolution appears solely as cap-preserving original-coordinate approximation.

Full QFORM remains OPEN.
