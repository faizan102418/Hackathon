import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

# Function to fetch YouTube transcript
def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

# Function to summarize the transcript
def summarize_text(transcript):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to extract video ID from URL
def extract_video_id(url):
    video_id_match = re.search(r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        return None

# Streamlit App Layout
st.set_page_config(page_title="YouTube Transcript Summarizer", layout="centered")
st.title("YouTube Transcript Summarizer")
st.write("### Enter the YouTube video URL below and click 'Summarize'.")

# Input field for YouTube URL
video_url = st.text_input("YouTube Video URL", "")

# Button to trigger summarization
if st.button("Summarize"):
    if video_url:
        video_id = extract_video_id(video_url)  # Extract video ID from URL
        if video_id:
            # Fetch and display the transcript
            transcript = get_youtube_transcript(video_id)
            if "Error" not in transcript:
                st.subheader("Original Transcript:")
                st.write(transcript)
                
                # Summarize and display the summary
                st.subheader("Summarized Transcript:")
                summary = summarize_text(transcript)
                st.write(summary)
            else:
                st.error(transcript)
        else:
            st.error("Invalid YouTube URL. Please enter a valid URL.")
    else:
        st.error("Please enter a valid YouTube URL.")
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

# Function to fetch YouTube transcript
def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

# Function to summarize the transcript
def summarize_text(transcript):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to extract video ID from URL
def extract_video_id(url):
    video_id_match = re.search(r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        return None

# Streamlit App Layout
st.set_page_config(page_title="YouTube Transcript Summarizer", layout="centered")
st.title("YouTube Transcript Summarizer")
st.write("### Enter the YouTube video URL below and click 'Summarize'.")

# Input field for YouTube URL
video_url = st.text_input("YouTube Video URL", "")

# Button to trigger summarization
if st.button("Summarize"):
    if video_url:
        video_id = extract_video_id(video_url)  # Extract video ID from URL
        if video_id:
            # Fetch and display the transcript
            transcript = get_youtube_transcript(video_id)
            if "Error" not in transcript:
                st.subheader("Original Transcript:")
                st.write(transcript)
                
                # Summarize and display the summary
                st.subheader("Summarized Transcript:")
                summary = summarize_text(transcript)
                st.write(summary)
            else:
                st.error(transcript)
        else:
            st.error("Invalid YouTube URL. Please enter a valid URL.")
    else:
        st.error("Please enter a valid YouTube URL.")
