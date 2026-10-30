SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B07, 2026-09-24T00:39:45Z.
attacking: the r41 one-overlap diagonal-volume survivor — aggregate its bordered Schur two-volumes into a true physical third compound, close the bounded-support normalized core implication, and isolate the genuinely diffuse rank-two/diagonal-cloud obstruction without choosing one minor.

# fleet02/B07 — one-overlap principal compound, rank-two reduction, and diffuse-core obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / complementary constructions and source-valid counterexamples  
Run: `20260924T003945Z-fleet02-B07-qform-auto11`  
Status: **NEW PRINCIPAL-COMPOUND IDENTITY + LOW-DIAGONAL R2/CLOUD ROUTER + EXACT TARGET-CLASS CORE OBSTRUCTION / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

No moment, support, log-concavity, iid, diagonal-basis, post-rotation independence, or deletion of a small nonzero quadratic tail is used. All banks below are literal original-coordinate banks. The full theorem and full-target continuity remain open.

## 1. Fresh source state and actual incoming partner packet

The current owner control remains revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`, with no B07 pause or reassignment. The live correction ledger was read before publication; in particular no universal good physical minor, no arbitrary-joint coarea estimate, no post-rotation independence and no pointwise scalar stationary-phase bound is used.

The latest completed designated partner consumed is fleet03/B07 r41:

`yspennstate/math-open-problems@56c5b07296ce6fcc66cd3795e425cfad15b27aad`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T233906Z-fleet03-B07-qform-r41/REPORT.md`.

Its one-overlap diagonal-dominant sector has pairwise-disjoint physical banks `H,I,J`. For `h in H`, write

`a_h=A_hh`, `m_h=A[h,J]`, `u_h=A[I,h]`, `K=A[I,J]`,

and

`C_h=K(I-P_{m_h})`, `Z_h=e2(C_h C_h^T)`

(with `C_h=K` if `m_h=0`). Its low-diagonal survivor at `d=1/64` satisfies

`boxed:
W_lo:=sum_{h in H_lo} a_h^2 Z_h > 1/6250,
|a_h|<1/64,
||m_h||<1/64.
}`                                                              (1.1)

Every `h` in this diagonal-dominant set has `a_h!=0`. Its exact scalar Schur `I x J` block is

`R_h=K-a_h^(-1)u_h m_h`,                                         (1.2)

and r41 proves

`e2(R_hR_h^T)>=Z_h`.                                              (1.3)

The required pinned source was reread at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

## 2. New exact identity — the weighted r41 packet is genuine principal third-compound mass

Let

`P=A[H_lo union I union J, H_lo union I union J]`                  (2.1)

be the actual physical principal block. Fix `h in H_lo`, row pair `r<s` in `I`, and column pair `j<k` in `J`. The bordered `3 x 3` minor with row set `{h,r,s}` and column set `{h,j,k}` is

`det [[a_h, m_h[j], m_h[k]],
      [u_h[r], K[r,j], K[r,k]],
      [u_h[s], K[s,j], K[s,k]]]`.

Because `a_h!=0`, the exact bordered Schur determinant identity gives

`det P[{h,r,s},{h,j,k}]
 =a_h det R_h[{r,s},{j,k}].`                                    (2.2)

The row/column triple pair in (2.2) uniquely identifies `h`, so these squared minors are disjoint terms in the Cauchy--Binet expansion of the third compound. Summing first over `r,s,j,k`, then over `h`, yields

`boxed:
e3(P^2)
 =sum_{|R|=|C|=3} det P[R,C]^2
 >=sum_h a_h^2 e2(R_hR_h^T)
 >=sum_h a_h^2 Z_h.
}`                                                               (2.3)

Here `P` is symmetric, so `P^TP=P^2`. On the actual low-diagonal branch,

`boxed: e3(P^2)>1/6250.`                                         (2.4)

This is stronger than an assertion about one bordered determinant: the complete determinant weight has been carried into a real spectral compound of an actual principal block before any inversion or selection.

