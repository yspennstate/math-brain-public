# Conditional flag paid from half an actual common-reference bank

All cubes are finite uniform Boolean cubes; entropy and complete reference cost are bits, I is ordinary physical influence. This stage consumes A088's independent acceptance of the previous no-cap theorem AND its new post-core-exposure local-price obstruction. Conditional mutual-information refund alone is not a payment.

## 1. Scope and exact account

Let b(x)=(-1)^q(x) be ANY F2 quadratic phase on n core coordinates, including arbitrary linear/constant terms, degenerate polar rank and unused coordinates. Pick any marked core vertex x0 and one fresh control bit z. Let F equal b except that its sign is flipped at (x0,z0). By translation/reflection take x0=z0=0. Put N=n+1, epsilon=2^(1-N)=2^-n, and let R be the polar rank of q (even). The control is absent from the base phase. Both actual core terminals b and b'=b with the marked sign flipped are retained.

Write u_T,v_T for the actual core/control Fourier row amplitudes, r_T=u_T^2+v_T^2, e=I_z(F)=epsilon, and I_X=(I(b)+I(b'))/2. The SAME normalized core reference r serves both actual terminals. Their actual averaged complete reference cost is H(r), not their average entropy. Define the unused common-reference child bank

    S_ref=4I_X-H(r).

The complete conditional output reference r_T P(V|T) is exactly the output squared spectrum (V is z occupancy). Replacing only the global flag prior by P(V|T) refunds exactly I(T;V) and leaves B=H(V|T). Thus the full cost is H(r)+B; no informative Fourier dummy is removed. Zero row masses use continuity; r covers both actual core spectra, though it need not be positive outside their joint support.

The target is the following checked statement (finite base cases certified in out/CHECK files):

    if R>0, S_ref>=0 and B<=4e+S_ref/2.                 (1)

Therefore every such node has a full rate-four payment, retaining both terminal references:

    H(F)=H(r)+B<=4I(F)-S_ref/2   (R>0).                 (2)

At R>0 at most HALF of the actual available common-reference bank is booked to the positive conditional flag excess [B-4e]_+. The other half is retained; it is not silently renewed at a descendant. The analytic proof below handles n>=5. Small n<=4 is an exact exhaustive certificate over all quadratic phases; all marked vertices reduce to the zero-point domain by translation preserving degree, rank, H and I. This is a selected point-attachment payment, not a universal arbitrary four-core surplus claim.

## 2. A quantitative support-rank surplus, with destroyed edges

A quadratic phase has flat squared Fourier spectrum on an affine set of 2^R labels, magnitude A=2^-R/2. Autocorrelation is a character on the radical of its polar matrix and zero off that radical; Fourier inversion proves this fact. Hence H(b)=R. No phase sign or linear term is assumed favorable.

For a phase on k coordinates flipped at one vertex put eta=2^(1-k). Outside the ORIGINAL affine Fourier support the new coefficients have magnitude eta. The outside mass beta=(2^k-2^R)eta^2<=2eta. For k>=4, 2eta<=1/4; the scalar bound h2(beta)<=beta log2(e/beta) and monotonicity of t log2(e/t) give

    H(b')<=R+h2(beta)+beta(k-R)
           <=R+2eta(2k-R-2+log2 e)
           <=R+2eta(2k-R).                             (3)

Let a be the number of nonzero polar rows and l the number of remaining coordinates with constant derivative one. Then I(b)=a/2+l and a>=R. At the marked vertex at most a+l original edges are pivotal. A vertex flip changes each influence by plus or minus eta. Since eta<=1/8, the coefficients of a,l below are nonnegative:

    I(b')>=a/2+l+eta(k-2a-2l)
           >=R/2+eta(k-2R).

Thus (3) yields the quantitative surplus

    4I(b')-H(b')>=R(1-6eta),                            (4)

while the clean core has surplus >=R. This includes edits destroying all available edges, all affine support orientations and all dummy-coordinate counts. It improves the earlier zero-linear/quadratic-point scope with an explicit bank; it does not claim the phenomenon of bounded FEI for quadratic edits is new. A017 already proves a general quadratic few-edit bound at 4+2/ln2 and a zero-linear one-point rate-four scope; A097/A094 already price bent zero-point selectors. Those baselines are not rerun as discoveries.

For the selector F with N=n+1 and n>=5, eta_core=2epsilon. Its averaged actual-ENTROPY child surplus S_ent therefore obeys

    S_ent=4I_X-E H(core)>=R(1-6epsilon).                  (5)

The complete common-reference bank includes the channel cost J:

    H(r)=E H(core)+J,  S_ref=S_ent-J,
    0<=J<=2e/ln2<3epsilon.

Hence S_ref>=R(1-6epsilon)-3epsilon>0 for R>=2,N>=6. J is not free and is never erased from the shared reference cost.

## 3. Half-bank payment in all larger dimensions

For R>0 the edited core has largest squared coefficient at most (A+2epsilon)^2. (The outside coefficients also satisfy this maximum bound.) Min-entropy therefore gives

    H(b')>=R-2log2(1+2epsilon/A).

Together with (3) for the full N-bit output, and ln(1+t)<=t,

    Delta H=H(F)-E H(core)
        <=4N epsilon+2epsilon/(A ln2).

Consequently

    Delta H-4e < epsilon[4(N-1)+3*2^(R/2)].             (6)

For N>=6 and even 2<=R<=N-1,

    epsilon[4(N-1)+3*2^(R/2)+3R]<=R/2.                 (7)

To verify (7) in the continuum-free integer domain: for fixed R the left side decreases with N. The minimum allowed N is max(6,R+1). At R=2,N=6 equality holds in (7); at R=4,N=6 the left numerator is44/32<2. For R>=6,N=R+1 the comparison is 7R+3*2^(R/2)<=R*2^(R-1). Each summand is at most R*2^R/4: 2^R>=28 and R*2^(R/2)>=12. This proves all remaining integers.

Equations (5)-(7) show Delta H-4e<=S_ent/2. The REQUIRED complete-reference version follows rather than assuming entropy slack is available:

    B-4e=Delta H-J-4e
        <=S_ent/2-J<= (S_ent-J)/2=S_ref/2.

This is the new payment. The retained terminal bank and the query refer to the SAME actual row law; the channel is subtracted once from both. It directly covers A088's G_m after its actual first core query, with R=2m and N=2m+2, although B/e diverges there.

## 4. Affine guard and finite endpoints: the failed pilot is preserved

The first pilot correctly refuted the overbroad affine extension. We had miscounted the fair outside rows by a factor two. The helper/spec/failure are preserved as code/check_v1.py, FROZEN_SPEC.json and out/PILOT_V1_FAILURE.json; v2 changes the theorem to POSITIVE polar rank and records affine cases as guards.

For R=0 the clean core has one coefficient of magnitude one. The exceptional selector row has masses (1-epsilon)^2,epsilon^2; all other 2^n-1 rows have equal masses epsilon^2,epsilon^2. Their total flag entropy is 2epsilon-2epsilon^2, and their total core marginal mass is the same rho. Thus B<=2epsilon+2(N-1)epsilon^2<=3epsilon for N>=2, but this does not make the common-reference terminal bank available.

For a CONSTANT clean core, I_X=n epsilon and

    H(r)=eta(1-rho)+rho(2n-1), rho=2epsilon-2epsilon^2,
    S_ref/epsilon=2+(4n-2)epsilon-eta(1-rho)/epsilon
                 ->2-2/ln2<0,

where eta(t)=-t log2 t. So this particular common reference eventually costs MORE than4I_X despite the actual point-sign family obeying H<=4I. A source bank or a changed reference must pay that excess; it cannot be silently admitted. This diagnostic is not claimed new against A003's sharp point allowance; it isolates why positive quadratic rank supplies the reserve needed here. The zero-core case is trivial.

The actual entropy H<=4I for affine point flips is still true: outside the original singleton spectral support the mass is <=2eta, so the same scalar estimate as (3) gives H<=4k eta on k>=2 coordinates, while physical influence is >=k eta. Smaller dimensions are checked directly. This is a separate entropy certificate, not a free certificate for r.

For positive R and n<=4 the current frozen exact certificate exhausts every F2 quadratic coefficient tuple (constant, linear and all pair coefficients), not an arbitrary real relaxation. It checks S_ref>=0, B<=4e+S_ref/2 with complete core laws, exact physical influence and rational prime-log entropy. No dimension is increased automatically. These finite cases are the only computational bridge needed by the all-dimensional proof.

## 5. Scope of one owner and physical histories

A088's parent P_m restricted at c=0 is exactly G_m in this selector family. Its post-exposure bank S_ref is explicitly computed and certified unused BEFORE booking (1), and both core terminal references remain. This statement does not claim the bank was unused by an arbitrary incoming parent ledger; if an earlier ledger spent it, subtract that booking before applying the inequality. Nor does it transport an arbitrary prescribed parent reference into r for free. Our owner is the explicitly constructed common output-core reference at this node.

Any proper core restriction of a point-flipped quadratic phase leaves either a clean quadratic phase or a point-flipped quadratic phase. The bound H<=4I above therefore supplies actual rate-four leaf certificates after further restrictions. However, a half-bank is not reinitialized at every node: extension of the SAME supplied incoming reference through a second mixed query still needs its signed reference-transfer cost and earlier booked debit. This is the FIRST unsupported universal/history line. For arbitrary nonquadratic terminal cores, the rank surplus (4) is unavailable; root influence capacity is not a substitute for unused child surplus.

## 6. Review dependencies and first unsupported universal line

A088's conditional-flag obstruction is independently reconstructed here, rather than treated as a refutation of FEI. A066's mixed G,R ledger and A069's inherited-reference core-query identity are independently reviewed and retained at their exact scopes. Their formulas show why conditional loss-only or a nonnegative reference decrement is not a signed history payment. The older A068 parity-star rank reference is reviewed separately before opening this new candidate, leaving its later tag-deletion closure pending from our perspective.

The new theorem uses the accepted singleton restriction/channel identity and elementary quadratic Fourier flatness; no universal FEI assumption is used. Finite small-core certification plus Sections 2-4 prove the scoped all-dimensional statement. Full FEI remains open: the unresolved line is a comparable UNUSED actual common-reference surplus for arbitrary nonflat core branches, with all inherited reference transfer, prior bookings and terminal debt retained under another physical query.
