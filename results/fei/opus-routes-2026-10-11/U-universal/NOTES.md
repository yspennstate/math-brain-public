# U-universal: the universal FEI statement, its bridges, and the missing inequality

Route: U-universal (campaign ledger C000, C018, C019, C024). Author: Opus agent, folder
`~/fei_opus_2026_10_11/U-universal/`. Started 2026-10-12 00:3x (owner's clock).
Full FEI remains OPEN. Nothing below claims a proof of C000.

Status words: PROVED (complete proof below), KNOWN (literature, exact citation), EVIDENCE
(finite computation, floating logarithms unless stated), PARTIAL (rests on a named unproved
step), CONJECTURE, REFUTED (explicit witness).

## 0. Conventions

f : {-1,1}^n -> {-1,1}. fhat(S) = E[f chi_S], p_S = fhat(S)^2, S a random set with law p,
S_i = 1[i in S]. H(f) = sum p_S log2(1/p_S) (bits). I(f) = E|S| = sum_i Inf_i,
Inf_i = P(i in S). Var = 1 - p_empty. J(f) = sum_i min(Inf_i, 1-Inf_i) (= D_char).
B_i = H(S_i | S_{-i}), B = sum B_i, DTC = H - B, TC = sum_i h(Inf_i) - H, where h is binary
entropy in bits. L(f) = sum_S p_S sum_{i in S} log2(1 + p_{S-i}/p_S) (downward-edge functional).
f_{i,+-}: physical restriction x_i = +-1. Delta_i(f) = H(f) - (H(f_{i,+}) + H(f_{i,-}))/2.
JS_i = Delta_i - B_i (Jensen-Shannon term). For a block A of physical coordinates, I_A = sum_{i in A} Inf_i.
All sup/inf below range over all n >= 1 and all nonconstant Boolean f (extended reals).

Baseline facts used (all in the campaign sources, reproved there):
* (E1) [ER sec.1-4, C005] Delta_i = B_i + JS_i, 0 <= JS_i <= (2/ln2) sum_{T not i} min(p_T, p_{T+i})
  <= (2/ln2) min(Inf_i, 1-Inf_i); I(f) = Inf_i + (I(f_{i,+}) + I(f_{i,-}))/2.
* (E2) [ER sec.3] B <= H; H, B, I, J, DTC, TC, L are additive under disjoint tensor products.
* (E3) [ER sec.5] L <= B <= L + I log2 e.
* (E4) [BR, C006] For a fixed block A with live complement C and uniform assignment X on A:
  H(f) - E_X H(f_X) = H(S_A | S_C) + I(X; D), D drawn from the spectrum of f_X, and
  I(X;D) <= (2/ln2) I_A(f). Also I(f) = E_X I(f_X) + I_A(f).
* (E5) 0 <= Delta_i <= 2 (since B_i <= H(S_i) <= 1 and JS <= 1 bit).
* (E6) Edge isoperimetry (Harper; Hart 1976): with mu = min(P(f=1), P(f=-1)), I(f) >= 2 mu log2(1/mu).

## 1. The target and the sharpest equivalent missing inequality (summary)

C000: exists C < infinity with H(f) <= C I(f) for all Boolean f.

Section 2 proves that the following are all equivalent to C000, with explicit constants:

* (GEI) B(f) <= K I(f) for all f            [C018; K_E finite]
* (LEI) every nonconstant f has a coordinate i with B_i(f) <= K Inf_i(f)          [K_loc finite]
* (LDI) every nonconstant f has a coordinate i with Delta_i(f) <= K Inf_i(f)      [K_Delta finite]
* (DTC) H(f) <= A (I(f) + DTC(f)) for all f                                       [Thm C1, new form]
* (o(n)) H(f) <= C I(f) + o(n), uniformly over f on n bits                         [tensor trick]
* (CRIT) every *ratio-critical* f with all Inf_i <= 1/2 satisfies H <= K I         [Thm C]

The sharpest single missing inequality, in the form isolated here, is

  (M)  There is K < infinity such that no Boolean function is "erasure-expensive at rate K":
       for every nonconstant f there is a coordinate i with H(S_i | S_{-i}) <= K P(i in S),

and one may additionally assume f ratio-critical (Sec. 2.4), hence DTC(f) <= (2/ln2) J(f), every
block conditional entropy H(S_A | S_{A^c}) >= (c - 2/ln2) I_A(f), the random-order erasure profile
beta_f is flat (Thm C(viii)), all Inf_i <= Var 2^{6.08 - c}, and deg f >= 1 + c I/2. In words: the only
way FEI can fail is through Boolean spectral laws that look, at every coordinate and at every
scale, like product laws with small marginals. Exact product laws are excluded by integrality
(C016); the missing inequality is a *quantitative stability* version of that rigidity, and Sec. 4
shows it cannot be obtained from hypercontractivity plus operator Booleanity alone.

**Main new result (Sec. 5).** Lemma G-key |fhat(S)| <= 2^{|S|-1} I_S(f) (I_S = sum_{T sup S} fhat(T)^2, a
one-line consequence of the parity of +-1 sums over restrictions) gives the universal inequality
  (Theorem G)  H(f) <= 2(I(f) - Var(f)) + 2 U(f),   U(f) = sum_S p_S log2( I_S(f)/p_S ) <= H(f),
which settles the product-like case quantitatively: every Boolean f with U(f) <= c I(f) has
H(f) <= (2 + 2c) I(f), and spectral laws that are product-like with small marginals in the upper-set sense
have U ~ I log2 e while H ~ I log(1/theta), so no Boolean spectrum is of that kind.
It is tight to leading order on point defects and asymptotically tight on the extremal read-once
formulas. Consequently FEI is equivalent to
  (M_U)  U(f) <= K I(f) for all Boolean f      (C_FEI <= 2 + 2K, and K >= 2.227 by Hod),
and the exact restriction identity for U (Sec. 5.1) shows that the local logarithm behind the
obstructions X003/X009 is refunded inside U. Sufficient forms of (M_U) with strong numerical support:
GU (sum_i Delta_i U <= K I, max observed 3.09), GU' (with + b U, b < 1), and the lift form of Sec. 5.3.
Unlike FEI, (M_U) is not contradicted by the quantum counterexample, so soft tools are not excluded.

## 2. Bridge assembly (PROVED unless marked)

### 2.1 Constant sandwich (Theorem A) - PROVED

Define C_FEI = sup H/I, K_E = sup B/I, K_L = sup L/I,
K_loc = sup_f min_{i: Inf_i>0} B_i/Inf_i, K_Delta = sup_f min_{i: Inf_i>0} Delta_i/Inf_i.

**Theorem A.** K_loc <= K_E <= C_FEI <= K_Delta <= K_loc + 2/ln2, and K_L <= K_E <= K_L + log2 e.
Hence C_FEI <= K_Delta <= C_FEI + 2/ln2 and all five constants are finite together.

*Proof.* (a) K_loc <= K_E: if Inf_i = 0 then S_i = 0 a.s. and B_i = 0. If every i with Inf_i > 0
had B_i > K_E Inf_i, summing would give B > K_E I, contradicting the definition of K_E.
(b) K_E <= C_FEI: B <= H by (E2).
(c) C_FEI <= K_Delta: induction on n. Constants have H = I = 0. For nonconstant f on n bits choose
i with Inf_i > 0 and Delta_i <= K_Delta Inf_i (it exists by definition of K_Delta, the minimum over
a finite set being attained). The restrictions are Boolean on n-1 bits, so by induction
H(f) = Delta_i + (H(f_+) + H(f_-))/2 <= K_Delta Inf_i + K_Delta (I(f_+) + I(f_-))/2 = K_Delta I(f), by (E1).
(d) K_Delta <= K_loc + 2/ln2: for the i attaining min B_i/Inf_i <= K_loc, (E1) gives
Delta_i = B_i + JS_i <= (K_loc + 2/ln2) Inf_i.
(e) is (E3) divided by I. Chaining (c),(d),(a),(b): C_FEI <= K_Delta <= K_loc + 2/ln2 <= K_E + 2/ln2 <= C_FEI + 2/ln2. QED

Known numerical floors: C_FEI >= 6.454784 (Hod, arXiv:1711.00762). Campaign F4 (route map sec.5,
numerical, not replayed here): K_E >= 4.5388, K_loc >= 4.5048, K_Delta >= 7.0518 (Numaro
self-composition). Exhaustive n <= 4 (Sec. 6, EVIDENCE): max H/I = 3.4025 (4-bit point defect),
max B/I = 2.7042, max_f min_i B_i/Inf_i = 2.6725, max_f min_i Delta_i/Inf_i = 4.8677.

### 2.2 Tensor reformulation (Theorem B) - PROVED (standard tensor trick)

**Theorem B.** Let Psi be any nonnegative functional on Boolean functions with
Psi(f^{(x)t})/t -> 0 as t -> infinity for every f, where f^{(x)t} is the product of t copies of f on
disjoint variables. If H(f) <= C I(f) + Psi(f) for every Boolean f, then H <= C I for every f. The
same holds with B or L in place of H.

*Proof.* H and I are additive on disjoint products (E2): t H(f) <= C t I(f) + Psi(f^{(x)t}); divide
by t and let t -> infinity. QED

Admissible Psi include o(n), o(deg f), any o(I) function of I, A log(2 + I + n), A Var log(1/Var)
(Var(f^{(x)t}) <= 1). Thus FEI is equivalent to "H <= C I + o(n)": only the linear-in-dimension
behaviour matters. Multiplicative losses that are not tensor-sublinear (log I, log deg, the
KKLMS factor log(|S|+1)) cannot be removed this way: under tensor powers |S| and I grow.

### 2.3 Existential-coordinate formulation and stopping trees (C019) - PROVED

For a restriction tree T (each internal node v queries a coordinate i_v of its current restriction
f_v; w_v = 2^{-depth(v)}; leaves l), (E1) telescopes to the exact pair
  H(f) = sum_v w_v Delta_{i_v}(f_v) + sum_l w_l H(f_l),  I(f) = sum_v w_v Inf_{i_v}(f_v) + sum_l w_l I(f_l).
Hence H/I <= max(max_v Delta_v/Inf_v, max_l H(f_l)/I(f_l)) for every tree. C019's hypothesis (a genuine
stopping tree whose cumulative charge sum_v w_v Delta_v is paid linearly by the consumed influence
and whose leaves are FEI-certified) implies FEI; conversely FEI with constant C implies, by
Theorem A, that the tree which always queries a coordinate with Delta_i <= (C + 2/ln2) Inf_i and
stops at constants satisfies C019's hypothesis with constant C + 2/ln2. So C019 is FEI-equivalent;
its local form is (LDI). With the mismatch bound of RM sec.2.1, Delta_v <= M_v[log(1/M_v) - D_2(nu_v||q_v)
+ 3/ln2] and M_v <= j_v, C019's open payment is sum_v w_v M_v[log(1/M_v) - D_2(nu_v||q_v)] = O(I).

