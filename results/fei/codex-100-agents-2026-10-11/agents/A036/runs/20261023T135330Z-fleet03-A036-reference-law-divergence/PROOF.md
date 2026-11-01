# Character-anchored reference: a decreasing off-character bank

All logarithms are base two. All cubes are finite, uniform, and genuinely Boolean. This is a replacement supplier for A048's exhausted mod3 mechanism, not a proof of full FEI. The initial supplier and every signed conversion remain booked to the SAME original owner.

## 1. Explicit complete reference and a universal normalized-divergence bound

Fix a nonempty character mask J, which is protected from queries. Put p_f(S)=fhat(S)^2, u=p_f(empty), a_J(f)=1-p_f(J), alpha in (0,1), beta=1-alpha, ell=log2(1/beta). Define the complete normalized law

    q_f^J(empty)=u,
    q_f^J(S)=beta*p_f(S)+alpha*(1-u)*1[S=J] (S nonempty).

It sums to one, contains every source-positive atom, and retains the empty mass exactly. If p_f(J)=0 it has a genuine reference-only atom at J: do not erase it or identify the supports. Constants have u=1 and q=p; the characters +/-chi_J also have q=p. Every KL below is finite since q>=beta*p on nonempty atoms. Directly separating the J atom gives

    0<=K_J(f):=D(p_f||q_f^J)<=ell*(1-u-p_f(J))<=ell*a_J(f).       (1)

Indeed all other nonempty atoms contribute ell*p; the J contribution is nonpositive since q(J)>=p(J). No entropy or FEI assumption enters (1).

For a physical query i outside J use the ACTUAL coherent channel. Delete i from paired masks, let Pbar(T)=p(T)+p(T+i), Qbar similarly, child spectra p_y, and

    k_y(T)=p_y(T)/(2*Pbar(T)) if Pbar(T)>0, else 1/2;
    r_y=sum_T Qbar(T)*k_y(T), Q_y(T)=Qbar(T)*k_y(T)/r_y.

Both r_y are positive: the beta*source part alone supplies beta/2. Thus source-zero reference-only rows, all their mass, and their fair fallbacks survive explicitly. The exact chain identity is

    K_J(f)=E_i + O_i + (K_inherited,0+K_inherited,1)/2,
    E_i=D(p||q)-D(Pbar||Qbar)>=0,
    O_i=D((1/2,1/2)||(r_0,r_1))>=0.                    (2)

Actually resetting BOTH children to their own normalized q_child^J has signed cost

    sigma_i=(K_J(f_0)+K_J(f_1))/2
                -(K_inherited,0+K_inherited,1)/2
            <=(K_J(f_0)+K_J(f_1))/2.                  (3)

This is an upper bound on the actual signed cost, not an equality replacing the inherited law by a free fresh supplier. The old bills and negative conversions are retained in the telescoping recovery below.

## 2. A decreasing bank on EVERY protected-character query tree

Let r_h be the number of still-queryable coordinates outside J at history h, and define B_h=r_h*a_J(f_h). For any next query i outside J, write b=fhat_h(J+i). Literal restriction coefficients fhat_{h,y}(J)=fhat_h(J)+(-1)^y*b give

    E_y a_J(f_hy)=a_J(f_h)-b^2,
    B_h-E_y B_hy=a_J(f_h)+(r_h-1)*b^2
                   >=E_y a_J(f_hy).                 (4)

This holds even when coefficients vanish and reference-only atoms appear. Multiplying (3) by the physical history reach and summing (4) over ANY finite adaptive tree, allowing early stopping and arbitrary branch-dependent next coordinates, proves

    Sum_h reach(h)*sigma_h
           <=ell*(B_root-E_terminal B_terminal)
           <=ell*r_root*a_J(f_root).                   (5)

In particular the initially priced reference and ALL later actual signed resets satisfy the normalized divergence payment

    K_J(root)+Sum_h reach(h)*sigma_h
          <=ell*(r_root+1)*a_J(root).                  (6)

Every internal node resets both children; if selected nodes omit reset, the next parent need not equal q^J and this proof must instead stop/restart with an explicitly priced conversion. We assert (5)-(6) for the reset-after-every-query policy and stopped subtrees of that policy. The query rule is arbitrary, but it never queries protected coordinates J. The bank is off-character spectral mass, not full variance: this distinction saves a near-character nonfactor source that variance would charge as order one.

## 3. Independently reconstruct A048's cumulative obstruction

