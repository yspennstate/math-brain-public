# Overlap wells and local minima

The result below isolates the landscape implication needed in T347.
A strict well in the shell ground-state profile supplies a single-spin
local minimum. The absence of such a well does not, for general binary
Hopfield patterns, exclude even strict local minima at overlap tending to
one. The counterexample has correlated patterns. It establishes no
capacity bound for iid patterns.

## 1. Finite-volume implication and stability convention

Fix arbitrary patterns \(\xi^1,\ldots,\xi^M\in\{-1,1\}^N\), and set
\[
 Q(\sigma)=\sum_{\nu=1}^M(\xi^\nu\cdot\sigma)^2,
 \qquad H(\sigma)=-\frac{Q(\sigma)}{2N}.
\]
For a reference pattern \(\xi^\mu\), let
\[
 d_\mu(\sigma)=\#\{i:\sigma_i\ne\xi_i^\mu\},
 \quad m_\mu(\sigma)=1-\frac{2d_\mu(\sigma)}N,
 \quad E_\mu(d)=\max_{d_\mu(\sigma)=d}\frac{Q(\sigma)}{2N^2}.
\]
Thus larger \(E_\mu\) means smaller energy, and
\(\min_{d_\mu=d}H=-NE_\mu(d)\).

**Proposition 1.** If integers \(0\le d_a<d_b\le N\) satisfy
\(E_\mu(d_a)>E_\mu(d_b)\), there is a single-spin local minimum
\(\widehat\sigma\) with \(d_\mu(\widehat\sigma)<d_b\).
It is a fixed point of asynchronous zero-temperature dynamics using the
zero-diagonal local field and retaining the current spin at a tie.

**Proof.** Choose \(\sigma^a\) attaining the maximum on shell \(d_a\).
Minimize \(H\) on the finite cap
\(C=\{\sigma:d_\mu(\sigma)\le d_b\}\), obtaining \(\widehat\sigma\).
Then
\[
 H(\widehat\sigma)\le H(\sigma^a)
 =-NE_\mu(d_a)<-NE_\mu(d_b)
 \le H(\tau)\qquad(d_\mu(\tau)=d_b).
\]
Consequently \(d_\mu(\widehat\sigma)\le d_b-1\). A single spin flip
changes Hamming distance by one, so every neighbor of
\(\widehat\sigma\) belongs to \(C\). Minimality in \(C\) proves
\(H(\widehat\sigma)\le H(\widehat\sigma^{(i)})\) for every \(i\).

To verify the dynamics assertion, put
\[
 A_{ij}=\sum_{\nu=1}^M\xi_i^\nu\xi_j^\nu,
 \quad J=A/N,\quad
 h_i^0(\sigma)=\frac1N\sum_{j\ne i}A_{ij}\sigma_j.
\]
Expanding the quadratic form gives the exact identities
\[
 Q(\sigma)-Q(\sigma^{(i)})
   =4\sigma_i\sum_{j\ne i}A_{ij}\sigma_j,
 \qquad H(\sigma^{(i)})-H(\sigma)=2\sigma_i h_i^0(\sigma).
\]
The local-minimum condition is therefore \(\sigma_i h_i^0\ge0\)
for every \(i\). These are precisely the fixed-point conditions with
ties retained. The inequality is strict for all \(i\) exactly when
the local minimum is strict. Since \(A_{ii}=M\), using the full field
instead would require
\[
 \sigma_i(J\sigma)_i\ge M/N,
\]
not merely a nonnegative full field. The diagonal contributes a constant
to \(H\), but must be removed in a coordinate update. \(\square\)

If an initial state has energy below every state on shell \(d_b\),
strictly energy-decreasing updates starting inside the cap cannot leave
it: any path out visits that shell first. Such updates, continued whenever
an energy-decreasing flip is available, terminate because the state space
is finite. Their terminal state is another local minimum
inside the cap. This asserts trapping for those initial states only;
Proposition 1 does not assert that every state in the cap is attracted.

