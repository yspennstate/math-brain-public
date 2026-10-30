SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T12:37:28Z.
attacking: recolor the genuinely transverse one-child/two-cross diffuse hybrid into a robust third physical cross singular direction, while retaining the full same-bank/cross remainder and then apply the completed robust-s3 ambient receiver.

# fleet01/B08 r29 — diffuse recoloring creates a third cross direction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING STRUCTURAL/ANALYTIC ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture and its global continuity conclusion remain open. Every random variable below is an original independent coordinate with density bounded by one. No rotation of random variables, moment hypothesis, support regularity, arbitrary-joint coarea bound, law-uniform pointwise van-der-Corput estimate, or deletion of a small random quadratic perturbation is used.

## 1. Source-pinned inputs actually used


The current programme state still records the unrestricted target as OPEN and records the law-uniform pointwise oscillatory-decay shortcut as refuted.

The designated partner result actually applied is fleet02/B08 r26,

`yspennstate/math-open-problems@ac7e9c4772e977672044e7cacd55b74c91ea8b6d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T104126Z-fleet02-B08-qform-diffuse-r26/REPORT.md`.

Its actual `k=1` hybrid gate supplies

`c=(1/2)sqrt(3/5)`,
`beta=(3/16)sqrt(3/5)`,

so one physical child has a genuine eigenvalue of magnitude at least `c L` and the actual full cross block has `s_2(B)>=beta L`. Its D5 router also proves that if `s_5(B)>=L/64`, then the full ambient form already has a continuous density with

`||p_Q||_infinity<306/L`.

The ambient receiver used after recoloring is fleet01/B08 r24,

`yspennstate/math-open-problems@a11ebd02f863b82324e449b4a31d468ec654f080`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260923T063906Z-fleet01-B08-qform-r24/REPORT.md`.

It proves: if an ORIGINAL-coordinate cross block `M` satisfies `s_3(M)>=sigma`, then either the full ambient form has a continuous `C_0` density with

`||p_Q||_infinity <= 6 sqrt(e)/sigma`,

or the same physical cross block has both a row star and a column star of Euclidean norm `>sigma/sqrt(6)`.

## 2. Balanced coloring of a three-dimensional physical frame

### Lemma 2.1 — `QFORM-3FRAME-BALANCED-COLORING-v1`

Let `F` be an `m x 3` matrix with `F^T F=I_3` and

`max_i ||F_{i,*}||_2^2 <= 1/64`.

Then there is a partition of its original coordinate rows into `S disjoint_union T` such that

`(3/8)I_3 <= F_S^T F_S <= (5/8)I_3`,

and hence also

`(3/8)I_3 <= F_T^T F_T <= (5/8)I_3`.

#### Proof

Choose independent Bernoulli `xi_i` with mean `1/2`, let `f_i` denote the i-th row of F, and set

`X_i=(xi_i-1/2) f_i f_i^T`.

Then `E X_i=0`,

`||X_i|| <= (1/2)(1/64)=1/128`,

and, since `(f_i f_i^T)^2=||f_i||^2 f_i f_i^T`, the matrix variance obeys

`||sum_i E X_i^2||
 <= (1/4)(1/64)||sum_i f_i f_i^T||
 =1/256`.

The self-adjoint matrix Bernstein inequality in dimension three therefore gives, at `t=1/8`,

`P(||sum_i X_i||>=1/8)
 <=6 exp[-(1/64)/(2/256+(2/3)(1/128)(1/8))]
 =6 exp(-24/13)
 <1`.

Thus some realization obeys `||F_S^T F_S-(1/2)I||<1/8`, which is exactly the claim. QED.

This step is deterministic-existential in the final theorem; the random coloring is only a proof device and does not alter the input law.

## 3. Recoloring a one-child/two-cross hybrid

Consider disjoint original-coordinate banks `I,J`. Write

`C=A[I,I]`, `B=A[I,J]`.

Let `lambda,u` be a normalized eigenpair of the symmetric child block C with

`|lambda|=s_1(C)`,

and put

`r=s_2(C)`, `R=C-lambda u u^T`, so `||R||=r`.

Let

`B_2=V Sigma W^T`

be the rank-two truncated SVD of B, where `V` has two orthonormal columns and the second retained singular value is at least `beta_0>0`. Put

`epsilon=s_3(B)`.

Let

`d=dist(u,Ran V)`.

When `d>0`, set

`w=(u-VV^T u)/d`, `F=[V,w]`.

Then F has three orthonormal columns.

### Theorem 3.1 — `QFORM-K1-DIFFUSE-RECOLOR-THIRD-CROSS-v1`

Assume

`max_i ||F_{i,*}||^2 <=1/64`.

Then there is an original-coordinate partition `I=S disjoint_union T` for which the recolored physical cross block

`M=A[S,T union J]=[ C[S,T] , B[S,J] ]`

satisfies

`boxed:
 s_3(M)
 >= (3d/(8 sqrt(2))) min(beta_0,|lambda|)
    - sqrt(r^2+epsilon^2).
