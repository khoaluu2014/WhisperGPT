import whisper
from whisper.utils import get_writer
import docx
import os

model = whisper.load_model('base.en')
#specialized prompt for clarity
personalPrompt = 'This is the audio lectures of a history class about US history from past to present.'
###
#   This script is used to transcribe audio files into text files
#   The audio files are stored in ~/HIST300_Audio_Lecture
#   The text files are stored in ~/Code/WhisperProject/Transcripts
###
# os.path.expanduser treats ~ as the home directory
audio_file_folder = os.path.expanduser('~/HIST300_Audio_Lecture')
transcripted_file_folder = os.path.expanduser('~/Code/WhisperGPT/Transcripts')

def audioTranscribe(audio_file_path):
    audio_file = whisper.load_audio(audio_file_path)
    transcript = model.transcribe(audio_file, verbose = True, initial_prompt=personalPrompt, fp16 = True)
    return transcript

def saveAsTxt(transcript, transcripted_file_path, audio_file_path):
    txt_writer = get_writer('txt', transcripted_file_path)
    txt_writer(transcript, audio_file_path)

if __name__ == "__main__":
    audio_files = os.listdir(audio_file_folder)
    for file in audio_files:
        if(file.endswith('.mp3')):
            print(f'Transcribing {file}')
            audio_file_path = os.path.join(audio_file_folder, file)
            transcript = audioTranscribe(audio_file_path)
            saveAsTxt(transcript, transcripted_file_folder, audio_file_path)
            print(f'Saved to {transcripted_file_folder}')