### 2.4 Criticality reduction and the profile of an extremizer (Theorem C) - PROVED

Let c_n = max{H(f)/I(f) : f nonconstant Boolean on n bits} (a finite maximum; c_n is
nondecreasing in n since adding a dummy variable changes nothing). Call f *ratio-critical* if
H(g)/I(g) <= H(f)/I(f) for every nonconstant restriction g of f.

**Theorem C.** Let f on n bits attain c := c_n. Then:
(i) f is ratio-critical; every restriction g of f satisfies H(g) <= c I(g).
(ii) every Inf_i(f) <= 1/2.
(iii) Delta_i(f) >= c Inf_i(f) for every i; hence B_i >= c Inf_i - JS_i >= (c - 2/ln2) Inf_i.
(iv) DTC(f) <= sum_i JS_i(f) <= (2/ln2) J(f) <= (2/ln2) I(f).
(v) for every block A with complement C: H(S_A | S_C) >= (c - 2/ln2) I_A(f), and
    H(S_C) <= c I_C(f) + (2/ln2) I_A(f)  ("hereditary marginal bound").
(vi) Inf_i(f) <= Var(f) 2^{6.0782 - c} for every i (with the variance-local bound of RM sec.2.2:
    Delta_i <= Inf_i[log2(Var/Inf_i) + 6.078162672495945]).
(vii) deg f >= 1 + c I(f)/2 (granularity: every nonzero p_S >= 4^{1-deg f}, so H <= 2(deg f - 1)).
(viii) (flat random-order erasure profile) Let beta(t) = sum_i E[H(S_i | S_{A_t})], where A_t is a
    Binomial(t) random subset of [n]\{i} independent of S. Then for every t in (0,1]:
    (c - 2/ln2) I <= beta(t) <= (c - 2/ln2) I + (2/ln2) I / t.
