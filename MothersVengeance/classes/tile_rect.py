class TileRect(object):
    def __init__(self, tile_type="0", rect=None, countdown=-1):
        self.tile_type=tile_type
        self.rect=rect
        self.countdown = countdown