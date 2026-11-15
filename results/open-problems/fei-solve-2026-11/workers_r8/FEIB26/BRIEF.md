# Worker FEIB26 (account acc2)

disk: small

# FEIB26 - transitive functions: the one-coordinate erasure inequality, its composition law, and towers

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 12(u) (with its correction block), 12(v), 12(w) (all
seven items); code ~/fei_solve_agent/code/cyc_hill.py, step_info.py, relative_step.py
(`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu, I = E|U|, H = H(mu). g = E_i f, h = D_i f, Inf_i = E h^2 = delta,
p_T = g^(T)^2, q_T = h^(T)^2, E_i = H(1[i in U] | U - i) = sum_T Phi(p_T, q_T), Phi(p, q) = (p + q) h2(p/(p + q)).
Exact forms (checked to 1e-15, step_info.py):
   E_i = h2(delta) - I(1[i in U]; U - i) = h2(delta) - (1 - delta) D(rho_g || nu) - delta D(rho_h || nu),
   delta E_{rho_h}[log2(p/q)]_+ <= E_i <= delta (1/ln 2 + 1) + delta E_{rho_h}[log2(p/q)]_+ .
Constants: C* = sup H/I (>= 6.5218), A* = sup sum_i E_i / I, G* = sup_f min_i E_i/Inf_i, and
C* - 2/ln 2 <= G* <= A* <= C*. Best explicit min_i E_i/Inf_i on record: 3.7137 (FEIB24).

The point. If a transitive group of coordinate permutations fixes f, all E_i/Inf_i are equal, so
   G(f) := E_1/Inf_1 = sum_i E_i / I = min_i E_i/Inf_i <= H/I.
For transitive f the good-coordinate statement is ONE inequality E_1 <= C Inf_1. Disjoint compositions of
transitive functions are transitive (wreath product), and the record functions for H/I are towers of a transitive
base (perfect matchings of K33, 9 variables). So towers are the natural place to push G up, and a proof of
E_1 <= C Inf_1 for all transitive f would be a new unconditional theorem.

Tasks, in this order.
1. Composition law for E (prove, then check by exact computation on small cases). F on k variables, psi on m
   variables with E psi = 0, f = F(psi(y^1), ..., psi(y^k)). The spectral sample of f is the union over j in V of
   independent U_j ~ mu_psi, V ~ mu_F. Derive the exact formula for E_i(f), i in block 1, in terms of mu_F, mu_psi,
   E_i(psi) and the "thinned erasure" sum_{V'} Phi(mu_F(V'), a mu_F(V' + 1)) with a = psi^({i})^2. Do the same
   for unbalanced psi (E psi = c: then blocks can be hit at the empty set; write the law carefully). State
   H, I, sum_i E_i of the k-fold tower F^{(k)} and the limit of G(F^{(k)}) as k grows, as a function of the base.
2. Towers. Using 1, compute lim G for towers of: PM(K33) (the C* record base), the 6.278 base of O'Donnell-Tan if
   you can reconstruct it, tribes, small bent functions, every transitive function on n <= 7 variables (cyclic
   group: exhaustive at n <= 7; add dihedral and the full list of transitive groups of degree <= 8 if cheap),
   mixed towers (base A inside base B). Report the best limit of G and beat 3.7137 if possible. Is
   sup over transitive f of G(f) equal to C* - (something explicit)? Is it plausibly equal to G*?
3. Search. Annealing over cyclically invariant functions for n = 12..20 with objective G (cyc_hill.py does this;
   improve it: restarts from structured seeds, pair flips, objective mixes). Also graph properties on 4 vertices
   (exhaustive, 2^11) and 5 vertices (annealing), and functions invariant under translations of F_2^k (variables
   indexed by F_2^k, k = 3, 4). Record the best G per n and the function.
4. Proof attempts for E_1 <= C Inf_1 under symmetry, every step written:
   (a) symmetric functions (follows from the known FEI for symmetric functions, O'Donnell-Wright-Zhou; give the
       direct argument and the constant);
   (b) cyclic functions of the form OR / threshold of shifts of one pattern;
   (c) any transitive f: use that mu is invariant, so for U ~ mu and i a uniform element of U the pair
       (U - i, i) has a law you can write down; E_1 / Inf_1 = E over (U, i in U uniform... size-biased) of
       log2(1 + mu(U - i)/mu(U)) up to the bounded terms above. Try: Shearer / Han-type inequalities for
       invariant measures, the identity f * f = delta (sum_S f^(S) f^(S + R) = 0 for R nonempty), and the
       convolution facts g^ * h^ = 0, g^ * g^ + h^ * h^ = delta_empty.
   A clean lemma, proved, on a subclass is worth more than a broad heuristic. If you find a transitive f with
   G(f) above 4, report it first.
5. One neutral clause each on what is known (only from sources you can open): FEI for symmetric functions, for
   transitive functions, composition theorems for Fourier entropy (O'Donnell-Tan; Chakraborty-Kulkarni-Lokam-
   Saurabh), and any earlier use of "erasure entropy" for the spectral sample.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 150 MB (the disk on this machine is
near its floor: no large arrays on disk, delete scratch as you go). Proofs go in PROOFS.md with every step
written; mark each statement PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. RESULTS.md as you go;
REPORT.md at the end.

