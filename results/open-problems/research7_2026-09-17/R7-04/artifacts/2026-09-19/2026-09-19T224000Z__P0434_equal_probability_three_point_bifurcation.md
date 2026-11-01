# P0434 — equal-probability three-point bifurcation and an exact SOAP comparison

Target: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1*, Proc. ACM Meas. Anal. Comput. Syst. 4(1), Article 11 (2020), DOI 10.1145/3379477, Section 8, Conjecture 8.1. The source asks whether the sharp all-load approximation ratio of M-SERPT relative to optimal Gittins is 2.

This note does **not** close Conjecture 8.1. It carries out the STUCK1 recovery action selected in the preceding R7-04 report and proves a larger exact one-parameter restricted theorem. No novelty claim is made from a negative literature search.

## 1. The recovery family

Let

\[
\Pr\{X=1\}=\Pr\{X=2\}=\Pr\{X=c\}=\frac13,
\qquad c>2,
\tag{1.1}
\]

and write

\[
m=\mathbb EX=\frac{c+3}{3},
\qquad \rho=\lambda m<1.
\tag{1.2}
\]

The preceding three-point rank theorem gives, for age \(u\), the exact Gittins candidates

\[
A_1(u)=3(1-u),\qquad
A_2(u)=\frac{5-3u}{2},\qquad
A_3(u)=m-u,
\qquad 0\le u<1,
\tag{1.3}
\]

\[
B_1(u)=4-2u,\qquad
B_2(u)=2-u+\frac{c-2}{2},
\qquad 1\le u<2,
\tag{1.4}
\]

and

\[
r_G(u)=c-u,\qquad 2\le u<c.
\tag{1.5}
\]

Thus

\[
r_G(u)=\min\{A_1(u),A_2(u),A_3(u)\}
\quad(0\le u<1),
\tag{1.6}
\]

and

\[
r_G(u)=\min\{B_1(u),B_2(u)\}
\quad(1\le u<2).
\tag{1.7}
\]

The fresh Gittins rank is therefore

\[
\boxed{
r_0=r_G(0)=\min\left\{3,\frac52,m\right\}
=\min\left\{\frac52,m\right\}.
}
\tag{1.8}
\]

For M-SERPT, the exact three envelope levels are

\[
M_0=m,
\qquad
M_1=\max\left\{m,\frac c2\right\},
\qquad
M_2=\max\{M_1,c-2\}.
\tag{1.9}
\]

Two elementary differences control all changes of policy topology:

\[
\boxed{
D_2(c):=(c-2)-m=\frac{2c-9}{3},
}
\tag{1.10}
\]

and

\[
\boxed{
D_1(c):=\frac c2-m=\frac{c-6}{6}.
}
\tag{1.11}
\]

Both are strictly increasing in \(c\). Hence the only relevant bifurcation points for the equal-probability family are

\[
\boxed{c=\frac92\quad\text{and}\quad c=6.}
\tag{1.12}
\]

This is method B13's monovariant reduction: terminal demotion begins exactly when \(D_2\) becomes positive, and the extra M-SERPT demotion at age 1 begins exactly when \(D_1\) becomes positive.

## 2. B4: the selected recovery case X uniform on {1,2,3}

Set \(c=3\). Then \(m=2\). Equations (1.3)--(1.7) reduce to

\[
r_G(u)=
\begin{cases}
2-u,&0\le u\le \frac12,\\
3(1-u),&\frac12\le u<1,\\
\frac52-u,&1\le u\le\frac32,\\
4-2u,&\frac32\le u<2,\\
3-u,&2\le u<3.
\end{cases}
\tag{2.1}
\]

The rank does jump upward at ages 1 and 2, but the jump heights are respectively \(3/2\) and \(1\), both strictly below the fresh rank

\[
r_G(0)=2.
\tag{2.2}
\]

This corrects a phrase in the preceding STUCK1 diagnosis: those are local jumps of the raw rank, but they are **not hills in the source's increasing-envelope sense**, because the increasing envelope has already attained value 2 at age 0 and never rises above it.

For every positive age before completion, the running job has Gittins rank at most 2, and at every equality a newly arriving job is later in FCFS tie order. The source's SOAP convention is to serve the minimum rank and break rank ties in FCFS order. Consequently, once a job starts service it is never preempted by a later arrival. The next job to start is the earliest waiting arrival. Hence Gittins is sample-path identical to FCFS.

For M-SERPT, (1.9) gives

\[
M_0=M_1=M_2=2,
\tag{2.3}
\]

so M-SERPT is also sample-path identical to FCFS. We have proved:

**Theorem 2.1.** If \(X\) is uniform on \(\{1,2,3\}\), then for every stable load \(0<\rho<1\),

\[
\boxed{
T_{MS}\overset d=T_G\overset d=T_{FCFS}
}
\tag{2.4}
\]

under the common arrival/service sample path, and therefore

