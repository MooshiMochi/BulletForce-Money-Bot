from objects import Button


class Buttons:
    # height of bottom bar = 90 px

    width = 1844
    height = 1065

    play_now = Button("Play Now", 230 / 461, 124 / 213)
    confirm = Button("Confirm", 960 / width, 720 / height)
    settings = Button("Settings", 1540 / width, 920 / height)
    login = Button("Login", 1100 / width, 300 / height)
    login_confirm = Button("Login Confirm", 920 / width, 820 / height)

    # Watching ads
    get_ads = Button("Get Ads", 1590 / width, 60 / height)
    watch_ads = Button("Watch Ads", 1220 / width, 450 / height)
    ad_done = Button("Ad Done", 1670 / width, 900 / height)

    # Back button
    back = Button("Back", 90 / width, 160 / height)

    # Full screen (relative to the game size)
    full_screen = Button("Full Screen", 1780 / width, 1020 / height + 90)

    # hide bottom bar
    # 1540, 1875
    hide_bar = Button("Hide Bar", 1540 / 3072, 1875 / 1920)

    # assuming that the user will be in full screen mode, the game size will be the same as the screen size

    fb_logo = Button("FB Logo", 1729 / width, 29 / height)


# fb logo:
#   x   1729
#   y   29
#   w   86
#   h   86

# 1762, 69: color -> 50, 50, 47
# 1766, 64: color -> 227, 225, 219
# 1790, 65: color -> 227, 225, 219
# 1790, 87: color -> 227, 225, 219
# 1767, 87: color -> 227, 225, 219
