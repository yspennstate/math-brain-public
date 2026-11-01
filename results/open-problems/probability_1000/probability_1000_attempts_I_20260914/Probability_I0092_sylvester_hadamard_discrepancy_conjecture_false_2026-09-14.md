# The discrepancy of the Sylvester Hadamard matrices

**Problem.** Randomstrasse 2024 problem list, Conjecture 13: let $H_k$ be the $2^k \times 2^k$ Sylvester
Hadamard matrix and $\operatorname{disc}(A) = \min_{x \in \{\pm1\}^n} \|Ax\|_\infty$. For odd $k$,
$$\operatorname{disc}(H_k) = \sqrt2\,\sqrt{2^k}.$$
The list proves $\operatorname{disc}(H_k) = \sqrt{2^k}$ for even $k$, gives $\sqrt2 \sqrt{2^k}$ as an
upper bound for odd $k$ by an explicit tensor construction, and notes that the conjecture would settle
its Conjecture 12.

**Answer.** False. The conjecture holds exactly for $k \in \{1,3,5,7\}$ and fails for every odd
$k \ge 9$. At $k=9$ the true value is at most $28$ against the conjectured $32$.

The list's own Remark 6.1 says that $H_k$ "essentially corresponds to the boolean Fourier transform" and
points the reader at Boolean analysis without following the thread. Followed, it closes the question
immediately, because the quantity conjectured about is one that the Boolean-functions literature has
been computing since the 1970s under another name.

## The translation

Write $n = 2^k$ and index rows and columns of $H_k$ by $a, u \in \mathbb{F}_2^k$, so that
$(H_k)_{a,u} = (-1)^{a\cdot u}$. A sign vector $x \in \{\pm1\}^n$ is the $\pm1$ truth table of a Boolean
function $f$ on $k$ variables, $x_u = (-1)^{f(u)}$, and
$$(H_k x)_a = \sum_u (-1)^{f(u) + a\cdot u} = W_f(a),$$
the Walsh--Hadamard transform of $f$. The nonlinearity of $f$, its Hamming distance to the nearest affine
function, is $\operatorname{NL}(f) = 2^{k-1} - \tfrac12 \max_a |W_f(a)|$. Hence
$$\operatorname{disc}(H_k) = \min_f \max_a |W_f(a)| = 2^k - 2\max_f \operatorname{NL}(f),$$
and $\max_f \operatorname{NL}(f)$ is the covering radius of the first-order Reed--Muller code
$\mathrm{RM}(1,k)$.

Under this dictionary the conjecture reads
$$\max_f \operatorname{NL}(f) = 2^{k-1} - 2^{(k-1)/2} \qquad (k \text{ odd}),$$
which is the *bent concatenation bound*: for even $k$ bent functions have a perfectly flat spectrum
$|W_f| \equiv 2^{k/2}$, and gluing a bent function on $k-1$ variables gives the odd-$k$ value above. The
list's tensor construction $x^{\natural}_{(k)} = y \otimes x^{\natural}_{(k-2)}$ is exactly that gluing.

Whether the bent concatenation bound is optimal for odd $k$ is one of the older questions in the subject,
and the answer has been known since 1983 for large $k$ and since 2006 in full.

## What is known, and why the conjecture fails

- **Patterson and Wiedemann (1983)** produced a function on $15$ variables of nonlinearity $16276$,
  against the bound $2^{14} - 2^{7} = 16256$. In the discrepancy language,
  $\operatorname{disc}(H_{15}) \le 2^{15} - 2\cdot 16276 = 216 < 256 = \sqrt2\sqrt{2^{15}}$. Their
  function lives on $\mathrm{GF}(2^{15})$ and is invariant under multiplication by $\mathrm{GF}(2^5)^*$
  and under the Frobenius map, a group of order $465$. This counterexample predates the conjecture by
  forty-one years.
- **Kavut, Maitra and Yücel (2006)** settled the remaining small odd cases, and their title is the whole
  answer: there exist Boolean functions on $n$ odd variables with nonlinearity exceeding
  $2^{n-1}-2^{(n-1)/2}$ *if and only if* $n > 7$. They found nonlinearity $241$ on nine variables inside
  the rotation-symmetric class; **Kavut and Yücel (2007, 2010)** raised it to $242$ in a generalised
  rotation and dihedral class.
- For odd $k \le 7$ the bound is attained and is optimal, so the conjecture is true there.

So $\operatorname{disc}(H_9) \le 2^9 - 2 \cdot 242 = 28 < 32$, and the conjecture fails at every odd
$k \ge 9$.

## Verification, computed here rather than cited

The nonlinearity $242$ functions are published as hexadecimal truth tables. Reading the three of them and
computing the Walsh spectrum directly gives $\max_a|W_f(a)| = 28$ in each case, that is, nonlinearity
$242$, against the conjectured minimum of $32$. The reading convention cannot affect this: permuting the
input coordinates permutes the spectrum and complementing $f$ negates it, so the nonlinearity of a hex
string is the same however its bits are assigned to $\mathbb{F}_2^9$.

