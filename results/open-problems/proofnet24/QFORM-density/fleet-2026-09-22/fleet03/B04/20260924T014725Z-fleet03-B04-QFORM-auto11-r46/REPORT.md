SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T01:47:25Z.
attacking: retain a high fourth-volume carrier as a literal Fourier hub, downshift its anchored E4 packet to projected E3 entropy currency, and remove the row-norm loss in the live high-carrier branch.

# fleet03/B04 r46 — anchored E4 carrier paid by hub-retaining product Fourier

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Status: **NEW SUPPORTING THEOREM / LIVE HIGH-CARRIER BRANCH STRENGTHENED / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Continuity in the new branch: **proved (`C_0`)**. Full-target continuity remains OPEN.

The full universal conjecture is not proved here. The new point is that a physical row carrying fourth exterior volume should sometimes be kept as the one-dimensional Fourier hub rather than deleted. The carrier amplitude then cancels against the projected three-volume scaling at the critical `q=1` exponent, producing a scale-correct anchored E4 currency with no reciprocal local minor and no row-norm loss.

## 1. Fresh source boundary and checked dependencies


The analytic inputs are all source-pinned completed supporting results:

1. `QFORM-ARBITRARY-WEIGHT-PROJECTED-CROSSING-v1`, fleet03/B04 r37:
   `yspennstate/math-open-problems@ea2f45957db06473799ce27affa30162fda98982`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T165007Z-fleet03-B04-auto11-r37/REPORT.md`.
   In grouped-hub notation, for a feasible `ell`-minor law with row marginals at most `1/2`, determinant/marginal currency `Gamma`, `d=k+ell>2`, hub density cap `M_H`, hub-cross singular product `S`, it gives
   
   `||p_Q||inf <= [d/(d-2)] 2^((k+3ell)/(2d)) M_H^(1/d) S^(-1/d) Gamma^(-1/(2d))`,
   
   with `phi_Q in L1` and hence a continuous `C_0` density. Arbitrary same-bank curvature, outside couplings and induced affine terms are retained.

2. `QFORM-FIXED-CARDINALITY-ENTROPY-v1`, fleet03/B04 r39:
   `yspennstate/math-open-problems@04f0b30d5f729ed26d9f8c2cb1354973c587c3cc`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T185112Z-fleet03-B04-auto11-r39/REPORT.md`.
   For a probability law on `ell`-subsets with inclusion marginals `alpha_i`,
   
   `H(w)+sum_i alpha_i log alpha_i <= log(ell^ell/ell!)`.

3. `QFORM-CANONICAL-E4-PAIR-TO-DENSITY-v1`, fleet03/B04 r45:
   `yspennstate/math-open-problems@02558c47299849273ed5f8fd6105763fc1e2d618`,
   same-slot r45 report. For canonical E4 pair mass `eta_ij`,
   
   `||p_Q||inf <= C4 [eta_ij E4(M)]^(-1/8)`,
   `C4=2 sqrt(2)e^(1/4)3^(3/4)=8.278650626819047...`,
   
   with continuous `C_0` density.

