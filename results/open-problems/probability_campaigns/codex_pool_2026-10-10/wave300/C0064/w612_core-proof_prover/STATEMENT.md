# C0064 statement for independent challenge

Fix an integer d > 6. Independently open every unoriented nearest-neighbour edge of Z^d with probability p. Write tau_p(x) = P_p(0 is connected to x), p_c(d) = inf{p : P_p(|C(0)| = infinity) > 0}, and D(x) = 1{|x|_1 = 1}/(2d). For p < p_c, tau_p is summable and hat(tau_p)(k) = sum_x tau_p(x) exp(i k.x), k in [-pi,pi]^d; hat(D)(k) = (1/d) sum_j cos(k_j).

Target: for every integer d > 6, find a finite A_d, independent of p, such that

    0 <= hat(tau_p)(k) <= A_d / (1 - hat(D)(k))

for all 0 <= p < p_c(d) and k != 0 modulo 2pi. At criticality interpret the assertion as a bound on the Fourier density obtained in the p-up-to-p_c weak limit, not as an absolutely convergent Fourier series. A critical-only formulation is the dated C0064 intake target; a uniform subcritical estimate is a sufficient route to it. No quantitative claim about A_d is made.

Primary reference establishing the corresponding d >= 11 theorem: Fitzner and van der Hofstad, Mean-field behavior for nearest-neighbor percolation in d > 10, Electronic Journal of Probability 22 (2017), DOI 10.1214/17-EJP56; author extended version https://rhofstad.win.tue.nl/PercPaper_ext.pdf, Theorem 1.1, equations (1.11)-(1.12). Primary open-problem locator recorded by intake: Heydenreich and van der Hofstad, Progress in high-dimensional percolation and random graphs, author version, Open Problem 10.1 (the intake calls this p.145; printed/PDF pagination still needs direct confirmation).

Current openness: UNKNOWN. Targeted public searches on 2026-10-10 recovered the published d >= 11 result but did not certify the absence of a later solution. The owner-attempt and same-target peer checks are in progress. This statement makes no novelty or solved claim.

Independent adversary: w613. Please challenge this statement and the critical Fourier interpretation before reading my proof route. Referee: w614. I will save the proof route separately after this statement is sent.
