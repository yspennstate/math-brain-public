MAJOR

The interval theorem is correct, including uniform conditioning of every subset and the affine-progression extension. The absolute-value obstruction is also correct as a limitation of the specified estimate. The main defect is its claimed relationship to the open problem: the cited source contains no sub-dictionary alternative. Moreover, older character-sum estimates already imply the interval conclusion, and general deterministic column-selection theorems already give tall, almost orthogonal Paley sub-dictionaries of this size. This is a valid structured-support corollary with no demonstrated research novelty, rather than a solution of an alternative in Conjecture 29.

Errors and gaps requiring correction (line locations are in the submitted `claim_files/REPORT.md`):

1. **Unsupported source alternative, line 37.** The assertion that the theorem answers a permitted sub-dictionary alternative is false as an attribution to arXiv:2603.29571v1. Conjecture 29, Entry 12, PDF page 10, and its surrounding text contain no retention exponent or permission to discard columns. The original blog agrees. Fix: remove this assertion and describe a structured special case of the support problem. If a separate task brief authorized another target, identify that brief separately; it does not change the published conjecture.

2. **Incomplete classical comparison, lines 39, 57, 72, 123–145.** Heath-Brown–Pierce is a valid input, but is not necessary here. Burgess's older rationally twisted estimate plus approximation and Abel summation gives the same conclusion. Ordinary untwisted Burgess applied to Fourier-row energy gives a stronger bound. Fix: include these derivations, given below, and describe the theorem as a corollary of established estimates. The report already disclaims novelty priority; this is an incomplete comparison rather than a false explicit priority assertion.

3. **Missing benchmark for tall sub-dictionaries, lines 35–39 and 229–231.** Even if an unrestricted sub-dictionary alternative were added, its conditioning conclusion would already follow from general deterministic selection results, without Paley-specific analysis. Fix: compare with restricted invertibility and almost isometric column selection. Prescribing the consecutive labels is a different assertion from finding some good subset; neither controls arbitrary supports of the full ETF.

I found no additional substantive proof error or incorrect theorem/page citation in the submitted report. Its qualifications about conditional results, the direction discrepancy ⇒ RIP ⇒ clique bounds, and the distinction between the absolute-value bound and the actual condition number are appropriate.

