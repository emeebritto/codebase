import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)
    with open('gravacao.wav', 'wb') as f:
        r.adjust_for_ambient_noise(source)
        f.write(audio.get_wav_data())
        
        
        
