# r35 late-source addendum — projection certificate as zero-KL Gibbs certificate

After the main r35 report was written, I consumed the newer completed fleet01/B04 result

`QFORM-GIBBS-SOFT-HUB-v1`, source

`yspennstate/math-open-problems@da8e2c011cc93a5c776a1de6010f7366da5f2fbf:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T144427Z-fleet01-B04-QFORM-auto11-r13/REPORT.md`.

For row-triple aggregate volumes `a_S`, let `p(S)=a_S/E3(M)`. Fleet01/B04 defines, for a marginal cap `h`,

`G_h(M)=max_{mu: all inclusion marginals <=h} exp(H(mu)+sum_S mu_S log a_S)`

and proves the exact identity

`G(mu)=E3(M) exp[-D_KL(mu||p)] <= E3(M)`.

It also proves the Gibbs dual and the soft-hub alternative: poor `G_h` forces a physical hub set `H` with `|H|<3/h` and residual third volume `E3(M[H^c,*])<=G_h`.

The r35 projection/tail certificate gives an exact zero-KL criterion for this new optimizer. If a projection `P` has

`h(P)=max_i [sqrt(P_ii)+sqrt(3)|||(I-P)M||op/sqrt(T2)*sqrt(1-P_ii)]^2 <3/4`,

then the canonical volume law itself has every marginal at most `h(P)`. Therefore it is feasible in the definition of `G_{h(P)}` and

`boxed( G_{h(P)}(M)=E3(M) ).`

So the r35 certificate is precisely a **zero entropy-loss region** of the newer Gibbs dual: no determinant-volume reweighting is necessary. The optimized q in the main report then spends the entire `E3` currency.

For the explicit Hadamard target `M=D H_32/sqrt(32)`, `D=diag(2,2,1^30)`, the exact canonical marginals are

`alpha_heavy = 4[4*30+C(30,2)]/8020 =2220/8020`,
`alpha_tail  = [16+8*29+C(29,2)]/8020 =654/8020`.

Thus `max alpha=2220/8020<1/2`; at `h=1/2`, the Gibbs optimum is exactly

`G_(1/2)=E3=8020`.

Applying the completed fleet01/B04 theorem at its actual inequality gives again

`||p_Q||inf <=3e*8020^(-1/6)=1.822720208282299...`,

with `p_Q in C_0`. This is a direct equation-level application of the newest same-role peer theorem, with zero KL penalty certified by the new projection/tail estimate.

A useful universal downstream split for any rank-at-least-three physical cross block is obtained by setting `h=3/5` and `g=2^(-18)` in the peer theorem. Either

`G_(3/5)>=2^(-18)`

and

`||p_Q||inf <= [3e/((3-12/5)sqrt(6/5))] * 8`
`             =99.25761834022717...`,

with a continuous density, or there is a physical hub set `H` with at most four rows and

`E3(M[H^c,*]) <2^(-18)`.

This does not solve the full conjecture because the bare full-matrix spectral hypothesis does not itself force one rank-three physical cross block. It does sharpen the remaining B04 cross-block obstruction: after the projection/tail zero-KL exit and entropy-reweighting exit, the survivor is a bounded physical hub plus a quantitatively tiny residual third volume.