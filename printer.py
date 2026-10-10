"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from decimal import Decimal

from .device import Device
from .device_status import DeviceStatus
from .printer_type import PrinterType


class Printer(Device):
    """Máy in thông thường; mặc định không mang năng lực mạng."""

    def __init__(
        self,
        device_id: str,
        name: str,
        year_in_use: int,
        purchase_price: int | float | Decimal,
        printer_type: PrinterType,
        printed_pages: int,
        is_color: bool,
        status: DeviceStatus = DeviceStatus.ACTIVE,
    ) -> None:
        super().__init__(device_id, name, year_in_use, purchase_price, status)

        if not isinstance(printer_type, PrinterType):
            raise TypeError("printer_type phải là một giá trị PrinterType.")
        if printed_pages < 0:
            raise ValueError("Số trang đã in không được âm.")

        self.printer_type = printer_type
        self.printed_pages = printed_pages
        self.is_color = bool(is_color)

    @property
    def supports_network(self) -> bool:
        """Printer thường không hỗ trợ mạng trong mô hình đã chọn."""
        return False

    def calculate_annual_maintenance_cost(self) -> Decimal:
        cost = self.purchase_price * Decimal("0.04")
        if self.printed_pages > 100_000:
            cost += Decimal("500000")
        if self.is_color:
            cost += Decimal("300000")
        return cost

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, type={self.printer_type.value}, "
            f"pages={self.printed_pages:,}, color={'Yes' if self.is_color else 'No'}, "
            f"network={'Yes' if self.supports_network else 'No'}"
        )
