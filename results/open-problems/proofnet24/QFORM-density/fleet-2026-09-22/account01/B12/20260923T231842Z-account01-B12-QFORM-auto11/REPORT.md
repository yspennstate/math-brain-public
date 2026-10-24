SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T23:18:42Z.
attacking: hub-aligned spectral-packet stability via an inverse-free graph shear; arbitrarily many unbounded signed added eigenmodes collapse to one physical carrier channel, while only a local-row tail is charged.

# account01/B12 — hub-aligned spectral-packet stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T231842Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for the new branch; essential boundedness only.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source boundary

The exact target remains: independent real coordinates with scalar densities bounded by one, arbitrary real symmetric coefficient matrix, and at least three eigenvalues of modulus at least one. No moments, compact support, connected support, Gaussianity, log-concavity, iid assumption, or independence after a spectral rotation is used.

Fresh control was resolved from `yspennstate/math-research-brain/main`; OWNER CONTROL is `2026-09-22.15`, programme revision `2026-09-22.5`. The current `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and this assignment card were read. In particular, I do not use the false pointwise quadratic-phase decay, arbitrary-joint coarea, conditional-density-moment, naive fiber-supremum, or post-rotation independence interfaces.

The designated partner actually applied below is account02/B12:

`yspennstate/math-open-problems@894dfe1e6cc4817c2b3e0bbe46036e4839f10dbf`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T215456Z-account02-B12-QFORM-auto11b/REPORT.md`.

Its Theorem 2.1 (`QFORM-RANKONE-SELF-CARRIER-RETENTION-v1`) is used at the actual final-matrix inequality in Section 5.

A newer account03/B12 theorem, introduced at commit `a25e07c03123944c302875c3eb079b0df394f86c`, gives an arbitrary-orientation spectral-packet Schur budget by spending one reserve direction per unbounded added mode. The theorem below is different: in a geometrically aligned chamber it allows **arbitrarily many** unbounded added modes while spending **zero spectral-count reserve** on their number; only their aggregate physical carrier channel matters.

## 2. Inverse-free graph shear

Split the ORIGINAL coordinates as `H union J`, with `|H|=m`, and write

`A = [[C,B],[B^T,D]]`.

For any deterministic matrix `Q` of size `m x |J|`, define

`T_Q = [[I_m,-Q],[0,I_J]]`.

This corresponds only to the algebraic substitution

`x = z-Qy`, equivalently `z=x+Qy`.

A direct multiplication gives the exact identity

`T_Q^T A T_Q = [[C,R_Q],[R_Q^T,S_Q]]`,                       (2.1)

where

`R_Q = B-CQ`,                                                   (2.2)

`S_Q = D-Q^T B-B^T Q+Q^T C Q`.                               (2.3)

No inverse of `C` is required. Thus this remains valid for singular, even rank-one, physical cores.

For a symmetric addition

`E = [[K,L],[L^T,M]]`,

its sheared blocks are

`T_Q^T E T_Q
 = [[K, L-KQ],
    [L^T-Q^T K, M-Q^T L-L^T Q+Q^T KQ]]`.                     (2.4)

Hence the exact graph-gauge cone is

`G_Q={ G K G^T : K=K^T },   G=[I_m;Q^T]`.                     (2.5)

Indeed, for `E=GKG^T`, both non-core blocks in (2.4) vanish. The addition changes only the conditional core matrix after the shear. Since `G` has full column rank, the nonzero inertia of `GKG^T` equals the inertia of `K`; positive and negative packets of arbitrary magnitude are both allowed.

### Spectral-mode defect formula

Let one added eigenmode be

`E_theta = theta v v^T`, `v=(a,b)` relative to `H union J`.

Put

`e=b-Q^T a`.                                                     (2.6)

Then

`T_Q^T E_theta T_Q
 = theta [a;e][a;e]^T`.                                          (2.7)

Therefore the departure from the graph is measured exactly by `e`:

- core contribution: `theta a a^T`;
- cross defect: `theta a e^T`;
- complement defect: `theta e e^T`.

In particular, an arbitrarily large signed eigenmode with `b=Q^T a` has **zero cross and complement defect** after the shear. For a packet `sum theta_j v_jv_j^T`, these identities add exactly.

