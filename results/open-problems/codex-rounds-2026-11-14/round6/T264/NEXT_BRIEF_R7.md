# T264 round 7 brief (an agent, 15 Nov 2026; corrected the same day)

Already proved (round 5, REPORT copied in round 6's PROMPT.md): for n iid uniform inputs on S^(d-1), Rademacher labels
and zero regression function, every measurable minimum-norm selection has E[R_n^r] = infinity for every n >= 3 and
r >= (d-1)/2, so E[R_n] = infinity in d = 2 and d = 3. The event used has probability 2^(3-n), so this is not
divergence in probability. Round 6 showed antipodal extra points cancel the blow-up, so the hemisphere geometry matters.
An earlier draft of this brief asked for that iid statement; it is not needed.

Pick ONE and say which in LOG.md first.

A. Lower bound with high probability (not benign). Karhadkar, Sietsema, Needell, Montufar (arXiv:2602.00825) prove
   near-minimal W^{k,p} interpolants of noisy labels keep excess risk >= c > 0 w.h.p. Two-layer ReLU min-norm
   interpolation in d >= 2 minimizes the R-norm of Ongie, Willett, Soudry, Srebro (arXiv:1910.01635). Find the
   inequality that replaces their Sobolev inequality for the R-norm and prove liminf R_n >= c > 0 w.h.p. A proof in
   d = 2 alone is a result. (Upper bounds, i.e. tempered rather than catastrophic in probability, are the other half.)

B. Mean risk for d >= 4. Round 5 leaves E[R_n] open for d >= 4 (its tail exponent (d-1)/2 exceeds 1). Decide it:
   either a second mechanism with a heavier tail, or a proof that E[R_n] < infinity.

Same compute rules as round 6: one thread, nice 15, under 1 GB, 20 minutes a run, no GPU.
