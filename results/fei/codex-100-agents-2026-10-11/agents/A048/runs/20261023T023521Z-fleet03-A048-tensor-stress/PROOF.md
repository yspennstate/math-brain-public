# Independent correlated-lift review and signed tensor stress

All laws are finite, all functions are uniform Boolean signs, and all logarithms are base two. References are normalized and dominate the actual spectral law. This is a conditional, source-complete result, not full FEI.

## 1. Independent reconstruction of A050 v1

Source: A050-CORRELATION-PRESERVING-SIGNED-LIFT@1, exact statement SHA256 671f52984dae0135907a518e7324c3efee58268b8065ab0e92137948844d937e. No repair or changed hypothesis is required. The following reconstruction uses a sector/latent-label entropy representation and direct pivotal probabilities; our finite checker was written without reading A050's checker.

For a core h let p be its Fourier-square law, mu=E h, u=mu^2. Calibrate a supplied q to q*(empty)=u and q*(s)=(1-u)q(s)/(1-q(empty)) on nonempty s. If u=1 use delta_empty. The KL chain rule on the empty/nonempty partition gives CE(p,q*)=CE(p,q)-B, where B=D(Ber(u)||Ber(q(empty))). Domination ensures the denominators and every source-positive likelihood are defined, using standard zero conventions. This credit is used once in specifying the INITIAL reference.

Let F be the selector of the independent a-character when x=0 and g when x=1, with g=1 on b=0 and h on b=1. Fourier expansion, with bit masks x,a,b numbered 0,1,2, gives masses 1/4 at a and xa; masses (1+mu)^2/16 at empty and x; masses (1-mu)^2/16 at b and xb; and four copies p(s)/16 at masks 0,x,b,xb for each nonempty data s. Replace just those latter p(s) by q*(s), retaining the actual other six atoms. The resulting Q is normalized since its sector totals are 1/2, (1+u)/4, and (1-u)/4. It dominates P_F. All source/reference likelihoods are one except in those four copies, so

    A_F = D(P_F||Q) = D(p||q*)/4.

The a-containing and a-free sectors of F have disjoint support, and the independent x label doubles each g frequency at one-quarter mass, hence H(F)=2+H(g)/2. Erasing b from g produces (delta_empty+p)/2. Including its fair mixture label bounds its entropy by 1+H(h)/2. Reinstating the binary b frequency adds at most one bit, so H(g)<=2+H(h)/2. Thus gamma:=H(F)-H(h)/4<=3 and

    CE(P_F,Q)=gamma+CE(p,q*)/4 <=3+CE(p,q*)/4.

Physical pivotal probabilities are Inf_x=Inf_a=1/2, Inf_b=t/2, and Inf_data=Inf_data(h)/4, where t=Pr(h=-1). Therefore I(F)=1+t/2+I(h)/4. A supplied CE(p,q*)<=C I(h), C>=4, yields margin M:=C I(F)-CE(P_F,Q)>=C-3+C t/2.

At each fresh query, erase that frequency in both laws and use the actual coherent branch kernel. On source-zero rows use fair fallback. Keep every reference-only row and normalize reference children by their OWN branch probabilities. Data processing with the SAME kernel gives the exact decomposition of initial A into erasure KL, outcome KL, and mean inherited-terminal KL. Each erasure term is the source-erased weighted conditional-membership KL. The branch outcome term is averaged over the erased label. There is no extra independent copy of A to book.

For any finite tree put R=Iroot-E Ileaf, e=Hroot-E Hleaf-C R and S=E(C Ileaf-Hleaf). Pure algebra gives

    A+e=S-M,   J=[A+e]_+,   S-J=min(S,M).               (1)

This retains signed query refunds in the SAME full source account. Replacing J by A+[e]_+ changes the theorem.

