# Linking the store: from one card in five to nine in ten

On the morning of 28 October 2026 the store held about 90,600 nodes, and only about 16,300 of them touched an edge.
The largest connected piece held 8,654 nodes (9.9 percent). A walk from a card the search found could go almost nowhere,
so most of what a graph walk is for (the definition a lemma uses, the paper a result came from, the other paper that
proves the same thing) was out of reach. Over the next three days the cards were linked in rounds. By the 42nd round
90,679 of 90,893 nodes touched an edge and the largest component held 82,756 of them (91 percent).

## The routine every round followed

1. Stage, do not write. A round builds its edges into a staging folder from a read of the live store and predicts the
   component sizes it will produce. Nothing touches the store yet.
2. Read a sample by hand. Each round's sample was read edge by edge before landing (16 of 16, 25 of 25, 40 of 40 on
   the rules that held; 26 of 30 on the weakest one that was kept). A rule that fails its sample is cut back or dropped.
3. Land under the store's write lease, once the hourly export has released its read lock, and write the id of every
   landed edge to a list. Retracting that list undoes the round exactly.
4. Verify after landing that every listed id is present and none is retracted, and count the components again.

Edges carry the store's own relation kinds and weights: `cites` for a card and its paper, `depends_on` (0.5 to 0.6)
where one card uses another's object, and `semantic_association` (0.4) where two cards are about the same thing.

## Rounds 1 to 4: every card to its own paper

The first rounds were deterministic. Every harvested card got a source node for its paper and a `cites` edge to it
(3,396 source nodes, 71,508 edges). Inside a paper, a card that uses a multi-word term another card of the same paper
defines got a `depends_on` edge (5,456 edges; about 26 of 30 right in the sample, which is why single-word terms were
left out). Cards naming the same concept got 325 associations, and a card naming another paper's arXiv id got a
`cites` edge to that paper (437).

After these, 87,244 nodes touched an edge, but the largest component had only doubled, to 18,144 (20.0 percent).
Rounds 1 and 2 alone would have left it at 10.4 percent. Within-paper links make one island per paper. Only links
between papers make the store walkable, and every later round was about those.

## Rounds 5 to 10: from papers to the general cards

Rounds 5 to 8 reached 2,925 of the 3,178 cards still alone, with 3,385 edges and 153 more sources. Round 9 linked a
card that names a result by name (a named theorem, inequality or lemma) to the store's general card on that result:
1,577 edges, 16 of 16 right, and the largest component went from 20.4 to 30.3 percent.

Round 10 was the large one. A harvested card that uses a multi-word concept the store defines in general got a
`depends_on` edge to the general definition (11,377 edges), and a paper whose title names such a concept got an
association from its source node (7,617). Samples of 25 and 12 were all right. Staged, this one round was predicted to take the
largest component from 27,492 nodes to about 72,300. The general definitions act as hubs: thousands of papers that never cite
each other all use "Brownian motion" or "Sobolev space", and through the hub card they become two steps apart.

Rounds 11 to 25 extended the term and hub tables of rounds 9 and 10.

## Rounds 26 to 31: what the matcher was missing, and where rules get unsafe

Round 26 found that the hub table keyed only each hub's own singular title, so titles saying "random walks",
"branching processes" or "stochastic differential equations" never reached hubs the store already had. Adding plural
forms and folding accents staged 56 links; reading them dropped 3 that used the right words in another sense
("compactness theorem" for Rellich-Kondrachov rather than the theorem of logic, "absolute continuity" in its spectral
sense). When a probe says a link is missing, check whether the card is missing or only the match.

Round 28 used the "Classical toolkit of <title>" cards, which summarise the standard tools a paper relies on and
already sat in the main component. A result card whose title is exactly that paper's title, when the toolkit card names
the same arXiv id and only one result card has the title, got a `depends_on` edge to its toolkit card. 1,145 edges,
40 of 40 right, and the largest component went from 87.1 to 88.5 percent.

