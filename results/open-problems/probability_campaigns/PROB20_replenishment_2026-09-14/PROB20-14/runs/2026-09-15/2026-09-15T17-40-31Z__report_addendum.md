# PROB20-14 — correction addendum to 2026-09-15T17:40:30Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

This append-only addendum corrects Section 9 and the corresponding all-level ledger bullet of the immediately preceding report. The new root results in Sections 3–8 are unchanged.

## 1. Issue found in self-review

Section 9 reused the statement that, outside a conditioned-negligible event, a sublinear boundary width \(L=Z_k\) satisfies
\[
N=1+Z_1+\cdots+Z_{k-1}\le C_k(1+L).
\]
The earlier factor-two downward-jump argument does show that **if** \(N>C_k(1+L)\), then some transition \(Z_i\to Z_{i+1}\) makes a factor-two downward jump starting from a population of order \(N\). Its ordinary Galton–Watson probability is therefore exponentially small in \(N\). However, after division by the size-conditioning denominator \(a_n=e^{-\lambda_n}\), this only makes the event conditioned-negligible when \(N\) is sufficiently larger than \(\lambda_n\); it does not justify discarding all prefixes with \(N>C_k(1+L)\) uniformly when \(N\) is smaller.

Accordingly, Theorem 9.1 as stated in the preceding report is **retracted in that form**. It is replaced by the corrected statement below.

## 2. Correct stopping-length reduction

For fixed \(k\), if
\[
N>C_k(1+L),
\]
then there are constants \(c_k,c'_k>0\) and some \(i<k\) such that
\[
Z_i\ge c_kN,
\qquad
Z_{i+1}\le Z_i/2.
\]
Critical nondegeneracy gives a fixed negative exponential tilt, hence
\[
\Pr(Z_{i+1}\le Z_i/2\mid Z_i=z)\le e^{-c'_kz}.
\]
A union bound over the finitely many generations yields
\[
\Pr_{\rm GW}(N>C_k(1+L),\ N\ge u)\le C_ke^{-c_ku}.
\tag{A.1}
\]
For every completable prefix, the exact prefix density satisfies the crude bound
\[
W_n\le \frac n{a_n}=ne^{\lambda_n},
\]
and \(L^r\le n^r\). Thus
\[
\mathbb E[\ell_k(T_n)^r;\ N>C_k(1+L),\ N\ge u]
\le
C_kn^{r+1}e^{\lambda_n-c_ku}.
\tag{A.2}
\]
Choose
\[
u_n:=A_k(\lambda_n+\log n+1)
\tag{A.3}
\]
with \(A_k\) sufficiently large. Then the right-hand side of (A.2) tends to zero. Therefore, outside a contribution negligible for the target fractional moment,
\[
\boxed{
N\le C_k(1+L)+u_n.
}
\tag{A.4}
\]
The already established small-remainder estimate still separately removes \(n-N<\delta_kn\).

## 3. Corrected all-level entropy theorem

Let \(B_n\to\infty\), and put
\[
M_n:=C_k(1+B_n)+u_n.
\]
On the non-negligible region with \(L\le B_n\), the first-\(k\)-level prefix is measurable from the first \(M_n\) allocation coordinates. The exact prefix representation and block entropy bound then give, exactly as in Section 9 of the report,
\[
\mathbb E[\ell_k(T_n)^r;K<\ell_k(T_n)\le B_n]
\le
C_k\mathbb E_{\pi^{\otimes M_n}}[Z_k^q;Z_k>K]
+o_K(1)+\mathcal E_n,
\]
where the entropy-Bernstein error satisfies
\[
\boxed{
\mathcal E_n
\le
C_k\left[
B_n^{q/2}\sqrt{\frac{M_n\lambda_n}{n}}
+B_n^q\frac{M_n\lambda_n}{n}
\right].
}
\tag{A.5}
\]
Hence the valid sufficient condition is
\[
\boxed{
B_n^q\,
(B_n+\lambda_n+\log n+1)
\frac{\lambda_n+1}{n}
\longrightarrow0.
}
\tag{A.6}
\]
Under (A.6),
\[
\boxed{
\lim_{K\to\infty}\limsup_n
\mathbb E[\ell_k(T_n)^r;
K<\ell_k(T_n)\le B_n]=0
}
\tag{A.7}
\]
for every fixed \(k\).

This is weaker than condition (9.8) in the preceding report because the stopping length may contain an additional \(O(\lambda_n+\log n)\) term.

## 4. Universal consequence of the corrected theorem

Recall
\[
\lambda_n=o(n^\beta),
\qquad
\beta=\frac{1-r}{1+r}.
\]
For \(r>1/3\), (A.6) gives an explicit polynomial every-level window
\[
B_n=n^\gamma
\]
for every
\[
\boxed{
\gamma<
\min\left\{
\frac{2r}{(1+r)(2+r)},
\frac{3r-1}{(1+r)^2}
\right\}.
}
\tag{A.8}
\]
At \(r=1/3\), the little-o bound \(\lambda_n=o(n^{1/2})\) still gives a sufficiently slowly diverging \(B_n\), but no fixed positive polynomial exponent follows from this estimate alone. For \(0<r<1/3\), the present denominator bound does not guarantee that (A.6) admits a diverging universal deterministic cutoff; the earlier fixed-shift diagonalization still supplies a non-explicit diverging root window, but this entropy argument does not produce a universal growing all-level scale in that subrange.

Thus the preceding report's claim of the exponent
\[
2r/((1+r)(2+r))
\]
for **all** \(0<r<1\) is withdrawn.

## 5. Unchanged new results

The following results from the preceding report are unaffected by this correction:

- renewal localization \(\sum_{|s-d|\le\varepsilon d}\Pr(S_s=d)\to h\);
- the exact Palm identity \(N_0=d+\sum_{i=1}^{n-1}(\xi_i-1)_+\);
- the complementary large-shift local-ratio bound
  \[
  R_{n,d}\le C+\exp\{\lambda_n-cd^{q/(q-1)}n^{-1/(q-1)}\};
  \]
- the entropy–truncated-variance one-coordinate estimate;
- root UI for every cutoff \(B_n\) with \(B_n^q(\lambda_n+1)/n\to0\), and hence for every fixed
  \[
  \gamma<\frac{2r}{(1+r)^2};
  \]
- confinement of any root failure to the self-normalized middle window around the natural \(n^{1/q}\) scale.

## 6. Verification status

This correction was produced by an adversarial self-review of the stopping-prefix step after the main report had already been committed. It narrows, rather than strengthens, the all-level claim. The corrected argument uses only the previously established exact prefix density, the fixed negative-tilt bound for a factor-two Galton–Watson downward jump, and the block relative-entropy estimate. It remains author-side checking, not independent/formal verification.
