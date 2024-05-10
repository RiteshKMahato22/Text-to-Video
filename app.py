# app.py

from flask import Flask, jsonify, send_file
from flask import render_template, request
import json
import main
from main import process_data

app = Flask(__name__)

app.config['TIMEOUT'] = 300

@app.route('/')
def visualize():
    # Here you would call your Python script or perform any other action
    # For this example, let's just return a dummy video URL


    return render_template('index.html')

# @app.route('/index')
# def video_play():
#     return render_template('')

# @app.route('/',methods=['POST'])
# def content():
#     record=json.loads(request.data)
#     return jsonify(record)

@app.route('/text-video')
def text_video():
    # Here you would call your Python script or perform any other action
    # For this example, let's just return a dummy video URL
    process_data()
    return render_template('blog-single.html')



@app.route('/blog-single')
def blog_single():
    # Here you would call your Python script or perform any other action
    # For this example, let's just return a dummy video URL
    return render_template('blog-single.html')
    #process_data()

    # video_url = 'https://www.youtube.com/watch?v=6M3LzGmIAso'

    # return jsonify({'video_url': video_url})
    #return "Hello world!"

# @app.route('/video_page')
# def video_page():
#     return render_template('video_page.html')

# @app.route('/generate_video')
# def generate_video():
#     try:
#         process_data()
#         return ''
#     except:
#         print("something went wrong")

@app.route('/demo_video.mp4')
def get_video():
    video_path = "./demo_video.mp4"  # Replace this with the path to your video file
    return send_file(video_path, as_attachment=True)


@app.route('/video_page')
def video_page():
    # Logic to determine remaining time and spinner visibility
    remaining_time = 180  # Assuming 180 seconds remaining
    spinner_visible = True  # Show spinner

    return render_template('video_page.html', remaining_time=remaining_time, spinner_visible=spinner_visible)




if __name__ == '__main__':
    app.run(debug=True, threaded=True)