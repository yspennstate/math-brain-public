# fleet02/B20 QFORM r13 — heavy-ridge third-compound transfer

**Run:** `20260922T165822Z-fleet02-B20-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control used:** revision `2026-09-22.8`  
**Assignment:** Proof closure and keeper / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source pins

Target: for every finite `n`, independent real random variables `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid counterexample. No rotated-coordinate independence, compact-support, moment, log-concavity, Gaussian, or diagonal-basis assumptions are introduced here. Continuity is kept separate from essential boundedness.


Newest completed designated partner actually consumed and applied: fleet03/B20 run `20260922T154341Z-fleet03-B20-QFORM-r12`, canonical mathematics `yspennstate/math-open-problems@eb7976d14c75a2a5945e03c6b947774e26fdebcb`. Its high-window theorem is used quantitatively in Section 5.

Also consumed: fleet03/B07 run `20260922T163733Z-fleet03-B07-qform-r12`, canonical mathematics `yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`, especially its full-matrix third-compound O0/O1/O2/O3 reduction and O0 ridge calibration.

Corrections retained: no law-uniform pointwise quadratic-phase decay; no dimension-free fiber-supremum shortcut; no post-rotation independence; no generic conditional three-dimensional spectral-projection density cap; no single-good-minor inference; no raw operator-norm slab-continuity argument under unrestricted translations; and no same-square absorption of arbitrary same-bank curvature.

## 2. Strongest conditional end-to-end state

Let `A` satisfy the target spectral hypothesis.

1. **High-window diffuse branch (fleet03/B20).** Put `P=1_{|A|>=1/64}=UU^T`, `H={i:P_ii>1/64}`. If `||U_H^TU_H||_op<=1/2`, the partner theorem gives a continuous density and
   `||p_Q||_infinity < 194`.

2. **Full-matrix third-compound reduction (fleet03/B07).** Since
   `sum_{|S|=|T|=3} det(A[S,T])^2 = ||wedge^3 A||_HS^2 >=1`, one of O0/O1/O2/O3 occurs. In O0 there is a physical cross cut `B=A[L,R]` with
   `E_3:=e_3(BB^T)>=1/256`.

3. **O0 diffuse ridge (fleet03/B07).** Choose the unique `gamma>0` with
   `K=BB^T(gamma^2 I+BB^T)^{-1}` and `tr K=8/3`. If `max_i K_ii<=1/2`, then `||p_Q||_infinity<19.54`.

4. **O0 ridge-heavy branch (new here).** If some physical row `i` satisfies `K_ii>1/2`, Theorems A and B below force a source-realizable singleton-plus-five-bank packet carrying more than `1/110592` of actual squared third-minor mass. Thus the previous opaque O0 ridge-heavy endpoint is replaced by a concrete original-coordinate aggregate certificate.

5. **Every unresolved target matrix also has high-window energy currency (new here, using the designated partner exactly).** If the partner diffuse condition fails, then either the heavy set carries diagonal square energy at least `1/24576`, or some physical cut has cross Frobenius square exceeding `1/49152`.

Consequently, a full proof now follows from universal analytic payments for O1/O2/O3 and for the new O0 singleton-plus-five-bank packet, with the simultaneous high-window diagonal/cross-cut currency available in every remaining matrix. The unpaid analytic step must tolerate arbitrary self blocks and affine terms while preserving original-coordinate product structure. No full-proof claim is made.

## 3. Theorem A — ridge-heavy row carries actual third-compound mass

### Statement: `QFORM-O0-DPP-HEAVY-THIRD-MASS-v1`

Let `B` be a real matrix, `M=BB^T`, and suppose

`E_3=e_3(M)=sum_{|S|=3,|T|=3} det(B[S,T])^2>0`.

Choose `gamma>0` so that

`K=M(gamma^2 I+M)^{-1}`,  `tr K=8/3`.

For a physical row `i`, define

`E_3(i)=sum_{S: |S|=3, i in S} det(M[S,S])`
`      =sum_{S: |S|=3, i in S} sum_{|T|=3} det(B[S,T])^2`.

If `K_ii>1/2`, then

`E_3(i)/E_3 > 1/48`.

In particular, if `E_3>=1/256`, then

`E_3(i)>1/12288`.

### Proof

Scale by `gamma` and write

`L=M/gamma^2 = V diag(ell_1,...,ell_r) V^T`, `ell_j>0`,

where the zero eigenspace may be omitted. Put

`k_j=ell_j/(1+ell_j)`.

Then

`sum_j k_j=tr K=8/3`.

For the fixed physical row `i`, write `alpha_j=|V_{ij}|^2`. Hence

`K_ii=sum_j alpha_j k_j`.

Consider the fixed-size three determinantal distribution on physical row triples

`P(S)=det(L[S,S])/e_3(L)`, `|S|=3`.

Cauchy-Binet gives the following elementary spectral mixture. First choose an eigen-index triple `J` with probability

