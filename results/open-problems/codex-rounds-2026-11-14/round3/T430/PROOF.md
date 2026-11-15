# Tagged arrival rates need not increase with the number of servers

Fix an arrival parameter 0<λ<1 and an integer d≥2. Sampling in this note is uniform without replacement, with uniform tie breaking. This is the convention in the combinatorial arrival-rate formula audited below.

For a deterministic queue-length vector x=(x_1,...,x_N), let a_N(x) be the instantaneous rate of arrivals routed to server 1. Queue lengths determine routing at a given instant. They are not being used as Markov states for general service times.

## 1. Appending a shorter queue

**Proposition 1.** Let N≥d, and append a queue with length y<x_1. Then

\[
 a_{N+1}(x_1,\ldots,x_N,y)
 =\frac{N+1-d}{N}\,a_N(x_1,\ldots,x_N).
 \tag{1}
\]

Consequently, if a_N(x)>0, then

\[
 a_{N+1}-a_N=-\frac{d-1}{N}a_N<0.
 \tag{2}
\]

**Proof.** For each d-element subset S of {1,...,N}, let w_x(S) be the probability that the routing decision chooses server 1, conditional on sampling S and the state x. Explicitly, w_x(S)=0 if 1 is absent from S or if some sampled queue is shorter than x_1. Otherwise it is the reciprocal of the number of queues in S with length x_1. Thus

\[
 a_N(x)=\frac{\lambda N}{\binom Nd}
               \sum_{|S|=d}w_x(S).
 \tag{3}
\]

In the enlarged system, a sample containing server N+1 cannot route to server 1, because y<x_1. For every sample excluding server N+1, the routing weight is still w_x(S). Therefore

\[
 a_{N+1}(x,y)=\frac{\lambda(N+1)}{\binom{N+1}d}
                    \sum_{|S|=d}w_x(S).
 \tag{4}
\]

The ratio of the two prefactors is

\[
 \frac{N+1}{N}\frac{\binom Nd}{\binom{N+1}d}
 =\frac{N+1-d}{N}.
\]

Equations (3) and (4) prove (1), including when the sum is zero. Subtracting a_N gives (2). ∎

There is a separate derivation of the factor in (1). In the enlarged system, the probability that an arrival excludes server N+1 is (N+1-d)/(N+1). Poisson thinning gives rate λ(N+1-d) for these arrivals, and their sampled set is uniform among the d-subsets of the first N servers. Arrivals containing the new shorter queue never route to the tag. The original arrival stream has rate λN and the same conditional routing distribution on those subsets. The rate ratio is therefore again (N+1-d)/N.

## 2. One fixed configuration with infinitely many decreases

Use the infinite configuration

\[
 x_{3j+1}=1,\qquad x_{3j+2}=2,\qquad x_{3j+3}=0,
 \qquad j\geq0.
 \tag{5}
\]

Write a_N for the tagged rate of its first N coordinates. The tagged queue has length one.

**Proposition 2.** For every m≥d-1, put N=3m+2. Then a_N>0 and

\[
 a_{3m+3}=\frac{3m+3-d}{3m+2}\,a_{3m+2}<a_{3m+2}.
 \tag{6}
\]

In particular, this rate sequence is not eventually nondecreasing. The empirical queue-length measures of these same prefixes converge to

\[
 \frac13\delta_0+\frac13\delta_1+\frac13\delta_2.
 \tag{7}
\]

**Proof.** The first 3m+2 coordinates contain m+1 queues of length one, m+1 of length two, and m of length zero. Thus the number exactly at the tagged length is m+1≥d, the number strictly above that length is also at least d, and the number at least that length is 2m+2≥d. In particular all count restrictions needed below hold.

There are at least d-1 queues of length two. A sample consisting of server 1 and d-1 such queues routes to server 1 with probability one. It has positive sampling probability, so a_N>0. The next coordinate x_{3m+3} is zero. Apply Proposition 1 to obtain (6). Such m are arbitrarily large, ruling out every eventual nondecrease threshold. Finally the three counts in prefixes differ by at most one, proving (7). ∎

