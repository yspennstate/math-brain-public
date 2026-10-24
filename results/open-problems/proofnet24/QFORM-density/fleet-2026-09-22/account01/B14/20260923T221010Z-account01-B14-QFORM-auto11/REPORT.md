SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T22:10:10Z.
attacking: hybrid localization across a vanishing square pivot and a diffuse quadratic receiver; keep the outside law as one mixture and pay whichever whole active third-direction resource is nondegenerate.

# account01/B14 — exact outside-affine localization and a square-or-receiver max certificate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** translations and localization  
**Status:** NEW SUPPORTING LOCALIZATION / TARGET-VALID HYBRID THEOREM. **Full unrestricted QFORM remains OPEN.**  
**Continuity:** not asserted; the conclusions below are interval bounds / essential-density bounds.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh sources and corrections actually used

Fresh control was re-read on `math-research-brain/main`; the owner control remains revision `2026-09-22.15`, QFORM-only, with no later stop for this slot. The live corrections excluding law-uniform pointwise quadratic Fourier decay, post-rotation independence, bounded-diameter/fixed-fragment localization, arbitrary-joint rank-three coarea, and normalized-fiber positive-moment arguments remain in force.

Two completed `account02/B14` sources are used below.

1. Latest generic-closure report:

`yspennstate/math-open-problems@9b3f83bd70880feb4c0ce0fb1820aa0efb335d20`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T214233Z-account02-B14-QFORM-generic-closure/REPORT.md`.

It proves zero-loss closure under total-variation approximation of the product laws and coefficient convergence of the quadratic/affine polynomial, and the exact equivalence of full QFORM to the smooth-compact, generic-matrix, strict-margin class, with affine terms recovered at the same constant.

2. Pre-Jensen receiver report:

`yspennstate/math-open-problems@6bc5027a5df12a2cd28130ded9fb53711eb90e39`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T173217Z-account02-B14-QFORM-r41/REPORT.md`.

For `4/3<r<2`, `p=r/(r-1)`, independent cap-one driver coordinates `Z` and receiver `W`, a core `T_z` independent of `W`, and

`Q=T_Z+s(Z)+hW^2+(2a^T Z+e)W`,

with `R0=sqrt(h^2+||a||_2^2)>0`, it proves

`||p_Q||_infinity <= K_r 2^{3(r-1)/(2r)} (2-r)^(-1/r) R0^{-(r-1)/r}`      (1.1)

whenever `||p_{T_z}||_p<=K_r` uniformly. Its stronger pre-Jensen form allows an integrated `L^p` core budget; the uniform version is enough for the new inequality below.

## 2. Exact localization lemma: outside variables cost zero once the active theorem is affine-uniform

For a symmetric `m x m` matrix `B`, define its affine cap-one interval constant

`C_aff(B) = sup_{product cap-one X} sup_{ell,c} sup_{bounded intervals I}
            P(X^T B X+ell^T X+c in I)/|I|`.                     (2.1)

### Lemma 2.1 — `QFORM-AFFINE-UNIFORM-CONDITIONAL-LIFT-v1`

Let a full symmetric matrix be written in original coordinates as

`A=[[B,C],[C^T,D]]`.                                              (2.2)

For arbitrary independent cap-one active coordinates `X` and arbitrary independent cap-one outside coordinates `Y`, with no support or moment assumptions,

`boxed: Lambda(X^T B X+2X^T C Y+Y^T D Y) <= C_aff(B)`,            (2.3)

where `Lambda` is the extended interval-density functional `sup_I P(Q in I)/|I|`.

#### Proof

Condition on the outside original coordinates, `Y=y`. Then

`Q_y(X)=X^T B X + (2Cy)^T X + y^T D y`.                          (2.4)

The definition of `C_aff(B)` gives, for every bounded interval `I` and every `y`,

`P(Q_y(X) in I | Y=y) <= C_aff(B)|I|`.                           (2.5)

Integrating in the actual outside law gives the identical inequality for `Q`. No truncation, expectation, support diameter, fragment count, fragment location, or moment enters. QED.

If `s_3(B)>=1`, Cauchy interlacing implies the ambient `A` also has at least three eigenvalues of modulus at least one. Thus (2.3) is an exact target-preserving localization: arbitrary outside curvature and active-outside couplings become only affine shifts after conditioning, and **the constant is unchanged**.

### Corollary 2.2 — generic smooth active theorem lifts to rough ambient theorem with the same constant

Suppose a constant `C` has been proved for all smooth compact cap-one product laws and all generic `B` with `s_3(B)>1`, in the homogeneous active theorem. The latest `account02/B14` generic-closure theorem upgrades this, with the same `C`, to arbitrary cap-one active laws, threshold `s_3(B)>=1`, and arbitrary deterministic affine terms. Lemma 2.1 then upgrades it, still with the same `C`, to every ambient extension (2.2) and arbitrary rough/unbounded outside product law.

