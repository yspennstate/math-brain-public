# Arbitrary-Boolean-source positive canonical-to-floor conversion

New theorem; independent review pending. Every quantity is in ideal bits. Let g be ANY Boolean function on a>=1 uniform source bits (constant functions permitted), let m>=8 dummy data bits, n=a+m,M=2^n and epsilon=1/M. Form the actual fair-selector full-point edit F of g on n+1 bits. By translating the edited point and output-negating if necessary, assume the point is0 and g(0)=1. Such operations preserve squared spectra and costs. Write A_s=ghat(s), N=number of nonzero A_s and W=2epsilon-N epsilon^2. The canonical reference Qcan assigns (1-W)A_s^2 to old source masks with empty selector/dummy frequencies and epsilon^2 to EVERY other full Fourier mask. This is the specified INCOMING complete normalized reference, not a free supplier.

At the SAME F and same physical reach lambda>0, convert to the actual A011 data floor (P_g,embedded+3epsilon U_n)/(1+3epsilon), lifted by the true conditional selector-frequency kernel. Denote it Qfloor. Both laws cover every true atom and normalize. No physical Boolean function, dimension, control, source bank or sibling is replaced. Then

    (23/512)lambda*epsilon
       < e=lambda[CE(P_F,Qfloor)-CE(P_F,Qcan)]
       < lambda*epsilon.

The conversion genuinely changes the CONDITIONAL-NONEMPTY model shape. The existing fair selector has physical influence EXACTLY epsilon: it is pivotal precisely at the full edited data point. Thus this is also a uniform conversion price between(23/512)lambda*Inf_selector and lambda*Inf_selector. It costs a strictly positive amount; an already supplied original owner with unused quota >=lambda*epsilon can retain every old debit and both terminals while paying it. The selector influence is NOT a newly issued or reusable credit: actual unused original quota is required. This is a uniform conversion price for arbitrary Boolean SOURCES within the named point-selector/reference interface, not a universal initial influence-priced supplier.

## Exact complete laws

As in POSITIVE_HANDOFF.md, old full probabilities are(A_s-epsilon)^2, all complementary full probabilities epsilon^2. There are N old and2M-N complementary masks; sum A_s=g(0)=1 and sum A_s^2=1 prove full normalization. The data marginal q equals A_s^2-2epsilon*A_s+2epsilon^2 on old source support and2epsilon^2 on all other data masks. Floor data R equals(A_s^2+3epsilon^2)/(1+3epsilon) on old support and3epsilon^2/(1+3epsilon) outside it. It has mass1, and true conditional lift gives EXACT complete Dfloor=D(q||R). Canonical complete Dcan=D(P_F||Qcan), so the reached conversion subtracts the ACTUAL current-model divergence: e=lambda(Dfloor-Dcan).

## Quantization supplies the uniform estimate

Each nonzero A_s is a signed integer sum divided by2^a, hence |A_s|>=2^-a; no lower bound for arbitrary non-Boolean spectral measures is asserted. Consequently N<=2^a and L=sqrt(sum_nonzero A_s^-2)<=2^a*sqrt(N). Put u=2^-m<=1/256. Then N epsilon<=u and epsilon<=u/2<=1/512. Both inequalities retain the actual source ambient dimension even when g is constant or ignores coordinates.

For old source data masks, the square root of their chi-square contribution to chi2(q,R) is at most

 epsilon[3+2sqrt(N)+epsilon(6sqrt(N)+L)+6epsilon^2 L]/sqrt(1+3epsilon)

by the Euclidean triangle inequality. Since sqrt(N)>=1, L<=2^a sqrt(N), this is <=epsilon sqrt(N)[5+6epsilon+u+6epsilon*u]/sqrt(1+3epsilon)<6epsilon sqrt(N). The inequality is checked at u=1/256,epsilon=1/512. Off-source chi-square is exactly(M-N)epsilon^2(1-6epsilon)^2/[3(1+3epsilon)]<=epsilon/3. Therefore

 Dfloor <(3/2)chi2(q,R)
        <54N epsilon^2+epsilon/2
        <=(91/128)epsilon <epsilon.                    (1)

