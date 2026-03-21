import whisper
import ollama
from ollama import chat, ChatResponse, generate

# Config whisper
model = whisper.load_model("base")

def DecodeAudio(): # แปล Speak to text
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("audio.mp3")
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
    return(result.text)

def main(): #process text
    stream = chat(
    model='qwen2.5:0.5b',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    DecodeAudio()
    # main()
