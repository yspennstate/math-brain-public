SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T17:10:49Z.
attacking: eliminate the localized two-hub high-column-leverage survivor by converting fixed-pair anchored third volume into a two-hub plus one projected-crossing packet before any reciprocal pair-core or physical-column inversion.

# fleet03/B09 r37 — localized hub-pair projected-crossing closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Logical worker: `fleet03/B09`  
Run: `20260923T171049Z-fleet03-B09-QFORM-r37`  
Status: new supporting theorem proved and applied; full QFORM remains **OPEN**.  
Continuity: proved in the branch below.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and completed dependency

The target remains: for every dimension, independent real variables with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has universally bounded density, or give a valid counterexample. No Gaussianity, moments, support bounds, log-concavity, connected support, diagonal-basis assumption, or independence after rotation is used here.

The analytic input is the independently checked grouped projected-crossing theorem at

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its `(GC)` estimate allows `k` grouped hub directions and an `ell`-volume projected crossing remainder. For `k=2, ell=1`, if the physical opposite-bank hub cross has rank two, the projected crossing has nonzero Frobenius norm, and every projected-crossing row marginal is at most `1/2`, then with hub projection density cap `M_H`, singular-value product `S`, and `Z_1=||C||_F^2`,

`||p_Q||_infinity <= 3*2^(5/6) M_H^(1/3) S^(-1/3) Z_1^(-1/6)`.

The source proof supplies an integrable characteristic-function envelope. Arbitrary internal hub functions, arbitrary same-bank quadratic terms, every diagonal, every linear term, and arbitrary outside-conditioned affine terms are retained.

## 2. Predecessor branch

In the r32/r34/r35 chain there is a rank-two physical hub/star factorization

`A[H,I]=P C0^T`, `P^T P=I_2`,

with completely arbitrary leaf block `D=A[I,I]`. Let `Gamma_k^2` be the singleton third-volume resources and

`G_* = sum_k Gamma_k^2`.

In the diffuse-singleton branch,

`Gamma_k^2 < (c/2) G_*` for every leaf `k`, where `c=27/256`.

The r32 Bernoulli compiler gives a leaf partition `S,T` such that

`W(S)>=c G_*`.

The r34 high-hub routing either pays a one-anchor branch or gives two literal physical hub rows `a,b` with Pluecker weight

`w=det(P[{a,b},:])^2 >=16/25`.

For this fixed pair, r35 proves

`V_ab(S)=w W(S) >= (27/400) G_*`,                         (2.1)

where

`V_ab(S)=sum_{k in S} sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`.

The r36 regularized-determinant theorem paid this branch only when the column-side range projection of the cross cut was diffuse. The remaining debt was column leverage `>1/2`, possibly one.

## 3. Exact exterior-volume identity

Condition on every original coordinate outside `{a,b} union S union T`. Put

`B=A[{a,b},T]`, `R=A[S,T]`, `Delta=det(BB^T)`.

Because `V_ab(S)>0`, the two rows of `B` are linearly independent, so `Delta>0`. Let `Pi` be the orthogonal projection in `R^T` onto `row(B)` and define

`C=R(I-Pi)`.                                                  (3.1)

For each `k in S`, let `r_k` be row `k` of `R`, `c_k=r_k(I-Pi)`, and

`V_k=sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`.             (3.2)

### Lemma 3.1

For every `k in S`,

`V_k = Delta ||c_k||_2^2`,                                   (3.3)

and therefore

`boxed: V_ab(S)=Delta ||C||_F^2.`                             (3.4)

### Proof

The Gram matrix of the three-row matrix `[B;r_k]` is

`[[BB^T, B r_k^T], [r_k B^T, ||r_k||^2]]`.

Its determinant equals, by the Schur-complement formula,

`det(BB^T) * (||r_k||^2-r_k B^T(BB^T)^(-1)B r_k^T)`

`= Delta ||r_k(I-Pi)||^2 = Delta ||c_k||^2`.

By Cauchy--Binet that Gram determinant is exactly the sum of squared physical `3x3` minors in (3.2). Summing over `k` proves (3.4). QED.

