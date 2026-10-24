# Direct entropy induction for lacunary finite-crossing scores

Date: 2026-10-02. **Complete elementary derivation of an already covered
class.** This is useful as a checkpoint for the nearby-three-crossing
research route, not a new solution of an open FEI subclass. The general
tree class below is already covered by the tree-covariance theorem of
Wan--Wright--Wu; the lacunary score corollary is already a bounded-read
decision-tree class. The direct proof is preserved because it isolates
the exact hypothesis that fails for general score weights.

## A decision-tree parameter and theorem

Prune every constant residual function to a leaf. Queries do not repeat
a coordinate on one root-to-leaf path. Call a queried node branching if
**both child residual functions are nonconstant**. Suppose every path
contains at most `b` such nodes; ordinary query depth may be unbounded.
Then, for uniform inputs and full Fourier entropy,

\[
 \boxed{H(f)\le(8+4b)I(f).} \tag{1}
\]

This parameter is not called ordinary decision-tree rank here: rank has
a different recurrence. Input restriction cannot increase the parameter
of a given tree after pruning, since it only deletes nodes and can turn
previously nonconstant children into constants.

## The two local entropy estimates, proved explicitly

For a split `f(x,z)=A(x)+zB(x)`, let `a_S,b_S` be its real Fourier
coefficients, `P_S=a_S^2+b_S^2`, and

\[
 q_S=b_S^2/P_S,\qquad r_S=(a_S+b_S)^2/(2P_S).
\]

Zero pairs are omitted. Since `A^2+B^2=1`, the `P_S` sum to one, and
\(\alpha=I_z(f)=\sum_S b_S^2\). Direct expansion of the entropy of
the full coefficients `a_S,b_S` and restricted coefficients `a_S±b_S`
gives

\[
 \Delta_z H(f)
 =\sum_S P_S[1+h_2(q_S)-h_2(r_S)]. \tag{2}
\]

The elementary inequality `h_2(t)>=4t(1-t)` follows, for example, from
the positive power series for `1-h_2((1+x)/2)`: its coefficients sum to
one and every `x^(2j)<=x^2` on `[-1,1]`. Because
`r_S(1-r_S)=(1-2q_S)^2/4`, (2) implies

\[
 \Delta_zH(f)\le2\sum_SP_Sh_2(q_S)\le2h_2(\alpha). \tag{3}
\]

### A universal bound by the total influence

For a minority event of density `p<=1/2`, cube edge isoperimetry is
`I(f)>=2p log_2(1/p)`. A short induction supplies this fact. For an event
of size `a`, split its sections of sizes `a_0,a_1` and put
`q=min(a_0,a_1)/a`. The two internal boundaries are at least
`a log_2(2^(n-1)/a)+a h_2(q)` by induction. The crossing boundary is at
least `a(1-2q)`. Concavity gives `h_2(q)>=2q`, so their sum is at least
`a log_2(2^n/a)`. Multiplying by `2/2^n` gives the physical influence
formula. Empty/full events use `0 log(1/0)=0`.

Every pivotal coordinate edge has a minority endpoint, hence
`alpha<=2p`. For `p<=1/4`, monotonicity of `h_2` up to `1/2` gives

\[
 h_2(\alpha)\le h_2(2p)
 \le2p[\log_2(1/p)-1+\log_2e]
 \le4p\log_2(1/p)\le2I(f).
\]

For `p>=1/4`, the concave function `p log_2(1/p)` is at least `1/2`
on `[1/4,1/2]`, so `I(f)>=1` and `h_2(alpha)<=1<=I(f)`. Consequently

\[
 \boxed{\Delta_zH(f)\le4I(f)} \tag{4}
\]

for every Boolean function and every split. Constants are immediate.

### One constant child

If one child is constant, an output sign change makes that value `+1`.
Then `A=1-|B|`; here `B` is either `0,+1` or `0,-1`. Its support density
is `alpha`, and `|EB|=alpha`. The nonempty pair-spectrum mass is

\[
 1-(1-\alpha)^2-\alpha^2=2\alpha(1-\alpha)\le2\alpha.
\]

Its contribution to the conditional entropy in (3) is therefore at most
`2alpha`. If `alpha>=1/2`, the whole conditional entropy is at most
one, already at most `2alpha`. Otherwise its empty-pair contribution is
at most

\[
 2\alpha^2\log_2(1/\alpha)+(\log_2e)\alpha^2
 \le\left(\frac{2\log_2e}{e}+
           \frac{\log_2e}{2}\right)\alpha<2\alpha.
\]

