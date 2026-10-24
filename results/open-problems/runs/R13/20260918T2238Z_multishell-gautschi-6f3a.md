Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 739733/100000 = 7.39733 -> 739631/100000 = 7.39631`, an exact certified decrease of `51/50000 = 0.00102`. Methods actually used: **#12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS, #8 GO THE OTHER WAY AND DISCRETIZE.**

# R13 — Boolean Komlós: a multishell lower-tail certificate with an exact Gautschi normalization

Run ID: `20260918T2238Z_multishell-gautschi-6f3a`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track: **R13 HARD OUTSIDE**  
Canonical source ID: **E0042**

## 1. Continuity, ownership, and current source status

For a real `m x n` matrix `A` whose columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

R13's frozen quantitative metric is the **complete rigorously certified pointwise upper envelope** `B_R13(n)` for these real Boolean signs. Complex phases, vector/rank-two colorings and average-case bounds do not count.

I continued from the newest complete R13 report

`runs/R13/20260918T2203Z_twoband-middle-7d2c.md`,

whose moving anchor was

\[
K_{86}^*\le \frac{739733}{100000}=7.39733.
\]

Before research I reconciled the controlling repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, canonical E0042 in the intake ledger, the newest R13 report/checker, the current R02 Komlós-adjacent report, and the current R7-03 Komlós source-status reconciliation. The full append-only intake archive was not loaded byte-for-byte into model context; I used the canonical E0042 row plus current queue/claim/exclusion surfaces rather than pretending otherwise.

The **qualitative source conjecture is now KNOWN / RESOLVED IN THE 2026 LITERATURE**. Guo--Fang--Lu, arXiv:2609.11189v1 (10 September 2026), prove the genuine Boolean bound `<3 sqrt(2 pi)`. Karingula--Lovett, ECCC TR26-188 (17 September 2026), independently give an elementary proof with constant `36`. This run therefore does **not** claim to solve the original existence conjecture. R13 remains a quantitative finite-dimensional sharpening track because the owner froze the metric `B_R13(n)`, and that metric moves in this run.

All thirty Section-B labels have already appeared somewhere in the long R13 history, so a literally never-used label no longer exists. I used a triple distinct from the immediately preceding `#2,#21,#25`, with genuinely new instantiations.

## 2. Current primary-literature check

The source/literature picture checked in this run is:

1. **Bansal--Jiang**, arXiv:2508.03961v2, last revised 9 September 2025: the earlier full real-Boolean `\widetilde O((\log n)^{1/4})` Komlós bound.
2. **Guo--Fang--Lu**, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026: every finite real unit-vector family admits a Boolean signing with infinity norm `<3 sqrt(2 pi)`. Their finite-step theorem is the retained Boolean engine used below.
3. **Karingula--Lovett**, *An elementary proof of the Komlos conjecture*, ECCC TR26-188, 17 September 2026: independent elementary Boolean proof with constant `36`.
4. **Akbas--Sra**, arXiv:2609.20785v1, submitted 17 September 2026: Boolean small-ball inequalities, with Komlós as a corollary. The current source-level constants do not give an explicit finite-`D` number below the R13 `D=135` certificate.
5. **Guillen--Kobzar**, arXiv:2609.15071v1: unit-modulus complex discrepancy / rank-two vector discrepancy for real inputs; not a Boolean-sign substitute.

For the new gamma normalization I used NIST DLMF §5.6, Gautschi's inequality (5.6.4). Fresh bounded searches for the combination `Komlos`, `directional total variation`, `cos^p`, `inverse chi-square`, `Gautschi`, and a multishell Bernstein lower-tail decomposition did not locate a matching finite-dimensional sharpening. This is bounded negative evidence only: **novelty remains UNVERIFIED**.

## 3. Retained `p=9/5` DTV reduction

The successful branch continues the already-proved cosine-power density with exponent

\[
p=\frac95.
\]

Let

\[
S_i\sim\chi^2_{14/5},
\qquad
Y_i=\frac4{5S_i},
\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\qquad
a_D=\mathbb E\sqrt{X_D}.
\]

