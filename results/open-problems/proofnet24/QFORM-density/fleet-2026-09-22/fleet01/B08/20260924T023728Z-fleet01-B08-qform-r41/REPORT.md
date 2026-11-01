SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-24T02:37:28Z.
attacking: the ultra-thin approximate-alignment survivor — retain the genuine nonzero spectral-tail residual and prove that a star with even one-percent transverse sine already produces a stable literal rank-three crossing.

# fleet01/B08 r41 — robust angle-free crossing in the ultra-thin alignment layer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING END-TO-END BRANCH + LATEST PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains **OPEN**. The unrestricted continuity conclusion remains **OPEN**. The new paid branch below has a continuous `C_0` density. All stochastic coordinates remain ORIGINAL independent coordinates with densities bounded by one. No moments, bounded support, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea bound, pointwise van-der-Corput decay, or deletion of a small random quadratic perturbation is used.

Fresh prepublication owner control remained revision `2026-09-22.15`, QFORM only, with no pause of fleet01/B08. The live correction inbox was reread at SHA `a884b835aba929c5376e6417ae5cfcd44c0f7a76`.

## 1. Pinned completed inputs

### 1.1 Deletion geometry and quantitative alignment

From fleet01/B08 r36 and r38, in the original-coordinate deletion setup

`A=[[a,b^T],[b,C]]`,

choose three genuine eigenvectors with modulus at least `L`, let `p` be their squared leverage on the deleted coordinate, let `U` be the top-two absolute-eigenvalue frame of `C`, and write

`C=U Theta U^T+E`, `EU=0`, `x=||E||op/L=s_3(C)/L`,

`b=tau w+U beta`, `w perpendicular to Ran(U)`, `W=[w,U]`.

For `p<=1/48`, `x<=1/130`,

`tau >= (1-x)L sqrt((1-p)/p) >= tau0 L`,

`tau0=(129/130)sqrt(47)=6.802918795782575...`,

and

`s_2(C)>=sigma0 L`, `sigma0=sqrt(47/48)=0.9895285072531598...`.

The r38 quantitative alignment theorem gives, for

`d := D_U(E)/L`,

an exact decomposition

`E=U R0 U^T+D0+F`,

where `R0` is symmetric, `D0` is a physical diagonal matrix, `F` is symmetric, and

`||F||F <= c0 d L`,

`c0=12/sqrt(47)=1.7503798979747347...`.

Sources:
- `yspennstate/math-open-problems@be69878c354322977d5741284a7802d2c12a75e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260923T213743Z-fleet01-B08-qform-r36/REPORT.md`;
- `yspennstate/math-open-problems@6691a29d20e3cfd119c67b7b6bc345c68f407712`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260923T234122Z-fleet01-B08-qform-r38/REPORT.md`.

### 1.2 Own r40 carrier contraction

From fleet01/B08 r40, because `EU=0`, every such decomposition obeys

`(1-nu)||R0||op <= xL+2||F||op`,

where `nu=max_i ||U_i||^2`. Therefore, if `nu<=1/48`,

`||R0||op/L <= [x+2c0 d]/(1-1/48)`.

Source: `yspennstate/math-open-problems@e7816c67f620c184df76dcc6bc2b15a1d9621911`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T014447Z-fleet01-B08-qform-r40/REPORT.md`.

### 1.3 Completed fleet02/B08 physical half-cut

The completed designated-partner r28 theorem says that if the orthonormal physical three-frame `W=[w,U]` has maximum row leverage at most `1/48`, then an ORIGINAL-coordinate partition `S disjoint_union T` exists with

`W_S^T W_S >= I_3/4`, `W_T^T W_T >= I_3/4`.

Source: `yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T153836Z-fleet02-B08-qform-r28/REPORT.md`.

### 1.4 Literal-cross volume stability

