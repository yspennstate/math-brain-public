# Audited partial results on FEI and forest negative correlation

Research continuation, 2 October 2026. Full proofs, independently written audits and reproducible verification code accompany both results. Historical novelty remains unverified. Neither theorem resolves its full famous conjecture.

## General third-coefficient forest theorem

For an arbitrary connected finite weighted graph, let R_ef be the multivariate forest Rayleigh difference for two distinct non-bridge edges, evaluated at activities lambda*c. Write

    R_ef(lambda*c)=H0 lambda^(2n-4)+H1 lambda^(2n-5)
                    +H2 lambda^(2n-6)+... .

The established spanning-tree coefficient is nonnegative. A recent primary paper gives a nonnegative electrical formula for H1 under H0=0, and describes the equality geometry. The present derivation proves a further general statement:

    H0=H1=0  implies  H2>=0.

It supplies an explicit identity

    H2=tau^2 sum_(g,h) c_g c_h (eta_e,g T eta_f,h^T)^2,

where tau is the weighted spanning-tree sum, T is the Green matrix on the common zero-potential interface, and eta are explicitly defined harmonic current-response rows. All definitions, conductance hypotheses, endpoint boundary cases and derivative normalization are in `GENERAL_H2_SOS_PROOF.md`.

The proof is general, not inferred from tested graph families. It uses exact two- and three-component grounded forest-minor identities, conditional Gaussian Grassmann factorization through the electrical interface, invariance of harmonic data under marked conductance changes, and an electrical circulation energy identity. A separate original lowering-operator proof is preserved in the draft. An independent reviewer derived the cleaner conditional proof independently, and another reviewer audited the normalization, equality geometry, determinant signs and electrical completion. The root analyst read both full derivations and reran both independent exact graph-check programs successfully.

The independent programs enumerate full forest configurations and separately compute the electrical formula with exact rational arithmetic. They include non-twin support regions, varying interior harmonic exit rows, two- and three-dimensional interfaces, varied marked conductances, a marked endpoint on the interface, and adjacent edges. These checks support implementation and normalization; the analytic argument proves the theorem.

When H2>0 the theorem proves strict marked-pair negative correlation at sufficiently large fugacity. If H0=H1=H2=0 the next coefficient is still uncontrolled. The recent paper gives examples with arbitrarily long strings of leading zero coefficients, so this theorem must not be advertised as a proof of every high-fugacity case. It also does not prove all-fugacity negative correlation, negative association, or the q<1 random-cluster conjecture.

Primary boundary: Ciceksiz--Ravichandran, arXiv:2610.00549v1, https://arxiv.org/html/2610.00549v1 . Their H0/H1 result and equality classification are credited explicitly. The current proof extends the coefficient analysis beyond those statements. This comparison does not establish priority against all earlier literature.

## FEI for monotone functions confined to a fixed Hamming band

Let f be coordinatewise monotone on the uniform n-dimensional Boolean cube. Assume f is constantly minus below a band of k consecutive Hamming layers and constantly plus above it; arbitrary monotone decisions inside the band are permitted. The complete proof gives

    H(f) <= [25+64(k+1)^2] I(f).

For one exceptional layer it improves this to H(f)<=62 I(f). In particular it covers arbitrary-bias positive weighted thresholds whose sum_i |w_i/c-1| is bounded independently of dimension, for some common positive scale c. Coordinate labels need not have any symmetry inside the band.

The proof uses an entropy stability inequality for nearby Boolean functions, a random symmetric threshold reproducing the layer averages and expected total influence, and a Dirichlet spectral bound on a short Hamming band. In small dimensions an averaged Poincare identity supplies the required disagreement bound. The only pre-existing FEI theorem imported is the symmetric-function bound of O'Donnell--Wright--Zhou (2011), constant12.04, https://www.cs.cmu.edu/~odonnell/papers/fei.pdf .

The root analyst checked the full derivation and constants and reran the author's verifier. A separate auditor checked every proof step and exhaustively verified the algebraic identities on every monotone function through dimension five, including all7581 monotone functions in dimension five. Influence, random-threshold disagreement and variance identities use exact rational arithmetic; floating entropy computations are supplementary checks. The author also checked thousands of perturbation and band spectral instances, arbitrary single-layer decisions, and weighted thresholds with tail bias.

This is a restricted FEI theorem. Its constant grows with band width. It does not give a dimension-free bound for all linear threshold functions or all monotone functions, and does not prove full FEI. A wider prior-art review is still required before claiming novelty.

## Continuation targets

For forests, study the response-orthogonality condition H2=0 and higher boundary interactions; do not recycle the now-proved third coefficient as an open step. For FEI, control the entropy cost for wider weighted bands or obtain a rigorous dimension-free Gaussian-to-discrete transfer. The already proved maximum-influence and separator obstructions continue to rule out those particular shortcuts. Archive failed routes and precise gaps alongside any subsequent proof.
