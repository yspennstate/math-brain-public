SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-24T02:12:49Z.
attacking: the account03/B19 r46 star-aligned rank-two collar; sharpen it bilaterally, then exploit the full bordered two-anchor physical cross block when the anchors are distinct.

# account02/B19 r11 — bilateral two-star collar and bordered-E3 tradeoff

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL STRUCTURAL STEP / NEW PHYSICAL-E3 SUBBRANCH / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact target remains: independent real ORIGINAL coordinates with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concave, diagonal-basis, post-rotation-independence, conditional-density-cap, small-random-error, or arbitrary-joint-coarea assumption is used. Continuity is claimed only on cited Fourier-L1 physical-volume branches.

## 1. Sources actually consumed

Fresh owner control at startup was `math-research-brain@7cf1634e4f95be0030b1485d77ef830f410b17de`, OWNER CONTROL revision `2026-09-22.15`, with the QFORM-only continuation active and no later stop. The newest completed designated partner at the first source refresh was account03/B19 r46:

`yspennstate/math-open-problems@628222e360badf19079bf4e36c2122d894669e57`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T010216Z-account03-B19-QFORM-r46/REPORT.md`.

Its theorem `QFORM-TWOSTAR-TO-ALIGNED-R2-OR-E3-v1` starts from disjoint physical banks `R,C`, physical anchors `p,q` outside them (possibly `p=q`),

`N=A[R,C]`, `u=A[R,p]`, `v=A[q,C]`, `delta=||u|| ||v||`,

with the live packet satisfying

`delta>=2/9`.                                                     (1.1)

For a literal appended-star physical cross block it proves the exact exterior identity and then either the completed physical-E3 receiver pays, or `N` lies within `0.076547` Frobenius distance of a rank-two matrix containing the stronger literal star direction exactly.

The owner-pinned completed source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`

was reread. In particular its marginal-free D5 theorem states, for every literal physical cross block `M`,

`||p_Q||_infinity <=5 sqrt(2e) e5(M^T M)^(-1/10)`,                (1.2)

with all same-bank curvature, affine terms, outside couplings and extra spectrum retained.

I also use the current account02/B20 one-anchor checkpoint (present at math master source refresh `73f5015193de11d14a7c7c1c53a98d7250d47fd0`) and the source-valid `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1` in account02/B06 (`math-open-problems@434d3ab3168164b38fdba61456e35e747a67bea3`) only to state the remaining graph correctly; no unsupported `H_{1/2}=>L^infinity` promotion is made.

## 2. A sharp rank-one-tail inequality

For any real matrix `W`, let its squared singular values be

`x_1>=x_2>=...>=0`,

and write

`d_1(W)^2=sum_(j>=2)x_j=dist_F(W,{rank<=1})^2`.

Then

`boxed: d_1(W)^4 <=2 e2(WW^T).`                                  (2.1)

Indeed,

`x_1 sum_(j>=2)x_j >=sum_(j>=2)x_j^2`,

so

`2e2=x_1*2sum_(j>=2)x_j+2sum_(2<=i<j)x_i x_j
     >=(sum_(j>=2)x_j)^2`.

This is dimension-free and exact enough for the partner packet.

## 3. New theorem: both physical appended stars constrain the survivor

Put

`e=u/||u||`, `f=v/||v||`,

and define the two literal physical third volumes

`Z_L=E3([N u])`,
`Z_R=E3([N;v^T])`,                                                (3.1)

where `E3(M)=e3(MM^T)`. Both blocks are genuine disjoint original-coordinate cross blocks even when `p=q`: the first uses rows `R`, columns `C union {p}`, while the second uses rows `R union {q}`, columns `C`.

The r46 appended-star identity, applied on both sides, gives

`Z_L >= ||u||^2 e2((P_e^perp N)(P_e^perp N)^T)`,
`Z_R >= ||v||^2 e2((N P_f^perp)^T(N P_f^perp)).`                  (3.2)

Define

`eta_L=dist_F(P_e^perp N,{rank<=1})`,
`eta_R=dist_F(NP_f^perp,{rank<=1})`.                              (3.3)

Combining (2.1) and (3.2),

`eta_L^4 <=2Z_L/||u||^2`,
`eta_R^4 <=2Z_R/||v||^2`,

and hence

`boxed:
 (eta_L eta_R)^4 <=4 Z_L Z_R/delta^2.
}`                                                                (3.4)

