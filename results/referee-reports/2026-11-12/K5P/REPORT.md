Result: proved

For every finite irreducible reversible chain \(X\), and every pair of distinct states \(u,v\),

\[
\boxed{t_{\rm mix}(X/\{u,v\})\le 2t_{\rm mix}(X).}
\]

The constant 2 is optimal. In fact the inequality is strict for every finite chain with at least two states, but a four-state family approaches equality. The proof below also gives an entrywise refinement. There are no unproved steps in the argument.

Together with the quotient-state bound proved below, this establishes \(K(5)=2\). This conclusion uses a case split by quotient size; multiplying the bounds for successive single merges would not establish it.

## 1. Hitting potentials and their energy

Write \(d_x=\sum_y w_{xy}\), \(W=\sum_x d_x\), and \(\pi_x=d_x/W\). A loop contributes once to \(d_x\). The Laplacian is

\[
L_{xy}=-w_{xy}\quad(x\ne y),\qquad
L_{xx}=\sum_{y\ne x}w_{xy}.
\]

Thus \(L=D_d(I-P)\); loops cancel from \(L\), and remain in the speed measure \(d\). Define

\[
\mathcal E(f,g)=f^{\mathsf T}Lg
=\frac12\sum_{x,y}w_{xy}(f_x-f_y)(g_x-g_y).
\tag{1}
\]

Let \(H(x,j)=\mathbb E_xT_j\), and put

\[
F_{ij}=H(i,j)-\sum_x\pi_xH(x,j).
\tag{2}
\]

We will use the following identities:

\[
F_{ij}=F_{ji},\qquad
\sum_x\pi_xF_{ix}=0,\qquad
LF_{\cdot j}=d-We_j.
\tag{3}
\]

Here is a derivation, including symmetry. Ground any vertex \(r\); let \(K\) be the inverse of the grounded Laplacian, extended by a zero row and column at \(r\). Set

\[
a=Kd,\qquad \mu=\frac{d^{\mathsf T}Kd}{W}.
\]

The hitting equations give

\[
H(i,j)=a_i-a_j-W(K_{ij}-K_{jj}).
\tag{4}
\]

Indeed, this expression is zero at \(j\), and its Laplacian is \(d-We_j\), so it is the unique hitting-time solution. For \(j\ne r\), the identity used here is \(LK_{\cdot j}=e_j-e_r\); the case \(j=r\) follows from \(La=d-We_r\). Since \(K\pi=a/W\), centering (4) gives

\[
F_{ij}=a_i+a_j-\mu-WK_{ij}.
\tag{5}
\]

This is symmetric. Column centering, symmetry, and the hitting equations prove (3).

Define the optimal mean stopping time from \(i\), and its nonnegative potential, by

\[
t_i=\max_jF_{ij},\qquad
\phi_i(x)=t_i-F_{ix}.
\tag{6}
\]

The Lovász–Winkler formula in the question says \(T:=t_{\rm mix}(X)=\max_i t_i\). Equation (3) gives \(t_i\ge0\) and

\[
\phi_i\ge0,\qquad
\mathbb E_\pi\phi_i=t_i,\qquad
L\phi_i=We_i-d.
\tag{7}
\]

In particular, for every function \(z\),

\[
\mathcal E(\phi_i,z)=W\bigl(z_i-\mathbb E_\pi z\bigr),
\qquad
\mathcal E(\phi_i,\phi_j)=-WF_{ij}.
\tag{8}
\]

The second identity follows by substituting \(z=\phi_j\) in the first and using symmetry of \(F\).

## 2. The exact effect of one merge

Let \(h_x=\mathbb P_x(T_u<T_v)\), with boundary values \(h_u=1,h_v=0\). Let \(R>0\) be the effective resistance between \(u,v\), and let \(p=\mathbb E_\pi h\). Then

\[
Lh=\frac{e_u-e_v}{R},\qquad \mathcal E(h,h)=\frac1R.
\tag{9}
\]

Ground \(v\) in the preceding construction. The unit-current potential gives \(K_{uu}=R\) and \(K_{xu}=Rh_x\). If \(S=I\setminus\{u,v\}\), the matrix

