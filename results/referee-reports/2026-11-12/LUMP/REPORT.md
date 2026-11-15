Overall verdict: SOUND

## 1. Theorem 1, the induced chain, and the four-inequality upper bound — SOUND

References: `PAPER.tex:43–104`, `162–175`, `293–299`.

I found no false mathematical statement or missing load-bearing step in the theorem. This verdict concerns the mathematics in the supplied files. Neither Aldous–Fill nor Hermon–Peres is supplied here, and browsing was prohibited. I therefore do not certify the external quotation, theorem numbers, historical priority, or exact statements in those sources. I independently establish the inequalities needed below instead of treating their citations as evidence.

**Definition and conventions.** Write $F_a=f^{-1}(a)$. The definition gives

$$
\widehat w_a=\sum_{x\in F_a}w_x,\qquad \widehat w=w,\qquad
\widehat\pi_a=\sum_{x\in F_a}\pi_x,
$$

and

$$
\widehat\pi_a\widehat p_{ab}
=\sum_{x\in F_a,y\in F_b}\pi_xp_{xy}
=\widehat\pi_b\widehat p_{ba}.
$$

Connectivity descends to the quotient, so it is irreducible. Every reversible chain has the claimed representation by taking $w_{xy}=\pi_xp_{xy}$. Internal edges contribute both orientations to the quotient diagonal; this is exactly what preserves the row weights and the clock. Loops have weight counted once in a row sum. The definition uses stationary one-step flows and requires no strong lumpability of the process $f(X_t)$.

The other introductory contraction claims in lines 73–76 are consistent with these conventions. Maximum commute time contracts by the same resistance comparison used below. A Cheeger variational constant contracts because quotient cuts correspond to fibre-saturated original cuts, preserving both cut stationary flow and the two stationary masses: the optimization is over a restricted family of sets. This argument is unaffected by the usual constant normalization choices for that parameter, although the manuscript does not reproduce Aldous–Fill's precise definition of $\tau_c$.

**Stopping-time formula (68).** I independently derived it from the occupation linear program; the derivation and attaining randomized rule are in the checks section below. It holds in discrete time, including periodic chains, with $T_j=0$ when started at $j$. There is no missing additive one.

The four inequalities in (165) have precisely the stated constants:

1. $t_{\rm mix}\le\tau_0$: draw $J\sim\pi$ independently, reveal it as auxiliary randomness, and stop at $T_J$. Irreducibility makes the mean finite, the terminal law is exactly $\pi$, and the mean is Kemeny's constant $\sum_j\pi_jE_iT_j$. This works even for periodic chains and permits stopping at time zero.
2. $\tau_0(\widehat X)\le\tau_0(X)$: the random-target identity gives $\tau_0=\frac12\sum_{x,y}\pi_x\pi_y C(x,y)$. For these row-weight conventions, $C(x,y)=wR(x,y)$, including loops. Gluing preserves $w$ and decreases resistance. Expand the quotient stationary weights over their fibres to compare the two sums. The factors $1/2$ and $w$ are correct. For example, the deterministic two-state alternator has $w=2$, $R=1$, and commute time 2.
3. $\tau_0(X)\le(m-1)\tau_2(X)$: $\tau_0=\operatorname{tr}(I-P+\Pi)^{-1}-1=\sum_{k=2}^m(1-\lambda_k)^{-1}$. This is the discrete-time identity for the stated zero-time hitting convention. Reversibility orders all eigenvalues in $[-1,1]$; every summand is at most $(1-\lambda_2)^{-1}$. Negative eigenvalues are included, rather than discarded or replaced by their moduli. Periodicity causes no divergence.
4. $\tau_2\le t_{\rm mix}$ is Lemma 2, checked separately below.

Thus the upper bound follows without importing continuous-time mixing constants. A one-state quotient has stopping time zero. The original chain has $t_{\rm mix}\ge\tau_2\ge1/2$, so division is legitimate.

There is also an immediate **stronger upper bound**. If a quotient is a genuine identification and has $q\ge2$ states, then $q\le m-1$ and

