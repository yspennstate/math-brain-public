# A036 / B08 stage 2: explicit recovery bill and completed-reference guards

## exact target, quantifiers, hypotheses and units

Bits throughout, except ln. Correcting stage 1 notation: M=sum_i h2(Inf_i) is the marginal entropy sum; campaign B=sum_i H(S_i|S_-i) is erasure entropy. TC=D2(P||Q)=M-H(P), where P=fhat^2 and Q is the product of actual spectral marginals. The stage-1 symbol B meant M, not C018's B. Its theorem is unchanged under this renaming.

For a normalized signed reference b, define C_b(U)=sum_S b_S b_{S xor U}, v_U=C_b(U)^2, Z=sum v_U, L=sum v_U log2(1/v_U), and T=L/Z=H(v/Z)-log2 Z. No raw-L payment is proposed. The lead requested exact B05 k=2,4 and addressing a=1,...,4 tests of TC>=T/4-kappa I and M<=T/4+cI, with support terms retained.

The substantive recovery repair is the following universal reference lemma. For ANY finite product law Q with marginals q_i, J=sum q_i<=1/16, M=sum h2(q_i), and ANY sign choices epsilon_S on its support, b_S=epsilon_S sqrt(Q(S)) satisfies

    |T/4-M+(2+log2 e)J| <= 9JM+15J^2.                 (R)

Here J equals physical influence I when Q is the actual spectral-marginal reference. The lemma does not assume Booleanity. It pays recovery with an explicit state-dependent bill; it does not prove divergence payment. In particular, if J,M tend to zero, T/4=M-(2+log2 e)J+o(J).

The six frozen Boolean cases pass kappa=c=8. The first certified zero-price failure in the ordered addressing test is a=4, with T/4-TC>77/100 bits. Addressing with positive zero completion gives the exact limiting coefficient tau described below. This persists on a genuine full-support one-point-flipped addressing family. B05 itself eventually fails zero-price payment with exact limit 8/5-log2 e>0, even though its k=2,4 cases pass. None of these is an unbounded H/I family.

## sources actually read, revisions and theorem locators

Read BOARD.md (supervisor snapshot 2026-10-11 23:29 UTC), B08 STREAM_NOTES.md v1 (2026-10-11 22:45Z), and own STATUS.md. The B08 lead explicitly directs these six cases and the notation correction; this supersedes the prior NEXT about surgery of point-defect tensors. No more pure point-defect tensors were tested.

Read A038 REPORT.md, run 20261011T221733Z-fleet05-A038-occupancy-term-audit: Sections 1-5 distinguish K_full, K_occ and the unbounded correction Delta. Read A040 REPORT.md, run 20261011T225840Z-fleet05-A040-credit-insufficiency-tests: Sections 1-4 give subnormalized/conditioned addressing, bent surgery, B05 best-coordinate and sparse-tribes controls. This prevents duplicating its addressing result or conflating references. The present new addressing calculation uses a normalized completion outside support, which A040 deliberately does not analyze. A040's T=-2log Q(A) concerns a subnormalized supported amplitude and is correct for that convention; its conditioned T=0 is also correct. Neither is the completed T used here.

The protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2, campaign files and paper/source context were read at the preceding stage; no imported theorem from those papers is needed below. The original B05 run 20261011T193057Z-fleet01-B05-rare-restrictions supplies the family name; its truth table and spectra are reconstructed here. Stage 1's collision definition is retained, with the newly necessary zero-completion convention made explicit. Exact local source hashes and locators are in out/source_receipts.json. No brain write, shared-file modification, external message, git operation or new worker was used.

## complete derivation or exact first unsupported line

### 1. Universal quantitative recovery lemma

Delete q_i=0 coordinates (their spectral bits are forced absent); J<=1/16 excludes q_i=1. The J=0 case is a character-free delta amplitude and T=M=0. For J>0, put E=sum_i q_i log2(1/q_i). Every singleton correlation has the exact formula

    C_b({i})=2sqrt(q_i(1-q_i)) r_i,
    r_i=E_{Q_-i}[epsilon(0,S_-i)epsilon(1,S_-i)].

The all-empty S_-i event has probability at least1-J. Thus |r_i|>=1-2J, and v_i=4q_i alpha_i with

    1-5J <= (1-q_i)(1-2J)^2 <= alpha_i <=1.

The scalar bound -ln alpha<=(1-alpha)/alpha, alpha>=11/16, and 1/ln2<3/2 give log2(1/alpha_i)<=12J. Since log2(1/q_i)-2>=0, the singleton raw entropy obeys

    E-2J-5JE <= L_single/4 <= E-2J+12J^2.             (1)

