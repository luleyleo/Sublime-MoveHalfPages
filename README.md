# Move Half Pages

A Sublime Text plugin which provides a command to move by half pages (or any custom percentage).

## Usage

Add these to your keymap:
```json
[
    { "keys": ["pageup"], "command": "move_half_pages", "args": {"forward": false} },
    { "keys": ["pagedown"], "command": "move_half_pages", "args": {"forward": true} },
]
```

You can optionally override the percentage like this:
```json
[
    { "keys": ["pageup"], "command": "move_half_pages", "args": {"forward": false, "percentage": 0.5} },
    { "keys": ["pagedown"], "command": "move_half_pages", "args": {"forward": true, "percentage": 0.5} },
]
```

## Thanks

This was only possible thanks to this awesome post:

https://forum.sublimetext.com/t/move-cursor-to-top-middle-bottom-of-visible-lines/4586
