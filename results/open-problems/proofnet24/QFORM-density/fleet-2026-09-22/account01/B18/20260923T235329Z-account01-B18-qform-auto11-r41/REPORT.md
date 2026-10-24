SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T23:53:29Z.
attacking: transfer LPP orthogonal-marginal bounds into a definite two-bank conditional quadratic receiver, then apply it to account02/B18's newest tetrahedral four-bank target family.

# account01/B18 — definite two-bank receiver and same-sign four-bank closure

Programme: `QFORM-DENSITY-3EIG-20260922` revision `2026-09-22.5`.

Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM + DESIGNATED PARTNER APPLIED. FULL QFORM REMAINS OPEN / NOT PROVED.**

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction audit

Fresh control was read from `yspennstate/math-research-brain@90312c326fadb9f7604a4d47043413cf67c9810f`, then refreshed through newer main commits before this write. The live owner continuation is still exclusive full-QFORM work. Consumed controls: `AGENTS.md`, `scheduled_tasks/README.md` including OWNER MESSAGE, `fleet.json`, `roles.json`, `PROTOCOL.md`, QFORM `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account01/B18.json`.

The latest completed designated-partner report used below is account02/B18:

- `yspennstate/math-open-problems@3e4aa614ab09df1badb2f169d00141189204134b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260923T230752Z-r11/REPORT.md`.

It proves/records the exact tetrahedral four-bank target family, the identity `Q=S^T K S` with `K=I_4-(1/4)11^T`, its spectrum `{1,1,1,0}`, and a global continuous-density bound `<=12` from the pinned diffuse theorem. It also records the source-valid LPP transfer for the bank sums.

The primary external theorem actually used is:

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Israel J. Math. 216 (2016), Theorem 1.1.

Exact hypothesis match: the original source density is a genuine product `prod_i f_i`, every factor is a probability density with `||f_i||_infinity<=1`, and the map to each bank scalar is a one-dimensional orthogonal projection. The theorem gives density cap `sqrt(2)` in dimension one and `2` for a two-dimensional orthogonal marginal. No moments, iid hypothesis, bounded support, connected support, log-concavity, centering, symmetry, or smoothness are required. I use it only for marginal density caps. I never infer independence after rotation; independence of different bank scalars comes solely from disjoint ORIGINAL-coordinate blocks.

Live corrections preserved: no law-uniform pointwise Fresnel decay; no arbitrary-joint indefinite rank-three coarea; no conditional cap substituted for independence; no post-rotation independence; no fixed-good-minor consequence of the bare spectral hypothesis; no deletion of a small nonzero remainder.

## 2. Elementary definite two-dimensional receiver

### Lemma 2.1 — `QFORM-DEFINITE-PAIR-DENSITY-v1`

Let `Z=(Z_1,Z_2)` have an arbitrary joint probability density `rho` with

`||rho||_infinity <= M`.

Let `H` be a real symmetric definite `2 x 2` matrix. For arbitrary `ell in R^2` and `c in R`, put