Probabilistic warning: `(z,y)` is not declared independent. Conditional on the ORIGINAL outside vector `Y=y`, however, `z=X_H+Qy` is a deterministic translation of the independent coordinates `X_H`, so their scalar density caps are preserved. The probability estimate below is ultimately applied in the original coordinates through the partner theorem, not by pretending the shear preserves global independence.

## 3. Arbitrarily many aligned signed eigenmodes collapse to one hub channel

Fix a unit vector `u in R^m`. Suppose a baseline has

`C_0=lambda_0 u u^T`,                                           (3.1)

`B_0=u w_0^T+R`, with `u^T R=0`.                                (3.2)

Let

`E=sum_a theta_a v_a v_a^T`                                    (3.3)

be any finite spectral packet, with the `v_a` orthonormal if this is taken from a spectral decomposition. Assume only that every physical `H`-projection is collinear with the same hub direction:

`P_H v_a = alpha_a u`.                                          (3.4)

Write `b_a=P_Jv_a`. Then, exactly,

`E[H,H]=(sum_a theta_a alpha_a^2) u u^T`,                       (3.5)

`E[H,J]=u (sum_a theta_a alpha_a b_a)^T`.                       (3.6)

Thus after **arbitrarily many** added modes, with arbitrary signs and arbitrary magnitudes,

`C_*=lambda u u^T`,                                              (3.7)

`B_*=u w^T+R`,                                                   (3.8)

where

`lambda=lambda_0+sum_a theta_a alpha_a^2`,                     (3.9)

`w=w_0+sum_a theta_a alpha_a b_a`.                              (3.10)

The transverse matrix `R=(I-uu^T)B_*` is **exactly invariant**. No individual `|theta_a|` appears in the deterministic carrier estimate below.

This is the key additional-eigenvalue reduction: a potentially very high-rank signed spectral packet is compressed to the two aggregate quantities `lambda` and `w`, provided all its physical `H`-footprints lie in one line.

## 4. Exact row-carrier lower bound

Assume `lambda !=0`. Put

`q=w/lambda`, `t=||q||`, and `Q=u q^T`.                          (4.1)

Then

`B_*=C_*Q+R`.                                                     (4.2)

Let

`W_*=[C_*,B_*]`.                                                  (4.3)

Right-multiplication by the block shear gives

`W_* [[I_m,-Q],[0,I_J]]=[C_*,R]`.                               (4.4)

For rank-one `Q=u q^T`, the smallest singular value of the inverse shear is exactly

`gamma(t):=(sqrt(t^2+4)-t)/2
          =2/(sqrt(t^2+4)+t)`.                                  (4.5)

Since `u^T R=0`,

`[C_*,R][C_*,R]^T=lambda^2 uu^T+RR^T`,                          (4.6)

an orthogonal row-space sum. If

`d:=s_2(R)>0`,                                                    (4.7)

then

`s_3([C_*,R]) >= min(|lambda|,d)`.                              (4.8)

Combining (4.4)-(4.8),

`boxed:
 s_3(W_*) >= gamma(||w||/|lambda|) min(|lambda|,d).`             (4.9)

This is magnitude-free in every individual added eigenvalue. It depends only on the final aggregate carrier strength and the relative hub slope.

### Why the slope cannot simply be deleted

Take `m=3`, `u=e_1`, `lambda=1`, and

`R=[[0,0],[0,1],[1,0]]`, `w=(M,0)`.

Then `s_2(R)=1`, but the nontrivial 2x2 row Gram block is

`[[1+M^2,M],[M,1]]`,                                             (4.10)

whose smaller eigenvalue is

`(M^2+2-M sqrt(M^2+4))/2 ~ M^{-2}`.                             (4.11)

Hence `s_3(W_*)~M^{-1}`. A bounded aggregate slope (or another fleet exit) is genuinely needed for this carrier mechanism.

## 5. Local-row-tail stability and actual application of account02/B12

Now allow an arbitrary further symmetric perturbation `T`, but charge only its rows touching `H`:

`epsilon:=||P_H T||op`.                                         (5.1)

The `J x J` block of `T` may therefore have arbitrarily large norm and spectrum. An arbitrary complement-only matrix `S` with `P_H S=0` is completely free as well.

