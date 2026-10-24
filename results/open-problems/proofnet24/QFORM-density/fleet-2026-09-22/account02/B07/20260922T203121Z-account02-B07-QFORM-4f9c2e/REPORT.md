SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-22T20:31:21Z.
attacking: aggregate coordinate-minor payment: convert determinant-weighted third-compound mass directly into a dimension-free ridge/Fourier bound before any reciprocal tiny-minor selection.

# account02/B07 — effective-dimension payment of aggregate exterior mass

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** 20260922T203121Z-account02-B07-QFORM-4f9c2e  
**Assignment:** Coordinate minor selection / complementary constructions and source-valid counterexamples  
**Control at start:** math-research-brain main e56fb0b7356cd84241c8cfe8ca1921a13f9be4f8, OWNER CONTROL revision 2026-09-22.15.  
**Execution:** WITHOUT_VERIFIED_BRAIN.  
**Classification:** ESSENTIAL_STEP_APPLIED; full QFORM OPEN.

## 1. Sources actually used

1. Current target/corrections and assignment from `yspennstate/math-research-brain` main, including `CURRENT_RESEARCH.md`, `CORRECTION_INBOX.json`, `PATHWAYS.md`, `MEMORY_PROTOCOL.md`, and `assignments/account02/B07.json`.
2. Completed analytic theorem `QFORM-RIDGE-DENSITY-v1`, full proof:
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   Exact scope used below: for an original-coordinate cross block `B=A[I,J]`, with
   `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+BB^T/gamma^2)`, if `1<=q<=2`, `max_i (K_gamma)_ii<=q/2`, and `theta>2q`, then the full quadratic form, retaining arbitrary self blocks, outside couplings, affine terms and extra spectrum, has
   `||p_Q||_infinity <= e/(sqrt(2q) gamma) * theta/(theta-2q) * D^(-1/(2theta))`.
   The theorem may be applied after transposing `B` and therefore either physical side may supply the leverage gate.
3. Designated partner account03/B07 r16, complete report:
   `yspennstate/math-open-problems@4ee3cfb2d6682d5be670819cf5de173ad859f6cf:proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T193812Z-account03-B07-qform-r16/REPORT.md`.
   Its `QFORM-COLORED-EXTERIOR-MATCHING-v1` keeps compound mass aggregated over original-coordinate banks and, on the full O0 branch, supplies the exact source-valid resource
   `E_3(B):=e_3(BB^T)>=1/256`.
