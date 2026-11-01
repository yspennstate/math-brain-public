# B08 r30 substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.
Run: `20260923T134051Z-fleet01-B08-qform-r30`.
Execution status: `WITHOUT_VERIFIED_BRAIN` (repository retrieval/use occurred; no native learned-memory ingestion is claimed).

## Checkpoint theorem: a variable spectral-window frontier

Let `L>0`. Let `A` be real symmetric with at least three eigenvalues of modulus at least `L`. Fix `0<tau<1`, and let `P_tau` be the spectral projection of `A` onto all eigenspaces with `|lambda|>=tau L`. Suppose

`max_i (P_tau)_{ii} <= ell`.

Define

`delta = 1/2 - sqrt(2 ell) - ell`,

`sigma = delta-tau`.

Assume `delta>tau`. If there are `q in [1,2]` and `r>0` such that

`(sqrt(ell/delta)+tau/(r sigma))^2 <= q/2`

and

`3/(1+r^2)>2q`,

then, for every independent product input with one-dimensional densities bounded by one, `Q=X^T A X` has a continuous `C_0` density and

`||p_Q||_infinity <= [sqrt(e)/(sqrt(2q) r sigma L)] * [theta0/(theta0-2q)]`,

where `theta0=3/(1+r^2)`.

Equivalently,

`||p_Q||_infinity <= 3 sqrt(e) / [sqrt(2q) r sigma {3-2q(1+r^2)} L]`.

### Proof skeleton already closed

Write `A=A_H+E`, where `A_H=U Lambda U^T` is the spectral truncation to `|lambda|>=tau L`. Then `||E||<tau L`, every row of `U` has squared norm at most `ell`, and `Lambda` has at least three singular values at least `L`.

MSS two-part frame partitioning gives an original-coordinate cut `I,J` such that both Gram matrices `M_I=U_I^T U_I`, `M_J=U_J^T U_J` are bounded below by

`delta I`, because each complementary Gram has operator norm at most `(1/sqrt(2)+sqrt(ell))^2=1/2+sqrt(2ell)+ell`.

For `B_0=(A_H)[I,J]`, whitening the two restricted frames gives `s_3(B_0)>=delta L`. Its left range is `range(U_I)`, whose physical projection has diagonal at most `ell/delta`. The true cross block is `B=B_0+E[I,J]`, so `s_3(B)>=sigma L`.

Set `gamma=r sigma L`. The completed one-scale ridge-leverage theorem and its deterministic perturbation estimate give

`max_i K_gamma(ii) <= (sqrt(ell/delta)+tau/(r sigma))^2 <= q/2`,

while the three singular values `>=sigma L` give

`theta_gamma=tr K_gamma >=3/(1+r^2)=theta0>2q`.

The ridge theorem therefore gives the displayed continuous-density bound. This retains the entire spectral tail inside the actual cross block and never treats a small matrix tail as a small random quadratic perturbation.

## New deterministic spectral-projector leakage lemma

Let `H` be symmetric, let `S` be the orthogonal projection onto `range(H)`, let `A=H+E`, and suppose `||E||<=eps`. For `a>0`, let `P_a=1_{|A|>=a}`. Then

`||(I-S)P_a|| <= eps/a`.

Indeed, for `x in range(P_a)`, write `x=A z` with `z in range(P_a)` and `||z||<=||x||/a`. Since `(I-S)H=0`,

`||(I-S)x||=||(I-S)Ez||<=eps ||x||/a`.

Consequently, if `max_i S_ii<=ell0`, then

`max_i (P_a)_ii <= (sqrt(ell0)+eps/a)^2`.

This is a matrix/spectral leakage statement, not a probabilistic perturbation claim.

## Concrete partner application queued for final report

Use fleet02/B08 r27's completed target-valid diffuse family

`A_m^diff=[[u_1u_1^T,B_m],[B_m,u_1u_1^T]]`, `B_m=u_2u_2^T+u_3u_3^T`,

whose nonzero spectrum is `{-1,-1,1,1,1,1}` and whose physical range leverage is `3/m`.

After scaling by `L`, let `H=L A_m^diff`, `m>=128`, and let `A=H+E` for an arbitrary symmetric `E` with `||E||<=L/1024`. Weyl leaves at least three eigenvalues of `A` with modulus at least `L0=(1023/1024)L`. Take the actual `A`-spectral window at `tau=1/32` relative to `L0`. The projector-leakage lemma gives

`ell <= (sqrt(3/128)+32/1023)^2 = 0.033993645149794...`.

For `q=1`, `r=3/5`, the frontier parameters are

`delta=0.205262629519014...`,
` sigma=delta-1/32=0.174012629519014...`,
` ridge_gate=0.498803848329426...<1/2`,
` theta0=75/34>2`.

Thus the full perturbed target has a continuous `C_0` density with a universal `O(1/L)` bound; the final report records the exact resulting constant and checks.

## Remaining gap

This still does not prove that every matrix under the bare three-large-eigenvalue hypothesis has a sufficiently diffuse spectral window. The complementary high-window-leverage/low-cross-rank aggregate branch remains the first full-target debt. The present result strengthens the diffuse exit by making it quantitative over a continuum of window/leverage parameters and stable under an arbitrary dense nonseparable operator tail.
