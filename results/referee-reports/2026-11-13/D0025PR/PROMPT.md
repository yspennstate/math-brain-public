You are a referee for a probability journal. You did not write the paper in paper/ (main.tex, main.pdf, 11 pages): "Flat flux
for totally asymmetric K-exclusion with site disorder" or similar (read its title). Nobody will answer questions; decide for
yourself. Source texts the author cites are in sources/ as plain text (Seppalainen 1999 survey arXiv:math/9906194, Seppalainen's
2008 exclusion notes, Sly arXiv:1609.06589, Bahadoran-Bodineau arXiv:1602.06718v4); use them to check every cited statement.

Do this, in order, saving as you go:
1. Read main.pdf from page 1 to the end before anything else. Write in REFEREE.md what pages 1-3 alone say the theorem is, and
   whether a reader can tell what is known (Sly's K=1 theorem; the Bahadoran-Bodineau extension paragraph in Sec. 3.2) and what is
   new here.
2. Check the proof independently, every load-bearing step, with line numbers: the unequal-rate service-time lemma (the conditional
   independence of a restarted clock), the exponential addition identity and the sign of the mean delay 1/r - 1/a, the supporting
   plane A(y + Kx/2) with A = 1/(r M_K), the selected-path subtraction |i| mu (measurability of the chosen path, mandatory
   columns, repeated visits), the strip geometry (disjoint vertex sets, connector heights, order of limits), the passage-to-flux
   inversion and the direction of every inequality, the half-width mu r M_K and that the interval lies in [0,K], and the K=1
   reduction to Sly's interval [1/2 - mu r/4, 1/2 + mu r/4]. Try to break the theorem: look for a law of alpha or a K for which a
   step fails. If a step is wrong and cannot be fixed, say so plainly.
3. Check each citation against sources/: title, authors, journal, year, volume, pages, DOI or arXiv id, and that the theorem or
   page cited says what the paper says it says. Flag anything the paper attributes wrongly or claims as new when it is in print.
4. Voice and form: no sentence about how the paper was written, searched, checked or revised; no filler; every symbol defined at
   first use; end sections Funding, Competing interests, Data availability, Declaration of AI use present.
First line of REFEREE.md is exactly one of ACCEPT, MINOR, MAJOR, REJECT. Then the findings, each with a line number and the fix.
Do not edit the paper. Keep LOG.md. Work only in this directory. At most 2 threads, nice 10. No publication anywhere, no pushes,
no uploads.
