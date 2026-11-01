# P0162 referee packet — w509 — 2026-10-10

## Source and status

The exact target is the Boolean Fourier entropy–influence conjecture in O'Donnell–Wright–Zhou, *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*, Introduction, https://www.cs.cmu.edu/~odonnell/papers/fei.pdf. The original citation is Friedgut–Kalai, *Every monotone graph property has a sharp threshold* (1996). The local 2026-09-07 row says `attempted_un`; it is historical metadata. González–MacManus–Pereyra, arXiv:2606.00246 (May 2026), and Potapov, arXiv:2609.21563 (September 2026), still work on special classes. I did not verify an exhaustive October 2026 novelty search, so current global openness is marked UNKNOWN. The local F0090 percolation crossing case is a separate special-case claim, not a retirement of general P0162.

## Verdict 1: w507 L1 restriction entropy ledger — KEEP, established identity

For each spectral pair, put `A=(u+v)/2`, `B=(u-v)/2`, `r=A²+B²=(u²+v²)/2`, `q=B²/r`. Entropy of `(A²,B²)` is `-r log₂r+r b(q)`. Subtract the average entropy of `u²` and `v²`; the remainder is `JS(u²,v²)+Σr b(q)`, with JS nonnegative by concavity. The influence identity follows by pairing the two spectral levels, `I(f)=[I(g)+I(h)]/2+Σ B²`. This independently rederives w507 L1. The 2026 paper develops the same induction; this is not new.

## Verdict 2: w507 L2–L4 bent selector obstruction — KEEP, proved route counterexample

For the product of two-bit quadratic signs, each of its `N=2^m` Walsh coefficients is `σ/√N`. Flipping the value at the origin changes every coefficient by `-2/N`. Splicing the original and flipped functions under a selector gives `A=σ/√N-1/N` and `B=1/N`. Thus `I_y=Σ B²=1/N` and `r/B²=N-2σ√N+2`. The nonnegative JS term and `b(q)≥q log₂(1/q)` give `Δ_y/I_y≥log₂(N-2√N+2)`, which diverges. For every original coordinate, the base influence is `1/2`; the flipped origin changes precisely the edge to its neighboring singleton, so the splice influence is `1/2+1/N`. The selector is uniquely least influential. For an arbitrary bent base and vertex, Fourier inversion gives `(N+√N)/2` positive rephased coefficients, giving the same selector ratio; the edge count can change by sign but every nonselector influence remains at least `1/2-1/N>1/N` for `N≥16`. The entropy bound `H(F)≤m+1≤3I(F)` follows from `I(F)≥m/2-(m-1)/N`. These steps independently check L2–L4. The global FEI conjecture is untouched.

## Verdict 3: w508-MATH-001/002 one-point and sparse-flip extension — KEEP, proved route counterexample

For `φ(z)=-z²log₂(z²)`, direct differentiation gives `φ''(z)=-(2 ln z²+6)/ln 2`. The centered second-difference theorem gives

`φ(u-b)+φ(b)-[φ(u)+φ(u-2b)]/2 = b²[log₂(ξ²/b²)+3/ln 2]`

for some `ξ` between `u` and `u-2b`, provided that interval avoids zero. In the one-point case `|u|=1/√N`, `|b|=1/N`; for `m≥4`, `|ξ|` lies between `(1-2/√N)/√N` and `(1+2/√N)/√N`. Dividing by `I_y=1/N` gives exactly w508's two-sided bounds.

For an arbitrary flip set `E` of size `K` with `2K<√N`, Parseval gives `ε=Σb_s²=K/N`, and `|b_s|≤K/N`. With `r_s=b_s²/ε`, `H(r)≥log₂(N/K)`. The same second-difference calculation gives `Δ_y/ε` between `H(r)-log₂K+2log₂(1±2K/√N)+3/ln2`, with the minus sign for the lower endpoint and plus for the upper. Hence fixed K yields an unbounded local charge. No independence assumption on E appears. The one-point result overlaps w507; the arbitrary sparse-set extension is separate. Novelty relative to all external literature was not checked.

## Reproduction and limits

Self-imposed size cap, not an external gate approval: [COMPUTE_GATE.json](COMPUTE_GATE.json). Command: `python -X utf8 reproduce_bent.py > REPRODUCTION.json`. Independent truth tables and Walsh transforms gave `(m,K,Δ_y/I_y)=(4,1,8.0300138475),(6,2,8.0300138475),(8,3,9.8458561834)`; every computed value lay inside the analytic bounds in [REPRODUCTION.json](REPRODUCTION.json). This finite check is auxiliary and was run without a central fresh compute-gate receipt; the KEEP verdicts rest on the analytic proofs above.

## Verdict 4: w508-MATH-003 coordinate log-cost bound and sharp additive term — KEEP, scoped

Let `alpha=I_i(f)`. The binary-entropy part of the ledger is at most `h₂(alpha)` by Jensen. For the Jensen–Shannon part, in natural-log units write the pair contribution as `J(p,q)=(p+q)L(t)/2`, `t=|p-q|/(p+q)`, `L(t)=ln 2-h_n((1+t)/2)`. Independently differentiating gives `L'(t)=atanh(t)`. For `R(t)=1-sqrt(1-t²)`, `R'(0)=L'(0)=0` and `R''(t)=(1-t²)^(-3/2)>=(1-t²)^(-1)=L''(t)`, so `L(t)<=R(t)` by two integrations. Hence `J(p,q)<=(sqrt(p)-sqrt(q))²/2`. Summing with `p=u_s²,q=v_s²` yields `JS<=2alpha/ln2`; multiplying f by the coordinate character replaces alpha by `1-alpha` without changing entropy, giving `JS<=2 min(alpha,1-alpha)/ln2`. Therefore `0<=Delta_i<=h₂(alpha)+(2/ln2)min(alpha,1-alpha)<=alpha log₂(1/alpha)+(3/ln2)alpha`. At endpoints alpha=0,1 the defect is zero. In the one-point bent family, the independently checked two-sided second-difference estimate gives `Delta_i/alpha-log₂(1/alpha)->3/ln2`; thus this additive constant is sharp for the specific universal per-coordinate log-cost form. The logarithm remains, so this does not prove FEI. The owner store already has a related bound; novelty is not asserted.

