# SPDX-FileCopyrightText: CZ.NIC z.s.p.o.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import NewType, Optional

__all__ = ("SID", "AbsoluteSID", "RelativeSID", "check_sid")

SID = NewType("SID", int)

def check_sid(sid: int) -> Optional[SID]:
    if sid <= 0 or sid >= 2**63:
        return None
    return SID(sid)

class AbsoluteSID(int):
    def __init__(self, sid: SID) -> None:
        super().__init__(sid)

class RelativeSID(int):
    def __init__(self, relative: int) -> None:
        super().__init__(relative)

