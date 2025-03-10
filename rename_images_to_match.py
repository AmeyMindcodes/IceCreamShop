import os
import shutil
from django.utils.text import slugify

# Directory containing the images
image_dir = 'static/images'

# Mapping of flavor names to their slugified versions
flavor_names = [
    # Regular Flavors
    'Classic Vanilla',
    'Rich Chocolate',
    'Strawberry Delight',
    'Butter Pecan',
    'Coconut Jaggery',
    
    # Premium Flavors
    'Chocolate Chip Cookie Dough',
    'Mint Chocolate Chip',
    'Cookies and Cream',
    'Salted Caramel',
    'Malai Kulfi',
    'Kesar Pista',
    'Paan Delight',
    'Gulab Jamun',
    
    # Seasonal Flavors
    'Pumpkin Spice',
    'Peppermint Bark',
    'Summer Berry Swirl',
    'Mango Passion',
    'Alphonso Mango',
]

# Current image files we have
current_images = {
    # Regular Flavors
    'Classic Vanilla': 'classic_vanilla.jpg',
    'Rich Chocolate': 'rich_chocolate.jpg',
    'Strawberry Delight': 'strawberry_delight.jpg',
    'Butter Pecan': 'butter_pecan.jpg',
    'Coconut Jaggery': 'coconut_jaggery.jpg',
    
    # Premium Flavors
    'Chocolate Chip Cookie Dough': 'chocolate_chip_cookie_dough.jpg',
    'Mint Chocolate Chip': 'mint_chocolate_chip.jpg',
    'Cookies and Cream': 'cookies_and_cream.jpg',
    'Salted Caramel': 'salted_caramel.jpg',
    'Malai Kulfi': 'malai_kulfi.jpg',
    'Kesar Pista': 'kesar_pista.jpg',
    'Paan Delight': 'paan_delight.jpg',
    'Gulab Jamun': 'gulab_jamun.jpg',
    
    # Seasonal Flavors
    'Pumpkin Spice': 'pumpkin_spice.jpg',
    'Peppermint Bark': 'peppermint_bark.jpg',
    'Summer Berry Swirl': 'summer_berry_swirl.jpg',
    'Mango Passion': 'mango.jpg',
    'Alphonso Mango': 'alphonso_mango.jpg',
}

# Copy and rename the images to match the slugified names expected by the template
for flavor_name, current_image in current_images.items():
    slugified_name = slugify(flavor_name) + '.jpg'
    src_path = os.path.join(image_dir, current_image)
    dest_path = os.path.join(image_dir, slugified_name)
    
    if os.path.exists(src_path):
        try:
            # Copy instead of rename to keep the original files
            shutil.copy2(src_path, dest_path)
            print(f"✓ Copied {current_image} to {slugified_name}")
        except Exception as e:
            print(f"✗ Error copying {current_image} to {slugified_name}: {e}")
    else:
        print(f"✗ Source file {current_image} does not exist")

print("\nFinished renaming images to match slugified names!") 