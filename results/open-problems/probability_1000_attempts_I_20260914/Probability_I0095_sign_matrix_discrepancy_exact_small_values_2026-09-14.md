# The largest discrepancy of a sign matrix, exactly, for small sizes

**Problem.** Randomstrasse 2024 problem list, Open Problem 11: what is the value of
$$\sup_{n} \ \sup_{A \in \{\pm1\}^{n\times n}} \frac{1}{\sqrt n}\operatorname{disc}(A),
\qquad \operatorname{disc}(A) = \min_{x \in \{\pm1\}^n}\|Ax\|_\infty\ ?$$
The list records $\sqrt2$, from the two-by-two Hadamard matrix, as the lower bound it knows, and asks
whether "just a couple of deviations suffice all along". By Spencer's theorem the supremum is finite;
the constant there has come down from $5.4$ to $4.1$ (Pesenti and Vladu, 2022).

**What is here.** The exact value of $\max_A \operatorname{disc}(A)$ for every $n \le 11$, an
identification of the quantity as a covering-code problem, and hence the lower bound
$$\sup_n \sup_A \frac{\operatorname{disc}(A)}{\sqrt n} \ \ge\ \frac{5}{3} = 1.6667,$$
attained at $n = 9$ by an explicit matrix. This is above the $\sqrt2 = 1.4142$ the list records.

## The table

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\max_A\operatorname{disc}(A)$ | 2 | 1 | 2 | 3 | 4 | 3 | 4 | 5 | 4 | 5 |
| ratio | 1.414 | 0.577 | 1.000 | 1.342 | **1.633** | 1.134 | 1.414 | **1.667** | 1.265 | 1.508 |

The extremal matrix at $n=9$, with rows written as signs:
```
---++++++   -+---++++   +---++-++   +++++--++   +-+----++
++--+++-+   +--+-++-+   -+-+-+--+   --+-+---+
```
Every one of the $512$ sign vectors $x$ has some row with $|r\cdot x| \ge 5$, so
$\operatorname{disc} = 5$ and the ratio is $5/3$.

At $n=6$ the extremal matrix is
```
--++++   +--+++   +++-++   +-++-+   -+-+-+   -----+
```
with $\operatorname{disc} = 4$ and ratio $4/\sqrt6 = 1.633$.

## Why this is a covering-code question

Since $r\cdot x = n - 2\,d(r,x)$ in terms of Hamming distance,
$$|r\cdot x| \ge v \iff d(r,x) \le \tfrac{n-v}2 \ \text{ or }\ d(\bar r, x) \le \tfrac{n-v}2 .$$
So $\operatorname{disc}(A) \ge v$ says exactly that the $n$ rows of $A$ *together with their
complements* cover the whole cube within radius $(n-v)/2$. Hence
$$\max_{A \in \{\pm1\}^{n\times n}} \operatorname{disc}(A)
= n - 2\min\{\,R : \text{some complement-closed binary code of length } n \text{ and size } 2n
\text{ has covering radius } R\,\},$$
and the quantity is read off the tables of $K(n,R)$, the least size of a binary covering code of length
$n$ with radius $R$: if $K(n,R) \le n$ the radius is achievable, and if $K(n,R) > 2n$ it is not.

This explains the ragged look of the table, which is the raggedness of $K(n,R)$. It does not, however,
settle $n = 12$: discrepancy $6$ there would need a complement-closed covering code of length $12$, size
$24$ and radius $3$, and the published bounds are $18 \le K(12,3) \le 28$, which straddle $24$. So
$n=12$ is left open here, by the tables as much as by the integer programme, which was given a further
fifty minutes on that single case and returned a time limit rather than a verdict. The same straddling leaves
$n = 15$, $18$, $20$, $21$ and beyond undecided, and those are where the interesting room is: at $n=21$,
for instance, a radius-$6$ covering code of size $42$ would give discrepancy $9$ and a ratio of $1.96$. It also gives the route to extending the table: every published
$K(n,R)$ value with $K(n,R)\le n$ produces a lower bound on the supremum, namely
$(n-2R)/\sqrt n$.

## What the covering tables give up to $n = 24$

The identification turns the published bounds on $K(n,R)$ into bounds on the maximum discrepancy:
$K_{\mathrm{upper}}(n,R) \le n$ makes radius $R$ achievable with the $2n$ codewords of a
complement-closed code, so $\max_A\operatorname{disc} \ge n-2R$; and $K_{\mathrm{lower}}(n,R) > 2n$ makes
radius $R$ impossible, so $\max_A\operatorname{disc} < n-2R$. Reading Kéri's tables, which descend from
Cohen, Honkala, Litsyn and Lobstein, that gives

