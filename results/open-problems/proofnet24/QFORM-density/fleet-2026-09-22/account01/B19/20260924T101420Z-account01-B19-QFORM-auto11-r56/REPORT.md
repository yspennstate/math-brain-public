SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-24T10:14:20Z.
attacking: the near-zero-tetrad / finite-hub boundary after scalar Schur inheritance; derive a dimension-free quantitative stability dichotomy that either preserves a rank-two half-Riesz/Fresnel currency or forces a literal finite physical star/triangle receiver, and apply the latest account02/B19 mathematics to an actual inequality.

# account01/B19 r56 — exact diagonal-plus-rank-three endpoint and one-edge tetrad stability

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval and transport are not native learned-memory receiver ingestion.

Continuity is tracked separately. The new exact diagonal-plus-rank-three diffuse branch below has a continuous `C_0` density because it uses the completed `L^1` Fresnel/Brascamp--Lieb receiver. The quantitative near-tetrad stability lemma is deterministic and by itself has no regularity conclusion.

All random coordinates remain literal ORIGINAL coordinates. No random variable is rotated. The input variables are arbitrary independent real variables with densities bounded by one; no moments, compact support, smoothness, iid, centering, log-concavity or connected support is assumed. Orthogonal changes below occur only in finite deterministic coefficient spaces. Small nonzero coefficient matrices are never discarded as probabilistically small.

## 1. Fresh source-pinned premises and corrections

Fresh owner control was reread on `math-research-brain/main`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole target, and the full theorem remains open. The live correction inbox was reread. In particular this report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, post-rotation independence, a uniform conditional-fibre cap, deletion of a small coefficient matrix, or extraction of one uniformly good physical minor.

The immediate same-slot source is account01/B19 r55,

`yspennstate/math-open-problems@879ad8a0be00493b8a826558a993a45a6070f162`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260924T082048Z-account01-B19-QFORM-auto11-r55/REPORT.md`.

It supplies, among other things:

1. for a nonzero literal scalar pivot `a=A_hh` and exact scalar Schur complement `S`,

   `s_(k+1)(A) <= s_k(S)`, hence `s_3(A)>=1 => s_2(S)>=1`;

2. the aggregate disjoint-tetrad receiver: with

   `W_2(S)=sum_{I,J disjoint, |I|=|J|=2} det S[I,J]^2`,

   `W_2(S)>0` implies

   `||p_Q||_infinity <= 8 sqrt(2) e^(1/4) |a|^(-1/2) W_2(S)^(-1/8)`;

3. at `W_2(S)=0`, exact rigidity `S=Delta+K`, `Delta` physical diagonal, `rank K<=2`;

4. a finite leverage peel for the exact rank-two Schur carrier, and a hub/rank-two transverse Fresnel receiver.

The newest designated partner result is account02/B19 r14,

`yspennstate/math-open-problems@02a537de4788fa8821d7986ef53fc5ad0a311003`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260924T083831Z-account02-B19-QFORM-auto11-r14/REPORT.md`,

`QFORM-BL-RANKR-LATENT-PSEUDODET-ENDPOINT-v1`.

In its exact proved scope: if a literal original-coordinate source bank `I` satisfies

`A[I,I]=D+W H W^T`,

where `D` is physical diagonal, `W^T W=I_r`, every physical source row has leverage `||W_i||^2<=1/2`, and `H=H^T` has rank `k>=3`, then with arbitrary outside blocks/couplings and affine terms retained the FULL ambient law has a continuous `C_0` density and

`||p_Q||_infinity <= [4k/(k-2)] |pdet(H)|^(-1/k)`.               (1.1)

For `k=3` this is

`||p_Q||_infinity <=12 |det H|^(-1/3)`.                          (1.2)

This theorem is applied below at an actual target inequality, not merely cited as an analogy.

## 2. New exact endpoint: physical diagonal plus rank at most three

The first new theorem removes the scalar-pivot size from a large exact boundary chamber.

### Theorem 2.1 — `QFORM-DIAG-R3-TOTALCORE-DIFFUSE-PEEL-v1`

Let

`A=D+L`,                                                          (2.1)

where `D` is diagonal in the original independent coordinates,

