Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 739631/100000 = 7.39631 -> 739377/100000 = 7.39377`, an exact certified decrease of `127/50000 = 0.00254`. Methods actually used: **#24 FIND THE EXTREMAL OBJECT, #3 PROVE SOMETHING STRONGER, #19 MAKE IT AN ALGORITHM.**

# R13 — Boolean Komlós: Cantelli lower tails and a five-threshold occupancy cascade

Run ID: `20260918T2334Z_cantelli-cascade-c4a7`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track: **R13 HARD OUTSIDE**  
Canonical source ID: **E0042**

## 1. Continuity, metric, and current source status

For a real `m x n` matrix `A` whose columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

R13's fixed quantity is the **complete rigorously certified pointwise upper envelope** `B_R13(n)` for genuine real Boolean signs. Complex phases, vector/rank-two colorings and average-case bounds do not count.

I continued from the newest complete R13 report

`runs/R13/20260918T2238Z_multishell-gautschi-6f3a.md`,

whose moving anchor was

\[
K_{86}^*\le \frac{739631}{100000}=7.39631.
\]

Before new mathematics I reread/reconciled the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the controlling new-methods policy and owner directive, the newest R13 report and checker, and the current Komlós-adjacent R02 and R7-03 source-status reports. The append-only intake archive was not pretended to have been loaded byte-for-byte into model context; the canonical E0042/R13 history and current ownership/exclusion surfaces were used.

The **qualitative Komlós conjecture is now KNOWN / resolved in the current 2026 literature**, not a fleet claim: Guo--Fang--Lu, arXiv:2609.11189v1 (10 September 2026), prove the genuine Boolean constant `3 sqrt(2 pi)`, and Karingula--Lovett, ECCC TR26-188 (17 September 2026), independently give an elementary Boolean proof with constant `36`. Bansal--Jiang remains the earlier `\widetilde O((\log n)^{1/4})` Boolean result. Akbas--Sra, arXiv:2609.20785v1 (17 September 2026), prove Boolean small-ball inequalities and recover Komlós, but their source statement does not expose a numerical finite-dimensional specialization beating the R13 certificate below. R13 therefore remains only a **finite-dimensional quantitative sharpening** track.

All thirty Section-B labels have already appeared somewhere in R13 history. The immediately preceding triple was `#12,#27,#8`; this run uses the distinct triple `#24,#3,#19` with materially new implementations.

## 2. Retained `p=9/5` directional-TV reduction

The starting density is the already-proved cosine-power family with

\[
p=\frac95.
\]

Let

\[
S_i\sim\chi^2_{14/5},\qquad
Y_i=\frac4{5S_i},\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\qquad a_D=\mathbb E\sqrt{X_D}.
\]

The retained directional-total-variation calculation gives a genuine Boolean signing cube with half-side

\[
C_D=\frac{27\sqrt{10\pi}}{20}\,a_D.\tag{2.1}
\]

Since `E Y_i=1`,

\[
2(1-a_D)=\mathbb E(\sqrt{X_D}-1)^2.\tag{2.2}
\]

Thus any rigorous positive lower bound on the squared Jensen defect, from disjoint lower- and upper-tail events, lowers the Boolean signing constant.

## 3. Method #3 — prove a stronger truncated-moment package

Put

\[
U=\frac{157}{20},\qquad s_0=\frac{16}{157},\qquad Z\stackrel d=Y\mid Y\le U.
\]

The Gautschi certificate retained from the preceding run is

\[
\frac{4434}{5000}<\Gamma(7/5)<\frac{4437}{5000},\tag{3.1}
\]

with exact fifth-power witnesses. Using the alternating incomplete-gamma series together with

\[
\frac{401132760363}{10^{12}}<s_0^{2/5}<\frac{401132760364}{10^{12}},
\]

\[
\frac{2639015821545}{10^{12}}<2^{7/5}<\frac{2639015821546}{10^{12}},
\]

the new checker proves the stronger probability and first-moment brackets