No random-variable rotation is used.

## 4. The projected-crossing row gate is automatic

The r32/r35 factorization gives

`V_k=w w_k(S)`, `V_ab(S)=w W(S)`.

Hence the normalized one-volume row marginal of `C` is

`alpha_k = ||c_k||^2/||C||_F^2`

`= V_k/V_ab(S) = w_k(S)/W(S)`

`<= Gamma_k^2/W(S)`

`< [(c/2)G_*]/[cG_*] = 1/2`.                                 (4.1)

Thus the row-marginal gate needed by the reviewed `k=2, ell=1` projected-crossing theorem is exactly the diffuse-singleton hypothesis already present upstream. No column leverage appears.

## 5. Main theorem

### `QFORM-LOCALIZED-HUBPAIR-PROJECTED-CROSSING-CLOSURE-v1`

Under the localized-pair setup above, with `V_ab(S)>0` and (4.1), the full quadratic form, with arbitrary physical pair core, arbitrary leaf curvature, arbitrary conditioned outside couplings, arbitrary affine terms and arbitrary signs, has a continuous density satisfying

`boxed: ||p_Q||_infinity <= 3*2^(5/6) V_ab(S)^(-1/6).`         (5.1)

Consequently every interval `L` satisfies

`P(Q in L) <= 3*2^(5/6) V_ab(S)^(-1/6) |L|`.                 (5.2)

Using (2.1),

`boxed: ||p_Q||_infinity`

`<= 3*2^(5/6)*(400/27)^(1/6) G_*^(-1/6)`

`< 8.378 G_*^(-1/6).`                                       (5.3)

### Proof

Take the two *physical* hub variables themselves: `X_H=(X_a,X_b)`, `U=I_2`, `W=X_H`. Their joint product density is bounded by one, so `M_H<=1`.

Let `X'=(X_S,X_T)`. The conditioned polynomial has exactly the source form

`Q=F(X_H)+2<W,M X'+beta>+R0(X')`,                            (5.4)

where `F` contains the arbitrary pair core and hub affine terms, and `R0` contains the arbitrary quadratic-affine leaf polynomial. Split the light variables as `I=S`, `J=T`. Then `M_J=B`, and the product of its two nonzero singular values is

`S_B=sqrt(det(BB^T))=Delta^(1/2)`.                            (5.5)

The source projected crossing is exactly `C` in (3.1), so

`Z_1=||C||_F^2=V_ab(S)/Delta`.                               (5.6)

The source row-marginal condition is (4.1). Apply `(GC)` with `k=2`, `ell=1`, `d=3` (for `ell=1` its entropy exponential is omitted):

`||p_Q||_infinity`

`<=3*2^(5/6) Delta^(-1/6) [V_ab(S)/Delta]^(-1/6)`

`=3*2^(5/6) V_ab(S)^(-1/6)`.                                (5.7)

The `Delta` dependence cancels exactly before any reciprocal physical-pair or column-minor selection. The source characteristic-function envelope is integrable, so Fourier inversion gives a continuous density and (5.2). QED.

An explicit envelope is

`|phi_Q(t)| <= min(1, 2^(5/4) pi^(3/2) V_ab(S)^(-1/4) |t|^(-3/2))`.  (5.8)

Integrating (5.8) gives (5.1).

## 6. Consequence for the previous debt

The r35 exact-core routing split according to the algebraic type of `E=A[{a,b},{a,b}]` and left near-stratum blow-up. r36 removed `E` but needed diffuse opposite-bank column leverage. The theorem above depends on neither:

- no reciprocal `det E`, `sigma_min(E)` or rank-one core coefficient;
- no column-side range leverage.

Therefore the r36 debt `QFORM-LOCALIZED-HUBPAIR-HIGH-COLUMN-LEVERAGE-v1` is closed inside this rank-two hub/star pathway.

This does not solve full QFORM. The remaining connection is upstream: force a universal-scale aggregate resource `G_*`, or route the small-`G_*` near-model into another already-paid cross/pivot/ridge branch while keeping the residual quadratic phase exactly. A small coefficient-matrix norm cannot be discarded because the admissible input laws have no support or moment bound.