4. Previous own completed theorem `QFORM-CROSS-FIBER-PLANCHEREL-v1`, source:
   `yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39:proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.
   In exact cross rank `r>=3` it gives `||p_Q||_infinity <= e r/(r-2) (prod s_j)^(-1/r)` while retaining all self/outside terms.

No arbitrary-joint coarea bound, post-rotation independence, single-minor reciprocal averaging, or law-uniform pointwise quadratic-phase decay is used.

## 2. General aggregate exterior-payment lemma

Let `B` be a real physical cross block and let its nonzero singular values be `s_1,...,s_r`. For an integer `k>=3`, define

`E_k(B)=e_k(BB^T)=sum_{|I|=|J|=k} det(B[I,J])^2`.

Assume `r>k`. Since

`theta(gamma)=sum_nu s_nu^2/(gamma^2+s_nu^2)`

is continuous and strictly decreases from `r` to `0`, there is a unique `gamma_k>0` such that

`theta(gamma_k)=k`.                                            (2.1)

Put

`K=BB^T(gamma_k^2 I+BB^T)^(-1)`,
`D=det(I+BB^T/gamma_k^2)`.

### Theorem 2.1 — `QFORM-EK-EFFECTIVE-DIMENSION-PAYMENT-v1`

If for one physical side of `B` there is `q in [1,2]` with

`max diagonal(K) <= q/2`,  and  `k>2q`,                       (2.2)

then the full quadratic form has a continuous bounded density and

`boxed(
 ||p_Q||_infinity
 <= [e/sqrt(2q)] [k/(k-2q)] E_k(B)^(-1/(2k)).
)`                                                              (2.3)

All arbitrary same-side quadratic blocks, outside couplings, affine terms, and additional spectral directions are retained.

### Proof

Apply `QFORM-RIDGE-DENSITY-v1` at `gamma=gamma_k`. Because `theta=k`,

`||p_Q||_infinity
 <= e/[sqrt(2q) gamma_k] * k/(k-2q) * D^(-1/(2k)).`             (2.4)

The regularized determinant is the generating polynomial of the compound masses:

`D=prod_nu (1+s_nu^2/gamma_k^2)
  =sum_{j=0}^r gamma_k^(-2j) E_j(B)`.

Every term is nonnegative, hence

`D >= gamma_k^(-2k) E_k(B)`.                                  (2.5)

Taking `2k`th roots gives the exact cancellation

`gamma_k^(-1) D^(-1/(2k)) <= E_k(B)^(-1/(2k)).`                (2.6)

Substitute (2.6) into (2.4). QED.

This is the desired aggregate-before-inversion mechanism: it spends the full Cauchy--Binet packet `E_k` through the regularized determinant and never chooses a physical `k x k` minor.

## 3. Third-compound specialization

Take `k=3`. For `r>3`, let `gamma_3` be the unique effective-dimension-three scale `theta(gamma_3)=3`. Let

`rho_L=max_i [BB^T(gamma_3^2I+BB^T)^(-1)]_ii`,
`rho_R=max_j [B^TB(gamma_3^2I+B^TB)^(-1)]_jj`,
`rho=min(rho_L,rho_R)`.

Because the ridge theorem may use either side, Theorem 2.1 gives:

* if `rho<=1/2`, choose `q=1`:

  `||p_Q||_infinity <= (3e/sqrt(2)) E_3(B)^(-1/6)`;            (3.1)

* if `rho<=2/3`, choose `q=4/3`:

  `boxed(
  ||p_Q||_infinity <= 9 e sqrt(3/8) E_3(B)^(-1/6).
  )`                                                             (3.2)

More generally, if `1/2<=rho<3/4`, choosing `q=2rho` yields

`||p_Q||_infinity
 <= [3e/(2 sqrt(rho)(3-4rho))] E_3(B)^(-1/6).`                 (3.3)

Equation (3.3) is not a uniform closure as `rho` approaches `3/4`; (3.2) is the fixed-margin branch used below.

### Exact-rank-three endpoint

If `rank(B)=3`, no finite `gamma` has `theta=3`; instead the previous `QFORM-CROSS-FIBER-PLANCHEREL-v1` applies directly. Since

`E_3(B)=(s_1s_2s_3)^2`,

it gives

`boxed(
 ||p_Q||_infinity <= 3e E_3(B)^(-1/6).
)`                                                              (3.4)

Thus the third-compound resource is paid in exact cross rank three with no leverage assumption at all.

## 4. Application to the designated partner's complete O0 resource

Account03/B07 r16 supplies, on O0,

`E_3(B)>=1/256`.                                                (4.1)

Therefore:

1. If `rank(B)=3`, (3.4) gives

   `||p_Q||_infinity <= 3e * 256^(1/6) <20.549`.               (4.2)

2. If `rank(B)>3` and either physical side has maximum ridge leverage at most `1/2` at the unique `theta=3` scale, (3.1) gives

   `||p_Q||_infinity <14.531`.                                 (4.3)

3. If `rank(B)>3` and either physical side has maximum ridge leverage at most `2/3` at that scale, (3.2) gives

   `boxed(||p_Q||_infinity <37.751).`                           (4.4)

Consequently the entire O0 third-compound branch is now reduced to the genuinely bi-heavy state

`rank(B)>=4`,
`max diag K_L(gamma_3)>2/3`,
`max diag K_R(gamma_3)>2/3`.                                   (4.5)

This is strictly narrower than the preceding generic matching-bank transducer debt. It also preserves all extra spectrum: the analytic theorem is applied to the actual full physical cross block, not to a rank-three surrogate.

## 5. Relation to the partner's colored matching theorem

The r16 colored theorem still has independent value: from the same `E_3>=1/256` it produces three disjoint original-coordinate matching banks and rainbow third-minor mass. The present result shows that these packets need no further local selection whenever the effective-dimension-three ridge geometry is diffuse on either side. Only the bi-heavy ridge state (4.5) needs the pair/replacement/near-coloop geometry developed in the partner's earlier r15 analysis.

In particular, a family may have every individual rainbow minor tending to zero while (4.4) remains dimension-free, because only `E_3` enters. This directly respects the live correction against reciprocal single-packet extraction.

## 6. Why the residual branch is real

The bare lower bound on `E_3` cannot force the ridge-diffuse gate. Already an exact-rank-three diagonal physical cross block has limiting ridge kernel equal to the identity, so its maximum physical leverage is one. Such a block is nevertheless paid by (3.4). Therefore (4.5) is a method boundary, not evidence against QFORM and not a reason to infer that a heavy coordinate itself is harmful.

For rank strictly above three, the next useful implication must exploit the fact that *both* physical sides are heavy at the same effective-dimension-three scale rather than discarding the aggregate determinant weight.

## 7. First unpaid implication after this run

`QFORM-O0-BIHEAVY-RIDGE-COLOOP-PAYMENT-v1`:

Starting from (4.1) and (4.5), use the two physical ridge-heavy coordinates (one on each side), the partner's exact DPP/exclusion identities, and the surviving regularized determinant weight to obtain a universal product-preserving density or half-Riesz bound, or descend to an already-paid exact-rank, scalar-pivot, pair-log, zero-self, or grouped-coordinate branch.

A sufficient structural refinement would be to show that the bi-heavy state forces either a quantitatively conditioned physical pair/edge or a residual cross block with a fixed effective-dimension margin above two after deleting one heavy coordinate. Any such proof must keep the full same-unitary/original-coordinate product provenance and may not replace the aggregate bank by one reciprocal tiny minor.

O1/O2/O3 and scalar-Schur S1/S2 are separate global synthesis debts. Full QFORM is therefore OPEN / not proved / not disproved.

## 8. Deterministic check used

The companion checker tests (2.6) on 200 seeded random singular spectra of ranks 4 through 12 and records the exact O0 constants. Output:

```
random spectral inequality PASS, worst ratio 0.999999305736017
E3>=1/256 factor 2.5198420997897464
rank3 bound 20.548922971333656
rho<=1/2 bound 14.530282779110046
rho<=2/3 bound 37.750782032642554
STATUS=QFORM_E3_RIDGE_AGGREGATE_CHECK_PASS
```

The finite check is only a regression/calibration; the proof is the algebra above.
