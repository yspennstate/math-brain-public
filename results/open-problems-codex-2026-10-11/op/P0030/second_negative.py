from pathlib import Path
with Path('ATTEMPT.md').open('a',encoding='utf8') as out:out.write('''

## Theorem J (proved stronger special case: only negative pieces need domination)

In Theorem H the summable Hellinger condition can be imposed only on k<0. All nonnegative-index pieces may follow arbitrary independent Brownian stopping rules allowed by Definition 2.2, subject to the assumed divergence of their total durations. More generally it suffices that the joint law of all negative stopped pieces is absolutely continuous with respect to the negative half of an i.i.d. finite-mean stopped-piece reference law P_0.

### Full proof

Work at the decomposition boundary S_0=0. The negative-time path is a measurable function solely of the stopped pairs indexed k<0. The nonnegative-time path is a measurable function solely of the stopped pairs indexed k>=0. Those two sigma fields are independent under Definition 2.2. The latter path has standard Brownian law, independently of the choice of nonnegative stopping rules. Here is the Brownian-law verification behind this fact: replacing a Brownian post-stopping-time continuation by an independent standard Brownian continuation preserves its law by the strong Markov property for the given normal filtration. Apply this successively for any finite number of independent stopped pieces, appending a Brownian continuation after the last piece. The resulting entire one-sided path has Brownian law and agrees with the desired concatenation until the corresponding joining time. As the number of pieces tends to infinity those joining times tend to infinity a.s.; on every compact time interval the constructed path therefore eventually agrees with the actual concatenation. Finite-dimensional distributions (or bounded continuous compact-window functionals) give the Brownian law of the limit. This is also the assertion immediately after Definition 2.2 in the source.

Let Q^- be the actual product law of negative pieces and P^- the negative product of P_0. By hypothesis Q^-<<P^-; under the summable negative-index Hellinger condition this follows from Lemma G with enumeration -1,-2,... . Let W_+ be one-sided Wiener law. Then

    Q^- times W_+ << P^- times W_+.

To check this domination, if a joint measurable set has zero P^- times W_+ mass, its W_+-section measure is zero P^--a.e. by Fubini, hence zero Q^--a.e.; another Fubini application gives zero actual mass. Map each pair of a negative piece sequence and a Brownian future to the full centered path by concatenating the negative pieces backwards from zero and using that future on t>=0. This map is measurable by the same evaluation argument in Theorem H. Its reference image has exactly the unmarked path law of the fully i.i.d. P_0 concatenation: the latter has this reference past and an independent standard Brownian future. Its actual image has the law of the given decomposable process. Thus the actual unmarked path law is absolutely continuous with respect to the reference unmarked path law.

The reference law admits a finite shift to W by source Theorem 5.1. The absolute-continuity stability result in Corollary F now gives a finite shift to W for the actual law, on an extension. QED.

This is stronger than Theorem H: summability or identical distribution of the positive pieces is irrelevant to the unmarked path law. The argument still adds a genuine condition on the infinite negative sequence. BBM alone has not been shown to imply that condition.

## Second-attempt hostile referee ledger

1. **Transport direction:** Lemma E starts with Q=fP and targets P. Its probability weights pull accepted destination mass back by theta^n, then divide by f; reversing that direction without changing weights would be wrong. Both the source-row sums and destination-column sums were checked exactly in finite models.
2. **Why mass is exhausted:** residual source and target have equal integrals, and the source can only decrease along its orbit. If residual target has positive mass, ergodicity forces every surviving source orbit to encounter it infinitely often, contradicting finite original source density. The residual identity is essential; recurrence alone without mass conservation is insufficient.
3. **Where auxiliary randomness enters:** the measurable kernel p_n(x) is sampled with an independent uniform. No deterministic-path integer shift is claimed. Arbitrary f cannot in general be implemented by a deterministic integer selection; this is a stated scope restriction of E/F/H/J, not hidden in the proof.
4. **Full product law versus local laws:** Lemma G obtains an L^1 probability density with total mass one. Mere finite-dimensional domination without Hellinger summability would not suffice. The first attempt's local total-variation limit is not substituted for this density.
5. **Correct comparison space:** the affinities compare (T,entire stopped Brownian path), not durations alone. Example I computes that density explicitly, including both the stop and continue decisions.
6. **Reference random shift:** it is sampled by disintegration on the entire piece sequence. Domination passes to that joint law and then to shifted paths. It is not assumed independent of the stopped pieces or unchanged in law after a tilt. Corollary F corrects precisely that remaining tilt.
7. **Actual stopping rule:** Example I retains an unconditioned Brownian motion and changes only the decision at time 1 using an independent uniform and B(1). Its T is a genuine stopping time in a normal filtration. Tilting an arbitrary stopped pair and assuming the tilted B is Brownian would not be justified; the example avoids that error by construction.
8. **Unmarked versus marked singularity:** the alternating deterministic-duration example disproves the attempted deduction that BBM forces a finite Hellinger sum for the supplied decomposition. Singularity of clocks does not by itself obstruct unmarked 2BM.
9. **No full-source inference:** the full problems allow arbitrary independent stopped pieces, potentially no common dominating reference, and arbitrary independent cut laws. Neither negative product domination nor equality on all invariant events has been derived from these hypotheses.

Updated precise remaining gap: for an arbitrary decomposable FBM which is BBM, show that its unmarked law agrees with Wiener law on shift-invariant events (possibly after a preliminary shift), or find a shift-invariant null event distinguishing it. Product domination provides one sufficient route, but fails for some harmless markings and is not a necessary condition on the given decomposition. For 7.2/7.3, independence of the two selected halves has not been shown to determine those full-path invariant-event probabilities. All full questions remain unresolved here.
''')
print('saved stronger negative-half theorem and referee ledger')
