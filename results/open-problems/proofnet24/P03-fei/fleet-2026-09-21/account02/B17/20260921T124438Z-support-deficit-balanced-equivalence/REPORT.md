TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T12:44:38.448761Z — balanced support-deficit equivalence and the sharp shared-graft obstruction

Status: PARTIAL. Full Friedgut–Kalai Fourier entropy-influence (FEI) remains OPEN / NOT PROVED.
Brain status: WITHOUT_VERIFIED_BRAIN.
Role: FEI new proof mechanisms.
Live sprint assignment adopted: account02/B17, “support-deficit transfer and its actual sharp obstruction”.
Math source at start: yspennstate/math-open-problems master d48d1cdf71ec1a44ef2eede8222c531eb7c48096, refreshed during the run.
Normalization: uniform cube, Boolean values ±1, base-2 spectral entropy
H(f)=sum_S p_S log2(1/p_S), p_S=fhat(S)^2, and total influence
I(f)=sum_S |S|p_S.

## 1. What changed

The previous support-deficit route proposed, for every nonempty cube set A of density δ,
U(A)=H_A-log2(1/δ), E(A)=J_A-(1/2)log2(1/δ),
and the stronger universal inequality U(A)<=C E(A).

This run identifies the exact obstruction: **on balanced sets this “stronger” inequality is not stronger at all — it is exactly equivalent, constant-for-constant, to full FEI.** The equivalence uses balanced suspension in one direction and balanced recursive composition in the other.

Consequently the newly certified 162-bit balanced shared-core graft immediately gives a finite balanced set whose support-deficit ratio is
6.521850083658612443633672199029299526203969333...,
so the earlier support-deficit target C=6.4547837 is false by an exact source-admissible Boolean example. This does NOT refute FEI; it refutes that stronger intermediate constant.

Before this run the best explicit support-deficit obstruction recorded in the route was the one-third staircase ratio
6.425122239075223...
After this run the finite balanced-set lower bound is
>6.521850083658612443633672199029299526203969333,
an increase of >0.0967278445833894.

The three FLEET_RULES moves executed were:
- #2 ATTACK THE NEGATION FIRST: apply the newest shared-graft witness to the proposed zero-slack support-deficit inequality;
- #11 DUALIZE / CHANGE REPRESENTATION: identify balanced sets with balanced Boolean spectra;
- #7 TAKE THE LIMIT: use finite balanced self-compositions to recover the exact H/(I-1) amplification obstruction.

No publication-priority or novelty claim is made for the composition ingredients; O’Donnell–Tan’s 2013 composition theorem and Hod’s 2017 recursive lower-bound work were checked as relevant prior literature.

## 2. Balanced-set identity

For a nonempty set A in the n-cube let g=1_A, δ=E g, and
mu_A(S)=ghat(S)^2/δ.
Let H_A=H(mu_A), J_A=E_{S~mu_A}|S|, L_A=log2(1/δ),
U(A)=H_A-L_A, E(A)=J_A-L_A/2.

Assume A is balanced, δ=1/2, and put f=2 1_A-1. Then f is balanced and
fhat(empty)=0. For S nonempty,
ghat(S)=fhat(S)/2,
while ghat(empty)=1/2. Hence
mu_A(empty)=1/2,
mu_A(S)=fhat(S)^2/2  (S nonempty).
Thus mu_A is the equal mixture of an empty-set atom and the spectral law of f. Therefore

H_A = 1 + H(f)/2,
J_A = I(f)/2,
L_A = 1,

and exactly

U(A)=H(f)/2,
E(A)=(I(f)-1)/2.                                      (2.1)

Whenever E(A)>0,

U(A)/E(A)=H(f)/(I(f)-1).                              (2.2)

This is an identity, not an inequality.

## 3. PROVED: full FEI is equivalent to the balanced support-deficit inequality

### Theorem

Fix any constant C>=0. The following are equivalent.

(A) Every Boolean h on every finite uniform cube satisfies
    H(h) <= C I(h).

(B) Every balanced Boolean f satisfies
    H(f) <= C (I(f)-1).

(C) Every balanced cube set A satisfies
    U(A) <= C E(A).

