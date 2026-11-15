---
name: pdftotext_drops_overlines_look_at_the_page_2026_11_12
description: "Identity typed from pdftotext output fails a numerical test on a clean fraction of cases (here 146 of 227)? Look at the PDF page first: pdftotext drops overlines (complex conjugates), hats and tildes. NT01 Lemma 4.1 (Gauss sums over Q(sqrt(-3)), 5 Oct 2026 preprint) passes 227 of 227 as printed"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T05:32:04+02:00
  status: verified
  evidence: "06_math_research/nt01_quasi_rh_agent_2026_11_12/NT01_CHECK.md, nt01_check.out, nt01_check_asextracted.out; push 7d580569c6c114f9bdb49f92a2fc054e809146df"
---

Checked on 12 Nov 2026 while testing Lemma 4.1 of the 5 Oct 2026 preprint on Hecke L-functions over Q(sqrt(-3))
(open-problem row NT01; folder 06_math_research/nt01_quasi_rh_agent_2026_11_12).

What happened. The lemma's Gauss-sum identities were typed into a test from the pdftotext output. Three of them
((4.2b), (4.4), (4.5)) held for 81 of 227 values of n and failed for the rest. That looked like an error in the
paper. It was not: pdftotext drops overlines, and the printed page has G(n) = conj(chi_n(4)) gamma_3(n) and
conj(alpha(n)) in (4.4) and (4.5). With the bars, every identity holds in all 227 cases and all 168 pairs, and
three planted wrong forms fail as they should.

How the lost bar showed itself before the page was opened:
- the two extracted identities contradicted each other unless alpha^2 = 1 ((4.2b) gave gamma_1 gamma_2 = mu alpha G
  and (4.4) gave alpha gamma_2 gamma_1 = mu G);
- the failures were not random: the identity held exactly when chi_n(4) was real (about a third of cases), which
  is the signature of a missing complex conjugate;
- a derivation from a standard formula (the duplication formula for Gauss sums) gave the conjugate form.

Rule. When an identity taken from extracted PDF text fails a numerical test, look at the page (Read tool with
pages) before writing that the paper is wrong. Overlines, hats, tildes and some primes do not survive
pdftotext; superscripts survive as trailing digits. A pass rate near 1/2 or 1/3 with a clean pattern points at a
lost conjugate or sign, not at a false lemma. Test both readings and keep both outputs.

Result for the row: Lemma 4.1 (4.1) to (4.6) confirmed numerically as printed; (4.7) and the analytic sections
are not checked; the zero-free half-plane claim stays unconfirmed. See NT01_CHECK.md.
Related: [[lo05_h10_over_q_openai_preprint_section5_checked_2026_11_12]],
[[nt02_landau_siegel_zeros_excluded_proof_read_in_full_2026_11_12]].

