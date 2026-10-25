# Literature record, random matrix theory, 13 September 2026

Every arXiv id below was checked against its abstract. Negative searches are listed separately; they
describe the search, not the literature.

## Confirmed sources

**arXiv:2005.02797** — Van H. Vu, *Recent progress in combinatorial random matrix theory*. Abstract
opens "We discuss recent progress many problems in random matrix theory of a combinatorial nature,
including several breakthroughs that solve long standing famous conjectures." All 21 pages read.
Statements transcribed from the PDF:

- Conjecture 2.2: $p_n=(2+o(1))n^22^{-n}$ (non-symmetric singularity).
- Preceding Conjecture 8.4: "We observe that $s_n\ge4^{-n}$, which is the probability that the first
  3 rows are the same (which guarantees that zero is an eigenvalue with multiplicity at least 2)."
  Conjecture 8.4 (Simplicity): $s_n=(4+o(1))^{-n}$. Current best upper bound $s_n\le e^{-n^c}$
  (Nguyen–Tao–Vu).
- Conjecture 8.5: "With probability $1-o(1)$, the singular values of $M_n^{\mathrm{sym}}$ are
  different." Followed by the remark that this asserts no two eigenvalues add up to zero. **No
  lower-bound construction is given for 8.5.**
- Conjecture 9.4: integral spectrum probability $2^{-(.5+o(1))n^2}$. Conjecture 9.5: Gaussian
  integral spectrum $2^{-(1+o(1))n^2}$. Conjecture 11.2 (Finger Print). Conjecture 11.3 ($\Theta(\sqrt
  n)$ real eigenvalues). Problem 11.4 (at least 2 real eigenvalues).

**Relevant finding:** no polynomial prefactor appears anywhere near 8.4, 8.5, 9.4, 9.5, 11.2–11.4.
Vu does give prefactors when he has them (Conjecture 2.2 carries $n^2$), so the absence is not a
convention of the survey.

**arXiv:2603.29571** — Bandeira, Dmitriev, Lucca, Nizić-Nikolac, Rödder, *Randomstrasse101: Open
Problems of 2025*. Entry 10, "Injectivity and Stability of Phase Retrieval" (author ASB). Definition
10.1 verbatim: "Given $A\in\mathbb R^{N\times M}$ let $\omega(A)$ be defined as
$\omega(A)=\min_{S\subseteq[N]:\mathrm{rank}(A_{S^c})<M}\sigma_M(A_S)$, where $A_S$ denotes the
submatrix made of the rows indexed by $S$." Conjecture 20 is Balan–Wang: there exist universal
$C>0$, $0<\beta<1$ with $\omega(A)\le C\max_k\|A_k\|\beta^M$ for any $A\in\mathbb{R}^{(2M-1)\times
M}$ whose every $M$ rows span. Open Problem 21: "What is the value of $\omega(A)$ for $A$ with iid
standard gaussian entries? Does it satisfy the bound in the conjecture? If so, what is $\beta$?"
This confirms the campaign ledger's paraphrase of P0016 exactly, including that the minimum runs
over *row* subsets.

**arXiv:2607.06249** — **Yitzchak Shmalo**, *Extreme least singular values of Gaussian row
submatrices and a phase retrieval stability problem*, 7 July 2026. Abstract, verbatim from the PDF:
"Let $\mathbb F$ be either $\mathbb R$ or $\mathbb C$ … We determine the exponential scale of the
smallest least singular value among all square row submatrices … With $c_\gamma=\gamma^\gamma/
(\gamma-1)^{\gamma-1}$ we prove $\frac1m\log M_m^{\mathbb F}\xrightarrow{P}-d_{\mathbb F}^{-1}\log
c_\gamma$ … As an application, for real phase retrieval at the critical number $N=2m-1$ of
measurements the Balan–Wang stability parameter satisfies $\omega(A_m)=4^{-m+o_P(m)}$, so the sharp
exponential base in the Gaussian Balan–Wang problem is $1/4$." Theorem 1.1 and Corollary 1.2 as
quoted in the P0016 memo. Method: second moment (Paley–Zygmund) over the hyperplanes spanned by
$m-1$ of the remaining rows, against the left-out row; Lemma 4.1 is the conditionally-independent
Haar-lines pair law. **This settles Randomstrasse Open Problem 21 and therefore campaign entry
P0016, which the ledger still carries as `attempted_unsolved`.**

