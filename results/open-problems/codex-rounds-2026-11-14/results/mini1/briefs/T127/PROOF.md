# A transience certificate for Bernoulli sleepers

Consider the rooted d-ary tree. Initially the root has one active frog and
each non-root vertex independently has one sleeping frog with probability q
and none otherwise. Frogs perform independent simple random walks. Count a
visit whenever a frog is at the root at an integer time, including time zero.

**Proposition.** This model has finite expected total root visits, and hence is
almost surely transient, for

- d=3 and 0 <= q <= 41/100;
- d=4 and 0 <= q <= 33/50.

At the respective endpoints, upper bounds on the expected number of visits are
1640000/1239 and 273700/461. If there is also a sleeping frog at the root, it
may be activated at time zero; the bounds double and transience still follows.

These are bounds for diluted initial conditions. They give no conclusion for
the one-sleeper-per-site model q=1. No assertion of optimality or of priority
over existing bounds is intended.

## 1. An upper process

A packet represents one or two frogs at a common vertex. Away from the root,
use three packet types:

- F: one frog, with no remembered information about its children;
- D: two frogs, with no remembered information about their children;
- B: one frog, with one specified child known to contain no sleeper.

The parent contains no sleeper. Indeed, every visited non-root vertex was
first reached from its parent. Thus its parent has already been visited.
Remembering that a child is empty is valid whenever a frog has just stepped
from that child toward the root.

In the upper process, all children not remembered empty receive independent
fresh Bernoulli(q) sleeper marks at each transition. A packet's frogs take
independent uniform choices among the d children and the parent. Marks are
shared for arrivals from the same packet to the same child. Distinct packets
ignore one another's marks and collisions.

For F or B, a step to the parent produces B. A step to a fresh child produces
D if its mark is one, and F otherwise. A B step to its specified empty child
produces F without a sleeper mark.

For D, two backward steps produce D, forgetting the now known empty child.
Exactly one backward step produces B at the parent. At a forward target with
one arriving frog, produce F or D according to its sleeper mark. At a forward
target with two arriving frogs, produce D when its mark is zero and D plus F
when its mark is one. In the latter case there are three represented frogs;
splitting them into two packets only discards information and future
collisions. All offspring move one level in the indicated direction.

At the root use type R, one frog per packet. Each R steps to a uniform child
and produces F or D there with probabilities 1-q and q. When a non-root
packet's offspring arrive at the root, replace a B by one R and a D by two R.
Initially there is one R.

Here and below, fresh marks at visited vertices may create extra frogs; they
never remove an actual frog. For completeness, a coupling can be constructed
at every finite time as follows. Map actual frogs injectively to the individual
frog slots of upper packets, with a common position for actual frogs in a
packet. Extra slots are auxiliary frogs. Make the actual frogs use their
slots' independent step choices, with the same child labels within a packet.
If an actual vertex is first visited, choose the first packet with an actual
arrival there, in a fixed ordering of packets. Couple its fresh sleeper mark
to the actual vertex's sleeper. The selection uses arrivals, before these
marks are sampled, so that mark still has Bernoulli(q) law independently of
the past. Every other packet uses its own independent mark. Actual sleepers
can equivalently be sampled on first visit: no unvisited sleeper has affected
the process. This deferred sampling gives the prescribed independent initial
configuration.

At a previously visited vertex no actual sleeper needs a slot. At a virgin
vertex, the selected packet supplies the actual sleeper's slot if it exists.
Within a D packet the rules provide exactly enough slots for its arrivals and
its one possible sleeper. Across packets, extra marks only add slots. All B
packets containing an actual frog have a truly empty specified child. Empty
slots may be retained when a packet represents fewer actual frogs than its
capacity. Repeating the construction preserves these properties. Independent
future step choices preserve the law of the actual frogs' walks. This gives
the desired domination at every time, including at the root.

## 2. The mean matrix

Write s=d+1 and choose t>1. Give an interior packet of type i at height x the
weight v_i t^(-x), in the order F,D,B. Backward offspring acquire a factor t,
and forward offspring a factor 1/t, relative to the parent's level. The
weighted mean offspring matrix is

```
           F                         D                         B
F    d(1-q)/(s t)              dq/(s t)                       t/s
D    d[2d(1-q)+q]/(s² t)       d(2dq+1)/(s² t)+t/s²          2dt/s²
B    [d-(d-1)q]/(s t)          (d-1)q/(s t)                   t/s
```

