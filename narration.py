# from elevenlabs import generate, set_api_key, save, RateLimitError
from openai import OpenAI
import os
# from elevenlabs.client import ElevenLabs
# from elevenlabs import play,stream, save, voice_generation


# elevenlabs_key = os.getenv("575c12ea6827ef74f1630fc749963b5a")

# if elevenlabs_key:
#     set_api_key(elevenlabs_key)
# client = ElevenLabs(api_key=elevenlabs_key, # Defaults to ELEVEN_API_KEY
# )
client = OpenAI(api_key='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')

narration_api = "openai" # (or "openai")

def parse(narration):
    data = []
    narrations = []
    lines = narration.split("\n")
    for line in lines:
        if line.startswith('Narrator: '):
            text = line.replace('Narrator: ', '')
            data.append({
                "type": "text",
                "content": text.strip('"'),
            })
            narrations.append(text.strip('"'))
        elif line.startswith('['):
            background = line.strip('[]')
            data.append({
                "type": "image",
                "description": background,
            })
    return data, narrations

def create(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    n = 0
    for element in data:
        if element["type"] != "text":
            continue

        n += 1
        output_file = os.path.join(output_folder, f"narration_{n}.mp3")

        if narration_api == "openai":
            audio = client.audio.speech.create(
                input=element["content"],
                model="tts-1",
                voice="alloy",
            )

            audio.stream_to_file(output_file)
        else:
            audio = client.generate(
                text=element["content"],
                voice="Michael",
                model="eleven_monolingual_v1"
            )
            save(audio, output_file)
