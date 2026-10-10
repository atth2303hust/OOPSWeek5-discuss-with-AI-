"""
/****************/
Mã sinh viên: 202419007
Họ tên: Phạm Anh Tú
/****************/
"""

from device_maintenance_lab import (
    Computer,
    Device,
    DeviceStatus,
    INetworkable,
    LabRoom,
    NetworkPrinter,
    Printer,
    PrinterType,
    Projector,
)


def format_vnd(value) -> str:
    """Định dạng số tiền theo VND, không lấy phần thập phân."""
    return f"{value:,.0f} VND"


def print_room(room: LabRoom) -> None:
    """In danh sách thiết bị, tổng bảo trì và thiết bị cần bảo trì."""
    print(f"=== {room.room_id} - {room.name} ===")

    for device in room.devices:
        print(device)
        print(
            "  -> Chi phí bảo trì:",
            format_vnd(device.calculate_annual_maintenance_cost()),
        )

    print("Tổng chi phí bảo trì:", format_vnd(room.calculate_annual_maintenance_cost()))
    print("Thiết bị cần bảo trì:")

    devices = room.get_devices_requiring_maintenance()
    if not devices:
        print("  (Không có)")
    else:
        for device in devices:
            print(f"  - {device.device_id}: {device.name}")
    print()


def test_duplicate_device(room: LabRoom, device: Device) -> None:
    """Kiểm thử quy tắc không cho trùng mã trong cùng một phòng."""
    print("[TEST] Thêm thiết bị trùng mã vào LAB-A:")
    try:
        room.add_device(device)
    except ValueError as exc:
        print(f"  Đã chặn đúng: {exc}\n")


def test_network_polymorphism(*network_devices: INetworkable) -> None:
    """Duyệt thiết bị mạng qua contract INetworkable, không phụ thuộc lớp cụ thể."""
    ip_addresses = ["10.0.0.11", "10.0.0.12", "10.0.0.21"]

    print("=== KIỂM THỬ INetworkable ===")
    for device, ip_address in zip(network_devices, ip_addresses):
        device.connect(ip_address)
        print(
            f"{type(device).__name__:<14} -> "
            f"Connected: {str(device.is_connected):<5} | IP: {device.ip_address}"
        )

    print("\n[TEST] Không cho phép kết nối lại khi đang kết nối:")
    try:
        network_devices[0].connect("10.0.0.99")
    except RuntimeError as exc:
        print(f"  Đã chặn đúng: {exc}")

    print("\n[TEST] Ngắt kết nối thiết bị đầu tiên:")
    network_devices[0].disconnect()
    print(
        f"  Connected: {network_devices[0].is_connected} | "
        f"IP sau khi ngắt: {network_devices[0].ip_address}"
    )


def main() -> None:
    """Tạo dữ liệu và chạy đầy đủ các ca kiểm thử tối thiểu của đề."""
    print("=== HỆ THỐNG QUẢN LÝ THIẾT BỊ VÀ HỢP ĐỒNG BẢO TRÌ ===\n")

    # Hai máy tính, trong đó một máy có GPU rời.
    computer1 = Computer(
        "C001", "Workstation AI", 2020, 25_000_000,
        32, "Intel Core i7", True,
    )
    computer2 = Computer(
        "C002", "Office PC", 2024, 18_000_000,
        16, "Intel Core i5", False,
    )

    # Hai máy in; P001 đã in trên 100.000 trang.
    printer1 = Printer(
        "P001", "Color Inkjet", 2023, 8_000_000,
        PrinterType.INKJET, 150_000, True,
    )
    network_printer = NetworkPrinter(
        "P002", "Network Laser", 2022, 12_000_000,
        PrinterType.LASER, 50_000, False,
    )

    # Máy chiếu đã dùng bóng đèn trên 3.000 giờ.
    projector = Projector(
        "PJ001", "Main Projector", 2021, 20_000_000,
        5_000, 4_000, DeviceStatus.UNDER_MAINTENANCE,
    )

    room_a = LabRoom("LAB-A", "Phòng thực hành A", 40)
    room_b = LabRoom("LAB-B", "Phòng thực hành B", 35)

    # Thiết bị tồn tại độc lập trước khi được thêm vào phòng -> aggregation.
    room_a.add_device(computer1)
    room_a.add_device(printer1)
    room_a.add_device(projector)

    room_b.add_device(computer2)
    room_b.add_device(network_printer)

    test_duplicate_device(room_a, computer1)
    print_room(room_a)
    print_room(room_b)

    print("=== KIỂM THỬ TÌM THIẾT BỊ ===")
    found = room_a.find_device("P001")
    print("Tìm thấy P001:" if found else "Không tìm thấy P001.", found.name if found else "")
    print()

    test_network_polymorphism(computer1, computer2, network_printer)


if __name__ == "__main__":
    main()
