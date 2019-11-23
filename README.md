# Python S3TC DXT1/5 Texture Decompression

<small>Inspired by <a href = "https://github.com/Benjamin-Dobell/s3tc-dxt-decompression">Benjamin Dobell</a>

<p> This script decompresses compressed S3 Textures to raw pixels</p>

<h2>Quick Tutorial</h2>

An instance of the DXTBuffer class needs to be created with the Texture's width/height as arguements.

Then simply call the DXTDecompress(file). The file must be open and the pointer needs to be at the compressed DXT data chunk