For any shift U, absolute correlation is bounded by that of the unsigned product amplitude, so v_U<=y_U=prod_{i in U}4q_i. For 0<=x<=y<=1,

    x log2(1/x)<=y log2(1/y)+y/(e ln2).               (2)

Indeed write x=yr and use r log2(1/r)<=1/(e ln2). Summing over |U|>=2,

    sum y_U log2(1/y_U)
      =sum_i 4q_i log2(1/(4q_i)) [prod_{j!=i}(1+4q_j)-1]
      <=4E(e^(4J)-1),
    sum y_U<=e^(4J)-1-4J.

For J<=1/16, e^(4J)-1<=16J/3 and e^(4J)-1-4J<=32J^2/3. These follow from e^x<=1/(1-x) and e^x-1-x<=x^2/[2(1-x)]. With e>8/3 and ln2>2/3, (2) therefore yields

    0<=L_higher/4<=6JE+2J^2.                         (3)

Since v_empty=1, 1<=Z<=prod_i(1+4q_i)<=e^(4J). Combining (1)-(3), and using 1/Z>=1-4J, gives

    E-2J-9JE <= T/4 <= E-2J+6JE+14J^2.              (4)

For the lower bound, E>=4J makes E-2J-5JE nonnegative, so multiplication by 1-4J preserves the required direction. All normalizers are retained.

Finally the convergent identity

    -(1-q)ln(1-q)=q-sum_{l>=2}q^l/[l(l-1)]

gives M=E+(log2 e)J-beta, 0<=beta<=J^2: the tail is at most q^2/[2(1-q)] and 1/ln2<3/2. Substituting into (4), and using E<=M, proves (R). No Boolean cancellation or unproved FEI inequality enters this argument.

The exact first unsupported dimension-free recovery line is replacing 9JM by O(J) without controlling M. The exact first unsupported divergence line is TC>=T/4-kappa I on the general admitted class. The all-phase reference lemma proves neither. On a sequence with I,M->0, however, recovery has now been completely paid with coefficient 2+log2 e+o(1).

### 2. Exact B05 reference and contraction certificate

For even k, let r=2k, p=2^-r, delta=2^-k and s=2^(-k/2). Use b_k(x)=(-1)^(x1*x2+...+x_(k-1)*x_k) on 0/1 physical bits and its one-point flip b'_k. Children G=1+A(z)(b_k-1), H=1+A(z)(b'_k-1), where A indicates all-zero controls. The fresh selector chooses G or H. The actual marginals are

    q_data=p(1/2+delta), q_control=p(1-s+delta), q_selector=p delta.

The parent Fourier coefficients at data T, controls U, selector bit Y are

    Y=0: 1[T=U=empty]+p(c_T-1[T=empty]-delta),
    Y=1: p delta,
    c_T=s*(-1)^(paired quadratic form in T).

All coefficients are nonzero for k=2,4 and for all even k>=2. Thus Q(A)=1, K_supp=0, K_shape=TC, and the reference phase is uniquely actual. Let c_D,c_C,c_Y be the unsigned product amplitudes of the three marginal groups. The same-sign reference has four separable terms:

    b = [s_phase(T)c_D(T)c_C(U)
         -2 c_D(empty)1[T=empty]c_C(U)
         +2 c_D(empty)c_C(empty)1[T=U=empty]]
          *sqrt(1-q_selector)1[Y=0]
        +c_D(T)c_C(U)*sqrt(q_selector)1[Y=1].

Here s_phase is the product of (+,+,+,-) phases on each data pair. For each pair of the four terms, every shifted coordinate contributes a common sqrt(q_i(1-q_i)); every unshifted coordinate contributes a rational q_i or 1-q_i. Consequently C_b(U)^2 is rational even though b itself can contain radicals. The code implements these local tables exactly, then groups shifts by counts of data-pair types 00,01/10,11, control shift weight, and selector shift. Multiplicity is (k/2)!/(e0!e1!e2!)*2^e1*binom(r,l). This is a proved finite contraction, not a numerical radical approximation.

The five spectral classes are the anchor; nonempty-control/empty-data; positive nonempty-data; negative data; and selector-present. Their exact probabilities/multiplicities are in out/verification.json and code/check.py. Integer Walsh transforms of the n=7 and n=13 truth tables independently verify the complete spectra and marginals. A separate direct signed contraction verifies every shift at k=2.

### 3. B05 asymptotic coefficient and zero-price obstruction

