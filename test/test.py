import pytest
import requests
import csv

from test.conftest import read_csv

API_URL = "http://localhost:5001"


    

@pytest.mark.parametrize("data", read_csv('test_values.csv'))
def test_land_api(data):
    description_color = "\033[96m"
    end_color = "\033[0m"
    green = "\033[92m"
    
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
    land_id = create_response.json()["id"]
    print(f"{green} - Passed Create Data: ID {land_id}{end_color}")

    # 2. Read data
    read_response = requests.get(f"{API_URL}/land/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    assert land_data["city"] == data["city"]
    assert land_data["width"] == int(data["width"])
    assert land_data["length"] == int(data["length"])
    assert land_data["local_price_per_area"] == int(data["local_price_per_area"])
    assert land_data["tax_per_area"] == int(data["tax_per_area"])
    print(f"{green} - Passed Read Data: ID {land_id}{end_color}")

    # 3. Update data
    updated_length = int(data["length"]) + 5
    update_response = requests.put(f"{API_URL}/land/{land_id}", json={
        "city": data["city"],
        "width": int(data["width"]),
        "length": updated_length,
        "local_price_per_area": int(data["local_price_per_area"]),
        "tax_per_area": int(data["tax_per_area"])
    })
    assert update_response.status_code == 200
    print(f"{green} - Passed Update Data: ID {land_id}{end_color}")

    # 4. Read updated data
    read_response = requests.get(f"{API_URL}/land/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    assert land_data["length"] == updated_length
    print(f"{green} - Passed Read Updated Data: ID {land_id}{end_color}")

     # 5. Calculate luas tanah (m²)
    read_response = requests.get(f"{API_URL}/land/area/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    luas_tanah = int(data["width"]) * updated_length
    assert land_data["area"] == luas_tanah
    print(f"{green} - Passed Calculate Luas Tanah: ID {land_id}{end_color}")

    # 6. Calculate harga tanah semuanya
    read_response = requests.get(f"{API_URL}/land/price/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    harga_tanah_semuanya = luas_tanah * int(data["local_price_per_area"])
    assert land_data["price"] == harga_tanah_semuanya
    print(f"{green} - Passed Calculate Harga Tanah: ID {land_id}{end_color}")

    # 7. Calculate PBB (Pajak Bumi Bangunan)
    read_response = requests.get(f"{API_URL}/land/tax/{land_id}")
    assert read_response.status_code == 200
    land_data = read_response.json()
    pajak_tanah = harga_tanah_semuanya * .2  
    assert land_data["tax"] == pajak_tanah
    print(f"{green} - Passed Calculate PBB: ID {land_id}{end_color}")

    # 8. Delete data
    delete_response = requests.delete(f"{API_URL}/land/{land_id}")
    assert delete_response.status_code == 200
    print(f"{green} - Passed Delete Data: ID {land_id}{end_color}")