Rounds 29 and 31 are the warning. Linking island papers to harvested definition cards of a concept their title names
was wrong one time in four: "survival probability" went to a dice-sum definition, "partition function" to the total
mass of one pinning model. Each paper defines its own model's version of a generic quantity, so a harvested definition
is a usable hub only for a named object (last passage percolation, the directed landscape, a Stein kernel). Matching
the same table against card statements instead of titles was worse, about one wrong in two: 178 staged, 81 left after
a stoplist of per-paper quantities (free energy, invariant measure, hitting time, weak solution, and others), and 39
kept after reading every one. At that rate the rule is only a list of candidates, and every edge has to be read.

## Rounds 32 onward: the last islands by hand

The islands left after that were single papers whose subject no table reached. For these, searching the main
component's card titles for the paper's subject phrase found a card on the same object within a minute, and one or two
hand-picked edges joined each island (Watson's lemma to Laplace's method, a Rosenthal inequality for random tensors to
the matrix Rosenthal inequality, a coherence lemma for credences to the cone form of Farkas' lemma). This beat writing
another rule.

When nothing in the store was about the island's subject, the island was joined through a new concept card, written
the way any contributor adds one: a draft bundle in the inbox, in the contributor's own words from an open-licensed
source, with relations to existing cards, ingested by `tools/integrate_drafts.py` under the write lease. The cards
written this way include multiple zeta values and their q-analogues, the score-function gradient estimator, the
compressible Euler equations, Orlicz spaces with the Luxemburg norm, the Allen-Cahn equation and De Giorgi's
conjecture, and log-crystalline cohomology with the Hyodo-Kato isomorphism. A new card can become a hub at once: the
multiple-zeta card made for one island was the target for a second island the same day.

Some islands were paper sources known only by their arXiv identifier, with no title to match on. The real titles were
fetched from the arXiv export interface (355 of 355), and 20 were checked by hand against the island's own claim cards,
all agreeing in subject. They could not be written into the nodes. A node's identifier is a digest of its content, the
store's state digest covers it, and nodes are only ever inserted, so a changed title would be a different node. The
fetched title, authors and year went instead into the metadata of the edges that joined each island, where they can be
retracted by edge id like any other link. Of the 355, 242 were already in the main component and 109 named no subject
any card covered; those titles (neural networks, gradient descent, the neural tangent kernel, in-context learning,
Levy processes) are a list of concept cards still to write.

Finding a target card by its title is the step these rounds repeat most, and the store itself is the slow place to
do it. A title search straight over the store's database, about 91,000 nodes with no index on titles, did not finish
in ten minutes on a machine whose disk other jobs were using. The same search over the prepared state that recall
already keeps on disk answered in about two seconds: it holds every node's id, kind, title and body, and its edge list
gives each node's degree, so islands and their likely hubs can be listed together. It has to run at normal priority.
At low priority the same 30 MB read was starved past ten minutes, against under nine seconds in the foreground. The
prepared state is a snapshot from its last build and can lag the store, so every target found this way was confirmed
against the live store before an edge was landed. Round 73 used it to join the last 40 claims that touched no edge,
with 79 edges, each picked and read by hand.

## Numbers

| after round | nodes | touching an edge | largest component | share |
|---|---|---|---|---|
| before (28 Oct) | 90,592 | about 16,300 | 8,654 | 9.9% |
| 4 | 90,596 | 87,244 | 18,144 | 20.0% |
| 8 | 90,792 | 90,546 | about 18,500 | 20.4% |
| 9 | | | 27,492 | 30.3% |
| 27 | 90,842 | 90,623 | 79,096 | 87.1% |
| 30 | 90,847 | 90,628 | 80,914 | 89.1% |
| 35 | 90,863 | 90,649 | 81,992 | 90.2% |
| 42 | 90,893 | 90,679 | 82,756 | 91.0% |

The store had 127,881 edges after round 42. The work continues one island at a time; after round 42 no island
other than the main one had more than 35 nodes.

## What carries over to another field

- Link every record to its source first, but expect that to make islands, not a graph.
- The links that make a store walkable are to general hub records. A field brain needs its definitions written as
  records in their own right, so that papers, tickets or shots that never mention each other share a neighbour.
- Match plurals and accents before concluding a hub is missing.
- A generic name is not an object. Rules that link by a generic name need every edge read.
- Keep every landed edge id, so a round that turns out wrong can be taken back whole.