**Corollary 2 (conditional iid consequence).** Suppose \(M_N=O(N)\)
and, for some fixed \(0\le a<b<1/4\) and \(\delta>0\), with probability
tending to one,
\[
 E_\mu(\lfloor aN\rfloor)
 \ge E_\mu(\lfloor bN\rfloor)+\delta
 \quad\text{for every }\mu\le M_N.
\]
Then with probability tending to one every pattern has a local minimum
within distance \(\lfloor bN\rfloor-1\). For iid uniform patterns these
minima can be chosen distinct.

**Proof.** For sufficiently large \(N\) the two shell indices are
ordered. Apply Proposition 1 to every pattern on the stated common event.
For distinct iid patterns their Hamming distance \(D\) has the binomial
law \(\operatorname{Bin}(N,1/2)\). For completeness, for \(c<1/2\),
\[
 \mathbb P(D\le cN)
 \le\exp[-2N(1/2-c)^2].
\]
Indeed, \(Y_i=1/2-\mathbf1_{\{\xi_i^\mu\ne\xi_i^\nu\}}\) takes
values \(\pm1/2\) independently, and
\(\mathbb E e^{tY_i}=\cosh(t/2)\le e^{t^2/8}\).
The last inequality follows by integrating
\(\tanh u\le u\). Markov's inequality bounds the tail by
\(\exp[-tN(1/2-c)+Nt^2/8]\); choosing \(t=4(1/2-c)\) gives the
displayed bound. Take \(c=2b<1/2\) and union bound over at most
\(M_N^2/2\) pairs. With probability tending to one, all pair distances
exceed \(2\lfloor bN\rfloor\), so the Hamming caps are disjoint.
Their respective minima are distinct. \(\square\)

For example, the common event in Corollary 2 follows if the two shell
profiles converge to deterministic limits with a positive gap and the
failure probability for either shell of one specified pattern is
\(o(1/M_N)\), uniformly in the pattern label. The union bound does not
require independence between shell energies. Existence of the limiting
expected profile alone supplies no such failure-probability estimate.

## 2. An exact finite counterexample to the converse

Here are eleven binary patterns on twelve neurons. A sign string lists
coordinates from 1 to 12. The first pattern is the reference.

| Pattern | Sign string |
|---|---|
| 1 | `++++++++++++` |
| 2 | `-++-+-+-+--+` |
| 3 | `++--+++-+++-` |
| 4 | `+---+-+-++-+` |
| 5 | `-+--+++-++++` |
| 6 | `+--++----++-` |
| 7 | `+++-+--++-+-` |
| 8 | `+-+-+--++++-` |
| 9 | `++-+++---+--` |
| 10 | `++-+-----+++` |
| 11 | `--+--+--+-++` |

Call this \(11\)-by-\(12\) pattern matrix \(P\), and write
\(Q_P(s)=\|Ps\|^2\). Set
\[
 s_*=(1,1,1,-1,1,1,1,1,1,1,1,-1).
\]
Direct multiplication gives
\[
 Ps_*=(8,0,8,0,4,-2,6,6,0,-4,-2),\qquad Q_P(s_*)=240.
\]
Writing \(A=P^\mathsf TP\), the signed off-diagonal fields are
\[
 \left(s_{*,i}\sum_{j\ne i}A_{ij}s_{*,j}\right)_{i=1}^{12}
 =(9,9,1,9,25,1,5,5,25,5,13,1).
\]
These values can also be obtained as
\(s_{*,i}(P^\mathsf TPs_*)_i-11\), using the displayed vector
\(Ps_*\). Every entry is positive. Hence \(s_*\) is a strict local
minimum, its overlap with the first pattern is \(2/3\), and the smallest
single-flip energy increase is \(2/12=1/6\).

