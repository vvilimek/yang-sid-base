import pytest

import yang_sid_base as sid

def test_sid_check():
    # TODO SID(0)

    assert sid.SID.check(1) == sid.AbsoluteSID(1)
    assert sid.SID.check(2**63 - 1) == sid.AbsoluteSID(2**63 - 1)
    assert sid.SID.check(1000) == sid.AbsoluteSID(1000)
    assert sid.SID.check(60000) == sid.AbsoluteSID(60000)
    # CZ.NIC PEN number is 25595
    assert sid.SID.check(3_255_950_000) == sid.AbsoluteSID(3_255_950_000)
    assert sid.SID.check(32_559_500_000) == sid.AbsoluteSID(32_559_500_000)

    assert sid.SID.check(-1) is None
    assert sid.SID.check(2**64-1) is None

    with pytest.raises(ValueError):
        sid.SID(-1)

    with pytest.raises(ValueError):
        sid.SID(2**64-1)

    int(sid.SID(1)) == 1
    int(sid.SID(1000)) == 1000
    int(sid.SID(60000)) == 60000

def test_arit():
    root = sid.SID(5)
    child = sid.SID(7)

    assert child - root == sid.RelativeSID(2)
    assert root + sid.RelativeSID(2) == child
    assert child - sid.RelativeSID(2) == root

