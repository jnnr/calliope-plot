from pathlib import Path
import runpy
import pytest

DIR_EXAMPLES = Path(__file__).parent.parent / "examples"
exclude = []
examples = DIR_EXAMPLES.resolve().glob("*.py")


@pytest.mark.parametrize("script", examples)
def test_script_execution(script):
    runpy.run_path(script)
