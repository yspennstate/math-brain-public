SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-24T08:20:48Z.
attacking: scalar-Schur two-mode inheritance and the zero-tetrad boundary; aggregate every disjoint Schur E2 packet before reciprocal payment, then close the exact diagonal-plus-rank-two diffuse endpoint and quantify the remaining hub localization.

# account01/B19 r55 — scalar-Schur two-mode inheritance, aggregate tetrad receiver, and exact zero-tetrad closure

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native authenticated memory ingestion.  
Continuity: tracked separately. One new Fresnel receiver below gives a continuous `C_0` density in its stated scope; the scalar-Schur half-Riesz receivers prove essential boundedness only.

All random-coordinate conditioning below is on literal ORIGINAL coordinates. No spectral rotation of the random vector is used. Inputs are arbitrary independent real variables with densities bounded by one; no moments, compact support, centering, iid, log-concavity, connected support or smoothness is assumed. All signs and singular/degenerate cases are retained as explicitly stated. Nonzero coefficient tails are never discarded as probabilistically small.

## 1. Fresh source-pinned premises and corrections

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with the unrestricted theorem still OPEN. Live corrections were reread. In particular this report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, post-rotation independence, a worst conditional-fiber density cap, generic Frostman-to-`L^infinity` interpolation, or deletion of a small coefficient matrix under unbounded cap-one laws.

The completed designated partner theorem actually applied below is account02/B19

`yspennstate/math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260924T031336Z-account02-B19-QFORM-auto11/REPORT.md`,

`QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`:

for every literal original-coordinate cross block `M` between disjoint product banks, with

`Z_2=e_2(M^T M)>0`,

and with arbitrary same-bank curvature, outside couplings, affine terms, signs and extra spectrum retained,

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <= C_R2 Z_2^(-1/16),`

`C_R2=3.929131770449763...`.                                      (1.1)

The stronger half-Riesz input used for the new scalar-pivot receiver is the completed account02/B06 theorem

`QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`,

source

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`:

`H_(1/2)(Y):=sup_s E|Y-s|^(-1/2)
 <=8 e^(1/4) e_2(M^T M)^(-1/8)`                                  (1.2)

for an arbitrary full ambient quadratic polynomial carrying a literal physical cross block `M`; arbitrary same-bank curvature and affine terms are retained. This is a fractional-potential theorem, not an endpoint density theorem by itself.

Two earlier account01 results are also used at their exact proved scopes:

* `QFORM-DISJOINT-TETRAD-RIGIDITY-v1` (account01/B19 r12): if every disjoint physical `2x2` minor of a symmetric matrix `S` vanishes, then `S=Delta+R` with `Delta` physical diagonal and `rank R<=2`.
* `QFORM-RANK2-DIFFUSE-SEPARABLE-HALF-RIESZ-v1` (account01/B14, source-pinned in account01/B13 r38): if `W^T W=I_2`, every physical row leverage is at most `1/2`, `M=M^T` is invertible, and the remaining perturbation is coordinatewise separable/affine, then

  `sup_s E |(W^T X)^T M(W^T X)+sum_j V_j(X_j)-s|^(-1/2)
   <=4 sqrt(2e)|det M|^(-1/4).`                                  (1.3)

