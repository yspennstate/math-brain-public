# PROB10-09 idea-before-code: noncentral extension / vector-valued cover lift

Timestamp: 2026-09-20T11:52Z.  Parent source remains the original Benjamini--Schramm Cayley-graph conjecture for iid **bond** percolation: `p_c(G)<p_u(G)` for every locally finite Cayley graph of every finitely generated nonamenable group.  This note is an idea record, not a closure claim.

## Continuity and collision boundary

The previous R20 theorem handles horizontal Cayley lifts through arbitrary **central abelian** kernels via scalar/character magnetic domination.  An earlier R20 report explicitly identified a noncentral semidirect/crossed-product fibre as the next missing mechanism.  NM13-11 owns the separate free-core / torsion-block / higher-rank-lattice subgroup lane; this note stays on the quotient-cover/operator lane and does not touch its `SL_n`, triangle-fibre, power-thickening, or factor-branching claims.

The June archive's finite-set escape/BK last-exit, killed-SAW, boundary-energy, scalar nonbacktracking/product, quotient/fibre-shell, and fixed-endpoint bridge attempts remain consumed history and are not renamed as new.

## Exact new idea

Let

`1 -> N -> Gamma --pi--> Q -> 1`

be **any** group extension, with no centrality or amenability assumption on `N`.  Let `S_Q` be a finite inverse-closed generating set of `Q`, and choose inverse-compatible lifts `S~` whose subgroup is all of `Gamma`.  Identify each fibre `pi^{-1}(q)` with `N` using a section.  Right multiplication by a lifted generator sends the Hilbert fibre over `q` unitarily onto the fibre over `qs`.  Thus the lifted adjacency is a matrix-/Hilbert-valued magnetic operator

`(A_Gamma f)(q) = sum_{s in S_Q} U(q,s) f(qs)`

with each `U(q,s)` unitary on `ell^2(N)`.  For `F(q)=||f(q)||_2`, fibrewise triangle inequality gives

`||(A_Gamma f)(q)||_2 <= sum_s F(qs) = (A_Q F)(q)`.

Therefore

`||A_Gamma||_{2->2} <= ||A_Q||_{2->2}`

for an arbitrary normal kernel.  This bypasses the scalar Fourier transform completely.

If `S_Q` contains `k` generator pairs freely generating `F_k`, their chosen lifts still freely generate `F_k` (a relation upstairs would project to one downstairs), so the lifted Cayley graph contains the standard `2k`-regular tree and

`p_c <= 1/(2k-1)`.

Combining this with the already-verified nonbacktracking transfer gives the structural criterion

`beta_D(rho_Q) < 2k-1  =>  p_c < p_{2->2} <= p_u`,

where `D=|S_Q|`, `rho_Q=||A_Q||`, and

`beta_D(rho)=sqrt(D-1)` if `rho<=2sqrt(D-1)`, otherwise
`beta_D(rho)=(rho+sqrt(rho^2-4(D-1)))/2`.

The key point is that this criterion is now stable under arbitrary group extensions, provided the selected horizontal lifts generate the full extension.

## Explicit noncentral infinite-kernel test family

Take the genus-two surface group

`Q = <a1,b1,a2,b2 | [a1,b1][a2,b2]=1>`

with its standard 8-element inverse-closed generating set.  Let

`M = [[0,-1],[1,1]] in SL_2(Z)`

and define `alpha:Q->SL_2(Z)` by `alpha(a1)=M` and `alpha(b1)=alpha(a2)=alpha(b2)=I`; the surface relation maps to the identity, so this is a homomorphism.  Set

`Gamma = Z^2 semidirect_alpha Q`.

Let `e1=(1,0)`, `e2=(0,1)`, and `v=(0,-1)`.  Since `(M-I)v=e1`, choose horizontal lifts

`A1=(0,a1)`, `B1=(v,b1)`, `A2=(0,a2)`, `B2=(0,b2)`

and their inverses.  The lifted surface relator evaluates to `(e1,1)`.  Conjugating this kernel element by `A1` gives `(M e1,1)=(e2,1)`.  Hence the lifts contain all of `Z^2`, and after removing their translation parts they contain the pure quotient generators; therefore they generate all of `Gamma`.

This kernel is infinite, abelian, normal, and **not central** because `M e1=e2 != e1`.  The group contains `Z^2`, so this example is outside the Gromov-hyperbolic special case.  Its infinite amenable normal subgroup is also a direct obstruction to non-elementary acylindrical hyperbolicity (to be source-checked before the final report).

For the standard genus-two quotient, the consumed Zuk bound gives `rho_Q <= 4 sqrt(2)`.  Freiheitssatz gives `k=3`; `D=8`.  Hence

`beta_8(4sqrt2)=1+2sqrt2 < 5 = 2k-1`,

so the expected certificate is

`p_c <= 1/5`, `p_u >= 1/(1+2sqrt2)`,

and

`p_u-p_c >= (10sqrt2-12)/35 > 61/1000`.

This is the same numerical floor as the earlier central genus-two horizontal family but on a genuinely noncentral infinite-kernel extension, so the source metric stays PARTIAL while the structural scope changes.

## Negation test / exact scope boundary

The adjacency domination itself needs only a graph-cover lift and does **not** need the lifts to generate all of `Gamma`.  However, if the lift subgroup `H=<S~>` is proper, `Cay(Gamma,S~)` is disconnected and is not the requested connected Cayley graph for `Gamma`; one has only proved a statement for `H`.  Therefore generation of the full extension is an essential admissibility hypothesis.  In the explicit semidirect example the lifted relator plus its `M`-orbit supplies a direct exact generation proof.

A second negation test is that replacing `M` by a matrix for which the orbit of `(M-I)v` spans only a proper sublattice makes the horizontal subgroup miss kernel cosets; such a parameter choice is not silently admissible.

## Three genuinely different routes compared

1. **Vector-valued cover domination (primary; pursue).**  Replace scalar central Fourier characters by unitary fibre transports and the fibrewise norm inequality.  This should prove the arbitrary-extension criterion and the explicit `Z^2 semidirect Q` family.
2. **Fourier orbit / crossed-product decomposition (backup; not needed if 1 works).**  For `Z^m semidirect Q`, Fourier transform `Z^m`; quotient generators move characters by the dual action, so one obtains an operator on `Q x T^m`, not scalar magnetic fibres.  A Schur bound appears possible but is less clean than the Hilbert-fibre domination above.
3. **Subgroup-only comparison (reject for this run).**  Prove a gap on a finite-index or normal subgroup and try to transfer it after adding generators.  The threshold monotonicities point in incompatible directions and do not preserve a strict `p_c<p_u` gap without a new theorem; this is the same exact obstruction already recorded in the central-kernel lane.

Next step after this note: execute a small exact checker only for the finite algebraic core (`det M`, `(M-I)v`, `M e1=e2`, radical gap inequality), while keeping the proof itself analytic and written in the immutable report.