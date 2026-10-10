# Lab W05A - Hệ thống quản lý thiết bị và hợp đồng bảo trì (Python)

## Chạy chương trình

Yêu cầu Python 3.10+.

```bash
cd src
python main.py
```

Bài chỉ dùng Python Standard Library, không cần cài package ngoài.

## Mô hình

- `Device(ABC)`: lớp trừu tượng chung cho thiết bị.
- `Computer(Device, INetworkable)`: máy tính, luôn có khả năng mạng.
- `Printer(Device)`: máy in thường.
- `NetworkPrinter(Printer, INetworkable)`: máy in có mạng.
- `Projector(Device)`: máy chiếu.
- `INetworkable(ABC)`: contract mô phỏng interface trong Python.
- `LabRoom`: kết tập nhiều `Device`.