Assume there are fixed numbers `L>0`, `q_0>=0` such that

`|lambda|>=L`,                                                   (5.2)

`||w||/|lambda|<=q_0`,                                          (5.3)

and

`L>(m+1)epsilon`.                                                (5.4)

Set

`r:=||R||op`,                                                     (5.5)

`g_L:=gamma(q_0) min(L,d)`,                                     (5.6)

`alpha_L:=(L-(m+1)epsilon)/m`,                                  (5.7)

`H_L:=(1+sqrt(m-1)) m epsilon
      (q_0 L+r+epsilon)/(L-(m+1)epsilon)`,                       (5.8)

and

`Delta_L:=g_L-2epsilon-H_L`.                                    (5.9)

### Theorem 5.1 — `QFORM-HUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`

If `Delta_L>0`, then every independent cap-one product input satisfies

`boxed:
 ||p_(X^T A X)||_(infinity,ess)
 <= 2^(11/4) binom(m-1,2)^(1/8)
    /sqrt(alpha_L Delta_L).`                                    (5.10)

This is uniform in:

- the number of aligned added eigenmodes;
- every magnitude `|theta_a|`;
- every sign of every `theta_a`;
- arbitrary complement-only signed spectrum;
- any additional small signed spectral packet absorbed into `T` through its operator norm.

#### Proof

Let the actual final row block be `W=P_H A`. Since only `T` changes the `H` rows beyond the aligned packet,

`||W-W_*||op<=epsilon`.                                         (5.11)

By (4.9), monotonicity of `gamma`, and (5.2)-(5.3),

`s_3(W)>=g_L-epsilon`.                                          (5.12)

Let `C=A[H,H]`. It is a rank-one matrix `lambda uu^T` plus a perturbation of norm at most `epsilon`. Therefore

`c:=s_1(C)>=|lambda|-epsilon`,                                  (5.13)

`b:=s_2(C)<=epsilon`.                                           (5.14)

The partner theorem uses

`alpha=c/m-b`,                                                   (5.15)

so

`alpha >= (|lambda|-(m+1)epsilon)/m >= alpha_L>0`.              (5.16)

For the partner's selected literal pivot row, its cross-row norm `h` is certainly bounded by the whole cross-block norm:

`h<=||A[H,J]||op
  <=||w||+r+epsilon
  <=q_0 |lambda|+r+epsilon`.                                    (5.17)

The partner penalty is

`eta_m h=((1+sqrt(m-1))b/alpha)h`.                              (5.18)

Using (5.14)-(5.17), with `x=|lambda|`,

`eta_m h
 <=(1+sqrt(m-1)) m epsilon
   (q_0 x+r+epsilon)/(x-(m+1)epsilon).`                          (5.19)

The scalar function on the right is decreasing for `x>(m+1)epsilon`, because the derivative of

`(q_0 x+r+epsilon)/(x-(m+1)epsilon)`                            (5.20)

has numerator

`-[q_0(m+1)epsilon+r+epsilon] <0`                               (5.21)

(unless all terms vanish, in which case it is constant). Hence (5.19) is at most `H_L`.

The designated account02/B12 theorem now applies to the **actual final matrix** with

`g=s_3(W)`,                                                      (5.22)

and yields

`s_2(B#)>= g-b-eta_m h`.                                        (5.23)

Equations (5.12), (5.14), and (5.19) therefore give the actual inequality

`boxed: s_2(B#)>=Delta_L.`                                      (5.24)

Its density conclusion is precisely (5.10). No added quadratic remainder is convolved independently, and no spectral-coordinate independence is asserted. QED.

### Small-eigenvalue compiler

If a further symmetric spectral packet `F_small` has every eigenvalue in `[-h,h]`, then

`||F_small||op<=h`.                                              (5.25)

Therefore it is absorbed by replacing `epsilon` with `epsilon+h` in Theorem 5.1, regardless of its rank, signs, or eigenvectors. Thus arbitrarily many smaller eigenvalues cost only their maximum absolute magnitude.

## 6. Exact target-class family and numerical constant

Take `m=3`, two active complement coordinates, and

`u=e_1`, `q=(1,0)`,                                               (6.1)

`R=[[0,0],[0,2],[2,0]]`.                                        (6.2)

