# RaceReader

## Description
RaceReader is a WIP library to extract telemetry from racing games and sims in a consistent and friendly manner.

## Example
Let's say we have F1 2018 running, and set it up in the settings so that it sends it's UDP telemetry towards another box, which will run this script:

```python
from racereader import Session, Source

sess = Session(source=Source.F1_2018)


@sess.on('best_lap_time')
def print_best(lap_time):
    if sess.state.current_track is None:
        return

    print(f'[{sess.state.current_track}] - {lap_time} (NEW BEST)')


@sess.on('last_lap_time')
def print_lap_time(lap_time):
    if sess.state.current_track is None:
        return

    print(f'[{sess.state.current_track}] - {lap_time}')


if __name__ == '__main__':
    sess.start()
```

The library will parse the incoming data from the game, abstract-away the F1-specific stuff, and allow you to work directly with the data that matters.

## Supported state keys
* `last_lap_time`: *timedelta*
* `best_lap_time`: *timedelta*
* `current_track`: *str*

## Requirements
* Python 3.7+