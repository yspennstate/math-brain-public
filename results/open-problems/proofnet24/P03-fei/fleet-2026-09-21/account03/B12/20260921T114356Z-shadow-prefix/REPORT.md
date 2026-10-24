# B12 FEI creative attempt: uniform-prefix shadow compression and a noise/sensitivity bridge

**Status:** full uniform-cube Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred in this run.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), with an exact bridge toward #3 (sensitivity/derivative structure).  
**Fresh starting point:** the required `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` were read from fresh `master`. This run continued the previous account03/B12 ordered-compression/Palm report and the later account01/B12 cancellation-entropy handoff; it did not recheck the read-once certificate or repeat the old exhaustive sweeps.

No novelty/prior-art claim is made for the lemmas below. They are recorded as proof-route mathematics for FEI.

## 1. Attack the negation first: the sharp scalar cancellation target is false

Write

\[
p_A=\Pr[S=A]=\widehat f(A)^2,\qquad
u_A=\sum_{B\supseteq A}p_B,
\]

and recall the previous handoff's cancellation functional

\[
B_{\rm can}(f)=\sum_A p_A\log_2\frac{u_A}{p_A}.
\]

That handoff proved

\[
H(f)\le 2I(f)+2B_{\rm can}(f),
\]

so the sharp candidate constant \(\beta=\beta(1/2)\simeq6.4547837\) would follow from the universal scalar inequality

\[
\tag{C_{\rm sharp}}
B_{\rm can}(f)\le \left(\frac{\beta}{2}-1\right)I(f)
       =2.22739185\ldots\,I(f).
\]

I tested this *before* trying to prove it.

For odd majority on \(n=2m+1\) variables, the exact Fourier mass is level-symmetric. For odd \(k\),

\[
\widehat{\mathrm{Maj}_n}(A)
=(-1)^{(k-1)/2}
\frac{\binom{n-1}{m}}{2^{n-1}}
\frac{\binom{m}{(k-1)/2}}{\binom{n-1}{k-1}},
\qquad |A|=k,
\]

and the even levels vanish. Hence, with \(W_k\) the exact level mass,

\[
p_A=\frac{W_k}{\binom nk},\qquad
\frac{u_A}{p_A}
=\frac{\sum_{b\ge k}\binom bk W_b}{W_k}.
\]

The committed checker evaluates every \(W_k\) as an exact `Fraction`; only the final logarithms use 80-digit `Decimal`.

At \(n=151\),

\[
I=9.820815687337559464\ldots,\qquad
\frac{B_{\rm can}}I=2.274836861229597398\ldots,
\]

which is **strictly above** \(2.22739185\ldots\). Therefore (C_sharp) is **REFUTED**. This is not a counterexample to FEI: for the same majority function, direct level evaluation gives \(H/I=2.7638347519\ldots\), far below \(\beta\). It only shows that the previous scalar cancellation reduction loses too much information to reach the sharp constant by bounding \(B_{\rm can}\) alone.

## 2. New construction: the uniform-prefix shadow

For any random subset law \(p_A\), not necessarily a Boolean spectrum, define for \(a=|A|\)

\[
\boxed{\quad
v_A:=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{a}}.
\quad}
\]

Interpretation: sample an independent \(T\) from the same subset law; if \(|T|\ge a\), choose a uniformly random \(a\)-subset of \(T\). Then \(v_A\) is exactly the probability that this random prefix-set equals \(A\).

Let

\[
K=|S|,\qquad W_a=\Pr[K=a],\qquad \tau_a=\Pr[K\ge a].
\]

Two exact identities are immediate:

\[
\sum_{|A|=a}v_A=\tau_a,
\]

and

\[
\tag{P}
\sum_{i\notin A}v_{A\cup\{i\}}
=(a+1)(v_A-p_A).
\]

Indeed, a fixed strict superset \(B\supsetneq A\) is counted \(|B|-a\) times on the left, and
\[
\frac{|B|-a}{\binom{|B|}{a+1}}
=\frac{a+1}{\binom{|B|}{a}}.
\]

## 3. PROVED: universal terminal log-loss is at most \((\log_2 e)I\)

Define the **shadow terminal surprisal**

\[
B_{\rm sh}:=\sum_A p_A\log_2\frac{v_A}{p_A}.
\]

Because the term \(B=A\) occurs in \(v_A\), we always have \(v_A\ge p_A\).

