"""Proposed pre-application gate for the P0321 Delaunay mixing bridge.

This checks the scope of supplied hypotheses, never their mathematical truth.
It does not establish mixing from samples or infer a hexatic phase.
"""
from collections.abc import Mapping
from typing import Any


def check_bridge_support(evidence: Mapping[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    if evidence.get("dependence_support") != "all_local_events_mixing":
        reasons.append("Density pair decay does not bound dependence of all local events.")
    if evidence.get("window_bound_uniform") is not True:
        reasons.append("Specify dependence on growing window size; fixed-window mixing is insufficient.")
    if evidence.get("void_bound_stated") is not True:
        reasons.append("A quantified empty-disk bound is needed for a decay consequence.")
    if evidence.get("observable") != "spatial_nearest_cell_delaunay_sixfold":
        reasons.append("The proved bridge uses a spatial nearest-cell mark, not a Palm particle mark.")
    if evidence.get("geometry_hypotheses_stated") is not True:
        reasons.append("State finite positive intensity, general position, unique nearest nuclei, and bounded cells.")
    return {
        "scope_compatible": not reasons,
        "reasons": reasons,
        "truth_verified": False,
        "phase_existence_proved": False,
    }
