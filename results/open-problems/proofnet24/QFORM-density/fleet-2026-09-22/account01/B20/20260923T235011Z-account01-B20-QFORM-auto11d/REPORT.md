SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T23:50:11Z.
attacking: the newest account02/B20 r39 aligned diagonal+rank-eight retained-tail survivor: force a literal physical E3 cut whenever both the physical diagonal and the rank-eight carrier leverage are diffuse.

# account01/B20 — diagonal/rank-eight diffuse-carrier physical-cut closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Classification: `ESSENTIAL_STEP_APPLIED_R39_RANK8_DIFFUSE_CARRIER_E3`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full unrestricted QFORM target: **OPEN**.  
Global continuity: **OPEN**. The branch paid below has a continuous `C_0` density.

The target remains: independent original real coordinates with densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal finite `L^infinity` bound for the density of `X^T A X`. No Gaussian, moment, iid, compact-support, log-concavity, or post-rotation-independence hypothesis is used.

## 1. Fresh completed designated partner actually consumed

The newest completed account02/B20 package visible at the dependency refresh is run

`20260923T233041Z-account02-B20-QFORM-auto11`,

with report commit `8273681c09ca73542cc27a74fdeec554000cfc28`, claims commit `dbb8f48320ce8334a4d23771537a3b68911bb18e`, and final source refresh `2618f34d8e9610ef92dc628baa81c605c38dfd9c`.

Its source-complete compiler says that, after the physical pair-volume coloop branch is separated, the diffuse branch is either paid by aggregate physical third volume, or else has the retained-tail representation

`A = D + K + E`,                                                   (1.1)

where

`D = diag(0_H,Delta)` is diagonal in the ORIGINAL physical coordinates,
`rank K <= 8`,
`||E||_op < 1/32`,                                                (1.2)

and, because `s_3(A)>=1`,

`boxed: s_3(D+K)>31/32.`                                         (1.3)

The same account02/B20 run proves the large aggregate-defect branch directly and leaves as its first source-complete obligation

`QFORM-R39-COLOOP-OR-ALIGNED-RANK8-RETAINEDTAIL-PAYMENT-v1`.

The present run applies (1.1)-(1.3) at an actual inequality and sharpens the aligned branch.

## 2. New deterministic paving lemma for a finite-rank physical carrier

Let `K=U Lambda U^T` be any real symmetric matrix of rank `r<=8`, where `U^T U=I_r`; put `P=UU^T` and

`mu := max_i P_ii = max_i ||U(i,:)||_2^2`.                        (2.1)

### Lemma 2.1 — physical half-cut from diffuse carrier leverage

If `mu<=1/16`, then there is a literal partition of the original coordinates

`[n]=I disjoint_union J`                                          (2.2)

for which

`U_I^T U_I >= g I_r`,  `U_J^T U_J >= g I_r`,                     (2.3)

with

`g := (1-1/sqrt(2))/2 = 0.146446609406726...`.                    (2.4)

Consequently, for every `1<=k<=r`,

`s_k(K[I,J]) >= g s_k(K)`.                                       (2.5)

#### Proof

Choose each physical coordinate independently for `I` with probability `1/2`. Write `u_i=U(i,:)^T` and

`R:=U_I^T U_I-(1/2)I_r=sum_i (xi_i-1/2)u_i u_i^T`.

Independence and centering give

`E ||R||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ||u_i||^4
 <= (mu/4) sum_i ||u_i||^2
 = (mu r)/4
 <= 1/8.`                                                        (2.6)

Hence one deterministic physical partition satisfies

`||R||_op <= ||R||_F <= 1/(2 sqrt(2))`.                           (2.7)

Because `U_J^T U_J=I_r-U_I^T U_I`, both Gram matrices in (2.3) are bounded below by `g I_r`.

For that partition put

`Q_I=U_I (U_I^T U_I)^(-1/2)`,
`Q_J=U_J (U_J^T U_J)^(-1/2)`.

The columns of `Q_I,Q_J` are orthonormal, and

`K[I,J]
 = Q_I (U_I^T U_I)^(1/2) Lambda (U_J^T U_J)^(1/2) Q_J^T`.

Left/right multiplication by the partial isometries does not change the nonzero singular values, while the standard singular-value product inequality gives

`s_k(K[I,J])
 >= lambda_min(U_I^T U_I)^(1/2)
    s_k(Lambda)
    lambda_min(U_J^T U_J)^(1/2)
 >= g s_k(K)`.

This proves (2.5). The random partition is only a probabilistic method on coordinate labels; no random-variable rotation is made. QED.

## 3. New theorem: the diffuse aligned rank-eight survivor is paid

