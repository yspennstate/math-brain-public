SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T04:18:14Z.
attacking: pair-anchored fourth-volume -> row-marginal-free product-Fourier receiver, then spend fleet04/B04's completed double-anchor packet.

# fleet03/B04 r48 — pair-anchored E4 promotion hierarchy

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Status: **QUANTITATIVE SHARPENING / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution status: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target is not proved here. This run sharpens the earlier fixed-pair fourth-volume receiver by retaining the literal physical pair as a Fourier hub and promoting any heavy residual rows rather than paying a generic fixed-pair constant. The proof stays in original coordinates, retains arbitrary same-bank curvature, affine terms and extra spectrum, and never uses law-uniform pointwise quadratic-phase decay or independence after a random-variable rotation.

## 1. Fresh controls and exact dependencies

Fresh owner control was resolved from `yspennstate/math-research-brain/main`; the prepublication refresh used commit

`ceea86b4db08435ab86f553e346d3d2d6168c4a0`,


`a884b835aba929c5376e6417ae5cfcd44c0f7a76`.

The main analytic input is the independently checked grouped projected-crossing theorem at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For literal original-coordinate hubs, it retains arbitrary internal hub functions and arbitrary same-bank light curvature. If `k` literal hub directions have right-bank singular-value product `S`, the residual projected crossing has `ell`-volume `Z_ell`, its canonical row marginals are at most `1/2`, and `d=k+ell>2`, then the characteristic function has an integrable `|t|^{-d/2}` envelope and

`||p_Q||_infinity
 <= d/(d-2) 2^((k+3ell)/(2d)) E_ent^(1/d)
      M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,                    (1.1)

where `E_ent` is the square root of the weighted-subset entropy factor. In the notation of that proof the exact entropy contribution before the final `1/d` power is

`exp{[H(w)+sum_i alpha_i log alpha_i]/2}`.                     (1.2)

For a law on two-subsets, uniformly order the sampled set as `(I_1,I_2)`. Then

`H(I_1,I_2)=H(w)+log 2`,

both ordered coordinates have law `alpha_i/2`, and entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= log 2`.                      (1.3)

Thus at `ell=2` the generic `exp(ell/2)` loss in the source theorem may be replaced by `sqrt(2)` in its weighted-subset estimate, or by `2^(1/(2d))` in the final density coefficient.

The designated-partner input is fleet04/B04 r2,

`QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1`,

at

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

In its high fourth-volume carrier state, failure of its anchored entropy gate produces a literal physical row pair with canonical fourth-volume pair mass `>2/75`.

For comparison, fleet03/B04 r45 already proved a generic fixed-pair receiver with coefficient `8.2786506268...`; the theorem below has the same pair-anchored input currency but improves its front coefficient to `2^(17/8)=4.3620309307...` by a physical promotion hierarchy. Fleet03/B04 r47 gives the generic global `E4` downshift coefficient `7.6590945236...`.

## 2. Exact pair-anchored factorization

Let `I,J` be disjoint sets of original coordinates and let

`M=A[I,J]`.

Write the physical rows of `M` as `m_r`. Fix distinct rows `a,b in I` and define the pair-anchored fourth-volume mass

`H_ab
 := sum_{R subset I, |R|=4, {a,b} subset R}
       det Gram(m_r : r in R)`.                                 (2.1)

Assume `H_ab>0`. Then `m_a,m_b` are linearly independent. Put

`D_2=det Gram(m_a,m_b)>0`,                                      (2.2)

let `P_2` denote orthogonal projection onto `span(m_a,m_b)`, and for every `r in I\{a,b}` set

`c_r=m_r(I-P_2)`.

Let `C` be the matrix with rows `c_r`. The Schur/Gram determinant identity gives, for every residual pair `{r,s}`,

`det Gram(m_a,m_b,m_r,m_s)
 = D_2 det Gram(c_r,c_s)`.                                      (2.3)

Summing (2.3),

`boxed: H_ab = D_2 E_2(C),`                                    (2.4)

where `E_2(C)=e_2(CC^T)`.

This identity is the key cancellation: the product-Fourier receiver pays `D_2` and the residual second compound with exactly the exponents needed to recombine into the aggregate `H_ab` before taking any reciprocal.

## 3. Main theorem — `QFORM-PAIR-ANCHORED-E4-PROMOTION-v1`

### Theorem

Let `X_1,...,X_n` be independent real random variables with probability densities at most one. Let

`Q=X^TAX+b^TX+c`

with arbitrary real symmetric `A` and arbitrary affine terms. Let `I,J` be disjoint original-coordinate banks, set `M=A[I,J]`, and fix `a!=b` in `I`. If the aggregate `H_ab` in (2.1) is positive, then `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity <= 2^(17/8) H_ab^(-1/8).`                    (3.1)

