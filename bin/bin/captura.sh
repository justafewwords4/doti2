#!/bin/sh

# Take a screenshot of a selected region using grim and slurp,
# and pipe it to swappy for editing.
grim -g "$(slurp)" - | swappy -f -
