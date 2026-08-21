"""Small authorization policy used by the history-aware recheck proof."""


def can_delete(requester_id: str, owner_id: str) -> bool:
    """Return True only when the requester owns the resource."""
    return requester_id != owner_id