$$
t_{\rm mix}(\widehat X)\le\tau_0(\widehat X)
\le(q-1)\tau_2(\widehat X)
\le(q-1)\tau_2(X)
\le(m-2)t_{\rm mix}(X).
$$

The eigentime estimate is being applied to the **quotient** here. A bijective map preserves the chain, and a one-state quotient has zero mixing time. Therefore $K(n)\le\max(1,n-2)$. This does not invalidate the posted $n-1$ bound; it improves it. Together with the four-state family in section 7, it determines $K(4)=2$ exactly.

**Lower bound and small/odd sizes.** The limiting estimate in (297) tends to $N$ for each fixed $N$. The supremum therefore is at least $N$; no finite parameter value attaining $N$ is required. For $n\ge4$, take $N=\lfloor(n-2)/2\rfloor$. If $n$ is odd the comb has $n-1$ states, which is permitted by “at most $n$.” For $n=2,3$, the identity map supplies the lower bound 1; no comb with $N=0$ is needed. In fact the same lemmas imply $K(2)=K(3)=1$: a proper quotient of a three-state chain has at most two states and its stopping mixing time equals its relaxation time. The weaker displayed upper bound at $n=3$ remains true.

**Abstract and historical account.** The bounded-degree claim in lines 29–32 and 83–88 is internally consistent: on a connected graph of uniformly bounded degree, $\pi_*\ge c/n$; contraction of relaxation time and a logarithmic stationary-mass bound give an $O(\log n)$ increase. A lazy total-variation example with a matching lower bound transfers, up to universal constants, to stopping-rule mixing if the standard reversible comparison stated in line 70 is used. This explains the claimed implication from Hermon–Peres; it does not authenticate that their Theorem 3(c) identifies pairs in exactly the stated manner, that Remark 1.8 says exactly this, or that the Aldous–Fill open problem is transcribed verbatim. Those source-text questions remain unverified under the imposed source restriction. No inconsistency in the manuscript's description itself establishes an error.

The “factor of about two” sentence is in the introduction, lines 91–92. Its valid precise meaning is **asymptotic**: the quotient of the displayed upper and nontrivial lower bounds is $2+O(1/n)$. It is not a uniform factor-two estimate at every size: the theorem alone has upper/lower quotient 3 at $n=4$ and 4 at $n=5$. The abstract's hitting-time statement is also justified asymptotically: the singleton-target examples give ratio $N$ against the bound $2N+1$. They do not establish optimality separately for every pair $(n,|A|)$, or determine an optimal leading constant. Read in this asymptotic sense, the abstract does not overclaim the theorems.

## 2. Lemma 2 (relaxation versus stationary stopping), including the equality statements — SOUND

References: `PAPER.tex:111–118`, `146–159`.

An eigenfunction is nonzero, so at a maximum of $|g|$ it can be rescaled, with sign reversed if necessary, to have $g(i)=1$ and $|g|\le1$. Stationarity gives $\pi g=\pi Pg=\lambda\pi g$, hence $\pi g=0$, without reversibility.

The martingale increment is

$$
M_{t+1}-M_t=g(X_{t+1})-\lambda g(X_t).
$$

It has conditional mean zero and absolute value at most $1+|\lambda|\le2$, since a stochastic matrix has spectral radius at most one. If $E_iU=\infty$, the claimed bound is automatic. Otherwise apply optional stopping to $U\wedge t$ and then dominated convergence: $|M_{U\wedge t}|\le1+2U$. This supplies the integrability justification behind the cited optional-stopping step. The terminal condition gives

$$
1=(1-\lambda)E_i\sum_{s<U}g(X_s)\le(1-\lambda)E_iU.
$$

Independent auxiliary randomization, either revealed initially or generated during the rule, preserves the martingale property. The author's “independent of the future” convention must be understood in this usual nonanticipating sense. No strong stationary time, or independence of $U$ and $X_U$, is assumed or needed.

