Result: no improvement

For the five-state question, the rigorous conclusion remains

\[
2\le K(5)\le3.
\]

I have not proved either $K(5)=3$ or a sharper upper bound. My conjecture is $K(5)=2$. The searches below support this conjecture but do not prove it.

There is a separate improvement for larger state counts: the construction in Section 5 proves

\[
\boxed{K(n)\ge\lfloor n/2\rfloor\quad(n\ge2).}
\]

In particular, six states suffice for a ratio tending to 3. This improves the supplied comb lower bound by one, but does not improve the supplied information about $K(5)$, since $K(4)=2$ already implies $K(5)\ge2$. “No improvement” in the first line refers to the requested five-state decision.

## 1. Exact calculation and stopping-rule certificates

Write $d_i=\sum_jw_{ij}$, $W=\sum_i d_i$, and $\pi_i=d_i/W$. The conductance Laplacian has diagonal $\sum_{j\ne i}w_{ij}$ and off-diagonal $-w_{ij}$. Thus loops affect $d$ and the clock, but cancel from the Laplacian.

Fix a root $c$, invert the Laplacian with row and column $c$ removed, and extend that inverse by a zero row and column. Call the resulting matrix $K$. Define

\[
a=Kd,\qquad \mu=\sum_i\pi_i a_i.
\]

Then

\[
a_i=H(i,c),\qquad
H(i,j)=a_i-a_j-W(K_{ij}-K_{jj}),
\tag{1}
\]

and the centered hitting-time matrix is

\[
F_{ij}:=H(i,j)-\sum_k\pi_kH(k,j)
=a_i+a_j-\mu-WK_{ij}.
\tag{2}
\]

Consequently $F$ is symmetric and $t_{\rm mix}=\max_{i,j}F_{ij}$. In particular $F_{ii}\le0$.

For completeness, the Poisson equation for $a$ is $La=d-We_c$. The extended inverse satisfies $LK_{\cdot j}=e_j-e_c$. The expression in (1) therefore has Laplacian $d-We_j$ and value zero at $j$, which characterizes the hitting-time solution. Symmetry of $K$ gives $\sum_k\pi_k K_{kj}=a_j/W$, and averaging (1) proves (2).

The calculations also certify optimal stopping, rather than just evaluating a matrix expression. For each start $i$, put $t_i=\max_jF_{ij}$ and

\[
v_j=\pi_j(t_i-F_{ij}).
\]

The program checks, with fractions, that

\[
v\ge0,\quad\min_jv_j=0,\quad
v(I-P)=e_i-\pi,\quad\sum_jv_j=t_i.
\]

These are optimal occupation certificates. Indeed, any feasible occupation vector satisfies $F_{ij}=\sum_xv_x-v_j/\pi_j$, so its objective is at least $\max_jF_{ij}$. Conversely, a feasible finite $v$ is realized by stopping on arrival at $j$ with probability $\pi_j/(v_j+\pi_j)$. The balance equation gives expected arrivals $v+\pi$; all stopping probabilities are positive, so the resulting rule is integrable and ends in stationarity.

Every exact example in this report was additionally checked by solving the killed hitting system separately for every target, independently of the single-grounded-inverse formula.

## 2. Why the four-state family works

Use the supplied weights, calling states 2 and 3 respectively $u$ and $v$. The two other states are leaves. Set

\[
W=t^6+2(t+1)^2,\quad
A=t+1+t^{-1},\quad C=t+2+t^{-1},
\]

\[
\mu=\frac{2\{t(t+1)A+C\}}W.
\]

Grounding at $v$, the values of $a$ are $A,A,C,0$. The largest entries of $F$, for every $t\ge2$, are exactly

\[
F_{uv}=F_{vu}=C-\mu
=\frac{(t+1)(t^6+t^5+4t+2)}W.
\tag{3}
\]

Thus an extremal optimal stopping rule starts at the light hub $u$, with $v$ its maximizing target in the Lovász–Winkler formula, or starts at the heavy state $v$, with $u$ its maximizing target. Both ordered pairs attain the maximum because $F$ is symmetric. The leaf starts have smaller optimal mean. A maximizing target here is a halting state of an optimal rule: its pre-stop occupation is zero. It need not be the sole terminal state of the rule.