\[
B=K-Rhh^{\mathsf T}
\tag{10}
\]

has zero rows and columns at \(u,v\), and \(B_{SS}=L_{SS}^{-1}\). To check the latter statement directly, the block identities \(L_{SS}K_{SS}+L_{Su}K_{uS}=I\) and \(L_{SS}K_{Su}+L_{Su}K_{uu}=0\) give

\[
L_{SS}\left(K_{SS}-\frac{K_{Su}K_{uS}}{K_{uu}}\right)=I.
\]

The grounded Laplacian of the quotient, with the merged state grounded, is exactly \(L_{SS}\). Also its total mass is still \(W\), and its stationary mass at a block is the sum of the original masses. Hence \(B\) is its grounded inverse lifted to the original state set.

For any matrix \(A\), write its centering as

\[
\mathcal C_\pi(A)_{ij}
=A_{ij}-(A\pi)_i-(\pi^{\mathsf T}A)_j+\pi^{\mathsf T}A\pi.
\]

Equation (5) says \(F=-W\mathcal C_\pi(K)\). Since centering a lifted block-constant matrix with \(\pi\) agrees with centering its quotient matrix with the aggregated law, (10) proves

\[
\widehat F_{f(i)f(j)}
=F_{ij}+WR(h_i-p)(h_j-p).
\tag{11}
\]

Define

\[
\beta_i=\phi_i(u)-\phi_i(v)=F_{iv}-F_{iu}.
\]

Formula (5), \(K_{iu}=Rh_i\), and \(a_u=\sum_x Rh_xd_x=WRp\) give

\[
\beta_i=WR(h_i-p),\qquad
\widehat F_{f(i)f(j)}=F_{ij}+\frac{\beta_i\beta_j}{WR}.
\tag{12}
\]

This also covers representatives of the merged state and diagonal entries.

## 3. The minimum-potential inequality

We prove the stronger assertion

\[
\boxed{\widehat F_{f(i)f(j)}\le t_i+t_j\quad\text{for every }i,j.}
\tag{13}
\]

If \(\beta_i\beta_j\le0\), (12) gives \(\widehat F_{f(i)f(j)}\le F_{ij}\le t_i\le t_i+t_j\).

Suppose \(\beta_i\beta_j>0\). Interchange the names \(u,v\), if necessary, so that both \(\beta_i,\beta_j\) are positive. This changes their signs together and leaves their product and \(R\) unchanged. Define

\[
g=\frac{\phi_i}{\beta_i},\qquad
k=\frac{\phi_j}{\beta_j},\qquad m=\min(g,k)
\tag{14}
\]

pointwise. These functions are nonnegative. Moreover,

\[
g_u-g_v=k_u-k_v=1,
\quad\text{so}\quad
m_u-m_v=\min(g_v+1,k_v+1)-\min(g_v,k_v)=1.
\tag{15}
\]

It follows from the Dirichlet principle that

\[
\mathcal E(m,m)\ge\frac1R.
\tag{16}
\]

For completeness, write \(m=m_v\mathbf1+h+z\), where \(z_u=z_v=0\). Equation (9) gives \(\mathcal E(h,z)=0\), and therefore \(\mathcal E(m,m)=1/R+\mathcal E(z,z)\ge1/R\).

Set \(a=g-m\ge0\) and \(b=k-m\ge0\). At each vertex at least one of \(a,b\) is zero, so \(a_xb_x=0\). By the nonpositive off-diagonal entries of \(L\),

\[
\mathcal E(a,b)
=-\sum_{x\ne y}w_{xy}a_xb_y\le0.
\tag{17}
\]

Expanding \(g=m+a\), \(k=m+b\) now gives

\[
\begin{aligned}
\frac1R
&\le\mathcal E(m,m)\\
&\le\mathcal E(g,m)+\mathcal E(k,m)-\mathcal E(g,k),
\end{aligned}
\tag{18}
\]

because the last expression equals \(\mathcal E(m,m)-\mathcal E(a,b)\).

Put \(\overline m=\mathbb E_\pi m\ge0\). By (8),

