# Cadmas web image processing

This repository contains scripts for product image processing. Photos are taken of the products with a mostly white / light gray background and these scripts prepare them for a darknet model that returns the bounding boxes of these products. The postprocessing script cuts out a square that contains the bounding box of the product if possible.
