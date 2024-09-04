from PIL import Image, ImageFilter
import os
import inquirer


image = Image.open('images/tajoriginal.jpeg')


questions = [
    inquirer.List(
        "choice",
        message="what operation you need to perform on 'tajoriginal.jpeg'?",
        choices=["rename the file to 'notsoimportant.jpeg'", "convert to grey", "blur the image", "change one pixel"]
    )
]

answers = inquirer.prompt(questions)


if answers["choice"] == "convert to grey":
    image.show()
    grey_img = image.convert('L')
    grey_img.save('images/tajoriginal.jpeg')
    grey_img.show()

elif answers["choice"] == "blur the image":
    image.show()
    blur_img = image.filter(ImageFilter.GaussianBlur(6))
    blur_img.save('images/tajoriginal.jpeg')
    blur_img.show()

elif answers["choice"] == "change one pixel":
    image.show()
    image.putpixel((0,0), (10,10,10))
    image.save('images/tajoriginal.jpeg')
    image.show()

else:
    os.rename('images/tajoriginal.jpeg', 'images/notsoimportant.jpeg')