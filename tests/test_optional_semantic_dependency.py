"""The dependency-free core works when the optional semantic lane is unavailable."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

SOURCE_ROOT = Path(__file__).resolve().parents[1] / "src"


def _isolated(script):
    env = {
        key: value for key, value in os.environ.items()
        if not key.startswith(("MATH_BRAIN_", "MATHBRAIN_"))
    }
    env["PYTHONPATH"] = str(SOURCE_ROOT)
    return subprocess.run(
        [sys.executable, "-S", "-c", script],
        env=env, capture_output=True, text=True, check=False, timeout=15,
    )


@pytest.mark.parametrize("mode", ["0", "1"])
def test_core_retrieval_without_site_packages(mode):
    result = _isolated(f"""
import os
os.environ["MATH_BRAIN_SEMANTIC"] = {mode!r}
import math_brain
from math_brain import semantic
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import retrieve
import json
node = GraphNode(
    id="lemma", kind=NodeKind.CLAIM, title="Bounded martingale convergence",
    body="Every bounded martingale in this fixture has a limiting random variable.",
)
result = retrieve("bounded martingale convergence", nodes=[node], edges=[])
print(json.dumps({{
    "abstained": result.abstained,
    "hits": [hit.node.id for hit in result.hits],
    "status": semantic.lane_status()[0],
    "semantic_scores": [hit.semantic_score for hit in result.hits],
}}))
""")
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["abstained"] is False
    assert payload["hits"] == ["lemma"]
    assert payload["semantic_scores"] == [0.0]
    assert payload["status"] == (
        "DISABLED" if mode == "0" else "DEPENDENCY_UNAVAILABLE"
    )


def test_missing_optional_dependency_has_explicit_status():
    result = _isolated("""
import os
os.environ["MATH_BRAIN_SEMANTIC"] = "1"
from math_brain import semantic
assert semantic.available() is False
assert semantic.lane_status() == (
    "DEPENDENCY_UNAVAILABLE", "optional semantic channel requires NumPy"
)
assert semantic.artifact_identity() == {}
""")
    assert result.returncode == 0, result.stderr


def test_broken_numpy_install_is_not_hidden():
    result = _isolated("""
import importlib.abc
import sys
class BrokenNumpy(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "numpy":
            raise ModuleNotFoundError("broken transitive dependency", name="numpy_internal")
sys.meta_path.insert(0, BrokenNumpy())
try:
    import math_brain
except ModuleNotFoundError as exc:
    assert exc.name == "numpy_internal"
else:
    raise AssertionError("a broken dependency was hidden")
""")
    assert result.returncode == 0, result.stderr
