SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T00:51:27Z.
attacking: convert the designated partner's high-E4 double-anchor packet into a continuous density bound by aggregate fixed-pair product Fourier, then test the bridge on a dense rotated indefinite family where every usable local four-row determinant decays with dimension.

# account03/B04 r45 — canonical E4 pair mass pays by aggregate fixed-pair product Fourier

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Status: **NEW SUPPORTING BRIDGE / DESIGNATED-PARTNER BRANCH CLOSED / FULL TARGET OPEN**.
Execution status: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. This report proves a quantitative bridge from canonical fourth-volume pair mass on a literal original-coordinate cross block to a continuous density bound for the full ambient quadratic form. It then applies the completed designated partner `account04/B04` result at an actual inequality and closes the partner's previously explicit double-anchor branch. The argument uses only original-coordinate product structure and a source-pinned aggregate fixed-pair Fourier theorem; it does not rotate the random variables and does not use law-uniform pointwise oscillatory decay.

## 1. Fresh controls and sources

Fresh `math-research-brain/main` was read in this invocation. The final prepublication control refresh was at brain commit

`c33c5449a7fcb686bf59450551ec160693c43ce3`,


The two mathematical inputs used are:

1. **Designated partner account04/B04 r2.**  
   `QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1`, source-pinned at
   `yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260924T001353Z-account04-B04-QFORM-r2/REPORT.md`.

   For a literal cross block `M=A[I,J]`, its canonical fourth-row-volume law `pi`, a carrier row `i` with `rho_i=P_pi(i in R)>1/25`, and conditional face marginals `beta_j=P_pi(j in R | i in R)`, the partner proves the dichotomy:

   - if `beta_*:=max_j beta_j <=2/3`, the anchored entropy-weighted third-volume theorem already pays the full ambient quadratic form;
   - if `beta_*>2/3`, then some literal row `j` satisfies
     `P_pi(i,j in R)>2/75`.

