SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-24T08:38:31Z.
attacking: QFORM-R49-ALIGNED-FOURNODE-LATENT-DETERMINANT-ENDPOINT-v1 — pay the exact aligned four-node rank-two network with a general-rank original-coordinate Fresnel receiver, then isolate the near-rank-drop/tail obstruction.

# account02/B19 r14 — general-rank latent Fresnel endpoint and four-node payment

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL STEP APPLIED / NEW COMPLETE SUPPORTING RECEIVER / EXACT B20 STRUCTURAL OBSTRUCTION PAID / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval is not native learned-memory receiver ingestion.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random variable is rotated. The only orthogonal changes are deterministic changes of basis in a finite coefficient space. No moment, support, log-concavity, iid, arbitrary-joint coarea, worst-fibre cap, post-rotation independence, or coefficient-continuity assumption is used.

## 1. Fresh frontier


The first global unpaid edge supplied by account02/B20 r49 is

`QFORM-R49-ALIGNED-FOURNODE-R2-PLUS-SELF-CURVATURE-ENDPOINT-v1`.

Its inherited constants are

`h = 1/2 - 1/(4 sqrt(2))`,

`s_grid = h/126 - 2^-16 = 0.002550005533980064...`.

It supplies four disjoint physical banks `R_1,R_2,C_1,C_2` and four actual cells `M_ab=A[R_a,C_b]` with `sigma_2(M_ab)>s_grid`. Its completed E3-or-alignment theorem pays every transverse same-side curvature branch; in the survivor, the same-side bridges are within `2^-15` of rank-two maps aligned to all relevant cell planes. Its required pinned D5 test pays any of eight augmented physical cuts with `e_5>=1/1024`; every survivor has all eight below that gate. The remaining unrestricted curvature is in the four principal node blocks plus aligned bridges and the genuine retained coefficient tails.

The exact obstruction exhibited by B20 r49 uses flat orthonormal two-frames `U_1,U_2,V_1,V_2`, each with physical leverage `2/m<=1/16`, and

`A[R_a,C_b]=s U_a V_b^T`,

`A[R_1,R_2]=t U_1U_2^T`,

`A[C_1,C_2]=t V_1V_2^T`,

with transpose blocks imposed and all four principal node blocks zero. Every augmented physical cross block in the B20 E3 test has rank two, so its `e_3` is exactly zero. For `s=t=1` the full nonzero spectrum is `{3,3,-1,-1,-1,-1,-1,-1}`. Thus transverse E3 cannot be forced in the aligned endpoint.

The newest compatible designated account03/B19 r52 result independently pays an exact diffuse four-latent carrier by `8|det H|^{-1/4}` and identifies determinant collapse with a small fourth singular direction, while explicitly retaining the actual diffuse residual/tail as the next debt.

## 2. Required pinned source and general-rank theorem

The completed source used here is Theorem H at the required exact source commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Theorem H is stated for arbitrary Fresnel rank `r>=0` and literal physical source bank `I`, with arbitrary outside blocks. We use it at equation level, not by analogy.

### Theorem 2.1 — `QFORM-BL-RANKR-LATENT-PSEUDODET-ENDPOINT-v1`

Let `I` be a literal original-coordinate set. Suppose

`A[I,I] = D + W H W^T`,

where

- `D` is physical diagonal;
- `W` is `|I| x r` with `W^T W=I_r`;
- every physical row has leverage `||W_{i,*}||_2^2<=1/2`;
- `H=H^T` has rank `k>=3`.

All blocks touching `I^c`, all curvature inside `I^c`, and all affine terms are arbitrary. Let

`pdet(H) = product of the nonzero eigenvalues of H`.