### Theorem 3.1 — `QFORM-TWOSTAR-BILATERAL-R1-DEFECT-PRODUCT-v1`

On the live packet (1.1), if either `Z_L` or `Z_R` is at least `2^-18`, the already-completed physical-E3 theorem pays the full law continuously by

`||p_Q||_infinity<=82.760672`.                                    (3.5)

Therefore every still-unpaid physical two-star state has both `Z_L,Z_R<2^-18`, and (3.4) gives

`boxed:
 eta_L eta_R <3/512=0.005859375.
}`                                                                (3.6)

In particular

`min(eta_L,eta_R)<sqrt(3/512)=0.07654655446197431...`,             (3.7)

which recovers the one-sided r46 collar, but (3.6) is strictly stronger: the two opposite star-transverse rank-one defects cannot both stay quantitatively large.

If `b` is a leading left singular direction of `P_e^perp N` and `d` a leading right singular direction of `NP_f^perp`, define the literal opposite-star off-plane leakages

`ell_L=||P_b^perp P_e^perp N f||`,
`ell_R=||P_d^perp P_f^perp N^T e||`.                              (3.8)

Best rank-one approximation immediately gives `ell_L<=eta_L`, `ell_R<=eta_R`, hence

`boxed: ell_L ell_R<3/512.`                                      (3.9)

Thus robust bilateral off-axis leakage is eliminated without rotating random variables or deleting either tail. The surviving two-star geometry is quantitatively one-sided / moving-ridge.

## 4. Distinct anchors: the full bordered physical block gives more

Assume now `p!=q`, and put

`b=A_qp`.

There is then a genuine literal physical cross block

`B=A[R union {q}, C union {p}]
  =[[N,u],[v^T,b]].`                                               (4.1)

Let

`C_0=P_e^perp N P_f^perp`, `F=||C_0||_F`,

and let `D_pq` be the sum of squares of the `3x3` minors of `B` that use both the appended physical row `q` and appended physical column `p`. Clearly

`D_pq<=E3(B)`.                                                     (4.2)

### Lemma 4.1 — `QFORM-TWOSTAR-BORDERED-E3-TRANSVERSE-TRADEOFF-v1`

One has the exact norm comparison

`boxed:
 |delta F-|b| sqrt(E2(N))| <=sqrt(D_pq)
 <=delta F+|b| sqrt(E2(N)).
}`                                                                (4.3)

#### Proof

Make deterministic orthogonal changes only in the coefficient row space `R` and column space `C`, sending

`u=||u|| e_1`, `v=||v|| f_1`.

These changes are used solely to compute Euclidean minor norms; no random coordinate is rotated or called independent. For every row pair `I subset R`, column pair `J subset C`, the bordered minor using `q,p` is

`det [[N[I,J],u_I],[v_J^T,b]]
 = b det N[I,J]-v_J^T adj(N[I,J])u_I`.                             (4.4)

Regard all these minors as one vector indexed by `(I,J)`. The first summand in (4.4) has Euclidean norm

`|b| sqrt(E2(N))`.                                                 (4.5)

The second is nonzero only when the selected row pair and column pair both contain their first basis vector. For `I={1,i}`, `J={1,j}` it equals, up to sign,

`||u||||v|| N_ij=delta N_ij`,

with `i,j` transverse. Its Euclidean norm is therefore exactly

`delta ||P_e^perp N P_f^perp||_F=delta F`.                        (4.6)

The triangle and reverse-triangle inequalities in this minor-vector space prove (4.3). QED.

### Consequence at the live E3 threshold

If

`E3(B)>=2^-18`,                                                   (4.7)

the full ambient law is again paid by (3.5). Hence every distinct-anchor survivor satisfies, by (4.2)-(4.3),

`boxed:
 delta F < |b| sqrt(E2(N))+2^-9.
}`                                                                (4.8)

Using `delta>=2/9`, this gives the explicit dichotomy

`boxed:
 |b| sqrt(E2(N))>=2^-9
 
 OR
 
 F<9/512=0.017578125.
}`                                                                (4.9)

At the exact zero shared edge `b=0`, the stronger exact conclusion is

`boxed: F<9/1024=0.0087890625.`                                   (4.10)

This directly removes a substantial part of the distinct-anchor r46 collar: after the literal E3 exits, either the *double-transverse* physical crossing is tiny, or the remaining quantitative currency is the weak-edge/large-E2 product `|A_pq| sqrt(E2(N))`.

