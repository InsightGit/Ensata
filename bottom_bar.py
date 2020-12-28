from adafruit_magtag.magtag import MagTag

class BottomBar:
    _magtag = None

    def __init__(self, magtag : MagTag) -> None:
        self._magtag = magtag
    
        magtag.add_text(
            text_position=(
                50,
                10,
            ),
            text_scale=3,
        )
        
        magtag.set_text("Spotlight")
        
    
    def update(self):
        pass
