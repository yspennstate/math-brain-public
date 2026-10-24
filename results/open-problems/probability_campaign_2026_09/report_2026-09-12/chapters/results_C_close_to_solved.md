## The ones close to solved

This chapter collects the problems on which the campaign has real mathematics but not a complete
answer. They are the rows that a reader looking for the next thing to do should read first, because in
each of them the remaining work is named. Some of the names are short: a finite computation, a reading
of one hypothesis in a source, an exact-arithmetic certificate replacing a floating-point one. Others
are long: uniformity in $n$ in an Ornstein and Zernike ratio, a spreading estimate for a nonlocal
front, a local limit theorem for a triangular array whose step law degenerates. In every case the
obligation is stated the way it would be stated to a collaborator, not as a wish.

Nothing in this chapter claims novelty, and no verification word has been strengthened. Where the
record says "author checked" it says author checked here; where it says "unreviewed" it says
unreviewed. Several of the rows carry corrections made by the same agents that produced them, and the
corrections are stated once, in place.

### How the list was built, and the counts

The six ledgers are the 20-hour Codex campaign at
`Downloads/Probability_1000_20h_20260906/` and the five Claude intakes at
`06_math_research/probability_1000_intake_{claude_20260907, D_20260908, E_20260908, F_20260908,
G_20260910}/`. Each ledger is a pair of append-only files, `problems.jsonl` and `attempts.jsonl`, and
both are appended to on revision, so a scan has to take the last record for each problem id rather
than the first one it meets.

Doing that gives 1,025 distinct problem ids across the six ledgers. The status labels that mark a
partial outcome come out as follows: 29 rows labelled `partial_result`, 12 labelled
`candidate_partial_counterexample`, 1 labelled `partial_counterexample_author_checked`, 2 restricted
cases (`settled_inertial_balls` and `settled_homogeneous_case`, both from the mobile Boolean model),
and 6 labelled `known_result_not_original`. That is 50 rows, and it reproduces the coordinator's own
count of the same six ledgers exactly, label by label.

The 9 September handoff, written when five of the six ledgers existed, gives a different breakdown and
the two should be compared rather than reconciled by force. Its words: "Ledger labels sum to 894: 12
candidate full solutions; 4 proved; 1 refuted; 38 partial labels (25 partial_result, 11
candidate_partial_counterexample, 1 partial_counterexample_author_checked, 1
partial_literature_resolved); 2 restricted cases; 2 explicitly known; 648 attempted unsolved; 187
unsolved." Against my 29 and 12 that is four fewer `partial_result` rows and one fewer
`candidate_partial_counterexample`. Three of the four are intake G, which added G0008, G0013 and G0014
on 10 September, a day after the handoff. One of the remaining two differences is E0064, whose row was
rewritten on 11 September when the explicit five-type counterexample was found and which now carries
`candidate_partial_counterexample`. The residual difference is in vocabulary, not in arithmetic: the
handoff's `partial_literature_resolved` label appears nowhere in my scan, and its "2 explicitly known"
sits against my 6 `known_result_not_original`, so the two tallies are counting over partly different
label sets and over 894 admitted records rather than 1,025 distinct ids. Neither count has been adjusted
to match the other.

To those 50 rows this chapter adds ten more that the labels miss. Four are rows whose recorded status
is `candidate_full_solution` while the attempt itself names a scope limit that has not been closed
(P0189, P0174, P0032, P0033). One, F0057, is labelled `proved` and carries a pending source
correction, finding P30H-F001 in the audit registry, against the very step the proof turns on. One,
D0039, is labelled resolved in the literature and is not: that exclusion was checked against the
source on 8 September and fails. Four more are intake G rows labelled `attempted_unsolved` whose
attempts contain a reduction worth recording (G0001, G0004, G0005, G0015). Two rows inside the 50,
F0066 and F0068, are marked excluded in their own titles and are carried only in the closing table.

The ranking below is by how close the problem is, in four grades:

1. one clean finite or computational obligation remains;
2. one analytic step remains and its shape is known;
3. the mechanism is right and the quantitative half is missing;
4. a special case is proved and the general case is open.

The grades are a reader's aid, not a measurement. A rank 1 problem can still be hard: "check whether
Theorem 2.1's displacements are bounded" is finite in the sense that it is a page of somebody's paper,
not in the sense that it is easy to get right.

### F0057, total variation for every large box count, and the step that is still owed

Source: Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and
condensation*, Probability Surveys 9 (2012), Problem 18.10, Section 18.2, PDF page 89. Notation: $w =
(w_k)$ is a weight sequence, $\Phi(t) = \sum_k w_k t^k$ has radius $\rho$, $\Psi(t) = t\Phi'(t)/\Phi(t)$,
$\nu = \Psi(\rho)$, $B_{m,n}$ is the allocation of $m$ balls into $n$ boxes with weight $\prod_i
w_{Y_i}$, and $Y_{(1)} \ge Y_{(2)} \ge \dots$ are the ordered box counts. The question, verbatim from
the source: does $d_{TV}(Y_{(j)}, \xi_{(j)}) \to 0$ hold for every fixed $j$, under the assumptions of
Theorem 18.7? Janson proves it for $j = 1$ in part (vi) and writes that he conjectures total variation
approximation for every $Y_{(j)}$, that presumably it follows by a modification of his proof for
$Y_{(1)}$, and that he has not checked the details.

What is proved, from attempt F0057-A002 (recorded 9 September, author
`claude-prob1000-e0077-0908`): under the assumptions of Theorem 18.7, $d_{TV}(Y_{(j)}, \xi_{(j)}) \to
0$ for every fixed $j$, in both the $\xi$ and the $\xi^{(n)}$ versions. The mechanism follows Janson's
own proof of (vi), read in full at pages 89 to 94, with $Y_{(j)}$ in place of $Y_{(1)}$: partition
$[0, B(n))$ into at most $4/\delta + 1$ intervals chosen using $\xi_{(j)}$, handling fat singletons by
the Kolmogorov bound (v); on a thin good interval $A$, sandwich the event $\{Y_{(j)} \in A\}$ between
count events that allow up to $j-1$ boxes above the interval,
$$\{N_B = b,\ N_A \ge 1,\ N_A + N_{A^c} \ge j-b\} \supseteq \{Y_{(j)} \in A\} \supseteq \{\bar N_B = b,\ \bar N_{A^c} = 0,\ \bar N_A \ge j-b\},$$
and then the joint Poisson limits for the counts turn the gap between the two sides into
$$P(1 \le X < k,\ X+Y \ge k) + (1 - e^{-\gamma}) P(X \ge k) \le \alpha\gamma + \gamma\delta,$$
with $\alpha \le \eta(\delta, D, j) = (\delta\, j!\, e^{2D})^{1/j}$ by thinness. Summing over the good
intervals gives $(\delta + \eta) D$; the bad intervals contribute $P(\mathrm{Po}(D/2) \le j-1)$ once one
shows that a thin bad rightmost interval cannot occur for $\delta$ below a constant $c(D,j)$. The
inequality that does the work in the gap estimate is the elementary
$P(1 \le X < k, X+Y \ge k) \le P(X \ge 1)P(Y \ge 1)$. No probabilistic input beyond Janson's three is
used: the truncation at $B(n)$, the joint Poisson approximation of the counts, and the Kolmogorov
bound (v).

The obligation that remains is a repair, not a new idea. The two displayed set inclusions are stated
without the truncation good events: Janson's argument runs on the event that no box exceeds $B(n)$ and
that the counts above the truncation level behave, and the inclusions as written above do not carry
those conditioning events, so the sandwich is asserted between events on the full space while the
Poisson limits are available only on the good event. What is missing is the version of both inclusions
with the good events inserted, together with the check that the error they contribute is $o(1)$
uniformly over the at most $4/\delta + 1$ intervals rather than for each interval separately. That is
finding P30H-F001 in the audit registry, and it is recorded as pending. Until it is closed, the right
reading of this row is that the argument is complete in outline and in every estimate except the
bookkeeping of one conditioning event, and that the bookkeeping has not been done.

Two further things are not claimed. The joint law of $(Y_{(1)}, \dots, Y_{(J)})$, which Janson also
conjectures, is not proved; the attempt records that the same scheme with a product partition should
give it and that it was not written out. Prior art was not searched, the attempt's own note being that
the budget was exhausted. Verification state, verbatim: `author_checked` on the attempt, with the
problem row's `verification` field reading `unreviewed`; the independent check recorded is "Argument
checked line by line against the source text; no numerics (limit theorem; machine under compute
distress); no Lean (elementary inequalities only). Prior art not searched (budget exhausted)."
Closeness rank 1.

### F0056, the sparse parity counterexample and the tilt that has to exist

Source: Janson, Probability Surveys 9 (2012), Problem 18.9, Section 18.2, PDF page 89, with the
notation of the previous section. The question: is Theorem 18.7, in the $\xi^{(n)}$ version, true also
for $\lambda = 0 < \nu$? Theorem 18.7 is proved for $0 < \lambda \le \nu$ with $\sigma^2 =
\operatorname{Var}\xi < \infty$, and its parts include (i) $N[h(n),\infty) \to \mathrm{Po}(\alpha)$
when $nP(\xi \ge h(n)) \to \alpha$, and (vi) $d_{TV}(Y_{(1)}, \xi_{(1)}) \to 0$.

Three things are on the record here and they have to be kept apart.

First, the literal statement is false, and the reason is trivial once seen. Attempt F0056-A002 takes
$m = 1$ with $w_0, w_1 > 0$: the allocation then has exactly one nonempty box, so $N[1,\infty) = 1$
and $Y_{(1)} = 1$ deterministically, while the tilted law $\xi^{(n)}$ has mean $1/n$, so $\tau_n \sim
(w_0/w_1)/n$ and $nP(\xi^{(n)} \ge 1) \to 1$; part (i) would then assert $N[1,\infty) \to
\mathrm{Po}(1)$, and part (vi) would assert $d_{TV}(Y_{(1)}, \xi^{(n)}_{(1)}) \to 0$ while
$P(\xi^{(n)}_{(1)} = 0) \to e^{-1}$. Conditioning on a bounded total makes the count of nonempty boxes
deterministic; the independent count is Poisson. So $\lambda = 0$ has to be read with $m \to \infty$,
and the row was corrected to say so.

Second, with $m \to \infty$ and $m/n \to 0$ the earlier attempt F0056-A001 isolated what is needed.
Of the three inputs to Janson's proof, two are insensitive to $\lambda$: the identity
$$P(Y_1 = k) = w_k \frac{Z(m-k, n-1)}{Z(m,n)}$$
is an identity for every $m$, and the Poisson approximation of the number of boxes above a level uses
only that the events $\{Y_i \ge h\}$ are negatively dependent under the fixed-total constraint, which
again holds for every $m$. The third input, the local limit theorem of Lemma 13.1 for the sum of $n-1$
copies of $\xi^{(n)}$ at the point $m-k$, is the whole question, because as $m/n \to 0$ the variance of
$\xi^{(n)}$ tends to zero and the local central limit theorem is replaced by a local Poisson statement.
The precise missing input is a local ratio limit theorem for the triangular array: that
$$\frac{P(S_{n-1} = m-k)}{P(S_{n-1} = m)} \to 1 \quad\text{uniformly for } k = o(\sqrt m),$$
where $S_{n-1}$ is a sum of $n-1$ independent copies of $\xi^{(n)}$. If that holds, parts (i) to (vi)
go through verbatim. The obstruction recorded is that Gnedenko-type local theorems assume a fixed step
law or a fixed limiting variance, and none of the ones the attempts know of covers a step law tending
to a point mass at $0$ with $n\operatorname{Var}$ tending to infinity. The F0055 comparison technique,
which settled the neighbouring problem about the largest box, gives one-sided bounds on such ratios
and not the $(1+o(1))$ equality the factorial-moment proof needs.

Third, a later lane produced a candidate counterexample in the regime with content, and it is at
author stage. The construction is $w_0 = 1$, $w_1 = 0$, $w_j = 1$ for $j \ge 2$, with $n = k^4$ and
$m = 2k+1$. The point is parity: since $w_1 = 0$, no box may contain exactly one ball, so every
nonempty box holds at least two, and an odd total cannot be split into boxes of size exactly two.
Hence the conditioned allocation has $Y_{(1)} \ge 3$ with probability one, while in the tilted
independent model the probability that any box reaches three is $o(1)$, so the total variation distance
tends to $1$ rather than $0$. What remains is exact tilt existence at mean $(2k+1)/k^4$ and then the
assembled independent-versus-conditioned limit.

I checked the finite half of that while writing, and report what the check says. For this weight
sequence $\Phi(t) = 1 + t^2/(1-t)$ with radius $\rho = 1$, and $\Psi(t) = t\Phi'(t)/\Phi(t)$ increases
from $0$ to $+\infty$ on $(0,1)$; sampled values are $\Psi(0.001) = 2.003 \times 10^{-6}$, $\Psi(0.5) =
1$, $\Psi(0.99) = 99.98$. So the tilt equation $\Psi(\tau_n) = m/n$ has exactly one root in $(0,1)$ for
every $k$, which is the existence statement the obligation names. Solving it at 40 digits for $k =
10, 30, 100, 300, 1000, 3000, 10^4$ gives $\tau_n k^{3/2} = 1.00073, 1.00369, 1.00174, 1.00069,
1.00023, 1.00008, 1.00002$, so $\tau_n \sim k^{-3/2}$; the tilted mean reproduces $m/n$ to the printed
precision at every $k$; $nP(\xi^{(n)} \ge 2) = 10.33, 30.41, 100.4, 300.5, 1000.5, 3000.5, 10000.5$,
that is of order $k$, so about $k$ boxes hold two balls and the total is about $2k$ as it must be; and
$nP(\xi^{(n)} \ge 3) = 0.327, 0.186, 0.101, 0.0579, 0.0316, 0.0183, 0.0100$, decaying like $k^{-1/2}$.
The parity half needs no numerics: the weight of allocations with no box above two is the coefficient
of $t^m$ in $(1+t^2)^n$, which vanishes identically for odd $m$, so $P(Y_{(1)} \ge 3) = 1$ exactly for
every odd $m$ and every $n$. A finite check of this kind proves nothing unbounded: it confirms the
arithmetic of the construction at seven values of $k$ and the exact vanishing of one coefficient, and
leaves the assembled limit, which is a statement about all large $k$, untouched.

Verification state, verbatim: the row's `verification` is `unreviewed`, with `status_note` "2026-09-09:
literal statement fails for bounded m (m=1 counterexample); the m -> infinity case is the live question
(F0056-A002)"; A002's independent check reads "The m = 1 computation is exact; no numerics needed."
Closeness rank 1.

### P0189, Brown measure from strong convergence: the construction, the strong-convergence step, and which limit

Source: van Handel, *The strong convergence phenomenon*, arXiv:2507.00346v2 (11 February 2026), Section
6.9, pages 69 to 70. The question as the ledger records it: does strong convergence of a family of
random matrices imply convergence of the empirical complex-eigenvalue measures of every noncommutative
polynomial to the corresponding limiting Brown measure? A lane on 12 September read the source and
recorded the scope precisely: Problem 6.9 states the conjecture for arbitrary strongly convergent
families, with strong convergence in the sense of Definition 1.1, which is norm convergence with matrix
coefficients. There is no independence hypothesis, no independent-entry hypothesis, and no hypothesis
that the limiting family is free. That literal generality is what the candidate addresses; the
narrower question about independent Ginibre matrices with adjoints is a separate row and is not
answered.

The construction, from `proofs/P0189_brown_measure_strong_convergence_counterexample_candidate.md`. Fix
an irrational $\theta \in (0,1)$ and reduced approximants $p_j/q_j \to \theta$ with $q_j \to \infty$.
Put $\omega_j = e^{2\pi i p_j/q_j}$ and, on the basis indexed by $k$ modulo $q_j$,
$$U_j e_k = \omega_j^k e_k, \qquad S_j e_k = e_{k-1}, \qquad V_j = e^{\pi i/q_j} S_j .$$
Then $U_j, V_j$ are unitary, $V_j U_j = \omega_j U_j V_j$, $U_j^{q_j} = I$ and $V_j^{q_j} = -I$. For
$A_j = U_j + V_j$ the characteristic polynomial is exactly $z^{q_j}$: in $\det(zI - U_j - V_j)$ only the
all-diagonal permutation and the full cycle contribute, the former giving $\prod_{k<q_j}(z -
\omega_j^k) = z^{q_j} - 1$ because $\omega_j$ is primitive, the latter giving minus the product of the
cyclic weights, that is $-e^{\pi i} = +1$. So $A_j^{q_j} = 0$ by Cayley and Hamilton, and every
empirical eigenvalue measure is $\delta_0$. Conjugating the pair by an independent Haar unitary makes
the family random without changing norms, traces, nilpotency or eigenvalues.

The strong-convergence step is the one the record itself flags, and it is argued in two ways. The first
maps the universal irrational rotation C*-algebra $A_\theta$, generated by unitaries $u,v$ with $vu =
e^{2\pi i\theta}uv$, into the norm quotient $\mathcal{Q} = \prod_j M_{q_j}/\bigoplus_j M_{q_j}$, the
direct sum being the sequences whose operator norms tend to zero. The classes of $(U_j)$ and $(V_j)$
satisfy the irrational relation exactly because $\omega_j \to e^{2\pi i\theta}$, so universality gives a
unital homomorphism, simplicity of $A_\theta$ makes it injective, hence isometric, and since the
quotient norm of a bounded sequence is its limsup norm,
$$\limsup_j \|P(U_j, V_j, U_j^*, V_j^*)\| = \|P(u,v,u^*,v^*)\|$$
for every noncommutative polynomial $P$ in the generators and their adjoints; applying this to every
subsequence upgrades the limsup to a limit. Because an injective homomorphism is completely isometric,
amplifying to $M_D(A_\theta)$ covers Definition 1.1's fixed matrix coefficients. The second route
avoids simplicity: the lower bound
$\|P_j\| \ge [(\mathrm{tr}_D \otimes \mathrm{tr}_{q_j})((P_j^*P_j)^m)]^{1/2m}$, with $j \to \infty$ then
$m \to \infty$, gives $\liminf_j \|P_j\| \ge \|P\|$ by faithfulness of the limiting trace, while
complete contractivity of the quotient map gives the matching limsup. The normalised traces converge to
the canonical irrational-rotation trace: every fixed word is a phase times $U_j^a V_j^b$, the shift has
no diagonal entries for $b \ne 0$ and large $j$, and for $b = 0$ the geometric sum of $\omega_j^{ak}$
vanishes once $q_j > |a|$.

