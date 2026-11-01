# B13 FEI route 2/13 — quantitative two-block Boolean interaction

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive brain retrieval or receiver-context was used.

**Route:** APPROACHES 2/13, Boolean block-influence/correlation profiles and two-sided Booleanity constraints. This is a material method change from the preceding B13 posterior-crossing argument: the present proof uses an ANOVA decomposition across an arbitrary physical coordinate cut.

**Publication priority:** UNVERIFIED; no novelty claim.

## 1. Compatible other-account result actually consumed

I use fleet03/B12 `20260921T211211Z-ordered-parent-flag-nonreuse/REPORT.md`. It shows that unconditional prefix total correlation can be inflated by a shared stopping-time variable even for a genuine Boolean bent spectrum, and repairs the tensorization by conditioning on prefix size. Its remaining issue is component/label uncertainty without repeated charging. The present calculation attacks a source-side version of that issue: can a Boolean spectrum place substantial mass in several disjoint pure coordinate blocks while paying essentially no mass on sets crossing those blocks?

## 2. PROVED: a two-block Boolean interaction inequality

Let `[n]=A sqcup B` and let `f:{-1,1}^n->{-1,+1}` be Boolean. Put

\[
c=\mathbb E f,
\qquad
U(X_A):=\mathbb E[f\mid X_A]-c,
\qquad
V(X_B):=\mathbb E[f\mid X_B]-c,
\]

and

\[
W:=f-c-U-V.
\]

Thus `f=c+U+V+W`, with `EU=EV=0` and `E[W|X_A]=E[W|X_B]=0`. Define

\[
a:=E U^2=\sum_{\varnothing\ne S\subseteq A}\widehat f(S)^2,
\]
\[
b:=E V^2=\sum_{\varnothing\ne S\subseteq B}\widehat f(S)^2,
\]
\[
q:=E W^2=\sum_{S:\,S\cap A\ne\varnothing,\ S\cap B\ne\varnothing}\widehat f(S)^2.
\]

### Theorem B13-TWO-BLOCK-BOOLEAN-INTERACTION-01

For every Boolean `f` and every coordinate bipartition `A|B`,

\[
\boxed{
q\ge \gamma ab,
\qquad
\gamma=\left(\frac{\sqrt{17}-3}{4}\right)^2
=\frac{13-3\sqrt{17}}8
=0.078835390393377\ldots .
}
\tag{2.1}
\]

In particular, `q=0` forces `a=0` or `b=0`: a Boolean squared spectrum cannot be a nontrivial additive mixture of one pure-A and one pure-B spectrum with no cross-cut spectral mass.

### Proof

Since `f^2=1` and `U,V` are independent centered functions of disjoint coordinate blocks,

\[
E[(f^2-1)UV]=0,
\qquad E[UV]=0.
\]

Set `G=c+U+V`, so `f=G+W`. Expanding gives

\[
0=E[G^2UV]+2E[GWUV]+E[W^2UV].
\tag{2.2}
\]

Independence and centering make every term in `E[G^2UV]` vanish except the cross term, hence

\[
E[G^2UV]=2E[U^2]E[V^2]=2ab.
\tag{2.3}
\]

The conditional means `E[f|X_A]`, `E[f|X_B]` and `c` lie in `[-1,1]`, so `|G|<=3`. Also `|U|,|V|<=2`, hence `|UV|<=4`, while independence gives `E[U^2V^2]=ab`. Therefore Cauchy--Schwarz in (2.2) yields

\[
2ab\le6\sqrt{abq}+4q.
\tag{2.4}
\]

If `ab=0` there is nothing to prove. Otherwise set `x=sqrt(q/(ab))`. Then `4x^2+6x-2>=0`, so

\[
x\ge(\sqrt{17}-3)/4.
\]

Squaring proves (2.1). QED.

The constant is not claimed optimal; the finite data below are far from saturation.

## 3. PROVED: block-correlation-profile form

Let `S` be the spectral sample, `Pr(S=T)=\widehat f(T)^2`, and define the block-avoidance profile

