SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T23:10:57Z.
attacking: the first source-complete r39/B20 gap after principal-minimal descent — convert the restored physical D2 pair-volume into either a genuine physical E3 density exit or a dimension-free common-plane reduction, without selecting one small minor and without discarding a nonzero coefficient tail.

# fleet02/B19 — aggregate E3 lift and dimension-free common-plane rigidity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS / complementary source-valid constructions  
Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: the positive E3 exit below has a continuous `C_0` density by the cited Fourier receiver; no unrestricted continuity claim is made.

All coordinates below are literal ORIGINAL product coordinates. There is no post-rotation independence, no support or moment hypothesis, no log-concavity, no iid hypothesis, no arbitrary-joint coarea substitution, no law-uniform pointwise quadratic-phase decay, and no deletion of a nonzero coefficient matrix as a small random error.

## 1. Fresh proof graph and exact source boundary


The newest completed designated partner fleet03/B19 r43 is

`yspennstate/math-open-problems@ef38106705da5fab5a2fb6dbdd64745206580f62`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T220120Z-fleet03-B19-QFORM-r43/REPORT.md`.

Its proved principal-minimal induction says that the full affine interval theorem with one constant reduces, with **no constant loss**, to matrices `A` satisfying

`N_A(1)>=3`, while every proper ORIGINAL-coordinate principal submatrix has `N<=2`.

Moreover an irreducible target has exactly three threshold-large eigenvalues, or four with mixed signs. Thus arbitrary additional target-scale spectrum is no longer a separate analytic debt.

The newest fleet02/B20 source used here is

`yspennstate/math-open-problems@405fc21676782cde5254f7a7b9709f06e188a672`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T225733Z-fleet02-B20-QFORM-auto11/REPORT.md`.

It restores the physical provenance lost by the compressed phrase “rank-six carrier”: there is a physical partition `H disjoint_union L`, `|H|<=124`, and a literal physical hub pair `T subset H` such that, with

`M=A[T,L]`, `G=MM^T`, `S=sqrt(det G)`,

one has

`S>S0:=1/(480 sqrt(7626))=2.3856699607287348e-5`.                    (1.1)

For the physical column leverage

`ell_j=m_j^T G^{-1}m_j`,                                             (1.2)

where `m_j` is column `j` of `M`, B20 proves the exhaustive alternative

* diffuse D2: `max_j ell_j<=3/4`, in which the full ambient law has `H_{1/2}<265.625`; or
* physical D2-coloop: some literal light coordinate has `ell_j>3/4`.

