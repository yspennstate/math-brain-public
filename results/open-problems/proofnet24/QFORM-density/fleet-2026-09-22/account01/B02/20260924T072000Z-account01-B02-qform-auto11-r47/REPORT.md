SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T07:20:00Z.
attacking: the live physical-diagonal hub branch of the robust rank-two cut; preserve the hub overlap exactly, prove a pivot/E2 Schur-cancellation trichotomy, and use the partner one-bank receiver before isolating the genuinely two-sided-twisted survivors.

# account01/B02 r47 — diagonal-pivot / robust-E2 Schur-cancellation trichotomy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL STRUCTURAL STEP + ESSENTIAL-DENSITY EXIT / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: the new paid branch gives an essentially bounded density; continuity is **not** claimed there. The designated partner's separate physical-2x2 Fourier-L1 branch gives `C0` continuity on its exact one-sided-twist scope.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moments, log-concavity, compact support, connected support, iid assumption, post-rotation independence, arbitrary-joint coarea bound, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero coefficient tail is used.

## 1. Fresh source boundary and the live packet

Fresh `math-research-brain/main` was resolved at startup. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. `AGENTS.md`, the full fresh `scheduled_tasks/README.md`, programme `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account01/B02.json` were read. The historical source owner message was also checked at immutable brain commit `0dc369ddf8b860648dd780d8f92c62994dc53ecf`; later main control wins. The literal root paths `fleet.json`, `roles.json`, and `PROTOCOL.md` are absent on resolved main and no contents are invented for them.

The live structural source is account03/B02 r47,

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T045848Z-account03-B02-qform-r47/REPORT.md`.

After its diffuse spectral-window and physical-E3 exits, it retains a literal full ORIGINAL-coordinate cut

`N=A[L,R]`, `L disjoint R`, `L union R=[n]`,

whose squared singular values `x1>=x2>=...` satisfy

`x1*x2 > kappa := 247/576`.                                      (1.1)

One still-unpaid alternative is an ORIGINAL coordinate `h` with

`|A_hh| > a0 := 1/228`.                                          (1.2)

Since `E2(N)=e_2(N^T N)>=x1*x2`, this diagonal-hub branch has

`E2(N)>kappa`.                                                     (1.3)

The newest completed designated partner is account02/B02 auto12,

`yspennstate/math-open-problems@19a3d60ceb5d0989aa527b32d3e76f388b9419f6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260924T060210Z-account02-B02-QFORM-auto12/REPORT.md`.

It proves `QFORM-RANK2-ONEBANK-LINEAR-DENSITY-v1`: if one bank of a physical rank-two crossing is exactly untwisted, then

`||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2)`.                  (1.4)

It also proves genuine Fourier `L1` for a literal invertible `2x2` crossing under that one-sided-twist hypothesis. No extension to arbitrary two-sided same-bank curvature is made here.

The row-gate-free residual `E2` half-Riesz receiver used below is account02/B06,

`yspennstate/math-open-problems@cd0be625c8f7143a46ad14bb936e9c24bfb19a8d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`.

For a literal physical residual cross block `B` with `Z=E2(B)>0`, it gives

`H_{1/2}(R):=sup_s E|R-s|^(-1/2) <= 8 e^(1/4) Z^(-1/8)`.          (1.5)

Finally, the exact exterior-square rank-one-update identity was already proved in account03/B02 r32 (read at repository snapshot `a58023f75d96035a9d71dd157e210d231c50af9c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T142846Z-account03-B02-qform-r32/REPORT.md`). I use that identity below rather than claiming it as new.

## 2. Exact pivot notation

Assume first that the diagonal hub `h` belongs to `L`; the case `h in R` is the transpose. Put

`a=A_hh`,
`r=N[h,R]`,
`M=N[L\{h},R]`,
`c=A[L\{h},h]`.                                                     (2.1)

Completing the ORIGINAL scalar square gives

`Q = a (X_h + a^(-1)(c^T X_{L\{h}} + r^T X_R))^2 + R`,            (2.2)

where `R` is the exact Schur residual quadratic form on the remaining independent original coordinates. Its `L\{h}`-to-`R` physical cross block is

`B = M - c r^T/a`.                                                 (2.3)

Nothing is discarded: every same-bank coefficient and every other cross coefficient is retained in `R`.

Define the literal `E2` mass incident to the pivot row inside the original full cut by

`I_h := sum_{j in L\{h}} ||r wedge M[j,:]||_2^2`.                  (2.4)

Cauchy-Binet, partitioning row pairs according to whether they contain `h`, gives the exact orthogonal decomposition

`boxed: E2(N)=E2(M)+I_h.`                                         (2.5)

Lagrange's identity also gives

`boxed: I_h = ||r||_2^2 ||M P_{r^perp}||_F^2.`                    (2.6)

The Schur rank-one update is parallel to `r` row by row. Therefore

`r wedge B[j,:] = r wedge M[j,:]`,                                (2.7)

so the incident packet is exactly invariant under pivot completion:

`boxed: I_h = ||r||_2^2 ||B P_{r^perp}||_F^2.`                    (2.8)

This conservation law is important: an `E2` packet carried by the pivot row cannot be made to disappear by the Schur subtraction; it becomes an explicit overlap packet rather than residual `E2` currency.

## 3. Exterior-square cancellation identity

Let

`F := ||P_{c^perp} B P_{r^perp}||_F
   = ||P_{c^perp} M P_{r^perp}||_F`,                              (3.1)

with the evident convention if `c=0` or `r=0`. The equality holds because the rank-one term `c r^T/a` is killed by either transverse projection.

For any matrix `S` and vectors `p,q`, the account03/B02 r32 identity is

`|| wedge^2(S+p q^T)-wedge^2 S ||_HS
 = ||p|| ||q|| ||P_{p^perp} S P_{q^perp}||_F`.                    (3.2)

Apply this to `M=B+c r^T/a`. Since `E2(T)=||wedge^2 T||_HS^2`, the triangle inequality gives

`boxed:
 sqrt(E2(M))
 <= sqrt(E2(B)) + (||c|| ||r||/|a|) F.
}`                                                                  (3.3)

This is the correct direction for the present problem: we start with a robust literal `E2` packet before the pivot and ask whether enough survives in the exact Schur residual.

## 4. Main theorem — robust E2 plus a nonzero physical diagonal pivot

### Theorem 4.1 — `QFORM-PIVOT-E2-SCHUR-CANCELLATION-TRICHOTOMY-v1`

Let `N=A[L,R]` be a literal full physical cut and let `h in L` satisfy `a=A_hh!=0`. In the notation above, suppose

`E2(N)>=kappa>0`.                                                    (4.1)

Then at least one of the following three alternatives holds.

**(INC) Pivot-row incident two-volume packet**

`boxed: I_h >= kappa/2.`                                          (4.2)

Equivalently, by (2.8),

`boxed: ||r||^2 ||B P_{r^perp}||_F^2 >= kappa/2.`                 (4.3)

This is an exact physical overlap packet and is retained, not declared paid.

**(RES) Residual Schur E2 survives**

`boxed: E2(B) >= kappa/8.`                                        (4.4)

In this case the full law has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 8 e^(1/4) |a|^(-1/2) (kappa/8)^(-1/8).
}`                                                                  (4.5)

