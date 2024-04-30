import os
import h5py
from PIL import Image
import pandas as pd

path = r'data\raw'
mat_path = r'data\raw\mat'
png_path = r'data\raw\png'
mask_path = r'data\raw\masks'

if not os.path.exists(png_path):
    os.makedirs(png_path)

if not os.path.exists(mask_path):
    os.makedirs(mask_path)

labels = []
pids = []
tumor_borders = []
image_paths = []
mask_paths = []
image_ids = []

for filename in os.listdir(mat_path):
    if filename.endswith('.mat'):

        with h5py.File(os.path.join(mat_path, filename), 'r') as file:
            cjdata = file['cjdata']
            label = int(cjdata['label'][0, 0])
            pid = "".join([chr(val[0]) for val in cjdata['PID'][()]]) 
            image_data = cjdata['image'][()]
            tumor_border = cjdata['tumorBorder'][()]
            tumor_mask_data = cjdata['tumorMask'][()]
        
        image_normalized_255 = (image_data / image_data.max()) * 255
        
        if label == 1:  
            mask_gray = tumor_mask_data * 85 # Meningioma
        elif label == 2: 
            mask_gray = tumor_mask_data * 170 # Glioma
        elif label == 3:  
            mask_gray = tumor_mask_data * 255 # Pituitary Tumor
        
        base_filename = os.path.splitext(filename)[0]
        
        image_id = base_filename.split('_')[-1]

        image = Image.fromarray(image_normalized_255.astype('uint8'))
        image.save(os.path.join(png_path, base_filename + '.png')) 
        
        mask_image = Image.fromarray(mask_gray.astype('uint8'))
        mask_image.save(os.path.join(mask_path, base_filename + '.png'))
        
        labels.append(label)
        pids.append(pid)
        tumor_borders.append(tumor_border.tolist())
        image_paths.append(os.path.join(png_path, base_filename + '.png'))
        mask_paths.append(os.path.join(mask_path, base_filename + '.png'))
        image_ids.append(image_id)

df = pd.DataFrame({
    'ID': image_ids,
    'Image Path': image_paths,
    'Mask Path': mask_paths,
    'Label': labels,
    'PID': pids,
    'Tumor Border': tumor_borders,
})

df.to_csv(os.path.join(path, 'metadata.csv'), index=False)