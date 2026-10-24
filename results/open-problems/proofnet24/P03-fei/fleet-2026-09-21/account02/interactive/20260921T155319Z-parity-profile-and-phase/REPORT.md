# FEI: a sharp compositional class, quadratic-phase compression, and an obstruction to sign-free profiles

Date: 21 September 2026. Interactive research continuation, account02; not a scheduled B-slot.

**Full uniform-cube FEI remains OPEN / NOT PROVED by this work.** Results below are new derivations in this invocation, not claims of publication priority. The analytic arguments and executed finite checks are self-checks; independent end-to-end review has not occurred. The sharp constant-four formula theorem uses an exhaustive integer finite gate check as well as an analytic composition proof.

MODEL: GPT-6 Astra Pro, self-report. Configured reasoning level and provider thinking counters: NOT_EXPOSED. Execution label: WITHOUT_VERIFIED_BRAIN. Authenticated GitHub source retrieval was used; native `math_brain`, `brain`, and `spread_recall` were unavailable. Repository delivery is not production-database ingestion or proof that another worker has consumed this result.

## 1. Target, starting frontier, and changes made

Work on the uniform cube, identified with F_2^n. For a Boolean function f taking values in {-1,1}, write

    a_s = 2^{-n} sum_x f(x)(-1)^{s.x},
    mu(s) = a_s^2,
    H(f) = sum_s mu(s) log_2(1/mu(s)),
    I(f) = sum_s |s| mu(s),
    o(f) = Pr_{s~mu}(|s| is odd).

Zero entropy terms are zero. Full FEI asks for H(f) <= C I(f) for every such f with one dimension-independent C.

The recovered frontier used here comprises three specific arguments:

* account01/B13, `fleet-2026-09-21/account01/B13/B13-20260921T1518Z-block-hypercontractive/REPORT.md`, blob `fd2e63db765dab8dcb5365fe2978cd7d1b73c1d9`: every spectral parity cell satisfies all-centre Laplace and dispersion inequalities, but a summable recursive use was missing.
* account02/B18, `fleet-2026-09-21/account02/B18/20260921T133721Z-han-credit-block-descent/REPORT.md`, blob `ea7b8e3d3ed9ac818a73c3552d400a0cae55ff7e`: exact restriction descent retains the negative Han credit; universally summable Bayes-Han tolls were missing.
* account02/B18, `fleet-2026-09-21/account02/B18/20260921T103159Z-product-phase-kl-stability/REPORT.md`: Fourier signs and all-shift orthogonality give stability, but the available Hellinger-scale payment does not supply the required KL-scale bound.

Paths in this list are relative to `proofnet24/P03-fei/`. These reports were recovered from scientific master at `029e091cde1e37bd86d24b3935426ab1a50b7b6a`; fresh searches also encountered `4f2cf7dfa5e248a7b30ac2ee75c5a07244c93453`. The read-once AND/OR certificate is preserved unchanged, not rerun or claimed as this run's result.

The changes are:

1. An analytic infinite-family obstruction: the entire recorded parity-profile relaxation, together with the spectral Bayes-Han necessary inequalities, admits non-Boolean laws with unbounded entropy per expected set size. The problem is not just that a few small cases were untested.
2. A sign-sensitive compression theorem and its quantitative extension: quadratic Fourier phase of polar rank r forces an entropy-preserving genuine Boolean compression to r variables; approximate agreement gives a universal entropy bound with an explicit Fourier-l1 error payment.
3. A complete sharp constant-four theorem for an unbounded compositional class: read-once formulas built from quadratic-phase gates of at most four inputs, with every non-root gate odd, satisfy H <= 4(I-o) <= 4I. Recursive ternary majority shows the constant four cannot be reduced for this class.

The full quadratic-phase class and unrestricted FEI remain unresolved. No universal step is obtained by dropping the gate, phase, or oddness hypotheses.

## 2. Parity conditioning changes a product mean by at most one

### Lemma 2.1 — exact parity mean-shift inequality

Let Z_i be independent Bernoulli variables with arbitrary parameters theta_i in [0,1]. For a nonempty J let Y=(-1)^{sum_{i in J} Z_i}, and let Pr(Y=y)=r>0. For K=sum_i Z_i,

    | E[K | Y=y] - E K | <= 1-r.                         (2.1)

More generally, for real weights w_i the right side becomes max_{i in J}|w_i| (1-r). This asserts a mean bound, not an unproved coupling or Wasserstein statement.

