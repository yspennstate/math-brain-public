# A rare queried coordinate with a nonvanishing whole-block refresh bill

All cubes are finite and uniform; functions are signs; logarithms are base two. This is an obstruction to a particular reference-price inequality, NOT an FEI counterexample. The reference is ONE whole-essential-core full-spike law, not the product of separate point-factor laws in A073/A036.

## 1. Frozen statement, actual Boolean family and rule

Let d_m be +1 except at the all-one point of m bits, where it is -1. For every integer k>=1 put

    g_k(z,a_1,...,a_6,i,y_1,...,y_k)
       =chi_z d_6(a) d_{k+1}(i,y).

Every displayed root variable is essential. For either s=+/-1 let J_s(x,w)=s if x=0 and g_k(w) if x=1. The physically queried coordinate is i. Its influence in g_k is 2^-k, and in J_s it is 2^(-k-1). Both i children remain noncharacter Boolean functions.

For a current core g with spectrum p and variance v, the WHOLE-ESSENTIAL-BLOCK law is q_alpha(0)=p(0), q_alpha(T)=(1-alpha)p(T)+alpha v 1_{T=Ess(g)} for nonempty T. Constants/characters use their exact laws. All physical coordinates remain represented; inessential coordinates carry zero frequency, and the spike mask is recomputed as the ACTUAL essential set after each restriction. This last clause matters: we do not inject dummy-coordinate mass into the killed y block. Its activation lift copies the two actual zero-data atoms and has q_alpha(T)/4 in each of the two nonempty controller copies. Fix alpha=1/7.

Start at that FULL fresh activation reference. Query i using the actual coherent kernel, with fair source-zero fallback and each reference's own outcome mass. Reset BOTH physical children to fresh whole-essential-block lifts with the SAME alpha. Let sigma_k be the average complete signed KL change, new-minus-inherited. Then

    sigma_k > 1/2048 for EVERY k>=1,
    sigma_k / Inf_i(J_s) > 2^(k-10).

Consequently NO finite K can make sigma_i<=K Inf_i hold universally for this particular reference/query/reset rule. Smaller fixed alpha is not asserted to repair it; this proof freezes alpha1/7 rather than extrapolating to all alpha. Both source/reference support and correct vacuum matching at the FRESH nodes do not cure this obstruction.

## 2. Exact scalar formula from full erasure and outcomes

The character z ensures Eg=0 and E[g|i=b]=0 for both outcomes. Hence each activation source has two vacuum atoms of mass1/4. Write

    ell=log(1/(1-alpha)), c=alpha/(1-alpha),
    psi(t)=t log(1+c/t) for t>0, psi(0)=0.

For ANY balanced core with full-essential Fourier mass t, direct summation gives D(p||q_alpha)=ell-psi(t). Its fresh activation KL is half that value. This accounts for every actual spectral row; ordinary nonempty rows have ratio1/(1-alpha), and the full row has the extra spike.

Put p*=4*2^-12=1/1024, the squared full coefficient of chi_z d_6. The i=0 child is this core, with all y variables dummy; its fresh full-essential mass is p*. The i=1 child is chi_z d_6 d_k; its full-essential mass is

    t_k=4*2^(-2k)*p*.

At the ROOT full frequency and the full frequency without i, the coefficients have opposite signs and equal squared masses t_k/4. Their erased mass is w=t_k/2. All spike reference mass therefore goes to the i=1 physical outcome under the actual coherent kernel. The reference outcome probabilities, INCLUDING the two vacuum atoms, are

    Z_0=(1-alpha/2)/2,
    Z_1=(1+alpha/2)/2.

On the erased nonempty data spectrum the reference is the full-spike mixture with spike mass at the erased full frequency; global vacuum masses still match. Thus its complete erased KL is (ell-psi(w))/2. The physical source outcome is fair, while its reference counterpart is (Z_0,Z_1), so its outcome KL is -log(1-alpha^2/4)/2. The exact erasure/outcome chain rule gives average inherited child KL as erased KL MINUS this outcome KL. The average fresh child KL is [2ell-psi(p*)-psi(t_k)]/4. Subtracting gives

    sigma_k = psi(t_k/2)/2 - psi(t_k)/4 - psi(p*)/4
                 -log(1-alpha^2/4)/2.                 (1)

Both vacuum rows, both outcomes, and full normalized terminal references have been used. We have not replaced normalization by physical fair weights. The finite certificate independently transports all actual atoms and compares its resulting interval with(1).

## 3. All-dimensional lower bound: no finite-search extrapolation

For t>0,

    psi''(t)=-c^2/[ln(2)*t*(t+c)^2]<0.

Since psi is continuous at0 with psi(0)=0, concavity implies psi(t/2)>=psi(t)/2. Hence the first two terms of(1) have nonnegative sum. At alpha1/7,

    psi(p*)=(1/1024)log(515/3)<1/128,
    -log(1-alpha^2/4)/2=-log(195/196)/2>1/392.

The first inequality follows from515/3<256. The second uses -ln(1-u)>=u and ln2<1, at u=1/196. Thus

    sigma_k > 1/392-1/512 > 1/2048.

