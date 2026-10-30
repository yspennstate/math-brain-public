# B17 FEI new proof mechanism: face-channel information packing

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical-brain retrieval/context was used.  
**Role:** fleet03/B17, FEI new proof mechanisms.  
**Fresh mathematical source before the write:** `master` at `6dd9661a6bab369aeb5afa4e3a436935e1391b7e`.  
**Current lower-bound correction used:** the sprint's shared-core graft at `ba37f4275024ddfff125dec2eb1f75fd871cd6c7`, which gives the rigorous lower bound `C_FEI > 6.521850083658...`.

## 0. Route chosen and what changed

This run continues the owner-assigned **higher-order face-boundary / rare-pair information** direction. It does not audit the read-once certificate, repeat the old `n<=5` sweep, or rerun the preceding B17 signed-diagonal/support-deficit checkers.

The immediately preceding rare-pair handoff proves that two arbitrarily rare spectral membership bits can be exactly independent, and then pays that independence by introducing two physical face-label sets `U,V` and applying edge isoperimetry. Its unresolved issue is **certificate packing**: summing many pair boundary certificates may charge the same control-coordinate influence repeatedly.

The new mechanism is:

> **Route 16 — face-channel information packing.** For an arbitrary coordinate block `R`, view the Fourier spectrum of each physical `R`-face as a probability channel from the outside assignment `Y` to a local spectral subset `T`. The information in that channel is paid in one shot by the outside influence through the sharp cube log-Sobolev inequality.

This replaces two separately tracked rare face-label sets by the complete local Fourier pattern of the face. It gives a dimension-free block theorem and, for a pair, a three-channel certificate involving pair mutual information, physical control influence, and double-membership overlap.

## 1. Setup

Let

\[
f:\{-1,1\}^n\to\{-1,1\}
\]

and let `S` denote its spectral sample,

\[
\Pr(S=A)=\widehat f(A)^2.
\]

Fix an arbitrary block `R subseteq [n]` and write `C=R^c`. For `y in {-1,1}^C`, let

\[
f_y(x_R)=f(x_R,y).
\]

For each `T subseteq R`, define the local Fourier coefficient

\[
a_T(y)=\mathbb E_{x_R} f(x_R,y)\chi_T(x_R).
\]

Because each `f_y` is Boolean, Parseval on the `R`-face gives

\[
\sum_{T\subseteq R}a_T(y)^2=1.
\]

Thus

\[
\nu_y(T):=a_T(y)^2
\]

is a probability law on subsets of `R` for every physical face `y`.

Now draw `Y` uniformly on the outside cube and, conditionally on `Y=y`, draw `T` according to `nu_y`.

## 2. PROVED: the local-face channel has the correct spectral marginal

The Walsh transform of `a_T` in the outside variables is exactly

\[
\widehat {a_T}(U)=\widehat f(T\cup U),\qquad U\subseteq C.
\]

Therefore Parseval in the outside variables gives

\[
\Pr(T=t)
=\mathbb E_Y a_t(Y)^2
=\sum_{U\subseteq C}\widehat f(t\cup U)^2
=\Pr(S\cap R=t). \tag{1}
\]

So the output of the physical-face channel `Y -> T` is **exactly** the spectral projection `S cap R`; it is not a surrogate distribution.

Consequently,

\[
\boxed{
H(S\cap R)-\mathbb E_Y H(\nu_Y)=I(Y;T).
} \tag{2}
\]

Writing `Ent_2` for entropy relative to the uniform measure, in bits,

\[
\operatorname{Ent}_2(g^2)
=\mathbb E\left[g^2\log_2\frac{g^2}{\mathbb E g^2}\right],
\]

the mutual information also has the exact decomposition

\[
\boxed{
I(Y;T)=\sum_{t\subseteq R}\operatorname{Ent}_2(a_t^2).
} \tag{3}
\]

Indeed, (3) is just the KL-divergence formula for the channel, grouped by output `t`.

## 3. PROVED: face-channel packing theorem

The sharp cube log-Sobolev inequality, in the present Fourier normalization, is

\[
\operatorname{Ent}_2(g^2)
\le \frac{2}{\ln 2}
\sum_{U}|U|\widehat g(U)^2. \tag{4}
\]

Apply (4) to every scalar coefficient field `a_t(y)` and sum over `t`. Using
`ahat_t(U)=fhat(t union U)`, every global spectral coefficient is counted with exactly its number of outside coordinates. Hence

\[
\begin{aligned}
I(Y;T)
&\le \frac{2}{\ln2}
  \sum_{t\subseteq R}\sum_{U\subseteq C}|U|\widehat f(t\cup U)^2\\
&=\frac{2}{\ln2}\sum_{j\in C}\operatorname{Inf}_j(f).
\end{aligned}
\]