### Theorem

For every random subset \(S\),

\[
\boxed{\qquad
B_{\rm sh}\le (\log_2 e)\,\mathbb E|S|.
\qquad}
\]

### Proof

Fix a level \(a\) with \(W_a>0\). On the \(a\)-subsets define

\[
P_a(A)=\frac{p_A}{W_a},\qquad
Q_a(A)=\frac{v_A}{\tau_a}.
\]

Since the \(v_A\)'s sum to \(\tau_a\),

\[
\begin{aligned}
\sum_{|A|=a}p_A\log_2\frac{v_A}{p_A}
&=
W_a\log_2\frac{\tau_a}{W_a}
-
W_a D_2(P_a\|Q_a)\\
&\le
W_a\log_2\frac{\tau_a}{W_a}.
\end{aligned}
\]

Write \(s_a=\tau_{a+1}/\tau_a\). Since
\(W_a=\tau_a(1-s_a)\),

\[
W_a\log_2\frac{\tau_a}{W_a}
=(\log_2 e)\tau_a(1-s_a)[-\ln(1-s_a)]
\le
(\log_2 e)\tau_a s_a
=(\log_2 e)\tau_{a+1},
\]

using \(-x\ln x\le1-x\) for \(x\in[0,1]\).
Summing over \(a\) and using the tail-sum identity
\(\sum_{a\ge0}\tau_{a+1}=\mathbb E K\) proves the claim. QED.

This is a genuine dimension-free compression payment that requires no Booleanity.

## 4. PROVED: an exact prefix-chain decomposition of spectral entropy

Sample \(S\), then uniformly randomly order its \(K\) elements. At a current unordered prefix \(A\), identity (P) shows that the exact transition law is

\[
\Pr[\text{stop}\mid A]=\frac{p_A}{v_A},
\]

and, conditional on not stopping,

\[
r_A(i):=
\Pr[\text{next}=i\mid A,\text{ continue}]
=
\frac{v_{A\cup\{i\}}}{(a+1)(v_A-p_A)}.
\]

Let \(h_2\) denote binary entropy and define

\[
J:=\sum_A v_A h_2(p_A/v_A),
\]

\[
\mathrm{Br}:=
\sum_A (v_A-p_A)H(r_A).
\]

The randomly ordered list has entropy \(H(S)+\mathbb E\log_2(K!)\). Applying the chain rule to its stop/continue and next-coordinate decisions gives the exact identity

\[
\boxed{\qquad
H(S)=J+\mathrm{Br}-\mathbb E\log_2(K!).
\qquad}
\]

Moreover, on level \(a\), concavity of binary entropy gives

\[
\sum_{|A|=a}v_A h_2(p_A/v_A)
\le
\tau_a h_2(W_a/\tau_a).
\]

The right side is the entropy cost of the scalar survival process for \(K\); summing levels yields

\[
\boxed{J\le H(K).}
\]

Thus this prefix chain refines the previous ordered-set code. Coding every next coordinate with the global distribution
\(q_i=\Pr(i\in S)/I\) gives \(\mathrm{Br}\le I H(q)\), recovering

\[
H(S)\le H(K)+I H(q)-\mathbb E\log_2(K!).
\]

The point is that \(\mathrm{Br}\) is the *actual local branching entropy*, not the much coarser \(I H(q)\). This keeps the factorial rebate that was discarded by the scalar \(B_{\rm can}\) route.

## 5. PROVED: the prefix shadow is a Beta average of noisy derivative energy

Now use Boolean Fourier structure. For nonempty \(A\), \(a=|A|\), let the normalized iterated derivative \(D_A f\) be defined by

\[
\widehat{D_A f}(C)=\widehat f(A\cup C),\qquad C\subseteq A^c.
\]

Then

\[
\|T_\rho D_A f\|_2^2
=
\sum_{B\supseteq A}p_B\,\rho^{2(|B|-a)}.
\]

Using
\[
a\int_0^1 t^{a-1}(1-t)^{b-a}\,dt
=\frac1{\binom ba},
\]
we obtain the exact representation

\[
\boxed{\qquad
v_A
=
a\int_0^1 t^{a-1}
\left\|T_{\sqrt{1-t}}D_A f\right\|_2^2\,dt.
\qquad}
\]

Likewise, for \(i\notin A\),

