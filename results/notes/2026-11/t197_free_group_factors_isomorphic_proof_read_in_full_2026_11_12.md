---
name: t197_free_group_factors_isomorphic_proof_read_in_full_2026_11_12
description: "Free group factor isomorphism problem solved (OpenAI 23 Sep 2026; Shlyakhtenko arXiv 2610.19590): L(F_n) isomorphic for all n >= 2; 23-page proof read in full and checked by hand, no error; moments of T_m T_m* equal the squared Kesten-McKay law of the (m+1)-regular tree; free entropy dimensions are not W*-invariants; do not work the row as open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:18:27+02:00
  status: verified
  evidence: "06_math_research/t197_free_group_factors_agent_2026_11_12/T197_CHECK.md, t197_check.out; push 1207767f79648ec4bc1da6e24dc377a4ed2a27e0"
---

Row T197 of the top-200 list (are the free group factors L(F_n) isomorphic for different n) is reported solved, and the report holds up to a full reading. Sources: OpenAI, "An isomorphism of the free group factors", 23 Sep 2026, 23 pages, public repository openai/math (preprints folder of the same name; the PDF there carries the folder's name, not main.pdf; not on arXiv); D. Shlyakhtenko, arXiv 2610.19590 (14 Oct 2026), 28 pages, a self-contained proof by the same strategy of the stronger C*(S_1..S_n) = C*(S_1,S_2) for semicircular systems, which gives L(F_n) = L(F_2) for every n at once. His acknowledgements say the work is based on AI-generated proofs and that a language model was used in analysing the original.

What I did (12 Nov 2026): read all 23 pages and checked every step by hand, no error. The argument: with free Haar unitaries A_1..A_n, C generating L(F_{n+1}) and S = arg C, a polynomial flow X_j' = i (sum_g h_j(g) X_g S X_g*) X_j gives trace-preserving automorphisms fixing S (first variation of every moment vanishes at time 0 because conjugating one S_g by a unitary from the others keeps the joint law; then analyticity). With the cocycle D x_j = h_j the flow moves A_j by at most 3 pi ||h_j|| and sends A_w within 3 pi ||Dw - delta_e|| of C A_w. For w_m = p_m a with p_j = (a b_1)...(a b_j), b_j = x_2^j x_3 x_2^-j, Dw_m = T_m h, T_m = 1 + sum lambda(p_j), and T_m T_m*/m has limiting density (1/2pi) sqrt((4-x)/x) with no atom at 0, so a cutoff inverse gives a small h with T_m h near delta_e. Composing with the automorphism C -> C A_w gives an automorphism that almost fixes the generators of L(F_n) and carries A_w almost onto C; iteration gives L(F_n) = L(F_{n+1}) for n >= 3, and rank 2 follows by amplifying L(F_3) = L(F_5) by sqrt 2.

Computer tests (t197_check.py, 18 s): exact moments of T_m T_m* by free reduction on the actual words agree with free symbols (42 cases) and with a closed form I derived, the square of the Kesten-McKay law of the (m+1)-regular tree, density N sqrt(4(N-1)t - t^2)/(2 pi t (N^2 - t)), N = m+1 (48 values, relative difference 2e-11); Dw_m = T_m h on 200 random cases, 0 failures; the cutoff errors; freeness of the conjugates and the 3 pi norm bound in a 300 x 300 Haar matrix model (ratio at most 0.38).

How to use: do not work T197 as open. The four free entropy dimensions are not invariants of the von Neumann algebra (each takes every integer n >= 2 on generators of L(F_2)); do not propose them as invariants in any note. Open next to it: an explicit isomorphism; whether isomorphic group factors have first L2-Betti numbers vanishing together; which inclusions have the automorphism approximation property. Reusable: for a sum of N free Haar unitaries the law of |x|^2 is the squared Kesten-McKay law (the Hermitian dilation is the adjacency operator of the N-regular tree); an isomorphism N = M from automorphisms of M that almost fix a finite part of N and carry an element of N almost onto a given element of M (Baire category).

What would change this: an error found in Lemma 3.2 or 3.4 (moment invariance of the flow), which carry the most weight; a formalization would raise the check further.

