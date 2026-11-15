# A four-type transience comparison

Let T_d be the rooted d-ary tree. There is one active frog at the root.
Every other vertex independently contains one sleeping frog with probability
q and no frog otherwise. Active frogs perform independent simple random
walks and activate sleepers on arrival. Let V be the total number of root
visits, counting every frog at the root at every integer time, including
time zero.

**Proposition.** The following bounds hold:

| d | Range of q | Upper bound for E[V] |
|---|---|---|
| 3 | 0 <= q <= 419/1000 | 155982888000/2349271 |
| 4 | 0 <= q <= 337/500 | 32481964500/2275273 |

In particular the model is transient almost surely in these ranges. An
additional frog at the root multiplies the expectation bounds by two.

The endpoint probabilities exceed 41/100 and 33/50, respectively, by
9/1000 and 7/500. These are bounds for Bernoulli sleepers. They give no
conclusion for the initial configuration with one sleeper at every site.

## 1. Packets and their transitions

A packet contains one or two frog slots at the same vertex. Away from the
root its type is one of the following, in the indicated order:

1. F: one frog, with no remembered child.
2. D: two frogs, with no remembered child.
3. B: one frog, with a specified child containing no remaining sleeper.
4. E: two frogs, with a specified child containing no remaining sleeper.

The parent is treated as empty in every type. This is valid for actual
frogs: any visited vertex other than the root was first reached from its
parent, so that parent was visited already. A child from which an actual
frog has just returned also has no remaining sleeper. Here empty refers
to sleeping frogs; active frogs may be present.

Each slot independently chooses a uniform neighbor. Each distinct child
target not remembered empty receives a fresh independent Bernoulli(q)
mark. A child remembered empty receives mark zero. Marks at the same target
within a packet are shared. Marks belonging to distinct packets are
independent, even if those packets choose the same physical vertex.

The output at the parent, when there is one, is B for one backward-moving
frog and E for two backward-moving frogs. In either case the specified
empty child is the vertex just left. Previous remembered information is
discarded.

At a child target, add its mark to the number of arriving slots. One slot
produces F; two slots produce D; three slots produce D and F. No child
information is retained in these forward outputs. Thus two frogs choosing
the same fresh child create only one extra frog if its mark is one. Two
frogs choosing distinct fresh children use independent marks. Collisions
between different packets are ignored.

At the root use one type R, with one slot per packet. An R packet steps to
a uniform child and produces F or D with probabilities 1-q and q.
Backward outputs at the root are replaced by one R for B and two R for E.
There is initially one R.

Compared with the three-type construction, the only change is that a pair
moving to its parent retains the empty child as E. Its later visits to
that child create no sleeper.

## 2. Domination of the frog model

At each integer time, inject actual active frogs into upper-process slots
at the same positions. Use the slot's next direction for its assigned
actual frog. All slots make independent choices conditional on the past.
The allocation of an actual frog to a slot occurs before that slot's future
choices are sampled, preserving the independent walk laws.

Actual sleepers can be sampled on first visit. Before that visit their
values have influenced no move or activation, so these samples are
independent Bernoulli(q) variables. This construction has the same law as
sampling all sleepers at time zero.

After directions at a transition have been chosen, consider any actual
vertex that is visited for the first time. Select the first upper packet
with an actual arrival there in a fixed ordering. The choice uses only
directions and previous information. Its target cannot be a parent or a
remembered empty child: for a packet carrying an actual arrival those
vertices were already visited. Hence this packet has a fresh mark there.
Use that mark for the actual sleeper. The mark has Bernoulli(q) law
independently of the past and of the selection. Give the awakened actual
frog one of the extra output slots.

If several actual frogs arrive together, the selected packet supplies the
single sleeper slot needed. The other packets' marks only add auxiliary
slots. At a previously visited vertex there is no sleeper to accommodate.
Within one packet the number of outputs equals the number of arrivals plus
its mark, including the three-slot case, where D and F provide three slots.
All arriving actual frogs therefore retain slots.

Whenever a B or E packet carries any actual frog, its specified empty child
was actually visited: that actual frog just left the child on the backward
move that created the packet. If a packet carries only auxiliary frogs,
its remembered child need not have been visited by an actual frog. An
auxiliary-only packet and its descendants remain auxiliary-only under this
allocation rule: assigning an actual sleeper requires an actual arrival
from that packet. Thus its remembered child has no bearing on actual
frogs. Forward outputs discard the old memory, and any new B or E memory
comes from the vertex just left. Root replacements preserve all actual slots.

Induction over time gives the injection at every finite time, with every
required empty-child invariant. A packet has at most four output slots, so
the upper process is finite at every finite time. This completes the
coupling.

## 3. Weighted mean matrix

Write s=d+1 and choose t>1. At height x>=1 give a type i packet weight
v_i t^(-x), where all four coordinates of v are positive. The weighted
mean offspring matrix, with rows and columns in the order F,D,B,E, is

