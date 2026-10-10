"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal

from .device_status import DeviceStatus


class Device(ABC):
    """Lớp cơ sở trừu tượng cho mọi thiết bị trong hệ thống."""

    def __init__(
        self,
        device_id: str,
        name: str,
        year_in_use: int,
        purchase_price: int | float | Decimal,
        status: DeviceStatus = DeviceStatus.ACTIVE,
    ) -> None:
        # Mã thiết bị chỉ được gán trong constructor và không có setter.
        if not device_id or not device_id.strip():
            raise ValueError("Mã thiết bị không được rỗng.")

        self._device_id = device_id.strip()
        self.name = name
        self.year_in_use = year_in_use
        self.purchase_price = purchase_price
        self.status = status

    @property
    def device_id(self) -> str:
        """Mã thiết bị chỉ đọc sau khi đối tượng đã được khởi tạo."""
        return self._device_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Tên thiết bị không được rỗng.")
        self._name = value.strip()

    @property
    def year_in_use(self) -> int:
        return self._year_in_use

    @year_in_use.setter
    def year_in_use(self, value: int) -> None:
        current_year = date.today().year
        if value <= 0 or value > current_year:
            raise ValueError(
                f"Năm đưa vào sử dụng phải nằm trong khoảng 1..{current_year}."
            )
        self._year_in_use = value

    @property
    def purchase_price(self) -> Decimal:
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value: int | float | Decimal) -> None:
        price = Decimal(str(value))
        if price <= 0:
            raise ValueError("Giá mua phải lớn hơn 0.")
        self._purchase_price = price

    @property
    def status(self) -> DeviceStatus:
        return self._status

    @status.setter
    def status(self, value: DeviceStatus) -> None:
        if not isinstance(value, DeviceStatus):
            raise TypeError("status phải là một giá trị DeviceStatus.")
        self._status = value

    @property
    def years_in_use(self) -> int:
        """Số năm thiết bị đã được sử dụng tính theo năm hiện tại."""
        return date.today().year - self.year_in_use

    @abstractmethod
    def calculate_annual_maintenance_cost(self) -> Decimal:
        """Tính chi phí bảo trì dự kiến trong một năm."""

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.device_id}, name={self.name}, "
            f"year={self.year_in_use}, price={self.purchase_price:,.0f} VND, "
            f"status={self.status.value})"
        )
