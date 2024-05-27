Dataset: https://figshare.com/articles/dataset/brain_tumor_dataset/1512427

In this project, the dataset available at the url above will be used.
Composed of brain tumor MRI images containing 3,064 contrast-enhanced T1 images
of 233 patients with three types of brain tumor: meningioma (708 slices), glioma (1,426 slices) and pituitary tumor (930 slices). Due to the file size limit of the repository, the entire dataset was divided into 4 subsets, resulting in 4 .zip files with each .zip file containing 766 slices.

-----

This data is organized in matlab data format (.mat file). Each file stores a structure containing the following fields for an image:

cjdata.label: 1 for meningioma, 2 for glioma, 3 for pituitary tumor
cjdata.PID: Patient ID
cjdata.image: image data
cjdata.tumorBorder: a vector that stores the coordinates of discrete points on the tumor border.
cjdata.tumorMask: a binary image with 1s indicating the tumor region