\[
\boxed{
\frac{9878872}{10^7}<\Pr(Y\le U)<\frac{9878955}{10^7}},\tag{3.2}
\]

\[
\boxed{
\frac{3376616}{10^7}<\mathbb E[Y;Y>U]<\frac{3378901}{10^7}}.\tag{3.3}
\]

Consequently

\[
0.6702226095776325\ldots<\mathbb EZ
<0.6704595423445106\ldots .\tag{3.4}
\]

The new point is that the second moment can be bounded without the old crude inequality `Y^2<=UY`. Writing `c=4/5`, integration by parts gives the exact identity

\[
\begin{aligned}
M_2&:=\mathbb E[Y^2;Y\le U]\\
&=
\frac{c^2(5/3)s_0^{-3/5}e^{-s_0/2}}
{2^{7/5}\Gamma(7/5)}
-\frac23+\frac23\mathbb E[Y;Y>U].
\end{aligned}\tag{3.5}
\]

The same rational root/gamma/Taylor bounds therefore yield

\[
\boxed{\mathbb E Z^2<1.2789865976106685\ldots},\tag{3.6}
\]

and, using the lower bound in (3.4),

\[
\boxed{\operatorname{Var}(Z)<0.8297882512216169\ldots}.\tag{3.7}
\]

This is the stronger statement that made the next route worthwhile: the previous retained variance cap was about `0.96917`.

The four disjoint middle shells from the predecessor are retained and re-certified under (3.1):

\[
I_j=(U\rho_{j-1}^5,U\rho_j^5],
\quad
(\rho_1,\rho_2,\rho_3,\rho_4)=(1.03,1.06,1.09,1.13),
\]

with probability lower bounds

\[
(p_1,p_2,p_3,p_4)
=10^{-7}(22157,17660,14155,14717),\tag{3.8}
\]

and exact upper endpoints

\[
(v_1,v_2,v_3,v_4)=
(9.100301483255,10.50507078416,12.078198045965,14.463116157505),\tag{3.9}
\]

where each decimal in (3.9) is merely the rendering of the exact rational `U rho_j^5`.

## 4. Method #24 — Cantelli is the extremal one-sided second-moment bound

The preceding lower-tail certificates used Bernstein after conditioning on a shell pattern. Once the first two moments in Section 3 are available, the sharper object is the one-sided second-moment extremal inequality itself.

If `Z_1,...,Z_N` are independent copies of `Z`, `E Z<=mu_+`, `Var(Z)<=v_+`, and `x>mu_+`, Cantelli gives

\[
\Pr\!\left(\frac1N\sum_{j=1}^NZ_j\le x\right)
\ge
\frac{N(x-\mu_+)^2}{v_++N(x-\mu_+)^2}.\tag{4.1}
\]

This is valid because the true conditional mean is at most `mu_+`, so an upper deviation beyond `x` is at least `x-mu_+`; the variance of the mean is at most `v_+/N`.

For the exact `D=135` certificate take

\[
q=\frac{106965}{10^6},\qquad t=(1-q)^2.\tag{4.2}
\]

Condition first on the exact shell-count pattern and apply (4.1) only to the remaining low variables. The checker counts disjoint patterns with 0, 1 and 2 middle-shell excursions. Their rigorous probability contributions are

\[
P_0>0.13975579652417644\ldots,\tag{4.3}
\]

\[
P_1>0.05099158549163446\ldots,\tag{4.4}
\]

\[
P_2>0.000006793702570204777\ldots.\tag{4.5}
\]

For `k=1` all four shells contribute. For `k=2`, the exact residual-mean test leaves only the pattern with both excursions in the first shell. No pattern with `k>=3` has residual threshold above the certified conditional-mean upper bound. Hence

\[
\Pr(X_{135}\le t)
>0.1907541757183811\ldots .\tag{4.6}
\]

On this event `(1-sqrt(X_135))^2>=q^2`, giving the lower-tail contribution