2. **Aggregate fixed-pair Fourier theorem.**  
   `QFORM-FIXEDPAIR-AGGREGATE-FOURVOLUME-v1`, source-pinned at
   `yspennstate/math-open-problems@2a53120a6f9206721f98811b05cd8c80002aab68`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T174734Z-account01-B09-QFORM-auto11/REPORT.md`.

   For any fixed pair `H={a,b}` of literal original coordinates define

   `U_H = sum_{S subset H^c, |S|=2} sum_{T subset H^c\S, |T|=4} det A[H union S,T]^2`.

   If `U_H>0`, then the full ambient quadratic-plus-affine form has a continuous `C_0` density and

   `||p_Q||_infinity <= C4 U_H^(-1/8)`,

   where

   `C4 = 2 sqrt(2) e^(1/4) 3^(3/4)
       = 8.278650626819047...`.

   The theorem retains arbitrary same-bank curvature, the full physical hub core, outside couplings, affine terms, and signs.

## 2. First missing implication: pair mass in a cross block is already fixed-pair currency

Let `I,J` be disjoint sets of original coordinate indices and

`M=A[I,J]`.

Write

`E4(M)=e_4(M M^T)`.

By row Cauchy--Binet,

`E4(M)
 = sum_{R subset I, |R|=4} det(M[R,:] M[R,:]^T)
 = sum_{R subset I, |R|=4} sum_{T subset J, |T|=4} det A[R,T]^2`.    (2.1)

Fix two literal rows `H={i,j} subset I`. Define the anchored row-four volume

`H_ij
 := sum_{R subset I, |R|=4, H subset R}
       det(M[R,:]M[R,:]^T)`                                      (2.2)

and the canonical pair probability

`eta_ij := H_ij/E4(M)`                                            (2.3)

when `E4(M)>0`.

Expanding every row Gram determinant in (2.2) over column minors gives the exact identity

`H_ij
 = sum_{S subset I\H, |S|=2}
   sum_{T subset J, |T|=4}
   det A[H union S,T]^2`.                                        (2.4)

Because `I cap J=empty`, every term on the right of (2.4) is among the terms defining `U_H`: its two leaf rows lie in `H^c`, its four columns lie in `H^c`, and the leaf row set is disjoint from the column set. Therefore

`boxed: U_H >= H_ij = eta_ij E4(M).`                              (2.5)

This is the essential bridge. It aggregates the whole canonical pair packet before taking a reciprocal; no single local four-row determinant is selected or inverted.

## 3. New theorem — `QFORM-CANONICAL-E4-PAIR-TO-DENSITY-v1`

### Theorem

Let `X_1,...,X_n` be independent real random variables with probability densities at most one. Let

`Q=X^TAX+b^TX+c`

for arbitrary real symmetric `A` and arbitrary affine terms. Let `I,J` be disjoint original-coordinate banks, set `M=A[I,J]`, assume `E4(M)>0`, and let `i != j` lie in `I`. If the canonical row-four-volume pair probability is

`eta_ij=P_pi(i,j in R)>0`,

then `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C4 [eta_ij E4(M)]^(-1/8),
 C4=2 sqrt(2)e^(1/4)3^(3/4)<8.279.`                              (3.1)

The same coefficient gives the linear interval estimate

`P{Q in B} <= C4 [eta_ij E4(M)]^(-1/8) |B|`                      (3.2)

for every interval `B`.

### Proof

Equation (2.5) gives `U_H>=eta_ij E4(M)>0`. Apply the source-pinned fixed-pair theorem to the literal original-coordinate pair `H={i,j}`:

`||p_Q||_infinity <= C4 U_H^(-1/8)
                   <= C4 [eta_ij E4(M)]^(-1/8)`.

Its Fourier envelope is integrable, so the resulting density is continuous and vanishes at infinity. No random-coordinate rotation occurs. QED.

## 4. Actual designated-partner application: the double-anchor branch is paid

Apply account04/B04 r2. In its live high-carrier branch

`rho_i=P_pi(i in R)>1/25`.                                       (4.1)

If its anchored-face entropy gate fails at the chosen clean threshold `2/3`, then the partner proves that some `j != i` satisfies

`eta_ij=P_pi(i,j in R)=rho_i beta_j>2/75`.                        (4.2)

Insert (4.2) into (3.1):

`||p_Q||_infinity
 < C4 (2E4(M)/75)^(-1/8)`                                        (4.3)

or explicitly

`boxed:
 ||p_Q||_infinity
 < 13.023072655226386... E4(M)^(-1/8).`                           (4.4)

This branch has a continuous `C_0` density.

Thus the partner's r2 double-anchor packet is no longer an unpaid endpoint. Its high-carrier theorem can now be restated as a complete two-branch receiver:

- **anchored entropy branch:** if `beta_*<=2/3`, use the partner's explicit bound

  `||p_Q||_infinity
   < (9 e sqrt(3)/2)
     (25 ||m_i||_2^2/E4(M))^(1/6)`;                              (4.5)

- **double-anchor branch:** if `beta_*>2/3`, use (4.4).

Both branches prove continuity. The remaining global obstruction is structural: the bare three-large-eigenvalue hypothesis still has to force an appropriate fourth-volume carrier/cut, or route the matrix into another already-paid mechanism.

## 5. Dense genuinely rotated indefinite stress family

The bridge is useful on a family where canonical fourth-volume mass is concentrated on a physical pair while every individual nonzero four-row determinant shrinks with dimension.

Take `N=256`, `m=N-2=254`, and let

`w_1,w_2,w_3,w_4 in R^N`

be four distinct rows of the normalized Sylvester Hadamard matrix `H_256/16`. They are orthonormal and every coordinate of every `w_r` is `+/-1/16`.

Put

`a=1/sqrt(127)`, `L=16`,

and define the `N x N` literal cross block `M_*` by its physical rows:

- row 1: `L w_1`;
- row 2: `L w_2`;
- rows 3 through 129: `a w_3` (127 rows);
- rows 130 through 256: `a w_4` (127 rows).

Every entry of `M_*` is nonzero. Let

`A_* = [[0, M_*], [M_*^T, 0]]`                                   (5.1)

on `2N=512` original coordinates.

### 5.1 Spectrum

Because the four Hadamard rows are orthonormal, the four nonzero singular values of `M_*` are exactly

`16,16,1,1`.                                                      (5.2)

Hence

`spec_nonzero(A_*)
 = {16,16,1,1,-1,-1,-16,-16}`.                                  (5.3)

So `A_*` is indefinite and satisfies the owner's spectral hypothesis with eight eigenvalues of modulus at least one. It is genuinely nonseparable in the original product coordinates: its cross block is dense and the active right singular directions are Hadamard mixtures of all 256 right-bank coordinates.

### 5.2 Exact fourth-volume law

A physical row four-set has nonzero Gram determinant iff it consists of the two heavy rows, one row from the `w_3` group and one row from the `w_4` group. For every such row set,

`d_R = 16^4 a^4
     = 65536/16129`.                                              (5.4)

There are `127^2=16129` such row sets, so

`boxed: E4(M_*)=65536=16^4.`                                     (5.5)

The two heavy rows occur in every supported four-set. Thus

`rho_1=rho_2=1`,
`beta_2|1=1`,
`eta_12=1`.                                                       (5.6)

The designated partner r2 therefore lands exactly in its double-anchor branch, not in its entropy branch.

Applying the new pair-mass theorem with the exact pair mass `eta_12=1` gives, for every admissible independent cap-one product law,

`boxed:
 ||p_{X^T A_* X}||_infinity
 <= C4 * 65536^(-1/8)
 = C4/4
 = 2.069662656704762... .`                                       (5.7)

The density is continuous and vanishes at infinity.

### 5.3 Why the aggregation is substantive

For this family `rank(M_*)=4`, so `E5(M_*)=0`; a fifth-volume exit is unavailable. The left range projection has leverage one on each heavy row, so a diffuse max-leverage `<=1/2` ridge gate fails.

Every nonzero physical four-row restriction has singular-value product

`16^2 a^2 = 256/127`.                                             (5.8)

The exact local rank-four crossing theorem applied to any single such row set therefore gives only

`2 sqrt(2) (256/127)^(-1/4)
 = 2.373755217959999...`.                                        (5.9)

Thus the aggregate fixed-pair bridge strictly improves every single nonzero local four-row certificate on this concrete matrix:

`2.0696626567... < 2.3737552180...`.                              (5.10)

More generally, with `m` light rows split evenly between the two diffuse leaf directions and the same normalization, the best single four-row certificate grows like `m^(1/4)` while the aggregate pair bound remains `C4 L^(-1/2)`. This is exactly the aggregate-before-reciprocal behavior required by the live corrections.

## 6. Quantifier audit

The theorem in Section 3 is valid for:

- arbitrary dimension;
- arbitrary independent real input laws with one-dimensional densities bounded by one;
- arbitrary symmetric ambient `A` and arbitrary signs;
- arbitrary same-bank quadratic terms and outside couplings;
- arbitrary affine terms from conditioning;
- fragmented, unbounded, non-log-concave supports.

Its extra hypothesis is the explicit cross-block canonical pair currency `eta_ij E4(M)>0`. The theorem does **not** claim that the owner's bare three-large-eigenvalue hypothesis forces such a pair at a universal scale. Continuity is proved in this branch because the source fixed-pair Fourier theorem has an integrable characteristic-function envelope.

## 7. Remaining full-target implication

Full QFORM remains OPEN. The immediate new frontier after this bridge is sharper than the partner r2 frontier:

`QFORM-HIGH-E4-CARRIER-ENTROPY-SCALE-OR-GLOBAL-CUT-v1`:

> On a target-valid remaining physical cross block, either obtain a high fourth-volume carrier for which the anchored entropy currency is target-scale, or force a different already-paid crossing/ridge/star/square-bank receiver. The former double-anchor alternative no longer needs new analysis: pair mass `eta` is already paid by `C4 (eta E4)^(-1/8)`.

Equivalently, future structural work should not stop at `P_pi(i,j in R)>c`; that state is now a completed Fourier endpoint. The genuinely unpaid issue is producing target-scale aggregate currency from the bare spectrum without paying a vanishing local minor.

## 8. Checks and provenance

`CHECKS.py` and `CHECKS.json` in this run directory verify the exact family arithmetic, constants, local-vs-aggregate comparison, `E5=0`, and heavy-row range leverage. No Monte Carlo evidence is used.

Model self-report: `GPT-5.6 Sol`.
Configured reasoning effort: `UNKNOWN` (not exposed in the available same-slot scheduler inventory during this run).
Provider reasoning-token/thinking-time counters: `NOT_EXPOSED`.
Native learned-memory ingestion: not verified; execution label remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler state, task identity, cadence, email setting, push notification, repository visibility, account connection, public release, paid API/model call, or cross-account authentication was changed.
