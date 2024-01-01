from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut


class AmnonDistanceCalculator:
    def __init__(self, source_address):
        self.geolocator = Nominatim(user_agent="address_distance_calculator")
        self.source_coordinates = self._get_address_coordinates(source_address)

    def get_distance_from_address(self, address: str) -> float:
        target_address_coordinates = self._get_address_coordinates(address)
        return self._calculate_distance_from_target(target_address_coordinates)

    def _get_address_coordinates(self, address: str) -> (float, float) or None:
        try:
            address_location = self.geolocator.geocode(address)
            return address_location.latitude, address_location.longitude
        except (AttributeError, GeocoderTimedOut):
            print(f"error with getting coordinates for address {address}")
            return None

    def _calculate_distance_from_target(self, address_coordinates: (float, float)) -> float:
        return geodesic(address_coordinates, self.source_coordinates).kilometers