This is the precise constant-preserving route from a compact/generic active proof to the original arbitrary-shift, arbitrary-fragment, no-moment problem. Exact zero pivots can be removed by the partner closure; a reciprocal estimate that diverges as a pivot tends to zero still cannot be used unless another whole-active resource takes over.

## 3. Two elementary translation-uniform `L^p` estimates

The hybrid theorem below needs only two physical-space inequalities.

### Lemma 3.1 — translated hyperbolic pair

For independent cap-one `U,V`, every `c!=0`, arbitrary shifts `u0,v0`, and `1<=p<infinity`,

`boxed: ||p_{2c(U-u0)(V-v0)}||_p <= p |c|^{-1+1/p}.`             (3.1)

For fixed `U=x`, scaling the cap-one density of `V` gives conditional `L^p` norm at most

`(2|c||x-u0|)^(-1+1/p)`.

Minkowski and the sharp one-dimensional rearrangement estimate

`E|U-u0|^{-alpha} <= 2^alpha/(1-alpha)`, `alpha=1-1/p`,            (3.2)

give (3.1). In particular,

`||p_{2c(U-u0)(V-v0)}||_3 <=3|c|^(-2/3).`                        (3.3)

### Lemma 3.2 — translated square

For cap-one `X`, `delta!=0`, and arbitrary `x0`, the density `g` of `delta(X-x0)^2` satisfies

`g(u)<= (|delta|u)^(-1/2)` on the appropriate half-line.           (3.4)

Therefore

`int g^(3/2) <= |delta|^(-1/2) E|X-x0|^(-1/2)
               <=2sqrt(2)|delta|^(-1/2)`,                        (3.5)

and hence

`boxed: ||g||_(3/2) <=2|delta|^(-1/3).`                          (3.6)

Both estimates are completely independent of support geometry and translations.

## 4. New hybrid theorem: pay the maximum of a square pivot and a diffuse receiver norm

Let all coordinates below be independent and cap one. Select an original-coordinate principal active block of the form

`A_* = [[0,c],[c,0]] direct_sum [delta] direct_sum S`,             (4.1)

where

`S=[[H,a],[a^T,h]]`,                                              (4.2)

`H` is an arbitrary symmetric matrix of any dimension, and

`R0=sqrt(h^2+||a||_2^2)`.                                        (4.3)

The full ambient matrix may have **arbitrary coefficients and couplings to every coordinate outside this active block**. Put

`rho=max{|delta|,R0}`.                                            (4.4)

### Theorem 4.1 — `QFORM-HYPERBOLIC-SQUARE-OR-RECEIVER-MAX-v1`

