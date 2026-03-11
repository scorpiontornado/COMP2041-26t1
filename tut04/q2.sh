#!/bin/dash

# 1. get current hour: date "+%H"
cur_hour=$(date "+%H")

# 2. check if hour >= 9 and hour < 17
[ "$cur_hour" -ge 9 ] && [ "$cur_hour" -lt 17 ]