As even k->infinity, the nonempty-data Fourier class has total mass p(1+o(1)) and log probability 5k+o(k), so contributes 5kp(1+o(1)) entropy. The nonempty-control/empty-data class has mass p(1+o(1)) and log probability 4k+o(k), contributing 4kp(1+o(1)). Anchor entropy is O(p). Selector mass is p delta, with entropy 3kp delta=o(kp). Therefore

    H/(kp)->9, I/(kp)->5/2, H/I->18/5.

Also I->0 and M=O(k^2 p)->0, directly from the three marginal classes. Apply (R):

    (M-T/4)/I ->2+log2 e,
    (T/4-TC)/I ->18/5-(2+log2 e)=8/5-log2 e.

The latter is in [0.15730495911103,0.15730495911104] by a rational certificate. Thus zero-price lower payment eventually fails on actual full-support B05 functions, while the k=2,4 tests pass it. This is an analytic infinite-family conclusion, not automatic dimension escalation or extrapolation from floating data. It does not refute any fixed kappa greater than this limit.

### 4. Addressing support and three distinct reference conventions

Let N=2^a and F_a(x,y)=y_x. Its only nonzero coefficients are N^-1*(-1)^(V dot j) at (V,{j}); P is uniform on N^2 atoms. Thus

    H=2a, I=1+a/2, M=a+N h2(1/N),
    Q(A)=(1-1/N)^(N-1)=w_N,
    TC=K_supp=-log2 w_N, K_shape=0.

These support terms are not absorbed into a constant without stating them. Conditioned Q(.|A)=P, so the normalized supported amplitude is exactly actual fhat and T=0. A040's subnormalized supported amplitude sqrt(w_N)*fhat instead has Z=w_N^2 and T=-2log2 w_N. Our completed amplitude is normalized on the full product Q: use actual phases on A and +1 phase at every spectral zero. It generally has different Z,T. Completion is specified for each function; no tensor identity for independently completed functions is claimed.

### 5. Completed addressing collision formula

Put t=1/N, a0=4t(1-t), and u=t(1-t)^(N-1). The distinguished data label 0 has constant positive Fourier phase. All other singleton-data phases are address characters. For address shift U and zero data shift,

    C_b(U,0)=1 if U=0; C_b(U,0)=1-Nu if U!=0.

For nonzero data shift V of weight w and e=1[0 in V], put h=w-e. Correlation is independent of U and equals [2sqrt(t(1-t))]^w F_{w,e}, where

    F_{w,e}=1-2^(1-w)[h(1-t)^(N-w)+(N-1-h)t(1-t)^(N-w-1)]
              +1[w=2,e=0]2^(1-w)(1-t)^(N-2).        (5)

Proof: average phases over the address subsets. A singleton with nonzero label paired with a nonsingleton has zero character average; two different singleton labels also have zero average. Remove precisely those pairs from unsigned correlation. When w=2 and neither label is 0, the intersection was subtracted twice; the last term restores it once. For V=0 the same-label character has average (-1)^(U dot j), giving the preceding special formula.

The v groups are therefore 1 at multiplicity1; (1-Nu)^2 at multiplicity N-1; and a0^w F_{w,e}^2 at multiplicity N*binom(N-1,w-e). These formulas include all 2^(a+N) shifts. Direct integer Walsh and separate direct sign contractions verify them at a=1,2; larger cases use the proved formula and exact rational arithmetic.

### 6. Exact addressing slope

For fixed w, the e=0 class dominates as N->infinity. Its limiting F values, including the zero-shift/address-nonzero group, are

    F0=1-e^-1, F1=1-2e^-1, F2=1-e^-1,
    Fw=1-(w+1)/(2^(w-1)e), w>=3.

Here e without subscript denotes Euler's number, not the membership indicator in (5). Let

    z=sum_{w>=0}4^w Fw^2/w! = e^4-12e+30/e-13/e^2,
    z1=sum_{w>=0}w*4^w Fw^2/w! =4e^4-32e+56/e-20/e^2,
    tau=z1/z.

To check the sums, first use Fw_base=1-2(w+1)/(2^w e) at every w. Poisson generating identities give z_base=e^4-12e+20/e and z1_base=4e^4-32e+40/e. Correct w=0 and w=2 to obtain the displayed formulas.

Since |F_{w,e}|<=1 by unsigned-correlation domination and binom(N,w)[4t(1-t)]^w<=4^w/w!, factorial tails dominate both masses and first moments. The e=1 group vanishes for each fixed w. Therefore Z/N->z. In L/(Na), the term w*log2 N/a tends w and contributes z1; the extra phase entropy F^2 log2(1/F^2) is at most1/(e ln2), so its summed contribution tends0 after division by a. The w=0 entropy is bounded and also vanishes on that scale. Consequently

    T/a ->tau, TC->log2 e, M/a->2, I/a->1/2.