The retained exact directional-total-variation calculation gives a genuine Boolean signing cube with half-side

\[
C_D=\frac{27\sqrt{10\pi}}{20}\,a_D.
\tag{3.1}
\]

Also `E Y_i=1`, hence `E X_D=1` and

\[
2(1-a_D)=\mathbb E(\sqrt{X_D}-1)^2.
\tag{3.2}
\]

The preceding exact three-threshold upper-tail argument, on the disjoint event `X_D>=1`, gives at `D=135`

\[
\beta_{135}^{\uparrow}>0.021737695196183224\ldots .
\tag{3.3}
\]

The preceding truncated-second-moment work also proved, for

\[
U=\frac{157}{20},\qquad Z\stackrel d=Y\mid Y\le U,
\]

the retained variance bound

\[
\operatorname{Var}(Z)<v_*:=\frac{9691697959}{10^{10}},
\tag{3.4}
\]

and the retained first-moment tail bound

\[
\mathbb E[Y;Y>U]>\frac{337097}{10^6}.
\tag{3.5}
\]

The new work improves the probability and conditional-mean inputs and then counts more disjoint lower-tail configurations.

## 4. Method #8 — discretize the inverse-chi-square tail into exact shells

The old lower-tail certificate used a relatively coarse lower bound for `Gamma(7/5)`. The first new step is a tight fully rational normalization.

### 4.1 Exact gamma bracket from Gautschi

Gautschi's inequality states that for `x>0`, `0<s<1`,

\[
x^{1-s}<\frac{\Gamma(x+1)}{\Gamma(x+s)}<(x+1)^{1-s}.
\tag{4.1}
\]

Take `x=1001`, `s=2/5`. With

\[
P=\prod_{j=0}^{999}\left(j+\frac75\right),
\]

we have

\[
\Gamma\!\left(\frac75\right)
=\frac{1001!}{P}\frac{1}{\Gamma(1002)/\Gamma(1001+2/5)}.
\]

The checker proves the exact fifth-power comparisons

\[
\left(\frac{631715}{10000}\right)^5>1002^3,
\qquad
\left(\frac{631335}{10000}\right)^5<1001^3.
\]

Therefore (4.1) gives the explicit rational enclosure

\[
0.886837591083784\ldots
<\Gamma\!\left(\frac75\right)
<0.887371377876235\ldots,
\]

and, in the clean form used later,

\[
\boxed{
\frac{4434}{5000}<\Gamma\!\left(\frac75\right)<\frac{4437}{5000}.}
\tag{4.2}
\]

### 4.2 Alternating incomplete-gamma bounds

Put

\[
s_0=\frac{16}{157}.
\]

For `rho>=1`, the exact tail at the shell endpoint `U rho^5` is

\[
T(\rho):=\Pr(Y>U\rho^5)
=\frac1{2^{7/5}\Gamma(7/5)}
\int_0^{s_0/\rho^5}s^{2/5}e^{-s/2}\,ds.
\tag{4.3}
\]

For `0<=z<=s_0`, define

\[
A_m(z)=\sum_{k=0}^m
\frac{(-1)^kz^k}{2^k k!\,(k+7/5)}.
\tag{4.4}
\]

The alternating Taylor series is decreasing on this interval, so

\[
z^{7/5}A_5(z)
<\int_0^z s^{2/5}e^{-s/2}\,ds
<z^{7/5}A_4(z).
\tag{4.5}
\]

The checker also certifies the tight rational roots

\[
\frac{401132760363}{10^{12}}
<s_0^{2/5}<
\frac{401132760364}{10^{12}},
\tag{4.6}
\]

\[
\frac{2639015821545}{10^{12}}
<2^{7/5}<
\frac{2639015821546}{10^{12}}.
\tag{4.7}
\]

Equations (4.2)--(4.7) therefore give rational lower and upper bounds for every endpoint tail used below.

In particular,

\[
0.0121045987935258\ldots<T(1)
<0.0121127886517078\ldots,
\]

