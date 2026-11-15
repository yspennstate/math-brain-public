disk: small

Read ~/fei_solve_agent/FLOW.md first: sections 7, 9 and 10 state this task. Check scripts are in
~/fei_solve_agent/code (check_erasure.py computes every quantity below; hill_rho.py is a search).
Earlier workers' folders: ~/codex_fleet/20261108_pro/workers/FEIB02 (symmetric functions), FEIB10-FEIB13. Build on them,
do not redo them.

Setting. f Boolean (+-1) on n bits, mu(S) = fhat(S)^2, U ~ mu the spectral sample, I = E|U|, H = H(mu).
  E_i = H(1[i in U] | U - i) = sum_{T not containing i} (a^2+b^2) h(b^2/(a^2+b^2)),  a = fhat(T), b = fhat(T+i).
  H^- = sum_i E_i (the erasure entropy of U).  H^- <= H, and FEI (H <= C I) is equivalent to H^- <= C' I, with
  sup H^-/I <= C* <= sup H^-/I + 2/ln 2.
  Witness principle: for any statistic s_i of U - i, E_i <= H(1[i in U] | s_i(U - i)).

Task: prove H^- <= C I with explicit C for classes of functions, each time by exhibiting the witness statistic s_i,
and find out which witnesses are needed in general.

1. Symmetric functions. Parity of |U - i| is a witness for odd/even functions. For a general symmetric f the ratio is
   (W_(k-1)/W_k)(n-k+1)/k. Prove H^- <= C I with the best C you can; compare with FEIB02's constants for H.
2. Read-once formulas (AND/OR/XOR/MAJ gates on disjoint variables) and read-once decision trees. Give the witness
   (for AND/OR gates: the block witness of FLOW 10(d) with N = the siblings) and a constant independent of depth.
   A composition rule: express E_i of f(g_1,...,g_m) on disjoint blocks through the spectra of f and g_j, exactly.
3. DNF of width w, decision trees of depth d or size s, degree-d functions: H^- <= C(w) I etc. State what is known
   for H in each class (Chakraborty-Kundu-Lokam-Saurabh; Wan-Wright-Wu; O'Donnell-Wright-Zhou; Shalev) and whether
   the erasure form gives a shorter proof or a better constant.
4. Linear threshold functions and monotone functions: which witness works? Test numerically first on random LTFs
   (n <= 14) and on monotone functions (n <= 6 exhaustively by Dedekind enumeration or sampling).
5. The general question. On the n <= 5 NPN census and on samples at n = 6..10, for each f compute the best witness
   in each family: (i) parity of |T cap P| over all P; (ii) "T meets N" over all N; (iii) both together;
   (iv) |T| alone; (v) |T cap N| for the best N. Report sup over f of (sum_i H(1_i | best s_i))/I per family, and
   the functions where each family fails. Is there a finite family of witnesses that keeps the ratio bounded on
   everything you can compute?

Deliverables: PROOFS.md (each statement labelled PROVED, CHECKED with scope, or OPEN), scripts with outputs,
RESULTS.md (tables, extremal truth tables in hex), REPORT.md with one verdict line per numbered item, LEARNINGS.md
(what failed and why). Write as you go. Memory: each process under 3 GiB, at most 2 threads, nice 10.
