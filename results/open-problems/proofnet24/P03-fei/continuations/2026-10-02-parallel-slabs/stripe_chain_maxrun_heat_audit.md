# Independent audit: maximum exceptional-layer run and influence deficit

2 October 2026. This audits the root's proposed extension of the unchanged
[almost-symmetric candidate](stripe_extension_almost_symmetric_candidate.md)
and the exact projection identity proved in
[stripe_almost_symmetric_heat_audit.md](stripe_almost_symmetric_heat_audit.md).
Neither earlier file was edited. This new audit records an analytic
derivation rather than an inference from finite examples.

**Verdict: PASS.** The maximum consecutive exceptional-layer run may replace
the number of exceptional layers. The entire disagreement term may also be
charged to the nonsymmetric Dirichlet-energy deficit. For isolated
exceptional layers the stronger exact identity gives the stated uniform
constant 57, independently of how many such layers there are.

## Definitions and scope

Let f be Boolean on the uniform n-cube, n≥1, and let Λ be a set of layer
indices outside which f is constant on each layer. The constant label may
vary arbitrarily with the layer. Let ell be the largest number of vertices
in any consecutive block of Λ. This does not mean the distance between
the first and last exceptional layers. If Λ is empty, f is symmetric and
the established symmetric FEI theorem applies directly.

Let P_sym be the orthogonal projection obtained by averaging over all
coordinate permutations; P_sym f is the real-valued layer-mean function.
For any real u use

I(u)=Σ_S |S| uhat(S)².

Define D_sym=I(f)−I(P_sym f). This is nonnegative because P_sym commutes
with the cube Laplacian and is self-adjoint, so

I(f)=I(P_sym f)+I(f−P_sym f).

In particular D_sym is the residual Dirichlet energy, not merely a
nonnegative difference asserted without a projection argument.

## Exact chain energy

For the uniform random maximal chain Π let the symmetric Boolean
comparator be g_Π(r)=f(X_r^Π), and let d_Π=f−g_Π. As in the audited
candidate, uniform chain edges give E_Π I(g_Π)=I(f), and uniform chain
points give E_Π g_Π=P_sym f. The Dirichlet bilinear form therefore gives

E_Π I(d_Π)
=I(f)+E_Π I(g_Π)−2< f,E_Π g_Π >_Dirichlet
=2[I(f)−I(P_sym f)]
=2D_sym.

The identity is exact for nonmonotone layer labels. Every d_Π is supported
on Λ and ||d_Π||²=4δ_Π, where δ_Π=Pr(f≠g_Π).

## Maximum-run adjacency estimate

For u supported on Λ set v_r²=2^(−n)Σ_{x in layer r}u(x)². Layer-edge
Cauchy–Schwarz gives

<u,A_cube u>≤(n+1)Σ_{r,r+1 in Λ}v_r v_(r+1).

The retained layer path is block diagonal, one block for each consecutive
run. Its top adjacency eigenvalue is the maximum of the block eigenvalues
2cos(π/(b+1)), where b is that block's length. These eigenvalues increase
with b, so the maximum is at most 2cos(π/(ell+1)). It is independent of
the number of distinct blocks. Thus

<u,A_cube u>≤(n+1)cos(π/(ell+1))||u||².

Writing q=ell+1, for n≥q² the same elementary inequality as in the
earlier audit gives

n−(n+1)cos(π/q)≥n/q²,

and hence I(u)≥n||u||²/(2q²). Applying this to d_Π and averaging gives

(2n/q²)E δ_Π≤E I(d_Π)=2D_sym,

so nEδ_Π≤q²D_sym in this regime.

## Small dimension

The candidate's averaged variance proof requires no adjacency or
monotonicity hypothesis. For independent comparators define
D_chain(Π,Π')=Pr(g_Π≠g_Π'). One has E D_chain=Eδ_Π, and

Var_Π(E_x g_Π)
≤2E D_chain²≤2Eδ_Π.

Therefore E_Π Var_x(d_Π)≥2Eδ_Π. Poincaré and the exact energy identity
give 2Eδ_Π≤E I(d_Π)=2D_sym, or Eδ_Π≤D_sym. If n<q², multiplying
by n proves nEδ_Π≤q²D_sym. Together with the preceding regime this
establishes that bound in every dimension.

## Entropy and the isolated-layer case

Average the valid Boolean perturbation inequality
H(f)≤2H(g_Π)+32nδ_Π and use symmetric FEI with constant 12.04 and
E I(g_Π)=I(f). The result is exactly

H(f)≤24.08I(f)+32(ell+1)²D_sym.

Since D_sym≤I(f), this yields the dimension-independent constant
24.08+32(ell+1)² for bounded maximum run, irrespective of |Λ|. One may
round the first term to 25 if a simpler constant is wanted.

If ell=1, no two exceptional layers are adjacent. No cube edge has both
endpoints in the support of any d_Π, so <d_Π,A_cube d_Π>=0 exactly.
Consequently

I(d_Π)=(n/2)||d_Π||²=2nδ_Π.

Averaging and comparing with E I(d_Π)=2D_sym gives the stronger equality
nEδ_Π=D_sym. Therefore

H(f)≤24.08I(f)+32D_sym≤56.08I(f)<57I(f).

This statement allows arbitrary assignments on any number of pairwise
nonadjacent Hamming layers, including alternating layers. It needs no
restriction on the constant labels on intervening layers. Endpoint layers
are automatically constant because they are singletons, but including
them in an upper-bound exceptional set does not invalidate the proof.

## Assessment

The maximum-run scope and deficit bound are fully justified. The empty
exceptional-set case should be declared symmetric rather than using an
undefined maximum block; one can set ell=0 by convention if desired.
The isolated-run disagreement bound is in fact an equality. No new
analytic gap, sign error, normalization error, or dimension assumption
was found. External specialist review and research-priority verification
remain outside this internal audit.
