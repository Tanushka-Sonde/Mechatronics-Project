# Self-Cleaning Solar Panel Robot

## Project Overview
In this project, we have developed a rover designed for cleaning solar panels to minimize human intervention. The rover incorporates advanced mechanisms and components to ensure efficient cleaning, reducing maintenance costs and improving the overall efficiency of solar panels.

# Features
- **Custom CAD Design:**  
  All structural components of the rover are designed in CAD, ensuring precision and modularity. These files are included in the repository for easy replication and customization.
  
- **Autonomous Movement:**  
  Equipped with a Raspberry Pi and servo motors, the rover can be controlled remotely.With its strong computing power when came across a solar panel can actually predicts whether the panel 
  which came across it is clean or dirty and cleans if its dirty.
  
- **Remote Control Interface:**  
  Operated via a Flask web server, allowing users to monitor and control the rover from any device with a web browser.

- **Compact and Lightweight:**  
  The rover’s design ensures portability and minimal impact on the solar panel layout. After Assembly the rover will weigh 10kg at max.

# Repository Structure

1. **STL Files**  
   All 3D-printable components required to build our rover are provided in the `CAD` folder. Components include:  
   - Full base  
   - Bracket  
   - U frame  
   - Final  

2. **Source Code**  
   - `app.py`: The primary code for controlling servo motors which are connected to wheels. 
   - `trained.h`: This is the vgg18 model pretrained on imagenet and add a dense layer with softmax at the end for binary classification for clean and dirty. The dataset of 2390 images was used to train the model and 738 images we used to test our data to get 80% accuracy on the given dataset.

3. **Prototype Reference Images**  
   After almost 8 iterations we finalised the rover which is attached in image below.
   - Final model image: `final.jpeg`
  
# Hardware Requirements

## Electronics
- **Controller:** Raspberry Pi  
- **Servo Motors:**  
  - Four for rotating wheels
  - Four for controlling directoin
- **DC Motor:**  
  - One for controlling the rotation of brush
- **Camera:** RPi Camera Module for obstacle detection,  (optional)
- **PCA 9685:** Connecting rpi powered by a battery can control 16 motors at a time , makes it necessary for simultaneous tyre rotation.
- **L298N** This a driver used for controlling DC motors. Can control 2 DC motors at once.

## Circuit Diagram  
- ![RPi Circuit Diagram](circuit_diagram/circuit.png)  

## 3D-Printed Parts  
- STL files are included for all major structural components in CAD foler.  

---

# Software Requirements

- **Python Programming Language** As python has pre-installed libraries for motor drivers we are using and machine learning models are easier to use in python.  

---






## References
1. [Source for installed solar energy capacity](https://www.sciencedirect.com/science/article/pii/S2352484723014579)
2. [Source for solar energy in desert areas](https://www.mdpi.com/1996-1073/16/19/6794)

## Figures
![Dust Efficiency Relationship](path/to/your/graph_image.png)
