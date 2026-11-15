# C33 v1: finite-site block upper comparison and exact range closure

Status: proof (unaudited). Kind: special. Target: 2.
This is a comparison/finite-probability method, with novelty unassessed.
No T4 contraction certificate or classification is asserted in this proof.
The hardest open piece is a rigorously verified contraction for ordinary T4.

## 1. Block exploration and the proposed upper process

Consider the ordinary frog model on the rooted d-ary tree, d>=2, with one
resident away from the root and finitely many initial root frogs. Choose a
finite rooted prefix-closed tree A containing its root. Cut at each missing
child edge, attach another copy of A, and repeat. The missing-child words
form a complete finite prefix code, so every infinite downward ray is cut
repeatedly and the original tree is partitioned into these finite blocks.

An episode starts when one frog enters a block. For a downward entry into
its top vertex, regard every resident in its new copy as cold. For an upward
entry from a child block into vertex v, omit all residents on the path from
the block's top to v, inclusive; call this set W warm. Allow one resident at
each other site, waking it only on its first visit in this episode. Run the
ordinary walks, stop every frog on its first exit from the block, and let
each exit start a fresh episode in its adjacent block. Distinct episodes
use independent copies of all the residents they permit. Retain all frog
motions. The global root block uses degree d at the global root, while all
other vertices use degree d+1. Upward exits of the global root block do not
exist. The initial root episode may use all its residents; this supplies
only finitely many initial paths and has finitely many expected exits.

This is an upper comparison. In the actual process, all vertices on the
ancestral path of any visited vertex are already awake: the visited set is
connected to the original root. In particular every resident omitted by an
upward episode is already awake in the actual process. Its actual frog is
already represented by its own walk and need not be born again. All other
residents may be copied afresh, which can add frogs. Within an episode,
each permitted site contributes at most one resident.

Here is a pathwise exploration coupling with the order of exposure explicit.
Preassign independent complete original resident walks to the physical
vertices. At the FIRST upper visit to a nonroot vertex v, use its original
resident walk for that upper birth. This walk has not been exposed before
this visit, so it is fresh and independent of the upper past. Later clones
at v use additional independent walks. A first upper visit cannot be a warm
omission: the upper visited set is connected to the global root too, so an
upward entry's ancestral path has already been visited. Initial root frogs
are represented in the initial episode. Continue every upper frog across
block boundaries with its ordinary fresh future; never discard its motion.

Now explore the actual model using the preassigned original paths. If an
original frog at u is awake in the actual model, its matching first upper
birth at u has the same COMPLETE path, including its continuations through
later episodes. Every vertex that path awakens is therefore eventually
visited above and has its corresponding first upper birth. Induction over
finite awakening witnesses gives domination of every actual awakened frog
and each of its root visits. This argument does not condition on an actual
activation event while choosing an already exposed clone. Independent
unused original walks and the extra clone walks give precisely the fresh
per-episode laws, by deferred exposure and strong Markov at boundaries.
It does not require mutual independence of an episode's offspring counts.

## 2. Exact finite-site calculation

Fix one episode, its seed location s, warm set W, and cold set C=A\W.
Preassign to the seed and each cold resident its independent ordinary walk
stopped on first exiting A. Each path exits in finite expected time: the
finite internal Markov chain has accessible absorbing boundary. For v in C
let O_v be the cold sites visited by its assigned path. Define O_0 similarly
for the seed. The final cold awake set Q is exactly the reachability closure
of O_0 under the independent outgoing sets O_v, v in C.

For S subset C, put g_v(S)=P(O_v subset S), and let g_s(S) refer to the seed
path with the same starting location. These probabilities are obtained by
killing at cold sites outside S and accepting exits from A. On W union S,
solve the finite rational system

    g_v(S)=P_v(next step exits A)+sum_(u in W union S) P(v,u) g_u(S).

For starts outside W union S, the answer is zero. All matrix entries are
rational for ordinary motion. The matrix is invertible by finite absorption;
exact rational elimination therefore accounts for all return excursions,
without a time or path-length truncation.

Write q_T=P(Q=T). Then for every S subset C,

    g_s(S) prod_(v in S) g_v(S)
      =sum_(T subset S) q_T prod_(v in S\T) g_v(S).       (1)

