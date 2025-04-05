# Zenkai IMP Dataset Preparation Tool

A utility for preparing datasets for image-to-image machine learning models with associated prompts and masks.

[Workflows: IMP Dataset Creation and Loading Nodes](https://github.com/MushroomFleet/DJZ-Workflows/tree/main/DJZ-Nodes-Examples/ZenkaiImageMaskPrompt)

## 📋 Overview

The Zenkai IMP Dataset Preparation Tool simplifies the process of creating properly structured datasets for image-to-image machine learning models. It automates the collection and organization of:

- Source images
- Text prompts associated with images
- Image masks with proper naming

The tool reads a simple JSON configuration file that points to your source directories, then creates a timestamped dataset folder with all files properly organized according to the required format.

## ✨ Features

- Creates a timestamped dataset folder to prevent overwriting
- Handles various prompt file scenarios:
  - If there's only one prompt file, duplicates it for all images
  - If there are multiple prompt files, copies them directly
- Automatically appends "_M" to mask filenames
- Simple configuration through a JSON file
- Detailed console output during processing

## 🔧 Installation

### Requirements

- Python 3.6 or higher
- Windows operating system

### Setup

1. Clone or download this repository:
```
git clone https://github.com/your-username/zenkai-imp-prepare.git
cd zenkai-imp-prepare
```

2. Run the installation script:
```
install.bat
```

This will:
- Create a Python virtual environment
- Install required dependencies
- Prepare the environment for running the tool

## ⚙️ Configuration

The tool uses a JSON configuration file (`config.json`) to locate your source files. Create this file with the following structure:

```json
{
  "base_path": "C:/path/to/your/data/folder"
}
```

### Expected Folder Structure

Your data folder should be organized as follows:

```
C:/path/to/your/data/folder/
├── images/            # Source images
├── prompts/           # Text prompt files (.txt)
└── mask/              # Mask image files
```

## 🚀 Usage

1. Create and edit your `config.json` file as described above
2. Run the tool:
```
run.bat
```

3. The tool will:
   - Create a new folder named `dataset_YYYYMMDD_HHMMSS` in your base path
   - Copy all images directly from the `images` folder
   - Handle prompt files according to the logic:
     - If only one prompt file exists, duplicate it for each image
     - If multiple prompt files exist, copy them all
   - Copy mask files with "_M" appended to filenames

4. Check the console output for details on the process and any errors

## 📁 Output Structure

After running the tool, your dataset will be structured as:

```
C:/path/to/your/data/folder/dataset_YYYYMMDD_HHMMSS/
├── image1.jpg         # Original images
├── image2.jpg
├── ...
├── image1.txt         # Prompt files (matched to images)
├── image2.txt
├── ...
├── mask1_M.jpg        # Mask files with _M suffix
├── mask2_M.jpg
└── ...
```

## 🔍 Advanced Usage

You can specify a different configuration file by passing it as an argument:

```
run.bat path/to/custom-config.json
```

## 🛠️ Troubleshooting

- If you see an error about Python not being installed, make sure Python is installed and added to your PATH
- If paths in your configuration file aren't being recognized, make sure to use forward slashes (`/`) or escaped backslashes (`\\`) in your JSON file
- Check that your base folder contains the required subfolders: `images`, `prompts`, and `mask`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