Denote this matrix by M. The F row follows by separating the parent from d
fresh children. The B row separates the parent, one empty child and d-1 fresh
children.

For the D row, there are s² equally likely ordered direction pairs. Both
frogs go backward in one of them, giving D at displacement -1. Exactly one
goes backward in 2d of them, giving one B there. For each child, the
probability exactly one frog chooses it is 2(s-1)/s²=2d/s². Summed over d
children, the expected number of single-arrival forward targets is 2d²/s².
Each such target gives expected counts (1-q) F and q D. The probability of a
double-arrival forward target, summed over children, is d/s². It always gives
one D and gives one additional F with probability q. Adding these terms gives
the displayed D row. This accounts in particular for both frogs going to the
same child and for both going to the parent.

## 3. The reflecting root

Give each R weight c>0. Suppose

```
Mv < v componentwise,    c <= v_B,    2c <= v_D,
g := [(1-q)v_F + q v_D]/t < c.
```

For a packet above height one, its expected next weight is t^(-x)(Mv)_i.
At height one, backward offspring land at the root. The B replacement costs
c instead of v_B, and the D replacement costs 2c instead of v_D. The two
middle inequalities ensure that these replacements only decrease the weight
relative to the matrix calculation. A root R has expected next weight g.

Set

```
rho = max( (Mv)_F/v_F, (Mv)_D/v_D, (Mv)_B/v_B, g/c ) < 1.
```

Let W_n be the total upper-process weight at time n. The number of particles
is finite at every finite time, so conditional expectations may be added.
The preceding inequalities give

```
E[W_(n+1) | history through n] <= rho W_n,
E[W_n] <= c rho^n.
```

Let N_n be the actual number of frogs at the root at time n. The coupling
gives c N_n <= W_n. By summing nonnegative random variables,

```
E[sum_(n>=0) N_n] <= (1/c) sum_(n>=0) E[W_n] <= 1/(1-rho).
```

A nonnegative integer-valued extended random variable with finite expectation
is finite almost surely. This proves transience under the displayed
inequalities. Multiple initially active root frogs multiply the expectation
bound by their number.

## 4. Exact certificates

For d=3 choose

```
q = 41/100,  t = 41/20,
(v_F,v_D,v_B) = (203/200, 2, 483/500),  c = 483/500.
v-Mv = (1367/1640000, 1239/820000, 1777/1640000).
c-g = 11229/41000,   v_D-2c = 17/250.
rho = 1638761/1640000.
```

All three components of v-Mv, and c-g, are strictly positive. The equality
c=v_B and the positive pair margin check the height-one replacements.
The four ratios defining rho have the displayed maximum. Consequently the
expectation bound is 1640000/1239.

For d=4 choose

```
q = 33/50,  t = 51/20,
(v_F,v_D,v_B) = (1017/1000, 2, 483/500),  c = 483/500.
v-Mv = (1481/850000, 3173/796875, 1383/850000).
c-g = 3323/10625,   v_D-2c = 17/250.
rho = 273239/273700.
```

The same strict inequalities give expectation bound 273700/461.
Every number here is rational. The accompanying script computes these
fractions exactly and independently enumerates ordered directions and sleeper
marks to check the mean matrix, without using eigenvalues.

Finally, couple smaller q to the endpoint by deleting sleepers independently,
and use the same preassigned walk for every retained frog. The set of activated
frog paths can only decrease. Therefore transience and the same expectation
bound hold throughout the asserted intervals.

## 5. Comparison with the elementary bound

If all forward collisions and empty children are forgotten, a single interior
frog produces one backward frog with probability 1/s, or one plus an
independent Bernoulli(q) forward frog with probability d/s. Its expected
weighted offspring count is

```
m(t) = t/(d+1) + d(1+q)/[(d+1)t].
```

The minimum over t>0 is 2 sqrt[d(1+q)]/(d+1), at
t=sqrt[d(1+q)]. It is less than one exactly when
q < (d-1)²/(4d). For d=3,4 and 0<=q<=1, this minimizing t exceeds one and
the root ratio (1+q)/t=sqrt[(1+q)/d] is less than one, so the same weighted
argument also handles the root. Thus the elementary sufficient thresholds
are 1/3 and 9/16. The certified endpoint improvements are respectively

```
41/100 - 1/3 = 23/300,
33/50 - 9/16 = 39/400.
```

This comparison concerns these two sufficient tests. It does not compare
against every bound in the literature.
