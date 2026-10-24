# Universal variance-normalized restriction payment

Date: 2026-09-30. Complete analytic proof, independently reviewed. Full FEI remains open. No publication-priority claim.

## 1. The all-dimensional theorem

Let f be any +/-1-valued function on a uniform cube. Set v=Var(f), d=Inf_i(f)>0. Then

    B_i(f)<=d[log2(v/d)+(1+2/sqrt(e))/ln2],                       (1)
    Delta_i H(f)<=d[log2(v/d)+C_var],                            (2)
    C_var=(3+2/sqrt(e))/ln2=6.078162672495945... .

No monotonicity, certificate, degree, support or structural hypothesis is assumed. Here Delta_iH is root Fourier entropy minus average child Fourier entropy, and B_i is the conditional entropy of the queried spectral bit given all others. Influences d are actual physical influences, not folded influences. Since d<=v, log2(v/d)>=0.

### Proof

For every residual index T not containing i put u_T=fhat(T), z_T=fhat(T union {i}), q_T=u_T^2+z_T^2 and e_T=z_T^2. Then

    B_i=sum_T q_T h2(e_T/q_T).

Write c=fhat({i}). The exceptional empty packet has e0=c^2 and q0=(Ef)^2+c^2=1-v+c^2. All nonempty residual packets have exact totals

    E=sum_(T nonempty) e_T=d-c^2,
    Q=sum_(T nonempty) q_T=v-c^2.

In particular E<=d<=v and Q<=v. The last inequality d<=v is immediate because the squared coefficients containing i are among the nonempty Fourier coefficients.

The entropy bound q h2(e/q)<=e log2(euler*q/e), followed by log-sum, gives

    B_nonempty<=E log2(euler*Q/E)
               <=E log2(euler*v/E)
               <=d log2(euler*v/d).                            (3)

The final step holds because x log2(euler*v/x) is increasing for 0<x<=v. Zero total masses follow by continuity.

The physical derivative D_i^add f=(f_i^+-f_i^-)/2 takes values in {-1,0,1}; its absolute value is exactly the pivotal-edge indicator. Hence

    |c|=|E D_i^add f|<=E|D_i^add f|=d.

Thus e0<=d^2, while q0<=1. Monotonicity of q h2(e/q) in q and of x log2(euler/x) on [0,1] shows

    B_empty<=h2(e0)<=e0 log2(euler/e0)
             <=d^2 log2(euler/d^2).                            (4)

The scalar function d log2(euler/d^2), 0<d<=1, has derivative (-1-2 ln d)/ln2. Its maximum is attained at d=e^(-1/2) and equals 2/(sqrt(e)ln2). Combining (3)-(4) proves (1).

The exact restriction identity Delta_iH=B_i+JS, and the proved two-point logarithmic-Sobolev/Jensen-Shannon payment JS<=(2/ln2)min(d,1-d)<=(2/ln2)d, give (2). Irrelevant coordinates have d=B_i=Delta_iH=0. QED.

## 2. Decision-tree consequences

### Hereditary expected-depth theorem

Suppose every nonconstant physical restriction of f can be computed by a decision tree of expected depth at most D, where D>=1 is one uniform bound. Then

    H(f)<=(log2 D+C_var) I(f).                                 (5)

Indeed the O'Donnell-Saks-Schramm-Servedio inequality states

    Var(g)<=sum_i revealment_i(T) Inf_i(g)
           <=E depth(T) max_i Inf_i(g).

Thus every nonconstant restriction g has a coordinate of influence d>=Var(g)/D. Equation (2) then pays its full entropy decrement by (log2 D+C_var)d. Induction closes with the exact identity I(g)=d+average child influence.

The hereditary qualifier is essential. A small unconditional expected depth for just the root does not imply it after conditioning on a rare branch, and is not asserted to suffice for (5).

### Leaf-count theorem

If f is computed by a decision tree with at most s>=2 leaves, then

    H(f)<=[log2 log2 s+C_var] I(f).                            (6)

Prune repeated queries and irrelevant fixed tests. Under the uniform measure a reached leaf at depth a has probability 2^-a. Therefore expected depth equals the entropy of the leaf law and is at most log2 s. After any physical restriction the pruned tree still has at most s leaves. Applying (5) with D=log2 s proves (6).

The coefficient still grows with tree size. Formula (6) is not a dimension-independent FEI constant. The original short-certificate corollary and the child-defect logarithmic bound remain separately useful and are not superseded pointwise by (1).

## 3. Source comparison

Primary source for OSSS, including the exact variance/influence convention: O'Donnell, Saks, Schramm and Servedio, Every decision tree has an influential variable, https://arxiv.org/abs/cs/0508071 ; author-hosted paper https://www.cs.cmu.edu/~odonnell/papers/dt-influences.pdf .

Wan, Wright and Wu, Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture, https://arxiv.org/abs/1312.3003 , give a bound H<=12D I for expected depth D under their stated I>=1 condition. That is a different, nonhereditary parameter statement; neither comparison is a claim that one theorem universally replaces the other.

The repository September24 down-set continuation states log2 log2 s+7.85 for monotone decision-tree functions. Equation (6) applies to arbitrary Boolean functions, with the displayed exact constant. A bounded primary-source search did not establish literature priority for this ratio bound. No literature-first claim is made.

## 4. Review, computations and full-scope gap

A separate reviewer and the coordinating researcher reconstructed (1)-(2) from the exact packet totals, checked |fhat({i})|<=d, the scalar maximum, the OSSS normalization, and the hereditary/leaf-count distinction. No mathematical gap was found. The attached checker exhausts all Boolean functions through dimension4 and verifies the bound at each positive-influence coordinate using integer Walsh transforms followed by numerical entropy evaluation. These finite checks do not prove the theorem; the proof is above.

The all-coordinate sum of (2) still contains sum_i d_i log2(v/d_i). For families with many small influences that can exceed a constant multiple of total influence. Merely summing it does not prove the desired hereditary aggregate erasure inequality. The outstanding route must use actual signed Boolean convolution constraints and spectral-packet cancellations rather than discard them through log-sum.
