hl.on("hyprland.start", function()
    hl.exec_cmd("sh -c 'sleep 3 && caelestia shell lock lock'")
end)
hl.exec_cmd("hyprctl keyword xwayland:force_zero_scaling true")