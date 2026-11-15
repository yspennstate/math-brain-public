VERDICT: PARTIAL quantified the phase-density obstruction to the brief's conjectural formulation

The density-one exponent 1/2 in the brief does not match the published Zigzag Conjecture. This session proves a deterministic density theorem that quantifies the discrepancy. It proves no new unconditional bound on the chromatic number.

Let f(n)=2 log_2 n-2 log_2 log_2 n+2 log_2(e/2)+1. For any fixed phase band a<={f(n)}<=b with 0<a<b<1, put d=b-a and r=sqrt(2). Its lower natural density is (r^d-1)/(r-1), its upper natural density is r(1-r^(-d))/(r-1), and its logarithmic density is d. These formulas are proved in [PROOF.md](PROOF.md), including integer endpoints and the uniform approximation of theta by the phase.

The source's predicted width exponent is lambda(n)=max(theta(n),1-theta(n))/2. For every beta in (1/4,1/2), the set {n:lambda(n)<=beta} has the preceding densities with d=4 beta-1. At beta=3/8 its lower density is exactly 1/(1+2^{1/4})=0.4567863831..., its upper density is 0.5432136169..., and its logarithmic density is 1/2. These unequal natural densities are intentional: ordinary density does not exist.

Conditional on the Zigzag Conjecture, the same density formulas apply to the exponent of the shortest interval with any fixed confidence q in (0,1). In particular, the conjecture would prevent exponent 1/2 along any density-one set. This is a conditional consequence, not a disproof of that assertion about actual random graphs.

The source is Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, [arXiv:2103.14014v3](https://arxiv.org/html/2103.14014), Conjecture 10. The bounded literature search found no subsequent solution of fixed-p=1/2 concentration. Opened later related papers were Erlang Surya and Lutz Warnke, [*On the Concentration of the Chromatic Number of Random Graphs*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i1p44), and Zhifei Yan, [*The chromatic number of very dense random graphs*, arXiv:2405.13914](https://arxiv.org/abs/2405.13914); their new regimes have varying p. Also opened Annika Heckel and Konstantinos Panagiotou, [*Colouring random graphs: Tame colourings*, arXiv:2306.07253](https://arxiv.org/abs/2306.07253), originally submitted in 2023. This search is not exhaustive.

Reproduce the checks from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify_phase.py
```

All checks passed. Direct integer enumeration and inverse-interval counting agree at N=1000, 10000, 100000, 200000, with counts 454, 4976, 49829, 106225 respectively (integers below 16 excluded). An independent endpoint recurrence reproduces both density constants. The run recorded nice=20, peak RSS 14,483,456 bytes and elapsed time 0.169 seconds. Full data are in [verification.json](verification.json); the exact command and stdout are in [LOG.md](LOG.md). Floating-point checks support the algebra; the proof is analytic.

Two initial runs failed before mathematical checks because macOS rejected resource-limit changes; these attempts are recorded in LOG.md. The final script uses fixed small loops and records actual usage. The nice diagnostic reflects an already inherited nice=20, verified inside the process.

[AUDIT.md](AUDIT.md) records the independent derivations, boundary cases, and the distinction between fixed confidence and probability tending to one. No asymptotic bound on chi was attempted after choosing this formulation problem. The remaining obstacle is probabilistic: obtaining upper or lower concentration bounds at specified n. The deterministic phase frequencies alone cannot supply those bounds.

The next worker should replace the brief's density-one formulation by the precise phase-dependent conjecture, then choose a fixed band separated from phase endpoints and seek a probabilistic estimate there. The numerical enumeration here does not concern chromatic numbers and should not be extrapolated to them. No novelty is claimed for the elementary density calculation.

Task: “push this problem forward by one checkable piece” — 14 November 2026, first recorded local clock 20:48:16 +04.
