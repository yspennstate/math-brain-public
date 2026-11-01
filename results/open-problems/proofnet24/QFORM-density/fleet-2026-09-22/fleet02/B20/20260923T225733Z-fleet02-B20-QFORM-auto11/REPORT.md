SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T22:57:33Z.

# fleet02/B20 — restore the lost pair-volume provenance in the r39 rank-six carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / R39-PROVENANCE-RESTORED / D2-HALFPOTENTIAL-OR-PHYSICAL-COLOOP / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Global continuity: **OPEN**. The new half-potential statement is a rough-law small-ball statement and is not a continuity theorem.

The owner target remains unchanged: for every `n`, every family of independent ORIGINAL real coordinates with one-dimensional densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite `L^infinity` density bound for `X^T A X`, or produce a valid counterexample. No Gaussianity, moments, support regularity, log-concavity, connectedness, diagonal-basis independence, or post-rotation independence is added.

This report does not prove the full target. It does two things that matter for the proof graph:

1. it identifies a genuine information loss in the newest designated-partner r39 summary if the finite-core state is compressed only to “rank-six carrier + small operator error”; and
2. after restoring the source-pinned physical pair-volume that generated that carrier, it proves a universal dichotomy: either the **full ambient quadratic law** already has a bounded half-Riesz potential `<265.625`, or one literal physical light coordinate carries more than `3/4` of the whole two-volume of a fixed physical hub pair.

No random variable is spectrally rotated below.

## 1. Fresh controls and source boundary


The live corrections used here are the current ones: no law-uniform pointwise quadratic-phase decay, no worst-fibre supremum, no conditional projection-height shortcut, no arbitrary-joint three-dimensional coarea substitute, no independence after a deterministic spectral rotation, no deletion of a nonzero coefficient multiplying an unbounded random input, and no inference of one uniformly good physical minor from aggregate volume without proof.

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The pieces actually used at equations below are the physical `D_k` decoupling/Brascamp--Lieb estimate and its fractional-potential corollary. The same source also gives the marginal-free fifth-volume exit

`e_5(N^T N)>=1/1024  =>  ||p_Q||_infinity <=5 sqrt(2e)(1/1024)^(-1/10)=10 sqrt(2e)<23.317`       (1.1)

for any literal physical cross block `N`; this remains an immediate paid exit in the proof graph.

The pinned counterexample search reports no valid counterexample to the owner target. I do not use that observation as proof.

## 2. Newest designated partner r39, consumed at its exact expressions

The newest compatible completed designated partner is fleet03/B20 r39,

`yspennstate/math-open-problems@5d9892edb6f33beda5ce5e10c4482fcc5fe994a8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T214857Z-fleet03-B20-QFORM-r39/REPORT.md`.

Its pairwise-weak finite-core theorem uses

`kappa=2^(-20)`, `tau=kappa^3=2^(-60)`.                              (2.1)

If a physical principal triple in the finite core has determinant magnitude at least `tau`, its completed determinant-only receiver gives the literal payment

`||p_Q||_infinity <102 tau^(-1/3)
                    =102*2^20
                    =106954752`.                                    (2.2)

If that gate fails together with the pairwise-weak gate, r39 proves that the H-side core block has a symmetric rank-at-most-one approximation `L_H` satisfying

`||A[H,H]-L_H||_op
 < (3+122 sqrt(10)) 2^(-20)
 =:epsilon_H
 =0.0003707865472226546`.                                           (2.3)

Combining this with the inherited cross collar `||C-C_2||_op<1/64`, `rank C_2<=2`, r39 writes

`A = diag(0_H,A[L,L]) + K + E`, `rank K<=6`,                        (2.4)

with

`||E||_op < epsilon_H+1/64
          =0.015995786547222654`.                                   (2.5)

Hence, by Weyl and `s_3(A)>=1`,

`s_3(diag(0_H,A[L,L])+K)
 >1-(epsilon_H+1/64)
 =0.9840042134527773`.                                               (2.6)

These are the exact partner expressions used in this run. The retained error in (2.4) is never deleted from the random form.

## 3. A source-valid correction: the carrier-only compression loses indispensable provenance

The displayed conditions (2.4)--(2.6), if stated without the finite-core cross provenance that produced them, are not a narrower structural problem.

### Proposition 3.1 — `QFORM-R39-CARRIER-ONLY-PROVENANCE-LOSS-v1`

Fix any real symmetric target matrix `B` with `s_3(B)>=1`. Add any nonempty physical H-bank and set

`A=0_H direct_sum B`,
`K=0`, `E=0`, `A[L,L]=B`.                                           (3.1)

Then

