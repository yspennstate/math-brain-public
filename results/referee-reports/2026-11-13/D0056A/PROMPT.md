# Open problem D0056: the constant in the survival probability of the critical Derrida-Retaux recursion

Model. m >= 2 an integer (allow real m > 1 where it makes sense). X_0 is a random variable on Z_+ = {0,1,2,...}. Given X_n,
X_{n+1} = (X_n^{(1)} + ... + X_n^{(m)} - 1)^+ with X_n^{(i)} independent copies of X_n. The critical case is
(m-1) E(X_0 m^{X_0}) = E(m^{X_0}) < infinity.

CONJECTURE (Collet-Eckmann-Glaser-Martin 1984 and Derrida-Retaux 2014 for m = 2; general m in the ledger):
in the critical case P(X_n != 0) ~ (4/(m-1)^2) n^{-2} as n -> infinity.

Known (fetch and read before working): X. Chen, Y. Hu, Z. Shi, "The sustainability probability for the critical Derrida-Retaux
model", Probab. Theory Related Fields (2022), arXiv:2108.05610: P(X_n > 0) = n^{-2+o(1)} under an exponential moment beyond m
(E(X_0^3 m^{X_0}) < infinity or similar - check the exact hypothesis). Also look at: Chen, Dagard, Derrida, Hu, Lifshits, Shi,
"The Derrida-Retaux conjecture on recursive models", Ann. Probab. 49 (2021) (free energy near criticality, and the regime where
heavy tails change the answer); Hu-Shi "The free energy in the Derrida-Retaux recursive model" (J. Stat. Phys. 2018); Collet et
al. 1984; Derrida-Retaux 2014; any 2022-2026 paper on the critical Derrida-Retaux / parking on trees model (the critical
Derrida-Retaux model is related to parking on a binary tree: Curien-Henard, Chen, Contat, Aldous-Contat-Curien-Henard 2022-2023,
whose survival/critical exponents may already settle the constant in some cases). The ledger's sweep note says later work
warns the constant 4/(m-1)^2 needs stronger integrability than the bare critical condition.

TASK: settle the strongest piece you can.
1. Literature first: determine exactly what is proved about the constant (any paper proving P(X_n>0) n^2 -> 4/(m-1)^2 under
   some hypothesis, or a counterexample). If it is already proved under some moment hypothesis, say so with theorem numbers,
   then attack the remaining gap (weaker hypothesis, or a counterexample when only the critical condition holds).
2. Numerics: the law of X_n can be iterated exactly on a truncated support (generating functions / convolution powers with
   FFT, support up to a few thousand; track the truncation error rigorously or at least bound it). Compute n^2 P(X_n>0) for
   n up to 10^4-10^5 for several critical laws: two-point laws X_0 in {0,k} tuned to criticality, geometric-type laws, and
   heavy-tailed laws with E(X_0^a m^{X_0}) finite only for small a (P(X_0=k) ~ c m^{-k} k^{-b}). Fit n^2 P(X_n>0) =
   C + C1/n + C2 log n/n ... and compare C with 4/(m-1)^2. Does a heavy enough tail change the constant, the exponent, or the
   log corrections? Use m = 2 and m = 3 at least.
3. Proof: if the numerics support 4/(m-1)^2 under a moment hypothesis, try to prove it (Chen-Hu-Shi's method with sharper
   estimates, or a direct analysis of the generating function recursion G_{n+1}(s) = G_n(s)^m / s + (1-1/s) G_n(0)^m).
   If a heavy tail changes the constant, try to prove that as a COUNTEREXAMPLE to the conjecture under the bare critical
   condition, with an explicit law of X_0.
Keep peak memory under 4 GB; no worker pools larger than 4 threads; use compiled code or numpy for the iteration.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
