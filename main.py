import os
import json
import shutil
import datetime
import sys
from pathlib import Path

def create_dataset(config_path):
    """
    Create a dataset according to specifications in the config file.
    
    Args:
        config_path (str): Path to the configuration JSON file
    """
    try:
        # Load configuration
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        base_path = config.get('base_path')
        if not base_path:
            print("Error: base_path not specified in configuration file")
            return False
        
        # Validate paths
        base_dir = Path(base_path)
        images_dir = base_dir / 'images'
        prompts_dir = base_dir / 'prompts'
        masks_dir = base_dir / 'mask'
        
        for dir_path in [base_dir, images_dir, prompts_dir, masks_dir]:
            if not dir_path.exists() or not dir_path.is_dir():
                print(f"Error: Directory {dir_path} does not exist or is not a directory")
                return False
        
        # Create timestamped dataset folder
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        dataset_name = f"dataset_{timestamp}"
        dataset_dir = base_dir / dataset_name
        
        if dataset_dir.exists():
            print(f"Warning: Dataset directory {dataset_dir} already exists. It will be overwritten.")
            shutil.rmtree(dataset_dir)
        
        dataset_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created dataset directory: {dataset_dir}")
        
        # Copy images
        image_files = list(images_dir.glob('*'))
        if not image_files:
            print("Warning: No image files found in the images directory")
        else:
            for image_file in image_files:
                if image_file.is_file():
                    shutil.copy2(image_file, dataset_dir)
            print(f"Copied {len(image_files)} image files to dataset directory")
        
        # Handle prompt files
        prompt_files = list(prompts_dir.glob('*.txt'))
        
        if len(prompt_files) == 0:
            print("Warning: No prompt files found")
        elif len(prompt_files) == 1:
            # If only one prompt file exists, duplicate it for each image
            prompt_file = prompt_files[0]
            prompt_content = prompt_file.read_text(encoding='utf-8')
            
            for image_file in image_files:
                if image_file.is_file():
                    prompt_name = f"{image_file.stem}.txt"
                    prompt_path = dataset_dir / prompt_name
                    prompt_path.write_text(prompt_content, encoding='utf-8')
            
            print(f"Duplicated single prompt file for {len(image_files)} images")
        else:
            # Copy all prompt files to dataset directory
            for prompt_file in prompt_files:
                if prompt_file.is_file():
                    shutil.copy2(prompt_file, dataset_dir)
            print(f"Copied {len(prompt_files)} prompt files to dataset directory")
        
        # Copy mask files with _M suffix
        mask_files = list(masks_dir.glob('*'))
        mask_count = 0
        
        for mask_file in mask_files:
            if mask_file.is_file():
                # Create new filename with _M suffix
                mask_name = f"{mask_file.stem}_M{mask_file.suffix}"
                mask_path = dataset_dir / mask_name
                shutil.copy2(mask_file, mask_path)
                mask_count += 1
        
        print(f"Copied {mask_count} mask files to dataset directory with _M suffix")
        print(f"\nIMP Dataset creation complete: {dataset_dir}")
        return True
        
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in configuration file {config_path}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return False

def main():
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "config.json"
    
    print("Zenkai IMP Dataset Preparation Tool")
    print("===================================")
    print(f"Using configuration file: {config_path}")
    
    success = create_dataset(config_path)
    
    if success:
        print("\nDataset creation completed successfully.")
    else:
        print("\nDataset creation failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
