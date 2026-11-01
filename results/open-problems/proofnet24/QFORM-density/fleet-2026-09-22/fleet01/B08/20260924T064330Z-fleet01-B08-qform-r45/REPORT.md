SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-24T06:43:30.704219Z.
attacking: the global diffuse third-exterior-power branch — stop duplicating the already-proved Pluecker overlap ledger and use the newer marginal-free physical crossing receiver to close its entire disjoint packet.

# fleet01/B08 r45 — marginal-free closure of the diffuse disjoint Pluecker packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW END-TO-END DIFFUSE BRANCH PAYMENT + SHARPER OVERLAP-ONLY SURVIVOR / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Full-target continuity remains OPEN. This report gives a continuous density on the newly paid diffuse branch. It uses only original-coordinate physical cuts for probability arguments. No random-variable rotation, moment assumption, compact support, log-concavity, pointwise quadratic-phase decay, arbitrary-joint coarea, fiber supremum, or deletion of a complementary spectral tail is used.

## 1. Fresh source state and a deliberate change of mechanism


I changed mechanism from the preceding deletion/star/alignment runs r36--r44 to the third exterior power of the actual full matrix.

A source search found that the structural calculation I initially started to derive is already proved in fleet03/B08 r25, `QFORM-DIFFUSE-PLUECKER-OVERLAP-LEDGER-v1`, at the immutable source snapshot

`yspennstate/math-open-problems@3ca6f8113ff32fc642cc3582b4a338082e8d6d25`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T002108Z-fleet03-B08-qform-diffuse-r25/REPORT.md`.

I therefore stop duplicate work on that exact scope and use it as an input. The new step is that fleet03/B08 r25 predated the current marginal-free third-compound crossing theorem and could pay its disjoint packet only behind an additional cross-range leverage condition. This report removes that condition completely by applying the designated partner fleet02/B08 r34 to an actual random physical half-cut.

The designated partner input is fleet02/B08 r34, canonical source

`yspennstate/math-open-problems@3452feca9a3efbb5a716eb7453be7ae0433e463f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/fleet02-B08-20260924T053906Z-r34/REPORT.md`.

The only analytic fact imported from it is its completed marginal-free literal-crossing theorem: for any physical original-coordinate cross block `B=A[S,T]`,

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)`,                  (1.1)

whenever `e_3(BB^T)>0`; arbitrary same-side quadratic blocks, affine terms, outside couplings, signs, and extra spectrum remain present, and the resulting density is continuous and vanishes at infinity.

## 2. Existing diffuse Pluecker ledger, stated at the exact strength needed

Let `R` be an `n x 3` matrix with orthonormal columns consisting of genuine eigenvectors of `A`,

`AR=R Lambda`,
`Lambda=diag(lambda_1,lambda_2,lambda_3)`,
`min_j |lambda_j| >= L>0`.                                      (2.1)

Put

`ell_i=||R_{i,*}||_2^2`, `mu=max_i ell_i`,                       (2.2)

and assume the diffuse gate

`mu<=1/48`.                                                       (2.3)

For physical three-sets `I,J`, put

`M_{I,J}=det A[I,J]`,                                             (2.4)

and define the overlap energies

`E_q(A)=sum_{|I|=|J|=3, |I cap J|=q} M_{I,J}^2`, `q=0,1,2,3`.   (2.5)

Fleet03/B08 r25 proves, with `lambda_* = lambda_1 lambda_2 lambda_3`,

`sqrt(E_0(A)) + sqrt(3 mu (E_1+E_2+E_3)) >= |lambda_*|`.          (2.6)

For completeness, the mechanism is exact and tail-free: if `u_I=det R_I`, then `sum_I u_I^2=1`, `sum_{I contains i}u_I^2=ell_i`, two independent Pluecker triples intersect with probability at most `sum_i ell_i^2<=3mu`, and `u` is an eigenvector of `wedge^3 A` with eigenvalue `lambda_*`.

Using the split `3/4+1/4=1`, (2.6) implies the exhaustive alternative

`E_0(A) >= (9/16)|lambda_*|^2`                                   (2.7)

or

`E_1(A)+E_2(A)+E_3(A) > |lambda_*|^2/(48mu)`.                    (2.8)

The point of this report is to close (2.7) with no further leverage hypothesis.

## 3. Main new theorem: the entire disjoint diffuse packet is paid

### Theorem 3.1 — `QFORM-DIFFUSE-PLUECKER-DISJOINT-CLOSED-v1`

Under (2.1)--(2.3), if

`E_0(A) >= (9/16)|lambda_*|^2`,                                  (3.1)

then for every admissible independent product law,

`boxed: ||p_Q||_infinity <= 24 |lambda_*|^(-1/3) <= 24/L`,       (3.2)

and `p_Q` has a continuous `C_0(R)` representative.

#### Proof

Choose a random physical Bernoulli half-cut `[n]=S disjoint_union T`, each original coordinate independently assigned to `S` or `T` with probability `1/2`. Define the literal physical crossing third compound

`Z(S,T):=e_3(A[S,T]A[S,T]^T)
       =sum_{I subset S, J subset T, |I|=|J|=3} det A[I,J]^2`.   (3.3)

For every ordered pair of disjoint physical triples `(I,J)`, the event `I subset S` and `J subset T` uses six distinct original coordinates and therefore has probability exactly `2^(-6)=1/64`. Consequently

