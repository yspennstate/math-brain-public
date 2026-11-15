MINOR

1. **Underqualified description of the classical variational theorem — `main.tex:105–108`.** Liu–Röckner, Theorem 4.1, does not obtain existence from quadratic coercivity alone: it assumes (A1)–(A4), including hemicontinuity, monotonicity and growth, and square-integrable initial data. The manuscript's phrase “quadratic coercivity yields the energy class” should name that context explicitly. This is an introductory qualification, not a gap in Theorem 2.3 or Corollary 6.1, which use the appropriate local theory and linear assumptions. Replace those sentences with:

   ```latex
   In the classical variational framework of Krylov--Rozovskii \cite{KR},
   as formulated in Liu--R\"ockner \cite{LR}, Theorem~4.1 (arXiv version,
   p.~17), hemicontinuity, monotonicity, coercivity and growth give the
   energy class for square-integrable initial data when the coercivity
   exponent is $2$. The exponent $p$ in \cite{LR}, Theorem~1.1, controls
   moments; the time-integrability exponent of the variational norm there
   is the coercivity exponent $\alpha$.
   ```

2. **Unstated pagination convention — `main.tex:69–73`, and subsequent page references to `Survey`.** The bibliography gives both the published survey and arXiv:2501.18561v5, whose pagination differs substantially. The manuscript's page references are correct for the published NoDEA version: for example, Problem 6 is on published p. 130, but arXiv v5 p. 92. Thus these are not incorrect theorem numbers or incorrect published page numbers; the ambiguity is which version the reader should open. Add this sentence at the first survey citation:

   ```latex
   Unless another version is specified, page references to \cite{Survey}
   refer to the published NoDEA version.
   ```

3. **Distinguish a continuation method from a direct application of its earlier theorem — `main.tex:100–101`.** Part II, Theorem 4.15, is the right antecedent for the small-linear-growth method. Its statement assumes a growth estimate for every small parameter on all finite horizons; the manuscript chooses a cutoff and one sufficiently small coefficient for a fixed horizon, and proves continuation directly using the survey's Theorem 5.1(1). Part II itself explains that its proof only needs a sufficiently small fixed coefficient, so there is no mathematical conflict. Nevertheless, “the ... principle used below” leaves the exact dependency unnecessarily unclear. Replace that sentence with:

   ```latex
   The fixed-horizon cutoff continuation argument below follows the
   small-linear-growth method of \cite{AVII}, Theorem~4.15, pp.~39--41;
   we prove the required version directly using \cite{Survey},
   Theorem~5.1(1).
   ```

I found no counterexample or load-bearing proof gap. Subject to these minor qualifications, Theorem 2.3 and Corollary 6.1 are justified under the hypotheses actually stated. In particular, the proof does not silently assume weighted higher-exponent estimates, preservation of the original polynomial exponents by the cutoff, a uniform bound on the domain norms of the centers, or separability of the whole Hilbert space.

The following records what I verified and how. Line numbers refer to the supplied, unchanged `paper/main.tex`. I read all 822 lines and the text of all ten PDF pages. I consulted no other report about this result.

The setting and the endpoint theorem (`main.tex:115–245`) are sufficient. Hypothesis 2.1 is the autonomous Hilbert specialization of the survey's Assumption 4.1, including its real interpolation norm with second index 1. The equivalence

\[
\rho_j(\beta_j-\tfrac12)+\beta_j\le1
\quad\Longleftrightarrow\quad
(2\beta_j-1)(\rho_j+1)\le1
\]

is correct. The constants (F(0)) and (G(0)) are finite fixed vectors and need no additional moment assumption. Although line 124 only explicitly calls (X_0) Hilbert, the introduction specifies a Hilbert couple and Hypothesis 2.1 supplies an equivalent Hilbert graph norm on (X_1=D(A)). Thus the reference-operator construction has the Hilbert structure it needs. The endpoint bullet hypothesis is explicitly assumed, rather than inferred from higher-exponent estimates. The survey's Theorem 4.7 supplies the stated maximal solution, its localized energy regularity, and uniqueness. Its part (2) supplies initial-event localization; uniqueness on a common lifetime is also part of the solution theory/definition. Initial data are strongly measurable and may have no finite moments.

