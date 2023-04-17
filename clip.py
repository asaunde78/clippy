import subprocess
import math
# Set the input and output file paths
# Set the input and output file paths

class Clippy:
    def __init__(self,folder="contents",output="output"):
        if folder:
            self.folder = folder+"/"
        else:
            self.folder = ""
        self.output = output

    def textonimage(self,text,image):
        
        input_image = self.folder + image
        output_image = self.folder + self.output + "." + image.split(".")[1]
        imagemagick_cmd = ['convert', input_image,'-size', '70%x150', 'caption:' + text, '-background', 'transparent', '-gravity', 'South', '-pointsize', '24', '-fill', 'white', '-stroke', 'black', '-strokewidth', '1','-composite', output_image]
        subprocess.run(imagemagick_cmd)
    def imageaudiotovid(self,image,audio):
        input_image = self.folder +image
        input_audio = self.folder +audio
        output_video = self.folder + self.output + ".mp4"
        ffmpeg_cmd = ['ffmpeg', '-y','-loop', '1', '-i', input_image, '-i', input_audio, '-filter:v', "scale=w=1024:h=trunc(ow/a/2)*2", '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p', '-shortest', output_video]
        subprocess.run(ffmpeg_cmd)
        return self.output + ".mp4"
    def imagestogif(self,delay = 10,filesize=7):
        output_gif = self.folder + self.output  + ".gif"
        imagemagick_command = ["convert","-delay",f"{delay}","-loop","0",'-resize',"800x600!",self.folder+"*.png",self.folder+"*.jpeg",self.folder+"*.jpg", '-define',f"-target-size={filesize}MB", output_gif]
        subprocess.run(imagemagick_command)
        return self.output  + ".gif"
        # if(engine == "ff"):
        #     if(not glob):
        #         input_image = self.folder + images
        #         # ffmpeg_cmd = ['ffmpeg', '-y','-i', input_image, "-r", str(framerate),'-delay',f'{delay}','-vf',f"setpts=(1/{frametiming})*PTS",'-fs','7.9M',  output_gif]
        #         ffmpeg_cmd = ['ffmpeg', '-y','-i', input_image, "-r","24",'-vf', f"setpts=(1/{frametiming})*PTS", '-fs','7M',  output_gif]
        #     else:
            

                
        #         # ffmpeg_cmd = ['ffmpeg', '-y','-i', input_image, "-r", str(framerate),'-delay',f'{delay}','-vf',f"setpts=(1/{frametiming})*PTS",'-fs','7.9M',  output_gif]
        #         ffmpeg_cmd = ['ffmpeg', '-y', "-pattern_type","glob",'-i',self.folder+f"*.{filetype}", "-r","24",'-vf', f"setpts=(1/{frametiming})*PTS", '-fs','7M',  output_gif]
    def ffimagestogif(self,frametiming=.4,filesize=15,ftype="jpg"):
        output_gif = self.folder + self.output  + ".gif"
        
        ffmpeg_cmd = ['ffmpeg', '-y', "-pattern_type","glob",'-i',self.folder+f"*.{ftype}", "-r","60",'-vf', f"setpts=({frametiming})*PTS", '-fs',f'{filesize}M',  output_gif]
        subprocess.run(ffmpeg_cmd)
        return self.output  + ".gif"
    def imagestocollage(self,filesize=10, count=None,squares=True):
        ftype = "jpeg"
        output_image = self.folder + self.output + f".{ftype}"
        if count:
            rows = int(math.ceil(count**0.5))
            cols = int(math.ceil(count / rows))
            print(f"{rows}x{cols}")
        imagemagick_command = ["montage", self.folder+"*.png",self.folder+"*.jpeg",self.folder+"*.jpg","-resize",("600x600!" if squares else "800x"),"-geometry", "+0+0", "-tile", (f"{rows}x{cols}" if count else "5x"), "-background","none",output_image]
        subprocess.run(imagemagick_command)
        return self.output + f".{ftype}"
    def changeimagetype(self,ftype="jpg"):
        types = ["jpg","jpeg","png"]
        types.remove(ftype)
        print(ftype,types)
        imagemagick_command = ["mogrify","-format",ftype,f"{self.folder}*.{types[0]}",f"{self.folder}*.{types[1]}"]
        subprocess.run(imagemagick_command)
        return True
        
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