The latter must not be paid by silently assuming its E2 survives a pair Schur complement: account02/B07 supplied an exact target-class construction where a large pre-completion E2 packet collapses to rank one after pair completion. Thus (4.9) is a genuine sharpened debt rather than a hidden closure.

## 5. Required owner-pinned D5 result applied at equation level

Apply (1.2) to each actual literal appended-star physical block in (3.1), and, when `p!=q`, also to the full bordered block (4.1). If any such block `M` satisfies

`E5(M)>=2^-20`,                                                    (5.1)

then

`boxed:
 ||p_Q||_infinity
 <=5sqrt(2e)(2^-20)^(-1/10)
 =20sqrt(2e)
 =46.63287963194249... .
}`                                                                (5.2)

Thus every survivor in this run's two-star chamber may assume `E5<2^-20` for all these actual physical blocks. This is the required equation-level application of the owner-pinned completed source and retains arbitrary same-bank curvature, all signs, affine terms and additional spectrum.

## 6. Updated source-pinned proof graph

The current global route is now sharper but still conditional.

1. The third-compound operator funnel (account01/B07 r38) sends every target matrix into a principal physical triple, a disjoint physical E3 block, a one-anchor overlap-one packet, or a physical-pair overlap-two packet. Principal-triple and sufficiently large physical E3 exits are paid.
2. The pair compiler account03/B19 r45 pays a strong shared edge and reduces the weak pair to literal E2 / one-anchor / two-star / giant-rank-one currencies.
3. The E2 chamber is refined by account03/B20 r43: after the physical-E3 exit it is an ultra-thin robust-rank-two tube or a giant near-rank-one tube; its nonzero tail is retained.
4. The one-anchor chamber is refined by the current account02/B20 checkpoint: medium-small nonzero pivots are paid exactly by scalar Schur plus E2 half-Riesz; the remaining states are a tiny-pivot giant-E2 rank-two tube or a transverse-degeneracy collar. Exact rank-one shared-hub geometry is paid; finite leakage remains.
5. The physical two-star chamber is refined by account03/B19 r46 and this run. After the literal E3/D5 exits, it obeys the bilateral product collar (3.6). If the anchors are distinct, it also obeys the bordered tradeoff (4.9); if the shared edge is zero, the double-transverse corner is <`9/1024`.
6. If the two anchors coincide, the bordered block (4.1) is not a disjoint physical cut and cannot be used. The first surviving geometry is therefore the same-hub one-sided moving-ridge collar (3.6),(3.9), with arbitrary same-bank curvature and all nonzero tails retained.

No step above converts finite E2 half-Riesz credit alone into a density: the rank-two logarithmic saddle correction remains active. No small coefficient tail is dropped.

## 7. First remaining implication after this run

The first local synthesis gap is now

`QFORM-TWOSTAR-ONESIDED-OR-WEAKEDGE-E2-PAYMENT-v1`:

> Under the full arbitrary rough product target and after the completed physical E3/D5 exits, pay either
> (a) the shared-anchor / one-sided moving-ridge packet with `eta_L eta_R<3/512` (and hence `ell_L ell_R<3/512`), retaining arbitrary same-bank curvature and the complete nonzero tail; or
> (b) for distinct anchors, the weak-edge/large-E2 branch `|A_pq| sqrt(E2(A[R,C]))>=2^-9`, without assuming this raw E2 survives pair completion;
> or force an already-paid scalar/pair, grouped-hub, Fresnel, physical-volume, ridge/window, or inductive principal-block exit.

The complementary distinct-anchor branch with small weak-edge/E2 product already has

`||P_u^perp A[R,C] P_v^perp||_F<9/512`,

and at zero shared edge `<9/1024`; it should be spliced into the existing rank-one shared-hub tensor and one-sided leakage machinery rather than treated as an arbitrary bounded joint compression. The account04/B19 moving-ridge counterexample rules out that compression shortcut.

The global arbitrary-extra-spectrum bridge and unrestricted continuity remain separate debts. A full candidate still requires all target quantifiers and two independent end-to-end reviews; neither exists.

## 8. Status

- `QFORM-TWOSTAR-BILATERAL-R1-DEFECT-PRODUCT-v1`: **PROVED supporting structural theorem**.
- `QFORM-TWOSTAR-BORDERED-E3-TRANSVERSE-TRADEOFF-v1`: **PROVED structural identity/inequality**.
- New full-law paid subbranches: literal physical E3 gate `<=82.760672`; literal D5 gate `<=46.632880`.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
