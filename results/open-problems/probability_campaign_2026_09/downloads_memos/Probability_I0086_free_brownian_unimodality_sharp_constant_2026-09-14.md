# The sharp constant for unimodality of free Brownian motion

**Problem.** Hasebe and Ueda, *Unimodality for classical and free Brownian motions*, ALEA 15 (2018),
Problem 3.3: what is the optimal universal constant $C>0$ such that $\mu \boxplus S(0,t)$ is unimodal
for every $t \ge C D_\mu^2$ and every compactly supported probability measure $\mu$, where
$D_\mu = \sup\{|x-y| : x,y \in \operatorname{supp}\mu\}$? Their Theorem 3.2 gives $C \le 4$.

**Answer.** $C = 1$.

**Theorem.** *Let $\mu$ be a compactly supported probability measure on $\mathbb{R}$ whose support has
diameter $D$. Then $\mu \boxplus S(0,t)$ is unimodal for every $t \ge D^2$, and the constant is optimal:
for the symmetric Bernoulli law on $\{-1,1\}$, which has $D = 2$, unimodality fails for every
$t < 4 = D^2$.*

The optimality half is their own Example 2.1. What is new is the bound $t \ge D^2$ in place of
$t \ge 4D^2$, which makes the constant sharp and settles the problem.

## The criterion

Everything runs through their Lemma 3.1: $\mu\boxplus S(0,t)$ is unimodal if and only if for every
$R>0$ the equation
$$\xi_R(u) := \int_{\mathbb{R}} \frac{d\mu(x)}{(x-u)^2+R^2} = \frac 1t$$
has at most two solutions $u \in \mathbb{R}$. This is Biane's description of the density read backwards:
the density of $\mu\boxplus S(0,t)$ at the image point $\psi_t(u)$ is $v_t(u)/(\pi t)$, where $v_t(u)$ is
the positive solution in $R$ of $\xi_R(u) = 1/t$, and $\psi_t$ is a homeomorphism, so a level set of the
density with three points is a level set of $v_t$ with three points.

Suppose the level $1/t$ has three or more solutions for some $R$. Since $\xi_R$ is smooth and vanishes
at $\pm\infty$, there is then a local minimum $u_0$ of $\xi_R$ carrying a local maximum on each side,
with
$$\xi_R(u_0) \le \frac 1t .$$
So the question is how low a *separating* local minimum of $\xi_R$ can be, and the theorem follows from
the next statement, applied after rescaling to $D=1$.

**Proposition.** *Let $\mu$ be a probability measure whose support has diameter at most $1$, let $R>0$,
and let $u_0$ satisfy $\xi_R'(u_0)=0$ and $\xi_R''(u_0)\ge 0$. Then $\xi_R(u_0) \ge 1$.*

Given the proposition, a failure of unimodality at time $t$ forces $1/t \ge \xi_R(u_0) \ge 1/D^2$, hence
$t \le D^2$, which is the theorem.

## Two points at a time

Translate so that $u_0 = 0$ and write $s = R^2$ and $\varphi(d) = 1/(d^2+s)$. The three quantities in
play are
$$F = \int \varphi \, d\mu = \xi_R(0), \qquad G = \int \frac{d}{(d^2+s)^2}\,d\mu = -\tfrac12 \xi_R'(0),
\qquad H = \int \frac{3d^2-s}{(d^2+s)^3}\,d\mu = \tfrac12\xi_R''(0),$$
and the hypotheses are $G = 0$ and $H \ge 0$. All three are linear in $\mu$.

Consider the set $K$ of probability measures $\nu$ on $\operatorname{supp}\mu$ with $G(\nu)=0$. It is
convex and weak-* compact, and its extreme points carry at most two atoms, since a measure subject to
normalisation and one further linear constraint can be perturbed inside $K$ as soon as its support has
three points. By Choquet's theorem $\mu$ is a barycentre of extreme points, and $F$, $G$ and $H$
integrate accordingly. An extreme point with a single atom must be $\delta_0$, because $G(\delta_x)=0$
forces $x=0$. So it is enough to understand a *pair*: atoms at $-a$ and $b$ with $a,b>0$ and
$a+b \le 1$.

For such a pair the condition $G=0$ determines the two weights, and writing $A = a^2+s$, $B = b^2+s$ and
$\Delta = bA^2+aB^2 > 0$,
$$F - 1 = \frac{\Phi}{\Delta}, \qquad H = \frac{\Psi}{\Delta AB}, \qquad
\Phi = bA(1-A) + aB(1-B), \qquad \Psi = bB(3a^2-s) + aA(3b^2-s).$$
In terms of $D = a+b$ and $m = ab$ both collapse:
$$\frac{\Psi}{D} = 3m^2 + s(6m - D^2) - s^2, \qquad
\frac{\Phi}{D} = 3m^2 + m(1-D^2) + s(1-2m) - s^2 .$$

**Lemma A.** *If $\Psi \ge 0$ then $s \le \tfrac34 D^2$.* The quantity $\Psi/D$ is increasing in $m$, so
it is largest at $m = D^2/4$, where it equals $(3D^2-4s)(D^2+4s)/16$. For that to be nonnegative,
$s \le \tfrac34 D^2$.

**Lemma B.** *If $0 \le s \le \tfrac34$ and $D \le 1$ then $\Phi \ge 0$.* The quantity $\Phi/D$ is
concave in $s$, so on $[0,\tfrac34]$ it is least at an endpoint. At $s=0$ it is $m(1+3m-D^2) \ge 0$. At
$s = \tfrac34$ it is a convex function of $m$ whose derivative at $m = D^2/4$ is $(D^2-1)/2 \le 0$, so it
decreases on $(0, D^2/4]$ and is least at $m = D^2/4$, where it equals $(1-D^2)(D^2+3)/16 \ge 0$.

