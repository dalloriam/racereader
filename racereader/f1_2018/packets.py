import ctypes


class PacketHeader(ctypes.LittleEndianStructure):

    _pack_ = 1
    _fields_ = [
        ('format', ctypes.c_uint16),
        ('version', ctypes.c_uint8),
        ('packet_id', ctypes.c_uint8),
        ('session_id', ctypes.c_uint64),
        ('session_time', ctypes.c_float),
        ('frame_identifier', ctypes.c_uint),
        ('playercar_index', ctypes.c_uint8)
    ]


class MarshalZone(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('zone_start', ctypes.c_float),
        ('zone_flag', ctypes.c_int8)
    ]

class SessionPacket(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('header', PacketHeader),
        ('weather', ctypes.c_uint8),
        ('track_temp', ctypes.c_int8),
        ('air_temp', ctypes.c_int8),
        ('total_laps', ctypes.c_uint8),
        ('track_length', ctypes.c_uint16),
        ('session_type', ctypes.c_uint8),
        ('current_track', ctypes.c_int8),
        ('era', ctypes.c_uint8),
        ('session_time_left', ctypes.c_uint16),
        ('session_duration', ctypes.c_uint16),
        ('pit_speed_limit', ctypes.c_uint8),
        ('game_paused', ctypes.c_uint8),
        ('is_spectating', ctypes.c_uint8),
        ('spectator_car_idx', ctypes.c_uint8),
        ('sli_pro', ctypes.c_uint8),
        ('n_marshal_zones', ctypes.c_uint8),
        ('marshal_zones', MarshalZone * 21),
        ('safety_car_status', ctypes.c_uint8),
        ('network_game', ctypes.c_uint8)
    ]


class LapData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('last_lap_time', ctypes.c_float),
        ('current_lap_time', ctypes.c_float),
        ('best_lap_time', ctypes.c_float),
        ('sector_1_time', ctypes.c_float),
        ('sector_2_time', ctypes.c_float),
        ('lap_distance', ctypes.c_float),
        ('total_distance', ctypes.c_float),
        ('safety_car_delta', ctypes.c_float),
        ('car_position', ctypes.c_uint8),
        ('current_lap_num', ctypes.c_uint8),
        ('pit_status', ctypes.c_uint8),
        ('current_sector', ctypes.c_uint8),
        ('current_lap_invalid', ctypes.c_uint8),
        ('total_penalties', ctypes.c_uint8),
        ('grid_position', ctypes.c_uint8),
        ('driver_status', ctypes.c_uint8),
        ('result_status', ctypes.c_uint8),
    ]

class LapDataPacket(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('header', PacketHeader),
        ('lap_data', LapData)
    ]


class ParticipantsData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('is_ai_controlled', ctypes.c_uint8),
        ('driver', ctypes.c_uint8),
        ('team', ctypes.c_uint8),
        ('race_number', ctypes.c_uint8),
        ('nationality', ctypes.c_uint8),
        ('name', ctypes.c_char * 48)
    ]


class ParticipantsDataPacket(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('header', PacketHeader),
        ('car_count', ctypes.c_uint8),
        ('participants', ParticipantsData * 20)
    ]