Indeed the left event says the seed path and every resident path indexed by
S stay within W union S before exiting. It forces Q subset S. On Q=T, this
event additionally requires that every unused row v in S\T stays inside S.
The event Q=T uses only the seed row and rows in T. The other rows are
independent of that event and of one another. This proves the product and
the partition in (1). No independence between site-activation events is
asserted. Solving (1) in increasing inclusion order gives q_S exactly by
subtracting its proper-subset terms, since the coefficient of q_S is one.
Impossible disconnected awake sets have mass zero: every new visit follows
a connected walk from s through warm or newly awakened sites. Thus it is
legitimate to skip masks for which W union S is disconnected from s.

Let h_v(e) be the probability the assigned walk at v first exits through
boundary category e. The mean offspring count through that category is

    m(e)=h_s(e)+sum_(v in C) P(v in Q) h_v(e).            (2)

The first visit to v does not use v's own path. Removing that resident leaves
its activation event unchanged, so the event is independent of its unused
path, as in C3's standard first-moment identity. Equation (2) follows by
linearity. The number of offspring is at most 1+|C|. These formulas concern
sites once per episode, not a reproduction event at every revisited vertex.

## 3. A checkable sufficient transience criterion

Assign each episode entry a positive potential Phi. Suppose for every bulk
entry and every returning entry into the exceptional global-root block,

    E[sum_(offspring j) Phi(j) | entry type/context] <= a Phi(entry),
    where 0<=a<1.                                      (3)

The finitely many possible root-block entry sites must have potentials
bounded below by a positive constant. The finite initial root episode has
finite expected offspring potential. Induction and Tonelli bound the total
expected potential of all later episode generations by a geometric series.
It follows that the expected number of root-block episodes is finite.
Each such episode contributes at most the sum of 1+|A| preassigned stopped
walk local times at the global root; their finite-state Green functions
give a uniform finite expectation. Thus the upper process has finitely many
expected root visits. The original process, coupled above, does as well.
Consequently it is transient almost surely. With C3 this also gives summable
ordinary site-activation probabilities. Nonexistence of a tested potential
does not imply recurrence or rule out different upper comparisons.

For the prototype, A has a top, all d children, and the d children of each
of its first k selected children (or consists of its top alone). Boundary
parent categories e are the symmetry classes of unexpanded leaves, of
depth h_e. Use potential z^(physical entry depth) w_T(e) for a top entry
whose parent-block attachment is category e, and
z^(physical entry depth) w_B(c) for an upward entry at category c. The latter
weights do not depend on the block's unknown parent attachment b. Test every
possible b. Formula (2) supplies the following finite list of inequalities:

    top attached b:
      sum_e m_T(e) z^(h_e+1) w_T(e)+m_T(up) z^(-1) w_B(b)
          <= a w_T(b);
    bottom at c, attached b:
      sum_e m_c(e) z^(h_e+1-h_c) w_T(e)
          +m_c(up) z^(-1-h_c) w_B(b) <= a w_B(c);
    global-root bottom at c:
      sum_e m_root,c(e) z^(h_e+1-h_c) w_T(e) <= a w_B(c).

These physical-depth factors include the entry location and the global root
explicitly. Rational z>0, positive rational weights and rational a<1 checked
against every row give a certificate of (3). No independence multiplication
or unbounded-tail estimate is hidden in the test.

## 4. Computation, controls, and remaining task

`exact_site_block_upper.py` implements the finite formulas using Fraction.
Each solved linear system is checked by exact substitution; closure masses
are checked nonnegative and summing to one. Files checkpoint exact partial
mass tables and are separated by the full script's source hash. The sized
prototype permits at most 13 sites, one CPU core and a bounded command.
A separate Markov queue on a star checks its three episode means, including
the global-root degree. The one-site ordinary T6 control admits z=2/7,
w_T=2,w_B=1 and a=97/98; this is a known-case control, not a new theorem.
Floating-point potential search only proposes weights; an accepted
certificate is rechecked entirely in exact rational arithmetic.

This written method is unaudited. A coefficient file alone does not certify
the pathwise upper coupling. A failed candidate search is not a spectral
impossibility proof. No ordinary T4 certificate is supplied in this version.
Source context: HJJ, arXiv:1404.6238, Section 3.2, Proposition 18 and the
multitype martingale display (12), use branching comparisons and weighted
offspring matrices. That general transience method is known; this draft
does not claim it as new. The particular finite-site closure recurrence is
derived here without attributing it to HJJ. C3 supplies the independently
derived standard site first-moment identity.