Numerically,

`2^(17/8)=4.362030930661031...`.                                (3.2)

Equivalently, if `E_4(M)>0` and the canonical fourth-volume law has pair inclusion probability

`eta_ab=H_ab/E_4(M)`,                                           (3.3)

then

`boxed:
 ||p_Q||_infinity
 <=2^(17/8) eta_ab^(-1/8) E_4(M)^(-1/8).`                      (3.4)

### Proof

Condition all original coordinates outside `I union J`. This creates arbitrary affine terms in the surviving variables but preserves independence and the density cap on the surviving original coordinates. All estimates below are uniform in the conditioned values, so the same characteristic-function envelopes survive after averaging back.

**Case A: the residual `E_2(C)` law is diffuse.**

Let `w_{rs}=det Gram(c_r,c_s)/E_2(C)` and `alpha_r=sum_{s}w_{rs}`. Suppose every `alpha_r<=1/2`. Use the literal original coordinates `X_a,X_b` as the hub. Their joint density is the product of two one-dimensional cap-one densities, so `M_H<=1`. The hub-to-right-bank matrix has row Gram determinant `D_2`; therefore its singular-value product is

`S=sqrt(D_2)`.                                                  (3.5)

The projected light crossing is exactly `C`, so `Z_2=E_2(C)`. Apply the grouped projected-crossing proof with `(k,ell,d)=(2,2,4)` and replace its generic entropy loss by (1.3). The density coefficient is

`[d/(d-2)] 2^((k+3ell)/(2d)) 2^(1/(2d))
 =2 * 2^1 * 2^(1/8)=2^(17/8)`.                                 (3.6)

The geometric factor is

`S^(-1/4) Z_2^(-1/8)
 =D_2^(-1/8)E_2(C)^(-1/8)
 =H_ab^(-1/8)`                                                  (3.7)

by (2.4). This proves (3.1) in Case A.

**Case B: one residual row is heavy.**

Suppose some residual row `c` has `alpha_c>1/2`. Promote the literal original coordinate `c` into the hub. Put

`D_3=det Gram(m_a,m_b,m_c)>0`,                                  (3.8)

project every remaining row orthogonally off `span(m_a,m_b,m_c)`, and call the resulting residual matrix `C_3`. Define the triple-anchored fourth-volume mass

`H_abc
 :=sum_{r notin {a,b,c}}
 det Gram(m_a,m_b,m_c,m_r)`.                                   (3.9)

The same Gram-Schur identity gives

`H_abc=D_3 E_1(C_3)`.                                           (3.10)

Moreover the definition of the `E_2(C)` marginal gives exactly

`H_abc=alpha_c H_ab > H_ab/2`.                                 (3.11)

If every row marginal of the canonical `E_1(C_3)` law is at most `1/2`, apply the grouped theorem with `(k,ell,d)=(3,1,4)`. The `ell=1` entropy factor cancels exactly. Hence

`||p_Q||_infinity
 <=2^(7/4) H_abc^(-1/8)
 <2^(15/8) H_ab^(-1/8)`,                                       (3.12)

and `2^(15/8)=3.668016172818685...<2^(17/8)`.

**Case C: the promoted residual also has a heavy row.**

For `ell=1`, a row marginal is simply its normalized squared residual row length. If some remaining row `d` has marginal `>1/2`, then

`D_4:=det Gram(m_a,m_b,m_c,m_d)
 > H_abc/2 > H_ab/4`.                                           (3.13)

Condition all other left-bank variables. The four literal original coordinates `a,b,c,d` form one side of an exact-rank-four crossing to the right bank. Their four-dimensional density cap is at most one. The right rank-four orthogonal projection has density cap at most `2^(4/2)=4`. The exact-rank-four crossing theorem therefore gives

`||p_Q||_infinity
 <=2 (4/sqrt(D_4))^(1/4)
 =2^(3/2)D_4^(-1/8)
 <2^(7/4)H_ab^(-1/8)`,                                         (3.14)

again strictly smaller than the Case-A coefficient.

The three cases are exhaustive. Each branch supplies a uniform integrable characteristic-function envelope (`|t|^{-2}` at the final effective dimension four), so after undoing the initial conditioning the full ambient characteristic function is still in `L^1`. Fourier inversion yields a continuous `C_0` density. QED.

### Why this respects the live corrections

No eigenbasis coordinates are treated as independent. The only promoted variables are literal original coordinates. No law-uniform pointwise quadratic Fresnel decay is used; the decay comes from product-space Plancherel/weighted Fourier estimates after physical conditioning. No single vanishing determinant is inverted: the reciprocal is taken only after the pair-anchored aggregate `H_ab` is formed, and heavy marginals are promoted to larger physical hubs.

