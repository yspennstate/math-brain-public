# Correction notice for fleet03/B04 BT4 r11

The first immutable draft `report.md` in this run is **superseded and must not be used**. It transcribed the fleet04/B05 domination-ladder escape incorrectly by routing the cross transition through `h_i`.

The partner's proved construction is instead: after dominating `h_i->a_i`, if the dominator is packed, the cross transition uses the dominator's direct arc to `a_i`; if the first dominator is `r_{i-1}`, the next packed dominator reaches `a_i` through `r_{i-1}`. Thus the correct possible path shapes are

`h_{i-1}->a_i`,
`h_{i-1}->r_{i-1}->a_i`,
`b_i->a_i`,
`b_i->r_{i-1}->a_i`,

not paths containing `h_i` internally.

The corrected scientific result is `report-v2.md`. No handoff or receipt should cite the superseded draft as scientific evidence.