Use its exact same family: k=N even>=10; delta=2^-N; chi(z)=(-1)^z1; g=chi reversed at z=e2,e1+e2. Let h(t,z)=g(z), with the sign also reversed at z=0 iff tail weight is 0 modulo3. Under tail restrictions h_{m,r} has mean -2delta*rho_m(r) and full coefficient -2delta*A_m(r). Literal binomial sums give rho_m(r)=2^-m sum_{w=r mod3} binom(m,w), A_m(r)=2^-m sum_{w=r mod3}(-1)^w binom(m,w). Writing C for the cyclic shift, C^3=I and (I-C)^3=3(C^2-C). Hence (I-C)^6=9(C+C^2-2I)=-27*(I-(I+C+C^2)/3). Since I+C+C^2 is the all-ones matrix J_3, T=(I-C)/2 satisfies T^6=-(27/64)(I-J_3/3). Thus A_{m+6}=-(27/64)A_m for m>=1, because sum(A_m)=0 there. The six vectors printed in A048's proof follow directly. At each even m all full coefficients are nonzero; adjacent squared pairs give biases 0 or absolute value >=3/5.

For q^FULL with alpha=1/6 the reference physical-outcome bias is exactly eta=(u*d_empty+(1-u)*d_full)/6. Since u<=4delta^2, two phases have |eta|>1/12, hence actual O>1/288. After two queried bits each residue has probability >=1/4; thus good reach >=1/2 at every later block. Sum first-query invoices over the (N-4)/2 later two-query blocks, retaining second-query invoices and erasures as nonnegative. Exact reset telescoping yields Sigma_core>(N-4)/1152-ell, and global reach1/4 gives Sigma_F>(N-4)/4608-1/15. The original source margin is <=8. At N65536 the last lower bound is 9059/640, hence deficit>3939/640 before old quarter. The support claim follows from nonzero even-phase full coefficients and preservation of matching support by the common kernel.

We also reconstruct its source and sparse/tensor assertions: h differs from chi on at most3delta, p_chi complement mass is between delta and12delta; partition entropy and pivotal-edge symmetric difference give H(h)<=12delta(3N+2)<=3/8 and 1-12delta<=I(h)<=2. The correlated selector of section4 has supplied CE<=3+CE(h,q)/4 and influence<=2, so its source is genuinely admitted and H/I stays bounded. Tensor actual laws and physical weights multiply, KL/reset sums add. In its guarded sparse activation the quotient retains its own entropy and surplus beta_l, with 0<=beta_l<=4alpha(l+1); active inherited product law has reach alpha. Thus the remaining margin equals beta_l+alpha*T*(M0-Sigma_F). Taking T=2^r,r>=3,l=2(r+1),alpha=1/(4T^2) makes this negative, while its influence tends to zero. This verifies the stated mechanism refutation without converting it into an FEI counterexample. Independent dense/phase/account certificates are in out/REVIEW_CHECK.json. Acceptance is conditional on that file recording PASS; no author code is imported or used.

## 4. A paid replacement on the SAME exhausted original owner

Now FIX alpha=1/6, J={z1} and the SAME h=h_N0. Let a=1-p_h(J). Its distinguished coefficient is 1-4delta-2delta*rho_N(0), so 1-6delta<=hhat(J)<=1-4delta, whence delta<=a<=12delta. In particular J is source-positive. The root FULL coefficient has magnitude <=2delta, so p_h(J)>p_h(FULL).

For fixed u, a spike on a source atom of mass s has KL

    K(s)=(1-u)*ell-s*log2(1+alpha*(1-u)/(beta*s)).

It is decreasing in s>0 since ln(1+x)-x/(1+x)>0 for x>0; continuity handles s=0. Consequently the actual conversion from the OLD full spike to the J spike has

    c=K_J(h)-K_FULL(h)<0.                            (7)

The conversion is explicitly executed and credited once. The original full-spike KL is not also refunded elsewhere.

Take the SAME original selector F: F=chi_a when x=0, F=h when x=b=1, F=+1 otherwise. The SAME original Q0 copies the actual zero-data/control/character sectors, and uses q_h^FULL(S)/16 at the four control copies of each nonempty data S. Query b, retain b0; query x in b1, retain the x0 character. The active h has reach1/4 and inherits EXACTLY q_h^FULL, including its unchanged empty mass. Inert a is contracted only after its zero-frequency support is verified. Original KL is A0=K_FULL(h)/4. Actual control-outcome and erasure releases here are zero, since likelihood depends only on the unchanged data mask and matches the empty sector. The two retained complementary terminals contribute total rate4 surplus 2.

