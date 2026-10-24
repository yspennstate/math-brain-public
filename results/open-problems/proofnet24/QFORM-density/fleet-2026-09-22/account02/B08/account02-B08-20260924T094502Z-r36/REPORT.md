SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-24T09:45:02.148654Z.
attacking: QFORM-PUNCTURED-DOUBLEALIGNED-RANK2-TUBE-INTERPOLATION-v1: quantify the double-alignment tube and build a product-source-valid obstruction/receiver around the paid exact endpoint.

# account02/B08 r36 — literal three-bank crossing energy and an exact punctured-collar stress family

Programme: `QFORM-DENSITY-3EIG-20260922`.  Status: **NEW SUPPORTING STRUCTURAL THEOREM + TARGET-VALID PUNCTURED-COLLAR STRESS FAMILY / FULL QFORM OPEN**.  Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. The first unpaid implication after this run is

`QFORM-THREEBANK-TWISTED-CARRIER-OR-DOUBLECANCEL-COMPILER-v1`:

on the newest edge-capped diffuse branch, consume either (i) three disjoint ORIGINAL-coordinate source banks each carrying a target-scale literal crossing direction of the same rank-two carrier, or (ii) the already isolated two-mode complementary-cancellation branch; on the aligned deletion-child branch the receiver must also be uniform through the genuinely punctured double-alignment collar `s_3(C) downarrow 0`, where the exact endpoint is paid but the naive diffuse-third-mode Fourier bound diverges. No post-rotation independence or small-random-perturbation step is permitted.

## 1. Fresh source state used

The newest compatible localized/diffuse split is account01/B08 r47, canonical mathematics `73e69c64a5499c82342a527bc232d531b54f6874`. In its still-unpaid diffuse selected-three branch there is an ORIGINAL-coordinate cut `S union T`, a localized physical row `k in S`,

`D=A[S\{k},T]`, `z=A[k,T]`,

and

`sigma = sqrt(67/800)/2 = 0.14469796128487783...`

such that either

`(DC)  s_2(D)<sigma L` and `s_2((A-A_3)[S\{k},T])>sigma L`,

or

`(R2)  s_2(D)>=sigma L`, `dist(z,V_2(D))<||z||/2`,

and the actual top-two right singular carrier `V_2(D)` contains a unit vector `u` with

`||u_{K_r}||>=1/8`                                                (1.1)

on at least three pairwise-disjoint ORIGINAL-coordinate banks `K_1,K_2,K_3 subset T`. This branch came after the explicit actual spectral/localized gates and after the completed third-compound payment `||p_Q||_infinity<=665.986/L` on relative non-alignment.

The newest completed account03/B08 partner state is `QFORM-PUNCTURED-CROSSSTAR-DOUBLEALIGN-ROUTER-v1`, canonical mathematics `19c12072f7e67266ce894042034bcabb9c376bea`. In its nonlocalized punctured survivor

`A=[[a,b^T],[b,C]]`, `C=V Lambda V^T+E`,

`max_i ||V_i||^2<=1/16`, `s_2(C)>=sqrt(47/48)L`, `dist(b,range(V))<||b||/4`, and

`0<s_3(C)=||E||_op<L/4096`.                                      (1.2)

A literal child cut `J union K` has `s_2(C[J,K])>=0.3195945335L`, `s_3(C[J,K])<L/4096`; unless a completed payment/localized-row alternative has already fired, both hub-augmented crossings are within `0.0156269073L` of rank two and each star half is within `L/64` of the corresponding top-two singular plane. The exact point `(dist(b,range(V)),s_3(C))=(0,0)` was paid in the preceding endpoint theorem by `<362.039/L` (essential bound).

## 2. New deterministic theorem — three-bank footprint implies three literal target-scale crossing energies

### Theorem 2.1 — `QFORM-THREEBANK-R2-LITERAL-ENERGY-v1`

Let `D` be any real matrix with

`s_2(D)>=sigma L`,                                                (2.1)

and let `R=V_2(D)` be a chosen top-two right singular subspace. Suppose `u in R`, `||u||=1`, and there are three pairwise-disjoint physical coordinate banks `K_1,K_2,K_3` satisfying

`||u_{K_r}||>=1/8`, `r=1,2,3`.                                  (2.2)

Then for each `r` there is a unit vector `w_r`, supported entirely on the ORIGINAL coordinates in `K_r`, such that

`boxed: ||D w_r||_2 >= (sigma/8)L
       =0.01808724516060973... L.`                               (2.3)

