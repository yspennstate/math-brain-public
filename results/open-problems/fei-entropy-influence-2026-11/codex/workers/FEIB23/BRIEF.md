# Worker FEIB23 (account acc2)

disk: small

# FEIB23 - FEI for linear monotone DNFs of every width (a restriction-closed class), by tree accounting

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7 (all), 12(q), 12(r), 12(s), 12(u); the proof you build on
is ~/fei_solve_agent/workers_in/FEIB21/PROOFS.md (section 12 there is theorem (LIN)); code in
~/fei_solve_agent/code (hill_filt.py `rho`, filt_big.py `dnf`, mono_hidden.py `erasure`)
(`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`; python with numpy: ~/fei_solve_agent/venv if present,
else python3 -m venv in your folder).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu, I = E|U|, H = H(mu). For a coordinate i: g = E_i f, h = D_i f,
Inf_i = E h^2, E_i = H(1[i in U] | U - i) = sum_T Phi(g^(T)^2, h^(T)^2), Phi(p, q) = (p + q) h2(p / (p + q)),
J_i = Jensen-Shannon term. Exact identities (FLOW 7, 12(u)):

    H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i,   I(f) = (1/2) I(f_0) + (1/2) I(f_1) + Inf_i,   J_i <= (2/ln 2) Inf_i,

so for any decision tree reading every variable, H(f) = sum_v P(v) (E + J)(v) and I(f) = sum_v P(v) Inf(v).
FEI for f with constant C + 2/ln 2 follows from ONE tree with sum_v P(v) E(v) <= C sum_v P(v) Inf(v). A node may
be bad if other nodes pay for it. (If every function of a restriction-closed class has one coordinate with
E_i <= C Inf_i, that is the special case where every node is good.)

The class. L = monotone DNFs in which two terms share at most one variable ("linear"), any widths, any number of
terms. L is closed under restrictions (x_j = 0 deletes the terms through j; x_j = 1 shortens them; absorbed terms
drop out; a term of width 0 makes f constant).

Known.
 (LIN) (FEIB21, proved): all terms of width w, every variable in at most D terms, D <= 2^((1-eps)(w-1)): then
       E_i / Inf_i = 2 + o(1) at EVERY coordinate, explicit finite bound. Mechanism: the derivative's spectrum sits on
       sets where the restriction f_0 has weight O(Inf_i) (separation lemma, FLOW 12(s)).
 A variable that is alone in a term (f = y OR r) is good, E/Inf <= about 3. A variable of a term whose other
 variables are private to that term is good, E/Inf < 6 (FLOW 12(q), 12(r)(1)).
 False rules: "largest influence is good" (FLOW 12(s), 12(u)); "every variable of a shortest term is good" for
 general monotone DNFs (12(u); that example is not linear).
 Exact numbers on leafless planes (terms = lines of D parallel classes of Z_p^2): min_i E_i/Inf_i = 2.63, 2.10, 1.89
 (p = 3; D = 2, 3, 4) and 3.10, 3.24, 2.88, 2.20, 1.55 (p = 5; D = 2..6). So the dense end is not bad either.

Tasks.
1. Exhaustive ground truth. Enumerate every f in L on n <= 8 variables up to isomorphism (n = 9 if cheap) and
   compute, exactly: max over L_n of min_i E_i/Inf_i, max of H/I, and the functions attaining them. Report whether
   the maxima grow with n and what the extremal functions look like (widths, degrees, bias).
2. Mixed widths, sparse regime. Replace (D - 1) a in FEIB21's proof by the load of a variable,
   lambda_j = sum over terms s through j of 2^-(w_s - 1), and of a term. State and prove the strongest theorem of the
   form "if every variable of term t has load at most c ... then a (which?) variable of t has E_i <= C Inf_i".
   Every step written; constants explicit.
3. The other regime. When loads are not small the function is far from balanced, or has very short terms. Treat:
   (a) width-1 and width-2 terms present; (b) f close to constant (P[f = -1] or P[f = +1] small): prove directly
   H <= C I there, or a good coordinate; (c) what is left. Say exactly which functions of L are covered by no case.
4. The theorem or the obstruction. Either prove: there is an absolute C with H(f) <= C I(f) for every f in L (by a
   good coordinate at every node, or by a tree with good average cost; a term-by-term tree, reading a whole term
   before moving on, is a natural candidate), or exhibit the family in L on which every approach here fails and say
   what E_i/Inf_i, the tree average and H/I do on it numerically.
5. Literature, one neutral clause each, only from sources you can open: is FEI known for read-k DNFs, for
   "unambiguous" or "linear" DNFs, for DNFs of bounded width? Say what (LIN) and a theorem for L would add.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 200 MB. Proofs go in PROOFS.md with
every step written; mark each statement PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. A claimed
theorem gets a hostile second read by you before REPORT.md says PROVED. RESULTS.md as you go; REPORT.md at the end.

