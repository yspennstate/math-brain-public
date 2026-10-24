# PROB10-09 idea-before-code — quotient Cheeger transfer + nonbacktracking spectral gap

Timestamp: 2026-09-20T12:52Z.

Frozen parent remains the original Benjamini–Schramm iid **bond**-percolation conjecture for every Cayley graph of every finitely generated nonamenable group. This is a complementary R20 quotient-cover route; it does not take NM13-11's free-core / higher-rank-lattice / triangle-fibre lane.

## New idea before code

The previous R20 arbitrary-extension theorem proved, for an inverse-compatible horizontal lift of a finite symmetric quotient generating set,

`||A_X|| <= ||A_Q||`,

but its `p_c` witness still required a visible free subset in the quotient generators. Replace that free-tree witness by **edge expansion**, which survives arbitrary graph covers.

Let `X -> Q` be the labelled Cayley cover coming from a surjection `Gamma -> Q` and one horizontal lift of every quotient generator. For a finite `K subset X`, let

`f(q)=|K cap pi^{-1}(q)|`.

Above every undirected base edge `{q,q'}` the lift is a perfect matching, so the number of lifted boundary edges above it is at least `|f(q)-f(q')|`. Hence

`|partial_E^X K| >= sum_{qq'} |f(q)-f(q')|`.

Integer coarea gives

`sum_{qq'} |f(q)-f(q')| = sum_{m>=1} |partial_E^Q {f>=m}| >= phi_E(Q) sum_q f(q)`.

Thus

`phi_E(X) >= phi_E(Q)`.

Benjamini--Schramm's bound `p_c <= 1/(phi_E+1)` then gives

`p_c(X) <= 1/(phi_E(Q)+1)`.

On the uniqueness side, the previous Hilbert-fibre domination and the June nonbacktracking polynomial recurrence give, with `D=|S_Q|`, `r_Q=||A_Q||`,

`p_{2->2}(X) >= 1/beta_D(r_Q)`.

Therefore the complete quotient criterion should be

`beta_D(r_Q) < 1+phi_E(Q)  =>  p_c(X)<p_{2->2}(X)<=p_u(X)`.

This removes the visible-free-subgroup hypothesis entirely.

## Pure spectral corollary to derive exactly

Juschenko--Nagnibeda quote the Mohar/Dodziuk lower bound, in their normalization `rho=r_Q/D`,

`h=phi_E/D >= D(1-rho)/(D-1)`.

Equivalently

`phi_E(Q) >= D(D-r_Q)/(D-1)`.

So it is enough that

`beta_D(r_Q) < 1 + D(D-r_Q)/(D-1)`.

I will solve this inequality exactly before claiming a threshold. The expected nontrivial equality root is

`r_*(D)=(D^3+3D^2-4D+1)/(D(2D-1))`,

or normalized

`rho_*(D)=(D^3+3D^2-4D+1)/(D^2(2D-1))`.

If the algebra checks, this strictly improves the old `rho<1/2` sufficient condition at each finite `D`, while remaining only a sufficient criterion, not the universal conjecture.

## Three materially different routes compared

1. **Cover coarea + nonbacktracking operator — develop.** Transfers the base Cheeger witness to every connected horizontal lift and uses the already proved Hilbert-fibre/nonbacktracking endpoint. This is the primary route.
2. **Classical Benjamini--Schramm two-point theorem + spectral Cheeger — comparison only.** Their condition `r p_c<1`, combined with the same Mohar bound, gives a weaker finite-degree spectral threshold. Compute the exact gap against route 1 rather than relabel it as new.
3. **Visible free subgroup/tree witness — deliberately not used.** It gives stronger numerical bounds in surface examples but cannot address groups without nonabelian free subgroups. The present iteration is specifically testing whether expansion can replace that hypothesis.

## Negation / boundary tests planned

- Check the exact algebra of the root and the sign condition introduced by squaring the nonbacktracking radical.
- Check `D=3,4,5` against the branch point `2 sqrt(D-1)`; no hidden branch switch is allowed.
- Calibrate on the `D`-regular tree.
- Verify the criterion is not automatic from nonamenability (`rho<1` is much weaker than `rho<rho_*(D)`).
- Preserve the previous exact obstruction: if the horizontal lifts generate only a proper subgroup of `Gamma`, the labelled graph on all of `Gamma` is disconnected and is not the requested Cayley graph; cover inequalities alone do not fix admissibility.

No code or numerical checker was run before this note was persisted.