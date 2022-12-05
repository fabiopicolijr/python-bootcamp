import colorgram

rgb_colors = []
colors = colorgram.extract('painting.jpg', 30)

for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(new_color)


print(rgb_colors)