\[
\mathcal E(g,m)=\frac W{\beta_i}(m_i-\overline m),\qquad
\mathcal E(k,m)=\frac W{\beta_j}(m_j-\overline m),\qquad
\mathcal E(g,k)=-\frac{WF_{ij}}{\beta_i\beta_j}.
\tag{19}
\]

The pointwise minimum in (14) also gives

\[
m_i\le k_i=\frac{t_j-F_{ij}}{\beta_j},\qquad
m_j\le g_j=\frac{t_i-F_{ij}}{\beta_i}.
\tag{20}
\]

Substitute (19)–(20) into (18). All denominators are positive, so the inequality directions are preserved:

\[
\frac1R
\le\frac W{\beta_i\beta_j}
\left[t_i+t_j-F_{ij}-(\beta_i+\beta_j)\overline m\right].
\tag{21}
\]

Multiplication by \(\beta_i\beta_j/W\), followed by (12), proves

\[
\widehat F_{f(i)f(j)}
\le t_i+t_j-(\beta_i+\beta_j)\overline m
\le t_i+t_j.
\tag{22}
\]

This proves (13). Taking the maximum over quotient entries gives

\[
t_{\rm mix}(X/\{u,v\})\le\max_{i,j}(t_i+t_j)\le2T.
\]

Every quotient entry is represented by some \(i,j\), so this maximum includes all cases. This completes the proof of Q1.

There is also strictness for a finite chain. In the positive-product case, (15) and \(m\ge0\) imply \(m_u\ge1\), so \(\overline m\ge\pi_u>0\). Thus (22) is strictly below \(2T\). In the nonpositive-product case the entry is at most \(T<2T\). Here \(T>0\) for an irreducible chain with at least two states: otherwise a row of \(F\) would be identically zero by its zero stationary mean, contradicting \(LF_{\cdot i}=d-We_i\ne0\). There are finitely many entries, so the quotient time is strictly less than \(2T\).

## 4. A four-state family with limiting ratio 2

For an integer \(t\ge2\), take states \(a,b,u,v\), with conductances

\[
w_{au}=w_{bu}=1,\quad w_{uv}=t^2,\quad
w_{aa}=w_{bb}=t-1,\quad w_{vv}=t^6,
\tag{23}
\]

and all other entries zero, apart from symmetry. Merge \(u,v\). All weights are integers, and the underlying graph is a tree.

Let

\[
W=t^6+2t^2+2t+2,\quad S=t^2+2t+2,\quad
C=S/t^2,\quad M=t+C,\quad
\mu=\frac{2t^2+S^2/t^2}{W}.
\]

Grounding at \(v\), the inverse on \(a,b,u\) is

\[
K=\begin{pmatrix}
1+t^{-2}&t^{-2}&t^{-2}\\
t^{-2}&1+t^{-2}&t^{-2}\\
t^{-2}&t^{-2}&t^{-2}
\end{pmatrix}.
\tag{24}
\]

Multiplication by the grounded Laplacian checks this matrix. Its hitting potentials are \(H(a,v)=H(b,v)=M\), \(H(u,v)=C\), and their stationary mean is \(\mu\). Every entry of (24) is at least \(t^{-2}\). Since

\[
W/t^2-M=t^4+1-t>0,
\]

(5) bounds every entry with both indices different from \(v\) by \(2M-\mu-W/t^2<M-\mu\). Entries involving \(v\) are at most \(M-\mu\), attained with \(a\) or \(b\). Consequently,

\[
T=M-\mu
=\frac{t^7+t^6+2t^5+2t^4+2t^3+t^2+4t+2}{W}.
\tag{25}
\]

In the quotient, \(a,b\) are leaves attached by conductance 1 to the merged root. Each has root hitting time \(t\), and the mean root hitting time is \(2t^2/W\). The grounded inverse on the two leaves is the identity. Thus the largest entries are the two ordered pairs of distinct leaves, giving

\[
\widehat T=2t-\frac{2t^2}{W}
=\frac{2t^7+4t^3+2t^2+4t}{W}.
\tag{26}
\]

The ratio of (26) and (25) tends to 2 by their leading coefficients. Exact checks give:

| \(t\) | \(\widehat T/T\), rounded |
|---:|---:|
| 2 | 0.955974842767296 |
| 10 | 1.78256878232337 |
| 100 | 1.97980205978806 |
| 1,000 | 1.997998002006 |
| 1,000,000 | 1.999997999998 |