4. Designated partner fleet04/B04 r2, `QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1`:
   `yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.
   It constructs the exact anchored E4 face law and gives an entropy-payment / double-anchor dichotomy at a high carrier.

## 2. Anchored fourth-volume geometry as a projected third-volume law

Let `I,J` be disjoint ORIGINAL-coordinate banks and let

`M=A[I,J]`

with physical row vectors `m_a`. Fix a literal row `i in I` and assume its anchored fourth-volume mass

`H_i := sum_{R subset I, |R|=4, i in R} det(M[R,:]M[R,:]^T)`

is positive. Then `m_i != 0`. Put

`s=||m_i||_2`,
`P_i = orthogonal projection onto span(m_i)`,
`C = M[I\{i},J](I-P_i)`.

For every physical residual triple `S subset I\{i}`, the Gram height identity gives the exact equality

`d_{i,S}:=det Gram(m_i,(m_a)_{a in S})
        = s^2 det(C_S C_S^T).`                                  (2.1)

Consequently

`Z_3(C):=e_3(CC^T)=H_i/s^2`.                                   (2.2)

Let

`mu_i(S)=d_{i,S}/H_i`                                           (2.3)

on the supported residual triples. This is exactly the canonical projected third-volume law of `C`, because by (2.1)

`mu_i(S)=det(C_S C_S^T)/Z_3(C)`.                               (2.4)

It is also exactly the designated partner's anchored E4 face law. Let

`beta_a=P_{mu_i}(a in S)`.                                      (2.5)

Define the projected determinant/marginal currency

`Gamma_i := exp( sum_S mu_i(S) log det(C_S C_S^T)
                 -sum_a beta_a log beta_a )`.                   (2.6)

The scale-correct anchored fourth-volume entropy currency is

`Omega_i := s^2 Gamma_i
          = exp( sum_S mu_i(S) log d_{i,S}
                 -sum_a beta_a log beta_a ).`                   (2.7)

Thus `Omega_i` can be read directly from the anchored E4 packet; the projected row norm `s` disappears from its definition.

## 3. Main theorem — `QFORM-ANCHORED-E4-HUB-FOURIER-v1`

### Theorem 3.1

Assume the setup of Section 2 and

`beta_*:=max_a beta_a <= 1/2`.                                  (3.1)

Then the full ambient quadratic-plus-affine form, for arbitrary independent cap-one input laws, arbitrary same-bank quadratic curvature, all outside couplings and arbitrary signs, has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||infinity <= 2^(9/4) Omega_i^(-1/8).`                    (3.2)

Moreover

`boxed:
 Omega_i >= (2/9) H_i,`                                         (3.3)

and therefore

`boxed:
 ||p_Q||infinity
 <= 2^(17/8) 3^(1/4) H_i^(-1/8)
 = 5.740755551537958... H_i^(-1/8).`                             (3.4)

### Proof

Keep the literal original coordinate `X_i` as the one-dimensional grouped hub. Its one-dimensional density cap is at most one, so `M_H<=1`. Its coefficient row into the right bank is `m_i`, hence the hub-cross singular product in the grouped theorem is exactly

`S=s=||m_i||_2`.                                                (3.5)

After projecting the residual crossing rows away from `span(m_i)`, the projected matrix is precisely `C` in Section 2. Take `k=1`, `ell=3`, so `d=4`. The law `mu_i` is the canonical three-volume law of `C` and (3.1) is exactly the marginal hypothesis of the arbitrary-weight projected-crossing theorem. Therefore r37 gives

`||p_Q||infinity
 <= [4/(4-2)] 2^((1+9)/8) s^(-1/4) Gamma_i^(-1/8)
 = 2^(9/4) (s^2 Gamma_i)^(-1/8)
 = 2^(9/4) Omega_i^(-1/8)`.                                    (3.6)

The source theorem gives an integrable characteristic-function envelope, so the density is continuous and belongs to `C_0`.

For (3.3), since `mu_i` is canonical with determinant weights `D_S=det(C_SC_S^T)` and total `Z_3=H_i/s^2`,

`Gamma_i = Z_3 exp[-H(mu_i)-sum_a beta_a log beta_a].`          (3.7)

Apply the sharp fixed-cardinality entropy inequality at `ell=3`:

`H(mu_i)+sum_a beta_a log beta_a <= log(3^3/3!)=log(9/2)`.      (3.8)

Hence `Gamma_i >= (2/9)Z_3`. Multiplying by `s^2` and using (2.2) gives `Omega_i >=(2/9)H_i`. Substitution in (3.2) yields (3.4). QED.

The cancellation in (3.6) is the substantive point: deleting the carrier, as in a pure face-downshift, loses its strength. Retaining it as the Fourier hub turns `s^(-1/4) Gamma_i^(-1/8)` into the homogeneous E4 quantity `Omega_i^(-1/8)`.

