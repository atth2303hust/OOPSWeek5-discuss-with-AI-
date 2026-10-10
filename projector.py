"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from decimal import Decimal

from .device import Device
from .device_status import DeviceStatus


class Projector(Device):
    """Máy chiếu với độ sáng và số giờ sử dụng bóng đèn."""

    def __init__(
        self,
        device_id: str,
        name: str,
        year_in_use: int,
        purchase_price: int | float | Decimal,
        brightness_lumens: int,
        lamp_hours: int,
        status: DeviceStatus = DeviceStatus.ACTIVE,
    ) -> None:
        super().__init__(device_id, name, year_in_use, purchase_price, status)

        if brightness_lumens <= 0:
            raise ValueError("Độ sáng phải lớn hơn 0 lumen.")
        if lamp_hours < 0:
            raise ValueError("Số giờ bóng đèn không được âm.")

        self.brightness_lumens = brightness_lumens
        self.lamp_hours = lamp_hours

    def calculate_annual_maintenance_cost(self) -> Decimal:
        cost = self.purchase_price * Decimal("0.03")
        if self.lamp_hours > 3_000:
            cost += Decimal("1500000")
        return cost

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, brightness={self.brightness_lumens:,}lm, "
            f"lamp_hours={self.lamp_hours:,}"
        )
