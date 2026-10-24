SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T10:03:59Z.
attacking: QFORM-BL-R2-PLUS-DIFFUSE-THIRD-SOURCE-RETAINED-TAIL-ENDPOINT-v2 by resolving the exact singular boundary of the r52 four-latent carrier and isolating the genuinely punctured rank-three collar where the retained diffuse residual/tail must still be used.

# account03/B19 r53 — exact-singular latent endpoint and punctured rank-three stratification

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW COMPLETE SUPPORTING RECEIVER / NEW QUANTITATIVE FUNNEL / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval/use is not native authenticated learned-memory receiver ingestion.

Regularity: the new exact-rank >=3 receiver gives a continuous `C_0` density on its exact scope. Full-target continuity remains **OPEN**.

All coordinate sets are literal ORIGINAL-coordinate sets. No random variable is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise quadratic-phase decay hypothesis is introduced. Nonzero coefficient tails are never deleted.

## 1. Fresh source-pinned frontier

Fresh `yspennstate/math-research-brain/main` was resolved before the run. Owner control remains revision `2026-09-22.15`, QFORM-only.

Immediate same-slot source:

`yspennstate/math-open-problems@5ec1cc2bf208bc0249ea89d86fd7298b62ac324e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T070220Z-account03-B19-QFORM-r52/REPORT.md`.

The r52 aligned light skeleton is

`A_skel = D + W H_L W^T`,

where `D` is physical diagonal, `W^T W=I_4`, every physical row satisfies `||W_{i,*}||^2<=1/2`, and the normalized latent cross block has

`sigma_2(C_L)>=1/112`.

Hence, for singular values `s_1(H_L)>=...>=s_4(H_L)`,

`s_1(H_L),s_2(H_L)>=1/112`.

The ACTUAL r49/r51 light block additionally retains the nonseparable residuals

`(E_R direct_sum E_C)+T_cross`.

Those terms are not part of the exact skeleton receiver and are not discarded here.

The analytic source used below is Theorem H from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For an `r`-dimensional latent quadratic carrier with normalized physical row leverages at most `1/2`, Theorem H gives a product-preserving Fresnel/Brascamp--Lieb characteristic-function estimate while retaining arbitrary outside blocks.

## 2. Exact-rank latent endpoint, including singular coefficient matrices

### Theorem 2.1 — `QFORM-BL-EXACTRANK-LATENT-ENDPOINT-v1`

Let `I` be a literal original-coordinate set and suppose

`A[I,I]=D+W H W^T`,

where `D` is physical diagonal, `W^T W=I_m`, each physical row has leverage `||W_{i,*}||^2<=1/2`, and `H=H^T` is real. Let

`k=rank(H)>=3`

and let

`pdet_abs(H)=prod_{j=1}^k s_j(H)`

