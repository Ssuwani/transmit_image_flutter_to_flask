from flask import Flask, request

import base64
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    image_data = data['image']
    imgdata = base64.b64decode(image_data)
    
    # for show
    # from PIL import Image
    # import io
    # image = Image.open(io.BytesIO(imgdata))
    # image.show()
    
    # save image
    filename = 'something.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
        print("이미지 저장완료")

    return 'Receive Successfully and Saved image'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)