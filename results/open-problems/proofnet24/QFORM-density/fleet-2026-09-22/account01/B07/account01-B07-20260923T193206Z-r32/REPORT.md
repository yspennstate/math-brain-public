SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T19:32:06Z.
attacking: lift the r31 overlap-one/two determinant currencies through the latest rank-two rough-tail carrier and derive a dimension-free aggregate selection/pay-or-regenerate implication.

# account01/B07 r32 — swapped-extension determinant funnel for a physical E2 packet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T193206Z-r32`  
Initial brain main: `yspennstate/math-research-brain@7202d57ea54cce639ea408b33a2c270271c6f8f4`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SWAPPED-EXTENSION MAIN/CURVATURE IDENTITY / NEW PHYSICAL-E2-MARGINAL FUNNEL / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. Inputs remain independent ORIGINAL-coordinate variables with one-dimensional densities bounded by one. No post-rotation independence, moment, bounded-support, connected-support, Gaussian, iid, or log-concavity hypothesis is used. The argument below is entirely in physical coordinates. It keeps the true same-bank quadratic blocks: when they obstruct the cross-E3 payment, they appear as an explicit positive aggregate correction currency rather than being deleted as a perturbation.

## 1. Source-pinned inputs

### 1.1 Latest own overlap funnel

Source:

`yspennstate/math-open-problems@60106507e16f9a5eb4453e276a0642f880eeec9d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T191801Z-r31/REPORT.md`.

The r31 report combines the E2-to-E3 spectral extension lift with the completed marginal-free physical cross-E3 receiver. Its important lesson for this run is that a disjoint physical E3 packet is already a complete payment; the difficulty is to generate such a packet while retaining the same-bank curvature that can cancel a naive cross extension.

### 1.2 Marginal-free physical cross-E3 receiver

The completed receiver used through r31 is

`QFORM-CROSS-E3-MARGINALFREE-L1-v1`,

source `yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`.

For a literal disjoint original-coordinate cross block `A[U,V]` with complete third-compound mass `V3=e3(A[U,V]A[U,V]^T)>0`, the full ambient quadratic form has a continuous `C0` density with

`||p_Q||_infinity <= C_E3 V3^(-1/6)`,

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.

Arbitrary same-bank curvature, all outside couplings, affine terms and signs are retained.

### 1.3 Latest designated partner account02/B07

Source:

`yspennstate/math-open-problems@12da18e77ea3c2097023c2da5193c86ef3b6478c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T183825Z-account02-B07-qform-r11/REPORT.md`.

The actual partner cross block is

`K=A[L,R]`, with `L cap R=empty`,

and its complete physical E2 mass obeys

`Omega=e2(KK^T)>Z0 h^4`,

`Z0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`.

The partner's low-E3 rank-two-carrier branch retains its true nonzero interface tail and arbitrary same-bank blocks. The present theorem applies directly to this same actual `K`; it does not replace it by the rank-two truncation.

## 2. Exact inverse-free swapped-extension identity

Let `A` be any real symmetric matrix. Fix two disjoint physical coordinate banks `L,R` and put

`K=A[L,R]`.

For physical row pairs `I subset L`, column pairs `J subset R`, `|I|=|J|=2`, write

`B_(I,J)=K[I,J]`,
`d_(I,J)=det B_(I,J)`.

For `c in L\I` and `r in R\J`, the row triple `I union {r}` and the column triple `J union {c}` are disjoint physical coordinate sets. Define the corresponding actual 3x3 determinant

`D_(I,J;r,c)=det A[I union {r}, J union {c}]`.

Because, in the indicated row/column ordering,

`A[I union {r},J union {c}]
 = [[B_(I,J), A[I,c]], [A[r,J], K_(c,r)]]`,

the bordered-determinant identity gives, with no invertibility assumption on `B_(I,J)`,

`boxed:
D_(I,J;r,c)
 = d_(I,J) K_(c,r)
   - A[r,J] adj(B_(I,J)) A[I,c].`                 (2.1)

This is the elementary identity on which the run rests. The first term is the extension that would be present in the pure bipartite model. The second term is the exact same-bank-curvature correction. No reciprocal pivot appears.

Define vectors indexed by quadruples `(I,J;r,c)`, `c notin I`, `r notin J`,

`m_(I,J;r,c)=d_(I,J)K_(c,r)`,

`q_(I,J;r,c)=A[r,J]adj(B_(I,J))A[I,c]`,

and their squared Euclidean norms

`M=||m||_2^2`,
`C_curv=||q||_2^2`,
`H_swap=||m-q||_2^2
       =sum_(I,J) sum_(c notin I,r notin J) D_(I,J;r,c)^2`.      (2.2)