## 4. Uniform live high-carrier theorem — `QFORM-HIGH-E4-CARRIER-HUB-OR-PAIR-v1`

Let `pi` be the canonical E4 row law of `M` and

`rho_i=P_pi(i in R)=H_i/E4(M)`.                                 (4.1)

Suppose `rho_i>=r>0`. Then the entire high-carrier state is paid without any row-norm factor:

- If `beta_*<=1/2`, Theorem 3.1 and `H_i>=r E4(M)` give
  
  `||p_Q||infinity
   <= 2^(17/8)3^(1/4) r^(-1/8) E4(M)^(-1/8).`                   (4.2)

- If `beta_*>1/2`, choose `j` with `beta_j>1/2`. The exact conditional identity from the partner face law gives
  
  `eta_ij=P_pi(i,j in R)=rho_i beta_j > r/2`.                   (4.3)
  
  The completed r45 fixed-pair theorem then gives
  
  `||p_Q||infinity
   < C4 (r/2)^(-1/8) E4(M)^(-1/8).`                             (4.4)

Both branches have continuous `C_0` densities.

At the designated partner's live carrier threshold `rho_i>1/25`, the two front constants are

`2^(17/8)3^(1/4)25^(1/8)=8.58443181728124...`,                  (4.5)

and

`C4 50^(1/8)=13.499907897578499...`.                            (4.6)

Thus the whole high-carrier state satisfies the clean row-norm-free estimate

`boxed:
 rho_i>1/25
 => ||p_Q||infinity
    <13.500 E4(M)^(-1/8),`                                      (4.7)

with a continuous `C_0` density.

This strictly strengthens the shape of the designated partner r2 conclusion on the live high-carrier gate: its entropy branch contained `||m_i||` through `(rho_i E4/||m_i||^2)^(-1/6)`, whereas (4.7) depends only on aggregate E4 currency. The price is only a harmless change of the conditional split from `2/3` to `1/2`; the upper branch is already paid by the fixed-pair theorem.

## 5. Designated partner applied at an actual inequality

To make the comparison equation-level rather than verbal, use the explicit family in Section 6 below at `epsilon=1/16`. For its hub row `i=0`, the partner's exact anchored law has

`beta_*=129/259<1/2`,
`H_i=259`,
`||m_i||^2=256`,
`G_i=H_i/||m_i||^2=259/256`.                                   (5.1)

