# T186-C009 v1: a weighted downward-change branching process
Status: proof (unaudited), target 3; auxiliary tree statement only.
This does not establish convergence of finite-graph peeling.

Let M be the monotone four-state update in C005. At an interior fixed
point pi=(1-s,s-q,q-p,p) all four probabilities are positive. Let N have
independent Poisson(c*pi_j) coordinates. Let D={(a,b):0<=b<a<=3}.
Column vectors below count particles, so a matrix entry has offspring
type as its row and parent type as its column.

Define the six-type matrix
 L[(u,v),(a,b)] = c Pr(M(N+e_a)=u, M(N+e_b)=v), u>v.
Monotonicity ensures there are no upward differences. Define H with rows
indexed by thresholds 3,2,1 (coordinates p,q,s):
 H[t,(a,b)] = 1{b<t<=a}.
Let J be the Jacobian of the probability recursion in C005 at the fixed
point. Then H L = J H.

Proof. Move epsilon probability mass from b to a in the input law.
Its cumulative-probability displacement is epsilon H[:,(a,b)].
Differentiation of Poisson expectations gives, for every bounded f,
 d E f(N)/d epsilon = c E[f(N+e_a)-f(N+e_b)].
This follows by differentiating the absolutely convergent Poisson series;
a bounded f and finite positive Poisson means justify the differentiation.
Apply this to f(N)=1{M(N)>=t}. Since M is monotone, the difference is
exactly the sum over strict output drops (u,v) of H[t,(u,v)] times their
probabilities. The chain rule proves the asserted identity. In particular
J is nonnegative in the three cumulative coordinates.

If rho(J)<1, then rho(L)<1. Indeed w^T=1^T(I-J)^(-1)>0 and
theta^T=w^T H>0. The identity gives
 theta^T L = theta^T - 1^T H < theta^T
entrywise. A strictly positive left subinvariant vector for a finite
nonnegative matrix implies spectral radius strictly less than one.

The six types omit the baseline reverse message, which is important when
using this calculation in an exploration. Refine the types to (a,b,d),
(a,b) in D and d in {0,1,2,3}. Condition the vertex's other incoming
messages to have M(N)=d. Change the distinguished incoming message from a
to b. At each other neighbor whose outgoing update changes from u to v,
make a child of type (u,v,z), where z is that neighbor's message into the
current vertex. Conditional Poisson Palm calculation yields the 24-type
mean matrix
 T[(u,v,z),(a,b,d)] =
   c*pi_z/pi_d *
   Pr(M(N+e_z)=d, M(N+e_a)=u, M(N+e_b)=v).
Offspring of a parent can be dependent. Each child's continuation uses
an independent descendant tree conditioned on its individual message z.
That is a legitimate finite-type branching process, and conditional
independence of siblings is not required for its first-moment matrix.

Let E[(a,b,d),(a,b)]=pi_d, with all other entries zero. Summing over d gives
 T E = E L.
Since rho(L)<1, r=(I-L)^(-1)1>0 and Lr=r-1<r. Hence Er is strictly
positive and T(Er)=E(Lr)<Er, proving rho(T)<1.

All entries can be evaluated by the same exact finite caps as C006:
N_0 in {0,>=1}, ignore N_1, and N_2,N_3 in {0,...,k-1,>=k}.
No Poisson tail is discarded.

For clarity, J at a fixed point has rows
 (0, c*d*P_(k-1)(cq), c*p),
 (0, c*d*P_(k-2)(cq), c*q),
 (c*(1-d)*P_(k-2)(cp), c*d*P_(k-2)(cq),
  c*d*(Q_(k-1)(cq)-Q_(k-1)(cp))),
where d=exp(-c(1-s)) and P_j(x)=exp(-x)x^j/j!.
The certificates in C007 establish rho(J)<1 at the nine saved points,
so this lemma applies there, independently of the total-variation
obstruction in C008.

Unpaid step: the law of late changes in finite G(n,c/n) has not been
coupled to this stationary branching process with a uniform error bound.
In particular the hypotheses of Cooley--Lee--Ravelomanana Theorem 1.3
are not asserted. A finite-history coupling plus control of collisions,
multiple changed inputs, and conditioning on the baseline message is
still needed before deriving the density of the finite-graph core.

