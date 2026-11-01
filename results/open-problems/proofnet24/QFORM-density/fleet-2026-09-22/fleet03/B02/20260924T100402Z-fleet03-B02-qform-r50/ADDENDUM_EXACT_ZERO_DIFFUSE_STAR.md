SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T10:04:02Z.
attacking: the exact-zero endpoint of the diffuse Schur-star survivor, using the fresh physical-row half-Riesz theorem while preserving arbitrary leaf curvature.

# fleet03/B02 r50 addendum — exact-zero diffuse Schur star is paid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T100402Z-fleet03-B02-qform-r50`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SOURCE-PINNED APPLICATION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**

This addendum keeps every quantifier of the owner target. All coordinates below are ORIGINAL independent coordinates with one-dimensional densities bounded by one. No rotation of the random variables, support regularity, moment hypothesis, Gaussianity, log-concavity, or deletion of nonzero quadratic curvature is used.

## 1. Immediate r50 frontier

The main r50 report proved that after a nonzero original scalar pivot `a=A_hh`, the exact Schur complement

`S=C-bb^T/a`

inherits

` s_2(S) >= s_3(A) >= 1.`

On the live large-diagonal branch `|a|>1/228`, the only residual-star geometry not paid there was

`|S_jj|<=1/228`,
`c_j:=||S[j,j^c]||_2>1/228`,
`max_(k!=j) S_jk^2 <= (1/2)c_j^2`.

The main report deliberately left the exact-zero point `S_jj=0` inside this survivor because its then-used concentrated-edge argument did not cover a fully diffuse row.

## 2. Fresh theorem that closes the exact-zero point

Fresh compatible source:

- repository: `yspennstate/math-open-problems`
- full commit: `f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260924T091804Z-fleet02-B01-qform-auto11/REPORT.md`
- theorem: `QFORM-ZERODIAG-ROW-HALFRIESZ-v1`.

That theorem states: for an arbitrary quadratic-plus-affine form `R` in independent cap-one ORIGINAL coordinates, if one physical coordinate `j` has zero quadratic diagonal and off-diagonal row norm `c_j>0`, then, with completely arbitrary quadratic curvature among all remaining coordinates,

`H_(1/2)(R):=sup_s E|R-s|^(-1/2) <= 2^(11/4)c_j^(-1/2).`       (2.1)

Its proof conditions on all coordinates except the physical hub `X_j`; the hub then enters linearly. A one-dimensional bathtub bound is followed by the Rogozin--Ball density bound for the literal linear form in the remaining independent coordinates. Thus the theorem is compatible with the live correction against law-uniform scalar quadratic phase decay and does not require a rotated product law.

## 3. Actual r50 inequality

In r50 the outer original coordinate was completed exactly:

`Q=a(X_h+m(Y))^2+R(Y)`.

The exact scalar-square density kernel gives

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R).`                    (3.1)

Now impose the exact-zero diffuse-star endpoint

`S_jj=0`, `c_j=||S[j,j^c]||_2>1/228`.                           (3.2)

Applying (2.1) to the full Schur form `R`, including every leaf-leaf coefficient, and inserting it into (3.1) yields

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) (|a| c_j)^(-1/2).
}`                                                               (3.3)

At the live r50 scale `|a|>1/228` and `c_j>1/228`,

`boxed:
 ||p_Q||_infinity
 < 228*2^(11/4)
 = 1533.7950614227752.
}`                                                               (3.4)

This is an essential-density bound. Neither the row half-Riesz theorem nor the outer square peel by itself proves continuity, so no new continuity claim is made here.

The row-diffuseness condition `max S_jk^2 <= c_j^2/2` was not needed for this exact-zero payment. Therefore **every** exact-zero residual hub with `c_j>1/228` is paid, concentrated or diffuse.

## 4. Sharpened true frontier

The surviving r50 large-diagonal branch is now genuinely punctured:

`boxed:
 0 < |S_jj| <= 1/228,
 ||S[j,j^c]||_2 > 1/228,
 max_(k!=j) S_jk^2 <= (1/2)||S[j,j^c]||_2^2,
 s_2(S)>=1.
}`                                                               (4.1)

The exact-zero endpoint no longer belongs to the debt. One must not pass from (3.4) to (4.1) by continuity in the coefficient `S_jj`: the source theorem is an exact linear-hub statement, while a nonzero quadratic hub can create a double-root singularity after conditioning. A separate averaged or two-level argument is still required for the punctured interval.

The main r50 report already supplied the required equation-level use of the designated fleet04/B02 result: on a zero-diagonal principal-triple overlap, its Fourier-L2 theorem plus the r50 diffuse-Schur L-infinity exit gives

`||p_Q||_4 <= 27.734180732 |det H0|^(-1/12),`

with continuity on that exact partner overlap. This addendum does not enlarge that scope.

## 5. Status

- Full unrestricted QFORM: **OPEN**.
- Full-target continuity: **OPEN**.
- Target-wide universal unweighted `integral |phi_Q|`: **OPEN / not refuted**.
- New result here: exact-zero residual-star endpoint is uniformly paid by (3.3), and by `<1533.796` at the live r50 scale.
- Next B02 implication: `QFORM-SCHUR-PUNCTURED-DIFFUSE-STAR-PLUS-SECOND-DIRECTION-L1-OR-HALFRIESZ-v1`.
