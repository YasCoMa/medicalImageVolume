from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_up():
    response = client.get("/")
    assert response.status_code == 200

def test_calc_volume_file_empty():
    files = {'imageFile': None}
    response = client.post("/calculate-dicom-image-volume", files=files )
    assert response.status_code == 400

def test_calc_volume_wrong_filetype():
    with open('data/iff.png', 'rb') as tmp:
        files = {'imageFile': tmp}
        response = client.post("/calculate-dicom-image-volume", files=files )
        assert response.status_code == 422
        assert response.json() == { "detail": "This image is not a dicom file" }

def test_calc_volume():
    with open('data/1-101.dcm', 'rb') as tmp:
        files = {'imageFile': tmp}
        response = client.post("/calculate-dicom-image-volume", files=files )
        assert response.json() == { "name": "1-101.dcm", "volume": 150240.0, "pixelsAboveCutoff": 50080 }
