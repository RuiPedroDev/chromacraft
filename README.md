## Chormacraft image editing tool

_________ .__                                _________                _____  __   
\_   ___ \|  |_________  ____   _____ _____  \_   ___ \____________ _/ ____\/  |_ 
/    \  \/|  |  \_  __ \/  _ \ /     \\__  \ /    \  \/\_  __ \__  \\   __\\   __\
\     \___|   Y  \  | \(  <_> )  Y Y  \/ __ \\     \____|  | \// __ \|  |   |  |  
 \______  /___|  /__|   \____/|__|_|  (____  /\______  /|__|  (____  /__|   |__|  
        \/     \/                   \/     \/        \/            \/             


This is a simple image manipulation tool that leverages the PIL (Python Imaging Library) module for various image editing operations. It provides a set of command-line options for adjusting various image properties. 

### Requirements

- Python 3.5 or higher
- Pillow (PIL Fork)

### Installation

```bash
pip install Pillow
```

### Usage

```bash
python script.py image_path [--bright B] [--cont C] [--sat S] [--sharp S] [--invert] [--rotate R] [--blur B] [--glamour G] [--sepia S]
```

### Arguments

- `image_path`: Path to the image file.
- `--bright B`: Adjust brightness (float value).
- `--cont C`: Adjust contrast (float value).
- `--sat S`: Adjust saturation (float value).
- `--sharp S`: Adjust sharpness (float value).
- `--invert`: Invert the image color.
- `--rotate R`: Rotate the image by the specified degrees (float value).
- `--blur B`: Apply a Gaussian blur with the specified radius (float value).
- `--glamour G`: Apply a glamour filter with the specified intensity (float value).
- `--sepia S`: Apply a sepia filter with the specified intensity (float value).

### Examples

Adjust brightness:

```bash
python script.py image_path --bright 1.5
```

Invert image color:

```bash
python script.py image_path --invert
```

Apply a sepia filter:

```bash
python script.py image_path --sepia 0.6
```
