SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T15:57:41Z.
attacking: lift the latest account02/B18 exact-rank-three heavy-anchor closure through genuine original-coordinate conditioning to arbitrary ambient matrices, and pin the exact remaining principal-core collar.

# account01/B18 r33 — ambient principal-core lift of the heavy-anchor closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED SUPPORTING TARGET-LEVEL IMPLICATION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved only on the two Fourier-paid subbranches stated below; otherwise only essential boundedness is claimed.

## 1. Scope and live correction boundary

The owner target remains the unrestricted statement: for arbitrary independent real original-coordinate inputs with densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^T A X`. The unrestricted claim is still OPEN.


The new point is a transfer that is elementary but useful for proof assembly: the latest exact-rank-three partner theorem can be applied **inside an arbitrary ambient matrix** whenever an ORIGINAL-coordinate principal block has the required rank-three geometry. Arbitrary extra spectrum and arbitrary couplings to the conditioned coordinates then disappear into affine terms, which the cited analytic theorems already handle uniformly.

## 2. Primary-source audit

### 2.1 Livshyts--Paouris--Pivovarov: exact linear-map corollary

Livshyts, Paouris and Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1, assumes an actual product probability density `f=prod_i f_i` with `||f_i||_infinity<=1` and proves that every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`.

A direct linear-map corollary, used below as a source boundary, is:

### Lemma 2.1 — product projection under a full-row-rank map

If `X=(X_1,...,X_m)` has independent cap-one coordinates and `L` is a full-row-rank `k x m` matrix, then

`boxed: ||p_(L X)||_infinity <= 2^(k/2) / sqrt(det(L L^T)).`      (2.1)

**Proof.** Write `L=(LL^T)^(1/2) U` with `UU^T=I_k`. The vector `UX` is an orthogonal `k`-dimensional marginal of the product law, so LPP gives `||p_(UX)||_infinity<=2^(k/2)`. The invertible linear change `(LL^T)^(1/2)` multiplies a density by `det(LL^T)^(-1/2)`. If the source dimension equals `k`, the original product density itself is bounded by one, which is even stronger. QED.

For an exact-rank-three Parseval frame `R`, `R^T R=I_3`, and a physical row `u_i` of leverage `c_i=||u_i||^2<1`, apply (2.1) to the residual coefficient map `R_{-i}^T`. Since

`R_{-i}^T R_{-i}=I_3-u_i u_i^T`,
`det(I_3-u_i u_i^T)=1-c_i`,                                      (2.2)

we obtain the exact source-valid estimate

`boxed: ||p_(R_{-i}^T X_{-i})||_infinity <= 2 sqrt(2)/(sqrt(1-c_i)).}` (2.3)

After whitening,

`Z=(I_3-u_i u_i^T)^(-1/2) R_{-i}^T X_{-i}`,                       (2.4)

one has the uniform cap

`boxed: ||p_Z||_infinity <= 2 sqrt(2).}`                           (2.5)

This is a valid product-projection statement. It is **not** fed into the refuted arbitrary-joint indefinite coarea shortcut. Equation (2.3) also explains why the unwhitened projection cap alone is inadequate in the near-coloop limit `c_i->1`.

### 2.2 Quadratic-form regularity literature does not match the owner quantifiers

Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, studies iid inputs which arise as sufficiently smooth functions of a Gaussian field, and its emblematic strong-density convergence theorem assumes further centering/variance/operator conditions. Those hypotheses are substantially stronger than arbitrary non-iid fragmented cap-one densities. I therefore do not import that result as an exact solution of the owner target.

The Fourier endpoints used below are the already completed source-pinned synthesis in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, based on Beckner's sharp Hausdorff--Young theorem and Bennett--Carbery--Christ--Tao/Lieb Brascamp--Lieb Gaussian exhaustion. Its conventions explicitly allow arbitrary affine terms.

## 3. Incoming designated-partner theorem

The latest completed `account02/B18` report is

`yspennstate/math-open-problems@7586eaaa1b31bf811db4a4ab40b0a2ce7c2982c4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T154246Z-account02-B18-QFORM-auto11b/REPORT.md`.

For an exact-rank-three matrix

`B=R M R^T`, `R^T R=I_3`,                                         (3.1)

whose three nonzero eigenvalues have modulus at least one, write `u_k` for the physical rows and `c_k=||u_k||^2`. The partner proves:

1. **Double-heavy transverse closure.** If `c_i>1/2` and for some other ORIGINAL row `j`

`q_j:=||P_(n_i^perp)u_j||^2>1/2`, `n_i=u_i/sqrt(c_i)`,             (3.2)

then

`||p_(X^T B X + affine)||_infinity <363`.                          (3.3)

The proof is affine-uniform: a large scalar pivot uses the scalar square peel plus the rank-two affine half-Riesz theorem; if two pivots are small, an ORIGINAL indefinite physical pair is produced and the pair-log theorem allows arbitrary affine terms.