`E_cut Z(S,T)=E_0(A)/64
              >=9 |lambda_*|^2/1024`.                            (3.4)

Hence some actual deterministic original-coordinate cut satisfies

`Z(S,T)>=9 |lambda_*|^2/1024`.                                   (3.5)

Apply the completed designated-partner theorem (1.1) to this **actual** block `B=A[S,T]`. It gives

`||p_Q||_infinity
 <=6^(4/3) (9 |lambda_*|^2/1024)^(-1/6)
 =24 |lambda_*|^(-1/3)
 <=24/L`.                                                         (3.6)

The algebraic simplification is exact:

`6^(4/3)(1024/9)^(1/6)=24`.                                      (3.7)

The partner theorem retains every same-side entry of `A`, every outside coupling and every additional spectral direction, so no complementary spectrum has been dropped. Its Fourier envelope is integrable, which supplies the asserted `C_0` density. QED.

This is the requested completed-partner application at a concrete inequality: fleet02/B08 r34 is invoked at the physical crossing threshold (3.5), not merely cited abstractly.

## 4. Corollary: an unpaid diffuse three-frame has overlap energy at unit scale

Combining Theorem 3.1 with the alternative (2.7)--(2.8) yields the following sharper diffuse router.

### Corollary 4.1 — `QFORM-DIFFUSE-OVERLAP-ONLY-ROUTER-v1`

Assume (2.1)--(2.3). Then either

`boxed: ||p_Q||_infinity <=24/L,  p_Q in C_0(R)`,                 (4.1)

or

`boxed: E_1(A)+E_2(A)+E_3(A) > |lambda_*|^2/(48mu) >= L^6`.      (4.2)

Therefore some overlap multiplicity `q in {1,2,3}` satisfies

`boxed: E_q(A) > L^6/3`.                                         (4.3)

Thus, after the newest marginal-free crossing receiver is inserted, **the disjoint Pluecker packet is no longer an obstruction at all**. Every unpaid selected-three diffuse state must place macroscopic third-compound energy on physical triple pairs that share at least one original coordinate.

This is a strict strengthening of the r25 state. R25 still had a q=0 analytic branch whose payment required a one-side range-leverage gate; (4.1) removes that gate entirely.

## 5. Product-preserving finite-bank form of the remaining overlap debt

Fleet03/B08 r25 already combines its overlap ledger with the completed B07 coloring theorem. Since the q=0 branch is now fully paid, every unpaid state under (2.1)--(2.3) admits one of only the following three original-coordinate packets:

1. `q=1`: five pairwise-disjoint banks `H,R1,R2,C1,C2`, with shared physical hub bank `H` and squared determinant packet

   `P_1 > 4 L^6/9375`;                                           (5.1)

2. `q=2`: four pairwise-disjoint banks `H1,H2,R,C`, with a shared physical pair of hub banks and

   `P_2 > L^6/384`;                                              (5.2)

3. `q=3`: three pairwise-disjoint banks `H1,H2,H3`, carrying a physical-principal triple packet

   `P_3 > 2 L^6/27`.                                             (5.3)

These are aggregate squared-determinant statements. They do **not** imply one uniformly good physical minor and I make no such inference. The banks are sets of original independent coordinates, so subsequent conditioning/grouping may legitimately use their product structure.

The smallest guaranteed packet among the three survivors is

`4/9375 = 0.000426666666666...`.                                  (5.4)

## 6. Why this is useful relative to r44

R44 had reduced a thin-child deletion branch to sixteen independent star banks plus a rank-two physical crossing tube. The present run is a different, global route: it never deletes a coordinate and never assumes the fourth or later singular/eigenvalue directions are small. It says that whenever the selected three genuine eigenvectors themselves are diffuse, all arbitrary complementary spectrum is already absorbed into one of two outcomes:

- a literal rank-three physical cross-volume payment with the clean universal constant `24/L`; or
- macroscopic **overlapping** third-compound curvature in the actual full matrix.

This makes overlap, rather than small spectral tail or star alignment, the first global structural obstruction in the diffuse selected-three chamber.

## 7. First unpaid implication

The next B08 target is

`QFORM-DIFFUSE-OVERLAP-PACKET-COMPILER-v1`:

> Starting from one of the q=1,2,3 product-preserving packets (5.1)--(5.3), prove a universal density receiver or force a valid localized-coordinate conditioning certificate, while aggregating before reciprocal minor selection and retaining every same-bank quadratic term, complementary spectral direction and induced affine term.

The natural case split is now physically meaningful: q=1 is a shared-coordinate hub with two disjoint two-wings, q=2 is a shared physical pair with one row and one column wing, and q=3 is principal-triple aggregate curvature. Existing scalar/pair receivers may be used only after their hypotheses are actually forced; aggregate mass alone is not one good minor.

## 8. Correction audit and scope

- General rotations of the random vector are never used. `R` and `wedge^3 R` are deterministic coefficient objects only.
- The random half-cut partitions original independent coordinates.
- The theorem uses a completed marginal-free physical-crossing result, not a bounded-density projection shortcut.
- No pointwise van-der-Corput estimate is invoked.
- No Monte Carlo result enters the proof.
- Repeated eigenvalues cause no degeneracy: any selected orthonormal genuine eigenframe satisfying the diffuse leverage gate gives the exterior eigenvector identity.
- The branch paid by Theorem 3.1 has a continuous density. No continuity conclusion is claimed for the remaining overlap packets or for the full target.
- The full universal conjecture remains OPEN.

