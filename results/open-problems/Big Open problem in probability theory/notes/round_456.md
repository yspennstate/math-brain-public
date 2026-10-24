# Round 456 endpoint \(L^2\) extracts support-congestion sets

Round 456 records the inverse form of endpoint \(L^2\) congestion.

Let \(f\ge0\) be a skeleton endpoint weight on a finite sphere \(S\).  Decompose
into dyadic level sets
\[
  U_i=\{a\in S:2^i\le f(a)<2^{i+1}\}.
\]
If \(N_f\) is the number of nonempty levels, then
\[
  \|f\|_2^2
  =
  \sum_a f(a)^2
  \le
  4\sum_i 2^{2i}|U_i|.
\]
Hence some level set \(U=U_i\) satisfies
\[
  2^{2i}|U|
  \ge
  \frac{\|f\|_2^2}{4N_f}.
\]
Writing \(M_U=\sum_{a\in U}f(a)\), we also have
\[
  M_U\ge 2^i|U|,
\]
and therefore
\[
  \frac{M_U^2}{|U|}
  \ge
  \frac{\|f\|_2^2}{4N_f}.
\]

Thus a large endpoint \(L^2\) norm produces a boundary subset \(U\) carrying
large skeleton mass per square-root support:
\[
  M_U\gtrsim N_f^{-1/2}\|f\|_2\sqrt{|U|}.
\]
For skeleton weights of length \(O(L_H)\), \(N_f=O(L_H)\), so the loss is
subexponential in the radial-profile scale.

This converts endpoint two-replica congestion into a support-congestion
profile: many skeleton prefixes land in a comparatively small boundary set.
Such a set is a better interface for either a future counting-to-percolation
comparison or a deterministic support-volume estimate.