For **Lemma 3.1** (`main.tex:249–322`), I re-derived the estimate and constants. Write (e=\|w\|_E), (Z=\|w\|_{X_1}), and (a=2\beta-1\in(0,1)). Real reiteration identifies ((E,X_1)_{a,1}=X_{\beta,1}). Splitting its (K)-functional integral at (e/Z) gives

\[
\int_0^\infty t^{-a}\min(e,tZ)\,\frac{dt}{t}
=\left(\frac1{1-a}+\frac1a\right)e^{1-a}Z^a.
\]

This proves (3.2) with the required real interpolation index; replacing it by a mere complex interpolation estimate would not suffice, but the manuscript does not do that. The zero vector is handled separately. Polynomial splitting gives exactly the two types of terms in (3.3). The coefficient (C_N) uses (L_{N+2}) and fixed interpolation/polynomial constants, not the domain norm of (y).

At equality, (a(\rho+1)=1) implies ((1-a)(\rho+1)=\rho>0). Thus the critical term is (D_j(2d)^{\rho_j}Z). Formula (3.6), with zero (D_j)'s omitted as the text instructs, makes their sum at most (eta Z/2). Every remaining exponent of (Z) is strictly less than 1. Independently maximizing (hZ^b-\delta Z) over (Z\ge0) gives the displayed Young constant

\[
(1-b)b^{b/(1-b)}h^{1/(1-b)}\delta^{-b/(1-b)}.
\]

There are at most (2m) such terms, so (delta=eta/(4m)) leaves at most another (eta Z/2). Their additive constants may depend on (\|y\|_{X_1}); this does not affect the radius. The case (ho_j=0) is indeed strictly subcritical. This verifies precisely the independence of the radius needed later, not a stronger assertion about (C_y).

For **Lemma 4.1** (`main.tex:333–403`), the operator (A_*=(ii^*)^{-1/2}) is valid. Here (i) is the bounded dense injective embedding between Hilbert spaces, with its norm normalized if desired. Its polar decomposition shows

\[
\operatorname{Ran}(ii^*)^{1/2}=\operatorname{Ran}i,
\qquad D(A_*)=X_1.
\]

The inverse is a positive self-adjoint, boundedly invertible operator on (X_0), and its domain norm is equivalent to the given (X_1)-norm. This argument also works without separability. The survey's Theorem 3.13 applies to this reference operator and supplies its bullet estimates.

The zero-initial-value rewriting is correct:

\[
dv+A_*v\,dt=[f+(A_*-A)v]\,dt+(Bv+g)\,dW.
\]

Both new forcings have finite (L^q(\Omega\times(s,T))) norms by the assumed ordinary maximal regularity. Reference uniqueness identifies its solution with (v). The estimate is a transfer of regularity after (v) is known to exist; it requires no smallness of (A_*-A) or (B). Uniformity in deterministic interval endpoints follows from the reference bullet estimate and the uniformity explicitly built into (2.4).

For nonzero data, (e(t)=e^{-(t-s)A_*}\xi) is adapted and has the deterministic trace estimate uniformly in (s,T), using the stable half-line reference semigroup. Substitution of (v=e+z) gives the two corrections (f+(A_*-A)e) and (g+Be), with the signs in (4.2). A separate calculation gives

\[
\|v\|_{L^q(X_1)}
\le R_q(1+C_0D)\|\xi\|_{L^q(E_q)}
  +2C_0\mathfrak n_{q,s,T}(f,g).
\]