The rational formulas, rather than their decimal approximations, prove sharpness. The exact times and full matrices for these parameters are in `audit_proof_results.json`.

## 5. What follows for arbitrary lumpings and \(K(5)\)

An \(n\)-state partition into \(q\) blocks can be realized by \(n-q\) single-pair merges. Conductance summation is associative. Therefore Q1, by iteration alone, gives exactly the bound

\[
t_{\rm mix}(\widehat X)\le2^{\,n-q}t_{\rm mix}(X).
\tag{27}
\]

It does not give an overall factor 2 for an arbitrary number of merges.

We also have, for every reversible quotient on \(q\ge2\) states,

\[
t_{\rm mix}(\widehat X)
\le\tau_0(\widehat X)
\le(q-1)\tau_2(\widehat X)
\le(q-1)\tau_2(X)
\le(q-1)t_{\rm mix}(X).
\tag{28}
\]

Here are the ingredients of this separate argument. Stopping at an independent stationary random target has mean \(\tau_0\), giving its first inequality. For a reversible \(q\)-state chain, the inverse of \(I-P\) on mean-zero functions is \(Z=-FD_\pi\), by (3). Its trace is

\[
\operatorname{tr}Z=-\sum_j\pi_jF_{jj}
=\sum_j\pi_j\mathbb E_\pi T_j=\tau_0
=\sum_{k=2}^{q}\frac1{1-\lambda_k}.
\]

The random-target mean is independent of the starting state because \(\sum_j\pi_jH(i,j)=-\sum_j\pi_jF_{jj}\), by (3) and \(H(i,j)=F_{ij}-F_{jj}\). This proves the second inequality in (28). Restricting the Rayleigh quotient to functions constant on each block proves \(\tau_2(\widehat X)\le\tau_2(X)\). Finally \(\tau_2(X)\le t_{\rm mix}(X)\) is the eigenfunction stopping argument: normalize a second eigenfunction \(g\) so \(g(i)=1=\max_x|g(x)|\). For an integrable stationary stopping rule \(U\) from \(i\), optional stopping in

\[
g(X_s)+(1-\lambda_2)\sum_{r<s}g(X_r)
\]

gives \(1=(1-\lambda_2)\mathbb E_i\sum_{r<U}g(X_r)\le(1-\lambda_2)\mathbb E_iU\), since \(g\) has stationary mean zero. Its bounded increments justify optional stopping when \(\mathbb E_iU<\infty\); infinite means already satisfy the lower bound. Taking the optimal rule proves the last inequality.

Combining (27) and (28) gives

\[
\frac{t_{\rm mix}(\widehat X)}{t_{\rm mix}(X)}
\le\min\{2^{n-q},q-1\}\qquad(q\ge2).
\tag{29}
\]

For an original chain on exactly five states:

- A five-state quotient is just a relabeling and has ratio 1.
- A four-state quotient merges exactly one pair, so Q1 bounds its ratio by 2.
- A quotient with two or three states has ratio at most \(q-1\le2\), by (28).
- A one-state quotient has mixing time zero.

For originals on at most four states, a nontrivial quotient has at most three states, so (28) already gives the same upper bound 2. The family (23) proves the matching lower bound. Hence

\[
\boxed{K(4)=K(5)=2.}
\]

For example, a five-to-three lumping requires two single merges. The product bound from Q1 would be 4; (28), applied directly to its three-state quotient, gives 2. This is why the \(K(5)\) conclusion is valid without claiming that successive factors always have product at most 2.

## 6. Programs, searches, and exact audits

All computations were sequential and used one numerical-library thread. No agents, web access, Git pushes, visible windows, or writes outside this directory were used. Global brain, checklist, and mesh programs were not invoked because they would write outside the authorized directory. Every Python program executed or imported is saved here. The largest reported peak memory was 73,515,008 bytes; the longest computation was 12.485 seconds, within the stated limits.

`q1_core.py` supplies two methods: exact target-by-target killed-system solves using `Fraction`, and a numerical grounded-inverse formula. The exact method checks symmetry and scans every possible pair merge. All loops created by merging include both orientations of each internal edge.

