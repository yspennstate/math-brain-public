# Affine coset merge and quadratic GU

Let `C_j=b+j a+V` be two distinct affine cosets of the same subspace
`V<=F_2^m`, and put `D=C_0 union C_1`. For `x` in a finite set `E`, write

`N_E(x)=#{y in E:y>=x}`.

For `x in C_j`, with `R=supp(x)`, the within count is the zero fiber of the
linear projection `V -> F_2^R`; the cross count is the `a|_R` fiber. Hence the
cross count is either zero or equals the within count. Therefore

`log_2(N_D(x)/N_(C_j)(x)) in {0,1}`,

and averaging proves

`U(D)-[U(C_0)+U(C_1)]/2 <= 1`.

For a quadratic phase, the two restrictions in physical coordinate `i` are
`g` and `+/- chi_a g`. Their squared spectra are uniform on `C` and `C+a`.
If the cosets are distinct, the parent law is a fair new spectral bit times
the uniform law on their union, so

`Delta_i U <= 1/2+1=3/2=3 Inf_i`.

If the cosets coincide, the parent law is uniform on a graph over `C`; every
graph upper fiber injects into the corresponding upper fiber in `C`, giving
`Delta_i U<=0`. If `a=0`, `Delta_i U=0`. Thus every coordinate satisfies
`Delta_i U<=3 Inf_i`, and `G<=3I`.