\[
\boxed{
\beta_{135}^{\downarrow}>0.001091258021348740\ldots}.\tag{4.7}
\]

to `1-E sqrt(X_135)`.

## 5. Method #19 — make the upper-tail search a five-threshold occupancy algorithm

The predecessor used three sufficient upper-tail mechanisms. This run turns the whole finite threshold search into a small dynamic program and pushes it to five thresholds.

For `t>=1` and `k=1,...,5`, the event

\[
Y_i\ge \frac{Dt}{k}
\]

has probability at least

\[
\frac{A_{k,D}}D t^{-7/5},\tag{5.1}
\]

where one valid explicit choice is

\[
A_{k,D}=
\frac{5}{7(4437/5000)}
\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5}.\tag{5.2}
\]

This follows directly from the `chi^2_{14/5}` density and `e^{-s/2}>=1-s/2`; the factor in (5.2) is deliberately smaller than the exact linear correction, so it is valid uniformly for `t>=1`.

Set `a_k=A_{k,D}/D`, `a_0=0`, and `d_k=a_k-a_{k-1}`. Introduce a model category `R` with

\[
\Pr(R=k)=d_k x,\qquad x=t^{-7/5},\qquad k=1,\ldots,5,
\]

and remaining mass `1-a_5x`. The actual nested threshold category stochastically dominates this model in the required direction because its cumulative probabilities satisfy `P(R_actual<=k)>=a_kx`; a coordinatewise quantile coupling therefore makes the event below at least as likely for the actual variables.

The sufficient event for `X_D>=t` is

\[
\exists k\le5:\quad
\#\{i:Y_i\ge Dt/k\}\ge k.\tag{5.3}
\]

Its complement has every prefix count at most `k-1`. Let `F_{1,0}=1`, all unspecified `F` be zero, and recursively for `k=2,...,5`, `0<=r<=k-1`, define

\[
F_{k,r}=\sum_{s=0}^{r}F_{k-1,r-s}\frac{d_k^s}{s!}.\tag{5.4}
\]

Then the model complement polynomial is

\[
C_{D,5}(x)=
\sum_{r=0}^{4}
\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r},\tag{5.5}
\]

and `Q_{D,5}(x)=1-C_{D,5}(x)` is a rigorous lower bound for the upper-tail event in (5.3). Write

\[
Q_{D,5}(x)=\sum_{\ell=1}^{D}c_{\ell,D}^{(5)}x^\ell.\tag{5.6}
\]

The upper half of the Jensen defect is therefore bounded by the exact layer-cake integral

\[
\boxed{
\beta_{D,5}^{\uparrow}
=\frac12\sum_{\ell=1}^{D}c_{\ell,D}^{(5)}
\left(
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right).}\tag{5.7}
\]

At `D=135` the exact checker uses rational sub-coefficients

\[
A_1=\frac{31276223}{10^9},\quad
A_2=\frac{20573291}{250000000},\quad
A_3=\frac{18092773}{125000000},
\]

\[
A_4=\frac{215878339}{10^9},\quad
A_5=\frac{73539201}{250000000},\tag{5.8}
\]

verifies each is below (5.2) by an exact fifth-power comparison, and obtains

\[
\boxed{
\beta_{135,5}^{\uparrow}
>0.021769593407963823\ldots}.\tag{5.9}
\]

The lower and upper events are disjoint (`X_D<1` versus `X_D>=1`), so (4.7) and (5.9) add.

## 6. New `D=135` signing constant and `n=86` theorem

Combining (2.1)--(2.2), (4.7), and (5.9), and using the exact rational majorant

\[
\sqrt{10\pi}<\frac{1121}{200},
\]

the exact self-check proves

\[
C_{135}<7.3937676524472495\ldots
<\boxed{\frac{739377}{100000}}.\tag{6.1}
\]

Now let `A` be any real `m x 86` matrix with column norms at most one and put

\[
h=\frac{739377}{100000}.
\]

Call row `r_i` active when

\[
\|r_i\|_2>\frac h{\sqrt{86}}.
\]

