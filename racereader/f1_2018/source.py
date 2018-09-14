from collections import defaultdict

from racereader.f1_2018 import bridge, packets

from typing import Any, Iterable, Tuple

import ctypes
import socket

_packet_class_map = {
    1: packets.SessionPacket,
    2: packets.LapDataPacket,
    4: packets.ParticipantsDataPacket
}

Event = Tuple[str, Any]


class F12018Source:

    def __init__(self, host: str = "0.0.0.0", port: int = 20777) -> None:
        self._host = host
        self._port = port

        self._subscriptions = defaultdict(lambda: [])
    
    def _convert(self, packet_struct: ctypes.LittleEndianStructure) -> Iterable[Event]:
        for (field_name, _)  in packet_struct._fields_:
            val = getattr(packet_struct, field_name)

            if hasattr(bridge, f'on_{field_name}'):
                evt = getattr(bridge, f'on_{field_name}')(val)
                yield evt
            
            elif isinstance(val, ctypes.LittleEndianStructure):
                yield from self._convert(val)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self._host, self._port))

        while True:
            packet_data, _, = sock.recvfrom(2000)
            header = packets.PacketHeader.from_buffer_copy(packet_data)

            if header.format != 2018:
                raise RuntimeError(f'invalid packet format: {header.format}')
            
            packet_cl = _packet_class_map.get(header.packet_id)
            if packet_cl is None:
                continue
            
            full_packet = packet_cl.from_buffer_copy(packet_data)
            yield from self._convert(full_packet)