Negative real eigenvalues are covered by the proof. Complex eigenvalues are outside the lemma's explicit scope; an ordered bound $1/(1-\lambda)$ would not make sense for them. Replacing $\lambda$ by $|\lambda|$ would be false: the periodic two-state alternator has $t_{\rm mix}=1/2$ and an eigenvalue of modulus one. The choice of the maximum-absolute-value state is essential to the normalization and argument; the proof makes that choice correctly.

For a two-state chain with off-diagonal probabilities $p,q>0$, both optimal expected stopping times equal $1/(p+q)=\tau_2$. On $K_m$ without loops, $\lambda_2=-1/(m-1)$ and the hitting-time formula gives $t_{\rm mix}=(m-1)/m=\tau_2$. These equalities were also checked exactly.

## 3. Proposition 3 (hitting times of sets), Green identities, and sharpness — SOUND

References: `PAPER.tex:129–136`, `332–357`.

The hypothesis $A=f^{-1}(\widehat A)$ is used correctly: the target is a union of complete fibres. Let $L_A$ be the grounded conductance Laplacian on $I\setminus A$, with diagonal $\sum_{z\ne x}w_{xz}$, and $D=\operatorname{diag}(w_x)$. The killed transition matrix satisfies $I-Q=D^{-1}L_A$. Consequently

$$
G_A=L_A^{-1}D,\qquad G_A(y,y)=w_y(L_A^{-1})_{yy}=w_yR(y\leftrightarrow A).
$$

This proves the loop convention directly: loops cancel from $L_A$ but remain in $D$, so they increase the number of discrete-time visits and the clock. Visits include the visit at time zero and exclude the terminal visit to $A$. Counting visits gives $E_xT_A=\sum_yG_A(x,y)$. The strong Markov property at $T_y$ gives $G_A(x,y)=P_x(T_y<T_A)G_A(y,y)$, including $x=y$.

Equivalently, if $T_y^+=\inf\{t\ge1:X_t=y\}$, the escape probability is $P_y(T_A<T_y^+)=1/[w_yR(y,A)]$. A loop is an immediate return and is handled correctly in the manuscript's explanation.

Wiring $A$ to a grounded terminal and shorting every other fibre adds zero-resistance connections. Rayleigh monotonicity therefore gives $\widehat R(b,\widehat A)\le R(y,A)$ for **each** $y\in F_b$. The source fibre is shorted as well, which is allowed. Thus

$$
\widehat E_a\widehat T_{\widehat A}
\le\sum_{b\notin\widehat A}\widehat w_b\widehat R(b,\widehat A)
\le\sum_{y\notin A}G_A(y,y)
\le\sum_{y\notin A}E_yT_A
\le(n-|A|)\max_yE_yT_A.
$$

Each inequality has the correct direction. The last Green diagonal inequality follows because that diagonal is one nonnegative term in the expected hitting time started at $y$. No initial-distribution comparison between the original and quotient chains is being assumed.

For sharpness, the comb with $A=\{c\}$ has maximum original hitting time at most $h+(N+1)(1+\delta)$ and quotient hitting time at least $Nh\alpha/(1+\alpha)$. Their quotient lower bound tends to $N$ under the displayed scaling. Taking a sufficiently large finite parameter proves the $N-\varepsilon$ assertion. The endpoint loop does not affect either hitting time to $c$, so no heavy-endpoint assumption is missing in this proposition. The examples rule out a universal leading coefficient less than $1/2$ in the bound involving $n-|A|$.

## 4. Remark 4 (the minimum stationary mass) — SOUND

References: `PAPER.tex:178–188`.

The displayed inequality is valid in the paper's discrete-time stopping convention, even without laziness. Its exact attribution to Aldous–Fill Lemma 4.23 could not be authenticated from the supplied files. Here is an independent proof of a stronger bound, which removes any dependence on that attribution or a discrete/continuous-time convention in it.

Let $P_t=e^{t(P-I)}$ be the Poissonized semigroup. The hitting-time Poisson equation, or the spectral inverse of $I-P$ on the mean-zero subspace, gives

