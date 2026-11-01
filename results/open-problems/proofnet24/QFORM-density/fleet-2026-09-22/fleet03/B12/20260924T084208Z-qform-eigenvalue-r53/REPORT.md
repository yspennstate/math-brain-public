SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T08:42:08Z.
attacking: signed destructive interaction of arbitrary added eigenvalue packets on a literal original-coordinate carrier, rather than unsigned range-angle or operator-norm control.

# fleet03/B12 — signed anticommutator destructive-index stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T084208Z-qform-eigenvalue-r53`  
Status: **NEW SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The owner target remains the unrestricted product-law conjecture: independent real ORIGINAL coordinates `X_i`, each with a probability density bounded by one, and an arbitrary real symmetric coefficient matrix `A` with at least three eigenvalues of absolute value at least one. No Gaussianity, log-concavity, moment, support, iid, smoothness, diagonal-basis, or post-rotation-independence assumption is used.

This run deliberately changes mechanism after the recent relative-resonance / subspace-angle sequence. The new invariant is **signed**: only the negative part of the normalized local anticommutator can destroy protected carrier modes. Arbitrarily large constructive aligned spectrum and arbitrary transverse local action are free.


Two completed inputs are used at equations:

1. **Designated partner fleet04/B12 r9**, `yspennstate/math-open-problems@71b7db02d3bd2f5cb6bf07e800caa6bd13a1a3e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T021341Z-fleet04-B12-resonance-repair-r9/REPORT.md`. Its exact-resonance physical carrier in Section 4 has six orthogonal columns of norm two.
2. **Five-square-mode density compiler**, fleet03/B12 r47, `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`. For an ORIGINAL-coordinate carrier `H` of size `m>=5`, if `lambda_5((A^2)[H,H])>=h^2>0`, then

