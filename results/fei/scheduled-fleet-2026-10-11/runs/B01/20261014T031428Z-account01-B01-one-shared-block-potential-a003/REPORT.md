# B01 / A003 — coefficient-one block potential for one shared coordinate

Status: **AUTHOR-PROVED, PENDING INDEPENDENT A086/A094 REVIEW**. Full FEI remains **OPEN**.

## Result

The disjoint singleton-potential theorem now has a dimension-independent
replacement for exactly one reused physical coordinate.

Put

\[
q(y)=y\log_2(1/y)+\frac{2y}{\ln2},
\]

and for Boolean `f(x,u)` define

\[
\Lambda_x(f)=q(\widehat f(\emptyset)^2+\widehat f(\{x\})^2)
+\sum_{i\in u}q(\widehat f(\{i\})^2+
                      \widehat f(\{i,x\})^2).
\]

If `f(x,u)` and `g(x,v)` share only `x`, then

\[
\boxed{\Phi(fg)\le\Lambda_x(f)+\Lambda_x(g).}
\]

The sharper right side uses the two private block sums plus the minimum of
the two mean/shared blocks. The coefficient is one and is independent of
dimension, bias, rank, rarity, and both arbitrary Boolean cores.

The same potential pays actual physical revelation:

\[
\boxed{\frac12\Phi(f\mid x=1)+\frac12\Phi(f\mid x=-1)
\le\Lambda_x(f).}
\]

## Mechanism

For every private `i`, multiplication through `x` acts on
`(fhat(i),fhat(i,x))` by

\[
\begin{pmatrix}m_g&d_g\\d_g&m_g\end{pmatrix}.
\]

Its eigenvalues are `E[g|x=+1]` and `E[g|x=-1]`, so its operator norm is at
most one. Physical restriction is paid by Jensen because `q` is increasing
and concave. These are exact analytic statements, not finite-search evidence.

## Advancement and boundary

The reviewed B05 majority/rare-gate counterfamily defeats every scalar
shared-pivotal payment but is absorbed by `Lambda_x(xK_n)=Phi(K_n)`: the
missing degree-two slice is now retained explicitly. This is the first
positive overlap bridge beyond the disjoint closure theorem.

It does not settle the universal gap. `Lambda_x` has no proved universal
`I/U` payment, and a hierarchy may try to charge the same block at several
reused coordinates. The precise next lemma is a first-revelation ownership
and signed telescope for these blocks across two nested overlaps, then
arbitrary depth.

## Verification

Independent-from-proof truth-table computation passed 4,096 exhaustive
shared products, 10,000 larger random products, 20,256 physical restrictions,
and 160,801 scalar Jensen checks. Maximum observed slack was zero within
display precision.

## Literature scope

O'Donnell--Tan composition assumes disjoint inner blocks; it does not contain
this shared-coordinate block potential. No novelty or priority claim is made.
