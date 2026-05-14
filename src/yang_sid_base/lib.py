# SPDX-FileCopyrightText: CZ.NIC z.s.p.o.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import NewType

__all__ = ("SID", "AbsoluteSID", "RelativeSID")

SID = NewType("SID", int)

class AbsoluteSID(int):
    pass

class RelativeSID(int):
    pass