Which limit's Brown measure is the second half of the obligation, and it is the half a reader should
check first, because the whole mismatch rests on it. The 12 September lane recorded that Theorem 11.1
of the cited paper gives the spectrum of $u+v$ as the closed disk at $\lambda = 1$, and that Theorem
12.2 gives the Brown measure of $u+v$ as Haar measure on the unit circle at $\lambda = 1$, by a
separate proof in the same paper. The finite empirical measures are all $\delta_0$; Haar measure on the
circle is not $\delta_0$; so strong convergence does not force empirical Brown-measure convergence, and
the same example also blocks a universal lower bound on the spectral radius, since every $A_j$ has
spectral radius zero while $u+v$ has spectral radius one. On the citation: the proof packet attributes
the two theorems to Fang, Jiang, Lin and Xu, *On generalized universal irrational rotation algebras and
the operator u+v*, arXiv:1210.4771, Theorem 12.2, and names the question's own source as van Handel,
*The strong convergence phenomenon*, arXiv:2507.00346v2, Section 6.9, pages 69 to 70. A note written on
12 September gave the same theorem numbers with the author list spelled Fan, Jekel, Liang and Xu and no
title or identifier attached. The packet's attribution is the one carrying a title and an arXiv number
that can be checked, so it is the reading this report follows; the other spelling is treated as a slip.
Verifying the paper against its identifier remains part of the obligation below, because an attribution
with an identifier is still an attribution nobody has opened.

So the exact obligation is: confirm, in the paper the theorem numbers actually belong to, that the
$\lambda = 1$ specialisation is the one that applies to the pair $(u,v)$ built from this $\theta$, and
that the Brown measure there is of $u+v$ in the tracial von Neumann algebra generated by that pair
rather than of a related operator in a different normalisation; and independently confirm the isometry
of the quotient homomorphism, together with the primitive-root sign in the determinant, which is the
step that produces $z^{q_j}$ rather than $z^{q_j} - 2$. The packet lists those same items as its
load-bearing obligations. What is not claimed: the construction does not refute the conjecture for
independent-entry ensembles, for free limits, or for holomorphic polynomials in independent Ginibre
matrices, and the record notes that Yi Han's June 2026 paper, arXiv:2606.01664, claiming the last of
these, is compatible with this example. The two members of the random pair are dependent, and the
packet says so; the single random matrix $Q_j A_j Q_j^*$ is already a counterexample for a one-variable
polynomial.

Verification state, verbatim: the problem row reads
`verification: primary_statement_checked_with_scope_caveat`, the attempt reads
`verification: author_checked_limited_argument`, `independent_review: none`, `novelty: not_claimed`, and
its obstruction field reads "No gap presently identified in the literal-general-scope construction, but
there is no independent review and no novelty claim." A scoped parent review receipt is recorded with
SHA256 beginning `509f76b5e525eae2`; the packet itself states that because the parent contributed to the
amended proof, the amended argument still requires a different independent reviewer. Closeness rank 2.

### P0174, the sharp diameter threshold for free Brownian unimodality, and the Hasebe and Ueda normalisation fork

Source: Hasebe and Ueda, *Large time unimodality for classical and free Brownian motions with initial
distributions*, ALEA 15 (2018), 353 to 374, Problem 3.3; archived arXiv:1710.08240v2, PDF page 6. The
exact question: what is the optimal universal constant $C > 0$ such that $\mu \boxplus S(0,t)$ is
unimodal for all $t \ge C D_\mu^2$ and all compactly supported $\mu$, where $S(0,t)$ is the centred
semicircle law of variance $t$ and $D_\mu$ is the diameter of the support? The source proves $C \le 4$
and prints $2 \le C \le 4$.

What is proved, at candidate stage: the answer is $C = 1$, attained. The upper bound rests on a
Cauchy-profile lemma. For $R > 0$ put $F_R(u) = \int d\mu(x)/((x-u)^2 + R^2)$. Claim: $F_R$ has no
local minimum of value at most $1/D^2$. At a stationary point $u$ with $F_R''(u) \ge 0$, set $y = R^2$
and tilt, $dQ(x) \propto ((x-u)^2+y)^{-2} d\mu(x)$, so that stationarity reads $E_Q(X-u) = 0$. With
$a = E_Q(X-u)^2$ and $b = E_Q(X-u)^4$ the two moment inequalities for a centred variable supported in
an interval of length $D$ are
$$a \le D^2/4, \qquad b + 3a^2 \le D^2 a,$$
the first from $E[(X-l)(h-X)] \ge 0$ together with $-lh \le D^2/4$, the second from the pointwise bound
$(X-X')^4 \le D^2 (X-X')^2$ for an independent copy, which on taking expectations gives $2b + 6a^2 \le
2D^2 a$ and fixes the coefficient 3 exactly. The second derivative is
$$\frac{F_R''(u)}{2Z} = 3 - 4y\, E_Q \frac{1}{(X-u)^2+y},$$
so Jensen and $F_R''(u) \ge 0$ force $1/(a+y) \le 3/(4y)$, that is $y \le 3a$. The normalisation of $Q$
gives the exact reciprocal identity $1/F_R(u) = (b + 2ay + y^2)/(a+y)$, and therefore
$$\frac{1}{F_R(u)} - D^2 \le \frac{(y-3a)(y+a) + (4a - D^2)y}{a+y} \le 0,$$
both summands being nonpositive under $y \le 3a$ and $4a \le D^2$. Equality forces $y = 3a$ and
$4a = D^2$, hence $Q$, and then $\mu$, symmetric Bernoulli on $u \pm D/2$, where the point is a strict
maximum; so every local minimum has value strictly above $1/D^2$ and the boundary case $t = D^2$ is
included. Feeding this into Biane's parametrisation, in which $p_t(\psi_t(u)) = v_t(u)/(\pi t)$ with
$v_t$ the positive solution of $F_{v_t(u)}(u) = 1/t$, shows every positive density level has at most two
preimages, which is the source's own unimodality criterion. Sharpness comes from symmetric Bernoulli
on $\{-c,c\}$: for $c^2 < t < 4c^2$ implicit differentiation gives
$$v_t''(0) = \frac{4c^2 - t}{t\sqrt{t - c^2}} > 0,$$
a strict interior local minimum of the density, so unimodality fails for any proposed $C < 1$.

The normalisation fork is the obligation, and it is not a technicality. The source's own sentence reads
that for symmetric Bernoulli on $\{-1,1\}$ the free convolution is unimodal if and only if $t \ge 4$,
and that since $D_\mu = 2$ one concludes $2 \le C \le 4$. But the condition is $t \ge C D_\mu^2 = 4C$,
so unimodality exactly for $t \ge 4$ forces only $C \ge 1$; the printed 2 is what one gets by dividing
4 by $D_\mu$ rather than by $D_\mu^2$. The 8 September check re-derived the Bernoulli threshold inside
the source's own frame, using the source's own Lemma 3.1 criterion: for symmetric Bernoulli, $F_R$ has a
local minimum at $0$ of value $1/(1+R^2)$ exactly when $R^2 < 3$, and a third solution of $F_R = 1/t$
appears precisely when $1/(1+R^2) < 1/t$, that is when $t < 1 + R^2 < 4$, so the equation has at most
two solutions for every $R$ if and only if $t \ge 4$. The source's threshold and its $D_\mu = 2$ are
both right; what does not follow is the step to $C \ge 2$.

What is missing is the resolution of the fork, and it has exactly two branches. Either the source
normalises $D_\mu$ as a radius somewhere that the archived text does not show, in which case its own
$C \le 4$ would read as $C = 4$ exactly rather than as a bracket, and the candidate theorem would be a
restatement of the source's own sufficient constant rather than an improvement of it; or there is a
second example elsewhere in the paper supplying $C \ge 2$ that the check did not find, in which case
the candidate theorem contradicts the paper and one of the two is wrong. The check's own words are that
that fork, not the arithmetic slip, is the thing to settle before publishing anything. Alongside it
sits the citation obligation: search the papers citing ALEA 15 (2018) 353 to 374 for Problem 3.3. A
bounded author search on the same day returned only the paper itself, its repository copies and
adjacent unimodality work by the same group, which is not a clearance.

A later result on the same row is recorded and is separate from the threshold: for $t > D^2$ the mode
$m_t$ of $\mu \boxplus S(0,t)$ is unique and its density satisfies
$$p_t''(m_t) \le -\frac{t - D^2}{4\pi (t - D^2/4)^{5/2}},$$
sharp for every $t > D^2$, with equality for $D > 0$ forcing $\mu$ to be a translate of the equal law
on $\{-D/2, D/2\}$. Its status in the record is "complete author-derived proof with exact-algebra and
numerical controls; not independently refereed, not novelty-cleared, not fully formalized in Lean",
with 5 exact symbolic identities, 28 atomic-law cases at 80 digits and 7 finite-difference checks;
compact support is essential and it is not a theorem for arbitrary finite-variance inputs.

Verification state, verbatim: the problem row reads
`verification: author_checked_not_independently_reviewed`; the attempt reads
`verification: author_checked_complete_candidate`, `novelty: unverified`, and the obstruction field
reads "No mathematical gap currently identified in the full written candidate. Later-literature novelty
is unverified and there is no independent proof review. Check the reweighting normalization, Jensen
direction, equality case, and exact source density assumptions before promotion." Closeness rank 1,
because the obligation is a reading and a citation search rather than a new estimate.

### D0039, Virag's Question 1: the row that was wrongly excluded and has to go back on the list

Source: Virag, *Operator limits of random matrices*, ICM 2014, arXiv:1804.06953, Question 1 (Spectral
measure and multiplicative cascades), PDF page 6. Verbatim from the archived source: "Does the
beta-Hermite measure and the Gaussian multiplicative cascade measure with the same Hausdorff dimension
have the same fractal spectrum?" The object is the spectral measure at the first coordinate of the
Jacobi matrix of the source's Theorem 4.1, the rough version of the standard normal whose Hausdorff
dimension Breuer, Forrester and Smilansky showed is almost surely $(1 - 2/\beta)_+$ and which is pure
point for $\beta < 2$.

The ledger row D0039 records `result_status: not_attempted_resolved`, `current_status:
resolved_in_literature` and `admitted: false`, citing Chhaibi and Najnudel, arXiv:1904.00578, Journal
of the European Mathematical Society 28 (2026) 1 to 77. That exclusion fails. What the cited paper
proves is an exact identification of Kahane's Gaussian multiplicative chaos on the circle with the
circular beta ensemble, with $\gamma = 2/\beta$ for $\gamma \le 1$, that is $\beta \ge 2$. That is the
circular analogue of a different measure. The question names the beta-Hermite measure. The row's own
`status_search` field quotes a search summary saying the paper "answers positively a question raised by
Virag on the fractal spectrum of a random measure constructed from CbetaE" and then records the row as
resolved while noting a caveat about exactly this point; the caveat was right and the disposition did
not follow it.

So the disposition should be reversed and the problem re-admitted as open, with Chhaibi and Najnudel
recorded as the closest known relative and as the obvious first thing to try. The exact obligation is
the transfer: the two ensembles share the $\mathrm{Sine}_\beta$ bulk limit, so the identification of the
chaos measure with the circular ensemble's spectral measure is expected to carry over to the
beta-Hermite spectral measure, but carrying it over means producing, for the beta-Hermite Jacobi matrix,
the analogue of whatever coupling or exact identity the circular proof uses, and then computing the
multifractal spectrum of the transported object rather than of the circular one. Nobody has read the
paper's proof for that purpose; the record states that only the abstract and search summaries were read.

Two things about this row generalise, and the 8 September audit recorded both. The check that catches
the error is to compare the objects by name: what does the source's question name, and what is the
cited theorem about? "beta-Hermite" against "on the circle" caught this one; "more general ZRP's"
against "arbitrary bounded nondecreasing rate" confirmed a good exclusion elsewhere. And the
operational rule derived from it is not to distrust all exclusions but this: when a search summary
carries any hedge about scope, that row must be read against the source before it is discarded. The
full score on intake D's exclusion list, after all eight were checked, is seven hold and one is wrong,
the wrong one being this row, and it was also the only one whose own `status_search` had recorded a
caveat.

Verification state, verbatim: the row reads `verification: unreviewed`, and its `resolved_by` field
carries its own caveat, "flagged rather than certified: the source's Question 1 is phrased for the
beta-HERMITE measure while Chhaibi-Najnudel work with the CIRCULAR ensemble; the two share the
Sine_beta bulk limit, so the transfer is expected but I did not verify it, and I read only the abstract
and search summaries, not the paper (bounded recall)." Closeness rank 2: the mechanism is identified
and named, and what is missing is one transfer argument of known shape.

### E0064, Theorem 6 for strictly non-Volterra operators in four or more types

Source: the 2009 survey of open problems on quadratic stochastic operators, Problem 11, PDF page 7. A
quadratic stochastic operator is strictly non-Volterra if $P_{ij,k} = 0$ whenever $k \in \{i,j\}$. For
$m = 3$ every such operator has the form
$$x' = \alpha y^2 + c z^2 + 2yz, \quad y' = a x^2 + d z^2 + 2xz, \quad z' = b x^2 + \beta y^2 + 2xy,$$
with $a + b = c + d = \alpha + \beta = 1$, and the source's Theorem 6 states that (1) for all parameter
values the operator has a unique fixed point, which is not attractive, and (2) the operator has
2-cycles and 3-cycles depending on the parameters. The question: is Theorem 6 true for $m \ge 4$?

Three attempts are on the record and together they answer more of it than any one of them.

The spectral half has a clean mechanism. Strict non-Volterra means the diagonal of the derivative
vanishes identically, since $\partial V_k/\partial x_k = 2\sum_j P_{kj,k}x_j = 0$, so
$\operatorname{tr} DV(x) = 0$ at every point. Since $V$ is homogeneous of degree two, Euler's identity
gives $DV(x^*)x^* = 2V(x^*) = 2x^*$ at a fixed point, so $2$ is always an eigenvalue with the radial
direction as eigenvector. Zero trace then forces the remaining $m-1$ eigenvalues, the ones acting on the
tangent space of the simplex and hence the ones that decide attractiveness, to sum to $-2$, so at least
one has modulus at least $2/(m-1)$. At $m = 3$ that bound is exactly $1$, which reproduces Theorem 6's
non-attractiveness; for $m \ge 4$ it drops below $1$ and excludes nothing. That is a reason to expect
failure, not a failure.

The failure was then exhibited. For the symmetric equiprobable family $P_{ii,k} = 1/(m-1)$ for $k \ne
i$ and $P_{ij,k} = 1/(m-2)$ for $k \notin \{i,j\}$,
$$V_k - V_l = \frac{(x_l - x_k)\left[2 - \frac{m(x_k + x_l)}{m-1}\right]}{m-2},$$
so the coordinate diameter contracts by a factor at most $(2m-1)/(m-1)^2 < 1$ for $m \ge 4$ and every
orbit converges to the barycentre. The unique fixed point is therefore globally attracting and clause
(1) of Theorem 6 fails from $m = 4$ onwards. Prior art is named in the record: Jamilov, Ladra and
Mukhitdinov, Qualitative Theory of Dynamical Systems 16 (2017) 645 to 655, online 2016, study exactly
this family, so this half is recorded as literature-resolved rather than as an original result.

The uniqueness half was then refuted for $m \ge 5$ by an explicit operator. On five types, put the
symmetric three-type structure on the face $\{1,2,3\}$ ($P_{ii,k} = 1/2$ for the two other $k$ in the
face, $P_{ij,\mathrm{third}} = 1$), together with $P_{i4,5} = P_{i5,4} = 1$ for $i \le 3$, $P_{44,5} =
P_{55,4} = 1$, and $P_{45,k} = 1/3$ for $k \le 3$. Then both $p = (1/3,1/3,1/3,0,0)$ and $q =
(1/9,1/9,1/9,1/3,1/3)$ are fixed, in exact rational arithmetic: $V_k(q) = (1/81 + 1/81)/2 + 2/81 +
(2/3)(1/9) = 1/9$ for $k \le 3$ and $V_4(q) = 2(1/3)(1/3) + 1/9 = 1/3$. The tangential Jacobian
eigenvalues are $(-2,-1,-1,2)$ at $p$, index $-1$, and $(-4/3,-1/3,-1/3,0)$ at $q$, index $+1$, so
neither is attractive. The structural reason generalises: an invariant three-face carries the unique
fixed point of its own three-type restriction by Theorem 6 itself, two invariant triples must be
disjoint because a shared pair would have to land in two different third types, so $m \ge 6$ admits two
invariant faces and hence at least two fixed points.

The exact obligation that remains is uniqueness at $m = 4$. An index count would settle it if every
fixed point had index $+1$, but the five-type example shows that a saddle of index $-1$ can occur, so a
proof has to use the dimension rather than degree theory alone; that was not attempted. Clause (2) of
Theorem 6, the existence of 2-cycles and 3-cycles in higher dimension, is untouched. Prior art beyond
the source and the 2017 paper was not searched.

I re-ran the numerical half of this row while writing. Generating strictly non-Volterra operators with
Dirichlet weights on each admissible set and solving $V(x) = x$ on the affine hull of the simplex from 80
random starts per operator, 200 four-type operators each produced exactly one fixed point in the
simplex, and 60 five-type operators likewise produced exactly one each; the explicit five-type operator
above produced exactly two, and both $p$ and $q$ satisfy $V(x) = x$ to machine precision with the row
sums of $P$ exactly one. So the record's two statements survive an independent replication: uniqueness
at $m = 4$ is numerically robust and is not a theorem, and the five-type counterexample is a special
operator rather than typical behaviour. A finite search of this kind proves nothing: 200 random
operators say nothing about the operators the search does not reach.

Verification state, verbatim: the row reads `verification: unreviewed` with `result_status:
candidate_partial_counterexample`, the `status_note` reading "2026-09-09: non-attractiveness clause of
Theorem 6 fails for m>=4 (globally attracting symmetric family; Jamilov-Ladra-Mukhitdinov 2016/17);
uniqueness/cycles in general still open" and the `status_search` update reading "UPDATE 2026-09-11:
uniqueness clause refuted for m >= 5 (E0064-A003, explicit 5-type example, exact); m = 4 open,
numerically unique". Closeness rank 1 for the $m = 4$ clause, rank 4 for the cycle clause.

