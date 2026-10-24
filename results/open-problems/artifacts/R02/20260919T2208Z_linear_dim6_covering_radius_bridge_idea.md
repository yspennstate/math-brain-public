# R02 idea note — published dimension-6 covering radii eliminate every linear antipodal improvement through n=63

Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

This is an idea/provenance note written before any possible checker. No new checker is needed for the core argument below because the only finite theorem used is already a published exact covering-radius theorem and the remaining deductions are elementary integer inequalities.

## New route

Section-B moves used for this run are **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME**.

The previous R02 run reduced complement-closed linear row-code constructions to a low-dimensional covering-code problem and independently self-checked a Walsh-signing obstruction for dimension at most five. Instead of extending that finite search, look up the same least-covering-radius numbers in coding theory.

Tsonka Baicheva and Iliya Bouyukliev, *On the least covering radius of binary linear codes of dimension 6*, Advances in Mathematics of Communications **4** (2010), 399–404, DOI `10.3934/amc.2010.4.399`, define `t_2[n,k]` as the minimum covering radius among binary linear `[n,k]` codes. Their Theorem 4.1 proves

\[
t_2[n,6]=\left\lfloor\frac{n-8}{2}\right\rfloor,\qquad n\ge18.
\]

The paper also explicitly says that the values for dimensions up to five had already been determined in earlier literature. This is important provenance: the preceding R02 dimension-at-most-five Walsh theorem remains a valid independent proof in the narrower complement-closed setting, but its broad low-dimensional covering-radius content must not be presented as a novelty claim.

## Consequence for the R02 antipodal linear route

For a sign matrix with rows `r_i`, the associated antipodal code is

\[
C_A=\{r_i,-r_i:1\le i\le n\}\subset\{\pm1\}^n,
\]

and the exact dictionary retained in R02 is

\[
\operatorname{disc}(A)=n-2R(C_A).
\]

Suppose this antipodal code is binary linear and has at most `2n` words. For `32<=n<=63`, its dimension `k` satisfies `2^k<=2n<128`, hence `k<=6`.

* If `k<=5`, the preceding R02 theorem gives discrepancy at most `6` for even `n` and at most `5` for odd `n`.
* If `k=6`, Baicheva--Bouyukliev gives
  \[
  R(C_A)\ge t_2[n,6]=\left\lfloor\frac{n-8}{2}\right\rfloor.
  \]
  Therefore
  \[
  \operatorname{disc}(A)\le
  \begin{cases}
  8,&n\text{ even},\\
  9,&n\text{ odd}.
  \end{cases}
  \]

Neither can beat the current R02 witness. Indeed, for even `n>=32`,

\[
\frac{8}{\sqrt n}\le\frac8{\sqrt{32}}=\sqrt2<\frac7{\sqrt{17}},
\]

and for odd `n>=33`,

\[
\left(\frac9{\sqrt n}\right)^2\le\frac{81}{33}=\frac{27}{11}<\frac{49}{17}=\left(\frac7{\sqrt{17}}\right)^2,
\]

where the last strict inequality is the exact integer comparison `27*17=459 < 539=49*11`.

Combining this with the preceding dimension-at-most-five result yields the clean handoff statement:

> **No complement-closed binary linear covering-code construction with at most `2n` codewords can improve the explicit A17 bound at any order `n<=63`.**

The first order at which this construction class can have dimension seven is `n=64`, where `2n=128`. Thus a future linear-code attack, if I0095 is ever lawfully reactivated, should start at dimension seven / order at least 64 rather than repeat any dimension-at-most-six search.

This is a route-elimination / prior-art synthesis only. It does **not** improve the fixed source metric `7/sqrt(17)` and does **not** close Randomstrasse Open Problem 11.
