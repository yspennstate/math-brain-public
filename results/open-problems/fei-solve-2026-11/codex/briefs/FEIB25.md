account: acc2
disk: small

# FEIB25 - the edge form of FEI level by level: where the known bound loses a logarithm

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7 (all), 12(p), 12(u); code
~/fei_solve_agent/code/mono_hidden.py (`wht`, `phi`, `erasure`), hill_filt.py
(`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).

Setting. f Boolean (+-1) on n variables, mu(S) = f^(S)^2, U ~ mu, I = E|U|, H = H(mu), W_d = mu(level d).
Phi(p, q) = p log2((p+q)/p) + q log2((p+q)/q). The erasure entropy of coordinate i is
E_i = H(1[i in U] | U - i) = sum over T not containing i of Phi(mu(T), mu(T + i)), and (FLOW 7, 12(u))

    FEI  <=>  sum_i E_i <= C I for every f                                   (edge form)
         <=>  E_U sum_{i in U} log2(1 + mu(U - i)/mu(U)) <= C' E|U| for every f   (up form; the other half of Phi is <= I/ln 2).

So FEI is a statement about edges (T, T + i) of the subset lattice: on average over U ~ mu, the down-neighbours
of U do not carry much more mass than U. Split by level: for d >= 1 let

    A_d = sum over |S| = d of mu(S) sum_{i in S} log2(1 + mu(S - i)/mu(S)),        so FEI <=> sum_d A_d <= C' sum_d d W_d.

What I recall, to be checked against the paper itself before you use it: Kelman, Kindler, Lifshitz, Minzer and
Safra (Towards a proof of the Fourier-Entropy Conjecture?, arXiv:1911.10579) prove H(f) <= C sum_S mu(S) |S| log(|S| + 1),
that is FEI with an extra logarithm of the degree, by random restrictions and a hypercontractive estimate.

Tasks.
1. Open the paper (and its journal version if different) and write down its main theorems exactly as stated,
   with theorem numbers, and the two or three lemmas that carry the proof. If you cannot open it, say so and
   work from the definitions only; do not reconstruct statements from memory.
2. The level profile, exactly. For every NPN class on n <= 5 (exhaustive), and for families at larger n (majority,
   tribes, address, bent, towers of the K33 perfect-matching function - code in hill_filt.py and FLOW 12(g) -
   random functions, the hidden-coordinate function of mono_hidden.py), compute A_d, d W_d and (d - 1) W_{d-1}.
   Test the level-local inequalities
       (L1)  A_d <= C (d W_d + (d - 1) W_{d-1})        (L2)  A_d <= C d W_d + C' W_{d-1} + ...
   and find the weakest true-on-everything-you-can-compute form: which weights on W_{d-1}, W_{d-2}, ... are needed?
   Hill-climb (n <= 16 or so) to break each candidate. A_1 is special (S - i is empty: mu(empty) = mean^2).
3. Where the log comes from. In the edge form, reprove (or follow the paper to prove) the bound with the
   logarithm: sum_i E_i <= C E[|U| log(|U| + 1)], writing every step. Mark the single inequality where log(|U| + 1)
   enters and describe the functions for which that inequality is tight. Is there a Boolean function for which that
   step really loses, or only non-Boolean spectra? If only non-Boolean, say which use of Booleanity could remove it
   (e.g. g h = 0 and g^2 + h^2 = 1 for g = E_i f, h = D_i f; or the tree identity
   H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i).
4. Low levels. Prove what you can at fixed level: A_1 and A_2 in terms of W_0, W_1, W_2 and I (level-1 and level-2
   inequalities, Talagrand's level-k bounds W_k <= C_k var log^k(1/var) may help for biased f). A clean proved
   inequality for A_2 that is not implied by hypercontractivity alone is the kind of result wanted.
5. One page at the end: what you now believe is the true obstruction to removing the logarithm, with the
   evidence for and against, and the next lemma you would try.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 200 MB. Proofs go in PROOFS.md with
every step written; mark each statement PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. One neutral
clause of attribution per cited fact. RESULTS.md as you go; REPORT.md at the end.