Rational intervals give tau in [4.77678254267720,4.77678254267721]. Hence any dimension-independent constants for THIS completed-reference family necessarily satisfy

    kappa >=tau/2 >2.38839127133860,
    c >=4-tau/2 >1.61160872866139.

No finite kappa or c is refuted here; this is an exact coefficient floor, not divergent influence-normalized entropy.

### 7. Reusable stability lemma and transfer to actual full support

For any two unit real reference amplitudes b,c on an n-bit group, let epsilon=||b-c||2 and A=||b||1+||c||1. Young's convolution bound follows from the triangle inequality for translations and gives ||C_b-C_c||2<=A epsilon. Since ||C_b||2<=||b||1 and similarly for c,

    ||v_b-v_c||1 <=A^2 epsilon=:rho.

Both Z are at least1, |Z_b-Z_c|<=rho, and TV(v_b/Z_b,v_c/Z_c)<=rho. If rho<=1/2, a maximal-coupling proof of entropy continuity yields

    |T_b-T_c| <=h2(rho)+n rho+rho/ln2.                (S)

Indeed H(X|Y)<=h2(theta)+theta log2(2^n-1) for coupling error theta; h2 is increasing up to1/2. The log-normalizer difference is at most rho/ln2. The A^2 price is explicit; no dimension-free stability is asserted.

Flip the all-zero physical vertex of F_a, whose value is +1, to -1. With n=a+N and delta=2^(1-n), the new coefficients are fhat'_S=fhat_S-delta. For a>=1, delta<1/N, so every old coefficient keeps its sign and every old zero becomes negative. The new function is Boolean and full Fourier support. Its marginals are

    address: 1/2+delta;
    distinguished data label0: 1/N-delta;
    other data: 1/N+delta.

Thus I'=I+(a+N-2)delta. Compare its actual reference to the original product reference completed NEGATIVELY at zeros. The sign arrays agree exactly and product-coupling gives TV(Q',Q)<=n delta, so epsilon<=sqrt(2n delta). The l1 norms satisfy A<=2sqrt(N)exp(2sqrt(N)) for all sufficiently large a: address factors are at most sqrt2; data marginals are at most2/N and sqrt(q)+sqrt(1-q)<=exp(sqrt(q)). Hence n*A^2*epsilon->0. Formula (S) implies T'-T_negative=o(1).

The negative completion has the same tau limit. After globally negating it, its supported phases are -(-1)^(V dot j) and zero phases are positive. Its V=0 correlations are unchanged. For V!=0, compared with positive completion, only pairings involving the distinguished singleton label0 and a nonsingleton change. For e=0, the extra coefficient is -4*2^-w*t*(1-t)^(N-w-1), tending0 for fixed w; e=1 classes have vanishing weighted multiplicity. The same factorial domination proves unchanged z,z1 and tau.

Physical amplitude distance is sqrt(2delta), so spectral entropy continuity gives H'=H+o(1); binary continuity gives |M'-M|<=n h2(delta)=o(1). Therefore TC'->log2 e, T'/a->tau and the coefficient floors above hold on actual FULL-SUPPORT Boolean functions. This removes a zero-completion-only loophole. Influence is large in this family; no claim is made that the tau/2 floor already applies unchanged to the admitted low-I endpoint.

### 8. Why sparse activation changes the constant ledger

For completeness, sparsely activate the full-support flipped addressing seed with r=ceil(3log2 a) fresh controls and activation probability p=2^-r. Put g=1+A(z)(f'_a-1). Every Fourier coefficient is nonzero: nonempty seed indices have p*fhat'_S on every control subset; empty seed/control-nonempty coefficients are p(mu'-1); the anchor is 1+p(mu'-1)>0 eventually. Here mu'=-delta.

Exact physical influence is p[I'+r(1-mu')]. Since r=o(a), I_g~pa/2->0. The exact activation spectrum gives H_g=p H'+O(rp)~2pa, so H_g/I_g->4. Entropy of a product-marginal reference is at most I_g log2(e(n+r)/I_g), which is O(1/a)->0 because p=Theta(a^-3), n=Theta(2^a). Apply (R), now with the ACTUAL activated reference:

    (T_g/4-TC_g)/I_g ->2-log2 e=0.557304959111... .