$$
E_iT_j-E_\pi T_j=\int_0^\infty\left(1-\frac{P_t(i,j)}{\pi_j}\right)\,dt.
$$

This identity concerns the original discrete-time hitting times; Poissonization is just a way to represent the inverse. Reversibility and the spectral expansion give

$$
\left|P_t(i,j)/\pi_j-1\right|
\le e^{-t/\tau_2}\sqrt{(1/\pi_i-1)(1/\pi_j-1)}
\le \pi_*^{-1}e^{-t/\tau_2}.
$$

The integrand is also at most 1 by nonnegativity of $P_t(i,j)$. Integration of the smaller upper bound proves

$$
t_{\rm mix}\le\tau_2(1+\log(1/\pi_*))
\le2\tau_2(1+\tfrac12\log(1/\pi_*)),
$$

which implies the manuscript's weaker constant $4e/(e-1)$. Periodicity is harmless here because the Poissonized nonconstant modes decay with rates $1-\lambda_k$.

Relaxation contracts because its variational minimum on the quotient is the original Dirichlet quotient restricted to fibre-constant functions. Also $\widehat\pi_*\ge\pi_*$. Combining these facts with Lemma 2 proves exactly the stated quotient-chain bound, including its constant.

For the table's heavy-endpoint parameters, the smallest vertex weight is $w_{z_0}=1$. With $r=1+t^3$,

$$
w=[1+(N+2)t^2]\big[(1+\delta)r^N-\delta\big],\qquad \pi_*=1/w.
$$

Hence $\log(1/\pi_*)=\Theta(N\log t)$ for $N\ge1,t\ge2$, as claimed. The bounded-degree logarithmic comparison is mathematically consistent with the Hermon–Peres description, with the source-verification limitation stated in section 1.

## 5. Lemma 5 (bridge crossing) — SOUND

References: `PAPER.tex:194–202`.

The edge is a bridge, so $S$ is the whole component on the $x$ side and the only edge leaving it is $xy$. Remove everything on the other side except $y$ and remove the loop at $y$. This leaves every transition before hitting $y$ unchanged. The modified degree at $y$ is $w_{xy}$; the total row weight is $w(S)+w_{xy}$. Kac's positive return-time formula then gives

$$
E_yT_y^+=\frac{w(S)+w_{xy}}{w_{xy}}
=1+E_xT_y.
$$

Thus $E_xT_y=w(S)/w_{xy}$. Loops in $S$ remain in $w(S)$ and the proof handles them correctly. Neither aperiodicity nor stationarity of the walk started at $x$ is required.

## 6. Proposition 6 (comb), all three items and intermediate estimates — SOUND

References: `PAPER.tex:205–285`; lower-bound limit and table at `293–317`.

**Weights and prefix sums.** The stated degrees are correct, including $w_{z_N}=r^{N-1}(1+r+\alpha)$ because the edge to $c$ has weight $r^N$. Each tooth has degree $h\alpha r^k$ and exit probability $1/h$. The prefix cut at $z_kz_{k+1}$ contains exactly the listed spine vertices and teeth. Direct summation gives

$$
S_k=1+\frac{1+r+\alpha+h\alpha}{r-1}(r^k-1)
=1+(1+\delta)(r^k-1)\le(1+\delta)r^k.
$$

This includes $k=0$ and $k=N$.

**(i).** The bridge formula gives $E_{z_k}T_{z_{k+1}}=S_k/r^k$ and $E_{y_k}T_{z_{k+1}}=h$. The strong Markov property adds the crossings along the unique path. The two bounds in line 238 hold; $M$ is a slightly larger common bound. No endpoint loop enters these quantities.

**(ii), median step.** The median of three vertices in a tree lies on each connecting path, so both hitting times to $j$ split there. Loops do not change which vertices must be visited. The difference identity in (245) is exact.

For a start at $c$, the reversed bridge crossing is $(w-S_t)/r^t$. Summing it gives

