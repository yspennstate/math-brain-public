# Addendum: the new B18 sink frontier earns a real code-or-factorial payment

**Status:** PROVED partial lemma; full FEI remains **OPEN / NOT PROVED**.

After the main companion-flow report was committed, scientific master advanced with account04/B18's theorem `B18-SINK-SURVIVOR-01` / `B18-SINK-BUDGET-02` (commit `3750392e7c29d2c5acb912b0cc71d3507932b543`). I consumed that result rather than leaving the new companion channel disconnected from the newest proof integration.

B18 considers the doubly robust Palm/physical near-subcube sector, contracts reciprocal trigger components, takes the sink components of the resulting factor-7 DAG, chooses one representative `r_C` from each sink, and sets

\[
R=\{r_C\},\qquad A=\bigcup_{r\in R}F_r.
\]

It proves in particular

\[
R\cap A=\varnothing,\qquad F_r\subseteq A\quad(r\in R).
\tag{A.1}
\]

The B12 companion theorem from the main report gives, for every `epsilon<=1/16` Palm-robust row with nonempty trigger set,

\[
\Pr(C\in F_i\mid L=i)
=\frac{1}{p_i}\sum_{k\in F_i}r_{ik}
\ge\frac3{16}.
\tag{A.2}
\]

Combining (A.1) and (A.2) produces an actual nonreuse payment for the canonical B18 sink frontier.

## Theorem — sink-frontier code-or-factorial payment

Let

\[
J_R:=\sum_{r\in R}p_r.
\]

For the exact Palm sequential code,

\[
\boxed{
D_{\rm seq}+\mathbb E\log_2(K!)\ge \frac1{32}J_R.
}
\tag{A.3}
\]

### Proof

Let

\[
Y=1_{\{C\in A\}},
\qquad
\beta:=\Pr(Y=1).
\]

From the exact companion marginal,

\[
I\beta
=\sum_{j\in A}(p_j-u_j)
\le I-V
\le\mathbb E\log_2(K!).
\tag{A.4}
\]

There are two cases.

### Case 1: `beta >= 1/32`

Then (A.4) gives

\[
\mathbb E\log_2(K!)
\ge I\beta
\ge I/32
\ge J_R/32,
\]

because `J_R<=I`. Hence (A.3).

### Case 2: `beta < 1/32`

For every sink representative `r`, (A.1)-(A.2) give

\[
\alpha_r:=\Pr(Y=1\mid L=r)
\ge\Pr(C\in F_r\mid L=r)
\ge3/16.
\]

Therefore

\[
\alpha_r-\beta>\frac3{16}-\frac1{32}=\frac5{32}.
\]

Data processing from the full companion symbol `C` to the bit `Y`, followed by binary Pinsker in base two, yields

\[
\begin{aligned}
D_{\rm seq}
&\ge D_{\rm comp}
 =I I_2(L;C)
 \ge I I_2(L;Y)\\
&=\sum_i p_i\,d_2(\Pr(Y=1\mid L=i)\|\beta)\\
&\ge\sum_{r\in R}p_r\,d_2(\alpha_r\|\beta)\\
&\ge \frac{2}{\ln2}\left(\frac5{32}\right)^2J_R
>\frac1{32}J_R.
\end{aligned}
\tag{A.5}
\]

Thus (A.3) also holds in Case 2. QED.

## Why this is useful

This is the first direct component-level payment I know in the current B12 compression route that uses the **canonical noncolliding survivor block** produced by B18 rather than a hand-chosen pair or singleton witness.

The dichotomy is exact:

- if the common reveal block `A` is common enough under the companion marginal, its mass is already inside the first-moment quantity `I-V`, hence inside the factorial rebate;
- if `A` is rare under the companion marginal, then seeing that the actual companion lands in `A` predicts a sink representative by a fixed KL amount.

No sum of redundant pairwise KL terms appears. The same actual companion symbol is used once.

The lemma still does **not** close FEI. It pays only the influence mass of the chosen sink representatives, not the full entropy/address cost of all rows in their components or all successive sink layers. One cannot simply repeat (A.3) over every peeling layer and add the resulting lower bounds, because the same global `D_seq` and factorial rebate could then be reused. The next missing theorem is a genuinely chained block statistic (or a disjoint allocation of the companion/factorial resources) across the B18 sink-peeling hierarchy.