The exact source is Afonso S. Bandeira, Daniil Dmitriev, Kevin Lucca, Petar Nizić-Nikolac and Almut Rödder, *Randomstrasse101: Open Problems of 2025*, [arXiv:2603.29571v1](https://arxiv.org/abs/2603.29571v1), submitted 31 March 2026, 10:52:10 UTC. Its independently retrieved metadata lists only v1. The PDF title date is 1 April 2026; the generated HTML displays 24 August 2026, which is not its submission date. Entry 12 begins on page 9; Conjecture 29 is on page 10. The collection year 2025 is not its arXiv submission year.

The first sentence of Conjecture 29 reads:

> The Paley Equiangular Tight Frame construction satisfies the Restricted Isometry Property beyond the square-root bottleneck.

The next sentence gives precisely this mathematical content: there exists $\varepsilon>0$ such that, for $m\sim p^{1/2+\varepsilon}$, every choice of $m$ distinct Paley ETF columns has condition number bounded independently of $p$. In the notation of the claim, the support quantifier is

$$
\forall S\subseteq\mathbb F_p\cup\{\infty\},\quad
|S|=m\sim p^{1/2+\varepsilon}\quad\Longrightarrow\quad
\kappa_2((\Phi_p)_S)\le C,
$$

with one constant $C$ for the family of primes $p\equiv1\pmod4$. This is the exact mathematical statement, with its full quantifier over supports. There is **no sub-dictionary clause**: the next item is Entry 13. The complete wording is preserved in [the independent full-text extraction](sources/2603.29571v1.txt), page 10, and corroborated by the [original blog entry](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/).

Thus the source has no ambiguous alternative to interpret as tall versus overcomplete. Freely choosing a tall dictionary would replace the problem by a much weaker selection problem already covered by standard results. The prescribed interval assertion itself is not tautological: being tall alone does not make columns almost orthogonal. Its ratio of columns to rows is asymptotic to $2p^{-7/16-\rho}$, and its retained fraction is asymptotic to $p^{-7/16-\rho}$, both tending to zero.

The valid standalone theorem is the following. Fix $0<\rho<1/16$. For each prime $p\equiv1\pmod4$, let $L_p=\lfloor p^{9/16-\rho}\rfloor$, $D_p=\{0,\ldots,L_p-1,\infty\}$, and $\Psi_p=(\Phi_p)_{D_p}$. Then

$$
\|\Psi_p^*\Psi_p-I\|\le C_\rho p^{-\rho/3}+\sqrt{L_p/p}=o(1).
$$

Every subset of $D_p$ therefore has condition number tending uniformly to 1. The same holds with the finite labels replaced by $a+d\{0,\ldots,L_p-1\}$, for $d\in\mathbb F_p^\times$, with the special column optionally included.

Here is the analytic proof audit, retaining the submitted equation numbers.

(a) The finite columns have squared norm $1/p+(p-1)/p=1$. With the Hermitian inner product, the finite off-diagonal Gram entry is

$$
\frac1p+\frac2p\sum_{q\in Q}e(q(i-j)/p).
$$

For nonzero $t$, twice the sum over nonzero squares equals $-1+\chi(t)\tau_p$, where $\tau_p=\sum_x\chi(x)e(x/p)=\sqrt p$ for $p\equiv1\pmod4$. Hence equation (2) is exactly $\chi(i-j)/\sqrt p$, with the positive sign in the stated Fourier convention. The inner product with $e_0$ is $1/\sqrt p$. The diagonal deviation vanishes because $\chi(0)=0$. BFMW §5.3 and BMM equation (3) independently corroborate the normalization. Equivalent sign-switched ETF conventions do not invalidate this explicitly fixed convention.

(b) The finite deviation is $p^{-1/2}T_L$, with $T_{ij}=\chi(i-j)$. Since $\chi(-1)=1$, this is real symmetric. Define

$$
F_L(\theta)=\sum_{|h|<L}\chi(h)e(h\theta),\qquad
P_z(\theta)=\sum_{j<L}z_je(j\theta).
$$

Expansion and integration give exactly

$$
z^*T_Lz=\int_0^1F_L(\theta)|P_z(\theta)|^2\,d\theta.
$$

Parseval and the Hermitian Rayleigh principle yield

$$
\|T_L\|\le\|F_L\|_\infty
\le2\sup_{\theta\in\mathbb R}
\left|\sum_{h=1}^{L-1}\chi(h)e(h\theta)\right|.
$$

The factor 2 is present in the report. This is an upper bound, not equality of a finite Toeplitz norm with its symbol supremum. No positivity of the symbol is assumed.

(c) Heath-Brown–Pierce, [arXiv:1404.1677v1](https://arxiv.org/abs/1404.1677v1), Theorem 1.4, PDF page 5, applies to a nonprincipal character modulo a prime $q$, an arbitrary real linear polynomial $f$, an integer $r\ge2$, any $\eta>0$, and

$$
H<q^{1/2+1/(4(r-1))}.
$$

It bounds the interval sum by

$$
O_{r,\eta}\left(H^{1-1/r}q^{1/(4(r-1))+\eta}\right),
$$

uniformly in the starting point. Phase uniformity is genuine: the constant has only the displayed subscripts, and Section 2, page 7, begins with a supremum over all real polynomial coefficients and all shorter lengths. There is no rationality or Diophantine condition on the slope. Constant phases are included by continuity if “linear” is read as degree exactly one. Immediately before Theorem 1.4 the authors explain that the needed mean-value conjecture is already known for degree 1. This use is unconditional and assumes neither a higher-degree conjecture nor GRH.

(d) With $r=3$, the length ceiling is $p^{5/8}$ and the sum bound is $H^{2/3}p^{1/8+\eta}$. Dividing by $\sqrt p$ gives $O_\eta(L^{2/3}p^{-3/8+\eta})$. The chosen integer $H=L_p-1$ is admissible, since $9/16-\rho<5/8$. If $H=0$, the sum is empty. Taking $\eta=\rho/3$ gives

$$
\frac23\left(\frac9{16}-\rho\right)-\frac38+\frac\rho3=-\frac\rho3.
$$

Floors cause no loss. This arithmetic was also checked with exact fractions.

(e) Adjoining the special column adds the border

$$
B=\begin{pmatrix}0&p^{-1/2}\mathbf1\\p^{-1/2}\mathbf1^T&0\end{pmatrix},
$$

whose nonzero eigenvalues are $\pm\sqrt{L/p}$. The triangle inequality proves exactly (1), with the factor 2 absorbed into $C_\rho$. The border term has exponent $-7/32-\rho/2$. Every subset gives a principal compression, so the singular values lie in $[\sqrt{1-E_p},\sqrt{1+E_p}]$, eventually, where $E_p$ is the bound in (1). The submitted condition bound $\sqrt{(1+E_p)/(1-E_p)}=1+o(1)$ follows uniformly. The range $0<\varepsilon<1/16-\rho$ ensures $p^{1/2+\varepsilon}=o(L_p)$. The example $\rho=1/32$, dictionary exponent $17/32$, sparsity exponent $33/64$ is consistent.

For affine labels, $\chi((a+di)-(a+dj))=\chi(d)\chi(i-j)$. Here $d\ne0$ means nonzero modulo $p$ and $L\le p$, so labels remain distinct even across modular wraparound. The finite deviation changes by a scalar sign; the border estimate remains valid. No additional character-sum uniformity is required.

(f) Pólya–Vinogradov or ordinary completion used alone to estimate the twisted symbol gives $O(\sqrt p\log p)$, hence only $O(\log p)$ after normalization. That does not prove (1). Ordinary Burgess followed by one global partial summation in the original variable is also insufficient: its variation factor $1+|\theta|H$ is not uniformly bounded. Nevertheless, there are two older routes.

First, HBP page 2, equation (1.5), already records Burgess's rationally twisted estimate

$$
\max_{a\bmod p}\left|\sum_{n\le t}\chi(n)e(an/p)\right|
\ll_r t^{1-1/r}p^{1/(4(r-1))}(\log p)^2,\qquad t<p.
$$

The original reference is D. A. Burgess, *Partial Gaussian Sums*, Bull. London Math. Soc. **20** (1988), 589–592, [DOI](https://doi.org/10.1112/blms/20.6.589). HBP abbreviates the title to “Partial Gauss sums.” An independent primary confirmation is Burgess's *Partial Gaussian sums III*, Glasgow Math. J. **34** (1992), 253–261: its first page, equation (2), recalls the estimate uniformly in the integer twist. The 1992 full text was obtained; the paywalled 1988 original was not obtained in full.

For any real $\theta$, choose $a$ with $|\theta-a/p|\le1/(2p)$, modulo integer phases. Abel summation with $e((\theta-a/p)n)$ costs at most $1+2\pi H|\theta-a/p|\le1+\pi H/p=O(1)$. Apply the rational estimate to every prefix $t\le H$. The zero twist can also use ordinary Burgess. Therefore the same estimate holds uniformly for all real slopes in the range needed here. With $r=3$, the finite deviation is

$$
O\left(p^{-2\rho/3}(\log p)^2\right)
=O_\rho(p^{-\rho/3}).
$$

Thus the exact claimed exponent range was already accessible from the 1988 estimate and elementary partial summation.

Second, even mixed Burgess can be avoided. This supplies an independent analytic check and a stronger bound. For $z\in\mathbb C^L$, put

$$
u_n=\sum_{j<L}z_je(-nj/p),\qquad w_n=|u_n|^2.
$$

Fourier inversion of the quadratic character gives

$$
z^*p^{-1/2}T_Lz=\frac1p\sum_{n=0}^{p-1}\chi(n)w_n,
\qquad \sum_n w_n=p\|z\|_2^2.
$$

On the cyclic grid,

$$
\sum_n|w_{n+1}-w_n|
\le2\|u\|_{\ell^2}\|u(\cdot+1)-u\|_{\ell^2}
\le4\pi(L-1)\|z\|_2^2.
$$

Partition the $p$ points into $L$ consecutive blocks of lengths $\lfloor p/L\rfloor$ or $\lceil p/L\rceil$. Let $K=\lceil p/L\rceil$, and let $B_K$ bound character sums on all intervals of length at most $K$. Abel summation on each block costs $B_K$ times its last weight plus its internal variation. The sum of last weights is at most $\sum_n w_n/\lfloor p/L\rfloor$ plus the total variation. Thus, for $L\le p/2$,

$$
\|p^{-1/2}T_L\|\ll\frac Lp B_K.
$$

Ordinary Burgess with parameter 2, stated in HBP page 1, equation (1.2), gives $B_K\ll K^{1/2}p^{3/16}\log p$. Hence

$$
\|p^{-1/2}T_L\|\ll L^{1/2}p^{-5/16}\log p
=O\left(p^{-1/32-\rho/2}\log p\right)
$$

at the submitted length. This is stronger than the submitted finite-block bound. In general, the same argument with parameter $r$ gives $O_r(L^{1/r}p^{-(3r-1)/(4r^2)}\log p)$, yielding almost orthogonal intervals of length $p^\alpha$ for every fixed $\alpha<3/4$, by choosing $r$ sufficiently large. These are deductions supplied by this referee, not quotations of a previously located Paley interval theorem. The Fourier-row identity and variation estimate were checked numerically as well.

The report's absolute-value argument is sound. For any $s$-column support, including the special column,

$$
|G_S-I|=p^{-1/2}(J_s-I_s),\qquad
\big\||G_S-I|\big\|=(s-1)/\sqrt p.
$$

For $s=1$, both sides vanish. The bound prevents certification of $\delta_s<1$ through this nonnegative norm at and beyond $s=1+\sqrt p$. For $s\asymp p^{1/2+\varepsilon}$, it diverges on every support. Removing exceptional supports does not change this bound. The complete-graph density calculation and the two threshold cases in the report are correct. The signed norm need not grow. The equal-magnitude obstruction was already stated in [Mixon's 11 November 2026 announcement](https://dustingmixon.wordpress.com/2026/11/11/explicit-restricted-isometries-well-beyond-the-square-root-bottleneck/). It does not rule out future signed refinements or other methods using additional structure.

The general-selection benchmark further limits the scope. A real realization of the Paley ETF has $\Phi\Phi^T=2I_M$, $\|\Phi\|^2=2$, and $\|\Phi\|_F^2=2M$, hence stable rank $M$. It has a real realization because the displayed Gram matrix is real. Spielman–Srivastava, [arXiv:0911.1114v4](https://arxiv.org/abs/0911.1114v4), Theorem 2, page 2, applied to $v_i=\phi_i/\sqrt2$, its operator $L=I$, and its parameter $1/2$, selects at least $\lfloor M/4\rfloor$ columns with squared least singular value greater than $1/4$. The largest squared singular value is at most 2. Every subset of that selected dictionary therefore has condition at most $\sqrt8$, using a deterministic selection procedure and no Paley character sums.

For convergence to 1, Pierre Youssef, *A note on column subset selection*, [arXiv:1212.0976v2](https://arxiv.org/abs/1212.0976v2), Corollary 1.2, page 2, gives a deterministic selection of at least $\epsilon^2 M/9$ columns with singular values in $[1-\epsilon,1+\epsilon]$. For any prescribed $N=o(M)$, choose $\epsilon=3\sqrt{N/M}$ and keep exactly $N$ of those columns. Every subset has condition at most $(1+\epsilon)/(1-\epsilon)=1+o(1)$. This covers the submitted dictionary size. It does not prescribe interval labels, but it shows that an unrestricted tall alternative of the claimed kind would already be solved constructively.

Every explicit citation in the submitted report was checked against independently obtained full text, and journal information against arXiv metadata, publisher metadata or publisher-deposited Crossref records. The following table records the results. Page numbers mean PDF ordinals unless published pagination is specified.

| Work and bibliographic check | Relevant locations and finding |
|---|---|
| A. S. Bandeira, M. Fickus, D. G. Mixon, P. Wong, *The road to deterministic matrices with the restricted isometry property*, J. Fourier Anal. Appl. **19** (2013), 1123–1149; [1202.1234v2](https://arxiv.org/abs/1202.1234v2) | §5.3 pp.17–20; Theorem 20 p.14; Lemma 22 p.17; Theorem 23 pp.18–19; Conjecture 25 p.20 all match. Full spark and a prime-dependent gap do not settle the uniform question. No interval Burgess theorem found. |
| A. S. Bandeira, D. G. Mixon, J. Moreira, *A conditional construction of restricted isometries*, IMRN **2017**, no.2, 372–381; [1410.6457v1](https://arxiv.org/abs/1410.6457v1) | Theorem 2.3 p.3, proof pp.3–6; Proposition 3.2 p.4. The implication chain and allowed gamma range match. Conditional; not this interval result. |
| S. Satake, *On the restricted isometry property of the Paley matrix*, Linear Algebra Appl. **631** (2021), 35–47; [2011.02907v2](https://arxiv.org/abs/2011.02907v2) | Conjecture 7 p.4; Theorem 10 p.5, proof pp.5–8 match. The discrepancy hypothesis remains conjectural. |
| J. Bourgain, S. J. Dilworth, K. Ford, S. Konyagin, D. Kutzarova, *Explicit constructions of RIP matrices and related problems*, Duke Math. J. **159** (2011), 145–185; [1008.4535v3](https://arxiv.org/abs/1008.4535v3) | Theorem 1 p.3 matches. A different selected quadratic-phase construction, not a full Paley theorem or the stated interval corollary. |
| D. G. Mixon, *Explicit Matrices with the Restricted Isometry Property: Breaking the Square-Root Bottleneck*, in *Compressed Sensing and its Applications: MATHEON Workshop 2013* (2015), 389–417; [1403.3427v1](https://arxiv.org/abs/1403.3427v1) | Theorem 2 pp.14–15; §4.2 pp.18–19; exponent $4.4466\cdot10^{-24}$ match. Publisher confirms 389–417, despite the author's list saying 389–418. No interval theorem found. |
| K. Ford, D. Kutzarova, G. Shakan, *Explicit RIP matrices: an update*, Acta Math. Hungar. **168** (2022), 509–515; [2108.01794v3](https://arxiv.org/abs/2108.01794v3) | Theorem 1 p.2; $\epsilon=3.26\cdot10^{-7}$ and improvement $\epsilon/4=8.15\cdot10^{-8}$ match. Different construction. |
| C. Kümmerle, D. G. Mixon, *Explicit restricted isometries with $k=m^{2/3-o(1)}$*; [2611.14475v1](https://arxiv.org/abs/2611.14475v1), 10 November 2026 | Theorem 1 p.3; Lemma 3 pp.5–6; (9) p.6; Theorem 4 pp.6–7; Theorem 6 p.10; Lemma 7 and Proposition 8 p.11; (16) p.12; Proposition 10 pp.12–13 all match. Elliptic affine polar graph, norm-graph selection, $m=(q-1)(q^2+1)$, $n=\lfloor\log q\rfloor q^3$, and sparsity parameters match. Different overcomplete family. |
| D. Kunisky, X. Yu, *A degree 4 sum-of-squares lower bound for the clique number of the Paley graph*, CCC 2023, LIPIcs **264**, 30:1–30:25; [2211.02713v2](https://arxiv.org/abs/2211.02713v2) | Theorem 1.2 p.4 is Theorem 2 on published p.30:4. Both full texts independently fetched. The relaxation lower bound is correctly distinguished from an actual clique or RIP obstruction. |
| D. R. Heath-Brown, L. B. Pierce, *Burgess bounds for short mixed character sums*, J. London Math. Soc. **91** (2015), 693–708; [1404.1677v1](https://arxiv.org/abs/1404.1677v1) | Theorem 1.4 p.5 and the coefficient supremum p.7 verify its use. Page 2 supplies the omitted older comparison. |
| E. Gaar, D. Pucher, *The exact subgraph hierarchy and its vertex-transitive variant for the stable set problem for Paley graphs*; [2412.12958v2](https://arxiv.org/abs/2412.12958v2), 9 November 2025 | Theorems 14 p.10 and 19 p.17 match. Stable-set relaxations, not interval ETF conditioning. |
| E. J. King, *$k$-Homogeneous Equiangular Tight Frames*; [2505.00160v3](https://arxiv.org/abs/2505.00160v3), 28 September 2026 | Theorem 2.7 p.9 and Conjecture 4.2 p.16 match. The stated $q\equiv3\pmod4$ symmetry and spark questions do not settle this real family. |
| D. Cai, J. Zeng, X.-D. Zhang, *Sharp Bounds for Guiduli-Type Hereditary Spectral Problems*; [2606.08913v1](https://arxiv.org/abs/2606.08913v1), 8 June 2026 | Theorem 1.3 pp.3–4 matches. Hereditary-density spectral estimates for nonnegative graph matrices supply no Paley-sign cancellation. |
| Y. Wang, Y. Shen, V. A. Kobzar, *Lower Bound on the Block-Diagonal SDP Relaxation of the Clique Number for Seidel Spectrum Bounded Graphs*; [author text](https://yw3762.github.io/assets/pdf/paley.pdf) | Theorem 3.4 p.9 and Corollary 3.10 p.11 match. Date appropriately left unspecified. No arXiv version identified; author text independently fetched. |
| D. Kunisky, *Spectral pseudorandomness and the road to improved clique number bounds for Paley graphs*; [2303.16475v1](https://arxiv.org/abs/2303.16475v1); Experimental Mathematics **34** (2025), no.4, 684–711, online 15 October 2024 | Appendix C PDF pp.43–44 / printed pp.41–42 matches. It cautions that localization spectra do not control arbitrary RIP supports. No interval corollary found. |
| S. Satake, *On the Paley RIP and Paley graph extractor*; [2405.08608v2](https://arxiv.org/abs/2405.08608v2) | Theorem 18 and Corollary 21 p.6 match and assume suitable Paley RIP. |
| J. Zahl, *Sphere tangencies, line incidences, and Lie's line-sphere correspondence*, Math. Proc. Cambridge Philos. Soc. **172** (2022), 401–421; [2002.11677v2](https://arxiv.org/abs/2002.11677v2) | Theorem 1.8 pp.4–5 correctly identifies the geometric input to Kümmerle–Mixon. No direct interval result. |
| A. Kaplan, V. Pohl, H. Boche, *Deterministic Matrices with a Restricted Isometry Property for Partially Structured Sparse Signals*, SampTA 2019; [conference text](https://sampta2019.sciencesconf.org/267683/Kaplan.pdf) | Theorem 6 p.3 matches. Restricted patterns in a concatenation of two bases. No arXiv version identified; conference text independently fetched. |
| A. Bandeira, [*Deterministic RIP matrices — a new cooperative online project*](https://afonsobandeira.wordpress.com/2013/12/04/deterministic-rip-matrices-a-new-cooperative-online-project/), 4 December 2013 | Date and connection to Mixon's chapter checked. Does not give the interval theorem. |
| D. Mixon, [*Explicit restricted isometries well beyond the square-root bottleneck*](https://dustingmixon.wordpress.com/2026/11/11/explicit-restricted-isometries-well-beyond-the-square-root-bottleneck/), 11 November 2026 | Date and equal-magnitude absolute-value obstruction checked. This observation is already explicit prior art. |

The additional conditional reduction in the submitted report also checks. Equation (7) gives normalized flat correlations at most $p^{\varepsilon-\beta}$ for large sets; if either set is small, the trivial bound gives $p^{-(1/2-\alpha-\varepsilon)/2}$. The special column contributes at most $\sqrt{k/p}$. BMM Proposition 3.2 supplies $150\log k$, giving (8). This is a correct sufficient condition, not a new unconditional estimate. The report's clique and independent-set eigenvalues, complete-convolution norm $\sqrt p$, and arbitrary-mask limitation also check.

The bounded literature search additionally examined Mixon's thesis [1204.5958v1](https://arxiv.org/abs/1204.5958v1), §3.3.3; Bandeira–Fickus–Mixon–Moreira, *Derandomizing restricted isometries via the Legendre symbol*, [1406.4089v1](https://arxiv.org/abs/1406.4089v1); Arian–Yilmaz, *RIP constants for deterministic compressed sensing matrices-beyond Gershgorin*, [1911.07428v1](https://arxiv.org/abs/1911.07428v1); Magsino–Mixon–Parshall, *Kesten–McKay law for random subensembles of Paley equiangular tight frames*, [1905.04360v1](https://arxiv.org/abs/1905.04360v1); and Munsch–Shparlinski–Sun–Xiao, *A large sieve inequality for sums of Legendre symbols over short intervals*, [2604.23661v3](https://arxiv.org/abs/2604.23661v3). They concern the usual RIP candidate, derandomized sign matrices, constant improvements near the coherence scale, random spectral distributions, and averaging character sums over primes, respectively. They do not state the submitted interval theorem. Mixon's 2014 and 2019 blog discussions were also checked.

The selection references missing from the submitted assessment are Spielman–Srivastava, *An elementary proof of the restricted invertibility theorem*, Israel J. Math. **190** (2012), 83–91, and Youssef, *A note on column subset selection*, IMRN **2014**, no.23, 6431–6447. Their full arXiv texts and publisher-deposited metadata are retained.

Searches combined Paley ETF/matrix with interval, consecutive columns, arithmetic progression, Toeplitz character/Legendre matrix, near orthogonality, well conditioning, and Burgess, together with date-qualified 2024–2026 RIP/discrepancy searches and citation-following. Generated solution registries, including one misnumbering this conjecture, were excluded as mathematical evidence. No published statement of this exact prescribed-interval corollary, and no full resolution of Conjecture 29, was found. This is a bounded negative search result, not a priority proof or exhaustive certificate of openness. The positive literature conclusion is firmer: the required character-sum estimates predate HBP, generic deterministic tall dictionaries already have the stated behavior, and the absolute-value observation is explicit prior art. I would not accept a claim of a new solution or new analytic bound here. Whether this particular interval reformulation appeared verbatim remains unestablished.

Independent numerical evidence is reproducible with `python3 code/check_intervals.py`. The script constructs Fourier columns and exact Legendre-entry Gram matrices, then diagonalizes them in floating point. These are numerical full-Gram norms, not coherence surrogates or certified algebraic eigenvalues. It also checks both affine character signs, the Fourier integral by sufficient-degree quadrature, the border, the absolute-value norm, and the separate block-Abel argument. At $\rho=1/32$:

| $p$ | $L$ | finite norm | bordered norm | bordered condition |
|---:|---:|---:|---:|---:|
| 101 | 11 | 0.616772 | 0.619524 | 1.737518 |
| 257 | 19 | 0.445302 | 0.445302 | 1.579187 |
| 509 | 27 | 0.492722 | 0.493709 | 1.705950 |
| 1009 | 39 | 0.683029 | 0.734830 | 1.567312 |
| 2017 | 56 | 0.429211 | 0.484887 | 1.523358 |
| 4093 | 82 | 0.354050 | 0.354051 | 1.383290 |
| 10009 | 133 | 0.377151 | 0.408947 | 1.360117 |

The five overlapping rows agree with the submitted table. Maximum independent Fourier/character Gram-entry discrepancy was below $1.11\cdot10^{-13}$; quadrature discrepancy below $2.68\cdot10^{-14}$. The asymptotic proof does not depend on these observations. Computation used one numerical thread, inherited nice 20, and less than 150 MB peak RSS. Results are in `data/interval_checks.csv` and `data/verification.json`.

Sources were obtained independently over the network, not copied from the claimant's source directory. Every report-cited arXiv full text was obtained from its specified version. Blogs, conference text, published CCC version, undated author manuscript and older Burgess confirmation were obtained from primary hosts as separate non-arXiv artifacts. Only plain text is retained in `sources/`; PDF bodies were converted in memory, with no PDFs or page images written. `data/source_manifest.jsonl` records response and text hashes; `data/source_index.json` records final text hashes and page counts. The claimant's files were unchanged. No subagents, publication, pushes or writes outside this directory were used.

Precisely what survives is an unconditional theorem about every subset of prescribed interval or affine-progression supports of size $p^{9/16-\rho}+O(1)$, with decay (1), plus a limitation of the nonnegative-Gram estimate. Precisely what remains unproved is the bound for every support of size $p^{1/2+\varepsilon}$ in the full $(p+1)$-column ETF. The theorem verifies a structured special case; it settles no source-stated alternative.

Task: “You are an independent referee … Write REPORT.md” — 13 November 2026, 22:26 +04 (audit start).
