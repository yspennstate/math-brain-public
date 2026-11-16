---
name: p0251_af_crossover_chain_mixes_log_k_plus_log_l_via_czumaj_switching_networks_2026_11_14
description: "[PROVISIONAL] P0251 = Aldous-Fill book Open Problem 12.5 (random-pair binary crossover chain, K words of length L, show tau_1^disc = O(log K log L)): ANSWERED in stronger form O(log(K+1) + log(L+1)) by our short argument (unrefereed) on top of Czumaj STOC 2015 'Random permutations using switching networks' Prop 2.3 + Thm 3.4/3.7 (checked against the paper 14 Nov); quenched columns + Dobrushin submultiplicativity over independent blocks. Lower bounds log2 min(K,L) - 3 and (log2 L)/K - O(log K / K) for fixed K>=4; K=2 mixes in one step; note drafted 14 Nov"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-14T00:14:45.140Z
---

P0251 on the 200 list. Source: Aldous and Fill, "Reversible Markov Chains and Random Walks on Graphs", Sec 12.1.11
"Two base chains for genetic algorithms", Open Problem 12.5 (book.pdf p.401). Chain: K even binary words of length L;
each step a uniform random pairing of the words, and in each pair each coordinate is swapped independently with
probability 1/2. Column sums are preserved; uniform stationary law on each column-sum class. AF prove O(K log L) by a
coupling whose bottleneck is the last two mismatched words having to be paired (chance 1/(K-1) a step).

Answer (14 Nov 2026, ours, unrefereed): tau_1^disc = O(log(K+1) + log(L+1)), stronger than the O(log K log L) asked.
1. Given the pairing sequence, the L columns are independent: each is its 0/1 vector pushed through the same switching
   network (layers = the pairings) with its own fair switches. So TV(law_t, U) <= E_pi sum_l TV(quenched column l, U_l).
2. Each layer kernel is doubly stochastic, so TV(nu B, U) <= delta(B) TV(nu, U) with delta the Dobrushin coefficient;
   blocks of fresh pairings are independent, so E prod_b delta(B_b) = prod_b E delta(B_b).
3. Czumaj (STOC 2015, pp. 703-712): all but an O(n^-2) fraction of depth-c log n networks with uniform random perfect
   matchings are good (Prop 2.3), and a good network produces a uniform k-partial n-permutation from any input to
   within O(n^-c1) when k = Omega(n) (Thm 3.4). A column with K - m_l zeros is a coarsening of S_{K,K-m_l}; complement
   symmetry gives K - m_l >= K/2. So E delta(block of c log K layers) <= C K^-2 for K >= K0; a fixed depth handles K < K0.
4. TV(t) <= L (C K^-2)^{floor(t / c log K)}, giving O(log K + log(L/eps)).
Lower bounds: log2 min(K,L) - 3 (corrected 14 Nov: a lone 1 in ONE column mixes in O(1) steps averaged over the
pairings, so 'a lone 1 reaches 2^t words' gives nothing for one column; the right test puts a 1 in word 1 of
each of min(K,L) columns - under the chain they sit in at most 2^t words, under uniform in at least half as many
words as columns with probability >= 3/7). Omega(log K) for L = 1 is not proved. For fixed K >= 4, Omega_K(log L): start every column
at {1,2}; the quenched mass at {1,2} is dyadic with denominator 2^{tK/2}, the uniform mass 2/(K(K-1)) is not, and L
conditionally iid columns detect the gap. K = 2 is exactly uniform after one step for every L.

Literature (14 Nov): no paper found answering AF 12.5; Czumaj's 23 citers (OpenAlex W2162439784) are cryptography,
oblivious shuffling and lazy-swap papers, none on the AF chain.
Citation checked 14 Nov 02:4x against the paper itself (ACM DL, free access, read in the epdf reader): the model is
exactly the AF column process - layers are perfect matchings M_t from M^d, "almost all" = all but O(n^-2) of sequences
in M^d (footnote 2: any n^-c), each matched pair exchanged independently with probability 1/2 (Sec 1.1). Prop 2.3 and
Thm 3.4 read as used above (depth >= c log n, any input from S_{n,k}, k = Omega(n), TV O(n^-c1), any c1 per footnote 3).
Better: Thm 3.7 states the 0/1 case directly - almost every network (and every good one) of depth >= c log n gives,
for ANY s zeros and n-s ones, TV O(n^-c1) to uniform - so step 3 needs no coarsening or complement symmetry.
Remaining doubt (the hint for the next reader): the STOC version defers the Sec 3.1 coupling proofs (Lemmas 3.1-3.3)
to a full version, and Lemma 2.2 leans on Friedman's expander theorem for a union of four random perfect matchings;
our argument is unrefereed.
Work files: scratch area p0251/ of session agent (NOTES.md, slides, AF book text). Related: [[p0247_af_last_vertex_uniform_yes_under_dc_via_bht_open_torus_like_2026_11_14]].
Note drafted 14 Nov 03:1x: scratch area af-crossover-chain/paper/main.tex (7 pages, lints clean, references checked on
Crossref); next an independent audit, then a public repo crossover-chain-mixing. No Zenodo before the audit.
