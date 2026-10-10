"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from decimal import Decimal

from .device_status import DeviceStatus
from .inetworkable import INetworkable
from .printer import Printer
from .printer_type import PrinterType


class NetworkPrinter(Printer, INetworkable):
    """Printer chuyên biệt có thêm khả năng kết nối mạng."""

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
        super().__init__(
            device_id,
            name,
            year_in_use,
            purchase_price,
            printer_type,
            printed_pages,
            is_color,
            status,
        )
        self._ip_address: str | None = None

    @property
    def supports_network(self) -> bool:
        return True

    @property
    def ip_address(self) -> str | None:
        return self._ip_address

    @property
    def is_connected(self) -> bool:
        return self._ip_address is not None

    def connect(self, ip_address: str) -> None:
        if self.is_connected:
            raise RuntimeError(f"{self.device_id} đang kết nối; không thể kết nối lại.")
        if not ip_address or not ip_address.strip():
            raise ValueError("Địa chỉ IP không được rỗng.")
        self._ip_address = ip_address.strip()

    def disconnect(self) -> None:
        self._ip_address = None
