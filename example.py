from path import Path
from main import gen_qr_code

text = "https://vk.com/it_cube_gagarin"
#text = "https://t.me/Gagarin_it_cube"


path_to_download = Path().joinpath("example", "Cat.png")
path_to_save = Path().joinpath("example", "qr_code_out.png")

gen_qr_code(text, path_to_download, path_to_save)