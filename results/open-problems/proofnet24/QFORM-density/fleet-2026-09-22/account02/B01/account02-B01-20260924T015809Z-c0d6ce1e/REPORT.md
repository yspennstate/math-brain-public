SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T01:58:01Z.
attacking: the exact-W2 finite-support rank-two leakage endpoint; first compress its latent geometry to a single physical edge / star normal form, then spend the isotropic support-one star by half-Riesz before any small determinant is inverted.

# account02/B01 — finite-leak normal form and support-one star half-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account02-B01-20260924T015809Z-c0d6ce1e`  
Role: oscillatory replacement / complementary constructions and source-valid obstructions  
Status: **ESSENTIAL STEP APPLIED / NEW EXACT STRUCTURAL REDUCTION + NEW SCOPED HALF-RIESZ COMPILER / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Control, sources, and correction boundary


The required compatible source package was read at the exact pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The two source statements used below are proved there:

1. one-hub mixed Fresnel / Theorem MF with diagonal leaves: if the physical hub-to-leaf slope is `b`, its one-dimensional frame leverages `b_i^2/||b||_2^2` are at most `1/2`, and all leaf self-curvature is diagonal, then arbitrary hub self-curvature and affine terms are allowed and

`|phi(t)| <= 2 pi ||b||_2^(-1) |t|^(-1)`;                      (1.1)

2. the fractional-potential and square-peel lemmas:

`H_(1/2)(Z) <= (2 pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)| dt`,     (1.2)

and, after a literal original-coordinate scalar completion

`Q=a(X_0+h)^2+Z`, `a!=0`,

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(Z)`.                   (1.3)

The phase-aligned-density correction remains binding. For every prescribed nonzero frequency `s` and small `eta`, one can choose a finite union of intervals of total length one inside `{x:dist(sx^2,2pi Z)<=eta}`; its indicator is an admissible cap-one density with `Re E exp(isX^2)>=cos eta`. Hence no law-uniform scalar pointwise Fresnel power decay is asserted below. The proof uses a JOINT hub/leaf transform and an integrated half-Riesz weight.

No spectral-coordinate independence, arbitrary-joint coarea, conditional density-cap inheritance, moments, Gaussianity, log-concavity, support regularity, or deletion of a small random quadratic tail is used.

## 2. Starting endpoint from the preceding B01 reductions

The preceding account02/B01 exact-`W_2` work reduces one survivor, after a literal outer scalar completion, to a residual coefficient matrix

`H = D + U C U^T`,                                               (2.1)

where `D` is diagonal, `U` has two latent columns, and `C` is an invertible symmetric `2 x 2` matrix. On an exact-rank-one original-coordinate cut `I|J`, after an algebraic change of basis in the two-dimensional coefficient space only (NOT a rotation of random variables), one has

`U_I=[u,0]`, `U_J=[v,w]`,
`C=[[alpha,beta],[beta,gamma]]`, `Delta_C=alpha gamma-beta^2 !=0`. (2.2)

The previously proved transverse-wedge theorem shows that if the latent triple currency is positive, a literal re-cut creates a rank-two packet and pays it. At the exact zero-currency endpoint with genuinely two-dimensional `U_J`, the transverse vector satisfies

`|supp(w)| <= 2`.                                                (2.3)

The first unpaid implication was to spend exactly this finite physical support without rotating away independence.

For the algebra below, condition every coordinate outside `I union J`; this changes only affine/constant terms. Define the literal vectors on `I union J`

`z=(u on I, v on J)`,
`wtilde=(0 on I, w on J)`.                                      (2.4)

Then

`U C U^T
 = alpha z z^T + beta(z wtilde^T+wtilde z^T)+gamma wtilde wtilde^T`. (2.5)

## 3. Exact finite-leak normal form

### Theorem `QFORM-ZETA0-FINITELEAK-NORMALFORM-v1`

Under (2.1)-(2.5) and `|supp(w)|<=2`:

**(A) Non-isotropic latent direction: `alpha!=0`.** Put

`q=z+(beta/alpha)wtilde`, `tau=Delta_C/alpha`.                  (3.1)

Then exactly

`boxed: H = D + alpha q q^T + tau wtilde wtilde^T.`            (3.2)

Consequently:

- if `|supp(w)|<=1`, the last term is diagonal and can be absorbed into `D`, so the residual is **diagonal plus global rank one**;
- if `supp(w)={j,k}`, absorb the two diagonal entries of `tau wtilde wtilde^T` into `D`. What remains is exactly one literal physical edge:

`boxed: H = D' + alpha q q^T
              + eta(e_j e_k^T+e_k e_j^T),`
`eta=tau w_j w_k.`                                              (3.3)

Thus the entire genuinely rank-two zero-wedge leakage has collapsed to a global rank-one term plus ONE physical edge.

**(B) Isotropic latent direction: `alpha=0`.** Since `C` is invertible, `beta!=0`, and

`boxed: H=D+beta(z wtilde^T+wtilde z^T)+gamma wtilde wtilde^T.` (3.4)

If `supp(w)={j}`, all non-diagonal low-rank entries are incident to the single literal coordinate `j`. After absorbing the `jj` entry into the diagonal,

`boxed: H=D'+e_j b^T+b e_j^T,  b_j=0,`
`b_i=beta w_j z_i  (i!=j).`                                    (3.5)

