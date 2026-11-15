PARTIAL

# D0034: ψ-mixing and Harris-chain representations

This investigation does not resolve Bradley’s Question 6. I found no printed resolution in the sources and citation records checked. That is a bounded literature-search result, not a certification that no resolution exists through 2026. Neither a counterexample nor a construction covering every ψ-mixing or every 1-dependent sequence has been established here.

The proved results below are limited: the chain of pasts can fail Harris recurrence even for iid bits; a mixing instantaneous function of a stationary Harris chain is absolutely regular; block factors and absolutely regular finite-order Markov processes have the required representations. The original Berbee–Bradley obstruction is satisfied by every ψ-mixing process. These observations explain several failed routes, without settling the question. They are standard consequences and examples; no novelty is claimed.

## 1. Exact problem and literature first

The target is a strictly stationary real-valued process X=(X_k) indexed by Z. A representation means equality of its entire process law on the product Borel space R^Z with the law of (f(Y_k)), where Y is a real-valued strictly stationary Harris recurrent Markov chain and f:R→R is Borel. The hidden state need not be finite or countable; a standard Borel state space can be encoded in a Borel subset of R. The hidden chain need not inherit finite dependence or ψ-mixing from its observation.

The source is [1], Section 3.3, journal p. 122, PDF p. 16, Question 6. In the stationary convention used there, Harris recurrence requires, for π-almost every initial state y, that every Borel set of positive stationary measure be visited infinitely often with conditional probability one. The quantifier over y precedes the quantifier over sets. Recurrence for each fixed set with a set-dependent exceptional set does not establish this property.

The following literature was checked before selecting an argument.

| Source | Result or scope checked | Implication for D0034 |
|---|---|---|
| Berbee–Bradley (1984) [2], full text | Theorem 1.1; Section 1; Lemma 4.1 and Remarks 4.2–4.3 | A countably valued ψ*-mixing nonrepresentable process exists. Remark 4.3 explicitly leaves ψ-mixing and 1-dependence open. |
| Bradley (1993) [3], publisher abstract and [1] | Arbitrarily fast mixing rates, short of m-dependence, for nonrepresentable processes | Fast ψ*-mixing is insufficient; this does not give ψ-mixing. Full article not obtained. |
| Bradley (1983) [4], publisher abstract | Absolute-regularity characterization and an example that is an observation of a countable irreducible aperiodic chain | It is not a theorem that every absolutely regular process has such a representation. |
| Berbee (1986) [5], full text | Theorem 2.2 and periodic decomposition of stationary ergodic processes with β(n)<1 for some n | Gives necessary dependence structure, not its sufficiency for representation. |
| Berbee (1987) [6], full text, introduction and Theorem 1.2 | Countable-state Markov representations under a continuity/summability condition on the conditional transition rule | A positive result with additional hypotheses on conditional distributions. No deduction of these hypotheses from ψ-mixing was obtained. |
| Aaronson–Gilat–Keane–de Valk (1989) [7] | Original bibliographic record/abstract; discussion in [9,12] | Failure to be a two-block factor. Full original PDF was not accessible. |
| Burton–Goulet–Meester (1993) [8] | Bibliographic record; accounts in [9,12] | Failure to be any finite block factor. The example discussed there is hidden Markov with finite state space; it is not a Harris-chain counterexample. Full original PDF was not accessible. |
| Holroyd–Liggett (2016) [9], full text | Theorem 1, Proposition 3, definition immediately before Proposition 3 | 1-dependent 4-colorings and 2-dependent 3-colorings exist, and no finitely dependent coloring is an observation of a finite-state chain. Their term hidden Markov explicitly requires finite state space. |
| Holroyd (2017) [10], primary abstract/theorem excerpt | Theorem 1: the 1-dependent 4-coloring is a finitary iid factor | Finitary coding alone does not establish a Harris representation. |
| Holroyd–Hutchcroft–Levy (2020) [11], full text | Theorem 1(ii), Theorem 2, Proposition 35 | Some finitely dependent colorings, including 1-dependent colorings with at least five colors, have countable-state representations with recurrent hidden chains. Theorem 2 has a finite expected bit-finitary coding-radius hypothesis. |
| Spinka (2020) [12], full text | Theorem 1.1; Section 1.2 | Countable-valued finitely dependent stationary processes on Z have finitary iid codings. The theorem does not supply finite expected coding radius. |
| Bradley (2007) [13] | Publisher description and contents only | Vol. 2 covers periodicity and Markov chains in Chapters 20–21. The full books were unavailable; their text and any updated problem list have not been audited. |

