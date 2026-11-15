# T186 C025 v1: PASS for the stated auxiliary obstruction

Exact subject: w674/T186/proofs/C025_CLR_rare_history_obstruction.md,
SHA256 2b3061eb5f742ccf2e91b88ff8d4479b00ae7d3bbc9d66636db3f07ab6c42280.
Primary PDF arXiv:2111.15577v2 SHA256
1026da884918ee34329d0d169b472de11089d4077b18647b727576d691ef68b0.
Reviewer: codex-term-362ebe34, independent analytic check, 15 October 2026.

I read the counterexample and checked the primary source's actual Definition
3.4, the parameter paragraph on page24, and the rendered Claim7.5 on page26.
Definition3.4 gives independently sampled Poisson half-edges with independent
input histories before matching/deletion. Consequently, in the one-type
Poisson(2) example, a history of probability q has exactly Poisson(2nq)
total pre-matching inputs. Deletion cannot increase that count.

For OR messages initialized at1, p0=1 and F(p)=1-exp(-2p).
The exponential series gives exp(3/2)>67/16. Thus F(3/4)>51/67>3/4,
F(1)<1, and F'(p)<=32/67<1/2 on [3/4,1]. The positive fixed point
is unique in that interval, stable, and the top orbit decreases strictly
to it. Its gap after r steps is less than (1/4)2^(-r). A finite tree
chain of the required height has positive probability, so every last-flip
history used in C025 has positive probability. Monotonicity gives its
probability exactly q=p_(t0-1)-p_t0.

With delta0=2^(-100m), t0=100m-1, m>=1, the source's convergence condition
holds because p_(t0-1)-p* < 2^(-100m)=delta0. Meanwhile 0<q<delta0.
For a=delta0^(1/100)=2^(-m), the Poisson count has mean lambda*n,
lambda=2q<2^(1-100m)<a/2. Chebyshev therefore bounds the probability
of at least a*n inputs by 4lambda/(a^2 n)<2^(3-98m)/n, tending to0.
This contradicts the proposed lower bound with high probability.

The issue cannot be removed merely by choosing a different finite t0
after this small delta0: any t0 satisfying the displayed convergence
condition has 0<q<delta0, whereas 2delta0<delta0^(1/100). Hence the
same vanishing-probability upper estimate holds, with its corresponding
fixed q. This addresses the parameter-choice quantifier, not just a
single inconvenient horizon. Fixing a horizon first and then a different
history-dependent threshold is a different statement.

Disposition: PASS for an obstruction to Claim7.5's printed uniform
history-frequency threshold under the printed parameter ordering.
This is not a counterexample to Theorem1.3, a proof of any T186 finite
WP transfer, or a priority claim. The matching law, rare-history repair
and finite positive-core transfer still need their own proofs. C025 and
the author notes already identify this route failure; this audit adds
verification, not a new route or a replacement theorem.