Proof. Set c_i=1-2 theta_i and C=prod_{i in J} c_i, so r=(1+yC)/2. Independence outside J gives no change in its means. Direct expansion inside J gives

    E[K | Y=y]-EK
      = - y/[2(1+yC)] sum_{i in J}(1-c_i^2) prod_{j in J, j != i} c_j.  (2.2)

For x_i in [0,1] the elementary tensor inequality is

    sum_i (1-x_i^2) prod_{j != i} x_j <= 1-(prod_i x_i)^2.             (2.3)

It follows by induction from the two-factor identity

    1-a^2 b^2 - b(1-a^2) - a(1-b^2) = (1-a)(1-b)(1-ab) >= 0.

Apply (2.3) to |c_i| in (2.2). The absolute difference is at most

    (1-C^2)/[2(1+yC)] = (1-yC)/2 = 1-r.

For weighted sums take max |w_i| before the same estimate. Polynomial expressions handle zero c_i; events of probability zero are excluded. QED.

## 3. The full sign-free parity-profile relaxation does not imply FEI

For a law nu on subsets write I_nu=E_nu|X|. This notation is a spectral first moment; nu below is not the spectrum of a Boolean function.

### Theorem 3.1 — all centres, all parities, and the entire noise interval

Let 0<alpha<=1/4, Q=Bernoulli(alpha)^{tensor n}, and suppose

    n alpha >= (8/3) ln(1/alpha).                         (3.1)

For every nonempty J, either parity event Y_J=y, every Hamming centre T, and every s in [0,1], with r=Q(Y_J=y),

    E_Q[s^{|X triangle T|} | Y_J=y] <= r^{(1-s)/(1+s)}.    (3.2)

Proof. Write L_alpha=ln(1/alpha), I_Q=n alpha, and K=|X triangle T|. Its independent Bernoulli summands have parameters alpha or 1-alpha. Since c=1-2alpha is nonnegative and J is nonempty, r=(1+y c^{|J|})/2 >= alpha.

First take 0<=s<=1/2. Discarding the conditioning event in the numerator, and using the larger one-bit Laplace factor, gives

    E[s^K | Y_J=y] <= alpha^{-1}(1-alpha+alpha s)^n
                   <= exp(L_alpha-I_Q(1-s)).             (3.3)

The last expression is at most alpha^{(1-s)/(1+s)} whenever

    I_Q >= 2 L_alpha/(1-s^2).

On this half interval that requirement is implied by (3.1). Since r>=alpha, (3.2) follows.

Now take 1/2<=s<=1 and tilt the independent disagreement bits by s^K. A summand with original parameter theta has tilted parameter theta s/(1-theta+theta s) >= alpha s. The original event becomes a parity event of these disagreement bits, with a fixed possible sign flip. Lemma 2.1 applies to that tilted product law. With L(s)=E[s^K | Y_J=y], logarithmic differentiation gives

    (ln L)'(s) = E_s[K | Y_J=y]/s
               >= (I_Q s-1)/s >= I_Q-2.

Since L(1)=1, integration from s to 1 yields

    L(s) <= exp(-(I_Q-2)(1-s)).                          (3.4)

Here L_alpha>=ln4>1 and (3.1) imply I_Q-2 >= (2/3)L_alpha >= L_alpha/(1+s). Thus (3.4) is at most alpha^{(1-s)/(1+s)}, hence at most r^{(1-s)/(1+s)}. Endpoint s=1 is equality; s=0 is included in the first argument, with 0^0=1 for K=0. QED.

### Corollary 3.2 — explicit unbounded-ratio family

For every integer m>=2 put

    alpha_m=2^{-m},    n_m=2m 2^m,    Q_m=Bernoulli(alpha_m)^{tensor n_m}.

Then I_{Q_m}=2m and (3.1) holds because ln2<3/4. Consequently every Q_m satisfies (3.2) for every J,y,T,s. It also satisfies the stronger recorded first-moment inequality

    E[|X triangle T| | Y_J=y] >= (1/2) log_2(1/r).        (3.5)

Indeed E|X triangle T|>=2m, Lemma 2.1 lowers the conditional mean by at most one, and r>=2^{-m}, so

    E[|X triangle T| | Y_J=y] >= 2m-1 >= m/2 >= (1/2)log_2(1/r).

But

    H(Q_m)/I_{Q_m} = h_2(2^{-m})/2^{-m} > m -> infinity.  (3.6)

