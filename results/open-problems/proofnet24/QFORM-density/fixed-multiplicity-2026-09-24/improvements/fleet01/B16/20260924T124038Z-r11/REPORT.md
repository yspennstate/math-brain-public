# fleet01/B16 improvement audit — candidate threshold nine

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T124038Z-r11`  
Baseline audited first and independently: source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Upstream improvement reviewed only **after** completion of my independent baseline reconstruction: fleet03/B04 report at master commit `8ff490c177d0cd7d6f33130f1431785e312a9d10`, path `improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`, blob `054facef834d29927713c5d42a1f09a541c5644b`.

## Verdict

**PASS in this independent mathematical reconstruction of the nine-eigenvalue candidate.** Subject to the owner's review protocol, this is only one independent full review of the improvement and therefore the improvement remains **CANDIDATE_PENDING_SECOND_INDEPENDENT_FULL_REVIEW**. This report does not self-award validation/release status.

The reviewed candidate theorem is:

> If `X_i` are independent real variables with densities bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density with
> `||p_Q||_infinity <= 6010 K^2/s`.

Global continuity is not claimed. The no-pivot branch produced by the new Fourier receiver has a continuous `C_0` density.

## 1. Grouped product-Fourier compiler: reconstruction

Let `H,I,J` be disjoint original-coordinate sets, `X_H` independent of `X'=(X_I,X_J)`, and let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. The candidate considers

`Q=F(X_H)+2<W, M X'+beta>+R(X')`,

with arbitrary measurable same-bank phase `F`, arbitrary quadratic/affine `R`, a rank-`k` restriction `M_J`, singular-value product `S`, and residual projected cross rows `C`. For a weighted family of `ell`-subsets with total Gram volume `Z_ell` and inclusion marginals `alpha_i<=1/2`, set `d=k+ell`.

### 1.1 Hub-bank `L^2` step — PASS

Push the complex measure `e^{itF}dP_H` to `W`. Its density `a_t` satisfies pointwise `|a_t|<=p_W`, hence

`||a_t||_2^2 <= ||p_W||_infinity ||p_W||_1 <= M_H`.

With the manuscript Fourier convention and the substitution `xi=2t(l+beta)`, Plancherel gives

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

Push the phase-weighted light-bank law to the corresponding `k`-variable linear image, with complex density `mu_t`. Cauchy--Schwarz therefore gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.

No independence is asserted inside a projected vector.

### 1.2 Light-bank `L^2` reduction — PASS

Condition on `X_I`. Translation in the projected output by the `I`-linear contribution preserves the `L^2` norm. After compact approximate-identity regularization of the conditional pushforward and expansion of its square with an independent copy `X'_J`, the same-bank `J` phase has modulus one and the pure `I` phase cancels. The difference vector `D=X_J-X'_J` has independent coordinate densities bounded by one. Integrating the original independent `X_i`, `i in I`, produces the physical Fourier factors

`prod_i |psi_i(2t<a_i,D>)|`.

The remaining regularizing factor is a probability-density kernel in `M_JD`. This gives the candidate's equation (1.5). Uniform `L^2` bounds on the mollified pushforwards imply, by weak compactness / lower semicontinuity in `L^2`, the same bound for `mu_t`; the report compresses this standard final limiting sentence but no extra assumption is required.

### 1.3 Weighted-subset Brascamp--Lieb step — PASS

Write each relevant row as `a_i=c_i+lambda_i M_J` with `c_i` orthogonal to `row(M_J)`. For an `ell`-subset `T`, the map

`D -> (M_JD,(<c_i,D>)_{i in T})`

has Gram determinant exactly

`S^2 det(C_T C_T^T)`.

Applying the baseline product-projection theorem to the full-row-rank map therefore gives density cap

`e^(d/2)/(S sqrt(det(C_T C_T^T)))`.

For `alpha_i<=1/2`, the baseline scalar Fourier-power estimate at `p=1/alpha_i>=2`, including the scale `2t`, gives

`int |psi_i(2t(y+u))|^(1/alpha_i) dy <= pi sqrt(2e alpha_i)/|t|`.

Weighted Holder over the `ell`-subsets is legitimate after discarding zero-weight subsets. The determinant geometric mean is

`Z_ell^(-1/2) exp(H(w)/2)`,

while the Fourier marginal factors contribute

`exp((1/2) sum_i alpha_i log alpha_i)`.

