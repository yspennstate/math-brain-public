# Independent recheck of the round 5 testing lemma

Let \(W_1,\ldots,W_K\) be distinct length-\(n\) binary words, and let \(P_i\) be the law of \(m\) independent complete deletion traces of \(W_i\). The observation space \(Z\) is finite: each trace has length at most \(n\). Suppose \(R\) is one probability law on \(Z\).

A randomized decoder assigns conditional output probabilities \(a_i(z)\) to the words \(W_i\). Distinctness gives
\[
0\le a_i(z)\le1,\qquad \sum_{i=1}^K a_i(z)\le1.
\]
For \(h_i(z)=P_i(z)-R(z)\), the sum over \(z\) is zero. Consequently
\[
\sum_{h_i(z)>0}h_i(z)
=\tfrac12\sum_z|h_i(z)|
=\operatorname{TV}(P_i,R).
\]
Since \(a_i\) lies between zero and one,
\[
\sum_zP_i(z)a_i(z)
\le\sum_zR(z)a_i(z)+\operatorname{TV}(P_i,R).
\]
Summing over \(i\), dividing by \(K\), and using the decoder inequality proves
\[
\frac1K\sum_{i=1}^K\Pr_{P_i}(\widehat W=W_i)
\le\frac1K+\frac1K\sum_{i=1}^K\operatorname{TV}(P_i,R).
\tag{1}
\]
In particular, if each distance is at most \(\varepsilon\), every-word success at least \(s\) requires \(s\le K^{-1}+\varepsilon\).

There is a second direct derivation. Pointwise, the decoder's correct-probability sum is at most \(\max_i P_i(z)\). Also
\[
\max_iP_i(z)
\le R(z)+\sum_i(P_i(z)-R(z))_+.
\]
Summing this inequality over \(z\) and dividing by \(K\) gives (1) again, without using the preceding expectation argument.

For \(K=2^g\), the round 5 bound follows. Given fixed \(s>0\), take a fixed integer \(g\) with \(2^{-g}<s\). The supplied estimate
\[
\varepsilon=\sqrt{mgN^{-d}}+2mgE
\]
would contradict every-word success at least \(s\) whenever \(\varepsilon<s-2^{-g}\). Specifically, for \(0<\eta<s-2^{-g}\), the inequalities
\[
m\le\frac{\eta^2N^d}{4g},\qquad 2mgE\le\eta/2
\]
give \(mgN^{-d}\le\eta^2/4\), hence the square-root term is at most \(\eta/2\) and \(\varepsilon\le\eta\). Here \(N>0\), \(g\ge1\), \(m\ge0\), and \(E\ge0\) are required.

If all \(P_i=R\), (1) gives the attained guessing rate \(1/K\). If the word map repeats words, the bound on \(\sum_i a_i\) can fail, so injectivity is essential. If \(g=0\), the bound is merely \(s\le1+\varepsilon\) and supplies no contradiction. These cases agree with the lemma.

This verifies round 5's inference. The existence of the hard family and its quantitative distance estimate are not proved here.
