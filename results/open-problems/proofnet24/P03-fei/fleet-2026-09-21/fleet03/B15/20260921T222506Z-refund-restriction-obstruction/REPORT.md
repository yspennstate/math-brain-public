# fleet03/B15 — exact-refund restriction obstruction and Boolean convolution reformulation

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval or receiver context entered this mathematics.

**Role / joint interface:** FEI spectral remainder proof, interface D: conditional packet decompositions under actual coordinate restrictions and the unpaid arithmetic/Shannon remainder. No read-once certificate was rerun and no publication-priority claim is made.

## 1. Peer results consumed and exact target

This run substantively consumes two completed other-account results.

1. **fleet04/B15, `20260921T211141Z-refunded-radius1-transfer/REPORT.md`** (REPORT blob `ec1224f39f7ac67703d1a5b22235561f167f0a78`). For the squared Fourier law `p_s=\widehat f(s)^2`, independent `S,S'~p`, and `D=S\oplus S'`, it proves the exact collision-KL-refunded high-shift quantity

\[
T_2(f)=\sum_s p_s\log_2\frac1{p_s}
\left(1-p_s-\sum_i p_{s\oplus e_i}\right)
\]

and the exact refund-aware remainder

\[
R_*(f)=T_2(f)-G_{\le1}(f),\qquad G_{\le1}(f)\ge0.
\]

The still-open sharp sufficient transfer is `T_2<=4J`, where

\[
J(f)=\sum_i\min(\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)).
\]

The coefficient four is asymptotically necessary on the one-point-defect family.