\[
v_{A\cup\{i\}}
=
(a+1)\int_0^1 t^a
\left\|T_{\sqrt{1-t}}D_iD_A f\right\|_2^2\,dt.
\]

Therefore the exact next-coordinate law \(r_A\) is a normalized Beta-mixture of derivative-energy / influence profiles across noise scales. This is the promised route-1/route-3 bridge: the sequential spectral predictor can be attacked through the sensitivity/derivative structure of noisy restrictions rather than through an arbitrary subset law.

## 6. A second attempted simplification, and its counterexample

Since \(v_A\le u_A\), write

\[
B_{\rm can}=B_{\rm sh}+M,\qquad
M:=\sum_A p_A\log_2\frac{u_A}{v_A}\ge0.
\]

Combining the previous cancellation reduction with the new theorem gives

\[
H(f)\le
(2+2\log_2 e)I(f)+2M
\]
after dropping the favorable lower-order correction terms from the earlier exact inequality.

A tempting nonsharp target was \(M\le I\), which would imply FEI with constant

\[
4+2\log_2 e=6.8853900817\ldots.
\]

This is already **REFUTED** by majority on only \(n=13\) variables:

\[
\frac{M}{I}=1.06856969553401258\ldots>1.
\]

To reach Hod's candidate \(\beta\) through this coarsened decomposition one would need

\[
\frac{M}{I}
\le
\frac{\beta-(2+2\log_2 e)}2
=
0.78469680911103659\ldots,
\]

which fails even more strongly. For majority \(n=251\),

\[
B_{\rm can}/I=2.3845948076495134\ldots,\qquad
B_{\rm sh}/I=0.1258679184420959\ldots,\qquad
M/I=2.2587268892074175\ldots.
\]

So **bounding \(M\) by a small scalar multiple after discarding the factorial rebate is the wrong closure**. A dimension-independent bound \(M\le cI\) for some larger universal \(c\) remains OPEN; this run does not assert or refute it.

## 7. The new exact target: keep the factorial rebate

Since \(J\) contains the terminal surprisal \(B_{\rm sh}\), write

\[
R_{\rm seq}
:=
(J-B_{\rm sh})+\mathrm{Br}-\mathbb E\log_2(K!).
\]

Then the prefix-chain identity is

\[
H(S)=B_{\rm sh}+R_{\rm seq}.
\]

The universal theorem above pays the first term by \((\log_2 e)I\). Therefore the following is now the exact sharp sufficient statement I would attack:

\[
\tag{SEQ_\beta}
R_{\rm seq}(f)
\le
\bigl(\beta(1/2)-\log_2 e\bigr) I(f)
=
5.0120886591\ldots\, I(f)
\]
for every Boolean function.

This formulation deliberately preserves the cancellation between branching multiplicity and
\(\mathbb E\log_2(K!)\), which majority shows is destroyed by the \(B_{\rm can}\) scalar route.

The next attack is to use the Beta-noise formula above to express each local next-coordinate law \(r_A\) as a scale-mixture of influence profiles of \(D_A f\), then seek a coupling to the sensitive coordinates of the corresponding noisy/restricted derivative. The desired one-step payment is not a bound on \(H(r_A)\) alone: it must include the local share of the factorial rebate. Majority is the stress test precisely because its local branching is large while that rebate is also large.

## 8. Reproducible computation and classification

`shadow_majority_check.py` uses exact rational Fourier level masses for majority and 80-digit decimal logarithms. Its archived output is `verification.txt`.

Classification:

- **PROVED:** uniform-prefix identities for \(v_A\).
- **PROVED:** \(B_{\rm sh}\le(\log_2 e)I\) for every random subset law.
- **PROVED:** exact stop/branch prefix-chain identity \(H=J+\mathrm{Br}-E\log_2 K!\), with \(J\le H(K)\).
- **PROVED:** Beta-noise representation of \(v_A\) and its child weights for Boolean Fourier derivatives.
- **REFUTED:** the sharp scalar target \(B_{\rm can}\le(\beta/2-1)I\), by majority \(n=151\).
- **REFUTED:** the simplified residual target \(M\le I\), by majority \(n=13\).
- **OPEN:** (SEQ_beta), hence full FEI.
- **NOT CLAIMED:** novelty or publication priority.

The useful mathematical change in this run is not another finite sweep: it replaces a now-refuted scalar cancellation payment by an exact sequential prefix process whose branching probabilities are tied directly to noisy derivative energies.
