

from test.conftest import read_csv

API_URL = "http://localhost:5001"


    

@pytest.mark.parametrize("data", read_csv('test_values.csv'))
def test_land_api(data):
    description_color = "\033[96m"
    end_color = "\033[0m"
    green = "\033[92m"
    magenta = "\033[95m"
    print(f"""
    

    {description_color}==================================
    Daerah : {data['city']}
    Panjang Tanah : {data['length']}
    Lebar Tanah : {data['width']}
    Harga Tanah per Meter Persegi : {data['local_price_per_area']}
    Pajak Tanah per Meter Persegi : {data['tax_per_area']}
    ==================================={end_color}
    
    """)

    # 1. Create data
    create_response = requests.post(f"{API_URL}/land", json={
        "city": data["city"],
        "width": int(data["width"]),
        "length": int(data["length"]),
        "local_price_per_area": int(data["local_price_per_area"]),
        "tax_per_area": int(data["tax_per_area"])
    })
    assert create_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {float(create_response.status_code)}}} {end_color}")
    land_id = create_response.json()["id"]
    print(f"{green} - Passed Create Data: ID  {land_id}{end_color}\n")
    

    # 2. Read data
    read_response = requests.get(f"{API_URL}/land/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    assert land_data["city"] == data["city"]
    print(f"{magenta}   {{Expected city: {data['city']}, Actual city: {land_data['city']}}} {end_color}")
    assert land_data["width"] == int(data["width"])
    print(f"{magenta}   {{Expected width: {float(data['width'])}, Actual width: {land_data['width']}}} {end_color}")
    assert land_data["length"] == int(data["length"])
    print(f"{magenta}   {{Expected length: {float(data['length'])}, Actual length: {land_data['length']}}} {end_color}")
    assert land_data["local_price_per_area"] == int(data["local_price_per_area"])
    print(f"{magenta}   {{Expected local_price_per_area: {float(data['local_price_per_area'])}, Actual local_price_per_area: {land_data['local_price_per_area']}}} {end_color}")
    assert land_data["tax_per_area"] == int(data["tax_per_area"])
    print(f"{magenta}   {{Expected tax_per_area: {float(data['tax_per_area'])}, Actual tax_per_area: {land_data['tax_per_area']}}} {end_color}")
    print(f"{green} - Passed Read Data: ID {land_id}{end_color}\n")

     # 3. Calculate luas tanah (m²)
    read_response = requests.get(f"{API_URL}/land/area/{land_id}")
    assert read_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {read_response.status_code}}} {end_color}")
    land_data = read_response.json()
    expected_land_area = float(data["expected_land_area"])
    assert land_data["area"] == expected_land_area
    print(f"{magenta}   {{Expected Luas Tanah: {float(expected_land_area)}, Actual Luas Tanah: {land_data['area']}}} {end_color}")
    print(f"{green} - Passed Calculate Luas Tanah: ID {land_id}{end_color}\n")

    # 4. Calculate harga tanah semuanya
    read_response = requests.get(f"{API_URL}/land/price/{land_id}")
    assert read_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {read_response.status_code}}} {end_color}")
    land_data = read_response.json()
    expected_land_area_price = float(data["expected_land_area_price"])
    assert land_data["price"] == expected_land_area_price
    print(f"{magenta}   {{Expected Harga Tanah Keseluruhan: {float(expected_land_area_price)}, Actual Harga Tanah Keseluruhan: {land_data['price']}}} {end_color}")
    print(f"{green} - Passed Calculate Harga Tanah: ID {land_id}{end_color}\n")

    # 5. Calculate PBB (Pajak Bumi Bangunan)
    read_response = requests.get(f"{API_URL}/land/tax/{land_id}")
    assert read_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {read_response.status_code}}} {end_color}")
    land_data = read_response.json()
    expected_land_tax = float(data["expected_land_tax"])
    assert land_data["tax"] == expected_land_tax
    print(f"{magenta}   {{Expected Pajak Tanah: {expected_land_tax}, Actual Pajak Tanah: {land_data['tax']}}} {end_color}")
    print(f"{green} - Passed Calculate PBB: ID {land_id}{end_color}\n")

    # 6. Update data
    updated_length = int(data["length"]) + 5
    update_response = requests.put(f"{API_URL}/land/{land_id}", json={
        "city": data["city"],
        "width": int(data["width"]),
        "length": updated_length,
        "local_price_per_area": int(data["local_price_per_area"]),
        "tax_per_area": int(data["tax_per_area"])
    })
    assert update_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {update_response.status_code}}} {end_color}")
    print(f"{green} - Passed Update Data: ID {land_id}{end_color}\n")

    # 7. Read updated data
    read_response = requests.get(f"{API_URL}/land/{land_id}")
    assert read_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {read_response.status_code}}} {end_color}")
    land_data = read_response.json()
    assert land_data["length"] == updated_length
    print(f"{magenta}   {{Expected Updated length: {float(land_data['length'])}, Actual Updated length: {updated_length}}} {end_color}")
    print(f"{green} - Passed Read Updated Data: ID {land_id}{end_color}\n")

    # 8. Delete data
    delete_response = requests.delete(f"{API_URL}/land/{land_id}")
    assert delete_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {delete_response.status_code}}} {end_color}")
    print(f"{green} - Passed Delete Data: ID {land_id}{end_color}\n")

    #9. Read Data
    read_response = requests.get(f"{API_URL}/land/{land_id}")
    assert read_response.status_code == 200
    print(f"{magenta}   {{Expected StatusCode: 200, Actual StatusCode: {read_response.status_code}}} {end_color}")
    land_data = read_response.json()
    assert land_data == None
    print(f"{magenta}   {{Expected Land Data: None, Actual Land Data: {land_data}}} {end_color}")
    print(f"{green} - Passed Read Data: null{end_color}")

