"""Webhook signature verification helpers."""

from __future__ import annotations

import hashlib
import hmac


def verify_github_webhook(payload: bytes, signature: str, secret: bytes) -> bool:
    """Verify a webhook payload using GitHub's documented signature header."""
    expected = "sha256=" + hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


def extract_signature(headers: dict[str, str]) -> str | None:
    """Read the GitHub webhook signature header."""
    return headers.get("X-GitHub-Signature-Sha256")
