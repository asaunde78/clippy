import subprocess

# Set the input and output file paths
# Set the input and output file paths

class Clippy:
    def __init__(self,folder="contents",output="output"):
        if folder:
            self.folder = folder+"/"
        else:
            self.folder = ""
        self.output = output

    def imageaudiotovid(self,image,audio):
        input_image = self.folder +image
        input_audio = self.folder +audio
        output_video = self.folder + self.output + ".mp4"
        ffmpeg_cmd = ['ffmpeg', '-y','-loop', '1', '-i', input_image, '-i', input_audio, '-filter:v', "scale=w=1024:h=trunc(ow/a/2)*2", '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p', '-shortest', output_video]
        subprocess.run(ffmpeg_cmd)
        return self.output + ".mp4"

    def textonvideo(self,text,video,fontsize = 24,font="Arial",align=2):
        
        with open("subtitles.srt" ,"w") as r:
            r.write("1\n00:00:00,000 --> 10:00:00,000\n"+text)
        #text = split_txt_into_multi_lines(text, 37)
        input_video = self.folder + video
        output_video_text = self.folder +self.output + '_text.mp4'

        #ffmpeg_cmd = ['ffmpeg', '-y','-i', input_video, '-vf', f'[0:v]drawtext=fontfile=Roboto.ttf:text=\'{text}\':fontcolor=white:fontsize=45:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-(text_h+30))[outv]', '-codec:a', 'copy', output_video_text]
        ffmpeg_cmd = ['ffmpeg', '-y','-i', input_video, '-vf', f"subtitles=subtitles.srt:force_style='FontName={font},Alignment={align},Fontsize={fontsize}'", '-codec:a', 'copy', output_video_text]

        subprocess.run(ffmpeg_cmd)
        return self.output + '_text.mp4'

# clip = Clippy()

# text = "Okay! What if the text is really long,\
#  and I mean like- REALLY LONG! XD HAHA I feel like there are a lot of \
# very long lines in league lol\n-Ashe"
# clip.textonvideo(text,clip.imageaudiotovid("image.jpg","audio.ogg"))






