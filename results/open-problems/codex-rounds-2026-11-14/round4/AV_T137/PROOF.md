# Source-level identification of the diluted Lean statement

This note identifies the definitions in the saved `Model.lean` with the
quantities in the saved manuscript `model.tex`. It does not prove the
Mézard–Parisi formula or check the imported Lean proofs.

## Model and admissibility

Identify `false` with -1 and `true` with +1. This is a bijection from
`Spin := Bool` to the manuscript's spin space. A function `Fin N → Spin`
therefore enumerates each of the 2^N spin configurations exactly once.
The default norm of a function on a finite type is the supremum norm;
thus `‖z.1‖` is max_s |theta(s)|. The projections of
`InteractionSample p` give theta, a, b and the p functions f_l.

The fields of `Admissible M` impose p >= 2, even p, positive density,
integrability of max_s |theta(s)| and |h|, and almost-sure equality

\[
e^{\theta(s)}=a\left(1+b\prod_l f_l(s_l)\right),\qquad
a>0,\quad \left|b\prod_l f_l(s_l)\right|<1.
\]

The remaining fields impose mutual independence and identical laws for
the f_l, independence of b from their entire vector, and finite
nonnegative expectations E[(-b)^n] for n >= 1. These are the paper's
standing hypotheses. In particular, there is no independence condition
on a and no separate integrability condition on log a. Encoding the
witness together with theta merely takes its joint law; the pressure
and functional use the theta projection alone. The almost-sure
quantifier simultaneously over spin tuples is equivalent to one for
each tuple because there are finitely many tuples.

The explicit moment-integrability field corresponds to the paper's
requirement that the expectations be finite. It is not an additional
bounded-coupling hypothesis.

## Finite-system pressure

Fix N >= 1 and a clause count k. There are N^(kp) maps

\[
\texttt{indices}:\operatorname{Fin}k\to\operatorname{Fin}p
\to\operatorname{Fin}N.
\]

Uniformly averaging over these maps gives probability N^(-kp) to every
ordered endpoint tuple. This is exactly kp independent uniform indices,
including repetitions. The product measures on the theta samples and
fields give independent disorder with the prescribed laws, and the
outer `poissonMeasure (M.alpha * N)` gives k ~ Pois(alpha N).

`logWeight` is the manuscript's -H_N, and `logPartition` is its log Z_N
with counting measure. Consequently, for every N >= 1,

\[
\texttt{pressure M N}=N^{-1}\mathbb E\log Z_N=F_N.
\]

There is no perturbation term in this definition. All expectations are
ordinary integrable expectations: pointwise,

\[
|\log Z_N-N\log2|
\leq\sum_{j=1}^k B(\theta_j)+\sum_{i=1}^N|h_i|,
\]

whose expectation is alpha N E B(theta) + N E|h|. Thus neither the
division at N=0 nor the totalized integral of a nonintegrable function
explains the convergence statement. Only N >= 1 matters to the limit.

## Messages and the hierarchy

The Lean `q`, `edge`, `appendSpin`, `message` and `siteLog` give,
respectively, q_x, C_theta, insertion of the last spin, U_theta and
log V_s in the manuscript. In particular the division by 2 in
`siteLog` is precisely the spin average in V_s. Each label is distinct:
`Fin p` for an edge and `Fin k × Fin (p-1)` for a site insertion.

Put H_0 = R and H_(j+1) = P(H_j), with the weak topology and its Borel
sigma-field. This is `Hierarchy j`. Therefore H_j = M_j for j >= 1,
and a trial law `ζ : Hierarchy (r+1)` is the manuscript's ζ in M_(r+1).
No finite-support restriction or message-moment condition occurs.

For fixed physical disorder let g = log V, where V is either V_s or
V_e. Let L_r(g;m;eta) denote Lean's `logMean r g m eta`. Its definition is

\[
L_0(g;x)=g(x),\qquad
L_r(g;m;\eta)=\frac1{m_1}\log
\int \exp\{m_1 L_{r-1}(g;(m_2,\ldots,m_r);x)\}
\prod_\omega\eta^\omega(dx^\omega).
\tag{1}
\]

We identify this with log T_0 V by induction on r. For r=0 both sides
are log V. For r >= 1, condition on the root measures eta_0. Their
independent descendants have product law over the message labels. The
remaining levels, with exponents m_2,...,m_r, give
L_(r-1) = log T_1 V by the induction hypothesis. Hence
exp(m_1 L_(r-1)) = (T_1 V)^(m_1). Integrating the descendants and taking
log divided by m_1 gives exactly the paper's definition of log T_0 V.
The root measures themselves are then independently averaged with law
ζ in `trialLog`. Physical disorder remains fixed in g during every
step of (1).