Here1/ln2<3/2 is proved by ln2>2/3. Both models are normalized; ln x<=x-1 gives the KL/chi-square bound, so no source entropy is discarded.

For the full canonical reference only old masks contribute to chi-square. Triangle inequality gives

 sqrt[(1-W)chi2(P_F,Qcan)]
   <=W+2epsilon sqrt(N)+epsilon^2 L
   <=epsilon sqrt(N)(4+u)<(33/8)epsilon sqrt(N).

Since1-W>=1-2epsilon>=255/256,

 Dcan <(3/2)(33/8)^2(256/255) N epsilon^2
      <26N epsilon^2 <=(13/128)epsilon.                (2)

No logarithm precision is needed to certify this small upper bound; it is an exact rational chi-square comparison.

## Strict positive lower bound

Partition the data frequencies into original source support and its complement, retaining both masses. Complement masses under q and R are

 x=2epsilon(1-N epsilon),
 y=3epsilon(1-N epsilon)/(1+3epsilon).

Thus0<x<y<=3epsilon and

 y-x=epsilon(1-N epsilon)(1-6epsilon)/(1+3epsilon)
     >=epsilon(255/256)(253/256)/(515/512)
     >(15/16)epsilon.

Binary KL curvature, exactly as derived in POSITIVE_HANDOFF.md, and log-sum imply

 Dfloor>=d2(x||y)>=(y-x)^2/(2 ln2*y)
          >(75/512)epsilon.                            (3)

Combining(2),(3), Dfloor-Dcan>(75/512-52/512)epsilon=(23/512)epsilon. Nonnegativity of Dcan and(1) give the upper bound<epsilon. Multiplying by the ORIGINAL physical reach lambda proves the theorem. Every bound holds for all integers a>=1,m>=8, not by an exhaustion or a limit interchange.

## It changes conditional nonempty shape, not just mass

Choose any nonzero source coefficient A_s and any data mask outside the source support (such masks exist since m>=8). Give both labels selector membership1, so both full labels are NONEMPTY and their old Qcan masses are both epsilon^2. Their new/old ratios could agree only if

 (A_s^2+3epsilon^2)/(A_s^2-2epsilon*A_s+2epsilon^2)=3/2,

equivalently A_s(A_s-6epsilon)=0. Nonzero Boolean quantization gives |A_s|>=2^-a=2^m epsilon>=256epsilon, so equality is impossible. This proves a genuine conditional-nonempty profile change for every source, including constant/parity sources; it is not a vacuum calibration or an isospectral zero-model change.

## Owner ledger, scope and next unpaid step

If the incoming fixed-target complete ledger is G+T=CE_original+sum old reached resets, installing Qfloor changes ONLY the reached terminal CE by e. Keep both full terminal costs, all query releases, original source price/rate and every previously booked debit. Because0<e<lambda epsilon, paying lambda epsilon from actual unused original quota suffices. No original remaining quota is asserted to exist for arbitrary g; its supply remains a separate hypothesis. Arbitrary source models that are not the stated canonical interface are also outside this theorem.

POSITIVE_HANDOFF.md supplies an ACTUAL paid two-reset history where this conversion is performed at reach1/4 and all old positive bookings stay charged; its sharper class constants leave>191/16384 from original rate4. This connects the uniform conversion lemma to an actual original-owner instance rather than renaming a source reserve. Further new-reference conversions, a universal initial influence-priced reference and arbitrary interacting-edit iteration remain unproved.

After installation, any finite restriction tree using ONLY mass-preserving physical inheritance from the installed floor retains the same complete bill. For each query raw child references use actual likelihoods, positive normalizers Z0,Z1 with Z0+Z1=2; nonnegative full release follows from entropy contraction, conditional KL and -average log Z. Telescoping preserves the original G+T including all full exits. This inherited-only corollary supplies no price for another fresh canonical/floor reset. NEXT must specify that new reset and its actual source owner; a physical query alone is already paid by inheritance.
