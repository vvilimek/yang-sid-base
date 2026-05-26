# SPDX-FileCopyrightText: CZ.NIC z.s.p.o.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import NewType, Optional, overload, NoReturn, Union, Self

__all__ = ("SID", "AbsoluteSID", "RelativeSID")

AbsoluteSID = NewType("AbsoluteSID", int)

class SID(int):
    @staticmethod
    def check(sid: int) -> Optional[AbsoluteSID]:
        if sid < 0 or sid >= 2**63:
            return None
        return AbsoluteSID(sid)

    def __new__(cls, sid: int) -> Self:
        if SID.check(sid) is None:
            raise ValueError(f"Invalid value for a SID number {sid}")
        return super().__new__(cls, sid)

    @overload
    def __add__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __add__(self, other: object) -> NoReturn: ...

    def __add__(self, other: object) -> Union["SID", NoReturn]:
        if not isinstance(other, RelativeSID):
            raise TypeError
        return SID(int(self) + int(other))

    @overload
    def __sub__(self, other: "SID") -> "RelativeSID": ...
    @overload
    def __sub__(self, other: object) -> NoReturn: ...

    def __sub__(self, other: object) -> Union["RelativeSID", NoReturn]:
        if not isinstance(other, int):
            raise TypeError
        return RelativeSID(int(self) - int(other))

    def to_int(self) -> int:
        return int(self)

    def __cbor__(self) -> int:
        return self.to_int()

class RelativeSID(int):
    def __new__(cls, relative: int) -> Self:
        return super().__new__(cls, relative)

    def to_int(self) -> int:
        return int(self)

    def __cbor__(self) -> int:
        return self.to_int()

