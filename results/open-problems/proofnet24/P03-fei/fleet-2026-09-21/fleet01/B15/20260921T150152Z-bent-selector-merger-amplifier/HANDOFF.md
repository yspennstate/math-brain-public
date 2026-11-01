# B15 handoff — raw merger carry is unbounded; only compensated transfer survives

Full FEI remains **OPEN / NOT PROVED**. This run is `WITHOUT_VERIFIED_BRAIN` and does not rerun the settled read-once certificate.

## Exact universal identity

For the packet valuation and arithmetic remainder

`R(f)=sum_a p_a r_a`, `D(f)=sum_a p_a log2(1/(a 2^r_a))`, with `H=2R+2D`, define for restriction in coordinate `i`

`G_i=(R(f_+)+R(f_-))/2-R(f)` and `L_i=D(f)-(D(f_+)+D(f_-))/2`.

Then exactly

`L_i-G_i = ( H(f)-(H(f_+)+H(f_-))/2 )/2 >= 0`.

Thus any positive valuation/carry created by restriction is accompanied by at least as much arithmetic-remainder drop. The raw ledgers should not be paid separately.

## Infinite bent-selector obstruction

For `r>=2`, let

`g_r(y)=(-1)^(y1*y2+...+y_(2r-1)*y_(2r))`,

so every Fourier coefficient of `g_r` has magnitude `q=2^-r`, and its unique signed packet has carry depth `r`. Let

`F_r(y,t)=g_r(y)` for `t=0`, and `F_r(y,t)=-1` for `t=1`.

The parent has exactly three Fourier magnitudes:

* `q/2`, multiplicity `2(4^r-1)`, packet depth `1`;
* `(1-q)/2`, singleton depth `0`;
* `(1+q)/2`, singleton depth `0`.

On the `t=0` branch the child is `g_r`. Its depth-`r` packet splits by parent-pair ancestry into only two source groups:

* `4^r-1` nonempty coefficients, signed mask `2^r g_r-1`, depth `0`;
* one empty coefficient created from the unequal exceptional parent magnitudes, signed mask `1`, depth `0`.

Their sum is `2^r g_r`, depth `r`. Thus **two depth-zero ancestry groups create arbitrarily deep child carry**. Their ancestry-label entropy is `h_2(4^-r)->0`.

The raw average valuation gain and selector influence are

`G_t(F_r)=(r-1+4^-r)/2`,

`Inf_t(F_r)=(1+2^-r)/2`.

Therefore `G_t/Inf_t -> infinity`, even if the denominator is augmented by the ancestry-label entropy. No universal local inequality can pay raw merger valuation by coordinate influence, by number of ancestry classes, or by that label entropy.

Yet the restriction entropy cost stays bounded:

`Delta_t H -> 2`, `Delta_t H / Inf_t -> 4`,

and `D(F_r)=G_t(F_r)+Delta_t H/2`. The two `Theta(r)` arithmetic ledgers cancel to the actual `O(1)` entropy step.

## Next B15 target

Do **not** try to bound merger-created `R` or the `D` drop separately. The only viable restriction-scale arithmetic target from this decomposition is the compensated quantity

`L_i-G_i = Delta_i H/2`.

Use cross-coordinate relations in the merger graph to seek an existential coordinate with `(L_i-G_i) <= C Inf_i`. The bent-selector family is a mandatory stress test: any proposed lemma that first upper-bounds `G_i` or `L_i` individually is already false.
