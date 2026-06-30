import requests
import io
from PIL import Image

def test_api():
    url = "http://localhost:5000/api/process"
    # Create a dummy image
    img = Image.new('RGB', (100, 100), color='red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    files = {'file': ('test.png', img_byte_arr, 'image/png')}
    data = {'filter': 'canny'}
    
    try:
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("API test successful! Received image of size:", len(response.content))
        else:
            print(f"API test failed with status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"API request failed: {e}")

if __name__ == '__main__':
    test_api()
