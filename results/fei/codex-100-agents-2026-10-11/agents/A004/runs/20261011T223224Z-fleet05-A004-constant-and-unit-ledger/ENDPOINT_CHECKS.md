# Endpoint audit, bits and normalized sign spectra

Put e=2^-n in the rare-defect row, Hplus=sum_nonempty P log2(1/P), E0=P_empty log2(1/P_empty), D=sum min(I_i,1-I_i). A zero-mass conditional law is omitted. Formulas are exact; limits below have analytic justification.

| Sign | Spectrum | H | I | v | I-v | D | E0 |
|---|---|---|---|---|---|---|---|
| Constant +/-1 | P_empty=1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dictator +/-x_j | P_{j}=1 | 0 | 1 | 1 | 0 | 0 | 0 |
| Character +/-chi_A, k=|A|>=1 | P_A=1 | 0 | k | 1 | k-1 | 0 | 0 |
| f_n=1-2*1_{x=x0} | P_empty=(1-2e)^2; P_S=4e^2 for every nonempty S | E0+8e(1-e)(n-1) | 2ne | 4e(1-e) | 2e[n-2+2e] | 2ne for n>=2; 0 for n=1 | (1-2e)^2 log2(1/(1-2e)^2) |

For the rare defect the conditional nonempty spectrum is uniform on 2^n-1 subsets, so H(R)=log2(2^n-1). In particular H(R)/I diverges; a uniform bound on *unweighted* conditional entropy by total I is false. The valid decomposition is h2(v)+vH(R). The unnormalized nonempty entropy is 8e(1-e)(n-1), with E0=4e/ln2+O(e^2). Thus H/I->4, Hplus/I->4, and E0/I->0. These are calibration limits, not a disproof of FEI. The Taylor remainder follows from analyticity of -(1-2e)^2 ln((1-2e)^2) near e=0. All displayed endpoint formulas were checked by exact Walsh arithmetic for n=1..8.

The n=1 rare defect is itself a dictator: H=0 and I-v=0. At n=2 it is a bent function with four spectral atoms 1/4: H=2, I=1, v=3/4, I-v=1/4, D=1, E0=1/2. It attains D=4(I-v). This explicitly catches dividing a strong-FEI statement by a zero deficit or treating D as I at every dimension.

For an indicator g=1_{x=x0} of mass e, every coefficient has squared magnitude e^2. Its raw full spectral entropy is 2ne, total spectral mass e, normalized full spectral entropy n, and Dirichlet energy ne/2. Its boundary influence is 2ne. At a constant indicator g=1, the normalized spectrum is a single empty atom; at g=0 it has no normalized law. For the dictator indicator (1+x_j)/2 the normalized full indicator law has two atoms 1/2 and entropy 1; the associated sign has entropy 0. These examples expose the omitted normalization and affine -2v term.

## Imported inequality endpoint decisions

