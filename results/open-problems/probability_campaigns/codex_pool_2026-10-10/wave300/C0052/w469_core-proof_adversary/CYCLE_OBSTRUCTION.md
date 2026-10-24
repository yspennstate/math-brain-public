# Exact obstruction to extending the tree argument by edge factorization

Author: w469, 2026-10-10. Status: author proof of a finite-cycle special case; independent check by w470 pending. No counterexample to C0052 or to a possible nonlinear comparison on cyclic graphs is claimed.

Consider a simple four-edge cycle with uniform coupling parameter t=beta J>0, zero field and free boundary. For one sourceless random current, the parity vector of the four edges is either all even or all odd: each vertex has degree two, so the requirement of even incident parity makes adjacent edge parities equal, and this propagates around the cycle.

The total factorial weight of the all-even sector is cosh(t)^4 and that of the all-odd sector is sinh(t)^4. Consequently the event O that every edge is odd has probability

h = sinh(t)^4/[cosh(t)^4+sinh(t)^4]
  = tanh(t)^4/[1+tanh(t)^4],

with 0<h<1/2. For two distinct edges e and f, let B_e=1{n_e is odd}. Then B_e=B_f almost surely, E B_e=E B_f=h, E[B_e B_f]=h, while (E B_e)(E B_f)=h^2<h. Thus edge values in the conditioned sourceless current are not independent. This is an exact dependency obstruction, not a numerical estimate.

The tree proof's edge independence comes from uniqueness of the parity vector fixed by a source set. On this single cycle the source constraint permits a global cycle parity bit. More generally a cyclic graph has a cycle-space family of parity assignments; conditioning on only the sources does not fix them. Conditional independence of factorial edge weights inside one fixed parity vector does not establish independence after mixing the vectors.

Therefore the attempted direct extension of TREE_NONLINEAR.md stops at its first product over bridge-edge laws. The missing premise would be a proved comparison after averaging over the correlated cycle parity variables, or an alternative exploration/martingale argument under the full current law. Neither has been established here for critical Z^3. Replacing the lattice by a spanning tree changes the current measure and needs a quantitative comparison of its own.

NEXT: Attempt the original-current lower bound through a dependence-aware exploration, or prove a nonlinear original-versus-augmented comparison that controls cycle-space mixing.
