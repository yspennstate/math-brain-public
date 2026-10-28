SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T03:07:01Z.
attacking: the N3 four-bank survivor — convert the disjoint star-star-core packet into a paid diffuse-tail branch or a quantitative low-tail/two-sided physical-core alternative.

# account03/B07 QFORM r22 — four-bank tail/core trichotomy and a paid volume branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Run:** `20260923T030701Z-account03-B07-qform-r22`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `NEW STRUCTURAL ALTERNATIVE + PAID CONTINUOUS-DENSITY BRANCH / FULL TARGET OPEN`.

## 1. Scope and correction boundary

The full target remains unrestricted: for every dimension, arbitrary independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `Q=X^TAX`, or give a valid counterexample. The stronger continuous-density conclusion is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, iid, diagonal-basis, post-rotation independence, law-uniform pointwise Fresnel decay, arbitrary-joint rank-three coarea bound, worst conditional projection-density cap, or single-good-minor assertion is used. The live correction ledger was reread at brain commit `10bffccff59452d117bf5117b4583f54064c125f` immediately before this report.

The newest owner continuation assigns B07 to prove an actual physical-core or low-tail alternative in the no-pivot class. This report does exactly that for the current four-bank survivor. It also consumes the newest volume-tail theorem at an equation, as required.

The designated `account04/B07` canonical QFORM directory was checked again and remains absent. I do not fabricate a partner result. A completed compatible account04 result, account04/B18, is applied to the actual large-star inequality in Section 7.

## 2. Incoming disjoint physical packet

The immediate predecessor is this slot's completed r21 physical-deshearing result, current canonical path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T004111Z-account03-B07-qform-r21/REPORT.md`.

Inside the current N3/O0 branch, after the residual-second-compound branch has not fired, it gives four mutually disjoint ORIGINAL-coordinate banks and a residual physical cross block `M` for which

    C R F > kappa,                                             (2.1)

where

    C = ||c_L||_2,
    R = ||r_R||_2,
    F = ||M||_F,
    kappa = 1/(256 sqrt(3)).                                  (2.2)

The two star coefficient banks and the row/column banks supporting `M` are pairwise disjoint. Equation (2.1) is an aggregate determinant consequence, not a claim that one matrix entry or one minor is large.

