# B19 / A094 independent review — B12 tensor terminal-reserve no-go

## Verdict

**INDEPENDENTLY ACCEPTED AT DECLARED SCOPE; NO REPAIR REQUIRED.**

The B12 package at canonical receipt commit
`ef67e8cd5c8e81b3eb4ffb13ce2a786bb52bddc3` correctly proves two no-go
statements for the exact upper-set potential $U$:

1. no absolute constant can pay every endpoint-centered one-child cocycle
   solely by $C\,\beta(1-\mu^2)$; and
2. no absolute constant can pay every such cocycle solely by
   $C\,\beta I(h)$, even when the child $h$ is a genuine Boolean point
   defect.

The package also gives a genuine six-physical-input Boolean composition
whose normalized endpoint-centered cocycle is exactly greater than $4$.
These are child-only terminal-reserve obstructions. They do not refute a
joint outer/child ledger, the proposed universal GU inequality, or FEI.
Full FEI remains **OPEN**.

## Object and normalization

For a Boolean outer gate with distinguished input $y$, write its two
slices as $u$ and $v$, put

\[
 a=(\widehat u+\widehat v)/2,\qquad
 b=(\widehat v-\widehat u)/2,\qquad
 \beta=\sum_Tb_T^2=(1-\langle u,v\rangle)/2.
\]

For a Boolean child $h$ of mean $\mu$, the source cocycle states

\[
 U(g(h,z))=\beta U(h)+\Theta(\mu).
\]

The endpoint-centered remainder is

\[
 \overline\Theta(\mu)=\Theta(\mu)
 -\frac{1-\mu}{2}\Theta(-1)
 -\frac{1+\mu}{2}\Theta(1).
\]

This is the only quantity reviewed here. In particular, the normalization
retains the physical distinguished-input factor $\beta$ and uses the
child's actual physical total influence when the source payment is tested.

## Independent analytic reconstruction

The four-bit slices are

\[
u=(-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1)
\]

and full parity

\[
v=(1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1).
\]

The Walsh transform of $u$ is

\[
\widehat u=\frac18(-1,3,1,-3,1,-3,3,-1,-3,-3,-1,-1,-1,-1,1,1),
\]

while $\widehat v$ is supported on the full set. Hence
\(\rho=\langle u,v\rangle=1/8\). If
\(p_T=\widehat u(T)^2\) and
\(C_T=\sum_{R\supseteq T}p_R\), exact rational arithmetic gives

\[
A:=\sum_T\frac{p_T}{C_T}=\frac{6911}{960}>7.
\]

For tensor slices $U_k=u^{\otimes k}$ and $V_k=v^{\otimes k}$,
\(\beta_k=(1-8^{-k})/2\). Differentiating the cap expression at
\(\mu=-1\), each non-full tensor atom contributes

\[
-p_T\log_2\frac{C_T}{p_T}
+\frac{p_T(1+C_T)}{2C_T\ln2}.
\]

The omitted full-set and derivative-energy terms are nonnegative. Using
tensor multiplicativity of $A$, additivity of $U(u^{\otimes k})$, and
the crude bound $U(u)\le4$ yields

\[
\frac{\overline\Theta'_k(-1+)}{2\beta_k}
\ge \frac{A^k-3}{2\ln2}-2k.
\]

The right side diverges exponentially. Therefore an endpoint-centered
bound $\overline\Theta(\mu)\le C\beta(1-\mu^2)$ cannot hold uniformly.

For the $8k$-bit point-defect child, let
\(r=2^{-8k}\), \(\mu=-1+2r\), and \(q=1-r\). For every non-full atom,
the relevant mixed cap is $qC_T+r$. Since $C_T\ge64^{-k}$,

\[
x=\frac r{qC_T}\le\frac12,
\]

and $\ln(1+x)\ge x/2$ applies. Keeping all signs and normalization terms
gives the source package's bound

\[
\frac{\overline\Theta_k(\mu)}{\beta_k I(h)}
\ge \frac1{8k}\left[
\frac{q(A^k-1)}{2\ln2}-4k-\frac2{\ln2}
\right].
\]

It too diverges exponentially. This is a genuine Boolean child with
physical influence $I(h)=16kr$; the proof uses the weaker denominator
bound $\beta_k I(h)\le8kr$ in the correct direction.

## Exact six-input certificate

At $k=1$ take the two-bit AND-sign child
\(h=(-1,-1,-1,1)\), whose mean is $-1/2$. The resulting composition has
two child variables and four outer variables, hence six physical inputs.
The independent checker reconstructed its complete truth table and the
upper-set potential directly. It obtained

\[
\frac{\overline\Theta(-1/2)}{\beta(1-1/4)}
=4.053216515937682655274247143673\ldots>4.
\]

The strict sign is not based on this decimal. Clearing the rational
coefficients of the prime-log expression gives denominator $336$ and an
exact integer comparison with bit lengths $3358$ and $3340$; the left
integer is larger. The direct six-input chain rule agrees with the
slice formula to $6\times10^{-89}$ at 90-digit diagnostic precision.

## Independent computational challenge

`INDEPENDENT_CHECK.py` was written independently of the source checker.
It:

- recomputes both Walsh spectra, $\rho=1/8$, and $A=6911/960$ exactly;
- certifies the six-input ratio above $4$ by exact integer arithmetic;
- reconstructs the complete Boolean composition and checks the cocycle;
- directly evaluates endpoint tensor ratios for $k=1,2,3$;
- directly evaluates point-defect source ratios for $k=1,2,3$; and
- checks every rational premise of the source-influence estimate for
  $1\le k\le40$.

All checks pass. The direct endpoint ratios for $k=1,2,3$ are about
$6.34$, $39.54$, and $272.29$; the direct source ratios are about $1.54$,
$4.93$, and $22.68$. These finite values are diagnostics, not the proof of
unboundedness; the displayed analytic lower bounds supply that proof.

## Proof-chain and scope challenge

The following claims survive review:

- the one-biased-child $U$ cocycle and its endpoint centering;
- the exact six-input refutation of constant $4$ for the variance-only
  reserve;
- the all-$k$ endpoint-centered variance-only no-go; and
- the all-$k$ Boolean point-defect source-influence-only no-go.

The following conclusions do not follow and are not accepted:

- that every terminal-reserve strategy fails;
- that no joint ledger using outer influence, activation cost, retained
  endpoint $U$, or correlation information can work;
- that the displayed tensor family has unbounded Fourier entropy/influence
  ratio; or
- that FEI is false or proved.

The tensor parameter $k$ increases both arity and the custom cap ratio.
Its exponential growth is a no-go for the two named child-only payments,
not an FEI counterfamily.

## Literature comparison

O'Donnell--Tan proves an FEI composition theorem for outer functions
composed with Boolean functions on disjoint input blocks, under biased-FEI
hypotheses. It does not state a bound for this upper-set potential or a
child-only terminal reserve. Potapov proves FEI for plateaued Boolean
functions; that endpoint theorem does not control this coherent
nonflat-slice cocycle. Accordingly, this review accepts no priority or
novelty claim beyond the exact internal no-go statements.

## Status and next unpaid step

The B12/A056 child-only terminal-reserve route is closed at its stated
hypotheses. The surviving target is a joint payment whose budget includes
the outer physical gate and can charge each activation or correlation
resource only once. Such a theorem must remain uniform in tensor depth,
bias, weight groups, address count, overlap, and correlation gap.

No dimension-independent universal payment has been proved. Full FEI
remains **OPEN**.
