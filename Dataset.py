from roboflow import Roboflow
rf = Roboflow(api_key="Nga0Js5z4zqDaRkWt4gU")
project = rf.workspace("roboflow-universe-projects").project("license-plate-recognition-rxg4e")
version = project.version(4)
dataset = version.download("yolov8")
                