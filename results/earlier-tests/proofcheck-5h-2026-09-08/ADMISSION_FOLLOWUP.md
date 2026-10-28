# Compute admission follow-up (v1/v2 remain frozen)

The candidate threshold gate rejects ordinary pressure, but Python's JSON parser accepts NaN and comparisons against NaN are false. Unknown status or mode strings also bypass its two equality checks. No unsafe launch was observed: this lane ran no actual compiler. This is a static counterexample to treating unchecked numeric fields as trusted telemetry.

`admission_followup.validate_state` adds explicit known status/mode checks, finite nonnegative numeric fields, an integer hung-window count, complete timestamps, the existing 180-second freshness bound, and unchanged CPU/RAM/commit thresholds. Owner presence remains permitted with headroom. It neither changes the governor nor kills any process.

Suggested root integration: inline this pure validator into the final lean_check.py (to avoid adding a deployment dependency), then have admission() read the governor JSON and call validate_state(). Preserve the candidate's existing pre-launch and periodic checks. Keep this separate from frozen v2 until root review and final source pins are refreshed.

Tests are deterministic fixtures only; no new process or actual resource probe is launched. These checks do not authenticate telemetry or establish continuity between observations.
