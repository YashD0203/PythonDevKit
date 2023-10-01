#!/bin/bash

battery_status=$(pmset -g batt)

echo "Battery Status:"
echo "$battery_status"