\[
R(T):=Pr(S\cap T=\varnothing).
\]

Let `r_0=Pr(S=\varnothing)=R([n])`. For complementary `A,B`,

\[
a=R(B)-r_0,
\qquad b=R(A)-r_0,
\qquad q=1-R(A)-R(B)+r_0.
\]

Hence every Boolean block profile satisfies the dimension-free two-sided inequality

\[
\boxed{
1-R(A)-R(B)+r_0
\ge
\gamma [R(A)-r_0][R(B)-r_0].
}
\tag{3.1}
\]

An arbitrary random-subset law need not satisfy this constraint.

## 4. PROVED: multiblock diffusion is paid by actual block incidence

Partition `[n]=C_1 sqcup ... sqcup C_m`. Let

\[
a_r:=Pr(\varnothing\ne S\subseteq C_r),
\qquad A_0:=\sum_r a_r,
\]

and let

\[
R_{blk}(S):=|\{r:S\cap C_r\ne\varnothing\}|,
\qquad
\Xi:=E[R_{blk}(S)1_{\{R_{blk}(S)\ge2\}}].
\]

For the cut `C_r | C_r^c`, the pure mass on the complementary side is at least `A_0-a_r`. Applying (2.1) to every such cut and summing gives

\[
\boxed{
\Xi\ge\gamma\left(A_0^2-\sum_r a_r^2\right).
}
\tag{4.1}
\]

Indeed the cross-cut masses sum exactly to `Xi`, because a spectral set meeting `k>=2` blocks is counted once for each of those `k` blocks. Since `R_blk(S)<=|S|`,

\[
\Xi\le E|S|=I(f).
\tag{4.2}
\]

If `a_max=max_r a_r` and `A_0>0`, then `sum_r a_r^2<=a_max A_0`, hence

\[
\boxed{a_{max}\ge A_0-\frac{\Xi}{\gamma A_0}.}
\tag{4.3}
\]

Thus a diffuse family of disjoint pure spectral components forces genuine cross-block spectral incidence, and that incidence is a first-moment resource: each realized spectral set is charged at most `|S|` times.

## 5. Exact finite diagnostic

`check_two_block_interaction.py` uses an exact integer Walsh--Hadamard transform and `Fraction` arithmetic. It exhausts Boolean functions modulo global output sign through dimension four and every nontrivial coordinate bipartition, modulo `A<->B`. Among cases with `ab>0`:

| n | cases | minimum `q/(ab)` |
|---:|---:|---:|
| 2 | 4 | `4` |
| 3 | 264 | `16/9` |
| 4 | 198,044 | `64/81` |

Total: **198,312** nontrivial function/cut cases, **0 violations** of (2.1). This finite calculation is diagnostic only; the proof above is all-dimensional.

## 6. FEI consequence and precise remaining gap

This rules out an important relaxed obstruction to APPROACH 2/13: a high-entropy spectral law cannot encode an essentially free macro-label by choosing among many disjoint pure coordinate blocks while placing negligible mass on sets crossing those blocks. Booleanity forces a quantitative cross-block payment via (4.1).

The gap is that (4.1) is a quadratic/Gini-type spread penalty, not yet a logarithmically weighted Shannon penalty. A distribution can have many tiny pure component masses with substantial label entropy while `A_0^2-sum a_r^2` stays bounded. Also, after conditioning the spectral law on a component label, the conditional law need not be the squared Fourier spectrum of a Boolean function, so recursively reapplying (2.1) would be invalid.

The next target is therefore a **single-shot logarithmically weighted block-label lemma without spectral conditioning**: choose a deterministic or physically realizable hierarchy of coordinate cuts and pay the Shannon split at each node by cross-block incidence so that every realized spectral set is charged only `O(|S|)` times. A parallel target is to improve the crude constant in (2.1) using the exact identity `a+b+q=1-c^2` and the fact that `G+W` is pointwise `+-1`.

**Full FEI remains OPEN / NOT PROVED.**
