SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T20:27:12Z.
attacking: the r42 near-zero two-hub continuation. First test the tempting arbitrary-remainder dyadic extension; after it fails, keep the exact rank-one hub geometry and spend the original-product slope innovation through a dependence-safe curved square/linear receiver.

# account03/B06 r43 — near-zero core correction and rank-one hub innovation receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** `2026-09-22.15`; programme revision `2026-09-22.5`  
**Assignment:** curved fiber integration  
**Status:** `NEW INTERMEDIATE CORRECTION + TARGET-LEVEL RANK-ONE-HUB BRANCH PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concave, moment, compact-support, connected-support, iid, finite-rank, sign, or post-rotation-independence hypothesis is introduced. The main positive theorem below uses only original independent coordinates, the cap-one product marginal theorem, and exact completion in the two literal physical hub coordinates.

## 1. Fresh source-valid inputs

The immediate predecessor is account03/B06 r42:

`yspennstate/math-open-problems@f9e66ed7e4f036debb6911c4c623fe374d32bdf4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T191938Z-account03-B06-qform-r42/REPORT.md`.

Its unpaid state has two literal physical hub variables `X,Y`, an environment product bank `Z`, a small physical `2x2` hub core, and complete slope vectors

`A(Z)=alpha dot Z+a_0`, `B(Z)=beta dot Z+b_0`,                    (1.1)

with arbitrary same-bank environmental quadratic curvature retained in `R(Z)`. At the exact zero hub core r42 proved a continuous density bound from the full slope wedge, and otherwise forced a quantitative four-star packet. The declared next debt was to pass through a genuinely nonzero hub core without replacing it by zero.

The one-dimensional product-marginal input is read from account01/B18 r21,

`yspennstate/math-open-problems@406753a39f5fbaf78396b31075f36ae5682ef3ad`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T015618Z-qform-B18-a01-r21/REPORT.md`.

It records the Livshyts--Paouris--Pivovarov theorem in the exact form used here: if `gamma !=0` and `Z` has independent cap-one original coordinates, then

`||p_(gamma dot Z)||_infinity <= sqrt(2)/||gamma||_2`.             (1.2)

The designated partner source is account04/B06 r1,