After merging $u,v$ into $c$, both leaves have degree $t(t+1)$ and edge weight $t+1$ to $c$. The grounded inverse is diagonal with entries $1/(t+1)$. Put $\widehat\mu=2t^2(t+1)/W$. Then

\[
t_{\rm mix}(\widehat X)=F^{\widehat X}_{01}
=F^{\widehat X}_{10}=2t-\widehat\mu
=\frac{2t(t^6+t^2+3t+2)}W.
\tag{4}
\]

The worst start is either leaf and the hard target is the other leaf. Starting at the merged heavy state is not worst. Although its stationary mass tends to one, exact stationarity still requires the correct small masses at both leaves. Those small masses have a nonvanishing cost in the mean stopping time.

Here is the asymptotic behavior of **every** factor in the upper-bound chain. The two nonzero eigenvalues of $I-\widehat P$ are

\[
\widehat\gamma_2=1/t,\qquad
\widehat\gamma_3=1/t+\frac{2(t+1)}{t^6+2(t+1)}.
\]

Thus $\tau_2(\widehat X)=t$ and

\[
\tau_0(\widehat X)=2t-\widehat\mu=t_{\rm mix}(\widehat X).
\]

The random-target stopping rule actually attains the optimum from a leaf in this three-state quotient. For the original chain one nonzero gap is $1/t$. The other two are the roots of

\[
\gamma^2-S\gamma+Q=0,
\]

\[
\rho=\frac2{t^5+2},\quad
S=1+t^{-1}+\rho,\quad
Q=\frac1{t+1}+\rho\left(1+\frac1{t(t+1)}\right).
\tag{5}
\]

The smaller root is asymptotic to $1/t$, while the larger root tends to 1. Therefore

\[
\frac{t_{\rm mix}(\widehat X)}{\tau_0(\widehat X)}=1,\quad
\frac{\tau_0(\widehat X)}{2\tau_2(\widehat X)}\to1,\quad
\frac{\tau_2(\widehat X)}{\tau_2(X)}\to1,\quad
\frac{\tau_2(X)}{t_{\rm mix}(X)}\to1.
\]

This explains the factor 2. The original has two slow modes and a fast mode; the quotient retains two almost equal slow gaps. The heavy stationary mass and vanishing leaf masses are essential to making its mixing time as large as the sum of its relaxation modes.

## 3. What a ratio $n-2$ would force

Fix $n\ge4$. Along any sequence of examples with ratio tending to $n-2$, eventually the examples must use exactly $n$ states and the quotients exactly $n-1$ states. Otherwise the supplied state-count bound leaves a fixed gap. Thus the map must merge exactly one pair.

All four nonnegative factors in

\[
\frac{t_{\rm mix}(\widehat X)}{(n-2)t_{\rm mix}(X)}
=\frac{t_{\rm mix}(\widehat X)}{\tau_0(\widehat X)}
\frac{\tau_0(\widehat X)}{(n-2)\tau_2(\widehat X)}
\frac{\tau_2(\widehat X)}{\tau_2(X)}
\frac{\tau_2(X)}{t_{\rm mix}(X)}
\]

are at most one, so each must tend to one. In particular all quotient nonzero gaps must become equal **relatively**:

\[
\frac{1-\widehat\lambda_k}{1-\widehat\lambda_2}\longrightarrow1
\quad(2\le k\le n-1).
\tag{6}
\]

It is not enough that the eigenvalues themselves merely approach 1. The Rayleigh quotient on fibre-constant functions must approximate the original minimum; a lifted quotient slow eigenfunction is then an approximate minimizing vector for the original relaxation problem. Finally the original optimal stopping time must nearly attain its eigenfunction lower bound. With a slow eigenfunction normalized by $g(i)=1=\max|g|$, that martingale proof gives the precise occupation deficit

\[
E_i\sum_{s<U}(1-g(X_s))=E_iU-\tau_2(X).
\]

For a minimizing rule from this $i$, the right side must be $o(t_{\rm mix}(X))$.