\[
\boxed{
\frac{\mathbb ET_{MS}}{\mathbb ET_G}=1.
}
\tag{2.5}
\]

The common mean is the Pollaczek--Khinchine value

\[
\boxed{
\mathbb ET_G=\mathbb ET_{MS}
=2+\frac{7\rho}{6(1-\rho)}.
}
\tag{2.6}
\]

Indeed \(\mathbb EX=2\) and \(\mathbb EX^2=14/3\).

Thus the STUCK1 recovery target is completely settled, but it was more degenerate than the preceding diagnosis anticipated.

## 3. B5: deform the third atom

The same argument actually proves a whole interval.

### Theorem 3.1: FCFS-neutral cell

If

\[
2<c\le\frac92,
\tag{3.1}
\]

then both Gittins and M-SERPT are sample-path identical to FCFS at every stable load.

**Proof.** In this range \(m\le5/2\), so (1.8) gives \(r_0=m\). After service starts:

- on \([0,1)\), the candidate \(A_3(u)=m-u\) shows \(r_G(u)\le m\);
- on \([1,2)\), the candidate \(B_2(u)\) is maximized at age 1, where \(B_2(1)=c/2\le m\) because \(c\le6\);
- on \([2,c)\), \(r_G(u)=c-u\le c-2\le m\), where the last inequality is exactly \(D_2(c)\le0\).

Thus the Gittins rank never becomes worse than the fresh rank. FCFS tie-breaking again prevents later arrivals from preempting the job in service, so Gittins is FCFS.

For M-SERPT, \(c\le9/2<6\) gives \(M_1=m\), and \(D_2(c)\le0\) gives \(M_2=m\). Hence its rank is constant \(m\) and it is FCFS. □

Therefore

\[
\boxed{
2<c\le\frac92
\quad\Longrightarrow\quad
\frac{\mathbb ET_{MS}}{\mathbb ET_G}=1
\quad\text{for every }0<\rho<1.
}
\tag{3.2}
\]

The common exact mean is

\[
\mathbb ET_{FCFS}
=m+\frac{\lambda(c^2+5)}{6(1-\rho)}.
\tag{3.3}
\]

## 4. The first nontrivial cell: 9/2 < c <= 6

Now suppose

\[
\frac92<c\le6.
\tag{4.1}
\]

Then

\[
r_0=\frac52,
\qquad
c-2>m,
\qquad
\frac c2\le m.
\tag{4.2}
\]

Thus M-SERPT has rank \(m\) through age 2 and rank \(c-2\) thereafter. Gittins, by contrast, has rank strictly better than the fresh rank throughout \(0<u<2\), jumps to \(c-2>5/2\) at age 2, and its deterministic terminal rank falls back to the fresh threshold \(5/2\) at age

\[
\boxed{u=c-\frac52.}
\tag{4.3}
\]

Hence every long Gittins job has a discarded terminal segment of length

\[
\boxed{c-\frac92}
\tag{4.4}
\]

followed by a recycled high-priority terminal block of the constant length

\[
\boxed{\frac52.}
\tag{4.5}
\]

The discarded length (4.4) is itself a strict monovariant in \(c\); the recycled length (4.5) is invariant.

### 4.1 Exact SOAP work accounting

Put

\[
\beta:=1-\lambda\mathbb E\min\{X,2\}
=1-\frac{5\lambda}{3}>0.
\tag{4.6}
\]

For a short or medium Gittins tagged job, the worst future rank is \(r_0=5/2\). New \(r_0\)-work is zero because a new arrival starts at exactly \(r_0\) and loses the FCFS tie to the tagged job. The 0-old work is \(\min\{X,2\}\), and an old long job has one recycled block of length \(5/2\). Therefore

\[
\mathbb E\min\{X,2\}=\frac53,
\qquad
\mathbb E\min\{X,2\}^2=3,
\tag{4.7}
\]

and

\[
3+\frac13\left(\frac52\right)^2
=\frac{61}{12}.
\tag{4.8}
\]

The SOAP mean-response theorem gives the common waiting term

\[
\boxed{
W_G^{(0)}=\frac{61\lambda}{24\beta}.
}
\tag{4.9}
\]

No new job delays the tagged short or medium job during residence, so

\[
\boxed{
T_G(1)=1+\frac{61\lambda}{24\beta},
\qquad
T_G(2)=2+\frac{61\lambda}{24\beta}.
}
\tag{4.10}
\]

For M-SERPT at the same short/medium threshold, there is no recycled block. Thus

\[
\boxed{
T_{MS}(1)=1+\frac{3\lambda}{2\beta},
\qquad
T_{MS}(2)=2+\frac{3\lambda}{2\beta}.
}
\tag{4.11}
\]

For a tagged long job under either policy, the worst future rank is \(c-2\). A new job contributes exactly \(\min\{X,2\}\) before a possible long job reaches the equal terminal rank, an old job contributes its whole service requirement, and there is no recycled old block at this worst threshold. Hence the common long-job waiting term is

