# QFORM fleet03/B04 r23 — optimized projection/volume-weight certificate

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** B04-20260923T032130Z-r23  
**Role:** Product Fourier rearrangement  
**Status:** NEW SUPPORTING THEOREM + INDEPENDENT REVIEW PASS ON THE CHECKED MATRIX/TAIL CHAIN; FULL QFORM OPEN  
**Execution label:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and live obligation

For arbitrary independent real coordinates with probability densities `0<=f_i<=1` and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample. No moments, support bounds, Gaussianity, log-concavity, iid assumption, or independence after spectral rotation is used here.

The current B04 obligation is to optimize an admissible projection/third-volume certificate on the actual physical cross matrix, after independently checking the new matrix/tail certificate in

`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

and `PEER_TAIL_EXTENSION.md` in the same directory. I checked the matrix identity, the projection-to-marginal inequality, the q-dependent Hausdorff--Young/Brascamp--Lieb step, and the Fourier inversion constants. I found no error in that checked chain. The argument below then improves and extends its fixed `q=4/3` choice.

The scheduled peer result used at equation level is fleet01/B20

`math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T234545Z-fleet01-B20-QFORM-auto11/REPORT.md`,

which proves the exact singular-value inequality

`T2 E2 <= 3 E3`,  where `T2=sum_{j>=3}s_j(M)^2` and `Ek=e_k(M^T M)`.

The designated partner `fleet04/B04` still had no canonical current-QFORM report or shared handoff at the fresh lookup, so no partner theorem is invented.

## 2. Reviewed ingredients

Let `M` be a physical ORIGINAL-coordinate cross block. Put `lambda_j=s_j(M)^2`, `E2=e2(lambda)`, `E3=e3(lambda)>0`. Under squared third-minor volume sampling, let `alpha_i` be the row inclusion marginals. The exact marginal matrix is

`W=U diag(p_j) U^T`,

`p_j=lambda_j e2(lambda without j)/E3`,

and therefore

`W<=I`,  `W<=(E2/E3) M M^T`.

Fleet01/B20's identity gives

`E2/E3 <= 3/T2`,

hence

`W <= (3/T2) M M^T`.                                               (2.1)

For an orthogonal projection `P` on the row space, define

`L=max_i P_ii`,  `epsilon=||(I-P)M||op`,  `rho=epsilon/sqrt(T2)`,  `delta=sqrt(3) rho`.

Then, for each physical row coordinate `e_i`,

`sqrt(alpha_i)=||W^(1/2)e_i||`

`<=||W^(1/2)P e_i||+||W^(1/2)(I-P)e_i||`

`<=sqrt(P_ii)+delta sqrt(1-P_ii)`.                                 (2.2)

The first term uses `W<=I`; the second uses (2.1). This step is coordinate-product preserving: `P` is used only in a matrix inequality and no random coordinate rotation is made.

The reviewed q-dependent fractional-volume Fourier theorem states: if `1<=q<3/2` and every `alpha_i<=q/2`, then for the full ambient quadratic-plus-affine form, including arbitrary same-bank quadratic terms and outside couplings,

`||p_Q||inf <= C(q) E3(M)^(-1/6)`,

`C(q)=3e/[(3-2q)sqrt(q)]`,                                        (2.3)

and the density has a continuous representative vanishing at infinity.

I independently checked (2.3): after decoupling in original coordinates, the BL/Hausdorff--Young estimate gives

`|phi_Q(t)| <= min(1,K |t|^(-3/(2q)))`,

with `K^(2q/3)=e*pi*q^(-1/2)*E3^(-1/6)`. Integrating this envelope and dividing by `2pi` gives exactly (2.3). Also

`d/dq log C(q)=2/(3-2q)-1/(2q)=(6q-3)/(2q(3-2q))>0`               (2.4)

for every `q>=1`. Thus the smallest admissible q is optimal inside this theorem.

## 3. New theorem: optimized projection/volume gate

### Theorem `QFORM-OPTIMIZED-VOLUME-MARGINAL-GATE-v1`

Assume `L<=1/2` and `delta<=1`. Define

`A(L,rho)=[sqrt(L)+sqrt(3)rho sqrt(1-L)]^2`.                        (3.1)

If `A(L,rho)<3/4`, set

`q_* = max(1, 2 A(L,rho))`.                                        (3.2)

Then `1<=q_*<3/2`, every third-volume row marginal satisfies `alpha_i<=q_*/2`, and the full ambient quadratic form obeys

`||p_Q||inf <= C_*(L,rho) E3(M)^(-1/6)`,                           (3.3)

where

`C_*(L,rho)=3e` if `A(L,rho)<=1/2`,

and

`C_*(L,rho)=3e / ([3-4A(L,rho)] sqrt(2A(L,rho)))`                  (3.4)

if `1/2<A(L,rho)<3/4`.

The density is continuous and vanishes at infinity.

### Proof

For `0<=l<=1/2` and `0<=delta<=1`, the function

`s(l)=sqrt(l)+delta sqrt(1-l)`

is increasing: its stationary point is `l=1/(1+delta^2)>=1/2`. Therefore (2.2) gives

`alpha_i <= s(P_ii)^2 <= s(L)^2=A(L,rho)`.

If `A<=1/2`, the endpoint `q=1` is admissible. If `1/2<A<3/4`, `q=2A` is admissible and lies below `3/2`. Equation (2.4) shows this is the optimal admissible q in the reviewed q-family. Substitution into (2.3) gives (3.3)--(3.4). QED.

This is not a pointwise van-der-Corput estimate. It is an integrated product-space Fourier bound with the volume weights optimized before inversion.

## 4. Quantitative consequences

### 4.1 Previously used `rho=1/15` gate

With `L=1/2`, `rho=1/15`, put `d=sqrt(3)/15`. Then

`A=(1+d)^2/2=0.6221367205045919...`,

`q_*=(1+d)^2=1.2442734410091838...`.

Hence

`C_*=14.29394117441255...`,                                       (4.1)

improving the fixed-`q=4/3` coefficient

`9sqrt(3)e/2=21.1869100628203...`.

### 4.2 Relaxed top-two tail stable-rank threshold

Take `P` onto the top two left singular vectors. Then `epsilon=s3(M)` and

`rho=s3(M)/sqrt(T2)`.

For `L<=1/2`, the optimized gate remains finite whenever

`rho < rho_*=[sqrt(3/2)-1]/sqrt(3)=0.1297565119969217...`,          (4.2)

because this is exactly the condition `(1+sqrt(3)rho)^2/2<3/4` in the worst case `L=1/2`.

Equivalently it is enough that

`T2/s3(M)^2 > 1/rho_*^2 = 59.39387691339818...`.                  (4.3)

Thus the prior simple sufficient threshold `225` is not intrinsic to the volume method. For instance stable tail rank at least `64` already gives a finite explicit bound. If one insists only on the worst-case leverage `L=1/2`, the coefficient at `rho=1/8` is `166.6516672276...`; actual smaller leverage can be dramatically better.

### 4.3 Improved near-diffuse perturbation theorem

Suppose `M=M0+E`, `s3(M0)>=a>0`, `max diag(P_range(M0))<=1/2`, and `||E||op<=a/16`. Put `P=P_range(M0)` and `kappa=s3(M)`. Then

`kappa>=15a/16`, `epsilon<=a/16`, and since `T2>=kappa^2`,

`rho<=epsilon/kappa<=1/15`.

Apply (4.1), and use `E3(M)>=s1^2 s2^2 s3^2>=kappa^6`. This yields

`||p_Q||inf <=14.29394117441255 / kappa`

`<=15.24687058604004 / a`.                                       (4.4)

So the reviewed `<23/a` perturbation theorem sharpens, under exactly the same hypotheses, to

`boxed: ||p_Q||inf < 15.247/a`.

Continuity and `C_0` regularity are retained.

## 5. Explicit genuinely rotated indefinite family

Let `m` be a Sylvester-Hadamard order, `m>=32`, let `U=H_m/sqrt(m)`, and set `N=m-2`. Define

`M_m = U diag(1,1,N^(-1/2),...,N^(-1/2)) U^T`,

and the `2m x 2m` symmetric physical matrix

`A_m = [[0,M_m],[M_m,0]]`.

This is genuinely rotated in the original coordinates. Its eigenvalues are

`+1,+1,-1,-1`, together with `+N^(-1/2)` and `-N^(-1/2)` each repeated `N` times. Hence it satisfies the exact target spectral hypothesis and is indefinite.

Let `P` project onto the top two left singular vectors of `M_m`. Because those vectors are two normalized Hadamard columns,

`L=max_i P_ii=2/m`.

Also

`T2=N*(1/N)=1`, `epsilon=s3(M_m)=N^(-1/2)`, `rho=N^(-1/2)`.

The marginal gate simplifies exactly:

`sqrt(A)=sqrt(2/m)+(sqrt(3)/sqrt(m-2))*sqrt((m-2)/m)`

`=(sqrt(2)+sqrt(3))/sqrt(m)`,

so

`A=(5+2sqrt(6))/m`.                                               (5.1)

For every `m>=32`, `A<1/2`; hence the optimal endpoint is already `q=1`, and

`||p_(X^T A_m X)||inf <=3e E3(M_m)^(-1/6) <3e`.                  (5.2)

Here

`E3(M_m)=1+(N-1)/N+(N-1)(N-2)/(6N^2)>1`.

Therefore, for arbitrary independent cap-one input laws and every Hadamard order `m>=32`,

`boxed: ||p_(X^T A_m X)||inf < 3e = 8.154845485377136...`.        (5.3)

The density is continuous and vanishes at infinity. Every individual cross entry satisfies

`|(M_m)_ij| <= (2+sqrt(N))/m = O(m^(-1/2))`,

so the result pays aggregate third-volume structure before any local coefficient is inverted.

For `m=32`, the exact coefficient from (5.2) is approximately `7.1966049073`; the clean universal display (5.3) is retained.

This family is substantially outside the old crude `L=1/2, T2/s3^2>=225` sufficient test: at `m=32`, `T2/s3^2=N=30`, yet the actual low leverage makes `q=1` admissible.

## 6. Why this matters to the full proof map

The new gate converts the diffuse/tail branch into a continuous tradeoff rather than the old binary `max leverage<=1/2` plus `rho<=1/15` cutoff. The structural obligation can now be phrased quantitatively:

- if a physical cross block has a row projection `P` with `L<=1/2` and `A(L,rho)<3/4`, the branch is paid by (3.3);
- therefore a surviving un-paid matrix must force, for every relevant projection/tail decomposition, either high leverage or `A(L,rho)>=3/4`, i.e. a genuinely concentrated/low-tail geometry.

This is useful for N3 assembly because it enlarges the paid collective-tail region and improves constants without assuming a good individual physical minor.

It does **not** prove that every matrix with three large eigenvalues admits such a physical cross block. The remaining structural bridge from the bare spectral hypothesis to one of the paid diffuse-volume, low-cross-rank, hub/star, ridge, or grouped-bank endpoints is still open.

## 7. Correction-awareness and regularity

No refuted premise is used: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint coarea bound, no worst conditional-density supremum, and no universally well-conditioned physical minor. The theorem keeps original-coordinate product provenance throughout the decoupling/BL step.

Unlike several earlier half-Riesz branches, this Fourier branch proves a **continuous** density vanishing at infinity because the optimized characteristic-function envelope is integrable.

## 8. Independent-review status

This run is one of the two workers specifically assigned to check the new volume-stability extension. My review outcome on the checked chain is **PASS**: equations (2.1)--(2.4), the perturbation gate, the tail extension, and the constants are internally consistent under the stated hypotheses. This is a review of the supporting theorem, not an end-to-end review of full QFORM.

The full conjecture remains **OPEN** and therefore this recurring worker should continue. The next B04 step is to use the optimized two-parameter gate `(L,rho)` inside an actual no-pivot/N3 structural alternative, especially the high-leverage/small-tail boundary where `A(L,rho)>=3/4`, rather than returning to a pointwise Fourier estimate.
