# A073 stage18: a genuinely changed nonempty profile

All entropy, cross-entropy and KL are in bits. This proves a scoped reset theorem, not full FEI. Independent review is pending.

## Statement and physical scope

Take A050-CORRELATION-PRESERVING-SIGNED-LIFT@1, with h a product of disjoint point signs of arbitrary heterogeneous widths r>=2. Use its specified initial complete lifted reference Q and retain its original signed account and old eligible booking 0<=omega<=1/4. Query b, keep b0, and in b1 query at most ONE data coordinate. At any selected resulting leaves expose x, keeping BOTH children and all complementary leaves. On the x1 core child replace the actual inherited reference by the product of the fresh restricted point-factor references. The signed reset cost is nonpositive. Subsequent arbitrary finite data-query trees in these core children, with that fresh factor reset after each query, also have nonpositive reset costs. All final entropy and KL bills remain included. At unchanged rate4 the SAME signed owner retains >=3/4 bit after the old quarter. The supplier and frontier hypotheses are verified for this point-tensor family; no arbitrary-core supplier is asserted.

The restriction to one incoming data coordinate is essential to the derivation here: the initial attempted cumulative-erasure formula is FALSE after two sequential unreset queries. TRANSPORT_OBJECTION.json contains an actual width4 counterexample. The reset claim itself is not refuted by that objection; the wider incoming-prefix application is left open in this stage.

## Exact local computation

A width-r point sign has defect v=2^-r, p(empty)=(1-2v)^2, and p(s)=4v^2 on each nonempty set. Its reference is q(empty)=p(empty), q(s)=(7/8)p(s)+(4v(1-v)/8)1_full(s). This is normalized and has complete support for r>=2. Under one coherent data observation, the killed child is constant and its inherited reference is delta_empty. A surviving width1 child is a character and its inherited reference is delta_full. These resets cost zero. Untouched factors also cost zero.

For a surviving queried factor of remaining width k>=2 let u=2^-k, v=u/2, h=u-v, z=(1-2u)^2, D=1-4v+4vu. Erasing the queried frequency and multiplying by the actual child/source likelihood gives unnormalized masses

    r0 = z*(1-v*h/(2D)),
    rordinary = (7/2)*u^2,
    rfull = u/2+(7/2)*u^2-v*u/2,
    Z = sum r = 1+h^2/(2D).

Normalize by the ACTUAL Z. The fresh reference has masses z, (7/2)u^2, and u/2+3u^2 respectively. Direct summation against the actual child spectrum gives the signed reset price

    E*ln2 = L
          = z ln(1-v*h/(2D)) +4u^2 ln(1+h/(1+6u))
            -ln(1+h^2/(2D)).

This expression also has a useful algebraic certificate on the larger parameter rectangle 0<u<=1/4, 0<v/u<=1/2. That rectangle is an algebraic inequality, NOT an assertion about sequential multi-query physical transport.

Put kappa=v/u, D=1-4*kappa*u+4*kappa*u^2 and h=(1-kappa)u. Elementary logarithm bounds ln(1-a)<=-a, ln(1+b)<=b, and ln(1+c)>=c/(1+c) give

    L/h <= -z*v/(2D)+4u^2/(1+6u)-h/(2D+h^2)
         = -u*P/[2D*(1+6u)*(2D+h^2)],

where

    P=z*kappa*(1+6u)*(2D+h^2)
      +2D*(1-kappa)*(1+6u)-8D*u*(2D+h^2).

The exact Bernstein certificate divides the rectangle into 16 boxes. Every coefficient is positive; the smallest is 385/1024. Each polynomial is a convex combination of its Bernstein coefficients, so P>=385/1024 throughout the rectangle. Also D<=1, h<=1/4 and 1+6u<=5/2, giving denominator <=165/16; h>=u/2. All logarithm arguments and denominators are positive (D>=1/2, v*h/(2D)<1). Thus

    L <= -(7/384)u^2,
    E = L/ln2 < -(7/384)u^2 < 0.

No numerical precision refinement is involved. For width3->width2 the independent exact comparison is

    E=(1/4)log2(849408000/860934420)<-1/256,
    2*849408000^64 < 860934420^64.

The full/ordinary nonempty mass ratio changes strictly when h>0, so this is not merely an empty-atom calibration.

## Lifted transport and original account

After b1 the actual function is the selector of the a character and h. The character frequencies contain a; all core frequencies do not. Their supports remain disjoint until the stated x query. On a data observation the core part inherits the actual core coherent reference, while the character part only changes its scalar weight. For the ONE incoming data observation, the x1 child therefore has the normalized r above, tensor the untouched block references. Its x0 sibling has the exact character reference. This factorization was checked atomwise from actual truth tables, including a nonflat width4->width3 core child. No sibling or reference-only row is deleted.

Once the core is reset to fresh factor references, each further data observation is again the one-step calculation above. Product structure and disjoint blocks give closure by induction over arbitrary finite adaptive data trees. Negative reset prices add with actual physical reaches; they do not create a fresh copy of the original source bank.

Write A=D(P_root||Q_root), e=Hroot-EHleaf-4(Iroot-EIleaf), S=E(4Ileaf-Hleaf), and M=4Iroot-CE(P_root,Q_root). A050 gives M>=1 and the exact identity S-(A+e)=M. Let Ztot be the sum of all physically weighted signed reset prices. Reference KL chain rules, retaining every terminal KL, replace the complete liability by A+e+Ztot. The local result gives Ztot<=0. Consequently

    S-[A+e+Ztot]_+ = min(S,M-Ztot).

The retained b0 contributes1 to S. Every unchanged selector frontier has surplus>=2; each x child pair has mean surplus>=2 because its character contributes4 and the point-tensor core has nonnegative rate4 surplus. Further core data queries preserve nonnegative core surplus, and the character siblings remain. Thus S>=2 on the entire permitted frontier. Subtracting the old omega<=1/4 leaves >=3/4. Both terminals' full entropy and inherited/fresh KL costs remain included; using A+[e]_+ would be a different, unsupported conservative assertion.

## Validation and first unsupported line

code/bernstein.py checks 384 exact Bernstein coefficients in16 boxes, minimum385/1024, and the integer comparison above. code/physical.py independently constructs actual Boolean truth tables and Walsh spectra for widths (2),(3),(4),(2,3),(3,3), checks every prefix of length0 or1, both outcomes, and every next core coordinate/outcome after fresh reset. All45 frontiers,320 continuation children and595 exact assertions PASS in1.50 seconds; fixed16-term atanh bounds certify all required logarithm signs and the complete remaining >=3/4 account. The prior failed batch helper and its frozen spec are preserved. No Lean check or independent-agent acceptance is claimed.

First unsupported line for a universal conclusion: construct and price the complete reference for an arbitrary Boolean core, and certify arbitrary later controller/collision frontiers from the same original account. The additional technical gap at this stage is arbitrary sequential UNRESET prefixes before x; the failed cumulative-erasure identity cannot bridge it.
