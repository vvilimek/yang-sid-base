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
    rel = sid.RelativeSID(5)

    assert child - root == sid.RelativeSID(2)
    assert root - child == sid.RelativeSID(-2)
    assert root + sid.RelativeSID(2) == child
    assert child - sid.RelativeSID(2) == root
    assert sid.RelativeSID(2) + root == child
    assert -sid.RelativeSID(2) + child == root

    assert root + (child - root) == child
    assert child + (root - child) == root
    assert (child - root) + root == child
    assert (root - child) + child == root

    assert type(sid.SID(2) + sid.RelativeSID(3)) == sid.SID
    assert type(sid.RelativeSID(3) + sid.SID(2)) == sid.SID
    assert type(sid.SID(2) - sid.SID(1)) == sid.RelativeSID
    assert type(sid.SID(3) - sid.RelativeSID(1)) == sid.SID
    assert type(-sid.RelativeSID(5)) == sid.RelativeSID

    assert sid.RelativeSID(-3) == -sid.RelativeSID(3)

    with pytest.raises(TypeError):
        r1 = root + 1

    with pytest.raises(TypeError):
        r2 = root - 1

    with pytest.raises(TypeError):
        r3 = rel + 1

    with pytest.raises(TypeError):
        r4 = rel - 1 

    with pytest.raises(TypeError):
        r5 = root == 1

    with pytest.raises(TypeError):
        r6 = rel == 1

    with pytest.raises(TypeError):
        r7 = root == rel

    with pytest.raises(TypeError):
        r8 = 1 + root

    with pytest.raises(TypeError):
        r9 = 1 - root

    with pytest.raises(TypeError):
        r10 = 1 + rel

    with pytest.raises(TypeError):
        r11 = 1 - rel

    with pytest.raises(TypeError):
        r12 = 1 == root

    with pytest.raises(TypeError):
        r13 = 1 == rel

    with pytest.raises(TypeError):
        r14 = rel == root

    with pytest.raises(TypeError):
        r15 = -sid.SID(2)

    with pytest.raises(TypeError):
        r16 = rel - sid.SID(3)


def test_cont():
    l1 = [sid.SID(1), sid.SID(2)]
    l2 = [sid.RelativeSID(3), sid.RelativeSID(4)]
    l3 = [sid.SID(1), sid.SID(2), sid.RelativeSID(3), sid.RelativeSID(4)]

    l1 = (sid.SID(1), sid.SID(2))
    l2 = (sid.RelativeSID(3), sid.RelativeSID(4))
    l3 = (sid.SID(1), sid.SID(2), sid.RelativeSID(3), sid.RelativeSID(4))

    # test __hash__
    d1 = {sid.SID(1): "value", sid.SID(2): "other"}
    d2 = {sid.RelativeSID(3): "rel", sid.RelativeSID(4): "ative"}
    d3 = {sid.SID(1): "value", sid.SID(2): "other", sid.RelativeSID(3): "rel", sid.RelativeSID(4): "ative"}
