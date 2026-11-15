VERDICT: PROVED adjacent-interval incompatibility of the scalar extremizer and a positive separation G >= G* + 1/1944 in the strengthened moment relaxation

The round-3 scalar result holds. Its moment witnesses and threshold were independently re-derived. What is new is the proposed next step: its extremizer F* fails the adjacent-interval constraints already for lengths a=1 and b=1/4.

For nonnegative integer counts A,B and T=A+B, the pointwise inequality

1_{A>0}+2·1_{T>0} >= 2T−T(T−1)/2−B(B−1)/2

implies, under the specified Poisson moments,

F(a)+2F(a+b) >= 2(a+b)−(a+b)²/2−b²/2.

At the selected lengths F* gives 79/48, while the right side is 81/48: an exact contradiction of margin 1/24. A second proof uses the scalar equality support {0,2,3}. The certificate also holds directly for finite spectral counts and tolerates small moment errors; no convergence of count laws is used.

Adding only this one joint law to the scalar relaxation forces its support endpoint to satisfy G >= G*+1/1944. Here G* is the preceding report's exact root near 2.00636. The proof converts the certificate's positive deficit into excess area above the scalar CDF envelope. This is a necessary bound for a strengthened relaxation, not its optimum and not an improved flat-torus gap theorem. The complete proof and exact constant audit are in [PROOF.md](PROOF.md); commands, source checks and intermediate results are in [LOG.md](LOG.md).

The under-five-minute web check found no solution of the two-dimensional target. Opened primary sources include Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, [*Triple correlation and long gaps in the spectrum of flat tori*, arXiv:1809.07881](https://arxiv.org/abs/1809.07881), and its [publisher text](https://ems.press/content/serial-article-files/31432). Their averaged triple theorem must not be replaced by pointwise triple convergence. The already-recorded [Kim–Marklof–Welsh result](https://arxiv.org/html/2601.03209v2) remains a three-dimensional Dirichlet-box pair-correlation theorem. No SOLVED_ELSEWHERE.md is warranted by this check.

Validation: the incompatibility was proved by two independent arguments; the envelope was checked by CDF and density integration; all rational margins, area and slope estimates, root signs, large-endpoint comparisons, error coefficients, and ordered-count factors were checked separately. No numerical program was run. Read commands used `OMP_NUM_THREADS=1 nice -n 15 /bin/cat` and `/bin/ls`; the sandbox continued to deny priority adjustment. Writes used apply_patch and stayed in this folder. No git or subagents were used.

What failed and what remains uncertain: F* cannot be jointly realized under these moments. No optimal joint threshold or finite-endpoint realization was found. The new bound has not been transferred through the averaged torus theorem. The literature check is bounded, and no global priority claim is made for the elementary inequality or its use here.

Next worker: start with the exact finite-count inequality (20) in PROOF.md. Combine its two triple terms with the scalar long-gap inequalities using nonnegative weights, and prove the needed common-subsequence upper bound through the published density-point/averaging argument. Establish that quantifier step before announcing any improved torus gap constant.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 04:54:16 Asia/Tbilisi; prompt receipt time unavailable.