The completed theorem at `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, states: for an actual literal ORIGINAL-coordinate cross block `M=M0+H`, if

`s_3(M0)>=kappa`, `max_i(P_Ran(M0))_ii<=1/2`, `||H||op<=kappa/16`,

then the full ambient quadratic-plus-affine form has a continuous `C_0` density and

`||p_Q||infinity <23/kappa`.

This theorem retains the perturbing cross block in the actual quadratic form; it is not a random-perturbation deletion.

## 2. New deterministic singular-value lemma

### Lemma 2.1 — `QFORM-STAR-CARRIER-MIN-SINGULAR-v1`

Let `K=K^T` be invertible `2x2`, `k=s_min(K)>0`, `tau>0`, and `beta in R^2`. Define

`H=[[0,0,tau],[K_11,K_12,beta_1],[K_21,K_22,beta_2]]`.

Then

`boxed: s_3(H) >= k tau / sqrt(k^2+tau^2+||beta||^2).`

Equivalently, if

`s = tau/sqrt(tau^2+||beta||^2)`

is the sine of the physical star `b=tau w+U beta` from the carrier plane, then

`boxed: s_3(H) >= k s / sqrt(1+k^2/(tau^2+||beta||^2)).`

**Proof.** For `z=(u,v)` with `u in R^2`, `v in R`, `||u||^2+v^2=1`,

`||Hz||^2=tau^2 v^2+||Ku+beta v||^2`

`>= tau^2 v^2+(k||u||-||beta|| |v|)^2`.

Set `r=||u||`, `q=|v|`. The last expression is the quadratic form of

`G=[[k^2,-k||beta||],[-k||beta||,||beta||^2+tau^2]]`

on `(r,q)`, with `r^2+q^2=1`. Since

`det G=k^2 tau^2`, `lambda_max(G)<=tr G=k^2+tau^2+||beta||^2`,

we have

`lambda_min(G)>=det G/tr G`.

Taking square roots proves the claim. QED.

This inequality is useful exactly where the earlier shear estimate `s_3(H)>=min(tau,k)/(1+||beta||/k)` loses too much for a large aligned star: if `||beta||/tau` is bounded, the new estimate remains of order `k` independently of the absolute star size.

## 3. Robust approximate-alignment crossing

Put

`K=Theta+R0`.

By the child rigidity and r40 contraction,

`s_min(K)/L >= sigma0-[x+2c0 d]/(1-1/48)`.

Define the current ultra-thin alignment threshold from r40

`d_- = 7.544307417596869e-5`.

For every `0<=d<=d_-`, at the worst allowed `x=1/130`,

`||F||op/L <= ||F||F/L <= f0`,

`f0=c0 d_-=0.00013205404047903242...`,

and

`boxed: s_min(K)>=k0 L`,

`k0=0.9814028060379096... L/L`.

The transverse-star amplification gives `tau>=tau0 L`, with `tau0=6.802918795782575...` above.

Assume now the full physical three-frame is diffuse,

`max_i ||W_i||^2<=1/48`.

Apply completed fleet02/B08 r28 to obtain the physical half-cut `S|T`. Put the deleted hub on the `T` side. Since `D0` is physical diagonal, its cross block vanishes. Thus the ACTUAL literal cross block is

`M=[C[S,T],b_S] = M0 + H_F`,

where

`M0=[U_S K U_T^T,b_S]`,

`H_F=[F[S,T],0]`, `||H_F||op<=f0 L`.

Factor the reference as

`M0 = W_S H blockdiag(U_T^T,1)`

with the `3x3` matrix `H` from Lemma 2.1. The half-cut gives

`s_3(W_S)>=1/2`,

and the three nonzero singular values of `blockdiag(U_T^T,1)` are at least `1/2`. Therefore

`s_3(M0)>=s_3(H)/4`.

Let

`s_star=tau/sqrt(tau^2+||beta||^2)`.

Lemma 2.1 and the monotonicity in `k,tau` give

`s_3(M0)/L
 >= [k0/(4 sqrt(1+(k0/tau0)^2))] s_star`

`=: c_star s_star`,

with

`boxed: c_star=0.2428368108056762... .`

Moreover `Ran(M0)=Ran(W_S)` because `K` and `H` are invertible. Hence its physical row leverage is at most

`(1/48)/(1/4)=1/12<1/2`.

The literal-cross stability theorem therefore applies whenever

`f0 <= c_star s_star/16`.

The exact critical sine is

`boxed: s_star >= 0.008700759331563135... .`

A clean sufficient form is `s_star>=1/100`. In that case

`s_3(M0)>=0.002428368108056762 L`,

while

`16||H_F||op <= 0.002112864647664519 L < s_3(M0)`.

Therefore:

### Theorem 3.1 — `QFORM-ULTRATHIN-ALIGNMENT-STAR-ANGLE-ROBUST-v1`

Under the deletion setup above, if

- `p<=1/48`,
- `s_3(C)<=L/130`,
- `max_i ||[w,U]_{i,*}||^2<=1/48`,
- `D_U(E)<=d_- L`, with `d_-=7.544307417596869e-5`, and
- the physical star has transverse sine
  `tau/||b|| >=1/100`,

then the full ambient quadratic form has a continuous `C_0` density satisfying

`boxed: ||p_Q||infinity <9471.382/L.`

Indeed `23/0.002428368108056762=9471.381181333809...`.

No term `F` has been removed: it is retained in the actual literal cross block and consumed only through the proved deterministic volume-stability theorem.

### Consequence for the r40 survivor

The r40 ultra-thin non-scalar layer was

`0<D_U(E)<7.54431e-5 L`.

Theorem 3.1 now pays **all of that layer except the extremely aligned physical-star sublayer**

`boxed: tau/||b|| <0.008700760.`

Thus the remaining diffuse geometry is quantitatively much sharper than the former `star angle <1/2` obstruction: at ultra-small spectral-tail misalignment, an unpaid star must lie within about `0.5` degrees of the top-two child plane.

## 4. Latest completed fleet02/B08 r30 applied to an actual inequality

The latest completed designated-partner result at prepublication refresh is fleet02/B08 r30:

`yspennstate/math-open-problems@747e6c68617cff947d9277b2b6ec8674cf14cee5`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260923T234130Z-auto11b/REPORT.md`.