### Bounded-support normalized core consequence

Suppose a subpacket of mass at least `theta W_lo` is supported on one physical coordinate set `C` of cardinality `m`; equivalently the corresponding bordered minors all lie inside `P_C=A[C,C]`. Then

`e3(P_C^2)>=theta W_lo`.                                         (2.5)

If `s1>=s2>=s3` are the singular values of `P_C`, then

`e3(P_C^2)
 <= binom(m,3) s1^2 s2^2 s3^2`.                                 (2.6)

Hence

`boxed:
s3(P_C)
 >= sqrt(theta W_lo)/[sqrt(binom(m,3)) s1(P_C)s2(P_C)]
 >= 2 sqrt(theta W_lo)/[sqrt(binom(m,3)) ||P_C||_F^2].
}`                                                               (2.7)

In particular, if all entries of this actual `m`-coordinate core are bounded by `L`, then `||P_C||_F^2<=m^2L^2` and

`boxed:
s3(P_C)
 >= 2 sqrt(theta W_lo)/[m^2 L^2 sqrt(binom(m,3))].
}`                                                               (2.8)

Fleet04/B07's completed physical-fiber theorem may then be applied after conditioning only outside `C`; arbitrary outside couplings become affine terms. Thus bounded support plus a genuine coefficient/Frobenius normalization is fully compiled into an actual spectral core. Section 5 below shows that the normalization cannot simply be deleted: constant packet mass alone does not force any bounded-cardinality core.

## 3. New low-diagonal router — paid Z3, quantitative rank-two carrier, or diagonal cloud

Put

`E2=e2(KK^T)`, `E3=e3(KK^T)`,                                    (3.1)

and let `s1(K)>=s2(K)>=...` be the singular values. First, projection is a contraction on the second exterior power, so for every anchor

`Z_h=||wedge^2(K(I-P_{m_h}))||_F^2
    <=||wedge^2 K||_F^2=E2.`                                    (3.2)

Second, there is an exact compound-to-rank-two inequality. Write `x_j=s_j(K)^2` and

`tau_2=sum_{j>=3}x_j=||K-K_2||_F^2`,                             (3.3)

where `K_2` is the best rank-two SVD truncation. Since

`3e3(x)
 =sum_{i<j} x_i x_j sum_{k notin {i,j}} x_k`,                    (3.4)

and `x_i+x_j<=x_1+x_2`, every complement sum in (3.4) is at least `tau_2`. Therefore

`boxed: tau_2 E2 <=3 E3.`                                        (3.5)

This elementary inequality is sharp for equal singular values: if `x_1=...=x_r`, the ratio tends to the factor three appearing above.

Choose the fixed thresholds

`eta=2^(-30)`, `zeta=2^(-12)`.                                   (3.6)

Then the actual partner low-diagonal branch (1.1) satisfies one of the following three alternatives.

### A. Genuine third-volume crossing — analytically paid

If

`E3>=eta`,                                                        (3.7)

then the completed marginal-free physical-Z3 theorem from fleet02/B03 gives the full ambient form a continuous density with

`||p_Q||_infinity
 <=C3 E3^(-1/6)
 <=32 C3
 =337.6054025972728...`,                                         (3.8)

where `C3=3*2^(4/3)*e^(1/3)`.

This application is legitimate even though the anchors couple to `I`: condition on `H_lo` and every coordinate outside `I union J`; all such couplings become arbitrary affine terms, which the theorem allows.

The mandatory pinned-e5 result also applies at a real equation. Under its D' row-marginal gate `max alpha_i<=2/3`, the same actual crossing obeys

`||p_Q||_infinity
 <=9sqrt(3e) E3^(-1/6)
 <=288sqrt(3e)
 =822.432674411177... .`                                         (3.9)

Thus the original pinned theorem already pays the spread subcase; the later marginal-free theorem removes its remaining marginal gate and gives (3.8).

### B. Small third compound but macroscopic second compound — a genuine rank-two tube

If

`E3<eta`, `E2>=zeta`,                                             (3.10)

