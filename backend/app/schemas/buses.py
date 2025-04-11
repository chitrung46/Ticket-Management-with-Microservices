def individual_serial(bus) -> dict:
    return {
        "id": str(bus["_id"]),
        "brand": bus["brand"],
        "num_plate": bus["num_plate"],
        "color": bus["color"],
        "bus_type_id": bus["bus_type_id"]
    }

def list_serial(buses) -> list:
    return[individual_serial(bus) for bus in buses]