To verify the entropy bound, order the sampled `ell`-subset uniformly. The entropy of the ordered tuple is `H(w)+log(ell!)`; subadditivity bounds it by the sum of the coordinate entropies, each at most `log ell - sum_i (alpha_i/ell) log alpha_i`. Therefore

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining these terms yields, for `t!=0`,

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^(-d/2))`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4) (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

For `d>2`, direct integration of this envelope and Fourier inversion gives the candidate's formula (1.2). The formal `k=0` endpoint is simply the same light-bank argument with no hub coordinates; treating the zero-dimensional projection separately avoids any notational ambiguity.

## 2. Terminal exact-rank bounds — PASS

When the residual block is absent, the same complex-pushforward/Plancherel argument for `r` literal physical coordinates crossing an independent product bank through a rank-`r` block `P` yields

`|phi(t)| <= min(1, pi^(r/2)e^(r/4)[det(PP^T)]^(-1/4)|t|^(-r/2))`.

Therefore

- `r=3`: `||p||_infinity <=3 sqrt(e)[det(PP^T)]^(-1/6)`;
- `r=2`: `sup_a E|Q-a|^(-1/2) <=4 sqrt(2)e^(1/4)[det(PP^T)]^(-1/8)`.

All within-bank quadratic and affine phases remain inside the complex pushforwards; no projected-coordinate independence is used.

## 3. Marginal-free order-three density receiver — PASS

For a literal cross block `M`, put `Z=E_3(M)=e_3(MM^T)`. Let `J_i` be the incident third-volume mass at physical row `i`; `sum_i J_i=3Z`.

- If every normalized marginal `J_i/Z<=1/2`, apply the grouped compiler at `(k,ell,d)=(0,3,3)`.
- If some `J_i>Z/2`, keep row `w=m_i` as a physical hub and orthogonally project the other rows off `w`. Exact Gram--Schmidt gives
  `J_i=||w||^2 e_2(CC^T)`.
- If a residual row `j` is heavy for that second volume, promote it. With promoted two-row matrix `P`, another exact Gram--Schmidt identity gives
  `H_ij=det(PP^T)||C_2||_F^2>J_i/2`.
- If a remaining row is heavy for this first volume, promoting it gives a physical three-row Gram determinant greater than `H_ij/2`.

The four resulting branches are paid respectively by `(k,ell)=(0,3)`, `(1,2)`, `(2,1)`, or the terminal exact-rank-three estimate. The largest constant is

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

so

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`.

Each branch has an integrable characteristic-function majorant, hence a `C_0` density for this fixed-cross-block conclusion.

## 4. Marginal-free order-two half-potential receiver — PASS

The identical promotion scheme one dimension lower gives

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,

with

`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

This is correctly used only as a half-potential bound, not as a bounded-density theorem. The branch constants after one and two promotions are smaller than `C_2`.

## 5. Nine-direction theorem — PASS

Normalize `K=s=1`.

### No pivot

The baseline spectral-to-volume proposition at `k=3` applies under `s_9(A)>=1` and gives `V_3(A)>=kappa^3`. The fair coordinate cut gives a literal cross block with

`E_3(M)>=4^(-3)kappa^3`, hence `E_3(M)^(-1/6)<=160`.

The new order-three receiver therefore gives

`||p_Q||_infinity <=160 C_3=2370.93402605488...<2400`.

### Scalar pivot

A scalar pivot removes one coordinate, so the Schur complement retains at least eight eigenvalues of modulus at least one.

- If the Schur complement has a manuscript pivot, the baseline pivot proposition needs only two large directions and gives truncated half potential at most `600`; adding the `|R-a|>1` tail costs at most one.
- If it has no pivot, then `s_5>=1`. The baseline spectral-to-volume proposition at `k=2` gives, after a fair cut, `E_2>=4^(-2)kappa^2`. The new order-two receiver yields
  `C_2 sqrt(160)=152.99191115498...<153`.

Thus the full Schur half potential is at most `601`, and the scalar square profile gives

`||p_Q||_infinity<=eta^(-1/2)*601=6010`.

### Pair pivots

A definite pair is bounded by `pi/sqrt(eta)<32`. An indefinite pair leaves at least seven Schur directions, so in particular one surviving direction; the baseline hyperbolic/log-potential calculation applies unchanged and gives `<251`.

Hence the normalized theorem is bounded by `6010`. Rescaling `Y=KX` and `Q=(s/K^2)Qtilde` gives

`||p_Q||_infinity <=6010 K^2/s`.

All original hypotheses are preserved.

## 6. Why this run does not claim a threshold below nine

The present structural route reaches a genuine terminal obstruction at eight directions. For an order-three no-pivot volume argument, the worst sampled bad-ratio seed has `r=2`. The baseline completion has global rank at most `3r=6`; under only `s_8>=1`, singular-value rank subtraction forces only two large diagonal residual coordinates. The restricted interpolation rank is also at most two, so a diagonally dominant `2x2` residual block has rank exactly two and creates no contradiction. Under `s_9`, three such coordinates are forced and the contradiction closes. Thus changing constants cannot remove the `9=3r+(r+1)` count at this endpoint.

Nor can one simply replace the order-three density receiver by an order-two indefinite receiver. Even for independent cap-one variables, an indefinite rank-two quadratic can have an unbounded logarithmic density: for `U,V` independent uniform on `[-1,1]`, the density of `U^2` is `1/(2 sqrt{s})` on `(0,1)`, so the density of `U^2-V^2` at zero contains

`int_0^1 [1/(2 sqrt{s})]^2 ds = infinity`.

This does not disprove an eight-eigenvalue theorem; it shows that an `E_2` crossing-volume bound alone cannot be its density endpoint. The eight-direction terminal seed carries additional overlap-one / multi-bank structure and would require a genuinely new product-preserving receiver using that extra structure before absolute values are taken.

## Review-state conclusion

- Baseline 17-eigenvalue theorem: independently PASS in this run (separate audit artifact).
- Candidate 9-eigenvalue theorem: independently PASS in this run.
- Candidate 9 status under owner protocol: **PENDING A SECOND GENUINELY SEPARATE COMPLETE REVIEW**; do not mark independently validated from this report alone.
- Threshold `<9`: **not proved in this run**.
- Unrestricted three-eigenvalue conjecture: not addressed by this fixed-multiplicity improvement and remains open.
