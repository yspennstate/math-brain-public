# B12 FEI spectral-sample compression — death-chain Green kernel and amortized selector information

TASK: B12 ACCOUNT: account02 RUN: 2026-09-21T13:51:26.509051Z  
CURRENT WORK: random-order spectral-sample death chain, exact hazard/selector information split, and the remaining amortized selector target  
ROLE: FEI approach 1 — spectral-sample compression / sequential prediction  
EXECUTION: WITHOUT_VERIFIED_BRAIN  
STATUS: **FULL FEI REMAINS OPEN.** This report gives exact reformulations, a universal payment for the spectral-size/hazard part, and two Boolean counterexamples to stronger local bridges. It does not claim a universal selector bound, FEI closure, or novelty/priority.

## 0. Fresh dependencies, scope, and research moves

The required FEI entry was read in the owner-prescribed order: `TASKS_2026-09-21.md`, the certified read-once `REPORT.md`, `APPROACHES.md`, then the fresh `proofnet24/P03-fei/README.md`. I also recovered the immediate predecessor
`account02/B12/20260921T125427Z-terminal-shadow-equivalence/REPORT.md`
and the active sprint directive. The sprint contains an older slot-local B12 numerical subassignment, but the present direct owner task assigns this worker to approach 1 (spectral-sample compression / sequential prediction); I therefore continue the current B12 route rather than duplicate the read-once region-2 work.

The current neighboring account02 FEI scopes remain complementary: B13 Booleanity/block profiles, B14 existential restriction/erasure, B15 arithmetic remainder, B16 signed transport, B17 new mechanisms, and B18 integration. Here “selector” means the **next element of a random ordering of the spectral sample**, not B14's existential coordinate selector.

This run used three different FLEET_RULES moves from the predecessor: **#2 attack the negation first** (AND and tribes kill two tempting pointwise information charges), **#5 add a parameter and differentiate in it** (continuous-time independent thinning/noise gives a Green-kernel formula for the shadow), and **#20 find why the algorithm fails** (naive local per-step coding fails; only an amortized continuation-Palm statement can remain).

Fresh literature checks before any novelty claim found: Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45 (2025); González–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (2026), using stopping binary trees; and Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563 (submitted 2026-09-18), proving structured plateaued/partially-bent cases. None of these sources as retrieved states a proof of full FEI. I make no claim that the random-order identities below are new to the literature without a full paper-level comparison.

## 1. Setup and the predecessor's shadow

Let
\[
p_B=\widehat f(B)^2,\qquad \sum_Bp_B=1,\qquad
K=|S|\quad(S\sim p),\qquad I=\mathbb E K.
\]
For every \(A\subseteq[n]\), \(a=|A|\), define the uniform-prefix shadow
\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{a}}.
\tag{1}
\]
The predecessor proved
\[
R_{\rm seq}=-\sum_Ap_A\log_2v_A,\qquad
H=B_{\rm sh}+R_{\rm seq},
\]
and
\[
B_{\rm sh}\le \log_2(1+I).
\tag{2}
\]
It also identified \(v_A\) as a mixed Shapley/martingale interaction and showed that the sharp constant for \(R_{\rm seq}\le C I\) is exactly the full FEI constant. The unresolved issue was to find a genuinely sequential payment that survives both tiny AND atoms and selector transfer.

## 2. Exact death-chain / Green-kernel interpretation of \(v_A\)

Draw \(B\sim p\). Starting from \(B\), let every present coordinate die after an independent rate-one exponential time. Equivalently, delete the elements of \(B\) in a uniformly random order.

For fixed \(A\subseteq B\), the death chain ever visits \(A\) iff every element of \(B\setminus A\) is deleted before any element of \(A\). Among the \(\binom{|B|}{a}\) possible sets of the last \(a\) survivors, each is equiprobable. Hence
\[
\Pr_B(\text{death chain hits }A)=\frac1{\binom{|B|}{a}},
\]
and averaging over \(B\),
\[
\boxed{v_A=\Pr_{S\sim p}(\text{death chain ever hits }A).}
\tag{3}
\]

