# Literature audit for the erasure form of FEI

FEIB15, 10 November 2026. This extends FEIB11/LITERATURE.md. All sources linked below were opened during this task; `sources_*.json` preserves the returned passages and failed searches. A negative search is limited to those passages and terms. Mathematical restatements below use sign-valued functions and base-2 entropy. Quoted theorem formulas are distinguished from our restatements.

## 1. Is the criterion already known?

Verdict: KNOWN in algebraic form. The relevant paper is not among the older papers listed in the brief. María José González, Paul MacManus, and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (2026), arXiv:2606.00246v2, Corollary 4.2 and equation (22), gives exactly the good-coordinate erasure criterion. Its Appendix B, equation (32), gives exactly the restriction decrement split. [Primary HTML](https://arxiv.org/html/2606.00246v2), [primary PDF](https://arxiv.org/pdf/2606.00246v2), printed pp. 16–17 and 27–28.

The complete short statement of Corollary 4.2 is:

> We can replace hypothesis (ii) in Ansatz 1.1 and Ansatz 1.2 (appropriately adapted to the branching nodes) by (22).

To identify the quantity, write u_T=fhat+(T), v_T=fhat-(T). Their equation (22) has left side

    sum_T ((u_T^2+v_T^2)/2) h((u_T-v_T)^2/[2(u_T^2+v_T^2)]).

Substitute u=a+b and v=a-b. This is exactly E_i=H(1[i in U] | U-i), with no factor left over. Ansatz 1.1 selects a splitting coordinate depending on f and inducts within a restriction-closed class. Ansatz 1.2 allows stopping trees. Appendix B equation (32) is D_i=E_i+J_i in the notation of FLOW; the authors bound J_i by a constant times influence, and explicitly allow a change of constants in the equivalence. Thus neither the good-coordinate algebra nor the restriction induction should be presented as new. The paper does not call E_i erasure entropy in the passages inspected. Its sufficient stopping-tree statement and the existence criterion are already there. Our proof in PROOFS.md supplies the necessity from FEI and the summed criterion, with the sharper additive 2/ln 2 comparison. I did not locate an earlier statement of the summed criterion or this sharp constant; that limited absence is NOT a novelty claim.

The named-paper concordance follows. Each verdict concerns this specific equivalence, not whether the cited paper proves FEI for useful classes. Short exact quotations are followed by restatements where needed.

| Authors, title, year; exact location | Short statement quotation / exact theorem formula | Verdict for the erasure criterion |
|---|---|---|
| Andrew Wan, John Wright, Chenggang Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*, preprint 2013 / ITCS 2014, Theorem 1.1 | “Then H[X ] ≤ 9k · Inf[f].” Assumptions: f is computed by a read-k decision tree, X is its spectral sample. | PARTLY KNOWN: restriction spectra and tree methods are ingredients. Proposition 2.3 describes the restriction mixture. No general erasure criterion located. Theorem 1.2 separately requires I>=1 and gives H<=12dI for expected tree depth d. [PDF](https://www.cs.cmu.edu/~jswright/papers/readk.pdf) |
| Ryan O’Donnell, John Wright, Yuan Zhou, *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*, ICALP 2011, Theorem 1 | “The FEI Conjecture holds for symmetric functions, with C = 12.04.” | PARTLY KNOWN: Theorem 3 uses induction for read-once decision trees; Theorem 5 bounds spectral level entropy by 3I. No general good-coordinate erasure statement located. [PDF](https://www.cs.cmu.edu/~odonnell/papers/fei.pdf) |
| Sourav Chakraborty, Raghav Kulkarni, Satyanarayana V. Lokam, Nitin Saurabh, *Upper Bounds on Fourier Entropy*, ECCC 2013 revision 2 / journal 2016, Theorem 5.11 | Exact concluding formula: “H(f) ≤ 10 Inf(f) + κ(p).” Assumptions: read-once AND/OR/XOR/NOT formula. | PARTLY KNOWN: composition induction and complexity bounds; no erasure equivalence located. Remark 5.1 has κ(p)<=0. The author list here follows the actual paper. [ECCC PDF](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/) |
| Esty Kelman, Guy Kindler, Noam Lifshitz, Dor Minzer, Muli Safra, *Towards a Proof of the Fourier–Entropy Conjecture?*, 2020, Theorem 1.3 | Exact displayed bound: “H[\widehat{f^{≤D}}] ≤ K∑_{|S|≤D}|S|log(|S|+1)\widehat f(S)^2 + K I[f].” | NOT FOUND: erasure or good-coordinate equivalence. This is a weighted vertex entropy bound; see item 4. [arXiv v2](https://arxiv.org/html/1911.10579v2) |
| Parikshit Gopalan, Rocco A. Servedio, Avishay Tal, Avi Wigderson, *Degree and Sensitivity: tails of two distributions*, arXiv 2016, Theorem 6.7 in the opened four-author PDF | “H[f] ≤ I[f] · (2 log s[f] + O(1)).” | NOT FOUND: erasure equivalence. This involves maximum sensitivity s, not average sensitivity I inside the logarithm. Some earlier hosted versions have only three authors; this citation uses the four-author arXiv text. [PDF](https://arxiv.org/pdf/1604.07432) |
| Bireswar Das, Manjish Pal, Vijay Visavaliya, *The Entropy Influence Conjecture Revisited*, 2011, Theorem 1 | “A random function satisfies the FEI conjecture with high probability with C = 2 + δ, for any constant δ > 0.” | NOT FOUND: the equivalence. This is a random-function result. [PDF](https://arxiv.org/pdf/1110.4301) |
| Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, 2018 / arXiv v2 2019, Theorem 3 | Exact concluding implication: “Then FEI holds for all Boolean functions.” Assumption: FEI for all functions with I<=2^{-s(n)}, s(n)=o(n). | PARTLY KNOWN: important warning that low-influence restrictions need not be easier. Theorems 6 and 9 concern bounded spectral norm and read-k trees. No erasure equivalence or theorem literally about low rank was located in this text. [HTML](https://arxiv.org/html/1806.03646) |
| Srinivasan Arunachalam, Sourav Chakraborty, Michal Koucký, Nitin Saurabh, Ronald de Wolf, *Improved Bounds on Fourier Entropy and Min-entropy*, TOCT 2021, Theorem 1.6 | “H(\hat f²) ≤ 2 · aUC⊕(f).” | NOT FOUND: erasure equivalence. Average unambiguous parity certificates control Shannon entropy. Theorem 1.8 concerns min-entropy; it cannot be substituted for Shannon entropy or erasure entropy. [Journal author PDF](https://www.isical.ac.in/~sourav/papers/TOCT21.pdf) |
| Nathan Keller, Elchanan Mossel, Tomer Schlank, *A Note on the Entropy/Influence Conjecture*, preprint 2011 / publication 2012, Proposition 3.1 | “In particular, Ent_{1/2}(f) ≤ 2k.” Assumptions there: integer-valued function with Fourier support in levels <=k. | NOT FOUND: erasure equivalence. Granularity and strong tail hypotheses differ from a general mean-degree bound. [HTML](https://arxiv.org/html/1105.2651) |
| Rani Hod, *Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions*, 2017, Theorem 4.4 | “Any constant C in Conjecture 1.1 satisfies C≥β(1/2)>6.4547837, even when restricted to monotone functions.” | NOT FOUND: erasure equivalence. This is a lower bound through composition. [HTML](https://arxiv.org/html/1711.00762) |

Literal searches for `erasure` in these sources found none relevant; KKLMS mentions erasure channels in a coding application. Absence of the word does not establish absence of a mathematically equivalent idea. That is why the González–MacManus–Pereyra formulas are compared explicitly above.

## 2. General bounds and the lower-bound record

Verdict: the general full-entropy bound H<=O(I log(I+2)) is NOT a consequence of KKLMS and is not an established intermediate theorem in the sources checked. In fact a uniform bound of this form would imply FEI itself; PROOFS.md proves a selector reduction. The same warning applies to a putative H^-<=O(I²+I), even under constant variance. Pure H^-<=CI² for all Boolean functions is false as I tends to zero.

The precise general bounds checked here are:

* The elementary entropy bound H^-<=H<=sum_i h(Inf_i)<=I log2(e n/I). It holds for every subset law, without Boolean structure.
* KKLMS Theorem 1.3: H_{<=D}<=K∑_{|S|<=D}|S|log(|S|+1)mu(S)+KI. At D=degree(f), this gives the full-entropy bound with a log(degree+1) loss. At D=O(I/v), v=Var(f), it bounds only the truncated entropy by O(I log(2+I/v)). Theorems 1.1 and 1.2 give a large nonempty coefficient and concentration at the normalized scale (I/v)log(1+I/v), not a full Shannon-entropy bound at that scale.
* Gopalan–Servedio–Tal–Wigderson Theorem 6.7 gives H<=I(2log s+O(1)). This and the KKLMS weighted-moment estimate are useful incomparable parameter bounds; there is no single bound called best across every parameter regime.
* Xiao Han, *A new bound for the Fourier-Entropy-Influence conjecture*, arXiv:2312.08271 (2023, revised 2025), Theorem 1, displays H<c1 I+c2∑_i Inf_i log(1/Inf_i). This is an influence-profile bound, not I log I. [Primary text](https://arxiv.org/html/2312.08271). The later Li–Han paper arXiv:2512.03117 is withdrawn in its current version and is not used. [Withdrawal notice](https://arxiv.org/abs/2512.03117).
* Manaswi Paraashar and Nitin Saurabh, *Fourier Entropy Bounds via Approximations*, arXiv:2611.06451v1 (4 November 2026), gives entropy bounds through approximate spectral norm, parity query complexity, and conical representations. Its introduction still gives the KKLMS weighted-degree moment as the general influence-related bound. It does not state H=O(I log I). [Primary text](https://arxiv.org/html/2611.06451v1).

The checked public constant record is >6.521845710923046575, with no higher record found in the searches. Its primary artifact is the [C71 record and certificate links](https://teorth.github.io/optimizationproblems/constants/71a.html), entry Num2026 (2026), not a numbered paper theorem. The page attributes 6.278 to O’Donnell–Tan (2013); Hod’s Theorem 4.4 improves that to >6.4547837. The current record is already stronger than both.

Our independent reconstruction from the PM(K3,3)+nine-coins description gives I=261/128 and H=6.7766053090059780825 bits, hence H/(I-1)=6.5218457109230465756581 (75-digit arithmetic; `audit.json`). This reproduces the numerical construction, not a hash comparison with the public truth table and not an interval certificate. Its amplification is proved in PROOFS.md. The public record page separately reports an exact-rational/interval certificate. We found no newer improvement, but did not certify exhaustiveness of the world's literature.

## 3. Erasure entropy, pseudo-likelihood, and structural hypotheses

Verdict: the information quantity is standard; the listed negative-dependence/log-concavity hypotheses alone CANNOT give a universal H^-<=C E|U|. This failure has a direct product-law counterexample, so it is stronger than a negative literature search.

Sergio Verdú and Tsachy Weissman, *The Information Lost in Erasures*, IEEE Transactions on Information Theory 54(11), 5030–5058 (2008), Definition 1 and Theorem 1, define the sum of individual conditional entropies and bound it by joint entropy. The abstract describes it as the “sum of entropies of the individual variables conditioned on all the rest.” [Primary PDF](https://web.stanford.edu/~tsachy/pdf_files/The%20Information%20Lost%20in%20Erasures.pdf). Their earlier ISIT 2006 contribution is titled *Erasure Entropy*; the full 2008 text is the one inspected here. Some displayed formulas in this scanned extraction were not machine-readable; the chain-rule proof of the inequality is supplied independently in PROOFS.md.

For a law pi of X, define PL_pi(x)=prod_i pi(x_i | x_{-i}). Then H^-(pi)=E_pi[-log2 PL_pi(X)] directly. For a trial law rho the same expected loss is H^-(pi)+∑_i E_pi D(pi(X_i|X_-i)||rho(X_i|X_-i)). This is an exact conditional cross-entropy identity; the product need not normalize to a joint law. Julian Besag, *Statistical Analysis of Non-Lattice Data*, The Statistician 24(3), 179–195 (1975), is a primary pseudo-likelihood reference. [Opened scan](https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf). Its body is image-only in the returned extraction, so no theorem/equation number or quotation from its body is claimed VERIFIED. The identity here is proved from the definition, independently of that historical attribution.

Julius Borcea, Petter Brändén, Thomas M. Liggett, *Negative Dependence and the Geometry of Polynomials*, JAMS 22 (2009), 521–567, Theorem 4.9: “If μ∈P_n is strongly Rayleigh then it is CNA+.” Proposition 3.5 says positive-contraction determinantal laws are strongly Rayleigh. [Primary text](https://arxiv.org/html/0707.2340).

Independent Bernoulli(p) bits have H^-/E|U|=h(p)/p, which diverges as p decreases to zero. They are negatively associated, strongly Rayleigh (a product of stable affine factors), positive-contraction determinantal (kernel p Id), log-submodular with equality, and log-concave in their generating polynomial. Their binomial rank sequence is ultra-log-concave. Thus none of these assumptions alone supplies the desired absolute constant. A lower bound on nonzero marginals would yield a constant by the elementary entropy estimate, but is an additional assumption. For any fixed-cardinality law, H^-=0 because the erased membership is determined by all other memberships. PROOFS.md gives both proofs. No applicable published inequality overcoming the product-law obstruction was found in searches combining erasure entropy with negative association, Rayleigh, and determinantal terminology.

### Exact census and certificates

`census.py` checks every truth table through n=4. Spectral weights are integer Walsh sums squared divided by 4^n. NA checks every pair of increasing indicator events on disjoint blocks; layer cake makes this the full definition, not just pairwise negative correlation. Global log-submodularity means mu(A)mu(B)>=mu(A intersection B)mu(A union B) for ALL A,B, including zeros. Rank log-concavity/ULC include the no-internal-zero condition; these are rank-sequence properties, not a certification of every multivariate notion of log-concavity.

| n | Boolean functions | NA | pairwise NC | global log-submodular | rank log-concave | rank ULC | positive-contraction DPP / strongly Rayleigh |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| 2 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| 3 | 256 | 88 | 104 | 88 | 112 | 88 | 88 |
| 4 | 65,536 | 2,104 | 6,168 | 3,544 | 21,528 | 10,776 | 2,104 |

Sources: `census.json`, `structural.json`, `dpp_certificates.json`. The last column is certified, not inferred from a finite stability grid: `certify_dpp.py` constructs rational kernels for every NA spectrum type, checks det(Id-K+K diag(z)) against the exact generating polynomial, and checks all principal minors of K and Id-K. Conversely DPP/strong Rayleigh implies NA by the cited theorem. There are 14 NA spectrum types modulo coordinate permutations at n=4. All are DPPs; this is a finite-census observation only.

`logsub_catalog.csv` answers which functions are log-submodular: it lists every spectrum type, a representative truth-table integer, its multiplicity, and exact canonical coefficients. The `.npz` files give the complete classification for each truth table. At n=4 there are 19 log-submodular spectrum types, and 1,440 log-submodular functions fail NA. All NA samples here are log-submodular. These coincidences are not asserted at larger n. Among the 168 monotone truth tables on four bits, exactly 18 are NA/log-submodular; all 18 have product spectra. `census.json` records the monotone convention.

Concrete witnesses use bit x of table t equal to 1 when f(x)=-1:

* Table 27 on three bits has mu supported uniformly on masks {2,3,4,5}. Its generating polynomial is (1+z1)(z2+z3)/4. It is a nonproduct DPP/NA example.
* Table 23 on three bits is majority up to output/input convention. Its sample is uniform on {1,2,4,7}. Inclusion bits are pairwise independent, but Cov(X1, X2 X3)=1/8>0. Thus it is not NA, strongly Rayleigh, or a positive-contraction DPP. Its rank sequence has an internal zero.
* Table 1 on three bits is AND up to conventions. mu(empty)=9/16 and all other masses are 1/16. Cov(X1,X2)=1/16>0, and the log-submodular inequality for {1},{2} fails. So these structural hypotheses fail even for a monotone Boolean function.

`audit.py` independently uses dense integer character sums on the complete census and finds zero discrepancy with the Walsh census weights. It also checks selector identities and the PM record. The strongest observed H^-/I through four variables is 2.704153205629417 bits per unit influence, at n=4 table 19. This is not a claim about the FEI constant.

The brain helped locate prior FEI audit scars and the record construction. The math recall store was absent. No shared memory was written because fleet RULES.md confines writes to this folder.
