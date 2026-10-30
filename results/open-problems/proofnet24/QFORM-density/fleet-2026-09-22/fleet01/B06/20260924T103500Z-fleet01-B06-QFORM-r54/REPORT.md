SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T10:35:00Z.
attacking: near-rank-one hub stability via exact approximate-sparse-kernel deletion, retaining the full small hub curvature as an affine child rather than treating it as a random perturbation.

# fleet01/B06 r54 — approximate sparse-kernel affine deletion

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted QFORM remains **OPEN**. Global continuity remains **OPEN**. This run proves a supporting structural theorem and a quantitative near-rank-one corollary. No Gaussian, moment, log-concavity, compact-support, connected-support, or rotated-independence assumption is used.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval/writeback is authenticated GitHub transport, but the programme protocol distinguishes that from verified native learned-memory ingestion.

## 1. Sources actually consumed

- Current programme state: `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/fleet01/B06.json` from fresh main.
- Immediate predecessor fleet01/B06 r53: `yspennstate/math-open-problems@16d43afc2381f65dde19296a917ffc436d823850`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T100917Z-fleet01-B06-QFORM-r53/REPORT.md`.
- Designated partner fleet02/B06 theorem `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1`: `yspennstate/math-open-problems@006892a091e8f58edf21e071244a2c7e2a340ec0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260924T092809Z-auto11-a9c3/REPORT.md`.

The live corrections consumed here are especially: no independence after spectral rotation; no unrestricted fiber-sup integration; no treatment of a small matrix coefficient as a small random quadratic error on unbounded cap-one inputs; and no removal of translated density masks after a random shear. The proof below conditions on a literal original coordinate first and uses an exact identity.

## 2. Main theorem — `QFORM-APPROX-SPARSE-KERNEL-AFFINE-DELETE-v1`

Let `A=A^T` be an `n x n` real symmetric matrix. Let `w` be a unit vector supported on a literal original-coordinate set `H` of size `m`, where `1<=m<=3`. Put

`epsilon = ||A w||_2`.

Choose any `k in H` with `a=w_k !=0`, let `R={1,...,n}\{k}`, and write

`C=A_RR`,  `T=w_R/a`,  `P=[-T  I_R]`,

`q=(Aw)_R/a`,

`d=(Aw)_k/a - q^T T`.

Then the following hold.

### (i) Exact matrix identity

After ordering coordinate `k` first,

`A = P^T C P + E`,

where

`E = [[d,q^T],[q,0]].`

This is an exact identity for every `w`; no null-vector assumption is made.

### (ii) Exact product-preserving conditional identity

For an arbitrary affine parent

`Q(X)=X^T A X + 2 g^T X + c`,

condition on the literal original coordinate `X_k=t` and define

`Z=X_R-T t`.

For fixed `t`, the coordinates of `Z` are independent deterministic translations of the original coordinates in `R`, so their one-dimensional densities remain bounded by one. Moreover

`Q | (X_k=t) = Z^T C Z + 2 (g_R+t q)^T Z + c_t`

for a scalar `c_t` depending on `t`.

Thus **all** nonzero failure of `w` to be a kernel vector becomes an affine term after conditioning; no small quadratic random error is discarded.

### (iii) Stable singular-value transfer

The exact norm identities and bounds are

`||P||_op^2 = 1/|a|^2`,

`||q||_2 <= epsilon/|a|`,

`|d| <= epsilon/|a| + epsilon sqrt(1-a^2)/|a|^2`,

and hence

`||E||_op <= |d|+||q||_2
             <= epsilon [ 2/|a| + sqrt(1-a^2)/|a|^2 ].`

For every singular-value index `j`, Weyl plus the product inequality gives

`s_j(A) <= s_j(P^T C P)+||E||_op
        <= |a|^{-2} s_j(C)+||E||_op`.

Therefore

`boxed( s_j(C) >= |a|^2 s_j(A)
                    - [2|a|+sqrt(1-a^2)] epsilon ).`

Since `(2,1) dot (|a|,sqrt(1-a^2)) <= sqrt(5)`, one has the simpler universal bound

`boxed( s_j(C) >= |a|^2 s_j(A) - sqrt(5) epsilon ).`

If `k` is chosen with maximal `|w_k|`, then `|a|^2>=1/m`; hence

`boxed( s_j(C) >= s_j(A)/m - sqrt(5) epsilon ).`

In particular, if `s_3(A)>=sigma` and

`epsilon <= sigma/(2 m sqrt(5))`,

then

`boxed( s_3(C) >= sigma/(2m) ).`

For the present three-hub use (`m=3`), the explicit sufficient threshold is

`epsilon <= sigma/(6 sqrt(5))  ==>  s_3(C)>=sigma/6`.

### (iv) Affine-child density compiler

Write `C_r^aff` for the scale-one affine QFORM constant in dimension `r`: the least constant such that every symmetric `r x r` matrix with `s_3>=tau`, arbitrary affine term, and independent cap-one inputs has density sup at most `C_r^aff/tau`.

Under the preceding `m<=3` small-residual hypothesis,

`||p_{Q|X_k=t}||_infinity <= [2m C_{n-1}^aff]/sigma`

uniformly in `t`, and therefore

`boxed( ||p_Q||_infinity <= [2m C_{n-1}^aff]/sigma ).`

For `m=3`, this is `6 C_{n-1}^aff/sigma`.

This is a genuine conditional-density average, not an integral of fiber suprema.

## 3. Proof of the exact identities

Order coordinate `k` first and write

`A=[[alpha,b^T],[b,C]]`,  `w=(a,w_R)=(a,aT)`.

The lower block of `Aw` is

`(Aw)_R = a(b+CT)`,

so

`q=b+CT`.

The upper-left difference between `A` and `P^T C P` is

`alpha-T^T C T`.

Also

`(Aw)_k/a = alpha+b^T T`,

hence

`(Aw)_k/a - q^T T
 = alpha+b^T T-(b+CT)^T T
 = alpha-T^T C T=d`.

Therefore

`A-P^T C P=[[d,q^T],[q,0]]=E`.

For a fixed `X_k=t`, `P X=X_R-Tt=Z`. The correction contributes

`X^T E X = d t^2+2t q^T X_R
          = 2t q^T Z + (d+2q^T T)t^2`,

so only an affine term in the remaining variables survives; the rest is absorbed into `c_t`. This proves the conditional identity without requiring `q^T T=0`.

Because `w` is unit,

`1+||T||^2 = 1/|a|^2`,

and `P P^T=I+T T^T`, giving `||P||^2=1/|a|^2`. The stated bounds on `q,d,E` follow from Cauchy--Schwarz. Weyl's singular-value inequality and

`s_j(P^T C P)<=||P||^2 s_j(C)`

give the spectral transfer. Multiplying the error bound by `|a|^2` yields

`|a|^2||E|| <= [2|a|+sqrt(1-a^2)]epsilon <= sqrt(5)epsilon`.

Finally maximal coordinate selection on an `m`-supported unit vector gives `|a|^2>=1/m`.

## 4. Near-rank-one three-hub corollary

Return to a literal three-coordinate hub decomposition

`A=[[K,M],[M^T,C_0]]`.

Suppose the hub block has one dominant direction and let `W` be the two-dimensional spectral subspace spanned by the two smaller-in-modulus eigenvectors of `K`. Put

`eta = ||K|_W||_op`,

`nu = min_{w in W, ||w||=1} ||M^T w||_2`.

Choose a unit minimizer `w in W`, extended by zero on the tail. Then

`||Aw||_2^2 = ||Kw||_2^2 + ||M^T w||_2^2
            <= eta^2+nu^2`.

Consequently, if `s_3(A)>=sigma` and

`boxed( sqrt(eta^2+nu^2) <= sigma/(6 sqrt(5)) ),`

then some literal hub coordinate can be deleted product-preservingly and the remaining principal block satisfies

`boxed( s_3(C)>=sigma/6 )`, 

while the conditional law is exactly an affine QFORM in independent translated cap-one variables. Therefore

`boxed( ||p_Q||_infinity <= 6 C_{n-1}^aff/sigma ).`

This is the requested stable extension of r53's **delete branch** from exact rank-one `K` to a genuinely near-rank-one `K`; the small nonzero hub curvature is retained exactly through `Aw` and becomes an affine child coefficient after conditioning.

The complementary branch is now quantitatively explicit: if `eta` is already within the near-rank-one regime but the delete compiler fails, then `nu` must be bounded below at scale `sigma`. That remaining branch should be paid by the existing product-weighted transverse / two-hub gradient-volume receivers; this report does not yet prove the necessary uniform splice for every nonzero `eta`.

## 5. Designated partner result applied at an actual inequality

At the exact endpoint `epsilon=0`, `w` is a genuine sparse kernel vector. Applying fleet02/B06 `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1` with `d=1`, `m<=3` gives a literal coordinate `k` for which

`boxed( s_3(C) >= s_3(A)/3 >= sigma/3 ).`

Conditioning on that original coordinate preserves the product law exactly, so the actual affine-child inequality is

`boxed( ||p_Q||_infinity <= 3 C_{n-1}^aff/sigma ).`

Thus the new approximate theorem is stable around the partner's exact endpoint, while the completed partner theorem remains sharper at `epsilon=0`.

In dimension four, combining this exact endpoint with the pinned three-dimensional affine bound `C_3^aff<=6 sqrt(pi)` again gives

`||p_Q||_infinity <= 18 sqrt(pi)/sigma`.

## 6. Why this is not a forbidden perturbative argument

The theorem never asserts that `X^T E X` is small because `||E||` is small. Such an assertion is invalid for arbitrary unbounded cap-one inputs. The smallness of `E` is used **only** in a deterministic singular-value comparison between matrices. The random-variable identity is exact after conditioning:

`Q|X_k=t = Z^T C Z + affine_t(Z)+constant_t`.

Thus the arbitrary tails and their self-curvature are retained.

## 7. Sanity check

A 1000-case random audit in ambient dimension eight verified the reconstruction identity to operator error about `1.2e-15`, verified `||E||` never exceeded the stated residual bound, and verified the singular-value lower bound in every trial. This is only an algebra check; Sections 2--3 are the proof.

## 8. Status and next debt

**Proved this run:** `QFORM-APPROX-SPARSE-KERNEL-AFFINE-DELETE-v1` and the near-rank-one delete corollary.

**Essential boundedness:** obtained conditionally on the lower-dimensional affine target constant in the delete branch; exact endpoint gets the sharper partner factor three.

**Continuity:** not proved globally. If the lower-dimensional affine child has a uniformly bounded continuous density, the conditional averaging step passes continuity by dominated convergence; no full-target continuity theorem is asserted here.

**Full QFORM:** OPEN. No counterexample found.

**First unpaid implication:** `QFORM-NEARRANKONE-TRANSVERSE-PAYMENT-v1`: when `sqrt(eta^2+nu^2)` exceeds the delete threshold because the transverse map is genuinely large while `eta` remains small, prove a direct product-weighted curved receiver that is stable in `eta` and keeps arbitrary tail self-curvature. The natural inputs are r52's transverse P2 packet and r51's two-hub gradient-volume receiver. A second assembly issue remains: prevent repeated lower-dimensional deletions from accumulating a dimension-dependent spectral loss.

## 9. Source pins

- Owner source: `https://github.com/yspennstate/math-research-brain/blob/0dc369ddf8b860648dd780d8f92c62994dc53ecf/scheduled_tasks/README.md`.
- Predecessor r53: `yspennstate/math-open-problems@16d43afc2381f65dde19296a917ffc436d823850:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T100917Z-fleet01-B06-QFORM-r53/REPORT.md`.
- Designated partner: `yspennstate/math-open-problems@006892a091e8f58edf21e071244a2c7e2a340ec0:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260924T092809Z-auto11-a9c3/REPORT.md`.