Then the triangle inequality gives

`sqrt(M)<=sqrt(H_swap)+sqrt(C_curv)`,

and therefore the following sharp-enough dichotomy:

`boxed:
max(H_swap,C_curv) >= M/4.`                                    (2.3)

Indeed, if both terms on the left were strictly below `M/4`, the sum of their square roots would be strictly below `sqrt(M)`.

This is `QFORM-SWAPPED-E3-MAIN-OR-CURVATURE-v1`.

## 3. The main energy is exactly controlled by E2 determinant-law marginals

Assume the complete E2 mass

`Omega=sum_(I,J) d_(I,J)^2=e2(KK^T)`

is positive, and let `w_(I,J)=d_(I,J)^2/Omega` be its physical determinant law. Define its row/column inclusion marginals

`alpha_c=P_w(c in I)`, `c in L`,

`beta_r=P_w(r in J)`, `r in R`.

As usual,

`sum_(c in L) alpha_c=2`,
`sum_(r in R) beta_r=2`.                                       (3.1)

Rearranging the sum in the definition of `M` gives the exact identity

`M
 =Omega sum_(c in L,r in R) K_(c,r)^2
      P_w(c notin I, r notin J).`                              (3.2)

The union bound is now used in a direction that loses no dimension:

`P_w(c notin I,r notin J)
 =1-P_w((c in I) union (r in J))
 >=1-alpha_c-beta_r`.                                          (3.3)

Hence, if

`alpha_*:=max_c alpha_c <= a`,
`beta_*:=max_r beta_r <= b`,
`a+b<1`,

then with `E=||K||_F^2`,

`boxed:
M >= (1-a-b) Omega E.`                                         (3.4)

Nothing about the singular-vector coordinates has been used; these are the actual physical E2 determinant marginals.

Combining (2.3) and (3.4) gives the structural theorem:

### Theorem 3.1 — `QFORM-PHYSICAL-E2-MARGINAL-SWAP-FUNNEL-v1`

For every `a,b>=0` with `a+b<1`, a literal physical cross block `K=A[L,R]` with `Omega=e2(KK^T)>0` satisfies at least one of:

1. **physical E2 hub:** `alpha_*>a` or `beta_*>b`;
2. **swapped disjoint E3 currency:**

   `H_swap >= (1-a-b)Omega E/4`;
3. **same-bank adjugate correction currency:**

   `boxed:
   C_curv
   =sum_(I,J)sum_(c notin I,r notin J)
     |A[r,J]adj(K[I,J])A[I,c]|^2
   >=(1-a-b)Omega E/4.`                                        (3.5)

The third branch is not called an error term. It is a positive aggregate resource carried by the true same-bank quadratic blocks, and it is retained for the next receiver.

## 4. The swapped-E3 branch is a full ambient payment

Every determinant counted by `H_swap` has disjoint row and column triples. Although the row/column roles use coordinates from both `L` and `R`, a random two-colouring of the original coordinates retains any fixed ordered disjoint triple pair with probability `2^-6=1/64`. Consequently there is a deterministic colouring and disjoint physical coordinate banks `U,V` such that the complete E3 volume of `A[U,V]` satisfies

`V3 >= H_swap/64`.                                              (4.1)

Therefore branch 2 of Theorem 3.1, followed by the completed marginal-free cross-E3 receiver, proves a continuous full-ambient density bound

`boxed:
||p_Q||_infinity
 <= C_E3 [ (1-a-b)Omega E /256 ]^(-1/6).`                       (4.2)

This argument retains all same-bank curvature because (2.1) used the actual determinants of `A`, not those of a bipartite surrogate.

A convenient symmetric choice is

`a=b=2/5`.                                                       (4.3)

Then either a physical coordinate has E2 determinant inclusion marginal exceeding `2/5` on one side, or

`C_curv >= Omega E/20`,                                         (4.4)

or the full ambient law has a continuous density satisfying

`boxed:
||p_Q||_infinity
 <= C_E3 (1280/(Omega E))^(1/6).`                               (4.5)

The `2/5` threshold is useful because the E2 marginals sum to two, so there are at most four such physical hubs on either side.

## 5. Scale-only corollary

The elementary singular-value identity

`Omega=e2(KK^T)
      =sum_(i<j) s_i^2s_j^2
      <=(sum_i s_i^2)^2/2
      =E^2/2`

gives

`E>=sqrt(2Omega)`.                                               (5.1)

Thus in the symmetric `2/5` diffuse-marginal branch,