In particular, non-block-factor and non-finite-state-hidden-Markov conclusions are weaker than the conclusion required in this problem. The original coloring argument does not rule out uncountable Harris states. Conversely, the countable representations in [11] give positive examples, rather than a representation theorem for all finitely dependent processes.

Searches covered the exact question, its distinctive phrases, the original nonrepresentation paper and addendum, later Bradley material, conditional-transition representations, and the coloring/coding literature. Search snapshots are in data/search_*.json. A forward-citation screen of the survey’s OpenAlex record returned 929 distinct works dated 2005-01-01 through 2026-11-13. All titles and 671 available abstracts were screened for representation, Harris, hidden Markov, finite dependence and question-specific terms. The candidate records did not identify a resolution. The remaining 258 records lack abstracts; this was not a full-text review of all 929 works. Index omissions and books remain additional limitations. Raw pages and the screening program are saved for inspection.

## 2. Why the chain of pasts does not solve the problem

For any stationary real-valued X, put

    P_n = (X_{n+j}: j≤0).

This process is stationary and Markov: its current state contains every earlier state, and its transition appends X_{n+1} according to the regular conditional law given the past. Stationarity supplies a time-homogeneous version of that kernel. The last coordinate observes X_n. The state space R^{Z≤0} is standard Borel, so real encoding is possible. The remaining requirement is Harris recurrence.

Here is an explicit failure, even when X consists of independent fair bits. Let ν be product fair-bit measure on the past-state space S={0,1}^{Z≤0}. Fix any s∈S. For n≥1 define the Borel set

    E_n(s) = {z∈S: z_j=s_{j+n} for every j≤−n}.

Starting from s, after n steps the past chain belongs to E_n(s) with probability one: all the old coordinates have merely moved n places to the left. But ν(E_n(s))=0, because specifying arbitrarily many independent fair bits has probability tending to zero. Therefore

    B_s = S \ union_{n≥1} E_n(s)

has ν(B_s)=1 and K^n(s,B_s)=0 for every n≥1. Irreducibility fails at every s, hence so does Harris recurrence. The dependence of B_s on s is allowed by the quantifier order above.

This is a failure of this particular representation. The iid process itself is already a stationary Harris chain: from every state, its next state has its stationary law. Thus failure of the past chain is not an obstruction to the existence of another representation.

## 3. A necessary condition: mixing Harris observations are absolutely regular

Write F_a^b=σ(X_j:a≤j≤b), and use Bradley’s normalization

    β(A,B) = (1/2) sup sum_{i,j}|P(A_i∩B_j)−P(A_i)P(B_j)|,

where the supremum is over finite measurable partitions in the two sigma-fields. Set β_X(n)=β(F_{−∞}^0,F_n^∞).

**Proposition 1.** Suppose X is mixing in the ergodic-theoretic sense and has the required stationary Harris-chain representation. Then β_X(n)→0. The representing chain may be periodic.

**Proof.** Work on the probability space realizing X_k=f(Y_k). Data processing gives β_X(n)≤β_Y(n): partitions formed from observations are also partitions formed from hidden variables. A stationary Harris chain has some finite period p and

    lim β_Y(n) = 1−1/p < 1.

For a stationary mixing process, the absolute-regularity dichotomy is that either β_X(n)→0 or β_X(n)=1 for every n. Consequently the latter alternative is impossible. These two standard facts are Theorem 3.5 and Theorem 4.1(3)(a) of [1]; see also the periodic decomposition in [5]. This proves the assertion. ∎

