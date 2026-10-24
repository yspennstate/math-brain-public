# FEI handoff — account01/B14 high-influence selector reduction

Source scientific package:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T063833Z-high-influence-selector/`

Scientific report commit at first publication: `3578bd119c619615b390c480507bdda0606ca104`.
Checker blob: `2d7665e3b269ca9e92cd965465578ae8ce9ddc0c`.
Output blob: `0866fafef93c68ef03b3a891184e056e0df42061` (`PASS`).

Classification: `ESSENTIAL_STEP_APPLIED`. Full FEI remains OPEN.

## New theorem

For the live center

`C^dagger = 6.521851214`, `a^dagger = 4(C^dagger-6.4548)=0.268204856`,

if FEI at `C^dagger` is false and `f` is a minimum-dimensional counterexample, then

1. `Inf_i(f) < 1741/10000 = 0.1741` for every original coordinate;
2. every one-coordinate cofactor `f_{i=b}` is noncharacter.

Equivalently, in balanced-uniform margin units, any minimum-arity gate with `c_G>a^dagger` must be diffuse-influence and cofactor-prime.

## Mechanism

Use the exact fresh-character lift `g(y,x)=(-1)^y f(x)`. It preserves `H(g)=H(f)` and gives `I(g)-1=I(f)`, while every restriction at an original coordinate is balanced. The account01/B15 sharp posterior-credit cocycle therefore yields at a uniform original-coordinate pivot with disagreement `d=Inf_i(f)`

`local gluing >= F(d) = C^dagger d - 1 - h_2(d) + Theta(|1-2d|)`.

The new scalar proof shows `F(d)>0` for every `d>=0.1741`. The exact rational checker certifies

- `F(0.1741) > 0.000124952707245502`;
- `F'(d)>1.390410224556456926` on `[0.1741,1/2]`;
- `F(1/2)=1.260925607` and `F` is increasing above `1/2`.

Minimum dimension makes both lower-dimensional children safe, so any coordinate of influence at least `0.1741` is a valid physical singleton selector and contradicts minimality.

For the character-cofactor branch, the exact named other-account input is account04/B17 `20260922T061604Z-character-cofactor-local-threshold/REPORT.md`, which proves the exact character-cofactor threshold `Q(d)<5.1`. After the high-influence branch has already forced `d<0.1741<1/2`, this theorem applies directly and excludes every character cofactor at the live center.

## Obstructions retained

Addressing is caught by a true address coordinate of influence `1/2`; the theorem does not claim every coordinate pays. Large majority, tribes and diffuse tensor constructions can survive the new hard-core conditions and are not silently excluded. Rare-gating density alone is not used; account02/B17's counterexample to that shortcut and account03/B18's nonamplification theorem remain compatible.

## Next exact arrow

The first unpaid class is

`max_i Inf_i(f) < 0.1741` and every `f_{i=b}` noncharacter.

A successor should construct a genuinely physical multi-coordinate block selector (or a bounded noncircular potential) for this diffuse cofactor-prime class. Do not spend another run reproving the high-influence scalar threshold.
