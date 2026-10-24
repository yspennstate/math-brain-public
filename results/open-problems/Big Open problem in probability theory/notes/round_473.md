# Round 473 finite-type formula for \(\pc(T_d\square F)\)

Round 473 adds the matching finite-width percolation object for the
finite-fiber annular transfer.

Let \(F\) be finite and connected, and let \(q=d-1\).  Root the tree and
explore Bernoulli bond percolation on \(T_d\square F\) away from the parent
direction.  A cluster entering a bag carries a type
\[
  A\subseteq V(F),\qquad A\ne\emptyset,
\]
where \(A\) is the set of fiber coordinates in the current bag connected to
the parent-side cluster after closing under open \(F\)-edges inside the bag.

Given a type \(A\), one forward child bag receives initial open entries
\[
  D=\{f\in A:\text{ the tree edge from }(v,f)\text{ to }(w,f)\text{ is open}\}.
\]
Inside the child bag, close \(D\) under the open percolation subgraph of
the finite graph \(F\).  Let the resulting nonempty subset be \(B\).  This
defines a finite transition kernel
\[
  K_p(A,B)=
  \mathbb P_p\bigl(\operatorname{cl}_F(D)=B\bigr),
  \qquad A,B\subseteq V(F),\ A,B\ne\emptyset.
\]
The \(q\) forward child bags are conditionally independent and identically
distributed, so the multitype Galton-Watson mean matrix is
\[
  M_p(A,B)=q\,K_p(A,B).
\]

Consequently,
\[
  \pc(T_d\square F)
  =
  \inf\{p\in[0,1]: r(M_p)>1\},
\]
equivalently the critical point is determined by \(r(M_p)=1\) when the
crossing is nondegenerate.  The root bag has \(d\) children rather than
\(q\), but this finite initial difference does not change the survival
threshold.

Thus the finite-fiber annular target from Rounds 470--472 can be stated as a
comparison between two finite objects:

1. the self-avoiding boundary-transfer singularity
   \[
     \rho_F(q)=\Gamma_{\rm ann}(T_d\square F);
   \]
2. the inverse percolation threshold \(1/p_*\), where
   \[
     r(M_{p_*})=1.
   \]

The desired finite-fiber inequality is
\[
  \rho_F(q)<1/p_*.
\]
This comparison is better calibrated than the embedded-tree sufficient
condition \(\rho_F(q)<q\), because the finite graph \(F\) can increase the
branching capacity of percolation as well as the annular SAW transfer.