The periodic case matters: β_Y need not converge to zero, even when its observation does. An independent check is to condition on the p hidden cyclic classes. Under each phase, the p-step chain is aperiodic Harris and its path blocks are absolutely regular. The conditional output laws are invariant under the p-step shift. Since mixing X is ergodic under that shift, its finite mixture of invariant phase laws must have identical components. Mixing of the output therefore removes the observable phase obstruction, consistently with Proposition 1.

This condition cannot distinguish the requested examples. For ψ(n)<∞, the defining bound on every partition cell gives

    β_X(n) ≤ ψ_X(n)/2,

by summing P(A_i)P(B_j), whose double sum is one. Thus ψ-mixing already implies absolute regularity. A 1-dependent process has β_X(n)=ψ_X(n)=0 for n≥2.

Both classes also have trivial one-sided tails. For example, if A lies in the future tail of a 1-dependent process, A is independent of every fixed finite coordinate block by placing it sufficiently far in the future. A monotone-class argument makes A independent of the sigma-field of the entire process, including itself; hence P(A) is zero or one. The same argument uses α(n)→0 for a ψ-mixing process. One-sided tail triviality supplies no obstruction here.

## 4. The original product-minorant obstruction, and why it stops

Lemma 4.1 of [2], transferred to observations by Remark 4.2, gives the following necessary condition. There exist p,m,n_0≥1 with p dividing m and γ>0 such that for each n≥n_0 divisible by p there is a finite measure φ_n on R^{n+1}, of mass γ, satisfying

    Law(X_{−n},…,X_0, X_m,…,X_{m+n}) ≥ φ_n ⊗ φ_n.       (1)

The inequality is domination of measures on the whole product Borel sigma-field. The same measure occurs on the two sides, and its mass is bounded away from zero uniformly as the windows grow. This is stronger than a nonzero overlap condition for a single pair of coordinates. The small-set argument in [2] proves it for Harris chains, and measurable pushforward proves it for observations.

**Proposition 2.** Every stationary ψ-mixing process satisfies (1). Every stationary 1-dependent process satisfies (1) with p=1, m=2 and γ=1.

**Proof.** Choose m with ε=ψ_X(m)<1, and let λ_n be the law of (X_0,…,X_n). For all events in the left and right windows,

    P(A∩B) ≥ (1−ε)P(A)P(B).

Stationarity identifies both marginal laws with λ_n. Finite disjoint unions of measurable rectangles, followed by measure approximation, extend the bound to all product Borel sets. Thus the joint window law dominates (1−ε)λ_n⊗λ_n. Take

    φ_n = sqrt(1−ε) λ_n,
    p=1, n_0=1, γ=sqrt(1−ε).

For 1-dependence, the separated windows at m=2 are independent, so ε=0 and γ=1. ∎

This reproduces the limitation already stated in Remark 4.3 of [2]. Using its obstruction to reject a 1-dependent coloring would be incorrect.

Harris-chain small sets also explain the regeneration intuition. On a suitable m-step skeleton, a minorization K^m(y,·)≥aν(·) on a positive-measure recurrent set permits a split transition with a common restart law. The intervening path coordinates require conditional bridges. For m>1, splitting the skeleton alone does not prove that full consecutive observation blocks are iid. No converse from (1), absolute regularity, or tail triviality to such a consistent hidden regeneration construction has been proved here.

## 5. Positive cases with explicit constructions

**Proposition 3.** Every stationary finite block factor of iid variables taking values in a standard Borel space has the representation required by Bradley.

**Proof.** Write X_n=h(U_n,…,U_{n+r−1}), where the U_n are iid with law μ and h is Borel. Let

    Y_n=(U_n,…,U_{n+r−1}).

The transition shifts the window and appends one independent μ variable. Hence Y is stationary Markov, with stationary law π=μ^r, and K^r(y,·)=π for every y. Under every initial state, the states at times r,2r,3r,… are independent with law π. Every Borel set of positive π measure is visited infinitely often with probability one. This proves Harris recurrence directly. Encode the standard Borel space in R and use the observation h after decoding, extending the observation arbitrarily off the encoded space. ∎

An iid coding window with coordinates on both sides of n is covered by taking the corresponding shifted window for Y_n; the same shift-and-append construction applies. The argument does not require a finite alphabet.

