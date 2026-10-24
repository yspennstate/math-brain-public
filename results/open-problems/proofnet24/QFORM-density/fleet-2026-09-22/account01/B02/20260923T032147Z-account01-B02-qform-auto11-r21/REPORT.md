SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T03:21:47Z.
attacking: integrated Fourier estimate — exact pivoted compound identities in the two-sided third-volume star collar, then a D5-to-low-rank reduction and partner stability compiler.

# account01/B02 r21 — anchored compound normal form and D5-to-low-rank Fourier closure

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains open. This run does **not** prove a universal target-wide `L^1_t` characteristic-function bound and does not give a valid counterexample to that stronger criterion. It proves a new exact structural identity for the currently live two-sided heavy third-volume collar, converts weak fifth volume into quantitative low-rank coefficient structure, and then applies the completed account02/B02 volume-stability theorem to obtain a genuine unweighted `L^1_t` estimate on the resulting diffuse-core branch.

Continuity is proved on the final stability branch because that partner theorem is proved through an `L^1` characteristic-function envelope. Outside that branch, only structural information is asserted here.

## 1. Sources actually consumed

Fresh control was resolved from `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`; QFORM remains the sole research target. The live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, the fleet protocol and this worker's assignment were read before the mathematics below.

The designated partner result actually used is account02/B02, canonical report

