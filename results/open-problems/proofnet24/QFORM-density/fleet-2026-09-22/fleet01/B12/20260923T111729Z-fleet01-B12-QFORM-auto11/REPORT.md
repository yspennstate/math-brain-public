SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T11:17:29Z.
attacking: additional-eigenvalue control via a thresholded spectral split and a ridge-leverage shield for the arbitrarily large part.

# fleet01/B12 — thresholded spectral additions through a ridge-leverage shield

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T111729Z-fleet01-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM; FULL QFORM REMAINS OPEN.**  
Continuity: **proved in the scope of the theorem below** via the ridge-density theorem; unrestricted continuity remains open.

## 1. Exact sources used


The analytic receiver used below is the complete one-scale ridge theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Its exact statement used here is: for an actual original-coordinate cross block `B=A[I,J]`, `gamma>0`,

`K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`,

if for some `1<=q<=2`

`max_i K_ii <= q/2`, `theta>2q`,

then the full quadratic form (arbitrary self blocks, outside coordinates/couplings and induced affine terms) has a bounded continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.

The designated partner result actually applied in Section 6 is fleet02/B12's completed `QFORM-D5-CROSS-RANK-RESERVE-HYBRID-v1` at

`yspennstate/math-open-problems@639e7e151f5d8b83be56a2c6093257fe83deddc3`,

