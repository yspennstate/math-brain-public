# A004 constant and unit ledger

## exact target, quantifiers, hypotheses and units

This is the finite, reusable normalization audit assigned to A004/B01, not a new candidate proof of FEI. For every n>=0 and every Boolean sign f on the uniform cube, use a_S=E[f chi_S], P_S=a_S^2, H=sum P_S log2(1/P_S), I=sum |S|P_S, v=Var(f)=1-a_empty^2, and delta=I-v. Constants satisfy H=I=v=delta=0, so no ratio is formed there. All zero entropy summands are zero; conditional laws of mass zero are omitted. The universal target remains existence of one finite C with H<=CI in every dimension.

The two requested deliverables are CONVENTIONS.json and ENDPOINT_CHECKS.md. The report and code give their derivations and certificates. Scope: normalization of the current threshold/percolation interfaces, the source erasure and physical-block identities, the posterior forest residual, the prior-mixture interface, and the history endpoint. Reading an imported theorem for units is not an independent reconstruction of its entire analytic proof.

## sources actually read, revisions and theorem locators

The canonical EXECUTION_PROTOCOL.json was read in full: revision 2026-10-11-execution-v2. README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS, AGENT_ASSIGNMENTS/A004, and the campaign TeX provide the contracts and source graph. The BOARD snapshot is 2026-10-11 22:26 UTC. B01 STREAM_NOTES.md is absent at the supplied path; no inferred lead instruction is used. A001--A003's board summaries already cover quantifiers, transformations and forest residuals; those tasks are not restarted here.

The supplied threshold_paper_38pp.txt was consulted at its definitions, Theorems A--D, Lemmas 2.1--2.2, Section 5.5/Proposition 5.5, Section 6.1/Theorem 6.6, Proposition 7.1, Lemmas 7.5--7.6/Corollary 7.7, and Section 8 selector/activation identities. The canonical campaign pins the current public source to b38ba0ab49618ccbe6d1518a34c141dcec9f247c; local TXT files are separately hashed because PDF extraction is not that source. The earlier 29-page version was consulted for convention/revision comparison, not as a replacement for the current result.

The supplied percolation_spectral_pivotal_entropy_30pp.txt was consulted especially at Section 1.1, equations (1)--(5), Lemma 2.1, Theorem 3.1, and the physical/spectral normalization equation (18). The 31-page other version was consulted for comparison. In particular its J denotes spectral expected size, unlike several other sources' use of J for a deficit or recombination term.

Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted with sources/ERASURE_REDUCTION.md Sections 1--4, BLOCK_RESTRICTION_IDENTITY_2026-09-18.md Sections 1--3, LOG_ALLOCATION_CURATED.md Sections 2--5, ONE_BIT_ENDPOINT.md, GAMMA_ENDPOINT_LEDGER.md, and ROUTE_MAP_CURATED.md. The original B05, B09 and B19 reports under the canonical runs tree were consulted for the actual normalization and review boundaries. Source snapshots/hashes and retained copies are in out/source_manifest.json and out/sources/. Large combined tool outputs were truncated; only the specifically used mathematical sections above are asserted as inspected, not a line-by-line reconstruction of every paper. No older numerical certificate is upgraded to exact merely by being imported.