The small cases were also computed exhaustively, over all $2^n$ sign vectors:

| $k$ | $n$ | $\operatorname{disc}(H_k)$ | predicted |
| --- | --- | --- | --- |
| 1 | 2 | 2 | $\sqrt2\sqrt2 = 2$ |
| 2 | 4 | 2 | $\sqrt4 = 2$ |
| 3 | 8 | 4 | $\sqrt2\sqrt8 = 4$ |
| 4 | 16 | 4 | $\sqrt{16} = 4$ |

so the conjecture is confirmed where it is true and the even-$k$ theorem is confirmed as well.

The half of the answer that rests on the literature, that the bound is optimal for odd $k \le 7$, was
corroborated here as far as a search can: steepest descent over sign vectors reaches exactly
$\max|W| = 4$ at $k=3$ and $8$ at $k=5$, the conjectured values, and never less. At $k=7$ the same search
only reaches $20$ against the true $16$, so it corroborates nothing there; that case rests on
Mykkeltveit, as $k=5$ rests on Berlekamp and Welch.

A search of my own over the rotation-symmetric class on nine variables reached
$\max|W| = 32$ repeatedly and no lower, which is consistent with the published account: functions at $30$
and $28$ are rare and were found with a specialised heuristic over many runs, and an exhaustive
enumeration has since shown that no plain rotation-symmetric function does better than $241$.

## What this does to the neighbouring problems

Conjecture 12 of the same list asks whether
$\limsup_n \sup_{A \in \{\pm1\}^{n\times n}} \operatorname{disc}(A)/\sqrt n > 1$, and Conjecture 13 was
offered as the route to it. That route is now closed, but the conclusion is not: for odd $k$ no bent
function exists, so Parseval's identity is strict and
$\operatorname{disc}(H_k) > \sqrt{2^k}$ for every odd $k$, while for even $k$ the ratio is exactly $1$.
What the Sylvester family gives is therefore a sequence of ratios strictly above one whose limit is not
known to exceed one: the measured values are $28/2^{4.5} = 1.237$ at $k=9$ and at most
$216/2^{7.5} = 1.193$ at $k=15$, both well below the conjectured $\sqrt2$, and Hou's upper bound on
nonlinearity gives only $1 + o(1)$ from below asymptotically. So Conjecture 12 remains open and now has
no proposed route through $H_k$.

For Open Problem 11 of the same list, which asks for
$\sup_n \sup_A \operatorname{disc}(A)/\sqrt n$, the lower bound $\sqrt2$ from $H_1$ stands, and this note
says only that the rest of the Sylvester family does not improve it.

## Status

Answered, and the answer is a literature connection the source's own remark points at: Conjecture 13 is
true exactly for odd $k \le 7$ and false for every odd $k \ge 9$. Verification: author checked; the
refuting functions were verified here by computing their Walsh spectra from the published truth tables,
and the small cases exhaustively. Prior art: the whole content is Patterson and Wiedemann 1983 and Kavut,
Maitra and Yücel 2006 and 2007, restated through the dictionary above. Not a clearance: what is new is
only the observation that the conjecture is a known solved question in different words.

## New open problems

1. **The exact discrepancy of $H_9$.** The covering radius of $\mathrm{RM}(1,9)$ is known only to lie
   between $242$ and $244$, so $\operatorname{disc}(H_9) \in \{24, 26, 28\}$ and the true value is open.
   This is the smallest case of the conjecture that fails and the smallest case where the discrepancy of
   a Sylvester matrix is unknown.
2. **Does the odd-$k$ ratio stay away from one?** Is
   $\liminf_{k \text{ odd}} \operatorname{disc}(H_k)/\sqrt{2^k} > 1$? This is what the Sylvester family
   would need to supply to settle Conjecture 12, and it is exactly the question whether the maximum
   nonlinearity on $k$ odd variables is $2^{k-1} - c\,2^{k/2 - 1}(1+o(1))$ with $c$ bounded away from
   zero. The known constructions give $c \approx 1.19$ at $k=15$ and the known upper bounds allow
   $c \to 0$.
3. **A family with ratio above $\sqrt2$.** Every ratio computed so far, over all $\pm1$ matrices, is at
   most $\sqrt2$, attained at $H_1$. Is $\sqrt2$ the supremum in Open Problem 11, and if a matrix beats
   it, does its discrepancy also come from a spectrum that is far from flat in the same sense?
4. **Discrepancy of other Hadamard families.** The Sylvester construction is one of many. For a Paley
   Hadamard matrix of order $n$, is $\operatorname{disc}$ closer to $\sqrt n$ than the Sylvester value,
   and is there a family whose discrepancy ratio tends to a limit greater than one?