Thus all of the predecessor's Laplace, atom, small-ball, all-centre dispersion and their weighted two-parity consequences hold on an infinite family that violates every proposed universal entropy/first-moment constant.

For example the ratios computed from the exact closed formula are approximately 7.431365 at m=6, 11.441990 at m=10, and 21.442694 at m=20. These are evaluations of the analytic family, not enumerations of 768-, 20,480-, or 41,943,040-bit truth tables.

### Compatibility with the spectral Bayes-Han necessary conditions

For Q_m, let h_q be average q-coordinate marginal entropy and epsilon_q the average one-bit Bayes minority probability after seeing q other coordinates. Then exactly

    h_q=q h_2(alpha_m),
    A_q=h_q-(q/n_m)H(Q_m)=0,
    epsilon_q=alpha_m.

Both total correlation and dual total correlation vanish. In particular

    0<=A_q <= (2/ln2)(n_m-q)epsilon_q

and the predecessor's entropy-profile consequence hold at every q. For every block A,

    H(X_A | X_{A^c}) / sum_{i in A}Pr(i in X) = h_2(alpha_m)/alpha_m > m.

The erasure-heavy spectral inequalities are therefore compatible too.

This is precisely a refutation of sufficiency of the combined SIGN-FREE NECESSARY INEQUALITIES. It does not supply the signed recombination terms R_A, a realizable physical restriction tree, or all-shift Boolean autocorrelation. The B13 and B18 theorems remain valid. A proof using more of their genuine Boolean structure is not refuted.

### Why these are rigorously not Boolean spectra

Every normalized Walsh coefficient of a Boolean function is rational. In a full-support product spectrum Q_m adjacent squared coefficients would have ratio

    alpha_m/(1-alpha_m)=1/(2^m-1).

Their absolute coefficient ratio would therefore be 1/sqrt(2^m-1), which is irrational: for m>=2 the integer 2^m-1 is 3 modulo 4 and cannot be a square. This contradiction excludes Q_m from Boolean spectra. No counterexample to FEI is claimed.

## 4. Use the signs: quadratic-phase compression

A quadratic phase completion means a degree-at-most-two polynomial Q:F_2^n->F_2 such that

    a_s=(-1)^{Q(s)} |a_s|                              (4.1)

at every nonzero coefficient. Values of Q at zero coefficients are unrestricted. Its polar form is

    B(s,u)=Q(s+u)+Q(s)+Q(u)+Q(0).

Let r be the rank of this alternating bilinear form and R its radical. The rank r is even.

### Theorem 4.1 — genuine Boolean compression preserving the whole spectrum

Under (4.1), the Fourier support meets each coset of R in at most one point. If L:F_2^n->F_2^r is any surjection with kernel R, then

    g(y)=f(L^T y)

is Boolean and has exactly the same nonzero Fourier coefficients as f, only relabelled. Consequently

    H(g)=H(f),    |supp fhat|<=2^r,    H(f)<=r.          (4.2)

Proof. Booleanity f^2=1 is equivalent to

    sum_s a_s a_{s+u} = 1_{u=0}.                       (4.3)

For nonzero u in R, the sign Q(s)+Q(s+u)=Q(u)+Q(0) is independent of s. All nonzero summands in (4.3) therefore have the same sign, so each must vanish. Two support points cannot differ by nonzero u in R. This proves coset injectivity.

Expansion of f(L^T y) gives

    ghat(t)=sum_{Ls=t}a_s.

By injectivity each sum contains at most one nonzero coefficient. This proves all assertions, including actual Boolean realizability, without manufacturing a probability law on the quotient. QED.

The compression preserves entropy but NOT ordinary influence:

    I(g)=sum_s |Ls| a_s^2,    I(f)=sum_s |s| a_s^2.       (4.4)

For example f(x)=(-1)^{x_1}, Q(s)=s_1 s_2, and L with rows (1,1),(1,0) satisfy all hypotheses. Then g(y)=(-1)^{y_1+y_2}, so I increases from one to two. This example is degenerate in entropy but decisively forbids claiming influence preservation. No universal influence comparison is supplied by (4.2).

### Corollary 4.2 — polar rank at most two, sharp constant two

If f has a completion with polar rank r<=2, then H(f)<=2 I(f), in every ambient dimension.

Proof. Rank zero gives a single coefficient, hence H=0. For rank two, the compressed function is on two bits. Of the sixteen two-bit Boolean functions, eight are signed characters; the other eight have all four Fourier coefficients of magnitude 1/2. This classification follows directly by considering whether the number of negative values is even or odd: a two-point subset of F_2^2 is an affine line.

