from pathlib import Path
P=Path('.')
proof=r'''
## A1. The proposed matching bound (MB) is false for every nonzero principal charge

This is a counterexample to our proposed sufficient hypothesis, **not** a counterexample to existence of the electric-field scaling limit. It invalidates the first attempt's suggestion that (MB) was a plausible target.

Recall W_epsilon(z)=exp(iTheta) a_s epsilon^(-s^2) exp(2pi i s h(f_epsilon(z))), with a_s>0 fixed and 0<|s|<1/2. For n positive insertions all lying in Q_epsilon(f), and n negative insertions all lying in Q_epsilon(g), the balanced product has expectation of modulus exactly

    a_s^(2n) epsilon^(-2n s^2) |E exp(2pi i n s (h(f)-h(g)))|.       (A.1)

Proof: the phase exp(iTheta) cancels, all n copies of the same cell value multiply, and their exponents add. No independence or approximation is used.

Fix epsilon=1/N, f=(0,0), g=(N,0). Their embedded cells are near 0 and (1,0). For N>=4 every cross distance |x_i-y_j| is at least 1/2. Thus the matching sum on the right of (MB) is at most

    n! 2^(2n s^2),                                               (A.2)

independently of N. The set of these insertion configurations has positive Lebesgue measure epsilon^(4n), and contains tuples of pairwise distinct continuum points. Therefore an almost-everywhere bound cannot exclude it.

### Rational charge: an exact contradiction, with no asymptotic theorem
If s=a/b in lowest terms, take n=b. Then ns=a is an integer. Since h(f)-h(g) is deterministic modulo Z,

    exp(2pi i a(h(f)-h(g)))

is deterministic of modulus 1. The left side of (MB) is exactly a_s^(2b) N^(2b s^2), which diverges. No fixed C_b,K can multiply the bounded expression (A.2) to dominate it. This works for any dimer measure with the pinned height convention, provided the two cells are present.

For the concrete charge s=1/4 (alpha=pi/2), n=4: the eight-point correlator on these open cell products has modulus a_s^8 N^(1/2). The proposed cross-pairing majorant remains at most 24 sqrt(2). This is the simplest exact example.

### Irrational charge: contradiction using only the verified two-point theorem
Choose an integer n>1/(4s^2). Write ns=k+t with k integer and -1/2<t<1/2. Because s is irrational, t is neither zero nor a half-integer. The exact charge-alias identity from ATTEMPT.md P1 shows that the modulus in (A.1) equals

    |E exp(2pi i t(h(f)-h(g)))|.

Dubedat Proposition 23, with complex conjugation if t<0, makes this asymptotic to A_t N^(-2t^2), with A_t>0. Hence (A.1) is asymptotic to

    a_s^(2n) A_t N^(2n s^2-2t^2).

Its exponent is positive: n s^2>1/4>t^2. It diverges while (A.2) stays bounded. Again no C_n,K exists. This irrational case uses the canonical zero-slope infinite-volume measure to which Proposition 23 applies.

These cases exhaust all nonzero s in (-1/2,1/2). QED.

### Referee checks
- n is fixed once s is fixed, before epsilon tends to zero. The constants allowed in (MB) may depend on n but not epsilon; divergence defeats any such constant.
- The bad set is not an equality diagonal. The distinct real insertion points can all occupy the same constant lattice cell; this is an open, positive-measure set for each epsilon.
- The cells remain macroscopically separated, so every *cross* distance is uniformly bounded below. Same-sign distances shrink; these are absent from the original matching bound.
- The arbitrary fixed normalization a_s does not change divergence. The additional random phase cancels exactly for balanced moments.
- Aliasing is applied to a fused charge, not incorrectly to an individual Gaussian vertex operator. The rational case is exact; the irrational case uses an already verified two-point asymptotic with a fixed reduced charge t.
- The exact contradiction does not say that integrated high moments diverge. The bad configuration set has vanishing volume; this is examined below.
'''
with (P/'SECOND_ATTEMPT.md').open('a',encoding='utf8') as f:f.write(proof)
p=P/'ATTEMPT.md';s=p.read_text(encoding='utf8');s=s.replace('# F0087 — mathematical attempt, 2026-10-11','# F0087 — mathematical attempt, 2026-10-11\n\n**Second-attempt correction:** the matching hypothesis (MB) in Section 7 is false for every nonzero principal charge for this piecewise constant embedding. See SECOND_ATTEMPT.md A1. The conditional implication remains logically valid, but is inapplicable to this dimer field.');p.write_text(s,encoding='utf8')
p=P/'CLAIMS.jsonl';rows=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines()] if False else []
print('Saved charge-fusion counterexample proof immediately.')