Here `log(1+t)<=t` in natural logarithms bounds the other empty-pair
entropy term. Thus (3) proves

\[
 \boxed{\Delta_zH(f)\le8\alpha} \tag{5}
\]

whenever one child is constant. This is an actual support identity,
not an assumption about the sign of a general derivative.

## Full induction

Write `C_b=8+4b`. A leaf has zero entropy. At a node with one constant
child, each nonconstant child still has branching budget at most `b`.
By induction, the exact influence decomposition and (5),

\[
 H(f)\le8\alpha+C_b\tfrac12[I(f^+)+I(f^-)]\le C_bI(f).
\]

At a node with two nonconstant children, `b>=1` and each child has budget
at most `b-1`. Equation (4) gives

\[
 H(f)\le4I(f)+C_{b-1}\tfrac12[I(f^+)+I(f^-)]
 \le(4+C_{b-1})I(f)=C_bI(f).
\]

This proves (1) without controlling sums of component influences.

## Arbitrary crossings of a superincreasing score

Suppose the positive weights are ordered and satisfy

\[
 w_j>\sum_{i>j}w_i \qquad\text{for every }j<n. \tag{6}
\]

After coordinate sign changes this also permits signed nonzero weights.
The score order of all vertices is lexicographic in `x_1,...,x_n`.
Let `m` be the number of actual sign changes in that attained-score
order; arbitrary point labels are allowed and only retained changes
count. Splitting the largest remaining weight separates the two score
copies strictly, so their label strings concatenate. Therefore

\[
 m_{\rm parent}=m_-+m_++\epsilon,
 \qquad\epsilon\in\{0,1\}. \tag{7}
\]

If both children are nonconstant then each has at least one sign change,
and either chosen child's crossing count is at most the parent's minus
one. Consequently the branching budget is at most `m-1` for `m>=1`.
Constants (`m=0`) are treated separately. The direct theorem gives

\[
 \boxed{H(F(\sum_iw_ix_i))\le(4m+4)I(F(\sum_iw_ix_i)).} \tag{8}
\]

For three actual crossings this is the constant 16. This is a completed
subsidiary calculation, **not** a new qualitative FEI class: at each
depth the nonconstant score copies are disjoint ordered intervals,
each containing an actual crossing, so there are at most `m` of them.
The ordered tree queries each coordinate at that one depth and hence
is read-`m`, already covered by earlier FEI results.

## Precise prior-art overlap

I opened the full primary manuscripts:

* Wan--Wright--Wu, *Decision Trees, Protocols, and the Fourier
  Entropy-Influence Conjecture*, ITCS 2014,
  [arXiv:1312.3003](https://arxiv.org/pdf/1312.3003).
  Theorem 1.1 gives `H<=9k I` for read-`k` trees; Theorem 1.2 treats
  bounded average depth with `I>=1`. Lemma 1.7 gives a coding bound
  `4I+2Cov[T]`, and Lemma 1.5 converts it to entropy with alphabet size
  three and an additional `2I`, retaining the empty spectral atom.
* Shalev, *On the Fourier Entropy Influence Conjecture for Extremal
  Classes*, [arXiv:1806.03646v2](https://arxiv.org/pdf/1806.03646).
  Theorem 9 improves read-`k` dependence to `O(sqrt(k))`.

In fact the first source already covers the general `b` class directly.
Let child functions be `u,v`. Their covariance is at most
`(Var(u)+Var(v))/2`, and this average is at most `Var(f)`. Tree covariance
is zero at one-constant-child nodes apart from the child average. An
induction on `b` therefore gives `Cov[T]<=b Var(f)`. The prior coding
result yields

\[
 H(f)\le[4\log_2 3+2+2b\log_2 3]I(f). \tag{9}
\]

This is usually better than (1). Neither (1) nor the lacunary qualitative
corollary is claimed historically new. The point of retaining the full
elementary proof is to isolate **crossing-count descent**: it is valid
for disjoint score copies, and the
[tiny-weight full-retention obstruction](three_crossing_full_retention_obstruction.md)
shows why it fails for general three-crossing scores.

The standalone checker and report are
[verify_three_crossing_direct_entropy_heat.py](verify_three_crossing_direct_entropy_heat.py)
and [three_crossing_direct_entropy_heat_checks.json](three_crossing_direct_entropy_heat_checks.json).
Checks supplement the proof; they cannot establish historical priority
or arbitrary nearby-crossing FEI.