Let \(q_t(A)\) be the law of the death chain at time \(t\). A nonempty state \(A\) of size \(a\) has holding time of mean \(1/a\) and can be visited at most once, so
\[
\boxed{v_A=a\int_0^\infty q_t(A)\,dt,\qquad a\ge1.}
\tag{4}
\]
Writing \(s=e^{-t}\), independent thinning with survival probability \(s\) gives
\[
q_s(A)
=s^a\sum_{B\supseteq A}p_B(1-s)^{|B|-a},
\]
and therefore
\[
\boxed{v_A=a\int_0^1 q_s(A)\,\frac{ds}{s}.}
\tag{5}
\]

There is also a direct Fourier-noise form. For the normalized discrete derivative \(D_A\), whose Fourier coefficient on \(D\subseteq A^c\) is \(\widehat f(A\cup D)\),
\[
\|T_{\sqrt r}D_Af\|_2^2
=\sum_{D\subseteq A^c}p_{A\cup D}r^{|D|}.
\]
The beta integral yields
\[
\boxed{
v_A
=a\int_0^1(1-r)^{a-1}
\|T_{\sqrt r}D_Af\|_2^2\,dr
\quad(a\ge1).
}
\tag{6}
\]
Thus the prefix shadow is literally a Green potential of Boolean random restriction / noise energy, not merely a combinatorial sum.

## 3. The exact random-order transition law

Now run the same process forward as a random-order reveal. Draw the terminal spectral set \(B\sim p\), choose a uniformly random ordering of its elements, and reveal one coordinate at a time. If the current unordered prefix is \(A\) with \(|A|=a\), then the probability of having reached \(A\) is exactly \(v_A\).

The posterior law of the terminal set is
\[
w_A(B)
=\Pr(B\mid A\text{ is the first }a\text{-set})
=\frac{p_B}{\binom{|B|}{a}v_A},
\qquad B\supseteq A.
\tag{7}
\]
In particular the stopping probability is
\[
t_A:=\Pr(B=A\mid A)=\frac{p_A}{v_A},
\qquad
u_A:=1-t_A=\frac{v_A-p_A}{v_A}.
\tag{8}
\]

The shadow satisfies the exact recurrence
\[
\sum_{i\notin A}v_{A\cup\{i\}}
=(a+1)(v_A-p_A),
\tag{9}
\]
because a strict superset \(B\supsetneq A\) contributes
\[
\frac{|B|-a}{\binom{|B|}{a+1}}
=\frac{a+1}{\binom{|B|}{a}}.
\]
Hence the unconditioned probability that the next outcome is coordinate \(i\notin A\) is
\[
q_A(i)=\frac{v_{A\cup\{i\}}}{(a+1)v_A},
\tag{10}
\]
with
\[
t_A+\sum_{i\notin A}q_A(i)=1.
\]
Conditioned on continuing, the next-coordinate distribution is
\[
r_A(i)
=\frac{v_{A\cup\{i\}}}{(a+1)(v_A-p_A)}.
\tag{11}
\]

Given the terminal \(B\supsetneq A\), however, the next coordinate is simply uniform on \(B\setminus A\). Therefore the extra information in the next coordinate about the whole terminal set is
\[
\boxed{
j_A
:=I\!\left(B;X_{a+1}\mid A,\ B\ne A\right)
=H(r_A)
-\mathbb E\!\left[\log_2(|B|-a)\mid A,\ B\ne A\right].
}
\tag{12}
\]
It is automatically nonnegative.

## 4. Exact hazard + selector decomposition of Fourier entropy