Thus the only nontrivial original spectrum consists of four coefficients of magnitude 1/2. Their support must be an affine two-plane. Indeed a pair difference u must have another pair with the same difference in (4.3); otherwise the unique pair contributes twice a nonzero product. The four support points therefore sum to zero. A uniform affine two-plane has at least two nonconstant coordinate marginals, each equal to 1/2, giving I>=1. Since H=2, the result follows. A two-bit AND truth table attains equality. QED.

## 5. A universal quantitative extension, with its exact remaining payment

For an arbitrary Boolean f and an arbitrary quadratic template Q of polar rank r, define its phase-disagreement Fourier-l1 mass by

    Lambda_Q(f)=sum_{s:a_s != 0, sgn(a_s) != (-1)^{Q(s)}} |a_s|.

### Theorem 5.1 — approximate-phase entropy bound

For every such f,Q,

    H(f) <= r + 2 log_2(1+2 Lambda_Q(f)).                (5.1)

There is also a sharper conditional-entropy version. Let L have kernel equal to the radical R. In each fibre Ls=t let G_t and B_t be the sums of |a_s| over phase-agreeing and phase-disagreeing coefficients respectively, and m_t=sum_{Ls=t}a_s^2. Then

    H_mu(S | LS)
       <= log_2 sum_t(G_t+B_t)^2
        = log_2(1+4 sum_t G_t B_t)
       <= 2 log_2(1+2 sqrt(sum_t B_t^2))
       <= 2 log_2(1+2 Lambda_Q(f)).                     (5.2)

Proof. The restriction u -> Q(u)+Q(0) is linear on R. Choose x_0 extending this functional, so x_0.u=Q(u)+Q(0) on R. Within a fibre, (-1)^{Q(s)+x_0.s} is constant. Hence the genuine Boolean function g(y)=f(x_0+L^T y) has coefficients

    ghat(t)=sum_{Ls=t}a_s(-1)^{x_0.s}= +/- (G_t-B_t).

Parseval gives sum_t(G_t-B_t)^2=1. Therefore

    sum_t(G_t+B_t)^2=1+4 sum_t G_t B_t,
    ||G+B||_2 <= ||G-B||_2+2||B||_2 = 1+2||B||_2.       (5.3)

On a fibre of positive mass m_t, Shannon entropy is at most the order-one-half Renyi entropy:

    H(S | LS=t) <= 2 log_2[(G_t+B_t)/sqrt(m_t)].

For completeness this is Jensen applied to E log(1/sqrt(p)) <= log E(1/sqrt(p)) for its conditional probability p. Average with weights m_t, apply Jensen again, and use (5.3) to obtain (5.2). Finally H(LS)<=r proves (5.1). QED.

At rank zero, this includes the familiar spectral-l1 entropy argument; that underlying inequality is not claimed as new. The useful refinement is localization to phase errors in the radical fibres and the authentic Boolean quotient. A sufficient new route to full FEI would be to construct, for every f, a quadratic template with

    r(Q)+2 log_2(1+2 Lambda_Q(f)) <= C I(f).

No such construction or uniform bound is proved here. Rank alone can be much too large, and Fourier-l1 error must not be replaced without proof by the bounded Hellinger distance from the earlier continuation.

## 6. Transfer the exact small-gate computation to formulas of arbitrary size

### Finite gate lemma 6.1 — exhaustive INTEGER certificate

Every Boolean G on at most four variables with a quadratic Fourier phase completion satisfies

    H(G) <= 4(I(G)-o(G)).                               (6.1)

This is a computer-assisted finite lemma. `verify_fei_advance.py`, function `phase_check`, enumerates every truth table and every quadratic completion, including possible signs at zero coefficients. It verifies all 43,414 qualifying functions across dimensions zero through four.

The entropy inequality is checked with integer arithmetic, not a tolerance on logarithms. For N=2^k and unnormalized integer Walsh coefficients W_s=N Ghat(s), put

    D=sum_s W_s^2 (|s|-1_{|s| odd}),
    A=2k N^2-4D.

Then (6.1) is exactly equivalent to

    prod_{s:W_s != 0} (W_s^2)^{W_s^2} >= 2^A.           (6.2)

For A<=0 this is automatic. Otherwise Python arbitrary-precision integers perform the comparison. Repeated amplitude-histogram/exponent pairs reduce these verifications to 32 distinct integer comparisons. Phase compatibility, support injection and Boolean quotient checks are also integer-exact. Floating ratio maxima are separately labelled diagnostics.