**Proposition 4.** Every stationary absolutely regular process that is Markov of some finite order r≥1 has the required representation. This includes every ψ-mixing or 1-dependent process with that additional finite-order Markov property.

**Proof.** Set Y_n=(X_{n−r+1},…,X_n). The finite-order assumption makes Y stationary Markov. For n≥r,

    β_Y(n) ≤ β_X(n−r+1) → 0,

because the left hidden window history lies in F_{−∞}^0 and the right hidden window history lies in F_{n−r+1}^∞. A stationary absolutely regular Markov chain is aperiodic Harris ([1], Corollary 3.6), after a Borel encoding in R. Observe its last coordinate. ∎

Finite dependence is an unconditional independence statement and does not imply a finite-order Markov property. Even a simple 1-dependent block factor illustrates the conditional difficulty. Let U_j be independent fair bits and X_j=U_j OR U_{j+1}. Then X_0 and X_2 are independent, but

    P(X_0=0 | X_1=1) = P(X_2=0 | X_1=1) = 1/6,
    P(X_0=0, X_2=0 | X_1=1) = 0.

Indeed, X_0=0 forces U_1=0 and X_2=0 forces U_2=0, contradicting X_1=1. Individually, each joint event with X_1=1 has probability 1/8, while P(X_1=1)=3/4. Thus conditioning on the bridge introduces dependence. This also rules out the first-order Markov property for this X. It does not rule out a hidden representation: Proposition 3 provides one. An argument that resets after an independent gap must still reproduce these conditional bridge laws.

The stronger coding theorem [11, Theorem 2] gives another positive class: discrete processes with a bit-finitary iid coding of finite expected coding radius. Its hidden chain is itself an equivariant factor of iid, hence stationary and ergodic. A stationary ergodic countable-state Markov chain restricts to one positive recurrent irreducible class of full measure, so it is Harris and can be encoded in R. Spinka’s almost-sure finiteness result [12] alone does not provide the integrability hypothesis needed for this application.

## 6. Checks, failed routes, and scope left open

The mathematical checks were as follows.

- Re-read the original survey’s representation definition and stationary Harris quantifiers, and [2]’s actual obstruction and open-question remark. ψ and ψ* were kept distinct throughout.
- Checked the finite-state restriction in [9] against the countable-state positive result in [11]. Failure to be a block factor was never used as failure to be a Harris-chain observation.
- Checked the periodic case in Proposition 1 both through the β dichotomy and through cyclic conditioning. No assumption that the representing chain is aperiodic was inserted into the problem.
- Proved recurrence of the iid window chain directly, independently of the absolute-regularity criterion.
- Enumerated all 16 fair-bit assignments in the bridge example using exact rational arithmetic. The conditional joint probability is zero, while the product of conditional marginals is 1/36. Separately verified the two-step transition of the four-state iid bit-window chain: every entry is exactly 1/4. These calculations check examples, not the general open question.
- Checked the citation counts independently by concatenating the five raw pages and counting unique work identifiers: 929 entries, 929 identifiers, 671 nonempty abstracts, 258 missing abstracts.

The following attempted implications fail or remain unjustified:

    stationary → past-chain representation → Harris recurrence        fails;
    non-block-factor → no Harris representation                       fails;
    no finite-state hidden chain → no real Harris hidden chain         unproved;
    ψ*-mixing, even very fast → ψ-mixing                               fails;
    absolute regularity or (1) → Harris representation                 unproved;
    almost surely finite coding radius → finite expected radius        fails in general;
    separated blocks independent → independent after bridge conditioning fails.

The remaining task is precisely the original one: either find a stationary ψ-mixing process, possibly 1-dependent, outside the full real Harris representation class, or construct such a representation for every process in one of those classes. None of the limited propositions above does this. The status is therefore PARTIAL, not PROVED, COUNTEREXAMPLE, or RESOLVED_IN_LITERATURE.

Artifacts: sources/ holds downloaded originals and extracted text; data/ holds source metadata, citation pages, search snapshots, and exact checks; code/ holds the reproducible citation screen and exact finite calculation. All writes stayed in this directory. No subagents, publication, git pushes, simulations, or background services were used. Effective inherited nice was 15, already at least 10; the work used one Python thread and small document/JSON data, far below 4 GB.

