from kivy_garden.mapview import MapView
from kivy.clock import Clock

class FarmersMapView(MapView):
    getting_markets = None
    def start_getting_markets_in_fov(self):
        # After one secons, get the markets in field of view
        try:
             self.getting_markets.cancel()
        except:
            pass
        self.getting_markets = Clock.schedule_once(self.start_getting_markets_in_fov, 1)