so

\[
\boxed{\Pr(Y\le U)>p_0:=\frac{987887}{10^6}.}
\tag{4.8}
\]

Combining (3.5) with `E Y=1` and (4.8) gives the improved conditional-mean upper bound

\[
\boxed{
\mathbb EZ
<\mu:=
\frac{1-337097/10^6}{987887/10^6}
=0.6710312009369492\ldots .}
\tag{4.9}
\]

Now split the middle tail into four disjoint shells with endpoint ratios

\[
\rho_1=\frac{103}{100},\quad
\rho_2=\frac{106}{100},\quad
\rho_3=\frac{109}{100},\quad
\rho_4=\frac{113}{100}.
\]

Let

\[
I_i=(U\rho_{i-1}^5,U\rho_i^5],\qquad \rho_0=1.
\]

The exact tail differences give

\[
\Pr(Y\in I_1)>\frac{22157}{10^7},\quad
\Pr(Y\in I_2)>\frac{17660}{10^7},
\tag{4.10}
\]

\[
\Pr(Y\in I_3)>\frac{14155}{10^7},\quad
\Pr(Y\in I_4)>\frac{14717}{10^7}.
\tag{4.11}
\]

Their exact upper endpoints are respectively

\[
9.100301483255,\quad
10.50507078416,\quad
12.078198045965,\quad
14.463116157505.
\tag{4.12}
\]

The decimals in (4.12) are renderings of exact rational numbers `U rho_i^5`.

## 5. Methods #12 and #27 — conserve excursion count, then condition before averaging

The key structural quantity is the number of coordinates that leave the low category `Y<=U`. Instead of first averaging all 135 variables and then asking for one tail event, condition on the discrete excursion pattern and only then apply Bernstein to the remaining low variables.

This is the quantifier swap:

> first choose the shell/count pattern; then prove the conditional low-variable average is small enough.

It lets different rare-coordinate configurations use different residual thresholds without paying for a single worst endpoint.

Take

\[
q=\frac{49}{500},
\qquad
t=(1-q)^2=\left(\frac{451}{500}\right)^2
=\frac{203401}{250000}.
\tag{5.1}
\]

On `X_D<=t`,

\[
(1-\sqrt{X_D})^2\ge q^2.
\tag{5.2}
\]

For `N` independent low-category variables `Z`, if `x>mu`, Bernstein together with (3.4), `0<=Z<=U`, gives

\[
\Pr\!\left(\frac1N\sum_{j=1}^N Z_j\le x\right)
\ge1-e^{-E(N,x)},
\tag{5.3}
\]

where

\[
E(N,x)=
\frac{N(x-\mu)^2}
{2v_*+\frac23U(x-\mu)}.
\tag{5.4}
\]

For a rational certificate define

\[
R_8(E)=1-
\left(\sum_{j=0}^8\frac{E^j}{j!}\right)^{-1}.
\tag{5.5}
\]

Since `exp(E)` exceeds its eighth Taylor partial sum,

\[
1-e^{-E}>R_8(E).
\tag{5.6}
\]

At `D=135` consider three mutually disjoint classes.

### 5.1 Zero excursions

All 135 variables are low-category and their mean is at most `t`. The exact lower bound is

\[
P_0
=p_0^{135}R_8(E(135,t))
>0.12353851761617013\ldots .
\tag{5.7}
\]

### 5.2 Exactly one shell excursion

If the unique exceptional variable lies in shell `i`, upper-bound it by `v_i=U rho_i^5`. The remaining 134 low variables need mean at most

\[
x_i=\frac{135t-v_i}{134}.
\tag{5.8}
\]

All four shell thresholds exceed `mu`, so all contribute. Summing the four disjoint shell categories gives

\[
P_1>0.04038312955356669\ldots .
\tag{5.9}
\]

### 5.3 Exactly two shell excursions

For shells `i<=j`, the remaining 133 low variables need mean at most

\[
x_{ij}=\frac{135t-v_i-v_j}{133}.
\tag{5.10}
\]