There is another necessary singularity: the quotient minimum stationary mass must tend to zero. Here is a proof. For a reversible $q$-state chain with all nonzero gaps exactly equal to $\gamma$, the transition matrix is $P=(1-\gamma)I+\gamma\Pi$. Its centered Green kernel gives $F_{ij}=\gamma^{-1}$ for distinct states and $F_{ii}=-\gamma^{-1}(1/\pi_i-1)$, so $t_{\rm mix}=\tau_2$, not $(q-1)\tau_2$. More generally, under (6), the Green operator divided by $\tau_2$ converges in $L^2(\pi)$ operator norm to the identity on mean-zero functions. If $\pi_*\ge\varepsilon>0$, the error in each normalized kernel entry is at most the operator error divided by $\varepsilon$. Thus $t_{\rm mix}/\tau_2\to1$. For $q\ge3$, this contradicts the required limit $q-1$. If the minimum masses failed to tend to zero, a subsequence bounded below would give that contradiction.

These are necessary conditions, not a proof that they can or cannot hold simultaneously for five states.

## 4. The suggested equal-leaf generalization: exact formulas

Take $m=n-2\ge2$ leaves $0,\ldots,m-1$, a light hub $u=m$, and a heavy state $v=m+1$. Use

\[
w_{iu}=1,\quad w_{iv}=t,\quad w_{ii}=t^2-1,
\quad w_{vv}=t^6,
\]

and no other edges or loops. Merge $u,v$. This is the supplied four-state family when $m=2$.

The following formulas hold whenever $t\ge2$ and

\[
t^6\ge mt(t^2-1).
\tag{7}
\]

In particular they hold for every tested $m=2,3,4,5$, $t\ge2$. Set $W=t^6+m(t+1)^2$. Then

\[
\boxed{t_{\rm mix}(X)=
\frac{(t+1)\{t^5(t+1)+m(2t+1)\}}W,}
\tag{8}
\]

\[
\boxed{t_{\rm mix}(\widehat X)=
\frac{t\{2t^6+m(t+1)(t+2)\}}W.}
\tag{9}
\]

**Proof.** Ground at $v$. On the leaves and $u$, the inverse entries are

\[
K_{ij}=\frac{\mathbf1_{i=j}}{t+1}+\frac1{mt(t+1)},\quad
K_{iu}=\frac1{mt},\quad K_{uu}=\frac{t+1}{mt}.
\]

Multiplying by the grounded Laplacian checks this inverse directly. Since $d_i=t(t+1)$, $d_u=m$, the values of $a$ are $A=t+1+1/t$ at a leaf, $C=t+2+1/t$ at $u$, and zero at $v$. Hence $\mu=m\{t(t+1)A+C\}/W$. Pairs involving $v$ have maximum $C-\mu$. For two distinct leaves, the condition $F_{ij}\le C-\mu$ is precisely

\[
W\ge m(t+1)(t^2+1),
\]

which is (7). For a leaf and $u$, the needed inequality is $W\ge mtA$, whose difference is $t^6+mt>0$. Diagonal entries are nonpositive. This proves $t_{\rm mix}(X)=C-\mu$, and simplifying yields (8). The only maximizing original pairs under strict (7) are $(u,v),(v,u)$.

In the quotient the grounded inverse on the leaves is $I/(t+1)$. Its hitting potentials are all $t$, and $\widehat\mu=mt^2(t+1)/W$. Distinct leaves give $F_{ij}=2t-\widehat\mu$, larger than a pair involving the root or a diagonal entry. This proves (9). ∎

The ratio tends to **2 for every fixed $m$**. The failure is precisely the first inequality in the upper-bound chain:

\[
\tau_2(\widehat X)=t,\quad
\tau_0(\widehat X)=mt-\widehat\mu,\quad
\frac{t_{\rm mix}(\widehat X)}{\tau_0(\widehat X)}\to\frac2m.
\]

The quotient has $m-1$ gaps $1/t$ and one gap

\[
1/t+\frac{m(t+1)}{t^6+m(t+1)}.
\]

The original has $m-1$ gaps $1/t$ and the two gaps in (5), with $\rho=m/(t^5+m)$. Thus all three other factors still tend to one. The inverse/eigenvalue formulas follow by separating leaf differences from the three-dimensional subspace constant on the leaves; its generator is

\[
\begin{pmatrix}
1/t&-1/[t(t+1)]&-1/(t+1)\\
-1&1&0\\
-\rho&0&\rho
\end{pmatrix}.
\]

Exact computations from `exact_core.py`, saved in `leaf_exact.json` and `leaf_exact.txt`, give:

| states | $t=10$ | $t=100$ | $t=1000$ | $t=10^6$ |
|---:|---:|---:|---:|---:|
| 5 | 1.653125155725 | 1.960592127940 | 1.996005992013 | 1.999996000006 |
| 6 | 1.653202681051 | 1.960592137649 | 1.996005992014 | 1.999996000006 |
| 7 | 1.653280203419 | 1.960592147358 | 1.996005992015 | 1.999996000006 |

