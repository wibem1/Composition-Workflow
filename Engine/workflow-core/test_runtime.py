"""Regression smoke tests for the portable Python workflow runtime.

Run: python -m unittest discover -s Engine/workflow-core -p 'test_runtime.py'
Requires only the Python standard library.
"""
import json
import unittest
from pathlib import Path
from runtime import create_workflow_core

HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE / "spec.json").read_text(encoding="utf-8"))
core = create_workflow_core(SPEC)

class WorkflowRuntimeTests(unittest.TestCase):
    def test_allowed_modes(self):
        for mode in ("compose", "analysis", "continue", "instruments", "revise"):
            self.assertTrue(core.check("request", {
                "mode": mode, "task": "Variation", "transition_bars": 0,
            }))

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            core.check("request", {
                "mode": "unknown", "task": "Variation", "transition_bars": 0,
            })

    def test_missing_task(self):
        with self.assertRaises(ValueError):
            core.check("request", {
                "mode": "compose", "task": " ", "transition_bars": 0,
            })

    def test_transition_bars_only_on_continue(self):
        for bars in (2, 3, 4):
            self.assertTrue(core.check("request", {
                "mode": "continue", "task": "Weiterführen", "transition_bars": bars,
            }))
            with self.assertRaises(ValueError):
                core.check("request", {
                    "mode": "compose", "task": "Variation", "transition_bars": bars,
                })

    def test_original_guard(self):
        self.assertTrue(core.check("apply", {
            "state": "ready", "source_guard": "A", "current_guard": "A",
        }))
        for data in (
            {"state": "ready", "source_guard": "A", "current_guard": "B"},
            {"state": "applied", "source_guard": "A", "current_guard": "A"},
            {"state": "ready", "source_guard": "", "current_guard": ""},
        ):
            with self.assertRaises(ValueError):
                core.check("apply", data)

    def test_transitions(self):
        self.assertEqual(core.advance("draft", "propose"), "ready")
        self.assertEqual(core.advance("ready", "apply"), "applied")
        with self.assertRaises(ValueError):
            core.advance("applied", "apply")

    def test_prompt(self):
        self.assertIn("Bewusste Einfachheit", core.prompt("analysis"))

if __name__ == "__main__":
    unittest.main()