$$
H(c,z_p)\le\frac{r}{r-1}wr^{-p}\le2wr^{-p}.
$$

The per-level estimate in lines 255–257 uses the **first**, sharper bound here. The level-$p$ weight is $r^{p-1}(1+r+\alpha+h\alpha)$, so its contribution is at most

$$
\frac{r^{p-1}(1+r+\alpha+h\alpha)}w
\frac r{r-1}wr^{-p}=1+\delta.
$$

Using only the final factor 2 in (252) would lose this precise estimate, but the manuscript explicitly invokes the geometric-series bound, so there is no gap. There are $N-q$ higher levels. The levels at most $q$ have weight $S_q$ and contribute at most $2(1+\delta)$. For a tooth target, only the target itself adds the downward tooth crossing, with contribution at most $h$. This also handles $j=z_0$ ($q=0$). Thus $d(c,j)\le h+(N-q+2)(1+\delta)\le B$.

For $x,j\ne c$, $c$ is a leaf after ignoring its loop, so their median with $c$ is different from $c$. The path from $c$ to that median includes $cz_N$, whose expected crossing time is exactly $w_c/r^N=\rho$. The path from $x$ to that median is part of the path to $c$. Consequently (270) and $d(x,j)\le M-\rho+B$ hold. The separate cases $j=c$ and $x=c$ are covered by $M\le B$ and $d(c,c)\le0$. This proves the maximum in item (ii), including when $\rho<M$.

**(iii).** Lumping produces the claimed path: both original edges into $z_{k+1}$ contribute to its conductance $(1+\alpha)r^k$. The cut prefix for a forward crossing contains $b_k$, and its degree includes the entire degree $h\alpha r^k$ of the tooth. This proves the lower bound for every crossing and their sum. The far endpoint $b_0$ maximizes hitting time to $c$ on this path, so every difference in (283) is nonnegative; the $a=c$ term alone gives $\pi_c\widehat H(b_0,c)$. The quotient endpoint stationary mass equals $\pi_c$.

**Limit and numbers.** For $t\ge2$, $\delta=(2+t+t^2)/t^3\le1$ and tends to zero. Increasing only the endpoint loop can enforce both $\rho\ge M$ and $\pi_c\ge1-1/t$. Substitution gives exactly (297), tending to $N$. Independent exact computations reproduce every table entry and all 48 comb rows in the author's JSON. Additional parameters with $r=2$, $h=1$, small $\alpha$, fractional parameters, and non-heavy endpoints also satisfy all three items. The table's failure to increase mixing for $N=1$ is acknowledged correctly and does not affect a supremum lower bound of 1.

The actual ratios, rather than only the lower estimates, tend to $N$ under the heavy-endpoint scaling. Indeed $t_{\rm mix}(X)\ge\pi_c\max_xH(x,c)\ge\pi_c h$, while its upper bound is $h+O_N(1)$, so $t_{\rm mix}(X)/h\to1$. The exact quotient endpoint hitting time is

$$
\widehat H(b_0,c)=\sum_{k=0}^{N-1}\frac{h\alpha+S_k/r^k}{1+\alpha}+S_N/r^N
=Nt+O_N(1).
$$

For a path with endpoint $c$, the edge formula for Kemeny's constant is $\tau_0=\sum_e W_e(W-W_e)/(Wc_e)\le\sum_eW_e/c_e=\widehat H(b_0,c)$, with $W_e$ the weight on the side away from $c$. Together with $t_{\rm mix}(\widehat X)\ge\pi_c\widehat H(b_0,c)$, this squeezes the quotient time to $Nt+O_N(1)$ and proves the asserted limiting ratio.

## 7. Remark 7 (four states) — SOUND; substantially stronger examples exist

References: `PAPER.tex:320–329`.

Independent exact computation gives precisely

$$
t_{\rm mix}(X)=149731115/63193903=2.369391790850456\ldots,
$$

$$
t_{\rm mix}(\widehat X)=346900/114917=3.018700453370694\ldots,
$$