After b first and data queries only on b1, each physical terminal is a selector of the a-character and a restricted core g. Thus Hleaf=2+H(g)/2 and Ileaf=1+I(g)/2. Supplied hereditary H(g)<=C I(g) gives S>=C-2. Equation (1) leaves at least C-3. At C=4, permit a single x or a exposure at any chosen active frontier leaf, then stop at BOTH children. An x-pair has mean surplus [4+(4I(g)-H(g))]/2>=2. For an a-pair the mean child surplus is Sparent-4 Inf_a+D_a, with Inf_a=1/2 and D_a>=0: the entropy decrement is conditional membership entropy plus Jensen-Shannon divergence. Hence its mean surplus is >=0. The untouched b0 branch has reach 1/2 and surplus 2, contributing 1 to the full frontier. Consequently S>=1; M>=1 remains the ORIGINAL margin, and (1) leaves >=1, or >=3/4 after a genuinely eligible old booking omega<=1/4. No individual a-child certificate is asserted.

The explicit supplier is also checked analytically. For a width-r point sign, r>=2, delta=2^-r, v=4delta(1-delta), the empty probability is (1-2delta)^2 and every nonempty probability is 4delta^2. Set q_r(empty)=p_r(empty), q_r(s)=(7/8)p_r(s)+(v/8)1_full(s). Then A_r<=v log2(8/7)<v/4, because 8^4<2*7^4. The nonempty entropy is 8(r-1)delta(1-delta), and the empty entropy is at most v/ln2<3v/2, since ln2>2/3. Therefore CE(p_r,q_r)<(8r-1)delta(1-delta)<8r delta-delta=4I_r-delta. Products add the complete price and influence. Every restricted factor is a smaller point sign, character, or constant up to sign; the same entropy estimate proves H<=4I for all its actual restrictions. Thus ALL m>=1,r>=2 satisfy the supplier and hereditary certificates. At r2 the exact A_r=(1/4)log2(256/245). At m512, the lifted A=32log2(256/245)>2 by 256^16>2*245^16, but after full data revelation S=2. This independently confirms the necessity of the signed convention and excludes the conservative source-only assertion. Initial references are compared at the same root; no incoming reference conversion is forgiven.

Disposition: A050 v1 HOLDS at its stated scope. The source statement, hypotheses, contributors and hash are preserved in CLAIMS.json. The review does not claim to certify A050's Lean source or external persistence.

## 2. Signed tensor and sparse payment, including mixed frontiers

This application advances A048's prior conservative tensor stress to the newly consumed signed account. It is not a new unrestricted reference supplier.

Take T independent actual seed functions f_j, supplied dominating Q_j, and a specified independent physical stopping policy for each seed. Each may be A050's b/data/one-x-or-a mixed policy. Let A_j,e_j,S_j,M_j be the quantities in (1) at C=4. Initially the product reference is product Q_j. Entropy, influence and cross-entropy add; so do A and e. The exact total signed remainder is

    min(sum_j S_j, sum_j M_j).

Since min(sum S_j,sum M_j)>=sum min(S_j,M_j), each certified seed remainder rho_j provides total remainder at least sum rho_j. This holds for different independent policies and nonidentical seeds. For identical seeds and policies, J_T=T J and the remainder is EXACTLY T times the original remainder. No T log T term occurs. This claim concerns the inherited product reference, not a new canonical projection of the product.

Now take k fresh independent controls and an independent balanced sign z, retained throughout. Write alpha=2^-k and V=product_j f_j. Define the actual Boolean function

    W=1+AND_k(C)(z V-1),
    W0=1+AND_k(C)(z-1).

W0 is a point sign on k+1 bits up to complements. In the Fourier spectrum of W, the z-absent sector is EXACTLY the z-absent sector of W0 with empty seed frequency. In the z-present sector, for EVERY control frequency U and seed frequency s, P_W(U,z,s)=alpha^2 product_j P_j(s_j). Its total mass is alpha. Define Q_W by retaining the actual z-absent quotient sector and replacing product P_j by product Q_j in that z-present sector. This is a normalized dominating INITIAL reference. It is not an unpriced descendant reset. The disjoint sectors give exactly

    H(W)=H(W0)+alpha sum_j H(f_j),
    I(W)=alpha(k+1+sum_j I(f_j)),
    CE(W,Q_W)=H(W0)+alpha sum_j CE(P_j,Q_j),
    A_W=alpha sum_j A_j.                               (2)

