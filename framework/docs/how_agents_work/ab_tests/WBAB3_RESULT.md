# WBAB3 result (scored 14 Nov 2026)

Rules: WBAB3_PREREG.md (committed before any page existed). Twelve Codex writers (gpt-6.1-sol high, normal
speed), four per arm, three tasks, 36 pages; four blind Codex judges each ranked all 12 pages of each task (1 best).

## Primary: B- (no word walk, stem check) vs C (no brain)
Mean rank B- 6.40, C 5.73; Mann-Whitney U=80, one-sided p=0.69
for B- better. Flags B- 3, C 3. B- does not win.

## Second: B (WBAB2's brain) vs C
Mean rank B 7.38, C 5.73; U=100, one-sided p=0.95 for B better
(the gap runs the other way, two-sided about 0.10). Flags B 2, C 3. B does not win.

## Secondary prediction
Stems in 3+ paragraphs per 100 content words: C 3.59, B 4.76, B- 2.46. B- below B: holds.
Across the 36 pages the measure against worse mean rank: Spearman -0.005 (p 0.98): fails.
So the word walk does raise stem repetition, but stem repetition did not predict how the judges ranked pages here;
the WBAB2 pattern did not replicate.

## Room to fail
Room to fail: per-page mean ranks across the four judges have sd 2.74, so a one-sided p<0.10 with 12 pages per arm needed about a 1.4-place gap (of 12) in the arm's favour; B- came out 0.67 places the other way. Neither ceiling nor floor: the test could have shown a win.

## Judges
Median inter-judge Spearman by task: page1 0.32, page2 0.67, page3 0.39 (WBAB2 with two judges: 0.05-0.48).

## Tokens
Writers: C 300,260, B 423,618 (1.41x C), B- 533,618 (1.78x C). Judges 206,241.
Per writer and judge in wbab3_tokens.json beside this file. The key that maps letters to arms stays off GitHub.