The convention in (B) and (C) at I(f)=1/E(A)=0 is the inequality itself, not a ratio.

### Proof: (B) <=> (C)

This is exactly (2.1).

### Proof: (B) => (A), balanced suspension

Let h be arbitrary Boolean and add one fresh uniform sign y. Define

f(y,x)=y h(x).

Then E f=0, so f is balanced. Fourier coefficients are shifted by the new coordinate:
fhat(S union {y})=hhat(S), and coefficients not containing y are zero. Therefore

H(f)=H(h),
I(f)=I(h)+1.

Applying (B),

H(h)=H(f) <= C(I(f)-1)=C I(h).

Hence (A).

### Proof: (A) => (B), balanced self-composition

Let f be balanced, with a=I(f) and b=H(f). Define f^(1)=f and recursively let
f^(m+1) be f applied to independent blocks, each block computing f^(m).

Because every inner function is balanced, its empty Fourier coefficient is zero. A spectral sample of a composition can therefore be generated injectively by:

1. draw the outer spectral set S from fhat(S)^2;
2. for each active outer block j in S, independently draw an inner spectral set from the spectral law of f^(m);
3. take the labelled union across blocks.

The active block set is recoverable from the union, so Shannon chain rule gives

H(f^(m+1)) = b + a H(f^(m)),
I(f^(m+1)) = a I(f^(m)).

Consequently, if a!=1,

I(f^(m))=a^m,
H(f^(m))=b(1+a+...+a^(m-1))
        =b(a^m-1)/(a-1).

Applying (A) to every finite m gives

b(a^m-1)/(a-1) <= C a^m.

For a>1, let m->infinity to obtain b<=C(a-1).
If a=1, the recurrence is H(f^(m))=mb and I(f^(m))=1; (A) gives mb<=C for every m, hence b=0, again b<=C(a-1).
A balanced nonconstant Boolean function cannot have a<1 by the ordinary edge-isoperimetric lower bound at measure 1/2.

Thus (B). QED.

### Sharp-constant corollary

Writing C_FEI for the optimal universal FEI constant (possibly +infinity),

C_FEI
 = sup_{balanced f, I(f)>1} H(f)/(I(f)-1)
 = sup_{balanced A, E(A)>0} U(A)/E(A).                (3.1)

So the balanced part of the support-deficit route is FEI-complete.

This is the precise obstruction to treating U<=CE as an easier stability theorem: even before unbalanced densities are considered, it already contains the full conjecture.

## 4. Exact current Boolean obstruction from the shared-core graft

The sprint’s current shared-core construction supplies a balanced monotone Boolean F on 162 bits with

I(F)=68013/32768

and rigorously enclosed entropy

7.014850042680291613033104756310658624299893163
<= H(F) <=
7.014850042680291613033104756310658624299893164.

This construction belongs to the interactive sprint handoff; this report does not claim authorship of it.

Let A_F={x:F(x)=1}. Since F is balanced, δ(A_F)=1/2. By (2.1),

E(A_F)=(I(F)-1)/2 = 35245/65536
                   = 0.5377960205078125,

and

3.5074250213401458065165523781553293121499465815
<= U(A_F) <=
3.507425021340145806516552378155329312149946582.

Therefore the finite 162-dimensional set A_F satisfies

6.521850083658612443633672199029299526203969333669...
<= U(A_F)/E(A_F)
<=
6.521850083658612443633672199029299526203969334600....

In particular:

- `(SD_C)` is false for C=6.4547837, by margin >0.0670663836586124;
- it also exceeds the independently reproduced external-seed amplified baseline upper endpoint
  6.521845710923046575658143972948578468366662293
  by >0.000004372735565867975528226080721057837307040;
- this is a counterexample only to those support-deficit constants, NOT to FEI.

The reason the same number appears in the sprint’s amplification calculation is now structural rather than coincidental: for a balanced F the support-deficit ratio is H(F)/(I(F)-1), precisely the limiting FEI ratio of balanced self-compositions.

## 5. Replacement route: keep the scalar activation credit instead of deleting it

The zero-slack target U<=CE discards a scalar term that FEI is allowed to use. For an arbitrary minority set A of density 0<δ<=1/2, let f=2 1_A-1,
L=log2(1/δ), and V=4δ(1-δ). The exact identity from the support-deficit reduction is