`||p_(X^TAX)||_infinity <= sqrt(24*pi*m+K_3^2)/h`,  
`K_3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,

and the density has a representative in `C_0(R)`.

## 2. First missing implication: sign matters inside a completely aligned added packet

The previous principal-angle theorem is intentionally unsigned: if the added carrier image equals the old carrier image, every canonical correlation is one and its lower bound vanishes, even if almost all of the aligned addition is strongly constructive. We therefore keep the exact relative **signed** interaction instead of only the two ranges.

Let `M in R^(n x m)` have full column rank and put

`G=M^T M`,  `g=s_m(M)>0`,  `U=M G^(-1/2)`.

Then `U^T U=I_m`. For arbitrary `N in R^(n x m)`, define

`B=U^T N G^(-1/2)=G^(-1/2) M^T N G^(-1/2)`,

and let

`H=(B+B^T)/2`,

with eigenvalues in increasing order

`mu_1<=mu_2<=...<=mu_m`.

### Theorem 2.1 — `QFORM-SIGNED-ANTICOMMUTATOR-MODE-STABILITY-v1`

For every `q=0,...,m-1`,

`boxed: s_(m-q)(M+N) >= g (1+mu_(q+1))_+.`                    (2.1)

Thus `q` arbitrarily destructive normalized directions may be spent, while the `(q+1)`st signed interaction controls the next surviving carrier mode. No norm or rank bound on `N` appears.

### Proof

Set

`C=N G^(-1/2)`.

Orthogonally decompose the codomain action as

`C=U B+Z`,  `U^T Z=0`.

Since `M G^(-1/2)=U`,

`(M+N)G^(-1/2)=U(I+B)+Z`.

The two summands are orthogonal in the codomain, hence exactly

`[(M+N)G^(-1/2)]^T[(M+N)G^(-1/2)]
  =(I+B)^T(I+B)+Z^T Z`.                                       (2.2)

Therefore

`s_k((M+N)G^(-1/2)) >= s_k(I+B)`                              (2.3)

for every `k`. Multiplying on the right by `G^(1/2)` and using the standard product inequality gives

`s_k(M+N) >= g s_k(I+B)`.                                     (2.4)

Let `L_q` be the span of the eigenvectors of `H` belonging to `mu_(q+1),...,mu_m`; it has dimension `m-q`. For `y in L_q`, if `1+mu_(q+1)>0`, Cauchy-Schwarz and the definition of `H` give

`||(I+B)y|| ||y||
 >= y^T(I+B)y
 = ||y||^2+y^T H y
 >= (1+mu_(q+1))||y||^2`.                                     (2.5)

Hence the minimum expansion of `I+B` on this `(m-q)`-dimensional subspace is at least `1+mu_(q+1)`. The singular-value min-max principle yields

`s_(m-q)(I+B)>=1+mu_(q+1)`.

If `1+mu_(q+1)<=0`, the claimed positive-part lower bound is trivial. Combining with (2.4) proves (2.1). QED.

### Sharpness

If `N=kappa M`, then `B=H=kappa I` and

`s_m(M+N)=|1+kappa|g`.

For `kappa>=-1`, (2.1) is equality. The threshold `kappa=-1` is genuine exact cancellation. More generally, on an orthogonal carrier with diagonal relative multipliers, spending the most negative modes makes (2.1) exact mode-by-mode.

The theorem also explains why a very large aligned addition need not be dangerous: if `H>=0`, then

`boxed: s_m(M+N)>=s_m(M)`                                     (2.6)

with no restriction at all on `||N||`.

## 3. QFORM form: the normalized local anticommutator

Let `H0` be `m` literal ORIGINAL coordinates and let `P:R^m->R^n` be the coordinate embedding. Let `A_*` and `E` be real symmetric matrices and put

`M=A_*P`, `N=EP`, `G=P^T A_*^2 P=M^TM`.

Assume `M` has full column rank. Then the symmetric interaction matrix in Theorem 2.1 is

`H_E
 = (1/2) G^(-1/2) P^T(A_*E+EA_*)P G^(-1/2)`.              (3.1)

This is a normalized **local anticommutator**. Since `A_*+E` is symmetric,

`(M+N)^T(M+N)=P^T(A_*+E)^2P=((A_*+E)^2)[H0,H0]`.

Therefore Theorem 2.1 becomes

`boxed:
 sqrt(lambda_(m-q)(((A_*+E)^2)[H0,H0]))
 >= g (1+mu_(q+1)(H_E))_+.`                                  (3.2)

This is purely a deterministic statement about the final coefficient matrix. The random vector is never rotated and `X^TEX` is never treated as an independent convolution factor.

## 4. Many arbitrary signed packets: spend only destructive rank and tail

Now let

`A=A_* + sum_(ell=1)^L E_ell + T`,                             (4.1)

where every `E_ell` and `T` is real symmetric. There is no global rank, sign, eigenvalue-size, or eigenvector-orientation restriction on the `E_ell`.

For each packet define the normalized local anticommutator `H_ell` by (3.1), and its negative part

`D_ell=(-H_ell)_+ >=0`.

Choose integers `q_ell>=0`, set

`Q=sum q_ell`,

and, with eigenvalues of `D_ell` in decreasing order, set

`eta_ell=s_(q_ell+1)(D_ell)`,

with `eta_ell=0` if `q_ell` reaches the rank. Put

`eta=sum eta_ell`.

### Theorem 4.1 — `QFORM-DESTRUCTIVE-ANTICOMMUTATOR-BUDGET-v1`

If `Q<=m-1`, then before the final tail `T`,

`boxed:
 s_(m-Q)((A_*+sum E_ell)P) >= g(1-eta)_+.`                    (4.2)

If additionally

`epsilon=||TP||_op`,

then

`boxed:
 sqrt(lambda_(m-Q)((A^2)[H0,H0]))
 >= [g(1-eta)-epsilon]_+.`                                    (4.3)

### Proof

For each `ell`, truncate `D_ell` to its top `q_ell` eigendirections:

`D_ell=D_ell^(q)+R_ell`,

where `rank D_ell^(q)<=q_ell` and `0<=R_ell<=eta_ell I`. Since `H_ell>=-D_ell`, summing gives

`sum H_ell >= -D-eta I`,

where

`D=sum D_ell^(q)`, `rank D<=Q`.                                (4.4)

On `ker D`, a subspace of dimension at least `m-Q`, the Rayleigh quotient of `sum H_ell` is at least `-eta`. Therefore, for the increasing eigenvalues of `sum H_ell`,

`mu_(Q+1)(sum H_ell)>=-eta`.                                  (4.5)

Theorem 2.1 with `N=(sum E_ell)P` and `q=Q` proves (4.2). Rectangular Weyl for the added local tail `TP` proves (4.3). QED.

### Interpretation

This budget is signed and finite-codimensional:

- arbitrarily large **constructive** anticommutator spectrum is completely free;
- `Q` arbitrarily severe destructive directions are completely spent;
- only the first unspent negative anticommutator eigenvalue of each packet is charged;
- arbitrary transverse carrier action is free because it contributes the positive term `Z^TZ` in (2.2);
- no small coefficient matrix is reinterpreted as a small random quadratic error.

This differs materially from an operator-norm perturbation theorem and from the preceding principal-angle theorem: it can succeed even when the old and new carrier images coincide exactly.

## 5. Density-level corollary

Assume `m-Q>=5` and define

`h=g(1-eta)-epsilon>0`.                                       (5.1)

Then (4.3) implies

`lambda_5((A^2)[H0,H0])>=h^2`.

Applying the completed five-square-mode compiler gives

`boxed:
 ||p_(X^TAX)||_infinity
 <= sqrt(24*pi*m+K_3^2)/h,`                                  (5.2)

and the density has a representative in `C_0(R)`.

Thus the signed anticommutator stability theorem is an end-to-end density compiler whenever five physical square-energy modes survive. This is still a supporting theorem: the bare hypothesis `s_3(A)>=1` is not proved to force such a carrier/budget.

## 6. Required fleet04/B12 application: full range alignment, one exact cancellation, unbounded mixed-sign spectrum

Use the exact physical carrier proved in designated partner fleet04/B12 r9. In its Section 4 take `n=12`,

`H0={1,...,6}`,

and let `A_*` denote the partner's matrix after its exact resonant rank-one packet. The partner proves literally

`A_* e_1=-2e_1`,

`A_* e_j=2e_(6+j)` for `j=2,...,6`,                           (6.1)

so the six columns of

`M_*=A_*P_H`

are orthogonal and all have norm two. In particular

`boxed: s_6(M_*)=2,  G=4I_6.`                                (6.2)

This is the required equation-level use of the completed partner result.

Fix any `L>=3` and define relative multipliers

`kappa=(-1,-1/4,L,L^2,3,L^3)`.                               (6.3)

Construct one real symmetric added matrix `G_L` by

`(G_L)_(1,1)=2`,

`(G_L)_(j,6+j)=(G_L)_(6+j,j)=2 kappa_j` for `j=2,...,6`,

and zero in all other entries relevant here. Then

`G_L P_H=M_* diag(kappa)`.                                    (6.4)

Every `kappa_j` is nonzero, so

`Ran(G_LP_H)=Ran(M_*)`.

Hence **all six canonical correlations are exactly one**. The previous unsigned principal-angle shield supplies no positive mode at all on this example.

By contrast, the normalized signed interaction is exactly

`B=H=diag(kappa)`.                                            (6.5)

Its negative part has eigenvalues `1,1/4,0,0,0,0`. Spend the single exact-cancellation direction (`q=1`), leaving `eta=1/4`. Theorem 4.1 gives

`boxed:
 s_5((A_*+G_L)P_H) >= 2(1-1/4)=3/2.`                         (6.6)

In fact this is sharp. The six exact carrier singular values are

`2|1+kappa_j|`,

namely, in decreasing order for `L>=3`,

`2(1+L^3), 2(1+L^2), 2(1+L), 8, 3/2, 0`.                    (6.7)

Thus `s_5=3/2` exactly.

The added symmetric packet has genuinely arbitrary large spectrum of both signs: for each `j>=2` the physical pair `(j,6+j)` contributes eigenvalues `+2|kappa_j|` and `-2|kappa_j|`, while the first coordinate contributes eigenvalue `2`. As `L->infinity`, positive and negative added eigenvalues diverge at three different scales. The theorem is insensitive to those constructive magnitudes.

Finally add any symmetric `T` satisfying only the **local** condition

`||TP_H||_op<=1/10`.                                          (6.8)

There is no bound on the global `||T||`, its outside-outside spectrum, signs, or rank. Equation (4.3) gives

`boxed: s_5(AP_H)>=3/2-1/10=7/5.`                             (6.9)

Since restriction of the domain cannot increase singular values,

`s_5(A)>=s_5(AP_H)>=7/5`,

so the final matrix has at least five, hence at least three, eigenvalues of absolute value greater than one and is genuinely inside the owner target class.

With `m=6`, the five-mode compiler constant is

`sqrt(144*pi+K_3^2)=23.74227041550599...`.

Therefore

`boxed:
 ||p_Q||_infinity
 <= 23.74227041550599/(7/5)
 =16.95876458250428... <16.959.`                              (6.10)

The density has a representative in `C_0(R)`. Without the final local tail, the sharp carrier value `h=3/2` gives `<15.829`.

This example is intentionally hostile to the previous unsigned mechanism: the added packet has the **same entire carrier image** as the baseline and unbounded mixed-sign spectrum, yet only its two genuinely negative relative interactions matter; one is spent and the other costs `1/4`.

## 7. Deterministic computation

`check_signed_anticommutator.py` performs two independent seeded matrix checks.

1. **Single arbitrary symmetric packet.** 10,000 random symmetric baselines and additions were generated on a six-coordinate physical carrier. Inequality (2.1) was checked for every `q=0,...,5`, for 60,000 singular-index tests total. Violations: `0`. Minimum numerical margin: `0.24701044984881626`.
2. **Three-packet destructive budget.** 10,000 random symmetric baselines and three symmetric packets were generated; one destructive direction per packet was spent (`q_ell=1`). Inequality (4.2) was checked against the actual aggregate final carrier. Positive right-hand side occurred in all 10,000 tests. Violations: `0`. Minimum numerical margin: `1.102979283834014`.
3. **Partner hostile family.** At `L=10^6`, the exact carrier singular values were

`2e18, 2000000000002, 2000002, 8, 1.5, 0`,

and the theorem gives `s_5>=1.5`, equality. With local tail budget `0.1`, the certified reserve is `1.4`, giving density cap `16.95876458250428...`.

These are consistency checks only. The proof is the exact orthogonal Gram decomposition (2.2), a min-max estimate for the symmetric part, and a finite-rank truncation of the negative anticommutator.

## 8. Exact remaining gap

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

This run proves a new dependence-safe stability principle for extra spectrum: magnitude and even complete range alignment are not themselves hostile; only sufficiently many negative normalized anticommutator directions can destroy the carrier.

The next B12 structural implication is therefore sharper. Starting solely from `s_3(A)>=1`, one must either:

1. extract a bounded ORIGINAL-coordinate carrier and a decomposition into a baseline plus added packets whose normalized anticommutator negative part has a bounded finite-codimension tail, leaving five square-energy modes; or
2. show that failure forces many independent destructive directions, and convert that certificate into one of the already-paid physical-pair, projected-crossing, grouped-bank, ridge, hub/common-plane, Schur, or Pluecker-volume receivers.

The full theorem's continuous-density conclusion is not established. Continuity is proved only for the positive five-mode branch (5.2)/(6.10).

## 9. Source pins and integrity

- Designated partner: `yspennstate/math-open-problems@71b7db02d3bd2f5cb6bf07e800caa6bd13a1a3e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T021341Z-fleet04-B12-resonance-repair-r9/REPORT.md`.
- Density receiver: `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`.
- Latest Claude continuation observed this run: `math-open-problems@8edfa020d8904154efd9488a01828e22e2e7b2d4`, `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/`.

Manual changed-file privacy review: this run contains only mathematical formulas, deterministic test code/results, logical fleet labels, source commits and repository-relative paths. No credentials, tokens, personal archives, client/company/trading data, private machine paths, or public-release action is included. No installation or external workflow was used.