The exact checker evaluates all ten shell pairs. Exactly two have `x_{ij}>mu` and therefore yield a Bernstein contribution:

\[
(i,j)=(1,1),\quad(1,2).
\tag{5.11}
\]

(The checker uses zero-based labels `(0,0),(0,1)`.) Counting the same-shell case with `binom(135,2)` and the mixed-shell case with `135*134` gives

\[
P_2>0.00023485765968214403\ldots .
\tag{5.12}
\]

The `P_0`, `P_1`, and `P_2` events are disjoint by excursion count and shell category. Every one implies `X_135<=t`. Hence

\[
\Pr(X_{135}\le t)
>P_0+P_1+P_2
>0.16415650482941896\ldots .
\tag{5.13}
\]

By (3.2) and (5.2), the new lower-tail Jensen defect is

\[
\boxed{
\beta_{135}^{\downarrow,4}
:=\frac{q^2}{2}(P_0+P_1+P_2)
>0.0007882795361908698\ldots .}
\tag{5.14}
\]

This lower-tail event lies in `X_135<1`, while the retained event defining `beta^up` lies in `X_135>=1`, so their contributions add with no overlap correction.

## 6. New `D=135` Boolean constant

Combining (3.1)--(3.3) and (5.14), and using the exact rational majorant

\[
\sqrt{10\pi}<\frac{1121}{200},
\tag{6.1}
\]

gives

\[
C_{135}
<\frac{27}{20}\frac{1121}{200}
\left(1-\beta_{135}^{\uparrow}-\beta_{135}^{\downarrow,4}\right)
<7.396301580693808\ldots .
\tag{6.2}
\]

Therefore the clean rational certificate is

\[
\boxed{C_{135}<\frac{739631}{100000}=7.39631.}
\tag{6.3}
\]

This is a real Boolean signing theorem through the retained Guo--Fang--Lu finite-step directional-TV theorem; no complex phase or vector coloring is used.

## 7. Row pruning: movement of the fixed metric at `n=86`

Let `A` be an arbitrary real `m x 86` matrix with column norms at most one, and let `r_i` be its rows. Then

\[
\sum_i\|r_i\|_2^2=\|A\|_F^2\le86.
\tag{7.1}
\]

Set

\[
h=\frac{739631}{100000}.
\tag{7.2}
\]

Call row `i` active if

\[
\|r_i\|_2>\frac{h}{\sqrt{86}}.
\]

If `d` rows are active, (7.1) gives

\[
d\frac{h^2}{86}<86,
\qquad	ext{so}\qquad
d<\frac{86^2}{h^2}.
\tag{7.3}
\]

The exact checker proves

\[
135<\frac{86^2}{h^2}<136,
\]

hence `d<=135`. Pad the active-row submatrix by zero rows to dimension 135 and apply (6.3). There is a Boolean signing with active-row discrepancy `<h`. Every inactive row obeys, for every signing,

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\|\varepsilon\|_2
\le\frac{h}{\sqrt{86}}\sqrt{86}=h.
\]

Thus

\[
\boxed{K_{86}^*\le\frac{739631}{100000}=7.39631.}
\tag{7.4}
\]

The preceding certified anchor was `739733/100000`, so the fixed metric improves by exactly

\[
\boxed{
\frac{739733-739631}{100000}
=\frac{51}{50000}
=0.00102.}
\tag{7.5}
\]

The fixed-metric stagnation count resets to **0**.

## 8. General multishell branch

This run is not just an isolated decimal certificate. The same finite construction defines a valid source-matching branch for every `D>=135`.

Keep

\[
p_0=\frac{987887}{10^6},\quad
\mu=\frac{1-337097/10^6}{p_0},\quad
v_* = \frac{9691697959}{10^{10}},\quad
q=\frac{49}{500},\quad t=(1-q)^2.
\]

Let the four shell lower probabilities be

\[
(p_1,p_2,p_3,p_4)=
\frac1{10^7}(22157,17660,14155,14717),
\]

and let