`yspennstate/math-open-problems@f24c8db8946d54f4da2d11898697913af766ad32`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260923T184145Z-account04-B06-QFORM-r1/REPORT.md`.

Its `QFORM-BANKWISE-TRIPLE-CURVATURE-v1` is applied at a new sharpened inequality in Section 5.

The live correction ledger was read before this derivation. In particular, no conditional projection-density cap, arbitrary-joint coarea theorem, law-uniform pointwise Fresnel decay, rotated independence, unrestricted curved-fiber supremum, or small-nonzero-as-zero step is used.

## 2. The tempting arbitrary-remainder extension is false

The first missing implication from r42 was to replace the exact-zero hub core by a small nonzero hyperbolic core while keeping only the joint slope-density input and allowing the environment remainder to be arbitrary. That interface is false even when the two slopes themselves are independent cap-one variables.

### Proposition 2.1 — `QFORM-NEARZERO-ARBITRARY-REMAINDER-EXTENSION-FALSE-v1`

For every `0<epsilon<=1/2`, let `X,Y,A,B` be four mutually independent `Uniform[-1/2,1/2]` variables. In particular, `X,Y` have density caps one and the slope pair `(A,B)` has joint-density cap one. Define

`Q_epsilon
 =2 epsilon X Y+2 A X+2 B Y+2 A B/epsilon`.                    (2.1)

Then the physical hub core

`H_epsilon=[[0,epsilon],[epsilon,0]]`                              (2.2)

is nonzero and tends to zero in norm as `epsilon downarrow0`, but `Q_epsilon` has an unbounded density for every such `epsilon`.

#### Proof

Factor exactly:

`Q_epsilon
 =2 epsilon (X+B/epsilon)(Y+A/epsilon)`.                          (2.3)

Put

`U=X+B/epsilon`, `V=Y+A/epsilon`.                                  (2.4)

The pair `(X,B)` is independent of `(Y,A)`, hence `U` and `V` are independent. Since `B/epsilon` has density `epsilon` on `[-1/(2epsilon),1/(2epsilon)]`, convolution with `X` shows

`p_U(u)=epsilon`, `p_V(v)=epsilon`                                 (2.5)

throughout `|u|,|v|<=1/2` when `epsilon<=1/2`.

For `0<w<1/4`, the product `W=UV` has density

`p_W(w)= integral_R p_U(u)p_V(w/u) du/|u|`.                        (2.6)

Restricting the integral to `2w<=u<=1/2` keeps both arguments inside the plateau in (2.5), so

`p_W(w)
 >=epsilon^2 integral_(2w)^(1/2) du/u
 =epsilon^2 log(1/(4w)).`                                         (2.7)

Since `Q_epsilon=2epsilon W`, for `0<t<epsilon/2`,

`p_(Q_epsilon)(t)
 >=(epsilon/2) log(epsilon/(2t)).`                                 (2.8)

The right side tends to infinity as `t downarrow0`; indeed every height is exceeded on a positive interval, so the essential supremum is infinite. QED.

### Why this is NOT a counterexample to the owner's conjecture

In variable order `(X,Y,A,B)`, the symmetric matrix of (2.1) is

`M_epsilon =
 [[0,epsilon,1,0],
  [epsilon,0,0,1],
  [1,0,0,1/epsilon],
  [0,1,1/epsilon,0]].`                                            (2.9)

After ordering the two factor banks as `(X,B)|(Y,A)`, its cross block is

`C_epsilon=[[epsilon,1],[1,1/epsilon]]`,                           (2.10)

which has determinant zero and rank one. Therefore `M_epsilon` has spectrum

`{ +(epsilon+epsilon^(-1)), -(epsilon+epsilon^(-1)), 0,0 }`.       (2.11)

It has only two nonzero eigenvalues. Thus Proposition 2.1 refutes the **intermediate arbitrary-remainder continuation**, not QFORM. It pinpoints the missing resource: the target's genuine third curvature cannot be hidden inside an arbitrary `R` and then ignored. Any valid near-zero-core proof must spend that third curvature, or exploit an exact degeneracy that turns the remaining hub direction linear.

This correction also explains why a naive dyadic averaging of the frozen two-dimensional hyperbolic density cannot by itself close r42: the moving critical value can be aligned by the remainder and preserve a logarithmic singularity on a positive set of slope values.

## 3. Exact rank-one hub core: the logarithm disappears

The determinant-zero but nonzero hub surface is qualitatively different from Proposition 2.1 once its **slope innovation** is retained instead of allowing an arbitrary completed remainder.

Let `X,Y` be independent cap-one original coordinates and `Z` an independent original-coordinate product bank, also cap one coordinatewise. Let

`H=[[a,b],[b,d]]`, `det H=0`, `H!=0`,                              (3.1)

and

`A(Z)=alpha dot Z+a_0`, `B(Z)=beta dot Z+b_0`.                    (3.2)

For an arbitrary measurable `R(Z)`, consider

`Q=a X^2+2bXY+dY^2+2A(Z)X+2B(Z)Y+R(Z)`.                           (3.3)

Because a nonzero symmetric rank-one matrix has a nonzero diagonal, after possibly swapping the two physical hubs we may assume `a!=0`. Then `d=b^2/a`.

### Theorem 3.1 — `QFORM-RANKONE-HUB-INNOVATION-v1`

Define the original-product innovation vector

`Gamma := a beta-b alpha`.                                        (3.4)

If `Gamma!=0`, then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) ||Gamma||_2^(-1/2)
 =6.727171322... ||Gamma||_2^(-1/2).`                              (3.5)

No assumption is made on `R(Z)`, and in particular it may contain arbitrary same-bank quadratic curvature and every nonzero spectral tail. Continuity is not claimed.

#### Proof

Set

`C(Z):=B(Z)-(b/a)A(Z)`.                                           (3.6)

Using `d=b^2/a`, exact completion in the literal physical variable `X` gives

`Q
 =a [X+(bY+A(Z))/a]^2
  +2 C(Z)Y+R(Z)-A(Z)^2/a.`                                       (3.7)