Let the local outcome be either STOP or the next coordinate. Its entropy is
\[
h_2(u_A)+u_AH(r_A).
\]
Conditioned on the terminal set \(B\), there is no uncertainty at STOP and, on continuation, exactly \(\log_2(|B|-a)\) bits of random-permutation noise.

The full ordered reveal transcript determines \(B\), and conditioned on \(B\) its only randomness is the uniform ordering, of entropy \(\log_2|B|!\). Subtracting this permutation noise in the chain rule gives the exact identity
\[
\boxed{
H(f)
=
\underbrace{\sum_A v_A h_2(u_A)}_{\mathcal H_{\rm haz}}
+
\underbrace{\sum_A(v_A-p_A)j_A}_{\mathcal H_{\rm sel}}.
}
\tag{13}
\]
I call the two terms **hazard information** and **selector information**.

Also
\[
\sum_A(v_A-p_A)
=\left(\sum_Av_A\right)-1
=I,
\tag{14}
\]
so
\[
\mu(A):=\frac{v_A-p_A}{I}
\tag{15}
\]
is a probability law whenever \(f\) is nonconstant. It has a direct sampling interpretation:

1. draw \(B\) from the size-biased spectral law \(|B|p_B/I\);
2. choose \(a\) uniformly from \(\{0,\ldots,|B|-1\}\);
3. choose a uniformly random \(a\)-prefix of a uniformly random ordering of \(B\).

Then \(A\sim\mu\). Consequently
\[
\boxed{
\mathcal H_{\rm sel}
=I\,\mathbb E_{A\sim\mu}j_A.
}
\tag{16}
\]
This is the cleanest sequential target I found: **average information revealed by the next random spectral coordinate at a uniformly sampled continuation event**.

## 5. The hazard part is already universally payable: \(\mathcal H_{\rm haz}\le3I\)

First,
\[
\boxed{\mathcal H_{\rm haz}\le H(K).}
\tag{17}
\]
Reason: interleave the STOP/CONTINUE bits with the revealed coordinate identities. The hazard term is exactly the sum of conditional entropies of the STOP/CONTINUE decisions. These bits reveal information only about the stopping time \(K\). The coordinate identities can themselves reveal additional information about \(K\), so by the chain rule/data processing the total information assigned to the stop bits cannot exceed \(H(K)\).

For completeness this can also be seen by comparing two entropy expansions of the random ordered path. Write
\[
\operatorname{Coord}
=\sum_A(v_A-p_A)H(r_A).
\]
Then
\[
H(\text{path})=\mathcal H_{\rm haz}+\operatorname{Coord}.
\]
On the other hand
\[
H(\text{path})=H(K)+H(X_1,\ldots,X_K\mid K).
\]
Conditioning the next coordinate on the exact \(K\) cannot increase its entropy compared with conditioning only on survival \(K>a\), hence
\[
\operatorname{Coord}\ge H(X_1,\ldots,X_K\mid K),
\]
which proves (17).

Now use Booleanity only to control \(H(K)\). Put
\[
V=\Pr(K>0)=1-\widehat f(\emptyset)^2=\operatorname{Var}(f).
\]
Then
\[
H(K)=h_2(V)+V H(K\mid K>0).
\tag{18}
\]
For any positive-integer random variable \(L\),
\[
H(L)\le\mathbb E L
\tag{19}
\]
in bits: compare its law to the prefix code distribution \(2^{-k}\), \(k\ge1\), via nonnegativity of KL divergence. Hence the second term in (18) is at most \(I\).

For a Boolean \(f\in\{\pm1\}\), let
\[
\alpha=\min\{\Pr(f=1),\Pr(f=-1)\}\le\frac12.
\]
Then \(V=4\alpha(1-\alpha)\), and the edge-isoperimetric inequality gives
\[
I\ge 2\alpha\log_2\frac1\alpha.
\tag{20}
\]
Moreover
\[
h_2(V)\le4\alpha\log_2\frac1\alpha.
\tag{21}
\]
A short proof of (21): if \(\alpha\le1/8\), then \(V\le4\alpha\le1/2\),
\[
h_2(V)\le h_2(4\alpha)
\le4\alpha\log_2\frac{e}{4\alpha}
\le4\alpha\log_2\frac1\alpha
\]
because \(e<4\). If \(\alpha\in[1/8,1/2]\), then \(h_2(V)\le1\), while
\(4\alpha\log_2(1/\alpha)\ge1\) on this interval.