`family_analysis.py` verifies the rational formulas and computes the four upper-bound factors at high precision. Its outputs are `family_analysis.txt` and `family_spectral.json`. `audit_results.py` independently checks the spectral formulas against full normalized-Laplacian eigensystems at 80-digit precision.

The largest exactly checked five-state ratio from this family was at $t=10^6$. Its weights are the integer matrix specified above, namely three loops $10^{12}-1$, three light-hub edges 1, three heavy-state edges $10^6$, and the heavy loop $10^{36}$. Merge $\{3,4\}$. The exact times are

\[
t_{\rm mix}(X)=
\frac{1000002000001000000000000000006000009000003}
{1000000000000000000000003000006000003},
\]

\[
t_{\rm mix}(\widehat X)=
\frac{2000000000000000000000003000009000006000000}
{1000000000000000000000003000006000003}.
\]

Their ratio is the quotient of those two numerators, approximately $1.999996000006$. This is a finite certified example, not a claim of optimality among finite examples.

## 5. A stronger general lower bound: a comb with two end leaves

**Theorem.** For every $n\ge2$, $K(n)\ge\lfloor n/2\rfloor$.

**Construction and proof.** Fix an integer $N\ge0$. There are $2N+4$ states:

\[
a,b,c,\ z_0,\ldots,z_N,\ y_0,\ldots,y_{N-1}.
\]

For an integer $t\ge2$, put $r=t^3$, $\alpha=t$, and use the tree edges

\[
w_{az_0}=1,\quad
w_{z_kz_{k+1}}=r^{k+1},\quad
w_{y_kz_{k+1}}=\alpha r^{k+1}\quad(0\le k<N),
\]

\[
w_{bz_N}=\alpha r^{N+1},\qquad
w_{cz_N}=r^{N+2}.
\]

The loops are $t-1$ at $a$, $(t-1)\alpha r^{k+1}$ at $y_k$, $(t-1)\alpha r^{N+1}$ at $b$, and

\[
L=(N+2)r^{N+4}
\]

at $c$. All unspecified weights vanish. Merge each pair $\{z_k,y_k\}$, $k<N$, and merge $\{z_N,c\}$. Keep $a,b$ separate. The quotient has $N+3$ states. Its graph is a path from $a$ through the $N$ tooth fibres to the heavy root, with $b$ as another leaf at that root. For $N=0$, the original is a four-state star and the quotient is a three-state star.

Here are exact formulas, including the terms discarded in the limit. Let

\[
G_k=\sum_{\ell=1}^k r^\ell,\qquad B=2+\alpha(t+1),
\]

\[
S_k=t+1+r^{k+1}+BG_k\quad(0\le k<N),
\]

\[
S_N=t+1+r^{N+2}+BG_N+(t+1)\alpha r^{N+1},
\quad W=L+r^{N+2}+S_N.
\]

For $k<N$, $S_k$ is the row weight on the side of $a$ at the spine edge $z_kz_{k+1}$; $S_N$ is the entire row weight away from $c$. These formulas follow by counting internal edges twice, boundary edges once, and loops once.

Define

\[
M=t+\sum_{k=0}^{N-1}\frac{S_k}{r^{k+1}}+
\frac{S_N}{r^{N+2}},\quad
Q_k=S_k+t\alpha r^{k+1},
\]

\[
A=t+\sum_{k=0}^{N-1}\frac{Q_k}{(1+\alpha)r^{k+1}}.
\]

Empty sums are zero. The bridge-crossing identity $H(x,y)=S/w_{xy}$ gives $M=H(a,c)=\max_xH(x,c)$. To verify that identity directly, sum the hitting-time Poisson equations over the component on the side of $x$: all internal Laplacian terms cancel, leaving $w_{xy}H(x,y)=S$. Each holding leaf costs exactly $t$ to exit; starting at a tooth or $b$ skips some of the nonnegative spine crossings that appear after the initial $t$ in $M$. In the quotient, $A=H(a,\widehat c)$, since the prefix weight at the $k$-th edge is $Q_k$. Also $H(b,\widehat c)=t$.

Put