Consequently the stated (M_{q,T}=1+R_q(1+C_0D)+2C_0) is more than sufficient. The factor 2 in passing from the sum of forcing norms to (mathfrak n) is legitimate. Choosing (1/q<\theta<1/2) permits application of the survey's mixed trace Proposition 2.1 and gives (C([s,T];E_q)). There is no assumption that (A) itself is self-adjoint or has a bounded functional calculus.

For the **cutoff construction and Proposition 4.2** (`main.tex:405–506`), the strict gap (1-1/q>\max_j\beta_j) implies both embeddings (4.5), including the second index 1 in (X_{\beta_j,1}). The original maps extend uniquely from dense (X_1\subset E_q) and are Lipschitz on bounded (E_q)-balls. Multiplying by the trace-ball cutoff preserves this property. On its support Lemma 3.1 applies to (w=x-y), and (\|x-y\|_{X_1}\le\|x\|_{X_1}+\|y\|_{X_1}) gives the stated (K_y). Off its support the maps are constant. Thus (4.7) is a global bound on (X_1).

The new local-theory parameters are valid: take (m'=1), (ho'=0), and (eta'\in(1-1/q,1)). The embedding (X_{\beta',1}\hookrightarrow E_q) converts local Lipschitz continuity on (E_q) into the survey's required difference estimate. Condition (4.4a) of the survey reduces to (eta'\le1), strictly satisfied. All other linear/sectorial hypotheses are unchanged, with the bullet property supplied by Lemma 4.1. It is therefore legitimate to apply Theorem 4.7 to these cutoffs; there is no need to verify their original critical exponents at exponent (q).

The stopped continuation is also sound. Further stopping at the (n)-level of the accumulated (X_1)-norm gives (Y_n^q\le n) almost surely, so the norms used before absorption are finite. The killed forcings are progressive and have finite joint probability-time (L^q) norms. Solving the linear equation on the full deterministic horizon, and then using stopped uniqueness, avoids any assumption about higher-order time regularity on a random terminal interval. Minkowski gives

\[
Y_n\le M_{q,T}(\|\xi\|_{L^q(E_q)}+\eta Y_n+K_yT^{1/q}).
\]

The choice (M_{q,T}\eta\le1/2) permits absorption. Monotone convergence yields the finite bound through (	au\wedge T). The final killed-forcing linear solution has a continuous (E_q) trace through that time, so a trace limit exists on the whole event ({\tau\le T}), including ({\tau=T}). The survey's Theorem 5.1(1) applies to this maximal cutoff solution with the local parameters just verified. It excludes that event. This proves continuation to the chosen horizon, without making an infinite-horizon assertion for a cutoff with one fixed radius. The finite-horizon formulation is essential and is respected.

For **Lemma 5.1** (`main.tex:513–541`), the progressive (X_1)-valued representatives on the countably many localized intervals permit Fubini. At almost every deterministic (s), the trace agrees almost surely, on ({s<\sigma}), with an (\mathcal F_s)-measurable (X_1)-valued variable. A full Lebesgue measure set contains a deterministic countable dense subset. One cannot simply substitute all rational times for this set, and the manuscript correctly does not do so. Taking the union of the countably many exceptional null sets for the selected times gives the simultaneous versions needed in the covering argument.

The claimed progressive representatives do not conceal a separability assumption: with the Hilbert graph norm, bounded resolvent regularizations of (A) recover the graph-valued map from the (X_0)-valued progressive version wherever it belongs to (D(A)). Strong measurability is then preserved by passage to the limit and by restriction to the localized intervals.

For the centers, each strongly measurable rational-time (E)-valued variable has an essentially separable range. Their countable union lies in one deterministic closed separable subspace (E_*). Outside one null set, trace continuity places all lifetime path values in (E_*). Approximating a countable dense subset of (E_*) by domain vectors in (E) is sufficient. The domain vectors need not lie in (E_*). This last point correctly avoids assuming that (X_1\cap E_*) is dense in (E_*).