### G0014, the Bramson correction for threshold cascades on unimodular random trees

Source: Kumar and Dudeja, threshold cascades of interacting diffusions on unimodular random trees,
arXiv:2608.21125 (21 August 2026), Conjecture 3.2, Section 3.2, PDF page 4. In the setting of the
source's Theorem 2.1, which represents the cascade by a supercritical branching random walk with tilt
parameter $\theta^*$, speed $c^*$ and derivative martingale $\partial W_n$, the conjecture is that
$\partial W_n$ is uniformly integrable, equivalently that $\partial W_\infty > 0$ almost surely on
survival, and that consequently the time-indexed front obeys
$$F(t) = c^* t - \frac{3}{2\theta^* c^*}\log t + O_P(1),$$
with the recentred front tight and converging to a randomly shifted Gumbel decorated point process, the
shift a multiple of $\log \partial W_\infty$, exactly as for branching Brownian motion. The source's
Programme 3.3 lists three ingredients and says the $x\log^2 x$ moment condition on the offspring point
process is the missing one.

What is on the record is a reduction to a single hypothesis check. Uniform integrability of the
derivative martingale of a branching random walk holds if and only if the offspring point process
satisfies the $x\log^2 x$ condition, in the boundary-case normalisation; the record attributes the
sufficiency to Biggins and Kyprianou and to Aidekon, and the equivalence to Chen 2015. So the
conjecture's first half becomes a theorem as soon as the cascade's offspring point process is shown to
satisfy $E[X\log_+^2 X] < \infty$ with
$$X = \sum_{\text{children}} e^{\theta^* \Delta},$$
$\Delta$ the displacement. If the displacements are bounded by some $M$ then $X \le N e^{\theta^* M}$
with $N$ the offspring count, and $E[N\log^2 N] < \infty$ follows at once from the source's own
exponential-moment hypothesis on $N$. Given the first half, the second half, the Bramson delay and the
decorated Gumbel limit, needs the Aidekon and Madaule programme for branching random walks adapted to
the cascade's spine structure, which the source states is available from its own reference [1, Appendix
A].

The obligation is exactly one reading. What is missing is whether the displacements in the hypotheses of
the source's Theorem 2.1 are bounded. The attempt says so in as many words: "I did not read Theorem
2.1's hypotheses to confirm whether displacements are bounded; the row's status depends on that one
check." If they are bounded, the first half of Conjecture 3.2 follows from published results plus the
source's own hypothesis and the row is a short note, not a theorem. If they are unbounded, the
$x\log^2 x$ condition needs a separate tail estimate on $\sum e^{\theta^*\Delta}$, and that estimate is
the real content, because the exponential tilt can turn a light displacement tail into a heavy tail for
$X$.

Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`, and the row's
`status_search` notes "Source (2026-08-21) states it as the missing step of its Bramson programme. Not
in the earlier ledgers... No other search run." Closeness rank 1.

### G0015, the continuum random tree limit with a continuous type space

Source: Kumar and Dudeja, arXiv:2608.21125, Conjecture 7.2, Section 7, PDF page 8. Under the hypotheses
of the source's Theorem 6.1 at criticality $\rho(K) = 1$, with the additional exponential-moment
hypothesis on the offspring count, the critical cluster conditioned on having $n$ vertices, with graph
distance rescaled by $\Sigma_c/\sqrt n$, converges in the Gromov, Hausdorff and Prokhorov sense to
Aldous' continuum random tree, with an explicit constant $\Sigma_c$ built from the offspring variance
and the tilted stationary law. The source's Programme 7.3 names the obstacle: the type space is the
Polish space $\mathbb{R}$, or $D \times \mathbb{R}$, not a finite set, so Miermont's finite-type
invariance principle does not apply directly, and the missing input is a tightness estimate uniform in
the discretisation mesh.

What the attempt supplies is a literature route that appears to make the conjecture a corollary. For
multitype Galton-Watson trees with a general Polish type space and a spectral gap for the mean-offspring
kernel, the continuum random tree limit can be obtained by the Lukasiewicz path and height process
route of the single-type theory with the types projected away: under the spectral gap the total-progeny
walk is a Markov additive process of finite variance, and de Raphelis, *Scaling limit of multitype
Galton-Watson trees with infinitely many types* (2017), already handles infinitely many types under a
spectral-gap and moment condition, producing the continuum random tree with an explicit constant. The
attempt records that the conjecture's $\Sigma_c$ should match his constant.

The obligation is to check de Raphelis's hypotheses against the cascade's kernel $K$, and the attempt
names the place it is likely to fail: his conditions include a Doeblin-type condition on the type
kernel together with moment bounds, and the $D \times \mathbb{R}$ type space with a diffusion coordinate
may fail the Doeblin condition. So the work is either to verify Doeblin for the source's $K$, or, if it
fails, to replace it with the weaker mixing condition that the Lukasiewicz route actually needs, which
is where a new estimate would enter. The attempt was explicit that it had not verified anything against
the source's exact hypotheses in that session.

Verification state, verbatim: `result_status: attempted_unsolved`, `verification: unreviewed`; the
result field reads "A literature route (de Raphelis 2017) that appears to cover the conjecture's
setting... Not verified against the source's exact hypotheses in this session." Closeness rank 1 in the
sense that the next step is a hypothesis comparison, rank 3 if the Doeblin condition fails.

### C0062, the maximal-dimension Young diagram for finite n

Source: Romik, *The surprising mathematics of longest increasing subsequences*, Section 1.18
discussion, page 74. The question, in three parts: for finite $n$, describe the shape of maximal
dimension, that is the partition of $n$ maximising the number of standard Young tableaux, explicitly or
by an efficient algorithm; prove it is unique; and improve the asymptotic bounds on the maximal
dimension.

The uniqueness part cannot be true as stated, and the reason is an identity, not a counterexample. By
the hook length formula $\dim\lambda = n!/\prod_{\text{hooks}} h$, and conjugation preserves the
multiset of hook lengths, so $\dim\lambda = \dim\lambda'$ for every $\lambda$. Uniqueness can therefore
only mean uniqueness up to conjugation, and the source's question needs that qualifier. With the
qualifier, exact enumeration over all $p(n)$ partitions confirms it for every $n \le 40$, where
$p(40) = 37{,}338$: for each such $n$ the maximiser is either a single self-conjugate shape, which
happens at $n = 1, 3, 5, 6, 8, 10, 12, 15, 17, 21, 23, 27, 30, 34, 36, 38$, or exactly one conjugate
pair, and no tie between non-conjugate shapes occurs.

I replicated that computation independently up to $n = 30$ while writing, with the hook length formula
in exact integer arithmetic over all partitions. The maximiser is unique up to conjugation at every $n
\le 30$, with no other ties, and the self-conjugate values in that range agree with the list above,
including the pattern of long gaps: 12, 15, 17, 21, 23, 27, 30. The maximal dimensions grow as one
expects, from 7,700 at $n = 12$ to 1,865,134,921,890,240 at $n = 30$. A check to $n = 30$ or to $n = 40$
proves nothing about all $n$; enumeration cost grows like $p(n)$, which is exponential in $\sqrt n$, so
the method has a ceiling not far above 40.

The obligation is a structure theorem for the discrete maximiser. What is missing is any monotonicity or
exchange property along paths in the partition lattice: the attempt's obstruction field records that
the dimension is not unimodal along natural paths, which is exactly why enumeration and not local
search is being used, and why no efficient algorithm is known. Asymptotically the maximiser approaches
the Vershik, Kerov, Logan and Shepp limit shape, so the asymptotic part of the source's question is
about the second-order correction to that shape and to $\log\dim$, on which nothing is recorded here.

Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`; the
independent check reads "Conjugation preserves the multiset of hook lengths; the enumeration used exact
integer arithmetic over all p(n) partitions (p(40) = 37338)." Closeness rank 1 for the uniqueness
clause as corrected, rank 4 for the description and the algorithm.

### C0033, concavity of the entropy of determinantal measures in the kernel

Source: Lyons, *Determinantal probability: basic properties and conjectures*, Conjecture 2.6, page 5,
and Conjecture 5.3, page 22. The finite statement: for positive contractions $Q_1, Q_2$ on
$\ell^2(E)$ with $E$ finite,
$$\operatorname{Ent}(P_{(Q_1+Q_2)/2}) \ge \tfrac12\left(\operatorname{Ent}(P_{Q_1}) +
\operatorname{Ent}(P_{Q_2})\right).$$
The row originally described this as equivalent to Conjecture 5.3, concavity of the entropy rate
$H(P_f)$ of a stationary determinantal process in its symbol; attempt C0033-A002 corrects that to an
implication. Conjecture 2.6 implies Conjecture 5.3 by taking limits of finite restrictions; the converse
is not claimed and is not known, and the numerical evidence below is evidence for Conjecture 2.6 only.

What is proved is a set of exact special cases: for $|E| = 1$ the measure is Bernoulli and the entropy
$h(q)$ is concave; for commuting diagonal kernels the measure is a product and
$\operatorname{Ent} = \sum_i h(q_i)$ is concave; and for $Q_2 = I - Q_1$ the midpoint is $I/2$, whose
entropy $|E|\log 2$ is the maximum possible, so the inequality is trivially true there. The identity
that makes the finite entropy computable is
$$P_Q(A) = \det(I-Q)\det(J_A), \qquad J = Q(I-Q)^{-1},$$
and with it the entropy is an exact finite sum over subsets. Numerically, 1,440 random pairs of
symmetric positive contractions in dimensions 2 to 6 with spectra in $(0.02, 0.98)$ gave a positive
concavity gap in every trial, the smallest gap being $8.5\times 10^{-4}$ and occurring in dimension 2.

The obligation is the $2\times 2$ case, and the numerics say why. Since the minimum gap over 1,440
trials was attained in dimension two, dimension two is where the inequality is tightest and therefore
where a proof has to start; there the measure has four atoms with explicit determinants, so the
statement is an inequality between four-term entropies in the entries of two $2\times2$ positive
contractions. What is missing is any analytic argument beyond diagonal kernels: the obstruction field
records "No analytic argument beyond diagonal kernels; the 2x2 case is the natural next target."
Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`, with the
independent check reading "Probabilities summed to 1 within 1e-8 in every trial and were non-negative."
Closeness rank 1.

### C0034, a coupling of determinantal projection measures with the union marginal

Source: Lyons, Question 2.8, page 6. If $H = H_1 \oplus H_2$ is an orthogonal decomposition inside
$\ell^2(E)$, is there a coupling of $P_{H_1}$ and $P_{H_2}$ whose union has law $P_H$?

The first step is exact and reduces the question to a linear feasibility problem. Since $|X_1| = \dim
H_1$, $|X_2| = \dim H_2$ and $|X_1 \cup X_2| = \dim H$ almost surely, any such coupling has $X_1$ and
$X_2$ disjoint almost surely, so the question is whether the transportation polytope with marginals
$P_{H_1}$, $P_{H_2}$ and the disjoint-union marginal $P_H$ is nonempty. Equivalently it asks for a
Markov kernel from $P_H$ to pairs, a random rule splitting a $P_H$-sample $C$ into $(C_1, C_2)$ with the
right marginals. The record then reports the polytope nonempty in 1,360 random instances with $|E| \in
\{3,\dots,6\}$ over all dimension splits, in generic instances with $|E| = 7, 8$, in Fourier-mode
subspaces on cycles of length 5 to 8, and in star-space splits in the edge space of $K_4$, that is for
uniform spanning tree kernels.

Two negative facts are exact and worth keeping. The naive canonical rule, sample $X_1$ from $P_{H_1}$
conditioned on $X_1 \subseteq C$ and set $X_2 = C \setminus X_1$, does not give the correct marginal for
$X_2$ in general; this was checked directly at $|E| = 4$. So whatever the coupling is when it exists, it
is not the conditional one.

The obligation has two halves, and attempt C0034-A002 states the first of them as a correction of its
own predecessor's wording. HiGHS reported minimum total constraint violation $0.0$ on every instance,
in double precision; that is numerical evidence and not an exact feasibility certificate. What is
missing first is a rational linear program, or a feasible point verified in exact arithmetic, on
rational-kernel instances. That is finite and has not been done. What is missing second is a general
construction, and here the record offers no mechanism at all beyond the observation that the naive one
fails. Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`;
`correction_note` on A001 reads "Codex review 11:15: floating-point LP feasibility is not an exact
certificate." Closeness rank 1 for the certificate, rank 4 for the construction.

### C0036, the Fuglede and Kadison bounds for equivariant determinantal processes

Source: Lyons, Conjecture 5.7, page 23. For every $\Gamma$-equivariant positive contraction $Q$ on
$\ell^2(\Gamma)$, the determinantal measure $P_Q$ stochastically dominates the product measure of
density $\mathrm{FK}(Q) = \exp\operatorname{tr}\log|Q|$ and is dominated by the product measure of
density $1 - \mathrm{FK}(I-Q)$, and these bounds are optimal. The source says the conjecture is open
even for finite groups.

What is proved is the same statement with the geometric mean replaced by the harmonic mean, and the
proof is a one-site conditional computation. For a finite group $\Gamma$ and equivariant $Q$ with
$0 < Q < I$, the identity $P_Q(X = A) = \det(I-Q)\det(J_A)$ with $J = Q(I-Q)^{-1}$ gives
$$P(e \in X \mid X \setminus e = B) = \frac{s_B}{1 + s_B}, \qquad s_B = J_{ee} - J_{eB}J_B^{-1}J_{Be} =
\frac{1}{((J_{B \cup e})^{-1})_{ee}},$$
and $s_B$ is nonincreasing in $B$ by Schur complement monotonicity, so its minimum over $B$ is
$1/(J^{-1})_{ee} = 1/((Q^{-1})_{ee} - 1)$. Equivariance turns $(Q^{-1})_{ee}$ into the average of
$1/\lambda_\chi$ over characters, that is $1/\mathrm{HM}$ with $\mathrm{HM}$ the harmonic mean of the
spectrum, so the minimal one-site conditional probability of presence equals $\mathrm{HM}(Q)$. Holley's
inequality, whose hypothesis against a product measure reduces exactly to that one-site statement, then
gives domination of $P_Q$ over the product measure of density $\mathrm{HM}(Q)$, and symmetrically
domination by the product measure of density $1 - \mathrm{HM}(I - Q)$.

Attempt C0036-A002 corrects the identity line of its predecessor and the correction is worth stating
once: A001 wrote $\min_B P(e \in X \mid X\setminus e = B) = 1/(J^{-1})_{ee} = \mathrm{HM}$, which
equates the odds with the probability. The correct chain is $s_{\min} = 1/(J^{-1})_{ee} =
\mathrm{HM}/(1-\mathrm{HM})$ and the minimal conditional probability is $s_{\min}/(1+s_{\min}) =
1/(Q^{-1})_{ee} = \mathrm{HM}(Q)$. The conclusion is unchanged.

Since $\mathrm{HM} \le \mathrm{GM} = \mathrm{FK}$, the whole content of the conjecture is the improvement
from the harmonic to the geometric mean. What is missing is a conditional argument that uses partial
information rather than the worst case: the harmonic mean arises as the minimum of the one-site
conditional probability over all configurations of the rest, and the geometric mean is what one should
get from the average behaviour, so the obligation is an inequality for the conditional probability given
a typical rather than an extremal environment. Numerically the conjecture itself survives: on
$\mathbb{Z}/n$ for $n = 3$ to $6$, 102 random symmetric circulant contractions, a monotone-coupling
linear program certified both conjectured dominations with zero violation in every instance, and on one
$n = 5$ instance raising the product density from $\mathrm{FK}$ to $\mathrm{FK} + 0.01$ already made the
lower domination infeasible, with violation $0.006$, so the bound is sharp there to within $0.01$. The
same exactness caveat as in C0034 applies to those linear programs. Verification state, verbatim:
`result_status: partial_result`, `verification: unreviewed`. Closeness rank 3.

### G0013, Catalano and Lavenant: covered in chapter 10

The conjecture, restated by Schrott, arXiv:2609.10467 (9 September 2026), Conjecture 1.1, quoting
Catalano and Lavenant, Remark 3: with $\lambda$ the uniform law on $[0,1]$, the diagonal and
antidiagonal couplings $(\mathrm{id},\mathrm{id})_\#\lambda$ and $(\mathrm{id}, 1-\mathrm{id})_\#\lambda$
maximise the quadratic Wasserstein distance from the independent coupling $\lambda \otimes \lambda$ over
$\Pi(\lambda,\lambda)$. Schrott proves the Gaussian analogue for all dimensions by the Gaussian
isoperimetric inequality and says the uniform case remains open.

Where this now stands is in chapter 10 and the mathematics is not repeated here. In summary: the
objective is convex and weakly continuous on the weakly compact convex set $\Pi(\lambda,\lambda)$, so a
maximiser is an extreme doubly stochastic measure by Bauer's principle; discretised to $n$ equally
spaced atoms every extreme point is a permutation by Birkhoff, and the discrete problem is a
transportation linear program for each permutation. Exhaustive search over canonical classes under the
symmetry group now reaches $n = 9$: at $n = 8$, 5,282 classes covering all 40,320 permutations, best
objective $W_2^2 = 0.102539$, runner-up $0.098633$, 69 seconds; at $n = 9$, 46,066 classes covering
362,880 permutations, best $0.101204$, runner-up $0.098461$, 426 seconds. The conjecture holds at both,
and in both the runner-up is one adjacent transposition at the end of the permutation away from the
maximiser, the same local structure the smaller cases showed. The obligation is the exchange argument
for general $n$: that any permutation other than the identity and the reversal admits a local move
strictly increasing the objective. Chapter 10 also records the reason the maximiser prints as the
identity alone, which is that the reversal is identified with it under the symmetry used to form
canonical classes, so this is consistent with the earlier finding of two maximisers and not a change to
it. Closeness rank 2.

### G0008, monotonicity of the two-point connection probability on the square lattice

Source: Campos and de Lima, arXiv:2601.00291, abstract and introduction, PDF page 1, and Section 3, PDF
page 4. The source writes that "on the square lattice is an open question to prove that the probability
of the origin being connected to the vertex $(0,n)$ is monotone in $n$", and, after constructing a
transitive graph without the property, that "it remains an open question whether graphs like
$\mathbb{Z}^d$ satisfy the monotonic property or not". The question: for every $p \in (0,1)$, is
$n \mapsto P_p(0 \leftrightarrow (0,n))$ non-increasing on $\mathbb{Z}^2$, and on $\mathbb{Z}^d$? The
source traces it to Hammersley and Welsh, 1965, in first-passage percolation.

