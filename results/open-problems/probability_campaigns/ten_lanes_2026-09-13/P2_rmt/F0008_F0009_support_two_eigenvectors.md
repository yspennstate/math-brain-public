# F0008 and F0009. The polynomial prefactor in Vu's simplicity conjectures, and an exponential lower
# bound for the singular-value-distinctness conjecture

Random matrix theory, 13 September 2026.

## The two problems

Source for both: Van Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797
(fetched and read 2026-09-13). $M_n^{\mathrm{sym}}$ is the random symmetric matrix whose entries on
and above the diagonal are i.i.d. uniform on $\{-1,+1\}$.

**F0008** (Vu, Conjecture 8.4, Simplicity). Let $s_n=\mathbb{P}(\text{the spectrum of
}M_n^{\mathrm{sym}}\text{ is not simple})$. Vu writes, verbatim:

> We observe that $s_n \ge 4^{-n}$, which is the probability that the first 3 rows are the same
> (which guarantees that zero is an eigenvalue with multiplicity at least 2).
>
> **Conjecture 8.4 (Simplicity).** $s_n = (4+o(1))^{-n}$.

**F0009** (Vu, Conjecture 8.5). Verbatim:

> **Conjecture 8.5.** With probability $1-o(1)$, the singular values of $M_n^{\mathrm{sym}}$ are
> different.
>
> Notice that the singular values of a symmetric matrix are the absolute values of its eigenvalues.
> Thus, this conjecture asserts that there is no two eigenvalues adding up to zero.

No polynomial prefactor appears anywhere near either conjecture, and Vu gives no lower-bound
construction at all for 8.5. (He does give a prefactor elsewhere — Conjecture 2.2 for the
non-symmetric singularity probability reads $p_n=(2+o(1))n^22^{-n}$ — so the absence here is not a
convention.)

## What was in the ledger, and what is wrong with it

The ledger's last attempt on **F0009** argued:

> No sign-symmetry can force this: if $DMD=-M$ for a diagonal sign matrix $D$ then every diagonal
> entry of $M$ would vanish, impossible for $\pm1$ entries; so unlike the repeated-eigenvalue problem
> there is no local structure of exponential probability, and the conjectured event should have
> super-exponentially small probability.

The first clause is correct. The conclusion is **false**: there is a local structure of probability
$\Theta(4^{-n})$, and it is the same structure that drives Conjecture 8.4. The ledger's attempt on
**F0008** makes the mirror-image error, saying of the repeated-*nonzero*-eigenvalue case that "a
naive equidistribution heuristic puts $\mathbb{P}(\mathrm{discriminant}=0,\lambda\ne0)$ far below any
exponential". That is also false: repeated nonzero eigenvalues occur with probability at least
$\tfrac12n^4 4^{-n}(1-o(1))$, by the same construction.

## The primitive: support-two eigenvectors

Everything below runs on one observation. For a symmetric matrix $M$ and $i\ne j$, the vector
$e_i-e_j$ is an eigenvector if and only if

$$M_{mi}=M_{mj}\ \ (m\notin\{i,j\}),\qquad M_{ii}=M_{jj},$$

in which case the eigenvalue is $\lambda=M_{ii}-M_{ij}$; and $e_i+e_j$ is an eigenvector if and only
if

$$M_{mi}=-M_{mj}\ \ (m\notin\{i,j\}),\qquad M_{ii}=M_{jj},$$

with eigenvalue $\mu=M_{ii}+M_{ij}$. For $M_n^{\mathrm{sym}}$ each is $n-1$ independent fair-coin
conditions, so a *single* support-two eigenvector on a given pair costs $2^{-(n-1)}$ and there are
$2\binom n2$ of them: the expected number is $\sim n^22^{-n}$. That is exactly the mechanism behind
the singularity conjecture (a support-two eigenvector with eigenvalue $0$ is a pair of equal rows),
and the point of this memo is that **two disjoint support-two eigenvectors are the cheapest way to
produce every one of the spectral coincidences in Section 8 of the survey**, at cost $4^{-n}$ with
$\Theta(n^4)$ choices.

Both eigenvalues $\lambda,\mu$ lie in $\{-2,0,2\}$, each taking the value $0$ with probability $1/2$
and $\pm2$ with probability $1/4$ — and this is the whole reason the constant comes out the same for
the two conjectures: $\mathbb{P}(\mu+\nu=0)=\mathbb{P}(\mu=\nu)=\tfrac14+\tfrac1{16}+\tfrac1{16}
=\tfrac38$.

