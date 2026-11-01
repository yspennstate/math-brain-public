# Independent probability review: T384 coordinate-input initialization

**Disposition: probability proof passes for the stated inputs `x_j=e_j`, fixed `k`, and independent standard symmetric stable coordinates.** The proof of the joint marked-process/product/square law and the conditional effective-`Q` transform is sound. One **required scope repair** is to say conspicuously that “orthogonal inputs” here means this specified coordinate basis, not arbitrary orthonormal inputs. For `α<2`, an iid stable coordinate vector is not rotationally invariant: rotating the inputs changes the joint projection law, so the shared-mark independence and axis-separation argument cannot be transferred by an orthogonal change of basis. Signed/permuted coordinate axes can be handled by symmetry, but a general orthogonal family needs a new proof and likely a different law.

## Shared `W` and axis separation

For `X_j=W(U_j)_+`, conditional independence of `U_j,U_ell` at a fixed `W=w` gives, for fixed `ε>0`,

`P(|X_j|>εb_m,|X_ell|>εb_m | W=w) ≤ K_ε min(1,(|w|/b_m)^α)^2`.

With `P(|W|>x)≤Kx^(−α)` and the truncated-moment estimate `E[|W|^(2α)1_{|W|≤b}]≤Kb^α`, splitting at `b_m` yields

`mP(|X_j|>εb_m,|X_ell|>εb_m) ≤ K_ε m b_m^(−α)=O_ε((log m)^(−1))`.

This is the crucial shared-`W` calculation; it rules out a common product jump even though both outputs use the same neuron. For `N/F_j`, `N/C_j`, `F_j/C_j`, `F_j/C_ell` (`j≠ell`), and `C_j/C_ell`, the stated splits and independence similarly make each one-row overlap `o(1/m)`. Since `k` is fixed, every mixed term in the finite one-row transform has at least one such pair, so multiplication by `m` kills all cross terms. The limiting compound-Poisson coordinates and the marked PPP therefore factor jointly. The `N` factor is the **whole vector-marked process**: its compact-test Laplace functional and the mark-escape bound handle the unscaled iid `U_1,...,U_k` marks, not only individual atom counts.

The one-sided tail of each product is `αc²t^(−α)log t`, hence its normalized tail is `c²x^(−α)` because `b_m^α=m log m` and `log b_m/log m→1/α`. The stable-characteristic exponent `c|t|^α` is correct. The square tail and exponent are respectively `c x^(−β)` and `cΓ(1−β)s^β`. Symmetric truncation of each product summand has mean zero even when `α≥1`; the discarded sum's `L²` bound `O(ε^(2−α))` removes the product cutoff without an omitted centering. The discarded square sum's mean `O(δ^(1−β))` removes its cutoff. The finite list of coordinates permits a union bound, so this proves mutual independence of `N,F_1,...,F_k,C_1,...,C_k` rather than merely pairwise independence.

The effective-`Q` continuous mapping is also justified: `F_j=y_j` and `u_j=0` are null boundaries, the `|z|≤ε` contribution is uniformly controlled by its unmarked squared mass, large `|z|>R` atoms have vanishing probability as `R→∞`, and compact-annulus marks can be truncated. The limiting `Q_j` is almost surely finite.

## Conditional transform and dependence on `F`

Conditional on the full `F` vector, `N` and all `C_j` retain their independent laws. On either `z` half-axis, `x=z²` has Lévy measure `βc x^(−1−β)dx`, and one atom carries independent marks `B_j=1_{U_j>0}~Bernoulli(1/2)`. Integrating `1−exp(−x\sum_{\sigma_j=\pm1}\lambda_jB_j)` gives precisely

`E[e^(−Σ_j λ_j Q_j)|F] = exp{−cΓ(1−β)[Σ_j λ_j^β + E_B(Σ_{σ_j=+1} λ_j B_j)^β + E_B(Σ_{σ_j=−1} λ_j B_j)^β]}`.

Thus equation (8) has the correct half-axis coefficient and does **not** insert an extra factor of two. Each individual `Q_j` has conditional Laplace transform `exp[−(3/2)cΓ(1−β)λ_j^β]`, independent of the complete `F` vector. The **joint** `Q` law depends on the sign partition of `y_j−F_j`. For example, with `k=2`, `λ_1=λ_2=1`, and `h=cΓ(1−β)`, the conditional transform is `exp{−h[5/2+2^β/4]}` for equal signs and `exp(−3h)` for opposite signs. These differ strictly for `0<β<1`; all sign patterns have positive probability for finite fixed labels. In the opposite-sign case the two selected first-layer contributions use independent `z` half-axes, while equal signs can share a jump. This proves the stated warning that the `Q` vector is generally dependent on `F`, despite independence of all primitive limits.

## Requested edit

Retitle or qualify the first paragraph and final scope sentence as **coordinate orthogonal inputs `x_j=e_j` only**. No change to (1)–(8) is needed within that model. The dynamical interpretation of these `Q_j` remains a separate result and should explicitly retain whichever loss-normalization convention its ODE uses.
