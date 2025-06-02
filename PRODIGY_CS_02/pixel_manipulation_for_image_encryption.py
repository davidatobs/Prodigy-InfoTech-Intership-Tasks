from PIL import Image
import random

def load_image(path):
    try:
        image = Image.open(path).convert("RGB")
        print("Image loaded successfully.")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def encrypt_image(image, key):
    pixels = list(image.getdata())
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    
    encrypted_pixels = [None] * len(pixels)
    for i, shuffled_index in enumerate(indices):
        encrypted_pixels[shuffled_index] = pixels[i]
    
    encrypted = Image.new("RGB", image.size)
    encrypted.putdata(encrypted_pixels)
    return encrypted

def decrypt_image(image, key):
    pixels = list(image.getdata())
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    
    decrypted_pixels = [None] * len(pixels)
    for i, shuffled_index in enumerate(indices):
        decrypted_pixels[i] = pixels[shuffled_index]
    
    decrypted = Image.new("RGB", image.size)
    decrypted.putdata(decrypted_pixels)
    return decrypted

def save_image(image, path):
    image.save(path)
    print(f"Image saved as {path}")

if __name__ == "__main__":
    mode = input("Enter 'E' to encrypt or 'D' to decrypt: ").lower()
    filename = input("Enter the image filename (with extension): ")
    key = int(input("Enter a numeric key (e.g. 1234): "))

    img = load_image(filename)
    if not img:
        exit()

    if mode == 'e':
        result_img = encrypt_image(img, key)
        save_image(result_img, "encrypted_" + filename)
    elif mode == 'd':
        result_img = decrypt_image(img, key)
        save_image(result_img, "decrypted_" + filename)
    else:
        print("Invalid mode selected. Please enter 'e' or 'd'.")
