"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from decimal import Decimal

from .device import Device
from .device_status import DeviceStatus


class LabRoom:
    """Phòng thực hành kết tập nhiều đối tượng Device."""

    def __init__(self, room_id: str, name: str, capacity: int) -> None:
        if not room_id or not room_id.strip():
            raise ValueError("Mã phòng không được rỗng.")
        if not name or not name.strip():
            raise ValueError("Tên phòng không được rỗng.")
        if capacity <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")

        self.room_id = room_id.strip()
        self.name = name.strip()
        self.capacity = capacity
        self._devices: list[Device] = []

    @property
    def devices(self) -> tuple[Device, ...]:
        """Trả về view chỉ đọc để bên ngoài không sửa trực tiếp danh sách."""
        return tuple(self._devices)

    def add_device(self, device: Device) -> None:
        if device is None:
            raise ValueError("Không chấp nhận thiết bị None.")
        if not isinstance(device, Device):
            raise TypeError("Đối tượng thêm vào phải là Device.")
        if self.find_device(device.device_id) is not None:
            raise ValueError(
                f"Thiết bị có mã {device.device_id} đã tồn tại trong phòng {self.room_id}."
            )
        self._devices.append(device)

    def remove_device(self, device_id: str) -> bool:
        device = self.find_device(device_id)
        if device is None:
            return False
        self._devices.remove(device)
        return True

    def find_device(self, device_id: str) -> Device | None:
        return next(
            (device for device in self._devices if device.device_id == device_id),
            None,
        )

    def calculate_annual_maintenance_cost(self) -> Decimal:
        # Đa hình: chỉ gọi qua kiểu cơ sở Device; không kiểm tra lớp cụ thể.
        return sum(
            (device.calculate_annual_maintenance_cost() for device in self._devices),
            Decimal("0"),
        )

    def get_devices_requiring_maintenance(self) -> list[Device]:
        return [
            device
            for device in self._devices
            if device.status is DeviceStatus.UNDER_MAINTENANCE
            or device.years_in_use > 5
        ]