Then the complete ambient quadratic law has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= [4k/(k-2)] |pdet(H)|^{-1/k}.`          (2.1)

For `k=3,4,6,8` the prefactors are respectively `12,8,6,16/3`.

### Proof

Choose an orthogonal coefficient-space matrix `O` whose first `k` columns diagonalize the nonzero spectral part of `H`:

`H = O_k diag(mu_1,...,mu_k) O_k^T`,

with every `mu_j!=0`. Put `Z=W O_k`. Then

`Z^T Z=I_k`.

For each literal physical coordinate `i`,

`||Z_{i,*}||^2 <= ||W_{i,*}||^2 <=1/2`.

This is only a deterministic column change in coefficient space; no random coordinate is rotated.

Apply the pinned Theorem H with no hub coordinates, Fresnel rank `k`, source bank `I`, coefficient vectors the columns of `Z`, and diagonal twist `D`. The source Gram is `I_k`. The theorem gives for the full ambient characteristic function

`|phi_Q(t)| <= (4 pi)^(k/2) |t|^(-k/2) |pdet(H)|^(-1/2).`        (2.2)

Of course `|phi_Q(t)|<=1`. Set

`a=k/2>1`,

`K=(4 pi)^a |pdet(H)|^(-1/2)`.

Direct integration gives

`integral_R min(1,K|t|^-a) dt = 2 a/(a-1) K^(1/a).`              (2.3)

Since

`K^(1/a)=4 pi |pdet(H)|^(-1/k)`,

Fourier inversion yields

`||p_Q||_infinity`
` <= (1/(2 pi)) [2a/(a-1)] [4 pi] |pdet(H)|^(-1/k)`
` = 4a/(a-1) |pdet(H)|^(-1/k)`
` = [4k/(k-2)] |pdet(H)|^(-1/k).`

The right side of (2.2) is integrable because `k>2`, so the density is continuous and vanishes at infinity. QED.

Remarks. (i) The theorem strictly contains the pinned rank-three Theorem F endpoint, reproducing the constant `12`. (ii) For `k=4` it reproduces the account03/B19 r52 exact four-latent constant `8`. (iii) Exact rank drop is harmless provided at least three nonzero coefficient modes remain: one simply applies the theorem to the nonzero coefficient eigenspace. What is not justified is deleting a *small but nonzero* coefficient mode under rough cap-one laws.

## 3. Equation-level payment of the B20 aligned obstruction

For the exact B20 flat four-node family set

`I=R_1 union R_2 union C_1 union C_2`,

`W=diag(U_1,U_2,V_1,V_2)`.

Then `W` has eight orthonormal columns and every physical row has leverage `2/m<=1/16<1/2`. The source self-block is exactly

`A[I,I]=W H_8(s,t) W^T`,

where

`H_8(s,t)=B_4(s,t) tensor I_2`,

and, in node order `(R_1,R_2,C_1,C_2)`,

`B_4(s,t)=`
`[[0,t,s,s],`
` [t,0,s,s],`
` [s,s,0,t],`
` [s,s,t,0]].`                                                     (3.1)

The four eigenvalues of `B_4` are

`t+2s,  t-2s,  -t,  -t`.                                         (3.2)

Therefore each is repeated twice in `H_8`.

For the target-valid obstruction point `s=t=1`,

`spec_nonzero(H_8)={3,3,-1,-1,-1,-1,-1,-1}`,

`|det H_8|=9`.

Theorem 2.1 with `k=8` gives the full ambient bound

`boxed: ||p_Q||_infinity <= (16/3) 9^(-1/8)`
`                         = 4.052456990141827... .`                (3.3)

Thus the exact B20 r49 structural obstruction is not a density obstruction at all. It only disproves the strategy of forcing a transverse third physical crossing. Its whole aligned latent network is paid directly, source-preservingly, by the pinned Fresnel/Brascamp--Lieb theorem.

This payment retains arbitrary outside blocks and affine terms. It does not require independence of the eight latent projections; the random variables remain the original independent physical coordinates throughout.

## 4. Exact rank-drop endpoints of the same network

The pseudodeterminant version resolves the singular coefficient endpoints that a determinant-only theorem would artificially discard.

### 4.1 `t=2s`

For `s>0,t=2s`, the scalar-node eigenvalues are

`4s,0,-2s,-2s`.

Hence `H_8` has rank six and

`|pdet(H_8)|=(4s)^2(2s)^4=256 s^6`.

Theorem 2.1 with `k=6` yields

`boxed: ||p_Q||_infinity <= 6 (256s^6)^(-1/6)`
`                         = [6/2^(4/3)] s^(-1).`                  (4.1)

At the live B20 scale `s>=s_grid`, this is

`||p_Q||_infinity < 933.764.`                                    (4.2)

### 4.2 `t=0`

For `s>0,t=0`, the nonzero scalar-node eigenvalues are `2s,-2s`, so `H_8` has rank four and

`|pdet(H_8)|=(2s)^4=16s^4`.

Theorem 2.1 gives

`boxed: ||p_Q||_infinity <=4/s <1568.625`                         (4.3)

at `s>=s_grid`.

Thus exact latent rank collapse is itself an already-paid endpoint. The genuinely delicate object is a *near* rank drop: a nonzero coefficient can be arbitrarily small, and rough cap-one laws do not permit deleting it by coefficient continuity.

## 5. Determinant-or-near-rank-seven funnel for an exact eight-latent carrier

Suppose more generally an exact aligned four-node subbranch has

`A[I,I]=D+W H_8 W^T`,

with the same eight-column normalized physical frame, row leverage `<=1/2`, and at least one normalized two-by-two cell of `H_8` having `sigma_2>=s_grid`.

If

`|det H_8|>=2^-80`,                                               (5.1)

then Theorem 2.1 pays it by

`boxed: ||p_Q||_infinity <=(16/3) 2^10 = 16384/3 <5461.334.`      (5.2)

If (5.1) fails and `H_8` is full rank, the two singular values of the displayed two-by-two cell force

`s_1(H_8),s_2(H_8)>=s_grid`.

Writing `s_1>=...>=s_8>0`,

`|det H_8|=prod_j s_j >= s_grid^2 s_8^6`,

because `s_3,...,s_7>=s_8`. Therefore

`boxed: dist_op(H_8, rank<=7)=s_8`
` <= (|det H_8|/s_grid^2)^(1/6)`
` < 0.000709174346.`                                              (5.3)

This yields the compiler

`QFORM-R49-EIGHTLATENT-DET-OR-RANK7-COLLAPSE-v1`:

> an exact diffuse eight-latent aligned carrier with one live rank-two cell is either paid at a fixed determinant gate, or has an explicitly tiny eighth coefficient-space singular direction.

Equation (5.3) is deterministic structure only. It is not permission to erase the tiny direction.

## 6. Why this does not yet close the actual B20 r49 survivor

The actual B20 survivor is not asserted to have the exact source form `D+WH_8W^T`. It retains:

1. genuine `2^-16` coefficient tails in the four robust physical cells;
2. only `2^-15` collars for the same-side bridges, not exact latent factorization;
3. arbitrary quadratic curvature inside the four principal node blocks.

The pinned Theorem H allows arbitrary curvature *outside* the source bank but not arbitrary nonseparable additions inside the source bank on which Brascamp--Lieb factorisation is used. Hence none of the three items may be deleted or absorbed by a coefficient-continuity argument.

The present theorem nonetheless removes a real chamber: whenever all node curvature is diagonal plus curvature in the same aligned node two-frames, and the retained inter-node pieces factor exactly through those frames, the whole four-node product system is a finite latent Fresnel packet and is paid by Theorem 2.1. In particular, B20's exact E3-counterexample family is closed.

The first sharpened global debt is therefore

`QFORM-R49-ALIGNED-FOURNODE-INTERNAL-NONLATENT-OR-NEARRANKDROP-TAIL-ENDPOINT-v1`:

> Starting from the B20 r49 four literal cells with `sigma_2>s_grid`, after all E3 and augmented-D5 payments fail and the simultaneous two-sided alignment collars hold, either source-preservingly extract the non-plane part of one principal node block / retained cell tail into an already-paid physical E3/E5, hub+square, ridge/window, grouped, pair or inductive receiver, or prove a uniform endpoint for the resulting near-rank-drop finite latent packet **without deleting the genuine tails or a small nonzero latent coefficient**.

The exact determinant and exact rank-drop subbranches are now removed.

## 7. Current conditional proof graph

A source-pinned proof assembly can currently be stated as follows.

1. Same-constant principal-minimal descent removes any proper original-coordinate principal child that still has three target eigenvalues.
2. Completed scalar, physical pair, pair-log, local triple, ridge/window, grouped, hub+square, physical cross-E3, D/D', D5, null-coloop, and rank-two fractional receivers pay their exact branches with their stated arbitrary outside curvature.
3. The account03/B20 and account02/B20 rank-two compilers reduce one major no-pivot chamber to the balanced four-cell physical grid, then B20 r49 pays every transverse same-side curvature state by E3 and every large augmented five-volume by the required pinned D5 theorem.
4. In the remaining aligned four-node chamber, the present Theorem 2.1 completely pays every exact diffuse latent source block of rank at least three with quantitative pseudodeterminant, including the B20 target-valid obstruction and its exact rank-six/rank-four collapse endpoints.
5. The first live edge is the retained-tail / arbitrary-internal-node-curvature interaction and, after exact factorization is achieved, stability as a nonzero latent coefficient tends to zero. No current theorem permits erasing that coefficient or the physical tails.
6. Arbitrary-extra-spectrum closure and unrestricted continuity remain global debts where not already supplied branchwise by an `L^1` characteristic-function receiver.

No full proof is claimed. The target quantifiers are not yet all covered, and the required two independent end-to-end reviews do not exist.

## 8. Source/partner accounting

Required pinned completed result applied at equation level: Theorem H, exact source commit `e5f71d79eff325201dd0274053d20268ce65b837`, used in (2.2) and then on the actual B20 obstruction in (3.3).

Newest compatible designated partner consumed: account03/B19 r52, canonical commit `5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`, whose four-latent determinant endpoint is recovered as the `k=4` case of Theorem 2.1 and whose retained-tail warning is preserved.

Newest healthy B20 frontier consumed: account02/B20 r49, canonical commit `b7a664d483bcf443586a217441b6471caaf2c616`; its exact structural obstruction is paid above rather than used as a reason to wait.

Corrections preserved: no arbitrary-joint rank-three coarea; no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no coefficient-continuity deletion of small modes/tails; no generic fractional-small-ball-to-`L^infinity` interpolation; no mixed-norm absoluteization of the hub-star fiber.