`P(J)=prod_{j in J} ell_j/e_3(ell)`;

conditional on `J`, choose `S` with probability `det(V[S,J])^2`. The latter probabilities sum to one by Cauchy-Binet. Conditional on `J`, the one-point inclusion probability of physical row `i` is the diagonal of the rank-three projection onto the chosen eigenvectors, namely

`P(i in S | J)=sum_{j in J} alpha_j`.

Therefore

`P(i in S)=sum_j alpha_j pi_j`,

where

`pi_j = ell_j e_2(ell_{-j})/e_3(ell)`.

On the other hand, because `det(L[S,S])=gamma^{-6}det(M[S,S])`,

`P(i in S)=E_3(i)/E_3`.

It remains to compare `pi_j` and `k_j`. Fix `j` and let `m` be the multiset of all `ell` except `ell_j`, sorted `m_1>=m_2>=...`. Let

`T=sum_{r>=3} m_r`.

If there are fewer than three positive tail terms, the same estimates below hold with `T=0`. Otherwise the third-largest probability among the `m_r` satisfies

`3 m_3/(1+m_3) <= sum_s k_s = 8/3`,

so `m_3/(1+m_3)<=8/9`, hence `m_3<=8`. Thus every `m_r` for `r>=3` is at most eight, and

`T <= 9 sum_{r>=3} m_r/(1+m_r) <= 24`.

Write `e_q(tail)` for the elementary symmetric functions of `m_3,m_4,...`. Then

`e_2(m)=m_1m_2+(m_1+m_2)T+e_2(tail)`,

`e_3(m)=m_1m_2T+(m_1+m_2)e_2(tail)+e_3(tail)`.

Since `e_2(tail)<=T^2` and `e_3(tail)<=T e_2(tail)`,

`e_3(m)<=T e_2(m)<=24 e_2(m)`.

If `k_j=0` there is nothing to prove. Otherwise

`pi_j/k_j`
` = (1+ell_j)e_2(m)/(ell_j e_2(m)+e_3(m))`
` >= (1+ell_j)/(ell_j+24)`
` >= 1/24`.

Hence

`E_3(i)/E_3=P(i in S)`
` =sum_j alpha_j pi_j`
` >=(1/24)sum_j alpha_j k_j`
` =K_ii/24`
` >1/48`.

The numerical consequence `E_3(i)>1/(48*256)=1/12288` follows. QED.

### Scope note

This theorem transfers **regularized ridge leverage** into **actual unregularized third-minor mass**. It does not rotate the random variables, does not condition on spectral coordinates, and does not infer one good minor. The mass remains aggregated over physical-coordinate minors.

## 4. Theorem B — deterministic source-realizable singleton-plus-five-bank packet

### Statement: `QFORM-O0-HEAVY-SIXBLOCK-PACKET-v1`

Assume the O0 situation of Theorem A with physical row sets `L,R`, `i in L`, and `E_3(i)>1/12288`. Then there is a partition

`L\{i}=L_1 disjoint_union L_2`,

`R=R_1 disjoint_union R_2 disjoint_union R_3`

such that

`sum_{j in L_1, k in L_2}`
`sum_{a in R_1,b in R_2,c in R_3}`
`det B[{i,j,k},{a,b,c}]^2 > 1/110592`.

Empty summands are interpreted as zero, so the strict positive conclusion automatically makes every needed block nonempty. The six physical blocks `{i},L_1,L_2,R_1,R_2,R_3` preserve independence of the underlying original-coordinate source.

### Proof

Color each row in `L\{i}` independently and uniformly with one of two labels. For any unordered pair `{j,k}`, the probability that its two rows receive different labels is `1/2`.

Independently color each column in `R` uniformly with one of three labels. For any unordered triple `{a,b,c}`, the probability that its members receive all three distinct labels is

`3!/3^3=2/9`.

Thus each squared minor counted by `E_3(i)` survives into the displayed labeled packet with probability

`(1/2)(2/9)=1/9`.

The expected retained mass is `E_3(i)/9>1/110592`, so some deterministic coloring attains at least that expectation, and the strict input inequality yields the strict displayed bound. QED.

### Exact next analytic interface

The former endpoint “O0 ridge heavy row” can therefore be replaced by the source-valid statement:

> `QFORM-O0-HEAVY-FIVEBANK-PAYMENT-v1`: uniformly bound the quadratic-output density, or route to an already-paid branch, whenever a physical singleton plus five disjoint original-coordinate banks carry the above aggregate squared `3x3` cross-minor mass `>1/110592`, with arbitrary symmetric self blocks and arbitrary affine translations induced by conditioning.

This formulation keeps determinant mass before selection and preserves source provenance. It is compatible with the known counterexamples to one-good-minor, post-rotation independence, and conditional spectral-density caps.

## 5. Theorem C — exact use of the designated fleet03/B20 high-window theorem

