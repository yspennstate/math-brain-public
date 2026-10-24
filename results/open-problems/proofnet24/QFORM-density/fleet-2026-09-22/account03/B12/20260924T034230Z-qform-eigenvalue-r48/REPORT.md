SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T03:42:30Z.
attacking: near-resonant signed spectral packets — quantitatively repair low singular carrier modes with the transverse Gram term, then route the repaired physical carrier through the completed five-mode density compiler.

# account03/B12 — near-resonance transverse repair and density stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T034230Z-qform-eigenvalue-r48`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The target remains the unrestricted statement: for independent ORIGINAL coordinates with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal density bound for `X^T A X`, or produce a valid counterexample.

No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, or pointwise quadratic van-der-Corput hypothesis is used below. A small coefficient action is never interpreted as a small random quadratic error.

The exact carrier decomposition used here is from account01/B12,

`yspennstate/math-open-problems@6bbaa340406b8febd0270e186cc79040af81872a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260924T012115Z-account01-B12-QFORM-auto11/REPORT.md`.

The designated partner result actually applied is account04/B12 r9,

`yspennstate/math-open-problems@71b7db02d3bd2f5cb6bf07e800caa6bd13a1a3e5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T021341Z-account04-B12-resonance-repair-r9/REPORT.md`.

For the final density step I use the completed account03/B12 r47 five-mode compiler,

