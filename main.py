import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path, language='eng'):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=language)
        return text.strip()
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return None

def process_images_in_folder(folder_path, language='eng'):
    """Processes images in a folder and extracts text."""
    extracted_texts = {}
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp')):
                image_path = os.path.join(folder_path, filename)
                extracted_text = extract_text_from_image(image_path, language)
                if extracted_text is not None:
                    extracted_texts[filename] = extracted_text
                else:
                    print(f"OCR failed for: {filename}")
            else:
                print(f"Skipping non-image file: {filename}")

    except FileNotFoundError:
        print(f"Error: Folder not found at {folder_path}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    return extracted_texts

if __name__ == "__main__":
    folder_path = "/Volumes/Livre/ap_ai_raiz/Marketing_Sidarta_Djalma/Sidarta/fotos contatos whatsapp/jusprompt"  # Replace with your folder path
    extracted_data = process_images_in_folder(folder_path, language='eng')

    if extracted_data:
        for filename, text in extracted_data.items():
            print(f"Extracted Text from {filename}:\n{text}\n")
    else:
        print("No text extracted or folder not found.")