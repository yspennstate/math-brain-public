# K-read-k: read-k decision trees, covariance and entropy (route K, ledger C017, C021)

Owner of this folder: one Opus agent of the 11 Oct 2026 FEI workflow. Everything here is
working material: definitions, every attempt, complete proofs where they exist, and every
failed attempt with the witness that kills it. Statuses follow the campaign: PROVED,
REFUTED, PARTIAL, EVIDENCE, CONJECTURE, KNOWN, CANDIDATE_FULL.

## 0. Sources read (local copies of the arXiv sources in data/lit/)

- [WWW] A. Wan, J. Wright, C. Wu, Decision trees, protocols, and the Fourier
  entropy-influence conjecture, ITCS 2014, arXiv:1312.3003 (source readk.tex, read
  12 Oct 2026). Protocol of Section 2.3; Lemma 3.5 (length <= 4 I + 2 Cov[T]);
  Lemma 3.8 (Cov[T] <= sum_S (m_T(S)-1) fhat(S)^2 <= (k-1) Var f); Theorem 3.7
  (H <= (2+(2k+2)log2 3) I for read-k trees); the remark after it conjectures
  Cov[T] <= log2(k) Var f, with the dummy-layer example attaining log2(k) Var f.
- [Sha] G. Shalev, On the Fourier entropy influence conjecture for extremal classes,
  arXiv:1806.03646v2 (source guy_thesis.tex). Section 6.2: Cov[T] <= sum_S sq_T(S)
  fhat(S)^2 with sq_T(S) = 2 sum_{i in S} sqrt(a_i(T)), hence Cov[T] <= 2 sqrt(k) I
  (the proof needs a_i >= 16, repaired by adding 16 to every count). It records that the
  potential l_T(S) = sum_{i in S} log a_i(T) "did not follow through".

## 1. Definitions and conventions

f : {-1,1}^n -> {-1,1} computed by a decision tree T. Every internal node v has a label
l(v) in [n]; the left child is the x_{l(v)} = +1 branch, the right child the -1 branch.
No variable is queried twice on one root-to-leaf path. d(v) = depth (root 0). f_v is the
function computed by the subtree at v (a function of all variables not queried above v);
g_v, h_v are the functions of v's left and right subtrees.

- read-k: a_i(T) := number of internal nodes labeled i; T is read-k iff max_i a_i(T) <= k.
  (This is the exact hypothesis of [WWW] and [Sha]: k counts ALL query nodes for each
  variable, not occurrences on a path.)
- Cov(g,h) = E[gh] - E[g]E[h] = sum_{S nonempty} ghat(S) hhat(S).
- Cov[v] = Cov(g_v,h_v); Cov[T] = sum_v 2^{-d(v)} Cov[v]; recursively
  Cov[T] = Cov(g,h) + (Cov[T_0] + Cov[T_1])/2.
- beta_v := fhat_v({l(v)})^2 = ((E g_v - E h_v)/2)^2.
- Inf_i(f) = Pr[f(x) != f(x^i)] = sum_{S ni i} fhat(S)^2; I(f) = sum_i Inf_i(f).
- V(T) := sum_v 2^{-d(v)} Var(f_v) = E_x [ sum over internal nodes v on the path of x of Var(f_v) ].
- H(f) = - sum_S fhat(S)^2 log2 fhat(S)^2 (bits).

## 2. Target (sharpest exact version attacked)

T1 (campaign C021, log form): there is an absolute A with Cov[T] <= A log2(k+1) I(f) for every
read-k decision tree T computing a Boolean f, with k counting all query nodes of each variable.

T2 (per-variable log potential, stronger, suggested but abandoned in [Sha]):
   Cov[T] <= sum_i Inf_i(f) log2 a_i(T)        (variables with a_i = 0 have Inf_i = 0).
T2 implies T1 with A = 1 and implies, through [WWW] Lemma 3.5 and Lemma 2.2 (nozero),
   H(f) <= log2(3) (4 I + 2 Cov[T]) + 2 I <= (2 + 4 log2 3 + 2 log2(3) log2 k) I.

T3 ([WWW] conjecture, strongest): Cov[T] <= log2(k) Var(f).

Or the opposite outcome: read-k trees with Cov[T] / I(f) growing faster than log k.