2. **Exact-null heavy anchor.** If `c_i>1/2` and `B_ii=0`, then

`||p_(X^T B X + affine)||_infinity <363`.                          (3.4)

When in addition every transverse leverage satisfies `q_j<=1/2`, the completed null-hub mixed-Fresnel theorem gives the sharper continuous estimate

`||p||_infinity <=3*2^(4/3)[c_i |det M|]^(-1/3).`                 (3.5)

3. **Large physical pivot.** The completed scalar-pivot implication used in the same report is

`||p||_infinity <=128 [c_i |det M| |B_ii|]^(-1/4).`               (3.6)

All these estimates are for the original independent coordinates and are uniform over deterministic linear and constant terms.

## 4. New theorem — ambient principal-core lift

### Theorem 4.1 — `QFORM-PRINCIPAL-RANK3-ALL-BUT-COLLAR-v1`

Let `A` be an arbitrary real symmetric `n x n` matrix and `X_1,...,X_n` independent with densities at most one. Suppose there is an ORIGINAL-coordinate set `I` such that the principal block

`B=A_[I,I]`                                                        (4.1)

has exact rank three and its three nonzero eigenvalues all have modulus at least `s>0`. Write

`B=R M R^T`, `R^T R=I_3`,                                         (4.2)

and denote its physical rows by `u_k`, `c_k=||u_k||^2`.

Then the full ambient quadratic form `Q=X^T A X` is paid in each of the following cases.

**(A) Diffuse principal core.** If

`max_(k in I) c_k <=1/2`,                                         (4.3)

then `Q` has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <=12/s.`                                 (4.4)

**(B) Heavy exact-null core.** If some `i in I` obeys

`c_i>1/2`, `B_ii=0`,                                               (4.5)

then

`boxed: ||p_Q||_infinity <363/s.`                                 (4.6)

If furthermore all `q_j=||P_(n_i^perp)u_j||^2<=1/2`, then `Q` actually has a continuous `C_0` density and the sharper bound

`boxed: ||p_Q||_infinity <3*2^(5/3)/s
                         =9.5244063118092.../s.`                   (4.7)

**(C) Heavy transverse companion.** If for some `i,j in I`

`c_i>1/2`, `q_j>1/2`,                                             (4.8)

then

`boxed: ||p_Q||_infinity <363/s.`                                 (4.9)

**(D) Heavy non-small physical pivot.** If some `i in I` satisfies

`c_i>1/2`, `|B_ii|>=s/32`,                                        (4.10)

then

`boxed: ||p_Q||_infinity <=256 sqrt(2)/s
                         =362.0386719675.../s <363/s.`             (4.11)

Consequently, after choosing any heavy row `i` when (A) fails, the only state not paid by this theorem is the punctured near-null transverse-diffuse collar

`boxed:
 c_i>1/2,
 0<|B_ii|<s/32,
 ||P_(n_i^perp)u_j||^2<=1/2  for every j in I\{i}.
}`                                                                  (4.12)

The ambient matrix outside `I` is arbitrary: it may have any rank, any additional large or small eigenvalues of either sign, and arbitrary cross couplings to `I`.

### Proof

Condition on the ORIGINAL coordinates `X_(I^c)=y`. Independence gives the unchanged product law on `X_I`; no spectral conditioning occurs. For almost every `y`,

`Q_y(x_I)
 = x_I^T B x_I + b(y)^T x_I + c(y)`,                              (4.13)

where

`b(y)=2 A_[I,I^c] y`,                                             (4.14)

and `c(y)` contains the outside quadratic term. Thus the quadratic matrix in the active independent variables is exactly the principal block `B`; all ambient cross couplings become a deterministic affine perturbation.

Scale (4.13) by `s`: the matrix `B/s` has its three nonzero eigenvalues of modulus at least one, while the frame rows, leverages `c_k`, and transverse leverages `q_j` are unchanged. Every source theorem in Section 3 is uniform in the affine term `b(y)/s`.

For (A), diagonalize `M=O Lambda O^T`. The frame `RO` still has orthonormal columns and the same row leverages. The completed Fresnel--Brascamp--Lieb Theorem F applies to the conditional polynomial (4.13), with arbitrary affine term, and gives

`||p_(Q_y)||_infinity
 <=12 |det M|^(-1/3)
 <=12/s`                                                          (4.15)

uniformly in `y`.

For (B), apply the designated partner exact-null theorem to `B/s`; its conditional density cap is `<363` for `Q_y/s`, hence `<363/s` for `Q_y`. In the transverse-diffuse subcase, (3.5) and `|det M|>=s^3`, `c_i>1/2`, give

`||p_(Q_y)||_infinity
 <=3*2^(4/3)[c_i |det M|]^(-1/3)
 <3*2^(5/3)/s.`                                                    (4.16)

For (C), apply the partner's `QFORM-DOUBLEHEAVY-TRANSVERSE-CLOSURE-v1` to `B/s`, obtaining `<363` for the scaled conditional output and therefore `<363/s` for `Q_y`.

For (D), use (3.6) directly. Since `c_i>1/2`, `|det M|>=s^3`, and `|B_ii|>=s/32`,

`c_i |det M| |B_ii|
 >= (1/2) s^3 (s/32)
 = s^4/64`,                                                        (4.17)

so

`||p_(Q_y)||_infinity
 <=128 (s^4/64)^(-1/4)
 =256 sqrt(2)/s.`                                                  (4.18)

All these conditional bounds are uniform in `y`. Therefore, for every Borel set `E subset R`,

`P(Q in E)
 = E_y P(Q_y in E)
 <= C_s |E|,                                                       (4.19)