## References

[1] R. C. Bradley, “Basic properties of strong mixing conditions. A survey and some open questions,” Probability Surveys 2 (2005), 107–144. [Original PDF](https://arxiv.org/pdf/math/0511078); [DOI](https://doi.org/10.1214/154957805100000104). Local: sources/Bradley_2005_math0511078.pdf.

[2] H. C. P. Berbee and R. C. Bradley, “A limitation of Markov representation for stationary processes,” Stochastic Processes and their Applications 18 (1984), 33–45. [Full text](https://ir.cwi.nl/pub/1854/1854D.pdf); [DOI](https://doi.org/10.1016/0304-4149(84)90159-5). Local: sources/Berbee_Bradley_1984.pdf.

[3] R. C. Bradley, “An addendum to ‘A limitation of Markov representation for stationary processes’,” Stochastic Processes and their Applications 47 (1993), 159–166. [Publisher](https://www.sciencedirect.com/science/article/pii/030441499390102A); [DOI](https://doi.org/10.1016/0304-4149(93)90102-A).

[4] R. C. Bradley, “Absolute regularity and functions of Markov chains,” Stochastic Processes and their Applications 14 (1983), 67–77. [Publisher](https://www.sciencedirect.com/science/article/pii/0304414983900479); [DOI](https://doi.org/10.1016/0304-4149(83)90047-9). The 2005 survey’s bibliography gives this article an incorrect page range; the range here follows the publisher record.

[5] H. Berbee, “Periodicity and absolute regularity,” Israel Journal of Mathematics 55 (1986), 289–304. [Full text](https://ir.cwi.nl/pub/2487/2487D.pdf). Local: sources/Berbee_1986.pdf.

[6] H. Berbee, “Chains with infinite connections: uniqueness and Markov representation,” Probability Theory and Related Fields 76 (1987), 243–253. [Full text](https://ir.cwi.nl/pub/2448/2448D.pdf). Local: sources/Berbee_1987.pdf.

[7] J. Aaronson, D. Gilat, M. Keane and V. de Valk, “An algebraic construction of a class of one-dependent processes,” Annals of Probability 17 (1989), 128–143. [DOI](https://doi.org/10.1214/aop/1176991499).

[8] R. M. Burton, M. Goulet and R. Meester, “On 1-dependent processes and k-block factors,” Annals of Probability 21 (1993), 2157–2168. [DOI](https://doi.org/10.1214/aop/1176989014).

[9] A. E. Holroyd and T. M. Liggett, “Finitely dependent coloring,” Forum of Mathematics, Pi 4 (2016), e9. [Full text](https://arxiv.org/pdf/1403.2448); [DOI](https://doi.org/10.1017/fmp.2016.7). Local: sources/Holroyd_Liggett_2016.pdf; downloaded arXiv v4, dated 4 June 2015.

[10] A. E. Holroyd, “One-dependent coloring by finitary factors,” Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 53 (2017), 753–765. [DOI](https://doi.org/10.1214/15-AIHP735).

[11] A. E. Holroyd, T. Hutchcroft and A. Levy, “Mallows permutations and finite dependence,” Annals of Probability 48 (2020), 343–379. [Full text](https://arxiv.org/pdf/1706.09526); [DOI](https://doi.org/10.1214/19-AOP1363). Local: sources/Holroyd_Hutchcroft_Levy_2020.pdf. The theorem numbers used above refer to this downloaded arXiv version.

[12] Y. Spinka, “Finitely dependent processes are finitary,” Annals of Probability 48 (2020), 2088–2117. [Full text](https://arxiv.org/pdf/1901.00123); [DOI](https://doi.org/10.1214/19-AOP1417). Local: sources/Spinka_2020.pdf.

[13] R. C. Bradley, Introduction to Strong Mixing Conditions, Volumes 1–3, Kendrick Press, 2007. [Publisher contents](https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm). Local publisher page: sources/Bradley_2007_publisher.html. Full books not obtained.

Task: “Open problem D0034” — recorded start 13 November 2026, 04:59 Asia/Tbilisi.