\[
\mu=\frac1W\left[
t^2(1+\alpha G_{N+1})+
\sum_{k=0}^{N-1}\frac{S_k^2}{r^{k+1}}+
\frac{S_N^2}{r^{N+2}}\right],
\]

\[
\widehat\mu=\frac1W\left[
t^2(1+\alpha r^{N+1})+
\sum_{k=0}^{N-1}\frac{Q_k^2}{(1+\alpha)r^{k+1}}\right].
\]

These are exactly $E_\pi H(X,c)$ and $E_{\widehat\pi}H(\widehat X,\widehat c)$. Indeed, on a rooted tree with away-side weights $S_e$ and conductances $c_e$, summing the bridge formula over the starting distribution gives $W^{-1}\sum_e S_e^2/c_e$.

For all sufficiently large $t$, the exact mixing times are

\[
\boxed{t_{\rm mix}(X)=M-\mu,\qquad
t_{\rm mix}(\widehat X)=A+t-\widehat\mu.}
\tag{10}
\]

To prove the first assertion, the grounded inverse of a tree satisfies $K_{ij}=\sum_{e\in[c,i]\cap[c,j]}1/c_e$: the unit current to the root uses the unique path, and its voltage at $i$ is the resistance on the common path. All nonroot vertices share the last edge $cz_N$. Thus $K_{ij}\ge r^{-(N+2)}$ for $i,j\ne c$. If $W/r^{N+2}\ge M$, equation (2) bounds their entries by $2M-\mu-W/r^{N+2}\le M-\mu$; pairs with $c$ attain $M-\mu$.

For the quotient, the left arm has maximum root hitting time $A$, achieved at $a$, and $b$ has root hitting time $t$. The paths from $a$ and $b$ meet only at the root, so $F_{ab}=A+t-\widehat\mu$. All other cross-arm pairs are smaller, and pairs with the root are smaller. If $N\ge1$, two nonroot vertices on the left arm have common-path resistance at least $1/[(1+\alpha)r^N]$. Their entries are at most $2A-\widehat\mu-W/[(1+\alpha)r^N]\le A+t-\widehat\mu$ whenever $W/[(1+\alpha)r^N]\ge A-t$. For $N=0$ there is only one left-arm vertex. This proves (10) under two explicit sufficient inequalities, both eventually satisfied by the stated $L$.

Finally, for fixed $N$,

\[
S_k/r^{k+1}=1+O_N(t^{-1}),\quad
S_N/r^{N+2}=1+O_N(t^{-1}),
\]

so $M=t+N+1+O_N(t^{-1})$. Also

\[
A=t+\frac{Nt\alpha}{1+\alpha}+O_N(t^{-1}),
\quad A/t\to N+1.
\]

The original stationary mass at $c$ tends to one: $S_N=O_N(r^{N+2})$ whereas $L=(N+2)r^{N+4}$. Hence $\mu\le(S_N/W)M=o(t)$; likewise $\widehat\mu=o(t)$. The two sufficient inequalities above hold because $W/r^{N+2}$ grows like $(N+2)r^2$, and the other ratio grows faster still. Equation (10) now gives

\[
\frac{t_{\rm mix}(\widehat X)}{t_{\rm mix}(X)}\longrightarrow N+2.
\]

Thus $K(2N+4)\ge N+2$. For $n\ge4$, take $N=\lfloor n/2\rfloor-2$; the construction uses at most $n$ states. The identity map proves the assertion for $n=2,3$. ∎

For this construction the limiting ratio is also the quotient-state upper bound $q-1=N+2$. Therefore every factor in that upper-bound chain tends to one. It uses $N+1$ pair merges, rather than the one pair merge that a ratio $n-2$ would require.

`fork_comb.py` checks (10) by both exact hitting methods, including the maximizing pairs and the two sufficient inequalities, for $N=0,1,2,3$ and $t=2,10,100,1000$. Outputs: `fork_comb_exact.txt`, `fork_comb_exact.json`.

| original states | limiting ratio | ratio at $t=100$ | ratio at $t=1000$ |
|---:|---:|---:|---:|
| 4 | 2 | 1.980000019798 | 1.998000000002 |
| 6 | 3 | 2.931273539502 | 2.993012973055 |
| 8 | 4 | 3.863701555418 | 3.986037899261 |
| 10 | 5 | 4.778022414536 | 4.977082713970 |

