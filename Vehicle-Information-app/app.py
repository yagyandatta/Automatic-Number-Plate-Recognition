import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from vehicleModel import vehInfo

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2048 * 2048
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/uploads/'

def validate_image(stream):
    header = stream.read(512)  #reading 512 bytes out of whole image
    stream.seek(0) #setting it to 0 again to read full image afterwards 
    format = imghdr.what(None, header)  #what decides format of given data
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_files', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            #retrieving file extension
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            imgPath = app.config['UPLOAD_PATH'] + filename
            #passing image path to ML model
            vehicleData = vehInfo(imgPath)
            vehicleData = vehicleData.split(",")
            print("[+] Vehicle number is: ",vehicleData)
            return render_template('info.html', numplate=vehicleData)
        else:
            flash('Please upload an image')
            return redirect(url_for('.index'))


if __name__ == "__main__":
    app.run(debug=True)