Combining (18)--(21),
\[
\boxed{H(K)\le3I,\qquad \mathcal H_{\rm haz}\le3I.}
\tag{22}
\]
Thus the AND-type “rare survival” obstruction is globally paid without solving FEI.

Together with (13) and (16),
\[
\boxed{
H(f)\le 3I(f)+I(f)\,\mathbb E_{\mu}j_A.
}
\tag{23}
\]
So full FEI is equivalent, up to an additive 3 in the constant, to a dimension-free bound on the continuation-Palm average \(\mathbb E_\mu j_A\).

In fact the **sharp supremum constant** for \(\mathcal H_{\rm sel}/I\) equals the sharp FEI constant. One direction is immediate from \(\mathcal H_{\rm sel}\le H\). For the reverse direction, use the predecessor's balanced lift and disjoint recursive amplification of any nonconstant \(f\): along that sequence \(I_r\to\infty\) and \(H_r/I_r\to H(f)/I(f)\). For every nonnegative integer \(K\) of mean \(I_r\), the geometric maximum-entropy bound gives
\[
H(K)\le (I_r+1)\log_2(I_r+1)-I_r\log_2 I_r=O(\log I_r),
\]
so \(\mathcal H_{\rm haz}/I_r\to0\). Hence
\[
\sup_f\frac{\mathcal H_{\rm sel}(f)}{I(f)}
=
\sup_f\frac{H(f)}{I(f)}.
\tag{24}
\]
This is a reformulation, not a solution: the selector average carries the full sharp difficulty after amplification.

## 6. Two strong local bridges are false

### 6.1 AND kills a pointwise hazard charge

A tempting local inequality would be
\[
h_2(u_A)\le C u_A
\tag{25}
\]
at every prefix. It is false even for Boolean functions.

Take \(AND_n\) in \(\{\pm1\}\) normalization (one minority point). At the root \(A=\emptyset\),
\[
u_\emptyset=V=4\cdot2^{-n}(1-2^{-n}),
\]
so
\[
\frac{h_2(u_\emptyset)}{u_\emptyset}
=n-2+\log_2 e+o(1)\to\infty.
\tag{26}
\]
The checker gives ratios \(3.35,7.44,11.44,15.44,19.44,31.44\) for
\(n=4,8,12,16,20,32\). Thus a local continuation charge cannot pay rare survival. Equation (22) shows why the global size/hazard payment succeeds anyway.

### 6.2 Balanced tribes kills a uniform pointwise selector bound

After removing the hazard obstruction one might hope for
\[
j_A\le C
\tag{27}
\]
at every continuing prefix. This is also false for Boolean functions.

Take the standard transitive tribes function with \(m\) tribes of width \(w\),
\(n=mw\), and
\[
q=(1-2^{-w})^m
\]
the probability no tribe fires. Then
\[
V=4q(1-q),\qquad
I=mw\,2^{-(w-1)}(1-2^{-w})^{m-1}.
\tag{28}
\]
At the root, variable transitivity makes the conditional next-coordinate law exactly uniform on the \(n\) physical coordinates. Therefore
\[
j_\emptyset
=\log_2n-\mathbb E[\log_2 K\mid K>0].
\]
By Jensen,
\[
\boxed{
j_\emptyset
\ge \log_2\frac{nV}{I}
=\log_2\!\left(2^{w+1}(1-2^{-w})(1-q)\right).
}
\tag{29}
\]
Choose \(m\) to be the nearest integer to
\(\log(1/2)/\log(1-2^{-w})\), so \(q\to1/2\). Then
\[
j_\emptyset\ge w-o(1)\to\infty.
\tag{30}
\]
The executed formula checker gives lower bounds
\(3.9307,5.9770,7.9938,9.9980,11.9997,15.99998,19.999998\)
at \(w=4,6,8,10,12,16,20\).

