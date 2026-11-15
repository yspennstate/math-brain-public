# C035 v1: conditional analytic lead check

Proof SHA256 5756545619823225aa5702f4aa25880187d7bc8da056e58595d36c66d67c778b.
15 October2026, codex-term-362ebe34. Conditional correctness PASS given
C009's stationary conditional tree and C022's common augmented histories,
and the stated C034 drift/terminal probability witnesses. This is not a
new finite graph transfer, a full independent C034 matrix calculation,
or a substitute for the required independent account reviews.

The shared-copy step is sound: conditional on the complete immediate
label multiset and occurrence identities, the chosen occurrence is
constrained only by its original outgoing label. The new reverse boundary
uses all other occurrences and the incoming boundary, so it reveals no
additional information about that descendant subtree. Multiplication by
the local function (1+K)^eta preserves this marginal fact. Duplicate
copies remain dependent; linearity and the convexity bound require no
independence. The claim is about weighted path multiplicities.

With column-parent matrices, R=D_mu T^transpose D_mu^-1 gives
R(D_mu h)<=D_mu h-mu from the original LEFT drift. For the moment
perturbation B[j,i]=E[K_i K_ji], its row bound uses K_ji<=K_i and
E K_i^2<=9(C^2+C)/pi_a. Summing mu_i/pi_a over all a>b,d gives exactly6,
not24 or a minimum history probability. Consequently B(D_mu h)<=54H(C^2+C)
entrywise. The selected eta makes this perturbation at most q^2/2,
which is at most mu_j/2. Since h<=H, the contraction factor is at most
1-1/(2H). The forcing vector is at most2. Sum_i mu_i<=3 and g>=mu yield
the invariant moment bound12H^2. Monotone convergence passes from finite
reverse depth to full W. Conditional Jensen on one common tree gives the
history bound; Palm reversal and the root decomposition identify the
canonical right resolvent. No maximum-over-rare-history bound is used.

Own audit_t186_c035_constants.py independently recomputed all48 rational
left-drift inequalities from saved matrix upper entries and rational h,
the two eta values, moment constants, perturbation slack and recurrence
invariant. It also recomputed C034's A/theta/gamma formulas. The saved
matrix enclosures, terminal lower probabilities and original Poisson
encoding remain explicit premises. Source identity and arithmetic receipt
are in T186_C035_CONSTANT_AUDIT_RECEIPT.json.

The useful new scope is uniform weighted Lp control of latent history
occupation densities. C028/C029's adaptive matching filtration,
relative depletion, repeated-coordinate exposure, genuine two-coordinate
hits and planted-to-ER transfer remain unpaid. The tiny exponents are
valid existence constants, not practical finite-size estimates.
