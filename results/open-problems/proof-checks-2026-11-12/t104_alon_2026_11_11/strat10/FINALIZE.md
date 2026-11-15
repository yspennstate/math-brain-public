Stop the N=6 box-splitting ledger now: past 68,000 visits the OPEN count only grows (4,053 and rising), as expected,
because region (11) touches T=0 at the corner r=a=1 (your pressure family). More splitting cannot close it.
Finalize instead, in this order, saving as you go:
1. Record the final ledger totals you have (visits, positive, excluded, open, split) in RESULT.md, labeled PROVED partial.
2. Finish new_residual_witness.json / verify_new_residual.py only if it is nearly done; otherwise mark it OPEN.
3. Rewrite RESULT.md as a clean final record: every PROVED claim with its replay script, NUMERICAL claims separated,
   and an OPEN section stating exactly what is left (the corner neighborhood of (r,a)=(1,1) and the open leaves).
   Remove the "working write-up" line.
4. Make replay_all.py run every PROVED replay in sequence and print PASS/FAIL per script; run it once and save the
   output to replay_all.out.
Then exit. A separate run (STRAT11) will attack the corner by a first-order expansion.