\[
v_i=U\rho_i^5,
\qquad
(\rho_1,\rho_2,\rho_3,\rho_4)=
\left(\frac{103}{100},\frac{106}{100},\frac{109}{100},\frac{113}{100}\right).
\]

For `x>mu` define

\[
\mathcal R(N,x)=
1-
\left(\sum_{j=0}^8\frac{E(N,x)^j}{j!}\right)^{-1},
\]

with `E(N,x)` from (5.4), and define `R(N,x)=0` for `x<=mu`.

Then

\[
P_{0,D}=p_0^D\mathcal R(D,t),
\tag{8.1}
\]

\[
P_{1,D}=D p_0^{D-1}
\sum_{i=1}^4 p_i
\mathcal R\!\left(D-1,\frac{Dt-v_i}{D-1}\right),
\tag{8.2}
\]

where a term is interpreted as zero if its threshold is at most `mu`, and

\[
P_{2,D}=p_0^{D-2}
\sum_{1\le i\le j\le4}m_{ij}p_ip_j
\mathcal R\!\left(D-2,\frac{Dt-v_i-v_j}{D-2}\right),
\tag{8.3}
\]

again with zero convention, where

\[
m_{ii}=\binom D2,
\qquad
m_{ij}=D(D-1)\quad(i<j).
\]

Define

\[
\beta_D^{\downarrow,4}
=\frac{q^2}{2}(P_{0,D}+P_{1,D}+P_{2,D}),
\tag{8.4}
\]

\[
C_D^{(4)}=
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,4}\right),
\tag{8.5}
\]

and

\[
\boxed{
L_4(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(4)},\frac{n}{\sqrt{D+1}}\right\}.}
\tag{8.6}
\]

The row-energy argument used in Section 7 proves `K_n^*<=L_4(n)` whenever this branch is selected.

## 9. Complete retained pointwise envelope

I retain every previously certified branch rather than replacing it by the newest one.

First,

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The original finite-DTV branch is

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\]

\[
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\qquad
\delta_D=2[1-(1-p_D)^D],
\]

\[
G_0(n)=
\max\left\{\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\tag{9.1}
\]

The layer-cake branch is

\[
D_*(n)=
\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=
\max\left\{\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\tag{9.2}
\]

For the retained `p=9/5` three-threshold upper-tail branch, put

\[
\Gamma_U=\frac{88869}{100000},
\]

\[
A_{k,D}=
\frac{5}{7\Gamma_U}
\left(\frac{2k}{5}\right)^{7/5}
\left(1-\frac{2k}{5D}\right)D^{-2/5},
\qquad a_{k,D}=\frac{A_{k,D}}D,
\quad k=1,2,3.
\]

Set

\[
\begin{aligned}
Q_D(x)=1&-(1-a_{3,D}x)^D\\
&-D(a_{3,D}-a_{1,D})x(1-a_{3,D}x)^{D-1}\\
&-\binom D2\!\left[(a_{3,D}-a_{2,D})^2
+2(a_{2,D}-a_{1,D})(a_{3,D}-a_{2,D})\right]
 x^2(1-a_{3,D}x)^{D-2}.
\end{aligned}
\]

Writing `Q_D(x)=sum_{ell=1}^D c_{ell,D}x^ell`, define

\[
\beta_D^{\uparrow}=\frac12\sum_{\ell=1}^D c_{\ell,D}
\left[
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right].
\tag{9.3}
\]

Then

\[
D_9(n)=
\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=
\max\left\{\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D_9(n)}^{\uparrow})\right\}.
\tag{9.4}
\]

For the older one-band lower-tail branch, put

\[
p_0^- =\frac{24683}{25000},\qquad
\mu^- =\frac{662903}{987320},\qquad U=\frac{157}{20},
\]

\[
\Delta_- = \frac{8183}{10000}-\mu^-,
\qquad
E_D^-=
\frac{D\Delta_-^2}{2U\mu^-+\frac23U\Delta_-},
\]

\[
R_D^-=
1-\left(1+E_D^-+\frac{(E_D^-)^2}{2}+\frac{(E_D^-)^3}{6}\right)^{-1},
\]