This identity is the essential rank-one cancellation: the residual `Y^2` coefficient is exactly zero. No rotation of `(X,Y)` is performed.

Let

`W:=2C(Z)Y+R(Z)-A(Z)^2/a`,
`Psi:=(bY+A(Z))/a`.                                               (3.8)

Condition on `(Y,Z)`. The translated variable `X+Psi` still has conditional density cap one. The elementary translated-square kernel therefore gives, for almost every output `t`,

`p_Q(t)
 <= |a|^(-1/2) E |t-W|^(-1/2).`                                  (3.9)

Now condition only on `Z`. If `C(Z)=c!=0`, the random variable `2cY+const` has density cap `1/(2|c|)`. For any probability density bounded by `K`, the one-dimensional bathtub estimate is

`sup_s integral |u-s|^(-1/2) g(u)du <=2 sqrt(2K)`.                (3.10)

With `K=1/(2|c|)`, (3.10) gives

`E_Y |t-W|^(-1/2) <=2 |c|^(-1/2)`.                               (3.11)

Consequently

`p_Q(t)
 <=2 |a|^(-1/2) E |C(Z)|^(-1/2).`                                (3.12)

The coefficient vector of `C` is

`gamma:=beta-(b/a)alpha=Gamma/a`.                                (3.13)

By the source-valid one-dimensional product marginal theorem (1.2),

`||p_C||_infinity
 <=sqrt(2)/||gamma||_2.`                                         (3.14)

Apply (3.10) once more, now to `C`, at exponent one half:

`E |C|^(-1/2)
 <=2 sqrt( 2 sqrt(2)/||gamma||_2 )
 =2^(7/4) ||gamma||_2^(-1/2).`                                   (3.15)

Insert (3.15) into (3.12):

`||p_Q||_infinity
 <=2^(11/4) [ |a| ||gamma||_2 ]^(-1/2)
 =2^(11/4) ||a beta-b alpha||_2^(-1/2).`                          (3.16)

This proves (3.5). The exceptional event `C=0` has probability zero because `Gamma!=0` makes `C` absolutely continuous. QED.

### Interpretation

The theorem is a curved-fiber payment that never takes a worst fiber. One physical direction is paid as a translated square; because the hub core is exactly rank one, the other physical direction becomes exactly linear. Its reciprocal-square-root cost is averaged against the whole original-product innovation law before a supremum is taken. This is precisely the weighted replacement unavailable in Proposition 2.1 when a genuine hyperbolic residual remains.

## 4. Apply Theorem 3.1 to the actual r42 two-hub packet

Return to r42 notation. The complete two hub-to-environment slope vectors are

`alpha=(s,r)`, `beta=(c,t)`.                                      (4.1)

Suppose the physical hub core

`H_hub=[[a,b],[b,d]]`                                             (4.2)

is **exactly rank one and nonzero**. Choose a nonzero diagonal pivot, swapping the physical hubs if necessary. Then the full ambient target form is covered by Theorem 3.1 with

`J:=||a beta-b alpha||_2`.                                       (4.3)

Hence on the explicit innovation branch

`J>=2^(-12)`,                                                     (4.4)

we obtain the universal target-level bound

`boxed: ||p_Q||_infinity
 <=2^(11/4) 2^6
 =430.5389646099... <430.539.`                                    (4.5)

No environmental quadratic term or ultra-thin tail from r42 is deleted.

If (4.4) fails, the determinant-zero survivor is quantitatively sharper than before:

`boxed: ||a beta-b alpha||_2<2^(-12).`                            (4.6)

If the chosen first diagonal is zero, rank one forces `b=0` and `d!=0`; swapping the hubs gives the symmetric certificate

`||d alpha-b beta||_2<2^(-12)`                                    (4.7)

on the unpaid branch.

Thus the exact determinant-zero collar is no longer simply “nonzero core”: it is either density-paid, or its two full slope rows are aligned with the unique rank-one hub direction to absolute innovation below `2^-12`. The exact zero core remains governed by r42's wedge-or-four-star theorem.

This does **not** cover a merely small nonzero determinant. Proposition 2.1 shows why such a statement requires the third curvature rather than an arbitrary-remainder perturbation argument.

