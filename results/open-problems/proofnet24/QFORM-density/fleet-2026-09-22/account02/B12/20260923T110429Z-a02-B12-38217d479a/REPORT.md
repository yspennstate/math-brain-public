SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T11:04:29Z.
attacking: numerical-rank cross-footprint stability for arbitrarily many signed eigenvalue replacements, with a full-rank dense tail paid only at matrix level.

# account02/B12 — cross numerical-rank absorption under dense tails

Programme: QFORM-DENSITY-3EIG-20260922  
Status: **PROVED SUPPORTING THEOREM / EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

The new result below is a stability theorem, not the missing structural extraction. The remaining full-target implication is:

> starting only from `s_3(A)>=1`, force either (i) an ORIGINAL-coordinate cross cut whose five-direction reserve survives after spending a bounded numerical rank of hostile extra spectrum, (ii) a bounded physical protected compression of the kind supplied by the designated account03/B12 partner, or (iii) an already-paid volume/hub/ridge/grouped-bank/pair/triple/Schur branch.

Diffuse exact-rank-three examples and the live correction set prohibit simply postulating a uniformly conditioned small principal block or a universal rank-three cross cut. The theorem here says that **once a cross reserve exists, arbitrarily many individually unbounded eigenvalue replacements can be free if their physical cross footprint has low numerical rank**.

## 1. Sources and corrections actually used

Required newest-Claude source, fixed source commit:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- `FOURIER_ROUTE_REPORT.md`
- `COUNTEREXAMPLE_SEARCH.md`.

The equation-level result used below is the proved `D_5` theorem: for an ACTUAL original-coordinate cross block `M=A[I,J]`, with `Z_5=e_5(M^T M)`,

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`

with **no row-marginal condition**. Its scope allows arbitrary same-bank quadratic blocks, outside couplings and affine terms. In particular it is valid for the final matrix itself; no rotated random coordinates are introduced.

Designated partner actually consumed:

- account03/B12 r31,
- `yspennstate/math-open-problems@f6d5af0d6f222415ccd5c7d5391fd0de8be32013`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T104429Z-qform-eigenvalue-r31/REPORT.md`.

Its proved compression-footprint theorem says that an actual `m`-coordinate physical block carrying a protected Hermitian compression with three threshold eigenvalues `>=mu` in absolute value, perturbed by protected compression norm `eps<mu`, has three actual block eigenvalues of modulus at least `mu-eps`; the dependence-safe finite physical receiver then gives

`||p_Q||_infinity <= 2 sqrt(6 pi m)/(mu-eps)`.

Two live corrections are especially relevant. `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1` shows that `||T||op ->0` does not imply any law-uniform smallness of `X^T T X`, even in total variation or density sup norm, for unbounded cap-one sources. `QFORM-ARBITRARY-JOINT-INDEFINITE-PLANAR-L2-FALSE-v1` shows that an arbitrary dependent planar density cannot replace the original product provenance in an indefinite Fourier step. The argument below therefore uses the dense tail only in deterministic matrix inequalities and invokes D5 only on ORIGINAL coordinate banks.

## 2. Numerical-rank singular-value lemma

For a matrix `M`, write its singular values in decreasing order `s_1(M)>=s_2(M)>=...` and define

`d_r(M) := inf_{rank L<=r} ||M-L||op = s_{r+1}(M)`

by Eckart--Young (with `d_0(M)=||M||op`).

### Lemma 2.1

For arbitrary rectangular matrices `M0,L,E` of compatible size, if `rank L<=r`, then for every `j>=1`,

`boxed: s_j(M0+L+E) >= s_{j+r}(M0) - ||E||op.`

### Proof

The standard rank perturbation inequality is

`s_{j+r}(M0) <= s_j(M0+L) + s_{r+1}(-L)`.

Since `rank L<=r`, `s_{r+1}(L)=0`, so

`s_j(M0+L) >= s_{j+r}(M0)`.

Weyl's singular-value Lipschitz inequality then gives

`s_j(M0+L+E) >= s_j(M0+L)-||E||op`,

which proves the claim. No randomness appears. QED.

## 3. Main theorem: arbitrary-spectrum numerical-rank cross stability

Let `I,J` be disjoint sets of ORIGINAL coordinates. Write

`A = A0 + S + T`,

where

- `A0=A0^T` is a baseline matrix;
- `S=S^T` is completely arbitrary: any rank, any signs, any operator norm;
- `T=T^T` is an arbitrary full-rank dense tail with `||T||op<=delta`.

Set

`M0=A0[I,J]`,

and for an integer `r>=0` define the numerical-rank tail of the added spectrum on this physical cut by

`eta_r := d_r(S[I,J]) = s_{r+1}(S[I,J])`,

`rho := eta_r + delta`.

For `j=1,...,5`, put