The newest compatible product-Fourier receiver used below is fleet03/B04 r42,

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`,

which proves for every literal disjoint physical cross block `N`

`||p_Q||_infinity <= C_E3 E_3(N)^(-1/6)`,                           (1.3)

with

`C_E3=8.45302122552817687470491804598...`,                          (1.4)

without a marginal hypothesis; same-bank quadratic terms, outside couplings and affine terms are retained.

The owner-required pinned source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed result applied at an actual inequality below is its D' theorem: if a physical third-volume cross block has natural row marginals at most `h<3/4`, then

`||p_Q||_infinity <=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) E_3(N)^(-1/6)`. (1.5)

The pinned search still contains no valid counterexample to the owner target; that numerical/search observation is not used as proof.

## 2. Local third-column identity

Fix the physical pair `T` and light bank `L` from (1.1). For each `j in L`, write

`I_j=L\{j}`,
`P_j=M[:,I_j]^T`,
`c_j=A[I_j,j]`,
`d_j=dist(c_j,col(P_j))`.                                           (2.1)

Thus `[P_j,c_j]` is exactly the three-column physical cross block

`A[I_j,T union {j}]`.                                                (2.2)

### Lemma 2.1 — `QFORM-D2-LOCAL-E3-DEFECT-IDENTITY-v1`

For every `j`,

`boxed: E_3(A[I_j,T union {j}]) = S^2(1-ell_j)d_j^2.`                (2.3)

Here `E_3(N)=e_3(N^TN)`.

### Proof

The first two columns have Gram matrix

`P_j^T P_j=G-m_jm_j^T`.

The matrix determinant lemma gives

`det(P_j^TP_j)=det G (1-m_j^TG^{-1}m_j)=S^2(1-ell_j)`.               (2.4)

When `P_j` has rank two, the three-vector Gram determinant factors as

`det([P_j,c_j]^T[P_j,c_j])
 =det(P_j^TP_j) dist(c_j,col(P_j))^2`.                               (2.5)

If `P_j` has rank at most one, then `ell_j=1`, both sides of (2.3) vanish, and (2.3) remains valid. QED.

The quantity `d_j` is therefore not an invented coefficient norm: it is exactly the transverse part of one physical self-column measured by a physical E3 volume.

Define the aggregate third-volume defect

`Zagg := sum_(j in L) S^2(1-ell_j)d_j^2`.                            (2.6)

## 3. No single-minor loss: one physical cut captures a sixteenth of the aggregate defect

### Theorem 3.1 — `QFORM-D2-AGGREGATE-E3-RANDOM-CUT-v1`

There is a partition of the ORIGINAL light coordinates

`L=I disjoint_union J`

for which the literal physical cross block

`N=A[I,T union J]`                                                   (3.1)

satisfies

`boxed: E_3(N)>=Zagg/16.`                                           (3.2)

### Proof

Assign each light coordinate independently to `I` or `J` with probability `1/2`. In the Cauchy--Binet sum defining `E_3(N)`, retain only the column triples

`T union {j}`, `j in J`.                                             (3.3)

For a fixed `j`, Lemma 2.1 expresses its local volume as the sum of squared `3x3` minors over all row triples `R subset L\{j}`. Such a squared minor appears in the restricted sum for `N` exactly when

`j in J` and `R subset I`.                                          (3.4)

The four distinct physical coordinates involved are assigned independently, so (3.4) has probability `2^-4=1/16`. Hence

`E E_3(N) >= Zagg/16`.                                               (3.5)

Some physical split realizes at least its expectation. QED.

This is the point needed by the assembly: aggregate local transverse information is converted to **one disjoint physical cross block without dividing by `|L|` and without asserting one good local minor**.

## 4. Actual density payment and pinned-e5 application

Take the fixed threshold already native to the finite-core proof,

`zeta0=2^-60`.                                                       (4.1)

If

`Zagg>=zeta0`,                                                       (4.2)

Theorem 3.1 gives a physical cross block with

`E_3(N)>=2^-64`.                                                     (4.3)

Applying the marginal-free completed E3 receiver (1.3) gives

`||p_Q||_infinity
 <= C_E3 2^(64/6)
 =13740.374820570052... <13741.`                                    (4.4)

This branch has a continuous `C_0` density.

The owner-required pinned e5 theorem is also spent at the same **actual** block. If its natural third-volume row marginals are at most `h=2/3`, (1.5) gives

`||p_Q||_infinity
 <=9 sqrt(3e) E_3(N)^(-1/6)
 <=9 sqrt(3e) 2^(64/6)
 =41776.975761066285... <41777.`                                    (4.5)

Thus the pinned theorem directly pays the diffuse-marginal subbranch; the newer incident/heavy-row completion underlying (1.3) removes the marginal gate and improves the universal constant to (4.4).

The pinned D5 theorem remains an independent immediate exit as well: any physical cross block with `e_5(N^TN)>=1/1024` satisfies

`||p_Q||_infinity <=10 sqrt(2e)<23.317`.                             (4.6)

Consequently all states reaching the new rigidity branch may be assumed to have failed those already-paid physical volume exits.

## 5. Dimension-free common-plane rigidity in the diffuse D2 branch

Now assume the B20 diffuse condition

`max_j ell_j<=3/4`.                                                  (5.1)

Normalize the physical two-frame by

`v_j=G^(-1/2)m_j`, `V=G^(-1/2)M`,                                  (5.2)

so

`sum_j v_jv_j^T=I_2`, `||v_j||^2=ell_j`.                            (5.3)

The invertible right transformation in (5.2) does not change the column spaces in (2.1), hence it does not change `d_j`.

For each `j`, choose the least-squares vector `y_j in R^2` and residuals

`r_ij=A_ij-v_i^Ty_j`, `i!=j`,                                      (5.4)

so

`sum_(i!=j) r_ij^2=d_j^2`.                                         (5.5)

Put

`D^2=sum_j d_j^2`.                                                  (5.6)

### Theorem 5.1 — `QFORM-D2-DIFFUSE-COMMONPLANE-RIGIDITY-v1`

There is a real symmetric `2x2` matrix `K`, a physical diagonal matrix `Delta`, and a symmetric zero-diagonal residual `E` such that

`boxed: A[L,L]=Delta+V^T K V+E`,                                   (5.7)

with the dimension-free bounds

`||E||op <=||E||F <=sqrt(26) D`                                    (5.8)

and therefore

`boxed: ||E||op <=2 sqrt(26) sqrt(Zagg)/S.`                         (5.9)

Equivalently, since `V=G^-1/2M`, there is a symmetric `K_phys` with

`A[L,L]=Delta+M^T K_phys M+E`.                                     (5.10)

### Proof

Symmetry of `A[L,L]` gives, for `i!=j`,

`e_ij:=v_i^Ty_j-v_j^Ty_i=r_ji-r_ij`.                               (5.11)

Define

`B=sum_i v_i y_i^T`.                                                (5.12)

Using the Parseval identity (5.3), for each `j` one has the exact cancellation

`sum_(i!=j) v_i e_ij
 =(I-v_jv_j^T)y_j-[Bv_j-v_j(y_j^Tv_j)]
 =y_j-Bv_j`.                                                        (5.13)

The map `(a_i)->sum_i v_i a_i` has operator norm one by (5.3), so

`sum_j ||y_j-Bv_j||^2
 <=sum_(i!=j)e_ij^2
 <=4D^2`.                                                           (5.14)

Also

`B-B^T
 =sum_i v_i(y_i-Bv_i)^T`,                                          (5.15)

because `sum_i v_iv_i^T=I`. Cauchy--Schwarz and `sum_i||v_i||^2=2` give

`||B-B^T||F <=2 sqrt(2) D`.                                        (5.16)

Set

`K=(B+B^T)/2`.                                                      (5.17)

Then `||B-K||F<=sqrt(2)D`, and a second use of (5.3) yields

`sum_j ||y_j-Kv_j||^2
 <=2(4D^2)+2||B-K||F^2
 <=12D^2`.                                                          (5.18)

For `i!=j`, define

`E_ij=A_ij-v_i^TKv_j`,                                              (5.19)

and choose `Delta` so that `E_jj=0`. By (5.4),

`E_ij=r_ij+v_i^T(y_j-Kv_j)`.                                       (5.20)

Therefore

`||E||F^2
 <=2D^2+2 sum_j sum_i [v_i^T(y_j-Kv_j)]^2
 <=2D^2+24D^2
 =26D^2`,                                                           (5.21)

which proves (5.8).

Finally, (5.1) and (2.6) imply

`Zagg=S^2 sum_j(1-ell_j)d_j^2 >= (S^2/4)D^2`.                       (5.22)

Combining (5.8) and (5.22) proves (5.9). QED.

At the live physical scale (1.1), failure of the aggregate E3 payment (4.2) therefore forces

`boxed:
 A[L,L]=Delta+M^T K_phys M+E,
 ||E||op <2 sqrt(26) 2^-30/S0
          =0.00039811307176481383.}`                                (5.23)

This is a substantial narrowing: the arbitrary light-bank curvature has collapsed, in a source-valid dimension-free way, to a physical diagonal plus the **same two-dimensional common plane carried by the hub pair**, with a rigorously retained coefficient residual below `3.982e-4`.

Crucially, (5.23) is coefficient geometry only. The nonzero `E` is NOT discarded, and no assertion is made that `X^TEX` is small for arbitrary unbounded cap-one laws.

When `Zagg=0`, (5.9) gives `E=0`, hence the exact common-plane form

`A[L,L]=Delta+M^T K_phys M`.                                       (5.24)

This recovers algebraically the exact common-plane chamber used in the current latent-center pipeline, without choosing a local minor.

## 6. Why the D2-coloop must remain separate: an exact target-valid obstruction

The implication

`Zagg=0 => exact common-plane form`                                 (6.1)

is **false without excluding an exact physical volume-coloop**. The weight `(1-ell_j)` in (2.6) is essential.

### Proposition 6.1 — `QFORM-ZAGG-ZERO-COMMONPLANE-COLOOP-FALSE-v1`

Take `L={1,2,3,4}` and let

`a_2=a_3=a_4=1/sqrt(3)`, `s=2`.

Define the physical `2x4` cross block by

`m_1=s e_1`,
`m_k=s a_k e_2`, `k=2,3,4`.                                        (6.2)

Then

`G=MM^T=4I_2`, `S=4`,
`ell_1=1`, `ell_2=ell_3=ell_4=1/3`.                                (6.3)

Let the light self block have zero diagonal and only the star entries

`A_12=epsilon`, `A_13=-epsilon`, `A_14=0`,                          (6.4)

with symmetry, all other light off-diagonals zero, and take for example `epsilon=0.1`.

For `k=2,3,4`, the self-column `A[L\{k},k]` is exactly in `col(M[:,L\{k}]^T)`, so `d_k=0`. For `j=1`, `d_1` is nonzero, but `1-ell_1=0`. Hence

`boxed: Zagg=0`.                                                     (6.5)

Nevertheless no symmetric `K` can satisfy the exact common-plane relation: it would require

`A_1k=m_1^T K m_k =4 a_k K_12`,                                    (6.6)

so the ratios `A_1k/a_k` would have to be constant, contrary to `(epsilon,-epsilon,0)`.

This geometry occurs inside the owner target class. Put the `T-T` block equal to zero and take the full coefficient matrix

`A=[[0,M],[M^T,A[L,L]]]`.                                           (6.7)

With the light self block removed, (6.7) has nonzero spectrum `{2,2,-2,-2}`. The perturbation (6.4) has operator norm `sqrt(2) epsilon<0.142`, so Weyl leaves at least four eigenvalues of modulus greater than `1.85`; in particular the full matrix has at least three eigenvalues of modulus at least one.

Thus Proposition 6.1 is a target-valid counterexample to extending the diffuse rigidity theorem across an exact D2-coloop. It is **not** a counterexample to QFORM itself.

## 7. Splice into the current full proof graph

The source-pinned proof graph can now be sharpened as follows.

1. By fleet03/B19 r43, it suffices with the same desired interval constant to pay principal-minimal affine targets; those have three threshold-large eigenvalues, or mixed-sign four.
2. The finite-core route must retain the upstream physical pair-area. Fleet02/B20 supplies a literal `T,L` with `S>S0` and then the diffuse/coloop D2 dichotomy.
3. In **either** D2 branch, the aggregate third defect `Zagg>=2^-60` is now paid by one physical disjoint E3 cut, with `||p_Q||infinity<13741`; the pinned e5 D' theorem supplies the explicit subbranch (4.5).
4. In the **diffuse** D2 branch, failure of that E3 payment forces the source-valid common-plane approximation (5.23), with no dimension loss and no selected-minor denominator.
5. At `Zagg=0`, the light block is exactly diagonal plus the same rank-two physical common plane. This is precisely the coefficient geometry feeding the existing common-plane / latent-center analysis. Fleet01/B19 r11 then shows, in its exact invertible-pair center, that the two-dimensional latent core retains universal two-volume and the full Schur remainder has operator norm at least one.
6. A nonzero residual in (5.23) cannot be erased by coefficient continuity. The exact-coloop construction in Section 6 shows separately that the weighted aggregate defect cannot control an unweighted common-plane residual on the coloop side.

Accordingly the first sharpened analytic debt is now

`QFORM-DIFFUSE-D2-PUNCTURED-COMMONPLANE-RESIDUAL-PAYMENT-v1`:

> In the principal-minimal r39 survivor, after all existing physical pair/triple, D/D'/D5, E3, ridge/window, grouped-hub and exact common-plane exits have failed, pay the state
>
> `A[L,L]=Delta+M^T K M+E`,
> `sqrt(det(MM^T))>1/(480 sqrt(7626))`,
> `max_j m_j^T(MM^T)^(-1)m_j<=3/4`,
> `||E||op<0.000398114`,
>
> with `E` retained as an actual nonzero coefficient matrix and arbitrary rough cap-one product laws; or give a source-preserving descent to a completed receiver. No coefficient-continuity, moment bound, or post-rotation independence is permitted.

The parallel coloop debt is narrower and genuinely different:

`QFORM-D2-COLOOP-WEIGHTED-THIRD-RESOURCE-PAYMENT-v1`:

> spend the literal `ell_j>3/4` volume-coloop when the aggregate physical E3 defect is below `2^-60`; Proposition 6.1 shows that zero weighted defect alone does not imply an exact common plane.

These are now the first local analytic gates after the global principal-minimal descent; arbitrary extra target-scale spectrum no longer needs to be duplicated in them.

## 8. Deterministic checks

The companion checker verifies, over thirty seeded random instances:

* the local identity (2.3) to relative error below `2.8e-15`;
* exhaustive physical splits always beat the guaranteed `Zagg/16` by a factor at least `5.61` in the sample;
* the tested rigidity ratio `||E||F^2/D^2` is at most `1.413`, well below the proved constant `26`;
* the live constants are
  `S0=2.385669960728735e-5`,
  E3 branch `<13740.375`,
  pinned-D' subbranch `<41776.976`, and
  residual bound `<0.000398114`.

The checker terminates `QFORM_B19_AGGREGATE_E3_RIGIDITY_CHECK_PASS`. The proof itself is exact and does not depend on numerics.

## 9. Status

The unrestricted QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. The new E3 branch is a completed target-level payment; the common-plane theorem is a deterministic source-valid structural reduction; Proposition 6.1 is only a counterexample to an intermediate structural inference. Full-target continuity remains open and the required two independent end-to-end reviews do not exist.