In particular, r=1 gives m_1^(-1) log E_x V^(m_1) conditional on eta_0,
and r=2 gives

\[
\frac1{m_1}\log\mathbb E_{\eta_1\mid\eta_0}
\left[\left(\mathbb E_{x\mid\eta_1}V^{m_2}\right)^{m_1/m_2}\right].
\]

These agree with the manuscript's two explicit examples. The increasing
exponents are not reversed. At r=0 `trialLog` directly averages g over
iid real messages of law ζ, also as stipulated in the manuscript.

These operations are well defined for the actual g. The normalized
weights q_x are positive and sum to one. Therefore |log V_e| <= B(theta)
and |log V_s| <= |h| + sum_j B(theta_j). If |g| <= D, m > 0, and μ is a
probability measure, then

\[
e^{-mD}\leq\int e^{mg}\,d\mu\leq e^{mD}.
\]

Its logarithm divided by m lies in [-D,D]. Induction applies at every
level, independently of the values of the messages. For the actual
continuous functions of the messages these are Borel integrals; their
continuity and boundedness at subsequent levels follow from the weak
topology and the same bounds. Thus the positive logarithms do not
conceal a log-zero case. Integrating physical disorder is finite under
the stated first moments.

## Functional and infima

The definition of `functional` now gives exactly

\[
\log2+\mathbb E\log T_0V_s
-\alpha(p-1)\mathbb E\log T_0V_e=\mathcal B_r(\zeta,m).
\]

The site clause count is Pois(alpha p). The edge correction is one
clause multiplied by alpha(p-1), as in the paper. `Exponents` gives
0 < m_1 < ... < m_r < 1, vacuously at r=0. `phi` is the infimum over
the same trial laws and exponents, and `variationalValue` is the
infimum over every natural r, including zero.

The real infima are nonempty and bounded below. Iterated Dirac laws at
zero supply a trial law at every depth, and m_i = i/(r+1), 1 <= i <= r,
supplies exponents. Uniformly in the trial law, depth and exponents,

\[
|\mathcal B_r-\log2|
\leq\mathbb E|h|+\alpha(2p-1)\mathbb E B(\theta).
\]

This also bounds all Phi_r. Thus the formal infima describe the usual
finite real infima, rather than exceptional values for empty or
unbounded-below sets.

## Requested examples and checks against missed cases

For theta(s)=beta J product_l s_l, take a=cosh(beta J),
b=tanh(beta J), and every f_l(s)=s. The f_l are deterministic and hence
iid and independent of b. Symmetry of J makes odd moments of -b zero;
even moments are nonnegative and every moment is finite because |b|<1.
B(theta)=beta|J|. This includes both requested coupling laws and every
finite beta > 0 without bounding J. Set the field to zero for T137.

For a soft SAT clause of weight one, take a=1,
b=e^(-beta)-1 and f_l(s)=(1+epsilon_l s)/2, with independent fair signs.
The product of these functions is an indicator I, and
e^(-beta I)=1+(e^(-beta)-1)I. The product bound is strict at finite beta,
all moments of -b are nonnegative, and B(theta)=beta. This verifies
the stated even-K SAT instances. Odd K fails `Admissible.even`; these
witnesses do not remove that hypothesis. Infinite beta is also outside
the theorem.

As a normalization check, take a constant clause theta=t with
factorization a=e^t, b=0, f_l=0 and any integrable field law. Direct
factorization gives

\[
F_N=\log2+\mathbb E\log\cosh h+\alpha t\quad(N\geq1).
\]

For every trial hierarchy, log V_s=log cosh h+k t and log V_e=t.
All power means preserve constants, so the functional is the same
quantity: log2+E log cosh h+alpha p t-alpha(p-1)t. This separately
checks the sign, the spin-average factor, and the density coefficient.
At t=h=0 both sides are log2, not zero.

The saved solution definitions and challenge definitions agree even
before removing comments and internal whitespace, up to the challenge's
extra theorem comment and stub. `audit_definitions.py` independently
checks the normalized block and both theorem headers. These source
identities establish the correspondence of the displayed statement;
they are not a check of Lean's elaboration environment, its libraries,
the imported lower-bound proof, or the complete manuscript.