`

In particular this is an estimate on the actual matrix A: no complementary spectral component is removed from the final cross block.

#### Proof

Apply Lemma 2.1 to F and put `alpha=3/8`. Thus

`alpha I_3 <= F_S^T F_S, F_T^T F_T <= (1-alpha)I_3`.

Write

`u=Va+d w`, `||a||^2+d^2=1`.

Three consequences of the Gram lower bounds are immediate.

First,

`s_min(V_S)>=sqrt(alpha)`.

Hence the rank-two cross piece obeys

`B_2[S,J] B_2[S,J]^T
 >= beta_0^2 V_S V_S^T
 >= alpha beta_0^2 P_L`,

where `L=Ran(V_S)` and `P_L` is its orthogonal projection.

Second,

`||u_T||^2=[a;d]^T F_T^T F_T [a;d]>=alpha`.

Third, for every two-vector b,

`||w_S-V_S b||^2
 =[-b;1]^T F_S^T F_S[-b;1]
 >=alpha(1+||b||^2)>=alpha`.

Therefore

`dist(u_S,L)>=d sqrt(alpha)`.

Now define the ideal recolored block

`M_0=[ lambda u_S u_T^T , B_2[S,J] ]`.

The two column banks T and J are disjoint, hence exactly

`M_0 M_0^T
 =lambda^2 ||u_T||^2 u_Su_S^T
  +B_2[S,J]B_2[S,J]^T`.

We use the following elementary rank-three fact. If L is two-dimensional, `a,b>0`, and z has distance rho from L, then on `span(L,z)`

`lambda_min(aP_L+bzz^T) >= (rho^2/2) min(a,b)`.

Indeed, one direction in L orthogonal to `P_L z` has eigenvalue a. In the remaining two-dimensional plane, the determinant is `ab rho^2`, while the trace is at most `a+b` when `||z||<=1`; hence the lower eigenvalue is at least `ab rho^2/(a+b)>=(rho^2/2)min(a,b)`.

Apply this with

`a=alpha beta_0^2`,
`b=alpha lambda^2`,
`z=u_S`,
`rho>=d sqrt(alpha)`.

It follows that

`s_3(M_0)^2
 >= (d^2 alpha^2/2) min(beta_0^2,lambda^2)`,

or

`s_3(M_0)>= (d alpha/sqrt(2)) min(beta_0,|lambda|)`.

Finally

`M-M_0=[ R[S,T], (B-B_2)[S,J] ]`.

For a horizontal concatenation,

`||M-M_0||
 <=sqrt(||R[S,T]||^2+||(B-B_2)[S,J]||^2)
 <=sqrt(r^2+epsilon^2)`.

Weyl's singular-value inequality proves the displayed bound. QED.

## 4. Concrete application to the actual partner k=1 gate

Apply fleet02/B08 r26 to an actual target form with spectral scale L. Before any recoloring, its D5 theorem already gives the first alternative

`boxed: ||p_Q||_infinity<306/L`

with a continuous density whenever `s_5(B)>=L/64`.

Hence every unpaid k=1 state may be restricted, without deleting anything, to

`s_5(B)<L/64`.

Now use its actual gate values

`|lambda|>=cL`, `c=(1/2)sqrt(3/5)=0.387298334620742...`,

`s_2(B)>=beta L`, `beta=(3/16)sqrt(3/5)=0.145236875482778...`.

Suppose in addition that

`d=dist(u,Ran V)>=1/2`,

`max_i ||[V,w]_{i,*}||^2<=1/64`,

and define

`eta=(1/2)(3/8)beta/4
    =0.00680797853825523...`.

If both

`s_2(C)<=eta L`,
`s_3(B)<=eta L`,

then Theorem 3.1 gives

`s_3(M)
 >= (1/2)(3/8)beta L/sqrt(2)-sqrt(2)eta L
 =0.00962793558114550... L`.

Apply the completed r24 robust-third-cross receiver to this literal recolored physical cross block. Therefore either

`boxed:
 ||p_Q||_infinity
 <=6sqrt(e)/(0.00962793558114550 L)
 <1027.461/L,
`

and `p_Q` has a continuous `C_0` representative, or M has both a physical row and physical column star of norm

`boxed:
 >0.00962793558114550 L/sqrt(6)
 =0.00393058824169885... L.
`

Thus, after the partner's high-cross-rank payment, every still-unpaid genuinely diffuse/transverse k=1 state must fall into at least one of the following structural exits:

1. `s_2(C)>0.00680797854 L` — a second fixed-scale child direction has appeared;
2. `s_3(B)>0.00680797854 L` — a third fixed-scale original cross direction has appeared;
3. `dist(u,Ran V)<1/2` — the child direction is strongly aligned with the top-two cross left space;
4. `max_i ||[V,w]_{i,*}||^2>1/64` — a localized original coordinate is present;
5. the recolored block has bilateral physical stars `>0.00393058824 L`;
6. or the full density has already been paid by one of the two continuous Fourier branches (`<306/L` or `<1027.461/L`).

The new point is that the genuinely transverse, genuinely diffuse one-child/two-cross configuration is no longer an undifferentiated survivor: it automatically manufactures a third cross singular direction after a balanced recoloring of original coordinates.

## 5. What remains unpaid

The first remaining implication is

`QFORM-K1-ALIGNMENT-OR-SECONDCHILD-STAR-COMPILER-v1`:

pay the alignment survivor `dist(u,Ran V)<1/2`, the second-child exit `s_2(C)>0.0068L`, or the bilateral-star exit while retaining arbitrary same-bank curvature and the full complementary spectrum. The localized-frame exit should be handed to the existing coordinate-pivot/localized machinery rather than treated as diffuse.

The theorem above is only a supporting router. It does not prove the unrestricted target, and it does not claim continuity on the structural survivor branches.

## 6. Correction audit

The proof does not use any of the following refuted interfaces: law-uniform pointwise quadratic-phase decay; arbitrary-joint rank-three coarea; positive moments of conditional spectral-projection density; independence after spectral rotation; a uniformly good fixed-size physical principal block; deletion of a small matrix tail as a small random quadratic error. Small `r` and `epsilon` enter only a deterministic Weyl comparison of literal physical matrices before the full-ambient receiver is invoked.
