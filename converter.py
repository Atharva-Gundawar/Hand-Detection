import tflite2onnx

tflite_path = 'palm_detection.tflite'
onnx_path = '/'
print("----started----")
tflite2onnx.convert(tflite_path, onnx_path)
print("----ended----")