and ratio $419679620/329408453=1.2740402262840536\ldots$. The pair $(1,0)$ attains both maxima, with the quotient labelled $0,1,\{2,3\}$. Thus the remark's numerical and strict inequalities are correct.

The independent search found an exactly certified ratio $1.9981383418143137\ldots$, already much larger. Its full rational weight matrix is saved in `referee_search.json`. Studying that candidate yielded the following simpler family, also verified independently:

$$
w_{02}=w_{12}=1,\quad w_{03}=w_{13}=t,\quad
w_{00}=w_{11}=t^2-1,\quad w_{33}=t^6,
$$

with all other weights zero, symmetric off-diagonal weights, $t\ge2$, and the lump $\{2,3\}$. Put $W=t^6+2t^2+4t+2$. Its exact times are

$$
t_{\rm mix}(X)=\frac{(t+1)(t^6+t^5+4t+2)}W,\qquad
t_{\rm mix}(\widehat X)=\frac{2t(t^6+t^2+3t+2)}W.
$$

Here is a proof of the formulas, rather than an inference from the numerical samples. Ground the original Laplacian at 3. Its inverse on $0,1,2$ has

$$
K_{00}=K_{11}=\frac{2t+1}{2t(t+1)},\quad
K_{01}=\frac1{2t(t+1)},\quad K_{02}=K_{12}=\frac1{2t},\quad
K_{22}=\frac{t+1}{2t}.
$$

Extend it with a zero row and column at 3. With degrees $d_0=d_1=t(t+1)$ and $d_2=2$, let $a=Kd$. Then $a_0=a_1=A=t+1+1/t$, $a_2=C=t+2+1/t$, and $a_3=0$. The deviation matrix is

$$
D_{ij}=a_i+a_j-\mu-WK_{ij},\qquad
\mu=\sum_i\pi_i a_i.
$$

Its maximum is $C-\mu$: diagonal entries are nonpositive; $D_{01}\le C-\mu$ follows from $W\ge2(t+1)(t^2+1)$; and $D_{02},D_{12}\le C-\mu$ follow from $W\ge2tA$. Both inequalities hold for $t\ge2$, since their respective differences are $t^6-2t^3+2t\ge0$ and $t^6+2t\ge0$. Pairs with 3 are immediate. In the quotient, the two transient leaves have diagonal grounded inverse $1/(t+1)$ and no connection to one another; the largest deviation is $D_{01}=2t-2t^2(t+1)/W$. Simplifying gives the two formulas above.

Consequently the ratio is

$$
\frac{2t(t^6+t^2+3t+2)}{(t+1)(t^6+t^5+4t+2)}\longrightarrow2.
$$

For $t=10^6$ this is $1.999996000006\ldots$, the best finite ratio found in this audit. Exact rational values and occupation certificates are saved in `referee_four_family.json`. Thus $K(4)\ge2$. The quotient-state-count argument in section 1 gives the matching upper bound: a three-state quotient has $t_{\rm mix}\le\tau_0\le2\tau_2\le2t_{\rm mix}(X)$; quotients of at most two states cannot do better; and a bijective quotient preserves the chain. Hence **$K(4)=2$**. The posted example remains sound, but the manuscript's statement that this value is unknown can now be replaced with the exact value and these proofs.

## Independent checks, programs, and outputs

All referee programs are saved in this folder and import no author routines. I read the author program and compared its saved output against my computations; I did not use it to establish any numerical result. The largest matrices used have 18 states. Computation used one Python worker at a time, with numerical-library thread limits set to one, and no computation ran for five minutes; the longest was the 95-second search. The matrices and exact arithmetic are small, with no large-memory computations. No browsing, other agents, visible windows, or Git pushes were used.

### Derivation and independent certification of the stopping-rule formula

Fix the starting state $i$. For an integrable stationary stopping rule, let $v_x=E_i\sum_{s<U}1_{\{X_s=x\}}$. Flow conservation gives

$$
v(I-P)=e_i-\pi,\qquad v\ge0,\qquad E_iU=\sum_xv_x.
$$

