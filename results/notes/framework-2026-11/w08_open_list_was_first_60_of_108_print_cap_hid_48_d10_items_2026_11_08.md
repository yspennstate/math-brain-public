---
name: w08_open_list_was_first_60_of_108_print_cap_hid_48_d10_items_2026_11_08
description: "[VERIFIED] Scar: the W08 no-verdict list (59) was the first 60 of 108; a [:60] print cap hid 48 D10 items. Count a script's file output against its own total before working down it"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T04:10:36+04:00
  status: verified
  evidence: "unverdict.py miss[:60] under header '108'; uncapped rerun x w08_free_items.py = 48 open, 8 Nov 04:1x"
---

Scar, 8 Nov 2026 (an agent). The W08 "no verdict yet" list I worked from all night (miss1.txt, then miss2.txt with 59 items) was truncated. The scan script printed `miss[:60]` under a header that said 108. I saved the printout to a file and then treated the file as the population. 48 Domain 10 items (D10.17 to D10.92) were never on it. I told a peer at 04:02 that "all 59" were done before a recount caught the gap.

Caught by a recount: an uncapped rerun of the scan, crossed with w08_free_items.py (which reads range forms such as "D10 #17-#19"), gave 53 items, 48 of them real. The other 5 were D6 items my own status line had abbreviated as "D6.57/58/69/...", a spelling neither scanner reads.

The fixed scan is w08_unverdict_scan.py (no cap; it reads the ledger, CHECKLIST, BRAIN_INSTALL_STATUS, 1000_ways_mac_status.md and memory slugs). Cross it with w08_free_items.py and keep only the items both call free. The open list as of 04:1x is w08_open_20261108.txt.

**Why:** a printout saved to a file reads like a complete list, and the header that gave the real total sat one line above the cut.
**How to apply:** before working down a list a script wrote, compare its line count with the total the script reports, and grep the script for a slice such as `[:N]` or `head`. When writing a verdict, spell every item out in full ("D6.58", not "D6.57/58"), so a scanner can find it. Related: [[w08_scan_missed_domain_n_notation_and_write_overwrote_peer_script_2026_11_01]].

Follow-up, 04:16: w08_free_items.py now also reads 1000_ways_mac_status.md, and the D10.N spelling in that file only (backup .pre_macstatus_20261108). Domain 10 went from 65 free to 25 free. It still does not read the ledger, CHECKLIST or memory slugs, and its open-list guard can skip an item that follows the word OPEN within 60 characters (D6.70). So keep crossing it with w08_unverdict_scan.py: tonight both name the same 15.

Symptom as an agent meets it (SYMLEAD1, 8 Nov, written from this note alone): The W08 scan reports 108 items, but its saved list contains only 60, and working through that file leaves dozens of Domain 10 items untouched. Another scan still finds open items after you have marked everything in the saved list done.
