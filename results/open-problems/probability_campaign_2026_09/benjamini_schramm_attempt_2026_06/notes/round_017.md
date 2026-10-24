# Round 017 log

Date: 2026-06-08

## Focus

Pushed the line-factor theorem from \(d\ge5\) to \(d\ge4\) using a two-step
vertical-cluster comparison.

## Two-step comparison

The one-step vertical-cluster comparison was just short for \(d=4\).  At
\[
  p=\frac{1}{\sqrt3+1+\sqrt{2\sqrt3-1}},
\]
the one-step mean is about \(0.9903\).  A two-step comparison fixes a
parent-child-grandchild path in the oriented tree and allows the intermediate
child fiber to use all vertical components touched by source edges from the
parent vertical cluster.

Let \(b=1-p\) and
\[
  c=\frac{1-p}{1-p+p^2}.
\]
If a child-fiber component has length \(\ell\) inside the parent interval and
touches \(k\in\{0,1,2\}\) interval boundaries, the expected probability that
it fails to have both a source mark and a target mark is
\[
  f_k(\ell)=b^\ell+c^kb^\ell-c^kb^{2\ell}.
\]
Thus
\[
  A_k(z)=\sum_{\ell\ge1}p^{\ell-1}f_k(\ell)z^\ell
  =
  \frac{(1+c^k)bz}{1-pbz}
  -
  \frac{c^kb^2z}{1-pb^2z}.
\]
The failure generating function for a parent interval is
\[
  H(z)=A_2(z)+\frac{bA_1(z)^2}{1-bA_0(z)}.
\]
Averaging over the parent vertical cluster size distribution gives the
fixed-grandchild success probability
\[
  \Phi(p)=1-b^2H'(p).
\]

## The \(d=4\) certificate

For \(d=4\), \(q=d-1=3\).  Exact rational arithmetic at
\[
  p_0=23/100
\]
gives
\[
  9\Phi(p_0)-1>\frac1{100}.
\]
Hence the two-generation Galton-Watson comparison is supercritical and
\[
  p_c(T_4\square\mathbb Z)<23/100.
\]

The nonbacktracking exponent for \(T_4\square\mathbb Z\) is bounded by
\[
  \beta_4=\sqrt3+1+\sqrt{2\sqrt3-1}.
\]
The elementary estimates
\[
  \sqrt3<26/15,\qquad \sqrt{2\sqrt3-1}<11/7
\]
give
\[
  \beta_4<452/105<100/23.
\]
Therefore \(p_c(T_4\square\mathbb Z)<1/\beta_4\), and the SAW operator gap
criterion proves
\[
  p_c(T_4\square\mathbb Z)<p_{2\to2}(T_4\square\mathbb Z).
\]

## Status

The manuscript now proves the line-factor result for every \(d\ge4\):
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z).
\]
The case \(T_3\square\mathbb Z\) remains outside the current
nonbacktracking-plus-vertical-branching method; the two-step mean at the
nonbacktracking comparison point is still below one.