Since

\[
\sum_i\|r_i\|_2^2\le86
\]

and exact arithmetic gives

\[
135<\frac{86^2}{h^2}<136,\tag{6.2}
\]

there are at most 135 active rows. Zero-pad the active-row matrix to 135 rows and apply (6.1). Every inactive row satisfies, for every Boolean sign vector,

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\sqrt{86}\le h.
\]

Therefore

\[
\boxed{K_{86}^*\le\frac{739377}{100000}=7.39377}.\tag{6.3}
\]

The exact improvement over the preceding certified anchor is

\[
\frac{739631}{100000}-\frac{739377}{100000}
=\boxed{\frac{127}{50000}}=0.00254.\tag{6.4}
\]

Thus the fixed-metric stagnation count resets to `0`.

## 7. New general branch `L_5(n)`

The argument is not restricted to the single decimal in (6.3). For every integer `D>=135`, retain (5.2)--(5.7). For the lower tail define the exact D-independent constants

\[
p_L=\frac{9878872}{10^7},\quad
p_U=\frac{9878955}{10^7},\quad
m_L=\frac{3376616}{10^7},\quad
m_U=\frac{3378901}{10^7},
\]

\[
\mu_+=\frac{1-m_L}{p_L},\qquad
\mu_-=\frac{1-m_U}{p_U}.\tag{7.1}
\]

Let `v_+` be the rational upper variance certificate obtained from (3.5) by using

\[
q_U=\frac{401132760364}{10^{12}},\quad
b_L=\frac{2639015821545}{10^{12}},\quad
\gamma_L=\frac{4434}{5000},
\]

\[
e_U=\sum_{j=0}^{4}\frac{(-1)^js_0^j}{2^j j!},
\]

\[
M_{2,+}=\frac{(4/5)^2(5/3)(q_U/s_0)e_U}{b_L\gamma_L}
-\frac23+\frac23m_U,
\qquad
v_+=\frac{M_{2,+}}{p_L}-\mu_-^2.\tag{7.2}
\]

Numerically `v_+<0.829788272`, but (7.2), not the decimal, is the definition.

Fix

\[
q_5=\frac{106965}{10^6},\qquad t_5=(1-q_5)^2,
\]

and retain the four exact shell probability lower bounds `p_j` and exact endpoints `v_j=U rho_j^5` from (3.8)--(3.9). For a shell-count vector `c=(c_1,...,c_4)` with `|c|<=2`, put

\[
N_c=D-|c|,
\qquad
x_c(D)=\frac{Dt_5-\sum_j c_jv_j}{N_c}.\tag{7.3}
\]

For `x_c(D)>mu_+`, define

\[
R_D(c)=
\frac{N_c(x_c(D)-\mu_+)^2}
{v_++N_c(x_c(D)-\mu_+)^2};\tag{7.4}
\]

otherwise set `R_D(c)=0`. The disjoint-pattern lower-tail probability certificate is

\[
P_D^{\downarrow}
=
\sum_{\substack{c\in\mathbb Z_{\ge0}^4\\|c|\le2}}
\frac{D!}{(D-|c|)!\prod_jc_j!}
\,p_L^{D-|c|}
\prod_jp_j^{c_j}\,R_D(c),\tag{7.5}
\]

and

\[
\beta_{D,5}^{\downarrow}=\frac{q_5^2}{2}P_D^{\downarrow}.\tag{7.6}
\]

Define

\[
C_D^{(5)}=
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}\right),\tag{7.7}
\]

and the new source-matching row-pruning branch

\[
\boxed{
L_5(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(5)},\frac n{\sqrt{D+1}}\right\}.}\tag{7.8}
\]

The strict active-row inequality `d<n^2/h^2` shows that the second term in (7.8) guarantees `d<=D`. At `n=86`, `D=135`, the rational specialization in the checker gives (6.3).

## 8. Complete retained pointwise envelope

No predecessor certificate is discarded. Put

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The older finite-dimensional branches are retained exactly as follows.