be the product of the nonzero singular values of `H`. All blocks touching `I^c`, all curvature inside `I^c`, and all affine terms may be arbitrary. Then the full ambient quadratic polynomial has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= [4k/(k-2)] pdet_abs(H)^(-1/k).`        (2.1)

In particular:

- exact rank `3`: `||p_Q||_infinity <=12 [s_1s_2s_3]^(-1/3)`;
- exact rank `4`: `||p_Q||_infinity <=8 |det H|^(-1/4)`, recovering r52.

#### Proof

Diagonalize only in coefficient space,

`H=O diag(mu_1,...,mu_k,0,...,0) O^T`,

with all `mu_j!=0`. Let `Z` be the first `k` columns of `W O`. Then

`Z^T Z=I_k`

and deleting the zero-eigenvalue coefficient columns can only decrease each physical row leverage, so

`||Z_{i,*}||^2<=||W_{i,*}||^2<=1/2`.

No random coordinate is rotated.

Apply Theorem H with zero physical hubs, latent rank `r=k`, the columns of `Z`, and diagonal twist `D`. Its Gram matrix is `I_k`, hence

`|phi_Q(t)| <= K |t|^(-k/2)`,

`K=(4 pi)^(k/2) pdet_abs(H)^(-1/2)`.                              (2.2)

Also `|phi_Q(t)|<=1`. Put `p=k/2>1` and `T=K^(1/p)=K^(2/k)`. Then

`integral_R min(1,K |t|^(-p)) dt`
` =2[T+K T^(1-p)/(p-1)]`
` =2T p/(p-1)`
` =8 pi [k/(k-2)] pdet_abs(H)^(-1/k)`.                           (2.3)

Fourier inversion divides by `2 pi`, proving (2.1). Since `phi_Q in L^1`, the density is continuous and vanishes at infinity. QED.

This theorem is exact at singular `H`: zero latent eigenvalues are removed algebraically, not approximated by small nonzero ones.

## 3. r52 exact-singular boundary is paid except for a quantified rank-two collar

Apply Theorem 2.1 to the exact r52 skeleton.

If `rank(H_L)=3`, then `s_1,s_2>=1/112`, so

`||p_skel||_infinity <=12 [s_1s_2s_3]^(-1/3)`
` <=12 [112^2/s_3]^1/3.`                                         (3.1)

At the fixed gate

`s_3(H_L)>=2^-12`,                                                (3.2)

we obtain

`boxed: ||p_skel||_infinity <4461.148<4462`,                      (3.3)

with a continuous `C_0` density.

If instead exact rank three holds but (3.2) fails, then by Eckart--Young

`boxed: dist_op(H_L,{rank<=2})=s_3(H_L)<2^-12.`                   (3.4)

If `rank(H_L)<=2`, (3.4) holds trivially with zero distance.

Thus `det H_L=0` is no longer one undifferentiated failure of the r52 determinant receiver: the exact rank-three part is paid unless it lies in a fixed `2^-12` rank-two collar.

## 4. Full r52 determinant-collapse branch becomes a punctured-rank-three collar or rank-two collar

Recall the r52 determinant gate

`|det H_L|>=2^-40`,                                               (4.1)

which pays the exact rank-four skeleton by `||p||_infinity<=8192`.

Suppose now `rank(H_L)=4`, `s_3(H_L)>=2^-12`, and (4.1) fails. Since

`s_1s_2>=1/112^2`,

if

`s_4(H_L)>=delta_4`,

with

`delta_4:=2^-40 * 112^2 * 2^12`
`        =4.673004150390625e-5`,                                 (4.2)

then

`|det H_L|=s_1s_2s_3s_4>=2^-40`,

contradicting failure of (4.1). Therefore every unpaid full-rank state with `s_3>=2^-12` satisfies

`boxed: 0<s_4(H_L)<4.674e-5.`                                    (4.3)

Combining Sections 3 and 4 gives the compiler

### `QFORM-R52-PUNCTURED-RANK3-STRATIFICATION-v1`

For the exact r52 four-latent skeleton, at least one of the following holds:

1. determinant payment: `||p||_infinity<=8192`, continuous `C_0`;
2. exact rank-three payment with `s_3>=2^-12`: `||p||_infinity<4462`, continuous `C_0`;
3. rank-two collar: `dist_op(H_L,{rank<=2})<2^-12`;
4. genuinely punctured rank-three collar:
   `s_3(H_L)>=2^-12` and `0<s_4(H_L)<4.674e-5`.

No small nonzero `s_4` in branch 4 is replaced by zero. Under cap-one laws there is no moment/support hypothesis that would justify such a perturbative deletion.

This identifies the first latent analytic debt more sharply than r52: the exact singular boundary itself is not the obstruction; the obstruction is the **nonzero puncture** together with the retained r49 residual/tail.

## 5. Cross invertibility alone cannot remove the rank-two collar

A concrete exact family shows that the lower bound `sigma_2(C_L)>=1/112` does not force a third latent singular value.

For `eps>0` take

`H_eps=[[I_2,I_2],[I_2,diag(1,1+eps)]]`.

After permuting the latent basis into two channels, this is the direct sum of

`[[1,1],[1,1]]`

and

`[[1,1],[1,1+eps]]`.

Hence its cross block is exactly `I_2`, but `rank(H_eps)=3` and its nonzero singular values include

`lambda_-(eps)=(2+eps-sqrt(4+eps^2))/2 ~ eps/2`.

Moreover

`pdet_abs(H_eps)=2 eps` exactly.

Thus `s_3(H_eps)->0` although the cross block remains perfectly conditioned. This proves that no deterministic lower bound on the third latent scale can follow from the robust rank-two crossing alone.

The family is compatible with the r52 leverage geometry: take any orthonormal four-frame in at least eight physical coordinates with every row leverage `<=1/2` (for example four normalized Hadamard columns in dimension eight). Therefore the diffuse third source retained in `E_R direct_sum E_C` is genuinely needed in the small-`s_3` branch; it cannot be replaced by a latent-cross conditioning argument.

## 6. Designated partner account04/B19 applied at the live crossing scale

The corrected completed partner theorem is

`QFORM-FINITECARRIER-CURVED-R2-TERMINAL-v1`

from

`yspennstate/math-open-problems@97c4f5328da327cae4249c40253e466603b2ba5c`.

For a literal original-coordinate packet

`[[0,B,0],[B^T,C,h],[0,h^T,a]]`,

with arbitrary `C,h`, `a!=0`, and singular values `sigma_1>=sigma_2>0` of `B`, it gives

`||p_Q||_infinity <= min{2sqrt(pi)/sqrt(sigma_1 sigma_2), 4sqrt(2)/sqrt(|a|sigma_1)}`.

At the actual r51 robust-crossing scale

`sigma_2(B)>s_*:=4089/458752=0.008913312639508928...`,

one has `sqrt(sigma_1 sigma_2)>=sigma_2>s_*`, so **whenever the structural router manufactures the partner's exact zero-self-side/zero-I-w packet**, the full ambient law is immediately paid by

`boxed: ||p_Q||_infinity <2sqrt(pi)/s_*`
`                         =397.709342...<398.`                    (6.1)

This is a target-level inequality on the live coefficient scale and retains arbitrary opposite-bank curvature and outside coefficients exactly as in the partner theorem. The exact zeros are hypotheses: this run does not pretend that a merely small self block satisfies them.

## 7. Compact conditional proof assembly after r53

The current conditional route is:

1. principal-minimal descent and the completed diagonal / physical-pair / pair-log / physical-E3 / ridge-window / grouped / null-coloop / rank-two fractional receivers pay their exact branches;
2. r47--r51 reduce a major singular-pair/large-leaf chamber to a BL-compatible robust physical rank-two crossing or finite literal hub/star alternatives;
3. r49 turns the adaptive self-curvature planes into a four-latent carrier plus retained physically diffuse residuals and a genuine nonzero crossing tail;
4. r52 pays the nonsingular determinant-large four-latent skeleton;
5. the present run pays the exact rank-three singular skeleton above `s_3=2^-12` and reduces the rest of the exact singular locus to a fixed rank-two collar; full-rank determinant failure with `s_3>=2^-12` is now a genuinely punctured rank-three collar `0<s_4<4.674e-5`;
6. if a finite-carrier router reaches the exact account04/B19 zero-self packet at the live r51 crossing scale, (6.1) pays it below `398`.

The first essential remaining implication on this route is therefore

`QFORM-PUNCTURED-RANK3-OR-RANK2-CARRIER-PLUS-DIFFUSE-RESIDUAL-ENDPOINT-v1`:

> retain the nonzero latent puncture, the r49 diffuse self residuals, and the genuine cross tail, and either obtain an `L^infinity` endpoint from the original product coordinates or route to an already-proved exact physical receiver.

A proof may not set `s_4=0`, may not delete `T_cross`, and may not replace the projected latent variables by an arbitrary bounded joint density. The moving-ridge counterexample from the designated partner remains a direct warning against the last shortcut.

Parallel global debts (giant near-rank-one, small-Pluecker aggregate, hub/star completion, and extra-spectrum/carrier interactions) remain. No full candidate exists yet, so the required two independent end-to-end reviews are not triggered.

## 8. Exact computations / regression values

The constants used above were recomputed independently:

`s_*=4089/458752=0.008913312639508928...`,

`2sqrt(pi)/s_*=397.709341653513...`,

`12*(112^2*2^12)^(1/3)=4461.147443376924...`,

`delta_4=2^-40*112^2*2^12=4.673004150390625e-5`.

For the witness at `eps=2^-20`,

`lambda_-(eps)=4.768370445e-7...`,

`pdet_abs(H_eps)=2eps=1.9073486328125e-6`,

confirming quantitatively that the third latent scale can collapse with cross block exactly `I_2`.

These decimal evaluations are diagnostics; the inequalities and identities in Sections 2--6 are exact.

## 9. Status

Full unrestricted bounded-density conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

Full-target continuity: **OPEN**. Continuity is proved on the determinant-paid and exact-rank>=3 latent branches covered above, not on the remaining punctured/residual collar.

Model self-report: `GPT-5.6 Sol`. Reasoning-effort configuration and provider thinking counters are not exposed, hence `UNKNOWN/null`.