For **Lemma 5.2** (`main.tex:543–588`), (Gamma_{s,k,q}) is an initial-sigma-field event because (U_s) has the strongly measurable (X_1)-version and (X_1\hookrightarrow E_q) continuously. The truncated data have (L^q(\Omega;E_q)) norm at most (k). The additional initial-ball event is also (\mathcal F_s)-measurable. Stopped exits of adapted continuous traces are stopping times; localization before the lifetime and capping by the lifetime give exactly the stated conventions.

On any finite comparison interval, the higher-(q) solution and its forcings belong to the endpoint (L^2) class, and (E_q\hookrightarrow E). Thus endpoint uniqueness applies after intersecting the two localizing sequences and restricting to the initial event. Event restriction can, equivalently, be implemented by pasting in the endpoint solution with the truncated initial data on the complementary event. No comparison of solutions in incompatible uniqueness classes is being made. Equality extends to an exit strictly inside the common lifetime by trace continuity.

For **Proposition 5.3** (`main.tex:590–632`), all auxiliary choices are countable: the given sequence of (q)'s, (s\in D), integer (k,N,T), and (y\in\mathcal Y). Null sets can therefore be removed before choosing the sample point and time. The radius is fixed before choosing the approximating domain center and is independent of that center's domain norm. This permits a center within (d/4) of any given path value. Continuity provides the whole interval ([s,b]) within distance (d/2), and a deterministic good restart (s<t<b). Some finite (k) contains that sample's domain-valued restart datum. A cutoff exit before or at (b) would contradict equality at the exit and the strict (d/2) bound for (u). This proves local higher-(q) regularity at every positive lifetime time. Finite subcovers and smooth partitions of unity give regularity on each compact interval. The proof requires neither a uniform (K_y) nor an uncountable intersection of probability-one events.

For the **conclusion of Theorem 2.3** (`main.tex:636–683`), the stated complex interpolation identity preserves the exact spatial exponent. The reference scale satisfies (X_\delta=D(A_*^\delta)) with equivalent norms. The time Bessel multiplier and (A_*) commute, and their imaginary powers are bounded on the relevant Hilbert-valued (L^q) spaces. Interpolating the mixed domains, or constructing the interpolation family with these two commuting powers, gives

\[
[L^q(\mathbb R;X_1),H^{\theta_n,q}(\mathbb R;X_{1-\theta_n})]_\lambda
=H^{\lambda\theta_n,q}(\mathbb R;X_{1-\lambda\theta_n}).
\]

The spatial exponent is (1-\theta), not a shifted or weakened exponent. Compactly supported cutoffs justify extension by zero without a boundary trace issue. Interpolation between (L^q\hookrightarrow L^r) and (W^{1,q}\hookrightarrow W^{1,r}) on bounded intervals gives the asserted lowering of integrability for the Hilbert target spaces in use. An unbounded sequence of (q)'s suffices; intermediate-exponent linear estimates are not assumed or needed. For the Hölder conclusion choose (1/q<\varepsilon<\theta). The Sobolev embedding then gives the exponent (	heta-\varepsilon). Equality with the original trace representative follows from continuity in (X_0). All these deductions are deterministic on the one event already selected, so the universal quantifiers over real (r,\theta,\varepsilon) introduce no further null sets.

For **Corollary 6.1** (`main.tex:685–706`), the survey's Assumption 6.1 gives exactly the nonlinear estimate on the couple ((V^*,V)), with (E=H), and supplies coercivity of the linear pair. The critical variational paper's Lemma 4.1 gives the endpoint (L^2(\Omega;C(H))\cap L^2(\Omega\times(0,T);V)) estimate. Killing forcings and using uniqueness supplies the stopped version; constants can be chosen uniformly in starting times on a bounded horizon, as explained after that lemma. Coercivity also gives the sectorial realization on (V^*) and equivalent domain norm, as stated after the survey's Assumption 6.1. The extra higher-(q) assumption remains explicit. Thus this is a valid specialization of Theorem 2.3, not a derivation of arbitrary higher-exponent maximal regularity from endpoint coercivity.