What is proved is eventual monotonicity away from criticality, and it comes from Ornstein and Zernike
asymptotics rather than from any percolation-specific monotonicity. For every fixed $p < p_c$,
$$P_p(0 \leftrightarrow x) = C(p, x/|x|)\,|x|^{-1/2}\, e^{-|x|/\xi_p(x/|x|)}\,(1+o(1))$$
by Campanino and Ioffe 2002, so along an axis the two-point function is eventually decreasing; for
$p > p_c$ in two dimensions the same asymptotic holds for the truncated two-point function by Campanino,
Ioffe and Louidor 2010, and $P_p(0 \leftrightarrow (0,n)) = \theta(p)^2 + \text{(truncated term)}$, so
the sequence is again eventually decreasing. Hence: eventual monotonicity at every $p \ne p_c$.

A claim in the first attempt was withdrawn the same day, and the correction is the instructive part.
Attempt G0008-A001 asserted monotonicity for all $n$ at small $p$, on the grounds that
$P_p(0 \leftrightarrow (0,n)) = p^n(1 + O(p))$ with the correction coming from the number of
self-avoiding paths of length $n + 2k$. Attempt G0008-A002 withdrew it: the crude bounds
$p^n \le P_p(0 \leftrightarrow (0,n)) \le \sum_{k \ge n} \mu^k p^k$ give
$$P_p(0 \leftrightarrow (0,n+1)) \le \frac{(\mu p)^{n+1}}{1 - \mu p},$$
which is not below $p^n$ once $\mu^{n+1}p > 1 - \mu p$, that is for all large $n$ at any fixed $p$, with
$\mu = 2.64\dots$ the connective constant. The low-order expansion $P = p^n(1 + a_n p^2 + \dots)$ has
coefficients $a_n$ growing with $n$, so uniformity in $n$ is precisely what the argument does not have.

So there are two obligations and they are different in kind. The first is uniformity in $n$ in the
Ornstein and Zernike ratio: what is missing is a version of the two-point asymptotic whose error term is
controlled from $n = 1$ rather than for $n \ge n_0(p)$, or, failing that, an exact enumeration of
$P_p(0 \leftrightarrow (0,n))$ for small $n$ at intermediate $p$ that either confirms monotonicity on
the range the asymptotics do not reach or finds a violation there. The attempt names exact enumeration
to moderate $n$ as the natural test. The second obligation is at $p = p_c$, where no mechanism is known
at all: the two-point function decays as $n^{-1/4 + o(1)}$ on the triangular lattice and there is no
monotonicity statement to lean on, since the Ornstein and Zernike theory requires a positive mass gap.

I ran the finite test in its cheap form while writing, and it is only suggestive. Sampling bond
percolation on a $61 \times 71$ box with the origin at the centre of the lower part, computing connected
components once per configuration and reading off all the targets $(0,n)$ for $n = 1$ to $12$ from the
same configuration, 4,000 samples at $p = 0.35$ gave the decreasing sequence $0.417, 0.207, 0.108,
0.067, 0.038, 0.025, 0.016, 0.0095, 0.0038, 0.0025, 0.0020, 0.0010$ with standard errors from $0.0078$
down to $0.0005$, and no step increased. At $p = 0.5$, which is $p_c$ for this model, the same run gave
$0.757, 0.657, 0.603, 0.570, 0.535, 0.511, 0.496, 0.479, 0.457, 0.439, 0.432, 0.4315$ with standard
errors about $0.0079$, and again no step increased, although the last step is well inside one standard
error. Two caveats, and they are not small: the box truncates, so at $p_c$ the quantity estimated is the
box connection probability and not the infinite-volume one, and 4,000 samples cannot resolve
differences of order $10^{-3}$. A Monte Carlo run proves nothing about monotonicity; it says only that
no violation is visible at this resolution, and the place a violation would plausibly hide, small $n$ at
intermediate $p$ where the differences are large, is also where the estimate is most reliable, which is
mildly reassuring and no more.

Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`, with A001
carrying the field `corrected_by: "G0008-A002 (same day): the 'all n for small p' claim is withdrawn;
only the large-n Ornstein-Zernike statement stands."` Closeness rank 1 for the small-$n$ half at $p \ne
p_c$, rank 4 at criticality.

### G0005, the Kozma and Nitzan connectivity conjecture in the many-contacts regime

Source: Flammant, arXiv:2609.03492 (7 September 2026), in the proof of Theorem 2.4, Section 2, PDF page
3, restating Kozma and Nitzan's Conjecture 3 in its finite constant-parameter form. For Bernoulli bond
percolation with parameter $p$ on a finite graph $G = (V,E)$: for every $\eta > 0$ there is
$\delta = \delta(\eta) > 0$ such that for every finite $G$, every $A \subseteq V$ and all $o, z \in V$,
if $P[o \leftrightarrow A] > 1 - \delta$ and $P[a \leftrightarrow z] > 1 - \delta$ for every $a \in A$,
then $P[o \leftrightarrow z] > 1 - \eta$. Kozma and Nitzan's Theorem 6 shows this implies
$\theta(p_c, \mathbb{Z}^d) = 0$ for every $d \ge 2$.

What is proved is the conjecture under a bound on the number of contacts, by a union bound with the
Harris and Fortuin, Kasteleyn and Ginibre inequality used in the mixed direction. Write $N_A$ for the
number of $a \in A$ joined to $o$. For fixed $a$ the event $\{o \leftrightarrow a\}$ is increasing and
$\{a \nleftrightarrow z\}$ is decreasing, so
$$P[o \leftrightarrow a,\ a \nleftrightarrow z] \le P[o \leftrightarrow a]\,P[a \nleftrightarrow z] \le
\delta\, P[o \leftrightarrow a],$$
and summing over $a \in A$,
$$P[o \leftrightarrow z] \ge P[o \leftrightarrow A] - \sum_{a \in A} P[o \leftrightarrow a,\ a
\nleftrightarrow z] \ge 1 - \delta - \delta\, E[N_A].$$
So the conjecture holds with $\eta = 2\delta(K+1)$ on every instance with $E[N_A] \le K$, in particular
whenever $|A|$ is bounded and more generally whenever the cluster of $o$ meets $A$ in a bounded expected
number of points.

The open content is exactly the many-contacts regime, and the reason the route dies there is that the
union bound is wasteful by a factor $E[N_A]$, which in the instances that matter is enormous: for a box
in $\mathbb{Z}^d$ with $A$ a face, $N_A$ is of order $n^{d-1}$. What is missing is a statement that
the cluster of $o$, given that it reaches $A$ at all, reaches $A$ at some point $a$ whose own event
$\{a \leftrightarrow z\}$ occurs, that is a Fortuin, Kasteleyn and Ginibre type inequality conditional
on the cluster rather than a bound summed over $a$ separately. The attempt records that this is exactly
Flammant's Conjecture 2.2 with $E_a = \{a \leftrightarrow z\}$, so the natural strengthening of the
route is the next row rather than a repair of this one. Verification state, verbatim:
`result_status: attempted_unsolved`, no `verification` field on the attempt, the problem row reading
`verification: unreviewed`. Closeness rank 3.

### G0004, Flammant's increasing-events boundary-connectivity conjecture