Conversely, every finite nonnegative solution is realized by stopping on each arrival at $x$ with probability $q_x=\pi_x/(v_x+\pi_x)$. Expected arrivals are $v+\pi=e_i+vP$, and $\min_xq_x>0$, so this rule terminates with finite mean and has terminal law $\pi$. This proves that minimizing $\sum_xv_x$ subject to that balance equation is the stationary-stopping LP, including randomization and time-zero stopping.

Set $d_{ij}=H_{ij}-\sum_k\pi_kH_{kj}$. The hitting-time equations give $(I-P)H_{\cdot j}=\mathbf1-e_j/\pi_j$, whence any feasible occupation vector satisfies

$$
d_{ij}=\sum_xv_x-v_j/\pi_j.
$$

All solutions of the flow equation differ by a multiple of $\pi$, since the chain is irreducible. Shifting a feasible vector until $\min_jv_j/\pi_j=0$ therefore attains the minimum, equal to $\max_jd_{ij}$. This derives (68) and attainment. For every exact chain computed, the program explicitly constructs

$$
v_j=\pi_j\big(\max_kd_{ik}-d_{ij}\big)
$$

for each start, verifies the balance equation exactly, and verifies $v\ge0$, $\min v=0$, and the objective. These are primal certificates and matching hitting-potential lower bounds, not just evaluations of a quoted formula.

For the exact hitting computation, `referee_core.py` inverts one grounded conductance Laplacian and uses

$$
H_{ij}=(Kd)_i-(Kd)_j-W(K_{ij}-K_{jj}),
$$

where the root row and column of $K$ are extended by zero. This differs from the author's separate killed-chain solves. Separately, SciPy's LP solver checks the occupation minimization directly on the random chains.

### Reproducible results

Programs can be run separately from this directory with `python3 PROGRAM.py`; they write their own JSON files. For the numerical programs, use the single-thread environment shown in the run commands below. The environment had NumPy 2.2.3 and SciPy 1.15.2.

| Program | Output | Result |
| --- | --- | --- |
| `referee_core.py` | Imported by the other programs | Exact grounded inverse, hitting times, quotient weights, and occupation-flow certificates. |
| `referee_exact.py` | `referee_exact.json`, `referee_exact.log` | All exact certificates passed; all four table rows reproduced; additional limiting and fractional-parameter comb checks passed; complete-graph and two-state equalities passed. |
| `referee_random.py` | `referee_random.json`, `referee_random.log` | Seed 9812026: 225 reversible chains, 45 at each size 2–6; 900 separate LP solves; 675 eigenfunction bounds; all eigentime and relaxation comparisons passed; 4,560 hitting comparisons and 10,560 harmonic/Green identities passed. |
| `referee_details.py` | `referee_details.json`, `referee_details.log` | Seed 424211: 60 additional combs; 3,484 median estimates; 677 per-level estimates; 836 bridge identities and the prefix identities; all 48 author-output comb rows independently reproduced. |
| `referee_search.py` | `referee_search.json`, `referee_search.log` | Seed 579831: 6,000 random starts; 1,242 completed local searches; 1,824,463 objective evaluations in 95 seconds. Best rationalized candidate had exact ratio 1.9981383418143137. No optimality claim. |
| `referee_four_family.py` | `referee_four_family.json`, `referee_four_family.log` | Exact formulas and occupation certificates passed at $t=2,4,16,64,256,4096,10^6$; ratios tend to 2; best finite ratio 1.999996000006. |

Representative independent comb results:

| $N$ | $t$ | $t_{\rm mix}(X)$ | $t_{\rm mix}(\widehat X)$ | Mixing ratio | Hitting ratio |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 256 | 257.003911455 | 256.011693576 | 0.996139289 | 0.996139289 |
| 2 | 4 | 6.649693075 | 8.179941600 | 1.230123181 | 1.228853783 |
| 2 | 16 | 18.131817165 | 31.304213948 | 1.726479683 | 1.726398755 |
| 2 | 256 | 258.007835626 | 511.019493475 | 1.980635558 | 1.980635529 |
| 2 | 4096 | 4098.00048837 | 8191.00122055 | 1.998779952 | 1.998779952 |
| 4 | 4 | 9.347887340 | 15.127860842 | 1.618318695 | 1.616811713 |
| 4 | 16 | 20.266257659 | 61.548013836 | 3.036969867 | 3.036837255 |
| 4 | 256 | 260.015681425 | 1021.035090734 | 3.926821202 | 3.926821145 |
| 4 | 4096 | 4100.00097678 | 16381.0021970 | 3.995365438 | 3.995365438 |
| 8 | 256 | 264.031369972 | 2041.066282206 | 7.730393106 | 7.730393028 |

The random hitting comparisons verified the stronger intermediate trace bound, and resistance contraction for every vertex outside every tested saturated target. The largest random hitting increase was 1.0326215686273679. Moderate random weights rarely produce the extreme comb phenomenon; this statistic is not an extremal bound.

The details program also checks a nonreversible chain with clockwise probability $3/4$ and anticlockwise probability $1/4$ on a four-cycle. Its eigenvalues include $-1$ and $\pm i/2$; the real $-1$ mode satisfies the lemma, and the exact optimal expected stopping time from every state is $13/10$.

The search fixed the merged pair at $\{2,3\}$ while varying the symmetric weight matrix, using both full and sparse supports and Powell/Nelder–Mead local searches. Relabelling makes this representative of all pair identifications. Other proper four-state quotients have at most two states and cannot have ratio above 1, by Lemma 2, two-state equality, and relaxation contraction. Thus concentrating the numerical search on pair identifications loses no possible improving quotient. The floating objective used a fundamental-matrix inverse; final candidates were rationalized and recalculated by the separate exact grounded-inverse method. The search's floating estimate 1.9981383983 differed slightly from its certified value, so only the latter is reported as evidence.

Example run command, with the program name changed for each computation:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  PYTHONDONTWRITEBYTECODE=1 python3 referee_random.py > referee_random.log 2>&1
```

Numerical tests support the audit but do not replace the arguments in the result sections above.

## Corrections and clarifications

There are **no required mathematical corrections** to the numbered results or their displayed constants.

1. **`PAPER.tex:91–92`, also abstract lines 37–38:** resolve the possible finite-size reading of “about two.” Say “within a factor $2+o(1)$ as the number of states tends to infinity”; for hitting times, specify that singleton-target examples establish the asymptotic obstruction. A uniform factor-two claim, or sharpness for each $(n,|A|)$, would exceed the results proved.
2. **`PAPER.tex:360–362`:** replace the ambiguous parameter-range description with the actual sampled grid: $N\in\{1,2,3,4,6,8\}$ and $t\in\{4,16,64,256\}$, with both endpoint regimes. The program checks these 48 combs, rather than every parameter choice satisfying $N\le8$ and $t\le256$.
3. **`PAPER.tex:102`, `163–175` — mathematical strengthening:** applying the eigentime bound to the quotient gives $K(n)\le\max(1,n-2)$, as proved in section 1. The published weaker upper bound is correct.
4. **`PAPER.tex:141–142`, `320–329` — resolved small-state value:** the new four-state family above gives an explicit ratio 1.999996000006 at $t=10^6$ and proves $K(4)\ge2$. Together with the preceding upper bound it proves $K(4)=2$. Replace the assertion that this value is unknown if incorporating these additional results. The published 1.27 example itself requires no correction.
5. **`PAPER.tex:55`, `66`, `70–88`, `106–109`, `169–184`; `bib_main.tex`:** the supplied material does not permit authentication of exact external theorem numbers, quotations, or priority claims. No citation correction is established by this audit. A source-text audit would need the cited passages locally; the mathematical inequalities needed for the main results have been independently checked above.

Task: “Be a hard, independent referee” — 12 November 2026, approximately 20:16 +04 at run start.