## 4. Designated partner applied at an actual inequality

Fleet04/B04 r2 proves that in its live high-carrier branch, failure of its anchored entropy gate produces a literal pair `{a,b}` with

`eta_ab=P_pi(a,b in R)>2/75`.                                  (4.1)

Therefore

`H_ab=eta_ab E_4(M)>(2/75)E_4(M)`.                             (4.2)

Apply (3.4):

`||p_Q||_infinity
 <2^(17/8)(75/2)^(1/8)E_4(M)^(-1/8)`                           (4.3)

and the coefficient simplifies exactly to

`boxed:
 ||p_Q||_infinity
 <4*75^(1/8) E_4(M)^(-1/8)
 =6.861872579851902... E_4(M)^(-1/8).`                          (4.4)

This is an equation-level use of the completed designated partner result. It improves the prior r45 generic pair-payment coefficient `13.0230726552...` on the same `eta_ab>2/75` state and also improves the r47 generic `E4` downshift coefficient `7.6590945236...` whenever this partner pair concentration is available. The branch has a continuous `C_0` density.

## 5. Genuinely rotated indefinite stress test

Let `H_8` be the Sylvester Hadamard matrix and put

`U=H_8/sqrt(8)`.

Let

`D=diag(1,1,1,1,1/16,1/16,1/16,1/16)`,

and define the dense `8x8` cross block

`M_*=D U`.                                                       (5.1)

Every entry of `M_*` is nonzero. Its singular values are

`1,1,1,1,1/16,1/16,1/16,1/16`.                                (5.2)

Define the symmetric `16x16` matrix

`A_*=[[0,M_*],[M_*^T,0]]`.                                      (5.3)

Its nonzero spectrum is the signed singular spectrum of `M_*`, so it contains

`+1` four times and `-1` four times, as well as `+/-1/16` four times each in total. Thus eight eigenvalues have modulus at least one. The form is dense across the two physical banks, non-diagonal in the independent coordinates, and indefinite.

The physical rows of `M_*` are orthogonal. Their squared norms are

`x=(1,1,1,1,1/256,1/256,1/256,1/256)`.                         (5.4)

For the first two rows,

`H_12=e_2(1,1,1/256,1/256,1/256,1/256)
     =33795/32768
     =1.031341552734375`.                                       (5.5)

Hence the new theorem gives, for every admissible independent cap-one product input,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=4.345236573574204... .`                                      (5.6)

The density is continuous and vanishes at infinity.

For comparison on this identical matrix,

`E_3(M_*)=17171969/4194304=4.094116449356079...`,                (5.7)

so the direct marginal-free `E3` receiver gives `6.683212357679818...`; and

`E_4(M_*)=4565766145/4294967296=1.063050270313397...`,           (5.8)

so the r47 fourth-compound downshift gives `7.600780730452431...`. The generic exact-rank-eight crossing theorem, using the whole two-bank block, gives `16/3=5.333333333333333...`. Thus (5.6) is a strict improvement over all three generic certificates on this explicit genuinely rotated indefinite form.

The committed checker verifies the Hadamard orthogonality, exact fractions in (5.5)-(5.8), the promotion constants, the partner coefficient, and the strict comparison chain. No Monte Carlo evidence is used.

## 6. Scope and next obligation

This theorem does not solve the structural implication from three large eigenvalues to a target-scale pair-anchored fourth-volume packet. It is best viewed as an overlap receiver: once two literal physical rows carry a quantified aggregate fourth-volume packet, all row-marginal obstructions can be removed by literal physical promotion while keeping a universal aggregate reciprocal cost.

The full QFORM conjecture remains **OPEN**, and full-target continuity remains **OPEN** separately. The next B04 step is therefore

`QFORM-C2-OVERLAP-TO-PAIR-HUB-OR-CROSS-E3-v1`:

start from the physical `C2` overlap class in the third-compound decomposition and prove that target-scale two-row overlap mass either creates a pair-anchored packet of the form `H_ab` above or yields a target-scale literal cross `E3`; route the complementary heavy-coloop state into the existing star/ridge/square-bank receivers. The objective is to connect the bare three-large-eigenvalue hypothesis to an already-paid product-preserving endpoint, not to produce another subclass theorem.

No scheduler state, task identity, cadence, email/push notification, repository visibility, paid model/API call, remote workflow, or cross-account authentication was changed in this run. Model self-report is `GPT-5.6 Sol`; configured reasoning effort and provider thinking counters were not exposed.