`search_q1.py` (output `search_q1_output.txt`, candidates and exact all-pair scans in `search_q1_results.json`) tested 1,200 random log-weight networks at each of 3, 4, 5, and 6 states, scanning every pair. It then used differential evolution and Nelder–Mead, with multiple restarts and log weights in \([-12,12]\). Its counter records 337,734 numerical chain evaluations. Final matrices were rounded to nine significant decimal digits, interpreted as exact rationals, and scanned over all merges with the exact hitting solver. Its best exact ratios were:

| states | best exact ratio, rounded |
|---:|---:|
| 3 | 0.999999999998035 |
| 4 | 1.90670732573568 |
| 5 | 1.97848209179884 |
| 6 | 1.95633334404139 |

The numerical optimization produced a nearly singular three-state candidate with apparent ratio 1.0000022; exact arithmetic gave the value below 1 in the table. No numerical candidate was treated as a counterexample without exact checking.

`exact_and_structured.py` (output `exact_and_structured_output.txt`, details `exact_and_structured_results.json`) tested 100 exact random rational networks at each size 3–6, with every merge evaluated exactly. It also tested paths, stars, cycles, two cliques joined by an edge, the parallel-leaf family, and the supplied fork comb with **one merge at a time**. This comprised 466 exact networks in total, including fork combs with 4, 6, and 8 states. No ratio exceeded 2. It additionally checked (11) in 9,130 exact matrix entries. The largest ratio in its fork tests was 1.98000001979804 at \(N=0,t=100\); the largest parallel-leaf ratio was 1.96059213764917 at 6 states and \(t=100\).

`audit_proof.py` (output `audit_proof_output.txt`, exact family data `audit_proof_results.json`) is the decisive algebra audit. It independently solves all hitting systems and checks (7)–(8), the rank-one identity, normalization of the two potentials, their pointwise minimum, the disjoint-support energy sign, the Dirichlet lower bound, both source evaluations, both bounds in (20), and the final inequality (22). It also independently checks the integer-polynomial formulas (25)–(26) and all maximizing pairs. Its output ends:

```text
ALL CHECKS PASSED {'networks': 101, 'merges': 846, 'entries': 22392, 'minimum_lemmas': 12822}
```

These consist of 96 fresh exact random networks and five sharp-family parameters. The audit took 4.475 seconds and reported 28,114,944 bytes peak resident memory. It supports implementation correctness; the proof in Sections 1–3 is independent of the finite tests.

Three exploratory programs are also retained with their outputs:

- `metric_relaxation.py` → `metric_relaxation_output.txt` and `metric_relaxation_results.json`. It relaxes actual networks to centered kernels satisfying resistance triangle inequalities and the rank-one relation. That relaxation reaches 2.2944. It omits the Laplacian sign condition and does **not** produce a Markov-chain counterexample. Equation (17) identifies the sign property needed by the proof.
- `candidate_inequalities.py` → `candidate_inequalities_output.txt` and `candidate_inequalities_results.json`. It rejects the tempting stronger claim \(\widehat F_{ij}\le\max_k(F_{ik}+F_{jk})\); that claim is not used.
- `test_bound_variants.py` → `test_bound_variants_output.txt` and `test_bound_variants_results.json`. It tests five other proposed strengthenings, rejecting several numerically. The fourth tested bound is (13); the exact audit above checks the proved bound and every step establishing it. None of the rejected strengthenings is used in the proof.

To reproduce, run each program separately from this directory, with the following environment; all writes stay here:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit_proof.py > audit_proof_output.txt 2>&1
```

Replace `audit_proof.py` and its output filename with the other program names to reproduce their runs. `q1_core.py` is a library imported by those programs. The existing `check_fork_comb.py` and supplied paper/report were left unchanged.

`format_and_check_report.py`, with output `format_and_check_report_output.txt`, checks the result line, balanced TeX delimiters, referenced artifact files, exact family values, audit counts, and saved search records. It reports `REPORT CHECK PASSED`.

Task: “Is it true that merging a SINGLE pair {u,v} never more than doubles the mixing time” — 12 November 2026, 21:17 +04.