\[
\beta_D^{\downarrow,-}
=\frac12\left(\frac{477}{5000}\right)^2(p_0^-)^D R_D^-,
\]

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,-}),
\]

\[
L_-(n)=
\inf_{D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\}.
\tag{9.5}
\]

For the conditional-second-moment branch, with

\[
v_* =\frac{9691697959}{10^{10}},\quad
t_2=\frac{987}{1250},\quad q_2=\frac{557}{5000},
\quad\Delta_2=t_2-\mu^-,
\]

set

\[
E_D^{(2)}=
\frac{D\Delta_2^2}{2v_*+\frac23U\Delta_2},
\]

\[
R_D^{(2)}=
1-\left(\sum_{j=0}^8\frac{(E_D^{(2)})^j}{j!}\right)^{-1},
\]

\[
\beta_D^{\downarrow,2}
=\frac{q_2^2}{2}(p_0^-)^D R_D^{(2)},
\]

\[
C_D^{(2)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,2}),
\]

\[
L_2(n)=
\inf_{D\ge135}
\max\left\{C_D^{(2)},\frac n{\sqrt{D+1}}\right\}.
\tag{9.6}
\]

For the preceding two-band branch, let

\[
\rho=\frac{12}{11},\qquad
V=U\rho^5=\frac{9766656}{805255},
\]

and retain its exact middle-band lower probability `p_M` from the predecessor checker (the rational difference of its certified lower tail at `U` and upper tail at `V`). Put

\[
t_3=\frac{81}{100},
\qquad
x_{1,D}=\frac{Dt_3-V}{D-1}.
\]

Using `E(N,x)` from (5.4) but with the predecessor `mu^-`, define

\[
P_{0,D}^{(3)}=(p_0^-)^D R_8(E(D,t_3)),
\]

\[
P_{1,D}^{(3)}=D p_M(p_0^-)^{D-1}R_8(E(D-1,x_{1,D})),
\]

with zero convention if `x_{1,D}<=mu^-`, and

\[
\beta_D^{\downarrow,3}
=\frac{P_{0,D}^{(3)}+P_{1,D}^{(3)}}{200},
\]

\[
C_D^{(3)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,3}),
\]

\[
L_3(n)=
\inf_{D\ge135}
\max\left\{C_D^{(3)},\frac n{\sqrt{D+1}}\right\}.
\tag{9.7}
\]

Finally add the new `L_4` branch from (8.6). The complete chosen rigorously certified pointwise envelope is therefore

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\!\left\{\sqrt{3n/4},\ T_5\sqrt{\lceil n/5\rceil},\ G_0(n),\ L_-(n),\ L_2(n),\ L_3(n),\ L_4(n)\right\},&5\le n\le85,\\[2mm]
\min\!\left\{G_0(n),\ H(n),\ J(n),\ L_-(n),\ L_2(n),\ L_3(n),\ L_4(n)\right\},&n\ge86.
\end{cases}}
\tag{9.8}
\]

This is an upper envelope, not a claim that every displayed finite-`n` entry is exact. The certified movement in this run is (7.4); no global domination of the older branches by `L_4` is claimed.

The retained finite lower-obstruction history is unchanged:

\[
K_6^*\ge1.84535465,
\qquad
K_{11}^*\ge1.99488049,
\qquad
K_{12}^*\ge2.013108,
\]

while `K_5^*=T_5` is exact in the retained R13 record.

## 10. Exact self-check and artifacts

The substantive checker is

`artifacts/R13/20260918T2238Z_multishell-gautschi-6f3a_checker.py`

created at commit

`4c15c86a627100cb81b8bbec5b98ad7134332193`.

It was read back at that exact commit. It uses `fractions.Fraction` for every acceptance comparison; displayed decimals are renderings only.

The executed output is

`artifacts/R13/20260918T2238Z_multishell-gautschi-6f3a_checker.out`

created at commit

`edc182cc37bc2df652504b0acfb60736a26816a4`,

