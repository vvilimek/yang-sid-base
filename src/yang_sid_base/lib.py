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

    def __str__(self) -> str:
        return f"SID({int(self)})"

    def __repr__(self) -> str:
        return f"yang_sid_base.lib.SID({super().__repr__()})"

    @overload
    def __add__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __add__(self, other: object) -> NoReturn: ...

    def __add__(self, other: object) -> Union["SID", NoReturn]:
        if not isinstance(other, RelativeSID):
            raise TypeError
        return SID(int(self) + int(other))

    @overload
    def __radd__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __radd__(self, other: object) -> NoReturn: ...

    def __radd__(self, other: object) -> Union["SID", NoReturn]:
        if not isinstance(other, RelativeSID):
            raise TypeError
        return SID(int(other) + int(self))

    @overload
    def __sub__(self, other: "SID") -> "RelativeSID": ...
    @overload
    def __sub__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __sub__(self, other: object) -> NoReturn: ...

    def __sub__(self, other: object) -> Union["RelativeSID", "SID", NoReturn]:
        if isinstance(other, SID):
            return RelativeSID(int(self) - int(other))
        elif isinstance(other, RelativeSID):
            return SID(int(self) - int(other))
        else:
            raise TypeError

    @overload
    def __rsub__(self, other: "SID") -> "RelativeSID": ...
    @overload
    def __rsub__(self, other: "RelativeSID") -> "SID": ...
    @overload
    def __rsub__(self, other: object) -> NoReturn: ...

    def __rsub__(self, other: object) -> Union["RelativeSID", "SID", NoReturn]:
        if isinstance(other, SID):
            return RelativeSID(int(other) - int(self))
        elif isinstance(other, RelativeSID):
            return SID(int(other) - int(self))
        else:
            raise TypeError
        
    @overload
    def __eq__(self, other: "SID") -> bool: ...
    @overload
    def __eq__(self, other: object) -> NoReturn: ...

    def __eq__(self, other: object) -> Union[bool, NoReturn]:
        if isinstance(other, SID):
            return int(self) == int(other)
        else:
            raise TypeError

    def __neg__(self) -> Self:
        raise TypeError()

    def to_int(self) -> int:
        return super().__int__()

    def __cbor__(self) -> int:
        return int(self)

class RelativeSID(int):
    def __new__(cls, relative: int) -> Self:
        return super().__new__(cls, relative)

    def __str__(self) -> str:
        return f"RelativeSID({int(self)})"

    def __repr__(self) -> str:
        return f"yang_sid_base.lib.RelativeSID({super().__repr__()})"

    def __neg__(self) -> Self:
        return RelativeSID(-int(self))

    @overload
    def __add__(self, other: SID) -> SID: ...
    @overload
    def __add__(self, other: object) -> NoReturn: ...

    def __add__(self, other: object) -> Union[SID, NoReturn]:
        if isinstance(other, SID):
            return SID(int(self) + int(other))
        else:
            raise TypeError

    @overload
    def __radd__(self, other: SID) -> SID: ...
    @overload
    def __radd__(self, other: object) -> NoReturn: ...

    def __radd__(self, other: object) -> Union[SID, NoReturn]:
        if isinstance(other, SID):
            return SID(int(other) + int(self))
        else:
            raise TypeError

    def __sub__(self, other: object) -> NoReturn:
        # If the other operand in an expresion a - b is SID then (a) + (-b), (-b) SID is not valid
        raise TypeError

    @overload
    def __rsub__(self, other: SID) -> SID: ...
    @overload
    def __rsub__(self, other: object) -> NoReturn: ...

    def __rsub__(self, other: object) -> Union[SID, NoReturn]:
        if isinstance(self, SID):
            return SID(int(other) - int(self))
        else:
            raise TypeError

    @overload
    def __eq__(self, other: "RelativeSID") -> bool: ...
    @overload
    def __eq__(self, other: object) -> NoReturn: ...

    def __eq__(self, other: object) -> Union[bool, NoReturn]:
        if isinstance(other, RelativeSID):
            return int(self) == int(other)
        else:
            raise TypeError

    def to_int(self) -> int:
        return super().__int__()

    def __cbor__(self) -> int:
        return int(self)

