"""
/****************/
Mã sinh viên: <MSSV>
Họ tên: <HỌ VÀ TÊN>
/****************/
"""

from decimal import Decimal

from .device import Device
from .device_status import DeviceStatus
from .inetworkable import INetworkable


class Computer(Device, INetworkable):
    """Máy tính: một Device và luôn có khả năng kết nối mạng."""

    def __init__(
        self,
        device_id: str,
        name: str,
        year_in_use: int,
        purchase_price: int | float | Decimal,
        ram_gb: int,
        processor: str,
        has_dedicated_gpu: bool,
        status: DeviceStatus = DeviceStatus.ACTIVE,
    ) -> None:
        super().__init__(device_id, name, year_in_use, purchase_price, status)

        if ram_gb <= 0:
            raise ValueError("Dung lượng RAM phải lớn hơn 0.")
        if not processor or not processor.strip():
            raise ValueError("Loại bộ xử lý không được rỗng.")

        self.ram_gb = ram_gb
        self.processor = processor.strip()
        self.has_dedicated_gpu = bool(has_dedicated_gpu)
        self._ip_address: str | None = None

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

    def calculate_annual_maintenance_cost(self) -> Decimal:
        # 5% cơ bản; +2% nếu có GPU rời; +1% nếu đã dùng trên 5 năm.
        rate = Decimal("0.05")
        if self.has_dedicated_gpu:
            rate += Decimal("0.02")
        if self.years_in_use > 5:
            rate += Decimal("0.01")
        return self.purchase_price * rate

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, RAM={self.ram_gb}GB, CPU={self.processor}, "
            f"GPU={'Yes' if self.has_dedicated_gpu else 'No'}"
        )
