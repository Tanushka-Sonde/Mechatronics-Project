# Self-Cleaning Solar Panel Robot

## Project Overview
In this project, we have developed a rover designed for cleaning solar panels to minimize human intervention. The rover incorporates advanced mechanisms and components to ensure efficient cleaning, reducing maintenance costs and improving the overall efficiency of solar panels.

## Problem Statement
Solar panels convert sunlight into electricity using photovoltaic cells and are a key renewable energy source. However, dust accumulation on solar panels reduces their efficiency by up to 30%.  Figure below demonstrates the relation between efficiency and the density of dust on the solar panel.

![Alt text](https://github.com/Tanushka-Sonde/Mechatronics-Project/blob/main/Screenshot%202024-08-23%20190057.png?raw=true)

In large solar fields spanning 10 to 200 acres, manual cleaning becomes impractical due to the size, cost, and time required. Therefore, an automated, reliable, and cost-effective solution is needed to clean the panels at regular intervals, with high precision and minimal energy consumption.

## Solution

To address this issue, we have developed a solar cleaning robot inspired by the SolarCleano B1 model. This robot will move across solar panels in a field and clean them using a combination of sensors and automated mechanisms. The rough sketches of the solution are provided below, illustrating the robot's design and components.

<h2>Rough Sketches</h2>

<p>
  <img src="https://github.com/Tanushka-Sonde/Mechatronics-Project/blob/main/Rough%20Sketches/rough_sketch_1.jpg?raw=true" alt="Rough Sketch 1" width="45%" style="display:inline; margin:2%;" />
  <img src="https://github.com/Tanushka-Sonde/Mechatronics-Project/blob/main/Rough%20Sketches/rough_sketch_2.jpg?raw=true" alt="Rough Sketch 2" width="45%" style="display:inline; margin:2%;" />
</p>

<p>
  <img src="https://github.com/Tanushka-Sonde/Mechatronics-Project/blob/main/Rough%20Sketches/rough_sketch_3.jpg?raw=true" alt="Rough Sketch 3" width="45%" style="display:inline; margin:2%;" />
  <img src="https://github.com/Tanushka-Sonde/Mechatronics-Project/blob/main/Rough%20Sketches/rough_sketch_4.jpg?raw=true" alt="Rough Sketch 4" width="45%" style="display:inline; margin:2%;" />
</p>

## Mechanical Architecture:

### Movement Mechanism:
- **Wheels**: The robot will be equipped with four wheels, two on each side, to allow for smooth and controlled movement across the surface of the solar panels. These wheels will be powered by DC motors to propel the robot forward and backward.

### Self-Adjusting Cleaning Mechanism:
- **Cleaning Brush/Sponge**: The robot features a cleaning brush or sponge mounted on a rotating rod, driven by a motor.
- **Piston System**: A piston is attached to both ends of the brush or sponge, allowing it to self-adjust its angle relative to the solar panel. This ensures that the cleaning system is always aligned properly with the surface of the panel for optimal cleaning.

### Cleaning Mechanism:
- **Rotating Brush**: The cleaning brush is housed inside the robot and comes in contact with the solar panel when the system is lowered. The motor rotates the brush to clean off dust and debris.

### Edge Detection:
- **Ultrasonic Sensors**: Ultrasonic sensors are mounted on the front and sides of the robot to detect the edges of the solar panel. These sensors detect the edges of the solar panels and direct the upward and downward movement of the cleaning system, ensuring proper alignment and also stopping the movement when it reaches the boundary of the panel.

### Automation and Efficiency:
- **Control System**: An Arduino microcontroller will manage the motor movements, piston control, and sensor inputs. This ensures that the robot can autonomously navigate the solar panel, adjust the cleaning system, and perform the cleaning task without manual intervention.

## References
1. [Source for installed solar energy capacity](https://www.sciencedirect.com/science/article/pii/S2352484723014579)
2. [Source for solar energy in desert areas](https://www.mdpi.com/1996-1073/16/19/6794)

## Figures
![Dust Efficiency Relationship](path/to/your/graph_image.png)
