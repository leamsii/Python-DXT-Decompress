# Python S3TC DXT1/5 Texture Decompression

<small>Inspired by <a href = "https://github.com/Benjamin-Dobell/s3tc-dxt-decompression">Benjamin Dobell</a>

<p> This script decompresses compressed S3 Textures to raw pixels</p>

<h2>Quick Tutorial</h2>

An instance of the DXTBuffer class needs to be created with the Texture's width/height as arguments.

Then simply call the DXTDecompress(file) function. The file must be open and the file pointer needs to be at the start of the compressed DXT data.

<h2>Bonus</h2>
Inside the sample folder there is a small script that converts Don't Starve's .TEX Textures to PNG using DXTDecompress

<h6>Feel free to report any discovered issues</h6>