### Theorem 3.1 — `QFORM-R39-ALIGNED-R8-DIFFUSECARRIER-E3-v1`

Assume the account02/B20 aligned state (1.1)-(1.3). If simultaneously

`||D||_op <= 3/4`                                                  (3.1)

and, for the physical carrier projection `P=Proj range(K)`,

`max_i P_ii <= 1/16`,                                             (3.2)

then there exists a literal original-coordinate cross cut `N=A[I,J]` such that

`boxed: s_3(N) > gamma`,                                          (3.3)

where

`gamma := (5-7/sqrt(2))/64
        = 0.00078519580772136... >0`.                             (3.4)

Therefore

`e_3(NN^T) > gamma^6`,                                            (3.5)

and the completed marginal-free physical `E_3` theorem gives the full ambient law

`boxed:
 ||p_Q||_infinity
 < C_3/gamma
 = 13436.3539992... < 13436.354,`                                 (3.6)

where

`C_3=3*2^(4/3)*e^(1/3)=10.5501688311...`.

The density in this paid branch is continuous and vanishes at infinity.

#### Proof

From (1.3), (3.1), and singular-value Weyl,

`s_3(K)
 >= s_3(D+K)-||D||_op
 >31/32-3/4
 =7/32.`                                                          (3.7)

Apply Lemma 2.1 to the rank-at-most-eight carrier of `K`; (3.2) supplies the hypothesis. On its physical partition,

`s_3(K[I,J]) > g*(7/32)`.                                        (3.8)

The diagonal matrix `D` has zero `I x J` block. The retained coefficient tail is not deleted: literal compression gives

`||E[I,J]||_op <= ||E||_op <1/32`.                               (3.9)

Therefore Weyl on the actual physical cross block

`N=A[I,J]=K[I,J]+E[I,J]`

gives

`s_3(N)
 > (7/32)g-1/32
 = [7(1-1/sqrt(2))-2]/64
 = (5-7/sqrt(2))/64
 =gamma.`                                                         (3.10)

Positivity is exact because `25>49/2`.

If the singular values of `N` are `sigma_1>=sigma_2>=sigma_3>=...`, then

`e_3(NN^T)
 >= sigma_1^2 sigma_2^2 sigma_3^2
 >= sigma_3^6
 > gamma^6`,                                                      (3.11)

which is (3.5). The marginal-free physical third-volume receiver applies to this literal cut with arbitrary same-bank quadratic terms, affine terms, exterior coordinates, signs, and additional spectrum retained. It yields (3.6) and `C_0` continuity. QED.

## 4. Exact application to account02/B20 and new survivor

The partner's aligned diffuse survivor (1.1)-(1.3) is therefore completely paid whenever both (3.1) and (3.2) hold.

Hence every still-unpaid state after the newest completed account02/B20 compiler lies in at least one of the following ORIGINAL-coordinate packets:

1. **pair-volume coloop:** for the inherited physical pair frame, some literal `j in L` has `ell_j>3/4`;
2. **physical diagonal spike:** in the aligned state, some literal light coordinate has `|Delta_j|>3/4`;
3. **finite heavy rank-eight carrier coordinate:** for `P=Proj range(K)`, some literal coordinate has `P_jj>1/16`.

The third packet is quantitatively finite: since

`sum_j P_jj=rank(K)<=8`,                                          (4.1)

there are strictly fewer than `128` coordinates satisfying `P_jj>1/16`, hence at most `127`.

Thus the previous vague `aligned rank-eight retained-tail` obstruction has been replaced by an explicit physical coloop/diagonal-spike/finite-heavy-coordinate obstruction.

The first source-complete unpaid implication is now

`QFORM-R39-COLOOP-OR-DIAGSPIKE-OR-R8-HEAVYCOORD-PAYMENT-v1`:

> pay the physical `ell_j>3/4` pair-volume coloop, or the aligned physical `|Delta_j|>3/4` diagonal spike, or the at-most-127-coordinate carrier-heavy packet, while retaining the nonzero `1/32` coefficient tail and all original-coordinate product structure.

## 5. Scope and corrections

The full unrestricted theorem is **not** claimed. Global continuity is **not** claimed. No counterexample is produced.

This proof uses no law-uniform pointwise quadratic oscillatory decay, no worst-fibre supremum, no arbitrary-joint coarea replacement, no conditional-cap-as-independence step, no post-rotation independence, no deletion of a nonzero random quadratic tail, and no inference of one good physical minor from aggregate volume. The eigendecomposition of `K` is used only as deterministic coefficient geometry to choose a literal original-coordinate partition.

The account02/B20 retained tail `E` is spent only through the deterministic coefficient inequality `||E[I,J]||_op<=||E||_op`; the random polynomial containing that tail remains intact.
