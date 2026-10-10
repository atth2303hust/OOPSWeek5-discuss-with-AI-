"""
/****************/
Mã sinh viên: <MSSV>
Họ tên: <HỌ VÀ TÊN>
/****************/
"""

import unittest
from datetime import date
from decimal import Decimal

from device_maintenance_lab import (
    Computer,
    DeviceStatus,
    LabRoom,
    NetworkPrinter,
    Printer,
    PrinterType,
    Projector,
)


class LabW05ATests(unittest.TestCase):
    """Một số kiểm thử tự động cho các quy tắc quan trọng của đề."""

    def test_computer_maintenance_cost(self) -> None:
        computer = Computer("C1", "PC", 2020, 25_000_000, 32, "i7", True)
        self.assertEqual(computer.calculate_annual_maintenance_cost(), Decimal("2000000"))

    def test_printer_maintenance_cost(self) -> None:
        printer = Printer("P1", "Printer", 2023, 8_000_000, PrinterType.INKJET, 150_001, True)
        self.assertEqual(printer.calculate_annual_maintenance_cost(), Decimal("1120000"))

    def test_projector_maintenance_cost(self) -> None:
        projector = Projector("PJ1", "Projector", 2021, 20_000_000, 5000, 3001)
        self.assertEqual(projector.calculate_annual_maintenance_cost(), Decimal("2100000"))

    def test_duplicate_device_is_rejected(self) -> None:
        room = LabRoom("R1", "Room", 30)
        computer = Computer("C1", "PC", 2024, 10_000_000, 16, "i5", False)
        room.add_device(computer)
        with self.assertRaises(ValueError):
            room.add_device(computer)

    def test_future_year_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Computer("C1", "PC", date.today().year + 1, 10_000_000, 16, "i5", False)

    def test_network_reconnect_is_rejected(self) -> None:
        printer = NetworkPrinter("P1", "NP", 2024, 10_000_000, PrinterType.LASER, 0, False)
        printer.connect("10.0.0.1")
        with self.assertRaises(RuntimeError):
            printer.connect("10.0.0.2")

    def test_disconnect_clears_ip(self) -> None:
        computer = Computer("C1", "PC", 2024, 10_000_000, 16, "i5", False)
        computer.connect("10.0.0.1")
        computer.disconnect()
        self.assertFalse(computer.is_connected)
        self.assertIsNone(computer.ip_address)

    def test_lab_cost_uses_device_polymorphism(self) -> None:
        room = LabRoom("R1", "Room", 30)
        room.add_device(Computer("C1", "PC", 2024, 10_000_000, 16, "i5", False))
        room.add_device(Projector("PJ1", "Projector", 2024, 10_000_000, 3000, 0, DeviceStatus.ACTIVE))
        self.assertEqual(room.calculate_annual_maintenance_cost(), Decimal("800000"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