For $n=7$, the six-state construction is admissible under “at most $n$.” It proves $K(6),K(7)\ge3$. The equal-leaf calculations in Section 4 also explicitly test seven-state chains, but their limit is 2.

## 6. Numerical search on five states

All 15 upper-triangular weights, including the five loops, were varied in logarithmic coordinates. The numerical routine computes (2), grounding at a state of largest degree. Final candidates were rounded to eight significant decimal digits and recomputed with `Fraction`; candidates with a numerical/exact disagreement over the stated tolerances were not accepted.

`search5.py` used seed 20261112. It evaluated every one of the ten pair merges on 4,000 random log-weight matrices, with additional structured seeds. It then ran 22 Powell restarts, including a separate start for every pair; log weights were bounded by $[-14,14]$. There were 23,411 objective evaluations, taking 2.181 seconds. The recorded selected-pair best was 1.93600858269608. An exact final scan of all ten merges of those weights improved this to 1.94267593389616.

`search5_de.py` ran eight differential-evolution restarts, each with a population of 120, at most 350 generations, followed by up to 8,000 Nelder–Mead evaluations. It used $[-16,16]$ log bounds and independent seeds 47311 through 47318. These further restarts optimized the fixed pair $\{3,4\}$; permutation symmetry makes that the same unrestricted chain search problem, although the actual all-pair scans were still performed on final weights. There were 382,978 evaluations in 24.928 seconds. The selected-pair best was 1.99727558558727. Its best merge on exact rechecking is $\{0,3\}$, giving

\[
\boxed{1.99797073453948\ldots.}
\]

This is the best result from the unrestricted numerical searches, below the explicit family value 1.999996000006 in Section 4. Neither numerical search found a ratio above 2. They are bounded searches, not exclusion proofs.

The best numerical matrix is below. **All displayed finite decimals are exact rational weights**, with symmetric entries understood:

```
0.00000013165805  0.30363847       0.00016866869     2083.8825       7453977.5
0.30363847        8748.5053        0.00000011695011  2.2180308       6.5372821
0.00016866869     0.00000011695011 923.11784         0.92295775      0.033783624
2083.8825         2.2180308        0.92295775        0.000053201397  1559.4588
7453977.5         6.5372821        0.033783624       1559.4588       0.027539305
```

For this matrix and the merge $\{0,3\}$, exact recomputation gives

\[
t_{\rm mix}(X)=
\frac{4249000186329564173766769403142889733050283225240356747559961569319458730005197}
{4394555694933011578487367418989313947530237759379647391875947524595004373250}
=966.87821961813449\ldots,
\]

\[
t_{\rm mix}(\widehat X)=
\frac{6211266746778803051279835813568724132572930979305556443673662495673}
{3215283567272246888948691621390873897652164259629059569964114440}
=1931.79438666066426\ldots.
\]

The original maximizing pairs are $(0,1),(1,0)$. Quotient labels for this audited merge are $\{0,3\},1,2,4$; its maximizing pairs are the singleton states $(1,2),(2,1)$. The complete audited weights, merge, times, ratio, and maximizing pairs are saved together in `audited_search5_best.json` and reproduced by `audit_results.py`. The original search weights and its selected merge are in `search5_de_best.json`; the all-pair checks are in `audit_results.json`. The logs retain the distinction between the selected merge and the stronger merge found in the final audit.

Search files: `search5_output.txt`, `search5_results.json`, `search5_best.json`, `search5_de_output.txt`, `search5_de_results.json`, `search5_de_best.json`.

## 7. Attempt at a sharper upper bound: an exact rank-one identity

The following identity narrows where an obstruction would have to occur, but I did not extract a universal factor below 3 from it.

**Lemma.** Let $u,v$ be the pair being merged. Write

\[
h_i=P_i(T_u<T_v),\quad h_u=1,\ h_v=0,
\quad p=\sum_i\pi_i h_i,
\]

and let $R$ be the effective resistance between $u,v$. If quotient entries are lifted to the original states, then

\[
\boxed{\widehat F_{f(i)f(j)}
=F_{ij}+WR(h_i-p)(h_j-p).}
\tag{11}
\]

In particular, for every starting fibre $a$,

\[
\widehat F_{a,f(u)}\le t_{\rm mix}(X).
\tag{12}
\]

**Proof.** Ground at $v$. Then $K_{uu}=R$ and $K_{iu}=Rh_i$, by the equilibrium-potential equation. The inverse with both $u,v$ grounded, extended by zeros at the pair, is