I checked every explicit source locator used in the mathematical text:

| Manuscript lines | Cited statement and correct location | Check |
|---|---|---|
| 69–77, 209–211, 242–245, 710–714 | Survey, Theorem 5.7, published pp. 59–60, and (5.21) | Requires initial (p>2), the larger-ball growth estimate, and bullet estimates for every admissible larger exponent/weight. The manuscript accurately describes these and proves a different endpoint extension. |
| 72–73, 159–176 | Survey, Problem 6, p. 130; (6.1), p. 65 | The problem specifically includes equality in the critical Hilbert case. The displayed critical relation agrees. |
| 86–90 | Survey, (5.5) and discussion, pp. 51–52 | A small positive power of the trace difference multiplies the top spatial norm and is absorbed. The manuscript correctly attributes that mechanism, while proving its own fixed-domain-center version. The survey does not literally state Lemma 3.1. |
| 96–98 | Part I, Theorems 4.7 and 4.8, arXiv v5 pp. 30–31 and p. 31 | These are the quasilinear (L^0) and semilinear local results; background attribution is accurate. The main proof correctly uses the survey's later real-interpolation formulation. |
| 98–101 | Part II, Proposition 6.8, published pp. 76–80; Theorem 4.15, pp. 39–41 | Shifted regularization and small-linear-growth continuation respectively. See correction 3 concerning the latter's role. |
| 102–104 | Portal–Veraar, Theorem 5.3, pp. 572–573 | Explicitly includes (p=q=2,\alpha=0), with its spatially independent coefficients and other coefficient/nonlinearity hypotheses. The manuscript restricts its descriptive claim to that coefficient setting. |
| 105–108 | Liu–Röckner, Theorem 4.1, arXiv p. 17; Theorem 1.1, pp. 4–5 | Theorem numbers and page locator agree. Correction 1 supplies the omitted classical assumptions in the prose. The distinction between moment and variational time exponents is correct. |
| 109–111, 702–705 | Critical variational paper, Theorem 3.3, pp. 968–969; Lemma 4.1, p. 972 | Local critical energy theory and the coercive linear endpoint estimate respectively. |
| 165–173, 453–458 | Survey, Assumption 4.1 and (4.4a), pp. 38–39 | Both original endpoint parameters and replacement cutoff parameters satisfy the actual stated conditions. |
| 180–201 | Survey, Definitions 3.7–3.8, pp. 27–28 | The stopped ordinary estimate and deterministic-interval bullet estimates, including endpoint continuity, have the stated quantifiers. |
| 215–225, 453–458, 581–587 | Survey, Theorem 4.7, pp. 42–43 | Local existence, regularity and initial-event localization used within their stated scope. |
| 262–277 | Survey, Lemma 4.3, pp. 40–41 | Correct relation to the critical interpolation mechanism; the manuscript additionally proves the needed pointwise inequality. |
| 349–355, 730–731 | Survey, Theorem 3.13, pp. 31–33; Portal–Veraar, Theorem 3.9, pp. 556–557 | The Hilbert analytic-generator theorem and the reference-operator method support the uses made here. The paper does not invoke Portal–Veraar's theorem for a general nonzero (B) without its hypotheses. |
| 372–374 | Survey, Proposition 2.1, p. 18 | Mixed trace embedding with (	heta>1/q), as required here. |
| 400–402 | Part I, Proposition 3.10, arXiv pp. 22–23; Part II, Proposition 3.9, published pp. 21–23 | Both use a deterministic trace extension and the drift and noise corrections for nonzero initial data. |
| 496–502 | Survey, Theorem 5.1(1), p. 48 | A maximal solution cannot have a finite lifetime with a limit in its trace space. Applies to the cutoff with the new local parameters; it is not being applied merely from a bound in an unrelated norm. |
| 685–705 | Survey, Assumption 6.1 and following discussion, pp. 64–65 | Coercivity and the critical nonlinear conditions, including the sectorial realization. |
| 720–724 | Threshold note, Theorems 1 and 3, published pp. 372 and 374 | Correct statements and page numbers; no contradiction with the mixed space-time conclusion. |

