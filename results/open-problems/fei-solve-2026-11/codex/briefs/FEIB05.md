disk: small

Read ~/fei_solve_agent/NOTES.md first.

Task: score the known extremal functions and search for larger ratios, in the split H = A + B, with Gamma.
1. The record lower bound for FEI is 6.521845710923 = H/(I-1) on a balanced function: take the 9 edges of K_{3,3},
   f0 = 1 exactly when the chosen edge set is a perfect matching (6 of 512 inputs), and plant "coins" (replace
   constants by fresh variables: the record uses nine coin variables; `python3 ~/.claude/dreaming/brain.py recall
   "Numaro PM K33 nine coins FEI record 6.5218"` and `brain.py node
   numaros_fei_record_is_perfect_matching_of_k33_with_coins_2026_09_23` give the exact construction). Rebuild it,
   confirm 6.5218457109, and report A, B, Gamma, P, I for it, level by level. Which part carries the record?
2. Same table for: AND_n, tribes, majority, address, recursive majority of 3, the 4-variable record 0x00aaeeee-type
   (H 3, I 1.5), the 5-variable B-record 0x008eeeee, and the best functions you find.
3. Search balanced functions on 6 to 12 variables (hill-climb / tabu on truth tables with exact scoring; 2^12
   entries is small) maximising separately A/(I-1), B/(I-1), Gamma/(I-1), H/(I-1). Report the best by n. The question
   that matters: do sup B/(I-1) and sup A/(I-1) look bounded in n, and is the B-extremal function a known one?
4. Theorem 1 says H/(I-1) <= 2B/(I-1) + 2 on balanced functions, so the record forces sup B/(I-1) >= 2.26; the
   5-variable census has 2.1537593748. Find a function with B/(I-1) > 2.26 explicitly and the largest you can.
Deliverables: scripts with outputs, RESULTS.md (tables, truth tables in hex with the bit convention stated),
REPORT.md. Exact arithmetic (integers for 2^n fhat) for every reported record; each record recomputed by a second
independent script. Memory: each process under 3 GiB, at most 2 threads, nice 10.
