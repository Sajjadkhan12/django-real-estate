from .locations_data import locations

# For location
def search_locations(request):
    return {'search_locations': locations }