Proposed next B09 debt: `QFORM-RANK2-HUBSTAR-GSTAR-SCALE-OR-PAID-EXIT-v1`.

## 7. Target-valid stress family where r36 fails maximally

Fix `m>=10` and use original coordinates

`a,b,k_1,...,k_m,t_1,t_2,u_1,...,u_m`.

Let the only nonzero off-diagonal coefficients of the symmetric matrix `A_m` be

`A[a,t_1]=1`, `A[b,t_2]=1`, `A[k_i,u_i]=m^(-1/2)` for `1<=i<=m`,

with symmetric transposes and zero diagonal.

Across the physical cut

`{a,b,k_1,...,k_m} | {t_1,t_2,u_1,...,u_m}`

the cross block is diagonal with singular values

`1,1,m^(-1/2),...,m^(-1/2)`.

Hence the full symmetric matrix has eigenvalues `+1,+1,-1,-1` and `m` copies each of `+m^(-1/2),-m^(-1/2)`. It is target-valid with four eigenvalues of modulus one.

View `a,b` as the rank-two physical hubs. Then `P=I_2`, the fixed pair has `w=1`, every nonzero singleton volume equals `1/m`, and `G_*=2`. For `m>=10` the r32 diffuse-singleton gate holds. Choose `S={k_1,...,k_m}` and `T={t_1,t_2,u_1,...,u_m}`. Then

`W(S)=1`, `V_ab(S)=1`, `Delta=1`, `||C||_F^2=1`,

and every projected-crossing row marginal is `1/m`.

But the full cross matrix `A[{a,b} union S,T]` is square and invertible, so its column range projection is the identity: every column leverage is exactly one. Thus the r36 theorem is maximally unavailable, while the new theorem gives, uniformly in `m`,

`boxed: ||p_Q||_infinity <=3*2^(5/6)=5.345392308842...`.       (7.1)

## 8. Designated partner fleet04/B09 actually applied

The designated partner theorem is `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1` at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

For any literal invertible physical `3x3` cross block `K`, it proves

`||p_Q||_infinity <=3 |det K|^(-1/3)`,                       (8.1)

with arbitrary dense same-side curvature and a continuous density.

On the stress family, choose rows `{a,b,k_i}` and columns `{t_1,t_2,u_i}`. Then

`K=diag(1,1,m^(-1/2))`,

so the partner theorem gives the actual inequality

`||p_Q||_infinity <=3 m^(1/6)`.                              (8.2)

At `m=128`, this is

`boxed: ||p_Q||_infinity <=6.734772289856...`.                (8.3)

The estimate is valid but deteriorates with `m`; the aggregate projected-crossing theorem remains at `5.345392308842...` because it spends the entire diffuse packet before reciprocal minor selection.

## 9. Deterministic check

`CHECK.py` in this directory verifies on 100 seeded random instances that (3.3)-(3.4) hold to relative error below `1.5e-15`. It also checks the `m=128` regression:

- `Gamma_k^2=1/128=0.0078125`;
- diffuse threshold `(27/512)G_*=0.10546875`;
- `G_*=2`, `W=1`, `V_ab=1`;
- projected row marginal `1/128`;
- column range leverage exactly one;
- new aggregate constant `5.345392308842`;
- partner physical-minor constant `6.734772289856`;
- four eigenvalues satisfy `|lambda|>=1`.

All checks pass. These computations verify only the deterministic algebra/regression; no Monte Carlo or histogram is used as proof.

## 10. Scope

This run proves a source-coordinate, product-preserving `O(|L|)` estimate for the localized physical-pair survivor and removes both pair-core near-stratum blow-up and high opposite-bank column leverage in that branch. It does not assert the full owner conjecture.

Full QFORM status: **OPEN**.  
Full-target continuity: **OPEN**.  
Continuity in theorem (5.1): **PROVED**.  
Native learned-memory status: `WITHOUT_VERIFIED_BRAIN`.
