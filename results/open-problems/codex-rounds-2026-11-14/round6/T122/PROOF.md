# A uniform zero-temperature limit of the hierarchical upper bound

Fix an integer d>=3. All logarithms are natural. The hierarchy below
has no random root variable. The result concerns the finite-hierarchy
infimum J_d(beta) from round 5; it does not identify it with the
random regular graph pressure.

## 1. Finite-temperature functional and the recursion

For beta>0 and u,v in [-1,1], put

\[
 D_\beta(\sigma,u)=\frac{1-\sigma u}{2}
                  +e^{-\beta}\frac{1+\sigma u}{2},\qquad
 B_\beta(u,v)=\frac{1-uv}{2}+e^{-\beta}\frac{1+uv}{2},
\]
\[
 A_\beta(u_1,\ldots,u_d)
       =\frac12\sum_{\sigma=\pm1}\prod_{j=1}^d
                                      D_\beta(\sigma,u_j).
\tag{1}
\]

Choose r>=1, parameters 0<zeta_0<...<zeta_(r-1)<1, and a measurable
h:[0,1]^r -> [-1,1]. On each nonroot vertex gamma of the tree N^r,
take independent uniform marks U_gamma^j, one array for each input
label j, independent of normalized Ruelle cascade weights V_alpha.
Write h_alpha^j=h(U_(alpha|1)^j,...,U_(alpha|r)^j). The functional is

\[
 H_{d,\beta}(r,\boldsymbol\zeta,h)
 =\log2+\frac{\beta d}{2}
 +\mathbb E\log\sum_\alpha V_\alpha
                         A_\beta(h_\alpha^1,\ldots,h_\alpha^d)
 -\frac d2\mathbb E\log\sum_\alpha V_\alpha
                         B_\beta(h_\alpha^1,h_\alpha^2),
 \qquad J_d(\beta)=\inf H_{d,\beta}.
\tag{2}
\]

This agrees with the cut normalization of round 5: replacing each
uncut edge factor by exp(beta) times that factor shifts the site term
by beta*d and the edge term by beta, giving the shift beta*d/2 in (2).
The two expectations may use separate independent input arrays.

Here is the cascade recursion used below. If W is a bounded positive
function of the marks on one branch, bounded away from zero, define
W_r=W and, for k=r,r-1,...,1, define

\[
 W_{k-1}(z_1,\ldots,z_{k-1})
   =\left(\mathbb E_{z_k}W_k(z_1,\ldots,z_k)^{\zeta_{k-1}}
                                                   \right)^{1/\zeta_{k-1}}.
\tag{3}
\]

Each z_k may be a finite vector of independent uniforms, one for
each incoming message. Then

\[
 \mathbb E\log\sum_\alpha V_\alpha W_\alpha=\log W_0.
\tag{4}
\]

Equation (4) is the elementary cascade identity proved in Section 6
of [round 5 PROOF.md](~/codex_op_1114r5/briefs/T122/PROOF.md).
Its scale can also be checked directly. For a Poisson process with
intensity q*t^(-1-q)dt and independent marks Z, multiplication of
each point by f(Z) changes its intensity by E f(Z)^q. Division by
(E f^q)^(1/q) restores the process. Starting at the terminal vertices,
multiply their points by W_r/W_(r-1), sort, and repeat at the next
level with W_(r-1)/W_(r-2). The standardized descendant processes
are independent of all earlier marks and processes, because their
conditional laws are constant. Thus the operation can be iterated.
The product of ratios along a path is W/W_0. Consequently the tilted
unnormalized cascade total T_W has the same distribution as W_0*T,
where T is the original total. Taking logarithms of
sum V_alpha W_alpha=T_W/T proves (4).

These logarithms are integrable. Indeed T has a positive stable law
with exponent zeta_0: its Laplace transform is exp(-c*lambda^zeta_0)
for c>0. This follows inductively from the marked Poisson calculation;
at each earlier level the subtree total has the required positive
moment because zeta_(k-1)<zeta_k. The integral identities for positive
moments of order p<zeta_0 and negative moments of any order show
E|log T|<infinity. Alternatively those moment integrals and the full
summability induction are given in round 5, Sections 3 and 6.
Bounds l*T<=T_W<=u*T then give integrability for T_W. No independence
between T and T_W is required in taking the difference of their
expected logarithms.