| $n$ | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| at least | 4 | 3 | 4 | 3 | 4 | 5 | 4 | 5 | -- | -- | -- | -- | -- |
| at most | 6 | 5 | 6 | 7 | 6 | 7 | 8 | 7 | 8 | 9 | 8 | 9 | 10 |

where a dash means the tables certify nothing at that size. The brackets contain the exact value at every
$n \le 11$ computed above, which is the control on the reading.

Two things follow. The tables do not certify any ratio above $5/3$: the largest certified value in the
upper row is $5$ at $n = 17$ and $n = 19$, giving $1.21$ and $1.15$. And the room is all in the lower row,
where $n = 21$ and $n = 24$ would give $1.96$ and $2.04$ if their upper bounds were attained. Closing any
one of those is a matter of exhibiting a complement-closed covering code of size $2n$, that is, an
explicit matrix; an annealing search over the covering formulation at $n = 15$, $17$ and $18$ found none
in the budget it was given, which is unsurprising given that the corresponding $K$ values have resisted
since the 1990s.

## How the values were checked

Not by trusting a solver. Each entry has two halves and each half was verified on its own terms.

*Achievable.* The witness matrix is written out and its discrepancy recomputed by brute force over all
$2^{n-1}$ sign vectors. That is the table's top row.

*Not more.* For every $n \le 11$ except one, the next level up is ruled out by counting alone: a single
row covers $\sum_{j \le (n-v)/2}\binom nj$ sign vectors up to global sign, and $n$ times that falls short
of $2^{n-1}$. The exception is $n=10$ at level $6$, which the counting bound permits. That one case is
settled twice over: the integer programme returns a proved infeasibility rather than a time limit, and
independently $K(10,2) = 30 > 20$ in the covering-code tables forbids it. The two agree.

The integer programme that produced the witnesses was also made to distinguish a proved infeasibility
from a time limit, after an early version treated a solver timeout as a proof of impossibility. With
that fixed it declines to answer at $n = 12$ and above, which is the honest outcome, and the
covering-code tables answer instead.

## Where this sits

The list's Open Problem 11 restricts to matrices with entries $\pm1$. The nearby literature is about the
Komlós constant, the same supremum over real matrices whose columns have Euclidean norm at most one, for
which Kunisky (2021) proved a lower bound of $1+\sqrt2 \approx 2.414$. That construction uses matrices
with zero entries, so it does not bear on the $\pm1$ question, and neither does the unpublished numerical
example at $n = 15$ attributed to Spielman that Kunisky reports at $2.005$, which is in the same
column-normalised setting. The list itself mentions a numerical construction of Spielman's beating
$\sqrt2$ without saying which setting it is in, so the $5/3$ here is offered as a certified lower bound
for the $\pm1$ version rather than as a claim of priority. What I could not find anywhere is a table of
the exact maximum for small $n$, which is what this note supplies.

## Status

Partial, and the part that is done is exact: the maximum discrepancy of an $n\times n$ sign matrix is
computed for every $n \le 11$ and verified twice over, and the supremum asked for in Open Problem 11 is
at least $5/3$. Verification: author checked; every achievability by brute force over all sign vectors,
every impossibility by the counting bound alone except at $n=10$, where the programme's proved
infeasibility and the published covering-code minimum agree. Prior art: Spencer's theorem bounds the supremum by $4.1$; the
covering-code identification is elementary and may well be folklore, though I did not find it stated.
Not a clearance.

## New open problems

1. **Is the supremum approached or attained?** Through the identification it asks for the behaviour of
   $n - 2\rho(n, 2n)$, where $\rho(n,M)$ is the least covering radius of a complement-closed binary code
   of length $n$ with $M$ codewords. Does $(n - 2\rho(n,2n))/\sqrt n$ converge, and to what?
2. **How ragged is the table?** The values $4, 3, 4, 5, 4, 5$ at $n = 6,\dots,11$ do not increase.
   Is $\max_A\operatorname{disc}$ for $n+1$ at least that for $n$ minus one, and is the sequence
   eventually non-decreasing?
3. **The complement-closed cost.** A covering code and its complements have at most twice the size, so
   the complement-closed minimum lies between $K(n,R)$ and $2K(n,R)$. For which $n$ and $R$ is an optimal
   covering code complement-closed? At $n=6$, $R=1$ the optimal code has exactly $12 = 2n$ codewords and
   the extremal matrix above shows it can be taken complement-closed.
4. **Structure of the extremal matrices.** At $n=2$ the extremum is a Hadamard matrix, and at $n=4$ and
   $n=8$ the Hadamard matrix is not extremal. Is there a construction behind the good cases $n=6$ and
   $n=9$, and does it continue?