## The construction

Let $\{i,j\}$ and $\{k,l\}$ be disjoint pairs and let $s_1,s_2\in\{+,-\}$. Consider the event
$E_{s_1s_2}^{\mathrm{zero}}(\{i,j\},\{k,l\})$ that $e_i+s_1e_j$ and $e_k+s_2e_l$ are both
eigenvectors and their eigenvalues sum to zero; and $E^{\mathrm{eq}}_{s_1s_2}$, the same with equal
eigenvalues. Because the two vectors have disjoint supports they are orthogonal and nonzero, so on
$E^{\mathrm{zero}}$ there are two distinct spectral indices whose eigenvalues sum to zero (also when
that common value is $0$: then the eigenvalue $0$ has multiplicity $\ge2$), and on $E^{\mathrm{eq}}$
there is a repeated eigenvalue.

**Exact probability.** For each of the eight combinations (four sign patterns $\times$ two relations),
for every fixed ordered quadruple of distinct indices,

$$\mathbb{P}\big(E_{s_1s_2}^{\bullet}\big)=3\cdot4^{-n},\qquad
\mathbb{P}\big(E_{s_1s_2}^{\bullet}\cap\{\text{eigenvalue}\ne0\}\big)=1\cdot4^{-n}.$$

Derivation. Outside $\{i,j,k,l\}$ there are $n-4$ rows, each contributing one condition for each
eigenvector: $(1/4)^{n-4}$. Inside the block, the four cross entries $M_{ik},M_{il},M_{jk},M_{jl}$
must satisfy the two constraints coming from each eigenvector evaluated at the other pair's indices,
which pins them to one free sign out of sixteen assignments: $1/8$. The two diagonal equalities
$M_{ii}=M_{jj}$, $M_{kk}=M_{ll}$ give $1/4$. The eigenvalue relation is $3/8$ as computed above
(restricted to a nonzero common value, $1/8$). Multiplying, $\frac18\cdot\frac14\cdot\frac38
\cdot4^{-(n-4)}=3\cdot4^{-n}$, and $\frac18\cdot\frac14\cdot\frac18\cdot4^{-(n-4)}=4^{-n}$.

*Machine check.* Exhaustive enumeration of **all** $2^{n(n+1)/2}$ symmetric $\pm1$ matrices for
$n=4,5,6$ (`template_prob.py`, `template_all.py`, exact rational arithmetic) returns
$\mathbb{P}\cdot4^n=3$ and $1$ for every one of the eight combinations at every one of the three
sizes. Not approximately: exactly $3/256$, $3/1024$, $3/4096$.

For a fixed unordered pair-of-pairs the four sign assignments are mutually exclusive (they demand
$M_{mi}=M_{mj}$ and $M_{mi}=-M_{mj}$ simultaneously), and there are $\tfrac18n(n-1)(n-2)(n-3)$
unordered pairs-of-pairs, so

$$\sum_{\text{templates}}\mathbb{P}=\tfrac18n(n-1)(n-2)(n-3)\cdot4\cdot3\cdot4^{-n}
=\tfrac32\,n(n-1)(n-2)(n-3)\,4^{-n}$$

for each of the two relations, and $\tfrac12n(n-1)(n-2)(n-3)4^{-n}$ for the nonzero-eigenvalue part.

**Bonferroni.** Two distinct templates force at least three support-two eigenvectors on distinct
pairs (if they share one pair) or four (if they share none), so the joint probability is
$O(8^{-n})$ or $O(16^{-n})$, and the number of such pairs of templates is $O(n^6)$ resp. $O(n^8)$.
Since $n^68^{-n}+n^816^{-n}=o(n^44^{-n})$, the second Bonferroni term is negligible.

**Proposition.** As $n\to\infty$,
$$\mathbb{P}\big(\exists\,i\ne j:\ \lambda_i+\lambda_j=0\big)\ \ge\ \big(\tfrac32-o(1)\big)n^4\,4^{-n},
\qquad
\mathbb{P}\big(\exists\,i\ne j:\ \lambda_i+\lambda_j=0,\ \lambda_i\ne0\big)\ \ge\ \big(\tfrac12-o(1)\big)n^4\,4^{-n},$$
$$s_n\ \ge\ \big(\tfrac32-o(1)\big)n^4\,4^{-n},
\qquad
\mathbb{P}\big(\exists\,i\ne j:\ \lambda_i=\lambda_j\ne0\big)\ \ge\ \big(\tfrac12-o(1)\big)n^4\,4^{-n}.$$

