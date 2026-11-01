# Early tag exposure spends a bank that the graft does not supply

All entropies are bits; all coordinates are uniform binary bits, with sign characters (-1)^x. This is a proof plus an exact finite certificate, awaiting independent review. It refutes a proposed extension, not full FEI and not the hidden-tag theorem of A062.

## Exact proposed extension and the obstruction

For Boolean signs u,v on ONE common data cube, a Boolean sign a on a disjoint seed cube, and one fresh fair tag w, set b=(u+v)/2, c=(u-v)/2, t=E c^2=Pr[u!=v], M=b+w c, F=b+w a c. For a complete prescribed physical tree T, Q_C(g,T) is the least nonnegative reserve, defined recursively by Q=max(0,H(g)-average H(children)-C Inf_i(g)+average Q(children)), with constant leaves zero.

A062's scoped graft transports R=t Q_C(a,T_a)+Q_C(M,T_M), allowing shared-data and seed interleaving while w stays hidden until the seed is constant. The extension tested here permits w first, then all seed bits, then the original ordered data completion, with the SAME R and no extra bank. This extension is false already for a non-point majority controller at C=32609/5000.

## Universal prefix formula, including both complete terminals

The w-free b sector and w-present ac sector have disjoint Fourier labels. In the latter, seed and data Fourier coefficients multiply. Thus H(F)=H(M)+t H(a), including coherent empty rows in b; there is no orthogonality assumption on u and v.

Expose w and every seed bit, and stop before touching the remaining data. Every terminal is exactly u or v. Each is reached with total probability 1/2 because w is an independent fair sign, even if a is biased. Therefore the full terminal entropy is E H_terminal=(H(u)+H(v))/2. Write D_w(M)=H(M)-(H(u)+H(v))/2.

For each fixed data x, if u(x)=v(x), the function is constant in w and all seed bits. If u(x)!=v(x), it is a sign times w a. Consequently Inf_w(F)=t, and the expected influence paid by all seed queries is t I(a), irrespective of the deterministic order. Each physical coordinate is queried once, including zero-influence queries if the seed becomes determined early. The exact stopped debt is therefore

    epsilon_C = H(F)-E H_terminal-C Pi_I
              = D_w(M)+t H(a)-C t (1+I(a)).                 (1)

Both terminals and every queried influence are present. No terminal is called free, and no inherited child reserve is assumed to vanish without a finite check. By recursive nonnegative-reserve inequalities, any complete continuation of this prefix has Q_C(F)>=epsilon_C when epsilon_C>0. This lower bound uses the existing reserve criterion, not whole-path debt of a complete tree. Completing all data would include later credits and is a different quantity.

## Explicit Boolean witness and exact spectra

Let k=10, N=2^k, r=2^(k/2), delta=1/N. Let u(x)=(-1)^(x0*x1+x2*x3+...+x8*x9). Let v agree with u except v(0)=-1 instead of +1. Let a be majority on three sign bits (equivalently a(z)=(-1)^1[|z|>=2]). Its four nonzero Fourier coefficients have magnitude 1/2; hence H(a)=2 and I(a)=3/2. Both children at its first query are nonconstant AND/OR functions, so this controller is not a point event or a parity mask.

The bent Fourier coefficients of u are +/-r/N, with multiplicities n_plus=(N+r)/2 and n_minus=(N-r)/2. Their squared mass sums to 1 and their signed sum is u(0)=1. The spectra used below are EXACT:

* u: coefficients +/-r/N; H(u)=k.
* v: (r-2)/N repeated n_plus; (-r-2)/N repeated n_minus.
* M: tag-absent (r-1)/N repeated n_plus and (-r-1)/N repeated n_minus; tag-present 1/N repeated N.

These formulas retain the coherent constant coefficient; they come from uhat-minus-delta and uhat-minus-2delta, not an incoherent mixture. In each list the sum of coefficient squares is exactly 1; r>2 for every tested k, so no logarithm of zero occurs (the replay also explicitly skips zero terms in general). H is the sum of h(q)=q log2(1/q) over squared coefficients.

Integer Walsh and direct edge counts in BENT_EXACT certify Q_C(a,seed order)=0 and Q_C(M,data0..data9 then tag)=0, EXACTLY, at C=4,32609/5000,8. Interval upper endpoints for all those root reserves are zero. The prescribed complete early tree exposes tag, then seed0,seed1,seed2, then data0..data9. Its reserve interval at C=32609/5000 is positive. The independent closed-coefficient calculation of (1) encloses epsilon between

    5511213292348743 / 295147905179352825856
and 5511213292348745 / 295147905179352825856.

In particular epsilon>1/100000, checked by integer cross multiplication. The inherited R is zero and cannot pay this prefix. The raw tree lower and upper endpoints and closed-prefix endpoints overlap as a consistency check; the strict sign follows from the separate closed lower bound, not from interval overlap.

## Actual partial core history, without a renewed bank

Start from the same construction with bent12 and the SAME majority controller and tag. Exposing the first data pair x0=x1=0, probability 1/4, leaves exactly bent10 with its zero-vertex edit, the same unexposed majority3 and the same tag. The identity is checked on all 1024 remaining data inputs. Under the prescribed data-first profile tree, this child is precisely the already computed M10 node; its complete profile reserve is zero, as is the seed reserve. No profile is restarted or replenished. This gives an actual partially exposed shared-core frontier where the proposed local extension fails. We do not assert that the original bent12 root has positive stopped debt after its earlier data-query credits: that is a different claim, and those credits must be retained if one starts there.

## Linear growth of actual expected unpaid cost

For every positive integer L take a product G_L of L disjoint copies of this 14-variable F. This is an actual Boolean family on 14L variables. On each module expose its tag and three seed bits; query all 4L such coordinates and stop before any module data. The order may process modules sequentially. Fourier entropy and influence add under products on disjoint physical blocks, including at every terminal. Thus root H, expected complete terminal H, and queried influence each add. Equation (1) gives

    H(G_L)-E H((G_L)_terminal)-C Pi_I = L epsilon > L/100000.

The supplied module banks sum to zero. Any complete physical tree extending this prescribed prefix therefore has least nonnegative root reserve at least L epsilon, by averaging the recursive reserve inequality to the stopping cut and discarding only NONNEGATIVE frontier reserves. All paths carry their exact uniform probabilities; there is no rare-path-to-expectation inference. The terminal product spectra remain in the displayed expectation. This gives unbounded ABSOLUTE unpaid cost for the proposed zero-bank extension. Root influence also scales with L; no unbounded H/I ratio or FEI counterexample follows.

## What remains

The all-dimensional unpaid line is to supply extra signed source capacity for early tag exposure, or to select a policy that keeps the tag hidden/changes order and is globally payable. At least epsilon per module is necessary for this particular early policy at C=6.5218. A pointwise zero-bank extension of the hidden-tag graft is excluded. A062's actual late-tag theorem and every existential good-rule claim remain intact. A087/A094 should independently reconstruct the closed coefficient multiplicities, complete zero-profile certificates and product-prefix argument. No independent acceptance or full Lean certification is claimed.
