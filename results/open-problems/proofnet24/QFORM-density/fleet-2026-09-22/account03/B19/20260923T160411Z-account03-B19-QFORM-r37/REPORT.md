SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T16:04:11Z.
attacking: QFORM-ALIGNED-SKELETON-OR-SELFPAIR-PAYMENT-v1 — convert the overlapping self-bank packet plus the existing rank-two J-K bicore into a quantitative three-bank triangle, then force either a paid third-volume cross block, a physical third-volume anchor, or a finite 2x2x2 grouped survivor.

# account03/B19 r37 — balanced self-cut compiler for the overlapping STAR packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Outcome: **NEW STRUCTURAL COMPILER + PAID D3 SUBBRANCH / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the new D3-paid branch; not proved for the remaining aligned/heavy-anchor branches or for the full target.

## 1. Controls, corrections, and source pins

Fresh owner control at the prepublication refresh was `yspennstate/math-research-brain@f08ac7f091ff74a8d50036f4e2d484defb08930c`, OWNER CONTROL revision `2026-09-22.15`; QFORM remained the sole research target and account03/B19 was not paused. The live correction inbox was reread before this report. No post-rotation independence, arbitrary-joint coarea bound, pointwise scalar quadratic-phase decay, fixed-good-minor principle, Monte Carlo extremality claim, or deletion of a matrix tail is used below.

The immediate B19 predecessor is

`yspennstate/math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T145843Z-account03-B19-QFORM-r36/REPORT.md`.

Its aligned STAR4 branch has an original-coordinate partition `{h} disjoint_union J disjoint_union K`, a physical leaf cross block `N=A[J,K]`, top two singular product

`rho=s1(N)s2(N) >= rho_* := 63(1-tau)^2/16384`,                    (1.1)

with `tau=2^-20`, hence

`rho_*=0.003845207509588222...`,                                  (1.2)

and either an already isolated rank-at-most-five carrier or an actual same-bank self block `B` (on one of the leaf banks) satisfying

`F_B:=sum_(i!=j) B_ij^2 > 0.4537176735697731005`.                  (1.3)

The preceding run only extracted one arbitrary cut with cross energy `>0.113429418`; it did not coordinate that cut with the rank-two singular plane of `N`.

The newest account01/B19 result actually incorporated is

`yspennstate/math-open-problems@eeb16f2a52472725a8e30261c873bb2f30add26e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T151334Z-account01-B19-QFORM-auto11/REPORT.md`.

It proves `QFORM-LOWRANK5-PAVING-OR-3VOLUME-ANCHOR-v1` and, when applied to the r36 carrier, leaves only a paid continuous branch, a `>1/320` physical leverage, a literal same-bank cross packet, or a physical third-volume anchor. The literal packet alternative there has one actual cut with cross Frobenius square at least

`E_packet=6.102770589677675e-5`.                                  (1.4)

The newest designated partner is account04/B19 r4,