The first two are the content for F0009; the last two for F0008. Explicit matrices realising each
construction were built and their characteristic polynomials factored exactly with sympy for
$n=4,\dots,9$ (`f0009_construct.py`): in the "opposite" family both $+2$ and $-2$ are eigenvalues,
in the "repeat" family $2$ has multiplicity $\ge2$, at every size.

## What this says about the two conjectures

**F0008.** The survey's lower bound is $s_n\ge4^{-n}$ from three equal rows, i.e. $\Theta(n^3 4^{-n})$
once one counts the $\binom n3$ triples. The two-disjoint-pairs construction gives $\Theta(n^44^{-n})$
and therefore supersedes it: the cheapest mechanism is not three equal rows but *two* independent
two-row coincidences, and the prefactor is $n^4$, not $n^3$. Conjecture 8.4 is untouched — it only
claims base $4$ — but its sharp form should read
$$s_n=(c+o(1))\,n^4\,4^{-n}.$$

**F0009.** The ledger's reading was that the event should be super-exponentially rare. It is not:
its probability is at least $\tfrac32 n^44^{-n}$, the same order as the lower bound for $s_n$.
Conjecture 8.5 survives comfortably — this is still $o(1)$ — but the rate is now pinned from below,
and any proof of 8.5 has to be able to see an event of probability $\Theta(n^44^{-n})$ rather than
the $e^{-n^c}$ that the current gap technology resolves. The construction contributes *identically*
to the two events, because $\mathbb{P}(\mu+\nu=0)=\mathbb{P}(\mu=\nu)=3/8$ for the two independent
$\{-2,0,2\}$-valued eigenvalues; whether that common contribution is the leading term of either is
open (see the numerics, which say it is not yet at $n\le13$).

**Where the difficulty now sits.** Yi Han, *Repeated singular values of a random symmetric matrix and
decoupled singular value estimates*, arXiv:2504.15992 (April 2025), proves that all singular values of
$M_n^{\mathrm{sym}}$ in $[\kappa n^{1/2},(2-\kappa)n^{1/2}]$ are distinct with probability
$1-e^{-cn}$, for every $\kappa>0$; he states Conjecture 8.5 is open in full. Every $\pm$ pair my
construction produces sits at $\lambda=\pm2$ — that is $O(1)$, deep inside the window
$|\lambda|<\kappa n^{1/2}$ that his theorem cannot reach. So the cheapest obstruction to Conjecture
8.5 lives exactly in the part of the spectrum the current technology excludes, and it costs $4^{-n}$,
not $e^{-n^c}$. That is the concrete target: any proof of 8.5 has to handle $|\lambda|=O(1)$ and
must be able to see an event of probability $n^44^{-n}$.

## Numerical record