Source: Flammant, arXiv:2609.03492, Conjecture 2.2 (the paper's main conjecture), Section 2, PDF page 2.
For Bernoulli bond percolation with parameter $p$ on a finite graph $G$, with $o \in V$ and $B \subseteq
V$, call an event $A$ increasing with respect to the percolation configuration if
$\omega \mapsto P[A \mid \pi = \omega]$ is increasing on $\{0,1\}^E$, where $\pi$ is the configuration,
so that the event may depend on extra randomness. The conjecture: there is a universal function
$\varphi$ on $(0,\infty)$, independent of $G$, $o$, $B$ and $p$, with $\varphi(\varepsilon) \to 1$ as
$\varepsilon \to 0$, such that whenever $(E_b)_{b \in B}$ are increasing with respect to the
configuration and $P[E_b] \ge 1 - \varepsilon$ for every $b$,
$$P\Big[\bigcup_{b \in B} \big(\{o \leftrightarrow b\} \cap E_b\big)\Big] \ge \varphi(\varepsilon)\,
P[o \leftrightarrow B].$$
The source's Theorem 2.4 shows the conjecture implies $\theta(p_c) = 0$ for every $d \ge 2$, through
Kozma and Nitzan's Theorem 6.

Two supporting cases are on the record, no proof and no counterexample. For $|B| = 1$ both
$\{o \leftrightarrow b\}$ and $E_b$ are increasing, so Harris and Fortuin, Kasteleyn and Ginibre give
$P[\{o\leftrightarrow b\} \cap E_b] \ge P[o \leftrightarrow b]P[E_b] \ge (1-\varepsilon)P[o
\leftrightarrow b]$, and $\varphi(\varepsilon) = 1 - \varepsilon$ works. On the family of graphs where
the connections $o \leftrightarrow b$, $b \in B$, are independent, that is where the routes are
disjoint, with common probability $q$, the adversarial choice $E_b = \{o \leftrightarrow B \setminus
\{b\}\}$ has $P[E_b] \ge 1 - \varepsilon$ only if $(1-q)^{|B|-1} \le \varepsilon$, and then the union
event is $\{N \ge 2\}$ for $N \sim \mathrm{Bin}(|B|, q)$, whose failure
$P[N = 1] = |B|q(1-q)^{|B|-1} \le |B|q\varepsilon$ is at most $\varepsilon\log(1/\varepsilon)(1+o(1))$
times $P[N \ge 1]$; so on that family $\varphi(\varepsilon) = 1 - O(\varepsilon\log(1/\varepsilon))$
works for that $E_b$.

What is missing is either the inequality or a counterexample, and the attempt records what a
counterexample would have to look like: an instance where the origin connects to exactly one boundary
point with high probability, uniformly over many candidates, since that is what makes the union small
while every $P[o \leftrightarrow B\setminus\{b\}\,]$ stays large. Positive association of the connection
events works against exactly that concentration, and the attempt could not build a Bernoulli example
with $P[N = 1 \mid N \ge 1] \to 1$ under those constraints. The row also records the ordering: the
conjecture is strictly stronger than Kozma and Nitzan's Conjecture 3, since the source proves the
implication, so it is at least as hard as G0005 and therefore at least as hard as $\theta(p_c) = 0$.
Verification state, verbatim: `result_status: attempted_unsolved`, problem row `verification:
unreviewed`. Closeness rank 4.

### G0001, the stretched-exponential finite-cluster tail, which is $\theta(p_c) = 0$ in disguise

Source: Cerf, arXiv:2608.23661 (22 August 2026), Conjecture 1.4, Section 1, PDF page 3. For Bernoulli
site percolation on $\mathbb{Z}^d$ with $d \ge 3$ and $C(0)$ the cluster of the origin: for every
$p \in (0,1)$,
$$\theta(p, \mathbb{Z}^d) > 0 \implies \liminf_{n \to \infty} \frac{1}{\ln n} \ln\ln
\frac{1}{P_p(n \le |C(0)| < +\infty)} > 0 .$$
The source's Theorem 1.2 proves that at $p = p_c$ either $\theta(p_c) = 0$ or that liminf is $0$, and
the source writes that "it could be that the correct way to prove that $\theta(p_c, \mathbb{Z}^d) = 0$
is to prove separately theorem 1.3 and conjecture 1.4."

What the attempt establishes is that the conjecture is not a new target. Split by $p$. For $p > p_c$ the
supercritical finite-cluster tail is stretched exponential with exponent $(d-1)/d$, by Kesten and Zhang
1990 for bond percolation, Theorem 8.65 in Grimmett's book, the site version following by the same
Grimmett and Marstrand renormalisation, so the liminf is at least $(d-1)/d > 0$ and the conjecture holds
there. The only case left is $p = p_c$ with $\theta(p_c) > 0$, and there Conjecture 1.4 together with
the source's own Theorem 1.2 gives a contradiction: 1.4 makes the liminf positive, 1.2 makes it zero.
Conversely if $\theta(p_c) = 0$ the $p = p_c$ case is vacuous and the $p > p_c$ case is Kesten and
Zhang. So Conjecture 1.4 is equivalent to $\theta(p_c, \mathbb{Z}^d) = 0$ modulo the supercritical tail
theorem, and the row is a reformulation of the ledger's existing rows C0023 and C0094 rather than a new
problem; the two should be merged, and the only content beyond $\theta(p_c) = 0$ is the site-percolation
version of the supercritical tail bound.

The obligation is therefore $\theta(p_c) = 0$ itself in dimensions $3 \le d \le 10$, and the attempt is
explicit that the reformulation buys nothing: "Nothing beyond theta(p_c) = 0 itself; the reformulation
does not suggest a new route because Theorem 1.2 already consumes the tail information at p_c." The one
genuinely separable piece is the site version of the supercritical stretched-exponential tail, which the
attempt asserts follows by the same renormalisation and did not write out. Verification state, verbatim:
`result_status: attempted_unsolved`, `verification: unreviewed`, `key_identity: "theta(p_c) > 0 and Thm
1.2 => liminf = 0; Conj 1.4 => liminf > 0; contradiction"`. Closeness rank 4.

### P0001, negative correlation in uniform forests, proved for cactus graphs

Source: Grimmett, *Selected problems in probability theory*, Conjecture 4.2, PDF page 8, restated as
Conjecture 1.3 by Tang and Zhang, arXiv:2603.10738v1, March 2026. The exact question: for every finite
simple graph, does its uniform acyclic edge subset have pairwise nonpositive edge covariance? That is,
are distinct edge indicators of a uniform random forest always negatively correlated?

What is proved is the special case of cactus graphs, those in which every edge lies in at most one
cycle, and the proof is a factorisation. In a cactus the cycle constraints occupy disjoint coordinate
blocks, so acyclicity factorises over the cycles and the measure is a product of independent
per-cycle measures. The inequality inside one block is the conditional covariance identity
$$\operatorname{Cov}(f, g \mid H^c) = -\frac{q\,(f_* - a)(g_* - b)}{(1-q)^2},$$
where $H$ is the all-ones event on the cycle, $q = P(H)$, $f_*$ and $g_*$ are the values of the
increasing functions at the all-ones point and $a$, $b$ their means; the right-hand side is nonpositive
because an increasing function's value at the all-ones point dominates its mean. The identity expands
exactly, and a direct count confirms it: for a uniform $m$-cycle the covariance numerator is
$$(2^{m-2}-1)(2^m-1) - (2^{m-1}-1)^2 = -2^{m-2}$$
exactly, giving $-2^{m-2}/(2^m-1)^2$, hence $-2/49$ for a triangle, and the degenerate tree case gives
zero as it must. That identity is exact rather than asymptotic and I re-verified it in integer arithmetic
for $m = 2$ to $11$: the numerator is $-2^{m-2}$ in every case, so the covariances run $-1/9$, $-2/49$,
$-4/225$, $-8/961$ and so on.

The obvious route to the general case is refuted in the same packet, and this is the part worth
carrying. Conditioning on a decreasing event does not in general preserve negative correlation: fair
bits conditioned to avoid $X_1X_2 = X_2X_3 = 1$ have allowed states $000, 100, 010, 001, 101$ and
$\operatorname{Cov}(X_1, X_3) = 1/25 > 0$. So the generic conditioning argument fails, and it fails on
three bits.

What is missing is an inequality that survives overlapping cycles. The obstruction field names the shape
it should have: "Overlapping cycle constraints do not factor; generic conditioning on a decreasing event
fails. Need an inequality using graphic-matroid circuit elimination." That is, one wants a transfer or
exchange step in the graphic matroid, replacing the block factorisation, that produces the covariance
sign from circuit elimination rather than from independence of the constraints.

Verification state, verbatim: the problem row reads `result_status: partial_result`,
`verification: author_checked_special_case_only`; the attempt reads `verification: author_checked`,
`independent_review: none`, `novelty: not_claimed`, and the proof file's own header reads "Target remains
unsolved here. This note proves a special case and refutes an overly broad proof route." The 8 September
audit of the proofs directory records that both computations were checked independently and are correct.
Closeness rank 4.

### P0004, the quenched connective limit: root independence without a limit

Source: Grimmett, *Selected problems in probability theory*, Question 2.3: does $c_n(v)^{1/n}$ converge
almost surely on the supercritical percolation cluster, and independently of the starting vertex $v$?
Here $c_n(v)$ counts self-avoiding walks of length $n$ from $v$ in the open cluster.

What is proved is root independence of the limsup on every infinite connected graph of bounded degree,
by a visiting-time decomposition. For adjacent $v, w$,
$$c_n(v) \le c_{n+1}(w) + \sum_{k} c_k(w)\, c_{n-k}(w),$$
because a walk from $v$ either avoids $w$, in which case prepending the edge $wv$ injects it into walks
from $w$ of length $n+1$, or hits $w$ once at time $k$, in which case reversing the prefix and keeping
the suffix injects it into pairs of walks from $w$; the two cases are disjoint and both preserve lengths.
With $c_m(w) \le C(M+\epsilon)^m$ the bound becomes $[C(M+\epsilon) + nC^2](M+\epsilon)^n$, and the
polynomial factor is invisible at the exponential scale. An annealed upper bound $p\mu$ follows
separately.

What is missing is the existence of the limit, and the obstruction field is precise about why the
standard route is unavailable: "The cut-walk inequality has an environment-dependent endpoint maximum.
No stationary scalar subadditive process or liminf lower bound was obtained." In other words the
inequality above is almost subadditive but its error term depends on the environment near the endpoint,
so it does not produce a stationary subadditive sequence to which Kingman's theorem could be applied,
and nothing in the argument bounds the liminf from below.

The row also labels itself honestly as partly spent: the proof file records that the conclusion, root
independence, is already in Lacoin, arXiv:1203.6051, and that its own annealed bound $p\mu$ is weaker
than Lacoin's strict planar improvement. Verification state, verbatim: `result_status: partial_result`,
`verification: author_checked_special_case_only` on the problem row, `author_checked` on the attempt,
with the file's header reading "author-checked elementary partial result. No novelty claim. The source's
question about existence of a limit remains unsolved here." Closeness rank 4.

### P0389 and P0390, the ARW fixed-mass window obstructions

Source: the 2024 survey on universality for activated random walks, Conjecture 27, PDF page 15, and
Question 28, PDF pages 15 to 16. Conjecture 27 asks one to determine the subcritical linear-variance and
the critical or supercritical subvolume-variance regimes for particle counts in windows of the free-chain
torus configuration; Question 28 asks whether stationary wake-chain configurations have linear window
variance below criticality and a power saving at and above criticality. Both are hyperuniformity
statements: that the variance of the count in a window is of the order of the window volume below
criticality and strictly smaller at and above it.

What is proved is that the literal all-window quantifier is false, by conservation of mass alone, and the
computation is two lines. At step $k$ the free chain has exactly $k$ sleeping particles on $N = L^d$
sites, so for any window $B$ the count satisfies $S_B = k - S_{B^c}$, hence
$$\operatorname{Var}(S_B) = \operatorname{Var}(S_{B^c}) \le \frac{\min(|B|, N-|B|)^2}{4}.$$
Take the proper box $B = [0, L-2]$ times the full remaining coordinate intervals, which leaves only
$L^{d-1}$ sites outside $B$. In $d = 1$ that $B$ has $L-1$ sites and $\operatorname{Var}(S_B) \le 1/4$,
which contradicts any size-uniform lower bound $c(L-1)$ at a fixed positive subcritical density. The
independent check is exact: on a cycle $S_B = k - I_x$ for the single omitted site $x$, so
$\operatorname{Var}(S_B) = \operatorname{Var}(I_x) \le 1/4$, and translation invariance under uniform
driving gives $\operatorname{Var}(I_x) = (k/L)(1-k/L)$ exactly. For the stationary wake chain the same
argument runs under the unique stationary law: the complement-of-one-site window has variance
$\rho_N(1-\rho_N) \le 1/4$ with $\rho_N = k/N$, the whole torus has variance zero, and translation
invariance forces $\sum_y \operatorname{Cov}(I_x, I_y) = \operatorname{Cov}(I_x, k) = 0$.

That last identity is the reason the obstruction is only an obstruction. The exact global cancellation
of covariances is a consequence of fixed mass and says nothing about mesoscopic windows: the comparison
law of uniform $k$-subsets satisfies the same cancellation and yet has
$$\operatorname{Var}(S_B) = |B|\,\rho_N(1-\rho_N)\,\frac{N - |B|}{N-1},$$
which is of volume order whenever $|B| = o(N)$. So finite-volume covariance cancellation is compatible
with linear window variance, and no hyperuniformity follows from it.

What is missing is the statement in the intended regime, which the record identifies as the mesoscopic or
bounded-volume-fraction one: windows $B$ with $|B| \to \infty$ and $|B|/N \to 0$, for which one wants
$\operatorname{Var}(S_B) \asymp |B|$ below criticality and $\operatorname{Var}(S_B) = o(|B|)$ at and
above it, with the critical exponent identified. Neither the variance growth for small windows nor the
critical exponent is settled, and the attempts say so in the same words. The correction to the source is a
quantifier correction, not a refutation of the physics: the source's own statement permits every box with
size-uniform constants, and that is the part that fails.

Verification state, verbatim: both rows read `result_status: candidate_partial_counterexample` with
`verification: author_checked_partial`, `independent_review: none`, `novelty: not_claimed`; P0389's
obstruction field reads "This is a scope counterexample to the unrestricted window quantifier. It does
not settle variance growth for windows small compared with the torus, nor the critical exponent", and
P0390's reads "The literal all-window lower bound is false; the meaningful small-window transition is
unresolved. Exact global covariance cancellation alone cannot prove a subvolume variance bound." The
uniform $k$-subset law is explicitly "not asserted to be the ARW stationary distribution". Closeness
rank 3.

### P0411, the boundary-hole monotonicity and coefficient positivity for ideal Voronoi cells

Source: the 2023 ideal hyperbolic Voronoi tessellation manuscript, Conjecture 7.5, PDF page 48, with
Proposition 5.1 at PDF page 35. The conjecture is a conjunction: establish the proposed
normalised-hole monotonicity, the odd-dimensional positive rational polynomial form, and the
even-dimensional positive power-series form, together with the related decreasing-density behaviour. The
source already gives $d = 3$ explicitly and observes odd-dimensional rationality.

What is proved, and what is refuted, both come from one exact change of variables. Put $n = d-1$ and
$J = 1/H$ with $H$ the boundary-hole probability. After the substitutions $x = e^{-u}z$ and $q = e^{2u}$
the source's exact integral becomes
$$e^{-nu}J = c_d^{-1}\int \left[\sqrt{\tfrac{(q+1)^2}{4} + |z|^2} - \tfrac{q-1}{2}\right]^{-2n} dz .$$
For $z \ne 0$ the bracket strictly decreases in $q$, so $e^{nu}H$ strictly decreases: the monotonicity
clause holds in every dimension. When $n = 2m$ is even, a separate radial substitution gives
$J = e^{2mu}p_m(e^{2u})$ with $p_m$ of degree $m$ and strictly positive rational coefficients, written
in the packet as integer-argument beta integrals; that is the odd-dimensional ($d = 2m+1$) clause.

The even-dimensional power-series clause is where a candidate counterexample appears. In dimension two
the function the clause concerns, $f(u) = e^{-u}/H_2(u)$, has
$$[u^6]f = \frac{61}{240} - \frac{4}{5\pi} < 0,$$
negative because $\pi < 22/7$. So the literal clause, read in the source's displayed distance variable,
fails at the sixth Maclaurin coefficient in $d = 2$. I checked that sign while writing: $61/240 =
0.2541667$ against $4/(5\pi) = 0.2546479$, a difference of $-4.81 \times 10^{-4}$, and the stated
justification is valid with room to spare, since negativity needs only $\pi < 960/305 = 3.14754$ and
$22/7 = 3.142857$. The sixth coefficient was computed three ways, by an
exact reciprocal-cosh recurrence, by direct high-precision differentiation and by Cauchy extraction from
the original angular integral, agreeing to $5.5 \times 10^{-62}$; the polynomial coefficients for
$m = 1$ to $20$ were computed twice, all positive with $p_m(1) = 1$, and twenty high-precision
comparisons against the original angular integral agree below $10^{-45}$ relative error, with the known
$d = 3$ formula recovered.

Two obligations remain and they are of different kinds. The first is a question for the source's authors
rather than a theorem: whether the intended variable is the displayed distance variable or another
normalisation, since a different variable would move the coefficients and could restore positivity. The
second is mathematics: the even-dimensional decreasing-density and median claims beyond the $d = 2$ case
the source already knows are not proved, and nothing in the two substitutions above touches them. The
grouped row therefore stays partial even though two of its three clauses are settled in every dimension.
Verification state, verbatim: `result_status: candidate_partial_counterexample`,
`verification: author_checked_partial`, `independent_review: none`, `novelty: not_claimed`;
`candidate_scope` reads "All-dimensional monotonicity, odd-dimensional polynomial and density/median
proof, plus a d=2 counterexample to positive Maclaurin coefficients; other even-dimensional
density/median questions remain." Closeness rank 2.

### P0429, the largest growing fork-join batch compatible with asymptotic independence

Source: the 2021 survey on queueing at the frontiers of computing, Section 5, PDF page 16. The question:
determine how quickly the number $k(n)$ of tasks per uniformly routed job can grow while the
corresponding $k(n)$ stationary queues remain asymptotically independent. The source credits
$k = o(n^{1/4})$, which comes from fixed-dimensional convergence and therefore does not by itself answer
the growing-dimension question.

What is proved is a sufficient regime under exponential service, by an input coupling plus an emptying
estimate. Fix $k$ tagged servers among $n$. Jobs arrive at rate $\Lambda = \lambda n/k$ and choose a
uniform $k$-subset of servers; if $N$ is the number of tagged servers hit by one arrival then
$$E[N(N-1)] = \frac{k(k-1)\,k(k-1)}{n(n-1)},$$
a hypergeometric factorial moment. Remove the arrivals that hit at least two tagged queues and restore
the lost marginal rates by independent Poisson streams; a union bound over removed and added events is at
most $\tfrac32 \Lambda T\, E[N(N-1)]$, that is at most
$$\frac{3\lambda T k (k-1)^2}{2(n-1)},$$
and the resulting streams are independent with the correct marginal rates, so with independent task marks
and empty initial queues this bounds the total variation distance between the workload paths on $[0,T]$.
Extending the credited coupling to stationary starts costs the stationary emptying tail: total variation
at most $2k\,r(T) + 3\lambda T k(k-1)^2/(2(n-1))$ with $r(T)$ the stationary marginal emptying tail. For
independent exponential service of rate $\mu > \lambda$, a stopped generator calculation gives
$$r(T) \le \left(1 + \sqrt{\lambda/\mu}\right)\exp\left(-(\sqrt\mu - \sqrt\lambda)^2 T\right),$$
and taking $T = 2\log n/(\sqrt\mu - \sqrt\lambda)^2$ yields the sufficient condition
$k = o\big((n/\log n)^{1/3}\big)$. A conditional polynomial tail $r(T) \le CT^{-p}$ gives instead the
exponent $p/(3p+1)$.

So the cubic collision scale is the mechanism, and it is the exponent that is missing. What remains is
the optimal threshold, whether it is at $k$ of order $n^{1/3}$ as this bound suggests, together with the
general-service version, where the exponential emptying tail has to be replaced by whatever the service
law supplies, and the correlated-mark and uniform heavy-traffic versions. The obstruction field lists
exactly these and adds that the basic source coupling is credited, so what is new here is the stationary
extension rather than the coupling. Verification state, verbatim:
`result_status: candidate_partial_counterexample`, `verification: author_checked_partial`,
`independent_review: none`, `novelty: not_claimed`, with 77 hypergeometric and restoration cases, 81
generator identities, nine geometric exponential moments and five polynomial balancing identities checked
exactly, all described in the record as author checks and not independent review. Closeness rank 3.

### P0458 and P0459, the degree law and the concentration of bilateral preference degrees

Source: the 2025 bilateral connectivity paper, Open Problems, PDF page 3, first and second additional
questions. P0458 asks for the limiting law of $(D - E[D])/\sqrt{\operatorname{Var}(D)}$ for a typical
degree in the bilateral preference graph $LK(n,k)$ as the budget $k$ grows; P0459 asks for growth
conditions and quantitative bounds under which the degrees concentrate simultaneously around their mean.

For P0458 what is proved is the limit law in a range of $k$, and the mechanism is an order statistic plus
a Beta central limit theorem. The relevant root order statistic is $X \sim \mathrm{Beta}(k+1, n-k-1)$.
Ignoring internal edges among the root's preferred neighbours gives the conditional law
$D_0 \mid X \sim \mathrm{Bin}(k, 1 - q(X))$ with
$$q(X) = \frac{E[(X-T)_+]}{X}, \qquad T \sim \mathrm{Beta}(k, n-2k),$$
and the error of that simplification is controlled by $E[(D_0 - D)^2/k] = O(k^2/n + k^5/n^2)$. Beta
central limits and explicit moment controls then give
$$\frac{k - D}{\sqrt k} \longrightarrow g(Z), \qquad g(z) = \phi(z) + z\Phi(z),$$
$Z$ standard normal, with convergence of the first two moments; the variance constant is
$v = 1/3 + (\sqrt3 - 2)/(2\pi)$ and the standardised degree limit is $(1/\sqrt\pi - g(Z))/\sqrt v$, which
is not Gaussian. The packet's stated scope is $k \to \infty$ with $k = o(n^{2/5})$, which contains the
source's mean-asymptotic regime $k = o(n^{1/3})$.

For P0459 what is proved is a sufficient superlogarithmic regime, by thresholding the edge weights. Put
$\delta = \sqrt{6k\log n}$ and assume $k > 2\delta$; threshold the edge weights at $t = (k-\delta)/(n-1)$
so that each threshold degree $B_v$ is binomial with mean $k - \delta$. Chernoff and a union bound give
$k - 2\delta \le B_v \le k$ for all vertices with probability at least $1 - 2/n^2$, and on that event
every threshold edge is preferred at both endpoints, so $k - 2\delta \le D_v \le k$ simultaneously.
Hence $k/\log n \to \infty$ suffices for relative concentration. The argument uses independence of the
underlying edge weights and never independence of the degrees, which is the point, since the degrees are
dependent.

The obligations are the complementary regimes. For P0458 what is missing is the law outside
$k = o(n^{2/5})$, and in particular whether the non-Gaussian limit $g(Z)$ persists when $k$ grows fast
enough that the internal edges among the preferred neighbours are no longer negligible, since the error
term $O(k^2/n + k^5/n^2)$ is exactly what breaks there. For P0459 what is missing is the sharp tail and
the logarithmic boundary; the record notes the hard constraint that below the connectivity threshold
isolated vertices exist, so no statement of the form "every degree is near $k$" can hold there, which
means the boundary is a genuine threshold rather than an artefact of the method. Verification state,
verbatim: both rows read `result_status: candidate_partial_counterexample`,
`verification: author_checked_partial`, `independent_review: none`, `novelty: not_claimed`; P0458's
independent check records that all 720 rank permutations on four vertices for $k = 1, 2$ satisfy
$D \le D_0 \le D + 2J$ and that the degree means $3/5$ and $8/5$ agree with independent two-endpoint rank
probabilities. Closeness rank 2 for P0458, rank 3 for P0459.

### P0289, Ross's second conjecture: covered in chapter 10

Source: Leskela, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100
(2022), 213 to 215, Problem 1. A single-server queue with Cox arrivals of intensity
$\lambda_c(t) = \lambda(ct)$, $\lambda$ stationary and ergodic, independent and identically distributed
service, stable, and $w(c)$ the mean stationary workload: is $w$ nonincreasing in $c$, and if not, what
condition on $\lambda$ makes it so?

This row's current state is in chapter 10 and the mathematics is not repeated here. In summary: the
campaign's packet refutes the universal clause with a non-reversible cyclic environment, and on 12
September the light-traffic expansion on which the whole counterexample rests was re-derived from
scratch, by a square-workload balance, the shot lower bound $V \ge S$, the monotonicity of $D = V - S$
under added arrivals and a thinning coupling for the uniform remainder. The re-derivation added a clean
second-order criterion: the second-order coefficient is half the variance of the environment's average
over one service time,
$$w(c) = \frac{\varepsilon a}{2} + \varepsilon^2\left[\frac{a^2}{2} + \tfrac12
\operatorname{Var}(\bar F_c)\right] + R_c, \qquad \bar F_c = \frac1c \int_0^c F,$$
so faster modulation lowers the workload to second order exactly when it lowers that variance, and since
a reversible stationary chain has autocovariance $R(v) = \sum_k a_k^2 e^{-\lambda_k v}$, which is
nonincreasing, a reversible environment can never produce a second-order counterexample. Two obligations
are recorded and they are the reason this row is here rather than in the settled chapter: the prior-art
comparison, for both the counterexample and the criterion, against Heyman's periodic-intensity example,
Miyoshi and Rolski 2004 and the light-traffic literature on Cox queues, none of which was searched in
full; and whether the exact all-traffic condition in Problem 1 can be characterised at all, given that
the third-order term $E[\lambda(0)D(0)]$ showed no sign structure in $c$. Closeness rank 2 for the
prior-art half; the all-traffic characterisation is not ranked, because it is not known to be a
well-posed target.

### D0016, the zeros of a slice of the Brownian sheet

Source: Khoshnevisan, *Brownian sheet and quasi-sure analysis*, arXiv:math/0510518, Open Problem 1,
Section 8.1, PDF page 33. For a two-parameter Brownian sheet $B$ in $\mathbb{R}^d$ with $d \in \{2,3\}$:
is it true that outside a single null set, $B^{-1}\{0\} \cap (\{s\}\times(0,\infty))$ is finite for every
$s > 0$? The source conjectures the answer is no, and asks further for a gauge $\varphi$ with
$\varphi(r) \to \infty$ as $r \to 0$ such that some slice zero-set has positive $\varphi$-Hausdorff
measure.

What is proved is a first-moment budget that splits the two dimensions apart. For fixed $s$ and
$t_1 < \dots < t_k$ the increments $B(s,t_1), B(s,t_2)-B(s,t_1), \dots$ are independent Gaussians, since
they are driven by disjoint rectangles of the white noise, so the $k$-point function factorises and
$P(|B(s,t_i)| \le \epsilon \text{ for all } i)$ is of order $\epsilon^{kd}$ on a compact parameter box. In
the sheet's natural metric an $\epsilon$-ball has radius $\epsilon^2$ in each of the $k+1$ parameters
$s, t_1, \dots, t_k$, so a unit box needs $\epsilon^{-2(k+1)}$ such balls, and the count is
$$\epsilon^{-2(k+1)}\epsilon^{kd} = \epsilon^{kd - 2(k+1)},$$
which blows up exactly when $k(d-2) < 2$. The known facts come out as controls: $k = 1$ gives $4 - d > 0$
for $d \le 3$, the Orey and Pruitt threshold, with Euclidean dimension $2 - d/2$ for the zero set,
matching Rosen's theorem and the source's equation (1.7), and the pair condition gives dimension $3-d$
for $\{(s,t_1,t_2) : B(s,t_1) = B(s,t_2) = 0\}$. For $d = 2$ the criterion holds for every $k$, so slices
carrying arbitrarily many zeros should exist and the answer should be no, as the source conjectures. For
$d = 3$ only $k = 1$ is admissible and $k = 2$ is exactly critical, $2(k+1) = kd = 6$, so the count
predicts at most one zero per slice and the answer yes, against the source's conjecture.

What is missing is stated precisely in the record and is different in the two dimensions. For $d = 2$,
turning the count into a theorem needs a second-moment or capacity argument for the $k$-point set with
the exceptional $s$ handled by an energy estimate uniform in $k$, and then a limsup argument along a
nested family to pass from arbitrarily many to infinitely many zeros in one slice. For $d = 3$ the
concrete wall is the critical two-point estimate, where logarithmic corrections decide the answer and
where the gauge function of the source's second question would live; a first-moment count cannot see a
gauge. Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`, the
obstruction reading "This is a first-moment (box-counting) budget, not a proof, and it is silent exactly
where the source's second question lives." Closeness rank 2 in $d=2$, rank 3 in $d=3$.

### D0002, a generic proof of the complete mixability theorems

Source: the 2014 survey of open problems on complete and joint mixability, Open Problem 2, PDF page 10.
All the known sufficient conditions for $n$-complete mixability, a symmetric unimodal density, a
monotone density with the mean condition $a + (b-a)/n \le \mu \le b - (b-a)/n$, a concave density, a
density bounded below by $3/(n(b-a))$, and the Gaussian and elliptical families, are proved case by case
by discretisation plus combinatorial rearrangement. Is there one generic probabilistic or analytic proof
that yields them together, for instance through the duality of the source's Theorem 1?

What is proved is that an orbit criterion is genuinely generic and already covers two families. Write $F$
as the law of $g(U)$ with $U$ uniform. If $T$ is a measure-preserving map of $[0,1]$ with $T^n =
\mathrm{id}$ and $\sum_{k<n} g(T^k u) = n\mu$ almost everywhere, then $(g(U), g(TU), \dots,
g(T^{n-1}U))$ is a complete mix. Taking $T(u) = 1-u$ shows every law symmetric about $\mu$ is 2-complete
mixable, and concatenation ($n$-CM and $m$-CM imply $(n+m)$-CM) recovers symmetric unimodal for all even
$n$. In $\mathbb{R}^d$ the same criterion with $T$ induced by a linear map of finite order proves a whole
class at once: if $C$ is an affine image of a body invariant under a linear $R$ with $R^n = I$ and no
nonzero fixed vector, then the uniform law on $C$ is $n$-CM, because
$$\sum_{k=0}^{n-1} R^k = 0$$
whenever $R^n = I$ and $1$ is not an eigenvalue of $R$. That yields simplices and ellipsoids
simultaneously and is not in the source.

What is missing is a mechanism outside the group-orbit world, and the record identifies precisely where
the orbit route stops. The sharp monotone-density theorem is not of orbit type: its extremal complete
mixes are built by an $n$-dependent greedy rearrangement of the quantile function, and when $\mu$ sits at
an endpoint of the admissible interval the complete mix is rigid and non-exchangeable, so no $T$ with
$T^n = \mathrm{id}$ can produce it. A generic proof therefore has to produce a measurable selection from
the feasibility problem of the source's Theorem 1, and the dual certificate there is a pure existence
statement with no known normal form. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`. Closeness rank 3.

### D0005, uniform laws on convex bodies

Source: the same survey, Open Problem 5, PDF page 16. Let $C$ be a convex set in $\mathbb{R}^d$. Is the
uniform distribution on $C$ necessarily $n$-completely mixable for every $n \ge d+1$? The source states
the problem is equivalent to $(d+1)$-complete mixability and records only the trivial cases $d = 0$ and
$d = 1$.

What is proved is the $(d+1)$ case for two natural families in every dimension, by the orbit criterion of
the previous section. Every simplex in $\mathbb{R}^d$ is $(d+1)$-CM: for the regular simplex the rotation
$R$ cyclically permuting the $d+1$ vertices acts on the $d$-dimensional span of the centred vertices as
the standard representation of $\mathbb{Z}_{d+1}$, which has no invariant vector, so $\sum_{k=0}^{d} R^k
= 0$ and $(X, RX, \dots, R^dX)$ is a complete mix; every simplex is an affine image $T(x) = Ax+b$ of the
regular one and $\sum_k T(R^kX) = (d+1)b$ is constant. Every ellipsoid is $n$-CM for every $n \ge 2$, by a
rotation through $2\pi/n$ in a plane or by central symmetry. More generally every affine image of a body
with a fixed-point-free linear symmetry of order $n$ is $n$-CM.

Two things are missing. First, for a generic convex body the affine automorphism group is trivial, so the
orbit route gives nothing at all, and what is needed is a $(d+1)$-complete mix built from convexity
alone. The natural attempt, decomposing $C$ into simplices and mixing each piece, fails because the
pieces have different centroids, so their $(d+1)$-mixes have different centres and the mixture is not a
complete mix; making the centres agree is a transport constraint that convexity does not obviously
supply. Second, the record flags a gap in the source's own framing: the claim that the problem is
equivalent to $(d+1)$-CM is not obvious for bodies without central symmetry, because the usual route from
$(d+1)$-CM to all $n \ge d+1$ concatenates with 2-CM, and 2-CM of the uniform law on $C$ is exactly
central symmetry of $C$ about its centroid, which a scalene triangle does not have. So for a scalene
triangle the case $n = 4$ is not implied by the case $n = 3$ proved here. Verification state, verbatim:
`result_status: partial_result`, `verification: unreviewed`. Closeness rank 4.

### D0010, extra conditions for complete mixability of unimodal laws

Source: the same survey, Open Problem 10, PDF page 18. Counterexamples show the mean condition
$a + (b-a)/n \le \mu \le b - (b-a)/n$ is not sufficient for complete mixability of a law with a unimodal
density on a bounded interval. Under what extra conditions is such a law $n$-CM? The source singles out
the case where one of the inequalities is an equality.

What is proved is a quantitative necessary condition in exactly that tight case. If $\mu = a + (b-a)/n$
and $F$ is $n$-CM with centre $\mu$, then in the complete mix $\sum_i (X_i - a) = n\mu - na = b-a$ while
$0 \le X_i - a \le b-a$ for every $i$, so $(X_i - a)_{i \le n}$ is an exchangeable random composition of
the fixed total $b-a$ into $n$ nonnegative parts. Since at most $(b-a)/x$ parts of such a composition can
exceed $x$, exchangeability gives $n(1 - F(a+x)) \le (b-a)/x$, that is
$$F(a+x) \ge 1 - \frac{b-a}{nx} \qquad \text{for all } x \in (0, b-a].$$
Any unimodal density whose mean sits at the left boundary of the mean condition and which is too flat
near $a$ violates this and is therefore not $n$-CM.

The condition is sharp in its regime and empty outside it: away from the boundary the composition
structure disappears and the bound degrades to the mean condition itself. What is missing to convert it
into a sufficient condition is an existence theorem for exchangeable random compositions with a
prescribed one-dimensional marginal, which is the same feasibility problem that walls off D0002, D0007
and D0012. An earlier audit of this row recorded a related trap worth keeping: an earlier version of the
"extra necessary condition" here was Markov's inequality in disguise and excluded nothing, and what
repaired it into something that bites was keeping the integrality of the part count. Verification state,
verbatim: `result_status: partial_result`, `verification: unreviewed`. Closeness rank 3.

### D0003, the binary-multinomial layer decomposition

Source: the same survey, Open Problem 3, PDF page 14. The source's Theorem 3 says a $\mathbb{Z}_+^n$-valued
vector $X$ is a joint mix with integer centre $N$ if and only if $X = \sum_{k=1}^N X_k$ with each $X_k$
binary multinomial, that is $\{0,1\}^n$-valued with exactly one coordinate equal to $1$. Can this
decomposition, perpendicular to the $n$-discrete-uniform decomposition of Theorem 2, be used
non-trivially to characterise further classes?

Two consequences follow at once, so the answer to the source's question is yes. Layer concatenation: if
$(F_1,\dots,F_n)$ is jointly mixable with integer centre $N$ and $(G_1,\dots,G_n)$ with centre $M$, then
stacking the two independent layer systems shows $(F_1 * G_1, \dots, F_n * G_n)$ is jointly mixable with
centre $N+M$, a convolution stability invisible in the Theorem 2 picture. And a two-parameter family: for
any $p_1,\dots,p_n \ge 0$ summing to one and any $N$, the tuple $(\mathrm{Bin}(N,p_1), \dots,
\mathrm{Bin}(N,p_n))$ is jointly mixable with centre $N$, by taking $N$ independent layers each placing
its single $1$ in coordinate $i$ with probability $p_i$; setting all $p_i = 1/n$ recovers the source's own
remark that $\mathrm{Bin}(n,1/n)$ is $n$-CM, which is the diagonal case.

What is missing is a criterion in terms of the margins alone for the existence of a layer stack with
prescribed marginal counts, and the record explains why the construction cannot reach the interesting
theorems: it is confined to integer centres and $\mathbb{Z}_+$-valued margins and produces layers
exchangeable in $k$, whereas the monotone-density and concave-density theorems survive discretisation
only as laws on a fine lattice whose complete mixes are not layer-independent. Verification state,
verbatim: `result_status: partial_result`, `verification: unreviewed`. Closeness rank 3.

### D0035, prescribing the phi-mixing coefficients exactly

Source: Bradley, *Introduction to strong mixing conditions*, Question 7, Section 4.2, PDF page 19. Given
an arbitrary nonincreasing sequence $(b_n)$ in $[0,1]$, is there a strictly stationary sequence $X$ with
$\varphi(n) = b_n$ for every $n \ge 1$? The source notes that known constructions leave an arbitrarily
small window in the specification, and that it is not even known whether there is a stationary sequence
with $1 > \varphi(1) = \varphi(2) > 0 = \varphi(3)$.

The literal general form is false, and the counterexample is one line from the survey's own text. On PDF
page 18 the source quotes, for a strictly stationary sequence with no ergodicity assumption, that if
$\varphi(n) < 1/2$ for some $n$ then $X$ is $\varphi$-mixing, that is $\varphi(n) \to 0$. Take $b_n =
1/4$ for every $n$: it is nonincreasing and lies in $[0,1]$, but any stationary $X$ with $\varphi(1) =
1/4$ has $\varphi(n) \to 0$. More generally no nonincreasing sequence that drops below $1/2$ without
converging to zero is realisable, and the source's Theorem 4.1(3)(c) adds that for an
ergodic-theoretically mixing sequence either $\varphi(n) \to 0$ or $\varphi(n) = 1$ for all $n$.

So the substantive residual problem is to characterise the realisable set, and the source's own
sub-question is untouched by these constraints, since $\varphi(3) = 0$ makes $X$ 2-dependent and
$\varphi(1)$ may exceed $1/2$. What is missing, concretely, is uniform control of conditional
probabilities over the past: the known constructions, Kesten and O'Brien and its descendants, prescribe
$\alpha$, $\rho$ and $\rho^*$ exactly, because those are defined through measures of sets, and prescribe
$\varphi$ only up to a small window, because $\varphi$ is a supremum of conditional probabilities and
cutting and stacking does not control those uniformly. Verification state, verbatim:
`result_status: partial_result`, `verification: unreviewed`; the row's `status_search` notes "the literal
general form is refuted by a result quoted elsewhere in the same survey." Closeness rank 3.

### E0024, Hunt's hypothesis for a product of two independent Levy processes

Source: the 2019 survey on Hunt's hypothesis, Question 4, equivalently Question 4', PDF pages 15 and 18.
If $X_1$ on $\mathbb{R}^n$ and $X_2$ on $\mathbb{R}^m$ are independent Levy processes both satisfying
Hunt's hypothesis (H), does the $\mathbb{R}^{n+m}$-valued process $X = (X_1,X_2)$ satisfy (H)?
Equivalently: if $S$ is a nonempty proper subspace of $\mathbb{R}^n$ and the projections $X_S$ and
$X_{S^\perp}$ are independent and both satisfy (H), does $X$?

What is proved is a positive answer on a class strictly larger than the one the survey uses, and the
mechanism is that the exponent is additive. For independent coordinates $\psi(z_1,z_2) = \psi_1(z_1) +
\psi_2(z_2)$, so $\operatorname{Re}\psi$ adds and $|\operatorname{Im}\psi|$ is subadditive; hence any
sufficient condition of the pointwise shape
$$|\operatorname{Im}\psi| \le (1 + \operatorname{Re}\psi)\, f(1 + \operatorname{Re}\psi), \quad f
\text{ increasing}, \quad \int^\infty \frac{d\lambda}{\lambda f(\lambda)} = \infty,$$
survives the sum with $f$ replaced by $2f$, since $1 + \operatorname{Re}\psi_i \le 1 +
\operatorname{Re}\psi$ and monotonicity give $|\operatorname{Im}\psi| \le |\operatorname{Im}\psi_1| +
|\operatorname{Im}\psi_2| \le 2(1+\operatorname{Re}\psi)f(1+\operatorname{Re}\psi)$, and doubling $f$ does
not affect the divergence. Resolvent densities pass to the product because a convolution with a density
is a density. So the answer is yes for every pair in Rao's class, which contains Kanda and Forst, the
class the survey's own Proposition 3.10 uses, and the survey does not record this.

What is missing is the answer outside Rao's class, and that is not a technicality but the survey's whole
point: its Theorems 2.8, 2.11 and 2.12 exist precisely because (H) holds for processes outside that
class. The obstruction is concrete. The survey's weaker sufficient conditions, EKFR, $C_{\log}$ and
$C_{\log\log}$, are quantified over finite measures of finite $1$-energy with a measure-dependent
sequence $y_k$; under addition of exponents the level sets $\{y_k \le B(z) < y_k^\beta\}$ of $B = 1 +
\operatorname{Re}\psi$ change shape in the product space, and a finite-energy measure on
$\mathbb{R}^{n+m}$ need not factor, so there is no way to build the required sequence for the product out
of the two given ones. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`. Closeness rank 4.

### E0026, Hunt's hypothesis in one dimension with infinite jump variation

Source: the same survey, Question 6, PDF page 25. Does every one-dimensional Levy process with
$\int (1 \wedge |x|)\,\nu(dx) = \infty$ satisfy (H)? The survey notes, citing Kesten, that a positive
answer to its Question 7 would imply one here.

What is proved is a reduction that removes the large jumps from consideration. By the stability of Rao's
class under independent sums recorded in the previous section, any one-dimensional Levy process that
decomposes as an independent sum of processes each in Rao's class is itself in Rao's class and satisfies
(H). Splitting a process of infinite jump variation at a jump scale writes it as an independent sum of a
small-jump part and a compound Poisson part, and a compound Poisson process has bounded exponent and so
satisfies Kanda and Forst trivially. Hence the large-jump part is never the obstruction, and Question 6
holds whenever the small-jump component satisfies Rao's condition.

What is missing is the small-jump part, which is exactly where an oscillating Levy density can break the
ratio $|\operatorname{Im}\psi|/(1+\operatorname{Re}\psi)$, and the hypothesis of infinite jump variation
does not by itself force any lower bound on $\operatorname{Re}\psi$, so it does not force that ratio to be
bounded. The record adds the honest scale: Getoor's conjecture, which subsumes this question, has been
open for fifty years. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`. Closeness rank 4.

### E0027, is Hunt's hypothesis stable under independent sums

Source: the same survey, Question 7, PDF page 25. If $X$ and $Y$ are independent $n$-dimensional Levy
processes both satisfying (H), does $X+Y$ satisfy (H)? The survey states this as a question it has raised
before and records that a positive answer implies a positive answer to Question 6 by Kesten's Theorem
1(f).

What is proved is the same additivity argument as in E0024, in the form where it is cleanest. Kanda and
Forst is stable: if $|\operatorname{Im}\psi_X| \le M(1+\operatorname{Re}\psi_X)$ and likewise for $Y$,
then $|\operatorname{Im}\psi| \le M(2 + \operatorname{Re}\psi_X + \operatorname{Re}\psi_Y) \le
2M(1+\operatorname{Re}\psi)$. Rao's condition is stable by the same monotonicity step, and the sum has
resolvent densities as soon as one summand does. So the answer is yes whenever both summands lie in Rao's
class, which contains all stable processes and every process with a nondegenerate Gaussian part.

What is missing is the case where at least one summand satisfies (H) only through a measure-dependent
condition, and the obstruction is identical to E0024's: the survey's weaker conditions are not of the
pointwise form $|\operatorname{Im}\psi| \le g(\operatorname{Re}\psi)$, and adding exponents moves the
level sets with no available relation between the three measure-dependent sequences. Verification state,
verbatim: `result_status: partial_result`, `verification: unreviewed`. Closeness rank 4.

### E0008, a general coexistence theorem for long-range interactions

Source: Durrett's 2009 coexistence notes, Problem 2, PDF page 7. Durrett's Theorem 5 gives coexistence in
a stochastic spatial model with fast stirring at rate $\epsilon^{-2}$ whenever there is a function
$\varphi$ that decreases along solutions of the mean-field ordinary differential equation, is convex, and
tends to infinity as $\min_i u_i \to 0$. Formulate and prove a similar general result for systems with
long-range interactions, where the coexistence proofs are at present done case by case.

What is proved is that the Lyapunov step survives verbatim, with no new hypothesis. Under long-range
interaction of range $N$ the hydrodynamic object is not $u_t = \Delta u + f(u)$ but the nonlocal equation
$u_t = J*u - u + f(u)$ with $J$ the normalised kernel. For convex $\varphi$, Jensen against the
probability kernel gives $\varphi(J*u) \le J*\varphi(u)$, hence $\varphi(J*u) - \varphi(u) \le J*h - h$
with $h = \varphi(u)$, and the computation that produced $\partial_t h \le \Delta h + \varphi'(u)\cdot
f(u)$ in the diffusive case becomes
$$\partial_t h \le J*h - h + \varphi'(u)\cdot f(u),$$
again nonlocal heat flow with killing, since $\varphi'(u)\cdot f(u) \le 0$ by hypothesis. So convexity of
$\varphi$, used in the fast-stirring proof against the Laplacian, is exactly the hypothesis that makes the
nonlocal generator work.

What is missing is the spreading statement, and this is where long range and fast stirring genuinely
differ. For the diffusive equation, "one pile makes two piles" follows from a finite-speed travelling
front; for the nonlocal equation the front speed is finite only when $J$ has exponential tails, and for
heavy-tailed $J$ fronts accelerate and the block construction's fixed space-time box has no analogue. A
second difficulty is that the long-range particle system does not approach the nonlocal equation with a
small parameter multiplying the noise the way fast stirring does: the fluctuation term is of order
$N^{-d/2}$ and the hydrodynamic error has to be beaten uniformly over the block, which is what the
case-by-case proofs do by hand. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`. Closeness rank 3.

### E0058, another kind of Lyapunov function for Volterra operators

Source: the 2009 survey on quadratic stochastic operators, Problem 1, PDF page 3. For the Volterra
operator $V(x)_k = x_k(1 + \sum_i a_{ki}x_i)$ on the simplex, with $A$ skew-symmetric and $|a_{ki}| \le
1$, does there exist another kind of Lyapunov function beyond the known one?

What is proved delimits the known family exactly. For $\varphi_c(x) = \sum_i c_i \log x_i$ with $c_i \ge
0$,
$$\varphi_c(V(x)) - \varphi_c(x) = \sum_i c_i \log(1 + (Ax)_i) \le \langle c, Ax\rangle,$$
so $\varphi_c$ is nonincreasing along every trajectory as soon as $\langle c, Ax\rangle \le 0$ on the
simplex, in particular whenever $A^{\mathsf T}c = 0$, where the bound is exactly zero and the decrease is
strict unless $(Ax)_i = 0$ for every $i$ with $c_i > 0$. So the logarithmic family is precisely the
nonnegative kernel of $A^{\mathsf T}$, and for a skew-symmetric $A$ of full rank on the relevant subspace
there is no such $c$ at all: those operators are where a new Lyapunov function is needed.

What is missing is a function whose increment is controlled by a quadratic rather than a linear form in
$x$, and the obstruction names the constraint any candidate must satisfy: the Volterra dynamics preserves
the faces of the simplex, so a Lyapunov function must degenerate on every face, and the log family is the
only elementary family with that property; beyond it, the sign of a general quadratic form on the simplex
is not decidable from skew-symmetry alone. The record notes the derivation is elementary and presumably
known to the authors, and is recorded because it delimits the search. Verification state, verbatim:
`result_status: partial_result`, `verification: unreviewed`. Closeness rank 4.

### E0066, trajectories of quadratic bistochastic operators

Source: the same survey, Problem 13, PDF page 8. A quadratic operator $V$ on the simplex is bistochastic
if $V(x)$ is majorised by $x$ for every $x$. Investigate the behaviour of the trajectories.

What is proved is a free Lyapunov function, and a canonical one. Majorisation means every Schur-concave
function increases along trajectories, so the Shannon entropy $H(x) = -\sum_i x_i \log x_i$ satisfies
$H(V(x)) \ge H(x)$ for every bistochastic $V$ and every $x$. Hence $H$ is nondecreasing along every
trajectory and bounded by $\log m$, so $H(x(n))$ converges, the omega-limit set of any trajectory lies in
a level set of $H$, and any limit point $y$ satisfies $H(V(y)) = H(y)$, that is lies in the
entropy-preserving set. In particular, if the only entropy-preserving points are the permutations of a
fixed vector, every trajectory converges to that orbit.

What is missing is the entropy-preserving set for a given $V$, and the record explains why that is the
whole problem: for the identity-like extreme points of the bistochastic set every point preserves entropy
and nothing is learned, while for operators with strict majorisation the set is the centre of the simplex,
and deciding which case a given $P$ is in needs the classification of extreme quadratic bistochastic
operators, known only for small $m$. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`. Closeness rank 4.

### E0105, detection of a ball before a fixed point in the inertial Boolean model

Source: the 2014 mobile Boolean model survey, Open problem 3, PDF page 18. For the inertial Boolean
model, find the distribution of the detection time of a ball before a fixed point is hit.

This row is labelled `settled_homogeneous_case` and the label is the right one. The reduction is exact:
$\tau = \inf\{t : r_0 B \text{ meets } W(t),\ a \notin W(t)\}$ equals $S_K$ on $\{S_K < S_a\}$ and
$+\infty$ otherwise, because $W(t)$ is increasing, so the law of $\tau$ is a functional of the joint law
of the two detection times. For straight-line motion the set of starting states that detect $K$ by time
$t$ is a capsule $RB + [0,t](-v)$ with $R = r_0 + r$, and the set covering $a$ by time $s$ is the parallel
capsule $a + rB + [0,s](-v)$, so the marked-Poisson void probability gives
$$P(S_K > t, S_a > s) = \exp\left(-\lambda\, E_v \operatorname{Vol}(\text{capsule union})\right),$$
the union volume being the two capsule volumes minus an axial integral of the $(d-1)$-dimensional lens of
the cross-sections. The law of $\tau$ then has an atom at $0$ equal to $e^{-\lambda\omega_d r^d} -
e^{-\Lambda(0,0)}$, a density $(\partial_t\Lambda)(u,u)e^{-\Lambda(u,u)}$ on $(0,\infty)$, and an atom at
$+\infty$; $\Lambda$ is explicit up to a one-dimensional integral. This was validated in $d = 2$ against a
direct simulation of the particle system with 60,000 configurations: $P(S_K < S_a)$ $0.7670$ against
$0.7671 \pm 0.0017$, the atom $0.6953$ against $0.6967 \pm 0.0019$, and the joint survival at $t = 1, 3,
6$ to three decimals.

What is missing is everything inhomogeneous. Non-homogeneous intensities give the integrals the source
itself calls laborious; the survey's coverage problem (Open problem 1) and stability problem (Open problem
5) are untouched; and prior art was not checked beyond the source. The formula's continuous part sits
$0.0014$, about 1.5 standard errors, above the simulation, which the record attributes to quadrature
error. Verification state, verbatim: `result_status: settled_homogeneous_case`,
`verification: unreviewed`, `status_note` "2026-09-08: exact law of tau via the joint law of (S_K,S_a) as
a union-of-capsules void probability; validated by simulation." Closeness rank 1 within the inhomogeneous
extension, rank 4 for the Brownian analogue.