\[
B=K-Rhh^{\mathsf T}.
\]

This follows either by a block inverse or by subtracting the harmonic extension from each column. The same $B$ is the grounded inverse of the quotient at the merged state: its remaining Laplacian is precisely the original Laplacian with $u,v$ removed. Centering $K$ with respect to $\pi$ in (2), and doing the same for $B$, proves (11); the rank-one term centers to $R(h-p\mathbf1)(h-p\mathbf1)^{\mathsf T}$. Summing original masses within each fibre preserves this centering. For (12), choose the representative $u$ or $v$ whose $h-p$ has sign opposite to $h_i-p$. The correction in (11) is then nonpositive. ∎

Thus an increasing maximum must use **two unmerged states**, with $h_i-p$ and $h_j-p$ of the same sign. A target in the merged fibre cannot cause the increase. This matches the four-state family exactly. Opposite-sign pairs cannot cause an increase either.

For five states only three states remain outside the pair. A sufficient missing result would be the following statement, which is a **conjecture**, not a theorem of this report:

> Merging a single pair in a finite reversible chain increases stopping-rule mixing time by at most a factor of 2.

It would imply $K(5)=2$: four-state quotients would satisfy this conjectured bound, smaller quotients already have the supplied bound 2, and identity maps preserve the time. Equation (11), the maximum principle $0\le h\le1$, and the sign argument prove (12), but they do not by themselves bound same-sign unmerged entries by $2t_{\rm mix}(X)$. The correction can be very large and cancel a very negative $F_{ij}$. Bounding the correction alone is therefore not a valid proof.

`audit_results.py` checks (11) entry by entry, including both representatives of the merged fibre, on 120 additional random integer-weight five-state chains and all 1,200 pair merges. It also checks (12), all hitting systems, and all stopping certificates exactly. No pair ratio exceeded 2 in that finite audit; its largest ratio was 1.106828190005. This audit checks the identity and the implementation, and supplies limited further evidence for the conjecture.

## 8. Conjectures and limits of the evidence

My primary conjecture is $K(5)=2$. The suggested equal-leaf family satisfies all spectral tightness conditions but loses the factor $2/3$ at $t_{\rm mix}\le\tau_0$. The unrestricted searches also plateau near 2. Neither fact rules out a different family tending to 3, or a value strictly between 2 and 3.

A broader, more tentative conjecture is

\[
K(n)=\lfloor n/2\rfloor\quad(n\ge2).
\]

The construction in Section 5 proves its lower half for every $n$. The established values $K(2)=K(3)=1$ and $K(4)=2$ agree with it; the five-state searches agree with it. There is no matching upper proof here for any $n\ge5$.

One possible route would be the stronger, presently unproved bound

\[
t_{\rm mix}(\widehat X)\le (n-q+1)t_{\rm mix}(X).
\]

Combined with the proved $q-1$ bound and optimized over integer $q$, it would give $\lfloor n/2\rfloor$. The single-pair conjecture is just its $n-q=1$ case; proving that case alone would not establish the stronger general bound.

All computational programs run for this investigation are saved in this directory. Computation was sequential, numerical-library threads were restricted to one, and the largest matrix had ten states. No run approached five minutes or 1 GB. The final exact audit reported 19.47 MB peak resident memory and 0.980 seconds wall time; the longest search was 24.928 seconds. No browsing, other agents, visible windows, Git pushes, or writes outside this directory were used. The attempted `nice -n 10` wrapper was denied by the execution sandbox; computation continued with the existing process priority and the explicit single-thread limits. No global brain/checklist/mesh writes were made because this run expressly restricted writes to its own folder.

Reproduce each computational program with `python3 PROGRAM.py`, using the environment variables `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1`, and `PYTHONDONTWRITEBYTECODE=1`. Run `exact_core.py`, `family_analysis.py`, `fork_comb.py`, `search5.py`, `search5_de.py`, and finally `audit_results.py`. `format_report.py` only normalizes the report's inline math delimiters.

`audit_report.py`, with output `audit_report.txt`, verifies that the displayed search matrix and all four large rational times match the saved exact artifacts. It also checks the result line, math delimiters, and referenced program files. Both checks passed.

Task: “Start with n = 5: is K(5) = 3?” — run began 12 November 2026, 20:38 +04.