`M>=Omega E/5 >= (sqrt(2)/5)Omega^(3/2)`.                       (5.2)

Consequently either

`boxed:
C_curv >= (sqrt(2)/20)Omega^(3/2),`                             (5.3)

or the continuous payment sharpens to

`boxed:
||p_Q||_infinity
 <= C_E3 (1280/sqrt(2))^(1/6) Omega^(-1/4).`                    (5.4)

This is dimension-free. The only remaining alternative is a physical E2 determinant hub of marginal `>2/5`.

## 6. Required application to the latest designated partner

Apply Theorem 3.1 to the actual partner block from Section 1.3,

`Omega=Z>Z0 h^4`,
`Z0=854675.100194511`,
`h=1.1624826588606455e-6`.

No rank-two truncation is substituted here; the partner's true rough interface tail stays inside `K`.

With `a=b=2/5`, one of the following holds:

### (A) physical determinant hub

On the left or right side, one original coordinate has complete E2 determinant-law inclusion marginal

`>2/5`.

There are at most four such coordinates per side.

### (B) continuous full-form payment

Using (5.4) and the partner's actual lower bound on `Omega`,

`boxed:
||p_Q||_infinity < 928335.929.`                                (6.1)

The density in this branch is continuous and vanishes at infinity, by the cited cross-E3 receiver.

### (C) explicit same-bank rough-tail currency

The actual same-bank blocks satisfy

`boxed:
C_curv
 > (sqrt(2)/20) Z0^(3/2) h^6
 = 55871017.35631285 h^6
 > 1.37881334486e-28.`                                         (6.2)

Thus the latest partner's support-diffuse rough-tail problem is no longer a bare `K=C+small` perturbation in the physical-E2-diffuse subbranch. If the cross-E3 determinant packet does not already pay, the same-bank blocks themselves must carry the explicit inverse-free rank-at-most-two bridge currency (3.5).

This is an application of the completed partner result to the actual inequality `Z>Z0h^4`; no Monte Carlo or selected tiny minor is used.

## 7. Why this advances the rough-tail obstruction

The exact tail-zero bipartite model has `A_LL=A_RR=0`, hence `C_curv=0`. Theorem 3.1 then forces a disjoint swapped-E3 packet whenever the physical E2 determinant law is diffuse. This recovers, at the determinant level, why the exact flat two-frame endpoint is not the obstruction: its rank-two E2 volume automatically extends through the opposite physical banks.

For a true rough-tail/same-bank matrix, cancellation of those swapped extensions is possible, but (2.1)--(3.5) show that such cancellation is not free. It requires a quantitatively large contraction

`A[r,J] adj(K[I,J]) A[I,c]`

aggregated over the same determinant anchors. This is precisely product-preserving original-coordinate data, rather than a norm-small random perturbation. It is therefore a better currency for the next dependence-safe receiver than the bare Frobenius tail.

The argument also explains why selecting a single `2x2` pivot is the wrong operation: all determinants are retained until either a full disjoint E3 packet has been created or the curvature contraction has accumulated a dimension-free amount.

## 8. First remaining implication

The first B07 debt is now

`QFORM-E2-HUB-OR-SAMEBANK-ADJBRIDGE-RECEIVER-v1`:

> Starting from the partner r35/rank-two rough-tail state, pay either (i) a physical E2 determinant hub of marginal `>2/5` (at most four per side), or (ii) the aggregate same-bank bridge currency
>
> `sum |A[r,J] adj(K[I,J]) A[I,c]|^2 >= (sqrt(2)/20)Omega^(3/2)`,
>
> while retaining all nonzero interface tail, arbitrary same-bank curvature and outside couplings. The exact tail-zero diffuse case is already paid by the present swapped-E3 branch.

The likely next mechanism is grouped-coordinate/hub Fresnel smoothing for the finite hub set, with the adjugate bridge treated as a genuine two-sided star feature rather than a perturbation. The open `(SP)` conditional-adaptation statement in the latest Claude continuation is **not** used as a completed theorem.

The partner's separate rank-at-most-one carrier remains a separate unresolved face. Full QFORM and the global continuity conclusion remain OPEN.

## 9. Algebraic regression

For random finite symmetric matrices, direct enumeration verifies to floating-point precision both

`D_(I,J;r,c)=d_(I,J)K_(c,r)-A[r,J]adj(K[I,J])A[I,c]`

and

`M=Omega sum_(c,r)K_(c,r)^2 P_w(c notin I,r notin J)`.

These checks are only regression evidence; the proof is the exact determinant expansion and sum rearrangement above.