Exhaustive exact integer enumeration of all \(2^{12}\) states gives
\[
 \left(\max_{d(s,\boldsymbol1)=d}Q_P(s)\right)_{d=0}^{6}
 =(192,236,256,284,288,300,304).
\]
The remaining shells follow by \(Q_P(-s)=Q_P(s)\). Thus the shell
energy-gain profile is nonincreasing as positive overlap increases: it
has no pair \(0\le m_b<m_*\le1\) with the value at \(m_*\) larger
than the value at \(m_b\). Nonetheless \(s_*\) is a strict local
minimum. It is not even optimal on its own shell: the maximum there is
256, attained for example at
\((1,1,-1,1,1,1,1,-1,1,1,1,1)\).

The shell maxima in this paragraph are a finite computational certificate,
verified by `audit_landscape.py` in two independent quadratic expressions.
The next proposition uses only the explicit positive fields above and
the elementary bound \(0\le Q_P(s)\le11\cdot12^2=1584\); it does not
depend on an exhaustive enumeration claim.

## 3. Flat limiting profiles with strict minima near every pattern

**Proposition 3.** For any integer \(B\ge2\), there is a sequence of
deterministic binary Hopfield pattern arrays with
\[
 \frac{M_N}{N}\longrightarrow\frac{11}{B}
\]
such that the following hold:

1. Uniformly over all stored patterns and all their allowed overlaps, the
   shell energy-gain profiles converge to the constant \(11/2\).
2. Every stored pattern has a strict single-spin local minimum at Hamming
   distance at most 12, hence at overlap at least \(1-24/N\).
3. The smallest single-spin energy increase at each constructed minimum
   is at least \(2K/N\), where \(K\to\infty\) and \(N=12+B(K-1)\).
   In particular this lower bound tends to \(2/B>0\).

**Proof.** Let \(K=2^q\), with \(q\ge1\) and \(q\to\infty\), and write
\(\mathbb F_2^q\) for the binary vector space. For \(a,z\) in that
space put
\[
 \chi_a(z)=(-1)^{a\cdot z}.
\]
For \(a\ne0\), choose a coordinate \(j\) with \(a_j=1\).
The pairing \(z\leftrightarrow z+e_j\) reverses \(\chi_a\), proving
\(\sum_z\chi_a(z)=0\). Since
\(\chi_a\chi_b=\chi_{a+b}\), this also proves
\[
 \sum_z\chi_a(z)\chi_b(z)=K\mathbf1_{\{a=b\}}.
\]

Take twelve core neurons and one block of \(B\) additional neurons for
each nonzero \(a\in\mathbb F_2^q\). Thus \(N=12+B(K-1)\).
The patterns are indexed by \((\mu,z)\), where \(1\le\mu\le11\)
and \(z\in\mathbb F_2^q\). Their entries are
\[
 \xi^{\mu,z}_i=P_{\mu i}\quad(1\le i\le12),
 \qquad
 \xi^{\mu,z}_{a,\ell}=\chi_a(z)
 \quad(a\ne0,\ 1\le\ell\le B).
\]
There are \(M_N=11K\) patterns. The first core pattern with \(z=0\)
is the all-positive reference.

The Gram matrix of these patterns is block diagonal. Its core block is
\(KA\). Its core-to-additional-block entries vanish because
\(\sum_z\chi_a(z)=0\). Between two additional blocks its entries
are \(11K\mathbf1_{\{a=b\}}\), by orthogonality. In particular,
the diagonal block for each \(a\) is \(11K\) times the all-ones
\(B\)-by-\(B\) matrix. For any configuration \((s,u)\), if
\(S_a=\sum_{\ell=1}^B u_{a,\ell}\), the exact energy numerator is
\[
 Q(s,u)=KQ_P(s)+11K\sum_{a\ne0}S_a^2. \tag{1}
\]