`rank K=0<=6`, `||E||_op=0`, and

`s_3(diag(0_H,A[L,L])+K)=s_3(B)>=1>0.9840042`.                      (3.2)

Thus the carrier/error/spectral inequalities alone do **not** imply any nonzero carrier norm, any H-side spectral mass, any physical hub, or any interaction of the third target mode with `K`.

This is a counterexample to such an intermediate structural inference, **not** a counterexample to QFORM. Its purpose is proof-graph hygiene: the next theorem must retain the upstream physical cross currency rather than treating (2.4)--(2.6) as a self-contained simplification.

## 4. Restore the inherited physical two-volume

The r39 state comes from fleet03/B19 r42/r41. The compatible source

`yspennstate/math-open-problems@70d462947bf313c24fa3acf49114b5164c02138c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T200734Z-fleet03-B19-QFORM-r41/REPORT.md`

retains the literal physical partition `H disjoint_union L`, with

`m:=|H|<=124`,
`C=A[H,L]`,
`s_1(C)s_2(C)>1/480`,
`s_3(C)<1/64`.                                                       (4.1)

The last inequality is not needed for the theorem below; the first two are the provenance that must not be dropped.

For a physical row pair `T={i,j} subset H`, put

`S_T^2 := det(C[T,L] C[T,L]^T)`.                                   (4.2)

Cauchy--Binet gives

`sum_(|T|=2) S_T^2
 =e_2(CC^T)
 =sum_(r<s) s_r(C)^2 s_s(C)^2
 >=s_1(C)^2 s_2(C)^2
 >1/480^2`.                                                         (4.3)

There are at most

`binom(124,2)=7626`                                                  (4.4)

physical row pairs. Therefore a maximizing literal pair `T` satisfies

`S:=S_T > S_0:=1/(480 sqrt(7626))
             =2.3856699607287348e-5`.                              (4.5)

This is exactly the physical pair-area currency already present upstream of r39.

## 5. Main theorem: diffuse D2 half-potential or one physical volume-coloop

Fix the maximizing physical pair `T` from (4.5) and write

`M=C[T,L]`                                                           (5.1)

as a `2 x |L|` matrix. Let `m_j in R^2` be its column at a physical light coordinate `j in L`, and put

`G=MM^T`, `det G=S^2`.                                               (5.2)

Define the physical column leverage

`ell_j := m_j^T G^(-1)m_j`.                                        (5.3)

These are deterministic coefficient-space numbers; no projected random variables are declared independent.

### Theorem 5.1 — `QFORM-R39-MAXPAIR-D2-HALFPOTENTIAL-OR-COLOOP-v1`

Under the full original-product target hypotheses and the inherited finite-core state (4.1), one of the following holds.

**A. Diffuse two-volume.** If

`max_(j in L) ell_j <=3/4`,                                        (5.4)

then the **full ambient quadratic polynomial**, with arbitrary H-H curvature, arbitrary L-L curvature, all outside couplings, affine terms and extra spectrum retained, satisfies

`H_(1/2)(Q):=sup_t E|Q-t|^(-1/2)
 <=16 e^(1/4)(3/2)^(-1/4) S^(-1/4)
 <265.625`.                                                         (5.5)

Consequently, for every `rho>0`,

`sup_t P(|Q-t|<rho) <265.625 sqrt(rho)`.                            (5.6)

**B. Physical volume-coloop.** Otherwise there is one ORIGINAL light coordinate `j` with `ell_j>3/4`. For that coordinate,

`sum_(k!=j) det([m_j,m_k])^2
 =ell_j S^2
 > (3/4)S^2
 > 3/(4*480^2*7626)
 =4.2685658711425824e-10,`                                         (5.7)

while deleting that one physical column leaves

`det(G-m_jm_j^T)
 =S^2(1-ell_j)
 <S^2/4`.                                                          (5.8)

Thus more than `3/4` of the entire two-volume of the fixed physical hub pair is incident to one literal source coordinate. This is an aggregate coloop certificate, not a selected-small-minor statement.

### Proof

#### Step 1: identify the pinned `D_2` volume law exactly

Apply the pinned physical decoupling theorem to the literal cross block

`A[L,T]=M^T`.                                                       (5.9)

There is only one two-column set on the T-side. On the L-side the natural squared-minor law has weights

`w_{jk}=det([m_j,m_k])^2/S^2`, `j<k`.                              (5.10)

Its row marginal at the original coordinate `j` is the standard rank-two volume-sampling leverage

`alpha_j=sum_(k!=j) w_{jk}=m_j^T G^(-1)m_j=ell_j`.                (5.11)

Also the pinned two-volume currency is