`yspennstate/math-open-problems@ac55b70485c4108c7073a75365127e00be3bc097`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260923T151700Z-account04-B19-QFORM-r4/REPORT.md`.

Its `QFORM-MOVING-RIDGE-JOINT-CAP-BARRIER-v1` is applied quantitatively in Section 6. The older completed account04/B19 null-coloop theorem remains source-pinned at

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

and is also used at an actual inequality in Section 6.

Finally, the D3 cross-volume theorem used below is the completed owner-pinned physical cross-block theorem: for an ORIGINAL-coordinate cross block `M`, put

`Z_3=e_3(M M^T)`.

If its natural row three-volume inclusion marginals are all at most `1/2`, then the full ambient quadratic form has a continuous `C_0` density with

`||p_Q||_infinity <= 6 sqrt(e) Z_3^(-1/6)`.                       (1.5)

All same-bank phases, affine terms, and outside couplings are retained. If the marginal gate fails, an actual physical row carries more than half of the total three-volume mass. I use this theorem only with its gate intact.

## 2. First new theorem: a balanced self cut that preserves BOTH rank-two bicore legs

The main defect of the r36 packet cut is that it was selected only for `B`; it could in principle destroy one of the two singular channels of `N`. The next theorem removes that ambiguity whenever the top-two left singular plane is not itself physically heavy.

### Theorem 2.1 — `QFORM-BICORE-BALANCED-SELF-CUT-v1`

Let `N` be any real `m x k` matrix with

`rho=s_1(N)s_2(N)>0`,                                               (2.1)

and let `U` be an `m x 2` orthonormal frame for its top-two **left** singular plane. Write

`ell_i=||U(i,:)||_2^2`, `mu=max_i ell_i`.                           (2.2)

Let `B=B^T` be any symmetric matrix on the same `m` physical coordinates and put

`F_B=sum_(i!=j) B_ij^2`.                                           (2.3)

If

`mu <= 1/320`,                                                     (2.4)

then there is a literal original-coordinate bipartition

`{1,...,m}=D_1 disjoint_union D_2`                                (2.5)

such that simultaneously

`boxed: ||B[D_1,D_2]||_F^2 >= F_B/8,`                              (2.6)

and, for `r=1,2`,

`boxed: s_1(N[D_r,:]) s_2(N[D_r,:]) >= 3 rho/8.}`                  (2.7)

No rank assumption is made on the tail of `N`.

#### Proof

Choose a fair independent Rademacher cut and let `D_1={i:epsilon_i=+1}`, `D_2=D_1^c`. Put

`G=U[D_1,:]^T U[D_1,:]`,
`H=G-(1/2)I_2=(1/2)sum_i epsilon_i U(i,:)^T U(i,:)`.               (2.8)

By independence of the signs,

`E ||H||_F^2
 =(1/4) sum_i ||U(i,:)^T U(i,:)||_F^2
 =(1/4) sum_i ell_i^2
 <=(mu/4) sum_i ell_i
 =mu/2
 <=1/640`,                                                        (2.9)

because `sum_i ell_i=2`. Hence Markov gives

`P(||H||_F>1/8) <= (1/640)/(1/64)=1/10`.                          (2.10)

For the self-bank cross energy define

`Z=||B[D_1,D_2]||_F^2`.                                          (2.11)

Every ordered off-diagonal pair `(i,j)` enters with probability `1/4`, so

`E Z=F_B/4`.                                                      (2.12)

Because `B` is symmetric, a cut contains at most one orientation of each unordered edge, so

`0<=Z<=F_B/2`.                                                    (2.13)

If `p=P(Z>=F_B/8)`, then

`F_B/4=E Z <= (1-p)F_B/8+pF_B/2`,                                (2.14)

which forces `p>=1/3`. Therefore the event

`Z>=F_B/8` and `||H||_F<=1/8`                                    (2.15)

has probability at least `1/3-1/10=7/30>0`; fix such a cut.

The two eigenvalues of `G` then lie in `[3/8,5/8]`. Let

`N_2=U diag(s_1(N),s_2(N)) V^T`                                  (2.16)

be the top-two SVD truncation. For the first side,

`N_2[D_1,:]^T N_2[D_1,:]`

has its two nonzero squared singular values equal to the eigenvalues of

`diag(s_1,s_2) G diag(s_1,s_2)`,                                 (2.17)

so their product gives the exact identity

`s_1(N_2[D_1,:])s_2(N_2[D_1,:])
 =rho sqrt(det G)
 >=3rho/8.`                                                       (2.18)

For `D_2`, replace `G` by `I_2-G`, whose eigenvalues are also in `[3/8,5/8]`.

Finally, the SVD tail has right singular space orthogonal to that of `N_2`. Thus, after an algebraic orthogonal change of basis in the column space,

`N[D_r,:]N[D_r,:]^T
 =N_2[D_r,:]N_2[D_r,:]^T + T_r T_r^T`                            (2.19)

with `T_r T_r^T>=0`. Weyl monotonicity for positive semidefinite matrices shows that the top two singular values of the **actual** restricted block cannot be smaller than those of `N_2[D_r,:]`. This proves (2.7). The orthogonal column change in this last sentence is only a deterministic singular-value computation; no rotated random variables are introduced. QED.

### Quantitative application to the r36 strong self-bank packet

If the winning r36 self bank obeys the diffuse top-two leverage gate `mu<=1/320`, Theorem 2.1 gives a physical three-bank partition `D_1,D_2,K` with

`boxed: ||B[D_1,D_2]||_F^2 > 0.05671470919622164,}`              (2.20)

and

`boxed:
 s_1(N[D_r,K])s_2(N[D_r,K])
 >0.0014419528160955833,
 r=1,2.
}`                                                               (2.21)

If (2.4) fails, the unpaid geometry is not diffuse: one literal physical coordinate carries more than `1/320` of the top-two left singular plane. Thus the former broad "overlapping self packet" is already reduced to either a **heavy physical spectral leverage** or a quantitatively robust three-bank triangle.

### Application to the newer account01/B19 packet alternative

If account01/B19 produces one cut with cross energy `E_packet` as in (1.4), then the total ordered off-diagonal energy of that bank satisfies

`F_B >= 2 E_packet`.                                              (2.22)

Under the same diffuse leverage gate, Theorem 2.1 therefore produces a (possibly different) balanced cut with

`||B[D_1,D_2]||_F^2
 >= F_B/8
 >= E_packet/4
 >1.5256926474194188e-5`,                                       (2.23)

while retaining the same bicore lower bound (2.21). Hence the newest peer packet can also be compiled into the same three-bank geometry rather than left as an unstructured self-bank Frobenius certificate.

## 3. Second new theorem: a robust triangle is either D3-visible or genuinely 2x2x2 aligned

The balanced triangle still overlaps: `D_2` couples to both `D_1` and `K`. The next algebraic step says that this overlap is already paid by the D3 theorem unless the self packet itself lies almost entirely between the two rank-two bicore planes.

### Lemma 3.1 — exterior-volume injection

Let `A` be any real matrix with top two singular values `a_1,a_2>0`, let `P` be the projector onto its top-two left singular plane, and let `C` be any matrix with the same row space dimension. Then

`boxed:
 e_3([A,C][A,C]^T)
 >= (a_1a_2)^2 ||(I-P)C||_F^2.
}`                                                               (3.1)

#### Proof

Apply an orthogonal change of basis in the column space of `A` to put its first two singular columns in the form `a_1u_1,a_2u_2`. The quantity `e_3([A,C][A,C]^T)` is invariant under this column rotation. Among its Cauchy--Binet sum of squared `3x3` minors, retain only those using exactly these first two singular columns and one column `c` of `C`. Their total for this `c` is

`(a_1a_2)^2 ||u_1 wedge u_2 wedge c||^2
 =(a_1a_2)^2 ||(I-P)c||^2`.                                     (3.2)

Summing over the columns of `C` proves (3.1); every omitted squared minor is nonnegative. QED.

### Theorem 3.2 — `QFORM-BALANCED-TRIANGLE-D3-OR-2x2x2-v1`

Take three disjoint ORIGINAL-coordinate banks `D_1,D_2,K`. Put

`C=A[D_1,D_2]`,
`N_1=A[D_1,K]`,
`N_2=A[D_2,K]`.                                                   (3.3)

Assume

`||C||_F^2 >= F>0`,                                               (3.4)

and

`s_1(N_r)s_2(N_r) >= Delta>0`, `r=1,2`.                          (3.5)

Let `P_r` be the projector onto the top-two left singular plane of `N_r`. Fix `theta in (0,1/4)`. Then at least one of the following holds:

1. **Left D3 packet:** the physical cross block
   `M_1=[C,N_1]` from rows `D_1` to columns `D_2 union K` satisfies

   `e_3(M_1M_1^T) >= Delta^2 theta F`;                            (3.6)

2. **Right D3 packet:** the physical cross block
   `M_2=[C^T,N_2]` from rows `D_2` to columns `D_1 union K` satisfies

   `e_3(M_2M_2^T) >= Delta^2 theta F`;                            (3.7)

3. **Finite-plane alignment:**

   `||(I-P_1)C||_F^2 < theta F`,
   `||C(I-P_2)||_F^2 < theta F`,                                 (3.8)

   and therefore

   `boxed:
   ||P_1 C P_2||_F
   >= (1-2sqrt(theta)) ||C||_F.
   }`                                                            (3.9)

In particular, at `theta=1/64`, the aligned `2x2` component retains at least `9/16` of the self-cross Frobenius **energy**.

#### Proof

If the first inequality in (3.8) fails, Lemma 3.1 applied to `(A,C)=(N_1,C)` gives (3.6). If the second fails, apply the same lemma to `(N_2,C^T)` to get (3.7). If neither fails, then

`C-P_1CP_2=(I-P_1)C+P_1C(I-P_2)`,                                (3.10)

so

`||C-P_1CP_2||_F
 <=||(I-P_1)C||_F+||C(I-P_2)||_F
 <2sqrt(theta F)
 <=2sqrt(theta)||C||_F`.                                         (3.11)

The reverse triangle inequality gives (3.9). QED.

This theorem is purely in physical matrices. It neither rotates the input law nor drops the parts of the cross blocks outside their top singular planes.

## 4. Actual D3 payment and numerical constants

Apply Theorem 3.2 to the strong r36 triangle (2.20)-(2.21) with

`theta=1/64`,
`Delta=(3/8)rho_*`,
`F=0.4537176735697731005/8`.                                     (4.1)

On either D3 alternative,

`Z_3
 >=Delta^2 theta F
 >1.8425438602123219e-9`.                                       (4.2)

If the natural D3 row-marginal gate is diffuse (`<=1/2` for every row), the completed physical cross-volume theorem (1.5) yields the **full ambient target law**

`boxed: ||p_Q||_infinity < 282.529,}`                             (4.3)

with a continuous `C_0` density. No conditioning deletes the other triangle leg or either same-bank self block.

If the D3 marginal gate is not diffuse, then an actual physical row carries more than half the volume, hence more than

`boxed: 9.2127193010616e-10}`                                    (4.4)

of squared physical third-volume mass. This is a genuine row anchor, not a selected tiny reciprocal minor.

If neither D3 alternative occurs, (3.9) says that the self packet has a `2x2` grouped component between the two top bicore planes with energy at least

`(9/16)F > 0.031901...`.                                         (4.5)

Thus the previously uncontrolled overlapping branch has collapsed to a finite `2+2+2` grouped triangle, plus the already explicit heavy-leverage/row-anchor alternatives.

For the weaker account01/B19 packet (2.23), the same calculation gives

`Z_3>4.9566605558140e-13`,                                       (4.6)

and hence, on the diffuse D3 gate,

`boxed: ||p_Q||_infinity <1111.989}`                              (4.7)

continuously. The constants are intentionally nonoptimized; the gain is structural and dimension-free.

## 5. Compact conditional end-to-end proof graph after r37

The current correction-safe assembly is now:

1. The completed physical pivot, ruled, definite-pair, exact-null, D5, spectral-window, and diffuse-tail exits pay their stated gates.
2. In strict `N3(2^-20)`, the existing STAR compiler reaches the quantitative rank-two survivor with `rho>=rho_*`.
3. The completed selected-volume and aligned-carrier results pay their diffuse branches and isolate the aligned STAR geometry.
4. r36 forces the genuine third spectral resource either into a rank-at-most-five grouped carrier or into a same-bank self packet with the quantitative energy (1.3).
5. The newest account01/B19 low-rank paving theorem pays one carrier branch continuously and otherwise leaves heavy leverage, a self packet, or a physical third-volume anchor.
6. **New r37:** any self-packet branch with diffuse top-two bicore leverage can be recut so that the packet retains a fixed fraction of its energy **and both rank-two J-K channels survive quantitatively**. This creates an actual original-coordinate three-bank triangle.
7. **New r37:** that triangle is already paid continuously by D3 unless a row three-volume anchor appears or the packet is quantitatively confined to a finite `2x2x2` grouped triangle.

Accordingly the first essential unpaid implication is now

`QFORM-2x2x2-PRODUCT-TRIANGLE-OR-HEAVY-ANCHOR-PAYMENT-v1`:

> pay the finite grouped `2+2+2` triangle while retaining that each grouped pair comes from a linear image of its own original independent coordinate bank, or route the explicit `>1/320` top-plane leverage / physical third-volume row anchor to an existing ridge, grouped-square, or double-anchor receiver. The grouped variables may NOT be replaced by an arbitrary bounded joint density.

This is strictly narrower than the r36 debt: the overlap no longer ranges over an arbitrary-dimensional self bank.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open.

## 6. Designated partner account04/B19 applied at actual inequalities

### 6.1 Latest partner barrier used quantitatively

The newest partner theorem constructs, for every `0<epsilon<1`, a scalar `X` independent of a triple `(Y,Z,W)` having joint density cap one such that

`T=4XY+Z^2-YW`

has

`||p_T||_infinity >=1/(9epsilon)`,                                (6.1)

while the fixed coefficient matrix already has spectrum

`{1,0,+sqrt(17)/2,-sqrt(17)/2}`.                                 (6.2)

Apply this directly to the successor proposed after Theorem 3.2. If one tried to prove the finite `2x2x2` grouped survivor by replacing one product-origin three-variable grouped bank with **only** a cap-one joint density and claimed some universal constant `C_joint>1/18`, choose

`epsilon=1/(18 C_joint)`.                                        (6.3)

Then the partner inequality gives

`boxed: ||p_T||_infinity >=2 C_joint > C_joint,}`                 (6.4)

contradiction. Thus the last aligned triangle must retain the linear-image-of-product provenance supplied by the actual `D_1,D_2,K` banks. This is an equation-level application of the newest partner result, not a general warning.

### 6.2 Completed positive partner branch retained at its exact scope

The earlier account04/B19 null-coloop theorem gives, in its residual-diffuse exact-rank-three null-coloop normal form,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`,                         (6.5)