then (3.5) gives

`boxed:
||K-K_2||_F^2<3*2^(-18)=1.1444091796875e-5,
||K-K_2||_F<sqrt(3)*2^(-9)=0.003382911733533.
}`                                                               (3.11)

This is a deterministic rank-two carrier extraction for the common physical crossing `K`. The nonzero tail in (3.11) is retained; it is not called a negligible quadratic perturbation. Simultaneously every surviving anchor-to-`J` star still satisfies `||m_h||<1/64`.

This lands the r41 survivor directly in the same nonexact rank-two-interface architecture isolated in earlier B07 work, now with a completely explicit absolute Frobenius tail.

### C. Small second compound — a high-cardinality diagonal cloud

If

`E2<zeta`,                                                        (3.12)

then (3.2) and (1.1) imply

`1/6250<W_lo
 <=E2 sum_h a_h^2
 <2^(-12) sum_h a_h^2`.

Therefore

`boxed: sum_h a_h^2>4096/6250=0.65536.`                           (3.13)

Because every `|a_h|<1/64`, every contributing anchor has `a_h^2<1/4096`, so (3.13) forces at least

`boxed: 2685 contributing physical low-diagonal anchors.`         (3.14)

This is not a selected-pivot statement: it is an aggregate physical diagonal-energy cloud. Its internal `H_lo x H_lo` curvature is still arbitrary, so one may not replace (3.13) by a diagonal independent sum without further argument.

Equations (3.8), (3.11), and (3.13) prove the new structural theorem

### `QFORM-R41-LOWDIAG-COMPOUND-R2-OR-CLOUD-v1`

The entire fleet03/B07 r41 low-diagonal packet is either already paid by genuine physical third volume, or its common crossing is quantitatively within `0.003383` in Frobenius norm of rank two, or it contains a physical low-diagonal cloud with squared diagonal energy `>0.65536`. No individual minor is selected and no nonzero tail is discarded.

## 4. Exact target-valid rank-two stress — constant weighted packet does not force a bounded core

The remaining rank-two/cloud alternative is not an artifact of the estimates. It occurs exactly inside the owner target and defeats any attempted bounded-cardinality spectral-core selection.

Let `M` be a multiple of four. On two `M`-coordinate banks `I,J`, choose flat orthonormal pairs

`u_1,u_2 in R^M`, `v_1,v_2 in R^M`,                              (4.1)

with every coordinate of magnitude `M^(-1/2)`, and put

`K_M=u_1 v_1^T+u_2 v_2^T`.                                      (4.2)

Then `K_M` has singular values `1,1`, exactly,

`E2(K_M)=1`, `E3(K_M)=0`,                                       (4.3)

and every physical entry obeys `|(K_M)_{ij}|<=2/M`.

Take an additional `N`-coordinate physical bank `H`, set

`a_N=N^(-1/2)`,                                                  (4.4)

and define the symmetric matrix

`A_{N,M}=
 [[a_N I_H, 0, 0],
  [0,       0, K_M],
  [0,     K_M^T, 0]].`                                          (4.5)

For every `h in H`, `m_h=u_h=0`, hence

`Z_h=E2(K_M)=1`,
`sum_h a_N^2 Z_h=1`.                                            (4.6)

For `N>4096` it lies literally in the r41 low-diagonal scale `|a_h|<1/64`, `||m_h||=0`, with a constant weighted packet and an exact rank-two common crossing.

The nonzero spectrum is

`{+1,+1,-1,-1}` together with `a_N` repeated `N` times.           (4.7)

Thus it has four eigenvalues of modulus one and is an exact full-target family.

Now fix any cardinality bound `L` and any physical principal set `C` with `|C|<=L`. If `p=|C intersect I|` and `q=|C intersect J|`, then

`||K_M[C intersect I,C intersect J]||_op
 <=||.||_F
 <=(2/M)sqrt(pq)
 <=L/M.`                                                         (4.8)

The `H` block is decoupled and has norm `a_N`, so