If `c!=0` and `rho>0`, then the full ambient quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <= |c|^(-2/3) min{6|delta|^(-1/3),
                    3*2^(7/6) R0^(-1/3)}
 <=3*2^(7/6)|c|^(-2/3) rho^(-1/3),`                              (4.5)

with the corresponding branch interpreted as `+infinity` if `delta=0` or `R0=0`.

No moments, centers, connected supports, bounded supports, or fragment-count/separation assumptions occur.

#### Proof: first branch, square smoothing

Condition on every coordinate outside `A_*`. All outside couplings become deterministic affine terms. The hyperbolic and scalar pieces have the form

`P=2cUV+alpha U+beta V`,
`Sx=delta X^2+gamma X`.                                           (4.6)

Completing the product and square changes only the shifts and an output constant. By (3.3), (3.6), and Young `L^3*L^(3/2)->L^infinity`,

`||p_{P+Sx}||_infinity <=6|c|^(-2/3)|delta|^(-1/3).`              (4.7)

The entire `S`-block is independent of `(U,V,X)` after the outside conditioning; convolution with its probability law cannot increase the supremum. This proves the first term in (4.5), pointwise in the outside variables, hence also after averaging them.

#### Proof: second branch, completed partner receiver inequality

Still after conditioning only on the coordinates outside `A_*`, temporarily omit the independent scalar `Sx`; it will be convolved back at the end. Write the remaining active form as

`P + Z^T H Z + ell^T Z + hW^2 +(2a^T Z+e)W + const`.             (4.8)

Use `P` as the partner core. It is independent of `(Z,W)` and (3.3) gives its uniform `L^3` budget

`K_3<=3|c|^(-2/3)`.                                               (4.9)

Apply the completed `account02/B14` receiver theorem (1.1) at

`r=3/2`, `p=3`.

Since

`2^{3(r-1)/(2r)}(2-r)^(-1/r)=2^(7/6)`,                           (4.10)

we obtain the **actual inequality**

`||p_{P+receiver}||_infinity
 <=3*2^(7/6)|c|^(-2/3)R0^(-1/3).`                                (4.11)

Convolving the independent scalar `Sx` back in cannot increase the bound. Again the estimate is uniform in all affine terms produced by the arbitrary outside coordinates, so Lemma 2.1 averages them at zero cost. This proves the second branch.

Finally, if `rho=|delta|`, use the first branch and `6<3*2^(7/6)`; if `rho=R0`, use the second. This gives the max-form in (4.5). QED.

### Target validity

The first block in (4.1) has eigenvalues `+|c|,-|c|`. Also

`||S||_op >= ||S e_W||_2 = R0`.                                  (4.12)

Therefore, if

`|c|>=1`, `rho=max{|delta|,R0}>=1`,                               (4.13)

then `A_*` has at least three eigenvalues of modulus at least one: the hyperbolic pair supplies two, and either `[delta]` or `S` supplies the third. Since `A_*` is a principal block, interlacing preserves the threshold count in the full ambient matrix. Thus this is a genuine branch of the exact owner target, and

`boxed: ||p_Q||_infinity <=3*2^(7/6)=6.734772289856... .`         (4.14)

The point of (4.5) is not the numerical constant. It is that the certificate **does not invert one preselected near-zero pivot**. A vanishing square coefficient is harmless if a whole diffuse receiver norm remains; a vanishing receiver row is harmless if the square remains. The bound pays the larger of the two third-direction resources.

## 5. Explicit near-degenerate / diffuse family

For every `t>0` and integer `m>=1`, set

`c=1`, `delta=t`, `H=0`, `h=0`,
`a=(1/(t sqrt(m)))(1,...,1)`.                                    (5.1)

Then `R0=1/t`, while every individual receiver coupling is `1/(t sqrt(m))`. The active spectrum is

`{1,-1,t,1/t,-1/t,0,...,0}`,                                    (5.2)

so the exact three-large-eigenvalue condition holds for every `t>0`. Theorem 4.1 gives

`||p_Q||_infinity
 <= min{6t^(-1/3), 3*2^(7/6)t^(1/3)}.                            (5.3)

The first certificate diverges as `t downarrow0`; the second diverges as `t upward infinity`; their minimum is uniformly bounded. Its exact worst point is

`t_*=2^(-1/4)`,                                                   (5.4)

where the two terms agree, giving

`boxed: sup_{t>0} ||p_Q||_infinity <=6*2^(1/12)
       =6.356778566155... .`                                     (5.5)

This remains true after adding arbitrary outside dimensions and arbitrary outside-to-active couplings, and for arbitrary cap-one input laws with distant fragments or unbounded supports, because all such outside effects are absorbed by Lemma 2.1 as affine shifts. The family also shows why a single reciprocal-pivot certificate is the wrong closure object: one branch may become arbitrarily bad while the actual target remains controlled by a complementary whole-active resource.

## 6. Relation to the latest partner generic closure

The newest `account02/B14` result proves that exact algebraic zero pivots and rough/unbounded laws can be removed with no loss **provided the analytic constant is uniform along the approximating sequence**. Theorem 4.1 supplies precisely such a uniformity mechanism on the structured block (4.1): instead of a factor such as `|delta|^(-alpha)` or `R0^(-alpha)` alone, it yields a bound in terms of

`max{|delta|,R0}`.                                                (6.1)

Consequently a generic approximation may let either resource tend to zero without damaging the estimate as long as the complementary resource stays at target scale. This is a concrete repair of one near-degenerate interface identified in the partner's latest report.

It does **not** solve the general matrix problem because a bare hypothesis `s_3(A)>=1` has not been shown to force a principal block of form (4.1) with `|c|` and `max{|delta|,R0}` bounded below. In particular, dense configurations with no suitable zero-diagonal physical hyperbolic pair, or with the third spectral direction hidden in a bank not visible through the chosen receiver row, remain outside this theorem.

## 7. Remaining B14 implication

The law/support side of localization is now clean: generic/smooth compact reduction and outside-affine lifting preserve the exact constant. The next B14 structural task is to replace the special direct-sum block (4.1) by an aggregate statement valid when the hyperbolic pair has self-curvature and when the third direction can migrate through cross-couplings. The required analytic shape should remain a **max/aggregate certificate**, not a sum of reciprocal individual pivots, so that generic limits and remote-fragment laws remain zero-tax.

No law-uniform pointwise Fourier decay, post-rotation independence, arbitrary-joint coarea, bounded support diameter, fixed fragment count, or moment assumption was used.
