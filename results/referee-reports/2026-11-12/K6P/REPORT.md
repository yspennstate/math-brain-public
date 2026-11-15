Result: partial

The proposed inequality is

\[
\widehat T\le (r+1)T,\qquad r=n-q,\qquad T=t_{\rm mix}(X).
\tag{Q2}
\]

I found no counterexample. I did not prove Q2, including its remaining rank-two cases. In particular, this work does **not** establish \(K(7)=3\). The established bounds remain \(3\le K(7)\le4\).

The exact searches cover every partition with \(r=2\) and \(r=3\) on each tested network of sizes 4–8. Exact constructions approach the proposed constants; they give lower bounds, without proving the upper bounds. Two partial lemmas are proved below: an entry incident to the only merged block cannot exceed the corresponding original row maximum; and the minimum-potential argument extends to any partition when the two boundary-difference vectors are proportional. These isolate the unresolved entries.

The supplied [K5P_REPORT.md](K5P_REPORT.md) is used for the identities for \(F\), the one-pair theorem, and the quotient-state bound. Nothing below upgrades a finite test to a universal inequality.

For orientation, the existing bound already gives Q2 whenever

\[
q-1\le r+1\quad\Longleftrightarrow\quad n\le2r+2.
\]

Thus all the requested \(r=3\), \(n\le8\) cases satisfy Q2 without new work, as do all \(r=2\), \(n\le6\) cases. Among the requested sizes the unresolved cases are \((n,r)=(7,2),(8,2)\). Their available upper bound is 4, and the conjectured upper bound is 3.

Write \(d_x=\sum_y w_{xy}\), \(W=\sum_xd_x\), \(\pi=d/W\), and \(L=D_d-w\). Internal edges count in both orientations in a lump's loop, so \(W\) is preserved. Put

\[
t_i=\max_jF_{ij},\qquad \phi_i=t_i-F_{i\cdot}.
\]

The identities needed from the supplied proof are

\[
\phi_i\ge0,\quad E_\pi\phi_i=t_i,\quad
L\phi_i=We_i-d,\quad
\mathcal E(\phi_i,z)=W(z_i-E_\pi z),\quad
\mathcal E(\phi_i,\phi_j)=-WF_{ij}.
\tag{1}
\]

Here \(\mathcal E(f,g)=f^{\mathsf T}Lg\).

For completeness, the exact update used in the searches works for every partition. Choose one representative in each block and let the columns of \(C\) be \(e_a-e_b\), one for each nonrepresentative \(a\) and its block representative \(b\). There are \(r\) independent columns. Ground any vertex and extend the grounded inverse \(K\) by a zero row and column. Then

\[
B=K-KC(C^{\mathsf T}KC)^{-1}C^{\mathsf T}K
\tag{2}
\]

is the quotient's grounded inverse, lifted to the original vertices. One way to verify this is to solve the grounded Poisson problem with the constraints \(C^{\mathsf T}z=0\). The Lagrange multiplier equations give (2). The constraint space consists exactly of block-constant functions, and its energy and speed measure are those of the conductance quotient. Also \(C^{\mathsf T}KC\) is positive definite because \(C\) has independent columns of total mass zero.

Centering with \(\pi\), and using \(F=-W\mathcal C_\pi(K)\), gives

\[
\boxed{\widehat F_{f(i)f(j)}
=F_{ij}-[FC(C^{\mathsf T}FC)^{-1}C^{\mathsf T}F]_{ij}.}
\tag{3}
\]

The correction is positive semidefinite and has rank \(r\), but its individual off-diagonal entries can have either sign. The scanner evaluates (3) with `Fraction` arithmetic. It is independently compared with killed-system hitting-time solves, rather than checked only against another implementation of (3).

Here is the first partial lemma, with no gap. Suppose the only nonsingleton block is an arbitrary nonempty set \(B\). Then, for every original vertex \(j\),

\[
\boxed{\widehat F_{B,f(j)}\le t_j\le T.}
\tag{4}
\]

Let \(h(x)=E_xT_B\), zero on \(B\), and define

\[
\nu=\frac{d-Lh}{W}.
\]