Equivalently, each literal sub-crossing carries target-scale Frobenius energy:

`boxed: ||D[:,K_r]||_F >= (sigma/8)L.`                           (2.4)

The three `w_r` have disjoint physical supports. Consequently the three source blocks on which they live remain genuinely independent product blocks; (2.3) does **not** assert that any rotated residual variables are independent.

#### Proof

For each bank put

`w_r=u_{K_r}/||u_{K_r}||`.

Then `w_r` is a unit vector with physical support in `K_r` and

`<u,w_r>=||u_{K_r}||>=1/8`.                                     (2.5)

Let `P_R` be the orthogonal projection onto the top-two right singular plane. Since `u in R`,

`||P_R w_r|| >= |<u,w_r>| >=1/8`.                               (2.6)

The spectral decomposition of `D^T D` gives the PSD inequality

`D^T D >= s_2(D)^2 P_R`.                                        (2.7)

Therefore

`||D w_r||^2
 = <w_r,D^T D w_r>
 >= s_2(D)^2 ||P_Rw_r||^2
 >= (sigma L/8)^2`,                                              (2.8)

which proves (2.3). Since `w_r` is supported on `K_r`,

`||D[:,K_r]||_op >= ||Dw_r||`,                                  (2.9)

and operator norm is at most Frobenius norm, proving (2.4). QED.

### Corollary 2.2 — quantitative sharpening of the newest localized/diffuse survivor

Insert `sigma=sqrt(67/800)/2` from account01/B08 r47. Every still-unpaid `R2` branch now contains **three disjoint original-coordinate source banks** `K_r` for which

`s_1(D[:,K_r]) >= 0.01808724516060973... L`,                     (2.10)

whereas the complementary `DC` branch carries two independent cancellation singular directions at scale `0.14469796128487783...L`.

This is stronger than a carrier-footprint statement alone: the footprint is converted into a literal coefficient-energy gate in the physical matrix, without selecting a single edge and without paying a reciprocal minor. It is also source-valid: all three banks are disjoint before any linear change of the random variables.

## 3. A blockwise twisted-Fourier resource that preserves product provenance

The three-bank gate suggests a grouped rather than coordinatewise receiver. The following observation records exactly what remains legal at the source level.

### Lemma 3.1 — `QFORM-BLOCK-TWISTED-PROJECTION-LP-v1`

Let `K` be a set of ORIGINAL independent coordinates, let `w` be a unit vector supported on `K`, and put `Y=<w,X_K>`. The standard one-dimensional projection theorem for product densities bounded by one gives

`||p_Y||_infinity <= sqrt(2)`.                                   (3.1)

For any measurable real phase `tau(X_K)`, define

`G(s)=E exp(i tau(X_K)+ i s Y)`.                                 (3.2)

Then for every `p>=2`,

`boxed: integral_R |G(s)|^p ds <= 4 pi sqrt(2)/sqrt(p).`          (3.3)

#### Proof

Disintegrate with respect to `Y`. The complex measure in (3.2) has a density `h(y)` satisfying `|h(y)|<=p_Y(y)`, hence `||h||_1<=1` and `||h||_infinity<=sqrt(2)`. After the dilation `Z=sqrt(2)Y`, the corresponding complex density is dominated by a probability density bounded by one. Apply the completed one-dimensional twisted Hausdorff--Young interpolation lemma from the fixed Fourier package, then scale frequency back by `sqrt(2)`. This gives (3.3). QED.

For the three disjoint banks in Theorem 2.1, this estimate is available separately on all three banks with arbitrary internal twists. The missing step is algebraic, not a source-cap issue: one must expose a common Fourier parameter through three bank-supported carrier directions while retaining the unrestricted same-bank quadratic terms. Conditioning on rotated complements is not allowed.

## 4. Exact target-valid obstruction at the account03/B08 punctured double-alignment collar

The account03 collar is genuine even when every physical `2 x 2` principal block is weak.

Let `m=2^q` with `m>=16384`. On the Walsh group choose three normalized characters `u_1,u_2,u_3` and an independent sign character `chi`; take the physical half-cut

`J={chi=+1}`, `K={chi=-1}`,

with the characters chosen so that the restrictions of `u_1,u_2,u_3` to either half remain mutually orthogonal. Add one physical hub coordinate `h`. For `0<epsilon<1/4096`, set

`C_epsilon = L(u_1u_1^T+u_2u_2^T+epsilon u_3u_3^T)`,
`b = sqrt(2)L u_1`, `a=0`,

