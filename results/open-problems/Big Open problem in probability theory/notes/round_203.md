# Round 203

Round 203 decomposes the spherical self-avoiding envelope by excess path
length.

For \(n,k\ge0\), define
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  =
  \sup_x
  \frac1{|S_n(x)|}
  \sum_{a\in S_n(x)}
  \#\{\gamma:x\to a\ {\rm SAW}:|\gamma|=n+k\}.
\]
The root supremum does not commute with the sum over \(k\), so the valid
statement is the upper bound
\[
  \mathfrak S_p^{\rm saw,sph}(n)
  \le
  \sum_{k\ge0}p^k\mathfrak N_{n,k}^{\rm saw,sph}.
\]
Consequently, if \(q>p_c\) and the \(q\)-weighted excess-length profile
\[
  \sup_{c_sL<n\le(1/\alpha_\omega+3s)L}
  \sum_{k\ge0}q^k\mathfrak N_{n,k}^{\rm saw,sph}
\]
has the same strict exponent bound as the Round 202 envelope, then the
two-replica obstruction closes.  This isolates the current residual target as
a deterministic weighted count of excess-length self-avoiding paths between
half-logarithmic and full-logarithmic spheres.