| Imported interface | Constant | Dictator | Character/parity | Nearly constant point defect |
|---|---|---|---|---|
| H=h2(v)+vH(R) | zero law branch | 0=0 | 0=0 | equality with R uniform |
| H=Hplus+E0 | 0=0 | 0=0 | 0=0 | exact displayed row |
| E0<=v/ln2<=I/ln2 | equality zero | left zero | left zero | holds; E0/v->1/ln2 |
| E0<=beta(I-v), beta<2.553 | both zero | both zero | left zero | holds; at n=2, E0/(I-v)=2 |
| h2(v)<=2I and v<=I | both zero | 0<=2; equality v=I | 0<=2k; v<=k | certified, all n tested; all-n analytic proof in report |
| H(level)<=Clev I | zero | deterministic level | deterministic level k | level masses binomial except modified empty row; source universal lemma applies |
| H<=Creg D (regular functions) | zero | zero | k=1 valid; k>=2 not a regular-function premise | a point conjunction sign is unate regular, and H/I->4<Creg |
| D<=4(I-v) | zero | zero | zero<=4(k-1) | equality at n=2, holds for all n |
| Hcorr<=CT(I_spec-v), symmetric thresholds | zero after fixed inputs removed | zero corrected entropy/deficit | parity uses its separate source gate lemma | uniform point-conjunction is a threshold; limits give Hplus/(I-v)->4 |
| AND/OR Hcorr<=(2+4/ln2)delta; parity Hcorr<=(2/ln2)delta | zero | zero | fair parity Hcorr=0; biased parity finite checks pass | conjunction endpoint passes; sharp AND/OR limit in source is a different biased regime |
| Hplus<=Kdelta => H<=max(K,1/ln2)I and H<=(K+beta)delta | implication includes zero case | zero conclusion | zero left side | algebraic implication retains E0; no change in nearly constant limit |
| C018 Delta_i=B_i+JS; JS<=(2/ln2)min(I_i,1-I_i) | all zero | all zero even at I_i=1 | all zero; every spectrum atom deterministic | exact symbolic identities and interval bounds pass for n<=8 |
| C018 B<=K I => H<=(K+2/ln2)I | trivial base | zero entropy | zero entropy | implication valid, premise universally OPEN |
| Physical block/tree influence telescope | zero | querying support consumes 1 | each queried support bit consumes 1 | minority activation retains all control boundary cost |
| C020 H<=h2(v)+Kref I+R | treat without conditioning, zero | positive-probability code branch only | same; posterior law must remain normalized | rare logarithms and v normalizer stay in full R; universal payment OPEN |
| Prior-mixture conditional coding | v=0 handled separately | v=1 no empty charge | v=1 no empty charge | h2(v)+v weighted full description cost, prior fixed globally |
| Exact disjoint composition | remove constant output blocks before dividing by v_i | identity substitution | parity gate certified separately | nonbalanced output biases retained; no false balanced substitution |
| Shared-data selector bound H<=2a+average H(children) | a=0 or all constant is handled by exact formula | a dictator among branches still pays physical selectors when they actually change output | leaf characters cost zero H but nonzero I | low selector energy does not by itself pay 2a; no universal inference |
| Percolation entropy/refinement | generic refinement all zero if set deterministic empty | deterministic spectral set has zero H; *crossing theorem hypotheses do not hold* | same out-of-scope status | point defect is not a crossing; geometric occupancy growth must not be imported |
| C024 natural information generator identities | zero-information states legitimate | deterministic spectral source has zero TC/DTC | same | population cost and information units are distinct; lifetime transfer still OPEN |

The C020/code rows are normalization and hypothesis checks, not executed tests of a missing arbitrary-family reference construction. The source complete-reference theorem's premises must be supplied before evaluating its numerical cost. Likewise crossing theorems cannot be falsified with functions outside their geometry. No source result has been refuted by this audit.

For an increasing biased dictator on Bernoulli p, pivotal influence=1, spectral influence=v=4p(1-p), and corrected Hcorr=0. Ordinary spectrum entropy is h2(4p(1-p)) and is usually positive; the Shannon entropy of the *output* is h2(p), a third quantity. As p->0, H_Shannon/I_spec~log2(1/(4p))+1/ln2 diverges. Product-biased corrected FEI+ has no such divergence. At p=0,1 deterministic coordinates are removed.

For fair monotone signs oriented output changes each have probability I_i/2, independent resampling changes with probability I_i/2, while the lower-side pivotal fiber fraction is I_i. Under biases oriented changes are (1-p_i)rho_i and p_i rho_i; spectral influence is 4p_i(1-p_i)rho_i. The 256-case biased exact checker verifies the inclusion/resampling identities and 96 AND/OR/parity inequality certificates.

## Evidence boundary

Exact certificates: all 278 signs n<=3, 32 endpoint cases n<=8, and all 256 biased two-bit cases on the frozen bias grid. Equality checks use integer Walsh transforms/direct sums and prime-log linear forms. Rational logarithm enclosures certify tested signs and constants. General conversion identities are proved in REPORT.md. Independent acceptance by A086/A094, remote mirror save and actual downstream use remain pending. This is a baseline unit audit, not a full universal proof-chain reconstruction.
