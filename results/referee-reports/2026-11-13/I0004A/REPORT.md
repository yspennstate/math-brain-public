RESOLVED_IN_LITERATURE

The requested phase-zero walk is recurrent for Lebesgue-almost every irrational α, and for every bounded-type irrational α, including every quadratic irrational. These are printed results. The stopping rule therefore applies; this report does not claim a classification of all irrational α.

The decisive reference is Julien Brémont, *Markov chains in a stratified environment*, ALEA 14 (2017), 751–798, **Proposition 7.1, pp. 790–791**. It specifies precisely ε_n=1_[0,1/2)({nα})−1_[1/2,1)({nα}), p_n=q_n=r_n=1/3, and μ_n=δ_(ε_n), and concludes recurrence for almost every α. Its proof invokes the more explicit sufficient condition below. [Published paper](https://alea.math.cnrs.fr/articles/v14/14-36.pdf), saved as `sources/bremont_2017.txt`.

The source listing identifies **Ahmed Bou-Rabee and Yuval Peres**, *The randomly oriented Manhattan lattice in 2D is transient*, **arXiv:2609.07621v1 [math.PR]**, submitted **Monday, 7 September 2026, 15:24:35 UTC**. Only v1 appears in the listing checked on 13 November 2026. Section 7, Problem 3 is on manuscript p. 14. The title's capitalization is as above. [arXiv listing](https://arxiv.org/abs/2609.07621); its text and the entire paper are saved in `sources/bou_rabee_peres_2026_listing.txt` and `sources/bou_rabee_peres_2026.txt`.

The walk and the arithmetic condition

Put θ={α}∈(0,1), and write θ=[0;a_1,a_2,…]. Define

\[
 f(t)=2\mathbf1_{[0,1/2)}(\{t\})-1,\qquad \varepsilon_y=f(y\theta),\qquad
 A_m=\sum_{j=1}^m a_j.
\]

The state M_n=(H_n,V_n) starts at (0,0). Its discrete-time transition probabilities are

\[
 P((x,y),(x+\varepsilon_y,y))=	frac13,\qquad
 P((x,y),(x,y+1))=P((x,y),(x,y-1))=	frac13.
 \tag{1}
\]

There is no holding step. The horizontal move probability is 1/3; the total vertical move probability is 2/3. The vertical *coordinate* is lazy, with holding probability 1/3. Since every jump changes x+y by an odd number, returns at odd times have probability zero. Both signs of ε occur and the chain is irreducible.

This is Guillotin-Plantard–Le Ny's Definition 1 and Section 2.2 (January 2006 final preprint, p. 3), and is explicitly the convention in Bou-Rabee–Peres Section 1.4.2 (p. 5). Problem 3 refers to that partially oriented model. It is not the main Manhattan model, which has both coordinates oriented and chooses its two outgoing edges with probabilities 1/2 each (Bou-Rabee–Peres (1), p. 1). The main paper's continuous-time proof uses rate 1 on each of those two edges, total rate 2 (p. 2). It does not redefine Problem 3 with horizontal probability 1/2.

Poissonizing (1) at any constant total rate λ>0 preserves recurrence and divides the discrete Green function by λ. A rate-one clock on each of its three allowed edges has λ=3. Adding a fixed holding probability strictly below one also preserves recurrence. These are time changes, not extra laziness specified in the original partially oriented walk.

The arithmetic sufficient condition is

\[
 \mathcal D(\theta):\qquad
 \sum_{m\ge1}\frac{\log(1+a_m)}{A_m}=\infty.
 \tag{2}
\]

Brémont's *On planar random walks in environments invariant by horizontal translations*, MPRF 22(2) (2016), Proposition 1.5, proves recurrence under (2), even with any fixed horizontal probability p∈(0,1) and up/down probabilities (1−p)/2. The author's November 2014 preprint has the statement on p. 3 and proof on pp. 29–30; those are the page numbers used below. [Author text](https://perso.math.u-pem.fr/bremont.julien/julien_fichiers/Fichiers/mamith.pdf), saved as `sources/bremont_planar_2016.txt`. The publisher lists the article as pp. 267–310; the ALEA bibliography gives 267–309. This discrepancy does not affect the proposition or the independently published ALEA statement. [Publisher record](https://math-mprf.org/journal/articles/id1425/).

| Angle class, with phase fixed at 0 | Verified conclusion |
|---|---|
| Every θ satisfying (2) | Recurrent, by Brémont (2016), Proposition 1.5. |
| Bounded type: sup a_m<∞ | Recurrent: if a_m≤B, each summand in (2) is at least log 2/(Bm). |
| Quadratic irrational | Recurrent, because its continued fraction is eventually periodic and bounded. |
| Golden ratio, reduced modulo 1 | Recurrent; all partial quotients are 1. |
| Lebesgue-almost every irrational | Recurrent, explicitly Brémont (2017), Proposition 7.1. |
| Liouville irrational satisfying (2) | Recurrent. Infinite irrationality type is compatible with (2), as the remark after Proposition 1.5 explicitly states. |
| An arbitrary exceptional irrational failing (2), including an unspecified Liouville number | No classification supplied by these results. Failure of (2) is not a transience criterion. |

The a.e. conclusion uses the classical metric continued-fraction fact ∑_m 1/A_m=∞ for a.e. θ, cited to Khintchine (1935) in ALEA p. 791. Since log(1+a_m)≥log 2, this implies (2). In particular, the old suggestion that badly approximable rotations should be transient is not a theorem and is contradicted by bounded-type recurrence. A label such as “Liouville” does not by itself decide the walk's behavior in the results checked here.

The later paper, Brémont, *Planar random walk in a stratified quasi-periodic environment*, MPRF 27(5) (2021), 755–788, Theorem 3.2 and its following remark, proves recurrence under (2) for **every starting phase** x in ε_y=f(x+yθ), not merely almost every x. The statement is on p. 4 of both arXiv:2007.01573v2 and the author's June 2021 text. Take its local horizontal mean to be ε_y, its horizontal probability γ_y=1/3, and its generating function to be f/2, since γ_y/(1−γ_y)=1/2. [Author text](https://perso.math.u-pem.fr/bremont.julien/julien_fichiers/Fichiers/stratqp.pdf), saved as `sources/bremont_2021_author.txt`; [arXiv](https://arxiv.org/abs/2007.01573), saved as `sources/bremont_2021.txt`.

Proposition 3.3 of that paper (author p. 5; proof pp. 11–13) also gives transience for a different range of parameters: a_1 odd, a_m even for m≥2, and a_(m+1)≥a_m^δ eventually for some δ>1, with generating function f and horizontal drift ε_yγ_y/(1−γ_y)=f(x+yθ), for almost every phase x. For Dirac horizontal jumps this normalization can be realized with γ_y=1/2. Constant rescaling of all the drift sums leaves the flat-model recurrence criterion below unchanged, so this also gives the corresponding transience for horizontal probability 1/3 at those almost-every phases. It **does not establish transience at x=0**. The example a_m=2^(2^(m−1)) has rapidly growing partial quotients but is not automatically a Liouville number; rapid growth and infinite irrationality exponent must not be conflated. No phase-zero recurrent/transient pair of irrational angles is claimed here.

Verification of the reduction and the printed proof

The following checks explain why the literature theorem answers exactly the stated walk. They are an audit of existing arguments, not a claim of a new solution.

At successive vertical jump times, let Y_0=0 and Y_(k+1)−Y_k be independent fair ±1 variables. Let G_k count horizontal moves before the next vertical move. The G_k are independent of Y and of each other, with

\[
 P(G_k=r)=\tfrac23(\tfrac13)^r,\quad r=0,1,\ldots,
 \quad E G_k=\tfrac12,\quad \operatorname{Var}(G_k)=\tfrac34.
\]

Define T_0=0, T_k=k+∑_(j<k)G_j, and

\[
 X_k=\sum_{j<k}\varepsilon_{Y_j}G_j,\qquad
 L_k(y)=\#\{0\le j<k:Y_j=y\}.
\]

Then M_(T_k)=(X_k,Y_k) exactly. Also T_k/k→3/2 a.s. This is the embedding of Guillotin-Plantard–Le Ny, Section 3.1 and Lemma 1, pp. 5–6. Conditional on the whole vertical path,

\[
 X_k=\tfrac12\sum_y\varepsilon_yL_k(y)+W_k,
 \quad E(W_k\mid Y)=0,
 \quad E(W_k^2\mid Y)=\tfrac34 k,
 \tag{3}
\]

and, exactly,

\[
 E(e^{itX_k}\mid Y)=
 \prod_y\left[\frac{2/3}{1-(1/3)e^{it\varepsilon_y}}\right]^{L_k(y)}.
 \tag{4}
\]

Thus omitting W_k is unjustified when testing diffusive behavior. The coefficient 1/2 in (3) is also essential. At the alternating orientation, ε_(Y_j)=(−1)^j, so the local-time functional ∑ε_yL_k(y) is 0 or 1, although the geometric noise in X_k is diffusive. The correct recurrence question concerns a joint return with Y_k=0, not just a typical size of the unconditional functional.

The Green-function reduction can also be checked directly. Let σ_j be successive returns of the vertical skeleton Y to 0, with σ_0=0. The horizontal process Z_j=X_(σ_j) is a one-dimensional random walk with independent identically distributed increments, because the environment is invariant under horizontal translations. Write U(s)=∑_(j≥0)P(Z_j=s). Then

\[
 G_E:=\sum_{k\ge0}P(X_k=0,Y_k=0)=U(0).
\]

Since ε_0=+1, a horizontal block at height 0 starting at −r visits the origin once exactly when G_k≥r, an event of probability 3^(−r). Partitioning all original times into the blocks [T_k,T_(k+1)) therefore gives the identity

\[
 G_M:=\sum_{n\ge0}P(M_n=0)
     =\sum_{r\ge0}3^{-r}U(-r).
 \tag{5}
\]

If U(0)<∞, first hitting of s and spatial homogeneity give U(s)=P_0(hit s)U(0)≤U(0). Hence G_E≤G_M≤(3/2)G_E when finite; if G_E=∞ the lower bound suffices. The two walks have the same recurrence classification. This verifies the issue of visits occurring *between* vertical jumps, rather than treating a skeleton time change as sufficient without checking it. It is also the content of the trace reduction in Brémont (2016), Lemma 2.1, pp. 4–5.

The full flat-model criterion makes the drift-sum issue precise. Use Brémont's notation

\[
 \eta_i=\frac{p}{1-p}\varepsilon_i,\quad
 R_k^\ell=\sum_{i=k}^{\ell}\eta_i,\quad
 \Phi(n)^2=n^2+\sum_{-n\le k\le\ell\le n}(R_k^\ell)^2,
\]

\[
 \Phi_+(n)^2=n^2+
 \sum_{\substack{-n\le k\le\ell\le n\\k\ell>0}}(R_k^\ell)^2.
\]

Here p is horizontal probability, so p=1/3 and η_i=ε_i/2 for (1). For increasing functions, inverse means the integer generalized inverse. Brémont (2016), Definition 1.1 and Theorem 1.2, p. 2, give recurrence if and only if

\[
 \sum_{N\ge1}\frac{\Phi^{-1}(N)^2}{N^2\Phi_+^{-1}(N)}=\infty.
 \tag{6}
\]

For ε_(-i)=−ε_i, i≥1, Corollary 1.3(ii), p. 3, simplifies it to

\[
 \sum_{n\ge1}
 \left[n^2+\sum_{1\le k\le\ell\le n}(R_k^\ell)^2\right]^{-1/2}=\infty.
 \tag{7}
\]

The half-circle rule has exactly this antisymmetry away from 0, because no nonzero multiple of an irrational θ equals 0 or 1/2 modulo one. The value ε_0=+1 is allowed: changing finitely many layers does not change the classification in this vertically flat uniformly elliptic setting (remark after Theorem 1.2, p. 2). This stability is not asserted for all stratified models with unequal up/down probabilities.

For completeness, the arithmetic step in Proposition 1.5 is as follows. Let q_m be the convergent denominators, q_(-1)=0, q_0=1, and q_(m+1)=a_(m+1)q_m+q_(m−1). Denjoy–Koksma bounds the f-sum on every q_m block, uniformly in starting point. Ostrowski decomposition then bounds every interval sum of length at most q_(m+1) by C A_(m+1), with a fixed constant C. Consequently, for q_m≤n<q_(m+1),

\[
 \left[n^2+\sum_{1\le k\le\ell\le n}(R_k^\ell)^2\right]^{1/2}
 \le C' n A_{m+1}.
\]

The series in (7) is therefore bounded below, up to constants and finitely many terms, by

\[
 \sum_m\frac{\log(q_{m+1}/q_m)}{A_{m+1}}.
 \tag{8}
\]

This diverges under (2). If a_(m+1)≥2, log(q_(m+1)/q_m)≥log a_(m+1)≥c log(1+a_(m+1)). If a_(m+1)=1, group two consecutive logarithms: log(q_(m+1)/q_(m−1))≥log 2, and use A_m≤A_(m+1). Each summand is used at most twice. This checks the occasionally overlooked run of partial quotients equal to 1. It is the proof on author pp. 29–30. Combining (7)–(8), (5), and (2) gives recurrence of the original walk. For bounded type alone, the shorter check is |R_1^n|=O(log n), whence the square root in (7) is O(n log n) and ∑1/(n log n) diverges.

This proof does not infer a universal P(M_(2n)=0)∼c/n or an exact √n horizontal displacement scale. Logarithmic discrepancy can coexist with recurrence. Kesten's bounded-remainder characterization excludes bounded discrepancy for the half interval: its length 1/2 is not in Z+θZ for irrational θ. The characterization is recalled explicitly in Grepstad–Lev, *Sets of bounded discrepancy for multi-dimensional irrational rotation*, arXiv:1404.0165v2, Section 1.1, pp. 1–2 (saved as `sources/grepstad_lev_2015.txt`); their Propositions 2.1–2.2 address phase-independent formulations. The original is H. Kesten, *On a conjecture of Erdős and Szüsz related to uniform distribution mod 1*, Acta Arith. 12 (1966/67), 193–212; its full text was not obtained here. Unbounded discrepancy alone does not supply a summable return bound. Denjoy–Koksma, Ostrowski decomposition, and the dispersion/Green criterion are what matter here.

Other literature checked

The page references below are the displayed pages of the saved author/arXiv text unless explicitly identified as journal pages. They are not guessed conversions to journal pagination.

- **Campanino–Petritis**, *Random walks on randomly oriented lattices*, MPRF 9(3) (2003), 391–412, Theorems 1.6, 1.7, 1.8, all on arXiv manuscript p. 5: alternating orientations are recurrent; the orientation +1 for y≥0 and −1 for y<0 is transient; independent fair orientations give almost-sure transience (and zero speed in the stated theorem). The periodic extension is a remark following Theorem 1.6. [arXiv:math/0111305](https://arxiv.org/abs/math/0111305), `sources/campanino_petritis_2003.txt`.
- **Guillotin-Plantard–Le Ny**, *Transient random walks on 2D-oriented lattices*, Theory Probab. Appl. 52(4) (2008), 699–711, English DOI 10.1137/S0040585X97983353; original TVP 52(4) (2007), 815–826. Theorem 1 and condition (2.3), final-preprint p. 4: conditional independence given an orbit, P(ε_y=+1|x)=g(T^y x), mean ∫g=1/2 and ∫[g(1−g)]^(−1/2)<∞ imply a.e. transience. The deterministic indicator g=1_[0,1/2) violates that integral condition everywhere. Section 4, rotation example, pp. 13–14, poses the irrational case and speculates about type; those statements are conjectural. It proves no bounded-type transience. Its rational recurrent example is α=1/(2q), not every rational angle. A periodic phase-zero sequence of odd period generally has nonzero mean, so a blanket assertion that all rational angles are recurrent would be false. [arXiv:math/0601102](https://arxiv.org/abs/math/0601102); final preprint obtained from [mp_arc 06-4](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=06-4), `sources/gpln_2008b.txt`.
- **Guillotin-Plantard–Le Ny**, *Random walks on FKG-horizontally oriented lattices*, arXiv:math/0303063v1, Theorem 2.2, p. 3, under the assumptions on p. 2: stationary symmetric associated orientations with E(ε_0ε_y)=O(|y|^(−a)), a>1, give a.e. transience. Association alone is not its whole hypothesis. This is a preprint, not a result about irrational rotations. [Text](https://arxiv.org/abs/math/0303063), `sources/gpln_fkg.txt`.
- **Guillotin-Plantard–Le Ny**, *A functional limit theorem for a 2d-random walk with dependent marginals*, Electron. Commun. Probab. 13 (2008), 337–351, Theorem 2, author p. 3: in the independent fair orientation model, the joint horizontal/vertical scales are n^(3/4), n^(1/2), with dependent limiting coordinates. This functional theorem by itself would not prove transience for a new deterministic environment. [arXiv:0705.3342](https://arxiv.org/abs/0705.3342), `sources/gpln_2008a.txt`.
- **Pène**, *Transient random walk in Z² with stationary orientations*, ESAIM Probab. Stat. 13 (2009), 417–436. Theorem 1, journal p. 418, imposes weighted two-point correlation summability, a fourth-moment bound, and a block characteristic-function decorrelation bound. Theorem 2, p. 419, includes centered ±1 stationary orientations under sup_n n^6 α(n)<∞. These strong mixing hypotheses do not cover irrational rotation coding. [Published text](https://www.numdam.org/item/10.1051/ps:2008019.pdf), `sources/pene_2009.txt`.
- **Devulder–Pène**, *Random walk in random environment in a two-dimensional stratified medium with orientations*, Electron. J. Probab. 18 (2013), paper 18, 1–23, Theorem 1, author p. 2: for i.i.d. nonconstant horizontal probabilities p_y∈(0,1), with E[(1−p_0)^(−a)]<∞ for some a>1, transience holds for arbitrary orientations, a.s. in the horizontal probabilities. The nonconstant hypothesis excludes the present p_y≡1/3. [arXiv:1110.4865v2](https://arxiv.org/abs/1110.4865), `sources/devulder_pene_2013.txt`. The EJP archive identifies paper 18; some later bibliographies print 88.
- **Castell–Guillotin-Plantard–Pène–Schapira**, *A local limit theorem for random walks in random scenery and on randomly oriented lattices*, Ann. Probab. 39(6) (2011), 2079–2118, Theorem 20, arXiv manuscript p. 23, and Remarks 21–22: in their independent random environment setting, return probability has exponent 1+1/(ab), with the specified period restriction. For a=b=2 this is n^(−5/4) on even times, giving a summable annealed Green function and a.e. quenched transience. Their stable-law indices a,b are unrelated to the rotation angle α. [arXiv:1002.1878](https://arxiv.org/abs/1002.1878), `sources/castell_et_al_2011.txt`.
- **Campanino–Petritis**, *Type transition of simple random walks on randomly directed regular lattices*, J. Appl. Probab. 51(4) (2014), 1065–1080, Theorem 1.5, author p. 4: a balanced periodic background with independent random defects of probability c|y|^(−b) is a.s. transient for b<1 and recurrent for b>1. Proposition 1.8 covers finitely many deterministic defects. The theorem does not settle its borderline b=1 or quasi-periodic environments. [arXiv:1204.5297](https://arxiv.org/abs/1204.5297), `sources/campanino_petritis_2014.txt`.
- **Brémont (2021)**, Proposition 3.1, author p. 4: for periodic flat environments, recurrence is equivalent to zero total drift over a period. This supplies the precise periodic criterion; periodicity alone does not suffice. Theorems 3.2 and Proposition 3.3 are discussed above. The general stratified recurrence criterion also appears in Brémont (2017), Theorem 2.4, journal p. 754; the flat criterion (6) is enough here.

G. Matheron and G. de Marsily, *Is transport in porous media always diffusive? A counterexample*, Water Resources Research 16(5) (1980), 901–917, DOI 10.1029/WR016i005p00901, is the continuum stratified transport origin of this model. Its full text was not obtained: the publisher returned HTTP 403. Its bibliographic identification was checked against de Marsily's publication list and the primary mathematical papers above. No theorem number or recurrence claim is attributed to an unread original. The discrete three-neighbor walk should not be presented as the exact stochastic process defined in that hydrology article.

The requested “Brice” reference could not be uniquely identified as an oriented-lattice recurrence paper. Brice Franke, with Pène and Wendler, has work on U-statistics indexed by random walks; the retrieved arXiv:1401.7958v2 treats double sums of random scenery, not the rotation-directed walk. It is saved as `sources/franke_pene_wendler_2014.txt`. This possible identification is not treated as a resolution or a theorem about orientations.

Searches for 2026 work citing arXiv:2609.07621 located the author's [Manhattan-Transience formalization repository](https://github.com/nitromannitol/Manhattan-Transience), whose text is saved in `sources/manhattan_formalization_2026.txt`. It concerns the fully oriented fair-coin Manhattan result. No later paper settling every irrational phase-zero rotation was located. That is a search outcome, not a proof that none exists. No code from that repository was run. The source itself cites Nguyen's 2026 three-dimensional superdiffusivity work and Armstrong–Bou-Rabee–Kuusi's flow work; neither cited result is a classification of this deterministic two-dimensional orientation.

Checks and deliverables

The statement was checked independently against Brémont (2016) Proposition 1.5, the published ALEA (2017) Proposition 7.1, and Brémont (2021) Theorem 3.2. The phase, half-open endpoint convention, arithmetic condition, move probabilities, geometric mean and variance, row-zero exception, antisymmetric criterion, and passages to the original Green function were audited. All stored paper texts are plain text. PDF bytes were downloaded into memory and passed directly to `pdftotext`; no PDF, page image, scan, or image artifact was saved. The two author-hosted Brémont downloads required disabling verification of an invalid TLS certificate for those public-paper requests; provenance and response hashes are recorded in the text headers.

`code/get_sources.py` is the source downloader; `data/source_audit.json` records text hashes and page locations. `LOG.md` records progress and access failures. There was no mathematical simulation, large computation, extra worker, publication, push, or external write. Source processing used inherited nice 10 and a single process with one conversion child at a time. Steps 2 and 3 were not pursued because the user's step-1 stopping rule had already been satisfied. The unresolved scope is exceptional irrational angles outside (2), not bounded type or the a.e. result.

Task: “Open problem I0004.” Received 2026-11-13 15:57 Asia/Tbilisi.