Its theorem `QFORM-RANK2-CARRIER-DIAGONAL-STRICHARTZ-v1` applies to an exact physical light block

`D+U Lambda U^T`

with carrier row leverage at most `1/4`. If the carrier product is at least `p0 L^2` and a positive-leverage physical diagonal twist has modulus at least `d0 L`, then

`||p_Q||infinity <=12 S_*^(8/9) p0^(-4/9) d0^(-1/5) L^-1`,

continuously.

Apply this to the **exact-alignment endpoint** `D_U(E)=0` of the present deletion geometry. The r38 rigidity gives

`E=U R0 U^T+D0`, `||R0||op<=xL`.

Hence the exact child light block is

`U(Theta+R0)U^T+D0`,

with every carrier leverage at most `1/48`, and

`s_min(Theta+R0)>= (sigma0-1/130)L`

`=0.9818361995608521... L`.

Therefore its carrier eigenvalue product obeys the actual inequality

`boxed: P>=0.9640023227680974 L^2.`

If there is a physical coordinate `j` with `0<||U_j||^2<=1/48` and

`|(D0)_jj|>=L/128`,

then the partner theorem, with

`p0=0.9640023227680974`, `d0=1/128`,

gives

`boxed: ||p_Q||infinity <32.189 S_*^(8/9)/L`,

with a continuous `C_0` density. This is an equation-level application of the latest completed fleet02/B08 result. It also shows that the exact aligned carrier-plus-diagonal endpoint can be paid by a second, independent product-coordinate mechanism whenever a genuine diagonal twist is present; r38's angle-free crossing remains the stronger numerical bound in its own diffuse-three-frame scope.

## 5. Relation to the newest fleet03/B08 tangent-shear result

The newest completed fleet03/B08 r48 theorem (`math-open-problems@cdecc5cd3305f02b20e8fddc2d8dccb38c373cea`) pays an exact aligned rank-two carrier when an indefinite physical twist supplies product currency

`|d_j det R| det(MM^T)`.

The present theorem is complementary: it allows a genuinely nonzero spectral-tail residual `F` and spends it through a literal-cross stability theorem, but currently requires the ultra-thin alignment scale and a transverse star sine at least about `0.0087`. No claim is made that either theorem subsumes the other.

## 6. What remains

The first B08 implication after this run is

`QFORM-ULTRATHIN-SUPERALIGNED-STAR-COMPILER-v1`:

> In the same diffuse deletion chamber, consume the remaining state `D_U(E)<7.54431e-5 L` and `tau/||b||<0.00870076`, where the physical star is huge and almost entirely aligned with the top-two child plane. The likely currencies are the product-safe tangent-shear theorem, the rank-two carrier/diagonal Strichartz theorem, or an exact two-bank reparameterization. Arbitrary complementary spectrum, nonzero `F`, physical diagonals, and affine terms must remain in the full form.

The moderate alignment interval `d_- <= D_U(E)/L <=0.003798734...` is still forced into r39's scalar-carrier normal-form branch by r40, but a stable full-ambient receiver for its nonzero residual remains open. The unrestricted conjecture therefore remains OPEN, and continuity is proved only on the explicit paid branches.

## 7. Arithmetic check

Using

`p0=nu0=1/48`, `x0=1/130`, `c0=12/sqrt(47)`, `d_-=7.544307417596869e-5`,

the constants are

`f0=0.00013205404047903242`,
`r0=(x0+2f0)/(1-nu0)=0.008125701215250136`,
`k0=sqrt(47/48)-r0=0.9814028060379096`,
`tau0=(129/130)sqrt(47)=6.802918795782575`,
`c_star=0.2428368108056762`,
`16 f0=0.0021128646476645187`,
`c_star/100=0.002428368108056762`,
`(16f0)/c_star=0.008700759331563135`,
`23/(c_star/100)=9471.381181333809`,
`(sqrt(47/48)-1/130)^2=0.9640023227680974`,
`12*p0_carrier^(-4/9)*(1/128)^(-1/5)=32.18841920510914`.

These numerical evaluations only check the explicit constants; the proof is the deterministic argument above.