(ix) (random restrictions of extremizers are near-extremal) for J a Binomial(t) live set and X a
    uniform assignment of J^c: E[c I(f_{J,X}) - H(f_{J,X})] <= (2/ln2)(1-t) I(f).

*Proof.* (i) Restrictions of f are Boolean functions on fewer bits, with ratio <= c_{n-1} <= c_n.
(ii) If Inf_i > 1/2, then f chi_{i} has the same entropy (the spectrum is translated) and
I(f chi_i) = I(f) - (2 Inf_i - 1) < I(f), so its ratio exceeds c_n, impossible.
(iii) By (i), (H(f_+) + H(f_-))/2 <= c (I(f_+) + I(f_-))/2 = c (I - Inf_i) (E1), so Delta_i >= c Inf_i.
Then use Delta_i = B_i + JS_i and JS_i <= (2/ln2) Inf_i.
(iv) Summing (iii): B + sum JS_i >= c I = H, so DTC = H - B <= sum JS_i <= (2/ln2) J.
(v) By (E4), H(S_A|S_C) = H(f) - E_X H(f_X) - I(X;D) >= c I - c E_X I(f_X) - (2/ln2) I_A
= (c - 2/ln2) I_A, using (i) and E_X I(f_X) = I - I_A. Then H(S_C) = H - H(S_A|S_C) <= c I_C + (2/ln2) I_A.
(vi) c Inf_i <= Delta_i <= Inf_i [log2(Var/Inf_i) + 6.0782] (RM sec.2.2, proved there for actual Inf_i > 0).
(vii) Granularity (KNOWN, folklore; e.g. O'Donnell, Analysis of Boolean Functions, Ex. 1.11): a
Boolean f of degree d has every fhat(S) in 2^{1-d} Z, so nonzero p_S >= 4^{1-d}, the support has
at most 4^{d-1} sets, and H <= 2(d-1). Combine with H = c I.
(viii) psi(t) = E H(S_{A_t}) (A_t Binomial(t) in [n]) is a polynomial in t with psi(0)=0, psi(1)=H and,
by the Margulis-Russo formula, psi'(t) = sum_i E[H(S_{A_t + i}) - H(S_{A_t - i})] = beta(t). Coupling
A_t inside A_{t'} for t < t' shows beta is nonincreasing (conditioning reduces entropy), so psi is
concave and H = psi(t) + int_t^1 beta <= psi(t) + (1-t) beta(t). By (E4) applied with live block A_t,
psi(t) <= E H(f_{A_t,X}) + (2/ln2)(1-t) I and by (i) E H(f_{A_t,X}) <= c t I. Hence
c I - (1-t) beta(t) <= c t I + (2/ln2)(1-t) I, i.e. beta(t) >= (c - 2/ln2) I for t < 1, and t = 1 is (iii)
summed (beta(1) = B). Upper: int_0^1 beta = H = c I and beta nonincreasing give
t beta(t) <= int_0^t beta = c I - int_t^1 beta <= c I - (1-t)(c - 2/ln2) I.
(ix) Concavity gives psi(t) >= t H = t c I, so E H(f_{A_t,X}) >= psi(t) - (2/ln2)(1-t) I >= t c I - (2/ln2)(1-t) I,
while E c I(f_{A_t,X}) = c t I. QED

More generally, for any f and any c >= sup of the ratio over f's restrictions, the deficit
delta(g) = c I(g) - H(g) >= 0 satisfies E delta(f_{A_t,X}) <= t delta(f) + (2/ln2)(1-t) I(f)  (same proof).

**Corollary C1 (DTC form).** FEI holds iff there is A < infinity with H(f) <= A (I(f) + DTC(f)) for all f.
*Proof.* If the inequality holds, apply it to an extremizer f of c_n: c_n I <= A(I + (2/ln2) I) by (iv),
so c_n <= A(1 + 2/ln2) for all n. The converse is trivial (DTC >= 0). QED

Equivalently: FEI iff B(f) <= (A - 1) DTC(f) + A I(f). DTC(P) = 0 iff P is a product law (for two
variables DTC is their mutual information; in general DTC = sum_i I(S_i; S_{-i}) - TC). So
Corollary C1 says that FEI fails only through spectra that are *locally* product-like (small DTC),
possibly globally a mixture of few product laws (small DTC allows large TC).

**Corollary C2 (sharp missing inequality).** FEI iff there is K such that every ratio-critical f
with all Inf_i <= 1/2 has a coordinate with B_i <= K Inf_i. (Theorem A(c),(d) and Theorem C(i),(ii):
if FEI fails, extremizers c_n -> infinity and by (iii) none of their coordinates is cheap.)

### 2.5 Path-cost bridge (C024) - KNOWN in the campaign, placed here

RM sec.11.13: for Boolean f the true integrated conditional path cost satisfies
H_nat(f) - 3 I <= C_path <= H_nat(f) + I, so a universal linear bound on C_path is FEI-equivalent
(constants shift by 3 and 1 in natural units). RM sec.11.13 also gives
H_nat <= (4 + 2 ln2) I + Q_bias with |Q_bias - C_path| <= (1 + 2 ln2) I. In the frame of Theorem C,
the integrated quantities C_path and Q_bias are random-order (clock) analogues of the profile beta
in C(viii); for an extremizer they are within O(I) of c I and carry no extra information beyond (M).

## 3. Literature: exact status of universal bounds (KNOWN)

* Keller-Mossel-Schlank, arXiv:1105.2651 (2011); Han, arXiv:2312.08271 (v2 Dec 2025):
  H(f) <= O(I(f) + sum_k Inf_k log(1/Inf_k)). In bits it is the one-line subadditivity
  H(S) <= sum_i H(S_i) = sum_i h(Inf_i) <= sum_i Inf_i log2(1/Inf_i) + I log2 e.
* Kelman-Kindler-Lifshitz-Minzer-Safra, arXiv:1911.10579v2 (7 May 2020), Theorem 1.3 (natural logs,
  {0,1}-valued f): H[f^{<=D}] <= K sum_{|S|<=D} |S| log(|S|+1) fhat(S)^2 + K I[f], absolute K.
  Proof (their Sec. 7.1): bucket S by level d and by k with
  2^{-C(k+1) d log(d+1)} var^{1/2} < |fhat(S)| <= 2^{-C k d log(d+1)} var^{1/2}; Corollary 6.7 bounds the
  mass of each bucket with k >= 1 so that their total entropy contribution is O(I); the k = 0
  buckets are paid at rate 2 C d log(d+1) + log(1/var). Theorems 1.1, 1.2: min-entropy
  H_inf <= O(Itilde log(1 + Itilde)) and concentration on 2^{O(Itilde log(1+Itilde))} characters,
  Itilde = I/var. Their remark: removing the log factor "would essentially resolve" FEI.
* Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf, arXiv:1809.09819 (ToCT 13(4), 2021):
  H <= 2 aUC_parity(f) (average unambiguous parity-certificate complexity); H_inf <= 2 C_min,parity.
  This subsumes H <= 2 E[decision-tree depth] (which also follows from (E5) and Sec. 2.3).
* Granularity (folklore): H <= 2(deg f - 1).
* Class results: symmetric functions and read-once decision trees (O'Donnell-Wright-Zhou, ICALP
  2011); read-once formulas / composition (O'Donnell-Tan, arXiv:1304.1347); read-k decision trees
  O(k) (Wan-Wright-Wu, arXiv:1312.3003) and O(sqrt k) (Shalev, arXiv:1806.03646, which also proves
  the low-influence reduction); random LTFs (Chakraborty et al., arXiv:1903.11635); plateaued
  functions with sharp constant 4 and partially bent with 2 (Potapov, arXiv:2609.21563, Sep 2026);
  stopping-binary-tree classes (Gonzalez-MacManus-Pereyra, arXiv:2606.00246v2, Jun 2026); Upper
  bounds via decision trees (Chakraborty-Kulkarni-Lokam-Saurabh, TCS 654 (2016) 92-112; statement
  not re-read here). Lower bound C >= 6.454784 (Hod, arXiv:1711.00762); 6.278 (O'Donnell-Tan).
* Quantum: the quantum FEI conjecture for Pauli spectra of unitary Hermitian operators is false
  (Slote, arXiv:2608.01424, Aug 2026): for each d there is a norm-one Hermitian operator with
  N(d) = exp(Omega(d^2)) Pauli terms, all of degree d and magnitude N(d)^{-1/2}. See Sec. 4.

No universal bound of the form H <= C I psi with psi tensor-sublinear is known; the best universal
bounds are the three incomparable ones above (marginal, KKLMS, certificate/granularity) plus the
trivial level count H <= H(W) + sum_k W_k log2 binom(n,k).

Granularity proof (included for completeness; KNOWN): let F = (1 - f)/2 in {0,1} with deg F = d.
Its multilinear representation in 0/1 variables y_i = (1 - x_i)/2, F(y) = sum_T c_T prod_{i in T} y_i,
has integer coefficients c_T (Moebius inversion of integer values) and degree d. Substituting
prod_{i in T} y_i = 2^{-|T|} sum_{S subset T} (-1)^{|S|} chi_S gives Fhat(S) in 2^{-d} Z, hence
fhat(S) in 2^{1-d} Z for all S. So nonzero p_S >= 4^{1-d}, |supp p| <= 4^{d-1}, H <= 2(d - 1).

## 4. A meta-obstruction from the quantum counterexample (NEW to the campaign ledger)

**Facts (KNOWN).** (a) Slote, arXiv:2608.01424 (2 Aug 2026), Theorem 1 and Theorem 5: for each
d >= 1 there is a Hermitian unitary A_d (a quantum Boolean function in the sense of
Montanaro-Osborne, arXiv:0810.2435) on Theta(d 3^{d/2}) qubits, homogeneous of Pauli degree d, with
N(d) = 3^{d^2/4 + Theta(d)} nonzero Pauli coefficients all of magnitude N(d)^{-1/2}. Hence its Pauli
entropy is H = log2 N(d) = Theta(d^2) and its influence is I = sum_P |P| Ahat(P)^2 = d, so the quantum
FEI conjecture (Bu et al. 2024, Conjecture 4 in Slote) fails with H/I = Theta(d). For classical Boolean f
of degree d, granularity gives H <= 2(d-1), so the classical analogue of this growth is impossible.
(b) Quantum-valid tools: Parseval; hypercontractivity/Bonami-type and FKN for qubit
Pauli expansions (Montanaro-Osborne 2010; King 2014 for qubit product channels); KKL, Talagrand and
Friedgut junta theorems for quantum Boolean functions (Rouze-Wirth-Zhang 2022, cited by Slote).

**Mechanism (PROVED; verified numerically in code/slote_check.py for the smallest case).** If
P_1,...,P_L are pairwise anticommuting Hermitian unitaries and B_1,...,B_L are commuting Hermitian
operators with sum_l B_l^2 = I, then A = sum_l P_l (x) B_l satisfies
A^2 = sum_l P_l^2 (x) B_l^2 + sum_{a<b} (P_a P_b + P_b P_a) (x) B_a B_b = I. Slote takes B_l diagonal
(classical real functions of degree k, Golay-Hadamard type, flat on L^k characters) with only the
pointwise identity sum_l B_l(x)^2 = const. The anticommuting labels P_l make the coherent sum unitary
with no interference cost. This is exactly the campaign's obstruction X006/X013/C033/C034 (coherent
real superpositions are not Boolean), now realised by a genuinely "Boolean" (A^2 = I) object.

**Consequence (meta-obstruction, PROVED as a logical statement).** Let a proof strategy use only
ingredients that remain true when (classical Boolean f, Walsh law p) is replaced by (quantum Boolean
A, Pauli law p_P = Ahat(P)^2, with |P| = number of non-identity sites). Then its conclusion holds for
A_d, so the conclusion cannot be H <= C I, nor any bound H <= C sum_P p_P psi(|P|) + C I with
psi(d) = o(d). In particular:
* KKLMS Theorem 1.3 (psi = log(d+1)) is FALSE for quantum Boolean functions, so its proof
  necessarily uses a classical-only ingredient (it does: Boolean random restrictions f_{J->z} and the
  {0,+-1/2}-valuedness of classical derivatives in ||d_i f||_{4/3} <= 2 I_i^{3/4}).
* Hypercontractivity, LSI, KKL/Talagrand/Friedgut-type estimates, Parseval and operator Booleanity
  A^2 = I together cannot prove FEI. Any proof must use at least one classical-only ingredient in an
  essential way: physical restrictions being Boolean, integrality/granularity of Walsh coefficients,
  pointwise sign structure (derivatives in {0,+-1}, autocorrelation as an average of cut metrics),
  or the full commutative signed Booleanity sum_S a_S a_{S xor U} = 1[U = empty] for all U (C007),
  in particular the all-shift row identities sum_T g_T(x) g_{T xor U}(x) = 0 (U != empty) of RM sec.9.3,
  which encode the commutation of address characters that Slote's anticommuting labels violate.
* Practical falsifier for the fleet (X-Q): before investing in a universal argument, check whether
  every step survives the replacement f -> quantum Boolean A. If it does, the argument is wrong.
  The pointwise-norm-only row relaxation (sum_T g_T(x)^2 = 1 with no U != empty shifts) is already
  refuted classically by X006; the quantum example shows that adding operator Booleanity does not help.

What this does NOT say: it does not refute any classical inequality, and it does not decide which
classical-only ingredient suffices. It locates the missing inequality (M) on the commutative side:
in Corollary C1 terms, FEI fails only through locally product-like spectra; Slote's operators are
flat on a structured family (per data block a one-hot choice), and the classical obstacle to copying
them is that addressing must be done with commuting projections whose label entropy is paid by
physical influence (C010/C011/C035).

## 5. NEW: the granularity bound and the upward functional U (main new contribution)

Notation: pi(S) = sum_{T superset of S} p_T (the upper-set mass; pi(S) = E[(d_S f)^2] is the
generalized influence I_S of KKLMS, where d_S f(z) = fhat_{S,z}(S) is the top Walsh coefficient of
the restriction of f to the live set S with the other coordinates fixed to z). Define the
**upward functional**
  U(f) = sum_{S} p_S log2( pi(S)/p_S ) = E_{S ~ p} log2( E[(d_S f)^2] / (E d_S f)^2 )
(sum over all S with p_S > 0, the empty set included: its term is p_empty log2(1/p_empty); d_empty f = f).
U >= 0, U <= H (since pi <= 1), U = 0 on constants, U is additive on disjoint tensor products (p and pi factor),
U = 0 for every function whose spectrum is an antichain (e.g. homogeneous degree), and in words
U(f) = E log2(1 + Var_z(d_S f)/(E_z d_S f)^2): the log coefficient of variation of the S-derivative.

### Theorem G (granularity bound) - PROVED
For every Boolean f,
  H(f) <= 2 (I(f) - Var(f)) + 2 U(f) - (1 - Var) log2( 1/(1 - Var) )  <=  2 I(f) + 2 U(f).

*Proof.* Fix S != empty with p_S > 0 and put v(z) = d_S f(z) = fhat_{S,z}(S), z in {-1,1}^{S^c}.
(a) v(z) = 2^{-|S|} sum_{y in {-1,1}^S} f(y,z) chi_S(y) is 2^{-|S|} times a sum of 2^{|S|} terms +-1,
which is an even integer; so v(z) is an integer multiple of 2^{1-|S|} and v(z)^2 >= 4^{1-|S|} whenever v(z) != 0.
(b) E_z v = fhat(S) (average the definition over z) and, by Parseval in z, E_z v^2 = pi(S).
(c) With phi = P(v != 0): from (a), pi(S) >= 4^{1-|S|} phi; by Cauchy-Schwarz,
p_S = (E[v 1_{v != 0}])^2 <= pi(S) phi. So pi(S)^2 >= 4^{1-|S|} p_S, i.e.
  log2(1/pi(S)) <= (|S| - 1) + (1/2) log2(1/p_S).
Now H = sum_S p_S log2(1/pi(S)) + U. The empty set has pi = 1, so summing (c) over S != empty,
sum_S p_S log2(1/pi(S)) <= (I - Var) + (1/2)(H - p_empty log2(1/p_empty)). Hence
H/2 <= (I - Var) - (1/2) p_empty log2(1/p_empty) + U, which is the first inequality. QED

Checks (EVIDENCE, code/upward.py, code/families.py): holds with minimum slack 0 over all Boolean
functions with n <= 4; equality for 2-bit bent functions and for every addressing function tested
(a = 1,2,3); ratio (2(I-Var)+2U)/H between 1.00 and 1.76 on all structured families (point defects 1.06-1.17,
tribes 1.02-1.12). For the r-bit point defect, U/I -> 1 and the bound gives H <= 4I + o(I), matching
H/I -> 4 at leading order.

**Corollary G0 (new FEI-equivalent form).** U <= H <= 2I + 2U, so FEI holds iff sup U/I < infinity,
with C_FEI <= 2 + 2 sup(U/I) and sup(U/I) <= C_FEI. By Hod's lower bound, sup U/I >= (6.4548 - 2)/2 = 2.227.
EVIDENCE: all n <= 4: max U/I = 1.465; truth-table families <= 1.79 (maj3 o maj3 o AND2). On near-extremal
read-once AND/OR formulas found by a beam search with the exact composition recursion
(code/compose_rec.py, readonce_beam.py), H/I = 3.40, 3.89, 4.40, 4.74, 5.08, 5.29, 5.51, 5.66, 5.81, 5.91 with
U/I = 1.47 ... 2.06, and H/(2(I-Var)+2U) = 0.852, 0.893, 0.921, 0.942, 0.953, 0.963, 0.971, 0.978, 0.982, 0.986:
Theorem G becomes asymptotically TIGHT on the extremal read-once family. So the FEI constant problem is,
on that family, exactly the problem sup U/I, and C_FEI = 2 + 2 sup(U/I) is plausible.

**Composition formula (PROVED).** For a read-once composition f = g(h_1,...,h_k) with independent inner
functions of means mu_j, the spectral law is P_g^mu(J) prod_{j in J} q_j(T_j) (P_g^mu = squared mu-biased
Fourier law of g, q_j = nonempty-normalised spectral law of h_j); upper sets factor the same way, so
U(f) = U(P_g^mu) + sum_j P(j in J) U(q_j), exactly parallel to H(f) = H(P_g^mu) + sum_j P(j in J) H(q_j) and
I(f) = sum_j P(j in J) E_{q_j}|T|. (Checked against brute force to 1e-9 on chains of length 8.)

Meaning of Theorem G: it is classical-only (it uses integrality of Walsh coefficients of restrictions)
and it exactly kills the obstruction that Corollary C1 isolated. For a product law with marginals
theta_i, pi(S)/p_S = prod_{i not in S} (1-theta_i)^{-1}, so U ~ I log2 e while H ~ sum theta_i log(1/theta_i):
by Theorem G no Boolean spectrum is "product-like with small marginals" in the upper-set sense
(a robust, quantitative replacement for the exact product rigidity C016). The quantum operators of
Sec. 4 are homogeneous, so U = 0 for them, and Theorem G fails for them, as it must.

**Corollary G1 (a level-only universal bound) - PROVED.** Jensen within each level gives
U <= H(W) + sum_k W_k log2 m_k with W_k = P(|S| = k) and binomial moments m_k = E[binom(|S|, k)], so
  H(f) <= 2 (I(f) - Var(f)) + 2 H(W) + 2 sum_{k>=1} W_k log2 E_p[ binom(|S|, k) ].
This depends only on the law of |S|. It is new as far as I know; it replaces n by the random spectral
size in the trivial level count, recovers H <= 2(d-1) for homogeneous degree d, and equals Theorem G for
symmetric functions (there U is exactly the level expression), so it is O(I) for majority and point
defects. EVIDENCE (code/levelbounds.py): bound/I = 3.51, 4.14, 4.85 on tribes 3x4, 4x4, 2x8 (H/I = 3.13,
3.44, 4.33), 4.05 on maj13, 4.15 on pd12. It is NOT tensor-stable: for f = (x1 x2) (x) (activated parity on
D bits with p = 1/D) the right side is ~ 2 log2 D with I ~ 3, while U itself is O(1) (the symmetrisation
loses). So it is incomparable with KKLMS (both lose log D on that example).

**Corollary G2 (a tensor-stable level-only bound) - PROVED.** For any lambda > 0, Gibbs' inequality with the
weights c(S) = pi(S) lambda^{|S|}, whose total is sum_S c(S) = E(1+lambda)^{|S|}, gives
U <= log2 E_p[(1+lambda)^{|S|}] + I log2(1/lambda), hence
  H(f) <= 2(I - Var) + 2 inf_{lambda>0} [ log2 E_p (1+lambda)^{|S|} - I log2 lambda ]
(lambda = 1: H <= 2I + 2 log2 E[2^{|S|}]). Both terms are additive under tensor powers for fixed lambda.
It gives O(I), with constant about 4, whenever |S| has light upper tails relative to its mean (homogeneous:
the bound tends to 2(d-1) as lambda -> infinity), and it is weak (I log n) for majority. G1 and G2 are
incomparable; both are weaker than U itself.

### 5.1 Local structure of U under physical restriction - PROVED identity, EVIDENCE for bounds
Fix a coordinate i; for T in [n]\{i} put u_T = fhat(T), v_T = fhat(T+i), m_T = u^2 + v^2, s_T = v^2/m_T,
pi(T) as above (in [n]), V(T) = sum_{T' sup T} v_{T'}^2 = pi(T+i), r_T = V(T)/pi(T),
eta_T = 2 u_T v_T / m_T, C(T) = sum_{T' sup T} u_{T'} v_{T'}, x_T = 2 C(T)/pi(T).
Then (eta_T, x_T) are the asymmetries of the T-coefficient and of the T-upper-set mass between the two
restrictions: eta_T = (p^+_T - p^-_T)/(p^+_T + p^-_T), x_T = (pi^+(T) - pi^-(T))/(pi^+(T) + pi^-(T)).

**Identity (Theorem U-loc).** Delta_i U := U(f) - (U(f_{i,+}) + U(f_{i,-}))/2 equals
  sum_T m_T [ s_T log2(r_T/s_T) + (1 - s_T) log2(1/(1 - s_T)) + D2( (1+eta_T)/2 || (1+x_T)/2 ) ],
with D2 the binary KL divergence in bits (T = empty included; U as defined above). Equivalently
Delta_i U = B_i - Gamma_i + sum_T m_T D2(.||.), Gamma_i = sum_{S containing i} p_S log2(pi(S\i)/pi(S)).
*Proof sketch, all steps elementary:* split U(f) over T and T+i, write p_T log(pi/p_T) + p_{T+i} log(V/p_{T+i})
= m_T h(s_T) + m_T log(pi/m_T) - p_{T+i} log(pi/V); for the restrictions use p^+-_T = m_T(1 +- eta_T),
pi^+-(T) = pi(T)(1 +- x_T); the difference of the pi-terms is m_T [ (1/2)(1+eta)ln((1+eta)/(1+x)) +
(1/2)(1-eta)ln((1-eta)/(1-x)) ] - m_T * JS-term, and the JS terms cancel against the entropy terms.
Verified to 1e-10 against direct restriction on random tables (code/dU_exact.py).

Key effect: B_i - Gamma_i = sum_T m_T [s log(r/s) + (1-s) log(1/(1-s))]: the local logarithm of B_i
(the obstruction X003/X009, B_i/Inf_i ~ log(1/Inf_i)) is refunded by Gamma_i whenever the
exact conditional probability s_T of i is comparable to the upper-set probability r_T.

EVIDENCE (code/x003_scan.py, stress_dU.py): on the campaign falsifiers the selector coordinate has
  X003 (k = 4,6,8,10): Delta_y H/Inf_y = 8.33, 10.35, 12.34, 14.33 (grows ~ k) but Delta_y U/Inf_y = 3.69, 4.10, 4.25, 4.30;
  X009 (m = 4..12): Delta_t H/Inf_t = 8.0 ... 16.3, Delta_t U/Inf_t = 3.57 ... 4.31;
  X002 (m = 3..11): Delta_s U/Inf_s -> 3.0 (Delta H/Inf = 4).
So U is immune to the sparse-activation local-log obstruction that kills every local charge for H.

REFUTED-direction evidence (universal local form): the statement "Delta_i U <= K Inf_i for EVERY i"
is not supported: annealing over selector pairs f = (y ? g : h) gives max Delta_y U/Inf_y = 4.78, 5.11,
5.48, 6.15 at n = 6, 7, 8, 9 (data/anneal_sel*.json), dominated by the KL term (asymmetry mismatch).
Not a proof of unboundedness; recorded as a failed route.

### 5.2 A global sufficient condition (CONJECTURE GU, strong numerical support)
Let G(f) = sum_i Delta_i U(f). If G(f) <= K I(f) for every Boolean f, then every nonconstant f has a
relevant i with Delta_i U <= K Inf_i (irrelevant coordinates have Delta_i U = 0), so U <= K I by restriction
induction (U = 0 on constants), and by Theorem G, H <= (2 + 2K) I: FEI with C <= 2 + 2K.
EVIDENCE (code/globalU.py, anneal_G.py, sweepG*.py): max G/I = 2.75 over all n <= 4; annealing n = 5..8
finds 2.8203 (a 5-variable function, Walsh values in {+-4, +-12}/32, every local ratio >= 2.546) and nothing
larger at n = 6, 7, 8; compositions: maj3 o g5 3.090, and2 o g5 2.965, or3 o g5 2.959, and3 o g5 2.806,
and4 o g5 2.727; tribes <= 2.19; lexicographic (Hod-type) <= 2.19; LTFs <= 2.21; random n=12 ~ 1.0;
majority, addressing, recursive majority negative. With K = 3.09 the implied FEI constant would be 8.18,
consistent with Hod's 6.4548 lower bound. On the near-extremal read-once AND/OR formulas of the beam search
(exact recursion including leaf restrictions, code/readonce_G.py, readonce_G2.py), G/I = 1.94, 2.00, 2.20,
2.20, 2.26, 2.26, 2.285, 2.285 at H/I = 4.40, 4.74, 5.08, 5.29, 5.51, 5.66, 5.81, 5.91 (sizes 16..2048, U/I up to
2.06): it plateaus near 2.29 on the FEI-extremal family, below the overall maximum 3.09; note 2 + 2(2.29) = 6.58
against Hod's 6.4548. This is EVIDENCE only;
GU is stronger than FEI (it implies FEI but is not known to follow from it).

A weaker sufficient form (GU'): G <= a I + b U with some b < 1. Induction: choose i with
Delta_i U <= (a + b U(f)/I(f)) Inf_i (exists since G <= (a + bU/I) I); then
U(f) <= (a + b U(f)/I) Inf_i + K (I - Inf_i), which gives U(f) <= K I whenever K >= a/(1 - b). (With H in place
of U one needs b < 1/2, by Theorem G.) For comparison, the H-analogue is exactly at the threshold:
sum_i Delta_i H = B + sum JS_i <= H + (2/ln2) I (b = 1), which is why plain restriction induction on H cannot
close. EVIDENCE n <= 4: G <= 1.75 I + U, G <= 2.25 I + 0.5 U, G <= 0.75 I + H, G <= 1.5 H (code/GvsU.py).

### 5.3 The key lemma in its cleanest form, and chain rules (PROVED)

**Lemma G-key.** For every Boolean f and every nonempty S: |fhat(S)| <= 2^{|S|-1} I_S(f), where
I_S(f) = pi(S) = sum_{T sup S} fhat(T)^2 = E[(d_S f)^2] (KKLMS's generalized influence).
Equivalently p_S <= 4^{|S|-1} pi(S)^2. *Proof:* d_S f(z) = 2^{-|S|} sum_{y in {-1,1}^S} f(y,z) chi_S(y) is
2^{-|S|} times a sum of 2^{|S|} terms +-1, an even integer, so d_S f(z) in 2^{1-|S|} Z; hence
|d_S f| <= 2^{|S|-1} (d_S f)^2 pointwise, and |fhat(S)| = |E d_S f| <= E|d_S f| <= 2^{|S|-1} E(d_S f)^2. QED
For |S| = 1 this is the classical |fhat(i)| <= Inf_i. Exact integer check: no violation among all
984,884 pairs (f,S) with n <= 4 (266,492 equalities) and 63,028 pairs from 300 random/sparse f with
n = 5..9 (code/check_Gkey.py). Theorem G is Lemma G-key plus the identity H = E log(1/pi(S)) + U.
Equality holds for every S in the spectrum of a point defect (p_S = 4p^2, pi(S) = 2^{1-|S|} 2p).

**Chain rules (for ANY probability law P on subsets, not only Boolean spectra).** Merging coordinate
i (passing to the law m of S \ {i}) leaves upper-set masses of sets not containing i unchanged, and
  H(P) = B_i(P) + H(m),    U(P) = B_i(P) - Gamma_i(P) + U(m),
with Gamma_i(P) = sum_{S contains i} P_S log2( pi_P(S\i)/pi_P(S) ) >= 0. Iterating over any order
i_1,...,i_n, with P_k the law of S cap {i_k,...,i_n},
  H = sum_k B_{i_k}(P_k),  U = sum_k [B_{i_k}(P_k) - Gamma_{i_k}(P_k)],  H - U = E log2(1/pi(S)) = sum_k Gamma_{i_k}(P_k).
(Verified exactly on 8 families, code/chainU.py.) Each step: B_i - Gamma_i = sum_T m_T [s_T log2(r_T/s_T)
+ (1-s_T) log2(1/(1-s_T))], s_T = P(i in S | S\i = T), r_T = P(i in S | S\i sup T). The second part sums
to at most I log2 e over the chain. By Jensen, sum_T m_T s_T log2(r_T/s_T) <= Inf_i log2(Lambda_i/Inf_i) with
  Lambda_i/Inf_i = E_{T ~ law(S\i)} [ P(S\i sup T | i in S) / P(S\i sup T) ]   (an average "lift"),
so U <= I log2 e + sum_k Inf_{i_k} log2( Lambda^{(k)}_{i_k} / Inf_{i_k} ) for every order (marginal laws P_k).
EVIDENCE: this bound is <= 2.21 I on all eight test families, nearly order-independent.

**Structure of Lambda (PROVED).** Write rho(T) = m_T/pi(T) (stopping probability of the merged law m at T)
and R(T') = sum_{T subset T'} rho(T). Then E_m[R] = sum_T rho(T) pi(T) = 1 exactly, and
Lambda_i = sum_T m_T r_T = E_m[s_i R] with E_m[s_i] = Inf_i, so
  Lambda_i - Inf_i = Cov_m(s_i, R),   and   B_i - Gamma_i <= log2(e) Lambda_i
(using s log(r/s) <= (r - s) log2 e and (1-s) log(1/(1-s)) <= s log2 e). In the small-asymmetry regime the
KL term is K_i ~ (log2 e/2) sum_T m_T (eta_T - x_T)^2 with x_T = the m-weighted average of eta over the cone of T,
and by Jensen sum_T m_T x_T^2 <= sum_T m_T eta_T^2 R(T) <= 4 Lambda_i. So, up to the regime |x_T| -> 1 (where
only m_T D <= m_T log2(pi(T)/m_T) is available), the whole local decrement of U is governed by the covariance
under the merged law between "i is likely given S minus i" and "S minus i sits above many stopping points".
EVIDENCE: sum_i Lambda_i / I = 1.00 (bent8), 1.16 (g5, tribes 2x4), 1.49 (n = 9 selector), 1.77 (maj3 o g5),
1.99 (pd10), 2.11 (X003 k = r = 6), 2.26 (maj9) (code/lamsum.py).

### 5.4 What remains, in the U language (the new single missing inequality)
By Theorem G the only missing step for FEI is
  (M_U)  U(f) <= K I(f) for all Boolean f.
Three sufficient forms, in increasing strength, each with numerical support and no known counterexample:
  (a) existential local: every nonconstant f has i with Delta_i U <= K Inf_i;
  (b) global (GU): sum_i Delta_i U <= K I   [max observed 3.090];
  (c) lift form: some marginalization order has sum_k Inf_{i_k} log2(Lambda_k/Inf_{i_k}) <= K I  [max observed 0.77 I, i.e. the full bound I log2 e + sum is <= 2.21 I on the eight test families].
The universal local form (every i) fails numerically (Sec. 5.1). The sparse-activation obstruction X003/X009,
which kills every local charge for H and B, does not affect U: the logarithm is refunded by Gamma.
Unlike FEI itself, (M_U) is not contradicted by the quantum counterexample (U = 0 there), so soft tools
(hypercontractivity, LSI, KKL) are not ruled out for (M_U); the classical-only content of FEI is
exactly Lemma G-key.

## 6. Attempts that failed, each with the witness that kills it

F1. Random restrictions with entropy accounting (Han + E4). Han's inequality psi(t) >= tH and E4 give the
valid universal inequality H(f) <= (1/t) E H(f_{t}) + (2/ln2)((1-t)/t) I (PROVED, Sec. 2.4 proof of C(viii)).
Used inductively it only gives c_n <= c_m + (2/ln2)(n/m - 1), i.e. c_n = O(log n), weaker than the trivial
level count c_n <= log2 n + O(1). Killer: the channel term (2/ln2) I_A is paid at rate 1/t per surviving
coordinate; at t -> 1 the induction is exactly C018 and needs B <= K I.
F2. Per-set minimum of known references (marginal product, level count, KKLMS buckets) by the log-sum
trick: valid (KKLMS sec. 7.1 isolates the k >= 1 buckets with O(I) entropy), but still loses log log n on tribes
and log n on maj (x) tribes; no new mechanism.
F3. "Beat subadditivity by a constant factor", H <= theta sum_i h(Inf_i) + K I with theta < 1 (equivalently
H <= A(I + TC)): implied by FEI, known only with an extra I log(1+I) (RM sec. 11.16 via KKLMS). The size statistic
gives TC >= D(P_N || Q_N) >= ~ I log(Lambda/(e I^2)) with Lambda = sum Inf_i ln(1/Inf_i), logarithmic only; tribes
has TC ~ I log n invisible to |S|. Not FEI-equivalent (critical functions have large TC), so not pursued.
F4. Transport-entropy (Marton/Talagrand T1 for product Bernoulli laws) lower bounds on TC are quadratic:
TC >~ W_1^2/(2I) ~ I/2 on tribes, far from the needed I log n.
F5. Log-Sobolev on each derivative: Inf_i ln(1/Inf_i) <= 2 sum_{S contains i} (|S|-1) p_S, hence
H <= (2/ln2) E[|S|(|S|-1)] + I log2 e (quadratic, KNOWN-type); the per-coordinate version cannot beat
log(1/Inf_i) because of X003 (B_y/Inf_y ~ k with E[|S| | y in S] ~ 1.5k).
F6. Fixed-order Renyi with normalisation: H_alpha(P | S nonempty) <= C Itilde fails for every alpha < 1 by tensor
powers of point defects (SEED sec. 3: H_alpha/I -> infinity for the point defect, tensor power keeps Var -> 1).
F7. Pivotal-set entropy H(Piv(x)) <= C I is false: for the r-bit point defect H(Piv) ~ r^2 2^{-r} while
I = 2r 2^{-r}, ratio r/2 -> infinity.
F8. Level-only symmetrised bound (Cor. G1) as a route to FEI: not tensor-stable, witness (x1 x2) (x) activated
parity (bound ~ 2 log2 D, I ~ 3).
F9. Universal local inequality for U (Delta_i U <= K Inf_i for every i): ratios 4.78 -> 6.15 for n = 6 -> 9
(Sec. 5.1); the existential and global forms remain open and supported.
F10. Sign-coherence of derivatives: if every d_S f has constant sign, Paley-Zygmund and granularity give
log(pi/p) <= 2(|S|-1) + log(1/pi(S)), which only returns U <= (I - Var) + H/2 and, with Theorem G, nothing.

## 7. The single most promising next step for the fleet

Work with U instead of H. By Theorem G, FEI is exactly (M_U): U(f) <= K I(f), and the classical-only
input is already spent in Lemma G-key. The exact restriction identity
  Delta_i U = B_i - Gamma_i + K_i,   K_i = U(law of S minus i) - (U(f_{i,+}) + U(f_{i,-}))/2 >= 0,
shows that the local logarithm (the X003/X009 obstruction for H and B) cancels in B_i - Gamma_i, which is
<= Inf_i log2 e + sum_T m_T s_T log2(r_T/s_T). What remains is the KL asymmetry term K_i, the concavity gap of U
when the two restriction spectra are merged. Concretely: prove sum_i Delta_i U <= a I + b U for some b < 1
(GU', Sec. 5.2), or the existential local form, e.g. by bounding sum_i K_i through the upper-set correlations
C_i(T) = sum_{T' sup T} fhat(T') fhat(T'+i) = (I_T(f_{i,+}) - I_T(f_{i,-}))/4 (note C_i(empty) = 0 is exactly a
Booleanity identity). Because (M_U) is not contradicted by the quantum counterexample (U = 0 there), soft
tools (hypercontractivity of d_S f, log-Sobolev on upper-set masses, semigroup interpolation) are admissible
for this step. Test any candidate first on: maj3 o g5 (G/I = 3.09), the n = 9 selector pair (local 6.15), and
the near-extremal read-once formulas (G/I ~ 2.26, U/I ~ 2.0); code in code/.