Combining with (2):

### Theorem 3.1 — block face-channel information packing

For every Boolean `f` and every coordinate block `R`,

\[
\boxed{
H(S\cap R)
\le
\mathbb E_Y H(\nu_Y)
+\frac{2}{\ln2}\, I_C(f).
} \tag{5}
\]

where

\[
I_C(f)=\sum_{j\in C}\operatorname{Inf}_j(f).
\]

This is a universal all-dimensional statement. The important feature is the **packing**: all information needed to locate the complete local Fourier pattern of the `R`-face is charged to `I_C` once, rather than once per rare coordinate or once per rare pair.

Boundary checks are exact:

- `R=emptyset`: both entropy terms vanish.
- `R=[n]`: `C` is empty, there is one face, and (5) is equality.
- characters: every local spectral law is a point mass, so the information term vanishes.
- constants: every term is zero.

The constant `2/ln 2` in (4) is the sharp constant for arbitrary real coefficient fields: already on one bit, `g=1+epsilon chi` has `Ent_2(g^2)/(sum |U| ghat(U)^2) -> 2/ln2` as `epsilon -> 0`. Booleanity may still force a better constant for the special family of coefficient fields `a_t`; that is an open strengthening, not assumed here.

## 4. PROVED: exact two-face identity and a three-channel rare-pair certificate

Take `R={i,j}` and let the outside assignment be `y`. Modulo sign, a Boolean function on two bits is one of:

- an affine character: constant, `i`, `j`, or parity `ij`; its local spectral entropy is `0`;
- a one-defect/three-defect face `D`; its four local Fourier masses are all `1/4`, so its local spectral entropy is `2` bits.

Let `t` be the fraction of `D` faces and `w` the fraction of parity-character faces. Then

\[
\mathbb E_Y H(\nu_Y)=2t. \tag{6}
\]

Also, with

\[
q_{ij}:=\Pr(i,j\in S),
\]

Parseval applied to the local `{i,j}` coefficient gives the exact identity

\[
\boxed{q_{ij}=w+t/4.} \tag{7}
\]

Hence the block theorem becomes the stronger exact-structure inequality

\[
\boxed{
H(X_i,X_j)-2t
\le \frac{2}{\ln2}I_{[n]\setminus\{i,j\}}(f),
} \tag{8}
\]

where `X_k=1_{k in S}`. Since `2t<=8q_ij`,

\[
\boxed{
H(X_i,X_j)
\le \frac{2}{\ln2}I_{\rm ctrl}(f)+8q_{ij}.
} \tag{9}
\]

Equivalently, since

\[
H(X_i,X_j)=h_2(p_i)+h_2(p_j)-I(X_i;X_j),
\]

we obtain the **three-channel certificate**

\[
\boxed{
I(X_i;X_j)
+\frac{2}{\ln2}I_{\rm ctrl}(f)
+8q_{ij}
\ge h_2(p_i)+h_2(p_j).
} \tag{10}
\]

This cleanly separates the three places a dangerous rare pair can pay its marginal entropy:

1. direct spectral dependence `I(X_i;X_j)`;
2. physical variation of the whole two-face Fourier pattern, paid by control influence;
3. direct simultaneous activation `q_ij`.

The fleet02 rare-pair counterexample kills channel 1 by making the pair exactly independent. Formula (10) shows that independence alone cannot kill the combined certificate.

## 5. Numerical consequence on the exact rare independent family

Use the existing exact Boolean family with

\[
p_i=p_j=1/64,\qquad q_{ij}=1/4096,
\qquad I(X_i;X_j)=0.
\]

At the **current** sprint lower-bound scale

\[
C_*=6.521850083658612\ldots,
\]

the two marginal entropy terms still have positive FEI excess:

\[
2[h_2(1/64)-C_*/64]
=0.0284223354952078\ldots>0.
\]

Thus this remains a genuinely dangerous-scale rare pair.

But (10) now forces

\[
I_{\rm ctrl}
\ge \frac{\ln2}{2}
\left(2h_2(1/64)-\frac8{4096}\right)
=0.0798079355244913\ldots. \tag{11}
\]

The preceding face-boundary theorem gave `7/128=0.0546875`; the packed-channel lower bound is about **45.9% larger** on this exact family. The explicit lexicographic realization has actual

\[
I_{\rm ctrl}=355/2048=0.17333984375,
\]

so both rigorous lower bounds remain consistent.

This improvement is not a full FEI bound. It is a stronger universal certificate for the specific packing obstruction that the rare-pair route had exposed.

## 6. REFUTED-LEMMA: the tempting coefficient `2` is false even for exact Boolean functions

The general log-Sobolev constant `2/ln2=2.885390...` looks loose, so the first attempted strengthening was