The regular upper bound p_d(beta)<=J_d(beta), where p_d is limiting
cut pressure, follows from the invariant-law inclusion proved in round 5
and Theorem 2.7 of Amin Coja-Oghlan and Will Perkins,
[*Spin systems on Bethe lattices*, arXiv:1808.03440v1](https://arxiv.org/html/1808.03440v1).
The general regular finite-RSB upper bound is also Theorem 3.2 of
Viktor Harangi, [*RSB bounds on the maximum cut*, arXiv:2506.21296v1](https://arxiv.org/html/2506.21296v1).
The uniform limit of J_d established below is an analytic assertion
about (2) and (4). Its proof does not require an additional graph theorem.

## 2. The energetic functional

For 0<y_0<...<y_(r-1)<infinity and a bounded real function f of
z_1,...,z_r, define f_r=f and

\[
 f_{k-1}(z_1,\ldots,z_{k-1})
   =-\frac1{y_{k-1}}\log\mathbb E_{z_k}
                         e^{-y_{k-1}f_k(z_1,\ldots,z_k)},
 \qquad \mathcal L_{\boldsymbol y}f=f_0.
\tag{5}
\]

The expectations at successive levels integrate only the current
coordinates, keeping all preceding coordinates fixed. For a function
of q input messages, z_k is a q-vector of independent uniform variables.
Different inputs have independent vectors at every level.

For x_1,...,x_d in [-1,1] and x,y in [-1,1], define

\[
 S(x_1,\ldots,x_d)
      =\frac{\sum_{j=1}^d|x_j|-|\sum_{j=1}^d x_j|}{2},
 \qquad
 E(x,y)=\frac{|x|+|y|-|x-y|}{2}.
\tag{6}
\]

In particular S is the smaller of the total positive field and the
total absolute negative field. E(x,y) is zero for opposite signs or a
zero input, and is min(|x|,|y|) for inputs with the same nonzero sign.
Both functions are continuous. We have 0<=S<=d/2 and 0<=E<=1.
These are the local energetic costs in Harangi, Section 4, where
they are used for one-step trial bounds. The assertion here is
uniformity over the entire finite-hierarchy infimum in (2).

Given a measurable field function x:[0,1]^r -> [-1,1], use independent
copies of its input coordinates to form x^1,...,x^d. Define

\[
 K_d(r,\boldsymbol y,x)
     =\frac d2-\mathcal L_{\boldsymbol y}S(x^1,\ldots,x^d)
                 +\frac d2\mathcal L_{\boldsymbol y}E(x^1,x^2).
\tag{7}
\]

The operators for the site and edge terms use d and 2 input coordinates,
respectively. Define the two infima

\[
 K_d^{<b}=\inf_{\substack{r\geq1,\ 0<y_0<\cdots<y_{r-1}<b\\
                              x:[0,1]^r\to[-1,1]\ \mathrm{measurable}}}
                                     K_d(r,\boldsymbol y,x),
 \qquad
 K_d^\infty=\inf_{\substack{r\geq1,\ 0<y_0<\cdots<y_{r-1}<\infty\\
                              x:[0,1]^r\to[-1,1]\ \mathrm{measurable}}}
                                     K_d(r,\boldsymbol y,x).
\tag{8}
\]

All these quantities are finite. In fact (5) preserves the range of
its input, so every value in (7) is nonnegative, and x=0 gives d/2.
Thus 0<=K_d^infinity<=K_d^{<b}<=d/2.

**Theorem.** For every beta>0,

\[
 K_d^{<\beta}-\frac{2d\log2}{\beta}
 \ \leq\ \frac{J_d(\beta)}{\beta}
 \ \leq\ K_d^{<\beta}+\frac{(2d+1)\log2}{\beta}.
\tag{9}
\]

Consequently

\[
 \lim_{\beta\to\infty}\frac{J_d(\beta)}\beta=K_d^\infty.
\tag{10}
\]

The constants in (9) are independent of depth, parameters and field
function. No attainment of any infimum is assumed.

## 3. Uniform local estimates, including deterministic spins

For a possibly extended real field xi, assign two costs a_+,a_-:
if xi is finite, a_sigma=(|xi|-sigma*xi)/2; if xi=+infinity,
(a_+,a_-)=(0,infinity); if xi=-infinity, reverse these two values.
Use exp(-infinity)=0. Let

\[
 p_\sigma(\xi)=\frac{e^{-\beta a_\sigma}}
                         {\sum_{\tau=\pm1}e^{-\beta a_\tau}},
 \qquad N(\xi)=\sum_{\tau=\pm1}e^{-\beta a_\tau}.
\tag{11}
\]

We have 1<=N<=2. The spin mean is tanh(beta*xi/2) for finite xi
and is the corresponding deterministic spin at either infinity.
For xi=0 the spin is fair. Write x=clip(xi,-1,1), with the natural
endpoint interpretation at infinity.

From (1) and (11),

\[
 D_\beta(\sigma,\tanh(\beta\xi/2))
 =\frac{\sum_{\tau=\pm1}
              e^{-\beta[a_\tau(\xi)+\boldsymbol1\{\sigma=\tau\}]}}
              {N(\xi)}.
\tag{12}
\]

The least exponent cost in this numerator is x_+=max(x,0) if sigma=+1,
and x_-=max(-x,0) if sigma=-1. To verify this, if xi>0 its preferred
spin is +1: choosing tau=+1 costs 1 when sigma=+1 and 0 otherwise;
choosing tau=-1 costs xi plus the corresponding edge cost. Hence
the minima are min(1,xi) and 0. The argument reverses for xi<0,
and both minima are zero at xi=0. It also applies to infinite xi.

For any sum of k exponentials with at least one finite cost and least
cost c, the sum lies between exp(-beta*c) and k*exp(-beta*c).
Apply this with k=2 to (12), and use 1<=N<=2. For either sigma,

\[
 \frac12e^{-\beta x_\sigma}
 \leq D_\beta(\sigma,\tanh(\beta\xi/2))
 \leq2e^{-\beta x_\sigma}.
\tag{13}
\]

Multiplying (13) for d messages, summing over sigma and dividing by
two gives

\[
 2^{-(d+1)}e^{-\beta S(x_1,\ldots,x_d)}
 \leq A_\beta(\tanh(\beta\xi_1/2),\ldots,\tanh(\beta\xi_d/2))
 \leq2^d e^{-\beta S(x_1,\ldots,x_d)}.
\tag{14}
\]

For the lower bound, retain a minimizing value of sigma. For the upper
bound, bound each of the two terms by its maximum allowed value.
The minimum over sigma of sum_j (x_j)_sigma is exactly S in (6).

Likewise the edge factor is

\[
 B_\beta(\tanh(\beta\xi/2),\tanh(\beta\eta/2))
 =\frac{\sum_{\sigma,\tau=\pm1}
          e^{-\beta[a_\sigma(\xi)+a_\tau(\eta)
                                    +\boldsymbol1\{\sigma=\tau\}]}}
             {N(\xi)N(\eta)}.
\tag{15}
\]

If the preferred signs differ, their simultaneous choice has zero
cost. If exactly one field is zero, choose its spin opposite the preferred
spin of the other field; if both are zero, choose opposite spins.
Again the minimum is zero. If the preferred
signs agree, the minimum is min(1,|xi|,|eta|): retain both preferred
spins at cost 1, or reverse either one at its field cost. Reversing
both cannot improve this minimum. The same conclusions hold at infinity.
Clipping both fields to [-1,1] therefore gives precisely E(x,y) in (6).
Using four numerator terms and 1<=N(xi)N(eta)<=4 gives

\[
 \frac14 e^{-\beta E(x,y)}
 \leq B_\beta(\tanh(\beta\xi/2),\tanh(\beta\eta/2))
 \leq4e^{-\beta E(x,y)}.
\tag{16}
\]

In particular define f_A=-beta^(-1)log A_beta and
f_B=-beta^(-1)log B_beta for these messages. Equations (14) and (16)
give the pointwise bounds

\[
 S-\frac{d\log2}{\beta}\leq f_A
                \leq S+\frac{(d+1)\log2}{\beta},
 \qquad
 E-\frac{2\log2}{\beta}\leq f_B
                \leq E+\frac{2\log2}{\beta}.
\tag{17}
\]

## 4. Propagation through an arbitrary finite hierarchy

For a>0, let T_a f=-(1/a)log E exp(-a*f), conditionally on the
preceding coordinates when there are any. If f<=g pointwise, then
exp(-a*f)>=exp(-a*g), so T_a f<=T_a g. For any constant c,
T_a(f+c)=T_a f+c. It follows that f-epsilon<=g<=f+epsilon implies
T_a f-epsilon<=T_a g<=T_a f+epsilon. Applying this observation
successively proves the same monotonicity and constant-shift properties
for L_y in (5). In particular the error does not acquire a factor r.

Set y_k=beta*zeta_k. In (3) put W=exp(-beta*f). Inductively,
W_k=exp(-beta*f_k), because

\[
 (\mathbb E e^{-\beta\zeta_{k-1}f_k})^{1/\zeta_{k-1}}
 =\exp\left\{-\beta\left[-\frac1{y_{k-1}}
                         \log\mathbb E e^{-y_{k-1}f_k}\right]\right\}.
\]

Thus (4) gives the exact identity

\[
 \frac1\beta\mathbb E\log\sum_\alpha V_\alpha
                                      e^{-\beta f_\alpha}
                  =-\mathcal L_{\boldsymbol y}f.
\tag{18}
\]

By (2) and (18), each finite-temperature trial satisfies

\[
 \frac{H_{d,\beta}}\beta
 =\frac d2+\frac{\log2}{\beta}
       -\mathcal L_{\boldsymbol y}f_A
       +\frac d2\mathcal L_{\boldsymbol y}f_B.
\tag{19}
\]

Apply (17) through L_y. For the lower bound in (19), use the upper
bound on f_A and lower bound on f_B. The total additive error is
[1-(d+1)-d]log(2)/beta=-2d log(2)/beta. For the upper bound use
the other two bounds; the error is [1+d+d]log(2)/beta. Hence

\[
 K_d(r,\boldsymbol y,x)-\frac{2d\log2}{\beta}
 \leq\frac{H_{d,\beta}(r,\boldsymbol\zeta,h)}\beta
 \leq K_d(r,\boldsymbol y,x)+\frac{(2d+1)\log2}{\beta},
\tag{20}
\]

whenever h=tanh(beta*xi/2) with the endpoint conventions above and
x its clipped field function.

Every measurable message h:[0,1]^r -> [-1,1] is covered: on |h|<1
take xi=(2/beta)artanh(h), and at h=+/-1 take xi=+/-infinity.
This is a measurable extended field function. Then x=clip(xi,-1,1)
is an admissible field in (8), and y_(r-1)<beta. The lower bound
in (20), followed by the infimum over all original trials, yields
the lower bound of (9).

Conversely, given any trial (r,y,x) in K_d^{<beta}, take
zeta_k=y_k/beta and h=tanh(beta*x/2). These are admissible in (2),
and no clipping changes x. The upper bound in (20) applies. Since
J_d(beta) is at most this particular H, taking the infimum over
these energetic trials proves the upper bound of (9). This argument
uses both directions of trial conversion and does not assert that
clipping preserves finite-temperature trial values exactly.

## 5. Passing the optimized infimum to zero temperature

As b increases, the domains in K_d^{<b} increase, so these infima
decrease and are bounded below by K_d^infinity. Let epsilon>0. By
the definition of the latter infimum there is one finite trial
(r,y,x) with K_d(r,y,x)<K_d^infinity+epsilon. Every b>y_(r-1)
admits this trial, so

\[
 K_d^\infty\leq K_d^{<b}<K_d^\infty+\varepsilon
                    \qquad (b>y_{r-1}).
\]

Therefore K_d^{<b} decreases to K_d^infinity. Combining this fact
with (9) proves (10), even when the nearly minimizing depths and
all their parameters vary with beta. It also covers sequences of
scaled parameters approaching zero, infinity, or one another, since
(9) is uniform and the proof only uses strictly ordered finite
parameters at each individual trial. No compactness or minimizer
existence has been used.

There is no asserted rate for K_d^{<beta}-K_d^infinity. The error
in (9) is the error relative to the truncated energetic domain.

## 6. Relation to the unresolved regular-graph equality

Let c_d be the limiting MaxCut per vertex, and p_d(beta) its cut
pressure. From the round 5 upper bound and the elementary entropy
estimate,

\[
 c_d\leq\frac{p_d(\beta)}\beta
        \leq c_d+\frac{\log2}\beta,\qquad
 p_d(\beta)\leq J_d(\beta).
\tag{21}
\]

For each fixed energetic trial, (20), with zeta=y/beta and beta
larger than its last y, shows H/beta -> K_d(r,y,x). Taking the
limit in c_d<=H/beta gives c_d<=K_d(r,y,x), and then
c_d<=K_d^infinity. Finally, for Delta_d(beta)=J_d(beta)-p_d(beta),
(10) and (21) give

\[
 \lim_{\beta\to\infty}\frac{\Delta_d(\beta)}\beta
                        =K_d^\infty-c_d\geq0.
\tag{22}
\]

Thus the next reverse comparison can be posed entirely at zero
temperature: prove K_d^infinity<=c_d. This inequality is not proved
here. Formula (10) identifies the limit of the optimized hierarchical
upper bound; it does not identify the graph optimum.

## 7. Independent checks

For a direct check of the edge minimum in (15), put
t_sigma(x)=a_sigma(x) and list its four costs. If xi,eta>=0 these
are 1, |eta|, |xi|, |xi|+|eta|+1. Their minimum is
min(1,|xi|,|eta|). If xi>=0 and eta<=0 the preferred (+,-)
choice has cost zero. Spin reversal supplies the other cases.
This reproduces (6) independently of the preferred-spin argument.

For the star, minimizing first over incoming spins gives
min(sum_j (x_j)_+,sum_j (x_j)_-). The identity
min(P,N)=(P+N-|P-N|)/2 gives exactly S. Alternatively minimize
over all d+1 spins in its numerator at once. There are 2^(d+1)
terms, and its denominator is 2*prod_j N(xi_j), between 2 and
2^(d+1). This yields the same two constants in (14), independently
of multiplying (13). Four edge terms and denominator between 1 and 4
independently reproduce (16). Substitution in the site-minus-d/2-edge
expression rechecks both constants in (9).

At depth one, L_y f=-(1/y)log E exp(-y*f). At depth two it is

\[
 -\frac1{y_0}\log\mathbb E_{z_1}
            \left(\mathbb E_{z_2}e^{-y_1 f}\right)^{y_0/y_1},
\]

as also follows by marking the terminal and top processes separately.
For f=f_1(z_1)+f_2(z_2) this becomes
-(1/y_0)log E exp(-y_0*f_1)
-(1/y_1)log E exp(-y_1*f_2), checking the order of the exponents.

For the constant zero field, S=E=0, so K=d/2. Its finite-temperature
message is h=0, for which (2) is
log 2+(d/2)log((1+exp(beta))/2). Its limiting slope is d/2.
For a constant positive field t in (0,1], S=0 and E=t, giving
K=d/2+(d/2)t. Independently beta^(-1)log D_beta(+1,h) tends to -t
and beta^(-1)log D_beta(-1,h) tends to zero; beta^(-1)log A_beta
tends to zero, and beta^(-1)log B_beta(h,h) tends to -t.
Substitution in (2) gives the same K.
This checks the edge sign on a nonzero field.

As a nonconstant check, take d=3, r=1 and x=+1 or -1 with equal
probabilities. Then S=0 with probability 1/4 and S=1 with probability
3/4; E=0 and E=1 each with probability 1/2. With z=exp(-y),

\[
 K_3=\frac32+\frac1y\log\frac{1+3z}{4}
                    -\frac3{2y}\log\frac{1+z}{2}.
\tag{23}
\]

The probabilities can also be obtained from the eight sign triples
and four sign pairs: two triples are monochromatic and six are mixed;
two pairs agree. At y=log 3 this becomes
3-(5/2)log(2)/log(3), by direct substitution of z=1/3. Its value
lies strictly between 1 and 3/2: use 2^5<3^4 and 2^5>3^3,
respectively. This is only a normalization check and is not claimed
as an improved numerical bound.

In particular replacing fields by their signs would change the
constant-field check whenever 0<t<1. The field magnitudes in (6)
must be retained. Endpoint messages h=+/-1 correspond to infinite
unclipped fields and are included by (11); field zero is a fair spin,
not an undefined sign. These conventions also cover mixed zero and
endpoint inputs in both (14) and (16).