### Statement: `QFORM-HIGHWINDOW-ENERGY-CURRENCY-v1`

Let `A` satisfy the target spectral hypothesis. Put

`P=1_{|A|>=1/64}=UU^T`, `H={i:P_ii>1/64}`.

If the fleet03/B20 paid condition `||U_H^TU_H||_op<=1/2` fails, so that

`||U_H^TU_H||_op>1/2`,

then at least one of the following holds:

1. `sum_{i in H} A_ii^2 >= 1/24576`; or
2. there is a physical bipartition `J,J^c` with
   `||A[J,J^c]||_F^2 > 1/49152`.

### Proof

Functional calculus gives the positive-semidefinite operator inequality

`A^2 >= P/4096`,

because on the spectral range of `P` every eigenvalue of `A^2` is at least `1/64^2=1/4096`.

Let `D_H` denote the diagonal coordinate projection onto `H`. Then

`sum_{i in H,j} A_ij^2 = tr(D_H A^2)`
` >= tr(D_H P)/4096`
` = tr(U_H^TU_H)/4096`
` >= ||U_H^TU_H||_op/4096`
` > 1/8192`.

Write this directed heavy-row energy as `D+O`, where

`D=sum_{i in H}A_ii^2`,
`O=sum_{i in H,j != i}A_ij^2`.

If `D>=1/24576`, alternative 1 holds. Otherwise

`O>1/8192-1/24576=1/12288`.

Let

`W=sum_{i<j: {i,j} intersects H} A_ij^2`

be the corresponding unordered off-diagonal energy. Every `H-H` edge is counted twice in `O` and every `H-H^c` edge once, so `W>=O/2>1/24576`.

Now color every physical coordinate independently with two fair colors and take `J` to be one color class. Each unordered off-diagonal edge crosses the cut with probability `1/2`; hence

`E ||A[J,J^c]||_F^2 >= W/2 >1/49152`.

Some deterministic cut attains this bound. QED.

### Connection to partner's exact expression

The designated partner's theorem already closes the complementary case with `||p_Q||_infinity<194` and continuity. Theorem C therefore applies to **every matrix not paid by that theorem** and converts its exact spectral-window failure into original-coordinate diagonal/cross-cut currency without rotating the input law.

## 6. What moved and what remains

### Before

The B20 endpoint after the previous run was `QFORM-HIGHWINDOW-BANK-ENTANGLEMENT-v1`: partner high-window localization produced physical bank/cross-cut currency, but O0 ridge-heavy configurations were still described only as “one large ridge leverage row,” with no quantitative transfer to the actual third-compound mass.

### After

Theorem A proves a uniform transfer:

`K_ii>1/2  =>  E_3(i)/E_3>1/48`.

In the universal O0 certificate this becomes `E_3(i)>1/12288`, and Theorem B converts it into the explicit source-realizable six-block packet `>1/110592`. This is target-level mechanism movement: the O0 ridge-heavy wall is no longer an abstract regularized-leverage state.

Theorem C independently sharpens the newest fleet03/B20 high-window wall into a universal physical energy dichotomy. These two reductions can coexist in the same unresolved matrix.

### First unpaid universal implication

`QFORM-O0-HEAVY-FIVEBANK-PAYMENT-v1`, under the full target hypotheses and arbitrary self blocks/affine shifts: pay the singleton-plus-five-bank determinant packet above by a dependence-safe quadratic density estimate, or show it necessarily transfers a fixed amount into an already-paid O1/O2/O3, grouped-square/rank-two, or ridge/separator packet.

The difficult point is analytic, not combinatorial: the singleton and bank variables that generate the useful cross determinant also appear in contaminating square/cross terms. They cannot be replaced by independent convolution noise or by conditionally capped spectral coordinates.

### Next method

Expand the six-block determinant packet relative to the singleton row and seek an **aggregate** two-compound Schur currency, never a single minor. The exact identity `det M[{i,j,k}] = M_ii det(Sc_i M[{j,k}])` suggests the correct algebraic object, but any analytic use must keep the right-bank variables in their original product coordinates. The planned dichotomy is: either the singleton linear aggregate itself admits a product-preserving hyperbolic payment, or enough two-compound mass survives in two disjoint left banks and two right banks to invoke a dependence-safe rank-two ridge/grouped-coordinate theorem.

This is a changed mechanism from the prior B20 high-window-only attempt, so no three-run stagnation trigger applies.

## 7. Status discipline

- `ESSENTIAL_STEP_APPLIED`: yes.
- `TARGET_LEVEL_REDUCTION_PROVED`: yes, Sections 3–5.
- `CANDIDATE_REFUTED`: no new target-level candidate was refuted in this run.
- `FULL_PROOF_CANDIDATE`: no.
- Full QFORM remains open.
- Continuity is inherited only on already-paid branches where the cited theorem proves it; Theorems A–C are structural reductions and make no standalone continuity claim.
