# signal_locator.py

import random

def get_mock_location():
    """
    Simulates geolocation data. In a real system, this would interface with GPS or signal triangulation.
    """
    # Coordinates near Ringsted, Denmark (mock data)
    latitude = round(55.442 + random.uniform(-0.01, 0.01), 6)
    longitude = round(11.791 + random.uniform(-0.01, 0.01), 6)
    return {"latitude": latitude, "longitude": longitude}

def get_nearest_emergency_center(location):
    """
    Simulates a lookup of the nearest emergency center.
    """
    centers = [
        {"name": "Ringsted Medical Center", "distance_km": 1.2},
        {"name": "Køge Hospital", "distance_km": 18.5},
        {"name": "Roskilde Emergency", "distance_km": 25.7}
    ]
    return sorted(centers, key=lambda x: x["distance_km"])[0]

if __name__ == "__main__":
    location = get_mock_location()
    print("📍 Caller Location:", location)
    nearest = get_nearest_emergency_center(location)
    print("🚑 Nearest Emergency Center:", nearest)
