import argparse
import json
from whisper_transcribe import load_whisper_model, transcribe_audio
from llm_analysis import analyze_transcript_azure, analyze_transcript_ollama

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio and generate meeting insights")
    parser.add_argument("audio_file", type=str, help="Path to audio file")
    parser.add_argument("--use", type=str, choices=["azure", "ollama"], default="azure",
                        help="Choose LLM backend: azure or ollama")
    args = parser.parse_args()

    pipe = load_whisper_model()
    transcript, raw_json = transcribe_audio(pipe, args.audio_file)

    with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    with open("outputs/transcript.json", "w", encoding="utf-8") as f:
        json.dump(raw_json, f, indent=2)

    print("\n✅ Transcription complete. Running analysis...\n")

    if args.use == "azure":
        insights = analyze_transcript_azure(transcript)
    else:
        insights = analyze_transcript_ollama(transcript)

    with open("outputs/meeting_insights.txt", "w", encoding="utf-8") as f:
        f.write(insights)

    print("🔍 Analysis complete.\n")
    print(insights)