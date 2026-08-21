from delete_policy import can_delete


def test_only_owner_can_delete() -> None:
    assert can_delete("owner-1", "owner-1") is True
    assert can_delete("attacker", "owner-1") is False
