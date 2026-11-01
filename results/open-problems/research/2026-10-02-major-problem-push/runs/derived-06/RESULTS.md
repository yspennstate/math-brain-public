# Strong LTF entropy and unbounded-fan-in balanced threshold formulas

Research checkpoint, 2 October 2026. This derives a stronger theorem from
the all-LTF result in derived-04 and applies it beyond single thresholds.

For every linear threshold function under uniform input,

\[
 H(f)\le C_+[I(f)-\operatorname{Var}(f)],
\]

with one universal constant. H is the complete spectral entropy, including
the empty Fourier atom. The stronger largest-weight split bound is
Delta H<=C_+ alpha(1-alpha), where alpha is its physical influence.

The same constant works for every read-once LTF-gate formula with balanced
nonroot outputs and disjoint leaf blocks, independently of gate fan-in,
formula size or depth. The root may have arbitrary output bias.

Full proof, original alternate candidate, independent audits, two check
suites and source record are in
[`proofnet24/P03-fei/continuations/2026-10-02-strong-LTF-composition/`](../../../../proofnet24/P03-fei/continuations/2026-10-02-strong-LTF-composition/).

The new elementary complement lemma applies to EVERY unate split:
alpha>1/2 implies Delta H<=8(1-alpha). Its proof explicitly controls the
empty pair and the nonempty pair entropy mass. Combining it with the
completed LTF split bound yields the alpha(1-alpha) local estimate.
The variance decrement is exactly alpha^2, so I-Var is the precise
induction budget. The preserved longer halfspace/KL route independently
corroborates the near-dictator branch.

Disjoint balanced composition has an injective hierarchical spectral
sampling law. Its exact entropy and influence recursions telescope the
I-Var budget with no loss in the constant. This generic composition
framework is credited to O'Donnell--Tan2013; it is not claimed new. The
additional theorem supplies one uniform LTF-gate bound for unrestricted
fan-in in the stated balanced subclass. Its full-entropy definition is
distinguished from the established FEI+ nonempty-entropy convention.

Three independent internal analytic audits pass, including root's separate
elementary reconstruction. Root reran both suites: 7,778 monotone functions,
3,488 near-dictator splits, 401 LTFs and 150 composition nodes/90 formula
roots in the author suite; 2,977 exact recursions, 281 unate splits and five
compositions in the independent suite. Entropy calculations are numerical
sanity checks, not an asymptotic proof substitute.

Historical novelty and external specialist review remain unverified.
Unrestricted Boolean FEI, shared-input threshold circuits, arbitrary
unbalanced children and input-biased FEI are outside this result.

The forest all-graph high-fugacity theorem and integer threshold in
derived-05 remain established baselines. New parallel-slab/strictly-separated
crossing FEI arguments are undergoing audits separately; endpoint equality
has an exact cancellation obstruction and must not be silently admitted.
