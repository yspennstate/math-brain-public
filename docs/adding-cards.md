# Adding cards to the store: the draft bundle

New definitions, lemmas, theorems and concepts enter the store as draft bundles. A contributor, human or agent, writes
plain JSON; `tools/integrate_drafts.py` checks it, computes the digests and source manifests, seals the entries and
ingests them. A contributor never computes a digest and never writes to the store directly.

## Where a bundle goes

Each contributor has a folder in the inbox, and each bundle is one file in it:

    <inbox>/<contributor>/bundle_<NNN>.json

The inbox is `math-brain-inbox` beside the repository, or the folder named by `MATH_BRAIN_INBOX`. The integrator
reads `<inbox>/BUNDLE_SPEC.md` and records its digest with every bundle it ingests, so a copy of this page belongs
there under that name. Write a bundle under a `.part` name and rename it to `.json` only when it is complete; the
integrator ignores `.part` files. A bundle holds at most 200 entries; a contributor may write any number of bundles.

## The shape

```json
{
  "spec": "mathbrain-draft-v1",
  "author_agent": "<contributor>",
  "bundle_slug": "algebra-core-001",
  "entries": [
    {
      "key": "def-group",
      "namespace": "algebra.groups",
      "logical_name": "group-definition",
      "kind": "definition",
      "title": "Group",
      "statement": "A group is a set G with a binary operation * such that: the operation is associative; there is an identity element e with e*g = g*e = g for all g in G; every g in G has an inverse h with g*h = h*g = e.",
      "proof_text": null,
      "assumptions": [],
      "domain": "abstract algebra",
      "source": {
        "source_id": "proofwiki:Definition:Group",
        "url": "https://proofwiki.org/wiki/Definition:Group",
        "revision": "as-read-2026-08-02",
        "license": "CC-BY-SA-4.0",
        "excerpt": null
      }
    },
    {
      "key": "thm-lagrange",
      "namespace": "algebra.groups",
      "logical_name": "lagrange-theorem",
      "kind": "theorem",
      "title": "Lagrange's theorem",
      "statement": "If G is a finite group and H a subgroup of G, then the order of H divides the order of G.",
      "proof_text": "The left cosets of H partition G and each coset has exactly |H| elements, via the bijection h -> gh. Hence |G| = [G:H] |H|.",
      "assumptions": ["G is a finite group", "H is a subgroup of G"],
      "domain": "abstract algebra",
      "source": {
        "source_id": "proofwiki:Lagrange's Theorem (Group Theory)",
        "url": "https://proofwiki.org/wiki/Lagrange%27s_Theorem_(Group_Theory)",
        "revision": "as-read-2026-08-02",
        "license": "CC-BY-SA-4.0",
        "excerpt": null
      }
    }
  ],
  "relations": [
    {"from_key": "thm-lagrange", "to_key": "def-group", "kind": "depends_on",
     "rationale": "Lagrange's theorem is stated for groups"}
  ]
}
```

## The rules the integrator enforces

1. `kind` is one of `definition`, `lemma`, `theorem`, `concept`. A lemma or theorem needs a `proof_text` of at least
   twenty characters: a correct sketch of the main idea is enough, an invented one never is. A definition or concept
   carries no proof text. There is no open-problem kind: an open problem is a concept titled `Open problem: ...`.
2. `statement` is complete and self-contained, at least twenty characters, in plain text or light LaTeX. No truncation
   and no "see source". This is the text an agent will be handed in the middle of a proof, so write it the way you
   would want to receive it there.
3. `namespace` is a dotted lowercase area path (`analysis.measure`, `probability.concentration`,
   `combinatorics.designs`) and `logical_name` a meaningful lowercase-kebab name (`fundamental-theorem-of-algebra`,
   not `thm1`). Keys and logical names are unique within a bundle.
4. Every entry has a `source` with `source_id`, `url`, `revision` and `license`. The license must begin with one of
   `cc-by-sa`, `cc-by`, `cc0`, `apache-2.0`, `gfdl`, `public-domain`, `mit`, `arxiv-nonexclusive` or `owner-own-work`
   (the last for results of the store's own authors: papers in progress, campaign proofs, refuted routes). A note may
   follow the tag, so `owner-own-work (attributed, not reproduced)` passes and `author's own work` does not. Open
   sources that fit: ProofWiki, Wikipedia, the Stacks Project, nLab, Metamath, the Open Logic Project, the mathlib4
   documentation, arXiv papers under a licence that allows it, and public-domain texts.
5. Statements are in the contributor's own words. A mathematical fact is not copyrightable, long verbatim prose is;
   keep any `excerpt` short and attributed.
6. `relations` join keys of the same bundle, with kinds `depends_on`, `defines`, `proves`, `refutes`, `generalizes`,
   `specializes`, `analogous_to`, `cites` and `semantic_association`; `depends_on` must be acyclic within the bundle.
   To link to a card already in the store, give `"to_existing_logical": "math:<namespace>:<logical_name>"` in place
   of `to_key`. A target that does not resolve is skipped with a note, never fatal.

## Correctness first

A wrong statement in the store is worse than a missing one, because it will be put in front of an agent reasoning
live. When unsure of the exact hypotheses (does the theorem need completeness, sigma-finiteness, a compact support?),
include them: an over-hypothesized true statement is acceptable, an under-hypothesized false one is not.

## Running the integrator

    python tools/integrate_drafts.py --only <contributor>

Run it inside the store's write lease, then read what it prints. A bundle it refuses gets a `REJECTED` line and a
`.rejected-note` file beside the draft listing every reason; nothing from that bundle is ingested. Read the result
every time. A licence string that starts with the wrong word is enough to leave a bundle sitting in the inbox,
unnoticed, for days.

Take the lease for an hour, not a few minutes. After ingesting, the integrator refreshes the derived indexes, which can
take ten minutes or more on a busy machine, and a run that outlives its lease leaves the store open to a second writer
partway through; after a rejection, take the lease again before retrying. The lease has to cover the whole store, the
database file included. Each bundle is sealed to the store's state at approval and checked against it at ingest, so
another writer changing the store in between gets the bundle rejected, with its file name already spent in the ledger.

Two behaviours catch people out. The integration ledger records every draft it has looked at by file name, rejected
ones included, so a rejected bundle corrected in place is skipped without a word on the next run; save the corrected
draft under a new name (`bundle_017b.json`) and integrate that. And the integrator reads the store's existing cards
once, at the start of a run, so a draft that cites by `to_existing_logical` a card landing in the same run has that
edge skipped as `xrel-unresolved` even when the name is right; land the cited bundle first and the citing one in a
second run. A wrapper script that stops before it copies the bundle into the inbox (a failed lock or lease check, for
instance) has landed nothing, whatever its own log says: the ledger line for the draft is the evidence.

## When to write a new card instead of a link

Most gaps in the store are missing links, not missing cards (see [linking-the-store.md](linking-the-store.md)).
Search for a card on the same object first. Write a new concept card when nothing in the store is about the subject;
link it to the cards it uses with `to_existing_logical`, and it can serve at once as the hub other papers on that
subject reach.