This example is admissible for FIFO service with G=δ_1: assign a job with positive residual requirement to every nonempty queue and a further waiting job to each length-two queue. The instantaneous routing calculation uses no departure mechanism. It is not a stationary construction.

## 3. A direct two-choice calculation

For d=2, let e be the number of queues equal to the tagged length, including the tagged queue, and h the number strictly longer. An unordered pair is sampled uniformly. The tag wins against each of the h longer queues, wins with probability 1/2 against each of the e-1 equal queues, and loses against every shorter queue. Hence

\[
 a_N=\frac{\lambda N}{\binom N2}
                  \left(h+\frac{e-1}{2}\right)
     =\lambda\frac{2h+e-1}{N-1}.
 \tag{8}
\]

An independent derivation conditions on inclusion of the tag, which has probability 2/N. The other server is uniform among N-1 servers, and the probability of routing to the tag is [h+(e-1)/2]/(N-1). Multiplication by λN gives (8) again.

For (5), at N=3m+2 one has e=h=m+1. Appending the next zero does not change these counts. Thus, for m≥1,

\[
 a_{3m+2}=\lambda\frac{3m+2}{3m+1},\qquad
 a_{3m+3}=\lambda,\qquad
 a_{3m+2}-a_{3m+3}=\frac{\lambda}{3m+1}>0.
 \tag{9}
\]

For example the first pair satisfying e,h≥2 is N=5,6:

\[
 a_5=\frac54\lambda,\qquad a_6=\lambda.
 \tag{10}
\]

At N=5 the favorable-pair weights total 2+1/2=5/2, so the rate is (5λ/10)(5/2)=5λ/4. At N=6 the same total weight gives (6λ/15)(5/2)=λ. This checks both finite values without using the ratio formula.

## 4. The rates in this example nevertheless converge

The distinction between convergence and monotonicity can be checked explicitly. For arbitrary d and e>0, the probability that an arrival is routed to some queue at the tagged length is

\[
 \frac{\binom{e+h}d-\binom hd}{\binom Nd}.
\]

The numerator counts samples with no shorter queue and at least one queue at the tagged length. Uniform tie breaking and symmetry among the e queues at this length give

\[
 a_N=\frac{\lambda N}{e}
              \frac{\binom{e+h}d-\binom hd}{\binom Nd}.
 \tag{11}
\]

In configuration (5), e/N→1/3 and h/N→1/3. For fixed d, expansion into d falling factors shows that if z_N/N→z, then

\[
 \frac{\binom{z_N}d}{\binom Nd}
 =\prod_{r=0}^{d-1}\frac{z_N-r}{N-r}\longrightarrow z^d.
\]

Apply this to (11) to obtain

\[
 a_N\longrightarrow
 3\lambda\left[\left(\frac23\right)^d-
                  \left(\frac13\right)^d\right].
 \tag{12}
\]

For d=2 this is λ, consistent with (9). The example disproves eventual monotonicity, while its rate limit exists.

## 5. Relation to the cited stationary argument

Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, [arXiv:1809.05373](https://arxiv.org/pdf/1809.05373), use a tagged routing-rate function in (3.1). Their Lemma 3.3, printed page 11, asserts eventual nondecrease in N uniformly over x and the tagged length. The paragraph after (3.1) imposes lower bounds on the relevant counts. Configuration (5) satisfies those bounds for all sufficiently large prefixes, including the infinitely many decreasing pairs (6). Thus the monotonicity assertion fails on its stated domain. The proof in Appendix A.2 treats appended queues above and equal to the tagged length; the shorter case has the opposite sign by (2). Theorem 3.2 and the proof of Theorem 3.4 invoke this lemma. Section 4 then invokes earlier results for stationary initial laws.

This refutes that supporting lemma, not the conclusion of Proposition 4.1 or the original stationary product-limit assertion. Correct convergence estimates may exist without monotonicity, as (12) illustrates. A proof of stationary independence must also address the conditional-mean concentration term identified in the earlier work. Neither that concentration nor full-state stationary independence is proved here.