`boxed:
s3(A_{N,M}[C,C])
 <=max(N^(-1/2),L/M)
 ->0
}`                                                               (4.9)

as `N,M->infinity`, uniformly over all such `C`.

Therefore:

### `QFORM-R41-WEIGHTED-PACKET-BOUNDED-CORE-FALSE-v1`

A constant one-overlap weighted packet, even with an **exact** rank-two physical common crossing and arbitrarily small physical coefficients, does not force a uniformly spectral bounded-cardinality physical principal core. This refutes only that intermediate extraction mechanism, not QFORM.

The required pinned e5 source still gives a real curvature-safe inequality on this family. Conditioning on the cloud `H`, the far `I x J` crossing has `Z2=1`, so the pinned general `D_k` plus fractional-potential lemma gives

`boxed:
H_(1/4)(Q_far | H)<=3.929131771.
}`                                                               (4.10)

The bound is uniform in the conditioned cloud values. It is fractional-potential currency, not a full density estimate; the missing upgrade is precisely the rank-two/cloud receiver exposed by this construction.

## 5. A rank-three diffuse variant is paid by the pinned e5 theorem for the correct reason

To distinguish the structural obstruction from a QFORM counterexample, replace the pair in (4.1) by three flat orthonormal vectors on each side and put

`K_M^(3)=sum_{r=1}^3 u_r v_r^T`,
`a_N=(3N)^(-1/2).`                                                (5.1)

Then

`E2(K_M^(3))=3`, `E3(K_M^(3))=1`,
`sum_h a_N^2 Z_h=1`,                                             (5.2)

while the symmetric bipartite block has three `+1` and three `-1` eigenvalues. Every fixed-cardinality physical principal block again has `s3->0`, since `|(K_M^(3))_{ij}|<=3/M` and `a_N->0`.

For exact rank three the volume-sampling row marginals equal the row leverage of the left singular frame. Here every row marginal is exactly

`alpha_i=3/M`.                                                    (5.3)

For `M>=6`, `alpha_i<=1/2`, and the **pinned e5 Theorem D** applies with `Z3=1`. Conditioning on `H` only adds a constant shift, so

`boxed: ||p_Q||_infinity<=6sqrt(e)=9.89232762420077... .`        (5.4)

Thus the diffuse family is paid by product-law volume smoothing, not by a hidden bounded physical core. This is the exact behavior any valid completion of the rank-two/cloud branch should emulate.

## 6. What is now closed and the first unpaid implication

Three points are now settled for B07.

First, r41's diagonal/projected-two-volume currency is not merely a formal Schur packet: (2.3) embeds it monotonically into the true third spectral compound of an actual physical principal block.

Second, the bounded-support normalized spectral subproblem is explicit in (2.7)-(2.8). If determinant weight genuinely localizes to a bounded physical set with controlled Frobenius/entry scale, fleet04/B07's physical-fiber theorem pays the full ambient law after conditioning outside that set.

Third, the exact family (4.5) proves that **no universal bounded-cardinality core can be inferred from constant weighted packet mass alone**, even after the common crossing has become exactly rank two. The remaining diffuse case must therefore be paid analytically, not by ever finer minor selection.

The sharpened first unpaid implication is

`QFORM-R41-R2-CARRIER-PLUS-DIAGONAL-CLOUD-ROUGH-RECEIVER-v1`:

> Starting from a literal original-coordinate common crossing `K=K_2+T` with the nonzero tail retained (quantitatively `||T||_F<0.003383` on branch B), or from the diagonal cloud `sum_h A_hh^2>0.65536` on branch C, prove a universal density estimate while preserving arbitrary `H x H`, `I x I`, `J x J` curvature, all outside couplings and all additional spectrum. The exact family (4.5) is the mandatory regression: a valid argument may not select a bounded core, delete `T`, or assume the low-diagonal cloud is independent of its internal curvature.

The partner's separate dense-high-edge graph and skew-mismatch packet remain separate debts. Full QFORM is **OPEN / not proved / not disproved**. Full-target continuity is **OPEN**.