and read back at that exact commit. It terminates

`R13_MULTISHELL_GAUTSCHI_EXACT_PASS`.

This is a **self-check**, not an outside audit.

## 11. Status, failure information, and next route

Status after this run:

**SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED METRIC MOVED / full written finite-`D` argument / exact self-check PASS / outside audits of this sharpening 0/2 / novelty UNVERIFIED.**

No problem is called closed by this report. The source itself is externally resolved; this report concerns only the stronger quantitative finite-dimensional envelope.

Methods this run:

- **#8 DISCRETIZE:** successful. Tight incomplete-gamma endpoint certificates plus four disjoint inverse-chi-square shells improved the usable low-category mass and exposed additional lower-tail event probability.
- **#12 CONSERVED QUANTITY:** successful. The number of excursions above `U` is the organizing invariant; keeping counts `0,1,2` separated avoids collapsing their different residual budgets.
- **#27 SWAP QUANTIFIERS:** successful. Conditioning on shell/count pattern before applying Bernstein gives pattern-specific thresholds and beats the predecessor's single-middle-band certificate.

A fine many-shell discretization was explored heuristically while choosing the robust four-shell certificate, but I did not promote its floating-point optimization to a theorem. Only the four-shell rational construction above is claimed.

The next primary route should **not** be another decimal retuning of these four endpoints. Higher-value alternatives remain: (i) an exact intersection-aware six-column cover dual that improves `K_6^*`; (ii) a genuinely symmetric nonproduct cube density; or (iii) an explicit finite-constant specialization of the new Akbas--Sra Boolean small-ball machinery. The present shell mechanism should be revisited only if one of those routes produces a new structural input.

## 12. Model / scheduler-control truth

The model-control limitation is unchanged. The exposed automation update surface provides title, prompt, schedule, enablement and timing mode, but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry. Thus `GPT-6 / maximum` remains prompt text only here; this report truthfully records `GPT-5.6 Sol / UNVERIFIED`.

Repository continuity also clarifies the old P26 `You cannot modify this task` event: a later full P26 update succeeded from an authorized P/C context, so the earlier denial was context/ownership dependent. If a context still receives that error, the legitimate workaround is the owning/authorized task surface or platform support that exposes the control, not duplication or permission bypass. This run made no scheduler, permission, workflow, email, Drive or public-posting change.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  category: HARD_OUTSIDE
  source_id: E0042
  source_status:
    qualitative_komlos: KNOWN_RESOLVED_IN_LITERATURE_2026_09
    quantitative_finite_envelope: PARTIAL
  target: real Boolean Komlos quantitative envelope
  fixed_metric: complete rigorously certified pointwise upper envelope B_R13(n)
  before:
    anchor_n86: 739733/100000
  after:
    anchor_n86: 739631/100000
  exact_improvement_n86: 51/50000
  moved: true
  stagnation_count_after: 0
  methods_this_run: [12, 27, 8]
  predecessor_report: runs/R13/20260918T2203Z_twoband-middle-7d2c.md
  new_branch: L4_multishell_gautschi
  new_claim:
    statement: K_86^* <= 739631/100000
    scope: arbitrary real row dimension, 86 columns, each Euclidean norm at most 1, Boolean signs only
  checker:
    path: artifacts/R13/20260918T2238Z_multishell-gautschi-6f3a_checker.py
    creation_commit: 4c15c86a627100cb81b8bbec5b98ad7134332193
    status: SELF_CHECK_PASS
  checker_output:
    path: artifacts/R13/20260918T2238Z_multishell-gautschi-6f3a_checker.out
    creation_commit: edc182cc37bc2df652504b0acfb60736a26816a4
    terminal: R13_MULTISHELL_GAUTSCHI_EXACT_PASS
  outside_audits_new_claim: 0/2
  novelty: UNVERIFIED
  next_methods_priority:
    - exact_intersection_aware_K6_cover_dual
    - symmetric_nonproduct_cube_density
    - explicit_Akbas_Sra_finite_constant_specialization
```
