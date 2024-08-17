# imagetolatex
Takes images (handwritten problems or screenshots of problems) and converts them into LaTeX.
Two models with two different datasets. note: running a handwritten equation on the typed one will result in less-than-optimal results

## Typed model
Cropped images used from the database <sup>1</sup> and placed in a folder called **fixed_formula_images** using crop.py Note: some images in the database were blank so those were removed in the new folder while running crop.py. This process had to happen since the formulas were too small to use effectively. Uses a bounding box and expands it since small pieces are being cut out.

Images are then prosecuted in loadata.py which shrinks the images again and adjusts the contrast and brightness to make the image more usable. Not sure if less or more preprocessing is needed to be computationally efficient as that is the goal of this project.

The model implemented is similar to that of Singh et al. <sup>2</sup> but goes up to block 3 instead of 4. 

This repo is for a project called **MathFusion**.

## Handwritten Model
Contained in Kaggle as seen in the .ipynb. Will use a transformer for the model(most likely) 

# Citations
1. Kanervisto, A. (2016). im2latex-100k , arXiv:1609.04938 [Data set]. Zenodo. https://doi.org/10.5281/zenodo.56198
2. Singh, S. S., & Karayev, S. (2021). Full Page Handwriting Recognition via Image to Sequence Extraction. In Document Analysis and Recognition – ICDAR 2021 (pp. 55–69). doi:10.1007/978-3-030-86334-0_4