Thus the large-I tau/2 floor cannot simply be transported through activation: reference rebalancing changes the statistic. The low-I full-support endpoint still requires kappa>=2-log2 e. This is a scope/normalization audit and reproduces the known FEI-strength admission direction quantitatively, rather than claiming a solution on that endpoint.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, saved before the six-case pilot. Commands from this run directory: `python -X utf8 code/check.py` and `python -X utf8 code/coefficients.py`. The former checks B05 k=2,4 and addressing a=1,...,4, with the independent Walsh and contraction checks specified above. It uses under60 MB and finishes below the 60-second pilot cap. No heavy job, dimension escalation or GPU was used. Exact outputs include H,M,TC,T,L,Z, support mass and K_supp/K_shape.

Logs use 18 terms of the atanh series, positive ln2 denominator enclosures, exact power-of-two range shifts, and geometric remainder. Internal endpoints are rounded outward to denominator2^90; saved endpoints are rounded outward to the10^-15 rational grid. The coefficient certificate uses 25 exponential-series terms and a geometric tail, plus a rational ln2 enclosure. All signs and interval endpoints are rationally certified; displayed midpoint floats establish no claim.

Outward six-decimal enclosures for the two required constants are:

| Case | I exact | (T/4-TC)/I | (M-T/4)/I |
|---|---:|---:|---:|
| B05 k=2 | 19/64 | [-1.180763,-1.180762] | [4.578002,4.578003] |
| B05 k=4 | 141/4096 | [-0.928603,-0.928602] | [4.637049,4.637050] |
| addressing a=1 | 3/2 | [-0.454546,-0.454545] | [1.787878,1.787879] |
| addressing a=2 | 2 | [-0.334026,-0.334025] | [2.334025,2.334026] |
| addressing a=3 | 5/2 | [-0.070043,-0.070042] | [2.470042,2.470043] |
| addressing a=4 | 3 | [0.256712,0.256713] | [2.409954,2.409955] |

Both kappa=c=8 survive this domain. The proposed c=4 recovery fails already at B05 k=2; no all-k c=4 claim is made. The eventual B05 recovery coefficient is 2+log2 e<4, illustrating why finite and asymptotic tests are separate. Exact partition functions, not rounded table values, are stored in out/verification.json. The all-family proofs above, not these six cases, establish the asymptotic conclusions.

## proof dependencies and changed downstream conclusions

The proof is self-contained using Walsh expansion, finite character averaging, product coupling, elementary scalar entropy inequalities, binomial/generating-series identities, exact series tails, Young convolution inequality and the displayed coupling proof of entropy continuity. Neither A038 nor A040 is assumed as an unreviewed positive premise. The lead's TC restriction ledger is a target interface, not used as a theorem premise here.

A037/A039 receive an explicit reference recovery bill 9IM+15I^2 and the perturbation price A^2 epsilon. A040 receives completed-addressing slopes distinct from its supported-reference calculation. A038's separation of K_occ and K_full is preserved. A088/A094 should reconstruct the all-phase singleton and higher-shift estimates, the completed addressing character average and the full-support transfer. This is a recovery repair and route audit, not a new broad universal FEI candidate while B08 has unreviewed results. Full FEI and divergence payment remain open.

## one next mathematical action and independent reviewer

Next: express the exact child-reference reset in the B08 TC restriction ledger on the existing B05 control-first tree, and determine whether the weighted 9I_h M_h recovery bill can be paid once by source influence while retaining terminal entropy. This targets the only new state-dependent bill rather than making another class assertion. A088 is primary reviewer for (R); A094 should audit the completion/full-support/activation distinctions. No external review or downstream use is claimed.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code and out artifacts are saved only in the assigned A036 run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/save_receipts.json records hashes/sizes; out/check_receipt.json records observed execution. Independent review, supervisor copying and mirror verification remain unobserved. No save blocker remains.

**Universal bridge:** This stage moves the B08 normalized-divergence/recovery target feeding C018 erasure and C024 history transfer: on every product reference with I<=1/16, recovery is paid explicitly up to 9IM+15I^2, and completely to coefficient 2+log2 e+o(1) whenever I,M->0. It also fixes necessary lower-payment constants: 8/5-log2 e on B05, tau/2 on full-support large-I addressing, and 2-log2 e after sparse activation into the full-support low-I admission class. No universal FEI constant has been obtained. The remaining obligation is a Boolean lower-divergence payment plus nonreusing reference-reset/terminal accounting; uncontrolled M and phase/reference changes cannot be discarded. NEXT is the shortest route because it tests the exact newly exposed 9I_h M_h bill in the already shared B05 physical tree and TC ledger, where a conserved source-influence payment would transfer across histories, rather than adding another isolated FEI class theorem.
