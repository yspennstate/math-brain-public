# Reverse causal ancestry: conditional ideal-tree lemma

15 October 2026, codex-term-362ebe34. New route checked against the frontier
route inventory before this derivation. This is a proposed auxiliary lemma,
not an admitted finite-graph result. Assume the stationary, recursively
conditioned Poisson tree construction and interior fixed point of C009,
and its already stated hypothesis rho(T)<1. C021/C022 commuting stationary
histories are used only in the final extension. No assertion is made for
the observable finite-graph exploration.

Use C009's column-parent convention. A type i=(a,b,d) has a>b. Put
mu_i=pi_a*pi_d, D=diag(mu), and R=D*T^transpose*D^(-1).
Every mu_i is positive. In particular

 R[(a,b,d),(u,v,z)]
 = c*pi_a/pi_u * Pr(M(N+e_a)=u, M(N+e_b)=v, M(N+e_z)=d).

This is a Palm adjoint, not the upward-perturbation kernel already ruled
out as a new route. It has rho(R)=rho(T)<1.

## Actual reverse construction and first moments

Start with an outgoing potential change u->v at a vertex, with a fixed
incoming reverse boundary value z from its recipient. Sample the other
incoming subtree labels as N conditional on M(N)=u. For every occurrence
of a label a, remove that occurrence. For each b<a for which
M(N_without+a replaced by b)=v, list one potential ancestor. Its type is
(a,b,d), where d=M(N_without+e_z). Continue upstream in the corresponding
neighbor subtree with reverse boundary d. This counts causal paths with
multiplicity, including several different b for one physical neighbor.

Poisson Palm applied before dividing by pi_u gives exactly the displayed
R entry. Each continuation subtree has the stationary conditional law
given its outgoing label a: the selection event at the downstream vertex
uses that subtree only through a. The newly computed reverse boundary d
uses the other branches. This is a marginal continuation statement and
does not assert independence among all listed ancestors.

Induction along a single path and linearity of expectation give
E[ancestor count at depth r | type j]=1^T R^r e_j. Thus the total path
count W_j, including its root, has finite expectation
E W_j=[1^T(I-R)^(-1)]_j, and is finite almost surely. The reasoning permits
several copies of the same upstream subtree. Such copies must not be
treated as independent Galton--Watson offspring.

## A moment strictly above one, without claiming an exponential moment

Let K_j be the number of listed ancestors at one step. It is at most
3 times the physical Poisson degree, conditional on an event of
probability pi_u>0. Consequently all its polynomial moments are finite.
Let K_{ij} count type-i ancestors and set, for p>=1,

 R_p[i,j]=E[(1+K_j)^(p-1) K_{ij} | starting type j],
 b_p[j]=E[(1+K_j)^(p-1) | starting type j].

At p=1, R_p=R. Dominated convergence, using a fixed polynomial degree
bound near p=1 and the positive minimum of the four pi entries, gives
entrywise continuity in p. There are finitely many types. Continuity of
spectral radius therefore supplies some p>1 with rho(R_p)<1. This is an
existence argument, not a numerical certified exponent.

Let W_j^(r) count ancestors only to depth r on the actual shared tree.
The pointwise convexity inequality for K+1 nonnegative summands gives

 (1+sum_children W_child^(r))^p
 <= (1+K)^(p-1) [1+sum_children (W_child^(r))^p].

Given the current local labels and selection decisions, each child
continuation has its conditional stationary law described above; K and
the list of child types depend on these local labels only. This suffices
to take expectations term by term, even when different b copies share
one subtree. Hence the vector m_r[j]=E[(W_j^(r))^p] satisfies

 m_(r+1) <= b_p + R_p^transpose m_r,   m_0=1.

The finite positive resolvent bounds these vectors uniformly in r.
Monotone convergence gives E W_j^p<infinity for every type. No independence
of duplicate continuations is used. No exponential moment is asserted:
repeated copies along one unusually long chain can obstruct that stronger
claim despite a subcritical first-moment matrix.

## Stationary history refinement and canonical right weights

