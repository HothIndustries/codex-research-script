"""Run the repository's shell upload script."""

from __future__ import annotations

import argparse
import subprocess
from importlib.resources import as_file, files
from pathlib import Path
from typing import Sequence


def _execute(script_path: Path) -> int:
    result = subprocess.run(["bash", str(script_path)], check=True)
    return result.returncode


def run_script(script: str | Path | None = None) -> int:
    """Run the bundled script, or an explicitly supplied shell script."""
    if script is None:
        bundled_script = files("codex_research_script").joinpath("script.sh")
        with as_file(bundled_script) as script_path:
            return _execute(script_path)

    script_path = Path(script).expanduser().resolve()
    if not script_path.is_file():
        raise FileNotFoundError(f"Script not found: {script_path}")
    return _execute(script_path)


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        description="Run the repository upload shell script."
    )
    parser.add_argument(
        "script",
        nargs="?",
        default=None,
        help="optional path to a shell script (default: bundled script.sh)",
    )
    args = parser.parse_args(argv)
    return run_script(args.script)


if __name__ == "__main__":
    raise SystemExit(main())