for `0<D_res<=1`. Therefore on the already-used proof-graph interval

`e^-8 <=D_res<=1`,                                                (6.6)

we retain the concrete paid inequality

`boxed: ||p_Q||_infinity <102.}`                                  (6.7)

I do not transfer (6.5) to the punctured near-coloop or grouped-triangle regimes.

## 7. Verification and scope ledger

The run checker independently verifies:

- the exact restricted rank-two determinant identity `rho sqrt(det G)` on random noncommuting frames;
- monotonicity when arbitrary orthogonal SVD-tail columns are restored;
- the exterior-volume inequality (3.1) on random matrices;
- every numerical threshold in Sections 2 and 4.

It terminates

`QFORM_B19_R37_BALANCED_TRIANGLE_CHECK_PASS`.

No Gaussianity, log-concavity, moment bound, compact support, connected support, iid assumption, diagonal-basis assumption, or post-rotation independence is used. Repeated eigenvalues are harmless. The D3 theorem is invoked only with its marginal gate; a failed gate is recorded as an anchor rather than silently paid. Monte Carlo is not used as proof. Essential boundedness is proved only on the displayed D3/null-coloop branches; continuity is claimed only where the cited Fourier/D3 theorem supplies an `L^1` characteristic function.

The full conjecture remains open.