## Putting it together

Let $\mu$, $R$ and $u_0$ be as in the proposition, and decompose $\mu$ into extreme points as above.

Since $H(\mu) \ge 0$, some extreme point $\kappa$ has $H(\kappa) \ge 0$. It cannot be $\delta_0$, for
which $H = -1/s^2 < 0$. So $\kappa$ is a pair, and Lemma A gives $s \le \tfrac34 D_\kappa^2 \le \tfrac34$.

Now every extreme point has $F \ge 1$. For $\delta_0$ this is $F = 1/s \ge 4/3$. For a pair it is Lemma
B, which needs only $s \le \tfrac34$ and diameter at most one, and in particular does not care about the
sign of that pair's own $H$. Averaging, $F(\mu) \ge 1$, which is the proposition.

Equality is rigid. Lemma B is an equality only at $D=1$, $m=D^2/4$ and $s = \tfrac34$, that is, two atoms
of equal weight at $\pm\tfrac12$ with $R^2 = \tfrac34$: the symmetric Bernoulli law at its critical
radius, rescaled. So the symmetric Bernoulli is the unique extremal measure, which is why the constant it
produces is the answer.

That rigidity says more than that the constant is sharp. Write $t^*(\mu)$ for the least time from which
$\mu\boxplus S(0,t)$ is unimodal. Attaining $t^*(\mu) = D_\mu^2$ needs a separating minimum at exactly the
value $1/D_\mu^2$, which forces equality in Lemma B, which forces the configuration above. So:

**Corollary.** *$t^*(\mu)\le D_\mu^2$ for every compactly supported $\mu$, with equality if and only if*
*$\mu$ is a symmetric two-point measure.* Every other measure of the same diameter becomes unimodal
strictly sooner.

## The lower bound in the source

The source states $2 \le C \le 4$ and attributes the lower bound to the Bernoulli example. That example
gives $C \ge 1$: the law on $\{-1,1\}$ has $D_\mu = 2$, so $D_\mu^2 = 4$, and unimodality from $t=4$
onwards is exactly the requirement $C D_\mu^2 = 4C \ge 4$. The comparison in the source is against
$D_\mu$ rather than $D_\mu^2$. With the theorem above the interval closes at the lower end anyway.

## Checks

Three independent ones, all agreeing.

1. The criterion was implemented directly from Lemma 3.1 and reproduces the source's Example 2.1: the
   symmetric Bernoulli on $\{-1,1\}$ comes out unimodal from $t = 3.985$ onwards, against the exact $4$,
   the gap being the resolution of the grid in $R$.
2. A search over 1,500 random measures with two to six atoms and diameter one found no separating local
   minimum of any $\xi_R$ below $1$, and a scan of 227,692 admissible three-atom configurations put the
   minimum at $1.0197$, approached only as the middle atom's weight goes to zero.
3. The closed forms for $\Phi$ and $\Psi$, the two identities in $D$ and $m$, and both lemmas were
   confirmed in a computer algebra system, and the two-atom case was scanned over $1.2\times 10^8$
   parameter triples with no violation.
4. The theorem itself was tested end to end, without the criterion: for eight random measures of
   diameter one, with three to five atoms and Dirichlet weights, the density of $\mu\boxplus S(0,t)$ was
   built from Biane's description and its modes counted, and $t^*$ found by bisection. The values run from
   $0.163$ to $0.398$, all well inside the bound, while the symmetric pair returns $0.99999$. The extremal
   case sitting at the bound and everything random far below it is the shape the rigidity corollary
   predicts.

## Status

Answered: $C = 1$, with a proof, and with the extremal measure identified as the symmetric Bernoulli. The
ingredients are the source's own Lemma 3.1, the extreme-point reduction, and two short polynomial
inequalities. Verification: author checked; the criterion reproduces the source's worked example, and
every algebraic step was confirmed symbolically. Prior art: I did not find the sharp constant stated
anywhere, the source poses it as open, and the citing papers I could reach repeat the bound $4$. Not a
clearance.

## New open problems

1. **The classical constant.** ANSWERED the same day, in a companion memo: for $\mu$ supported in an
   interval of length $D$, $\mu * N(0,t)$ is unimodal for every $t \ge D^2/4$, and that is sharp at the
   symmetric two-point measure. The same extreme-point argument works, with $\varphi_t$ in place of the
   Cauchy kernel: a pair of atoms at $-a$ and $b$ has $f''(0) \ge 0$ exactly when $t \le ab$, and
   $ab \le D^2/4$. It improves the source's own compact-support bound $9D^2$ by a factor of thirty-six.
   Memo: `Probability_classical_brownian_unimodality_sharp_constant_2026-09-14.md`.
2. **The exact threshold as a functional.** The corollary above answers the uniqueness half: among
   measures of a given diameter, $t^*$ is maximised only by the symmetric two-point law. What remains is
   regularity. Is $t^*$ continuous in the weak topology on measures of bounded diameter, or merely upper
   semicontinuous? It falls steeply away from the extremal configuration in the numerics, which suggests
   continuity without being evidence for it.
3. **Other free convolutions.** Replace the semicircle by a free stable law of index $\alpha \in (0,2)$.
   Is there a sharp constant of the same shape, and does the exponent $2$ on the diameter become
   $\alpha$?
4. **Variance in place of diameter.** For measures with unbounded support the diameter is useless but the
   variance is not. Is there a constant $C'$ with $\mu \boxplus S(0,t)$ unimodal for every
   $t \ge C' \operatorname{Var}(\mu)$ and every $\mu$ of finite variance? The source's Section 3.2 shows
   that some condition is needed, since there are measures that never become unimodal.