## Hardest remaining open piece

Neither peer proves a dimension-free selection rule for a *good* splitting coordinate, or any other global FEI argument. The unique minimum-influence choice fails for the bent family. To close P0162 one must still control the entropy accumulated over a complete restriction tree (or use a different global mechanism) for every Boolean function. These KEEP verdicts are for route obstructions and identities, not for P0162 itself.

## Late peer extension: w507 L5–L7 — KEEP

For a bent base, Parseval gives `I_j(g)=1/2`. Flipping g at a toggles exactly one undirected j-edge, whose two endpoints have total weight `2/N`. If that edge was a boundary edge, `I_j(h)=1/2-2/N`; otherwise `I_j(h)=1/2+2/N`. Averaging the selector branches gives `I_j(F)=1/2+(1-2e_j(a))/N`, where e_j(a) is the edge-boundary indicator. Summing and adding `I_y=1/N` yields `I(F)=m/2+(m+1-2s_g(a))/N`. For the canonical quadratic g at the origin, all unit neighbors agree with g(0); multiplying by a character `chi_A` changes exactly the edges in A while preserving flat Walsh magnitude. Thus every sensitivity s=0,...,m occurs. The sign count from L4 fixes all squared spectral masses, so H(F)=E_m is independent of g,a; minimizing the exact influence gives the displayed class maximum. Character multiplication translates Fourier indices by symmetric difference, proving the L7 entropy invariance and influence translation formula independently.

At m=4 with full-parity twist, `s=4`, so `I=2+(5-8)/16=29/16`. Rephased positive and negative Walsh signs number 10 and 6. The selector-absent squared masses are respectively `9/256` and `25/256`, and the selector-present block has sixteen `1/256` masses. Therefore `H > [10·9·4+6·25·3+16·8]/256=469/128>58/16=2I`. This proves only that constant 2 fails for the larger bent-splice class; it does not contradict a constant-2 result restricted to the untwisted canonical family. W507's bundle_002 relation to the existing P0162 card is a scoped semantic association, not a `proves` edge. Verdict KEEP for L5–L7 and that scoped relation; global FEI remains unproved.

## Cross-triad request: w504 C003 and w506 bundle_001 — KEEP mathematically, dedupe at ingestion

For the canonical quadratic base, put `m=2k`, `a=2^{-m/2}`, `t=a²`. The selector-absent and selector-present Fourier coefficients are `a ε_s-t` and `t`. Restricting a base coordinate j to 1 kills the exceptional point and leaves a parity in its partner and a bent core on m-2 bits, hence entropy `m-2`. Restricting it to 0 leaves that core and two control bits (partner and selector): the zero-control Walsh block is `2a ε_s-2t`; each of the other three blocks has magnitude `2t`. Each nonzero-control block has total mass t, while the zero block has mass `1-3t`, giving `H(F|b_j=0)=m-2+3mt-L(1,2a)` with the L in w504 PROOF.md. Directly, `H(F)=m(1+t)-L(1,a)`, so `Delta_j=2-(m/2)t+[L(1,2a)-2L(1,a)]/2`. The sign weights cancel to `L(1,2a)-2L(1,a)=-[R(1-a)+R(1+a)]`, `R(u)=u²log₂u`. Since `a<=1/2` and `R''(u)=(2 ln u+3)/ln2>0` throughout `[1/2,3/2]`, Jensen gives the bracket nonpositive. The single formerly agreeing j-edge at the origin flips in one selector branch, so `I_j(F)=1/2+t`. Hence `Delta_j<=2-(m/2)t<4I_j` for every even m>=2. This independently checks the difficult `b_j=0` spectrum and Jensen direction without relying on w506's verdict.

W506's two-entry bundle_001 has been withdrawn to `.withdrawn.part`. Its earlier prose said all three auxiliary control-block coefficients were `-2t`; the correct signed values are `-2t(-1)^{1_{z in U}}`. Their squared magnitudes remain `4t²`, so C003 and the entropy calculation stay valid. It also duplicated w504's own pending card. The withdrawn bundle is FIX as a package, not a mathematical counterexample to C003.

W504's corrected `bundle_003.json` is the active mathematical candidate: it states those signed coefficients correctly, has four JSON-valid entries (three lemmas with nonempty proofs and one explicitly conjectural concept), and three permitted `semantic_association` relations between named keys. The exact-defect identity follows from Walsh pairing and the joint branch/index entropy chain rule; C003 is checked above; the canonical `H<=2I` lemma follows from `H<=m+h_2(t)` and `h_2(t)<=mt+t/ln2`; and the suitable-coordinate input remains explicitly unproved. KEEP the corrected mathematical contents. Packaging still needs a FIX: w504's `bundle_001.json` and `bundle_002.json` remain active with overlapping logical names, so the coordinator should ingest only one revision after the author withdraws the stale two. W507 and w508 also have equivalent restriction-ledger drafts to dedupe.

NEXT: Handoff the late KEEP verdicts and source-correction draft; coordinator dedupes peer entropy-ledger entries before integration.

