"""
/****************/
Mã sinh viên: <MSSV>
Họ tên: <HỌ VÀ TÊN>
/****************/
"""

from abc import ABC, abstractmethod


class INetworkable(ABC):
    """Contract cho các đối tượng có khả năng kết nối mạng.

    Python không có từ khóa ``interface`` như C#/Java. Ở bài này,
    ``ABC`` và các ``@abstractmethod`` được dùng để biểu diễn cùng ý nghĩa:
    lớp cụ thể muốn đóng vai trò INetworkable phải cài đặt đầy đủ contract.
    """

    @property
    @abstractmethod
    def ip_address(self) -> str | None:
        """Trả về địa chỉ IP đang hoạt động; None nếu chưa kết nối."""

    @property
    @abstractmethod
    def is_connected(self) -> bool:
        """Cho biết thiết bị hiện có đang kết nối mạng hay không."""

    @abstractmethod
    def connect(self, ip_address: str) -> None:
        """Kết nối thiết bị bằng một địa chỉ IP hợp lệ."""

    @abstractmethod
    def disconnect(self) -> None:
        """Ngắt kết nối và xóa địa chỉ IP đang hoạt động."""