Thus **both** natural pointwise bridges fail:
- AND: local stop/survival information per continuation is unbounded;
- tribes: local next-coordinate selector information is unbounded.

The only surviving statement of this form is necessarily **amortized across prefixes** under the continuation-Palm measure \(\mu\).

## 7. Exact remaining approach-1 target

Define
\[
\mathsf{Sel}(f)
:=\sum_A(v_A-p_A)\,
I(B;X_{|A|+1}\mid A,\ B\ne A).
\tag{31}
\]
Then
\[
H(f)=\mathcal H_{\rm haz}(f)+\mathsf{Sel}(f),
\qquad
0\le\mathcal H_{\rm haz}(f)\le3I(f),
\tag{32}
\]
and the sharp constant of \(\mathsf{Sel}(f)\le C I(f)\) is the full FEI sharp constant.

Equivalently, the unresolved universal statement is
\[
\boxed{
\mathbb E_{A\sim\mu}
I(B;X_{|A|+1}\mid A,\ B\ne A)
\le C
}
\tag{33}
\]
for the size-biased uniformly sampled continuation prefix \(A\).

Equation (33) is not a cosmetic reparametrization in the sense of the failed local routes: it has removed the globally payable size/hazard entropy and exactly identifies the unpaid **coordinate-identity information** at a random continuation. But by (24), proving it still requires the full strength of FEI. A viable proof must be a true Carleson/amortized argument, allowing the root cost to be \(O(w)\) for tribes while preventing comparable costs from recurring at too many subsequent continuation prefixes.

## 8. Executed checks and exact scope

`check_selector_chain.py` constructs Walsh probabilities with exact `Fraction` arithmetic for five nontrivial examples (parity, AND, majority, addressing, tribes). It verifies exactly:
- every shadow recurrence (208 state checks total);
- every nonempty Green/beta identity (203 state checks total);
- \(\sum_Av_A=1+I\).

After these exact probabilities are constructed, it numerically checks the logarithmic identities
\(H=\mathcal H_{\rm haz}+\mathcal H_{\rm sel}\),
\(\mathcal H_{\rm haz}\le H(K)\), and \(H(K)\le3I\).
It separately evaluates the closed-form AND and tribes obstructions above. All assertions passed. These finite checks are supporting engineering evidence only; the universal claims are proved algebraically in this report.

Script SHA-256:
`b9518f8b583b9b178499aeb234ec7e16162fb0f5a88250db0a9da0af8c2f6888`

Output SHA-256:
`b4c55af09f8c3215318e84ea08cd655b7a2be77a1c86c74f6e4da1846115d0d3`

## 9. What this changes for the next B12 run

The previous target “find a cross-block selector-information potential that survives AND and addressing” is now sharper:

1. **Do not** spend more effort on pointwise stop hazards; (22) pays them globally.
2. **Do not** try a uniform pointwise bound on next-coordinate information; tribes disproves it.
3. Attack the continuation-Palm average (33) with a genuine Carleson/square-function or martingale information-budget argument.
4. Any proposed budget must permit one \(O(w)\) spike at the tribes root, yet show that such spikes cannot recur on \(O(w)\) many \(\mu\)-typical prefixes.
5. Keep the exact Green/noise formula (6) available: it may let hypercontractivity or random-restriction inequalities control recurrence of large selector-information spikes without reverting to false local charges.

**Final status:** full uniform-cube FEI remains OPEN. The run produces a sharper exact sequential target and two rigorous Boolean no-go results, not a proof of (33).
