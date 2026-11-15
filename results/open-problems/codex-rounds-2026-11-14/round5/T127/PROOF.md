# Applicability of the retrieved formal statements

This note checks the meaning of the definitions at commit
`d6b298c0100af57a8f46f8314eca8bf8f7eb4693` of mt0-svg/frog-model-tree.
It does not prove the imported recurrence and transience theorems or verify
their finite certificates. Local source paths below are relative to outside/.

## The graph and walks

In FrogModel/Defs.lean, Vertex d is the type of finite lists over Fin d.
The empty list is root. The adjacency relation joins v to c :: v for each
c in Fin d. Reversing each list identifies this with the usual tree whose
children append a letter. There are d distinct children of each vertex.
A nonempty list has exactly one parent, its tail; its parent has smaller
length and hence cannot be one of its children. The root therefore has
degree d, and every other vertex degree d+1.

A step variable is a pair (a,b) in Fin d × Fin(d+1), uniform on that finite
set. At the root, step chooses child a. For a fixed child, exactly d+1 of
the d(d+1) pairs choose it, giving probability 1/d. At a non-root vertex,
b=0 chooses the parent, and b=c+1 chooses child c. For each neighbor,
exactly d of the d(d+1) pairs choose it, giving probability 1/(d+1).
Thus the unused component of the pair introduces no bias.

The sample space gives a step variable to every pair (starting vertex,
step number). frogMeasure is the iterated product of their uniform laws.
Consequently all these variables are independent. The function paths
iterates step for each frog from its own starting vertex, using its own
sequence. Conditional on that frog's previous steps, its next step variable
is independent and uniform. The marginal kernel just computed proves that
each path is simple random walk, and the disjoint coordinate families prove
independence of the paths of distinct frogs.

## Activation and visits

For any fixed family of paths S, wake S 0 u is some 0 precisely at root,
and none elsewhere. At time t+1 an existing wake time is preserved.
Otherwise wake becomes some(t+1) precisely when an active frog w, with
wake time s, satisfies S w (t+1-s)=u. This is exactly a sleeping frog
being visited by a frog which moves during that step. Induction on t shows
that wake records the activation times of the usual synchronous frog model.
A newly awakened frog starts at its own path index zero, so it does not
take a walk step until the next time. Several arrivals activate a sleeper
only once because each starting vertex has a single wake entry.

The set visits consists of pairs (u,t) with t≥1, where frog u is active
and its path at elapsed time t-s is at root. Thus it counts all root
visits after time zero, including repeated visits by the same frog.
Omitting time zero cannot affect finiteness.

There are finitely many active frogs at each finite time. More explicitly,
starting with one frog, at most 2^t are active at time t: each active frog
can reach only one vertex in its next step and hence activate at most one
new frog. This proves the bound by induction. Consequently a finite set
of times accounts for only finitely many pairs in visits. Conversely a
finite set of visit pairs has a finite set of time coordinates. Infinitude
of visits is therefore equivalent to infinitely many root-visit times.

Transient d is the assertion that visits is finite almost surely under
frogMeasure d. In FrogModel/D3/Defs.lean, Recurrent d asserts that this
same set is infinite almost surely under the same measure. The measure is
a probability measure for d=3 and d=4, since each factor is a probability
measure. These are the required notions of transience and recurrence.

## An additional sleeping root frog

The formal definition has one active root frog and sleepers at non-root
vertices. If the task's words “one sleeping frog at each vertex and an
active frog at the root” include an additional root frog, that sleeper
wakes at time zero. This convention does not change either conclusion
claimed by the outside paper. Here is a pathwise comparison that proves
the assertion, conditional on those outside conclusions.

Fix the non-root frogs' paths and the two independent initial root paths
A and B. Form a directed graph on non-root starting vertices by drawing an
edge u→v whenever the path of frog u visits v. Also allow two seed symbols
A and B, whose outgoing edges are the non-root vertices visited by their
paths. All frogs follow their entire paths after activation.

A non-root frog is activated if and only if it is reachable from an initial
seed by a finite directed path. For the forward implication, trace its
activation backwards to an active visiting frog; activation times strictly
decrease until a seed is reached. For the reverse implication, induct along
a finite directed path: once a frog is activated, it reaches each specified
finite index of its own path at a finite time and activates the next frog.

Reachability from {A,B} is the union of reachability from A and from B.
Consider two single-seed systems using these same non-root paths, one
starting with A and the other with B. Their activated sets therefore have
union equal to that of the two-seed system. The activation times may differ,
but an activated frog contributes the same total number of root visits
along its path. With all counts excluding the initial time-zero positions,
the two-seed visit count is at most the sum of the two single-seed counts:
every activated non-root frog is counted in at least one single-seed system,
and each root seed is counted in its own system. The two single-seed systems
each have the standard model's marginal law; independence between systems
is unnecessary.

If the single-seed count is finite almost surely, both single-seed counts
are finite almost surely, so their sum and the two-seed count are finite.
If it is infinite almost surely, the A system alone contributes infinitely
many visits in the two-seed system. This proves applicability under either
root convention. No expectation estimate is needed for this comparison.

## What remains unchecked

The target files declare recurrent_three : Recurrent 3 and
transient_four : Transient 4, and the d=4 file also declares a mean bound.
Their displayed terms use imported assembly and data-checking theorems.
The definitions audited here express the intended model, but that does not
establish the correctness of those imported terms. A source-text comparison
with the independent challenge files confirms matching definitions; it is
not a substitute for a Lean build or comparator run.