\[
\boxed{
W_\infty
=
\frac{\lambda\mathbb EX^2}{2(1-\rho)\beta}
=
\frac{\lambda(c^2+5)}{6(1-\rho)\beta}.
}
\tag{4.12}
\]

Under Gittins, the long job sees new-work load \(5\lambda/3\) until age \(c-5/2\), then zero new-work load for its final \(5/2\) units. Thus

\[
\boxed{
T_G(c)
=W_\infty+
\frac{c-5/2}{\beta}+\frac52.
}
\tag{4.13}
\]

Under M-SERPT, the long job's worst future rank remains \(c-2\) throughout its service, so

\[
\boxed{
T_{MS}(c)
=W_\infty+rac{c}{\beta}.
}
\tag{4.14}
\]

Subtracting (4.10)--(4.14) gives the exact size-specific charges

\[
\boxed{
T_{MS}(1)-T_G(1)
=T_{MS}(2)-T_G(2)
=-\frac{25\lambda}{24\beta},
}
\tag{4.15}
\]

and

\[
\boxed{
T_{MS}(c)-T_G(c)
=\frac{25\lambda}{6\beta}.
}
\tag{4.16}
\]

Averaging the three equally likely sizes yields the central identity

\[
\boxed{
\mathbb ET_{MS}-\mathbb ET_G
=\frac{25\lambda}{36\beta}
=\frac{25\lambda}{12(3-5\lambda)}.
}
\tag{4.17}
\]

This is an exact finite-load identity over the whole cell (4.1), not a simulation or asymptotic expansion.

### 4.2 Uniform all-load bound on this cell

Equation (4.17) is positive for \(\lambda>0\), so Gittins is strictly better once the terminal demotion exists. But the gap remains small. Because stability gives

\[
\lambda<\frac1m=\frac3{c+3},
\tag{4.18}
\]

and \(\lambda/(1-5\lambda/3)\) is strictly increasing in \(\lambda\),

\[
\mathbb ET_{MS}-\mathbb ET_G
<\frac{25}{12(c-2)}
<\frac56.
\tag{4.19}
\]

Also every response time contains its service requirement, so

\[
\mathbb ET_G\ge\mathbb EX=m>\frac52.
\tag{4.20}
\]

Combining (4.17)--(4.20),

\[
0<
\frac{\mathbb ET_{MS}-\mathbb ET_G}{\mathbb ET_G}
<\frac13.
\tag{4.21}
\]

Therefore:

**Theorem 4.1.** For every equal-probability law on \(\{1,2,c\}\) with \(9/2<c\le6\) and every stable load,

\[
\boxed{
1<\frac{\mathbb ET_{MS}}{\mathbb ET_G}<\frac43<2.
}
\tag{4.22}
\]

Together with Theorem 3.1, the factor-two conjecture is thus verified with substantial slack on the complete equal-probability range

\[
\boxed{2<c\le6.}
\tag{4.23}
\]

This remains a restricted theorem and does not move the frozen universal source metric \(W_{MS}=3\).

## 5. What changes at c>6

For \(c>6\), (1.11) becomes positive and M-SERPT develops an additional demotion already at age 1:

\[
M_0=m<M_1=\frac c2<M_2=c-2.
\tag{5.1}
\]

Gittins still has fresh rank \(5/2\), remains better than fresh work until age 2, then has the same terminal discarded span \([2,c-5/2)\) followed by a final rescued block of length \(5/2\). Thus \(c=6\) is the first equal-probability point at which the genuine multiple-valley interaction from the STUCK1 diagnosis appears.

This identifies a cleaner next target than \(c=3\): solve the complete \(c>6\) equal-probability cell, beginning with the exact instance \(c=7\), where the two M-SERPT demotions and Gittins's terminal recycle coexist.

## 6. Exact self-check

The accompanying exact SymPy checker verifies the algebraic bifurcation identities, the \(c=3\) switch identities, and all SOAP difference factorizations in Section 4. It uses exact rational arithmetic for the identities and terminates with

`ALL_EXACT_CHECKS_PASS`.

Checker:
`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T223700Z__P0434_equal_probability_three_point_exact.py`

Archived executed output:
`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T223700Z__P0434_equal_probability_three_point_exact.out`

This is a self-check, not an independent P26 or OTHER-track audit.

## 7. Status and scope

- The selected STUCK1 special case \(X\sim\mathrm{Unif}\{1,2,3\}\) is completely solved: both policies are FCFS, ratio 1.
- The same FCFS identity holds for all \(2<c\le9/2\).
- For every \(9/2<c\le6\), the exact SOAP identity (4.17) holds and the ratio is strictly below \(4/3\) at every stable load.
- The source conjecture for arbitrary service laws remains OPEN.
- No claim of novelty is made. A bounded fresh literature search on 2026-09-19 UTC recovered the 2020 source and related later scheduling work but no later all-load M/G/1 resolution of Conjecture 8.1; absence from those searches is only negative evidence.
