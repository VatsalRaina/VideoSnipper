from moviepy.editor import *

def make_snips(input_file, times, snippet_length):

    # Open clip
    clip = VideoFileClip(input_file)

    # Remove audio
    clip_no_audio = clip.set_audio(None)

    # Extract the times into a list
    times_list = times.split()

    output_clip_prefix = "clip"
    for clip_num, start_time in enumerate(times_list):

        # Get time in correct format
        parts = start_time.split(':')
        min = parts[0]
        secs = parts[1]

        overall_secs = float(min)*60 + float(secs)

        start = overall_secs
        end = overall_secs + float(snippet_length)

        clipped = clip_no_audio.subclip(start, end)

        # Write to file
        out_name = output_clip_prefix + str(clip_num)+".mp4"
        clipped.write_videofile(out_name)