### `G_0`

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\quad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\]

### `H`

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=\max\left\{\frac{148709}{20000},3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

### Retained `p=9/5` three-threshold upper defect and `J`

Let

\[
\Gamma_U=\frac{88869}{100000},
\]

\[
A_{k,D}^{(3)}=
\frac{5}{7\Gamma_U}
\left(\frac{2k}{5}\right)^{7/5}
\left(1-\frac{2k}{5D}\right)D^{-2/5},
\quad a_{k,D}^{(3)}=\frac{A_{k,D}^{(3)}}D,
\quad k=1,2,3.
\]

Set

\[
\begin{aligned}
Q_D^{(3)}(x)=1&-(1-a_3x)^D
-D(a_3-a_1)x(1-a_3x)^{D-1}\\
&-\binom D2[(a_3-a_2)^2+2(a_2-a_1)(a_3-a_2)]
 x^2(1-a_3x)^{D-2},
\end{aligned}
\]

where `a_k=a_{k,D}^{(3)}`. If

\[
Q_D^{(3)}(x)=\sum_{\ell=1}^D c_{\ell,D}^{(3)}x^\ell,
\]

define

\[
\beta_D^{\uparrow,3}=\frac12\sum_{\ell=1}^D c_{\ell,D}^{(3)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right].
\]

Then

\[
D_9(n)=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=\max\left\{\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\]

### `L_-`

With

\[
U=\frac{157}{20},\quad p_0=\frac{24683}{25000},\quad
\mu_0=\frac{662903}{987320},\quad
\Delta_-=\frac{8183}{10000}-\mu_0,
\]

\[
E_D^-=\frac{D\Delta_-^2}{2U\mu_0+(2/3)U\Delta_-},
\quad
R_D^-=1-\left(1+E_D^-+\frac{(E_D^-)^2}{2}+\frac{(E_D^-)^3}{6}\right)^{-1},
\]

\[
\beta_D^{\downarrow,-}=\frac12\left(\frac{477}{5000}\right)^2p_0^DR_D^-,
\]

\[
C_D^-=\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\]

\[
L_-(n)=\inf_{D\in\mathbb Z,D\ge135}\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\}.
\]

### `L_2`

Let

\[
t_2=\frac{987}{1250},\quad q_2=\frac{557}{5000},\quad
v_*=\frac{9691697959}{10^{10}},\quad\Delta_2=t_2-\mu_0,
\]

\[
E_D^{(2)}=\frac{D\Delta_2^2}{2v_*+(2/3)U\Delta_2},
\quad
R_D^{(2)}=1-\left(\sum_{j=0}^8\frac{(E_D^{(2)})^j}{j!}\right)^{-1},
\]

\[
\beta_D^{\downarrow,2}=\frac{q_2^2}{2}p_0^DR_D^{(2)},
\quad
C_D^{(2)}=\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,2}),
\]

\[
L_2(n)=\inf_{D\ge135}\max\left\{C_D^{(2)},\frac n{\sqrt{D+1}}\right\}.
\]

### `L_3`

Let `V=U(12/11)^5`, and let `p_M` be the certified exact middle-band lower bound obtained from the predecessor's alternating incomplete-gamma bounds. Set

\[
q_L=\frac{401132760363}{10^{12}},\quad q_U=\frac{401132760364}{10^{12}},\quad
b_L=\frac{2639015821545}{10^{12}},\quad b_U=\frac{2639015821546}{10^{12}},
\]

\[
\gamma_L=\frac{4434}{5000},\qquad \gamma_U=\frac{4437}{5000},
\]

and

\[
p_M=T_L(1)-T_U(12/11)>0.
\]

For `rho>=1`, with `z=s_0/rho^5`,

\[
T_L(\rho)=\frac{s_0q_L}{\rho^7b_U\gamma_U}
\sum_{k=0}^{5}\frac{(-1)^kz^k}{2^kk!(k+7/5)},
\]

