# Exploratory computations and failed completions

19 September 2026. These searches use floating-point NumPy/SciPy. They are not proofs, independent audits, or certificates of absence of counterexamples. Their raw scripts and outputs are preserved in the conversation continuation ZIP. The exact arithmetic used in the mathematical delivery is separate: check_balanced_moments.py.

1. Direct transfer spectra were sampled for 500 kernels at each number of blocks 2 through 8. The sampled fifth-trace remainder after removing the Perron term did not give a certified counterexample. Values near roundoff are not used to assert a sign. This does not prove that remainder nonnegative.
2. Individual positive/negative spectral pairing was probed, followed by direct optimization of the fifth remainder. No pairing theorem was obtained. Numerical count changes near a tolerance must not be promoted to exact spectral obstructions.
3. Pair-chain fifth traces were sampled at block counts 2,3,4,5,6,8. No universal trace theorem was derived from the observations.
4. The unbalanced fourth-moment certificate was tested on 240 moderate kernels at each block count 3,4,5,6,8,10; the recorded floating bounds were at least one in these 1440 examples. Stress tests on 1500 highly uneven/sparse flows at block counts 3,4,5,6,8 showed many failures of this sufficient certificate. The counts meeting the numerical threshold were respectively 1334,1291,1292,1277,1312. These are not success probabilities for arbitrary kernels.
5. Positive diagonal balancing was proposed by a finite-dimensional convex numerical optimization. It often drastically reduced the maximum transfer row sum. Only the explicitly rounded positive rational vector in BALANCED_MOMENTS.md was promoted to an exact witness. Solver optimality is neither required nor claimed.
6. A search of the lowest eigenvalue relative to the Perron eigenvalue suggested a possible one-third lower-edge bound in its sampled examples. No proof was found. The theorem does NOT use it; it uses the proved lower edge -q(z)/2.
7. A diagnostic using numerically known Perron and negative-edge values sometimes makes the moment certificate much stronger. It cannot supply a rigorous replacement for a certified beta or q(z).
8. A preliminary second-moment probe encountered a JSON serialization error caused by a NumPy scalar. Its script was corrected but was not rerun after that edit; it is not counted as a completed saved-output experiment.

The exact direct-sum limitation is more decisive than broad numerical optimism: p=(1/100,99/100), W=diag(100,100/99), beta=t_C4(W)=2, a=50 gives a negative optimized fourth-moment lower bound, even though t_H(W)>1. More accurate Rayleigh lower bounds improve this example, but there is no proved universal finite-step certificate success theorem.

The missing full-problem step has not been hidden inside any numerical search: one must prove a successful parameter choice for every kernel, derive a stronger structural inequality, or use a different argument on the failure region. Current status: PARTIAL, not solved.
