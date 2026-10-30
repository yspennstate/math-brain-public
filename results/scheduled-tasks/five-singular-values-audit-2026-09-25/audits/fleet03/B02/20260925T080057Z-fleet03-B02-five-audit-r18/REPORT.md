SIGNED IN - auditing the exact fourteen-page five-singular-value proof, account fleet03, slot B02, 2026-09-25T08:00:57Z.

# fleet03/B02 audit r18 — pass 2 final theorem and Fourier anchors

## Pins and status

Objective: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925.

Prepublication control was refreshed on fresh main immediately before these writes. Objective blob: b167cb098b86d7f000e3fdd58efd17bcb2a58715. Corrections blob: 5d46395f49355daa0c540e6d4518c9380decee10. Most recent repository commit observed in that refresh: bcf0b35c6b059b2848d49b24c100d48f11d3b8f5.

Only the immutable original was used:
- yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c
- proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex
- TeX blob c4f2a997cf336ee974e15409b5bccdd8cca039d8
- PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423
- 14 pages.

Execution context: WITHOUT_VERIFIED_BRAIN.

B02 has one complete source-coverage pass. Pass 2 remains in progress. This run independently reconstructed the final proof of Theorem 1.1, source lines 618-639, and then re-audited the original B02 Fourier anchors, lines 80-127, with a second-pass normalization/Tonelli lens.

## 1. Theorem 1.1 final proof, lines 618-639, PDF pages 13-14

### Line 619 normalization — PASS

With K=s=1 the hypothesis s_5(A)>=s becomes s_5(A)>=1, equivalently at least five eigenvalues of the real symmetric A have modulus at least one.

### Line 621 no-pivot branch — PASS, conditional on the previously audited no-pivot dependency chain

Proposition 7.1(a) applies exactly under s_5(A)>=1 and no pivot and supplies a continuous density bounded by <167. No extra hypothesis is added.

### Lines 623-626 scalar-pivot branch — PASS, with upstream local-proof qualifications already recorded

Assume |a_ii|>=eta=1/12. The scalar block [a_ii] is invertible. Completing the square gives
Q=a_ii(X_i-mu(X_-i))^2+R(X_-i),
where the quadratic matrix of R is the scalar Schur complement.

Lemma 2.6 with k=1 and N_A(1)>=5 gives N_R(1)>=4; in particular s_3(R)>=1. The complement coordinates X_-i remain mutually independent with the same density caps.

Conditionally on X_-i, Lemma 5.1 gives
p_{Q|X_-i}(z)<=|a_ii|^{-1/2}|z-R(X_-i)|^{-1/2}.
Lemma 2.4 averages this domination, and Proposition 7.2 applies to R as a quadratic polynomial in the independent complement. Hence for a.e. z,
p_Q(z)<=|a_ii|^{-1/2} E|z-R|^{-1/2}
       <=sqrt(12)*77<267.
The last inequality is exact since 12*77^2=71148<71289=267^2.

The sign of a_ii is irrelevant because Lemma 5.1 allows a nonzero coefficient of either sign. Affine terms are retained in mu and R.

### Lines 628-632 pair-pivot branch and exhaustiveness — PASS, conditional on C01/C03 upstream local repairs

After the no-pivot and scalar-pivot cases, the remaining pivot possibility is exactly: all |a_ii|<eta and some pair has
|a_ii a_jj-a_ij^2|>=zeta=1/256.
Thus the case split is exhaustive.

Condition on the original complement. The pair (X_i,X_j) keeps its original independence and its joint density is at most one. Its quadratic part is the literal principal 2x2 block B=A_{ij,ij}; the conditional linear coefficients may depend on the complement but the matrix B does not.

If B is definite, det B>0 and det B>=zeta. The repaired Lemma 5.2 plus Lemma 2.4 gives
||p_Q||_infinity<=pi/sqrt(det B)<=16 pi<51.
The last inequality follows, for example, from pi<22/7.

