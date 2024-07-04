from moviepy.editor import VideoFileClip
import streamlit as st
import tempfile
import base64

st.title("Video to GIF Converter")

uploaded_file = st.file_uploader("Choose the video file:", type='mp4')
tfile = tempfile.NamedTemporaryFile(delete=False)

if uploaded_file is not None:
    tfile.write(uploaded_file.read())

    #Load the video file
    clip = VideoFileClip(tfile.name)

    #cutting the video to make it short
    clip = clip.subclip(0, 50) 

    #get the duration of the video
    duration = clip.duration

run = st.button("Convert")
if run:
    #Loop to create multiple gifs
    start= 0
    for i in range(0,int(duration/10)):
        gif = clip.subclip(start, start+10) 
        gif.write_gif(f"mygif{i}.gif",fps=10)
        start= start+10
        
        #display GIF
        file_ = open(f"mygif{i}.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
