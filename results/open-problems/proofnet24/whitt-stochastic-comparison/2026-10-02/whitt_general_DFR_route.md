# A route beyond finite hyperexponential laws: established algebra and remaining gap

2 October 2026. This note is an exploratory extension. The complete all-server theorem in `whitt_all_servers_light_traffic_proof.md` applies to finite hyperexponential laws. No general-service theorem is claimed here.

Let s(t)=P(S>t), L(t)=integral_t^infinity s(v)dv, m=L(0), and c>=2. For a finite hyperexponential law, its already-proved next delay coefficient can alternatively be written

    K_c=1/(c-1)! integral_0^infinity integral_0^infinity
          s(u)s(t)L(u+t)^(c-1)du dt.                (1)

To verify (1) without queueing assumptions, expand s(u), s(t), and the c-1 factors L(u+t) into their finite exponential mixtures. Each pair of elementary integrals gives the denominator

    [(1/a)+(sum_j 1/b_j)] [(1/a')+(sum_j 1/b_j)].

Changing all c+1 class laws to their size-biased versions gives

    m^(c+1)/(c-1)! E[X_1 X_2/
                     ((sum_j X_j-X_1)(sum_j X_j-X_2))].

Exchangeability turns this into the K_c formula in the completed proof. Thus (1) is established for that class.

For a more general strictly positive distribution, assume that its equilibrium residual survival L(t)/m is NWU, meaning

    L(u+t)>=L(u)L(t)/m.

Then the right side of (1), whether or not it is yet known to be the queue coefficient, satisfies

    K_c >=1/[(c-1)!m^(c-1)]
              [integral_0^infinity s(t)L(t)^(c-1)dt]^2
          =m^(c+1)/(c!c).                         (2)

The integral identity follows from L'=-s and integral s L^(c-1)=m^c/c. The inequality is strict if the NWU inequality is strict on a set of positive area on which s(u)s(t)>0.

A nonexponential strictly positive DFR law has the required residual NWU property. One direct way to see it is that its residual hazard s/L is decreasing: if the original decreasing hazard is h=-s'/s, then L/s>=1/h and

    (s/L)'=(s/L)(s/L-h)<=0.

Its residual survival is therefore log-convex and supermultiplicative after normalization. A continuous residual survival that is multiplicative at all u,t is exponential; for a strictly positive original law this forces the original law itself to be exponential. This establishes strictness unless the law is exponential, under the usual regularity allowing these hazard derivatives (or their almost-everywhere counterparts).

Suppose also that the original hazard is bounded below by 1/B. Then s(t+v)<=s(t)e^(-v/B), hence L(t)<=B s(t), and therefore

    L'(t)=-s(t)<=-L(t)/B,
    L(t)<=m e^(-t/B).

This stop-loss comparison proves that the original law is convex-order dominated by U=0 with probability1-m/B, BE with probabilitym/B. Both laws have mean m. Consequently, if the stationary delay expansion

    P(W>0)=m^c lambda^c/c!
       +[K_c-m^(c+1)/c!]lambda^(c+1)+o(lambda^(c+1))  (3)

were established for this general DFR class, (2) and the M/M/c endpoint coefficient would immediately give the same reversed delay inequality for all sufficiently small lambda.

## Remaining mathematical work

The missing step is a rigorous proof of (3) with coefficient (1) for general service laws. The finite-dimensional QBD proof used for hyperexponentials does not apply directly. General light-traffic derivative theorems may provide the interchange and finite-arrival expansion, but their detailed hypotheses must be read and checked; an abstract is insufficient. Alternatively one could give a regenerative expansion under an exponential service-tail bound and derive the first congestion correction directly. No such complete proof is included in this note.

Primary literature that may supply the missing tool:

* Reiman and Simon (1989), “Open Queueing Systems in Light Traffic”, Mathematics of Operations Research14(1),26–59, doi10.1287/moor.14.1.26; https://pubsonline.informs.org/doi/10.1287/moor.14.1.26 . Its abstract states that derivatives are justified by an interchange of limits and involve sample paths with finitely many arrivals. The full admissibility conditions were not available in the accessible abstract.
* Zazanis (1992), “Analyticity of Poisson-driven stochastic systems”, Advances in Applied Probability24(3),532–541, doi10.2307/1427478; https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/analyticity-of-poissondriven-stochastic-systems/D1C82D36C4381104B7BA2C37F1C95289 . Its abstract gives analyticity under moment conditions; those conditions have not been checked here.
* Wang (1997), “Light traffic approximations for regenerative queueing processes”, Advances in Applied Probability29(4),1060–1080, doi10.2307/1427854; https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/light-traffic-approximations-for-regenerative-queueing-processes/63E8EB9550362A276873DC16489BBB5C . Again only the abstract and references were accessible.
* Wang and Wolff (1998), “The M/G/c queue in light traffic”, Queueing Systems29,17–34. Its abstract concerns first-moment approximations, so it does not by itself establish the desired delay-probability coefficient or disprove the target conjecture.
