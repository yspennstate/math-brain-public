# Collision costs for finite permutation models

All logarithms are natural. All alphabets and random variables below are
finite, and entropy uses the convention $0\log0=0$.

## 1. The finite table

Let $F_r$ be the free group on generators $a_1,\ldots,a_r$.
Choose finite nonempty indexed lists of words $w_s,v_t\in F_r$, a
probability vector $p$ on a finite alphabet $A$, and a map

\[
 f:A^S\longrightarrow B.
\]

Repeated words in these lists are allowed. Write

\[
 W=\{1\}\cup\{w_s:s\in S\}\cup\{v_tw_s:t\in D,s\in S\}.
\]

Let $P\subset F_r$ be the union of the reduced-word prefixes of the
words in $W$, including the empty prefix (1). Thus $P$ is finite
and prefix closed. Multiplication of words always means multiplication
in the free group, including free reduction.

For a partition $\pi$ of $P$, write $[u]_\pi$ for the class of $u$.
Call $\pi$ admissible if, for each positive generator $a_j$ and every
two pairs $u,ua_j\in P$ and $v,va_j\in P$,

\[
 u\sim_\pi v\quad\Longleftrightarrow\quad
 ua_j\sim_\pi va_j.                                      \tag{1}
\]

Both implications are required.

**Lemma 1.** A partition of $P$ is admissible if and only if it is the
collision partition of the points $T_u(o)$, $u\in P$, at some root
$o$ of a finite permutation action of $F_r$. Every admissible partition
has such a realization on exactly $|P/\pi|$ points.

**Proof.** Use right evaluation, so

\[
 T_{uv}=T_v\circ T_u.
\]

If the partition comes from permutations, applying the bijection
$T_{a_j}$ to two equal or unequal points preserves their equality or
inequality. This gives (1).

Conversely let $Q=P/\pi$. For every pair $u,ua_j\in P$, prescribe

\[
 \theta_j([u]_\pi)=[ua_j]_\pi.
\]

The forward implication in (1) makes this prescription well defined;
the reverse implication makes it injective on its domain. Its domain
and range have equal cardinality. Choose any bijection from the unused
elements of $Q$ to the elements outside its range. Together these maps
give a permutation $\theta_j$ of $Q$. Do this independently for every
generator. The free group has no further relations to impose.

Take $o=[1]_\pi$. Following a reduced word in $P$ from its prefixes
shows inductively that $T_u(o)=[u]_\pi$. For a positive last letter
this is the prescribed map. For a negative last letter, say $u=va_j^{-1}$,
the prescription on the pair $u,ua_j=v$ gives
$\theta_j([u])=[v]$, hence $\theta_j^{-1}([v])=[u]$.
Prefix closure justifies every induction step. Distinct classes are
distinct points, so the collision partition is exactly $\pi$. ∎

For every admissible partition, give its classes independent $p$-labels
$(L_q)_{q\in Q}$, and form

\[
 R=L_{[1]_\pi},\qquad
 E=f((L_{[w_s]_\pi})_{s\in S}),\qquad
 N=\left(f((L_{[v_tw_s]_\pi})_{s\in S})\right)_{t\in D}.
\]

Define the collision cost

\[
 C_\pi=H(E)+H(R\mid N).                                 \tag{2}
\]

This is an explicit finite table: enumerate the partitions of $P$, test
(1), and sum over the $|A|^{|Q|}$ class labelings. Prefix classes outside
$W$ have no effect on the cost, but are needed to test realizability.

## 2. A sharper defect bound

Suppose a group $G$, a homomorphism $F_r\to G$, and the equality
pattern of $W$ in $G$ are specified. For independent $p$-labels on
$G$, set

\[
 Y_g=f((X_{g w_s})_{s\in S}),\quad
 C_0=H(Y_e)+H(X_e\mid(Y_{v_t})_{t\in D}),\quad
 \delta=H(p)-C_0.                                       \tag{3}
\]

Here subscripts denote the images of the words in $G$. Let
$\mathcal A$ be the finite set of admissible partitions of $P$.
Call a partition good if its restriction to $W$ equals the specified
group pattern. Every good partition has cost $C_0$. Define

\[
 M_{\rm bad}=\max\{C_\pi:\pi\in\mathcal A,
                                  \ \pi\text{ is not good}\}. \tag{4}
\]

**Theorem 2.** If $\delta>0$, then the set in (4) is nonempty,
$M_{\rm bad}\geq H(p)>C_0$, and every assignment of permutations to
the free generators on a nonempty finite set $V$ has a fraction $\eta$
of roots with incorrect $W$-pattern satisfying

\[
 \boxed{\displaystyle
 \eta\ \geq\ \frac{\delta}{M_{\rm bad}-C_0}.}            \tag{5}
\]

