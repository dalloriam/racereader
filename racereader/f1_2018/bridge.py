from datetime import timedelta

from racereader.f1_2018.data import TRACK_MAP

from typing import Any, Tuple

Event = Tuple[str, Any]


def on_best_lap_time(best_lap: float) -> Event:
    return "best_lap_time", timedelta(seconds=best_lap)

def on_last_lap_time(last_lap: float) -> Event:
    return "last_lap_time", timedelta(seconds=last_lap)

def on_current_track(track: int) -> Event:
    return 'current_track', TRACK_MAP.get(track, 'Unknown Track')