So the residual is exactly **diagonal plus one physical star**.

If `supp(w)={j,k}` and `S={j,k}`, put `L=(I union J)\S`. Then

`H[L,L]=D_L` is diagonal and

`boxed: H[S,L]=beta w_S z_L^T,`                                (3.6)

which has rank at most one. Thus the remaining object is a two-hub arrowhead with diagonal leaves and only a rank-one two-hub slope packet.

### Proof

For `alpha!=0`, complete the deterministic latent square:

`alpha z z^T+beta(zwtilde^T+wtilde z^T)+gamma wtilde wtilde^T`
`=alpha(z+(beta/alpha)wtilde)(z+(beta/alpha)wtilde)^T`
` +(gamma-beta^2/alpha)wtilde wtilde^T`
`=alpha q q^T+(Delta_C/alpha)wtilde wtilde^T`,

which is (3.2). If the support has one coordinate, its rank-one outer product is diagonal. If it has exactly two, its two diagonal entries are absorbed into `D` and its sole off-diagonal entry is (3.3).

For `alpha=0`, (3.4) is (2.5). If `wtilde` is supported at `j`, every off-diagonal term contains `e_j`; absorbing the `jj` coefficient gives (3.5). If its support is `S={j,k}`, then on the complement `L` both entries of `wtilde` vanish, so all low-rank off-diagonal coefficients within `L` vanish. Across `S|L`, only `beta w_S z_L^T` survives. QED.

This theorem is purely coefficient algebra in the ORIGINAL coordinate system. It neither creates nor assumes independence of latent coordinates.

## 4. The isotropic support-one star is paid by averaged frequency

The support-one `alpha=0` case (3.5) still contains an analytic issue: a star by itself has only critical `|t|^-1` decay, not an integrable characteristic function. The required fractional-potential source turns that critical decay into exactly enough half-Riesz control for the already-present outer square.

### Theorem `QFORM-ISOTROPIC-SUPPORT1-STAR-HALFRIESZ-v1`

Suppose a literal outer coordinate has been completed as

`Q=a(X_0+h)^2+R`, `a!=0`,                                      (4.1)

and the residual quadratic coefficient is

`H=D'+e_j b^T+b e_j^T`, `b_j=0`,                               (4.2)

with `D'` arbitrary diagonal. Affine terms are arbitrary. Assume `b!=0` and

`max_(i!=j) b_i^2/||b||_2^2 <= 1/2`.                           (4.3)

Then

`boxed: H_(1/2)(R) <= 8 ||b||_2^(-1/2),`                       (4.4)

and therefore

`boxed: ||p_Q||_infinity
        <= 8 |a|^(-1/2) ||b||_2^(-1/2).}`                      (4.5)

Essential boundedness is proved; continuity is not claimed by this peel.

### Proof

Use the literal coordinate `j` as the one hub and every other residual coordinate as a leaf. The leaf self-block is diagonal, the augmented one-dimensional hub frame is exactly the physical slope vector `b`, and (4.3) is precisely the source leverage gate. Theorem MF / Theorem H at one hub and rank `r=0` therefore gives, uniformly in all affine terms and the hub diagonal,

`|phi_R(t)| <= min{1, B/|t|}`, `B=2 pi/||b||_2`.               (4.6)

Now the source's half-Riesz lemma yields

`H_(1/2)(R)
 <= (2pi)^(-1/2) int_R |t|^(-1/2) min(1,B/|t|) dt`.             (4.7)

The integral is elementary:

`int_R |t|^(-1/2) min(1,B/|t|) dt = 8 sqrt(B)`.                 (4.8)

Since `B=2pi/||b||`, (4.7)-(4.8) give exactly (4.4). Finally apply the literal square peel (1.3), proving (4.5). QED.

In the high-outer-pivot chamber `|a|>=1/64`, a target-scale diffuse star `||b||>=1/16` is therefore paid by the completely explicit universal number

`||p_Q||_infinity <= 8*8*4 = 256`.                              (4.9)

No individual `3 x 3` minor and no small physical-pair determinant is inverted.

## 5. Concrete target family: all third/fifth cross volumes vanish, but the new star compiler gives 8

Take four ORIGINAL independent cap-one variables `(X_0,H,Y_1,Y_2)` and

`Q_*=X_0^2 + sqrt(2) H(Y_1+Y_2)`.                              (5.1)

Its coefficient matrix is

`A_* = [[1,0,0,0],
        [0,0,1/sqrt(2),1/sqrt(2)],
        [0,1/sqrt(2),0,0],
        [0,1/sqrt(2),0,0]].`                                    (5.2)