`yspennstate/math-open-problems@8f9128b3f3ce222f941a3b138460658059957a83`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`.

Its source-valid conclusion is: if an ORIGINAL-coordinate bank `H`, `|H|=m>=5`, satisfies

`lambda_5((A^2)[H,H]) >= g^2>0`,

then, with

`K3 = 3*2^(4/3)*exp(1/3) = 10.550168831164775...`,

one has a continuous `C_0` density and

`||p_(X^TAX)||_infinity <= sqrt(24*pi*m + K3^2)/g`.             (1.1)

This run does not re-claim the analytic receivers underlying (1.1).

## 2. Exact spectral-packet carrier identity

Let `H` be `m` literal ORIGINAL coordinates and let `P:R^m -> R^n` be their coordinate embedding. Let the baseline symmetric matrix `A0` have full-column carrier

`M0=A0 P`, `G0=M0^T M0>0`.

Add an arbitrary signed spectral packet

`E=U Theta U^T`,

where the columns of `U` are orthonormal and `Theta` is an arbitrary real diagonal matrix. Following account01/B12, put

`V=P^T U`, `R=M0^dagger U`, `Pi=M0 M0^dagger`,
`U_perp=(I-Pi)U`,
`L=I_m + R Theta V^T`,
`W=U_perp Theta V^T`.

Then

`(A0+E)P = M0 L + W`,                                           (2.1)

and `M0^T W=0`. Therefore, with

`F=G0^(1/2)L`,

one has for every `x in R^m`

`||(A0+E)Px||^2 = ||Fx||^2 + ||Wx||^2`,                         (2.2)

and equivalently

`((A0+E)^2)[H,H] = F^T F + W^T W`.                              (2.3)

The partner r9 result exploited (2.3) when `L` had an exact kernel. The new theorem below allows an arbitrary *near-resonant low-singular subspace* and gives a sharper quantitative constant even in the exact-kernel case.

## 3. Main deterministic theorem

### Theorem 3.1 — `QFORM-NEAR-RESONANCE-TRANSVERSE-REPAIR-v1`

Let `1<=q<=m-1`. Let `K` be the right-singular subspace of `F` spanned by its `q` smallest singular directions, and let `K_perp` be its Euclidean orthogonal complement. Because `K` is a spectral subspace of `F^T F`,

`F K` is orthogonal to `F K_perp`.                               (3.1)

Define

`a = inf_{x in K_perp, ||x||=1} ||Fx|| = s_(m-q)(F)`,
`b = inf_{x in K,      ||x||=1} ||Wx||`,
`c = ||W P_(K_perp)||op`.                                       (3.2)

Assume `a>0` and `b>0`, and set

`S = a^2+b^2+c^2`,

`rho(a,b,c)^2 = [ S - sqrt(S^2-4 a^2 b^2) ]/2`.                (3.3)

Then

`boxed: s_m((A0+E)P) >= rho(a,b,c).`                            (3.4)

In particular,

`boxed: rho(a,b,c) >= ab/sqrt(a^2+b^2+c^2) >= ab/(a+b+c).`      (3.5)

Thus exact resonance is not required: arbitrarily small singular values of the relative gain on `K` are harmless provided the transverse packet is quantitatively injective on `K` and the complementary transverse leakage is controlled.

### Proof

Take a unit `x=x0+x1` with `x0 in K`, `x1 in K_perp`. Put

`u=||x0||`, `v=||x1||`, so `u^2+v^2=1`.

By (3.1) and the definition of `a`,

`||Fx||^2 = ||Fx0||^2+||Fx1||^2 >= a^2 v^2`.                   (3.6)

By the definitions of `b,c` and the triangle inequality,

`||Wx|| >= b u - c v`.                                         (3.7)

There are two cases.

**Case 1: `bu>=cv`.** From (2.2), (3.6), and (3.7),

`||(A0+E)Px||^2 >= a^2 v^2 + (bu-cv)^2`.

Writing `z=(u,v)^T`, the right side is

`z^T Q z`,

where

`Q = [[b^2, -bc],[-bc,a^2+c^2]]`.                              (3.8)

The trace and determinant of `Q` are

`tr Q=S`, `det Q=a^2 b^2`.

Hence its smaller eigenvalue is exactly `rho(a,b,c)^2`, and since `||z||=1`,

`||(A0+E)Px|| >= rho(a,b,c)`.                                  (3.9)

**Case 2: `bu<cv`.** If `c=0` this case is impossible because `b>0`. For `c>0`,

`v^2 > b^2/(b^2+c^2)`,

so (3.6) gives

`||(A0+E)Px||^2 > a^2 b^2/(b^2+c^2)`.                          (3.10)

It remains to compare (3.10) with `rho^2`. Let

`t0=a^2 b^2/(b^2+c^2)`

and let

`p(t)=t^2-S t+a^2b^2`.

A direct substitution yields

`p(t0) = -a^4 b^2 c^2/(b^2+c^2)^2 <=0`.                       (3.11)

Since the two roots of `p` are the eigenvalues of the positive matrix `Q`, (3.11) places `t0` between the roots. Therefore `t0>=rho^2`. Combining with (3.10) again gives (3.9).

Taking the infimum over all unit `x` proves (3.4).

For (3.5), if the eigenvalues of `Q` are `lambda_-<=lambda_+`, then

`lambda_- lambda_+=a^2b^2`, `lambda_+<=tr Q=S`,

so `lambda_- >= a^2b^2/S`. The second inequality in (3.5) is elementary. QED.

### Remarks

1. The small singular values of `F` *inside `K` do not appear in the lower bound*. They may be exactly zero or arbitrarily close to zero.
2. The theorem is sign-blind in `Theta`; all signs enter only through the deterministic matrices `F,W`.
3. The theorem uses the actual final coefficient matrix in ORIGINAL coordinates. It makes no probabilistic independence assertion after spectral rotation.
4. If `K=ker F`, this strictly sharpens the partner r9 lower bound `ab/[2(a+b+M)]`: since `c<=M`, (3.5) already gives at least `ab/(a+b+M)`, a factor-two improvement, while the exact `rho` can be much larger.

## 4. Arbitrary later signed spectrum and local-tail stability

Let the final symmetric matrix be

`A = A0 + E + S0 + T`,                                          (4.1)

where

`S0 P=0`                                                        (4.2)

but `S0` is otherwise arbitrary: its rank, signs, eigenvalue magnitudes, and complementary spectrum are unrestricted. Let the remaining symmetric addition `T` satisfy only the *local carrier action* bound

`||T P||op <= epsilon`.                                         (4.3)

The global norm `||T||op` may be arbitrarily large because its action away from `H` is not charged.

Rectangular Weyl applied to `(A0+E)P + TP` gives

`boxed: s_m(AP) >= [rho(a,b,c)-epsilon]_+.`                     (4.4)

Consequently, if `m>=5` and

`g=[rho(a,b,c)-epsilon]_+>0`,                                   (4.5)

then

`lambda_5((A^2)[H,H]) >= s_m(AP)^2 >= g^2`.                    (4.6)

Combining (4.6) with the completed five-mode compiler (1.1) gives:

### Corollary 4.1 — `QFORM-NEAR-RESONANCE-DENSITY-STABILITY-v1`

Under (2.1)-(4.5), for every independent cap-one product input,

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24*pi*m+K3^2)/g.`                                      (4.7)

The density has a representative in `C_0(R)`.

This is a density-level stability theorem for an arbitrary signed spectral packet at or near a finite-dimensional destructive resonance, followed by arbitrary carrier-invisible spectrum and an arbitrary further signed remainder whose *coefficient action on the physical carrier* is small. No random quadratic remainder is discarded.

## 5. Required partner application: account04/B12 r9

The completed partner report uses

`n=12`, `H={1,...,6}`,

`A0 = [[0,2I6],[2I6,0]]`,                                      (5.1)

and the rank-one signed packet

`u=(e1+e7)/sqrt(2)`, `E=-4 uu^T`.                              (5.2)

