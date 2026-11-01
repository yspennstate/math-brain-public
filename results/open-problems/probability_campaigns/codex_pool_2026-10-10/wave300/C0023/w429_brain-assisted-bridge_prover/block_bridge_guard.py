"""Conservative C0023 block-bridge check. This is a proposal, not a proof checker.

The caller must supply independently established hypotheses. A failure of this
sufficient criterion is an abstention, never a proof of nonpercolation.
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class BridgeDecision:
    status: str
    reason: str
    exponent: int | None = None


def _compare_scaled_integer(numerator: int, exponent: int, denominator: int) -> int:
    """Compare numerator * 2**exponent with denominator without huge shifts."""
    if numerator == 0:
        return -1
    left_bits = numerator.bit_length() + exponent
    right_bits = denominator.bit_length()
    if left_bits != right_bits:
        return -1 if left_bits < right_bits else 1
    value = numerator << exponent  # bounded by the already supplied denominator
    return (value > denominator) - (value < denominator)


def assess_block_bridge(
    bad_bound: Fraction | None,
    dependence_range: int | None,
    *,
    sigma_field_independence_verified: bool = False,
    finite_bit_count: int | None = None,
    compatibility_verified: bool = False,
) -> BridgeDecision:
    """Check the strict numerical margin needed in ATTEMPT.md L4.

    Verified flags record caller-supplied evidence; this function cannot prove
    independence, the marginal bound, or deterministic path compatibility.
    """
    if bad_bound is None or dependence_range is None:
        return BridgeDecision("ABSTAIN", "Missing bad-marginal bound or dependence range.")
    if isinstance(dependence_range, bool) or not isinstance(dependence_range, int) or dependence_range < 0:
        raise ValueError("dependence_range must be a nonnegative integer")
    if not isinstance(bad_bound, Fraction) or not 0 <= bad_bound <= 1:
        raise ValueError("bad_bound must be an exact Fraction in [0,1]")
    exponent = 6 * (dependence_range + 1) ** 2
    if not sigma_field_independence_verified:
        return BridgeDecision("ABSTAIN", "Full sigma-field range independence is unverified.", exponent)
    if (isinstance(finite_bit_count, bool) or not isinstance(finite_bit_count, int)
            or finite_bit_count < 1 or not compatibility_verified):
        return BridgeDecision("ABSTAIN", "Finite determining sets or path compatibility are unverified.", exponent)
    comparison = _compare_scaled_integer(bad_bound.numerator, exponent, bad_bound.denominator)
    if comparison >= 0:
        return BridgeDecision("ABSTAIN", "No strict margin below 64^(-(r+1)^2); other valid criteria remain possible.", exponent)
    return BridgeDecision("SUFFICIENT_CONDITIONAL_BRIDGE", "The numerical margin passes; supplied geometric and independence proofs remain external.", exponent)