The spectrum is exactly

`{-1,0,1,1}`,                                                    (5.3)

so this is an actual owner-target form with three eigenvalues of modulus at least one.

The residual star has `a=1`, `b=(1/sqrt(2),1/sqrt(2))`, hence `||b||=1` and both leverages are exactly `1/2`. Theorem 4 therefore gives the law-uniform full-target estimate

`boxed: ||p_(Q_*)||_infinity <= 8.`                             (5.4)

This is also an actual application/obstruction for the required `20260922T211500Z` source. For every original-coordinate cut of `A_*`, the cross block has rank at most one. Hence

`e_3(M^T M)=e_5(M^T M)=0`                                      (5.5)

for every cut, so Theorem D, D', and D5 have exactly zero currency on this family. The one-hub mixed-Fresnel estimate plus half-Riesz peel succeeds where the rank-three/five volume receivers are structurally unavailable.

The phase-aligned scalar counterexample is not contradicted: (4.6) is a JOINT hub/leaf estimate, not a pointwise estimate for one scalar quadratic phase.

## 6. Newest designated partner account03/B01 applied at an actual target inequality

The newest completed account03/B01 report read in this invocation is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T012854Z-account03-B01-qform-auto11-r40/REPORT.md`.

Its theorem `QFORM-TWO-HUB-CONDITIONAL-LR-RESIDUAL-v1` proves, at `r=2`, that a two-hub packet with slope map `S(Y)=BY+d`, `rank B=2`, and a conditionally `L^2` residual obeys the corresponding averaged-frequency gluing bound. Its hyperbolic-edge corollary gives

`||p_Q||_infinity <= 3 D^(-1/6)|c|^(-1/3)`,
`D=det(BB^T)`,                                                   (6.1)

for an edge `2cUV` even with arbitrary slope-bank-dependent affine shifts of `U,V`.

Apply (6.1) to the actual target family, for any `k>=1`,

`Q_k=2k(H_1Y_1+H_2Y_2)+2k^(-2)UV`,                             (6.2)

with six independent original cap-one variables. Here

`B=k I_2`, `D=k^4`, `c=k^(-2)`,                                (6.3)

so the partner theorem gives the scale-cancelled inequality

`boxed: ||p_(Q_k)||_infinity <= 3}`                              (6.4)

uniformly in `k` and in all input laws. The coefficient spectrum is

`{+k,+k,-k,-k,+k^(-2),-k^(-2)}`,                               (6.5)

hence at least four eigenvalues have modulus at least one for every `k>=1`. This is a genuine full-target application of the newest partner result, not a summary.

The same partner theorem also marks the exact obstruction in the support-two isotropic normal form (3.6): its two-hub slope matrix has rank at most one, so `det(BB^T)=0`; the partner's rank-two slope hypothesis cannot be invoked there. That rank-one-slope arrowhead remains a real endpoint rather than an already-paid case.

## 7. What this changes in the first unpaid implication

Before this run the exact zero-wedge finite-leak survivor was only known to have a transverse latent direction supported on at most two physical coordinates. It now has a much sharper exhaustive normal form:

1. `alpha!=0`, support one: diagonal plus global rank one;
2. `alpha!=0`, support two: diagonal plus global rank one plus ONE physical edge;
3. `alpha=0`, support one: diagonal plus ONE physical star; its diffuse target-scale subbranch is paid by (4.5), e.g. by `256` when `|a|>=1/64`, `||b||>=1/16`;
4. `alpha=0`, support two: a two-hub arrowhead with diagonal leaves and rank-one hub-to-leaf slope.

Thus the next first unpaid implication is

`QFORM-FINITELEAK-SINGLEEDGE-OR-HEAVYSTAR-ROUTING-v1`:

> In the remaining exact-`W_2` branch, route (i) the single-edge perturbation of diagonal-plus-rank-one, (ii) the support-one star when its slope is concentrated in one physical leaf or quantitatively tiny, and (iii) the support-two rank-one-slope arrowhead, into a physical pair/three-square, conditional-L^r two-hub, or another completed receiver without paying a reciprocal tiny coefficient prematurely.

The support-two isotropic arrowhead is especially concrete: every diffuse leaf-leaf coupling is exactly zero, so the remaining difficulty is bounded-coordinate hub degeneracy plus one aggregate slope direction, not a diffuse rank-two tail.

Full QFORM remains OPEN. No counterexample was found or claimed.

## 8. Telemetry / execution facts

Model self-report: `GPT-5.6 Sol`. Reasoning level exposed to this run: `UNKNOWN`; standing owner request: maximum actually supported. Provider reasoning-token count and provider thinking time are not exposed and must remain `null`. Authenticated repository retrieval was used, but the receiver-memory query supplied no QFORM-specific state used in this proof; execution therefore remains `WITHOUT_VERIFIED_BRAIN`. Elapsed execution is recorded in the finish/receipt and includes reasoning, tool/network, validation, publication and readback overhead; it is not pure thinking.