`a_j := (s_{r+j}(M0)-rho)_+`.

### Theorem 3.1 (`QFORM-CROSS-NUMERICAL-RANK-ABSORPTION-v1`)

If `a_5>0`, then the full ambient quadratic form with arbitrary independent cap-one inputs has a continuous density and

`boxed: ||p_(X^T A X)||infinity <= 5 sqrt(2e) (a_1 a_2 a_3 a_4 a_5)^(-1/5).`

In particular, if

`s_{r+5}(M0) >= kappa > eta_r+delta`,

then

`boxed: ||p_(X^T A X)||infinity <= 5 sqrt(2e)/(kappa-eta_r-delta).`

No bound on `||S||op` appears. Thus an arbitrarily large, arbitrarily signed, arbitrarily high-rank spectral modification is permitted provided only that its ORIGINAL-coordinate cross footprint is close in operator norm to rank `r`.

### Proof

Choose a best rank-`r` approximation `L` to `S[I,J]`, so

`S[I,J]=L+R`, `rank L<=r`, `||R||op=eta_r`.

Because a coordinate compression cannot increase operator norm,

`||T[I,J]||op<=delta`.

The actual final cross block is therefore

`M=A[I,J]=M0+L+(R+T[I,J])`,

with

`||R+T[I,J]||op<=eta_r+delta=rho`.

Lemma 2.1 gives for `j=1,...,5`

`s_j(M)>=s_{r+j}(M0)-rho>=a_j`.

For `Z_5=e_5(M^T M)`, the elementary-symmetric expansion in squared singular values contains the product of the five largest squared singular values, hence

`Z_5 >= product_(j=1)^5 s_j(M)^2 >= product_(j=1)^5 a_j^2`.

Applying the pinned completed D5 theorem to this **actual final original-coordinate block** gives

`||p_Q||infinity <= 5 sqrt(2e) Z_5^(-1/10)`

`<= 5 sqrt(2e) (product a_j)^(-1/5)`.

If `s_{r+5}(M0)>=kappa`, then each `s_{r+j}(M0)>=kappa` for `j<=5`, so each `a_j>=kappa-rho`, yielding the displayed simplified bound. The D5 Fourier proof is an `L^1` characteristic-function bound, so this branch has a continuous density. QED.

## 4. Spectral-update corollary: large coefficients can cost exactly zero

Suppose now that the added matrix is literally a signed spectral update

`S = sum_a tau_a v_a v_a^T`,

where the `v_a` are orthonormal eigenvectors of `A0`. Then the corresponding baseline eigenvalues `lambda_a` are literally replaced by `lambda_a+tau_a`.

For any subset `G` of update directions, if

`dim span{(v_a)_I : a in G} <= r`,

then

`L := sum_(a in G) tau_a (v_a)_I (v_a)_J^T`

has rank at most `r`, regardless of the number, signs or magnitudes of the coefficients in `G`. Writing the remaining index set as `B`,

`R := sum_(a in B) tau_a (v_a)_I (v_a)_J^T`,

we get the source-valid bound

`eta_r <= ||R||op <= sum_(a in B) |tau_a| ||(v_a)_I||2 ||(v_a)_J||2.`

Therefore every coefficient in `G` is **magnitude-free**: it can cross zero or tend to either infinity without entering the density constant. Only the residual physical cross footprint outside the rank-`r` span is charged.

This is stronger than an exact global rank budget. `S` itself may have arbitrarily high rank; only its compression from the `J` bank to the `I` bank needs low numerical rank.

## 5. Exact target-class family with arbitrarily many independent eigenvalue replacements

The following construction shows that the theorem is not merely a restatement of a finite-rank perturbation result.

Fix `N=6` and any integer `k>=0`. Let `I` and `J` be two six-coordinate banks with standard bases `e_1,...,e_6` and `f_1,...,f_6`, and let `h_1,...,h_k` be spectator coordinates. Define

`A0 = [[0,2 I_6],[2 I_6,0]] direct_sum 2 I_k`.

For `ell=1,...,6`, put

`g_ell=(e_ell+f_ell)/sqrt(2)`, `q_ell=(e_ell-f_ell)/sqrt(2)`.

Then `g_ell` and every `h_a` are `+2` eigenvectors, while every `q_ell` is a `-2` eigenvector.

Let

`W=span{g_1,h_1,...,h_k}`

and choose **any** orthonormal basis `z_0,...,z_k` of `W`. Write

`c_a=<z_a,g_1>`.

Because the only `I` and `J` component of `W` is `g_1`,

`(z_a)_I = c_a e_1/sqrt(2)`,

`(z_a)_J = c_a f_1/sqrt(2)`.

For completely arbitrary real numbers `tau_0,...,tau_k`, define

`S_tau=sum_(a=0)^k tau_a z_a z_a^T`.