The newest source actually consumed is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`
and `PEER_TAIL_EXTENSION.md`.

For a physical cross block `M`, let its squared singular values be

    lambda_1 >= lambda_2 >= ... >= 0,

and put

    S = sum_j lambda_j = F^2,
    T = sum_{j>=3} lambda_j.                                  (2.3)

The completed scheduled-worker identity used by the newest source is

    T E_2(M) <= 3 E_3(M),                                    (2.4)

where `E_k(M)=e_k(MM^T)`. The same source proves the volume-marginal certificate: for ANY orthogonal projection `P` on the row-index space, with `epsilon=||(I-P)M||op`, the third-volume row marginal `alpha_i` satisfies

    sqrt(alpha_i)
      <= sqrt(P_ii)
       + sqrt(3) epsilon/sqrt(T) sqrt(1-P_ii).                 (2.5)

If `max_i P_ii<=1/2` and `epsilon<=sqrt(T)/15`, then every `alpha_i<2/3`, and its q=4/3 Fourier theorem gives the continuous-density estimate

    ||p_Q||infinity <= (9 sqrt(3)e/2) E_3(M)^(-1/6),           (2.6)

with arbitrary self blocks, outside couplings, signs and affine terms retained.

## 3. New scale lemma: non-low-tail forces third-volume mass

### Lemma 3.1 — `QFORM-TAIL-TO-E3-SCALE-v1`

Let `0<theta<=1/2`. If

    T >= theta S,                                             (3.1)

then

    boxed: E_3(M) >= (theta^2/6) S^3
                     = (theta^2/6) F^6.                       (3.2)

#### Proof

First suppose `T<=S/2`. Since `lambda_1+lambda_2=S-T`, the second elementary symmetric polynomial contains all top-versus-tail products, hence

    E_2(M) >= (lambda_1+lambda_2)T=(S-T)T.                    (3.3)

Using (2.4),

    E_3(M) >= T E_2(M)/3
            >= T^2(S-T)/3
            >= theta^2 S^3/6.                                (3.4)

Now suppose `T>=S/2`. Then

    lambda_1 <= lambda_1+lambda_2=S-T<=S/2.                   (3.5)

Therefore

    sum_j lambda_j^2 <= lambda_1 sum_j lambda_j <= S^2/2,    (3.6)

and Newton's identity for `E_2` gives

    E_2(M)=(S^2-sum_j lambda_j^2)/2 >= S^2/4.                 (3.7)

Again by (2.4),

    E_3(M) >= T E_2(M)/3 >= S^3/24.                           (3.8)

Since `theta<=1/2`, `theta^2/6<=1/24`, so (3.8) implies (3.2). QED.

This lemma is useful precisely because it does not ask for one substantial third singular value. A large collective tail creates third-volume mass even when every individual tail singular value is tiny.

## 4. A bounded-rank spectral core with a small operator tail

Assume from now on the non-low-tail condition (3.1). Define the singular threshold

    sigma_* = sqrt(T)/15.                                    (4.1)

Let `J` be the set of ALL singular directions satisfying

    s_j(M) > sigma_*.                                        (4.2)

Let `P_L` and `P_R` be the corresponding left and right singular-space projections. Since every selected squared singular value is `>T/225`,

    |J| T/225 < sum_{j in J} lambda_j <= S.                  (4.3)

Using `T>=theta S`,

    boxed: rank P_L=rank P_R=|J| <225/theta.                 (4.4)

By construction the omitted cross operator satisfies on BOTH sides

    boxed:
    ||(I-P_L)M||op <= sqrt(T)/15,
    ||M(I-P_R)||op <= sqrt(T)/15.                             (4.5)

Thus the entire possibly high-dimensional block has been split into a universal-rank core and an operator-small remainder, with the rank depending only on the fixed bookkeeping parameter `theta`, never on `n`.

There is also an actual ORIGINAL-coordinate consequence if one of these projections is heavy. If `(P_L)_ii>1/2`, then the selected-core row energy obeys

    ||e_i^T P_L M||_2^2
      = sum_{j in J} lambda_j u_{ij}^2
      > (T/225)(P_L)_ii
      > T/450.                                                (4.6)

Similarly, if `(P_R)_aa>1/2`,

    ||M P_R e_a||_2^2 > T/450.                               (4.7)

No one entry is selected or inverted: (4.6)-(4.7) are aggregate physical row/column core energies.

## 5. Diffuse core is completely paid

Suppose either

    max_i (P_L)_ii <=1/2                                    (5.1)

or

    max_a (P_R)_aa <=1/2.                                   (5.2)

In the second case transpose the physical cross block; `E_3`, `S` and `T` are unchanged. In either orientation, (4.5) plugs directly into the newest volume-tail marginal estimate (2.5). Since

    d:=sqrt(3)/15,

for `0<=ell<=1/2`,

    sqrt(alpha_i)
      <= sqrt(ell)+d sqrt(1-ell)
      <= (1+d)/sqrt(2),                                     (5.3)

so

    alpha_i <= (1+sqrt(3)/15)^2/2
             =0.6221367205... <2/3.                         (5.4)

The q=4/3 theorem therefore applies. Combining (2.6) and Lemma 3.1,

    boxed:
    ||p_Q||infinity
      <= (9 sqrt(3)e/2)(6/theta^2)^(1/6) F^(-1).             (5.5)

The density is continuous and vanishes at infinity on this branch. Every within-bank quadratic term, outside coupling and additional eigenvalue of the full ambient matrix remains present; this is not a small-random-error argument.

## 6. Main theorem: star / low-tail / paid / two-sided-core alternative

### Theorem 6.1 — `QFORM-T4-LOWTAIL-OR-BICORE-v1`

Assume the physical four-bank packet (2.1). Fix arbitrary constants

    Lambda>0,     0<theta<=1/2.                              (6.1)

Then at least one of the following four alternatives holds.

**A. Large disjoint two-star reserve**

    C R > Lambda.                                            (6.2)

**B. Quantitative low-total-tail block**

    T < theta F^2,                                           (6.3)

so equivalently

    dist_F(M,{rank<=2})=sqrt(T) < sqrt(theta) F.             (6.4)

**C. Paid diffuse-tail branch**

The full ambient quadratic form has a continuous density satisfying

    boxed:
    ||p_Q||infinity
      < 3456 e Lambda (6/theta^2)^(1/6).                     (6.5)

**D. Two-sided bounded-rank physical core**

There are matched left/right singular projections `P_L,P_R` satisfying

    rank P_L=rank P_R <225/theta,                            (6.6)
    ||(I-P_L)M||op, ||M(I-P_R)||op <=sqrt(T)/15,             (6.7)

and ORIGINAL physical coordinates `i,a` in the row and column core banks with

    (P_L)_ii>1/2,     (P_R)_aa>1/2,                          (6.8)

hence

    boxed:
    ||e_i^T P_L M||_2,
    ||M P_R e_a||_2
       > sqrt(T/450)
       >= sqrt(theta/450) F
       > sqrt(theta/450) kappa/Lambda.                       (6.9)

#### Proof

If (A) fails, (2.1) implies

    F > kappa/Lambda.                                        (6.10)

If (B) also fails, then `T>=theta F^2`, so Sections 3-4 apply. If either `P_L` or `P_R` is diffuse in the sense of (5.1)-(5.2), equation (5.5) and (6.10) give

    ||p_Q||infinity
      < (9 sqrt(3)e/2)(6/theta^2)^(1/6)(Lambda/kappa).

Since `1/kappa=256 sqrt(3)`, the prefactor is exactly

    (9 sqrt(3)e/2)(256 sqrt(3))=3456e,

which is (6.5). Otherwise both projections have a diagonal entry `>1/2`; choose corresponding original row and column coordinates. Equations (4.4)-(4.7), `T>=theta F^2`, and (6.10) give (6.6)-(6.9). QED.

This is a genuine dimension-free routing theorem. It does not assert a good local minor. It says that after the four-bank determinant packet is exposed, failure of a uniform analytic payment forces either a rank-two Frobenius tube, a large independent star pair, or two heavy ORIGINAL coordinates in a universally bounded-rank singular core with a quantitatively small operator remainder.

## 7. Completed account04 result applied to the large-star inequality

The designated `account04/B07` still has no completed current-QFORM artifact, so none is invented. The compatible completed account04/B18 sharp rearrangement/product-projection source is

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its one-dimensional product-projection consequence is, for an original-coordinate coefficient bank `u`,

    ||p_(u^T X)||infinity <= sqrt(2)/||u||_2.                 (7.1)

The two star banks in (2.1) are disjoint original-coordinate sets, so their scalar projections are genuinely independent. On alternative (A), (7.1) gives the ACTUAL two-dimensional coefficient-plane inequality

    boxed:
    ||p_(c_L^T X_L, r_R^T X_R)||infinity
      <= 2/(C R)
      < 2/Lambda.                                             (7.2)

This is deliberately not promoted to a generic indefinite quadratic density theorem: the correction ledger shows that a bounded projected joint density alone does not control every curved pushforward. Equation (7.2) is the source-valid resource to feed the remaining hub/star receiver.

## 8. Concrete collar

For the convenient fixed choice

    theta=1/16,     Lambda=1,                                (8.1)

Theorem 6.1 says that the T4 survivor has one of:

1. `C R>1`, with independent star-plane density cap `<2` by (7.2);
2. `dist_F(M,rank<=2)<F/4`;
3. a bounded continuous full-output density with

       ||p_Q||infinity <31910.485981;                         (8.2)

4. a two-sided selected singular core of rank `<3600`, operator remainder at most `sqrt(T)/15`, and physical core row/column norms each exceeding

       sqrt((1/16)/450) kappa
         =2.657866474... x 10^(-5).                           (8.3)

The large numerical constant is irrelevant to the universal-constant target; the gain is that a formerly amorphous high-dimensional T4 survivor has been reduced to two explicit structured geometries plus a fully paid branch.

## 9. Deterministic checks

`CHECKS.py` and its actual output `CHECKS.txt` are saved beside this report. The finite deterministic grid checks 97,625 ordered integer spectra in dimensions 3 through 7, verifies `T E2<=3E3`, verifies Lemma 3.1 on every grid point meeting `T>=S/16`, and checks the exact collar constants. Output ends `STATUS=PASS`.

The checks are diagnostics, not a substitute for the proof above.

## 10. What remains

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.** Continuity is proved here only on alternative (C).

For this B07 route, the first unpaid implication is now

`QFORM-N3-T4-STAR-LOWTAIL-BICORE-RECEIVER-v1`:

- pay the large disjoint-star branch using its genuine product-linear provenance rather than only the joint cap (7.2);
- pay the rank-two Frobenius tube using the completed rank-two fractional-volume/hyperbolic mechanisms without requiring a nonzero scalar pivot bounded away from zero; or
- use the two-sided bounded-rank physical core (6.6)-(6.9) to force a determinant-pair, mixed-hub, finite-core, D'/D5, or grouped-square exit.

The sibling residual-`E_2(D)>1/48` branch from the preceding O0 split remains separate. No easy subclass is being substituted for the full theorem.

## 11. Source status

Fresh pre-publication brain control: `10bffccff59452d117bf5117b4583f54064c125f`, revision `2026-09-22.15`. Current volume-tail package: `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`. Compatible account04 input: `math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`.

Repository access and native learned-memory ingestion are separate. No authenticated native receiver ingestion occurred, so this run remains `WITHOUT_VERIFIED_BRAIN`. No task identity, schedule, enabled/paused state, notification state, email/public workflow, paid API/model/Codex call, or cross-account native setting was changed.
