# Round 075 log

## Goal

Use finite-fiber cluster branching to push the finite cyclic product thresholds
below the embedded-tree \(p_c\) bound used in Round 074.

## Finite-factor cluster branching

The cluster-branching upper bound for \(p_c(T_d\square H)\) now allows finite
connected transitive factors \(H\).  The proof is unchanged: the tree factor
supplies disjoint future fibers, while transitivity gives the same cluster law
in every fiber.

## \(T_4\square K_2\)

For \(K_2\), the fiber cluster size is \(1+X\) with \(X\sim\mathrm{Bernoulli}(p)\), so
\[
  \varphi_{K_2}(p)=p+p^2-p^3.
\]
At \(p=3/10\),
\[
  3\varphi_{K_2}(p)=1089/1000>1,
\]
so \(p_c(T_4\square K_2)<3/10\).  The nonbacktracking operator bound gives
\[
  \beta(5,2\sqrt3+1)<10/3,
\]
therefore \(p_c(T_4\square K_2)<p_{2\to2}(T_4\square K_2)\).

Together with Round 074, this proves the \(K_2\) cyclic factor for all
\(d\ge4\).

## \(T_d\square C_m\)

For every cycle \(C_m\), \(m\ge3\), the two incident fiber edges at the root
give
\[
  \varphi_{C_m}(p)\ge1-(1-p)(1-p^2)^2.
\]
At \(p=1/5\), this lower bound is enough for \(d=5\), and the
nonbacktracking exponent satisfies \(\beta(7,6)=3+\sqrt3<5\).

At \(p=19/100\), the same lower bound is enough for \(d=6\), and
\[
  \beta(8,2\sqrt5+2)<100/19.
\]
Together with Round 074, this proves \(T_d\square C_m\) for every \(m\ge3\)
and every \(d\ge5\).
