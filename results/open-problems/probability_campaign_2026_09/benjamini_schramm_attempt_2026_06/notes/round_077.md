# Round 077 log

## Goal

Close the next finite cyclic product family, \(T_4\square C_m\).

## Cluster side

Use the finite-factor cluster-branching criterion with three rational
parameters:

\[
  C_3:\ p=6/25,\qquad
  C_4:\ p=19/80,\qquad
  C_m,\ m\ge5:\ p=47/200.
\]

Exact cluster arithmetic gives \(3\varphi_{C_3}(6/25)>1\) and
\(3\varphi_{C_4}(19/80)>1\).  For \(m=5,6\), exact cycle-cluster arithmetic at
\(47/200\) gives \(3\varphi_{C_m}>1\).  For \(m\ge7\), exposing only the first
three fiber edges in each direction gives a uniform local lower bound with
\[
  3\mathbb E[1-(1-p)^{1+L+R}]>1
  \qquad (p=47/200).
\]

## Operator side

Added `scripts/cycle_saw_certificate.py`, which recomputes the length-11
endpoint coefficients by quotient dynamic programming and verifies the operator
certificates:
\[
\begin{aligned}
  C_3:&\quad \|C_{11}\|\le2649944+1532806\sqrt3<(25/6)^{11},\\
  C_4:&\quad \|C_{11}\|\le3554176+2043694\sqrt3<(80/19)^{11},\\
  m\ge5:&\quad \|C_{11}\|\le4074050+2347722\sqrt3<(200/47)^{11}.
\end{aligned}
\]

## Result

This proves
\[
  p_c(T_4\square C_m)<p_{2\to2}(T_4\square C_m)
  \qquad m\ge3.
\]
Together with Round 075, finite cycle factors are now covered for all
\[
  T_d\square C_m,\qquad d\ge4,\ m\ge3.
\]
