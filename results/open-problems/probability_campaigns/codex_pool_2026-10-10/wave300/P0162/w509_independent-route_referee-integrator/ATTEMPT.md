# P0162 independent route

Initial plan, written before reading w507 or w508 proof artifacts: express Fourier entropy as the entropy of the spectral set under the distribution \(p(S)=\widehat f(S)^2\). Seek a decomposition by random restrictions or coordinate reveal that charges each conditional entropy increment to the chance that the coordinate is pivotal. The difficulty is controlling entropy from rare spectral configurations without silently multiplying conditional bounds. First verify the exact conjecture and the strongest known restricted cases; any proposed inequality must be checked against tribes and parity.

Source check: O'Donnell-Wright-Zhou state the exact Boolean FEI conjecture in their introduction. González-MacManus-Pereyra (arXiv:2606.00246) already develop the restriction induction and show a wrong split can defeat a stronger local inequality. The local intake also records that entropy versus mean spectral cardinality alone fails without Boolean realizability. W507 and w508 have restriction or selector routes, so this route is retired as duplicative before reading their detailed proofs.

The Boolean convolution route was also retired: a read-only query of `math-brain-build/local/population/brain.sqlite3` found an existing P0162 attempt card that already uses the nonzero `x_i x_j` coefficient of `f²` to rule out uniform singleton spectral mass. Repeating that computation would add nothing.

I considered a different information-theoretic route: let `S` have law `hat(f)(S)²`, with marginals `P(i in S)=I_i(f)`. The exact identity `H(S)=sum_i h(I_i)-TC(S)`, where `TC` is the nonnegative total correlation, reduces FEI to a Boolean-specific lower bound `TC(S)>=sum_i h(I_i)-C I(f)`. This is an exact reformulation rather than progress: the missing coercive estimate on `TC` is as hard as FEI. I do not assert such an estimate. The route is recorded so a future agent can test it against known tribes/addressing examples, but it is not promoted to the math brain as a theorem.

No proof claim yet. Current openness: UNKNOWN.