`||D||_op <= d <1`,                                               (2.2)

and `L=L^T` has

`rank L<=3`.                                                      (2.3)

Assume the target spectral condition

`s_3(A)>=1`.                                                      (2.4)

Then `rank L=3`. Write

`L=W H W^T`, `W^T W=I_3`,                                       (2.5)

with `H=H^T` invertible. Then

`boxed: |det H| >= (1-d)^3.`                                     (2.6)

Fix an integer `m>=6`, and put

`g=6/(m+1)`, `eta=3/(m+1)=g/2`.                                 (2.7)

Let

`Hvy={i: ||W_{i,*}||^2>eta}`, `Lgt=Hvy^c`,                       (2.8)

and

`G=W[Lgt,:]^T W[Lgt,:]`.                                        (2.9)

Then `|Hvy|<=m`, and exactly one of the following holds.

**Diffuse exact-rank-three branch.** If

`lambda_min(G)>=g`,                                              (2.10)

then the FULL ambient quadratic law has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity <= 12/[g(1-d)]
                    =2(m+1)/(1-d).`                              (2.11)

**Finite physical localization branch.** If (2.10) fails, there are a unit vector `y in R^3` and a literal original coordinate `i in Hvy` such that

`boxed:
 |<W_{i,*},y>|^2 > (m-5)/(m(m+1)).}`                             (2.12)

Thus failure is concentrated on at most `m` literal physical coordinates.

Two useful specializations at `d<=1/2` are:

- `m=6`: either `||p_Q||_infinity<=28` with a continuous `C_0` density, or at most six physical coordinates contain a latent directional amplitude `>1/sqrt(42)`;
- `m=10`: either `||p_Q||_infinity<=44` with a continuous `C_0` density, or at most ten physical coordinates contain a latent directional amplitude `>1/sqrt(22)`.

If already

`max_i ||W_{i,*}||^2<=1/2`,                                     (2.13)

then no peel is needed and the sharper partner bound is

`boxed: ||p_Q||_infinity <=12/(1-d),}`                           (2.14)

so at `d<=1/2` it is at most `24`.

### Proof

Singular values are 1-Lipschitz in operator norm. From (2.1)-(2.4),

`s_3(L)>=s_3(A)-||D||_op >=1-d>0`.                               (2.15)

Hence `rank L>=3`; with (2.3), `rank L=3`. The three nonzero singular values of `L` are the absolute eigenvalues of `H`, so each is at least `1-d`, proving (2.6).

The leverage scores satisfy

`sum_i ||W_{i,*}||^2=3`.                                        (2.16)

If `m+1` rows were all strictly larger than `eta=3/(m+1)`, their sum would exceed three. Hence `|Hvy|<=m`.

Assume (2.10). Define

`W_tilde=W[Lgt,:]G^(-1/2)`,                                     (2.17)

`H_L=G^(1/2) H G^(1/2)`.                                        (2.18)

Then

`W_tilde^T W_tilde=I_3`,                                        (2.19)

and every literal light physical row satisfies

`||W_tilde_{i,*}||^2
 <= eta/lambda_min(G)
 <= eta/g=1/2`.                                                   (2.20)

Moreover

`|det H_L|=det(G)|det H|
 >=g^3(1-d)^3`.                                                   (2.21)

On the literal source bank `Lgt`,

`A[Lgt,Lgt]=D[Lgt,Lgt]+W_tilde H_L W_tilde^T`.                   (2.22)

All coefficients touching `Hvy`, all curvature on `Hvy`, and all induced affine terms are simply outside the source bank and are explicitly allowed by the completed account02/B19 theorem. Applying (1.2) to the ACTUAL full form gives

`||p_Q||_infinity
 <=12 |det H_L|^(-1/3)
 <=12/[g(1-d)]`,                                                  (2.23)

and the partner theorem also gives the continuous `C_0` representative. This is the required equation-level application of the designated partner mathematics.

If (2.10) fails, choose a unit `y` with

`y^T G y<g`.                                                      (2.24)

Since `W^T W=I_3`,

`sum_(i in Hvy) <W_i,y>^2
 =1-y^TGy
 >1-g=(m-5)/(m+1)`.                                              (2.25)

There are at most `m` summands, so one exceeds `(m-5)/(m(m+1))`, proving (2.12). QED.

### Why this is useful

The theorem has no scalar-pivot denominator and no small-minor denominator. At an exact diagonal-plus-rank-three endpoint the target itself prevents the latent pseudodeterminant from collapsing: (2.6) is forced by `s_3(A)>=1`. Thus the newest partner's general-rank Fresnel theorem turns a structural exact low-rank boundary directly into a universal endpoint, unless the latent three-plane is concentrated on finitely many physical coordinates.

## 3. Application to the exact zero-tetrad scalar-Schur boundary

Take a literal scalar pivot `h` with

`a=A_hh !=0`,                                                    (3.1)

write

`A=[[a,c^T],[c,D_0]]`,                                           (3.2)

and let

`S=D_0-c c^T/a`.                                                  (3.3)

The exact rank-one scalar completion is

`A_0=[[a,c^T],[c,c c^T/a]]`, `rank A_0=1`,                       (3.4)

and

`A=A_0+diag(0,S)`.                                                (3.5)

Assume

`W_2(S)=0`.                                                       (3.6)

By the proved r55 tetrad rigidity theorem,

`S=Delta+K`, `Delta` physical diagonal, `rank K<=2`.              (3.7)

Then

`A=D_*+L_*`,                                                      (3.8)

where

`D_*=diag(0,Delta)`,                                              (3.9)

`L_*=A_0+diag(0,K)`, `rank L_*<=3`.                              (3.10)

Hence Theorem 2.1 applies immediately whenever

`||Delta||_op<=d<1`.                                              (3.11)

### Corollary 3.1 — `QFORM-SCALARSCHUR-ZEROTETRAD-TOTALR3-ENDPOINT-v1`

Under `s_3(A)>=1`, (3.1), (3.6), and `||Delta||_op<=d<1`, the exact total latent core `L_*` has rank exactly three and its three nonzero singular values are at least `1-d`. For every integer `m>=6`, either

`boxed: ||p_Q||_infinity <=2(m+1)/(1-d)}`                        (3.12)

with a continuous `C_0` density, or at most `m` literal original coordinates carry the finite localization (2.12) for the total rank-three latent plane.

At `d<=1/2`, the `m=6` version is the concrete alternative

`boxed: ||p_Q||_infinity<=28,}`                                  (3.13)

or a six-coordinate latent packet with one directional amplitude `>1/sqrt(42)`.

This is strictly different from the earlier r55 square-kernel closure: it is uniform as the physical scalar pivot `a` tends to zero. The pivot can become arbitrarily tiny; if the resulting total three-plane stays diffuse, the full law is already paid. If not, the obstruction is finitely localized in the original coordinates. This matches the designated partner's maximal-coloop stress rather than contradicting it.

The same conclusion covers all signs and degeneracies. If `K` has rank zero or one, or if the rank-one completion intersects its range, the target plus `||Delta||<1` simply forces the total `L_*` nevertheless to have rank three; otherwise (2.15) would fail.

## 4. New near-zero-tetrad stability from one strong Schur edge

The exact boundary is now substantially better understood. The next problem is stability when `W_2(S)` is positive but very small. The previous r12 stability theorem required a strong physical triangle. The following theorem needs only one strong edge.

For a symmetric matrix `S`, write

`W=W_dis(S)=sum_(I,J disjoint, |I|=|J|=2) det S[I,J]^2`,          (4.1)

`omega=sqrt(W)`.                                                  (4.2)

Choose two distinct physical indices `a,b` with

`s=S_ab`, `|s|>=mu>0`.                                           (4.3)

Let `U` be all remaining indices and put

`x=(S_ai)_(i in U)`, `y=(S_bi)_(i in U)`,                        (4.4)

`A_x=||x||_2`, `A_y=||y||_2`.                                   (4.5)

### Theorem 4.1 — `QFORM-TETRAD-ONEEDGE-STABILITY-v1`

Assume the adjacent physical Schur stars obey

`max(A_x,A_y)<=R`.                                                (4.6)

Then there are a physical diagonal matrix `Delta` and a symmetric matrix `K` of rank at most two such that

`boxed:
 ||S-Delta-K||_F
 <= (2+sqrt(2) R/mu) W^(1/4)
    +(1+sqrt(2)) W^(1/2)/mu.}`                                  (4.7)

More precisely, put

`tau=sqrt(2 omega)=sqrt(2) W^(1/4)`.                             (4.8)

There are two algebraically different subbranches.

**Star branch.** If

`min(A_x,A_y)<=tau`,                                              (4.9)

then `K` can be chosen as a literal symmetric rank-at-most-two star centred at one of the anchors, and

`boxed:
 ||S-Delta-K||_F
 <=2 W^(1/4)+W^(1/2)/mu
    +sqrt(2)R W^(1/4)/mu.}`                                     (4.10)

**Collinear branch.** If

`A_x>tau`, `A_y>tau`,                                            (4.11)

then `K` can be chosen rank one and

`boxed:
 ||S-Delta-K||_F
 <=sqrt(2) W^(1/4)
   +(1+sqrt(2))W^(1/2)/mu.}`                                    (4.12)

No triangle, sign coherence, dimension bound or nonzero-entry graph hypothesis is required.

### Proof

For distinct `i,j in U`, set

`D_ij=s S_ij-x_j y_i`.                                           (4.13)

This is exactly the disjoint tetrad

`D_ij=det S[{a,i},{b,j}]`.                                       (4.14)

Consequently

`sum_(i!=j) D_ij^2 <= W`.                                        (4.15)

Subtracting the reversed identity gives

`x_i y_j-x_j y_i=D_ij-D_ji`.                                    (4.16)

Therefore the exterior product satisfies

`||x wedge y||_2^2
 :=sum_(i<j)(x_i y_j-x_j y_i)^2
 <=2W`.                                                          (4.17)

#### Star subbranch

After swapping `a,b` if needed, assume `A_y<=tau`. Define `z` by

`z_b=s`, `z_i=x_i` for `i in U`, `z_a=0`,                        (4.18)

and

`K=e_a z^T+z e_a^T`.                                             (4.19)

Then `rank K<=2`; it matches the edge `ab` and the whole `a-U` row exactly. Let

`Delta=diag(S-K)`.                                                (4.20)

The symmetric `b-U` residual has Frobenius norm `sqrt(2)A_y`. For the `U x U` off-diagonal residual, (4.13) gives

`s S_ij=D_ij+x_j y_i`.                                           (4.21)

Hence

`||offdiag((S-K)[U,U])||_F
 <=(omega+A_x A_y)/|s|`.                                        (4.22)

Using `A_x<=R`, `A_y<=tau`, `|s|>=mu` and `sqrt(2)tau=2W^(1/4)` gives (4.10).

#### Collinear subbranch

Assume (4.11). Define

`rho=<x,y>/A_x^2`,                                                (4.23)

`e=y-rho x`.                                                      (4.24)

The standard exterior-product identity gives

`A_x^2 ||e||_2^2
 =A_x^2 A_y^2-<x,y>^2
 =||x wedge y||_2^2`.                                            (4.25)

Thus by (4.17),

`||e||_2 <=sqrt(2) omega/A_x
           <sqrt(2)omega/tau
           =W^(1/4)`.                                            (4.26)

Also `rho!=0`: if `rho=0`, then (4.25) gives

`||x wedge y||=A_x A_y>tau^2=2omega`,                            (4.27)

contradicting (4.17), which gives `||x wedge y||<=sqrt(2)omega`.

Define the physical vector `v` by

`v_a=s/rho`, `v_b=s`, `v_i=x_i` for `i in U`,                    (4.28)

and the symmetric rank-one matrix

`K=(rho/s) v v^T`.                                               (4.29)

Then

`K_ab=s`, `K_ai=x_i`, `K_bi=rho x_i`,
`K_ij=(rho/s)x_i x_j`.                                           (4.30)

Again put `Delta=diag(S-K)`. The symmetric `b-U` error contributes `sqrt(2)||e||`. For `i!=j`, (4.13) and `y_i=rho x_i+e_i` give

`s(S_ij-K_ij)=D_ij+x_j e_i`.                                    (4.31)

Therefore

`||offdiag((S-K)[U,U])||_F
 <=[omega+A_x||e||]/mu
 <=(1+sqrt(2))omega/mu`,                                         (4.32)

where the last inequality uses `A_x||e||<=sqrt(2)omega` from (4.25)-(4.17). Combining (4.26) with the symmetric `b-U` copy gives

`sqrt(2)||e|| <=2omega/A_x <2omega/tau=sqrt(2)W^(1/4)`.           (4.33)

Equations (4.32)-(4.33) prove (4.12). The common bound (4.7) dominates both subbranch bounds. QED.

### Original-coordinate provenance under a scalar pivot

If `S` is the scalar Schur complement (3.3), all currencies above are still literal bordered original-coordinate minors. For disjoint two-subsets `I,J` of the untouched coordinates,

`det A[{h} union I,{h} union J]=a det S[I,J]`.                    (4.34)

Likewise for a Schur edge,

`a S_ab=det A[{h,a},{h,b}]`.                                     (4.35)

Thus (4.7) does not arise from a spectral-coordinate surrogate; it is a stability statement for aggregate bordered physical minors after an exact physical square completion.

## 5. Target barrier: the collinear near-tetrad subbranch cannot survive too close to zero with a small diagonal residual

The rank-one refinement (4.12) interacts directly with the target `s_3(A)>=1`.

Return to the scalar-pivot setting (3.1)-(3.5). Suppose the collinear branch of Theorem 4.1 holds, producing

`S=Delta_1+K_1+E`, `rank K_1<=1`,                                (5.1)

with

`||E||_op<=||E||_F<=epsilon_1`,                                  (5.2)

where

`epsilon_1
 =sqrt(2)W^(1/4)+(1+sqrt(2))W^(1/2)/mu`.                    (5.3)

Then

`A=[A_0+diag(0,K_1)]+diag(0,Delta_1+E)`.                         (5.4)

The first bracket has rank at most two. Eckart--Young therefore gives

`s_3(A)
 <=||Delta_1+E||_op
 <=||Delta_1||_op+epsilon_1`.                                    (5.5)

Hence the target forces the exact inequality

`boxed:
 ||Delta_1||_op
 +sqrt(2)W^(1/4)
 +(1+sqrt(2))W^(1/2)/mu
 >=1.}`                                                           (5.6)

This is the first essential missing inequality attacked this run: it converts sufficiently small nonzero tetrad energy into a structural exclusion, rather than attempting to delete the residual probabilistically.

In particular, if

`||Delta_1||_op<=1/2`,                                           (5.7)

then the collinear branch is impossible whenever

`sqrt(2)W^(1/4)+(1+sqrt(2))W^(1/2)/mu<1/2`.                      (5.8)

A simple explicit sufficient gate is

`boxed:
 W < min{1/1024, mu^2/[16(1+sqrt(2))^2]}.`                       (5.9)

Indeed the first term in (5.8) is then `<1/4` and the second is `<1/4`.

Therefore, below the fixed gate (5.9), a strong-edge target survivor with small constructed diagonal residual cannot be the rank-one/collinear tetrad geometry. It must enter the **star-like rank-two branch** (4.10), or violate the bounded-star hypothesis (4.6), or have a large diagonal twist. This is exactly the type of physical finite-hub geometry for which the existing hub+square, pair, grouped-star and Fresnel compilers were designed.

No probabilistic coefficient perturbation statement is made here. The nonzero error `E` in (5.1) remains part of the actual quadratic coefficient matrix.

## 6. Partner mathematics applied to an actual target inequality

The main application is already equation (2.23): the completed designated account02/B19 rank-three pseudodeterminant theorem is applied to the literal light source block of the ACTUAL full matrix. The target gives the lower bound

`|det H_L|>=g^3(1-d)^3`,                                         (6.1)

so the partner estimate becomes the concrete full-law inequality

`boxed:
 ||p_Q||_infinity<=12[g^3(1-d)^3]^(-1/3)
                  =12/[g(1-d)].}`                               (6.2)

At the live exact zero-tetrad gate `d=1/2`, choosing `m=6`, hence `g=6/7`, gives

`boxed: ||p_Q||_infinity<=28}`                                   (6.3)

with a continuous `C_0` density unless the six-coordinate localization exit occurs.

As a second boundary check, the same partner theorem pays its own exact aligned four-node stress with `s=t=1`: the coefficient packet has rank eight and `|det H_8|=9`, hence

`||p_Q||_infinity<=(16/3)9^(-1/8)
                  =4.052456990...`.                              (6.4)

That stress therefore does not obstruct the present exact low-rank endpoint. It only warns that transverse physical `E_3` need not exist and that genuine nonlatent tails cannot be erased.

## 7. Compact conditional proof assembly after r56

The current proof tree can now be stated more cleanly.

1. Same-constant principal-minimal descent and the existing physical `D_k`, pair, pair-log, ridge/window, grouped-square, Fresnel, local-triple, `E_3`, `D5`, null-coloop and finite-core receivers pay their exact certified branches while retaining original-coordinate product provenance.
2. Whenever a literal nonzero scalar pivot is available, r55 scalar-Schur inheritance gives `s_2(S)>=1`.
3. If the aggregate disjoint tetrad energy `W_2(S)` is quantitatively positive, r55 pays it without selecting one tiny minor.
4. At the exact boundary `W_2(S)=0`, rigidity gives `S=Delta+rank<=2`. The present Corollary 3.1 now converts the **entire original matrix** to physical diagonal plus rank at most three. If the total rank-three plane is diffuse, the newest account02/B19 theorem pays the full law with a universal continuous-density bound independent of the scalar-pivot magnitude. If it is not diffuse, at most finitely many physical coordinates carry a quantitatively large latent direction.
5. For `0<W_2(S)<<1`, the new one-edge theorem removes the previous need for a strong triangle. One strong Schur edge plus bounded adjacent stars gives dimension-free `O(W_2^(1/4))` proximity to diagonal plus rank at most two. The collinear/rank-one subbranch is ruled out by the target itself under the explicit gate (5.9) whenever the constructed diagonal residual is small.
6. Hence a sufficiently small-tetrad strong-edge survivor is forced toward a **star-like rank-two physical hub geometry**, a large physical star, a large diagonal twist, or a genuinely transverse nonlatent residual. These are much narrower than an arbitrary near-low-rank Schur matrix.
7. The robust physical-rank-two route from account03/B19 r51 remains equipped with the designated account02/B19 full-law `H_(1/4)<12.787535` resource; the analytic fractional smoothing itself is no longer the missing inequality. Endpoint work must spend the genuine third resource without deleting the retained tail.

The first local debt is therefore sharpened to

`QFORM-NEARZEROTETRAD-STARLIKE-R2-PLUS-THIRDSOURCE-ROBUST-ENDPOINT-v1`:

> Starting from the star subbranch (4.10), or from the finite total-latent localization exit of Corollary 3.1, jointly spend the physical hub/rank-two carrier with the retained third target resource while retaining the genuine nonzero stability residual. Equivalently, prove that any component of the residual escaping the three-dimensional total latent space creates an already-paid physical `E_2/E_3`, pair, ridge/window, grouped-star or incident-volume currency. No argument may simply delete the residual under arbitrary unbounded cap-one laws.

A parallel no-strong-edge chamber remains: if every Schur edge is below the chosen fixed `mu`, one must use the diffuse/ridge or aggregate-star compilers rather than the present one-edge theorem. The large-star exit in (4.6) is also structural until coupled to a completed density receiver. These are the honest remaining interfaces.

The full QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity remains **OPEN**; continuity is proved only on the explicitly `L^1` Fourier branches, including Theorem 2.1's diffuse branch.

## 8. Sanity checks

The one-edge algebra was regression-tested on generated signed rank-one-plus-diagonal matrices with small symmetric off-diagonal perturbations. In 571 samples entering the collinear branch, the constructed rank-one approximation satisfied (4.12) in every sample; the largest observed `lhs/rhs` was about `0.1554`. A separate star-near configuration test of 1000 samples satisfied the pre-simplified star estimate in every sample, with largest observed ratio below `0.492`. These finite checks are diagnostics only; the proof is (4.13)-(4.33).

No external or paid computation was used.
