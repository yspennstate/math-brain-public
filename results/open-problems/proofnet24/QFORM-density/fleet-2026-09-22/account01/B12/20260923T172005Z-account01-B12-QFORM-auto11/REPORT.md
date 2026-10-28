SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T17:20:05Z.
attacking: destructive-Gram-defect stability — absorb arbitrary full-rank signed spectral additions whenever they do not destroy physical cross Gram energy, and spend reserve only against the low-rank/tail part of the destructive defect.

# account01/B12 — destructive Gram-defect compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: additional eigenvalue control.  
Status: **PROVED SUPPORTING STABILITY THEOREM / COMPLETED account02-B12 PARTNER APPLIED TO AN ACTUAL INEQUALITY / D5 RECEIVER APPLIED / EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 0. First unpaid implication and why this is not a full solution

The exact target remains open. Starting only from `s_3(A)>=1`, we still do not know how to force a product-preserving original-coordinate cross cut with five usable singular directions, nor a bounded physical principal core with a dimension-free three-mode certificate. In particular an exact rank-three matrix can satisfy the global hypothesis while every cross block has rank at most three, so no argument can extract a D5 certificate in complete generality. The diagonal/rank-three regimes must be routed to other already-paid exits.

This run therefore attacks the assigned additional-eigenvalue question only: once a physical cross certificate has reserve, how much can arbitrary larger/smaller signed spectral additions destroy it? The new mechanism is not an operator-norm bound on the added matrix. It charges only the **destructive part of the actual physical Gram change**, which can have rank zero even when the added matrix has full rank and arbitrarily large norm.

No step rotates the random input law, no spectral coordinate is declared independent, and no term `X^T R X` is treated as an independent convolution or a small random error.

## 1. Source actually used from the designated partner

Completed partner result used below:

- account02/B12 r33,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T115313Z-account02-B12-qform-r33/REPORT.md`,
- theorem `QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1`.

It states for same-size rectangular matrices

`M_final=M_base+L+R+T`, `rank L<=ell`, `||T||op<=delta`,

and `q+ell<=d=min(rows,cols)`, that

` s_q(M_final) >= max_{0<=p<=d-ell-q} [ s_{q+ell+p}(M_base)-s_{p+1}(R) ] - delta. `        (1.1)

The same report records the completed D5 receiver: for an ACTUAL original-coordinate cross block `M=A[I,J]`,

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`,

so `s_5(M)>=gamma>0` implies

`||p_Q||_infinity <= 5 sqrt(2e)/gamma`.                             (1.2)

The D5 branch supplies an integrable characteristic function and hence a continuous density. Same-bank blocks, outside couplings and affine terms remain unrestricted.

## 2. New object: destructive right-Gram defect

Let `M0,D` be real `m x n` matrices and put

`G0=M0^T M0`,
`G=(M0+D)^T(M0+D)`.

Define the PSD **destructive right-Gram defect**

`N_R(M0,D) := [G0-G]_+`
` = [- (M0^T D + D^T M0 + D^T D)]_+`.                            (2.1)

Here `[H]_+` denotes the positive part of a symmetric matrix. Write its eigenvalues decreasingly as

`nu_1>=nu_2>=...>=0`.

The exact identity behind the theorem is

`G-G0=M0^T D+D^T M0+D^T D`.                                      (2.2)

The key point is the `D^T D` term. A very large signed cross addition can have a strongly negative linear anticommutator and nevertheless have zero destructive Gram defect because the quadratic term repairs the loss. Thus (2.1) is strictly different from paying `||D||op`, `rank D`, or only the negative part of the linear anticommutator.

There is a left analogue

`N_L(M0,D):=[M0 M0^T-(M0+D)(M0+D)^T]_+`.                          (2.3)

Either side may be used; below the right form is enough.

## 3. Main deterministic theorem

### Theorem 3.1 (`QFORM-DESTRUCTIVE-GRAM-DEFECT-STABILITY-v1`)

Let `d=min(m,n)`. For every `k>=1` and every reserve integer `rho>=0` with `k+rho<=d`,

`boxed: s_k(M0+D)^2 >= ( s_{k+rho}(M0)^2 - nu_{rho+1} )_+ .`       (3.1)

Consequently

`boxed: s_k(M0+D) >= max_{0<=rho<=d-k} sqrt((s_{k+rho}(M0)^2-nu_{rho+1})_+).`  (3.2)

If a further arbitrary matrix `W` satisfies `||W||op<=eta`, then

`boxed: s_k(M0+D+W) >= [ max_rho sqrt((s_{k+rho}(M0)^2-nu_{rho+1})_+) - eta ]_+ .`  (3.3)

No bound at all on `||D||op` is assumed.

### Proof

Let `N=N_R(M0,D)`. Since for every Hermitian `K`, `K>=-[ -K ]_+`, identity (2.2) gives

`G >= G0-N`.                                                       (3.4)

Let `N_rho` retain the largest `rho` eigenmodes of `N`. Then

`rank N_rho<=rho`,
`||N-N_rho||op=nu_{rho+1}`.                                      (3.5)

By rank-`rho` Hermitian interlacing,

