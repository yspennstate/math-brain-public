SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T13:59:12Z.
attacking: normalized-fragment critical-budget barrier — test the partner square-root critical Fourier mixture on a fixed whole cap-one law partitioned into arbitrarily many active pieces, then compare with a whole-active target certificate.

# Early substantive checkpoint

Full QFORM remains open. The new calculation below is a proof-interface obstruction, not a counterexample to the conjecture.

Use the completed designated-partner theorem account03/B14 r35, `QFORM-SQRT-CRITICAL-BUDGET-MIXTURE-v1`, canonical `math-open-problems@29096949260b7ec2e9659c1379bd0a0882a37387`. For an invertible indefinite physical pair with `D=kappa=1`, its optimized critical-tail envelope is

`F(K)=inf_{y>0} [4 sqrt(K/y)+Omega(y)]`,

and for a positive decomposition into unnormalized remainder pieces of masses `m_j` satisfying

`|hat nu_j(t)| <= min(m_j,k_j/|t|)`,

the effective budget is `B=sum_j sqrt(m_j k_j)` and the theorem gives `||p_Q||_inf <= F(B^2)`.

Take independent cap-one variables `X1,X2,Z,V`, with `Z~Unif[1,2]`, `V~Unif[0,1]`, and

`Q=2X1X2+2ZV`.

The quadratic matrix has spectrum `{1,-1,1,-1}`. Condition on `Z=z`. The whole remainder `2zV` is uniform on an interval of length `2z`, so its minimal critical constant is exactly

`K_whole(z)=sup_{t!=0}|t||phi_(2zV)(t)|=1/z`.

Thus the whole-law square-root budget is

`b_1=int_1^2 z^(-1/2) dz = 2(sqrt(2)-1)`.

Now partition the SAME active law `V~Unif[0,1]` into `N` equal positive pieces `nu_j=1_[(j-1)/N,j/N] dx`, each of mass `m_j=1/N`, and normalize each piece before applying the r35 Fourier certificate. For fixed `z`, the normalized pushforward `2z V | {V in I_j}` is uniform on an interval of length `2z/N`, hence its minimal critical constant is exactly

`K_j(z)=N/z`.

Equivalently, for the unnormalized piece the exact coefficient is

`k_j(z)=m_j K_j(z)=1/z`.

Therefore the r35 Hellinger-type budget after active refinement is

`B_N(z)=sum_(j=1)^N sqrt(m_j k_j(z))=sqrt(N/z)`,

and after the outside `z`-mixture

`b_N=sqrt(N) b_1`,
`K_eff,N=b_N^2=(12-8sqrt(2))N`.

So merely partitioning one fixed unit interval law raises the optimized mixture parameter by an exact factor `N`, even though the underlying probability law and quadratic form have not changed.

For `K>=1`, the explicit envelope itself diverges: split the optimizer at `y=sqrt(K)`. If `y<=sqrt(K)`, the first term is at least `4K^(1/4)`; if `y>=sqrt(K)`, then `Omega(y)=log y+2c_E >= (1/2)log K+2c_E`. Hence

`F(K)>=min{4K^(1/4),(1/2)log K+2c_E}->infinity`.

Thus the fragment-first r35 certificate diverges (at least logarithmically in `N`) on a single unchanged cap-one input law. This is stronger than a remote-fragment stress test: no large translations or support diameter are needed.

The required Claude source has been freshly read at the current compatible master version of `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its proved Theorem A in `COUNTEREXAMPLE_SEARCH.md` applies to this same four-dimensional matrix because all four eigenvalues have modulus one, and gives

`||p_Q||_inf <= 6 kappa_3^(1/3)`,

uniformly in the laws. Hence the true output has a fixed target-valid bound while the normalized-fragment critical-Fourier proof interface diverges. This is an obstruction to the proof order only.

Provisional label: `QFORM-ACTIVE-INTERVAL-PARTITION-SQRT-BUDGET-BARRIER-v1`.

First unpaid implication: after exact law-level extreme localization, keep every certificate-active extreme marginal whole until a whole-active D'/D5/ridge/mixed-hub/grouped-bank/Schur-slope/fractional-trace certificate has been paid; do not recursively normalize its interval components unless the resulting unnormalized critical coefficient is genuinely mass-homogeneous (`k_j<=K0 m_j`).
