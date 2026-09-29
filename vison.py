from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the AI model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def analyze_image(image):

    # Open image
    image = Image.open(image).convert("RGB")

    # Convert image into model input
    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    # Generate description
    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

    # Convert model output to text
    description = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return description
