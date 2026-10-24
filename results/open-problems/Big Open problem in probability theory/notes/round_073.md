# Round 073 log

## Goal

Add a first explicit cyclic finite-fiber calibration after closing the
finite-type tree cases.

## Finite-fiber high-branching tree bundles

Added Proposition `finite-fiber-high-branching`.  The graph has vertex set
\(V(T_d)\times F\), vertical finite-fiber adjacency \(A_0\), and horizontal
coupling matrix \(P\) across every tree edge.  Its adjacency operator is
\[
  A_G=A_{T_d}\otimes P+I\otimes A_0.
\]
If \(b=d-1\), \(P(i_0,i_0)=1\), and
\[
  2\sqrt b\,\|P\|_{2\to2}+\|A_0\|_{2\to2}<b,
\]
then \(G\) contains a copy of \(T_d\), giving \(p_c(G)\le1/b\), while every
self-avoiding path is dominated by a walk and hence
\[
  \gamma_{\mathrm{SAW},2}(G)\le\|A_G\|_{2\to2}<b\le1/p_c(G).
\]
The SAW operator criterion gives \(p_c(G)<p_{2\to2}(G)\).

## Concrete cyclic examples

For \(T_d\square K_2\), the finite factor has adjacency norm \(1\), so
\[
  2\sqrt{d-1}+1<d-1
\]
holds for \(d\ge7\).  Thus \(p_c(T_d\square K_2)<p_{2\to2}(T_d\square K_2)\)
for \(d\ge7\).

For \(T_d\square C_m\), \(m\ge3\), the finite factor has adjacency norm \(2\),
so
\[
  2\sqrt{d-1}+2<d-1
\]
holds for \(d\ge9\).  Thus \(p_c(T_d\square C_m)<p_{2\to2}(T_d\square C_m)\)
for \(d\ge9\).

## Role

This is intentionally a high-branching result, but unlike the finite-type tree
calibrations it includes genuine short cycles in the fibers and allows
non-product horizontal finite-fiber couplings through \(P\).
