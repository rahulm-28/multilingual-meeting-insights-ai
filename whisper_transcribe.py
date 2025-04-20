import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os

model_id = "openai/whisper-large-v3"

def get_device():
    if torch.backends.mps.is_available():
        return "mps"
    elif torch.cuda.is_available():
        return "cuda:0"
    return "cpu"

def load_whisper_model():
    device = get_device()
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print(f"🚀 Loading Whisper model on device: {device}...")
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True
    ).to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
    )
    return pipe

def transcribe_audio(pipe, audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print(f"🎧 Transcribing audio file: {audio_path}")

    result = pipe(
        audio_path,
        return_timestamps=True,
        generate_kwargs={"task": "translate", "language": "en"}
    )

    formatted_segments = [
        f"[{round(seg['timestamp'][0], 1)}s - {round(seg['timestamp'][1], 1)}s] {seg['text']}"
        for seg in result.get("chunks", [])
    ]
    full_text = "\n".join(formatted_segments)
    return full_text, result