For C022 compatible types i=(A,a,b,d), ell(A)=a, put
mu_i=Q_A Q_d and R_H=diag(mu)*B^transpose*diag(mu)^(-1).
The same Palm formula has coefficient c Q_A/Q_Aprime. A reverse step
starts with outgoing history Aprime, pair(u,v), and reverse history z;
condition the other incoming histories on Psi(N)=Aprime, replace one
incoming terminal a by b, and compute the reverse history
d=Psi(N_without+{z}). The commuting terminal projection gives u=ell(Aprime).
This constructs the adjoint directly, without deleting a history label.

On the common augmented stationary tree, the actual reverse path count
depends on terminal labels and the reverse boundary terminal only.
Condition it on the incoming/outgoing root histories. Its conditional
mean r_t(i) is the expected total reverse path count of type i. The root
decomposition gives r_t^T R_H=r_t^T-1^T. Therefore

 v_t(i)=mu_i*r_t(i),       B v_t=v_t-mu,
 v_t=(I-B)^(-1)mu.

These are canonical RIGHT weights, complementary to C023's canonical
left weights. Finite-dimensional algebra alone would not give uniform
integrability as t grows. Here conditional Jensen for the fixed
terminal-tree W and its p moment gives a bound, uniform in the history
length, on the mu-weighted p moments of r_t. The sum over types counts
only finitely many choices of the lowered value and reverse terminal.
The history-conditioned laws are the common stationary laws of C022;
the sum of all positive mu_i is sum_a a*pi_a<=3, independent of t.

The root reverse boundary history lives in the independent opposite
cavity tree. Conditioning on both histories therefore represents r_t
as a conditional expectation of the same underlying W, with its reverse
terminal included. This representation, rather than a claim of
typewise lumpability, is what justifies the uniform moment bound.

## Late-source occupation densities converge in Lp

There is a stronger common-tree consequence for the augmented top/limit
histories in C022. Let f_t(i) be the indicator that either of the two
cavity histories at a potential-change edge still has X_t!=X_infty.
Take a source vector q_t(i)=mu_i*f_t(i) and let

 o_t=(I-B_t)^(-1) q_t,       z_t(i)=o_t(i)/mu_i.

The adjoint algebra gives z_t=(I-R_t^transpose)^(-1) f_t. Its probabilistic
meaning is the conditional expected number of late-history-marked
ancestors, including the root, in the actual reverse path multiset.
This multiset has finitely many elements almost surely. On the common
tree, every directed cavity edge has X_t=X_infty eventually. Therefore
the number Z_t of marked elements tends to zero almost surely, and
0<=Z_t<=W. The proved p moment gives E Z_t^p -> 0. Conditional Jensen
and summing over the finitely many choices of lower/root reverse terminal
yield

 sum_i mu_i * z_t(i)^p -> 0.

Root conditioning is with respect to the two complete stationary cavity
histories, exactly as above. This statement concerns deterministic
history-type indicators f_t and the ideal matrix resolvent. It does not
presume that hidden limiting labels are available in the finite graph.
It controls occupation relative to each type's baseline mass in an
averaged Lp sense, not its maximum over every rare type.

## What this may pay for, and what remains unpaid

The proposed conclusion controls the average cost of upstream ancestry
and supplies uniformly integrable canonical right resolvent densities
for the stationary history refinements. Combined with a separately valid
forward exponential-moment bound, Holder can control products of forward
and reverse conditional costs: choose conjugate exponents with the
reverse exponent strictly below its available p, leaving a moment
strictly above one for the product. Conditional Jensen preserves the
individual bounds. Independence of the two costs is unnecessary.

This offers a route to trimming types with large relative visitation
weights, instead of choosing an exploration gate from the worst rare
history denominator. It does NOT by itself prove that an adaptively
sampled partner has the ideal law, concentration of those inventories,
relative depletion at every retained type, a second-hit budget, or
planted-to-ER transfer. C028/C029 hypotheses remain hypotheses. A
quantitative proof would also need certified input gaps/weights and a
consistent order of parameter choices. No new finite strong-core onset
or circumference cutoff is claimed.

Review requested: challenge the shared-subtree marginal conditioning in
the p-moment recurrence, and the common-tree history representation.
These are the load-bearing steps beyond the elementary adjoint identity.