The final comparison is rational cross multiplication. In particular this is a checked analytic family with arbitrarily small queried influence, not an unproved fit to a numerical grid. As k tends to infinity the first two terms of(1) tend to0, so the cost tends to the strictly positive constant -psi(p*)/4-log(195/196)/2. The limit is explanatory; the uniform lower bound already proves the unbounded ratio.

## 4. Embedding in an ACTUALLY paid original account

The obstruction is not caused by an unpriced arbitrary incoming law. This family admits an explicit original source and a complete paid history. Let F_g(x,a,b,w)=chi_a on x0, g(w) on x=b=1, and +1 on x1b0. At its original root use the complete lift of the WHOLE-core q_beta with beta=1/8, copying the six actual control atoms and putting q_beta(T)/16 in the four nonempty data copies. This is the explicit A050-type lift, but with the present whole-core reference; we derive its price here instead of importing the product-source theorem.

Here the actual root has two a-sector atoms1/4, four zero-data controller atoms1/16, and four copies p_g(T)/16 for each nonempty T. Consequently H(F)=3+H(g)/4 exactly. Direct pivots give I(F)=1+Pr(g=-1)/2+I(g)/4. Here Pr(g=-1)=1/2. The phase character contributes4 to S4(g)=4I(g)-H(g). To check each point factor without assuming FEI: for width m>=2, d=2^-m, its nonempty entropy is8(m-1)d(1-d), and its empty entropy is at most4d(1-d)/ln2<6d(1-d). The latter uses ln2>2/3, the first positive term of2atanh(1/3). Thus H(d_m)<(8m-2)d(1-d)<8md=4I(d_m). Tensor additivity proves S4(g)>=4. The original KL is D(p_g||q_beta)/4<=log(8/7)/4. Therefore the SAME original margin satisfies

    M0=4I(F)-CE(P_F,Q_root)>=3-log(8/7)/4.

Query b, retain b0, then query a in b1 and retain BOTH signs. ACTUALLY reset both full activation laws to the alpha1/7 whole-core lift. Its signed first price sigma1 is at most its gross fresh KL, hence sigma1<=log(7/6)/4. Keep this exact first bill in the account. Now query i and reset both children in EACH activation sign. Their common local average price is(1), so the global second signed price is sigma2=sigma_k/2. It is positive, but its gross fresh-KL bound gives sigma2<=log(7/6)/4.

The actual final cores are point tensors with the retained phase character. Their S4>=0. The two activation signs have equal physical histories, and their signed mean terms cancel; equivalently their paired mean surplus is nonnegative by direct activation spectra. The retained b0 contributes exactly one globally, so the COMPLETE frontier surplus S>=1. No branch is thrown away.

For A0=D(P_F||Q_root), e=Hroot-EHleaf-4(Iroot-EIleaf), exact signed algebra retains all references and normalizers:

    S-[A0+e+sigma1+sigma2]_+
       =min(S,M0-sigma1-sigma2).

Integer certificates8^4<2*7^4 and7^4<2*6^4 show both logarithms <1/4. Thus M0-sigma1-sigma2>45/16>1. Subtract ONE old eligible booking0<=omega<=1/4 and the SAME original account still retains>=3/4. The actual reset price is positive and locally influence-unbounded while the original account pays it uniformly. This distinguishes failure of the LOCAL payment lemma from failure of FEI or even failure of the supplied global transaction.

## 5. Current intake and obsolete repairs

A073-ACTIVATION-NONEMPTY-OCCUPANCY-REFRESH@1 (368e1aee16ac9ee742d5de9e3f7d8928b2ccc23b461f2589e4a877be747449cb) closes A046's old all-width/all-load fixed1/7 gap for a PRODUCT of point-factor references. Its proof separates global vacuum KL, conditional occupancy KL and monotone within-point nonempty shape. The point ratio R_old>=R_fresh gives the last nonnegative term. That conditional decomposition is consistent with A046's two-vacuum recurrence; there is no remaining need for the old gross two-generation load bound in that PRODUCT rule. A050 already supplies the later selected-x continuation. We consume these advances rather than rerun the obsolete search. This reconstruction is scoped and author-dependency-aware, not an independent full upstream-chain review.

There is no contradiction: this stage deliberately treats a Boolean core as ONE full-spike factor. Changing the factorization changes the reference and the reset. A073 makes no arbitrary-factor claim. A049's minimal4bit all-alpha witness already refutes arbitrary-factor NONPOSITIVITY; the present family additionally refutes EVERY finite queried-influence multiplier at the fixed alpha1/7. Increasing K numerically, matching supports, matching fresh vacuum masses, or deleting dummy-coordinate mass cannot repair this exact local inequality. The last proposed repair is explicitly excluded by recomputing actual essential sets in this construction.

First unsupported universal line: determine a REQUIRED useful reference conversion, or choose a hereditary reference rule which avoids these whole-block refreshes, and price an arbitrary Boolean INITIAL supplier from the actual unused original influence account. Our chosen whole-block reset need not be mandatory in a proof of FEI; its necessity is NOT asserted. The displayed family obeys H<=4I and is not an actual Boolean unbounded-H/I counterfamily.