(The equality in the last line is exact because every residual row is orthogonal to the hub, so the partner's geometric height is identically `256`.) Its completed q=1 entropy theorem therefore gives the actual inequality

`boxed:
 ||p_Q||infinity
 <=3e (259/256)^(-1/6)
 =8.13902601868726... .`                                       (5.2)

The new hub-retaining theorem on the identical matrix gives the exact stronger bound

`||p_Q||infinity <=2.378720371807186...`                        (5.3)

computed below. Thus the designated partner result has been applied at an actual inequality and the quantitative gain is directly attributable to retaining the carrier amplitude instead of deleting it.

## 6. Genuinely rotated indefinite rank-five stress family

Let `w_0,...,w_4` be five distinct normalized rows of the Sylvester Hadamard matrix `H_8/sqrt(8)`. They are orthonormal and every coordinate is nonzero. For `0<epsilon<=1/16`, define the physical `9 x 8` cross block `M_epsilon` with rows

- `16 w_0`;
- two copies of `w_1/sqrt(2)`;
- two copies of `w_2/sqrt(2)`;
- two copies of `w_3/sqrt(2)`;
- two copies of `epsilon w_4/sqrt(2)`.

Every entry of `M_epsilon` is nonzero. Set

`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`.                    (6.1)

The singular values of `M_epsilon` are exactly

`16,1,1,1,epsilon`.                                             (6.2)

Hence

`spec_nonzero(A_epsilon)
 ={+-16,+-1,+-1,+-1,+-epsilon}`,                                (6.3)

so the matrix is indefinite, non-diagonal in the independent coordinates, and has eight eigenvalues of modulus at least one for every `epsilon>0`. Its active right singular directions are dense Hadamard mixtures, so no spectral-coordinate independence is used.

Take the hub row `i=0`. Its anchored fourth-volume mass is

`H_0=16^2 e_3(1,1,1,epsilon^2)
    =256(1+3epsilon^2).`                                       (6.4)

Conditioned on containing the hub, a supported residual triple chooses three of the four residual directions. Each strong physical row has marginal

`beta_strong=(1+2epsilon^2)/[2(1+3epsilon^2)]<1/2`,             (6.5)

and each weak physical row has

`beta_weak=3epsilon^2/[2(1+3epsilon^2)]<1/2`.                  (6.6)

Thus Theorem 3.1 applies uniformly as `epsilon->0`, even though the fifth singular direction vanishes. Its coarse consequence is already

`||p_Q||infinity
 <= 5.740755551537958 [256(1+3epsilon^2)]^(-1/8)
 <2.870378`,                                                     (6.7)

continuous `C_0`, uniformly for `0<epsilon<=1/16`.

At the concrete value `epsilon=1/16`, exact enumeration gives

`Z_3(C)=259/256`,
`H_0=259`,
`E4(M)=66305/256`,
`rho_0=66304/66305`,                                            (6.8)

six strong residual physical rows with marginal `129/259` and two weak rows with marginal `3/518`. The exact projected entropy currency is

`Gamma_0=0.9989708620178627...`,
`Omega_0=256 Gamma_0=255.73654067657284...`.                    (6.9)

Therefore

`boxed:
 ||p_{X^T A_(1/16) X}||infinity
 <=2^(9/4) Omega_0^(-1/8)
 =2.378720371807186... .`                                      (6.10)

For comparison, the strongest hub-plus-one-strong-row canonical pair has total anchored fourth-volume `129`; r45 therefore gives

`||p_Q||infinity <= C4 129^(-1/8)
 =4.509577357402878...`,                                        (6.11)

while the designated partner deletion inequality is (5.2), `8.139026...`. The hub-retaining rearrangement is strictly stronger than both on the same target-valid matrix.

No Monte Carlo argument enters any assertion above.

## 7. Quantifier audit and remaining debt

Theorem 3.1 is valid for arbitrary dimension, arbitrary independent one-dimensional probability densities bounded by one, arbitrary fragmented/unbounded supports, arbitrary signs, arbitrary same-bank quadratic curvature, all outside couplings and induced affine terms. It rotates coefficient vectors only inside deterministic linear algebra; it never declares rotated random coordinates independent. Continuity is proved in this branch through an `L^1` characteristic-function envelope.

Its extra hypothesis is an anchored E4 packet whose conditional projected triple marginals are at most `1/2`. Theorem 4.1 removes that conditional restriction once a carrier has a universal lower E4 leverage, by routing the complementary case to the already-paid fixed-pair endpoint.

The full conjecture remains OPEN because the bare three-large-eigenvalue hypothesis does not yet force a literal original-coordinate cross block with target-scale `E4` and a carrier `rho_i>c`, nor does it force this particular E4 mechanism instead of the current low-rank/star/ridge alternatives.

The next B04 implication is therefore:

`QFORM-E4-CARRIER-OR-E3-COLLISION-ROUTING-v1` — in the surviving global structural packets, either force a literal cross block with target-scale fourth exterior volume and one carrier of universal canonical leverage (now completely paid by (4.7)), or route failure into the completed cross-E3 collision, aligned-rank-two star, ridge, pair-log, square-bank or grouped-hub receivers without deleting a nonzero tail or inverting a vanishing local coefficient.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN` (not exposed in fresh fleet03 inventory). Provider reasoning-token/thinking-time counters: `NOT_EXPOSED`. Repository access/writeback occurred; native authenticated brain receiver use was not observed, so status remains `WITHOUT_VERIFIED_BRAIN`.