### E0104, comparing the detection times of two sets

Source: the same survey, Open problem 2, PDF page 18. For two sets $K_1$ and $K_2$, for example balls of
radii $r_1$ and $r_2$, with detection times $S_{K_1}$ and $S_{K_2}$ in the mobile Boolean model, find
$P(S_{K_1} < S_{K_2})$.

Two exact statements are on the record. First a reduction that holds for any motion: writing $A_i(t)$ for
the set of grain initial conditions detecting $K_i$ by time $t$, the Poisson void probability gives
$P(S_1 > s, S_2 > t) = \exp(-\lambda|A_1(s) \cup A_2(t)|)$, so differentiating expresses
$P(S_1 < S_2)$ as an explicit integral of $|A_1(s) \cup A_2(s)|$ against the intensity, and the whole
content is the geometry of the union of two swept regions. In the nested case $K_2 \subseteq K_1$ the
honest statement is $P(S_{K_1} < S_{K_2}) = P(\text{the first grain to touch } K_1 \text{ does not
simultaneously touch } K_2)$, since ties have positive probability. Second, for two balls in the
homogeneous inertial model the union is a pair of parallel capsules with $R_i = r_i + r$ and perpendicular
offset $h$, so the same capsule-union formula as in E0105 gives
$$P(S_{K_1} < S_{K_2}) = P(S_{K_1} = 0 < S_{K_2}) + \int_0^\infty (\partial_t\Lambda)(u,u)\,
e^{-\Lambda(u,u)}\,du,$$
and this row is labelled `settled_inertial_balls` on that basis.

