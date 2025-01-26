from ultralytics import YOLO
import cv2
import logging
import sys
import time

logging.getLogger('ultralytics').setLevel(logging.WARNING)

blackjack_values = {
    "2c": 2, "2d": 2, "2h": 2, "2s": 2,
    "3c": 3, "3d": 3, "3h": 3, "3s": 3,
    "4c": 4, "4d": 4, "4h": 4, "4s": 4,
    "5c": 5, "5d": 5, "5h": 5, "5s": 5,
    "6c": 6, "6d": 6, "6h": 6, "6s": 6,
    "7c": 7, "7d": 7, "7h": 7, "7s": 7,
    "8c": 8, "8d": 8, "8h": 8, "8s": 8,
    "9c": 9, "9d": 9, "9h": 9, "9s": 9,
    "10c": 10, "10d": 10, "10h": 10, "10s": 10,
    "Jc": 10, "Jd": 10, "Jh": 10, "Js": 10,
    "Qc": 10, "Qd": 10, "Qh": 10, "Qs": 10,
    "Kc": 10, "Kd": 10, "Kh": 10, "Ks": 10,
    "Ac": 1, "Ad": 1, "Ah": 1, "As": 1
}

def initialize_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    return cap

def check_camera_for_card(cap, model_path='best.pt'):
    model = YOLO(model_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        sys.stdout.write("\rDetecting...")
        sys.stdout.flush()

        results = model(frame)
        annotated_image = results[0].plot()

        detected_card_info = None
        for i, det in enumerate(results[0].boxes):
            class_id = int(det.cls)
            confidence = det.conf.item()
            label = model.names[class_id]

            if confidence > 0.25:
                blackjack_value = blackjack_values.get(label, None)
                detected_card_info = {
                    "label": label,
                    "confidence": confidence,
                    "bounding_box": det.xywh.tolist(),
                    "blackjack_value": blackjack_value
                }
                cv2.imshow("Detection Results", annotated_image)
                return detected_card_info

        cv2.imshow("Detection Results", annotated_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return None

def detect_card():
    cap = initialize_camera()
    if not cap:
        return None

    detected_card = None
    while True:
        detected_card = check_camera_for_card(cap)
        if detected_card:
            print("\nCard Detected:")
            print(f"  Label: {detected_card['label']}")
            print(f"  Confidence: {detected_card['confidence']:.4f}")
            print(f"  Blackjack Value: {detected_card['blackjack_value']}")
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected_card["blackjack_value"]

# Start detection
card = detect_card()
print(f"Detected Card's Blackjack Value: {card}")

card = detect_card()
print(f"Detected Card's Blackjack Value: {card}")


card = detect_card()
print(f"Detected Card's Blackjack Value: {card}")


card = detect_card()
print(f"Detected Card's Blackjack Value: {card}")