`T=Z^T H Z + ell^T Z + c`.

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity <= pi M / sqrt(|det H|).`                 (2.1)

No independence between `Z_1,Z_2` is required.

#### Proof

Multiplying `T` by `-1` if necessary, assume `H` is positive definite. Complete the square:

`T=(Z-z_0)^T H (Z-z_0)+c_0`,

where `z_0=-(1/2)H^{-1}ell` and `c_0` is deterministic.

For every interval `[a,b]`, `a<b`, its preimage is contained in the ellipsoidal shell

`{z: r_1 <= (z-z_0)^T H (z-z_0) <= r_2}`,

where `r_1=max(a-c_0,0)` and `r_2=max(b-c_0,0)`. The sublevel set

`{z:(z-z_0)^T H(z-z_0)<=r}`

has area exactly

`pi r / sqrt(det H)`.

Therefore the shell area is at most

`pi (b-a)/sqrt(det H)`.

Using `rho<=M`,

`P(T in [a,b]) <= [pi M/sqrt(det H)] (b-a)`.

Thus the law of `T` is absolutely continuous and its density has essential supremum at most the displayed constant. QED.

This lemma does not conflict with the live arbitrary-joint coarea counterexample: the present two-dimensional quadratic matrix is definite, so all relevant shells have finite area. The refuted interface concerns indefinite noncompact fibers in unrestricted joint laws.

## 3. Same-sign four-source rank-three theorem

### Theorem 3.1 — `QFORM-FOUR-SOURCE-SAMESIGN-v1`

Let `S_1,...,S_4` be independent real random variables with density caps

`||p_{S_i}||_infinity <= K_i`.

Let `H` be a real symmetric `4 x 4` matrix that is positive semidefinite or negative semidefinite, of rank exactly three, and whose three nonzero eigenvalue magnitudes are at least `s>0`. For arbitrary affine terms `ell in R^4`, `c in R`, define

`Q=S^T H S + ell^T S + c`.

Then there exists a pair `I={i,j}` such that

`boxed: ||p_Q||_infinity <= pi K_i K_j / sqrt(det H[I,I])`,         (3.1)

with

`det H[I,I] >= s^2/2`                                               (3.2)

(after replacing `H` by `-H` in the negative-semidefinite case). Consequently, if `K_i<=K` for all four sources,

`boxed: ||p_Q||_infinity <= pi sqrt(2) K^2 / s.`                    (3.3)

In particular, four cap-one scalar sources satisfy

`boxed: ||p_Q||_infinity <= pi sqrt(2)/s = 4.442882938.../s.`       (3.4)

#### Proof

Assume first `H>=0`. Let its three positive eigenvalues be `lambda_1,lambda_2,lambda_3>=s`. The second elementary symmetric polynomial satisfies

`e_2(H)=lambda_1 lambda_2+lambda_1 lambda_3+lambda_2 lambda_3 >=3s^2`. (3.5)

For every matrix, the coefficient identity for principal minors gives

`e_2(H)=sum_{1<=i<j<=4} det H[{i,j},{i,j}]`.                        (3.6)

Because `H>=0`, all six principal `2 x 2` determinants are nonnegative. Hence some pair `I={i,j}` obeys

`det H[I,I] >= (3s^2)/6 = s^2/2`.                                  (3.7)

That principal block is positive definite. Condition on the two complementary ORIGINAL source variables. The retained pair `(S_i,S_j)` remains independent and has joint density cap at most `K_i K_j`. All conditioned cross terms become an arbitrary linear term in the retained pair. Lemma 2.1 therefore gives (3.1), and (3.7) gives (3.3).

For `H<=0`, apply the same argument to `-H`; the pushforward density of `-Q` has the same `L^infinity` norm as that of `Q`. QED.

### Corollary 3.2 — four disjoint ORIGINAL-coordinate scalar banks

Suppose each `S_k` is a unit linear projection of a disjoint ORIGINAL-coordinate product block with all one-dimensional input density caps at most one. LPP Theorem 1.1 gives

`K_k<=sqrt(2)`.

The bank variables are genuinely independent because the source blocks are disjoint. Hence Theorem 3.1 gives

`boxed: ||p_Q||_infinity <= 2 pi sqrt(2)/s = 8.885765876.../s.`      (3.8)

This is a source-valid four-bank theorem for the semidefinite rank-three signature. It is much sharper than the general-signature four-source receiver because a definite physical pair can be paid by compact ellipsoidal shell area.

Continuity is **not** asserted from Lemma 2.1/Theorem 3.1 alone for arbitrary rough densities.

## 4. Actual application to the latest account02/B18 tetrahedral family

The designated partner report `3e4aa614...` constructs `m=4N`, four disjoint banks `I_1,...,I_4`, and normalized bank sums

`S_k=N^(-1/2) sum_{i in I_k} X_i`.

It proves exactly

`Q=X^T A_m X = S^T K S`,

with

`K=I_4-(1/4)11^T`,

`spec(K)={1,1,1,0}`.                                                (4.1)

Thus `K` is positive semidefinite rank three with `s=1`. Moreover every `2 x 2` principal block is

`[[3/4,-1/4],[-1/4,3/4]]`,

so

`boxed: det K[{i,j},{i,j}] = 1/2`                                  (4.2)

for every pair.

By LPP, each normalized bank sum has density cap at most `sqrt(2)`. Since the banks are disjoint original-coordinate blocks, any chosen pair has joint density cap at most `2`. Condition on the other two bank sums. Lemma 2.1 with `det H=1/2` gives the literal whole-line inequality

`boxed:
 ||p_(X^T A_m X)||_infinity
 <= 2 pi / sqrt(1/2)
 = 2 pi sqrt(2)
 = 8.885765876316732... .`                                         (4.3)

This holds for every `N>=2` and every admissible independent cap-one original-coordinate law.

The partner's same report had two prior certificates on this family:

- global diffuse Fourier payment: `<=12`;
- source-valid four-bank application of the general-signature four-source theorem: `<1184`.

Equation (4.3) improves both numerical bounds on this family. More importantly, it exhibits a reusable structural rule: for a same-sign four-bank rank-three carrier, pay a definite pair **after aggregation**, rather than feeding a tiny physical four-core or the full four-source general-signature receiver.

### Continuity on the tetrahedral family

The new definite-pair proof establishes essential boundedness only. Separately, the completed account02/B18 report applies the pinned diffuse Fourier theorem to this exact family and obtains an integrable characteristic-function majorant, hence a continuous `C_0` density. Therefore the tetrahedral family has a continuous representative, and since that representative equals the essentially bounded density a.e., continuity upgrades (4.3) to the pointwise bound

`p_Q(t) <= 2 pi sqrt(2)` for every real `t`.                         (4.4)

This continuity conclusion uses the partner's completed result; it is not inferred from the shell argument.

## 5. Why this matters to the full compiler

The latest partner report showed a sharp certificate gap: every fixed four **physical coordinate** core in the diffuse tetrahedral family has spectral scale `O(1/m)`, while exact bank aggregation restores unit rank-three scale. The theorem above shows that in the same-sign semidefinite branch one does not need a general four-source quadratic receiver after that aggregation: a single definite bank pair already closes the density at constant `2 pi sqrt(2)`.

Thus a useful target-level structural implication is now:

`FOUR DISJOINT SCALAR BANKS + SAME-SIGN RANK-THREE EFFECTIVE CARRIER AT SCALE s`

`=> density <=2 pi sqrt(2)/s`, with no moments and no post-rotation independence.

The remaining full-QFORM debt is structural, not analytic for this branch: from an arbitrary matrix having at least three eigenvalues of magnitude at least one, produce such a same-sign four-bank carrier at universal scale, or route failure to the already-paid indefinite/private-bank/ridge mechanisms while retaining arbitrary same-bank and extra-spectrum curvature. The bare spectral hypothesis does not itself provide four exact scalar banks, and small residual coefficients cannot be deleted for arbitrary unbounded inputs.

## 6. Prior-literature check and claim scope

LPP provides exactly the bounded marginal theorem needed for the bank density caps. A targeted search also found Juškevičius--Lee's sharp maximum-density/rearrangement theorem for sums of independent bounded-density random vectors, but it is not needed for the displayed constant. I found no exact published theorem in this targeted check that directly states the full unrestricted QFORM conjecture or the present four-bank semidefinite corollary under these exact rough non-iid hypotheses. This is only a hypothesis comparison; no novelty claim is made from a search miss.

## 7. Conclusion

New proved supporting theorem:

`QFORM-FOUR-SOURCE-SAMESIGN-v1`:
for four independent scalar sources with density caps `K_i`, a semidefinite rank-three effective quadratic matrix with nonzero eigenvalue magnitudes `>=s` has density bounded by `pi sqrt(2) K_max^2/s`.

Source-valid bank corollary:

`four disjoint unit original-coordinate banks => ||p_Q||_infinity <=2 pi sqrt(2)/s`.

Designated-partner application:

`account02/B18` tetrahedral target family =>

`boxed: ||p_Q||_infinity <=2 pi sqrt(2)=8.885765876316732...`,

with a continuous `C_0` representative supplied separately by the partner's completed diffuse Fourier theorem.

The unrestricted owner target remains **OPEN / NOT PROVED / NOT DISPROVED**.
