# Integer mixed-difference packet payment

All logarithms are natural. Let f:{0,1}^n->{-1,1}, with arbitrary independent interior biases p_i. Write v_i=4p_i(1-p_i), v_S=product v_i, P(S)=fhat(S)^2, c_S=fhat(S)/sqrt(v_S), Delta=sum_nonempty(|S|-1)P(S). Define h(t)=t^2 ln(1/t^2), h(0)=0. The corrected natural coefficient charge is E_S=v_S h(c_S).

## 1. Integer-profile lemma, no affine or arity assumption

For nonempty S, k=|S|, define the actual mixed-difference profile on the complementary physical inputs by

    Z_S(x_notS)=(1/2) sum_{b in{0,1}^S} (-1)^(k-|b|) f(b,x_notS).

Every Z_S is integer-valued: the even number2^k of signed Boolean summands has an even sum. Z_S=2^(k-1) times the normalized physical mixed derivative. Integrating independent centered coordinates gives

    m_S=E Z_S=2^(k-1)c_S,
    Var(Z_S)=(4^(k-1)/v_S) sum_{T strictly containing S}P(T).

The second identity is exact Parseval of the physical complementary-coordinate profile; it preserves all signs before squaring. It is not a reset to independent component references.

For any integer-valued random variable Z with finite variance, let m=E Z, t=|m|. If t>=1, h(m)<=0<=2Var(Z). If0<=t<=1, pointwise Z^2>=|Z| implies E Z^2>=|E Z|=t, so Var(Z)>=t(1-t). Also t^2ln(1/t^2)<=2t(1-t), by ln(1/t)<=1/t-1. Therefore, for every such profile,

    h(E Z)<=2Var(Z).

No range cap {-1,0,1}, low-degree assumption or affine dependence is needed. Multiplying by v_S/4^(k-1) and splitting the scale logarithm proves the universal local payment

    E_S <= (k-1)ln4*P(S)+2 sum_{T strictly containing S}P(T).       (1)

All sums involve actual physical Fourier packets of the SAME Boolean function. The inequality remains meaningful if the residual charge is negative. In particular, pair coefficient amplitudes near1 must not be artificially capped at1/2; integer profiles also cover these cases.

For k=2 the pair residual E_S-ln4P(S) is at most twice its actual strict-superset mass, irrespective of how many remaining coordinates the profile depends on. This generalizes A043's affine/difference normalization payment, including its requested two-coordinate profiles. At k=1, summing(1) is exactly E_single<=2sum_{|T|>=2}|T|P(T)=4Delta-2R, with R=sum_{|T|>=3}(|T|-2)P(T). Thus singleton and pair charges are not independent new reserves: their funding multiplicities must be added.

## 2. Degree-three audit and A043 scoped acceptance

If f has Fourier degree at most3, write B=sum_{|S|=2}P(S), T=sum_{|S|=3}P(S), Delta=B+2T. Equation(1) gives

    E_single<=4B+6T,
    E_pairs<=ln4*B+6T,
    E_triples<=ln16*T.

The last line follows directly from the integer constant profile at degree3; its variance is zero. The two different6T charges are BOTH included. Their sum proves

    E<=(4+ln4)B+(12+ln16)T
      =(4+ln4)Delta+4T <=(6+ln4)Delta.                 (2)

This is an independent proof of the upper-bound clause of A043-COHERENT-QUADRATIC-PRIME-PAYMENT@1, because its actual gate is the degree-three polynomial -1+2z+2xy-2z[ax+(1-a)y]. In bit units the constant is2+6/ln2. It does not require that gate's affine case split, the sharp endpoint source, own mux theorem or polynomial slack surrogate. No source repair is supplied. Review accepts the upper theorem, exact higher-degree ledger and its elementary disjoint-composition consequence; the bundled lower-path and polynomial-witness clauses are outside this stage's acceptance.

The degree-three bound is an algebraic consequence of the local mechanism, not a novelty assertion about bounded-degree FEI. Genuine disjoint composition of gates satisfying(2) retains that same constant at every depth, fan-in and induced independent child law: exact corrected entropy and deficit both decompose with weights w_j=I_j(g)/Var(child_j)>=0. Constant children are contracted. This consequence applies to repeated degree-three prime56067 gates and previously admitted gate families at this constant; it does not prove a bound for arbitrary gates of large degree.

## 3. Explicit congestion and first unsupported universal line

Summing(1) over ALL nonempty S yields the exact available upper ledger

    E <= ln4*Delta+2 sum_{|T|>=2}(2^|T|-2)P(T).         (3)

The count2^|T|-2 is the number of nonempty proper submasks of T. It is not a dimension-independent multiple of |T|-1. Even restricting to pairs charges each degree-d packet binom(d,2) times:

    sum_{|S|=2}[E_S-ln4P(S)]
      <=2 sum_{|T|>=3}binom(|T|,2)P(T).               (4)

Consequently this stage supplies the missing cofactor-compatible LOCAL assignment but not bounded congestion. Its first unsupported universal line is a signed/conditional allocation or rebate replacing these multiplicities by an absolute multiple of degree deficit while retaining full higher-degree/terminal entropy. A scalar allocation that simply forgets multiplicities is invalid.

An actual parity character on d physical fair inputs has only P([d])=1. The pair ledger(4) assigns cost d(d-1), while Delta=d-1, so the price/Delta=d. All pair means are exactly zero and their actual residual entropies are zero; the paid variance budget is completely wasteful. The full ledger(3) has cost2(2^d-2) although actual entropy is zero. This actual Boolean family proves that adopting the unmodified local upper ledger as the universal cost cannot work. It is not an FEI counterexample and does not refute(1). A viable selection/refund must detect these vanishing means and preserve cancellation rather than pay every profile variance.

NEXT: keep exact h(m_S), not its worst-case2Var majorant, and select joint pair profiles using one signed conditional reference. Test whether the selected complete-set cost, including terminal entropy and the returned parity budget, can be charged once to degree deficit. This directly advances C020/B09's cofactor payment interface; another all-bias grid cannot resolve the congestion obstruction.
