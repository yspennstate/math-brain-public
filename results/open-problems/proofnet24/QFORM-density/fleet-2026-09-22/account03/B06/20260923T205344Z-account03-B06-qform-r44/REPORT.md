SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T20:53:44Z.
attacking: the near-rank-one two-hub collar; separate definite ellipse geometry from indefinite hyperbola geometry, prove a product-weighted arcsine receiver uniform through the definite null limit, and identify the exact anchored third-curvature matrix that the indefinite branch must spend.

# account03/B06 r44 — definite near-null curved-fiber receiver and indefinite third-curvature obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** `2026-09-22.15`; programme revision `2026-09-22.5`  
**Assignment:** curved fiber integration  
**Status:** `NEW SUPPORTING THEOREM + NEW CORRECTION + EXACT THIRD-CURVATURE IDENTITY / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Nothing below assumes Gaussianity, log-concavity, moments, compact support, connected support, iid laws, post-rotation independence, finite ambient rank, or a diagonal spectral basis. The positive theorem uses literal original independent coordinates and an original-coordinate product bank. Continuity is not claimed for the new arcsine branch.

## 1. Fresh source state and predecessor


The immediate B06 predecessor is

`yspennstate/math-open-problems@461dac093ac693e6d38911e828fd96557ed56fd2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T202712Z-account03-B06-qform-r43/REPORT.md`.

It proved the exact rank-one hub innovation theorem and showed by an explicit two-eigenvalue example that a small nonzero hyperbolic hub cannot be handled if the completed environmental remainder is simply declared arbitrary. Its next debt was precisely the near-rank-one collar while retaining genuine third curvature.

The one-dimensional original-product marginal theorem used below is source-pinned in account01/B18 r21:

`yspennstate/math-open-problems@406753a39f5fbaf78396b31075f36ae5682ef3ad`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T015618Z-qform-B18-a01-r21/REPORT.md`.

For any nonzero coefficient vector `gamma` and independent cap-one original coordinates `Z`, it gives

`||p_(gamma dot Z)||_infinity <= sqrt(2)/||gamma||_2`.             (1.1)

The completed designated-partner theorem actually applied in Section 6 is account04/B06 r1:

`yspennstate/math-open-problems@f24c8db8946d54f4da2d11898697913af766ad32`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260923T184145Z-account04-B06-QFORM-r1/REPORT.md`.

## 2. Arcsine maximal lemma: integrate the complete curved shell before taking a maximum

For a probability density `f` on the line with `0<=f<=1`, define

`A f(v) := sup_(r>0) integral_(|y-v|<r)
                      f(y)/sqrt(r^2-(y-v)^2) dy`.                 (2.1)

Let the centered Hardy--Littlewood maximal function be

`M f(v) := sup_(r>0) (1/(2r)) integral_(v-r)^(v+r) f(y)dy`.       (2.2)

### Lemma 2.1 — `QFORM-ARCSINE-MAXIMAL-WEAK2-v1`

For every such probability density,

`A f(v) <= 4 sqrt(M f(v))`,                                      (2.3)

and therefore

`|{v: A f(v)>lambda}| <= 48/lambda^2`.                           (2.4)

Also `A f(v)<=pi` everywhere. Consequently, if a random variable `V` has density cap `K`, then

`E A f(V) <= 8 sqrt(3K)`.                                        (2.5)

#### Proof

Fix `v,r`, and split `I=(v-r,v+r)` into its left and right halves. Write `m_-` for the `f`-mass of the left half. There

`r^2-(y-v)^2=(y-(v-r))(v+r-y) >= r(y-(v-r))`,

so

`integral_left f(y)/sqrt(r^2-(y-v)^2)dy
 <= r^(-1/2) integral_left f(y)/sqrt(y-(v-r))dy`.                 (2.6)

Among functions bounded by one with mass `m_-`, the decreasing kernel `s^(-1/2)` is maximized by filling `[0,m_-]`; hence the last integral is at most `2 sqrt(m_-)`. The right half gives the same estimate with mass `m_+`. Thus

`integral_I ...
 <=2 r^(-1/2)(sqrt(m_-)+sqrt(m_+))
 <=4 sqrt((m_-+m_+)/(2r))
 <=4 sqrt(Mf(v))`,                                                (2.7)

which proves (2.3).

For completeness, the one-dimensional centered maximal function obeys the safe weak-(1,1) estimate

`|{Mf>s}| <=3 ||f||_1/s=3/s`:                                    (2.8)

choose for each point of the level set a witnessing centered interval, extract a disjoint Vitali subcollection, and cover the level set by the corresponding triple dilates. Applying (2.8) with `s=lambda^2/16` gives (2.4).

Because `f<=1`, the full arcsine kernel has mass `pi`, so `Af<=pi`. If `p_V<=K`, layer cake and (2.4) give

`E Af(V)
 <= integral_0^pi min(1,48K/lambda^2) dlambda
 <=2 sqrt(48K)
 =8 sqrt(3K)`.                                                    (2.9)

QED.

The important feature is the order of operations: the whole elliptical shell is integrated against the physical product density first. The only later maximum is the one-dimensional arcsine maximal operator, whose weak-`L^2` distribution is then integrated against the law of the shell centre. This avoids the dimension-growing unrestricted spectral-fiber supremum prohibited by the live correction ledger.

## 3. Definite two-hub theorem, uniform through the null determinant limit

Let `X,Y` be independent original-coordinate variables with densities at most one. Let `Z=(Z_j)` be an independent original-coordinate product bank, each coordinate again having density at most one. Let

`H=[[a,b],[b,d]]`,
`A(Z)=alpha dot Z+a_0`,
`B(Z)=beta dot Z+b_0`,                                            (3.1)

and let `R(Z)` be an arbitrary measurable real function. Consider

`Q=aX^2+2bXY+dY^2+2A(Z)X+2B(Z)Y+R(Z)`.                           (3.2)

### Theorem 3.1 — `QFORM-DEFINITE-HUB-ARCSINE-v1`

Assume the physical hub `H` is definite (equivalently, for a nonsingular real symmetric `2 x 2` matrix, `det H>0`). Multiply the entire form by `-1` if necessary so that `H` is positive definite; this does not change the density supremum. Then `a>0`. Set

`Gamma:=a beta-b alpha`.                                          (3.3)

If `Gamma!=0`, then `Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <=8*2^(1/4)*sqrt(3) ||Gamma||_2^(-1/2)
 =16.4781371513... ||Gamma||_2^(-1/2).`                           (3.4)

The bound is independent of `det H` and therefore remains uniform as a definite hub tends to rank one. It retains the arbitrary same-bank remainder `R(Z)` exactly.

#### Proof

After the harmless global sign change, take `H` positive definite and put

`delta:=d-b^2/a=det(H)/a>0`,
`C(Z):=B(Z)-(b/a)A(Z)`.                                          (3.5)

Complete first in the literal original coordinate `X`, then in `Y`:

`Q
 =a[X+(bY+A)/a]^2
  +delta[Y+C/delta]^2
  +S(Z)`,                                                        (3.6)

where

`S(Z):=R(Z)-A(Z)^2/a-C(Z)^2/delta`.                              (3.7)

Condition on `(Y,Z)`. The translated variable `X+(bY+A)/a` still has a conditional density bounded by one. The elementary square pushforward formula therefore gives, for almost every `t`,

`p_Q(t)
 <=a^(-1/2) E [t-S(Z)-delta(Y+C/delta)^2]_+^(-1/2).`              (3.8)

Now condition only on `Z`. If `q=(t-S(Z))/delta<=0`, the inner contribution is zero. If `q>0`, write `r=sqrt(q)` and `v=-C/delta`. Then the `Y` integral in (3.8) is exactly at most

`delta^(-1/2) A f_Y(v)`.                                        (3.9)

Thus

`p_Q(t)
 <=(a delta)^(-1/2) E_Z A f_Y(-C(Z)/delta).`                     (3.10)

Let `M=||p_C||_infinity`. The random centre `V=-C/delta` has density cap `delta M`. Lemma 2.1 gives

`E Af_Y(V) <=8 sqrt(3 delta M)`,                                 (3.11)

and hence

`||p_Q||_infinity <=8 sqrt(3) a^(-1/2) sqrt(M)`.                 (3.12)

The coefficient vector of `C` is

`gamma=beta-(b/a)alpha=Gamma/a`.                                 (3.13)

By the source-valid original-product projection theorem (1.1),

`M <=sqrt(2)/||gamma||_2
   =sqrt(2)|a|/||Gamma||_2`.                                     (3.14)

Substitute (3.14) in (3.12). The factor `a` cancels exactly and gives (3.4). QED.

### Coordinate-symmetric version

Let `E` be the `2 x m` slope matrix with rows `alpha^T,beta^T` and define

`J_H:=||adj(H)E||_F`.                                             (3.15)

The two rows of `adj(H)E` are

`d alpha-b beta`, `a beta-b alpha`.                              (3.16)

For a definite hub either physical coordinate may be chosen as the first pivot. Select the larger of these two row norms; it is at least `J_H/sqrt(2)`. Theorem 3.1 after the corresponding swap yields

`boxed: ||p_Q||_infinity <=8 sqrt(6) J_H^(-1/2).`                (3.17)

This is a coordinate-symmetric definite-side continuation of r43's exact-rank-one innovation payment.

### Actual r43 collar

On the live r43 branch where the chosen innovation obeys

`||Gamma||_2 >=2^(-12)`,                                         (3.18)

Theorem 3.1 gives, for every **definite** nonzero hub no matter how small its determinant,

`boxed: ||p_Q||_infinity <1054.601.`                             (3.19)

Every same-bank environmental quadratic term and the complete nonzero tail remain inside `R(Z)`.

The exact rank-one endpoint was already better in r43 (`<430.539` under the same numerical innovation threshold). The new content is that the entire definite collar is now paid uniformly as `det H ->0`.

Continuity is not asserted by this proof. It establishes an essentially bounded density.

## 4. Indefinite arbitrary-remainder continuation is false even with robust innovation

The sign condition in Theorem 3.1 is not cosmetic. On the hyperbolic side, a moving critical value can be aligned by the same-bank remainder and recreate the logarithmic rank-two singularity even when the slope innovation is exactly one.

### Proposition 4.1 — `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`

For every `0<epsilon<=1`, let `X,Y,C` be mutually independent `Uniform[-1/2,1/2]` variables and set

`Q_epsilon
 :=X^2-epsilon Y^2+2CY-C^2/epsilon
 =X^2-epsilon(Y-C/epsilon)^2`.                                   (4.1)

The physical hub is `diag(1,-epsilon)`, the slope data are `alpha=0`, `beta=1`, and therefore the innovation `Gamma=1`. Nevertheless `Q_epsilon` has an unbounded density.

#### Proof

Fix `c` with `|c|<=epsilon/4` and put `u=Y-c/epsilon`. The shifted `Y` interval contains `[-1/4,1/4]`. For `0<t<3/16` and `|u|<=1/4`,

`0<t+epsilon u^2<1/4`.                                           (4.2)

Because `X` is uniform on `[-1/2,1/2]`, the density of `X^2` is exactly `s^(-1/2)` on `(0,1/4)`. Therefore

`p_(Q_epsilon | C=c)(t)
 >= integral_(-1/4)^(1/4) du/sqrt(t+epsilon u^2)
 = (2/sqrt(epsilon))
    asinh(sqrt(epsilon)/(4 sqrt(t))).`                            (4.3)

The interval of such `c` has probability `epsilon/2`, hence

`p_(Q_epsilon)(t)
 >=sqrt(epsilon)
    asinh(sqrt(epsilon)/(4 sqrt(t)))`,                            (4.4)

which diverges as `t downarrow0`. Thus the essential supremum is infinite. QED.

This is **not** a counterexample to QFORM. In variable order `(X,Y,C)` the matrix is

`[[1,0,0],
  [0,-epsilon,1],
  [0,1,-1/epsilon]]`,                                            (4.5)

whose spectrum is

`{1,-(epsilon+epsilon^(-1)),0}`.                                 (4.6)

It has only two nonzero eigenvalues. Proposition 4.1 refutes only the tempting intermediate statement that a small indefinite hub plus robust slope innovation can absorb an arbitrary completed remainder. A valid target proof on the indefinite side must spend the target's genuine third curvature.

This correction is stronger than the r43 arbitrary-remainder obstruction: the first hub diagonal is now order one and the innovation is fixed at one. The obstruction is specifically the hyperbolic critical-value geometry.

## 5. Exact anchored critical-curvature matrix

The preceding failure shows exactly what cannot be hidden in `R`. The correct third-curvature object is algebraic and consists of the entire bank of physical `3 x 3` minors anchored at the two hubs.

Let a symmetric block matrix be

`M=[[H,E],[E^T,Cenv]]`,                                          (5.1)

where `H` is `2 x 2`, `E` is `2 x m`, and `Cenv` is `m x m`. Define

`K_H:=det(H) Cenv-E^T adj(H) E`.                                 (5.2)

### Lemma 5.1 — `QFORM-ANCHORED-CRITICAL-CURVATURE-ID-v1`

For every environment indices `j,k`,

`boxed:
 (K_H)_(jk)
 =det M[{hub1,hub2,j},{hub1,hub2,k}].`                            (5.3)

If `H` is invertible, `K_H/det(H)` is exactly the quadratic matrix of the environmental critical-value remainder obtained after completing both hub variables:

`Cenv-E^T H^(-1)E = K_H/det(H)`.                                (5.4)

If `H` has rank one, write `H=lambda u u^T` with `u` unit and let `n` be a unit null vector. Then

`adj(H)=lambda n n^T`,
`K_H=-lambda (n^T E)^T(n^T E)`,                                 (5.5)

and with `J_H=||adj(H)E||_F`,

`boxed: ||K_H||_F=J_H^2/|lambda|.`                              (5.6)

#### Proof

For invertible `H`, the determinant of the `3 x 3` block containing the two hubs, environment row `j`, and environment column `k` is the Schur determinant

`det(H)[(Cenv)_(jk)-E_(.,j)^T H^(-1) E_(.,k)]`,                  (5.7)

which is exactly (5.2). Both sides are polynomial in the entries of `H`, so (5.3) holds for singular `H` as well. Equation (5.4) is the same identity written as a matrix equality.

For a rank-one symmetric `2 x 2` matrix, the adjugate has the nonzero eigenvalue `lambda` on the null line, hence `adj(H)=lambda nn^T`. Equations (5.5) follow immediately. The Frobenius norm of the rank-one matrix `(n^T E)^T(n^T E)` is `||n^T E||_2^2`, while `J_H=|lambda| ||n^T E||_2`, giving (5.6). QED.

This identifies a continuous algebraic bridge between r43's rank-one innovation currency and the third-minor bank that must be retained when `det H` is small but nonzero. In particular, the indefinite obstruction of Section 4 succeeds only because its completed critical remainder has precisely the cancellation needed to leave `K_H` rank deficient enough to supply only two nonzero global eigenvalues.

## 6. Designated account04/B06 theorem applied at the new anchored-curvature identity

The designated partner account04/B06 r1 proves `QFORM-BANKWISE-TRIPLE-CURVATURE-v1`. In its live exact-rank-three chamber, for an invertible indefinite physical pair `H=B`, the Schur remainder is

`Cenv-E^T B^(-1)E=lambda h h^T`.                                (6.1)

Therefore the new identity (5.4) gives **exactly**

`K_B=det(B) lambda h h^T`.                                       (6.2)

On a partner bank `J_b`, writing `W_b=||h_b||_2^2`,

`||K_(B,b)||_F=D |lambda| W_b`,                                  (6.3)

where `D=|det B|`. The partner live packet gives

`D |lambda|>=1/4`,
`W_1 W_2 W_3>61/1728`.                                           (6.4)

Choose a bank of maximal normal mass. Then

`W_max>(61/1728)^(1/3)=0.328041431925...`,                        (6.5)

so the complete anchored third-minor bank on that physical bank satisfies the actual inequality

`boxed:
 ||K_(B,b_max)||_F
 >0.0820103579813.`                                               (6.6)

Thus the partner chamber contains a quantitatively robust **aggregate third-curvature bank** even before selecting any individual minor.

If that same maximal bank satisfies the partner's exact hypotheses

`max_k r_k^T G_b^(-1)r_k <=1/2`,
`det G_b >= W_b/64`,                                              (6.7)

then the completed account04/B06 theorem gives

`||p_Q||_infinity
 <=12[D|lambda|det G_b]^(-1/3)
 <110.480339847
 <110.481`,                                                       (6.8)

and supplies a continuous density on that branch.

If (6.7) fails, no conclusion is fabricated. The new information is that the unpaid branch now has (6.6) simultaneously with a specific heavy-leverage or shear-flat failure. This is a sharper input for the next indefinite near-null bridge than an unspecified third eigenvalue.

## 7. Checks

The companion checker records the exact constants and sanity-tests the anchored-minor identity and rank-one bridge on 5,000 random instances. Its output includes

`QFORM_B06_R44_CHECK_PASS`,

with maximum normalized discrepancies `1.30e-14` for (5.3) and `2.32e-16` for (5.6). These finite computations are only checks; Sections 2--6 contain the proofs.

## 8. What is now closed and what remains

The two-hub near-rank-one collar is now separated sharply by sign.

- **Exact rank one:** r43 pays robust innovation directly (`<430.539` at `||Gamma||>=2^-12`).
- **Definite nonzero determinant:** this run pays the entire collar uniformly (`<1054.601` at the same threshold), with arbitrary same-bank remainder and complete nonzero tail retained.
- **Indefinite nonzero determinant:** an arbitrary-remainder extension is impossible even when `Gamma=1`; the genuine third curvature must be used. The exact object to use is `K_H`, the entire anchored third-minor matrix, not one selected minor.
- **Partner exact-rank-three chamber:** the maximal original-coordinate bank has `||K||_F>0.0820103`; under the partner diffuse/transverse gates it is already density-paid by `<110.481` continuously.

The next exact B06 debt is therefore

`QFORM-INDEFINITE-NEARNULL-ANCHORED-K-RECEIVER-v1`:

start from small `det H<0`, retain the full hyperbolic pair-log geometry, and average the moving critical-value singularity jointly against the original-product structure encoded by a quantitatively nonzero `K_H`. The goal is a bound using an aggregate norm/volume of `K_H` that remains finite as `det H ->0-`, or a structural routing showing that failure activates the account04/B06 bankwise triple-curvature theorem, a physical-pair receiver, or a finite heavy-hub receiver. No environmental quadratic term may be replaced by an arbitrary remainder once doing so erases `K_H`.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** The new definite branch establishes absolute continuity and essential boundedness; continuity is only inherited on the separately scoped partner branch where account04/B06 proves it.
