# Probability literature proof bank: tools

These are the tools that built and graded the probability literature bank (PLIT), the first of the two literature
proof banks. Theorem and proof pairs were taken from the LaTeX sources of 2026 arXiv papers in probability, split
into numbered steps, and either left as written or given one changed step by a mutation operator. A solver reads
each item and says whether the proof is sound and, if not, which step fails. The multi-domain bank
(mdlit-multidomain-bank-2026-09-06) is the sibling built the same way outside probability.

| file | what it does |
|---|---|
| extract_proofs.py | finds the main file of each paper, inlines its inputs, and pairs each theorem or lemma with its proof as numbered steps |
| mutate.py | the mutation operators: each changes exactly one step (a dropped hypothesis, a reversed inequality, a wrong constant, a scope change and so on) and records what it changed |
| pairing_audit.py | checks that every proof is paired with the statement it proves (labels, references, step overlap) |
| plit_notes_bm25.py | builds the BM25 index of notes served to the brain arm, and the receipt of what each item was served |
| run_plit_wrapper.py | runs one solver arm over the bank with fixed prompts, effort and timeouts, and records every artifact |
| grade_plit.py | grades the verdicts against the sealed keys: verdict accuracy, step location, and a descriptive check of whether the stated reason names the changed text |

The sources of these files were lost from disk after the run; only their compiled bytecode survived. They were
rebuilt from the edit history in the session records. Five of the six (grade_plit, mutate, pairing_audit,
plit_notes_bm25, run_plit_wrapper) compile to code objects identical to the surviving bytecode: same instructions,
names, constants and line table. extract_proofs.py is the closest surviving copy and differs slightly from the
bytecode (16 bytes in a file of 26,283). Local paths read `<HOME>` and item identifiers read `<item>`; with those
strings put back the five match exactly.

The folder holds no items, no keys, no solver outputs and no per-item notes.
