"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from enum import Enum


class DeviceStatus(Enum):
    """Trạng thái hoạt động của thiết bị."""

    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"