At dimension four: 43,264 of 65,536 functions qualify; minimum polar-rank counts are 32 of rank zero, 1,120 of rank two, and 42,112 of rank four. The other 22,272 do not qualify. Every truth table is tested; these are not random samples or just affine representatives.

### Theorem 6.2 — a sharp constant-four compositional class

Consider a read-once formula on independent uniform bits. Every gate has at most four inputs and a quadratic Fourier phase completion. Every non-root gate is odd, meaning G(-x)=-G(x); the root need not be odd. Then the computed Boolean function F satisfies

    H(F) <= 4(I(F)-o(F)) <= 4 I(F).                     (6.3)

The constant four in the second inequality is optimal for this class.

Proof. Leaves are odd, with H=0,I=1,o=1. Inductively every non-root subformula is odd and therefore balanced. Let F=G(f_1,...,f_k), where the children depend on disjoint leaf sets and are odd. Disjointness and zero child means ensure no Fourier collisions: an outer spectral set U selects exactly the nonempty child spectral sets in blocks i in U. Consequently the entropy chain rule and the first moment give the exact identities

    H(F)=H(G)+sum_i Inf_i(G) H(f_i),
    I(F)=sum_i Inf_i(G) I(f_i).                         (6.4)

Every nonzero child spectral set has odd size, so o(F)=o(G). Apply (6.1) to the gate and the inductive inequality H(f_i)<=4(I(f_i)-1) to the odd children. The terms 4 I(G) cancel:

    H(F) <= 4(I(G)-o(G)) + 4 sum_i Inf_i(G)(I(f_i)-1)
          = 4(I(F)-o(F)).

This proves (6.3) at arbitrary depth and size.

The entire formula also retains a quadratic Fourier phase completion. Replace each child template Q_i by Q_i+Q_i(0), absorbing Q_i(0) into a linear outer phase. Nonemptiness of a selected child spectral set equals its parity, a linear form in the child support coordinates. Substituting these block parities in the outer quadratic phase and adding the child quadratic phases gives a quadratic global completion. This closure observation does not assert that every quadratic-phase Boolean function has such a formula.

For sharpness, let F_0=x_1 and recursively compose disjoint copies through M(x,y,z)=(x+y+z-xyz)/2. This gate is odd and has quadratic phase Q(s)=sum_{i<j}s_i s_j. Its H is two and its I is 3/2. Thus

    I(F_j)=(3/2)^j,
    H(F_j)=4((3/2)^j-1),
    H(F_j)/I(F_j)=4(1-(2/3)^j) -> 4.                    (6.5)

The recurrence follows immediately from (6.4), with initial H=0,I=1. All nonzero support sets stay odd and their signs are (-1)^{(|s|-1)/2}; the two-level nine-bit instance was independently materialized in the checker, giving support size 76, H=5 and I=9/4 exactly. This is an exact infinite-family proof, not extrapolation from that check. QED.

This theorem uses the standard balanced-disjoint composition mechanism. Such composition methods and recursive-majority examples have prior literature; no priority claim is made for those mechanisms or this sharp class without further comparison. The result does not improve the recorded AND/OR theorem on its different class. General AND/OR internal gates are not odd and cannot be inserted into (6.3).

### Research hypothesis, not a theorem

The stronger unrestricted-in-dimension quadratic-phase statement

    H(f) <= 4(I(f)-o(f))                                (6.6)

is a concrete candidate. It is proved above for rank at most two in its ordinary FEI form and for the formula class in (6.3), and verified exactly for all qualifying truth tables through dimension four. It is NOT proved for all quadratic-phase functions. Even proving it would still leave full FEI open because a general Fourier sign function need not have a quadratic completion.

An additional seeded exploratory search tested 10,000 uniform five-bit truth tables and found 40 with a quadratic completion; all 40 passed the exact version of (6.6). Samples of 5,000 six-bit and 1,000 seven-bit truth tables found no compatible functions, so they provide no further evidence for (6.6). The sampler and actual output are included; random search absence is not closure.

## 7. Verification, failed routes, and what remains

The main checker was run as

    python verify_fei_advance.py --part all --output verification.json

using Python 3.13.5 and NumPy, with no external model calls or remote compute. Separate part runs also executed. The delivered output records:

* 2,868 exact rational direct parity-mean checks and 5,460 exact scalar tensor checks.
* 32,368 exact rational Laplace checks on the m=2,n=16 family member, exhausting all J,T symmetry types at 17 rational noise values; 1,860 independent direct-enumeration checks of the symmetry formula.
* 43,414 exact Boolean compressions and exact corrected-entropy comparisons for every quadratic-compatible gate through four variables, with 32 distinct integer entropy comparisons.
* 1,536 seeded exact quotient/phase-error norm checks through six variables. Their conditional-entropy comparisons are floating diagnostics, with maximum excess 8.89e-16; the analytic proof supplies the bound.
* Exact nine-bit recursive majority and the influence-increase counterexample.

All report PASS. The finite noise grid does not prove the continuum statement; Section 3 does. Integer finite gate checking is a legitimate finite premise of Theorem 6.2 but is not an independent audit or a proof-assistant formalization. Cross-dimensional counts overlap through dummy variables and are not independent scientific replications.

Failed or insufficient routes retained explicitly:

1. All of the recovered sign-free parity-profile constraints plus spectral Bayes-Han inequalities do not force a dimension-independent entropy ratio: Corollary 3.2 supplies a full analytic counterfamily.
2. An entropy-preserving quotient does not automatically control influence: (4.4) and the explicit one-to-two example prohibit that inference.
3. A rank bound H<=r alone is insufficient when phase rank is large relative to influence. The error term in (5.1) is not shown to have a universal influence budget.
4. The finite gate lemma cannot be extended to arbitrary dimension merely because every tested case passed. Non-odd or shared-variable compositions do not satisfy the proof of (6.3).
5. Earlier Hellinger-scale separation from a product law cannot silently pay the present Fourier-l1 or KL-scale terms. No such comparison was proved.

The most useful next research targets are to prove or refute (6.6) beyond the composition class, or find a universally controlled phase/fibre decomposition using (5.2). For the existing Bayes-Han route, any proposed summability proof must use genuine signed Boolean compatibility or jointly realizable restrictions, not only the profile inequalities ruled out by Section 3. These are mathematical obligations, not a request to consume more runs on unchanged reporting.

## 8. Primary-literature comparison and claim ledger

Current primary sources checked during this continuation include:

* O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347. Composition is prior methodology, not invented here.
* Hod, *Improved lower bounds for the Fourier entropy/influence conjecture via lexicographic functions*, arXiv:1711.00762. The general constant cannot be identified with this run's restricted constant four.
* Gonzalez, MacManus and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, including its June 2026 HTML version. Restriction-based reasoning retains a missing universal payment; it is not an unconditional full proof imported here.
* Potapov, *On the Fourier Entropy Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563, 18 September 2026. The plateaued constant-four result is a distinct restricted result; the rank-two case here is not claimed as a new discovery of plateaued FEI.
* Chakraborty et al., *Fourier Entropy-Influence Conjecture for Random Linear Threshold Functions*, arXiv:1903.11635. This does not justify silently replacing a sign-phase hypothesis by arbitrary threshold structure.

Repository keyword checks included `Bayes-Han` and `parity product Laplace`; public searches included quadratic Fourier signs, alternating Fourier signs and FEI composition. These checks were bounded, not exhaustive priority clearance. All theorem-sized new claims above include their argument or the exact finite computation they use. No full external theorem body is assumed for Sections 2-5; the composition identities in Section 6 are derived directly.

Ledger:

    PROVED_ANALYTIC_SELF_CHECKED:
      parity mean shift (2.1);
      all-scale product-profile obstruction (3.2)-(3.6);
      exact quadratic-phase Boolean compression (4.2);
      rank-at-most-two FEI with sharp coefficient two;
      universal phase-error entropy bound (5.1)-(5.2).

    PROVED_WITH_FINITE_INTEGER_GATE_CHECK_SELF_CHECKED:
      sharp coefficient-four formula theorem (6.3), with exact hypotheses.

    VERIFIED_FINITE_ONLY:
      corrected inequality (6.1) through four variables;
      forty sampled compatible five-bit cases.

    CONJECTURAL:
      corrected inequality (6.6) for all quadratic-phase Boolean functions.

    REFUTED_RELAXATION_NOT_FEI:
      sufficiency of the combined sign-free necessary profile constraints;
      automatic influence preservation in the quotient.

    OPEN:
      dimension-independent phase-error or signed restriction payment;
      unrestricted quadratic-phase inequality;
      full uniform-cube FEI.

No scheduler assignments, permissions, historical proofs, benchmark answers or production verification statuses were changed. This private package is research input for the shared brain, with mathematical promotion pending independent review.
