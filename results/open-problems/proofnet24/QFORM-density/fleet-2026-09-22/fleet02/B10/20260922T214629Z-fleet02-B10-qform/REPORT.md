SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-22T21:46:29Z.
attacking: the heavy-null residual-leakage endpoint: group the heavy null coordinate with one residual bank, close every one-large-leakage state by the grouped L2 Fresnel theorem, then stress-test the double-small leakage chamber.

# fleet02/B10 — one-large-leakage grouped-Fresnel closure and a double-small hard family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**Method:** complementary constructions and source-valid counterexamples  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / LOCAL_CANDIDATE_REFUTED / FULL_TARGET_OPEN`.

The full target remains open: for arbitrary independent real original-coordinate inputs with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of magnitude at least one, prove one universal finite bound for the density of `X^T A X`, or give a target-valid counterexample. This report proves a new exact-rank-three branch and a structural falsifier; it does not promote the full conjecture.

## 1. Source and correction boundary


The essential immutable dependencies read for this run are:

1. **Named partner fleet03/B10 r18**, canonical `yspennstate/math-open-problems@ed915899a1cc9f7582b8462998fe024d6045805c`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T211827Z-fleet03-B10-QFORM-r18/REPORT.md`. It gives the residual-leakage factorization, the exact three-cross singular-value product, and the `<214` three-cross branch used below.
2. **Partner fleet03/B10 r15 null-bank compression**, canonical `yspennstate/math-open-problems@a3dd62b198d84dc9b92653b8a9c77494fc6ed2d4`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T191739Z-fleet03-B10-QFORM-r15/REPORT.md`. It replaces the near-full exact null bank by a genuine independent cap-one synthetic coordinate without changing the quadratic law and gives the quantitative heavy-null state used below.
3. **fleet03/B19 two-bank partition**, canonical `yspennstate/math-open-problems@63568dad79e5381abb3081ef4685ea126fdd4297`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T203112Z-fleet03-B19-QFORM/REPORT.md`. It proves the original-index residual partition with `det S_J det S_K >=1/640`.
4. **fleet01/B16 grouped product Fresnel theorem**, canonical `yspennstate/math-open-problems@e4c589aa572f7d140c78a832af2d554eed97fde4`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260922T211047Z-fleet01-B16-QFORM-r16/REPORT.md`. Its two-full-product-bank corollary is applied at an actual inequality below.
5. This slot's preceding bank-paving report, canonical `yspennstate/math-open-problems@2045e39c5eda8d2a94098d79932223c77f2a4db7`, established independently that residual-diffuse geometry is not a local-minor problem. The stronger B19 determinant-product partition is used here because it yields the sharper constant needed for the present splice.

The correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` from this slot remains binding: joint/conditional density caps alone do not control the heavy hyperbolic trace. Every grouping below is on disjoint **original-coordinate** sets, so independence is genuine before any spectral projection.

## 2. Inherited exact heavy-null state and the named partner inequality

After the completed cap-one null-bank compression, the unpaid exact-rank-three state can be represented by an `n x 3` Parseval frame `U`, `U^T U=I_3`, and an invertible real symmetric spectral matrix `M`. One physical coordinate, indexed `0`, is genuinely independent of all others and has spectral row

`u_0 = sqrt(c) r`,

where `r` is a unit null direction for `M` and

`c >= 7/9`, `D:=|det M| >=1/2`, `sigma_min(M)>=1/2`.                 (2.1)

Choose the Witt basis with first vector `r`. Write every complementary row as

`u_j=(alpha_j,v_j)`, `v_j in R^2`.                                 (2.2)

The previously paid residual-heavy branch leaves

`sum_j v_j v_j^T=I_2`, `||v_j||^2<=1/2`.                           (2.3)

Apply the completed fleet03/B19 partition. There is a partition of the complementary **physical coordinate** indices into disjoint banks `J,K` such that

`S_G := sum_(j in G) v_jv_j^T`, `G=J,K`,

satisfies

`det S_J det S_K >=1/640`.                                         (2.4)

For each bank let `V_G` have rows `v_j^T`, and make the exact least-squares decomposition

`alpha_G = V_G p_G + eta_G`, `V_G^T eta_G=0`,
`tau_G := ||eta_G||^2`.                                            (2.5)

The named partner r18 proves that the physical cross block `A[J,K]` has three nonzero singular values whenever `tau_J,tau_K>0`, with

`s_1s_2s_3 = D sqrt(tau_J tau_K det S_J det S_K),`                 (2.6)

and that if

`tau_J,tau_K >=1/64`, `min(L_J,L_K)<=2/3`,                        (2.7)

where `L_G` is the cross-range maximum leverage defined in that report, then

`||p_Q||_infinity <214`,                                          (2.8)

with a continuous density. This is an actual inequality-level use of the designated partner result. The point of the new argument below is that the leverage restriction in (2.7), and even the requirement that **both** leakages be large, are unnecessary once the heavy null coordinate is grouped with the opposite bank.

## 3. New theorem: one large leakage is enough

### Theorem 3.1 — `QFORM-HEAVY-NULL-ONE-LARGE-LEAKAGE-FRESNEL-v1`

In the state (2.1)--(2.5), if

`max(tau_J,tau_K) >=1/64`,                                       (3.1)

then the full exact-rank-three quadratic form has a bounded **continuous** density and

`boxed: ||p_Q||_infinity <46.282.`                               (3.2)

No assumption on `L_J,L_K` is needed. In particular this closes the partner r18 high/high-leverage complement of (2.7), and also closes states where only one leakage is at least `1/64`.

#### Proof

By symmetry assume

`tau_K>=1/64`.                                                    (3.3)

Form two disjoint original-coordinate source groups

`H={0} union J`, and `K`.                                        (3.4)

They are genuinely independent because the synthetic coordinate `0` produced by the cap-one compression is an independent source coordinate, and `J,K` are disjoint sets of the remaining original physical coordinates.

Let the corresponding `3 x 3` spectral frame operators be

`F_H = u_0u_0^T + sum_(j in J) u_ju_j^T`,
`F_K = sum_(j in K) u_ju_j^T`.                                   (3.5)

We compute their determinants exactly. Write `p_J=(p_1,p_2)` and use the determinant-one spectral shear

`T_J = [[1,0,0],[-p_1,1,0],[-p_2,0,1]].`                         (3.6)

Right multiplication of the row matrix by `T_J` sends

`(alpha_j,v_j) -> (eta_j,v_j)` for `j in J`,                     (3.7)

while leaving `u_0=(sqrt(c),0,0)` unchanged. Therefore

`T_J^T F_H T_J = diag(c+tau_J,S_J)`,                             (3.8)

because `V_J^T eta_J=0`. Since `det T_J=1`,

`boxed: det F_H=(c+tau_J) det S_J.`                              (3.9)

The same determinant-one shear calculation on bank `K`, without a heavy row, gives

`boxed: det F_K=tau_K det S_K.`                                 (3.10)

Consequently

`det F_H det F_K`
`=(c+tau_J)tau_K det S_J det S_K`
`>= c*(1/64)*(1/640)`
`>= 7/368640.`                                                   (3.11)

Both frame operators are positive definite. The two-full-product-bank corollary of fleet01/B16 `QFORM-GROUPED-L2-FRESNEL-v1`, applied with spectral matrix `M`, now gives

`||p_Q||_infinity`
`<=6 D^(-1/3) (det F_H det F_K)^(-1/6).`                         (3.12)

Using `D>=1/2` and (3.11),

`||p_Q||_infinity`
`<=6*2^(1/3)*(368640/7)^(1/6)`
`=46.2819858443... <46.282.`                                    (3.13)

That theorem also supplies continuity. No conditional density is introduced, no spectral-coordinate independence is asserted, and no small coefficient is discarded. QED.

### Consequence

Combining Theorem 3.1 with the already completed zero-leakage branch cited in the partner r18 report, the genuinely unpaid residual-leakage state is reduced to

`boxed: 0<tau_J<1/64 and 0<tau_K<1/64.`                         (3.14)

For the new argument alone, without importing the zero-leakage closure, the necessary survivor is simply `tau_J,tau_K<1/64`.

This strictly sharpens the previous partner frontier `small residual OR double-high leverage`: the double-high-leverage chamber is now irrelevant whenever either residual leakage is at least `1/64`.

## 4. Exact structure of the double-small chamber

The remaining chamber is not arbitrary. Parseval and the heavy row imply

`sum_j alpha_j^2 = rho:=1-c <=2/9`,
`V_J^T alpha_J + V_K^T alpha_K=0`.                               (4.1)

Using (2.5), the second identity is

`S_J p_J+S_K p_K=0`, `S_J+S_K=I_2`.                             (4.2)

Set

`d:=p_J-p_K`.                                                     (4.3)

Equation (4.2) solves exactly as

`boxed: p_J=S_K d,  p_K=-S_J d.`                                (4.4)

The generated longitudinal energy is therefore

`E_gen := p_J^T S_J p_J + p_K^T S_K p_K`
`       = d^T S_J S_K d`.                                       (4.5)

Orthogonality of the residuals gives the exact energy decomposition

`rho=E_gen+tau_J+tau_K`.                                        (4.6)

Let `s_1,s_2` be the eigenvalues of `S_J`. Then those of `S_K` are `1-s_1,1-s_2`, so (2.4) says

`prod_(a=1)^2 s_a(1-s_a)>=1/640`.                               (4.7)

Each factor is at most `1/4`, hence each factor is at least `1/160`. Thus

`(1/160)I_2 <= S_JS_K <=(1/4)I_2`,                              (4.8)

and (4.5) yields

`boxed: 4E_gen <= ||d||^2 <=160E_gen <=160rho <=320/9.`          (4.9)

So when both leakages are tiny, almost all longitudinal energy is a **generated mismatch between the two transverse banks**, and that mismatch is uniformly conditioned by the two-bank partition. This is the correct next resource. It cannot be treated as a small random perturbation: the input laws have no support or moment bound, so a coefficient of size `epsilon` can multiply a variable spread on scale `epsilon^(-1)` while retaining density cap at most one.

The first unpaid implication is therefore

`QFORM-HEAVY-NULL-DOUBLE-SMALL-LEAKAGE-v1`:

> Starting from (2.1)--(2.5), (2.4), and `0<tau_J,tau_K<1/64`, exploit the exact generated-mismatch identity (4.4)--(4.9) to absorb the two genuinely small orthogonal leakage directions without taking conditional-profile suprema or perturbing them away.

A plausible next mechanism is an interpolation between the exact generated-leakage/one-zero-triple theorem at `tau_G=0` and the grouped-Fresnel theorem above, but it must be nonperturbative in the source variables.

## 5. Exact target family showing why the remaining step cannot be a fixed local atom

The double-small chamber is genuine. The following exact-rank-three family has both leakages arbitrarily small while every scalar pivot, heavy-pair determinant, and physical principal triple determinant tends to zero with the number of coordinates.

Fix an even integer `m>=2` and `0<epsilon<1/3` with `epsilon^2<1/9`. Put

`c=7/9`,
`M=[[0,1,0],[1,0,0],[0,0,1]].`                                  (5.1)

Thus `M` has eigenvalues `{-1,1,1}` and `|det M|=1`. Let

`a_1=(1,0)/sqrt(3)`,
`a_2=(-1/2,sqrt(3)/2)/sqrt(3)`,
`a_3=(-1/2,-sqrt(3)/2)/sqrt(3)`.                                (5.2)

Then

`sum_(r=1)^3 a_ra_r^T=(1/2)I_2`.                               (5.3)

Create one heavy row

`u_0=sqrt(7/9)e_1`.                                             (5.4)

In each bank `G=J,K`, replicate each transverse direction `a_r` exactly `m` times with

`v_(G,r,l)=a_r/sqrt(m)`, `1<=l<=m`.                             (5.5)

Choose signs `s_l in {+1,-1}` with exactly `m/2` of each sign and define residual coefficients

`eta_(G,r,l)=epsilon s_l/sqrt(3m)`.                             (5.6)

Then in each bank

`S_G=(1/2)I_2`, `||eta_G||^2=epsilon^2`, `V_G^T eta_G=0`.       (5.7)

Choose `p in R^2` with

`||p||^2=2/9-2epsilon^2`,                                      (5.8)

and set

`alpha_(J,r,l)= v_(J,r,l).p + eta_(J,r,l)`,
`alpha_(K,r,l)=-v_(K,r,l).p + eta_(K,r,l)`.                    (5.9)

Finally set `u_j=(alpha_j,v_j)` for all complement rows and let `U` be the matrix of all rows.

### Exact verification

The transverse frame is Parseval because the two copies of (5.3) sum to `I_2`. The longitudinal-transverse cross term vanishes: the generated pieces contribute `(1/2)p-(1/2)p=0`, while the residual pieces vanish by (5.7). The longitudinal complement energy is

`2[(1/2)||p||^2+epsilon^2]=||p||^2+2epsilon^2=2/9`.             (5.10)

Together with the heavy mass `7/9`, this gives

`boxed: U^T U=I_3.`                                             (5.11)

Therefore

`A:=UMU^T`                                                       (5.12)

has exactly three nonzero eigenvalues, namely `{-1,1,1}`. This is a legitimate target matrix orientation for every `m` and `epsilon`.

The regression residuals are precisely (5.6), so

`boxed: tau_J=tau_K=epsilon^2`,                                 (5.13)

which may be arbitrarily small and positive. Moreover the cross-range row leverage from the named partner formula is, for every row,

`v_j^T S_G^(-1)v_j + eta_j^2/tau_G`
`=2/(3m)+1/(3m)=1/m`.                                          (5.14)

Thus the family is not hiding in a high-leverage exception. The partner three-cross determinant resource is exactly

`s_1s_2s_3`
`=sqrt(epsilon^4*(1/4)*(1/4))`
`=epsilon^2/4`,                                                 (5.15)

so that particular gate degenerates only through the two small residual leakages.

### Every fixed local atom can vanish

Let `P=sqrt(2/9-2epsilon^2)`. For every complementary row,

`|alpha_j| <=(P+epsilon)/sqrt(3m)`,
`|beta_j|,|gamma_j|<=1/sqrt(3m)`.                              (5.16)

Hence its scalar pivot obeys

`|A_jj|=|2alpha_j beta_j+gamma_j^2|`
`<= [2(P+epsilon)+1]/(3m)`.                                    (5.17)

The heavy cross coefficient satisfies

`|A_0j|<=sqrt(c/(3m))`,                                        (5.18)

so the heavy physical pair determinant is at most `c/(3m)`.

For a principal triple containing the heavy row, the exact rank-three Cauchy--Binet identity gives

`|det A_{0jk}|=c det(v_j,v_k)^2`.                              (5.19)

The maximum determinant between two vectors from (5.2), after the `m^(-1/2)` scaling, has square `1/(12m^2)`. Therefore

`boxed: |det A_{0jk}| <= c/(12m^2)=7/(108m^2).`                 (5.20)

A principal triple avoiding the heavy row has determinant at most the product of the three squared row norms and is `O(m^(-3))`, with a constant depending only on the fixed `epsilon` range. Thus, as `m->infinity`, no scalar pivot, heavy pair, or principal triple has a universal nonzero scale.

This is a **local mechanism falsifier**, not a counterexample to QFORM. It shows that the remaining double-small branch cannot be closed by proving that tiny `tau_J,tau_K` force one uniformly conditioned physical atom. The required payment must remain aggregate across source banks.

## 6. Computation and status

`CHECK.py` in this immutable run directory reconstructs the family for `m=2,10,50` at `epsilon=0.05`. It verifies `U^T U=I_3` numerically, nonzero spectrum `{-1,1,1}`, `tau_J=tau_K=epsilon^2`, maximum cross-range leverage `1/m`, the decay of local pivots/pairs/triples, and the constant in (3.13). These finite computations are regression checks only; all claims above are proved by the exact formulas for arbitrary even `m`.

**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / LOCAL_CANDIDATE_REFUTED`. The full exact-rank-three problem and the full arbitrary-rank QFORM conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. Continuity is proved in the one-large-leakage branch by the grouped-Fresnel theorem, not in the remaining double-small chamber or full target.
