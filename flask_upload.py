# import codecs
import csv
import os
import tempfile

from flask import Flask, flash, jsonify, redirect, render_template, request, \
                  Response, send_file, url_for
# from werkzeug import secure_filename

import reader


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file', None)
        if file:
            processed_string = reader.process_file(file, request.form['target_tag'])

            response = Response(
                processed_string,
                mimetype="text/html",
                content_type='application/octet-stream',
            )
            response.headers["Content-Disposition"] = "attachment; filename=result.html" # 다운받았을때의 파일 이름 지정해주기
            return response
        else:
            return redirect(url_for('index'))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
