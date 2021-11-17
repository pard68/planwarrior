# Planwarrior

Planwarrior is a tool for visualizing a plantext dayplanner in the terminal

```
❯ python3 planwarrior
---------Good morning!---------
08:00 -- Plan day
08:30 -- Design planwarrior
         ...
         ...
10:00 -- Work on planwarrior poc
         ...
         ...
         ...
12:00 -- break for lunch
         ...
13:00 -- Finalize planwarrior poc
         ...
         ...
         ...
         now
         ...
16:00 -- Publish planwarrior to GH
         ...
16:55 -- be lauded for my amazing snek skillz
---------Have a good evening!---------
```

## Usage

```
python3 planwarrior
```

## Dayplanner Format

The dayplanner format that Planwarrior uses is very simple Every line is a new
time entry. An entry consists of two parts, the start time and a description
Currently Planwarrior only supports times in 24-hour format, with `00:00`
equalling midnight.  There are plans to support additional time formats, but
those are nice-to-haves and not priorities to me.

Here is an example dayplanner:
```
08:00 Plan day
08:30 Design planwarrior
10:00 Work on planwarrior poc
12:00 break for lunch
13:00 Finalize planwarrior poc
16:00 Publish planwarrior to GH
16:55 be lauded for my amazing snek skillz
```

## Configuration

Planwarrior's configuration looks like this:

```
'resolution': 30,
'start_time': '8:00',
'end_time': '17:00',
'start_message': "Good morning!",
'end_message': "Have a good evening!",
```

### resolution

This refers to the time interval for each line of output. Your dayplanner can
contain any time you wish, this is merely the interal used for the filler
between items.

### start_time and end_time

These refer to the start and end of your day. Usually this would mean when you
start working, but it can be anything you wish (or nothing at all).  Any time
outside of this will still be visible if your day's plan includes it, but time
outside of this bounding will not be displayed by Planwarrior unless a plan
includes it.

### start_message and end_message

Planwarrior will optionally insert a message at the start and end deliminators
for the day.

## Future Features

- TODO: Taskwarrior integration
- TODO: Timewarrior integration?
- DONE: Read plan from file
- DONE: Read config from file
- TODO: Optional "live" mode?
- TODO: Unit tests