If B is indefinite, det B<0 and
D=a_ij^2-a_ii a_jj=|det B|>=zeta.
Writing the split matrix as
A=[[B,C],[C^T,E]]
and the pair linear coefficient as l(x)=2Cx+b_pair, completing the square gives the conditional critical value
v(x)=x^T E x+b_rest^T x+c-(1/4) l(x)^T B^{-1}l(x).
Its quadratic matrix is exactly E-C^T B^{-1}C, the pair Schur complement. Lemma 2.6 with k=2 and N_A(1)>=5 therefore gives at least three eigenvalues of modulus >=1 in that Schur complement. Its operator norm is consequently >=1, so Lemma 5.4 applies and gives, for every real z,
E log_+(1/|z-v|)<=L_0=2+2 log19.

The repaired hyperbola lemma gives the conditional Borel domination
D^{-1/2}[6+log_+(16 sqrt(D)/|z-v|)].
Using
log_+(xy)<=log_+x+log_+y
and Lemma 2.4 yields for a.e. z
p_Q(z)<=D^{-1/2}[6+log_+(16 sqrt D)+L_0].

For every D>0,
log_+(16 sqrt D)<=4 log2+(1/2)log_+D.
Since D>=1/256, D^{-1/2}<=16. Also
sup_{D>0} D^{-1/2} log_+D=2/e:
for D>1 put x=sqrt D, obtaining 2 log x/x, maximized at x=e; for D<=1 the log_+ term is zero. Therefore
p_Q(z)
<=16(8+4 log2+2 log19)+1/e.
The source's own coarse numerical inputs rigorously suffice:
log2<0.6932, log19<3, e>2.7,
so the right side is at most
16(14+4*0.6932)+10/27
=4534906/16875
=268.735170...<269.
Thus the final indefinite branch constant is valid.

The application of Lemma 2.4 is measurable: the critical value v is a quadratic polynomial of the original complement, so the conditional envelope is a measurable nonnegative function. Lemma 5.3's a.e. density domination implies the required Borel domination after integration. No independence after an eigenbasis rotation is used.

### Line 632 branch summary — PASS

The four normalized outcomes are <167, <267, <51, and <269, so an essentially bounded density with norm <269 exists in every case. This does not prove global continuity: only the no-pivot Fourier branch has continuity supplied directly.

### Lines 634-638 scaling — PASS

Any nonvacuous theorem instance has K>0, since a probability density cannot integrate to one while being bounded above by a nonpositive K. With Y=KX,
p_{Y_i}(y)=K^{-1}f_i(y/K)<=1,
and independence is preserved.

Direct substitution gives
Q=(s/K^2) Qtilde,
Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c.
Because s>0,
s_5(A/s)=s_5(A)/s>=1.
The normalized result therefore gives an essentially bounded density p_Qtilde with bound <269. Scaling a one-dimensional density by the positive factor s/K^2 gives
p_Q(z)=(K^2/s)p_Qtilde(K^2 z/s),
hence
||p_Q||_infinity<269 K^2/s<=270 K^2/s.
The arbitrary affine terms have the exact coefficients written in the source.

### Line 638 interval equivalence — PASS

A density bound p_Q<=C a.e. immediately gives P(Q in J)<=C|J|.

Conversely, suppose the interval estimate holds. Every open subset of R is a countable disjoint union of open intervals, so countable additivity gives P(Q in U)<=C|U|. For Borel B, monotonicity and Lebesgue outer regularity give
P(Q in B)<=inf_{U open, B subset U} C|U|=C|B|.
Thus the law is absolutely continuous with respect to Lebesgue measure, and its Radon-Nikodym density is <=C a.e. This justifies the theorem's equivalence statement.

### Final-proof dependency status

The algebra, case split, conditioning, Schur losses, affine terms, constants, measure scaling, and interval equivalence in lines 618-639 all PASS this reconstruction.

The immutable original manuscript as a whole is still not an unqualified PASS because this final proof depends on earlier clauses for which B02 records local literal-source issues C01, C02, C03 and C06. Their repaired mathematical statements have been independently reconstructed in earlier B02 runs. Descriptive C04/C05 and literature-status C07 do not alter the final theorem derivation.

## 2. Pass-2 Fourier anchors, lines 80-127, PDF page 2