Then

`d=s_2(R)=2`, `r=||R||op=2`, `||q||=1`.                         (6.3)

Let `g=(u,q)` in the combined `H union J` coordinates. Start from

`A_0 = 4 g g^T + [[0,R],[R^T,0]]`,                              (6.4)

and add

`tau g g^T`,                                                     (6.5)

where `tau` is arbitrary subject only to

`|4+tau|>=4`.                                                    (6.6)

The added rank-one matrix has its single nonzero eigenvalue

`2 tau`,                                                         (6.7)

so this permits arbitrarily large positive additions and arbitrarily large negative additions with a complete sign reversal of the physical carrier.

Also add any symmetric matrix supported entirely on extra spectator coordinates (hence giving literal additional eigenvalues of arbitrary number, signs and magnitudes), and finally any symmetric `T` with

`||P_H T||op<=1/100`.                                            (6.8)

Here `L=4`, `q_0=1`, `epsilon=0.01`, and

`gamma(1)=(sqrt(5)-1)/2
        =0.6180339887498948...`,                                 (6.9)

`g_L=1.2360679774997897...`,                                    (6.10)

`alpha_L=1.32`,                                                  (6.11)

`H_L=0.1099198750747144...`,                                    (6.12)

`Delta_L=1.1061481024250753...`.                                (6.13)

The partner theorem therefore gives

`boxed:
 ||p_(X^T A X)||_(infinity,ess)
 <=5.567226402756524... <5.568.`                                 (6.14)

Moreover, directly from (5.12),

`s_3(P_H A)>=g_L-0.01
           =1.2260679774997897...>1`.                            (6.15)

Since left multiplication by a coordinate projection cannot increase singular values,

`s_3(P_H A)<=s_3(A)`.                                            (6.16)

Thus

`boxed: s_3(A)>1`,                                               (6.17)

so every matrix in this family lies literally inside the owner's target class.

The spectator block may contain arbitrarily many literal eigenvalues above or below one, of either sign and arbitrarily large magnitude. The local-row tail may in addition contain arbitrarily many small signed eigenvalues. None is treated as an independent random quadratic error.

## 7. Arbitrarily many genuine spectral modes in the aligned chamber

The collinear-projection condition (3.4) is compatible with an arbitrarily large orthonormal spectral family. For any `N>=2`, let the complement contain `R^N`, put

`b_j=e_j-(1/N)1`,                                                (7.1)

and

`v_j=N^(-1/2)u \oplus b_j`, `j=1,...,N`.                        (7.2)

Then the `v_j` are orthonormal because

`||b_j||^2=1-1/N`, `b_j^T b_k=-1/N` for `j!=k`.                 (7.3)

For arbitrary signed eigenvalues `theta_j`, the packet

`E=sum_j theta_j v_jv_j^T`                                      (7.4)

has

`lambda`-increment `N^(-1) sum_j theta_j`,                      (7.5)

and hub-cross increment

`N^(-1/2) sum_j theta_j b_j`.                                   (7.6)

In particular, setting `theta_j=tau+xi_j` and using `sum_j b_j=0`, an arbitrarily large common signed shift `tau -> +infinity` or `tau -> -infinity` sends **all N added eigenvalues** to unbounded magnitude while the cross increment from that common shift is exactly zero. The number `N` costs no reserve direction in Theorem 5.1.

This is precisely where the theorem differs from a generic rank-budget argument: geometric collapse of the physical projections can make an unbounded spectral packet effectively one-dimensional on the carrier.

## 8. What remains open

The bare hypothesis `s_3(A)>=1` does **not** yet force the existence of an original-coordinate set `H` and a hub direction `u` for which all dangerous added spectral modes have collinear `H`-projections and bounded aggregate slope `||w||/|lambda|`. Nor is it proved that failure of every such hub-aligned certificate forces one of the already-paid D5, projected-crossing, grouped-bank/hub, ridge, half-Riesz, physical-pair, or Schur exits.

Therefore this is a real additional-eigenvalue stability theorem, not a solution of the unrestricted conjecture. The theorem establishes an essentially bounded density in its scope. A continuous representative is not claimed here because the partner scalar-Schur branch only supplies essential boundedness.