The partner computes exactly

`G0=4I6`,
`L=I6-e1 e1^T`,
`W=-2 e1 e1^T`.                                                 (5.3)

This is an exact resonance: `s_6(L)=0`. Take

`K=span{e1}`.

Then, in the notation of Theorem 3.1,

`F=2L`,
`a=2`, `b=2`, `c=0`.                                           (5.4)

Applying the new inequality at the partner's actual matrices gives

`rho(2,2,0)^2 = [8-sqrt(64-64)]/2 =4`,

hence

`boxed: s_6((A0+E)P_H) >=2.`                                   (5.5)

This recovers the partner's direct exact value, but now as an instance of a theorem that also covers near-resonant low singular subspaces.

The partner then permits simultaneously

`||E_low||op<=1/32`, `S P_H=0`, `||T P_H||op<=1/64`.           (5.6)

Thus the total charged local action is

`epsilon=1/32+1/64=3/64`,

and (4.4) gives the actual final-matrix inequality

`boxed: s_6(AP_H) >= 2-3/64 =125/64.`                           (5.7)

In particular

`lambda_5((A^2)[H,H]) >= (125/64)^2`.                           (5.8)

Applying the completed r47 five-mode density compiler with `m=6` and `g=125/64` yields

`boxed:
 ||p_Q||_infinity
 <= sqrt(144*pi + K3^2)/(125/64)
 = 12.156042452739065... <12.157.`                              (5.9)

The density is continuous and vanishes at infinity.

This strengthens the partner r9 displayed density cap `<654` on the same exact-resonant family. The gain comes from two completed improvements: the exact transverse-repair profile above and the five-mode E3/core compiler. No hypothesis of the target law is changed.

## 6. Near-resonant family, not merely exact resonance

The same partner geometry gives a transparent robust family. For `1<=j<=q<=5`, let

`u_j=(e_j+e_(6+j))/sqrt(2)`

and choose independent packet eigenvalues

`theta_j=-4+eta_j`, `|eta_j|<=1/2`.                             (6.1)

Let

`E=sum_(j<=q) theta_j u_j u_j^T`.

For the carrier `H={1,...,6}`, direct substitution into the account01 identity gives

`L = I6 + sum_(j<=q) (theta_j/4) e_j e_j^T`,
`W = sum_(j<=q) (theta_j/2) e_j e_j^T`.                         (6.2)

Take `K=span{e1,...,eq}`. Then

`a=2`,
`b=min_(j<=q) |theta_j|/2 >=7/4`,
`c=0`.                                                          (6.3)

Therefore Theorem 3.1 gives uniformly over all `q<=5` and all near-resonant choices in (6.1)

`boxed: s_6((A0+E)P_H) >= rho(2,7/4,0)=7/4.`                   (6.4)

The baseline-range term can be exactly singular (`eta_j=0`) or arbitrarily close to singular in as many as five physical directions at once, yet the transverse packet keeps the full six-dimensional physical carrier quantitative.

If any further arbitrary signed additions have aggregate local carrier action at most `1/4`, then

`boxed: s_6(AP_H)>=3/2`,                                       (6.5)

and the five-mode compiler gives the continuous bound

`boxed: ||p_Q||_infinity <= 15.828180277003993... <15.829.`     (6.6)

Additional carrier-invisible spectrum is completely unrestricted.

This family is illustrative only; Theorem 3.1 itself allows arbitrary signs and magnitudes in `Theta` whenever the deterministic parameters `a,b,c` are quantitative.

## 7. Deterministic consistency check

A seeded finite check generated 10,000 random square matrices `F` through random singular-value decompositions, chose `K` as a random-size bottom right-singular subspace, generated an independent rectangular `W`, and compared

`s_min([F;W])`

with `rho(a,b,c)` from (3.3). There were zero violations. The smallest observed numerical margin was

`0.0009979653641402075`.

The check is only a sanity test. The proof is the two-case argument in Section 3.

## 8. Exact remaining gap

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

This run removes a real instability in the additional-eigenvalue branch: a low-rank signed packet no longer needs to be separated from the finite Woodbury resonance set. Exact and near resonances are quantitatively harmless whenever the packet's transverse action repairs the corresponding low-singular right subspace.

The first unpaid implication is structural. Starting only from `s_3(A)>=1`, one must force a bounded ORIGINAL-coordinate carrier on which either:

1. the relative gain is quantitatively nonresonant;
2. the low-singular subspace has quantitative transverse repair `b>0` with manageable `c` as above; or
3. failure of both produces one of the already-paid physical pair, grouped-hub, projected-crossing, ridge, common-plane, or diffuse-volume exits.

No claim is made that the bare three-large-eigenvalue hypothesis supplies such a carrier automatically.