2. **fleet02/B15, `20260921T170301Z-valuation-tail-majorization/REPORT.md`** (REPORT blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`). If a Fourier magnitude packet has signed valuation depth `r_a` and packet mass `p_a`, then

\[
R:=\sum_a p_a r_a\le2J,
\]

indeed all valuation tails satisfy the stronger majorization stated in that report.

The negative collision information credit is **not discarded** below: the exact `R_*` is tested directly before passing to the sufficient upper quantity `T_2`.

## 2. PROVED: actual-restriction entropy identity with a negative orientation-information credit

Fix a physical coordinate `i`. Pair the parent Fourier coefficients as

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
m_T=u_T^2+v_T^2.
\]

Let `T` be distributed by `m_T`. Conditional on `T`, let `C` select the parent spectral member, so

\[
\Pr(C=1\mid T)=\frac{v_T^2}{m_T}.
\]

Let `O(T)` record which member of the unordered pair has the smaller squared magnitude, and put `L=C\oplus O(T)`. Then

\[
q_T:=\Pr(L=1\mid T)=\frac{\min(u_T^2,v_T^2)}{m_T},
\qquad
M_i:=\Pr(L=1)=\sum_T\min(u_T^2,v_T^2).
\]

Choose the actual restriction branch `Z\in\{+,-\}` uniformly. Its joint law with `T` is

\[
\Pr(Z=z,T)=\frac12(u_T+zv_T)^2.
\]

Therefore `Z` is uniform, its `T`-marginal is `m`, and

\[
\Pr(Z=+\mid T)=\frac12+\frac{u_Tv_T}{m_T}.
\]

### Theorem B15-REAL-RESTRICTION-01

For every Boolean `f` and every physical coordinate `i`, exactly

\[
\boxed{
\Delta_iH
:=H(f)-\frac{H(f_{i=+})+H(f_{i=-})}{2}
=h_2(M_i)-I(L;T)+I(Z;T).
}
\tag{2.1}
\]

Equivalently,

\[
\Delta_iH
=\sum_Tm_T h_2(q_T)
+\sum_Tm_T\left[1-h_2\left(\frac12+\frac{u_Tv_T}{m_T}\right)\right].
\tag{2.2}
\]

The term `-I(L;T)` is a genuine negative information credit. It is present before any scalar upper bound is taken.

**Proof.** The parent spectral entropy is `H(T)+H(C|T)`. The joint law `(Z,T)` has entropy

\[
H(Z,T)=1+\frac12H(f_{i=+})+\frac12H(f_{i=-})
      =H(T)+H(Z|T).
\]

Subtracting gives

\[
\Delta_iH=H(C|T)+1-H(Z|T).
\]

Since XOR by the deterministic orientation bit preserves conditional entropy,
`H(C|T)=H(L|T)=h_2(M_i)-I(L;T)`, while `1-H(Z|T)=I(Z;T)`. This proves (2.1); expanding the two conditional entropies gives (2.2). QED.

For the exact refunded remainder, if

\[
\Lambda(f):=b_0(f)+\sum_j b_{e_j}(f),
\qquad R_*(f)=H(f)-\Lambda(f),
\]

then the actual restriction drift is exactly

\[
\boxed{
\Delta_iR_*=h_2(M_i)-I(L;T)+I(Z;T)-\Delta_i\Lambda.
}
\tag{2.3}
\]

Thus a restriction proof of the sharp coefficient four may not omit either the negative orientation information or the low-self-XOR refund.

## 3. REFUTED: coefficient-four one-coordinate induction, even after the exact refund

Consider the **punctured character**

\[
f_n(x)=\chi_n(x)
\]

except at one physical point, where its sign is flipped. Put `N=2^n`. Its Fourier law is a translate of the one-point-defect law:

\[
P=\left(1-\frac2N\right)^2
\]

on one frequency and

\[
u=\frac4{N^2}
\]

on each of the other `N-1` frequencies. Consequently

\[
J_n=\frac{2n}{N}.
\tag{3.1}
\]

For any physical coordinate, exactly one restriction branch contains the flipped point and is a punctured character in dimension `n-1`; the other branch is an exact character. Hence for `X=T_2` or `X=R_*`,

\[
\Delta_iX=X_n-\frac12X_{n-1},
\qquad
\Delta_iJ=\frac2N.
\tag{3.2}
\]

The radius-one quantity has the closed form

\[
\boxed{
T_{2,n}=(N-1-n)u\left[
P\log_2\frac1P+(1-u)(2n-2)
\right].
}
\tag{3.3}
\]

The exact refunded quantity is

\[
\boxed{
R_{*,n}=H_n-c_{0,n}\log_2\frac1{c_{0,n}}
-\frac{8n^2(N-2)}{N^3},
}
\tag{3.4}
\]

where

\[
H_n=P\log_2\frac1P+(N-1)u(2n-2),
\]

\[
c_{0,n}=1-\frac8N+\frac{24}{N^2}-\frac{16}{N^3}.
\]

The rational-log interval checker accompanying this report certifies:

\[
\frac{\Delta_iT_2}{\Delta_iJ}
>4.309784754760329\qquad(n=4),
\tag{3.5}
\]

and, more importantly after the full low-fibre collision refund is retained,

\[
\boxed{
\frac{\Delta_iR_*}{\Delta_iJ}
>4.077806258441146\qquad(n=5).
}
\tag{3.6}
\]

At `n=6` the refunded ratio is already

\[
\frac{\Delta_iR_*}{\Delta_iJ}>4.503731448707076.
\tag{3.7}
\]

Every coordinate has the same drift on this family. Therefore the natural sharp local selector

\[
\exists i:\quad \Delta_iR_*\le4\Delta_iJ
\tag{3.8}
\]

is **REFUTED**, not merely unproved. The stronger `T_2` version is already refuted in dimension four.

This does **not** refute either global target `R_*<=4J` or `T_2<=4J`. On the same witnesses the global ratios remain below four. What fails is the attempt to prove the sharp global theorem by demanding coefficient-four payment at every single restriction step.

For the `n=5` punctured-character witness, the actual restriction information decomposition is numerically

\[
M_i=0.0625,
\]

\[
h_2(M_i)=0.3372900666170139,
\qquad I(L;T)=0.1839319514529550,
\qquad I(Z;T)=0.1284418719431953,
\]

so

\[
\Delta_iH=0.2817999871072543.
\]

The low-self-XOR term has

\[
\Delta_i\Lambda=0.02693709595468247,
\]

leaving

\[
\Delta_iR_*=0.2548628911525718
>0.25=4\Delta_iJ.
\]

Thus the local failure survives both the genuine negative orientation-information credit in (2.1) and the exact collision-KL refund built into `R_*`.

## 4. PROVED: the obstruction is not an artefact of choosing a special coordinate

More generally, restrict any block of `k<n` coordinates. Of its `2^k` branches, exactly one retains the puncture and becomes `f_{n-k}`; all others are characters. Therefore

\[
\Delta_A X=X_n-2^{-k}X_{n-k},
\qquad
\Delta_AJ=\frac{2k}{2^n}.
\tag{4.1}
\]

In particular, merely replacing one-coordinate induction by a bounded block does not automatically recover a sharp local coefficient-four rule.

There is also an asymptotic obstruction to leaving a fixed residual dimension. From (3.3),

\[
2^nT_{2,n}=8n-8+o(1).
\tag{4.2}
\]

For every fixed `m>=2`, the same closed form and the elementary bound
`-\ln(1-x)<=x/(1-x)` give

\[
T_{2,m}<\frac{8m-8}{2^m}.
\tag{4.3}
\]

Taking `k=n-m` in (4.1) therefore yields

\[
\frac{\Delta_AT_2}{\Delta_AJ}
=4+
\frac{4m-4-m(T_{2,m}/J_m)}{n-m}+o(1/n)
>4
\]

for all sufficiently large `n`. A sharp local coefficient-four induction must therefore use more than a fixed-depth or fixed-residual block payment on this family; it needs a genuinely telescoping/stopping credit.

## 5. Route switch to APPROACH 13: exact Boolean signed-convolution form of the refunded upper remainder

The restriction selector above is dead. This run therefore switches to the explicit **APPROACHES route 13, exploit Booleanity constraints**, instead of weakening (3.8) and repeating it.

Write `a_s=\widehat f(s)`. Booleanity `f^2=1` is exactly the signed convolution system

\[
(a*a)(d)=\delta_{d,0}.
\tag{5.1}
\]

For each frequency `s`, delete that one coefficient:

\[
b^{(s)}_u=
\begin{cases}
a_u,&u\ne s,\\0,&u=s.\end{cases}
\]

Then for every nonzero shift `d`, (5.1) gives the exact identity

\[
\boxed{
(b^{(s)}*b^{(s)})(d)=-2a_sa_{s\oplus d}.
}
\tag{5.2}
\]

Consequently, if

\[
w_s=\sum_{t:\,|s\oplus t|\ge2}p_t,
\]

then

\[
\sum_{|d|\ge2}\left[(b^{(s)}*b^{(s)})(d)\right]^2
=4p_sw_s.
\tag{5.3}
\]

Substituting the exact radius-one representation of fleet04/B15 gives a new source-exact Boolean form:

### Theorem B15-DELETED-CONVOLUTION-02

\[
\boxed{
T_2(f)=\frac14\sum_{s:p_s>0}
\log_2\frac1{p_s}
\sum_{|d|\ge2}\left[(b^{(s)}*b^{(s)})(d)\right]^2.
}
\tag{5.4}
\]

This is no longer a statement about an arbitrary probability law. The high-shift Shannon exposure is exactly a **log-weighted high-degree energy of the Boolean self-convolution left after deleting one Fourier atom**.

The unweighted energy is already influence-paid. Indeed, for independent `S,S'~p`,

\[
\sum_s\sum_{|d|\ge2}\left[(b^{(s)}*b^{(s)})(d)\right]^2
=4\Pr(|S\oplus S'|\ge2).
\tag{5.5}
\]

After median-character folding, if `q_i=min(Inf_i,1-Inf_i)`, then

\[
\mathbb E|S\oplus S'|
=2\sum_iq_i(1-q_i)\le2J,
\]

so

\[
\boxed{
\sum_s\sum_{|d|\ge2}\left[(b^{(s)}*b^{(s)})(d)\right]^2\le4J.
}
\tag{5.6}
\]

Thus the remaining difficulty is now sharply localized: control the correlation between this already-paid high-degree convolution energy and the coefficient height `log_2(1/p_s)`.

To apply the consumed valuation theorem to the **same** normalized remainder, for `s` in magnitude packet `a` write

\[
\log_2\frac1{p_s}=2(r_a+d_a).
\]

With `E_s` denoting the inner energy in (5.4), the valuation contribution is

\[
\frac12\sum_sE_sr_a
=2\sum_sp_sr_aw_s
\le2R\le4J.
\tag{5.7}
\]

Hence signed valuation depth is still completely influence-paid inside the new high-shift representation. The genuinely unpaid object is the **physical-height/mesh correlation with the high-degree deleted-convolution energy**, together with the need to retain the negative information slack rather than spend the whole `4J` valuation bound crudely.

## 6. Additional Booleanity lemma and limitation

A useful exact consequence of (5.1) is the pairwise amplitude exclusion

\[
\boxed{|a_s|+|a_t|\le1\quad(s\ne t).}
\tag{6.1}
\]

Indeed, for `d=s\oplus t`, the two distinguished terms in `(a*a)(d)=0` contribute `2a_sa_t`. Cauchy--Schwarz on the remaining terms gives

\[
2|a_sa_t|\le1-a_s^2-a_t^2,
\]

which is (6.1). The punctured-character family saturates (6.1) between its heavy Fourier coefficient `1-2/N` and every small coefficient `2/N`. Therefore pairwise amplitude exclusion alone cannot repair the local sharp-selector failure; the next step must exploit the higher-order convolution energy in (5.4), not only pairwise coefficient bounds.

## 7. Exact status, dead route, and next attack

### PROVED

- Exact real-restriction entropy identity (2.1), with negative orientation mutual information retained.
- Exact formula (2.3) for the drift of the already collision-KL-refunded remainder `R_*`.
- Closed punctured-character formulas (3.3)--(3.4).
- Exact Boolean deleted-coefficient convolution representation (5.4) and unweighted payment (5.6).
- Valuation contribution of that same representation is bounded by `4J` via the consumed fleet02 theorem.
- Pairwise Boolean amplitude exclusion (6.1).

### REFUTED

- `exists i: Delta_i T_2 <= 4 Delta_i J` universally; punctured character already fails in dimension four.
- `exists i: Delta_i R_* <= 4 Delta_i J` universally **even with the exact negative collision refund retained**; punctured character fails in dimension five.
- A sharp coefficient-four proof based only on leaving a fixed residual restriction dimension.

### OPEN / CONDITIONAL

- Global `T_2<=4J` and the sharper exact-refund target `R_*<=4J` remain OPEN.
- Full FEI remains OPEN.

### Next attack

Work directly with (5.4), not the dead local selector. Split the log height only after the high-degree convolution energy `E_s` is formed. Fleet02/B15 should receive the valuation-weighted part and seek a tail-majorized **energy-weighted** refinement; fleet04/B15 should receive the exact convolution form and try to retain `G_{<=1}` as the compensating information slack. The target for fleet03/B15 is a dimension-free bound on the physical mesh part

\[
2\sum_sp_sd_{a(s)}w_s
\]

coupled to either unused valuation slack or the exact low-fibre KL refund, not a separate credit-free mesh estimate.

## 8. Reproducibility

`check_refund_restriction_obstruction.py` uses only the Python standard library and rational arithmetic. Its `log_2` values are enclosed by the positive atanh series with an explicit rational tail. It certifies the strict margins

- `Delta T_2 - 4 Delta J > 0.0387230943450412` at `n=4`;
- `Delta R_* - 4 Delta J > 0.004862891152571594` at `n=5`;
- `Delta R_* - 4 Delta J > 0.015741607772096128` at `n=6`.

The checker proves only these stated inequalities and the punctured-character global sanity bounds; it is not an FEI certificate.