```
M =
[ d(1-q)/(st)                   dq/(st)                    t/s        0     ]
[ d[2d(1-q)+q]/(s^2 t)          d(2dq+1)/(s^2 t)           2dt/s^2    t/s^2 ]
[ [d-(d-1)q]/(st)               (d-1)q/(st)               t/s        0     ]
[ [2d^2-(d-1)(2d-1)q]/(s^2 t)  [d+2d(d-1)q]/(s^2 t)    2dt/s^2    t/s^2 ]
```

A backward output gains a factor t and a forward output a factor 1/t
relative to its source height.

For F, the parent direction has probability 1/s and produces B. The d
child directions produce F and D with probabilities 1-q and q. For B,
one of those d children has mark zero, giving the displayed third row.

For either two-slot type, both frogs choose the parent in one of the s^2
ordered direction pairs. This produces E with weighted coefficient t/s^2.
Exactly one chooses the parent in 2d ordered pairs, giving B with
coefficient 2dt/s^2.

Fix a child. Exactly one frog chooses it with probability 2d/s^2, and both
choose it with probability 1/s^2. For a fresh child, its F contribution is
[2d(1-q)+q]/(s^2 t), and its D contribution is (2dq+1)/(s^2 t).
There are d such children for D, proving its forward entries.

For E, there are d-1 fresh children and one empty child. The empty child's
F and D contributions are 2d/(s^2 t) and 1/(s^2 t). Therefore its total F
numerator is

```
(d-1)[2d(1-q)+q] + 2d = 2d^2-(d-1)(2d-1)q,
```

and its D numerator is

```
(d-1)(2dq+1)+1 = d+2d(d-1)q.
```

These prove all matrix entries without spectral approximation.

## 4. The root and finite expected visits

Give each R weight c>0. Suppose

```
Mv < v coordinatewise,
c <= v_B,     2c <= v_E,
g := [(1-q)v_F+q v_D]/t < c.
```

There are no D backward outputs in this four-type process. The additional
inequality 2c<=v_D, satisfied below, is harmless but is not needed.
For an interior packet at height greater than one, the expected next
weight is t^(-x)(Mv)_i. At height one, replacing B by R costs c instead
of v_B, and replacing E by two R costs 2c instead of v_E. Thus the same
upper bound applies at height one. The expected next weight from one R
is g, since every one of the root's d children has the same mark law.

Define

```
rho = max(g/c, (Mv)_F/v_F, (Mv)_D/v_D, (Mv)_B/v_B, (Mv)_E/v_E).
```

The strict inequalities imply rho<1. Let W_n be the total upper weight
at time n, and N_n the actual number of frogs at the root at time n.
The coupling and the root weight give c N_n<=W_n. Conditional expectation
and the packet bounds give

```
E[W_(n+1) | history through n] <= rho W_n,
E[W_n] <= c rho^n,
E[V] = sum_(n>=0) E[N_n] <= sum_(n>=0) rho^n = 1/(1-rho).
```

The sums are justified by nonnegativity. A nonnegative extended random
variable of finite expectation is finite almost surely. This proves
transience whenever the inequalities hold. With two initially active
root frogs the same argument starts from W_0=2c.

## 5. Exact certificates

For d=3, take

```
q = 419/1000, t = 51/25,
v = (1022057/1000000, 2, 971841/1000000, 382311/200000),
c = 382311/400000.
```

Direct rational multiplication gives

```
v-Mv = (210439/13600000000,
        1656539/54400000000,
        101517/6800000000,
        2349271/81600000000),
c-g = 517970983/2040000000,
v_B-c = 32127/2000000,
v_E-2c = 0.
rho = 155980538729/155982888000.
```

Every slack in v-Mv is positive. The maximum defining rho occurs in
the E row. The visit bound is 155982888000/2349271.

For d=4, take

```
q = 337/500, t = 127/50,
v = (511527/500000, 2, 971203/1000000, 1906179/1000000),
c = 1906179/2000000.
```

Rational multiplication gives

```
v-Mv = (2275273/31750000000,
        22341133/158750000000,
        2160033/31750000000,
        21335453/158750000000),
c-g = 369665863/1270000000,
v_B-c = 36227/2000000,
v_E-2c = 0.
rho = 32479689227/32481964500.
```

Every slack is positive. Here the maximum defining rho occurs in the
F row, giving the visit bound 32481964500/2275273.

The script four_type.py verifies each entry in three ways: the displayed
formula, summation over ordered directions with analytically integrated
marks, and enumeration of every ordered direction pair and every Bernoulli
mark at its distinct fresh targets. It also checks total weighted frog-slot
counts, the root replacements, and rho from both outgoing ratios and
normalized slacks. All certificate arithmetic uses fractions.

Finally, use the same preassigned paths for retained frogs while deleting
sleepers independently to reduce q. Every frog activated in the reduced
configuration is activated in the larger one. Its path begins no earlier
in the reduced configuration, but its total number of root visits is the
same once activated. Hence the total visit count can only decrease.
The endpoint bounds therefore hold for all smaller q.

For q=1 each of these two particular vectors has negative slack in all
four rows. No conclusion about recurrence or transience at q=1 follows.
