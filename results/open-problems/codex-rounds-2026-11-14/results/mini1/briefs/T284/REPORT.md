VERDICT: PARTIAL inverse-polynomial success amplifies to high probability with any fixed density loss

For fixed rational d>0 and 0<b<a<=1, a polynomial-time algorithm that finds an independent set of size ceil(a n) in G(n,d/n) with eventual success at least c n^(-s) can be transformed into a polynomial-time algorithm that finds one of size ceil(b n) with failure O(n^(-L)), for any fixed L>0. The graph distribution and degree d are preserved. PROOF.md gives every reduction step and an explicit finite-n failure bound. The only non-elementary input is the biased-product reverse hypercontractive inequality in Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/pdf/1108.1210 . No novelty claim is made for this application.

At every fixed integer d, the supremum of independent-set densities achievable with eventual inverse-polynomial success equals the supremum achievable with high probability. In particular, any inverse-polynomial-success algorithm crossing the (log d)/d barrier by epsilon would give a high-probability algorithm crossing it by every smaller positive epsilon'. This removes the success-probability quantifier, with fixed slack; it does not remove the need to prove hardness or construct an algorithm.

Verification command:

    env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py

Result: PASS. Exact rational enumeration checked 4096 Bayes identities and 225 conditional repair distributions on four vertices. Additional checks covered 3060 Boolean negative-moment examples, 80 non-Boolean examples, and 12933 ceiling/mean cases. The repair exponent was re-derived with an optimized Chernoff bound, and log(2) was evaluated independently by an exact series. Full data are in verification.json; exact command output is in LOG.md; the adversarial audit is in AUDIT.md. The run took 0.2713 seconds and peaked at 15253504 bytes of resident memory. OMP_NUM_THREADS was 1. The inherited nice value was 20; attempts to request nice 15 were denied by the sandbox, leaving the lower inherited priority in place.

What failed: the initial verifier launch stopped at an unsupported macOS address-space-limit operation, before doing any checks. The verifier now records that limitation and uses fixed tiny inputs; its measured peak memory is about 15 MB. Repetition with fresh solver coins alone does not handle hard input instances. Conditioning the repair law on the first selected successful trial would need an unjustified argument; the proof uses a union bound over predetermined trials instead.

Unresolved: T284 itself is not settled. No all-algorithm obstruction, named average-case complexity reduction, or barrier-crossing algorithm is supplied. No amplification at exactly the original density, no growing-d runtime claim, and no upgrade from an isolated success subsequence are asserted. The bounded literature search found no whole-problem settlement; it is recorded in LOG.md, together with the primary papers actually opened.

Next worker: use PROOF.md to formulate the remaining hardness question at inverse-polynomial success and with a fixed density margin. The substantive missing step is a distribution-preserving reduction from a separate, explicitly named average-case assumption, or a new algorithm. For improving this lemma itself, investigate amplification without fixed density slack and whether the runtime exponent can be reduced; the present proof needs both a refresh probability bounded away from zero as n grows and an exponential repair tail beating the number of trials.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 21:27 +04.
