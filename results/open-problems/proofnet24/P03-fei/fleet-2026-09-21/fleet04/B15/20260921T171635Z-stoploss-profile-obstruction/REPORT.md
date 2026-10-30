# B15 FEI spectral remainder: stop-loss order for packet valuations and a tail-profile blindness obstruction

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or isolated evaluator was used in this mathematics.

This run continues the unequal-Fourier-magnitude / arithmetic-remainder route from the spectral-lattice and centroid/carry handoffs. It consumes the fresh fleet02/B15 all-cost valuation-majorization theorem as a proved peer input and derives two new consequences:

1. the complete packet-valuation distribution is dominated, in increasing-convex order, by an explicit random variable built from the folded spectral marginals;
2. despite that strong control, the entire valuation stop-loss profile is asymptotically blind to the universal arithmetic remainder under the already-proved rare Boolean isolation construction.

The second result is a rigorous obstruction to a natural next step: no finite summable linear combination of *all* valuation-depth tails can materially reduce the universal coefficient needed to pay the remainder `D`.

## 1. Inherited exact setup

For a Boolean sign function `f:{0,1}^n->{-1,+1}`, group the nonzero Fourier coefficients by distinct magnitudes `a`. Let

- `A_a={S: |fhat(S)|=a}`;
- `p_a=|A_a| a^2`, so `sum_a p_a=1`;
- `epsilon_a` be the signed indicator of `A_a`;
- `V_a(x)=sum_S epsilon_a(S) chi_S(x)`;
- `r_a=min_{V_a(x) != 0} nu_2(V_a(x))`;
- `b_a=a 2^{r_a}`.

The spectral-lattice continuation proves `0<b_a<=1` and the exact decomposition

\[
R(f)=\sum_a p_a r_a,\qquad
D(f)=\sum_a p_a\log_2\frac1{b_a},\qquad
H(f)=2R(f)+2D(f).
\tag{1}
\]

It also proves `R(f)<=2J(f)<=2I(f)`, where

\[
q_i=\min(\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)),\qquad
J(f)=\sum_i q_i.
\tag{2}
\]

The fresh fleet02/B15 theorem strengthens this. Sort the folded marginals decreasingly,

\[
q_1^\downarrow\ge\cdots\ge q_n^\downarrow.
\]

If the random packet valuation `X_f` has law

\[
\Pr[X_f=r]=\sum_{a:r_a=r}p_a,
\tag{3}
\]

then for every `1<=m<=n`,

\[
\boxed{
T_m(f):=\mathbb E(X_f-m+1)_+
\le 2\sum_{k=m}^n q_k^\downarrow.
}
\tag{4}
\]

No automatic physical integrality is assumed in (1)--(4).

## 2. PROVED: an explicit increasing-convex dominator

Define an integer-valued random variable `Y_f` on `{0,1,...,n}` by its survival function

\[
\boxed{
\Pr[Y_f\ge k]=2q_k^\downarrow,\qquad 1\le k\le n.
}
\tag{5}
\]

This is a genuine probability law because `0<=q_n^\downarrow<=...<=q_1^\downarrow<=1/2`. Equivalently, with `q_{n+1}^\downarrow=0`,

\[
\Pr[Y_f=0]=1-2q_1^\downarrow,\qquad
\Pr[Y_f=k]=2(q_k^\downarrow-q_{k+1}^\downarrow).
\tag{6}
\]

### Theorem B15-STOPLOSS-ICX-05

For every Boolean `f`,

\[
\boxed{
\mathbb E(X_f-m+1)_+
\le
\mathbb E(Y_f-m+1)_+
\quad(1\le m\le n).
}
\tag{7}
\]

Consequently, for every nondecreasing convex function
`\phi:{0,1,...,n}->R` with `\phi(0)=0`,

\[
\boxed{
\mathbb E\,\phi(X_f)
\le
\mathbb E\,\phi(Y_f)
=
2\sum_{k=1}^n q_k^\downarrow
\bigl(\phi(k)-\phi(k-1)\bigr).
}
\tag{8}
\]

Thus `X_f` is dominated by `Y_f` in the increasing-convex (stop-loss) order.

### Proof

From (5),

\[
\mathbb E(Y_f-m+1)_+
=
\sum_{k=m}^n\Pr[Y_f\ge k]
=
2\sum_{k=m}^nq_k^\downarrow,
\]

so (7) is exactly (4).

For the second assertion put

\[
d_k=\phi(k)-\phi(k-1).
\]

Monotonicity and convexity say `0<=d_1<=...<=d_n`. For every integer `r>=0`,

\[
\phi(r)
=
d_1r+
\sum_{m=2}^n(d_m-d_{m-1})(r-m+1)_+.
\tag{9}
\]

Take expectations in (9), apply (7) term by term, and telescope the resulting coefficients. The coefficient of `q_k^\downarrow` is

\[
2\left[d_1+\sum_{m=2}^k(d_m-d_{m-1})\right]=2d_k,
\]

which gives (8). QED.

### Useful exact corollaries

Taking `\phi(r)=r^2` gives

\[
\boxed{
\mathbb E X_f^2
\le
2\sum_{k=1}^n(2k-1)q_k^\downarrow.
}
\tag{10}
\]

For every real `s>1`, taking `\phi(r)=s^r-1` gives the exponential/Orlicz family

\[
\boxed{
\mathbb E(s^{X_f}-1)
\le
2(s-1)\sum_{k=1}^n s^{k-1}q_k^\downarrow.
}
\tag{11}
\]

Equation (11) is a genuine all-depth statement: high 2-adic packet valuations have exponentially weighted mass controlled by the tail geometry of the folded influence profile. It is strictly more information than the first moment `R<=2J`.