H(f)-C I(f)
 =4δ[U(A)-C E(A)] + s_C(δ),

where

s_C(δ)
 = h2(V)+4δ[(1-C/2)L-h2(δ)].

Hence FEI at constant C for this f is **equivalent** to

U(A) <= C E(A) + kappa_C(δ),                           (5.1)

with the explicit density credit

kappa_C(δ)
 =(C/2-1)L + h2(δ) - h2(4δ(1-δ))/(4δ).                (5.2)

At balance, kappa_C(1/2)=C/2. Deleting this C/2 is exactly what turns the one-step FEI statement into the amplification-hard quantity H/(I-1).

This suggests a better proof target than `(SD_C)`: derive a coordinate-split/Bellman recursion for

B_C(A)=C E(A)+kappa_C(delta(A))-U(A),

preserving the signed/cancellation terms rather than forcing `kappa` to zero. This is not a proof of FEI — (5.1) is an exact reformulation — but it removes a now-certified false strengthening and identifies the only scalar slack a valid support-deficit induction is allowed to spend.

A useful next lemma would be a one-coordinate split inequality for B_C in which the Jensen–Shannon/restriction term is absorbed by the change in kappa_C plus a nonnegative physical-boundary term. That attack is genuinely different from proving U<=CE, ordinary coordinate compression, or pairwise spectral-information payment.

## 6. Exact sanity check

`verify_balanced_support_deficit.py` exhaustively checks:

- all 276 Boolean functions through n<=3 under balanced suspension, verifying exact preservation of the squared spectral-weight multiset and exact `I(f_susp)=I(f)+1`;
- 66 balanced n=2,3 functions with I>1 under depth-two self-composition, verifying exact `I_2=I^2` and the exact product spectral-weight multiset that yields `H_2=H(1+I)`.

The checker uses integer Walsh transforms and `fractions.Fraction`. No floating-point comparison decides pass/fail. The finite checks support only the tested algebraic implementation; the theorem above is proved analytically.

Checker SHA-256:
ce8b76032532882b1eb87df9378d71aaab374e7a67ad997e41b8b2e3af9599a2

Output SHA-256:
34dee1c4d51b1017256f772f73c0d167bee49e27b3907c0675f7fbc76b6a8251

## 7. Literature/applicability check

Relevant primary literature checked this run:

- O’Donnell and Tan, “A composition theorem for the Fourier Entropy-Influence conjecture” (2013), which supplies the established composition framework behind recursive amplification.
- Hod, “Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions” (2017), which explicitly uses recursive/compositional lower-bound mechanisms.
- Potapov, “On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions” (arXiv:2609.21563, 18 Sep 2026), a current class result with sharp plateaued constant 4; it does not supply the universal balanced support-deficit inequality.
- González–MacManus–Pereyra, “Further evidence towards the Fourier Entropy-Influence conjecture” (arXiv:2606.00246, May 2026), whose restriction/stopping framework is compatible with keeping one-step slack rather than demanding every-coordinate payment.

I did not locate an explicit published statement of the exact equivalence (A)<=>(B)<=>(C) in the quick search, but it is an immediate consequence of standard balanced suspension plus the established composition machinery. **Novelty is therefore NOT CLAIMED.**

## 8. Before/after and remaining universal gap

Before:
- support-deficit route’s explicit lower obstruction: 6.425122239075223... (one-third staircase);
- route described U<=CE as a stronger stability inequality that might simplify FEI.

After:
- finite balanced support-deficit obstruction: >6.521850083658612443633672199...;
- balanced U<=CE is proved constant-for-constant equivalent to full FEI;
- the old zero-slack target at C=6.4547837 is decisively refuted by a genuine balanced Boolean set;
- the replacement scalar-corrected Bellman functional B_C is identified exactly.

Remaining gap:
prove a dimension-independent nonnegative lower bound for B_C (equivalently FEI) by a genuine split/stopping mechanism. The next run should not return to zero-slack support deficit. It should derive or refute a one-coordinate Bellman recursion for B_C and test the exact shared-core graft as the first adversarial case.

Full FEI remains OPEN / NOT PROVED.