and

`A_epsilon = [[0,b^T],[b,C_epsilon]].`                           (4.1)

In the orthogonal basis `(h,u_1,u_2,u_3)` the nonzero block is

`L * [[0,sqrt(2),0,0],
      [sqrt(2),1,0,0],
      [0,0,1,0],
      [0,0,0,epsilon]]`.                                        (4.2)

Hence

`boxed: spec_nonzero(A_epsilon)={2L,-L,L,epsilon L}.`             (4.3)

Thus (4.1) is a genuine QFORM target matrix, with exactly three eigenvalues of modulus at least `L`.

For the child, `V=[u_1,u_2]`, `s_2(C_epsilon)=L`, `s_3(C_epsilon)=epsilon L<L/4096`, and `b in range(V)` exactly. On the chosen physical half-cut,

`D=C_epsilon[J,K]`

has singular values exactly

`boxed: L/2, L/2, epsilon L/2`,                                  (4.4)

because `sqrt(2)u_j|_J` and `sqrt(2)u_j|_K` are orthonormal families. Moreover

`b_K in R_2(D)`, `b_J in L_2(D)`,                               (4.5)

so both account03 star-alignment distances are **zero**, while the puncture is nonzero. The two hub-augmented crossings have distance exactly `epsilon L/2` from rank two.

No uniformly conditioned physical pair is hidden here. For two light coordinates every entry of the corresponding principal block has magnitude at most `(2+epsilon)L/m`, so its operator norm is at most `2(2+epsilon)L/m<6L/m<L/64`. For a hub-light pair, the off-diagonal entry has magnitude `sqrt(2)L/sqrt(m)` and the determinant has magnitude `2L^2/m`, hence its smaller singular value is at most `sqrt(2)L/sqrt(m)<L/64` for `m>=16384`. Therefore

`boxed: every physical 2 x 2 principal block has sigma_min<L/64.` (4.6)

As `epsilon downarrow0`, `||A_epsilon-A_0||_op=epsilon L`, and `A_0` is precisely an exact aligned rank-two-child endpoint of the partner theorem. Thus this is a literal coefficient collar around the paid endpoint, not a schematic limiting picture.

## 5. Required fixed-source theorem applied to the obstruction

The family (4.1) is **not** a counterexample. Apply the completed generalized Fresnel--Brascamp--Lieb Theorem F from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

on the full set of light ORIGINAL coordinates, conditioning only through the theorem's permitted outside block. The rank-three light frame is `[u_1,u_2,u_3]`; its physical leverage is `3/m<=1/2`, its Gram is the identity, and the three light eigenvalues are `L,L,epsilon L`. The hub scalar and hub-light star are allowed outside the used block. Therefore

`|phi_Q(t)| <= (4 pi)^(3/2) |t|^(-3/2) epsilon^(-1/2)L^(-3/2)`    (5.1)

and the theorem's integrated form gives

`boxed: ||p_{X^T A_epsilon X}||_infinity
       <= 12 epsilon^(-1/3)/L,   p in C_0(R).`                   (5.2)

This is a real target inequality for arbitrary cap-one product sources. For example at `epsilon=2^(-16)`,

`||p||_infinity <= 483.8096831596312.../L`.                      (5.3)

But (5.2) diverges as `epsilon downarrow0`, whereas the exact `epsilon=0` partner endpoint is paid by `<362.039/L`. The obstruction therefore pinpoints a genuine proof gap: neither the diffuse-third-mode Fresnel estimate nor endpoint control alone gives a uniform punctured collar, and coefficient convergence cannot be used as a probabilistic perturbation argument for arbitrary rough product sources.

## 6. Resulting hybrid picture

The newest diffuse/localized split now has a more concrete unpaid rank-two side: after the finite third-compound payment, either the complementary crossing retains two target-scale cancellation singular directions, or one literal deleted crossing has three disjoint source banks each carrying operator/Frobenius crossing energy at least `0.01808724516L`. Independently, the newest account03 deletion-child router shows that the aligned branch can sit arbitrarily close to the exact endpoint while remaining nonzero and while all physical pairs are weak; (4.1) realizes that geometry exactly.

The next useful compiler should therefore be stable under **both** degeneracies: source energy spread over several physical banks in a common rank-two carrier, and a third child curvature tending to zero inside an exactly aligned hub/carrier geometry. A proof that first rotates to the carrier or discards the puncture as a small random perturbation would leave the source class.

No claim of full QFORM, sharp constant, or full-target continuity is made.