### Lemma 2.1(a) — PASS

For the convention fhat(xi)=integral e^{i xi dot x}f(x)dx, Plancherel is
integral |fhat|^2=(2 pi)^d integral |f|^2.
The sign convention does not change the factor.

### Lemma 2.1(b) — PASS

If the characteristic function of the probability measure is in L1, finite-measure Fourier inversion gives the continuous density
p_Z(x)=(2 pi)^{-1} integral e^{-itx} phi_Z(t)dt.
Absolute convergence gives the stated sup-norm bound. This is a genuine continuity conclusion and should not be exported to non-L1 pivot branches.

### Lemma 2.1(c) — PASS

The Gaussian transform
integral e^{itx} e^{-t^2/(4v)}dt
=2 sqrt(pi v)e^{-v x^2}
has the stated normalization. Taking x=Z-a produces the sign e^{-ita} phi_Z(t). Fubini is justified because the absolute integrand before expectation is e^{-t^2/(4v)}, which is integrable for v>0.

### Lemma 2.2 — PASS

The envelope equals 1 for |t|<=a and a^p |t|^{-p} outside. Thus
integral_R min(1,(a/|t|)^p)dt
=2a+2a^p integral_a^infinity t^{-p}dt
=2ap/(p-1).
Lemma 2.1(b) then gives ap/[pi(p-1)] and continuity. The assumption p>1 is exactly the integrability threshold.

### Lemma 2.3 gamma representation and Tonelli — PASS

For z nonzero,
Gamma(1/4)^{-1} integral_0^infinity v^{-3/4}e^{-vz^2}dv=|z|^{-1/2};
for z=0 both sides are +infinity. Hence the first expectation/integral interchange is Tonelli with an extended nonnegative integrand.

After Lemma 2.1(c), taking the modulus gives a nonnegative double integral; Tonelli applies again. For t nonzero, with w=t^2/(4v),
integral_0^infinity v^{-5/4}e^{-t^2/(4v)}dv
=4^{1/4} Gamma(1/4)|t|^{-1/2}.
At t=0 that inner integral is infinite, but this occurs on a Lebesgue-null singleton and does not affect the integrated inequality. Since
4^{1/4}/(2 sqrt pi)=1/sqrt(2 pi),
the coefficient in (2.1) is exact.

Under |phi_Z(t)|<=min(1,u/|t|), splitting at |t|=u gives
2 integral_0^u t^{-1/2}dt
+2u integral_u^infinity t^{-3/2}dt
=4 sqrt u+4 sqrt u=8 sqrt u.
Thus the final half-moment constant is correct.

No new issue was found in lines 80-127 during this second-pass reconstruction.

## 3. Independent comparison after derivation

Only after completing the derivations above, B02 compared with genuinely separate source-pinned reports:
- fleet01/B19 pass 3, blob 24e9067385fb2afeeb42377a0bc924bcb5c09367;
- fleet02/B19 r13, blob 77ac2afc29116d510cb0c3aa2f18a095fe62a1c17c.

Both independently report the same four final normalized branch scales and the K^2/s scaling after local repairs. This agreement was not used as a premise. Previously recorded worker disagreements about line 222 and the completeness of line 148 remain preserved and do not change the new lines 618-639 derivation.

## 4. Current status and next cursor

- Complete B02 full source-coverage passes: 1.
- Pass 2: still in progress.
- Newly rechecked this run: final Theorem 1.1 proof, lines 618-639; Fourier anchors, lines 80-127.
- No new fatal theorem-level defect found.
- Literal original remains locally defective at the already documented C01-C06 clauses and has unverified C07; passing this final proof does not erase those statuses.
- The theorem conclusion remains essential boundedness; continuity is only proved where an L1 Fourier receiver supplies it.

Next pass-2 cursor: Lemma 2.7 / crossing-volume identities and a fresh full reconstruction of Lemmas 3.2-3.3, followed by the remaining introduction/bibliography clauses needed to make pass 2 itself complete.

No schedule, cadence, enabled/paused state, email/push setting, Drive delivery, public release, permissions, paid call, cross-account authentication, remote workflow, or installation was changed.
