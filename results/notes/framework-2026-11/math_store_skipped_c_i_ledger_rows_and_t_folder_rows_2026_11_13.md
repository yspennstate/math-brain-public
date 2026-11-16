---
name: math_store_skipped_c_i_ledger_rows_and_t_folder_rows_2026_11_13
description: "[VERIFIED] Our own research results missing from the math store? 13 Nov: math_transport's program guard knew ledger ids d/e/f/p only and frontier rows only under frontier/rows/T###, so verified C####/I#### rows and rows worked in 06_math_research/t###_* folders (T104, T042, T115, T188, T197) read SKIP 'no result marker'. Fixed (md5 fbd0ca5e, origin verified): 26 memories SKIP->QUEUE, nothing else; 25 ingested, 1 already in."
metadata:
  node_type: memory
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T22:55:58+02:00
  status: verified
  evidence: "commits 3ce4bf53 (md5 fbd0ca5e) and 57bdc6c1 (md5 d1c7a26c), origin md5 checked; corpus diffs scratchpad combo_diff.py, amb_diff.py"
  modified: 2026-11-13T21:24:20.508Z
---

Found by an agent on 13 Nov 22:2x. Of 92 frontier memories filed that day, the classifier gave 4 AUTO, 8 QUEUE, 80 SKIP. Two causes: PROGRAM_LEDGER_ID was ^[defp]\d{4}_ though the campaign also files c#### and i#### rows; and frontier_row_known looked only for frontier/rows/T### (and an absent row-list file), while ten rows are worked in 06_math_research/[tT]###_* folders. Fix: ledger ^[cdefip]\d{4}_, and a row also counts when a 06_math_research/[tT]<num>_* folder exists. Corpus diff over every memory (scratchpad combo_diff.py): exactly 26 change, all SKIP->QUEUE, all research rows (c0033 x2, c0034, c0119, c0149, c0153, i0003 x2, i0004, i0070, i0071, i0092, t042, t104 x10, t115, t188, t197); no tenor tag moved, nothing became AUTO. Ingested with math_transport.py ingest-many (one rebuild). Still SKIP by design: provisional program memories without a result word in the head (most of the day's 'open, lit check' notes), i0103 on 'ETF' (equiangular tight frame) and c0134 on 'call'. Watch: a new campaign letter prefix (a, b, g...) needs adding to PROGRAM_LEDGER_ID; a new t### work folder is picked up automatically.

Second fix, 13 Nov 23:2x (commit 57bdc6c1, md5 d1c7a26c): AMBIGUOUS_DENY gained call, puts?, etf, borrowing. Census of program memories refused on a deny word: 143, 66 verified, most of them rightly (film logs, campaign indexes, a 'benchmark session'). Per-word corpus diff over program memories: the four words together move exactly six research rows (c0134 'the author's call', i0103 Paley ETF, p0143 'simulations put the mean', p0434 Gittins 'borrowing', t248, a FEI lit note); 'memory' moved 7 and 'brain' 12, among them campaign process notes, so both stay hard. Ingested c0134, i0103, p0143, and with --force t348 Gaussian dense memory (blocked by 'memory'). p0434's memory is overtaken; its successor p0434_residence_lemma_p_false_zp_1_51_three_paths and t217 (blocked by the repo name research-repo) were already in the store, carried earlier by hand, so a SKIP verdict does not mean a memory is absent: check done_slugs before calling one dark. Night total: 29 research results newly in the store. A whole-corpus diff of seven classifier passes runs past 290 s on a loaded laptop: restrict it to slugs with program_of() true, the only ones the guard can move. Related: [[math_transport_beta_ambiguous_deny_t012_t016_2026_11_13]]