\[
T_U(\rho)=\frac{s_0q_U}{\rho^7b_L\gamma_L}
\sum_{k=0}^{4}\frac{(-1)^kz^k}{2^kk!(k+7/5)},
\]

using `q_L,q_U,b_L,b_U,gamma_L,gamma_U` from Section 3. Put

\[
t_3=\frac{81}{100},\quad x_1(D)=\frac{Dt_3-V}{D-1},
\]

\[
E(N,x)=\frac{N(x-\mu_0)^2}{2v_*+(2/3)U(x-\mu_0)},
\quad
R_8(E)=1-\left(\sum_{j=0}^8\frac{E^j}{j!}\right)^{-1},
\]

with a contribution interpreted as zero whenever `x<=mu_0`. Then

\[
P_{0,D}=p_0^DR_8(E(D,t_3)),
\]

\[
P_{1,D}=Dp_Mp_0^{D-1}R_8(E(D-1,x_1(D))),
\]

\[
\beta_D^{\downarrow,3}=\frac{P_{0,D}+P_{1,D}}{200},
\quad
C_D^{(3)}=\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,3}),
\]

\[
L_3(n)=\inf_{D\ge135}\max\left\{C_D^{(3)},\frac n{\sqrt{D+1}}\right\}.
\]

### `L_4`

Retain the predecessor's sharpened Gautschi low-category mass

\[
p_4=\frac{987887}{10^6},\qquad
\mu_4=\frac{1-337097/10^6}{p_4},
\]

with the same `v_*`, four shell probabilities/endpoints from (3.8)--(3.9), and

\[
q_4=\frac{49}{500},\qquad t_4=(1-q_4)^2.
\]

For a shell-count vector `c` with `|c|<=2`, define `N_c=D-|c|` and

\[
x_c^{(4)}(D)=\frac{Dt_4-\sum_jc_jv_j}{N_c},
\]

\[
E_c^{(4)}=\frac{N_c(x_c^{(4)}-\mu_4)^2}{2v_*+(2/3)U(x_c^{(4)}-\mu_4)},
\]

and set

\[
R_c^{(4)}=
1-\left(\sum_{j=0}^8\frac{(E_c^{(4)})^j}{j!}\right)^{-1}
\]

when `x_c^{(4)}>mu_4`, otherwise zero. Let

\[
P_D^{(4)}=
\sum_{|c|\le2}
\frac{D!}{(D-|c|)!\prod_jc_j!}
\,p_4^{D-|c|}\prod_jp_j^{c_j}R_c^{(4)},
\]

\[
\beta_D^{\downarrow,4}=\frac{q_4^2}{2}P_D^{(4)},
\quad
C_D^{(4)}=\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,4}),
\]

\[
L_4(n)=\inf_{D\ge135}\max\left\{C_D^{(4)},\frac n{\sqrt{D+1}}\right\}.
\]

The **complete current certified pointwise envelope** is therefore

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n)\},&5\le n\le85,\\[1mm]
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n)\},&n\ge86.
\end{cases}}
\tag{8.1}
\]

Every infimum branch above is restricted to integer `D>=135`; zero conventions for failed conditional thresholds are stated explicitly. Equation (8.1) is the fixed metric, not a claim that each branch is optimal or that the displayed finite lower obstructions match it.

## 9. Retained finite lower-obstruction history

No lower obstruction moved this run. The corrected R13 history remains

\[
K_5^*=T_5=1.792447191483282763\ldots,
\]

\[
K_6^*\ge1.84535465,
\qquad
K_{11}^*\ge1.99488049,
\qquad
K_{12}^*\ge2.013108.
\]

In particular, the exact `K_5^*` theorem and the `n=11,12` rational matrices remain preserved; this run is an upper-envelope improvement.

## 10. Verification and literature / novelty status

The finite claim is tested by the exact-arithmetic self-check

`artifacts/R13/20260918T2334Z_cantelli-cascade-c4a7_checker.py`.

Its executed output is archived at