Continuity is not claimed from this branch.

**(CAN) Quantitative two-sided Schur cancellation packet**

`boxed:
 ||c|| ||r|| F
 > |a| sqrt(kappa/2)/2.
}`                                                                  (4.6)

Thus failure of both (INC) and the bounded-density exit (RES) forces nontrivial coupling from the pivot into **both** physical sides together with a doubly transverse residual crossing. This is precisely the geometry that a future overlap-one/two-sided-twist Fourier receiver must spend.

#### Proof

If `I_h>=kappa/2`, we are in (INC). Otherwise, from (2.5),

`E2(M)>kappa/2`.                                                    (4.7)

If `E2(B)>=E2(M)/4`, then (4.7) implies (4.4). To prove (4.5), use (2.2). For fixed residual coordinates, the translated scalar square `a(X_h+m)^2` has density bounded by

`|a|^(-1/2)|u|^(-1/2)`                                            (4.8)

(after reflection when `a<0`). Hence, writing `R` for the exact Schur residual,

`p_Q(s) <= |a|^(-1/2) E|R-s|^(-1/2).`                            (4.9)

Apply the completed row-gate-free half-Riesz theorem (1.5) to the literal residual cross block `B` and use (4.4). This proves (4.5), including existence of an essentially bounded density.

It remains to suppose

`E2(B)<E2(M)/4`.                                                    (4.10)

Then `sqrt(E2(B))<sqrt(E2(M))/2`. Substitution in (3.3) gives

`(||c||||r||/|a|)F > sqrt(E2(M))/2
                  > sqrt(kappa/2)/2`,                              (4.11)

which is exactly (4.6). QED.

The theorem is dimension-free and has no perturbative step. A tiny coefficient is never erased; if Schur cancellation is strong enough to destroy residual `E2`, its exact cost reappears as the product packet (4.6).

## 5. Application to the live r47 diagonal-hub branch

On the r47 survivor, (1.1) gives

`E2(N)>kappa=247/576`,                                             (5.1)

and the diagonal branch gives

`|a|>a0=1/228`.                                                     (5.2)

