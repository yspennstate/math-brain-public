# Rights in this repository

The code under `src/`, `tools/`, `agent_tools/` and `tests/`, and the documentation written for this repository, are released under the MIT licence in `LICENSE`, copyright Yitzchak Shmalo.

The card store in `export/population/` mixes original work with material taken from published sources. Each card records its origin in the `source_id` field of `metadata_json` in `nodes.jsonl`. The prefix of that field determines the terms.

| `source_id` prefix | cards | origin | terms |
|---|---:|---|---|
| `wikipedia:` | 1,766 | lead sections of Wikipedia articles, summarised or quoted | CC BY-SA 4.0. Attribution is the article named in `source_id`; `source_revision` records when and how the text was read (for example `rest-summary-2026-08-02`); it is not a page revision number, and 18 cards have none. A card derived from this text is shared under the same licence. |
| `proofwiki:` | 378 | ProofWiki pages | CC BY-SA 3.0, attributed to the page named in `source_id`. `source_revision` is a read date in the same sense; 10 cards have none. |
| `arxiv:` | 2,613 | statements of results in arXiv papers, with the paper's identifier | Copyright in the papers stays with their authors. A card gives the statement of one result with its citation; it does not reproduce the paper. Anyone reusing the statements should cite the paper given in `source_id`. |
| every other prefix | 8,581 | statements, proofs, attempts and links written in the course of this project | MIT, as the code. |

A card with no `source_id` is original to this project.

The CC BY-SA cards keep that licence in this copy; the MIT licence does not override it.
