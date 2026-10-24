SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T00:54:11Z.
attacking: after detecting that the run's first conditional half-Riesz calculation duplicated a stronger earlier B16 theorem, change mechanism on the SAME target and test the first unpaid near-coloop implication by an authentic product-source obstruction to hub-first absolute root integration.

# account03/B16 r38 — authentic near-coloop hub-first trace obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T005411Z-account03-B16-QFORM-r38`  
**Role:** Projection-product interaction  
**Status:** `NEW SOURCE-VALID MECHANISM OBSTRUCTION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** no new full density theorem is claimed in this run. The unrestricted QFORM density bound remains open, and global continuity remains open.

## 1. Owner target and exact point attacked

The target is the unrestricted assertion that for independent real original-coordinate variables with probability densities at most one, every real symmetric matrix having at least three eigenvalues of modulus at least one produces a quadratic form with universally bounded density. No moment, compact-support, log-concavity, connected-support, Gaussianity, centeredness, diagonal-basis independence, or post-rotation independence may be inserted.

The current exact-rank-three B16 hard chamber contains a physical near-coloop. In the notation of the preceding B16 run `math-open-problems@bdbe6e38a3ee3d586e8e6119e518c573310253fb`, write

`A=R Lambda R^T`, `R^T R=I_3`,

with a literal physical hub row

`r_0=sqrt(c)e`, `c>63/64`,

and leaf rows

`r_j=s_j e+p_j e_2+q_j e_3`.

The earlier source-valid theorem already pays the endpoint `a=e^T Lambda e=0` by `<7.6`, and for `a!=0` gives

`||p_Q||_infinity <= 4 sqrt(2e)c^(-1/2)(|a| |det Lambda|)^(-1/4)`.

Thus `|a det Lambda|>=2^-12` is already paid by `<76`; the remaining scalar-pivot collar is

`0<|a det Lambda|<2^-12`.                                      (1.1)

The purpose of the present run is not to repeat that estimate. It asks whether one can bridge (1.1) to the exactly paid zero-pivot endpoint by first integrating the physical hub as a scalar quadratic, replacing its source density by the cap one, and then controlling the resulting positive half-Riesz trace using the genuine bounded-density projection theorem.

The answer is **no even on an authentic product-source near-coloop family satisfying the full owner spectral condition**.

## 2. Why the early scratch file is not a new claim

The immutable early file of this run derived a generic conditional-shift estimate from `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`. On the source refresh it became clear that this was a weaker re-derivation of the already committed B16 sign-free theorem above: the prior diffuse-frame constant is `4 sqrt(2e)`, while the scratch route only recovered a much larger constant.

That early file is therefore retained only as immutable failed/duplicate work. It is **superseded and not counted as this run's mathematical advance**. In accordance with the owner instruction to change mechanism after non-progress, the rest of the run switches to a source-valid no-go construction for the hub-first trace itself.

## 3. Exact product-source near-coloop family

Fix

`N=128`, `c=127/128`, `delta=1/128`.                            (3.1)

Take `1+3N=385` mutually independent variables, all uniform on `[-1/2,1/2]`, hence each with probability density exactly one on its support. Denote the hub by `X_0`, and split the leaves into three disjoint banks

`S_1,...,S_N`, `P_1,...,P_N`, `Q_1,...,Q_N`.

Define the `385 x 3` Parseval frame `R` by the rows

`r_0=(sqrt(c),0,0)`,

`r_(S_i)=(sqrt(delta/N),0,0)`,

`r_(P_i)=(0,1/sqrt(N),0)`,

`r_(Q_i)=(0,0,1/sqrt(N))`.                                      (3.2)

The three column supports are disjoint, and

`c+delta=1`,
`N*(1/N)=1`.

Therefore

`R^T R=I_3`.                                                     (3.3)

The hub is a true near-coloop:

`c=127/128>63/64`.                                               (3.4)

Every leaf transverse leverage is either zero or

`1/N=1/128<1/64`,                                                (3.5)

so this family lies inside the diffuse-transverse chamber rather than escaping through a heavy transverse physical row.

For `0<a<2^-14`, set

`Lambda_a = [[a,2,0],[2,0,0],[0,0,1]]`.                         (3.6)

Its determinant is

`det Lambda_a=-4`,                                               (3.7)

so

`0<|a det Lambda_a|=4a<2^-12`,                                  (3.8)

exactly the unpaid punctured scalar-pivot collar.

The eigenvalues of `Lambda_a` are

`1`,
`lambda_+(a)=(a+sqrt(a^2+16))/2`,
`lambda_-(a)=(a-sqrt(a^2+16))/2`.                               (3.9)

For every `0<a<=3`,

`lambda_+(a)>=1`, `|lambda_-(a)|>=1`;

indeed `|lambda_-|>=1` is equivalent to `sqrt(a^2+16)>=a+2`, hence to `a<=3`. Thus every matrix

`A_a=R Lambda_a R^T`                                             (3.10)

has three eigenvalues of modulus at least one and is an **exact owner-target matrix**.

## 4. The actual quadratic and the authentic projection

Define

`S=sqrt(delta/N) sum_i S_i`,
`U=(1/sqrt(N)) sum_i P_i`,
`V=(1/sqrt(N)) sum_i Q_i`,
`Y=sqrt(c)X_0+S`.                                                (4.1)

Then

`Q_a=X^T A_a X = aY^2+4YU+V^2`.                                (4.2)

No random coordinate has been rotated. The random variables `S,U,V` come from disjoint original source banks and are actually mutually independent; this is stronger than what the general theorem may assume.

The coefficient rows defining `(U,V)` are orthonormal. Therefore the actual two-dimensional bounded-density projection theorem applies directly and gives

`||p_(U,V)||_infinity<=2`.                                      (4.3)

In this special construction `U` and `V` are even independent copies of the normalized sum of `N` unit-interval variables. The obstruction below therefore does not arise from a fake joint law, a post-rotation independence claim, or a failure of the projection theorem.

## 5. Exact scalar-root discriminant and cancellation of the shared longitudinal source

Treat (4.2) as a quadratic polynomial in the literal physical hub `X_0`. Expanding `Y=sqrt(c)X_0+S` gives

`Q_a = ac X_0^2 + 2 sqrt(c)(aS+2U)X_0`
`      + aS^2+4SU+V^2`.                                        (5.1)

At target `t=0`, one quarter of the ordinary root discriminant is

`c[(aS+2U)^2-a(aS^2+4SU+V^2)]`
`=c(4U^2-aV^2)`.                                                (5.2)

The complete `S` dependence cancels exactly. This is the same Schur/discriminant mechanism used by the positive B16 result, but here it reveals the endpoint obstruction.

If, at this point, one replaces the actual hub density at the roots by the cap `1`, the sum of the at-most-two root contributions is bounded by the positive trace

`T_a(0):=c^(-1/2) E[(4U^2-aV^2)_+^(-1/2)]`.                     (5.3)

Any hub-first proof that takes this absolute scalar-root majorant and then tries to close the estimate solely from the law of the genuine projection `(U,V)` must uniformly bound (5.3).

It cannot.

## 6. Main result: the authentic hub-first trace diverges logarithmically

### Proposition `QFORM-AUTHENTIC-NEARCOLOOP-HUB-FIRST-TRACE-NONUNIFORM-v1`

For the valid product-source owner-target family (3.1)-(4.2),

`T_a(0) -> infinity` as `a downarrow 0`.

More precisely, there are fixed constants `eta>0` and `m>0`, depending only on the fixed choice `N=128` and not on `a`, such that for every `0<a<min(1/4,2^-14)`,

`T_a(0) >= c^(-1/2) (m^2 eta/4) log(1/(2 sqrt(a)))`.             (6.1)

Consequently the positive hub-first half-Riesz trace grows at least logarithmically throughout an authentic exact-target near-coloop family even though the joint projection `(U,V)` obeys the genuine universal density cap (4.3).

### Proof

Let `f_N` denote the density of

`N^(-1/2)(Z_1+...+Z_N)`

for iid `Z_i~Unif[-1/2,1/2]`. Since `N>=2`, convolution gives a continuous density. The origin is in the interior of the convolution support and the convolution is strictly positive there. Hence there exist fixed `eta>0` and `m>0` such that

`f_N(x)>=m` for `|x|<=eta`.                                     (6.2)

Both `U` and `V` have density `f_N`, and they are independent because their original-coordinate banks are disjoint.

Fix `0<a<1/4`. Restrict the expectation in (5.3) to

`eta/2 <= v <= eta`,
`sqrt(a) eta <= u <= eta/2`.                                   (6.3)

On this rectangle, `v<=eta` and `u>=sqrt(a)eta`, so

`4u^2-av^2 >= 4a eta^2-a eta^2 =3a eta^2>0`.                   (6.4)

Also

`sqrt(4u^2-av^2)<=2u`,                                          (6.5)

and therefore

`(4u^2-av^2)^(-1/2) >= 1/(2u)`.                                (6.6)

Using (6.2), independence, and positivity,

`T_a(0)`
`>= c^(-1/2) m^2 integral_(eta/2)^eta dv`
`                 integral_(sqrt(a)eta)^(eta/2) du/(2u)`
`= c^(-1/2) (m^2 eta/4) log(1/(2 sqrt(a)))`.                    (6.7)

This tends to infinity as `a downarrow0`, proving the proposition. QED.

## 7. What the proposition does and does not say

This is **not a counterexample to QFORM**. The quantity in (5.3) is the standard cap-one upper majorant obtained after discarding the actual values of the hub density at the two roots. Its divergence shows that this proof route is too lossy; it does not prove that the true density of `Q_a` diverges.

It is stronger than the earlier caps-only obstruction in one important sense. Every ingredient here comes from the permitted source class:

- all physical inputs are independent;
- every physical density is at most one;
- the matrix has three eigenvalues of modulus at least one;
- the physical hub is in the true near-coloop collar;
- every transverse leaf leverage is below `1/64`;
- `(U,V)` is an actual orthogonal product projection and satisfies the real projection theorem;
- there is no invented dependent `(Y,U,V)` law.

Thus the first missing implication cannot be repaired by saying that the earlier caps-only example was not source-realizable. Even with authentic product provenance, **integrate the nonzero quadratic hub, replace the root densities by their supremum, and then average an indefinite projection half-potential** is nonuniform as the pivot tends to zero.

The mechanism change forced by this proposition is sharp: a successful punctured-to-zero bridge must retain more information about the hub/source overlap before taking the positive root trace, or work on the Fourier/TT* side where source-bank phases and the shared frequency remain coupled.

## 8. Relation to the phase-weighted two-bank theorem

The newest compatible complementary B16 result read in this run is account02/B16

`math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T225009Z-account02-B16-QFORM-r37/REPORT.md`.

It proves the phase-weighted punctured two-bank receiver

`||p_Q||_infinity <= 3[L_H K_2 K_3/|alpha epsilon lambda|]^(1/3)` (8.1)

with a continuous `C_0` density, while allowing arbitrary same-bank phases. It also proves a source-valid obstruction to law-uniform perturbative comparison in `epsilon`.

The present proposition rules out a different fallback at the same interface: taking `epsilon` or the small hub pivot to zero by reverting to a positive scalar-root half-potential of the authentic projection. Together, the two obstructions isolate the remaining mechanism more narrowly: the proof must be nonperturbative in the vanishing coupling **and** must keep the shared product-source information through the relevant Hilbert/TT* pairing instead of converting it to a pointwise positive trace.

## 9. Designated account04/B16 result applied to an actual inequality

The designated partner result is account04/B16

`QFORM-PHYSICALPAIR-BANK-OVERLAP-v1`,
`math-open-problems@a70c05e517e8a195a31ab4f4c301c672d1c8d4e6`.

On the live three-bank packet it proves

`||p_Q||_infinity <=9.200275`
` [D |det Lambda| tau det G_b]^(-1/5)`.                          (9.1)

If a live bank satisfies its actual super-volume gate

`det G_b >= W_b s^2/(64 D tau)`,                               (9.2)

while

`W_b>61/1728`, `|det Lambda|>=s^3`, `s>=1`,                    (9.3)

then

`D |det Lambda| tau det G_b`
`>= W_b s^5/64`
`> (61/1728)s^5/64`.                                            (9.4)

Substitution into (9.1) gives the concrete live bound

`||p_Q||_infinity`
`<9.200275(64*1728/61)^(1/5)s^(-1)`
`=41.255284... s^(-1)`
`<=41.256`.                                                      (9.5)

This is the required partner application at an actual target inequality. It uses a literal physical pair and an original-coordinate residual bank, not post-rotation independence.

Therefore the r38 obstruction matters only downstream of the already-paid partner branch. If the overlap gate (9.2) holds, (9.5) exits. In its complement, account04/B16 reduces the live packet to shear-flat or heavy-normalized-row intermediate-volume banks. The proposition above shows that the complementary small-pivot state cannot then be closed merely by collapsing back to the hub-first positive root trace, even when the residual projection is as clean as an orthogonal product projection.

## 10. First remaining B16 implication

The next exact implication is now sharpened to

**`QFORM-OVERLAP-AWARE-PUNCTURED-HUB-TTSTAR-v2` (OPEN):**

> In the exact-rank-three near-coloop complement of the account04/B16 overlap gate, retain the common hub/source phase and the two-bank source provenance through a vector-valued or overlap-aware TT* estimate that is uniform as the puncture/pivot tends to zero. The estimate must not freeze the shared physical projection and use Minkowski (r34 obstruction), must not compare the punctured characteristic function perturbatively with the zero-coupling form (account02/B16 r37 obstruction), and must not first replace the hub roots by the cap-one positive half-Riesz trace (the present r38 obstruction).

The earlier disjoint projected-volume route also leaks the near-coloop mass by the r37 Pluecker barrier. A successful proof must therefore exploit **overlap before absolute values** rather than seek another disjoint projection certificate.

Arbitrary additional spectral components beyond exact rank three remain a separate full-target interface after this local closure. No claim is made that the exact-rank-three obstruction solves that global stability problem.

## 11. Deterministic verification

`CHECK.py` verifies without Monte Carlo:

- `c=127/128>63/64`;
- `delta=1/128` and `c+delta=1`;
- transverse leverage `1/128<1/64`;
- the constructed frame has exact column Gram `I_3`;
- `det Lambda_a=-4` and the three active eigenvalues have modulus at least one throughout the checked admissible range;
- the rectangle used in (6.3) satisfies positivity of `4u^2-av^2` and the lower integrand bound `>=1/(2u)`;
- the designated account04/B16 constant in (9.5) is `<41.256`.

The committed deterministic output ends `STATUS=PASS`.

## 12. Status

**New proved result:** `QFORM-AUTHENTIC-NEARCOLOOP-HUB-FIRST-TRACE-NONUNIFORM-v1` — a genuine original-product, three-large-eigenvalue, diffuse-near-coloop family on which the scalar-root cap majorant diverges at least logarithmically as the nonzero hub pivot tends to the already-paid zero-pivot endpoint.

**Designated partner:** applied at (9.1)-(9.5), giving `<41.256` on the actual account04/B16 super-volume gate.

**Full QFORM:** `OPEN / NOT PROVED / NOT DISPROVED`.

**Continuity:** global continuity remains open. This run proves no new continuity theorem; account02/B16's punctured TT* branch and account04/B16's overlap branch retain their previously proved branchwise `C_0` continuity.

**Brain status:** `WITHOUT_VERIFIED_BRAIN`. Repository source retrieval and publication were performed, but no authenticated native brain receiver/use was verified.
