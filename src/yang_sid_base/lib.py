# SPDX-FileCopyrightText: CZ.NIC z.s.p.o.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import NewType, Optional, overload, NoReturn, Union

__all__ = ("SID", "AbsoluteSID", "RelativeSID")

AbsoluteSID = NewType("AbsoluteSID", int)

def SID(int):
    @staticmethod
    def check(sid: int) -> Optional[AbsouteSID]:
        if sid <= 0 or sid >= 2**63:
            return None
        return AbsoluteSID(sid)

    def __init__(self, sid: int) -> None:
        value = SID.check(sid)
        if value is None:
            raise ValueError(f"Invalid value for a SID number {sid}")
        super().__init__(sid)

    @overload
    def __add__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __add__(self, other: object) -> NoReturn: ...

    def __add__(self, other: object) -> Union["SID", NoReturn]:
        if not isintance(other, RelativeSID):
            raise TypeError
        return SID(int(self) + int(other))

    @overload
    def __sub__(self, other: "SID") -> "RelativeSID": ...
    @overload
    def __sub__(self, other: object) -> NoReturn: ...

    def __sub__(self, other: object) -> Union["RelativeSID", NoReturn]:
        if not isinstance(other, AbsoluteSID):
            raise TypeError
        return RelativeSID(int(self) - int(other))

class RelativeSID(int):
    def __init__(self, relative: int) -> None:
        super().__init__(relative)

