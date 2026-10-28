# Complete child reserves at a critical source

The full child budget is exponentially small in K. This does not fund it.

Let f be a Boolean sign on the uniform n-cube. Entropies use bits. Let A
be a nonempty proper coordinate block of size r. Write sigma=I_A(f),
g_x=f restricted to X_A=x, Hbar=E_x H(g_x), and Ibar=E_x I(g_x).
For each COMPLETE child let a(g) be its least influence under invertible
affine input maps and multiplication by an output character. These finite
operations preserve Fourier entropy. Define

    t=E a(g_x), Rchild=Ibar-t>=0,
    S*=E[K a(g_x)-H(g_x)], D=H(f)-K I(f).

No child, signed Fourier row, or old debit is discarded. All assertions
below are finite-dimensional. The minima are actual child orbit minima,
not component costs.

1. Exact accounting. Physical influence decomposes as I(f)=sigma+Ibar.
Consequently, with L=H(f)-Hbar,

    D+S*+K Rchild = L-K sigma.                         (1)

This holds for every K>0, without any criticality. In particular S* can
be negative and cannot then be spent as a reserve.

2. Entropy bound. Write the Fourier coefficients as a(z,T), with z in A
and T outside A, and mu(T)=sum_z a(z,T)^2. The partial physical row is
v_T(x)=sum_z a(z,T) chi_z(x). Parseval gives E v_T^2=mu(T).
The chain rule, with zero-mass rows omitted, gives exactly

    L=H(S_A|S_outside)+(1/ln 2) sum_T Ent(v_T^2).

Here Ent(u)=E u ln u-(E u) ln(E u). The uniform cube log-Sobolev
inequality, with D_i v=(v(x)-v(x+e_i))/2, gives
Ent(v^2)<=2 sum_i E(D_i v)^2. Summing rows yields the upper bound
c sigma for the second term, c=2/ln 2. The conditional entropy is at
most sum_i h2(Inf_i(f)), which by concavity is at most r h2(sigma/r).
Thus, including sigma=0 and sigma=r by continuity,

    D+S*+K Rchild <= r[h2(sigma/r)-(K-c)sigma/r].       (2)

Only this paragraph uses log-Sobolev. It is the same fibrewise inequality
as B11 lead R1, now applied to complete original child savings.

3. Sharp scalar elimination. For every real a and x in [0,1],
h2(x)-a x<=log2(1+2^(-a)). To prove it set p=1/(1+2^a) and expand
the nonnegative binary relative entropy D_2(Ber(x)||Ber(p)); the
difference between the upper bound and the left side is exactly that
relative entropy. Since 0<p<1 all denominators exist; endpoints follow
with 0 log 0=0. Equality holds precisely at x=p. Applying this to (2),

    D+S*+K Rchild <= r log2(1+exp(2) 2^(-K)).          (3)

For exact finite verification a rational constant is convenient:
ln 2>2/3 by strict Jensen applied to 1/t on [1,2]. Hence c<3 and

    D+S*+K Rchild <= r log2(1+2^(3-K)).                (4)

The latter is weaker, not a replacement numerical value for c.

4. Genuine critical class. Suppose f has positive D at the SAME K,
is represented on exactly n essential coordinates, and has least
essential dimension among positive-deficit Boolean signs. Every
complete child has smaller essential dimension, as does every member
of its affine/character orbit. Thus S*>=0. Equations (2)--(3) imply

    0<D <= r log2(1+exp(2)2^(-K)),
    0<=Rchild < (r/K)log2(1+exp(2)2^(-K)),
    0<=S* < r log2(1+exp(2)2^(-K)).

If sigma=0, (1) contradicts positivity, so sigma>0. Using
h2(x)<=x log2(e/x), positivity in (2) further forces

    sigma < exp(3) r 2^(-K).                          (5)

This last inequality is an absolute bound on the ORIGINAL selector
influence. It does not assert small H/I, bounded dimension, or that a
critical witness exists. For a singleton, Boolean granularity
Inf_i>=2^(1-n) gives n>1+K-3 log2(e). This is a dimension lower bound,
not a contradiction. The all-dimensional gap is not removed.

The essential-coordinate condition matters: a two-bit point defect with
one dummy bit, K=1 and A the dummy has D=1, sigma=Rchild=0, S*=-1.
Its exact full budget is zero, whereas deleting S* would give the false
conclusion D<=0. The essential three-bit point defect at K=1 also has
a negative singleton child reserve; positivity alone does not qualify it.

5. Interface and old debits. Stage20 gives the exact original-source
invoice D+S*=L_F-K(J-t)+Pi, with Pi the retained phase price. Combining
it with (1) only rewrites the same budget. Equations (3)--(4) do not
bound Pi separately. If an old booked influence u>=0 remains in that
invoice, its Ku cost remains; subtracting it from an available budget
does not authorize a renewed root or child bank. Phase/input
normalization alone cannot turn this upper bound into positive funding.

First unsupported universal line: force one original proper query to
have a nonpositive full invoice, including Pi and old debits, using
exact nonnegative smaller-child reserves and unused quotient-rank
release. No dimension-independent constant improvement is asserted.

6. Scoped review. A052 stage11 rank-rigidity corollary follows directly
from its scoped A055 inequality Daff(fP)<=Daff(f)-r m with m>0. An
actual competitor has D<=Daff(fP); comparing it to Daff(f)-epsilon
gives r m<=epsilon. The strict epsilon<m case forces integer r=0;
a singleton Fourier support of a Boolean phase is a signed character.
At epsilon=m the strict conclusion is unavailable. This review accepts
that corollary conditional on its stated rank/cost premise, and does
not independently accept A055's arbitrary-core embedding or census.