`Z_2=e_2(MM^T)=det(MM^T)=S^2`.                                    (5.12)

#### Step 2: spend the pinned fractional-volume theorem

The pinned `D_k` proof, specialized to `k=2`, gives for every `q>=1` satisfying `q>=2 max_j alpha_j`

`|phi_Q(t)| <= B_q |t|^(-1/q)`,                                   (5.13)

with

`B_q=[e(2pi)^2 q^(-1) Z_2^(-1/2)]^(1/(2q))`.                     (5.14)

The self-blocks on both sides and all outside terms are permitted in this decoupling statement; they cancel or remain as harmless unit-modulus phases in the source proof. No small coefficient is discarded.

Under (5.4) take `q=3/2`. The pinned fractional-potential lemma at `alpha=1/2` gives exactly

`H_(1/2)(Q)
 <= 4 e^(1/4)(2h)^(-1/4)/(1-h) * Z_2^(-1/8)`                     (5.15)

with `h=3/4`. Hence

`H_(1/2)(Q)
 <=16 e^(1/4)(3/2)^(-1/4) S^(-1/4)`.                             (5.16)

Using (4.5), the right side is

`<16 e^(1/4)(3/2)^(-1/4)
  (480 sqrt(7626))^(1/4)
 =265.6245415480431...`,                                          (5.17)

which proves (5.5). Equation (5.6) follows from

`1_(|Q-t|<rho) <=sqrt(rho)|Q-t|^(-1/2)`.                          (5.18)

This is an actual inequality-level use of the required pinned source.

#### Step 3: exact coloop identities

If (5.4) fails, choose `j` with `ell_j>3/4`. Equation (5.11) immediately gives (5.7). The matrix determinant lemma gives

`det(G-m_jm_j^T)=det G (1-m_j^T G^(-1)m_j)
                 =S^2(1-ell_j)`,                                  (5.19)

which is (5.8). QED.

## 6. Interpretation in the proof graph

The r39 rank-six carrier is still useful, but (2.4)--(2.6) should not replace the physical currency (4.1)--(4.5). The stronger source-pinned survivor now has two simultaneously available descriptions:

1. **carrier description:** a rank-at-most-six deterministic carrier over arbitrary L-bank curvature, with retained operator error `<0.015996` and third singular value `>0.9840042` before that error is restored;
2. **physical pair-volume description:** a literal original-coordinate pair `T` with area `S>S_0`, and therefore either the full-law half-potential bound (5.5) or one physical `>3/4` volume-coloop (5.7)--(5.8).

The half-potential bound is not itself an `L^infinity` density bound. It is nevertheless a target-level analytic currency on the **full rough law**, with all same-side curvature and all extra spectrum present; it is precisely the amount of decay needed by a valid independent square/pair peel if a third source-preserving smoothing direction can be isolated.

The coloop branch is equally concrete: any next structural argument may focus on a single original coordinate that carries more than `3/4` of the pair-area, rather than trying to extract one uniformly large `2 x 2` minor from an arbitrarily diffuse packet.

## 7. First unpaid universal implication after this run

The first source-complete unpaid implication is now

`QFORM-R39-TWODIM-CROSS-HALFPOTENTIAL-TO-DENSITY-OR-COLOOP-PAYMENT-v1`:

> Under the full original independent cap-one target hypotheses, `s_3(A)>=1`, and the inherited r39 finite-core state (including `|H|<=124`, `s_1(A[H,L])s_2(A[H,L])>1/480`, the rank-six carrier/error representation, and every retained nonzero tail), use the third target-scale coefficient resource to do one of two things:
> 
> 1. in the diffuse branch `max ell_j<=3/4`, convert the already-proved full-law bound `H_(1/2)(Q)<265.625` into an `L^infinity` density bound by a source-valid third smoothing mechanism; or
> 2. in the concentrated branch, spend the literal physical `>3/4` two-volume-coloop through a completed physical hub/pair, grouped-square, projected-crossing, ridge, `E_3`, or `E_5` receiver.

A proof that only manipulates the abbreviated rank-six carrier conditions and forgets (4.1) is no longer considered a faithful narrowing, by Proposition 3.1.

The likely next mechanism is **aggregate-before-inversion**: in the diffuse branch combine the `D_2` half-potential with a genuinely independent physical square/pair packet; in the coloop branch keep the whole incident two-volume (5.7) until the third source-valid direction is identified. A return to one-good-minor selection would throw away the new quantitative information.

## 8. Target status

No target-valid counterexample was found. The full QFORM conjecture remains **OPEN**. No continuity upgrade is claimed. The report preserves all target quantifiers and every live correction listed in Section 1.
