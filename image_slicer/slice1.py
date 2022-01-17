from image_slicer import slice, save_tiles

tiles = slice('pexels-cup-of-couple.jpg',16, save=False)
save_tiles(tiles, directory="/home/ruli/coding/python-playground/image_slicer/result_slice1", prefix='pexels_slice', format="jpeg")