On novelty and the suggested shifted-couple objection, I did not find this endpoint theorem in the supplied literature. The survey's Theorem 5.7 requires a starting exponent strictly above 2. Matching the endpoint trace on the same couple would require ((1+\alpha)/r=1/2), which is the excluded weight endpoint. Its Proposition 5.9 instead assumes strictly sublinear domain growth on trace balls and some extra initial spatial regularity. Those are not consequences of the critical equality allowed here.

Part II, Proposition 6.8, explicitly requires (p>2) when its spatial shift is zero. At (p=2) its identity is

\[
\frac12=\frac{1+\alpha}{r}+\delta,
\qquad \delta>0.
\]

Its immediate conclusion is regularity in (X_{1-\delta-\theta}). It additionally assumes local theory, linear maximal regularity and compatibility on the shifted couple, and its larger-ball growth condition (6.22). The present hypotheses do not supply all these. In particular a bounded map (B:X_1\to\gamma(U,X_{1/2})) need not extend to the corresponding lower spatial domains. Even if the shifted estimates were available, the spatially shifted conclusion alone would not prove the original-domain (L^r_{\mathrm{loc}}(X_1)) assertion at (	heta=0). Shifting upward instead would demand stronger range regularity of the coefficients, which is also not assumed. Thus a shift is not an immediate proof under the assumptions of this manuscript.

There is a source-level sign typo worth distinguishing from a manuscript error: the survey's Remark 5.8(1) writes a positive downward shift with the opposite sign, ((1+\alpha)/r-1/2>0), although the admissible weights make that expression negative. The discussion before Theorem 5.6 and Part II's actual parameter identity give the correct sign displayed above. The manuscript's explanation at lines 74–77 and 98–100 is consistent with the correct identity and does not import that typo.

The supplied Navier–Stokes paper carries out model-specific bootstrap arguments with estimates on additional spatial scales. The two reaction-diffusion texts state their abstract temporal regularization theorem as Theorem 4.8 with starting (p>2); their range-shifted hypotheses are further structure. The singular-times text's Lemma 3.11 assumes the relevant instantaneous regularization in (3.13) and transfers it to the process being studied. None states the arbitrary-critical-nonlinearity, original-Hilbert-couple result proved here with only the stated sequence of ordinary higher-(q) estimates. This establishes a distinction from those sources; it is not a claim to have classified all SPDE literature.

The threshold note is compatible with the result for a concrete reason. In a positive self-adjoint variational model on the pivot space (H), write (V=D(\Lambda^{1/2})). Then

\[
X_{1-\theta}=[V^*,V]_{1-\theta}
=D(\Lambda^{1/2-\theta})
\]

with the usual scale interpretation. The threshold theorem obstructs positive time smoothness with target (V=D(\Lambda^{1/2})), unless the noise has additional spatial smoothness. The present theorem permits positive time smoothness only in the rougher target (D(\Lambda^{1/2-\theta})). At target (V), its assertion is solely (L^r) integrability, with (	heta=0). Arbitrarily large finite time integrability does not imply fractional time smoothness in the same spatial domain. The threshold note therefore provides no counterexample.

All eight mathematical bibliography entries (`main.tex:772–813`) have correct authors, titles, publication years, volumes, page ranges or article numbers, DOIs and arXiv identifiers. Title capitalization and the punctuation separating Part II from its subtitle are harmless. I checked the source title pages and journal metadata and used the following external primary records where needed:

| Key | Verified publication data | External record |
|---|---|---|
| Survey | Agresti–Veraar; NoDEA **32** (2025), no. 6, article 123, 150 pages; arXiv:2501.18561v5 | [Publisher](https://link.springer.com/article/10.1007/s00030-025-01090-2); [journal issue metadata](https://research.tudelft.nl/en/publications/nonlinear-spdes-and-maximal-regularity-an-extended-survey/) |
| AVI | Agresti–Veraar; Nonlinearity **35** (2022), no. 8, 4100–4210; DOI 10.1088/1361-6544/abd613; arXiv:2001.00512v5 | [Published article at the authors' institution](https://research-explorer.ista.ac.at/download/11701/11715/2022_Nonlinearity_Agresti.pdf); [version record](https://arxiv.org/abs/2001.00512v5) |
| AVII | Agresti–Veraar; J. Evol. Equ. **22** (2022), no. 2, article 56, 96 pages; arXiv:2012.04448v4 | [Publisher](https://link.springer.com/article/10.1007/s00028-022-00786-7); [version record](https://arxiv.org/abs/2012.04448) |
| CV | Agresti–Veraar; PTRF **188** (2024), 957–1015; arXiv:2206.00230 | [Publisher/DOI](https://doi.org/10.1007/s00440-023-01249-x); [arXiv](https://arxiv.org/abs/2206.00230) |
| Threshold | Agresti–M. C. Veraar; C. R. Math. **364** (2026), 371–379; DOI 10.5802/crmath.833; arXiv:2509.07803 | [Author institutional record](https://research.tudelft.nl/en/publications/a-note-on-a-threshold-for-temporal-regularity-of-stochastic-pdes/); [arXiv](https://arxiv.org/abs/2509.07803) |
| KR | N. V. Krylov–B. L. Rozovskii; J. Soviet Math. **16** (1981), 1233–1277; Russian original **14** (1979), 71–146; DOI 10.1007/BF01084893 | [MathNet original and translation record](https://www.mathnet.ru/php/archive.phtml?jrnid=intd&option_lang=eng&paperid=39&wshow=paper); [Krylov's institutional publication record](https://experts.umn.edu/en/publications/stochastic-evolution-equations/) |
| LR | Wei Liu–Michael Röckner; JFA **259** (2010), 2902–2922; DOI 10.1016/j.jfa.2010.05.012; arXiv:1005.0632 | [Publisher](https://www.sciencedirect.com/science/article/pii/S0022123610002247); [arXiv](https://arxiv.org/abs/1005.0632) |
| PV | Pierre Portal–Mark Veraar; Stoch. Partial Differ. Equ. Anal. Comput. **7** (2019), 541–597; arXiv:1810.01183 | [Publisher](https://link.springer.com/article/10.1007/s40072-019-00134-w); [arXiv](https://arxiv.org/abs/1810.01183) |

For presentation, all 36 internal labels are unique, all internal references resolve, and every citation has a bibliography entry. The PDF has the expected theorem and equation numbers. I found no undefined mathematical symbol that changes an argument. The main theorem asserts neither global existence nor a gain at time zero or at the lifetime, neither unlocalized moments nor the endpoint (	heta=1/2), and neither an unconditional answer based on endpoint coercivity alone. The moment estimate belongs to auxiliary cutoff equations and is not transferred to the original solution. Lines 82–84 and 710–738 state these limitations appropriately.

The requested inventory of writing-process statements is: line 751, and lines 759–761. They are in the protected end matter. I have not treated their assertions about earlier agents or checking as evidence for the mathematics, and I have not established a factual error in them. No alteration of those sections or of the final three bibliography entries is proposed. Private funding and authorship provenance cannot be established by checking the mathematical sources. The public ERC grant identifier in the funding paragraph does correspond to a Horizon Europe project at the Hebrew University, according to [CORDIS](https://cordis.europa.eu/project/id/101041711); this does not independently establish an individual's funding attribution.

No files under `paper/` were edited, and there was no publication, push or upload. Execution details and file hashes are in `LOG.md`.

Task: “Break it if it is wrong” — 13 November 2026, approximately 19:57 +04, the first locally recorded task time.