At active h EXECUTE (7); then query ANY subset of the 2N-1 coordinates outside z1, in ANY finite adaptive order, resetting both children to q^J after each actual query and retaining ALL stopped terminals. Formula (6), with r=2N-1, gives the ORIGINAL inclusive KL-plus-conversion-plus-refresh bill

    A0 + c/4 + Sigma_later/4
       =[K_J(h)+Sigma_later]/4
       <=(2N)*a*ell/4<=6Ndelta*ell<1/64.                 (8)

The last strict inequality follows from ell<4/15, proved by 6^15<2^4*5^15, and N*2^-N<=10/1024 for N>=10. No original source reserve is restarted.

## 5. Recovery implication, separately proved

At every complete adaptive terminal frontier, E a_J(f_leaf)<=a by (4). Write D=2N and A=E a_leaf<=a<=12delta<1/2. For every leaf entropy partition at atom J gives H(f_leaf)<=h2(a_leaf)+a_leaf*D. Concavity of h2 gives E H<=h2(A)+D*A<=h2(a)+D*a. Since a>=delta and a<=12delta, h2(a)<=a*(N+2). Therefore

    E H(f_leaf)<=12delta(3N+2)<=3/8,
    E I(f_leaf)>=E p_leaf(J)>=1-a.

J is never queried, so it remains a valid nonempty frequency even at variable-depth leaves. Thus the FULL final selector surplus satisfies

    S=2+(4E I_leaf-E H_leaf)/4
      >=3-a-3/32>=741/256.                           (9)

Root mean Eh=-2delta*rho<=0, so t=Pr(h=-1)>=1/2. Direct physical influences give I(F)=1+t/2+I(h)/4. Its root entropy obeys H(F)<=3+H(h)/4. To verify the latter directly, the two a-character atoms contribute entropy 1. The four vacuum/control masses are two copies each of (1+mu)^2/16 and (1-mu)^2/16, where mu=Eh. Their entropy is at most 1+mu^2: the discarded correction is one quarter of sum_(sign) (1+sign*mu)^2 log2(1+sign*mu), which is nonnegative by convexity of x*log(x) applied to the two squared values of total at least 2. The four control copies of each nonempty data atom contribute Var(h)+H_nonempty(h)/4. Adding gives H(F)<=3+H_nonempty(h)/4<=3+H(h)/4. Hence the original PHYSICAL surplus, independently of any proposed supplier, is

    4I(F)-H(F)>=3-a-3/32>=741/256.                    (10)

Let e=H(F)-E H_terminal-4*(I(F)-E I_terminal) be the actual physical entropy/influence transfer, and Sigma=c/4+Sigma_later/4 the full signed conversion sum. There is no assumption e>=0. Algebra alone proves

    S-[A0+e+Sigma]_+
       =min(S,4I(F)-H(F)-A0-Sigma).                  (11)

Using (8)-(10), this is >737/256. Subtract ONE retained old booking omega in [0,1/4] to get

    S-[A0+e+Sigma]_+-omega >673/256.                  (12)

Equation (11) is the separately proved recovery implication; (6) supplies its quantitative normalized-divergence payment. Full terminal KL, erasure releases and actual outcome KL remain in the exact identity A0+Sigma=sum erasure+sum outcome+E final KL, including source-zero fair fallback if it occurs. No positive part is split, no negative conversion clipped, and no earlier debit removed. This theorem pays all the stated protected-character histories on the SAME admitted source that A048 showed unable to pay repeated FULL-spike refresh.

## 6. Scope and first unsupported universal line

This repair changes supplier and actually prices that change; it does not rescue the retired unlimited FULL-spike protocol. In this family p_chi at the root is source-positive; after arbitrary other-coordinate queries it may become zero, producing a reference-only spike. Equations (1)-(6) explicitly accommodate that case. Protecting z1 is essential to the stated bank. No claim pays querying it and then inventing a new anchor for free.

The first unsupported universal line is to supply, for arbitrary Boolean f, a useful protected character or paid decomposition whose ORIGINAL (r+1)*(1-p_f(J)) bank is bounded by a dimension-independent multiple of I(f), and to pay any later anchor change from that same diminished owner. Such a price is not proved here. Uniform spectra show this particular bound can be dimension-sized while the rule is still only a crude bound; do not identify failure of this upper bound with FEI failure. T=L/Z=H(v/Z)-log2 Z and all its normalizers remain unchanged; raw-L is retired. The symbol ell in this proof is only log2(6/5), never the collision raw L. Full FEI is OPEN; no universal constant improves.
