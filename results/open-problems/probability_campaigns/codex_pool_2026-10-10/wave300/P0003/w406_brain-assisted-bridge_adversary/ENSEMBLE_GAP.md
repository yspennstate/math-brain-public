# P0003's recorded ensemble and a finite counterexample

Grimmett, Selected problems in probability theory, arXiv:2205.07318, Question 2.2 (PDF p. 3), asks whether suitable rescaling of a uniform n-step self-avoiding walk rooted at the origin of the deterministic hexagonal lattice converges weakly to SLE(8/3). The question does not specify the scaling constant, path topology, time parameter, or precise finite-length SLE law. Those choices must be fixed in a theorem statement; they are not supplied by substituting a chordal ensemble with two prescribed boundary endpoints.

The full returned P0003 brain card and its logical identifier are in narrow_source_lookup.json. The returned prior finite-prefix attempt already warns that fixed-length conditioning is a different ensemble. My initial source recovery used the related Duminil-Copin--Smirnov chordal fugacity conjecture; it was a formulation change, not recovery of the complete original P0003 statement. The packet is corrected to retain both and mark the missing bridge.

## Exact elementary facts (submitted for independent check)

Let G be finite, a!=b, x>0, and c_G(n;a,b) the number of vertex-simple a-to-b paths of exactly n edges. Let Z_G(x)=sum_n c_G(n;a,b)x^n>0. Under the fugacity law P_x(gamma)=x^length(gamma)/Z_G(x), conditional on length=n with c_G(n;a,b)>0, every n-edge path has probability 1/c_G(n;a,b). For any event E,

    P_x(E)=sum_n [c_G(n;a,b)x^n/Z_G(x)] U_(G,n;a,b)(E).

Proof: all paths in a length class have the same weight x^n; the length-class probability is c_G(n;a,b)x^n/Z_G(x). Divide, then apply the law of total probability. This conditional uniform law still has *both endpoints prescribed*; the original P0003 rooted law has its endpoint free, which is an additional distinction.

On G=C6, take adjacent vertices a,b. Exactly two simple a-to-b paths exist, of lengths 1 and 5. The uniform length-1 law assigns probability 1 to the short edge. The positive-fugacity law assigns probabilities 1/(1+x^4) and x^4/(1+x^4). Their total variation distance is x^4/(1+x^4)>0. At the critical honeycomb fugacity x_c=(2+sqrt(2))^(-1/2) it is exactly 1/(7+4*sqrt(2)). This disproves equality of the two finite-graph ensembles, not any claimed equivalence of their scaling limits.

A convergent mixture law need not identify its conditional components. For each k let a length label N be 2k or 2k+2 with probabilities 1/2 each. Given N=2k let X be the parity of k, and given N=2k+2 let X be the opposite parity. The marginal law of X is the same Bernoulli(1/2) for every k, while the conditional law of X given N=2k alternates between point masses and has no limit. This abstract two-state example is only a counterexample to a general deconditioning inference; it is not a model of honeycomb SAW.

## Minimal missing premise in the paired route

w405's outer-buffer lemma correctly transfers fixed-buffer avoidance probabilities for a chordal critical-fugacity law. Even if its T/B/C assumptions were proved, its conclusion would be chordal fugacity convergence in bounded marked domains. To connect that result to the recorded uniform n-step rooted target, add a separately proved ensemble/endpoint-conditioning transfer theorem, with the rescaling, path topology and intended SLE variant specified. Neither a domain Markov law nor convergence of the unconditioned length mixture supplies that theorem.

NEXT: Specify the rooted fixed-length limiting law and prove a length- and endpoint-conditioning transfer estimate; until then keep chordal fugacity progress as a distinct conditional result.
