import whisper
import ollama
import sounddevice as sd
from ollama import chat, ChatResponse, generate

# Config
model = whisper.load_model("base")
recordtime = 30 #sec


def DecodeAudio(): # แปล Speak to text
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("narration(1).mp3") # หามาใส่เด้อหล่า
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    return(result.text)

result = DecodeAudio() # Return ^

def main(): #process text
    stream = chat(
    model='qwen2.5:0.5b',
    messages=[{'role': 'user', 'content': result}],
    # messages=[{'role': 'user', 'content': "Where do you keep the chat logs?"}],
    stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    DecodeAudio()
    main()