**Exhaustive census, $n=2,\dots,7$** (`census.py`, `census7.py`). Every symmetric $\pm1$ matrix was
enumerated up to the diagonal sign-conjugation group $M\mapsto DMD$ — each orbit has size exactly
$2^{n-1}$ and contains exactly one matrix with $M_{0j}=+1$ for $j\ge1$, and every event here is
orbit-invariant, so the normalised counts are exact probabilities. Events were screened on floating
eigenvalues and then **decided exactly** on the integer characteristic polynomial: a $\pm$ pair with
$\lambda\ne0$ iff $\gcd(E,O)$ has a nonzero root, where $p(x)=E(x^2)+xO(x^2)$; a repeated eigenvalue
iff $\gcd(p,p')$ is nonconstant; corank $\ge2$ iff $x^2\mid p$. The smallest float margin among
matrices *not* flagged was $0.12$ at $n=6$ and $6.7\cdot10^{-3}$ at $n=7$, against a screening
threshold of $10^{-7}$, so there are no false negatives.

| $n$ | $\mathbb{P}(\text{pair}=0)$ | $\mathbb{P}(\text{pair}=0,\lambda\ne0)$ | $s_n$ | $\mathbb{P}(\text{rep.}\ne0)$ | $\mathbb{P}(\mathrm{corank}\ge2)$ | $\mathbb{P}(\text{integral spec.})$ |
|---|---|---|---|---|---|---|
| 2 | 1/2 | 1/2 | 0 | 0 | 0 | 1/2 |
| 3 | 1/2 | 3/8 | 1/4 | 1/8 | 1/8 | 5/8 |
| 4 | 0.5625 | 0.484375 | 0.25 | 0.125 | 0.125 | 0.078125 |
| 5 | 0.494141 | 0.380859 | 0.238281 | 0.125 | 0.113281 | 0.075195 |
| 6 | 0.452393 | 0.374969 | 0.225464 | 0.124237 | 0.102905 | 0.004181 |
| 7 | 0.335609 | 0.271184 | 0.157658 | 0.083453 | 0.076841 | 0.003683 |

These sizes are nowhere near asymptotic — $\mathbb{P}\cdot4^n/n^4$ is still rising — which is exactly
what one expects when the leading term carries an $n^4$ and the corrections carry $n^3,n^2$.

**Monte-Carlo census, $n=8,\dots,13$** (`mc_census.py`; $2$–$6\times10^6$ draws each, same exact
decision procedure, and every hit additionally tested for the presence of the construction). All
figures below are in units of $n^4 4^{-n}$, so the Proposition predicts that the *construction's own*
column converges to $\tfrac32$ from below (it is $\tfrac32\frac{n(n-1)(n-2)(n-3)}{n^4}$ times one
minus the Bonferroni overlap).

| $n$ | $\mathbb{P}(\text{rep.})\cdot\frac{4^n}{n^4}$ | constr. share | constr. own | $\mathbb{P}(\text{pair}=0)\cdot\frac{4^n}{n^4}$ | constr. share | constr. own | predicted constr. | ratio |
|---|---|---|---|---|---|---|---|---|
| 8 | 1.896 | 0.249 | 0.472 | 3.739 | 0.126 | 0.471 | 0.615 | 0.77 |
| 9 | 3.112 | 0.182 | 0.566 | 5.767 | 0.098 | 0.565 | 0.691 | 0.82 |
| 10 | 5.330 | 0.124 | 0.661 | 8.858 | 0.075 | 0.664 | 0.756 | 0.87 |
| 11 | 8.617 | 0.087 | 0.750 | 12.916 | 0.058 | 0.749 | 0.811 | 0.92 |
| 12 | 13.852 | 0.058 | 0.803 | 18.645 | 0.044 | 0.820 | 0.859 | 0.94 |
| 13 | 20.885 | 0.041 | 0.856 | 25.826 | 0.034 | 0.878 | 0.901 | 0.95 |

Two things to read off, and they point in opposite directions.

*The Proposition is confirmed sharply.* The construction's own contribution matches
$\tfrac32n(n-1)(n-2)(n-3)4^{-n}$ with a deficit that shrinks monotonically — ratio
$0.77,0.82,0.87,0.92,0.94,0.95$ — which is exactly the Bonferroni overlap term
$O(n^22^{-n})$ going away. And the construction's contribution to the **repeated-eigenvalue** event
and to the **pair-sums-to-zero** event agree at every size (0.472/0.471, 0.566/0.565, 0.661/0.664,
0.750/0.749, 0.803/0.820, 0.856/0.878), as the identity
$\mathbb{P}(\mu+\nu=0)=\mathbb{P}(\mu=\nu)=3/8$ demands. Two independent counts agreeing to a
percent across six sizes is a strong check on the exact per-template probability $3\cdot4^{-n}$.

*The dominance claim is not supported at these sizes.* The construction's share of the total falls
($0.249\to0.041$ for the repeated-eigenvalue event) and the total in units of $n^44^{-n}$ rises
($1.90\to20.9$). In raw terms $\mathbb{P}(\text{repeated eigenvalue})$ is
$0.1185,\,0.0779,\,0.0508,\,0.0301,\,0.01712,\,0.008888$, a per-step ratio of
$0.657,\,0.652,\,0.593,\,0.569,\,0.519$ — falling monotonically, but still far above the value
$0.25$ that base $4$ requires. So at $n\le13$ the event is dominated by mechanisms other than the
construction, and this census cannot tell whether those are a large pre-asymptotic term or a
genuinely cheaper structure. I therefore **withdraw any claim that the leading constant is $3/2$**;
what is measured is that the construction contributes what the Proposition says it contributes, and
nothing more.

**Why no census at reachable sizes can settle it.** Go one level down, to the *singularity*
probability, whose analogous prediction is $\mathbb{P}(\text{singular})\sim cn^22^{-n}$ from a single
support-two kernel vector (two equal or opposite columns). Measured over $4\cdot10^5$ to
$2\cdot10^6$ draws per size, rank decided exactly over two large primes (`kernel_struct.py`):

| $n$ | $\mathbb{P}(\text{singular})$ | $\div\,n^22^{-n}$ | share with a support-2 kernel vector | $\mathbb{P}(\mathrm{corank}\ge2)$ | $\div\,n^44^{-n}$ | share with two disjoint support-2 |
|---|---|---|---|---|---|---|
| 8 | 0.3276 | 1.31 | 0.567 | 0.0596 | 0.95 | 0.327 |
| 9 | 0.2723 | 1.72 | 0.460 | 0.0395 | 1.58 | 0.236 |
| 10 | 0.2150 | 2.20 | 0.379 | 0.0268 | 2.81 | 0.154 |
| 11 | 0.1645 | 2.78 | 0.312 | 0.0160 | 4.57 | 0.106 |
| 12 | 0.1200 | 3.41 | 0.261 | 0.00939 | 7.60 | 0.067 |
| 13 | 0.0850 | 4.12 | 0.221 | 0.00501 | 11.77 | 0.049 |

The normalised singularity probability is still *rising* monotonically at $n=13$ and its own
conjectured primitive explains only a fifth of the event. So the prefactor of the simpler,
one-coincidence quantity has not begun to settle; the prefactor of a two-coincidence event certainly
has not.

Why, quantitatively. Among corank-one matrices the exact primitive integer kernel vector was
computed with sympy (`support_hist.py`) and its support recorded:

| $n$ | support 2 | 4 | 6 | 8 | 10 | 12 | 14 | share with all coefficients in $\{0,\pm1\}$ |
|---|---|---|---|---|---|---|---|---|
| 8 | 0.503 | 0.309 | 0.117 | 0.008 | — | — | — | 0.915 |
| 10 | 0.339 | 0.258 | 0.183 | 0.074 | 0.010 | — | — | 0.782 |
| 12 | 0.242 | 0.185 | 0.162 | 0.118 | 0.071 | 0.016 | — | 0.637 |
| 14 | 0.187 | 0.121 | 0.120 | 0.107 | 0.096 | 0.079 | 0.026 | 0.510 |

Support two is *losing* share throughout the computable range, and by $n=14$ half of all kernel
vectors are not $\pm1$ vectors at all. A first-moment count explains this: a $\pm1$ kernel vector of
support $2s$ requires every one of the $n$ rows to have its $2s$ relevant entries sum to zero, which
costs $p_s=\binom{2s}{s}4^{-s}$ per row ($\tfrac12,\tfrac38,\tfrac5{16},0.273,\dots$), so the
expected number is $\approx\binom{n}{2s}2^{2s-1}p_s^{\,n}$. Support two has the largest base and
must win eventually, but it has by far the smallest count, and the two only cross over late. That
model reproduces the measured shares at $n=8$ and $n=10$ to within about 20% (model
$0.418/0.419/0.156/0.008$ against measured $0.503/0.309/0.117/0.008$ at $n=8$; $0.346/0.364/0.235$
against $0.339/0.258/0.183$ at $n=10$), and it says support two reaches a $90\%$ share only near
$n=30$ and $99\%$ near $n=40$. At $n=14$ it also over-predicts, because it counts only $\pm1$
vectors and half the kernel vectors there are not.

So the asymptotic regime for these conjectures begins somewhere around $n\approx30$–$40$, and the
largest exhaustive census is $n=7$ ($2^{22}$ matrices after the sign-conjugation quotient) with
Monte Carlo good to $n\approx14$. Read on its own, this data suggests that
base $4$ is wrong; that reading would be mistaken.

Independent corroboration at the other end, where the exhaustive census is exact: at $n=5$ the
corank-$\ge2$ templates predict $\sum\mathbb{P}\cdot4^n=n(n-1)(n-2)(n-3)=120$ and the exhaustive
count of corank $\ge2$ is $116$. At $n=5$ the construction explains essentially the whole event —
which is another way of saying that the size dependence here is not monotone and small-$n$
agreement proves nothing about the limit.

## Trying to break this

* **The obvious objection: is there a cheaper mechanism?** A support-$2k$ eigenvector with $\pm1$
  coefficients costs $\binom{2k}{k}2^{-2k}$ per outside row, which is $1/2$ at $k=1$ and $3/8$ at
  $k=2$ and decreasing — so support two is the cheapest primitive and larger supports are
  exponentially worse. A single primitive gives singularity ($\Theta(n^22^{-n})$), not a repeated
  eigenvalue or a $\pm$ pair; those need two, hence $4^{-n}$. A global structure (say $M$ commuting
  with an involution) costs $2^{-\Theta(n^2)}$. Three equal rows is two primitives on an overlapping
  triple and loses a factor $n$. I could not find a cheaper route, and the base-$4$ half of Vu's
  Conjecture 8.4 asserts there is none.
* **Could a repeated nonzero eigenvalue arise without any support-two eigenvector?** Certainly —
  that is most of the measured probability at $n=8$ (the construction's share is only $0.25$ there).
  The claim is only that those other mechanisms are lower order in $n$, and the small sizes are
  where they are largest. *The check that would settle it*: run the census to $n=14$ and watch
  whether the construction's share rises towards $1$ and whether
  $\mathbb{P}\cdot4^n/n^4$ flattens. `mc_census.out` records $n=8..14$: the construction's share of
  the repeated-eigenvalue event falls from $0.249$ to $0.029$ and $\mathbb{P}\cdot4^n/n^4$ is still
  rising at $n=14$. So the statement that $c$ is the same for both conjectures and the prefactor is
  $n^4$ is a conjecture that the computable sizes do not test, not a measured law.
* **Is the Bonferroni step sound?** At $n=5$ the template sum (120) exceeds the measured union
  (116), which is the correct direction and shows the overlap term is real at small $n$. The
  asymptotic claim is that it is $O(n^22^{-n})$ relative; that is a calculation, not a measurement.
* **Prior art.** Vu's survey gives the three-equal-rows bound and no prefactor; Han's paper gives
  the bulk result and no construction. Campos, Jenssen, Michelen and Sahasrabudhe (arXiv:2203.06141)
  prove $\mathbb{P}(\text{repeated eigenvalue})=e^{-\Omega(n)}$, which is consistent with and much
  weaker than base $4$. No paper found states the $n^4$ prefactor or the disjoint-pair construction
  for either conjecture (searches recorded in `LITERATURE_P2.md`). The construction itself is
  elementary enough that it may well be folklore; I would not claim priority on it, only that it is
  not in the survey and that it corrects the earlier ledger record.

## Status

* $\mathbb{P}(\text{pair sums to }0)\ge(\tfrac32-o(1))n^44^{-n}$ and the three companion bounds:
  **proved** (exact per-template probability machine-verified exhaustively at $n=4,5,6$; Bonferroni
  step is a routine estimate).
* The ledger's claims that the F0009 event is "super-exponentially small" and that repeated nonzero
  eigenvalues are "far below any exponential": **refuted**.
* The $n^4$ prefactor in Conjecture 8.4, superseding the survey's $n^3$-worth of triples:
  **proved as a lower bound**. Whether it is sharp is open and this census cannot say.
* $s_n$ and $\mathbb{P}(\text{pair}=0)$ have the same leading constant: **speculation, withdrawn as
  a claim.** What is measured is that the *construction's* contribution to the two events coincides
  at $n=8,\dots,13$, which is a check on the exact per-template probability, not on dominance.
  (Two cautions on that check: the two columns are counted on the same sampled matrices by the same
  detector, so their agreement is one instrument read twice. The per-template constant $3\cdot4^{-n}$
  is however corroborated by a genuinely different method — exhaustive enumeration of all
  $2^{n(n+1)/2}$ matrices with no eigenvalue computation at all, `template_all.py`, which returns
  exactly $3$ for all eight sign-and-relation combinations at $n=4,5,6$.)

## Remaining obligation

The matching upper bound. To prove $s_n=O(n^44^{-n})$ one needs: (i) that corank $\ge2$ without two
disjoint two-row coincidences is $o(4^{-n})$ — the corank-two analogue of Vu's Conjecture 3.3, which
is the symmetric Kahn–Komlós–Szemerédi problem and is open; and (ii) an anti-concentration statement
for a repeated *nonzero* eigenvalue at scale exactly zero, for which the gap method of
Nguyen–Tao–Vu gives nothing (it resolves $M-\lambda I$ at every scale $e^{-n^c}$ but cannot
distinguish an exact coincidence from a tiny gap). Han's decoupled estimates are the right tool for
(ii) but currently only on the bulk; extending them to $|\lambda|=O(1)$ is the concrete next step.

## Files

`f0009_construct.py` (explicit matrices, exact eigenvalues), `template_prob.py` and
`template_all.py` (exhaustive exact per-template probabilities), `census.py`, `census7.py`
(exhaustive census $n\le7$), `mc_census.py` (Monte-Carlo census with structure attribution).
