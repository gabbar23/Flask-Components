from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app=Flask(__name__)

photos=UploadSet("photos",IMAGES)
app.config["UPLOADED_PHOTOS_DEST"]='pictures'

configure_uploads(app,photos)


@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST' and 'thefile' in request.files:
        my_file=photos.save(request.files['thefile'])
        url=photos.url(my_file)

        return '<h1>'+url+'</h1>'
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

