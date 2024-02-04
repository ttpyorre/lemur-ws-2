import torch
from torchvision import transforms
import cv2 as cv
from PIL import Image
import sys

def predict_from_im(model, transform, image):
    # Convert OpenCV image to PIL Image
    color_converted_im = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    pil_img = Image.fromarray(color_converted_im)

    # Apply transforms to work with model
    img = transform['predict'](pil_img)
    img = img.unsqueeze(0)
    img = img.to(device)

    with torch.no_grad():
        outputs = model(img)
        _, preds = torch.max(outputs, 1)
        print(f"Prediction: {preds}")
        
if __name__ == '__main__':
    # Parse argument for model name
    if len(sys.argv) != 2:
        raise RuntimeError("Wrong number of arguments. Run the script as follows: python3 live-testing.py [model file name]")
    
    model_name = sys.argv[1]
    
    # Set up GPU
    device = torch.device("cpu")
    torch.backends.quantized.engine = 'qnnpack'

    # Load model that we trained
    model = torch.jit.load(f"~/{model_name}", map_location=torch.device('cpu')).to(device)
    model.eval()

    # Use the same transforms as validation
    data_transforms = {
        'predict': transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    # Set up the camera
    vc = cv.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        
        predict_from_im(model, data_transforms, frame)

        if cv.waitKey(1) == 27: # exit on ESC
            break

    vc.release()
