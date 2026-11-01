SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-24T02:37:12Z.

# fleet02/B02 r11 — full-cut exterior propagation from the ultra-rank-two packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Run: `fleet02-B02-20260924T023712Z-r11`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**

The exact target remains the unrestricted one: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence hypothesis is used. Continuity is asserted only on branches where the complete characteristic function is actually proved to lie in unweighted `L1(R)`.

## 1. Fresh source/control state actually used

Fresh `yspennstate/math-research-brain/main` was resolved at invocation start. Owner control remained revision `2026-09-22.15`, QFORM-only. The current exclusive-signin continuation, programme memory protocol, live correction inbox, assignment card, preceding B02 receiver memory, and current `fleet03/B02` receiver state were read. Authenticated repository retrieval and actual receiver-memory use occurred; native learned-memory ingestion was not verified.

The owner-pinned source package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The reviewed sharp-Hausdorff--Young refinement used below is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For every literal disjoint original-coordinate cross block `B`, the completed B02/partner compiler gives

`C3=10.345083232147514...`,

`E3(B)>0  =>  ||p_Q||inf <= C3 E3(B)^(-1/6)`,                    (1.1)

`integral_R |phi_Q(t)|dt <=2*pi*C3 E3(B)^(-1/6)`,                (1.2)

with a continuous `C0` density. This marginal-free coefficient is obtained by the reviewed `q`-dependent D' estimate at the rational threshold `q=9/8` on the diffuse branch and the completed physical heavy-row cascade on the complement. Thus (1.1) is an integrated Fourier estimate, not a scalar pointwise-decay claim.

The reviewed sharp-HY fifth-volume receiver is independently

`E5(B)>0  =>  ||p_Q||inf <=(5e/sqrt(2)) E5(B)^(-1/10)`,           (1.3)

also with genuine unweighted Fourier `L1`, with no fifth-volume marginal gate.

The newest completed designated partner consumed at equation level is `fleet03/B02` r44:

`yspennstate/math-open-problems@514300a8c39f8b5e998bcd1ab386df45ee423156`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T021648Z-fleet03-B02-qform-r44/REPORT.md`.

Its proved compiler says: if `M0=A[R0,C0]` is a physical crossing with `sigma_2(M0)<=1-alpha`, then either a physical diagonal has modulus at least `beta alpha`, or a secondary literal cut has energy at least `((1-beta)^2 alpha^2)/4`; outside the secondary cut's near-rank-one / near-rank-two tubes the ambient law is paid by the marginal-free physical-E3 Fourier theorem. At `(alpha,beta,theta)=(1/2,1/4,1/4)` the concrete alternatives are a diagonal `>=1/8`, a secondary cut of Frobenius-square at least `9/256` lying in one of its two low-rank tubes, or

`||p_Q||inf <=110.347554477`, `integral |phi_Q| <=693.334132969`. (1.4)

No later completed `fleet03/B02` result was present at the publication refresh used for this report.

The live ultra-near-rank-two packet to which the new result is applied is the completed `fleet01/B02` r42 theorem at

`yspennstate/math-open-problems@434d3ab3168164b38fdba61456e35e747a67bea3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T012005Z-fleet01-B02-qform-auto11-r42/REPORT.md`.

On its literal physical block `M=A[R,C]`, after the direct E3 exit is removed,

`x1*x2 > 247/576`,                                                (1.5)

`T:=sum_(j>=3) xj < 9/1011712`,                                  (1.6)

where `x1>=x2>=...` are the squared singular values. Every nonzero tail coefficient remains part of the actual form.

## 2. Main deterministic theorem — `QFORM-FULLCUT-EXTERIOR-LIFT-L1-v1`

Let `R,C` be disjoint sets of original coordinates and put

`O=[n] \ (R union C)`, `M=A[R,C]`.

Take an algebraic singular-value decomposition

`M=U diag(s_j) V^T`, `x_j=s_j^2`, `x1>=x2>=...>=0`.               (2.1)

Let `P_U` and `P_V` be the orthogonal coefficient projections onto the top two left and right singular planes `span(u1,u2)` and `span(v1,v2)`. These planes are used only for deterministic coefficient algebra. No rotated random coordinates are introduced.

Write the outside couplings

`G_C=A[O,C]`, `G_R=A[R,O]`,                                      (2.2)

and define their transverse energies

`delta_C^2=||G_C(I-P_V)||_F^2`,
`delta_R^2=||(I-P_U)G_R||_F^2`.                                  (2.3)

The two enlarged matrices

`B_C=A[C^c,C]=[M;G_C]`,
`B_R=A[R,R^c]=[M,G_R]`                                           (2.4)

are literal disjoint physical cross blocks covering a full coordinate cut on one side.

### Theorem 2.1 — third-volume full-cut lift

One has

`boxed: E3(B_C)>=E3(M)+x1*x2*delta_C^2,`                          (2.5)

`boxed: E3(B_R)>=E3(M)+x1*x2*delta_R^2.`                          (2.6)

#### Proof of (2.5)

Let `m_i` denote the physical rows of `M`, and append first a single physical row `g` of `G_C`. In the third exterior power, Cauchy--Binet gives

`sum_(i<k in R) |m_i wedge m_k wedge g|^2
 =sum_j |<g,v_j>|^2 e2(x without j).`                             (2.7)

To see (2.7), diagonalise only the coefficient covariance `M^T M`: the covariance of the family `m_i wedge m_k` on `Lambda^2` has eigenvalues `x_p x_q` on `v_p wedge v_q`; wedging with the `v_j` component of `g` retains exactly the pairs not containing `j`.

For every `j>=3`, the pair `(1,2)` remains available, so

`e2(x without j)>=x1*x2`.                                        (2.8)

Therefore the contribution of all third minors using `g` and two rows of `M` is at least

`x1*x2 ||(I-P_V)g||^2`.                                          (2.9)

Now sum (2.9) over the distinct appended physical rows. These minor families are disjoint in the Cauchy--Binet sum. Retaining also the triples entirely inside `M` gives (2.5). The transposed argument gives (2.6). QED.

This proof aggregates before selecting a coordinate. There is no factor depending on `|O|`.

### Theorem 2.2 — fifth-volume transverse companion

One also has

`boxed: E5(B_C)>=x1*x2*E3(G_C(I-P_V)),}`                          (2.10)

`boxed: E5(B_R)>=x1*x2*E3((I-P_U)G_R).}`                          (2.11)

#### Proof

In the Cauchy--Binet sum for `E5(B_C)`, retain only five-row subsets consisting of two physical rows of `M` and three physical rows of `G_C`. For a fixed three-vector

`w=g_a wedge g_b wedge g_c`,

the covariance of the two-row wedges of `M` again has eigenvalues `x_p x_q` on `v_p wedge v_q`. Retain only the `(p,q)=(1,2)` term. It wedges precisely with the `Lambda^3(V_2^perp)` component of `w`, hence

`sum_(i<k in R)|m_i wedge m_k wedge w|^2
 >=x1*x2 |Lambda^3(I-P_V)w|^2`.                                  (2.12)

Summing (2.12) over the physical triples of `G_C` and using Cauchy--Binet gives (2.10). Transpose for (2.11). QED.

Equations (2.5)--(2.11) are deterministic exterior identities/inequalities and retain every coefficient of `A`.

## 3. Integrated Fourier consequences on the actual enlarged cuts

Combining Theorem 2.1 with the completed marginal-free sharp-HY/D' compiler (1.1)-(1.2), each side gives the genuine Fourier-`L1` estimate

`boxed:
 ||p_Q||inf
 <=C3 [E3(M)+x1*x2*delta_*^2]^(-1/6),}`                          (3.1)

whenever the displayed lower bound is positive. In particular, dropping the nonnegative parent volume,

`||p_Q||inf
 <=C3 (x1*x2)^(-1/6) delta_*^(-1/3).`                            (3.2)

The same branch has

`integral |phi_Q| <=2*pi*C3 (x1*x2)^(-1/6) delta_*^(-1/3)`.       (3.3)

Thus an outside coupling transverse to the two-mode carrier is an actual smoothing resource; it cannot be hidden by saying that the original small block is merely 'near rank two'.

The fifth-volume companion and the reviewed D5 theorem give the independent exit

`boxed:
 ||p_Q||inf
 <=(5e/sqrt(2))(x1*x2)^(-1/10)
   E3(G_*(I-P_*))^(-1/10),}`                                     (3.4)

again with `phi_Q in L1`. On the r42 product floor (1.5), the numerical coefficients in (3.2) and (3.4) are respectively

`C3(576/247)^(1/6)=11.913011953...`,

`(5e/sqrt(2))(576/247)^(1/10)=10.459767748...`.                   (3.5)

This is the requested live use of D', D5 and the reviewed sharp-HY refinement on physical blocks. D' is inside the marginal-free `C3` theorem; D5 is kept as a distinct higher-volume exit rather than being relabelled as E3.

## 4. Actual r42 application — the ultra-rank-two tube propagates to both full cuts

Set

`epsilon=2^-18`, `kappa=247/576`,

`eta^2=epsilon/kappa
      =(576/247)2^-18
      =9/1011712
      =8.89581224696356e-6`,                                     (4.1)

so `eta=0.00298258482644896...`.

The live r42 packet has `E3(M)<epsilon`, `x1*x2>kappa` and `T<eta^2` by (1.5)-(1.6).

If either enlarged full cut satisfies

`E3(B_C)>=epsilon` or `E3(B_R)>=epsilon`,                         (4.2)

then (1.1)-(1.2) pay the complete ambient law:

`boxed: ||p_Q||inf <=8 C3 =82.760665858...}`,                     (4.3)

`boxed: integral |phi_Q| <=16*pi*C3 =520.000599727...`.           (4.4)

The density on this exit is continuous and vanishes at infinity.

Assume instead that both full-cut E3 exits fail:

`E3(B_C)<epsilon`, `E3(B_R)<epsilon`.                             (4.5)

Then Theorem 2.1 and `x1*x2>kappa` imply immediately

`boxed: delta_C^2<eta^2, delta_R^2<eta^2.}`                       (4.6)

The same top-two planes therefore approximate the **whole** one-sided physical cuts. Indeed

`||B_C(I-P_V)||_F^2
 =||M(I-P_V)||_F^2+||G_C(I-P_V)||_F^2
 =T+delta_C^2 <2 eta^2`,                                         (4.7)

so the rank-two matrix `B_C P_V` gives

`boxed:
 dist_F(B_C,{rank<=2})
 <sqrt(18/1011712)
 =0.004218011912493... .}`                                       (4.8)

Likewise

`boxed:
 dist_F(B_R,{rank<=2})<0.004218011912493... .}`                   (4.9)

This is the principal new structural gain of the run. The earlier r42 theorem only said that the **partial** `R x C` crossing was ultra-near rank two. After (4.2) is paid by integrated Fourier, every surviving outside coupling from `O` into `C` is almost contained in the same right singular plane, and every surviving coupling from `R` into `O` is almost contained in the same left singular plane. There is no dimension loss, no selected tiny minor, and no deletion of the small tail.

Equivalently: the third spectral credit can no longer remain an unspecified diffuse cloud across the boundary of the rank-two crossing. Either it creates a quantitative physical third volume and is paid, or the rank-two carrier propagates to both full one-sided cuts.

## 5. New equation-level use of designated partner fleet03/B02 r44

The r44 compiler was originally formulated for an arbitrary physical crossing. After Section 4, it can be applied to a much more rigid object: an actual **full partition cut** which is already known to be within `0.004219` in Frobenius norm of rank two.

Take for example

`N=B_C=A[C^c,C]`.                                                  (5.1)

Because appending rows cannot decrease singular values,

`sigma_2(N)>=sigma_2(M)`.                                         (5.2)

There are now two exhaustive regimes.

### 5.1 Balanced full-cut core

If

`sigma_2(N)>1/2`,                                                  (5.3)

then after the Fourier exits the survivor is no longer merely a partial rank-two crossing with unknown external coefficients. It is a **full-coordinate bipartite cut** with a robust second singular value and distance `<0.004219` from rank two. This is a strictly narrower analytic endpoint.

If both `B_C` and `B_R` satisfy (5.3), the remaining geometry consists of two overlapping robust near-rank-two full cuts whose common `R x C` carrier is the r42 block.

### 5.2 Low second singular value — invoke r44 on the actual propagated cut

If instead

`sigma_2(N)<=1/2`,                                                 (5.4)

apply the completed partner theorem with

`alpha=1/2`, `beta=1/4`, `theta=1/4`                              (5.5)

to this same literal full cut `N`.

The result is the concrete exhaustive alternative:

1. some physical diagonal obeys `|A_ii|>=1/8`; or
2. a secondary literal physical cut has Frobenius-square at least `9/256` and lies in its near-rank-one tube `y2<E_N/4`; or
3. such a secondary cut lies in its near-rank-two tube `sum_(j>=3)y_j<E_N/4`; or
4. the complete ambient law has genuine Fourier `L1` and obeys (1.4).

This is an actual equation-level use of the newest designated partner result: the input to r44 is the full physical cut produced by (2.4), with the quantitative tube (4.8), not a citation-only reference.

Hence after the present run, the former `QFORM-COUPLED-TWO-LOWRANK-CUTS-OR-LARGE-DIAGONAL-L1-v1` debt is narrowed further. On the r42 branch, after all established Fourier payments, one reaches only:

- a robust near-rank-two **full** partition cut (`sigma_2>1/2`), possibly on both overlapping sides;
- the partner's fixed-scale secondary near-rank-one / near-rank-two full cut;
- or the physical-diagonal branch `|A_ii|>=1/8`.

The vague possibility of third curvature hidden in an arbitrary outside crossing has been removed.

## 6. Why the large-diagonal shortcut cannot simply reuse scalar-Schur E2

A tempting next claim would be:

> a large physical diagonal together with a robust physical rank-two crossing forces a quantitative scalar-Schur two-volume, so the completed one-hub incident-E3 theorem always pays.

That implication is false even inside the exact QFORM target.

Order five physical coordinates as `(h,r1,r2,c1,c2)` and take

`A_* =
 [[1,1,0,1,0],
  [1,0,0,1,0],
  [0,0,0,0,1],
  [1,1,0,0,0],
  [0,0,1,0,0]].`                                                 (6.1)

Let `R={r1,r2}`, `C={c1,c2}`. Then

`M=A_*[R,C]=I_2`, `E2(M)=1`,                                      (6.2)

and the pivot `h` has `a=A_hh=1`,

`c=A[R,h]=(1,0)^T`, `r=A[h,C]=(1,0)^T`.                           (6.3)

The scalar cross-Schur residual is

`S=M-c r^T/a=diag(0,1)`,                                         (6.4)

so

`boxed: a^2 E2(S)=0`                                              (6.5)

despite the large diagonal and robust pre-Schur rank-two crossing.

The matrix is a valid target matrix. The `(h,r1,c1)` principal block has eigenvalues

`-1, 1-sqrt(2), 1+sqrt(2)`,                                      (6.6)

while `(r2,c2)` contributes `-1,+1`. Thus `A_*` has four eigenvalues of modulus at least one.

Moreover, because there are only five coordinates, every disjoint physical cross block has one bank of size at most two. Hence every physical third volume, and therefore every D'/D5 currency, vanishes identically on this exact target example. This is an obstruction to a D'/D5-plus-scalar-Schur-only proof architecture, not a counterexample to QFORM.

The original target is harmless here: the localized physical principal `3 x 3` theorem from `COUNTEREXAMPLE_SEARCH.md` applies to the block in (6.6), whose least absolute eigenvalue is `sqrt(2)-1`, giving

`||p_(X^T A_* X)||inf
 <=6 sqrt(pi)/(sqrt(2)-1)
 <25.675`.                                                        (6.7)

So the surviving balanced full-rank-two / aligned-diagonal geometry requires a genuinely complementary principal-block, mixed-hub, or phase-sensitive receiver rather than another attempt to manufacture third exterior volume.

This explicit witness is also a mechanism-change certificate: after the full-cut propagation theorem, continuing to demand E3/D5 or scalar-Schur E2 in the aligned five-dimensional core is provably the wrong next step.

## 7. Correction boundaries preserved

Nothing above uses any of the live refuted interfaces. In particular:

- no law-uniform scalar quadratic pointwise decay;
- no independence after spectral rotation, SVD, or Schur algebra;
- no arbitrary-joint coarea density cap;
- no conditional projection-density supremum;
- no selection of one uniformly good minor from aggregate exterior mass;
- no deletion of a nonzero small coefficient or singular tail on arbitrary unbounded product laws;
- no claim that a large diagonal alone absorbs arbitrary same-bank curvature.

The singular vectors in Sections 2-5 are coefficient-only devices. Every Fourier theorem is applied to a literal original-coordinate cross block.

## 8. Status and next implication

`QFORM-FULLCUT-EXTERIOR-LIFT-L1-v1`: **PROVED supporting deterministic/integrated-Fourier compiler**.

`QFORM-ULTRAR2-FULLCUT-PROPAGATION-v1`: **PROVED on the live r42 packet**; after the `E3>=2^-18` Fourier exits, both one-sided full cuts are within `0.004219` of the same two-mode carrier on their respective sides.

`QFORM-ALIGNED-R2-SCHURCOLLAPSE-D3D5-BARRIER-v1`: **PROVED exact-target obstruction to the indicated proof architecture**, not to QFORM.

Full unrestricted QFORM: **OPEN / not disproved**.

Full-target continuity: **OPEN**. Continuity is established on every E3/D5 Fourier exit in this report.

Target-wide universal unweighted `integral |phi_Q|`: **OPEN / not refuted**.

The next B02 implication is now

`QFORM-BALANCED-FULLCUT-RANK2-PLUS-INTERNAL-CURVATURE-L1-v1`:

start from a literal full partition cut `N=A[J,J^c]` with `sigma_2(N)>1/2` and quantitative distance to rank two, or the partner's fixed-energy low-rank secondary cut, and couple the rank-two crossing to the same-side principal curvature forced by `s3(A)>=1`. Use a genuinely different mechanism on the aligned core: a grouped two-bank/one-principal-block Fourier receiver, principal-block localization, or a phase-sensitive rank-two argument. Do not try a fourth time to force E3/D5 or scalar-Schur E2 from the aligned five-dimensional witness (6.1).

No task identity, title, schedule, enabled/paused state, notification, email, permission, public-release, paid-call, installation, or cross-account-authentication setting is changed by this report.