First expose all k controls in a fixed order. All inactive physical terminals are constants and are retained. On the active branch, retain z and execute the stated factor policies. Transport the ORIGINAL Q_W by the actual coherent kernels, keeping fair fallback, all reference-only rows, and all branch normalizers. The inherited reference need NOT factorize on source-zero ghost rows. The argument below uses the root KL chain rule and the actual physical frontier, so it does not assume factorization there or zero controller KL releases.

Let beta_k=4alpha(k+1)-H(W0)>=0. This follows from the elementary all-width point-sign H<=4I proof above; k=0 gives a character and is covered separately. Actual terminal entropy/influence and the root cross-entropy give

    S_W=4alpha+alpha sum_j S_j,
    M_W=beta_k+alpha sum_j M_j,
    e_W=H(W0)-4alpha k+alpha sum_j e_j,
    A_W+e_W=S_W-M_W.                                  (3)

The 4alpha in S_W is the actual retained z-character owner. Beta_k is the quotient ROOT margin; these are not additive independent banks. Keep the minimum in (1):

    S_W-[A_W+e_W]_+
      =min(4alpha+alpha sum S_j,beta_k+alpha sum M_j)
      >=alpha sum_j min(S_j,M_j).                      (4)

If the only eligible old debits are omega_j in the original seed accounts, carry them with their physical reach alpha ONCE. Equation (4) then leaves at least alpha sum_j(rho_j-omega_j), where rho_j<=min(S_j,M_j). In particular A050's mixed policies have rho_j=1 and 0<=omega_j<=1/4, so at least 3alpha T/4 remains. This pays the full erasure/outcome/terminal source once, including controller releases and every inactive terminal. There is no renewed seed bank, canceled old canonical bill, or free reference reset.

For identical seeds with fixed influence, choosing k=ceil(2 log2(T+1)) sends I(W) to zero, yet preserves this alpha-scaled margin. The quotient entropy contains the familiar O(alpha k) activation term, and its actual controller influence pays it through beta_k. No additional alpha T log T charge appears. A scalar seed claim already known to fail under A+[e]_+ is not restored by tensoring or sparse activation; equations (1)-(4) concern its correctly signed replacement only.

## 3. Irrelevant-factor test and first universal gap

For an independent unqueried spectator s with normalized dominating Q_s, root margin changes by M_s=4I(s)-CE(P_s,Q_s), terminal surplus by S_s=4I(s)-H(s), and initial source by A_s=D(P_s||Q_s); the signed edge e is unchanged. Thus the exact remainder changes from min(S,M) to min(S+S_s,M+M_s). If Q_s=P_s these two increments coincide, and a genuinely unused nonnegative spectator surplus adds exactly that surplus. An arbitrary reference can instead reduce the margin by its KL price. There is no reference-free credit from an irrelevant factor, and its full terminal entropy stays in the formula. A physically dummy coordinate has zero increment after contraction.

FIRST UNPAID UNIVERSAL LINE: supply for an arbitrary Boolean core a useful complete normalized dominating correlated reference with CE<=C I and actual mixed-frontier certificates, OR price the required incoming-reference conversion from an existing unused ancestor source. None of (1)-(4) supplies this. Taking q=p without an entropy bound would assume the missing FEI content. No universal C018/C019/C024 constant is improved.

## 4. Validation scope

The frozen finite checker recomputes all spectra by integer Walsh transforms and all influences by direct pivotal edges. It covers all 22 truth tables on n<=2, 66 b/stop/x/a frontiers, six direct guarded activation spectra (T1,2;k0,1,2;largest13bits), and60 rational scalar ledger cases. Its correlated reference implementation is written independently of A050's code. It uses our own previously checked interval helper only for logarithms and coherent-channel replay. Logarithms have a 40-term positive atanh expansion with universal tail 2/(3^81*81*(1-1/9)), range reduction to [1,2], and outward 2^-96 rounding. Equalities are checked by exact coefficient identities or interval overlap as supplemental evidence; the analytic proof establishes equality-boundary floors and all-dimensional conclusions. The main 710 assertions and 2366 coherent-channel assertions passed in under one arithmetic second. No Lean compiler or large job was launched. Independent review of the new tensor/sparse application remains pending.
