import imageio
import numpy as np    
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--gif1", required=True, help="The First gif")
parser.add_argument("--gif2", required=True, help="The Second gif")
args = parser.parse_args()

gif1 = imageio.get_reader(args.gif1)
gif2 = imageio.get_reader(args.gif2)

num = min(gif1.get_length(), gif2.get_length()) 

new_gif = imageio.get_writer('output.gif')

for frame_number in range(num):
        img1 = gif1.get_next_data()
        img2 = gif2.get_next_data()
        new_image = np.hstack((img1, img2))
        new_gif.append_data(new_image)

gif1.close()
gif2.close()    
new_gif.close()

# convert -delay 0 -loop 0 output.gif loopingImage.gif