**Proof.** Give $V$ independent $p$-labels $U_z$ and put

\[
 Z_z=f((U_{T_{w_s}(z)})_s),\qquad
 N_z=(Z_{T_{v_t}(z)})_t.
\]

The full $Z$-vector is a deterministic function of the full $U$-vector.
The chain rule, subadditivity and removal of conditioning give

\[
\begin{split}
 |V|H(p)
 &=H(Z_V)+H(U_V\mid Z_V)\\
 &\leq\sum_{z\in V}H(Z_z)+\sum_{z\in V}H(U_z\mid Z_V)\\
 &\leq\sum_{z\in V}\{H(Z_z)+H(U_z\mid N_z)\}.
\end{split}                                             \tag{6}
\]

Each $N_z$ is a function of $Z_V$, including when entries repeat.
By Lemma 1 the collision partition $\pi_z$ on $P$ is admissible.
Right evaluation gives

\[
 T_{w_s}(T_{v_t}(z))=T_{v_tw_s}(z).
\]

Consequently the summand in (6) is exactly $C_{\pi_z}$. At a good root
it is $C_0$, and elsewhere it is at most $M_{\rm bad}$. Dividing (6)
by $|V|$ gives

\[
 H(p)\leq (1-\eta)C_0+\eta M_{\rm bad}.                 \tag{7}
\]

To check the asserted denominator, take the one-point permutation action.
All words collide, $Z$ is the same diagonal function of the single
label at every position, and, since $D$ is nonempty,

\[
 H(Z)+H(U\mid N)=H(Z)+H(U\mid Z)=H(p).
\]

Thus its partition has cost $H(p)$. It cannot be good when
$C_0=H(p)-\delta<H(p)$. This proves the assertions about (4), and
rearranging (7) proves (5). ∎

Every table entry satisfies $C_\pi\leq\log|B|+H(p)$.
Hence (5) is at least as strong as the earlier bound

\[
 \eta\geq\frac{\delta}{\log|B|+\delta}.
\]

One may use $M=\max_{\pi\in\mathcal A}C_\pi$ instead of $M_{\rm bad}$.
When $\delta>0$, the preceding proof shows $M=M_{\rm bad}$.
Lemma 1 means that this $M$ is the smallest bound valid separately
at every root of every finite permutation model. The resulting defect
bound need not be sharp: it omits constraints linking different roots.

Lemma 1 imposes no relations of $G$ away from the chosen root. Its
completion is an action of the free group, and need not descend to $G$.
Thus realizing an individual pattern does not give a finite approximation
which is good at most roots. This distinction is essential when $G$
is not assumed sofic.

## 3. Individual word defects

Choose representative words in the equality classes of $W$ in $G$.
As in the earlier report, use equality tests between every word and its
class representative, and inequality tests between distinct class
representatives. Index these finitely many tests by $j$. Write
$m_j(\pi)=1$ when the test fails in $\pi$, and (0) otherwise.
For a finite permutation model let

\[
 q_j=|V|^{-1}\sum_{z\in V}m_j(\pi_z).
\]

For an equality test on $(u,v)$, this is the normalized Hamming defect
of $T_{uv^{-1}}$ from the identity; for an inequality test it is its
fixed-point fraction. Indeed

\[
 T_u(z)=T_v(z)\ \Longleftrightarrow\ T_{uv^{-1}}(z)=z.
\]

If nonnegative real weights $\omega_j$ satisfy the finite list of
inequalities

\[
 C_\pi-C_0\leq\sum_j\omega_jm_j(\pi)
                   \qquad(\pi\in\mathcal A),            \tag{8}
\]

then every finite permutation model satisfies

\[
 \boxed{\delta\leq\sum_j\omega_jq_j.}                   \tag{9}
\]

This follows by subtracting $C_0$ in (6), averaging (8), and
interchanging two finite sums. Choosing all weights equal to
$M_{\rm bad}-C_0$ proves feasibility when $\delta>0$: good types
have left side zero, and every bad type fails at least one test.
For any proposed vector of defect tolerances, minimizing the right side
of (9) subject to (8) is a finite linear program. No optimal weights or
global realization of a proposed distribution of types is asserted here.

## 4. An exact example with a genuine group pattern

Take $G=F_2=\langle a,b\rangle$, $S=D=(1,a,b)$,
$A=B=\{0,1\}$, and $f(x_0,x_1,x_2)=x_0x_1x_2$.
Let $p=\Pr[X=1]$, and write

\[
 h(p)=-p\log p-(1-p)\log(1-p).
\]

The required word set and its prefix closure are both

\[
 P=W=\{1,a,b,aa,ab,ba,bb\}.
\]

These seven freely reduced words are distinct in $F_2$, so the target
collision partition is certified without a word-problem assumption.
Models are still arbitrary assignments of two permutations; they need
not act freely.