`lambda_k(G0-N_rho) >= lambda_{k+rho}(G0)`.                       (3.6)

Restoring the residual PSD matrix `N-N_rho` and using Weyl gives

`lambda_k(G0-N) >= lambda_{k+rho}(G0)-nu_{rho+1}`.                (3.7)

By (3.4), eigenvalue monotonicity in Loewner order gives

`lambda_k(G)>=lambda_k(G0-N)`.                                   (3.8)

The left side is `s_k(M0+D)^2`; `lambda_{k+rho}(G0)=s_{k+rho}(M0)^2` in the stated index range. Since `G` is PSD we may clip the lower bound at zero, proving (3.1). Maximize over `rho` for (3.2). Finally singular-value Weyl gives

`s_k(M0+D+W)>=s_k(M0+D)-||W||op`,

which proves (3.3). QED.

### Sharp reserve interpretation

If `rank N_R<=rho`, then `nu_{rho+1}=0` and

`boxed: s_k(M0+D)>=s_{k+rho}(M0).`                                (3.9)

Thus a full-rank, arbitrarily large `D` can consume only `rho` baseline reserve directions if its **destructive Gram defect**, rather than `D` itself, has rank `rho`.

The reserve loss cannot be removed from information of this type. For `M0=2I_d`, let `D=-2P` where `P` is an orthogonal projection of rank `rho`. Then `M0+D=2(I-P)` loses exactly `rho` singular directions and

`N_R=4P` has rank exactly `rho`.

## 4. Nonlinear zero-cost class — much larger than small perturbations

A particularly useful case is

`(M0+D)^T(M0+D) >= M0^T M0`.                                    (4.1)

Then `N_R=0`, so every singular value is nondecreasing:

`boxed: s_k(M0+D)>=s_k(M0) for all k.`                            (4.2)

This class allows `D` to be full rank and arbitrarily large, with no sign restriction.

For example, when `M0=2I_d` and `J^T=-J`, `J^T J=I_d` (possible for even `d`), put

`D=tJ`, `t in R` arbitrary.                                       (4.3)

Then

`(2I+tJ)^T(2I+tJ)=(4+t^2)I`,                                    (4.4)

so `N_R=0` and in fact

`s_k(2I+tJ)=sqrt(4+t^2)` for every `k`.                           (4.5)

This packet is not in the earlier polar-positive cone for `M0=2I`: for `t!=0`, `tJ` is skew-symmetric rather than PSD. Thus (4.3) is a genuinely different large-eigenvalue mechanism.

More generally, in a right polar decomposition `M0=US`, decompose

`D=UY+Z`, `U^T Z=0`.

Then the exact structural identity

`(M0+D)^T(M0+D)=(S+Y)^T(S+Y)+Z^T Z`                              (4.6)

shows that an arbitrarily large left-orthogonal component `Z` can only help the right Gram matrix. Only the part of `(S+Y)^T(S+Y)-S^2` that survives as a negative Gram defect is ever charged by Theorem 3.1.

## 5. Literal high/low spectral split of a symmetric matrix addition

Let the full symmetric matrix be

`A=A0+E+T`, `E=sum_a theta_a v_a v_a^T`,                          (5.1)

with no sign restrictions. Fix a threshold `h>=0` and split

`E=E_{>h}+E_{<=h}`,
`E_{>h}=sum_{|theta_a|>h} theta_a v_a v_a^T`.                     (5.2)

Then

`||E_{<=h}||op<=h`.                                               (5.3)

For disjoint ORIGINAL-coordinate banks `I,J`, write

`M0=A0[I,J]`, `D_h=E_{>h}[I,J]`,
`N_h=[M0^T M0-(M0+D_h)^T(M0+D_h)]_+`,                            (5.4)

and let `nu_j(h)` be the eigenvalues of `N_h`. If `||T||op<=delta`, then compression gives

`||(E_{<=h}+T)[I,J]||op<=h+delta`.                               (5.5)

Therefore Theorem 3.1 yields the dependence-safe spectral-addition compiler

`boxed:`
`s_k(A[I,J]) >=`
` [ max_{0<=rho<=d-k} sqrt((s_{k+rho}(M0)^2-nu_{rho+1}(h))_+) - h-delta ]_+.`   (5.6)

Interpretation:

- all modes with `|theta_a|>h` may have arbitrary signs, multiplicities and magnitudes;
- they are charged only through the **negative Gram-defect spectrum** `nu_j(h)` of their physical cross action;
- if that defect has rank at most `rho`, their magnitudes disappear completely after spending `rho` reserve directions;
- all remaining spectral modes, however numerous and of either sign/orientation, cost only the single threshold `h`;
- the dense remainder `T` is paid only in a deterministic final-matrix singular-value inequality, never as a random-error/convolution statement.

## 6. Compilation with the completed account02/B12 partner theorem

The preceding theorem can be combined with a second arbitrary-magnitude packet and an unresolved residual tail.

Write the actual final cross block as

`M=M0+D+L+R+T_c`,                                                 (6.1)

where `D` is treated by the new destructive-Gram mechanism, `rank L<=ell`, `R` is arbitrary, and `||T_c||op<=delta`.

