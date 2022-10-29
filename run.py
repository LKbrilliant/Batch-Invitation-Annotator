# Code By: Anuradha Gunawardhana (@LKBrilliant)
# Date: 24.10.2022
# Description: Make named invitation cards
# Requirements: Empty invitation image, guest list, font file and this script needs to be in the same directory

from PIL import Image, ImageFont, ImageDraw
import os
import sys

empty_card_file_came = "Invitation.png"     # File name of the invitation image (JPG or PNG)
guest_name_text_file = "Name_List.txt"      # Text file containing the guest list. Each name should start in a new line.
invitation_dir_name = "Invitations"         # Name of the directory which the final invitations should be saved
font_file_name = "OoohBaby-Regular.ttf"     # https://fonts.google.com/specimen/Oooh+Baby?query=oooh
nameLineHeight = 330                        # Vertical space from top of the card to the name line
fontSize = 35
fontColor = (0,0,0)                         # Red, Green, Blue (0-255)

def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count}", end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def main():
    num_lines = sum([1 for i in open(guest_name_text_file,"r").readlines() if i.strip()]) # Get the total number of names
    if not os.path.exists(invitation_dir_name):
        print("\n[Creating]: A new directory named \"{}\"\n".format(invitation_dir_name))
        os.makedirs(invitation_dir_name)

    with open(guest_name_text_file, 'r') as f:
        for i in progressbar(range(num_lines), "[Processing]: ", 40):
            line = f.readline()
            guestName = line.strip()    # Remove line endings

            card = Image.open(empty_card_file_came)
            cardWidth,_ = card.size
            fontFace = ImageFont.truetype(font_file_name, fontSize)
            card_editable = ImageDraw.Draw(card)
            txtWidth,_ = card_editable.textsize(guestName, font=fontFace)   # Get text length before placing
            txtPos_y = nameLineHeight - fontSize
            txtPos_x = cardWidth/2 - txtWidth/2                             # Place the name in the center
            card_editable.text((txtPos_x,txtPos_y), guestName, fontColor, font=fontFace)
            card.save("{}/{}.png".format(invitation_dir_name,guestName))
    print("[Done]: {} invitations saved in the \"{}\" directory\n".format(num_lines,invitation_dir_name))

if __name__ == "__main__":
    main()




    