\[
H(X_i,X_j)\stackrel{?}{\le}2 I_{\rm ctrl}+8q_{ij}. \tag{12}
\]

This is false.

Take the four-bit Boolean function that is `+1` exactly at integer-labelled vertices `0` and `1`, and `-1` at the other fourteen vertices. For the zero-indexed pair `(1,2)`, exact Walsh arithmetic gives

\[
p_i=p_j=1/4,\qquad q_{ij}=1/8,
\qquad t=1/2,
\qquad I_{\rm ctrl}=1/4.
\]

The pair spectral law is

\[
(5/8,1/8,1/8,1/8),
\]

so

\[
H(X_i,X_j)
=3-\frac58\log_2 5
=1.5487949406953985\ldots.
\]

The proposed right side in (12) is exactly

\[
2(1/4)+8(1/8)=3/2,
\]

and therefore (12) fails by

\[
0.04879494069539847\ldots.
\]

**REFUTED-LEMMA:** one cannot simply replace `2/ln2` by `2` in the universal pair certificate.

This does not show `2/ln2` is optimal under Boolean section constraints. On the exhaustive four-bit test the largest observed ratio

\[
\frac{H(X_i,X_j)-2t}{I_{\rm ctrl}}
\]

was `2.195179762781594...`, attained by the same witness. Determining the all-dimensional Boolean face-channel constant is a concrete next question.

## 7. Targeted exact stress test

`face_channel_check.py` uses exact integer Walsh transforms and `Fraction` arithmetic for all probabilities and influences. Floating point is used only for Shannon logarithms.

It enumerated every one of the `65,536` Boolean functions on four variables and all six coordinate pairs, for `393,216` targeted tests. This is a **new-quantity stress test**, not the old FEI `n<=5` sweep.

Results:

- exact identity `q=w+t/4`: `0` failures;
- maximum observed violation of (8): `0`;
- maximum observed violation of (9): `0`;
- false coefficient-2 strengthening: maximum positive violation `0.04879494069539847...`, with the explicit mask-3 witness above.

The finite test is not evidence for universality; equations (5), (8), (9), and (10) are universal because they follow algebraically from the channel identity plus the standard cube log-Sobolev inequality.

## 8. Relation to the current literature boundary

A bounded current search recovered Han's `O(I + sum_i I_i log(1/I_i))` upper bound and the 2026 González--MacManus--Pereyra restriction/stopping-tree approach. The present theorem is aimed exactly at the dangerous rare-coordinate information term, but I have **not** performed a publication-level literature search for this precise face-channel packaging and make **no novelty or priority claim**.

The full conjecture remains open; the new 162-bit shared-core graft only raises the currently reproduced lower-bound scale and does not close FEI.

## 9. Claim ledger

### PROVED

1. The physical local-spectrum channel on an arbitrary block `R` has output law exactly `S cap R`.
2. Exact channel identity `H(S cap R)-E H(nu_Y)=I(Y;T)`.
3. Universal face-channel packing theorem (5): the entire location information is at most `(2/ln2) I_C(f)`.
4. For a two-coordinate block, exact identity `E H(nu_Y)=2t` and `q_ij=w+t/4`.
5. Universal pair certificate (9), equivalently the three-channel certificate (10).
6. On the exact `p=1/64` pairwise-independent Boolean family, (10) improves the previous analytic control-influence lower bound from `0.0546875` to `0.0798079355...`.

### REFUTED-LEMMA

The stronger coefficient-2 pair inequality (12) is false; an exact four-bit Boolean witness violates it by `0.04879494069539847...`.

### CONDITIONAL / OPEN

1. Full FEI remains **OPEN / NOT PROVED**.
2. The optimal constant in the face-channel theorem after exploiting the extra Boolean compatibility among all coefficient fields `a_T` is unknown.
3. The remaining global step is to turn the block theorem into a **hierarchical rare-coordinate packing** in which local face entropy is recursively paid without recharging the same influence at each scale.

## 10. Next attack

Do not rerun the four-bit enumeration.

The next fleet03/B17 run should attack one of these two precise statements:

1. **Boolean face-channel improvement.** Prove a constant `c_B < 2/ln2` for the coupled family of coefficient fields coming from Boolean sections, or construct an exact Boolean family whose ratio approaches `2/ln2`. The four-bit witness already rules out `c_B=2`.
2. **Hierarchical block packing.** Choose a dyadic rare-influence block `R` and use (5) only once for its outside-control cost; then prove that `E H(nu_Y)` can be decomposed into strong-overlap clusters whose activation entropy is paid by internal `q_ij` mass and influence, rather than by another copy of the full outside influence.

Either result would directly address the certificate-packing gap left by the rare-pair route. A finite example or a better constant for a special class is not full FEI.