## 5. Designated account04/B06 theorem: sharper actual inequality

Account04/B06 r1 proves, on its live exact-rank-three bankwise chamber,

`||p_Q||_infinity
 <=12 [D |lambda| det G_b]^(-1/3)`,                               (5.1)

provided the chosen bank has normalized three-curvature leverage at most `1/2`. Its live packet also supplies

`D |lambda|>=1/4`,                                                (5.2)

and three disjoint bank normal masses

`W_1 W_2 W_3>61/1728`, `0<W_b<=1`.                               (5.3)

The previous B06 application used only the weaker consequence `W_b>61/1728` for each bank. A sharper actual application chooses a bank `b_*` of maximal normal mass. Then

`W_(b_*) >(61/1728)^(1/3)
          =0.328041431925...`.                                    (5.4)

If this maximal-normal-mass bank satisfies the partner's diffuse leverage gate and its aggregate transversality gate

`det G_(b_*)>=W_(b_*)/64`,                                       (5.5)

then (5.1)--(5.5) give

`D |lambda| det G_(b_*)
 >(1/4)(61/1728)^(1/3)/64`,                                      (5.6)

and therefore

`boxed:
 ||p_Q||_infinity
 <12[(1/4)(61/1728)^(1/3)/64]^(-1/3)
 =110.4803398469... <110.481.`                                   (5.7)

The partner theorem supplies a continuous density on this branch. This is a genuine new insertion of the designated partner result into an actual inequality, and it sharpens the previous `232.274` payment when the **largest normal-mass bank** is the diffuse/transverse one. If that bank does not satisfy (5.5) or its leverage gate, no conclusion is fabricated; the failure itself is a stronger heavy-hub/shear-flat certificate on the bank carrying at least `0.328` normal mass.

## 6. Exact checks

The accompanying pure-Python checker evaluates:

- `2^(11/4)=6.727171322029716...`;
- the innovation threshold payment `2^(11/4)*2^6=430.5389646099018...`;
- `(61/1728)^(1/3)=0.3280414319251811...`;
- the sharpened partner payment `110.48033984697105...`.

For Proposition 2.1 the proof itself is symbolic: the rank-one cross block (2.10) has its sole singular value `epsilon+epsilon^(-1)`, so (2.11) is exact. The logarithmic lower bound (2.8) is an analytic density calculation, not a histogram or simulation.

## 7. What is now ruled out and what remains

The run produces two complementary pieces of information.

1. **False interface removed.** A small nonzero hyperbolic core cannot be handled by extending r42's joint-slope theorem while treating the completed environment remainder as arbitrary. The explicit independent-product example (2.1) has an unbounded logarithmic density at every nonzero `epsilon`, despite joint slope cap one. Its matrix is rank two, so it does not threaten the owner target; it proves the third eigenvalue must be used.

2. **Exact rank-one boundary paid.** On the actual r42 target packet, an exact nonzero rank-one hub core is paid whenever the original-product slope innovation is at least `2^-12`, with full environmental curvature retained. Failure gives the explicit alignment certificate (4.6)/(4.7), which is the correct input to a third-curvature/Schur receiver.

The next B06 debt is therefore

`QFORM-NEARRANK1-HUB-THIRD-CURVATURE-BRIDGE-v1`:

> In the r42 small-core survivor with `0<|det H_hub|` very small, retain the logarithmic physical-pair geometry and use the target's actual third curvature before taking a supremum. Quantitatively bridge either to the full-matrix indefinite-pair log theorem / a definite ellipse payment, or to account04/B06's bankwise triple-curvature theorem. In the determinant-zero alignment endpoint, use (4.6) to show that the third curvature lies in a residual original-product bank rather than replacing that bank by an arbitrary remainder.

A useful warning for that bridge is exact: completing an invertible hub pair and then declaring its Schur remainder arbitrary loses precisely the resource that distinguishes a rank-two counterexample from the three-large-eigenvalue target.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** This run proves essential boundedness on the exact rank-one innovation branch and continuity only on the separately scoped account04/B06 partner branch. It also gives an explicit counterexample to the overbroad near-zero arbitrary-remainder interface, not to QFORM.
