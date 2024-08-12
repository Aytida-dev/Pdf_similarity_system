import cv2
from skimage.metrics import structural_similarity as ssim

def calculateImgSimilarity(images1 , images2):
    # if len(images1) != len(images2):
    #     return 0.0
    
    total_similarity = 0.0
    count = 0

    if not len(images1) and not len(images2):
        return 0.5
    
    for img1, img2 in zip(images1, images2):
        if img1 is None or img2 is None:
            continue

        img1, img2 = resize_images(img1, img2)
        
        similarity = compute_image_similarity(img1, img2)
        total_similarity += similarity
        count += 1
    
    average_similarity = total_similarity / count if count > 0 else 0.0
    return average_similarity

def resize_images(img1, img2):
    height = min(img1.shape[0], img2.shape[0])
    width = min(img1.shape[1], img2.shape[1])
    
    img1 = cv2.resize(img1, (width, height))
    img2 = cv2.resize(img2, (width, height))
    
    return img1, img2

def compute_image_similarity(img1, img2):
    sim, _ = ssim(img1, img2, full=True)
    return sim