The newest live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` is preserved: a universal `|t|^(-1/2)||G_t||_2` integration closure can diverge logarithmically even in a target-valid hub-star family. The successful interfaces below therefore keep the product source and use already-proved half-Riesz/Fresnel receivers before taking dangerous absolute fiber suprema.

## 2. New exact linear algebra: one scalar pivot leaves two target-scale Schur singular directions

Let `i` be a literal original coordinate with

`a=A_ii !=0`.                                                     (2.1)

After reordering only deterministic coefficient indices, write

`A=[[a,c^T],[c,D]]`,

and let the scalar Schur complement be

`S=D-c c^T/a`.                                                    (2.2)

### Theorem 2.1 — `QFORM-SCALAR-SCHUR-SINGULAR-INHERITANCE-v1`

For every real symmetric `A` and every nonzero scalar pivot (2.1),

`boxed: s_(k+1)(A) <= s_k(S)  for every k>=1.`                   (2.3)

In particular the QFORM target hypothesis `s_3(A)>=1` forces

`boxed: s_2(S)>=1.`                                               (2.4)

This is an absolute-singular-value statement, hence includes every signature, repeated eigenvalue, kernel and degeneracy compatible with `a!=0`.

#### Proof

Define the exact rank-one completion

`A_0=[[a,c^T],[c,c c^T/a]]
    =[1;c/a] a [1,c^T/a]`.                                      (2.5)

Thus `rank A_0=1` and

`A-A_0=diag(0,S)`.                                                (2.6)

Let `S_(k-1)` be a best rank-`(k-1)` approximation to `S` in operator norm. Then

`rank(A_0+diag(0,S_(k-1)))<=k`,                                  (2.7)

while

`||A-[A_0+diag(0,S_(k-1))]||_op
 =||S-S_(k-1)||_op
 =s_k(S)`.                                                        (2.8)

Eckart--Young for the `(k+1)`st singular value gives (2.3). Taking `k=2` proves (2.4). QED.

This strengthens the usual qualitative statement that a scalar Schur complement retains target information: after one literal scalar completion the remainder has **two** singular directions of magnitude at least one, with no sign hypothesis and no coordinate rotation.

## 3. New aggregate scalar-pivot receiver: spend all disjoint Schur tetrads at once

The exact square completion in the literal pivot coordinate gives

`Q=a(X_i+m(Z))^2+R(Z)`,                                         (3.1)

where `Z` consists of the untouched original coordinates and the quadratic coefficient of `R` is exactly `S` from (2.2). Every affine term is retained.

For the Schur matrix define the ordered disjoint-tetrad energy

`W_2(S)
 :=sum_{I,J: |I|=|J|=2, I cap J=empty} det S[I,J]^2`.             (3.2)

### Theorem 3.1 — `QFORM-SCALARPIVOT-AGGREGATE-TETRAD-LINFINITY-v1`

If `a!=0` and `W_2(S)>0`, then the full ambient law has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(2) e^(1/4) |a|^(-1/2) W_2(S)^(-1/8)
 =14.527089270... |a|^(-1/2) W_2(S)^(-1/8).`                    (3.3)

No continuity conclusion is asserted by this argument.

#### Proof

Independently color every coordinate of `Z` red or blue with probability `1/2`. For a fixed ordered disjoint pair `(I,J)` in (3.2), the event `I subset red`, `J subset blue` has probability `1/16`. Hence

`E e_2(S[red,blue]^T S[red,blue])=W_2(S)/16`.                    (3.4)

Therefore one deterministic original-coordinate split `Z=R0 union C0` satisfies

`Z_2:=e_2(S[R0,C0]^T S[R0,C0])>=W_2(S)/16`.                     (3.5)

Apply the completed account02/B06 theorem (1.2) to the actual Schur-remainder polynomial `R(Z)`, using this literal cut. It retains the entire `S[R0,R0]`, `S[C0,C0]`, every further singular direction and all affine terms, and gives

`H_(1/2)(R)
 <=8 e^(1/4) (W_2(S)/16)^(-1/8).`                               (3.6)

Conditioning on `Z`, the translated variable `X_i+m(Z)` still has density cap one. The pushforward under `u -> a u^2` gives the standard kernel bound

`p_Q(t)<=|a|^(-1/2) E|t-R|^(-1/2)`.                              (3.7)

Combine (3.6)-(3.7), using `16^(1/8)=sqrt(2)`, to obtain (3.3). QED.

The point is that no individual physical tetrad is reciprocated. The entire disjoint two-volume packet is aggregated before payment, exactly as required by the fleet's earlier minor-selection corrections.

At any fixed thresholds `|a|>=a_0>0`, `W_2(S)>=w_0>0`, this is already a universal branch with constant

`8 sqrt(2)e^(1/4) a_0^(-1/2)w_0^(-1/8)`.                        (3.8)

## 4. New exact zero-tetrad closure in the small-diagonal/diffuse-rank-two chamber

Assume now

`W_2(S)=0`.                                                       (4.1)

By the proved disjoint-tetrad rigidity theorem,

`S=Delta+R`,                                                      (4.2)

where `Delta` is diagonal in the untouched physical coordinates and

`rank R<=2`.                                                      (4.3)

### Theorem 4.1 — `QFORM-SCALARSCHUR-ZEROTETRAD-DIFFUSE-CLOSURE-v1`

