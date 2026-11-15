# Referee task: Sections 3 and 4 of paper_c.txt (a preprint on Hilbert's tenth problem over Q)

You are an independent referee. The file paper_c.txt in this folder is the text extraction of a preprint. Read
Section 3 (about lines 738-1100) and Section 4 (lines 1101-1861) line by line.

For every lemma, proposition and displayed estimate in those two sections:
1. Re-derive each step yourself. Where a step is a computation (a genus, a degree, a valuation, a ramification count,
   an exponent), recompute it, by hand or with a short Python script in this folder.
2. Check each cited external theorem against the form in which it is quoted, and say whether the hypotheses used are
   the ones the cited result needs (name the result and what you checked; say plainly when you check from memory).
3. Classify each item as HOLDS, MISPRINT (harmless, say the corrected form), or GAP (a step that does not follow;
   state exactly what is missing and whether you can repair it).

Write REFEREE.md in this folder: one section per lemma or proposition with its classification and the reason, then a
final verdict on whether Sections 3 and 4 prove what the paper says they prove. Append a line to LOG.md after each
lemma so the work survives a crash. Text extraction artefacts (broken symbols, swapped columns) are not gaps: restore
them from context and say so.

Rules: do not search the web; do not edit paper_c.txt; no subagents; at most 2 worker processes and 1 GB of memory.
Normal speed only.