path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T093023Z-fleet02-B12-QFORM-auto11/REPORT.md`.

## 2. Deterministic shielding lemma for a large arbitrary cross addition

Let `B` be an `m x k` real matrix, let `U` be a subspace of `R^m`, and write `P` for the orthogonal projection onto `U`, `Q=I-P`. Assume only that an arbitrary matrix `L` satisfies

`range(L) subset U`.

Let `B=C+L`, where `C` is otherwise arbitrary. For `gamma>0` put

`K_B = B B^T (gamma^2 I+B B^T)^(-1)`.

Define the compressed cross matrix

`C_perp = Q C = Q B`

and its ridge operator (supported on `U^perp`)

`K_perp = C_perp (gamma^2 I + C_perp^T C_perp)^(-1) C_perp^T`.

Then

`Q K_B Q <= K_perp`                                             (2.1)

in Loewner order. Consequently, for every standard coordinate vector `e_i`, if

`p_i=P_ii`, `k_i=(K_perp)_ii`,

then

`(K_B)_ii <= (sqrt(p_i)+sqrt(k_i))^2`.                           (2.2)

### Proof

Since

`K_B = I-gamma^2 (gamma^2 I+B B^T)^(-1)`,

write `M=gamma^2 I+B B^T` in the orthogonal decomposition `U direct_sum U^perp`. Its lower-right block is

`M_22=gamma^2 I_(U^perp)+C_perp C_perp^T`.

The lower-right block of `M^(-1)` is the inverse Schur complement

`(M_22-M_21 M_11^(-1) M_12)^(-1) >= M_22^(-1)`

because the Schur complement is at most `M_22`. Therefore

`Q K_B Q <= Q-gamma^2 M_22^(-1)=K_perp`,

which proves (2.1).

Also `0<=K_B<=I`. Decompose `e_i=P e_i+Q e_i`. Positivity of `K_B` gives the Cauchy-Schwarz estimate for its mixed block, hence

`e_i^T K_B e_i`
` <= ( sqrt((P e_i)^T K_B(P e_i)) + sqrt((Q e_i)^T K_B(Q e_i)) )^2`
` <= (sqrt(P_ii)+sqrt((K_perp)_ii))^2`.

This proves (2.2). Notice that the norm and signs of `L` never enter.

## 3. Rank-shift lower bound for ridge effective dimension

Let `B_0` be a baseline cross block and suppose

`B = B_0 + W + L`,

with `||W||op<=h` and `rank L<=r`. Define

`a_j=(s_j(B_0)-h)_+`.

Then for every `j>r`, singular-value perturbation and rank interlacing give

`s_(j-r)(B) >= s_j(B_0+W) >= a_j`.                            (3.1)

Since `x -> x^2/(gamma^2+x^2)` is increasing,

`theta(B):=tr K_B`
` >= Theta_r(h,gamma)`
` := sum_(j=r+1)^(min(m,k)) a_j^2/(gamma^2+a_j^2)`.          (3.2)

This is the second key fact: a rank-`r` arbitrary-magnitude addition can destroy at most `r` singular directions in the lower bound for the ridge effective dimension.

## 4. Main theorem — `QFORM-THRESHOLDED-LARGE-MODE-RIDGE-SHIELD-v1`

Let `I,J` be disjoint sets of ORIGINAL coordinates and write

`B_0=A_0[I,J]`.

Let an arbitrary symmetric spectral addition be

`E=sum_a theta_a v_a v_a^T`.

Fix a threshold `h>=0` and split

`E=S_h+W_h`,

`S_h=sum_(|theta_a|>h) theta_a v_a v_a^T`,

`W_h=sum_(|theta_a|<=h) theta_a v_a v_a^T`.

Then `||W_h||op<=h` with no dependence on the number or signs of its eigenvalues.

On the left physical bank define

`U=span{(v_a)_I: |theta_a|>h}`,

let `P` be its orthogonal projection, put

`r=dim U`, `p=max_(i in I) P_ii`, `Q=I-P`,

and define the baseline row-size outside the large-mode footprint

`d=max_(i in I) || e_i^T Q B_0 ||_2`.                         (4.1)

For `gamma>0` and `1<=q<=2`, define

`a_j=(s_j(B_0)-h)_+`,

`Theta=sum_(j=r+1) a_j^2/(gamma^2+a_j^2)`.                   (4.2)

If

`( sqrt(p)+(d+h)/gamma )^2 <= q/2`,                           (4.3)

and

`Theta>2q`,                                                    (4.4)

then the FULL quadratic form with matrix

`A=A_0+E`

has a bounded continuous `C_0` density and

`boxed: ||p_(X^T A X)||infinity`
` <= sqrt(e)/(sqrt(2q) gamma) * Theta/(Theta-2q).`             (4.5)

All self blocks and all entries outside the selected cross block are unrestricted. The theorem is uniform in the number, signs and magnitudes of every eigenvalue with `|theta_a|>h`; only the dimension and coordinate leverage of their physical footprint on one bank are charged. Every remaining eigenvalue can have either sign and arbitrary multiplicity; all are charged only through the single threshold `h`.

The theorem also holds with `I,J` interchanged; one may therefore use whichever side of the large spectral footprint gives the better certificate.

### Proof

The actual final cross block is

`B=B_0+S_h[I,J]+W_h[I,J]`.

Put `L=S_h[I,J]`. Since

`L=sum_(|theta_a|>h) theta_a (v_a)_I (v_a)_J^T`,

its left range is contained in `U`, so `rank L<=r`. Also

`||W_h[I,J]||op<=h`.

Apply the shielding lemma of Section 2 with `C=B_0+W_h[I,J]`. Its compressed row `i` satisfies

`||e_i^T Q C||`
` <= ||e_i^T Q B_0|| + ||e_i^T Q W_h[I,J]||`
` <= d+h`.

Because

`K_perp=C_perp(gamma^2 I+C_perp^T C_perp)^(-1)C_perp^T`

and `(gamma^2 I+C_perp^T C_perp)^(-1)<=gamma^(-2)I`,

`(K_perp)_ii <= ||e_i^T C_perp||^2/gamma^2 <= ((d+h)/gamma)^2`.

Thus (2.2) yields

`max_i (K_B)_ii <= (sqrt(p)+(d+h)/gamma)^2 <= q/2`.          (4.6)

Next, Section 3 applies because `rank L<=r` and the small spectral tail has cross norm at most `h`; hence

`theta(B)>=Theta>2q`.                                         (4.7)

Now invoke the pinned one-scale ridge-density theorem on the ACTUAL final original-coordinate cross block `B`. It gives

`||p_Q||infinity`
` <= sqrt(e)/(sqrt(2q)gamma) * theta(B)/(theta(B)-2q)`.

The function `x/(x-2q)` decreases for `x>2q`, so (4.7) gives (4.5). Its Fourier proof gives a continuous density vanishing at infinity. No spectral coordinate is treated as an independent random variable and no quadratic remainder is convolved with the baseline law. QED.

## 5. Interpretation for additional eigenvalues

This theorem supplies a clean large/small split absent from the previous local-rank theorem.

* The large modes `|theta_a|>h` may be arbitrarily large, positive or negative, and arbitrarily numerous. Their amplitude disappears entirely. If many of them have restrictions to `I` lying in the same low-dimensional diffuse subspace, only `r` and `p` are paid.
* The small modes `|theta_a|<=h` may also be arbitrarily numerous and arbitrarily oriented; they are paid only once through `||W_h||op<=h`.
* The large modes are allowed to alter self blocks and outside couplings arbitrarily. The ridge theorem only needs the final physical cross block and retains all other terms.
* If the large footprint is unfavorable on `I` but favorable on `J`, transpose the cross block and use the right-bank version.

The proof is entirely deterministic until the final application of the product-coordinate ridge theorem.

## 6. Exact target-class family and required partner application

Take `|I|=|J|=64` and let

`A_0[H,H] = [[0,2I_64],[2I_64,4I_64]]`, `H=I disjoint_union J`. (6.1)

Let `u_1,...,u_4` be four columns of the normalized real `64 x 64` Sylvester-Hadamard matrix, so they are orthonormal and every coordinate square is `1/64`. Set

`w_a=(u_a,u_a)/sqrt(2)`, `a=1,...,4`,

and add

`S=sum_(a=1)^4 tau_a w_a w_a^T`,                              (6.2)

with completely arbitrary `tau_a in R`. These are literal eigenvalues of the added matrix `S`; their signs and magnitudes are unrestricted. Finally add any symmetric `T` with

`||T||op<=1/8`.                                               (6.3)

Treat `S` as the large arbitrary part and `T` as the small tail (`h=1/8`). On the cross block, the large part has left range

`U=span(u_1,...,u_4)`.

Hence

`r=4`, `p=max_i P_ii=4/64=1/16`.                             (6.4)

For `B_0=2I_64`,

`d=max_i ||e_i^T(I-P)2I||=2 sqrt(15/16)=sqrt(15)/2`.         (6.5)

Choose `gamma=6`, `q=1`. Then

`(sqrt(p)+(d+h)/gamma)^2`
` = (1/4 + (sqrt(15)/2+1/8)/6)^2`
` = (1/4+(4sqrt(15)+1)/48)^2`
` =0.3523395260... <1/2`.                                    (6.6)

All 64 singular values of `B_0` equal two. After paying `r=4` directions and `h=1/8`,

`Theta =60 * (15/8)^2/(6^2+(15/8)^2)`
`      =60*(25/281)=1500/281=5.3380782918... >2`.             (6.7)

Therefore the new theorem gives the uniform continuous-density estimate

`boxed: ||p_Q||infinity`
` <= sqrt(e)/(6sqrt(2)) * (1500/281)/(1500/281-2)`
` =125 sqrt(e)/(469 sqrt(2))`
` =0.3107201468...`                                           (6.8)

for every quadruple `(tau_1,...,tau_4)` and every dense tail (6.3).

This family stays inside the exact target class uniformly. The unperturbed `2x2` block `[[0,2],[2,4]]` has eigenvalues `2+2sqrt(2)` and `2-2sqrt(2)`. Hence `A_0` has 64 eigenvalues `2+2sqrt(2)>1`. A rank-four arbitrary update leaves at least 60 eigenvalues at least `2+2sqrt(2)` by rank interlacing, and the norm-`1/8` tail leaves at least 60 eigenvalues above `2+2sqrt(2)-1/8>1`.

### Designated partner result applied to the same actual family

Apply fleet02/B12's completed `QFORM-D5-CROSS-RANK-RESERVE-HYBRID-v1` to exactly (6.1)-(6.3). In its notation, the protected lower-right block is

`D=4I_64`,

the arbitrary update `S[H,H]` has rank at most `r=4`, the dense tail has `delta=1/8`, and

`s_(2r+11)(D)=s_19(4I_64)=4>2delta`.                          (6.9)

With total physical dimension `m_H=128`, its theorem therefore gives the independent actual inequality

`||p_Q||infinity`
` <= [5sqrt(2e)+2sqrt(6pi*128)]/(4-1/4)`
` =29.3060223655...`.                                         (6.10)

This explicitly applies the designated partner theorem to the same arbitrary-sign, arbitrary-magnitude spectral additions. The new ridge shield (6.8) is much sharper on this diffuse-footprint family because it exploits high-cardinality cross smoothing rather than a bounded-dimensional physical receiver.

## 7. What remains unpaid

The theorem is not a proof of the unrestricted QFORM conjecture. Starting from only `s_3(A)>=1`, we have not proved the existence of a cut and threshold for which the large spectral footprint is simultaneously low-dimensional/diffuse enough to satisfy (4.3) and the baseline has enough post-rank ridge reserve to satisfy (4.4).

The known singleton-plus-two-banks correction family shows that a single cross-rank/ridge condition cannot be asserted universally. The next structural step should therefore be a product-preserving dichotomy: either some threshold has a diffuse large-mode footprint plus sufficient post-rank ridge reserve (paid by this theorem), or concentration of that footprint forces one of the localized physical-core / grouped-bank / hub / scalar-Schur exits already developed elsewhere.

## 8. Forbidden shortcuts explicitly avoided

No Gaussianity, moments, compactness, log-concavity or connected support is assumed. No rotation of the random vector is used probabilistically. The small spectral tail is used only through the deterministic matrix norm `||W_h||op<=h`; it is not treated as a small random quadratic error. The proof does not use uniform pointwise van-der-Corput decay, arbitrary-joint coarea, conditional projection-density moments, naive fiber-sup integration, or Monte Carlo extremality.

A finite numerical linear-algebra regression of the shielding inequality was run locally on 100 random fixtures; the smallest eigenvalue of `K_perp-QK_BQ` was `-2.2e-14` (roundoff scale) and the coordinate leverage inequality had positive margin in every fixture. This computation is corroboration only; Sections 2-4 are the proof.