Fix an arbitrary reference pattern \(\xi^{\mu,z}\) and any distance
\(d\in\{0,\ldots,N\}\). In every configuration, (1) gives
\[
 Q\le K\cdot1584+11KB^2(K-1). \tag{2}
\]
To give a lower bound on the shell maximum, prescribe
\(d_p=\min\{d,B(K-1)\}\) errors among the additional neurons and
\(d_c=d-d_p\) errors among the core neurons. The latter is between
0 and 12 and can always be realized. Make as many entire additional
blocks erroneous as possible, then place any residual errors in one
more block. Because the reference is constant within each such block,
every wholly correct or wholly erroneous block has \(S_a^2=B^2\).
There is at most one partially erroneous block. Its squared block sum
is nonnegative. Since \(Q_P\ge0\), this configuration satisfies
\[
 Q\ge11KB^2(K-2). \tag{3}
\]
The bounds (2)--(3) do not depend on \(\mu,z,d\). Consequently every
shell profile lies between
\[
 \frac{11KB^2(K-2)}{2[12+B(K-1)]^2}
 \quad\text{and}\quad
 \frac{1584K+11KB^2(K-1)}{2[12+B(K-1)]^2}.
\]
Both quantities tend to \(11/2\). This proves uniform convergence
over the reference patterns and the entire overlap grid to a constant
profile. In particular the limiting profile has no strict well.

For each pattern \(\xi^{\mu,z}\), take the core configuration to be
\(s_*\), and make every additional block equal to that pattern's
block value \(\chi_a(z)\). There are at most twelve mismatches, all
in the core. Flipping core spin \(i\) changes \(Q\) by the core
difference multiplied by \(K\), so
\[
 H(\sigma^{(i)})-H(\sigma)
 =\frac{2K}{N}
  s_{*,i}\sum_{j\ne i}A_{ij}s_{*,j}\ge\frac{2K}{N}>0.
\]
Flipping one spin in a uniform additional block changes its squared
sum from \(B^2\) to \((B-2)^2\). Its energy increase is exactly
\[
 \frac{11K}{2N}\big[B^2-(B-2)^2\big]
 =\frac{22K(B-1)}{N}>0.
\]
Since \(B\ge2\), the smallest possible increase is at least
\(2K/N\). Every constructed configuration is a strict local minimum
and its overlap is at least \(1-24/N\). Finally,
\(11K/[12+B(K-1)]\to11/B\), completing the proof. \(\square\)

For example, \(B=79\) gives limiting load
\(11/79=0.139240506329\ldots\). This is a construction for correlated
patterns, not a counterexample to the proposed iid threshold. Its point
is that even the conjunction of a linear number of binary patterns,
a uniform limiting shell profile, and strict local stability does not
make the converse of Proposition 1 valid. Here barriers of order one
in total energy disappear after dividing energy by \(N\). To see the
upper bound on those barriers, reverse one uniform block at a time.
The energy excess during a block reversal is at most
\(11KB^2/(2N)=O(1)\). Changing the core has energy range at most
\(1584K/(2N)=O(1)\) as well, for fixed \(B\). The positive minimum
flip cost gives a nonvanishing lower bound.

## 4. Consequence for the earlier literature audit

The finite implication in Proposition 1 explains how simultaneous
energy barriers of the kind stated in Theorem 1.2(e) of the capacity
preprint yield local minima. Proposition 3 shows why the absence of a
strict well in the limiting overlap profile cannot by itself give the
opposite implication. To obtain the upper direction of T347 for iid
patterns one still needs an argument excluding local minima that are
invisible to that profile, with a precise overlap criterion.
The example has a flat limiting profile. It does not refute a possible
exclusion theorem that uses strict decrease of the limiting profile
together with additional iid information.

The references used for this scope comparison are Ayman Ali, Jeanne
Boursier, Hong-Bin Chen, Fu-Hsuan Ho, Victor Issa, Jean-Christophe
Mourrat, *Free energy of the Hopfield model*,
[arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1), and
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*, contributed by Yuwen
Zhou, [Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
No numerical capacity certificate or general replica-symmetry claim is
proved here.
