from PIL import Image
import os

original_dir = './original/ChictopiaPlus'

real_suffix = '_image:png.png'
sketch_suffix = '_label_vis:png.png'
new_suffix = '.png'

mode_list = [{'name': 'train', 'save_path': './train', 'number': 23012, 'padding': '{0:05d}'},
             {'name': 'test', 'save_path': './test', 'number': 2874, 'padding': '{0:04d}'},
             {'name': 'val', 'save_path': './val', 'number': 2914, 'padding': '{0:04d}'}]

original_image_size = (286, 286)

for mode in mode_list:
    print('Processing {}...'.format(mode["name"]))
    if not os.path.exists(mode['save_path']):
        os.mkdir(mode['save_path'])
    for index in range(mode['number']):
        index_padded = mode['padding'].format(index)
        real_image_path = os.path.join(original_dir, mode['name'], index_padded + real_suffix)
        sketch_image_path = os.path.join(original_dir, mode['name'], index_padded + sketch_suffix)
        real_image = Image.open(real_image_path)  # (286, 286)
        sketch_image = Image.open(sketch_image_path)  # (286, 286)
        canvas = Image.new("RGB", (original_image_size[0] * 2, original_image_size[1]))  # (512, 286)
        canvas.paste(sketch_image, (0, 0))
        canvas.paste(real_image, (original_image_size[0], 0))
        save_path = os.path.join(mode['save_path'], index_padded + new_suffix)
        canvas.save(save_path)
