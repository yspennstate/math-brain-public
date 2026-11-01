# Exact scoped reconstruction of A097 stage21

Units: bits. Target: A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER@1, statement hash 8e3a5074a89063d0bb52d1a8ac5d9e3743fbbd167e47b159b86e4b760171e170. Verdict: statement HOLDS by reconstruction; two proof-text equalities require correction. The corrections do not change the minimizer, sharp price, or supplied-owner condition. No universal source is supplied.

Let p be finite, p(0)=r, t=1-r>0, a=p(A) in (0,t), and q0 a normalized finite-CE reference with q0(0)=r and b=q0(A) in (0,ell), ell<t. Preserve the q0 conditional profiles on A and C=nonempty\A, including reference-only atoms. The reference q_z has total masses r,z,t-z. For ell<=z<t, expansion on the actual support gives

 F(z)=CE(p,q_z)-CE(p,q0)=a log2(b/z)+(t-a)log2((t-b)/(t-z)).

Finite CE makes every denominator on a positive-p atom positive. Zero-p atoms contribute zero; when r=0 there is no vacuum logarithm to evaluate. Both cells have positive true mass, so z=t has infinite CE and is excluded.

The derivative is F'(z)=[-a/z+(t-a)/(t-z)]/ln2 = t(z-a)/(z(t-z)ln2). A097 stage21 omits the factor t in its displayed derivative. Its stage20 proof includes it. Since t>0, the sign changes only at a. Thus the unique minimum is z*=max(a,ell); strict convexity follows also from F''(z)=[a/z^2+(t-a)/(t-z)^2]/ln2>0. The exact signed price is the displayed F(z*). Equivalently it is t times the difference of Bernoulli KLs to z*/t and b/t. A mandatory increase in q(A) need not cost positively: it may release already paid mismatch. The upper bound using z=ell and ln(1+x)<=x is valid but is not a necessary price.

If a full terminal law/reference have identical disjoint controller part and seed weight beta, atomwise log ratios cancel the controller and beta, leaving exactly beta F(z*). For reaches rho_h of ALL physical terminal outcomes, the total signed change is S=sum_h rho_h beta_h F_h(z*_h). With current full cost C, original capacity B, and old bills U, new cost is C+S. Therefore the exact residual is B-(C+S)-U=(B-C-U)-S. This is payable iff S<=B-C-U. Dropping negative terms is merely a sufficient conservative test. Each release occurs once. Neither this identity nor convex optimality constructs B<=K I(core).

# Second proof-text correction: inherited physical queries

A097 stage21 says 'CE increment=-D_occ'. Literally that equality omits erasure B_j. Let P(T,i) be the parent spectral law, Q(T,i) the current full reference and Qbar(T)=sum_i Q(T,i). An actual physical restriction has average child spectral law Pbar(T)=sum_i P(T,i), by ((u+v)^2+(u-v)^2)/2=u^2+v^2. Every child uses Qbar, so its average CE is CE(Pbar,Qbar). The chain rule gives

 CE(P,Q)=CE(Pbar,Qbar)+H_P(i|T)+sum_T Pbar(T)D_2(P(i|T)||Q(i|T)).

Consequently B_j+average CEchild-CEparent=-D_occ<=0, where B_j=H_P(i|T). This is the correct full-query identity already printed in A097 stage20. The weaker CE-only monotonicity survives, but the CE-only equality to -D_occ does not. Do not count -B_j as a release and separately erase its already charged cost.

Actual control: AND2 in sign convention, table (-1,1,1,1), has parent spectral law uniform on four atoms. Take Q=P, so CEparent=2. The inherited one-bit Qbar is uniform on two labels; both actual physical children have CE=1 against Qbar (their actual spectra are point masses). Hence mean CEchild-CEparent=-1, B_j=1, and D_occ=0. All normalizations and both children satisfy the hypotheses. This refutes the literal CE-only equality, not the source theorem or FEI.

# Signed Boolean endpoints

For g=-1 at the two all-equal three-bit inputs and +1 elsewhere, g=(1-y1y2-y1y3-y2y3)/2. The parent spectrum is uniform on empty and three pairs. After querying y1 both child spectra are uniform on four exterior labels. For A={23}, a=r=1/4, t=3/4, ell=1/3, matched q0 gives F=(1/4)log2(27/25)>0. Incoming q0=(1/4,5/16,5/16,1/8) gives F=(1/4)log2(27/32)<0. Both reach the same final reference (1/4,5/24,5/24,1/3). With beta=3/8 the full changes are (3/32) times the same logarithms. Signs are exact rational comparisons, not floating-point estimates.

# Rung and remaining gap

Rung: analytic proof reconstruction plus exact finite rational certificates; not Lean-checked. memok returned WAIT/exit1, physical free3.1GB versus required4GB, so the formal run was not admitted. No mathematical exception is inferred from this hold. A085/A094 should independently check the corrected proof wording; A093 supplies the local errata and does not claim to be a separate independent acceptor of an amended version. The original theorem statement is unchanged.

First unsupported universal line: construct an actually useful arbitrary-core original source with capacity O(I(core)) and enough unused margin for a required compatible admission/stopping rule. The profile restriction is an explicit hypothesis; no algorithmic necessity follows merely by declaring it. No dimension-independent FEI bound follows from a supplied bank alone.