Outside \(B\), the hitting equations give \(Lh=d\). On \(B\), nonnegativity of \(h\) gives \((Lh)_b=-\sum_{x\notin B}w_{bx}h_x\le0\). Thus \(\nu\) is supported on \(B\), has nonnegative entries, and has total mass one. The identities \(LF_{\cdot b}=d-We_b\) and \(E_\pi F_{\cdot b}=0\) imply

\[
h(j)-E_\pi h=\sum_{b\in B}\nu_bF_{jb}.
\tag{5}
\]

Indeed, both sides have Laplacian \(d-W\nu\), and both have stationary mean zero. Until hitting \(B\), the original and quotient chains have identical dynamics outside \(B\). Therefore the left side of (5) is precisely \(\widehat F_{f(j),B}\), including \(j\in B\). Symmetry and \(F_{jb}\le t_j\) prove (4).

This immediately restricts both rank-two shapes. For one triple, every entry incident to the triple is at most \(T\). For two disjoint pairs \(A,B\), merge \(B\) first and \(A\) second. Apply (4) to the second merge and the supplied Q1 row bound to the first:

\[
\widehat F_{A,f(j)}\le t^{X/B}_{f_B(j)}\le t_j+T\le2T.
\tag{6}
\]

Reverse the order to obtain the same assertion for entries incident to \(B\). Consequently, any rank-two counterexample to factor 3 must attain its maximum between two untouched singleton blocks. Equation (6) does not bound those entries.

There is a second extension of the supplied minimum trick, also with no gap. For any partition, define

\[
\beta_i=C^{\mathsf T}\phi_i\in\mathbb R^r.
\]

If \(\beta_i\) and \(\beta_j\) are proportional, or either is zero, then

\[
\boxed{\widehat F_{f(i)f(j)}\le t_i+t_j.}
\tag{7}
\]

Here is the proof. Work modulo constants with the energy inner product. Let \(V\) be the block-constant subspace, \(P\) the energy orthogonal projection onto \(V\), and \(Q=I-P\). For a block-constant test function \(z\), (1) shows that \(P\phi_i\) has the quotient source at \(f(i)\). Thus

\[
\widehat F_{f(i)f(j)}
=F_{ij}+\frac{\mathcal E(Q\phi_i,Q\phi_j)}W.
\tag{8}
\]

The restriction \(C^{\mathsf T}\phi_i\) uniquely determines \(Q\phi_i\). If \(\beta_i=\lambda\beta_j\), then \(Q\phi_i=\lambda Q\phi_j\). A zero vector gives zero correction; \(\lambda\le0\) gives a nonpositive correction and hence a bound by \(F_{ij}\le t_i\).

It remains to treat \(\lambda>0\). Set

\[
g=\phi_i/\lambda,\qquad k=\phi_j,\qquad m=\min(g,k),\qquad \bar m=E_\pi m.
\]

The functions \(g-k\) and \(m-k\) are block constant. For the second assertion, on a block \(g=k+c\) for a constant \(c\), so \(m=k+\min(c,0)\). In particular, \(Qm=Qk\), and the Dirichlet principle gives

\[
\mathcal E(m,m)\ge\mathcal E(Qk,Qk).
\]

The nonnegative functions \(a=g-m\), \(b=k-m\) have disjoint supports. Since the off-diagonal entries of \(L\) are nonpositive, \(\mathcal E(a,b)\le0\). Hence

\[
\mathcal E(Qk,Qk)
\le\mathcal E(g,m)+\mathcal E(k,m)-\mathcal E(g,k).
\]

Use (1), \(m_i\le k_i=t_j-F_{ij}\), and \(m_j\le g_j=(t_i-F_{ij})/\lambda\). This gives

\[
\mathcal E(Qk,Qk)
\le \frac W\lambda
[t_i+t_j-F_{ij}-(1+\lambda)\bar m].
\]

Multiply by \(\lambda/W\), substitute into (8), and use \(\bar m\ge0\). This proves (7), with the refinement

\[
\widehat F_{f(i)f(j)}\le t_i+t_j-(1+\lambda)\bar m.
\tag{9}
\]

For one pair there is only one coordinate, so proportionality is automatic. For rank two it need not hold, even at two singleton states with a positive correction. An exact seven-state example is saved in [q2_obstacle_results.json](q2_obstacle_results.json). This is an obstruction to this proof method, not a counterexample to Q2.

