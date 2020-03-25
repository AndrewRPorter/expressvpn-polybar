expressvpn-polybar
==================

Simple script to show expressvpn status in polybar

Usage
-----

[module/expressvpn]
type = custom/script
interval = 5
format-prefix = "VPN: "
exec = "python /path/to/script/vpn_status.py --status"
format-underline = #ffffff
