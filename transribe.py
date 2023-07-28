import openai
import docx
import os

API_KEY = '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'
model = 'whisper-1'
#specialized prompt for clarity
personalPrompt = 'This is the audio lectures of a history class about US history from past to present.'

###
#   This script is used to transcribe audio files into text files
#   The audio files are stored in ~/HIST300_Audio_Lecture
#   The text files are stored in ~/Code/WhisperProject/Transcripts
###
# os.path.expanduser treats ~ as the home directory
audio_file_folder = os.path.expanduser('~/HIST300_Audio_Lecture')
transcripted_file_folder = os.path.expanduser('~/Code/WhisperProject/Transcripts')

def transcribe(audio_file_path):
    audio_file = open(audio_file_path, 'rb')
    transcript = openai.Audio.transcribe(
        api_key = API_KEY,
        model = model, 
        file = audio_file, 
        prompt = personalPrompt)
    return transcript['text']

def saveToDoc(transcript, transcripted_file_path):
    doc = docx.Document()
    doc.add_paragraph(transcript)
    doc.save(transcripted_file_path)


if __name__ == "__main__":
    audio_files = os.listdir(audio_file_folder)
    for file in audio_files:
        if(file.endswith('.mp3')):
            print(f'Transcribing {file}')
            audio_file_path = os.path.join(audio_file_folder, file)
            transcript = transcribe(audio_file_path)
            # file[:-4] removes the .mp3 extension
            transcripted_file_path = os.path.join(transcripted_file_folder, 'Transcripted-' +  file[:-4] + '.docx')
            saveToDoc(transcript, transcripted_file_path)
            print(f'Saved to {transcripted_file_path}')