with the corresponding `C_s` above. Hence the unconditional law is absolutely continuous with essential density cap `C_s`. This proves the bounded-density assertions.

The alternative list is exhaustive after fixing a heavy row: if (A) fails, choose `i` with `c_i>1/2`; if its pivot is zero use (B), if its magnitude is at least `s/32` use (D), if it is nonzero and smaller but some transverse leverage exceeds `1/2` use (C), and otherwise (4.12) holds. QED.

## 5. Continuity lifts separately, without mixing it into essential boundedness

For branch (A), Theorem F gives conditionally, uniformly in the outside value and affine term,

`|phi_(Q_y)(t)|
 <= min(1,(4pi)^(3/2)|det M|^(-1/2)|t|^(-3/2)).`                  (5.1)

The right side is integrable. Since

`phi_Q(t)=E_y phi_(Q_y)(t)`,                                      (5.2)

we have the same integrable envelope for `|phi_Q(t)|`. Fourier inversion therefore gives a continuous `C_0` density for the full ambient form.

For the transverse-diffuse exact-null subcase of (B), the source null-hub theorem likewise supplies the uniform affine-stable `|t|^(-3/2)` envelope whose determinant currency is `c_i|det M|`; averaging over `y` preserves it. This proves the continuity assertion in (4.7).

The double-heavy/pair-log and generic exact-null `<363/s` branches are used only as essential-density estimates here. I do not infer continuity from them.

## 6. Actual designated-partner application and what it buys

The main target-level application of account02/B18 is equation (4.9): **the partner's exact-rank-three double-heavy theorem now controls the full arbitrary ambient quadratic form whenever one exact-rank-three ORIGINAL principal core has a heavy row and a transverse-heavy companion**. The outside spectrum does not need to be small, separable or low rank; conditioning converts it only into the affine term (4.13), which the partner theorem accepts.

Likewise, the partner's exact-null heavy-anchor completion yields (4.6) in the arbitrary ambient setting. This is strictly broader than reading those partner statements as theorems only for globally exact-rank-three matrices.

The price is structural: the bare hypothesis `s_3(A)>=1` does not automatically produce an ORIGINAL principal block satisfying (4.1) with `s` bounded below by a universal constant. Live counterexamples already rule out a naive fixed-good-minor dichotomy. Thus Theorem 4.1 is a genuine target-level implication, not a full solution.

## 7. Sharpened local debt

Inside any exact-rank-three principal core of scale `s`, all geometry is now paid except (4.12). The first local implication to attack is therefore precisely

`QFORM-PRINCIPAL-NEARNULL-TRANSVERSE-DIFFUSE-COLLAR-v1`:

retain the small but nonzero Rayleigh coefficient in (4.12) and obtain a bound `C/s` without paying a negative power of `|B_ii|`, or route the collar into another product-preserving paid packet. The exact-zero endpoint is already continuous by (4.7), while perturbatively setting `B_ii=0` is not allowed for arbitrary unbounded inputs.

The LPP whitening identity (2.5) is relevant but does not by itself close this step: the live correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` forbids converting a bare bounded three-dimensional joint density into the desired indefinite quadratic density estimate. Any successful use of (2.5) must retain additional product/Fourier structure through the curved trace.

## 8. Literature boundary and status

The primary anti-concentration theorem of LPP transfers exactly as (2.1)--(2.5). The Herry--Malicet--Poly quadratic-form regularity theorem does not match the arbitrary non-iid cap-one quantifiers. I found no primary theorem in this targeted audit that directly settles all owner quantifiers; this is a hypothesis comparison, not a novelty claim based on search absence.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**New proved implication:** `QFORM-PRINCIPAL-RANK3-ALL-BUT-COLLAR-v1`.  
**Designated partner used:** account02/B18 r33 theorem at the actual inequalities (4.6) and (4.9).  
**Continuity:** proved on (A) and the transverse-diffuse exact-null subbranch of (B), tracked separately elsewhere.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

No schedule, enabled/paused state, notification/email setting, task identity, cross-account authorization, repository visibility, permission, paid/remote call or public-release state was changed.