**arXiv:1308.4718** — Balan and Wang, *Invertibility and robustness of phaseless reconstruction*
(the source of Conjecture 20). **arXiv:1302.4618** — Bandeira, Cahill, Mixon, Nelson, *Saving phase:
injectivity and stability for phase retrieval*; its abstract states no exponential-in-$M$ rate for
the stability constant at minimal redundancy.

**arXiv:2504.15992** — Yi Han, *Repeated singular values of a random symmetric matrix and decoupled
singular value estimates*, April 2025. Names Vu's Conjecture 8.5 as its motivation and restates it
as "there does not exist any pair of two eigenvalues of $M_n^{\mathrm{sym}}$ whose sum is zero".
Proves: all singular values of $A_n$ in $[\kappa n^{1/2},(2-\kappa)n^{1/2}]$ are distinct with
probability $1-e^{-cn}$, for any $\kappa>0$. Says plainly: "Despite all the recent progress, no
positive answer seems to have been reached for Conjecture 1.1." **Conjecture 8.5 is open in full;
the bulk is done.**

**arXiv:2203.06141** — Campos, Jenssen, Michelen, Sahasrabudhe, *The least singular value of a random
symmetric matrix*. Proves $\mathbb{P}(\sigma_{\min}\le\varepsilon/\sqrt n)\le C\varepsilon+e^{-cn}$
and, along the way, that the probability of a repeated eigenvalue is $e^{-\Omega(n)}$, confirming a
conjecture of Nguyen, Tao and Vu. This is exponential decay without the base; Vu's base $4$ in
Conjecture 8.4 is untouched by it.

**arXiv:2105.11384** — same four authors, *The singularity probability of a random symmetric matrix
is exponentially small* ($\mathbb{P}(\det A=0)\le e^{-cn}$). Predecessors confirmed:
**arXiv:1809.04718** (Ferber–Jain), **arXiv:1904.11478** (Campos, Mattos, Morris, Morrison),
**arXiv:2011.03013** (Campos, Jenssen, Michelen, Sahasrabudhe).

**arXiv:2502.13819** — Yi Han, *Simplicity of singular value spectrum of random matrices and
two-point quantitative invertibility*. Confirms distinct singular values for general iid subgaussian
(non-symmetric) matrices — a different Vu conjecture, not 8.5.

## Negative searches

* "phase retrieval stability constant random frame exponentially small", "phase retrieval 2M-1
  measurements unstable", "condition number complement property Gaussian frame", "Balan Casazza
  Edidin complement property stability", "Cahill Casazza Daubechies phase retrieval stability",
  "almost injectivity stability phase retrieval minimal measurements", "sigma_A random frame
  exponential decay" — nothing stating a $4^{-M}$ rate before arXiv:2607.06249.
* "smallest Plücker coordinate random subspace", "minimum minor of a random Gaussian matrix",
  "smallest maximal minor" — no paper found treating the minimum Plücker coordinate of a uniformly
  random point on the real Grassmannian as an object of study. (This is the determinant-side
  reformulation of P0016: $\omega\approx\min_S|\det A_S|/\prod_{i<M}\sigma_i$, and by Cauchy–Binet
  $\sum_S(\det A_S)^2=\det(A^TA)$, so the question is the smallest coordinate of the Plücker vector
  of a Haar-random $M$-plane in $\mathbb{R}^{2M-1}$.)
* "random symmetric Bernoulli matrix repeated eigenvalue probability 4^{-n} lower bound two pairs of
  equal rows simplicity conjecture prefactor" — only Vu's own three-equal-rows bound surfaced. No
  paper found with an $n^4$ prefactor for Conjecture 8.4, and none studying "$e_i\pm e_j$ as
  eigenvectors" as a mechanism in random sign matrices beyond the equal-rows case in the survey.
* Restricted invertibility (Bourgain–Tzafriri) and full-spark-frame literature was scanned: it is
  about finding a *well*-conditioned submatrix, the opposite extremum, and does not bear on this.
  arXiv:2508.10452 (Xu, matrix selection) is a best-case bound, not on point.
