import numpy as np
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here

    stride = image_size / feature_size
    anchors = []
    
    for i in range(feature_size):
        cy = (i + 0.5) * stride
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            for s in scales:
                for r in aspect_ratios:
                    sqrt_r = np.sqrt(r)
                    w = s * sqrt_r
                    h = s / sqrt_r
                    x_min = cx - w / 2
                    y_min = cy - h / 2
                    x_max = cx + w / 2
                    y_max = cy + h / 2

                    anchors.append([x_min, y_min, x_max, y_max])
    return anchors