What is missing is the Brownian case, and the obstruction is a named object with no closed form: the
volume $|A_1(s) \cup A_2(t)|$ requires the joint law of the times at which a single moving grain sweeps
two given sets, which for Brownian motion is the two-set Wiener sausage volume, and that has no closed
form in any dimension. Two-ball instances were not separately simulated; the validation is E0105's.
Verification state, verbatim: `result_status: settled_inertial_balls`, `verification: unreviewed`,
`status_note` "2026-09-08: inertial case for balls settled by the capsule-union formula (E0104-A002);
Brownian case open." Closeness rank 4.

### F0019, strict negativity of the derivative of the polymer free energy

Source: Zygouras's 2024 review of directed polymers, Question 2, Section 3.1, PDF page 13, verbatim: does
$f'(\beta) < 0$ hold in the whole strong disorder regime? Here $f(\beta) = \lim n^{-1}\log W_n^\beta$ is
the free energy, and Bates and Bates and Chatterjee prove quantitative localisation under very strong
disorder plus the assumptions that $f$ is differentiable and $f'(\beta) < 0$.

What is proved is an exact identification of the question, and it required a correction. For Gaussian
disorder, $p_n(\beta) = n^{-1}E\log Z_n$ is convex with
$$p_n'(\beta) = \beta\,(1 - R_n(\beta)), \qquad R_n(\beta) = n^{-1}\sum_{i \le n}
E\,\mu_n^{\otimes 2}(S_i = S_i'),$$
the two-replica overlap under the length-$n$ polymer measure, by Gaussian integration by parts. By
convexity, at every differentiability point of the limit, which is all but countably many $\beta$,
$\lim_n R_n(\beta) =: R(\beta)$ exists and $f'(\beta) = -\beta R(\beta)$. So Question 2, at
differentiability points, is exactly positivity of the Cesaro two-replica overlap throughout strong
disorder. Two consequences come free: since $f(\beta) = -\int_0^\beta s R(s)\,ds$ and $f(\beta) < 0$ for
$\beta > \beta_c$ by Junk and Lacoin for disorder bounded above, $R(s) > 0$ on a set of positive Lebesgue
measure in $(0,\beta)$, so $f'$ cannot vanish identically; and in $d = 1, 2$ strong disorder is very
strong disorder for every $\beta > 0$, so there is no intermediate region there.

The correction is the substance. Attempt F0019-A001 had bridged the identity to the source's inequality
(3.11), $-c_1\log W_n \le \sum_{i \le n} I_i \le -c_2 \log W_n$ under strong disorder, and concluded
$f'(\beta) \le -\beta c_1 |f(\beta)| < 0$. Attempt F0019-A002 withdrew the bridge: (3.11) concerns the
one-step overlap $I_i = \mu_{i-1}^{\otimes 2}(S_i = S_i')$ under the length-$(i-1)$ measure, a different
functional from $R_n$, and the claim that the two differ by an $o(n)$ boundary term is unproven and is the
whole gap. The identity stands; the bridge does not.

So what is missing is an inequality bounding the length-$n$ replica overlap $R_n$ below by the one-step
overlaps, or directly by $|f(\beta)|$. The record names a route: differentiate the one-step decomposition,
$\frac{d}{d\beta}E[\log W_i - \log W_{i-1}]$, which involves mixed overlaps between $\mu_{i-1}$ and
$\mu_n$; if those are comparable to $R_n$ on average one obtains $R(\beta) \ge c|f(\beta)|/\beta$, which
would answer Question 2 quantitatively in the very strong disorder region. It was not carried out. That
Bates and Bates and Chatterjee assume $f' < 0$ on top of very strong disorder is itself evidence that no
such bridge is known. Verification state, verbatim: A002 carries `result_status: attempted_unsolved` while
the problem row still reads `partial_result`, both `unreviewed`. Closeness rank 2.

### F0029, the toppling-probability exponent for the Abelian sandpile in dimensions two to four

Source: Jarai's 2014 sandpile survey, Conjecture 3.7, Section 3.3.2, PDF page 19. With $\nu$ the
infinite-volume stationary sandpile measure on $\mathbb{Z}^d$, add a particle at the origin and let
$\mathrm{Av}_o$ be the set of vertices that topple. Theorem 3.6 gives $c|x|^{2-d} \le \nu[x \in
\mathrm{Av}_o] \le C|x|^{2-d}$ for $d \ge 5$; the conjecture is that for $2 \le d \le 4$ there is
$\eta(d) \ge 0$ with $\nu[x \in \mathrm{Av}_o] = |x|^{-(d-2+\eta)+o(1)}$.

What is proved is a two-sided bracket on $\eta$ from spanning-tree quantities. Dhar's formula gives
$E_\nu n(o,x) = G(o,x) \sim c|x|^{2-d}$ for $d \ge 3$, so Markov's inequality gives the upper bound and
$\eta(d) \ge 0$ for $d = 3, 4$; in $d = 2$ the Green function of the box diverges and Markov gives nothing,
which is the source's own remark. For the lower bound, the first wave started at $o$ is, by the
Ivashkevich, Ktitarev and Priezzhev bijection, the component of $o$ in a uniform two-component spanning
forest, and $x$ belongs to it exactly when $x$ is a descendant of $o$ in the wired uniform spanning
forest, so
$$\nu[x \in \mathrm{Av}_o] \ge \nu[x \in \text{first wave}] = |x|^{-(d - \dim \mathrm{LERW}_d) + o(1)} .$$
In $d = 2$ the loop-erased walk dimension $5/4$ gives $|x|^{-3/4 + o(1)}$ and hence $\eta(2) \le 3/4$; the
conjecture in $d = 2$ then says later waves do not change the exponent, that is $\eta(2) = 2 - \dim
\mathrm{LERW}_2 = 3/4$.

What is missing is control of the later waves. The number of waves is $n(o,o)$, whose mean is infinite in
$d = 2$, so a union bound over waves fails; and the $k$-th wave is the component of $o$ in a forest
conditioned on the previous waves, a dependence for which the record knows no monotonicity and no
domination by the first wave. So the obligation is a domination or decoupling statement for successive
waves, and nothing weaker will do. Verification state, verbatim: `result_status: partial_result`,
`verification: unreviewed`, with the independent check noting that the $d = 3$ loop-erased dimension
$1.624$ is Wilson's numerical estimate quoted from memory, consistent with the rigorous dimension of Li
and Shiraishi. Closeness rank 3.

### F0036, local finiteness of potential most recent common ancestors in the Brownian net

Source: the 2015 Brownian web and net survey, Conjecture 8.3, Section 8.2, PDF page 72. For the Brownian
web the set of first meeting points of pairs of paths started at time $0$,
$$M = \{(x,t) : t > 0,\ \exists\, \pi, \pi' \text{ with } \pi(t) = x = \pi'(t),\ \pi < \pi' \text{ on }
(0,t)\},$$
is easily seen to be locally finite; the conjecture is that the same holds when the web is replaced by the
Brownian net.

What is proved is a reduction with one unproved step, and the record labels it a sketch. In the web the
paths started at time $0$ coalesce and come down from infinity, so meeting points in a compact set are
bounded by the number of paths alive at an earlier time and local finiteness follows. In the net the set
of paths from $\{0\}\times\mathbb{R}$ is not locally finite, but the branching-coalescing point set
$\xi_t$ is almost surely locally finite for each $t > 0$, and the definition's requirement that $\pi <
\pi'$ on all of $(0,t)$ rules out the obvious bad configuration: a small bubble created by a branching at
time $t - \epsilon$ whose two sides meet again at $t$ has its two paths coinciding before $t-\epsilon$, so
it is not a pair of the required kind. The count is then over pairs of points of $\xi_s$, for any $s \in
(0,t)$, whose descendant sets first meet at $(x,t)$, and local finiteness of $\xi_s$ makes that finite
provided each pair $y < y'$ produces only finitely many first-meeting points in a compact window.

What is missing is exactly that provision: the claim that the first meeting point of any pair of net paths
from $y$ and $y'$ is the meeting point of the rightmost path from $y$ and the leftmost path from $y'$.
That needs a proof that non-extremal net paths from $y'$ cannot meet a path from $y$ earlier, and the fine
structure at separation points, where paths coincide and then split, has to be handled. The attempt also
records that the argument was not checked against the paths-topology definition of "$\pi < \pi'$ on
$(0,t)$". Verification state, verbatim: `result_status: partial_result`, `verification: unreviewed`, with
the independent check reading "The argument was not checked against the paths-topology definition... and
should be treated as a sketch." Closeness rank 2.

### F0059, can the largest box be $o(n)$ along the full sequence

Source: Janson, Probability Surveys 9 (2012), Problem 18.39, Section 18.6, PDF page 122. Is
$Y_{(1)}/n \to_p 0$ possible when $0 < \nu < \lambda$? The source's Example 18.36 shows it is possible
along a subsequence and conjectures it is not possible along the full sequence, and, a little stronger,
that there is always $\epsilon > 0$ and a subsequence along which $Y_{(1)} \ge \epsilon n$ with high
probability.

What is proved is a rigidity lemma about the weights. Write $g(k) = \log(w_k\rho^k)$; merging two boxes of
sizes $a$ and $b$ into one of size $a+b$, leaving an empty box, multiplies the configuration weight by
$w_{a+b}w_0/(w_aw_b) = w_0\exp(g(a+b) - g(a) - g(b))$. Then $g$ cannot be subadditive: if it were,
Fekete's lemma gives $g(k)/k \to \inf_k g(k)/k = L \le 0$, and $L < 0$ would make $w_k\rho^k$ decay
exponentially so that the radius of $\Phi$ exceeds $\rho$, while $L = 0$ forces $g(k) \ge 0$, that is
$w_k\rho^k \ge 1$ for all $k$, contradicting $\Phi(\rho) < \infty$. So every weight sequence with $0 < \nu
< \infty$ has infinitely many pairs $(a,b)$ at which merging is weight-favoured, which is consistent with
the conjecture and explains why the source's examples achieve $Y_{(1)}/n \to 0$ only along subsequences.

What is missing is a density statement in place of an infinitude statement: one needs the
merging-favoured pairs to occur at every scale with $a+b$ of order $(\lambda-\nu)n$, that is a positive
density for $\{k : g(k) > \max_{a+b=k}(g(a)+g(b))\}$, whereas Fekete gives only infinitude. The attempt
also records the shape of a possible counterexample to the weaker conjecture, a sequence with $g$ nearly
subadditive on longer and longer intervals separated by short merging intervals, and that it could not
decide whether such a sequence stays consistent with $\rho\Phi'(\rho) < \infty$. The pairwise weight
comparison also ignores the entropy factor, which boxes carry the large counts. Verification state,
verbatim: `result_status: partial_result`, `verification: unreviewed`. Closeness rank 3.

### F0133, microstates and non-microstates free entropy

Source: Guionnet's 2004 lecture notes on large deviations for random matrices, Conjecture 7.1
(Voiculescu's unification problem), Chapter 7, PDF page 81: for any tracial law $\tau$ with
$\chi(\tau) > -\infty$, is $\chi(\tau) = \chi^*(\tau)$? Here $\chi$ is the microstates free entropy,
$\chi^*$ the non-microstates one built from the free Fisher information, and Theorem 7.3 of Biane,
Capitaine and Guionnet gives $\chi \le \chi^*$ always.

What is proved is that the unrestricted form is false and that the hypothesis in the conjecture is
therefore load-bearing. The source's Remark 7.2 shows that $\chi = \chi^*$ for every $\tau$ would imply
that every tracial law of finitely many self-adjoint variables is a limit of matrix microstates, which is
the Connes embedding property; and Connes embedding was refuted by Ji, Natarajan, Vidick, Wright and Yuen
(MIP* = RE, arXiv:2001.04383, 2020). Concretely, for a non-embeddable $\tau$ and any $\epsilon > 0$, the
semicircular perturbation $\tau_\epsilon$ has $\chi^*(\tau_\epsilon) > -\infty$ by Remark 7.2 while
$\chi(\tau_\epsilon) = -\infty$, since otherwise $\tau_\epsilon$, hence $\tau$, would have microstates.
So the two entropies differ by an infinite amount on a nonempty set of laws, all of which have $\chi =
-\infty$; Conjecture 7.1 as stated survives, and is equivalent to the reverse inequality $\chi \ge \chi^*$
on $\{\chi > -\infty\}$.

What is missing is any mechanism producing microstates from finite Fisher information without convexity.
The only available one is Dabrowski's Laplace principle for Hermitian Brownian motion, which proves
$\chi = \chi^*$ for free Gibbs laws with convex potentials under regularity and growth conditions; and
MIP* = RE shows finite Fisher information alone never suffices. Since $\chi \le \chi^*$ always, finiteness
of $\chi^*$ is automatic on the conjecture's domain, so the live case is laws that have microstates but a
strictly larger $\chi^*$, and no candidate for such a law is known. Verification state, verbatim:
`result_status: partial_result`, `verification: unreviewed`; the record notes the MIP* = RE citation was
"my knowledge, not re-fetched this session." Closeness rank 4.

### P0032, embedding an equivalent Brownian law by adding a finite prefix

Source: Burdzy and Scheutzow, Problem 7.5, PDF page 26: given a process whose law on nonnegative time is
equivalent to Wiener measure, can a random finite prefix be added, on an enlarged probability space if
necessary, to produce a process with Wiener law? The row is labelled `candidate_full_solution` and is
included here because its scope caveat has not been closed.

What is on record is a complete candidate construction of a finite nonnegative integer prefix time, for
any suffix law absolutely continuous with respect to Wiener measure, by forward density matching on the
ergodic two-sided Wiener shift. Two independent checks are recorded: a two-state cyclic example that
verifies the pushforward direction and the normalisation, and a finite-window rejection sampling
construction that gives the same conclusion in a special case.

What is missing is an interpretation, and it is substantive rather than cosmetic. The construction's prefix
time is a finite nonnegative integer random time depending on entire paths together with auxiliary
randomness, and the row's own caveat records that no independence or Brownian stopping-time restriction is
explicit in the source. So the obligation is to decide which reading the source intends: if the prefix
time is required to be a stopping time of the process, or independent of the suffix, the construction does
not apply and the problem is open as intended; if arbitrary path-dependent times with auxiliary randomness
are allowed, the construction answers it. Alongside that sit the measurability details and the earlier
filling and embedding literature, both listed as under review. Verification state, verbatim:
`verification: candidate_under_author_and_literature_checks`, `novelty: unassessed`,
`independent_review: none`, obstruction "No mathematical gap currently identified under the stated
interpretation; source interpretation, measurability details, and earlier filling/embedding literature
still under review." Closeness rank 1, the obligation being a reading of the source.

### P0033, ergodicity of stationary Galton-Watson flows

Source: Lyons and Peres, *Probability on Trees and Networks*, Question 17.18, printed page 575, PDF page
592: if a consistent equivariant Borel flow rule has a stationary probability measure equivalent to the
Galton-Watson law, must the associated subtree Markov chain be ergodic? Also labelled
`candidate_full_solution`, and included here for its scope caveat.

What is on record is a candidate counterexample: an endogenous AND/OR tree colouring with conditional
subtree selection, under which the Galton-Watson law itself is stationary and there are two invariant
colour classes each of mass one half, so the chain is not ergodic. The checks recorded are an exact
second-moment recursion proving measurability of the colour, and a full conditional subtree law proving
stationarity.

What is missing is whether the construction is inside the question's intended scope. The row's caveat is
explicit: the definition of a flow rule permits zero child weights, strict positivity is a separate
sufficient hypothesis in the book's Proposition 17.17, and Exercise 17.22 treats only a merely absolutely
continuous stationary measure. The construction uses zero child weights. So the obligation is to determine
whether Question 17.18 is asked within the class where zero weights are allowed, in which case the
counterexample settles it, or implicitly within the strictly positive class of Proposition 17.17, in which
case it is a literal-scope counterexample and the intended question stands. A full author recheck and the
prior tree-automaton literature are both listed as pending. Verification state, verbatim:
`verification: candidate_under_author_and_literature_checks`, `novelty: unassessed`,
`independent_review: none`. Closeness rank 1, again a reading of the source.

### The rows that are carried only in the table

Nine rows are listed in the table below without a section of their own, and it is worth saying why in each
case, because in three of them the reason is that our result is not ours.

P0205, Metropolis relaxation for geometric-time Cayley targets, refutes the monotonicity clause of its
source's questions (i) to (iii) on a two-element group: for the nonlazy flip walk the target is $\mu_p =
(1/(2-p), (1-p)/(2-p))$, the Metropolis matrix has rows $(p, 1-p)$ and $(1, 0)$, its second
eigenvalue is $p-1$ and so the relaxation time $1/(1-\lambda_2) = 1/(2-p)$ is strictly increasing rather
than decreasing; a lazy base walk gives $\tau(p) = 1+p$, also increasing, and removes the spectral
convention ambiguity. What remains is the source's other universal-bound questions, its undefined
reference parameter $\tau(\infty)$, and prior art. Rank 3.

P0341, P0342 and P0347 are the three critical beta-splitting rows whose recorded outcomes are scope
corrections to Aldous and Janson's ansatz and open problems. P0341 refutes the unrestricted polynomial-test
ansatz with the sparse test $f(j) = 1$ on powers of two: the limiting sum $S$ is finite because $a(2^r) =
O(r2^{-r})$, while along $n = 2^K$ the certain root visit adds one, so the liminf is at least $S+1$; the
test $g(j) = jf(j)$ refutes the divergent clause, the true sum being at least $2^K$ against a proposed
order $K^2$. What remains is a sharp two-parameter error theory and the best admissible class of tests.
P0342 refutes the transfer of a fringe-process central limit theorem to the finite tree with a bounded
continuous functional whose finite normalised sums are not tight, and what remains is a positive-variance or
quantitatively local transfer theorem, since the counterexample has a degenerate Gaussian limit. P0347
corrects two of the source's one-split constants, $E(m-2I)^2 = m^2 - 2m(m-1)/H_{m-1} \sim m^2$ rather than
$m^2/4$, and $E|m-2I| = m - O(m/\log m)$ rather than $m/2$, and bounds the mean Colless index by the same
leading constant $3/\pi^2$ as the external path length; what remains is the distributional question the
source actually asks, the variances and normalised laws. All three rank 3.

P0355 is a degenerate-scope counterexample to a nonendogeny conjecture: with $N = 2$, $\eta = 0$, unit
weights and $Y \equiv 1$, every ray sum is zero, the homogeneous equation fixes $Y$, the source's condition
39 holds, and the all-$a$ tree process is invariant and endogenous because its root is constant, so the
literal conjecture needs an extra assumption. The intended strictly discounted nondegenerate regime is
untouched. Rank 4.

F0066 and F0068 are marked excluded in their own titles because each reduces to a problem already on the
list. F0066, the conjecture that $\nu = 1$ and $\sigma^2 = \infty$ force $W(T_n)/\sqrt n \to_p \infty$,
follows from the neighbouring height conjecture via $W \ge n/(H+1)$, and conversely the Donderwinkel and
Khanfir bound $HW = O(n\log n)$ makes the two equivalent up to a logarithm. F0068, whether $\nu < 1$
implies the same width divergence, is implied by either of those and is strictly weaker than both.

P0407, P0423, P0424, P0448, P0449 and P0460 carry the label `known_result_not_original`, which is the
label the campaign uses when its own answer duplicates published work. They are in the table for
completeness and they are not close to solved in the sense of this chapter; they are solved, elsewhere, and
the rows record that honestly. The pattern is worth one sentence: of the 25 written proof files in the Codex
campaign, five label themselves already known or excluded and do so correctly, which is the main reason the
8 September audit concluded that the campaign's unlabelled candidates deserve to be taken seriously.

### The table of every close-to-solved row

Ledger codes: X for the 20-hour Codex campaign, C, D, E, F, G for the five intakes. Rank is the closeness
grade of the introduction: 1 a finite or computational obligation, 2 one analytic step of known shape, 3 the
mechanism without the quantitative half, 4 a special case with the general case open. Rows marked with two
ranks have two obligations of different difficulty.

| Id | Ledger | What is proved | The obligation left | Rank |
| --- | --- | --- | --- | --- |
| F0057 | F | Total variation limit for every fixed $j$ | Insert the truncation good events in the two count inclusions (P30H-F001) | 1 |
| F0056 | F | Literal $\lambda=0$ statement false at bounded $m$; sparse parity candidate at $n=k^4$, $m=2k+1$ | Local ratio limit theorem for the degenerating array; assemble the candidate limit | 1 |
| P0174 | X | Candidate $C=1$, with matching sharpness | Settle the source's diameter-versus-radius normalisation; citation check | 1 |
| P0189 | X | Nilpotent clock and shift pairs converging strongly, empirical measures $\delta_0$ | Confirm the cited Brown-measure theorem and its author list; isometry step | 2 |
| D0039 | D | The literature exclusion fails; problem is open | Transfer Chhaibi and Najnudel from the circle to the beta-Hermite measure | 2 |
| E0064 | E | Non-attractiveness fails from $m=4$; uniqueness fails from $m=5$, exact example | Uniqueness at $m=4$; the cycle clause in higher dimension | 1, 4 |
| G0014 | G | Uniform integrability follows under bounded displacements | Read whether Theorem 2.1's displacements are bounded | 1 |
| G0015 | G | A de Raphelis route that appears to cover the conjecture | Check his Doeblin and moment conditions against the kernel | 1 |
| C0062 | C | Unique up to conjugation for every $n \le 40$; conjugation forces the qualifier | A structure theorem or efficient algorithm for the maximiser | 1, 4 |
| C0033 | C | Concavity for $\lvert E\rvert=1$, diagonal, and $Q_2=I-Q_1$; 1,440 numerical trials clean | The $2\times2$ case analytically | 1 |
| C0034 | C | Disjointness is forced; polytope nonempty in 1,360 instances; naive rule fails | An exact rational certificate; then a general construction | 1, 4 |
| C0036 | C | Domination by the harmonic mean, via one-site Schur complements | Improve harmonic to geometric mean using conditional, not worst-case, information | 3 |
| G0013 | G | Extreme-point reduction; exhaustive to $n=9$, 46,066 classes | The exchange argument for general $n$ | 2 |
| G0008 | G | Eventually monotone at every $p \ne p_c$ by Ornstein and Zernike | Uniformity in $n$ from $n=1$; and any mechanism at $p_c$ | 1, 4 |
| G0005 | G | Holds with $\eta = 2\delta(K+1)$ when $E[N_A] \le K$ | The many-contacts regime, where the union bound is wasteful | 3 |
| G0004 | G | Holds for $\lvert B\rvert=1$ and on independent-route families | The inequality, or an example concentrating on one contact point | 4 |
| G0001 | G | Equivalent to $\theta(p_c)=0$; holds for $p>p_c$ by Kesten and Zhang | $\theta(p_c)=0$ itself; the site version of the supercritical tail | 4 |
| P0001 | X | Negative association for all finite cactus graphs | An inequality from graphic-matroid circuit elimination | 4 |
| P0004 | X | Root independence of the limsup on bounded-degree graphs | Existence of the limit; no stationary subadditive process available | 4 |
| P0389 | X | Fixed mass refutes the all-window lower bound in $d=1$ | Variance growth for mesoscopic windows; the critical exponent | 3 |
| P0390 | X | Same for the stationary wake chain; global covariance cancellation is not hyperuniformity | The small-window transition | 3 |
| P0411 | X | Monotonicity in all $d$; odd-dimensional positivity; negative sixth coefficient in $d=2$ | The intended variable; even-dimensional density and median clauses | 2 |
| P0429 | X | $k = o((n/\log n)^{1/3})$ suffices under exponential service | The optimal threshold; general service; correlated marks | 3 |
| P0458 | X | Non-Gaussian limit $(1/\sqrt\pi - g(Z))/\sqrt v$ for $k = o(n^{2/5})$ | The law beyond $n^{2/5}$, where internal edges stop being negligible | 2 |
| P0459 | X | $k/\log n \to \infty$ suffices for simultaneous concentration | Sharp tails and the logarithmic boundary | 3 |
| P0289 | X | Counterexample re-derived; second-order criterion is a variance of the window average | Prior art; whether the all-traffic condition is characterisable | 2 |
| D0016 | D | First-moment budget $\epsilon^{kd-2(k+1)}$ splits $d=2$ from $d=3$ | Capacity argument in $d=2$; the critical two-point estimate in $d=3$ | 2, 3 |
| D0002 | D | An orbit criterion covering symmetric laws and finite-order symmetric bodies | A measurable selection from the Theorem 1 feasibility problem | 3 |
| D0005 | D | Every simplex is $(d+1)$-CM; every ellipsoid is $n$-CM | A $(d+1)$-mix from convexity alone; the source's equivalence claim | 4 |
| D0010 | D | $F(a+x) \ge 1 - (b-a)/(nx)$ necessary in the tight case | Existence of exchangeable compositions with a prescribed marginal | 3 |
| D0003 | D | Layer concatenation; the binomial family is jointly mixable | A margin-only criterion for a layer stack with prescribed counts | 3 |
| D0035 | D | Literal form false: $b_n \equiv 1/4$ is unrealisable | Characterise the realisable $\varphi$-sequences; uniform control over the past | 3 |
| E0024 | E | Yes for every pair in Rao's class, larger than Kanda and Forst | The measure-dependent conditions, whose level sets move under addition | 4 |
| E0026 | E | Reduces to the small-jump part; large jumps never obstruct | Rao's condition, or a substitute, for the small-jump component | 4 |
| E0027 | E | Yes when both summands lie in Rao's class | The case where one summand satisfies (H) only measure-dependently | 4 |
| E0008 | E | The convexity and Jensen step carries to $u_t = J*u - u + f(u)$ | A spreading statement for the nonlocal front; heavy-tailed kernels accelerate | 3 |
| E0058 | E | The log family is exactly the nonnegative kernel of $A^{\mathsf T}$ | A Lyapunov function with a quadratic increment, degenerate on all faces | 4 |
| E0066 | E | Entropy is nondecreasing; limit sets lie in the entropy-preserving set | Identify that set; needs the classification of extreme bistochastic operators | 4 |
| E0105 | E | Exact law of the detection time, capsule-union void probability, simulation-validated | Non-homogeneous intensities; the Brownian analogue | 1, 4 |
| E0104 | E | Exact reduction; settled for two balls in the inertial model | The two-set Wiener sausage volume for the Brownian case | 4 |
| F0019 | F | $f'(\beta) = -\beta R(\beta)$ at differentiability points; the question is $R > 0$ | Bound the length-$n$ replica overlap below by the one-step overlaps | 2 |
| F0029 | F | $\eta \ge 0$ in $d=3,4$; $\eta(2) \le 3/4$ from the loop-erased dimension | Domination or decoupling for successive waves | 3 |
| F0036 | F | Reduction to pairs of points of the branching-coalescing point set | The extremal-path claim for first meeting points; separation points | 2 |
| F0059 | F | $g(k) = \log(w_k\rho^k)$ cannot be subadditive | Positive density, not infinitude, of merging-favoured scales | 3 |
| F0133 | F | Unrestricted form false by MIP* = RE; conjecture is $\chi \ge \chi^*$ on its domain | Microstates from finite Fisher information without convexity | 4 |
| P0032 | X | Candidate finite prefix construction by forward density matching | Which reading of the source: stopping time, independence, or arbitrary | 1 |
| P0033 | X | Candidate counterexample with two invariant colour classes | Whether zero child weights are inside the question's scope | 1 |
| P0205 | X | Monotonicity in the geometric parameter is false on two states | The other universal bounds; the source's undefined $\tau(\infty)$ | 3 |
| P0341 | X | The unrestricted polynomial-test ansatz is false, both clauses | A sharp error theory and the admissible class of tests | 3 |
| P0342 | X | Fringe-to-finite transfer fails with a degenerate Gaussian limit | A positive-variance or quantitatively local transfer theorem | 3 |
| P0347 | X | Two one-split constants corrected; mean Colless at $3/\pi^2$ | Variances, normalised laws and joint distributions | 3 |
| P0355 | X | Literal conjecture needs an extra assumption, degenerate example | The strictly discounted nondegenerate regime | 4 |
| F0066 | F | Follows from the height conjecture; equivalent up to a logarithm | Excluded: reduces to Conjecture 20.5 | - |
| F0068 | F | Implied by either neighbouring problem, strictly weaker | Excluded: reduces to Problems 20.7 and 18.39 | - |
| P0407 | X | FCFS slowdown characterisation | Known result, not original | - |
| P0423 | X | Ideal Voronoi face-volume intensities | Known result, not original | - |
| P0424 | X | Indistinguishability of ideal hyperbolic cells | Known result, not original | - |
| P0448 | X | Offline common-concave speedup allocation | Known result, not original | - |
| P0449 | X | General FCFS multiserver-job stability representation | Known result, not original | - |
| P0460 | X | Leading logarithmic connectivity threshold | Known result, not original | - |

Sixty rows, of which fifty-two carry a closeness grade. Counting each row by its principal, that is its
first-listed, obligation: thirteen are at rank 1, nine at rank 2, seventeen at rank 3 and thirteen at rank
4, with eight rows outside the ranking. The middle of that distribution is where the chapter's character
lies. Rank 3 is the largest class, and rank 3 means the same thing in every one of those seventeen rows:
the mechanism is identified exactly, often by an identity that can be written in one line, and the missing
half is quantitative and was not attempted. That is what a month of reading sources with a few hours of
computing on each produces. The thirteen rank 1 rows are the ones worth an afternoon each, and five of
them, P0174, G0014, G0015, P0032 and P0033, are obligations to read a source correctly rather than to
prove anything.

One caution applies to every row. The verification column of these ledgers reads `unreviewed` far more
often than anything else, and where it reads `author_checked` the author is the same agent that produced
the argument. The audits of 8 September found no wrong calculation anywhere they looked: all 25 written
proof files of the Codex campaign were read, and all eight of intake D's literature exclusions were checked
against their sources. That is the strongest evidence available that the mathematics here is sound. What
the same audits did find were three overstated conclusions among the six flagged intake-D partials, and one
live problem thrown away, which is D0039 above. Both of those failure modes were caught by reading rather
than by computing, which is the reason so many of the obligations in this chapter are readings. Nothing in
this chapter has been independently refereed.
