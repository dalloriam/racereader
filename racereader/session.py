from collections import defaultdict

from racereader.f1_2018.source import F12018Source
from racereader.sources import Source
from racereader.state import State

from typing import Any, Tuple


class Session:

    def __init__(self, source: Source, *args, **kwargs) -> None:
        self._subscriptions = defaultdict(lambda: [])
        self.state = State()

        if source == Source.F1_2018:
            self._src = F12018Source(*args, **kwargs)
    
    def on(self, event_name: str):
        def internal(fn):
            self._subscriptions[event_name].append(fn)

            def wrapper(*args, **kwargs):
                fn(*args, **kwargs)

            return wrapper

        return internal
    
    def _update_and_dispatch(self, event: Tuple[str, Any]):
        (evt_name, value) = event
        if evt_name not in self.state or value != self.state[evt_name]:
            self.state[evt_name] = value

            for sub in self._subscriptions.get(evt_name, []):
                sub(value)
    
    def start(self):
        for event in self._src.run():
            self._update_and_dispatch(event)