Define for each admissible `j`

`g_j := max_{0<=rho<=d-j} sqrt((s_{j+rho}(M0)^2-nu_{rho+1})_+)`.   (6.2)

Theorem 3.1 gives `s_j(M0+D)>=g_j`. Applying the completed account02/B12 adaptive reserve envelope (1.1) to the **actual baseline `M0+D`** gives

`boxed:`
`s_q(M) >= max_{0<=p<=d-ell-q} [ g_{q+ell+p}-s_{p+1}(R) ]-delta.`   (6.3)

This is the required direct use of a completed partner result on an actual inequality.

For `q=5`, if the right side is `Gamma_5>0`, the completed D5 theorem gives

`boxed: ||p_{X^T A X}||_infinity <= 5 sqrt(2e)/Gamma_5`,           (6.4)

and the density is continuous in this branch.

## 7. Exact target-class family with a full-rank unbounded signed packet

Take two ORIGINAL-coordinate banks `I,J`, each of size `d=20`, and three spectator coordinates. Let

`A_base = [[0,2I_20],[2I_20,0]] direct_sum 2I_3`.                 (7.1)

Let `J0` be block diagonal with ten copies of

`[[0,-1],[1,0]]`,

so `J0^T=-J0`, `J0^T J0=I_20`.

### Full-rank arbitrary packet

For arbitrary `t in R`, add the symmetric dilation

`S_t=[[0,tJ0],[tJ0^T,0]] direct_sum 0_3`.                         (7.2)

Its eigenvalues are

`+|t|` (multiplicity 20), `-|t|` (multiplicity 20), and three zeros.  (7.3)

Thus this is a forty-mode signed spectral packet with completely unbounded magnitude. Its physical cross block is `D=tJ0`, and (4.4) gives

`N_R(2I_20,tJ0)=0`,
`s_j(2I_20+tJ0)=sqrt(4+t^2)>=2`.                                 (7.4)

### Additional hostile large modes and dense small tail

Add any symmetric dilation of a rank-one cross matrix `L`; its two nonzero eigenvalues are `+s_1(L),-s_1(L)` and can be arbitrarily large.

Add any symmetric dilation of a cross matrix `R` satisfying only

`s_6(R)<=1/5`.                                                    (7.5)

Its top five singular modes, hence ten signed eigenvalues of the symmetric dilation, may be arbitrarily large. Finally add any full symmetric matrix `T` on all 43 coordinates with

`||T||op<=1/10`.                                                  (7.6)

The actual cross block is

`M=2I_20+tJ0+L+R+T[I,J]`.                                        (7.7)

Use the completed account02/B12 theorem with

`q=5`, `ell=1`, `p=5`, `delta=1/10`.

Since `q+ell+p=11`, (7.4)-(7.5) give the actual inequality

`s_5(M) >= s_11(2I+tJ0)-s_6(R)-1/10`
`       >= 2-1/5-1/10`
`       =17/10`.                                                   (7.8)

Hence the completed D5 receiver yields, uniformly in every `t`, every rank-one `L` of arbitrary amplitude, every `R` satisfying (7.5), every admissible full dense `T`, and every independent cap-one product law,

`boxed: ||p_Q||_infinity <= 50 sqrt(2e)/17`
`                              = 6.85777641646213... .`             (7.9)

The D5 proof also gives a continuous density.

### Exact owner target check

Before adding `T`, the three spectator coordinates form a direct `2I_3` block and none of `S_t,L,R` touches them. Therefore the pre-`T` matrix has at least three singular values at least `2`. Singular-value Weyl under (7.6) gives

`s_3(A)>=2-1/10=19/10>1`.                                        (7.10)

Thus every matrix in this family literally satisfies the owner's global three-large-eigenvalue hypothesis. The family simultaneously contains:

- a full-rank forty-mode arbitrary signed packet whose magnitude is entirely free;
- an additional arbitrary-magnitude rank-one cross packet;
- five further arbitrary-magnitude hostile cross singular modes;
- an arbitrary full dense symmetric tail;
- and a universal continuous-density bound (7.9).

## 8. What this changes and what remains missing

The new deterministic parameter is not `||E||op` and not the rank of the large spectral addition. It is the spectrum of

`[M0^T M0-(M0+D)^T(M0+D)]_+`,                                    (8.1)

the part of the physical cross Gram matrix that is actually destroyed. This can vanish for a full-rank, arbitrarily large signed packet. It can also be low rank even when the addition itself has high rank, allowing reserve directions to absorb only the genuinely destructive component.

What remains unpaid is the global-to-physical extraction from the bare assumption `s_3(A)>=1`: prove that some original-coordinate branch has a suitable D5 reserve / low destructive Gram defect, or force one of the already completed diagonal, local-core, ridge, grouped-bank/hub, pair, half-Riesz, scalar-Schur or other physical exits. The exact rank-three obstruction shows why this compiler alone cannot close that step.

Full-target status: **OPEN**.  
Continuity: **PROVED only in the D5 scope above; unrestricted continuity remains OPEN**.  
Native brain status: `WITHOUT_VERIFIED_BRAIN`.