## 3. PROVED obstruction: all valuation tails can vanish while the remainder stays hard

The preceding remainder-isolation handoff proves the following rare Boolean replacement theorem. For every Boolean seed `g` with `I(g)>0`, there is a sequence of Boolean functions `F_t` such that

\[
H(F_t)\to H(g),\qquad
I(F_t)\to I(g),\qquad
R(F_t)\to0,
\tag{12}
\]

and therefore by (1),

\[
D(F_t)\to\frac12H(g).
\tag{13}
\]

This interacts decisively with the new stop-loss profile.

### Theorem B15-TAIL-BLINDNESS-06

For the sequence in (12),

\[
\boxed{
\sup_{m\ge1}T_m(F_t)\le R(F_t)\longrightarrow0,
}
\tag{14}
\]

while `D(F_t)->H(g)/2`.

Hence the **entire** packet-valuation stop-loss profile can collapse uniformly to zero while the unpaid arithmetic remainder converges to half the seed Fourier entropy.

More quantitatively, let `(w_m)_{m>=1}` be any fixed nonnegative summable sequence and suppose a universal inequality of the form

\[
D(f)
\le
C\,I(f)+\sum_{m\ge1}w_m T_m(f)
\tag{15}
\]

holds for all Boolean `f`. Then necessarily

\[
\boxed{
C\ge \frac{H(g)}{2I(g)}
}
\tag{16}
\]

for every nonconstant Boolean seed `g`. Therefore, in the extended-real sense,

\[
\boxed{
C\ge\frac12 C_{\rm FEI},
\qquad
C_{\rm FEI}:=\sup_f\frac{H(f)}{I(f)}.
}
\tag{17}
\]

### Proof

For every `m` and integer `r>=0`,

\[
(r-m+1)_+\le r.
\]

Therefore

\[
0\le T_m(F_t)\le R(F_t),
\]

which proves (14).

Let `W=sum_m w_m<infinity`. Applying (15) to `F_t` gives

\[
D(F_t)
\le
C I(F_t)+W R(F_t).
\]

Pass to the limit using (12)--(13):

\[
\frac12H(g)\le C I(g).
\]

This is (16); taking the supremum over seeds gives (17). QED.

### What this rules out

The all-cost valuation theorem is strong, but it controls the `r_a` side of the factorization

\[
a=2^{-r_a}b_a.
\]

The rare-isolation sequence proves that unrestricted FEI hardness can be moved almost completely into the mesh depths

\[
\log_2(1/b_a)
\]

while **every** stop-loss tail of `r_a` disappears. Thus a proof that first compresses all arithmetic information to the valuation distribution and then pays a fixed summable combination of its tails cannot close the universal remainder with a better base coefficient.

This does **not** refute FEI. It says the next successful remainder estimate must retain information that is invisible to the valuation profile alone: normalized physical mesh depth, product-shadow/KL credits, or a coupled restriction/transport quantity that can transfer credit between these ledgers. Nonsummable depth weights are not ruled out by Theorem B15-TAIL-BLINDNESS-06, but they would need a separate dimension-free influence payment.

## 4. Exact finite sanity checker

`verify_stoploss_order.py` independently recomputes integer Walsh transforms, packet valuations and folded spectral marginals. It exhaustively checks all 65,812 Boolean functions in dimensions 1 through 4.

Exact integer checks passed for:

- all `262,948` stop-loss inequalities (4), one for each function and depth;
- all corresponding packet-mass-tail inequalities;
- `65,812` quadratic consequences (10);
- `65,812` base-2 exponential consequences of (11);
- `65,812` base-4 exponential consequences of (11).

The largest packet valuation seen in this finite atlas was `2`. These checks are finite sanity evidence only; the proofs above do not infer the theorem from enumeration.

Checker SHA-256:
`510d5d5610eb199ab89067d42049e7a6d40a3f900983acf0ff77837b3d3133b9`

Verification-output SHA-256:
`677cc59992a5d6c38a5433008198d0f2646e1f375ad41bc8da2c512a58451c72`

The clean executed command was the current Python interpreter with `-S` and this checker; it exited `0` with empty stderr.

## 5. Fresh primary-literature scope check

A fresh search on 21 September 2026 found no primary source claiming unrestricted uniform-cube FEI closure.

- V. N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563 (18 Sep 2026), proves FEI for plateaued functions with sharp class constant `4`, and for partially bent functions with sharp class constant `2`.
- M. J. González, P. MacManus, M. C. Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (29 May 2026), develops a restriction/stopping-tree route and explicitly identifies a key restriction inequality whose general Boolean validity would imply full FEI.
- P. Li and G. Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, arXiv:2512.03117 (2 Dec 2025), proves a general bound retaining an additional influence-profile entropy term, rather than a dimension-independent `H<=C I` theorem.

No publication-priority claim is made here for Theorems B15-STOPLOSS-ICX-05 or B15-TAIL-BLINDNESS-06.

## 6. Next exact target

The valuation side is now unusually well controlled: not only its mean but every increasing-convex functional is dominated by an explicit folded-influence law. The obstruction shows that this cannot be the missing resource by itself.

The most focused next B15 target is therefore a **coupled mesh-depth/negative-credit inequality**. One concrete formulation is to seek a nonnegative packet quantity `K_a`, retained from the product-shadow/KL representation, such that

\[
\sum_a p_a\log_2(1/b_a)
\le
C I(f)+\sum_a p_a K_a
\]

while the same `K_a` telescopes or is refunded under restriction/transport. The point is to keep the mesh ledger and the information-credit ledger coupled until payment; recombining them first into `D`, `H-R`, or a pure valuation profile has now been shown to lose essential structure.

Full FEI remains OPEN.
