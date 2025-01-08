
# Image Processing Application

This application allows you to process images automatically using the **Cloudinary** API. It uploads images, processes them to specific dimensions, downloads them locally, and deletes them from Cloudinary to save credits.

![Cloudinary Platform Screenshot](https://res.cloudinary.com/drycov6o6/image/upload/v1736355406/wilmer-portafolio/aaqvsgerbqj2bhp3sv5h.png)

## Features
- Upload images to Cloudinary.
- Resize images to specific dimensions (1000x460 px by default) while maintaining quality.
- Automatically delete processed images from Cloudinary after downloading.
- Easy configuration through a `.env` file.

## Requirements
- Python 3.8 or higher
- A Cloudinary account ([Sign up here](https://cloudinary.com/))
- Installed dependencies (see [Installation](#installation) section).

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**:
   - Create a `.env` file in the root directory:
     ```bash
     touch .env
     ```
   - Add your Cloudinary credentials to the `.env` file:
     ```env
     CLOUDINARY_CLOUD_NAME=your_cloud_name
     CLOUDINARY_API_KEY=your_api_key
     CLOUDINARY_API_SECRET=your_api_secret
     ```

## Usage

1. **Place your images in the `imagenes` folder**:
   The application will automatically create this folder if it doesn't exist.

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **Processed images**:
   Processed images will be saved in the `imagenes_procesadas` folder.

4. **Output**:
   - Uploaded images will be processed to the desired dimensions (1000x460 px).
   - Images will be automatically removed from Cloudinary after processing.

## File Structure
```
project/
├── .env                  # Environment variables file
├── requirements.txt      # Dependencies
├── main.py               # Main script
├── README.md             # Documentation
├── imagenes/             # Input images folder
└── imagenes_procesadas/  # Output images folder
```

## Cloudinary
This project uses the [Cloudinary](https://cloudinary.com/) platform for image processing. Cloudinary provides a powerful API for uploading, transforming, and managing images in the cloud.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```