Under the full target `s_3(A)>=1`, a nonzero literal scalar pivot `a`, and (4.1), suppose the rigidity decomposition can be chosen with

`||Delta||_op<1/2`.                                               (4.4)

Then `R` has rank exactly two and its two nonzero singular values exceed `1/2`. Write

`R=U M U^T`, `U^T U=I_2`, `M=M^T` invertible.                    (4.5)

Define physical leverages `c_j=||U_{j,*}||^2`, the heavy set

`H={j:c_j>2/7}`, `L=H^c`,                                       (4.6)

and the light Gram

`G_L=U[L,:]^T U[L,:]`.                                           (4.7)

Then `|H|<=6` and exactly one of the following occurs.

**Diffuse zero-tetrad branch.** If

`lambda_min(G_L)>=4/7`,                                          (4.8)

then the FULL ambient law has an essentially bounded density with

`boxed:
 ||p_Q||_infinity
 <4 sqrt(2e)(4/49)^(-1/4)|a|^(-1/2)
 =17.448425855... |a|^(-1/2).`                                  (4.9)

**Finite physical-carrier branch.** If (4.8) fails, then at most six literal untouched coordinates carry more than `3/7` of one rank-two carrier direction, and in particular there are a unit vector `y in R^2` and a literal `j in H` such that

`boxed: |<U_{j,*},y>|>1/sqrt(14).`                               (4.10)

No density claim is made from (4.10) alone; it is a dimension-free finite original-coordinate localization of the exact zero-tetrad obstruction.

#### Proof

The new inheritance theorem gives `s_2(S)>=1`. Singular values are 1-Lipschitz in operator norm, hence

`s_2(R)>=s_2(S)-||Delta||_op>1/2`.                               (4.11)

Thus `rank R=2` and

`|det M|=s_1(R)s_2(R)>1/4`.                                      (4.12)

Since `sum_j c_j=2`, seven coordinates cannot all satisfy `c_j>2/7`; hence `|H|<=6`.

Suppose (4.8). Put

`W=U[L,:]G_L^(-1/2)`,
`M_L=G_L^(1/2) M G_L^(1/2)`.                                    (4.13)

Then `W^T W=I_2`. Every surviving physical row obeys

`||W_{j,*}||^2
 =U_{j,*}G_L^(-1)U_{j,*}^T
 <=(7/4)(2/7)=1/2`.                                              (4.14)

Moreover

`|det M_L|=det(G_L)|det M|
 >(4/7)^2(1/4)=4/49`.                                            (4.15)

Condition on the at-most-six original variables in `H`. The remaining Schur polynomial has quadratic part

`Delta_L+W M_L W^T`,                                             (4.16)

plus an arbitrary induced affine term. The completed diffuse separable rank-two theorem (1.3) therefore yields, uniformly in that conditioning,

`H_(1/2)(R|X_H)
 <4 sqrt(2e)(4/49)^(-1/4).`                                      (4.17)

Average in `X_H` and feed (4.17) into the literal outer square kernel (3.7). This proves (4.9).

If (4.8) fails, choose unit `y` with `y^T G_L y<4/7`. Since `U^T U=I_2`,

`sum_{j in H}<U_{j,*},y>^2
 =1-y^T G_L y>3/7`.                                              (4.18)

There are at most six summands, so one exceeds `(3/7)/6=1/14`, proving (4.10). QED.

This is an exact endpoint theorem: at zero disjoint-tetrad currency, the target itself prevents the low-rank part from degenerating to rank one whenever the physical diagonal part has norm below `1/2`. The only remaining obstruction in that chamber is concentrated on at most six literal coordinates.

For example, at the fixed scalar-pivot gate `|a|>=2^-12`, the diffuse branch obeys

`||p_Q||_infinity<1116.700`.                                      (4.19)

## 5. New hub/rank-two Fresnel interface: the exact transverse currency

The finite-hub residue in (4.10) suggests keeping a physical hub jointly with a rank-two same-bank carrier rather than taking a fiber supremum. The completed Theorem H permits an exact clean statement.

Let `h` be one literal physical coordinate and `I` a disjoint physical bank. Assume on `I`

`A[I,I]=D+V M V^T`,                                               (5.1)

where `D` is physical diagonal, `V^T V=I_2`, and `M=M^T` is invertible. Put