The gap is therefore explicit. Equations (4), (6), and (7) leave singleton-to-singleton entries with two independent boundary-difference vectors. No inequality in this report bounds all such entries by \(3T\). In particular, I have not justified either

\[
\widehat F_{f(i)f(j)}\le t_i+t_j+(r-1)T
\quad\hbox{or}\quad
\widehat T\le (\#\{\text{nonsingleton blocks}\}+1)T.
\tag{10}
\]

Both passed the tests described below. They remain conjectures. The shape scans suggest that a single triple or quadruple might even have constant 2; that is also unproved.

A separate tempting shortcut is false. If \(\kappa=-\sum_i\pi_iF_{ii}\) denotes Kemeny's constant, one cannot assert \(\widehat T\le T+\kappa-\widehat\kappa\). The supplied four-state family at parameter 10 gives exactly

\[
T=\frac{5611071}{500111},\qquad
\widehat T=\frac{10002120}{500111},\qquad
\kappa-\widehat\kappa=\frac{610061}{500111}.
\]

The proposed right side falls short by \(3780988/500111\). This calculation is in [q2_obstacles.py](q2_obstacles.py) and is not used in either partial proof.

Here are the best ratios encountered. The symbols in the table are exact rational numbers defined immediately below; the displayed decimals are only approximations. Full numerators, denominators, conductance matrices, partitions, and both times are in [q2_best.json](q2_best.json) and [q2_family_results.json](q2_family_results.json).

| Original states \(n\) | \(r=2\): exact best ratio | Decimal | \(r=3\): exact best ratio | Decimal |
|---:|:---:|---:|:---:|---:|
| 4 | \(1\) | 1 | \(0\) | 0 |
| 5 | \(R_2\) | 1.999999999998 | \(1\) | 1 |
| 6 | \(R_3\) | 2.999999999994 | \(R_2\) | 1.999999999998 |
| 7 | \(R_3\) | 2.999999999994 | \(R_3\) | 2.999999999994 |
| 8 | \(R_3\) | 2.999999999994 | \(R_4\) | 3.999999999987 |

Set \(M=10^{12}\), exactly. The first rational is

\[
R_2=
\frac{2M^7+4M^3+2M^2+4M}
{M^7+M^6+2M^5+2M^4+2M^3+M^2+4M+2}.
\tag{11}
\]

It is the supplied four-state sharp family. For \(R_3\), define the following integers:

\[
\begin{aligned}
W_3&=3M^{15}+2M^9+M^8+M^7+M^5+M^4+2M^3+M+1,\\
U_3&=M^3+M+1,\\
S_3&=W_3-3M^{15}-M^9,\\
V_3&=M^8+M^3+M+1.
\end{aligned}
\]

Then the exact times and ratio are

\[
\begin{aligned}
T_3&=M+\frac{U_3}{M^3}+\frac{S_3}{M^9}
-\frac{M^2+M^9+M^6+U_3^2/M^3+S_3^2/M^9}{W_3},\\
\widehat T_3&=2M+\frac{V_3}{M^7+M^3}
-\frac{M^2+M^6+V_3^2/(M^7+M^3)}{W_3},\\
R_3&=\widehat T_3/T_3.
\end{aligned}
\tag{12}
\]

This is the six-state fork \(N=1\), with indices \((a,b,c,z_0,z_1,y_0)=(0,1,2,3,4,5)\), lumped into

\[
\{a\},\quad\{b,z_0\},\quad\{c,z_1\},\quad\{y_0\}.
\]

For \(R_4\), define

\[
\begin{aligned}
W_4&=4M^{18}+2M^{12}+M^{11}+M^{10}+M^8+M^7+2M^6+M^5+M^4+2M^3+M+1,\\
U_4&=M^3+M+1,\\
V_4&=M^6+M^5+M^4+2M^3+M+1,\\
S_4&=W_4-4M^{18}-M^{12},\\
A_4&=M^5+M^3+M+1,\\
B_4&=M^{11}+M^6+M^5+M^4+2M^3+M+1.
\end{aligned}
\]

The remaining exact times and ratio are

\[
\begin{aligned}
T_4&=M+\frac{U_4}{M^3}+\frac{V_4}{M^6}+\frac{S_4}{M^{12}}
-\frac{M^2+M^6+M^9+M^{12}+U_4^2/M^3+V_4^2/M^6+S_4^2/M^{12}}{W_4},\\
\widehat T_4&=2M+\frac{A_4}{M^4+M^3}+\frac{B_4}{M^{10}+M^6}
-\frac{M^2+M^9+A_4^2/(M^4+M^3)+B_4^2/(M^{10}+M^6)}{W_4},\\
R_4&=\widehat T_4/T_4.
\end{aligned}
\tag{13}
\]

This is the eight-state fork \(N=2\), with order \((a,b,c,z_0,z_1,z_2,y_0,y_1)\), and blocks

\[
\{a\},\quad\{b,z_1\},\quad\{c,z_2\},\quad\{z_0,y_0\},\quad\{y_1\}.
\]

The integer expressions (11)–(13), evaluated at the specified integer \(M\), specify the exact numbers without decimal rounding or an unspecified limiting parameter. [q2_families.py](q2_families.py) verifies each time, each maximizing pair, and every partition of the relevant merge deficit using exact hitting equations and (3).

The padding in the table is explicit. To split a state \(c\) into \(k\) equal clones, replace each incident conductance by its share: a clone-to-unsplit edge has weight \(w_{ci}/k\); each ordered clone-to-clone conductance, including loops, has weight \(w_{cc}/k^2\). Other weights stay fixed. This preserves total mass. For different original states, the cloned chain has the same \(F\) entries. Between distinct clones the entry is \(F_{cc}+1/\pi_c\); on a clone's diagonal it is \(F_{cc}-(k-1)/\pi_c\). These formulas follow by separating the block-constant functions from the within-clone mean-zero modes, on which \(I-P\) is the identity.

For \((n,r)=(5,2),(6,3)\), split the heavy root of the four-state family into two or three clones and put all root clones and the old hub in the same block. For \((7,2),(8,2)\), split the untouched singleton \(a\) of the six-state construction into two or three clones, each kept singleton. For \((7,3)\), split \(c\) into two clones and include both in \(\{c,z_1\}\). In these specified cases the extra within-clone entries do not change the original maximum, nor the quotient maximum. Both facts are independently checked exactly. The entries equal to 1 come from \(w_{ij}=1\), including loops: the chain and every nontrivial quotient are independent stationary draws, with stopping-rule mixing time 1. A one-state quotient has time 0.

An early padding attempt split a vertex in a merged block but kept its new clone outside the block. That does not give a cloned quotient. The exact audit rejected the asserted equality of times; the construction above uses singleton cloning instead. The failed output is retained as [q2_family_output_failed.txt](q2_family_output_failed.txt).

The search programs and evidence are as follows. All random seeds and weight ranges are in the saved programs.

| Program | Work performed | Saved output/data |
|---|---|---|
| [q2_search.py](q2_search.py), [q2_batch.py](q2_batch.py) | Exact random and structured scans; numerical optimization followed by exact all-partition verification | `q2_random_4.txt`, `q2_random_8.txt`, `q2_structured_8.txt`, `q2_batch_output.txt`, `q2_opt_7_2_1121.txt`, `q2_opt_batch_output.txt`, `q2_counts.jsonl`, `q2_best.json` |
| [q2_opt_batch.py](q2_opt_batch.py) | Sequential numerical optimization for all requested sizes and deficits, every possible nonsingleton shape | `q2_opt_batch_output.txt` |
| [q2_exact_opt.py](q2_exact_opt.py) | Exact-rational objective optimization on seven and eight states, both triples and two pairs | `q2_exact_opt_7_22117.txt`, `q2_exact_opt_8_22118.txt`, corresponding `_results.json` files |
| [q2_shape_search.py](q2_shape_search.py) | All-partition scans and both proposed inequalities in (10), for every original representative | `q2_shape_output.txt`, `q2_shape_results.json` |
| [q2_families.py](q2_families.py) | Exact near-sharp families, clone padding, and formulas (11)–(13) | `q2_family_output.txt`, `q2_family_results.json` |
| [q2_audit.py](q2_audit.py) | Independent hitting solves for (3), plus the source and minimum-potential lemmas | `q2_audit_output.txt`, `q2_audit_results.json` |
| [q2_obstacles.py](q2_obstacles.py) | Exact singleton nonproportionality witness and rejection of the additive Kemeny shortcut | `q2_obstacle_output.txt`, `q2_obstacle_results.json` |
| [q2_summary.py](q2_summary.py) | Readable rational and shape summaries | `q2_summary_output.txt` |
| [q2_check_report.py](q2_check_report.py) | Final independent recomputation of every best ratio, formula checks, partition counts, search totals, and report references | `q2_check_report_output.txt` |

The initial exact random scan used 20 rational networks at each size, 100 networks and 40,180 quotient evaluations. A random tree ensures connectivity; extra edges, loops, and independent powers of ten provide varied bottlenecks and stationary masses. The structured scan used 96 networks and 45,252 quotient evaluations: fork combs, paths with heavy ends, weighted stars, and the supplied four-state family with extra leaves, at parameters 10, 100, 1,000, and 1,000,000.

For each tested network all set partitions of the required deficit were enumerated, not just the intended structured partition. The numbers per network are:

| \(n\) | Partitions with \(r=2\) | Partitions with \(r=3\) |
|---:|---:|---:|
| 4 | 7 | 1 |
| 5 | 25 | 15 |
| 6 | 65 | 90 |
| 7 | 140 | 350 |
| 8 | 266 | 1,050 |

The numerical optimizers performed 296,376 objective evaluations. They explored full networks, random trees, and paths, with differential evolution followed by Nelder–Mead. All 69 final rounded candidates were interpreted as exact rationals and scanned over every partition of their merge deficit. Numerical values alone were never accepted. For example, an apparent four-to-two ratio 1.0000023557 became strictly below 1 in exact arithmetic; the all-ones example later attained exactly 1.

The separate shape scan used the 96 structured networks plus 50 fresh random networks and checked 2,361,140 representative-level entries. Neither inequality in (10) failed. The extra exact optimizers evaluated 23,818 objectives on seven states and 13,931 on eight states, 37,749 exact objectives in total. They use rational objective values on every proposal; only proposal generation and annealing acceptance probabilities use floating point. They are searches, not global optimality certificates. Each run covered both rank-two shapes and stopped after approximately 170 seconds. Neither improved the final family values in the table.

The independent partial-proof audit used 20 fresh or symmetric networks, 8,356 partition comparisons, 9,352 merged-source entry checks, 22,176 two-pair incident-entry checks, and 78,800 proportional-vector checks. It checked the pointwise minimum's constraints, the disjoint-support energy sign, the Dirichlet lower bound, and the final refinement (9), wherever its hypothesis applied. Its output ends:

```text
ALL Q2 PARTIAL LEMMA AUDITS PASSED {'networks': 20, 'partitions': 8356, 'merged_source_entries': 9352, 'two_pair_entries': 22176, 'collinear_entries': 78800}
```

These tests support the implementation and the stated lemmas. They supply no missing argument for the independent-vector case.

The final report check independently recomputed every best chain and quotient from the saved conductances and checked the exact formulas and all reported run totals. Its output is `REPORT CHECK PASSED` in [q2_check_report_output.txt](q2_check_report_output.txt).

Every program was saved here before execution. Runs were sequential except for at most two task computations at once, used one numerical-library thread each, and used no web, agents, Git push, external file writes, or visible windows. Python bytecode writes were disabled. The largest numerical-search peak RSS was 75,612,160 bytes, well below 1 GB. The longest computation was 170.012 seconds; every computation was shorter than five minutes. The exact optimizers have their own 170-second stopping budgets. Global brain/checklist/mesh programs were not invoked because they write outside the directory authorized for this task.

To reproduce a single run from this directory, for example:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 q2_audit.py > q2_audit_output.txt 2>&1
```

Other commands are `python3 q2_batch.py`, `python3 q2_search.py random 4`, `python3 q2_search.py random 8`, `python3 q2_search.py structured 8`, `python3 q2_search.py opt 7 2 1121`, `python3 q2_opt_batch.py`, `python3 q2_exact_opt.py 7 22117`, `python3 q2_exact_opt.py 8 22118`, `python3 q2_shape_search.py`, `python3 q2_families.py`, `python3 q2_obstacles.py`, and `python3 q2_summary.py`, using the same environment and their corresponding output files. Repeated runs append to the event log and may improve saved incumbents.

Task: “Is it true that a lumping made of r = n - q merges raises the mixing time by at most a factor r + 1” — 12 November 2026, 21:58 +04 (first recorded task time).