Since `A0` is exactly `2I` on `W`, the vectors `z_a` remain eigenvectors and their eigenvalues are **independently and literally replaced** by

`2 -> 2+tau_a`.

The number of independently arbitrary replacements is `k+1`, with no bound as `k` grows. Nevertheless their entire `I x J` cross footprint is

`S_tau[I,J] = (1/2 sum_a tau_a c_a^2) e_1 f_1^T`,

which has rank at most one for every choice of all coefficients, even if every `|tau_a|` is enormous.

Now add **any** symmetric dense tail `T` on all `12+k` coordinates satisfying

`||T||op<=delta<1`.

The baseline cross block is `M0=2I_6`. Taking `r=1`, `eta_1=0`, Lemma 2.1 gives

`s_5(A[I,J]) >= s_6(2I_6)-delta = 2-delta`.

Therefore D5 yields the dimension-free bound

`boxed: ||p_(X^T(A0+S_tau+T)X)||infinity <= 5 sqrt(2e)/(2-delta),`

uniformly in `k`, the choice of orthonormal basis of `W`, every signed replacement coefficient `tau_a`, the arbitrary dense tail `T`, and every independent cap-one product law.

At `delta=1/4`,

`boxed: ||p_Q||infinity <= (20/7) sqrt(2e) = 6.661839947420355... .`

This entire family lies in the **exact owner target class**. Before `T`, the six vectors `q_1,...,q_6` still have eigenvalue `-2`, independently of every `tau_a`. Hence the sixth smallest eigenvalue is at most `-2`. Hermitian Weyl gives after the tail

`lambda_6^uparrow(A0+S_tau+T) <= -2+delta < -1`,

so the final matrix has at least six eigenvalues of modulus exceeding one. The arbitrary replacements never spend the eigenvalues certifying the target hypothesis.

This family is genuinely different from a global rank-one update: `rank S_tau` can equal `k+1` and tend to infinity. What remains rank one is only the physical cross footprint seen by D5.

## 6. Same family: actual use of the completed account03/B12 compression theorem

The designated partner supplies a second, logically independent certificate on the same final family. Take the four ORIGINAL coordinates

`H={e_2,f_2,e_3,f_3}`.

On this block,

`B0=A0[H,H] = [[0,2],[2,0]] direct_sum [[0,2],[2,0]],`

so all four eigenvalues have modulus `2`. Every update vector `z_a` is supported only on `g_1` plus spectators, hence

`S_tau[H,H]=0` exactly.

The dense tail satisfies

`||T[H,H]||op<=delta`.

Apply the partner compression theorem with `E=R^H`, `m=4`, `mu=2`, protected footprint `eps=delta`. It gives a final physical-core threshold

`N_abs((A0+S_tau+T)[H,H]; 2-delta) >= 3`

and therefore the real density inequality

`boxed: ||p_Q||infinity <= 2 sqrt(24 pi)/(2-delta).`

At `delta=1/4` this is

`9.923674348227669...`.

The D5 branch is sharper (`6.66184...`) for this family, but the partner certificate proves that the same arbitrary many-eigenvalue update can also be absorbed by a protected finite physical compression. This yields a valid dual-certificate router: use whichever of the numerical-rank cross reserve or protected-compression reserve is quantitatively stronger on the actual matrix.

No convolution with a dependent remainder occurs in either branch.

## 7. Dense tails are not random-small perturbations

The only use of `||T||op<=delta` above is

1. `||T[I,J]||op<=delta` in singular-value Weyl;
2. `||T[H,H]||op<=delta` in Hermitian Weyl/compression stability.

There is deliberately no step of the form `X^T T X is O(delta)`. Such a statement is false without support or moment assumptions. For example already `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]` give

`X^T T X >= delta R^2`

almost surely. The newer live matrix-perturbation correction is stronger: even a sequence of matrices converging in operator norm can produce output laws at total-variation distance one when the cap-one source is allowed to move to infinity. Hence matrix stability must be certified on the actual final matrix, as done here.

## 8. Scope and remaining gap

`QFORM-CROSS-NUMERICAL-RANK-ABSORPTION-v1` is a dimension-free stability theorem for the D5 route. It allows:

- arbitrary additional eigenvalues, smaller or larger, either sign;
- arbitrarily many such replacements;
- arbitrarily large update operator norm and global rank;
- arbitrary self blocks and outside couplings created by those updates;
- a completely nonseparable full-rank dense tail of small operator norm;
- arbitrary independent input laws with densities at most one.

What it does **not** prove is that a bare target matrix with only `s_3(A)>=1` can always be decomposed relative to some original-coordinate cut into a baseline with `s_{r+5}` reserve plus a low-numerical-rank hostile cross footprint. That is the first unpaid structural extraction stated at the top. Nor does it turn a small matrix norm into output-law continuity. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
