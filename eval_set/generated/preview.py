"""Controlled Phase 2 safety-review fixture.

This intentionally unsafe helper exists only in the review-bot evaluation
repository. ``filename`` represents an untrusted upload-form value.
"""

import subprocess


def render_preview(filename: str) -> None:
    """Render an uploaded filename into a fixed preview image."""
    subprocess.run(f"convert {filename} preview.png", shell=True, check=True)