A small primary-source web check returned the historical corrected threshold-entropy paper, [Upper Bounds on Fourier Entropy, revision 2](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/), and [Shalev's extremal-class paper](https://arxiv.org/abs/1806.03646). Neither is a proof dependency or a substitute for the local current manuscript. The ledger makes no novelty claim.

## complete derivation or exact first unsupported line

### 1. Logarithm units

For every probability/subprobability law, H_nat=(ln2)H_bits, and similarly for binary entropy, KL, JS, mutual information, TC, DTC and entropy-functionals. An influence or variance has no logarithm and does not change. Thus H_nat<=c I converts to H_bits<=c/(ln2) I; a bit constant converts to a natural constant by multiplication by ln2. If both sides are information quantities the coefficient is unchanged. A mixed charge a TC_nat+b I becomes a TC_bits+(b/ln2)I after dividing the entire inequality by ln2. The scalar ln2 factors in rank discrepancies, complete codes and normalization charges must therefore be converted together.

Checked explicit bit constants:

| Interface | Exact bit constant | Certified upper bound |
|---|---|---|
| Spectral-level entropy | Clev=log2(4+e) | 2.749 |
| Regular/weighted uniform threshold | Creg=Clev+2log2(e*pi) | 8.937 |
| Symmetric product-biased thresholds | CT=20(23+ln16)/ln2=80+460/ln2 | 744 |
| Erasure recombination | 2/ln2 | 2.886 |
| AND/OR corrected entropy | 2+4/ln2 | 7.771 |
| Parity corrected entropy | 2/ln2 | 2.886 |
| Complete forest base cost | Kref=3+2log2(3)+log2(6e) | 10.198 |

The decimal bounds in this table are outward rational bounds, not nearest-rounded interval endpoints. out/validation.json stores exact rational enclosures for Clev, Creg, CT, Kref and the erasure constant. The other displayed bounds follow from the same ln2 interval; their proof can be checked directly. In particular CT is already a bit constant: dividing 744 by ln2 a second time would be incorrect.

### 2. Signs, indicators, raw entropy and normalized entropy

Let g=(f+1)/2 with p=Eg. Then ghat(empty)=p, fhat(empty)=2p-1 and fhat(S)=2ghat(S) for S nonempty. Parseval gives sum ghat(S)^2=p, whereas sum fhat(S)^2=1. Consequently Var(f)=4p(1-p)=4Var(g), and the spectral Dirichlet energy I_spec(g)=sum |S|ghat(S)^2 is I(f)/4. Probability of a pivotal flip, however, is identical for f and g. The label "indicator influence" must therefore specify boundary probability or Dirichlet energy.

For a nonnegative vector q of total mass M>0, define Ent_raw(q)=sum q log2(1/q). Direct substitution gives

    H(q/M)=Ent_raw(q)/M+log2 M.

It is false to call Ent_raw(ghat^2) Shannon entropy without this normalization. For the nonempty sum Hplus(f), the exact scaling is

    Hplus(f)=4 Ent_raw(ghat(S)^2: S nonempty)-2 Var(f).

The additive term comes from log2(4)=2; pure factor-four scaling is false. Let H_g be Shannon entropy of the normalized full indicator spectrum ghat^2/p. Its empty atom has mass p, and its nonempty conditional law agrees with that of the sign. Hence

    H(f)=h2(v)+4p[H_g-h2(p)],   v=4p(1-p).

At p=0 the normalized indicator law is undefined and omitted. At p=1 its law is the empty atom and H_g=0. Both constant signs have H=0. The same nonempty affine scaling holds for corrected strong entropy with any fixed product basis and correction factor sigma_S^2; empty coefficients still require their own treatment.

### 3. Empty versus nonempty

Let R_S=P_S/v on S nonempty when v>0, and E0=(1-v)log2(1/(1-v)). Then

    H=h2(v)+vH(R),
    Hplus=vH(R)+v log2(1/v),
    H=Hplus+E0.

For v=0 the conditional law R is omitted; H=Hplus=E0=0. For v=1, E0=0 and H=Hplus=H(R). Thus the h2(v) term belongs to conditional nonempty entropy, whereas adding h2(v) to the raw nonempty sum double-counts v log2(1/v).

The universal bound E0<=v/ln2 follows from -(1-v)ln(1-v)<=v. Poincare v<=I gives E0<=I/ln2. Therefore Hplus<=K I implies H<= (K+1/ln2)I. More usefully Hplus<=K(I-v) implies

    H<=max(K,1/ln2) I.

The source also gives E0<=beta(I-v), beta=sqrt(2/(1-ln2))<2.553 (Lemma 7.6), so Hplus<=K(I-v) implies H<=(K+beta)(I-v). This explains the source's clean 744 and 747 constants.

For completeness, the empty-coefficient estimate uses entropy tensorization for the minority indicator: p ln(1/p)<= (ln2)I/2. Each pivotal fair fiber contributes (ln2)/2 to conditional entropy; this proves I>=2p log2(1/p). Put x=1-2p=|Ef| and a=1-ln2. Subtract v=1-x^2 to obtain

    I-v >= (1-x)[-ln(1-x)-x ln2]/ln2
          >= (1-x)(a x+x^2/2)/ln2.

The scalar inequality -sqrt(x) ln x<=1-x follows by x=exp(-2t), t<=sinh t. It gives E0/(I-v)<=2sqrt(x)/(a+x/2)<=sqrt(2/a) by AM-GM. The endpoints x=0,1 have E0=0. This proof treats parity and dictators, where I-v may vanish, without dividing by zero.

The other universal variance charge is h2(v)<=2I. The source proves the stronger I>=v+(v/2)log2(1/v): compare edge isoperimetry using x=sqrt(1-v) and the concave function (x-1)log2(1-x)+(1+x)log2(1+x)-2x, zero at x=0,1. Since h2(v)<=v log2(1/v)+v/ln2, the stronger comparison yields h2(v)<=2I+(1/ln2-2)v<=2I. This charge may be added once to a nonempty conditional code; it cannot be silently repeated at every witness choice.

### 4. Total, directional and biased influence

On the uniform cube, rho_i=P[f(X)!=f(X^i)]=E[((f_+-f_-)/2)^2]=sum_{S contains i}P_S. Total I=sum rho_i. If E_i counts undirected boundary edges in direction i, rho_i=E_i/2^(n-1). The sum over all vertices counts both orientations. The output-oriented probability P[f(X)=-1,f(X^i)=1] is rho_i/2. A monotone lower-side pivotal fiber fraction is instead rho_i. These are distinct common meanings of "directional". Independent fair resampling changes f with probability rho_i/2; its squared sign difference has expectation 2rho_i.

For independent Bernoulli inputs with parameter p_i, use phi_i=(X_i-p_i)/sqrt(p_i(1-p_i)). The pivotal event depends only on other coordinates. If its probability is rho_i, the squared Fourier inclusion mass is

    I_spec,i=4p_i(1-p_i)rho_i.

This follows by integrating i: its sign coefficient equals 2sqrt(p_i(1-p_i)) times the Fourier coefficient of (f_+-f_-)/2 on the other coordinates. Reversal change probability is rho_i, but independent resampling change probability is 2p_i(1-p_i)rho_i=I_spec,i/2. Biased output-oriented flip probabilities need not agree: for an increasing sign they are (1-p_i)rho_i and p_i rho_i. This explains why the uniform half-orientation rule cannot be imported under biases.

The threshold paper's I_mu is I_spec. The percolation paper's I is sum rho_i and its J is sum I_spec,i. They agree at p_i=1/2. On a uniformly interior bias interval [p0,1-p0],

    4p0(1-p0) I_piv <= I_spec <= I_piv.

The comparison constant depends on p0. Sending p0 to zero cannot retain it. Nor do equal one/two-point inclusion statistics imply equality of spectral and pivotal laws or their entropy. For a uniform dictator, the spectral set is deterministic but the output is a fair sign: H(S)=0 and H(f(X))=1.

### 5. Corrected strong entropy and character centering

Under product biases define sigma_i^2=4p_i(1-p_i) and

    Hcorr=sum_{S nonempty}P_S log2(product_{i in S}sigma_i^2/P_S)
         =Hplus+sum_i I_spec,i log2 sigma_i^2.

This is the threshold paper's Hplus_mu, not ordinary conditional entropy or ordinary Shannon entropy. E_mu=(ln2)Hcorr. For Boolean signs |fhat_mu(S)|<=E|phi_S|=product_i sigma_i, so each corrected summand is nonnegative. A biased dictator has P_empty=(2p-1)^2, P_{i}=4p(1-p), I_spec=v=4p(1-p), delta=0, Hcorr=0, and ordinary Shannon entropy h2(4p(1-p))>0 except at its special deterministic spectral endpoints. This refutes importing the biased corrected theorem as H_Shannon<=C delta. At p=0 or 1 fix the deterministic input and remove its basis coordinate before using these identities.

On the uniform cube character multiplication sends P_S to P_{S xor U}. It preserves full H but can change v, Hplus and I. Its new ith influence is 1-rho_i if i belongs to U, and rho_i otherwise. Therefore

    D=sum min(rho_i,1-rho_i)=min_U I(chi_U f).

One also has D<=4(I-v): |fhat({i})|<=rho_i, and min(rho_i,1-rho_i)<=2rho_i(1-rho_i)<=2(rho_i-fhat({i})^2). Summing gives at most twice the degree-at-least-two size-weighted mass; |S|<=2(|S|-1) there gives the bound. A dictator/character can be centered to a constant; its I changes while H remains zero. Character translation of the biased basis does not give this uniform XOR rule.

### 6. Universal bridge constants and first unsupported lines

For C018 use the source notation B_i=H(S_i|S_without_i), full spectral law including the empty atom. With u=fhat(T), w=fhat(T+i), m=u^2+w^2, the two child laws have atoms (u+w)^2,(u-w)^2. Chain rule gives Delta_i=B_i+JS(children). The scalar inequality [(1+z)ln(1+z)+(1-z)ln(1-z)]/2<=1-sqrt(1-z^2), obtained by derivative comparison, yields

    0<=JS<= (2/ln2)sum_T min(P_T,P_{T+i})
          <= (2/ln2)min(rho_i,1-rho_i).

Thus a universal B<=K_bits I would imply full FEI with C_bits<=K_bits+2/ln2 by choosing a weighted-average good coordinate and inducting with I=E I(child)+rho_i. In natural units the same conclusion is C_nat<=K_nat+2. No new bound on K is proved. The first unsupported line is the universal B<=K I, not the unit conversion or induction. The scalar additive constant's sharpness is not a claimed optimal Boolean FEI constant.

For C019 a genuine physical stopping tree obeys I(root)=sum_internal w_v I_{A_v}(f_v)+E I(leaf). Therefore a per-node entropy decrement bound K_bits times consumed influence and a terminal bound C_leaf I(leaf) yield max(K_bits,C_leaf)I(root). For blocks the exact decrement is H(S_A|S_complement)+MI(physical restriction; remaining spectrum), and the source channel cost is at most (2/ln2)I_A. The conditional spectral term is unpaid; replacing it by erasures of child laws is invalid. If the tree charges are natural, convert their whole sum before combining with a bit terminal bound. The local bent-defect no-go from B05 remains intact after unit conversion; no constant rescaling repairs a divergent ratio.

For C020 the campaign's forest interface is H<=h2(v)+Kref I+R. Hence R_nat<=k_nat I would imply C_bits<=2+Kref+k_nat/ln2. Both v(Lambda+log2 Z) and the posterior entropy subtraction in R must be in the same base, with distinct actual finite runs as witnesses. The rank discrepancy F written with ln must retain gamma/ln2 in a bit cost. The negative normalizer log2 Z is not a missing positive charge and cannot be bounded separately after cancellation. Universal payment of the complete R is the first unsupported line.

The seed prior-mixture bound H<=h2(v)+sum_nonempty P_S inf_j[b_j(S)+log2(1/w_j)] uses a fixed subprobability reference for each j and a globally normalized prior sum w_j<=1. For a countable dyadic prior, scale penalties and all normalizers stay inside the selected complete cost. If the entire conditional cost expectation is <=K I, the full bound is (K+2)I; no independent selection of cheapest components is licensed.

For C024 the gamma/history notes use natural units for TC, DTC, KL losses and Gamma. The population size J_t=sum marginals is log-free. Dividing the complete generator/integral identity by ln2 converts its information terms; any coefficient multiplying J0 also divides by ln2. Its paid weighted Gamma dissipation budget is not the weighted Gamma lifetime in the desired signed remainder. The first unpaid line is payment of that signed lifetime minus forced DTC-information losses, followed by a separate transfer to spectral H. Changing units closes neither line.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications were written before execution: out/FROZEN_SPEC.json and out/BIASED_FROZEN_SPEC.json. No symmetry quotient, adaptive dimension increase, GPU or heavy job was used. Memory estimate was 30 MB, below the mandatory memok threshold. Exact integer Walsh transforms were independently compared with direct character sums. Entropy identities were compared as rational linear combinations of log2 primes, so the equality checks do not use floating arithmetic. Named inequality signs used rational atanh-series logarithm intervals with proved geometric tail; constant enclosures use factorial e bounds and Machin arctangent pi bounds. Every displayed final interval is rounded outward to a dyadic grid, stored as rational strings. Fields labeled display_only are not certificates.

Commands from the A004 directory:

    python -X utf8 runs\20261011T223224Z-fleet05-A004-constant-and-unit-ledger\code\check_ledger.py
    python -X utf8 runs\20261011T223224Z-fleet05-A004-constant-and-unit-ledger\code\check_biased.py

The uniform domain consists of all 278 signs for n=0,1,2,3 and 32 labeled endpoint cases for n=1..8. The biased domain consists of all 16 two-bit signs on all 16 pairs of biases from {1/2,1/4,1/8,1/1024}: 256 cases. Final assertion totals, measured runtimes and exact certificates are in the corresponding validation JSON files. These finite checks verify ledger identities and named finite inequalities; the displayed analytic derivations provide the all-dimensional conversion statements. The first run hit a serialization size limit after algebraic checks; out/pilot_failure.json preserves it. Outward dyadic rounding repaired output formatting. This was not a failed mathematical mechanism.

## proof dependencies and changed downstream conclusions

Dependencies are finite-product entropy tensorization, Parseval, chain rule/Gibbs, and the explicitly located source statements. No open FEI/payment claim is assumed. Existing class estimates are reused at their stated hypotheses, not promoted to universal FEI. The single bundled baseline claim is a normalization interface, not another broad unreviewed theorem competing with B01's research candidates.

Downstream substitutions: natural C018 loses +2 rather than +2/ln2; C020 natural residual divides by ln2 only once; C019 natural node charges and bit terminals use a common base; indicator raw nonempty entropy requires the -2v affine term; percolation pivotal I is spectral J only at fairness; normalized nonempty entropy carries h2(v), while raw Hplus carries E0. No source theorem is refuted by these distinctions. In particular a biased dictator is a witness against a misreading, not against the manuscript's corrected FEI+ theorem. Independent acceptance and actual downstream use remain pending.

## one next mathematical action and independent reviewer

A086 is the nominated independent baseline reviewer, with A094 alternate. Reconstruct the affine indicator entropy conversion, the biased influence factor, and the outward constant enclosures using an independent representation. After that this baseline should be retired. The shortest new B01 mathematical action is to substitute this common ledger into A003's parity-lifted arbitrary-core family and identify the exact unpaid posterior expectation with terminal seed entropy retained. Rechecking constants on an already calibrated isolated class is not that action.

## actual persistence receipts or precise save blocker

All writes are confined to the assigned A004 directory. REPORT.md, CONVENTIONS.json, ENDPOINT_CHECKS.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json, code, frozen specs, validation outputs and source copies are local deliverables. out/persistence_receipt.json records SHA256 and size after schema checks and successful regeneration. No git, mail, brain write, external index mutation or another agent's file modification was performed. Supervisor adoption/copy, remote mirror verification, independent acceptance and downstream mathematical use are not claimed.

## Universal bridge

This stage makes C018, C019 and C020 mutually usable in one exact unit ledger: the erasure overhead is +2 natural units or +2/ln2 bits, the forest residual converts to the constant 2+Kref+k_nat/ln2, and physical stopping costs combine with terminal bounds only after matching bases and retaining the empty atom. It closes the assigned normalization baseline, contributing no new universal payment estimate. C024 still needs its signed history-lifetime payment and a distinct entropy-transfer step. The full FEI conjecture remains OPEN. NEXT is the A003 arbitrary-core posterior/terminal ledger because it directly exposes the universal unpaid expectation and uses completed B01 work, rather than rebuilding class calibrations.