Apply Theorem 4.1.

### 5.1 Residual-E2 payment

In (RES),

`E2(B)>=(247/576)/8=247/4608`.                                    (5.3)

Equation (4.5) and `|a|>1/228` give the explicit universal bound

`boxed:
 ||p_Q||_infinity
 < 8 e^(1/4) sqrt(228) (4608/247)^(1/8)
 = 223.605752...
}`                                                                  (5.4)

for the full ambient law. This is an essential-density conclusion only.

### 5.2 Exact unpaid packets if the density exit does not fire

If (RES) fails, the remaining diagonal-hub branch is forced into one of only two exact packets:

`boxed: I_h > 247/1152 = 0.2144097222...}`                         (5.5)

or

`boxed:
 ||c|| ||r|| F
 > (1/228) sqrt((247/576)/2)/2
 = 0.001015447312... .
}`                                                                  (5.6)

The first is a pivot-row rank-two crossing-area aggregate invariant under Schur completion. The second is a genuinely two-sided overlap packet: pivot-to-left coupling, pivot-to-right coupling, and doubly transverse Schur crossing are all simultaneously present in product. Neither is renamed as a solved density branch.

This is a strict narrowing of the r47 physical-diagonal alternative. In particular, it rules out the possibility that the robust second exterior volume simply disappears under completion of a small-but-fixed physical square without leaving quantitative overlap currency.

## 6. Required equation-level use of account02/B02

Before entering the two-sided analysis above, apply the newest designated partner theorem (1.4) to the **same live full cut** `N`. Its two leading singular values satisfy

`s1 s2 = sqrt(x1 x2) > sqrt(247/576)`.                             (6.1)

Therefore, if either bank is genuinely untwisted after the allowed outside-original-coordinate conditioning, transpose the cut if necessary and obtain

`boxed:
 ||p_Q||_infinity
 < 2 sqrt(pi) (247/576)^(-1/4)
 = 4.380627393... .
}`                                                                  (6.2)

So every survivor of (5.5) or (5.6) may additionally be assumed to have nonzero same-bank quadratic curvature on **both** sides. This is not an added hypothesis on the owner target; it is the complement of an already-paid partner branch.

On a literal invertible physical `2x2` crossing with one bank untwisted, the partner's stronger theorem gives genuine Fourier `L1` and hence a continuous `C0` density. I do not transfer that continuity to the broad theorem (6.2) or to the new residual-E2 payment.

## 7. What this changes in the B02 proof graph

The target-wide universal unweighted Fourier-`L1` assertion remains `OPEN_NOT_REFUTED`; no exact-target counterexample was found in this run. The new work instead removes a substantial part of the bounded-density fallback on the live physical-diagonal branch.

The first unpaid local interface is now

`QFORM-PIVOT-E2-INCIDENT-OR-BISIDED-CANCELLATION-L1-v1`:

starting from either the conserved incident packet

`||r||^2 ||B P_{r^perp}||_F^2 >247/1152`

or the two-sided cancellation packet

`||c|| ||r|| ||P_{c^perp} B P_{r^perp}||_F >0.001015447312`,

and assuming both banks retain same-bank curvature, prove a genuine integrated-Fourier or direct linear-small-ball receiver without deleting the pivot overlap. A valid proof must keep the actual hub modulation average; it cannot take a worst modulation, assume conditional projection caps, or rotate the independent random variables.

This local debt is compatible with the fleet's newer aggregate-third-arm and overlap-two machinery, but I do not claim those theorems automatically apply: `c` and `r` live on opposite physical sides of the overlapping pivot and are not two columns of one disjoint cross block.

## 8. Status and correction audit

- **Proved here:** `QFORM-PIVOT-E2-SCHUR-CANCELLATION-TRICHOTOMY-v1`.
- **Actual live payment:** the residual-Schur-E2 subbranch has `||p_Q||_infinity<223.605752`.
- **Designated partner applied:** account02/B02 auto12 gives `<4.380627393` on the one-bank-untwisted live subbranch.
- **Remaining exact packets:** (5.5) and (5.6), with both-bank twist after the partner exit.
- **Full QFORM:** OPEN / not proved / not disproved.
- **Target-wide Fourier L1:** OPEN_NOT_REFUTED.
- **Full-target continuity:** OPEN.

Corrections preserved: no law-uniform scalar van-der-Corput decay; no post-rotation independence; no arbitrary-joint coarea lemma; no universal conditional projection cap/moment; no fiber-sup dimension-free shortcut; no one-heavy-row same-square absorption; no coefficient-smallness perturbation; no inference that positive `E2` alone implies an `L^infinity` density. The density payment uses the physical scalar square **together with** residual Schur `E2` half-Riesz credit.