`yspennstate/math-open-problems@f7a221e0f40362a1ccad48cf81812f2143f3cc92`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T020523Z-account02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`.

Two pieces from it are used at equation level:

1. If the natural squared third-minor law of a physical cross block has a row `i` and column `j` with inclusion marginals at least `3/4`, then the joint anchored third-minor mass satisfies

`J_3(i,j) >= Z_3/2`,

where `Z_3=e_3(M^T M)`.

2. `QFORM-VOLUME-STABILITY-OPTIMAL-Q-v1`: if a physical cross block decomposes as `M=M0+E`, with `rho=s_3(M0)>0`, row-range leverage `max_l (P_range(M0))_ll<=1/2`, and `||E||op<=rho/16`, then the full quadratic form has a continuous density and

`||p_Q||infinity <= C_vs/rho`,

`C_vs=3600 e/(1035-227 sqrt(3))=15.246870586...`.

The proof is through an integrable characteristic-function envelope, hence also

`integral_R |phi_Q(t)| dt <= 2 pi C_vs/rho <95.799/rho`.

For the unconditional fifth-volume exit I also retain account02/B02 r16,

`yspennstate/math-open-problems@49c80441f24d6c697350119fac09426077b7e313`,

which gives

`||p_Q||infinity <= (5e/sqrt(2)) Z_5^(-1/10)`

and a continuous density, again from an `L^1_t` Fourier bound.

No post-rotation independence, no scalar pointwise quadratic decay, no small-tail deletion, and no fixed-good-minor extraction is used below.

## 2. Setup: the live double-heavy third-volume collar

Let `M=A[I,J]` be an ORIGINAL-coordinate physical cross block after conditioning on all coordinates outside `I union J`. Write

`Z_k=e_k(M^T M)=sum_{|S|=|T|=k} det(M[S,T])^2`.

Assume `Z_3>0`, and let `alpha_i,beta_j` be the row/column inclusion marginals under the natural squared `3x3`-minor law. In the two-sided D' failure collar there exist a row and column, relabelled first, satisfying

`alpha_0>=3/4`, `beta_0>=3/4`.

Write the physical block as

`M = [[a, r^T], [c, N]]`.

Define the anchored compound mass

`J_{k+1}:=sum_{|P|=|T|=k} det M[{0} union P,{0} union T]^2`.

The partner union-bound step gives

`J_3/Z_3=P(0 in S,0 in T)>=alpha_0+beta_0-1>=1/2`,

so

`boxed(J_3>=Z_3/2).`                                                (2.1)

The first missing implication was to understand this anchored mass without splitting it by triangle inequality. The next theorem gives an exact normal form at **every compound order**.

## 3. Exact anchored compound normal form

### Theorem 3.1 — `QFORM-ANCHORED-COMPOUND-NORMAL-FORM-v1`

For every integer `k>=1` for which the minors exist:

### (A) Nonzero central edge

If `a!=0`, set

`S=N-c r^T/a`.

Then

`boxed(J_{k+1}=a^2 e_k(S^T S).)`                                  (3.1)

### (B) Zero central edge

If `a=0`, then `J_3>0` forces `c!=0` and `r!=0`. Let

`P_c=I-c c^T/||c||^2`, `P_r=I-r r^T/||r||^2`,
`K=P_c N P_r`.

Then

`boxed(J_{k+1}=||c||^2 ||r||^2 e_{k-1}(K^T K).)`                    (3.2)

Here `e_0=1`.

#### Proof of (3.1)

For each residual row set `P` and column set `T`, both of size `k`, the block determinant identity gives

`det [[a,r_T^T],[c_P,N_PT]]
 = a det(N_PT-c_P r_T^T/a)
 = a det(S_PT).`

Squaring and summing over `P,T`, Cauchy--Binet yields (3.1).

Equivalently, deterministic block Gaussian elimination gives

`[[1,0],[-c/a,I]] M [[1,-r^T/a],[0,I]] = diag(a,S)`,

so in particular

`rank(M)=1+rank(S)`.                                                (3.3)

This is only a coefficient identity. It does **not** rotate or shear random inputs in the probabilistic argument.

#### Proof of (3.2)

Orthogonally rotate the residual row and column coefficient spaces **only to prove the deterministic identity**, so that

`c=||c|| e_1`, `r=||r|| e_1`.

For `a=0`, an anchored `(k+1)x(k+1)` determinant is

`-r_T^T adj(N_PT)c_P`.

It vanishes unless the selected residual row and column sets contain their respective first axes. When they do, expansion along those axes gives, up to sign,

`||c|| ||r||` times a `(k-1)x(k-1)` minor of the doubly projected block `K=P_cNP_r`.

Therefore the sum of squared anchored minors is

`||c||^2||r||^2` times the sum of squared `(k-1)x(k-1)` minors of `K`, namely `e_{k-1}(K^TK)`. This proves (3.2).

No independence statement is made in the rotated coefficient coordinates.

### Immediate strengthening of the partner star compiler

At order three, (2.1) and Theorem 3.1 give the **exact** alternatives

if `a!=0`:

`boxed(a^2 e_2(S^T S)>=Z_3/2),`                                    (3.4)

while if `a=0`:

`boxed(||c||^2||r||^2 ||K||_F^2>=Z_3/2).`                          (3.5)

This is stronger than the previous triangle-split conclusion `a^2e_2(N)>=Z_3/8` OR `||c||^2||r||^2||P_cNP_r||_F^2>=Z_3/8`: the anchored resource is now represented exactly and no cancellation between the two terms is paid by a factor four.

The price is explicit: in the `a!=0` case the exact residual is a Schur coefficient `S`, not itself an original-coordinate product block. It is used below only to construct a **physical coefficient decomposition** of `M`; no independence of Schur coordinates is assumed.

## 4. A compound-gap inequality

### Lemma 4.1 — `QFORM-COMPOUND-GAP-RANK-COLLAPSE-v1`

Let `x_1>=x_2>=...>=0`. For every `m>=1` with at least `m+2` entries,

`boxed(e_{m+2}(x)/e_m(x) >= x_{m+1}x_{m+2}/C(m+2,2).)`             (4.1)

#### Proof

The exact Euler/combinatorial identity is

`C(m+2,2)e_{m+2}(x)
 = sum_{|R|=m} x_R e_2(x_{R^c}).`

After deleting any `m` coordinates, the two largest surviving coordinates have product at least `x_{m+1}x_{m+2}`. Hence every summand satisfies

`e_2(x_{R^c})>=x_{m+1}x_{m+2}`.

Summing gives (4.1).

Two cases used below are

`e_3/e_1 >= x_2x_3/3`,                                             (4.2)

`e_4/e_2 >= x_3x_4/6`.                                             (4.3)

## 5. Weak fifth volume forces a quantitative low-rank normal form

Because every anchored fifth minor is among all fifth minors,

`J_5<=Z_5`.                                                         (5.1)

Combine this with `J_3>=Z_3/2`.

### Theorem 5.1 — `QFORM-JOINT-STAR-D5-LOWRANK-v1`

In the double-heavy collar above:

### (A) `a!=0`

Let `s_j(S)` be the singular values of the Schur coefficient `S`. Then

`e_4(S^TS)/e_2(S^TS)=J_5/J_3<=2Z_5/Z_3`.

Using (4.3),

`boxed(s_4(S) <= (12 Z_5/Z_3)^(1/4).)`                              (5.2)

Thus `S` is operator-close to rank at most three, with an exact scale controlled by the fifth-to-third compound ratio.

### (B) `a=0`

Let `s_j(K)` be the singular values of `K=P_cNP_r`. Then

`e_3(K^TK)/e_1(K^TK)=J_5/J_3<=2Z_5/Z_3`.

Using (4.2),

`boxed(s_3(K) <= (6 Z_5/Z_3)^(1/4).)`                               (5.3)

Thus the doubly transverse physical coefficient packet is operator-close to rank at most two.

These are exact coefficient statements. They do not say a small tail may be discarded probabilistically. The next section spends the small tail only through a completed stability theorem that explicitly retains it.

## 6. Convert the low-rank normal form into a genuine L1 Fourier branch

This is the required application of the completed **account02/B02** result to an actual inequality.

### Nonzero-edge core

Let `S_3` be a best rank-three approximation to `S`, and set

`E_S=S-S_3`,

`M_0=[[a,r^T],[c,c r^T/a+S_3]]`,

`E=[[0,0],[0,E_S]]`.

Then

`M=M_0+E`,

`||E||op=s_4(S)<=epsilon_+:=(12Z_5/Z_3)^(1/4)`.                    (6.1)

Let

`rho=s_3(M_0)`,
`ell=max_l (P_range(M_0))_ll`.

If

`ell<=1/2`,
`rho>=16 epsilon_+`,                                                (6.2)

then the account02/B02 volume-stability theorem applies exactly to this **physical** decomposition `M=M0+E`. Therefore

`boxed(||p_Q||infinity <= C_vs/rho <15.247/rho),`                   (6.3)

and

`boxed(integral |phi_Q(t)|dt <=2pi C_vs/rho <95.799/rho).`          (6.4)

The density is continuous and vanishes at infinity.

### Zero-edge core

Let `K_2` be a best rank-two approximation to `K=P_cNP_r`, and put

`E_K=K-K_2`.

Because `K` already has left/right projections `P_c,P_r`, embed `E_K` back into the residual physical block and define

`M_0=M-[[0,0],[0,E_K]]`,
`E=[[0,0],[0,E_K]]`.

Then

`M=M_0+E`,

`||E||op=s_3(K)<=epsilon_0:=(6Z_5/Z_3)^(1/4)`.                     (6.5)

Again set

`rho=s_3(M_0)`, `ell=max_l(P_range(M_0))_ll`.

If

`ell<=1/2`,
`rho>=16 epsilon_0`,                                                (6.6)

the same partner theorem gives exactly (6.3)--(6.4), with a continuous density.

### Interpretation

Therefore the previous vague `rank>=4, D'-failed, D5-weak joint-star collar` has a narrower exact form. Once both third-volume marginals are heavy, one of the following happens:

1. fifth volume itself is large enough to be paid directly by D5;
2. fifth volume is weak and the anchored coefficient geometry collapses quantitatively to a rank-three Schur residual (`a!=0`) or rank-two doubly transverse packet (`a=0`);
3. the resulting low-rank core is diffuse and retains a third singular value at least sixteen times the tail, in which case account02/B02 stability gives the genuine unweighted `L^1_t` estimate (6.4);
4. the **only unpaid part of this interface** is therefore a high-leverage core (`ell>1/2`) or a core whose third singular value is itself at the fifth-volume tail scale.

This is an aggregate-before-inversion reduction. No individual tiny `2x2` or `3x3` minor is selected.

## 7. Scale-parametrized D5/low-rank dichotomy

For any `tau>0`, if

`Z_5 >= tau^4 Z_3`,                                                  (7.1)

then D5 supplies the direct continuous-density Fourier exit

`||p_Q||infinity <= (5e/sqrt(2)) tau^(-2/5) Z_3^(-1/10)`.          (7.2)

If instead

`Z_5 < tau^4 Z_3`,                                                   (7.3)

then Theorem 5.1 gives

`a!=0: s_4(S)<12^(1/4) tau`,

`a=0:  s_3(K)<6^(1/4) tau`.                                        (7.4)

Thus the fifth-volume compiler and the low-rank normal form are complementary at every chosen scale. In branches where a previous aggregate argument supplies a dimension-free lower bound on `Z_3`, (7.2) is itself dimension-free; in the complementary branch, (7.4) forces a concrete low-rank coefficient structure for the next physical-core/hub compiler.

## 8. Relation to the exact target and corrections

This run does not prove that the bare hypothesis `s_3(A)>=1` always yields a cross block satisfying the final diffuse-core conditions (6.2) or (6.6). The first unpaid implication is now:

`QFORM-JOINT-STAR-HIGH-LEVERAGE-OR-THIRD-SINGULAR-CLOSURE-v1`.

Starting from the exact low-rank normal forms above, route either

- `max diag P_range(M0)>1/2`, or
- `s_3(M0)<16||M-M0||op`

into an existing original-coordinate pair/triple, hub, ridge, grouped-square, mixed-bilinear or scalar-Schur mechanism, without deleting the tail and without assuming independence after any coefficient rotation.

The stronger full statement

`integral_R |E exp(it X^T A X)| dt <= C`

remains `OPEN_NOT_REFUTED`. I found no target-valid counterexample in this run.

## 9. Finite algebra checks

Seeded random-matrix checks were run only as regressions, not as proofs. For random rectangular blocks, the maximum relative discrepancy in (3.1) across compound orders 1--4 was below `1.7e-15`; for the zero-edge identity (3.2) it was below `1.4e-15`. The symbolic proofs above are the mathematical justification.

## 10. Scope checklist

- arbitrary independent cap-one input densities: retained;
- arbitrary dimension: retained within the stated structural branch;
- arbitrary signs and same-bank quadratic phases: retained by the partner Fourier theorem;
- no moments/support/log-concavity assumptions: yes;
- no post-rotation independence: yes;
- no pointwise scalar oscillatory-decay claim: yes;
- bounded density: proved on the stability branch;
- continuous density: proved on the stability branch via `L^1_t`;
- full three-large-eigenvalue theorem: OPEN;
- target-wide universal `L^1_t` criterion: OPEN / no counterexample found.