**Proposition 3.** For this encoder and these windows, the exact maximum
of the collision table, over all finite permutation models, is

\[
 \boxed{M=h(p)+p\max\{h(p),h(p^2)\}.}                   \tag{10}
\]

**Proof.** At any root, $N$ contains $E=Z_{\rm root}$, because
$1\in D$. With $R=U_{\rm root}$,

\[
 H(E)+H(R\mid N)\leq H(E)+H(R\mid E)
                       =h(p)+H(E\mid R).               \tag{11}
\]

At the root $E=R U_{T_a(o)}U_{T_b(o)}$. After conditioning on $R=1$,
let $j\in\{0,1,2\}$ be the number of distinct encoder input positions
other than the root. If the two other positions coincide, they contribute
only one independent bit; occurrences of the root contribute the fixed
value one. Thus $E\mid(R=1)$ is a Bernoulli variable of parameter
$p^j$. On $R=0$ it is zero. Therefore

\[
 H(E\mid R)=p h(p^j)\leq p\max\{h(p),h(p^2)\},
\]

where $h(p^0)=h(1)=0$. This proves the upper bound, including
$p=0,1$ by direct evaluation.

For the first possible maximum, use two points with $T_a=T_b$ the
transposition. All three output names are the product of the two labels.
Thus $N$ determines precisely $E$, and (11) is an equality with
$j=1$, at each root. Its cost is $h(p)+p h(p)$.

For the second, use three points with $T_a$ a three-cycle and
$T_b=T_a^{-1}$. Each encoder reads all three labels. All output names
are their product, so equality holds in (11) with $j=2$. Its cost is
$h(p)+p h(p^2)$. These two models prove that the upper bound is
attained, establishing (10). ∎

For the fair base, $h(1/2)>h(1/4)$, and hence

\[
 M=\tfrac32\log2
       =1.0397207708399179\ldots,
 \qquad \log|B|+H(p)=2\log2
       =1.3862943611198906\ldots.                         \tag{12}
\]

The difference is $\tfrac12\log2$. This is an exact improvement of
the cap on defective roots for a certified group pattern. It is not a
positive-gap witness. In fact, for the discrete target partition here,
the coordinate sets used by the three output variables overlap only in
the ways shown by the seven words. The script computes $C_0\geq h(p)$
for the bases audited below. Thus (5), which assumes $\delta>0$, gives
no nontrivial lower bound on defects for these examples. The sharp cap
and the general theorem are the result; RBS remains unresolved.

The target cost can also be computed without enumerating seven labels.
Put $m_1=p^3$, $m_0=1-p^3$, $q_1=1$, and, when $m_0>0$,

\[
 q_0=\frac{p(1-p^2)}{1-p^3}.
\]

Here $q_i$ is the conditional probability that a child's root bit is
one given its output $i$. The two child outputs have independent laws
$(m_0,m_1)$, since their input sets are disjoint in $F_2$. Given
their outputs $(i,j)$, their root bits are conditionally independent
with probabilities $q_i,q_j$. The original root bit is still independent
of them. Its mutual information with its own output is consequently

\[
 h(pq_iq_j)-p h(q_iq_j).
\]

It follows that

\[
 C_0=h(p^3)+h(p)
      -\sum_{i,j\in\{0,1\}}m_i m_j
            \{h(pq_iq_j)-p h(q_iq_j)\}.                 \tag{13}
\]

Terms with $m_i m_j=0$ are omitted. Formula (13) and direct enumeration
agree exactly under rational entropy-product comparison for every audited
base, including $p=0,1$.

## 5. Verification and scope

`collision_costs.py` enumerates the partitions of the seven-word set,
tests (1), completes every admissible partition to explicit permutations,
and checks the resulting collision pattern at its root. It computes
every cost twice, by joint-minus-marginal entropy and by averaging
posterior entropies. For rational bases it also compares entropy sums
by expanding them into products of integer powers, giving exact signs.
The independent bound (11)–(10) does not rely on enumeration.

The table procedure is finite once the group pattern is specified. It
does not decide arbitrary presentation word problems, certify a new
non-sofic candidate, or characterize which distributions of rooted types
can occur in a large model. The latter issue can prevent sharpness of
(5) even though its cap is sharp at a single root. Bell-number growth
limits direct enumeration on larger windows.

The earlier conditional-entropy approach overlaps with Lewis Bowen and
Michael Chapman, *Surjunctivity does not characterize cosoficity of
invariant random subgroups*, [arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1),
Theorem 4.1 and Section 5. The earlier full-base reduction uses Brandon
Seward, *Krieger's finite generator theorem for actions of countable groups
II*, [arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4).
Neither reduction is claimed as new here. No priority claim is made for
the collision-table refinement or the partial-permutation completion
lemma.