`c=A[I,h]`,
`delta=||(I-VV^T)c||_2`.                                         (5.2)

The augmented physical row vectors are

`q_i=(V_{i,1},V_{i,2},c_i) in R^3`.                              (5.3)

Their Gram is

`G=sum_i q_iq_i^T
 =[[I_2,V^Tc],[c^TV,||c||^2]]`,                                  (5.4)

so the Schur determinant identity gives the exact transverse currency

`boxed: det G=delta^2.`                                           (5.5)

### Theorem 5.1 — `QFORM-HUB-R2-TRANSVERSE-FRESNEL-v1`

If `delta>0` and every augmented physical row satisfies

`q_i^T G^(-1)q_i<=1/2`,                                          (5.6)

then, with all outside blocks/couplings and affine terms arbitrary and retained, the full law has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2)(|det M| delta^2)^(-1/4).`                            (5.7)

#### Proof

Diagonalize the deterministic `2x2` coefficient matrix `M` inside coefficient space only. Theorem H applies with one physical hub (`|H|=1`) and two Fresnel squares (`r=2`). Its characteristic-function estimate is

`|phi_Q(t)|
 <=(2|t|)^(-1)(4 pi |t|)^(-1)|det M|^(-1/2)
   (4 pi)^3 det(G)^(-1/2)`
` =8 pi^2 (|det M|delta^2)^(-1/2)|t|^(-2).`                      (5.8)

Together with `|phi_Q|<=1`,

`int_R |phi_Q(t)|dt
 <=4[8 pi^2(|det M|delta^2)^(-1/2)]^(1/2)`.                      (5.9)

Fourier inversion divides by `2pi`, giving (5.7), and `phi_Q in L^1` gives the continuous `C_0` representative. QED.

There is a finite physical peel analogous to the previous two-frame compiler. Whiten `q_i` by `z_i=G^(-1/2)q_i`, so `sum z_i z_i^T=I_3`. Declare

`H_3={i:||z_i||^2>3/11}`.                                        (5.10)

Then `|H_3|<=10`. If the light Gram has smallest eigenvalue at least `6/11`, every re-normalized light leverage is at most `1/2`, its determinant is at least `(6/11)^3 det G`, and Theorem 5.1 gives

`boxed:
 ||p_Q||_infinity
 <4 sqrt(2)(11/6)^(3/4)(|det M|delta^2)^(-1/4)
 <8.913 (|det M|delta^2)^(-1/4).`                                (5.11)

If the light Gram has eigenvalue `<6/11`, the heavy set carries more than `5/11` of one whitened direction, so one of at most ten literal physical rows has directional amplitude

`boxed: >1/sqrt(22).}`                                           (5.12)

This identifies the exact algebraic quantity needed to spend a hub star against rank-two same-bank curvature: not the star norm by itself, but its component transverse to the rank-two carrier plane.

## 6. Designated partner account02/B19 applied to actual inequalities

The robust light-light branch of the fresh account03/B19 r51 compiler has an ACTUAL literal physical crossing `M_*` satisfying

`sigma_2(M_*)>m_0:=4089/458752
 =0.008913312639508928...`.                                      (6.1)

Applying the completed designated account02/B19 theorem (1.1) at this actual block gives

`Z_2(M_*)>=sigma_2(M_*)^4`,                                      (6.2)

and hence

`boxed:
 H_(1/4)(Q)
 <3.929131770449763 m_0^(-1/4)
 =12.787534221... .}`                                            (6.3)

This is the requested equation-level use of the partner mathematics: all same-bank curvature, every outside coupling and the genuine nonzero `2^-16` crossing tail remain in the full law.

A fresh completed theorem from account02/B06 now strengthens the same actual block further:

`boxed:
 H_(1/2)(Q)
 <8 e^(1/4)m_0^(-1/2)
 =108.803794... .}`                                              (6.4)

Equation (6.4) does **not** by itself imply `L^infinity`; the fleet has an explicit logarithmic-density counterexample to that abstract step. Its value for proof assembly is that the analytic upgrade from the r51 physical `E2` packet to half-Riesz smoothing is no longer the missing inequality. The missing work is specifically to couple that half-Riesz packet to the genuine third resource without losing product provenance.

The latest completed designated-partner stress, account02/B19 r53, is also an exact boundary check. Its principal-minimal family

`A_a=a(l_1l_2^T+l_2l_1^T)+ww^T`,
`l_1=e_h+v_1`, `l_2=u+v_2`,                                      (6.5)

has target spectrum `{2a,-2a,1}` and at `|a|=1/2` exactly `{1,-1,1}`. Every physical core diagonal is zero; the only nonzero scalar pivots are the `W`-coordinates, of size `1/m`, which tend to zero. Thus Theorems 3.1--4.1 cannot be promoted to a universal proof by postulating a fixed scalar-pivot scale. This is a genuine target-valid obstruction, not a defect of the estimates.

The same partner family also checks Theorem 5.1 sharply. On `I=V_1 union V_2`, the same-bank rank-two coefficient is

`M=[[0,a],[a,0]]`,                                                (6.6)

while the literal hub coupling is

`c=a v_2 in span(v_1,v_2)`.                                      (6.7)

Hence

`delta=dist(c,span(v_1,v_2))=0`,                                 (6.8)

so the new hub/rank-two transverse receiver correctly refuses to scalarize the curved two-bank core. The retained disjoint `w` square is the genuine third resource; the previous account01/B19 r54 one-hub/one-square theorem pays the full family by `<=12` throughout `|a|>=1/2`. This exactly matches the partner correction that the curved two-bank partial density can be logarithmically unbounded while the full three-resource law is uniformly bounded.

## 7. Compact conditional proof assembly after r55

The proof tree can now be stated more sharply without claiming completion.

1. Principal-minimal descent and the existing physical `D_k`, pair, ridge/window, grouped-square, Fresnel and finite-core compilers reduce the hard states while keeping original-coordinate product provenance.
2. Whenever a literal nonzero scalar pivot `a` is available, Theorem 2.1 guarantees that its exact Schur remainder has **two** singular values at least one.
3. For that pivot, all disjoint Schur `E2` geometry is summarized by the single aggregate `W_2(S)`. If it is quantitatively positive, Theorem 3.1 pays it with no good-minor extraction.
4. At the exact boundary `W_2=0`, rigidity gives `S=Delta+rank<=2`. If `||Delta||<1/2`, target inheritance forces an actual rank-two carrier with both singular values `>1/2`; Theorem 4.1 either pays it directly after a six-coordinate leverage peel or localizes the failure to at most six physical coordinates.
5. A finite physical hub interacting with exact rank-two same-bank curvature is paid whenever the hub star has transverse energy to that carrier plane: Theorem 5.1 gives the exact currency `|det M| delta^2`. Failure again localizes to finitely many physical rows.
6. On the independent strong-rank-two route, the designated account02/B19 theorem gives the actual full-law `H_(1/4)` inequality (6.3), and the newer E2 theorem upgrades the same block to `H_(1/2)` in (6.4). Endpoint work must therefore spend a genuine third resource rather than seek more two-volume fractional smoothing.

The first essential missing implication is now

`QFORM-SCALARPIVOT-NEARZEROTETRAD-STABILITY-OR-TINYPIVOT-HUBSTAR-THIRDRESOURCE-v1`:

> Fix universal small gates `a_0,w_0>0`. The branch `|A_ii|>=a_0` and `W_2(S_i)>=w_0` is paid by Theorem 3.1. The exact `W_2=0`, `||Delta||<1/2`, diffuse rank-two branch is paid by Theorem 4.1. Prove that the remaining `0<W_2(S_i)<w_0` states either admit a dimension-free quantitative approximation to `Delta+rank<=2` strong enough to preserve one of the half-Riesz/Fresnel currencies, or route to a physical pair/star/volume receiver; and simultaneously treat the genuinely tiny/zero-pivot chamber by coupling the hub-star to its retained third spectral source. The r53 family shows the tiny-pivot/hub-star alternative is unavoidable.

The existing r12 strong-triangle tetrad-stability theorem handles one portion of the `W_2 small` side. The no-strong-triangle / large-star stability interface and the r51 hub-star third-resource manufacture remain the first local algebraic debts. The latest hub-star mixed-norm correction forbids closing them by a universal worst-fiber `L^2` integral.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity remains **OPEN**; continuity is established only on the explicitly Fourier-`L^1` branches such as Theorem 5.1.