`artifacts/R13/20260918T2334Z_cantelli-cascade-c4a7_checker.out`

and ends

`R13_CANTELLI_CASCADE_EXACT_PASS`.

The checker uses `fractions.Fraction` for every acceptance comparison; the printed decimals are display only. It verifies the Gautschi bracket, incomplete-gamma probability and first-moment bounds, the second-moment recurrence, the shell probabilities, all five upper-tail threshold coefficients, the occupancy DP, every surviving Cantelli shell pattern, the final density inequality, and the exact row-pruning interval `(135,136)`.

This is a **self-check**, not an outside audit. New-claim outside audits remain `0/2`.

Fresh primary-source checks this run confirmed the 10 September 2026 Guo--Fang--Lu Boolean theorem, the 17 September Karingula--Lovett independent proof, the 17 September Akbas--Sra Boolean small-ball paper, and Bansal--Jiang's earlier result. Bounded searches for a Komlós finite-dimensional sharpening combining the `p=9/5` inverse-chi-square density, Cantelli after shell conditioning, and a five-threshold occupancy cascade did not locate a matching paper. That is negative evidence only: **novelty remains UNVERIFIED**.

## 11. What failed / what the new mechanism says to try next

The main gain did **not** come from another decimal retuning of a shell endpoint. The useful structural changes were (i) replacing the generic exponential tail inequality by the extremal second-moment inequality after conditioning, and (ii) turning the upper-tail sufficient mechanisms into an extensible occupancy DP.

The five-threshold DP can in principle be pushed to larger `K`, but doing so one threshold at a time risks becoming exactly the auxiliary-lemma/checker behavior the owner prohibited. The next primary route should instead be one of:

1. a genuinely symmetric nonproduct cube density, to attack the DTV constant before the scalar inverse-gamma tail estimates;
2. a hybrid active-row decomposition that inserts the exact five-column theorem `K_5^*=T_5` into the directional-TV step; or
3. a source-matching extraction from Akbas--Sra with explicit numerical Boolean small-ball constants, but only if their proof exposes constants that actually beat (8.1).

If none moves the fixed metric, the run should count as unchanged rather than manufacture a sixth-threshold checker.

## 12. Model / scheduler-control truth

The task-control interface exposed to this runtime still offers title, prompt, schedule, enablement and timing mode, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. Thus `GPT-6 / maximum` remains prompt text only; it was not truthfully attestable in this run.

Changing that requires an authorized product/backend or workspace control surface that actually exposes model and reasoning selectors plus authenticated run telemetry. The historical P26 `You cannot modify this task` failure is an authorization-context issue; repository history records later successful modification from an authorized P/C context. The legitimate workaround is the owning/authorized task surface or platform support, not duplication or permission bypass. No scheduler, permission, workflow, email, Drive, public posting or purchase action was taken.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R13
  lane: HARD_OUTSIDE
  source_id: E0042
  source_status: KNOWN_RESOLVED_IN_2026_LITERATURE
  quantitative_track_status: PARTIAL
  metric:
    name: B_R13_complete_pointwise_upper_envelope
    anchor_dimension: 86
    before: 739631/100000
    after: 739377/100000
    exact_improvement: 127/50000
    moved: true
  methods_this_run: [24, 3, 19]
  theorem_new:
    K_86_upper: 739377/100000
    new_general_branch: L_5
  retained_lower_history:
    K5_exact: T5
    K6_lower: 1.84535465
    K11_lower: 1.99488049
    K12_lower: 2.013108
  verification:
    checker: artifacts/R13/20260918T2334Z_cantelli-cascade-c4a7_checker.py
    output: artifacts/R13/20260918T2334Z_cantelli-cascade-c4a7_checker.out
    terminal: R13_CANTELLI_CASCADE_EXACT_PASS
    kind: SELF_CHECK
  outside_audits_new_claim: 0/2
  novelty: UNVERIFIED
  stagnation_count: 0
  shared_root_edits: 0
  peer_file_edits: 0
  scheduler_changes: 0
```
