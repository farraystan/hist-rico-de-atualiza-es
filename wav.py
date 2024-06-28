from moviepy.editor import AudioFileClip

# Caminho para o arquivo MP3
mp3_file = "GRAVAÇÃO/We'll Be Right Back - Sound Effect (HD).mp4"

# Caminho para o arquivo WAV de saída
wav_file = "GRAVAÇÃO/We'll Be Right Back - Sound Effect (HD).wav"

# Converter o arquivo MP3 para WAV
audio_clip = AudioFileClip(mp3_file)
audio_clip.write_audiofile(wav_file, codec='pcm_s16le')  # Especificando o codec PCM

