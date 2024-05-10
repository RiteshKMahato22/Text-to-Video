#!/usr/bin/env python3

from openai import OpenAI
import time
import json
import sys
import os

import narration
import images
import video

client = OpenAI(api_key='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')
# print({sys.argv(source)}.format(source='source.txt'))
# if len(sys.argv) < 2:
#     print(f"USAGE: {sys.argv[0]} SOURCE_FILENAME")
#     sys.exit(1)

# with open(sys.argv[1],"rt") as f:
#     try:
#         source_material = f.read()
#     except:
#         source_material='something went wrong'
#         print(sys.argv[1])

# with open("source.txt", "rt") as f:
#     try:
#         source_material = f.read()
#     except:
#         source_material = 'something went wrong'
#
# short_id = str(int(time.time()))
# output_file = "short.avi"
#
# basedir = os.path.join("shorts", short_id)
# if not os.path.exists(basedir):
#     os.makedirs(basedir)
#
# print("Generating script...")
#
# response = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "system",
#             "content": """You are a YouTube short narration generator. You generate 30 seconds to 1 minute of narration. The shorts you create have a background that fades from image to image as the narration is going on.
#
# You will need to generate descriptions of images for each of the sentences in the short. They will be passed to an AI image generator.
#
# Note that the narration will be fed into a text-to-speech engine, so don't use special characters.
#
# Respond with a pair of an image description in square brackets and a narration below it. Both of them should be on their own lines, as follows:
#
# ###
#
# [Narration Prompt]
#
# Narrator:"Generate a narration explaining the Contact Index (CI), and its significance in measuring user friction. Include details on how CI is calculated, its implications for product quality, and the process of setting CI goals every quarter."
#
# [Image Prompt]
#
# Narrator:"Create an image illustrating the Contact Index (CI) calculation process, showcasing the formula CI = scale × tickets / users. Include visual representations of Cloud and Server platforms, user interactions, and support tickets."
#
# [Video Prompt]
# Narrator:"Produce a video presentation on the importance of Contact Index (CI) in evaluating user experience. Include animations demonstrating how CI is measured, its impact on product improvement, and the collaboration between support teams and product development to address friction."
#
#
# ###
#
# The short should be 10 sentences maximum.
#
# You should add a description of a fitting backround image in between all of the narrations. It will later be used to generate an image with AI.
# """
#         },
#         {
#             "role": "user",
#             "content": f"Create a YouTube short narration based on the following source material:\n\n{source_material}"
#         }
#     ]
# )
#
# response_text = response.choices[0].message.content
# response_text.replace("’", "'").replace("`", "'").replace("…", "...").replace("“", '"').replace("”", '"')
#
# with open(os.path.join(basedir, "response.txt"), "w") as f:
#     f.write(response_text)
#
# data, narrations = narration.parse(response_text)
# with open(os.path.join(basedir, "data.json"), "w") as f:
#     json.dump(data, f, ensure_ascii=False)
#
# print(f"Generating narration...")
# narration.create(data, os.path.join(basedir, "narrations"))
#
# print("Generating images...")
# images.create_from_data(data, os.path.join(basedir, "images"))
#
# print("Generating video...")
# video.create(narrations, basedir, output_file)
#
# print(f"DONE! Here's your video: {os.path.join(basedir, output_file)}")

def process_data():
    with open("source.txt", "rt") as f:
        try:
            source_material = f.read()
        except:
            source_material = 'something went wrong'

    short_id = str(int(time.time()))
    output_file = "short.mp4"

    basedir = os.path.join("shorts", short_id)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    print("Generating script...")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": """You are a YouTube short narration generator. You generate 30 seconds to 1 minute of narration. The shorts you create have a background that fades from image to image as the narration is going on.

    You will need to generate descriptions of images for each of the sentences in the short. They will be passed to an AI image generator.  

    Note that the narration will be fed into a text-to-speech engine, so don't use special characters.

    Respond with a pair of an image description in square brackets and a narration below it. Both of them should be on their own lines, as follows:

    ###

    [Narration Prompt: This narration is about how to summarise steps to follow for the team going on a vacation.]

    Narrator:"Communicating steps like setting up calendars, notifying managers, arranging coverage for responsibilities, and updating communication tools."

    [Image Prompt: This is about preparing ourselves for vacation through setting up calendars, notifying managers, arranging coverage for responsibilities, and updating colleagues.]

    Narrator:"Communicating my vacation preparation process, encompassing calendar updates, discussions with a manager, scheduling coverage for roles, and setting up Out of Office notifications to ensure smooth operations"

    

    ###

    The short should be 10 sentences maximum.

    You should add a description of a fitting backround image in between all of the narrations. It will later be used to generate an image with AI.
    """
            },
            {
                "role": "user",
                "content": f"Create a YouTube short narration based on the following source material:\n\n{source_material}"
            }
        ]
    )

    response_text = response.choices[0].message.content
    response_text.replace("’", "'").replace("`", "'").replace("…", "...").replace("“", '"').replace("”", '"')

    with open(os.path.join(basedir, "response.txt"), "w") as f:
        f.write(response_text)

    data, narrations = narration.parse(response_text)
    with open(os.path.join(basedir, "data.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"Generating narration...")
    narration.create(data, os.path.join(basedir, "narrations"))

    print("Generating images...")
    images.create_from_data(data, os.path.join(basedir, "images"))

    print("Generating video...")
    video.create(narrations, basedir, output_file)

    print(f"DONE! Here's your video: {os.path.join(basedir, output_file)}")
